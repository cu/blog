Title: OpenSSH: The Poor Man's SOCKS Proxy
Date: 2009-01-21 01:17
Category: Linux

Just when I think I know everything I need to know about [OpenSSH](http://openssh.org/), I end up learning something new and tremendously useful. Today, that would be the -D argument.

Many times I have been stuck on an "untrusted" Internet connection and need to log in (insecurely) to a certain site. My university, for example, uses a system that has no way of logging in via HTTPS, nor does it secure the traffic to and from the browser. I have moderate faith that the folks at my ISP aren't snooping my traffic (since I know the company pretty well and used to work with them), so I don't have a huge problem logging into their site at home. I also have a colocated server at the web hosting company I work for, so I know the layout of their network even better and trust them not to snoop or interfere with my traffic. But when I'm on the road connected to some dodgy insecure hotel wifi, I acquire no small amount of anxiety over the fact that anyone with a packet sniffer can get access to all of my personal and academic details.

For the past few years, I've had this plan to get [OpenVPN](http://openvpn.net/) set up for my network and laptop so that I can always have a secure connection to my home and colocated server. And for the past few years, I've kept putting it off. While OpenVPN is easier to use than many other VPN solutions I could name, it's still at least a good hour of my time getting all the settings right and testing it out.

I was already aware of OpenSSH's -L option which simply forwards a local port through an SSH tunnel to a port on the remote machine. Very handy when you want to connect surely to a site hosted on that server and happen to have a shell account on it. But to do much more than that ranges from the complex to impossible. This is where -D comes in.

The -D arg tells OpenSSH to be a [SOCKS](http://en.wikipedia.org/wiki/SOCKS) proxy. So you simply log in to the endpoint via SSH with the -D arg like:

    ssh -D 1234 user@host.example.com

And then tell your web browser to use a SOCKS v5 proxy on localhost at the specified port and bingo, you have a secure connection to your endpoint. In fact, any application with SOCKS support can have its traffic routed through the SSH tunnel via SOCKS. Firefox supports SOCKS just fine, Opera doesn't. Konqueror is supposed to, but judging from the Google responses I got, support might be a little flaky.

The final test was whether I'd be able to use this newfangled (to me) proxy method on my Nokia N800, a device that I browse and email with quite often whilst traveling. Obviously OpenSSH has to be installed as it doesn't come with the firmware. And the N800's web browser, MicroB, uses the Gecko engine. The UI has no widgets for entering a SOCKS proxy, but you can set the preferences manually with about:config:

    network.proxy.socks localhost
    network.proxy.socks_port 1234
    network.proxy.type 1

The result? Portable proxy surfing!
