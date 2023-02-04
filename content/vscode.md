Title: Linux Neckbeard Shocked, A Newfangled Code Editor that Doesn't Suck
Date: 2017-10-29
Tags: Linux

<figure>
  <a href="{static}/images/vscode/vscode-01.png">
    <img src="{static}/images/vscode/vscode-01-640.png">
  </a>
</figure>

It was a dark and stormy night. My eyes were glued to the screen as I watched
the [Ansible](https://www.ansible.com/) playbook make its way through the
myriad configuration changes across dozens of production hosts. Of course all
of this had been tested in staging but if you work in technology, you have
more than a passing acquaintance with Old Man Murphy and his insipid law. This
is why my knuckles had turned white, poised over the `Ctrl` and `C` keys
waiting to abort the play in a hurry if I really had to... and if there was
enough time.

And then, inevitably, the moment I feared most had arrived. There was red.
Lots and lots of red splattered across the display, illuminated by the
display's backlight like some grotesque horror show. The scrolling came to a
dramatic halt while my breathing did the same. I scanned the errors, realized
what a fool I had been all this time (for at least the 12th time that day),
corrected a typo, and ran the play again. Successfully, no thanks to that
Murphy bastard.

The problem was caused by the fact that most changes to our Ansible playbooks
tend to span multiple files because we follow the recommended
[role-based directory structure](http://docs.ansible.com/ansible/latest/playbooks_reuse_roles.html).
Which means having multiple files open simultaneously and switching between
them as changes are made. This, as demonstrated by the not entirely fictional
account above, makes the whole process prone to error. It's growing
increasingly rare these days that I don't work on a project involving
multiple files and clearly my workflow is failing me.

I wouldn't call myself a [vim](https://vim.sourceforge.io/) fanboy. It's just
that vim is what I use. It's on virtually every host I'm likely to touch and
it speeds up the process of editing code and config files so tremendously
that I would be lost without it. The main problem with vim is that everything
beyond basic text editing is pretty clumsy. Everything else that's handy to
have in a ~~text~~ code editor has a learning curve, or is clumsy or annoying
to use, or both. That includes many of the more full-feature extensions, and
the graphical variants of vim.

For projects involving multiple files, lately I've been muddling through with
some combination of terminal tabs, [GNU
Screen](https://en.wikipedia.org/wiki/GNU_Screen), and vim's "tabs." This
works a little better than one would expect but it's still easy to get
temorarily lost when my brain is busy chugging away at a more important
problem.

And then it occurs to me that I've been trying to cobble together my own IDE.
Previous to this revelation I have never used--or thought I needed--an IDE. I
know that there are oodles of IDEs on Linux but my brief exposure to them in
the past informed me that they generally take a long time just to load, take
even longer to set up properly, and just come with way, _way_ more stuff than
I'll ever use. Oh, and I can't stand clutter. All I really want out of an IDE
is this:

* Integrated vim (because I can't be productive in anything else),
* the ability to have multiple tabs open,
* and a bare-bones file manager for finding and selecting files to edit.

Everything else lies somewhere on the contiuum between fluff and
brain-damaged anti-features. Gvim doesn't quite fit the bill due to lack of a
simple file manager that can stay put and its tabs that aren't really tabs.
Plus if you have to exit vim (or shut down your computer), the whole
arrangement is lost. Most other IDEs and editors get shot down either by not
supporting vim-style editing or not being open source.

Now, I wouldn't call myself a luddite but a lot of newfangled stuff doesn't
impress me. In many cases, a surprising amount of stuff that hits the front
pages of Hacker News and subreddits is just some old idea repackaged with
gushing praise for itself and support for emoji. So when
[Atom](https://atom.io/) made a big splash my first thought was, "great,
they're reinventing the text editor but this time in Javascript." I remember
running it once just to see what all the hype was about but recall it being
slow and unimpressive.

Well fast-forward a few years and Javascript is practically a first-class
citizen on the desktop today. It has a mature community, fast interpreters,
and lots of libraries. Some of my co-workers are using these
newfangled Javascript-based editors so I thought I would give them a whirl.
Atom started the movement but saw such success that it was quickly followed
by several work-alikes, also written in Javascript. Probably the most
well-known contenders would be [Brackets](http://brackets.io/) and [Visual
Studio Code](https://code.visualstudio.com/).

It started out purely as idle curiosity, I swear. For one, I was amazed that
Microsoft had an open-source code editor, hosted on GitHub no less, rather
than just trying to bundle it with with their other dev tools. When I saw that
they offered Linux packages prominently on their Download screen, I was
positively intrigued. I just _had_ to install it into a VM and give it a spin,
if for no other reason than to grin at the ensuing train wreck and shake my
head while making clucking sounds.

This is (approximately) what greeted me:

<figure>
  <a href="{static}/images/vscode/vscode-02.png">
    <img src="{static}/images/vscode/vscode-02-640.png">
  </a>
</figure>

The first thing that I wondered was whether this thing can do vim well enough
to hold at bay my chair-throwing tendencies when a tool doesn't work the way I
want. I installed the
[Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)
extension and gave it a test run. To my surprise, everything that I used on a
routine basis worked fine. It looked like this was off to a promising start.

When I first started using VSC I didn't really know what I was doing so I
opened my home directory as a folder. This turned out to be a mistake. For one,
this causes VSC to spawn a process that crawls the whole folder in order to
index the text. My home directory is relatively huge due to the nature of my
work and this positively hammered the disk as well as ate up a whole CPU core.
This actually caused me to write-off VSC as an ill-performing hunk of garbage
for longer than I care to admit. Ever since I figured out that opening a
folder dedicated to a single project is the right way to do it, things have
been much smoother.

It turns out that VSC is actually
[rather well documented](https://code.visualstudio.com/docs), so there's 
no point in me rehashing all of its features and whatnot here. So I'll just
mention a few of the things that tick my boxes:

**Integrated vim**. Basically, all of the important things I routinely do in
vim work in VSC.

**Integrated file manager**. It works pretty much exactly as I would expect
with no surprises. To spruce it up just a bit, I also installed the
[vscode-icons](https://marketplace.visualstudio.com/items?itemName=robertohuertasm.vscode-icons)
extension.

**Tabs**. Tabs works as you'd expect. When you have the vim extension installed,
you can even switch tabs with `gt`, although that stops working when you land
on a non-vim tab.

**Performance and stability**. It opens instantly and is always quick to
respond when typing. I haven't had it crash on me yet, that I can recall.
Good enough for me.

**Integrated terminal**. I don't have a problem using an external terminal
but the built-in one is nice to have.

**Ubuntu/Linux friendly**. The VSC package can be installed on Ubuntu where it
will be automatically updated alongside the usual `apt update && apt
dist-upgrade` routine.

**A vibrant extension community**. It's surprising how many extensions there
are. I personally only use a handful of them.

**Saves your work**. If you close VSC and come back to it, it pops right back
up where you were, with all your windows, tabs, and changes intact. Cool.

I've been using VSC for a while now and it has really grown on me.
I really like how it gets out of the way and lets me get my work done. However,
there are just a few things that worrry me or that I think could be improved:

**Minimap enabled by default**. The minimap is this icon-like view of the
whole file in one vertical bar. It's too small to read any of the text but it
shows sort of a vidual outline of the file. This is pretty worthless to me
since it takes up quite a lot of real estate relative to the value it
provides. Also, I believe that if you're working on a file that's becoming
too big to easily navigate, that's a good sign that the file needs to be
broken up anyway.

**Non-unix newline handling**. I filed
[a bug](https://github.com/Microsoft/vscode/issues/35181) about this but so
far, the devs don't seem to think its much of a problem.
Basically, this is a holdover from the editos's Windows roots. On Unix, all
lines in a file end in a newline, including the last line. Vim and all other
Unixy text editors automatically put a newline on the end of a file but don't
show it to you. There is a setting to work around this (see the bug), however
it still shows an empty line at the bottom of the editor and that annoys me.

**Integrated terminal as a separate pane**. The integrated terminal can only
live at the bottom of the window. You can't open one as a tab next to your
other editor tabs, which I would prefer. And while can you have multiple
terminals going at the same time, you have to switch between them via a
drop-down. Not tabs, unfortunately.

**Feature creep**. VSC already does an amazing amount of things, but (and this
is crucial) they mostly stay out of your way when you don't need or want
them. This is in stark contrast to most IDEs that try to shove all the
features into your face to show you how awesome they are. I worry that if the
VSC devs keep trying to add more and more features that the code base
will become bloated, slow, and hard to maintain if they don't draw a line in
the sand somewhere.

**Nagging**. VSC nags you when you're not using the latest version. This drives
me a little crazy. Not so crazy that I've looked up the setting to disable it,
but still.

<figure>
  <a href="{static}/images/vscode/vscode-03.png">
    <img src="{static}/images/vscode/vscode-03-640.png">
  </a>
</figure>

I have been using Linux both personally and professionally for basically all
of my adult life and have actively avoided Windows and other Microsoft
products because they represented everything that I saw as wrong with
proprietary, commercial software. But I guess we're seeing a kinder, gentler
Microsoft or something these days. VSCode is excellent and the fact that I'm
voluntarily running an open-source Microsoft product on my Linux machine for
day-to-day work is still pretty weird whenever I think about it.
