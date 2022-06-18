Title: Linux Terminal Speed Benchmarks
Date: 2008-10-27 02:54
Category: Linux

In system administration, you spend a lot of time typing into and reading back information from a terminal. Although all terminals pretty much do the same thing, they can differ somewhat in their UI features or which desktop they were designed to be integrated into.

A few years back I was doing a lot of compiling (Gentoo, FreeBSD) and I felt that a good deal of that time was spent just waiting for the terminal to print the enormous amount of compiler cruft to the screen. So I did some quick benchmarks. I don't remember the exact results of those benchmarks nor if I actually made a decision based on them but I clearly remember that results were interesting.

The topic of terminal speed came up at work today so I set out to replicate the experiment. Creating a benchmark like this is harder than it sounds because every time a single a character is printed in a graphical terminal, code is being run in the Linux kernel, numerous places in X, the video card driver, the command shell (bash), and the application running the benchmark itself and even the raw performance of the video card itself can come into play. To design the perfect graphical terminal benchmark, you'd need deep knowledge of how all of those work and carefully craft the benchmark so as to maximize the "stress" on the graphical terminal code while minimizing "stress" on the other components of the system.

However, I'm far too lazy for all that.

So I just catted a [Linux kernel changelog](http://www.kernel.org/pub/linux/kernel/v2.6/ChangeLog-2.6.23) to the screen. Each benchmark was run four times times sequentially and the time averaged among the last three trials. (The first is a dry run to ensure that the file is cached in memory.)

    Terminal        time cat ChangeLog-2.6.23
    -----------------------------------------
    xfce4-terminal  11.109
    gnome-terminal  11.022
    terminator      10.878
    xterm           7.320
    konsole         3.191
    rxvt            2.983


I was rather expecting rxvt to win since it's widely regarded as the minimalist terminal, but Konsole was a surprise. It beats even xterm by a large margin. Like KDE, Konsole is almost certainly written in C++, widely regarded as slower than C which is what makes these results pretty interesting. It's also noteworthy that the xfce4 terminal is right on par with the Gnome terminal when XFCE is supposed to be more lightweight than Gnome. (And probably is, overall.) Based on these figures, one could speculate that terminator, xfce4-terminal, and gnome-terminal are all based on similar code or libraries.

And finally, just in case you skipped the part above where I said how poorly this "benchmark" was really constructed, I want to emphasize it again: This benchmark is completely unscientific. This is how these terminals did on my computer. You may get a different (even perhaps contradictory) set of results if you run them on your computer. Nevertheless, I'm fairly confident that the results here are representative of what most people will see.
