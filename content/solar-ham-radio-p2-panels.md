Title: A Pretty Okay Solar Ham Station, Part 2: Panels
Date: 2025-08-11
Tags: Radio, Solar

<figure>
  <a title="Partonez, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Field_of_Solar_Panels_near_Ogwell.jpg">
    <img alt="A field of solar panels" src="{static}/images/solar-ham-radio/panel-field.jpg">
  </a>
  <figcaption>Field of dreams?</figcaption>
</figure>

Back in [Part 1]({filename}/solar-ham-radio-p1.md), I <s>emptied my soul</s> laid out the rough qualifications for a somewhat minimalist solar-powered ham radio station. Today, I'd like to walk you through my process for selecting the solar panels for this lash-up of geekery.

I thought picking out solar panels for this project would be easy peasy lemon squeezy. Instead, it turned out to be difficult difficult lemon difficult. There were several factors involved:

* **Type:** Rigid? Flexable? Foldable?
* **Size:** How much power (in watts) do I need?
* **Also Size:** Will they fit in my trunk and not be awkward to carry, deploy, and store at home?

We already covered power requirements, so we know we're targeting 100 watts, _maybe_ 200 in the future.

<figure>
  <img src="{static}/images/solar-ham-radio/jiggawatts.svg">
</figure>

Credit card at the ready, I headed straight to the jungle site to see what was available. I was quite drawn to the foldable solar panels because they looked like _exactly_ what I was after. Spoiled for choice, as it were. Looking closer, though, I spotted a major problem: Nearly _all_ of the reviews for nearly _all_ these are fake. Well, not exactly fake. Probably some are fake. Let's maybe compomise on "not even remotely trustworthy" since the writers were given the product for free (and just _happen_ to leave a gushing review), or got some kind of after-the-fact discount or rebate or something.

I couldn't find a _single foldable solar panel on all of Amazon_ with positive reviews that had any non-negligible number of honest-looking reviews. Don't bother going to YouTube looking for reviews, YouTubers _also_ typically get their products for free and/or get a kickback when you click their links to buy them. (And they usually don't test them for performance and durability. You know, the most important things.)

The more I looked at the foldable solar panels, the less I liked them in general:

* Many claim to be waterproof, but clearly are not. They are made of fabric or canvas which, yes, won't _immediately_ deteriorate on contact with water, but _will_ hold water in concealed areas for longer than you'd like. Possibly getting moldy in the process. Or breaking down with age and use. I want panels that can survive everything from night-time dew to actual, literal downpours. I'm trying to play radio here and don't want to be interrupted to un-deploy the panels at the slightest whiff of rain.
* Most have really flimsy or ill-engineered wires connecting the panels together. In other words, they have a limited number of fold/unfold cycles. Among other quality concerns.
* The solar cells are _flexible_, and [flexible panels do not last](https://www.mobile-solarpower.com/solar-panels.html).
* The kickstands for theses seem to be universally _terrible_.
* They cost quite a bit more than rigid panels.

<figure>
  <img src="{static}/images/solar-ham-radio/dumpster_fire.webp">
  <figcaption>Folding solar panels in a nutshell.</figcaption>
</figure>

Yes, there are also rigid panels that fold together, but they all seem to be weirdly expensive or of questionable quality, or both.

So what's a hambro to do? It turns out they sell smallish rigid 50 watt panels, and the price-per-watt is not out of line compared to the typical 100-plus watt panels that you see everywhere. These are about the size of a very thin couch cusion and probably stack very nicely. Especially in a custom-made canvas travel and storage bag I that I suddenly plan to ask my wife to make for me.

First, you can cross off the panels that have an obviously-offshore ring to them like SOLARRAWR or PureSunNiceShineGood. Nobody who buys these is concerned with quality, they're getting them because they're cheap. (Or free, see above.) Renogy is a well-known brand that generally gets favorable reviews, but I honestly can't tell if that's because they are actually okayish or because they are playing the payola game better than anyone else on the jungle site right now.

Buying panels made in the US is just an immediate not-gonna-happen because \[insert favorite political punching bag here\], so I did the next best thing and tried to find a company at least _run_ by people in North America that sells panels made overseas but to their own specifications. Bonus points for a decent website and warranty. This led me to the [Rich Solar MEGA 50 panels](https://richsolar.com/collections/solar-panels/products/mega-50-50-watt-12-volt-solar-panel) (not an affiliate link). The dimensions are 23 by 21 inches, so will easily fit in the trunk alongside other stuff. They have all of the specifications listed upfront and have a warranty (25 years output, 10 year workmanship). Mine claim to be made in Vietnam. They were $60 each shipped. 

<figure>
  <img src="{static}/images/solar-ham-radio/mega-50-panels.webp">
</figure>

So in addition to the wattage, there are also a couple other things you should pay attention to when buying the panels because they are important to know when buying your charge controller:

* Open circuit voltage: the voltage provided by the panel with no load connected
* Short circuit current: the amount of current that can be drawn with a full load (short circuit)

These play into figuring out what kind of charge controller to get, and your overall panel configuration.

On rigid panels, basically there is not much to screw up: they are just the solar panel itself, an aluminum frame, a junction box, and some wires. I can totally engineer my own carrying and kickstand solution, if it means I never have to worry about crappy hinges, connecting wires, or floppy kickstands failing on me at setup time.

The hardest part about building a solar power system is making sure everything works together. There are an almost infinite number of combinations and there are basically no parts that work for _all_ situations. In my case, it was made somewhat easier by the small scale of the system (100 watts, one battery, one charge controller) but in bigger installations you have to wrestle with questions like whether it's better to wire the solar panels together in series or parallel, or some combination of the two. How _many_ to wire in series vs parallel has knock-on effects like wire size (and thus cost), which charge controllers you can get away with, where to put fuses, etc.

[It's a deep rabbit hole.]({filename}/rabbit-holes.md)

In _most_ cases, for smaller installations at least, it is best to connect the panels in series up to the maximum voltage that the panels or the charge controller can handle. There are a few reasons for this, but I'll tell you the biggest. In the [previous article]({filename}/solar-ham-radio-p1.md), we said that power (watts) is equal to voltage times current:

```
voltage * current = watts
```

If we have two 50 watt panels, we can choose to wire them in series or parallel. Now keep in mind that voltage and current in a solar panel are _usually_ constantly changing but to simplify, let's say our panels are producing their max power of 50 watts according to the spec sheet:

```
17.1 volts * 2.92 amps = 49.932 watts
```

If we have two of them and wire them in parallel, we double the amount of current that can be drawn from them:

```
17.1 volts * (2.92 amps * 2) = 99.864 watts
```

And if we wire them in series instead, we double the voltage but the current stays the same:

```
(17.2 volts * 2) * 2.92 amps = 100.448 watts
```

Note that the power output is the same, except for a very small difference that is due to the precision of our numbers. (Not a physical trait of the solar panels or configuration.) So why do we care about the difference between series and parallel if we get the same power either way? In a word:

<figure>
  <img src="{static}/images/solar-ham-radio/current.jpg">
</figure>

When you want to move power from one place to another, and when you can choose between either higher voltage or higher current, you should almost always pick higher voltage. The reason for this is that higher current requires bigger wires, connectors, fuses, and other equipment. This adds cost (and perhaps weight) to the project.

But from a power engineering perspective, voltage is almost free. The main things to keep in mind as the volts creep up is that higher voltages tend to be more dangerous, so you have to do a good job of physical cable management and keeping the live bits away from wayward humans. (As well as staying within the specifications of your equipment, of course.)

In my case, with only two panels to worry about, whether to wire them in series or parallel is largely a function of which one my charge controller is going to be happiest with.

That'll do it for this one, I hope some of this made minimum amount of sense. In the next article, we'll be done with math for a while and instead talk about the near-futile journey of finding a decent battery.
