Title: My BITX40 Build
Date: 2017-06-09
Tags: Radio

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-01-640.jpg">
</figure>

The BITX40 is a QRP (low-power) transceiver kit for the 40 meter amateur radio
band. Although it is low-power (nominal 7 watts), and restricted to a single
band (7 MHz), the $60 USD price tag makes it very attractive to those like
myself who like to build things and play around with radio on a budget.

Usually when we think of an electronics kit, we imagine a big bag of components
that need to be soldered together. In the case of the BITX40, all of the
components have already been soldered to the PCB. You get the transceiver
board, a digital control board, an LCD module, and all of the supporting
hardware for the radio like a microphone, potentiometer, etc. The only things
the end user needs to add are a speaker and enclosure. (And like any ham
radio, a power supply and antenna.)

I started out trying to homebrew an enclosure out of galvanized sheet metal and
aluminum angle bracket. It did not go well. We will no longer speak of it.


Turning to eBay, I found a variety of surprisingly affordable project boxes.
This one here fits the BITX40 nicely with plenty of room to spare for mods and
whatnot. It's built like a tank and is extremely high quality overall. You
should be able to find it for around $20 shipped, just search for the
dimensions "203x144x68mm".

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-02-640.jpg">
</figure>

As she arrived. I ended up losing one of the standoffs somewhere. Also, it came
with a tiny SMD capacitor in the box that I have not been able to divine the
purpose of. Did not find it in the instructions, nor did any googling turn
anything useful up. If anyone knows what it's for, let me know.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-03-640.jpg">
</figure>

I started with the easy stuff. Power and antenna connectors mounted and vent
holes drilled. In this picture they look very misaligned. in real life, it's
hard to notice.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-04-640.jpg">
</figure>

Drilled more vent holes in the bottom of the case and mounted the stand-offs.
Again, not the best on alignment but these are on the bottom anyway, so whatev.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-05-640.jpg">
</figure>

The BITX40 mainboard mounted up just fine. I wanted to have both the antenna
connector and RF final transistor close to the back of the case. This achieves
that. Some day, it will be fairly easy to add a bigger heat sink to the final
transistor.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-06-640.jpg">
</figure>

Now the hard part: Mocking up placement of front panel parts. In this photo,
I'm just checking that everything fits comfortably on the 2D side of things.
This is the first of three front-panel mock-ups that I did.

Trying to get the front panel layout right accounted for the vast majority of
the time spent on this project. The project box came with two flat end panels.
Messing one up wouldn't have been the end of the world, but it would have
pissed me off greatly. So I tried very hard to get it right and checked
everything multiple times every step of the way.

The volume pot that shipped with the BITX40 felt flimsy so I replaced it with
one of my own. This knob doesn't have a switch built into it, so I had to add
one off to the side. All the Radio Shacks around me are going out of business
so I raided their goody bins one by one. Most of the "extra" parts you see here
are from those sales, including the knobs.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-07-640.jpg">
</figure>

First rough draft of the front panel layout.

For the speaker and microphone, I decided to go with a Baofeng speaker mic. I
mean, for $3.50 shipped, you'd be crazy not to, right? At the bottom is a
pinout of the speaker mic, as deduced by multimeter. If you have a look at the
first pic and then this pinout, you may be able to see where I was going to run
into trouble later on.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-08-640.jpg">
</figure>

A more precise layout of the front controls (reversed).

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-09-640.jpg">
</figure>

The final mockup using sheet metal. I ended up moving the power switch to the
left about a centimeter so I have more room for switches and buttons and stuff
later on.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-10-640.jpg">
</figure>

And a view of the rear of the mockup shows that everything is packed rather
tightly together. This is why I was so careful about laying it out multiple
times. I didn't want to be putting parts into the final panel only to discover
that one thing physically interfered with something else.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-11-640.jpg">
</figure>

This is why I was so careful about laying it out multiple times. I didn't want
to be putting parts into the final panel only to discover that one thing
physically interfered with something else.

Thankfully, it was all good.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-12-640.jpg">
</figure>

Starting to lay out the front panel.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-13-640.jpg">
<figure>

Pilot holes all drilled. Some will stay this size, some will get embiggened.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-14-640.jpg">
</figure>

To get a clean rectangular opening for the LCD panel, I used a dremel, a file, and a steady hand.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-15-640.jpg">
</figure>

All holes drilled finally. From the beginning of layout to the end product, it
took an absurd amount of time. But everything fit perfectly, so it was worth
it.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-16-640.jpg">
</figure>

The moment of truth: the final test fit. All good!

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-17-640.jpg">
</figure>

This is what I had to resort to in order to mount the front panel. Even if I
would have used the four standoffs that it came with, the radiuno board would
have been floppin' in the breeze. The right selection of standoffs and nuts
would take care of this issue.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-18-640.jpg">
</figure>

Remember the mic issue I alluded to before? Do you see it now?

The ring terminal of both jacks is affixed into metal. The left one is
"ground", which is good. The right one is the PTT, which is bad. Leaving it
like this and just plugging in the speaker mic would cause the radio to
transmit all SSB all the time.

What I *could* have done is remove the jacks, cut out a rectangle, rivet in a
piece of sturdy plastic, and mount the jacks in that. And that's exactly what I
would do if I were doing it all over again. But: A) I didn't have the room to
add a new piece of plastic plus rivets and B) couldn't really be arsed.

So, wat do?

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-19-640.jpg">
</figure>

It ain't pretty, but it works. The tip of the larger jack was unused, so now
it's the PTT.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-20-640.jpg">
</figure>

All wired up!

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-21-640.jpg">
</figure>

Wires and such prettied up with zip ties.

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-22-640.jpg">
</figure>

Verdict: EET VERKS!

<figure>
  <img src="{static}/images/my-bitx40-build/bitx40-23-640.jpg">
</figure>

Shot of the rear end, for those who are into that sort of thing.
