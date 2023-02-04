Title: Rabbit Holes: The Secret to Technical Expertise
Date: 2019-08-24
Tags: Linux

<figure>
  <img src="{static}/images/rabbit-holes/image1.png">
  <figcaption>
    (Alternate Title: How to Shut Up the Ubuntu MOTD, the Long Way)
  </figcaption>
</figure>

Sometimes, the simplest questions take you on exciting journies. This was, in fact, the most powerful and motivating force that got me into doing computery things from a very young age. I would ask a question, how do I X? And after some poking around I discover that I can't do X without learning about Y and Some Authoritative Resource says you _definitely_ can't do Y without also knowing the arcane black magic of Z. And so on and so forth until I get myself so buried in tangents that at a certain point, I have no choice but to stop and come up for air. Or a potty break and snack.

In the glamorous tech sector, we call these things rabbit holes. Unless you got into tech solely for the money (you monster), it's stuff like this that we nerds live for. It's how we got our start and crucially, it's how we continue to learn and hone our skillset.

But what, you ask, does a rabbit hole look like? And anyway, don't rabbits live in dens or burrows? First of all, nobody asked you to critique the metaphor. Second, I'll show you. This isn't the deepest or most complex rabbit hole that I've stumbled down but it is recent and that counts for something when I'm itching to write something. Please feel free to follow along on your own instance of Ubuntu 18.04 if you have one handy. When you log into such a host, you are greeted with 27 lines of this here nonsense:

```
[jayne:~]$ ssh ubuntu@127.0.0.1
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-1044-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat Aug 17 01:05:15 UTC 2019

  System load:  0.0               Processes:           87
  Usage of /:   13.7% of 7.69GB   Users logged in:     0
  Memory usage: 14%               IP address for eth0: 127.0.0.1
  Swap usage:   0%

 * Keen to learn Istio? It's included in the single-package MicroK8s.

     https://snapcraft.io/microk8s

 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

0 packages can be updated.
0 updates are security updates.


Last login: Fri Aug 16 23:40:01 2019 from 127.0.0.1
```

The first time you log into an Ubuntu host, all of this is very flashy and impressive. You think, wow, this looks like Serious Business. But right around the 427th time, it's just noise. Then at some inconvenient time in the future--when something on that host breaks badly and you have to endure that crap before you get to your shell prompt--you really hope that one day you can meet the guy who programmed it on the outside chance you might be able to covertly spike his coffee with a large dose of laxative.

In these 27 lines (which is three longer than the default terminal height, mind you), we have:

* a greeting, showing us the OS, version, kernel version, and CPU architecture
* links to documentation
* some arbitrary technical information about the host
* an ad for some Canonical product
* another ad for some Canonical product
* package update information
* when this account previously logged into this host

Somebody somewhere obviously thought that every piece here would be vital information to somebody else. But let's see about how we can pare this down to something managable. Or in the worst case, wipe it out altogether.

I happen to know, from my decades of previous BSD/Linux rabbit holes, that messages which are printed after you log in usually come from the file `/etc/motd`. "motd" by the way, stands for Message of the Day. In the Olden Days it was a way for administrators to tell users about important things about the system or communicate news, like, "Hey everyone, the print server is down again. We think Phil broke it." On Debian and Ubuntu, most every configuration file has a man page so let's check out that lead with `man motd`:

```
DESCRIPTION
       The contents of /etc/motd are displayed by pam_motd(8) after a success‐
       ful login but just before it executes the login shell.

       The abbreviation "motd" stands for "message of the day", and this  file
       has  been  traditionally  used  for exactly that (it requires much less
       disk space than mail to all users).

       On Debian GNU/Linux, dynamic content configured at /etc/pam.d/login  is
       also displayed by pam_exec.

FILES
       /etc/motd
       /etc/pam.d/login
```

Great, so if the man page is right, all that crap should be festering in `/etc/motd`, let's take a look:

```
ubuntu@ip-127-0-0-1:~$ cat /etc/motd
cat: /etc/motd: No such file or directory
```

Well, bugger. That certainly didn't pan out. Moreover, we've learned an important lesson: man pages can lie. Or at the very least, often don't tell the whole truth. Here is where we can try an experiment. What happens if we write something to `/etc/motd`? Will that replace the default Ubuntu MOTD? Could we be so lucky? Let's make ourselves root and see:

```
echo "Goodbye, Cruel World" > /etc/motd
```

And upon logging in again:

```
[jayne:~]$ ssh ubuntu@127.0.0.1
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-1044-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat Aug 17 01:09:15 UTC 2019

  System load:  0.0               Processes:           87
  Usage of /:   13.7% of 7.69GB   Users logged in:     0
  Memory usage: 14%               IP address for eth0: 127.0.0.1
  Swap usage:   0%

 * Keen to learn Istio? It's included in the single-package MicroK8s.

     https://snapcraft.io/microk8s

 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

0 packages can be updated.
0 updates are security updates.


Goodbye, Cruel World
Last login: Fri Aug 16 23:45:01 2019 from 127.0.0.1
```

Stellar. Now there are 28 lines of crap! But at least we know `/etc/motd` does _something_. _Sigh_. And we also know that `/etc/` is where a bunch of system configuration lives, so maybe there's something else in there that has to do with the MOTD. Let's use `grep`:

<figure>
  <img src="{static}/images/rabbit-holes/image2.png">
</figure>

It turns out there's quite a lot! There are some promising leads here, but skimming over the list of possibilities, the last few lines catch my attention the most since those files are in a directory called `/etc/update-motd.d`. These are the files in it:

```
root@ip-127-0-0-1:/etc/update-motd.d# ls -1 /etc/update-motd.d/
00-header
10-help-text
50-landscape-sysinfo
50-motd-news
80-esm
80-livepatch
90-updates-available
91-release-upgrade
95-hwe-eol
97-overlayroot
98-fsck-at-reboot
98-reboot-required
```

That's interesting: ignore a few of these and these files start to look a lot like our MOTD outline from earlier. Let's see what's in the first one. Omitting the comments and a bit of variable-setting code for brevity, we get:

```
printf "Welcome to %s (%s %s %s)\n" "$DISTRIB_DESCRIPTION" "$(uname -o)" "$(uname -r)" "$(uname -m)"
```

And the next one, `10-help-text` contains mostly this:

```
printf " * Documentation:  https://help.ubuntu.com\n"
printf " * Management:     https://landscape.canonical.com\n"
printf " * Support:        https://ubuntu.com/advantage\n"
```

It's as close to a smoking gun as we're likely to see: These definitely appear to match the first few lines of the MOTD. Given that the file names contain an integer prefix, we can guess that _probably_ all the scripts in this directory are executed sequentially and their output blurted out to us when we log in.

But by what? A normal, perfectly sane person would stop here and say, "Well now the rest is easy, you just delete or modify those scripts and Roberta's-yer-auntie!" And you would be right. But who said I was a normal, perfectly sane person? Certainly not Roberta. Let's look at disabling the most obnoxious thing in the MOTD, the Ubuntu news, announcements, and astrology section. I recall that this part changes from time to time so it must be phoning home to Canonical. As a refresher, here's what it says today:

```
 * Keen to learn Istio? It's included in the single-package MicroK8s.

     https://snapcraft.io/microk8s
```

Today, I'm mostly keen to learn how the f to get rid of this message. By perusing a few of the files, I suspect that `50-motd-news` is likely our guy. Not least of all because there's a URL in it: https://motd.ubuntu.com And if we go to that URL:

```
root@ip-127-0-0-1:~# curl https://motd.ubuntu.com
 * Keen to learn Istio? It's included in the single-package MicroK8s.

     https://snapcraft.io/microk8s
```

So the `/etc/update-motd.d/50-motd-news` script is what's printing ads into our young impressionable eyeballs. And again we dive deeper into the rabbit hole because we want to know _how_. I'll spare you the boring details of the full code listing but basically it's doing this:

* read some environment variables from `/etc/default/motd-news`
* exit immediately if `$ENABLED` is not `1`
* if the `--force` flag was _not_ provided, print whatever is in `/var/cache/motd-news`
* if the `--force` _was_ provided, go out and fetch the MOTD from https://motd.ubuntu.com

This tells us that 1) there is a way to disable this part of the MOTD easily by editing `/etc/default/motd-news` and 2) the output of this script is fetched and then cached somewhere. If we run the script, we get the same output as when we fetched the contents of the URL a moment ago. And if we print the contents of `/var/cache/motd-news`, we get the same thing as well:

```
root@ip-127-0-0-1:~# /etc/update-motd.d/50-motd-news 

 * Keen to learn Istio? It's included in the single-package MicroK8s.

     https://snapcraft.io/microk8s
root@ip-127-0-0-1:~# cat /var/cache/motd-news
 * Keen to learn Istio? It's included in the single-package MicroK8s.

     https://snapcraft.io/microk8s
```

So this pretty much confirms our broad understanding of how this is all working. Pop the cork off the champagne, we figured it out! Woohoo!

But wait... what's that `--force` flag all about? What calls this script with it? (Not the login process, as far as we know.) And how does `/var/cache/motd-news` ever get updated with new content? And we still don't know what part of the login process is running the scripts in `/etc/update-motd.d` anyway? These are questions that we could certainly live without knowing but deep down we know that it will be a hollow, meaningless existence unless we find out. It's not champagne time yet, I'm afraid.

Taking another close look at the `/etc/update-motd.d/50-motd-news` file, this comment catches the eye:

```
# If we've made it here, we've been given the --force argument,
# probably from the systemd motd-news.service.  Let's update...
```

"The systemd motd-news.service," you say? As in, something _else_ besides the login process calls this script? Weirder things I have seen. Let's look for that service:

```
root@ip-127-0-0-1:~# systemctl list-unit-files | grep motd
motd-news.service                              static         
motd.service                                   masked         
motd-news.timer                                enabled 
```

What we have here is a `motd-news` service and timer. There's also an `motd.service` but it's masked which means it's quite definitely not doing anything. I'm curious to know what that is for but the other two are what I'm interested in at the moment.

The Old Way of running jobs on a Unix system at specific intervals is through the cron daemon. You specify the interval as a sequence of fields and the job to run, and then `crond` takes care of the rest. It's a simple, elegant system and has been serving us well for decades. Systemd, which has good parts and bad parts and insane parts, has come up with a replacement for cron called timers. Long story short, timers are like cron jobs but with a lot more options for scheduling and management. Their configuration is also quite a bit more complex as a result. Another difference is that timers don't execute commands directly, instead you have to define a systemd _service_ which is then triggered by a timer.

Anyway, on Ubuntu the unit files live in `/lib/systemd/system` so that's where we find the `motd-news.*` units. Let's look at the timer first.

```
[Unit]
Description=Message of the Day

[Timer]
OnCalendar=00,12:00:00
RandomizedDelaySec=12h
Persistent=true
OnStartupSec=1min

[Install]
WantedBy=timers.target
```

The `Description` field confirms that `motd` doesn't actually stand for "Melon of the Deep" and the `OnCalender` and `RandomizedDelaySec` fields are what tells systemd to fire the timer once at some random time once within every 12-hour period. We don't see the service unit listed here because according to [the man page for timers](https://www.freedesktop.org/software/systemd/man/systemd.timer.html), a timer will by default trigger a service file of the same name. So let's crack open `motd-news.service`, then:

```
[Unit]
Description=Message of the Day
After=network-online.target
Documentation=man:update-motd(8)

[Service]
Type=oneshot
ExecStart=/etc/update-motd.d/50-motd-news --force
```

Aha, there's the `--force` flag! We are also helpfully informed that the `/etc/update-motd.d/` directory has it's own man page, something that might have been helpful earlier if I would have had the presence of mind to check for it. _This_ is what we could have used instead of the mostly-useless `motd` man page. An enterprising young hacker could do the world some good by submitting a patch to the Ubuntu `motd` man page containing a pointer to the `update-motd` man page.

At any rate, the man page describes a number of assumptions and best practices around writing and maintaining scripts in `/etc/update-motd.d`. Importantly, it also says, and I quote:

```
Executable  scripts in /etc/update-motd.d/* are executed by pam_motd(8)
as the root user at each login, and this information is concatenated in
/run/motd.dynamic.
```

But if we look at the PAM config files, they both have this same blurb:

```
# Prints the message of the day upon successful login.
# (Replaces the `MOTD_FILE' option in login.defs)
# This includes a dynamically generated part from /run/motd.dynamic
# and a static (admin-editable) part from /etc/motd.
session    optional   pam_motd.so motd=/run/motd.dynamic
session    optional   pam_motd.so noupdate
```

Cross-referencing this with the pam_motd man page, the `motd=/run/motd.dynamic` option simply tells `pam_motd` to print the contents of `/run/motd.dynamic`. And the `noupdate` option tells it _not_ to run the scripts in `/etc/update-motd.d`. So how are the scripts in `/etc/update-motd.d` _actually_ getting run on every login? One of these man pages is lying to us. Again.

As it sometimes the case, we will probably have to resort to looking at souce code to figure this one out. Debuan and Ubuntu make it extremely easy to get the source code for every package on the system. The first step is to enable all the source repositories in the `/etc/apt/sources.list` by uncommenting out the lines beginning with `deb-src` and then running `apt update`. You also need to install the `dpkg-dev` package to work with source packages. So, like, do that.

Next, as a regular user (not root) find out where `pam_motd.so` is, then figure out which package it belongs to, and then fetch the source code for that package, like so:

```
ubuntu@ip-127-0-0-1:~$ find /lib -type f -name pam_motd.so 2>/dev/null
/lib/x86_64-linux-gnu/security/pam_motd.so
ubuntu@ip-127-0-0-1-:~$ dpkg --search /lib/x86_64-linux-gnu/security/pam_motd.so
libpam-modules:amd64: /lib/x86_64-linux-gnu/security/pam_motd.so
ubuntu@ip-127-0-0-1:~$ apt-get source libpam-modules
Reading package lists... Done
Picking 'pam' as source package instead of 'libpam-modules'
NOTICE: 'pam' packaging is maintained in the 'Bzr' version control system at:
https://code.launchpad.net/~ubuntu-core-dev/pam/ubuntu
Please use:
bzr branch https://code.launchpad.net/~ubuntu-core-dev/pam/ubuntu
to retrieve the latest (possibly unreleased) updates to the package.
Need to get 1993 kB of source archives.
Get:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main pam 1.1.8-3.6ubuntu2.18.04.1 (dsc) [2212 B]
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu bionic-updates/main pam 1.1.8-3.6ubuntu2.18.04.1 (tar) [1990 kB]
Fetched 1993 kB in 0s (7884 kB/s)
dpkg-source: info: extracting pam in pam-1.1.8
dpkg-source: info: unpacking pam_1.1.8-3.6ubuntu2.18.04.1.tar.gz
```

What we're left with is a package description file, a source tarball, and a directory.

```
ubuntu@ip-127-0-0-1:~$ ls -l
total 1952
drwxrwxr-x 15 ubuntu ubuntu    4096 Feb 27 14:26 pam-1.1.8
-rw-r--r--  1 ubuntu ubuntu    2212 Feb 28 13:33 pam_1.1.8-3.6ubuntu2.18.04.1.dsc
-rw-r--r--  1 ubuntu ubuntu 1990490 Feb 28 13:33 pam_1.1.8-3.6ubuntu2.18.04.1.tar.gz
```

Delving into the directory, some exploration reveals that the source code for `pam_motd.so` is in `pam-1.1.8/modules/pam_motd/pam_motd.c`. Does that file have anything to do with `/etc/update-motd.d`? Let's grep that sucker and see:

```
ubuntu@ip-127-0-0-1:~/pam-1.1.8/modules/pam_motd$ grep update-motd pam_motd.c
ubuntu@ip-127-0-0-1:~/pam-1.1.8/modules/pam_motd$ 
```

Hmm. Nope. Okay, I know that Debian and Ubuntu source packages contain the software's pristine upstream source and that any changes that the distributions make to the package are shipped in the `debian` directory as patches. Let's check out that angle.

```
ubuntu@ip-127-0-0-1:~/pam-1.1.8/debian/patches-applied$ grep update-motd *
series:update-motd
series:update-motd-manpage-ref
update-motd:Provide a more dynamic MOTD, based on the short-lived update-motd project.
update-motd:+    /* Run the update-motd dynamic motd scripts, outputting to /run/motd.dynamic.
update-motd:+    if (do_update && (stat("/etc/update-motd.d", &st) == 0)
update-motd:+	if (!system("/usr/bin/env -i PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin run-parts --lsbsysinit /etc/update-motd.d > /run/motd.dynamic.new"))
update-motd:+            Don't run the scripts in <filename>/etc/update-motd.d</filename>
update-motd:+    Don't run the scripts in /etc/update-motd.d to refresh the motd file.
update-motd-manpage-ref:+       <refentrytitle>update-motd</refentrytitle><manvolnum>5</manvolnum>
update-motd-manpage-ref:+\fBupdate-motd\fR(5)
```

Bingo! Let's have a look at the `update-motd` patch, that probably has what we want. Sure enough, here's the code that runs the files in `/etc/update-motd.d`:

```
+    /* Run the update-motd dynamic motd scripts, outputting to /run/motd.dynamic.
+       This will be displayed only when calling pam_motd with
+       motd=/run/motd.dynamic; current /etc/pam.d/login and /etc/pam.d/sshd
+       display both this file and /etc/motd. */
+    if (do_update && (stat("/etc/update-motd.d", &st) == 0)
+        && S_ISDIR(st.st_mode))
+    {
+       mode_t old_mask = umask(0022);
+       if (!system("/usr/bin/env -i PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin run-parts --lsbsysinit /etc/update-motd.d > /run/motd.dynamic.new"))
+           rename("/run/motd.dynamic.new", "/run/motd.dynamic");
+       umask(old_mask);
     }
```

In plain english, what this does is essentially this: If `do_update` is true (presumably because the `noupdate` option was not set) and if `/etc/update-motd.d` exists and is a directory, execute the contents of `/etc/update-motd.d` via `run-parts` and drop the output into `/run/motd-dynamic`.

So we find yet again that the man pages weren't lying, but it could have saved us some effort if the `pam_motd` man page stated more explicitly that the scripts in `/etc/update-motd.d` are _always_ run unless the `noupdate` option is specified.

You can always dig deeper and deeper into a rabbit hole like this one until you wind up wandering aimlessly through the field of particle physics but this is about as far as I'm willing to take this one. All of my major questions in the beginning and along the way have been answered well enough. This was a fun diversion, even though the practical upshot is relatively trivial. If you stuck with it through the end, you should now be relatively well-equipped to explore similar rabbit holes yourself. Just remember that at the end, when you finally solve them, try to go easy on the champagne.
