Title: Rebuilding Docker for Custom Networks, a SysAdmin Tale
Date: 2018-05-04
Tags: Linux, Docker, DevOps

At work, we use [Docker](https://www.docker.com/) for developing, testing, and deploying applications. For the most part, it has simplified our lives greatly at the cost of a few annoyances and headaches here and there. I just spent the better part of a week dealing with one of them and since misery loves company, I'm going to share the pain with you. Aren't you excited?

Although we're looking into other options, right now we use [Docker Compose](https://docs.docker.com/compose/) to deploy applications invididually to one of several application hosts. Docker Compose, if you are not already familiar with it, essentially lets you deploy a collection of Docker containers as a single service. So for a blog, to pick a totally random and arbitrary example, you will have a container for the blog engine itself, another for the database it connects to, another one to handle the reverse proxy for TLS, perhaps yet another for ElasticSearch, and so on.

Now, when you deploy a multi-containered application like this with Compose, it creates a network so that all of the containers can talk to one another. This is an isolated network that can reach back out to the rest of the world via NAT. The only way traffic gets into this network from the outside is when you map ports into a container in your `docker-compose.yml` file. If you don't tell Compose which network to use for the set of containers, it will happily create one for you. It does this by pulling networks out of a default pool of `172.[17-31].0.0/16` and `192.168.[0-240].0/20`.

As long as your Docker host never needs to communicate with anything outside of itself on those subnets, you are fine. (Can you see where this is going? I bet you can see where this is going.) At my day job, however, an edict came down from on high that a bunch of our infrastructure had to be moved into the `172.18/12` space. Like me, you might think, "Well this is fine, because those docker networks are all internal to the host." Like me, you'd be wrong. Because when Docker creates these networks, it does so by creating a bridge for each one. Which adds an entry to the kernel's routing table for those networks. Which means if *anything* on the host wants to talk to something in `172.18/12`, it can't because the routing table says those IPs are not reachable via the default gateway:

```
default via 10.1.120.1 dev wlp1s0 proto static metric 600 
10.1.120.0/23 dev wlp1s0 proto kernel scope link src 10.1.121.89 metric 600 
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1 linkdown 
172.18.0.0/16 dev br-415a70ddd828 proto kernel scope link src 172.18.0.1 
```

In the above example, `172.17.0.0/16` is our `docker0` network. We're going to ignore that for now. The relevant network is `172.18.0.0/16`, which was created automatically by Docker Compose in response to deploying a new application.

In a fictional utopia of rainbow waterfalls, free beer and reasonable software engineering practices you would be able to tell Docker, "Hey there, buddy. Any chance you can use a different IP space for those internal networks you like to create?" And Docker would say, "Of course, friend! Just put that awesome stuff in the config file and I'll take care of everything. Also, here's some more beer!"

However, in the universe we presently inhabit, Docker is a bit of a jerk. Those 172.x and 192.168.x pools are literally hard-coded into docker. To be fair, there is [work underway](https://github.com/moby/moby/pull/36396) to be able to specify default address pools. This is good but _as I write this_ it's a little too late to help me and others like me who are facing this IP space conflict now. It has not yet been merged so it's hard to say when it will hit an actual release.

What are our options right now?

## Manually Specify Application Networks

In the `docker-compose.yml` file for each application we can specify the IP space of the network it will use. There are two obvious drawbacks to this, though. The first is that if you maintain the deployments of, say, 50-ish applications, individually mangling the config files for each of these is a huge pain. Moreover, you would have to track these assignments somehow (e.g. in everyone's favorite database, a spreadsheet, perhaps) because they can't overlap on the same host. Frankly, I'd rather stab myself in the ear.

## Hax0r Your Routing Table

If there are only certain subnets within Docker's default address pool that you need to avoid, you can add those to the routing table of the host and that will cause Docker to skip them when automatically creating its networks. This is what I did as a short-term fix. The reason it's a short term fix in my case is because ideally I don't want Docker to be using anything in its currently hard-coded list. The organization I'm working for for uses the entirety of _all three_ of the well-known private IPv4 address spaces on its internal network and these are expected to be routable from everywhere. I mean, I'm no network architect but let's just say that's not what I would have done.

## Wait for Docker to Support Custom Address Pools

This is the option that involves the least amount of work, so if you can get away with waiting for a release that supports custom address pools, then congratulations on being lazy. But seriously, if you're not facing any show-stopping IP conflicts with the default pool then this is the most reasonable option by far. 

## Patch and Rebuild Docker

Since the default address space is hard-coded into docker, a viable option is to patch Docker to use a different space. Here is roughly how. Whenever I start a project like this, I like to make a series of laughable assumptions:

1) You're running Docker on Ubuntu Xenial 16.04. Although this should work fine for any OS that Docker officially supports, this is what I tested it on and it's what I'll show.

2) You're running release 18.03-1-ce of Docker, which is the latest release as of this writing. Again, the same general idea applies to other versions of Docker but the code might be different, or the original problem might be fixed in newer versions, etc.

3) You're running Docker CE, not EE or any other variant. Because I don't know how to build the others.

If you don't have an Ubuntu 16.04 machine handy, blindly follow my expert example and fire one up in a VM. Note that this VM is going to need unhindered access to the Internet since the Docker build process fetches git repositories, docker images, and cute baby goat videos for all I know. You'll want something in the vicinity of 4 CPU cores, 8 GB of RAM, and 20 GB of disk space. Less might work fine. More is better. A speedy Internet connection is highly recommended.

The first thing you need to do is install a few dependencies: git, GNU make, and docker-ce. Yes, you read that right. You need Docker to build Docker. Don't ask why; this is not a rabbit hole we're going to throw ourselves down today. If some version of Docker is installed already and it's not the one we're building, stop any currently running containers and uninstall it. 

We'll start with setting up the Docker apt repository. The details for this are [over here](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository) but here's the simplified version:

```
# download and add the docker apt repository GPG key
wget -O - https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# add the docker apt repo to your system
echo "deb [arch=amd64] http://download.docker.com/linux/ubuntu xenial stable" | sudo tee /etc/apt/sources.list.d/docker.list

# update the package index
sudo apt update
```

Next we install git, make, and Docker:

```
sudo apt -y install git make docker-ce
```

Then check out the `docker-ce` git repo and `cd` into it:

```
git clone https://github.com/docker/docker-ce.git
cd docker-ce
```

Because we want to modify the release that we're using, switch to the tag corresponding to it. Use `docker --version` to see yours. In our case, that's version `18.03.1-ce` (note that the version string does not start with a `v` but the tag does):

```
git checkout v18.03.1-ce
```

Now we can patch the Docker source. If you haven't heard, Docker is written in [Go](https://golang.org/) so knowing it will be helpful, although not strictly necessary such a simple change as this. The file containing the IP address pools is `components/engine/vendor/github.com/docker/libnetwork/ipamutils/utils.go`. Let's edit that and see what we get. If you're just following along for entertainment (you weirdo) you can see the same thing [here](https://github.com/docker/docker-ce/blob/v18.03.1-ce/components/engine/vendor/github.com/docker/libnetwork/ipamutils/utils.go)

```
vim components/engine/vendor/github.com/docker/libnetwork/ipamutils/utils.go
```

Here are the important parts:

```
var (
	// PredefinedBroadNetworks contains a list of 31 IPv4 private networks with host size 16 and 12
	// (172.17-31.x.x/16, 192.168.x.x/20) which do not overlap with the networks in `PredefinedGranularNetworks`
	PredefinedBroadNetworks []*net.IPNet
	// PredefinedGranularNetworks contains a list of 64K IPv4 private networks with host size 8
	// (10.x.x.x/24) which do not overlap with the networks in `PredefinedBroadNetworks`
	PredefinedGranularNetworks []*net.IPNet
	initNetworksOnce           sync.Once

	defaultBroadNetwork = []*NetworkToSplit{{"172.17.0.0/16", 16}, {"172.18.0.0/16", 16}, {"172.19.0.0/16", 16},
		{"172.20.0.0/14", 16}, {"172.24.0.0/14", 16}, {"172.28.0.0/14", 16},
		{"192.168.0.0/16", 20}}
	defaultGranularNetwork = []*NetworkToSplit{{"10.0.0.0/8", 24}}
)
```

`defaultBroadNetwork` is the thing we're interested in. Notice that it's a list of several networks. Each list element contains an IP address range in [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation and the size of the network. For example, if we take `{"172.20.0.0/14", 16}`, then `172.20.0.0/14` is the range and `16` is the size (number of bits) of each network to dole out from the total range given. To further illustrate, `172.20.0.0/14` represents the range of addresses from `172.20.0.0` to `172.23.255.255` and if we specify a network size of `16`, Docker will allocate the following networks from that range:

```
172.20.0.0 - 172.20.255.255
172.21.0.0 - 172.21.255.255
172.22.0.0 - 172.22.255.255
172.23.0.0 - 172.23.255.255
```

In my case, I want to pick a network that has no chance of being routable anywhere [on the organization's internal network](https://en.wikipedia.org/wiki/Private_network#Private_IPv4_address_spaces) or on the Internet. There are two candidates here: the link-local address block `169.254/16` and and [carrier-grade NAT](https://en.wikipedia.org/wiki/Carrier-grade_NAT) block `100.64/10`.

I can already see the pedantic contingent rising up from their Aeron chairs and shaking their pocket protectors in blind fury for making such a bold suggestion but please, everyone, let's just keep our cool for one moment. Technically speaking, this is not an RFC-approved use of either of these spaces. I acknowledge that. But this is America, dammit, and since these spaces by their very definition do not route to the Internet under normal circumstances, they are perfectly cromulent to use in a scenario where they are further restricted to an isolated virtual network on a single host. So really, just relax, it will all be fine.

Of these two options, I think `169.254/16` is the slightly better choice for two reasons: 1) it is instantly recognizable to most other admins as a non-routable network, and 2) there's a tiny but not impossible chance that you're doing Docker somewhere on or near a CGNAT space. I mean, CGNAT sucks but _not_ torpedoing the network probably takes precidence over angst if you like staying employed.

However, for the purposes of illustration, I'm going to use the CGNAT space `100.64/10` because there is a non-zero chance that the `169.254/16` space [already has an entry in your routing table](https://askubuntu.com/questions/893097/how-to-get-rid-of-169-254-0-0-route). Now let's press forward by rejecting Docker's reality and substituting our own:

```
defaultBroadNetwork = []*NetworkToSplit{{"100.64.0.0/16", 24}}
```

This defines the address range `100.64.0.0 - 100.64.255.255` and tells Docker to grab a `/24` out of it every time it needs a network. This gives us 256 networks with 256 addresses in each. We save this change, update the comments if so inclined, and then rebuild Docker. Since we're on Ubuntu, we can tell the build system to build the whole thing and thing spit out a `.deb` package at the end. We have to specify the `DOCKER_BUILD_PKGS` variable because if we leave that out, it will try to build Docker (and packages) for _every_ OS and platform combination it knows about. And that takes longer than you'd like.

```
make DOCKER_BUILD_PKGS=ubuntu-xenial deb
```

Once your computer has done a bunch of computing, it's a simple matter of installing the package you just built. If you have any docker containers running, now would be an awesome time to stop them.

```
# stop docker
sudo service docker stop

# remove old docker
sudo apt -y remove docker-ce
# install the newly-built docker
sudo dpkg -i ./components/packaging/deb/debbuild/ubuntu-xenial/docker-ce_18.03.1~ce-0~ubuntu_amd64.deb

# start docker back up
sudo service docker start
```

One thing to keep in mind is that an `apt dist-upgrade` may very well overwrite your hacked docker package with one from the docker repository. To keep that from happening, you can tell apt to keep its grubby mitts off it:

```
sudo apt-mark hold docker-ce
```

Now then, let's test this puppy out and make sure it actually works. First, we can just create a network and see if it inhabits the right network space:

```
docker network create foobar
```

If it worked, we'll see it when we list the networks:

```
$ docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
adf186946399        bridge              bridge              local
370a94d1a1f1        foobar              bridge              local
be998f0e4c82        host                host                local
ad949b38a540        none                null                local
```

We can verify that it took the right subnet by inspecting the network:

```
$ docker network inspect foobar
...snip...
                    "Subnet": "100.64.0.0/24",
                    "Gateway": "100.64.0.1"
...snip...
```

And just to verify that containers attached to this redefined IP space can actually talk to one another, let's install Docker Compose and set up a test deployment of two containers.

```
# Install Python 3 pip
sudo apt -y install python3-pip

# Install docker-compose
sudo pip3 install docker-compose

# Create directory for test deployment
mkdir ~/docker-net-test
cd ~/docker-net-test
```

Paste the following file as `docker-compose.yml`:

```
version: "2"
services:
  foo:
    image: busybox
    entrypoint: tail -f /dev/null
  bar:
    image: busybox
    entrypoint: tail -f /dev/null
```

Bring up the deployment:

```
$ docker-compose up -d
Creating network "docker-net-test_default" with the default driver
Pulling foo (busybox:)...
latest: Pulling from library/busybox
f70adabe43c0: Pull complete
Digest: sha256:58ac43b2cc92c687a32c8be6278e50a063579655fe3090125dcb2af0ff9e1a64
Status: Downloaded newer image for busybox:latest
Creating docker-net-test_foo_1 ... done
Creating docker-net-test_bar_1 ... done

```

Now for the fun part. Exec into the container for service "foo":

```
docker-compose exec foo sh
```

We can see which IP the container was assigned by running:

```
# ip addr show eth0
16: eth0@if17: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue 
    link/ether 02:42:64:40:01:02 brd ff:ff:ff:ff:ff:ff
    inet 100.64.1.2/24 brd 100.64.1.255 scope global eth0
       valid_lft forever preferred_lft forever
```

We got 100.64.1.2, which is exactly what we expected. Yay. Let's ping the other container and see if the network is actually functional:

```
# ping -c3 bar
PING bar (100.64.1.3): 56 data bytes
64 bytes from 100.64.1.3: seq=0 ttl=64 time=0.056 ms
64 bytes from 100.64.1.3: seq=1 ttl=64 time=0.074 ms
64 bytes from 100.64.1.3: seq=2 ttl=64 time=0.083 ms

--- bar ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.056/0.071/0.083 ms
```

How about that, eh? It actually worked! So there you have it. You've modified, built, installed, and tested Docker using an IP range that (theoretically) does not conflict with most internal networks and definitely should not route to the Internet. If you actually read through all of this, then congratulations because anyone who can stick around all the way through my wild ramblings deserves some kudos.
