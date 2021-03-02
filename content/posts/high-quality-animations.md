title: Creating high-quality animations
slug: high-quality-animations
date: 2021-03-02
status: draft
summary: Animated videos are great for explaining stuff, and I want to incorporate such videos in my presentations. I had trouble finding the right tools for this task, but later realized that SVG and CSS can do what I want. Here I'll describe my motivation and the advantages of this method.


## Why animate?

I'm a fan of some popular science channels on YouTube,
like [Veritasium](https://www.youtube.com/c/veritasium)
and [SmarterEveryDay](https://www.youtube.com/c/smartereveryday).
Their videos are interesting to watch and explain concepts in a way that's easy to grasp.

One of the things that really impressed me is their use of high-quality animations.
Including animated diagrams in a presentation aids understanding
in the same way that including figures in a book or research paper does:
by making visualization easier.
However, the effect is more pronounced in animated diagrams
since they help us clearly see how a system changes over time.
As an example, Veritasium's video on
[measuring the speed of light](https://www.youtube.com/watch?v=pTn6Ewhb27k&t=107s)
(watch from 00:01:47 to 00:03:20)
clearly shows how the clocks and light pulses behave during different experiments.

Being an (aspiring) academic, I couldn't help but compare these videos
to those created by other academics, like lecture videos and conference talks
(due to the COVID-19 pandemic, many conference talks are now pre-recorded).
Most academic talks sound like PowerPoint presentations or whiteboard/blackboard presentations.
There's nothing wrong with this though, because
for most academic videos, if they contain enough figures,
then adding animated diagrams would have very little marginal utility,
and making high-quality animations is (apparently) a very time-consuming task.
However, occasionally some complicated explanations can benefit from them,
and classic, well-known results deserve good videos because a lot of people will watch them.
Consequently, creating such videos is something I wanted to dabble in.

## Searching for animation tools

I searched the internet for animation programs, but the results didn't seem relevant.
Specifically, most of them seemed to target two use cases:
artistic creations (like cartoons) and simple slideshow-like animations.
It's possible that I overlooked or misjudged some of these tools.
My sister, who is an artist, recommended
[Adobe After Effects](https://www.adobe.com/products/aftereffects.html),
but that is non-free and very expensive.
I was also afraid that some of these tools may have a very steep learning curve.

Then an idea struck me: why not ask Derek Muller (the creator of Veritasium)?
The kind of animations his videos have are very similar to what I want to make.
So I emailed him, and this was his reply:

> I hire animators and I would advise you do the same.
> It's a specialized skill set so it's best to hire an expert.

I was pleasantly surprised that he replied so quickly;
I thought he would be too busy for that.
But I can't hire people, so the reply didn't help much.

## The solution

Because of some front-end web development work that I did
(check out my [github repos](https://github.com/sharmaeklavya2?tab=repositories)
labeled 'web' for examples), I could recall that we can
[animate SVG elements using CSS](https://blog.logrocket.com/animating-svg-with-css-83e8e27d739c/).
This technique seems to be useful for GIF-like animations,
but I think they can be used to create longer animations too.

I created the following short animation to experiment
(you can click the image and then
[view the source code](https://www.computerhope.com/issues/ch000746.htm)):

<figure>
<a href="{static}/img/snake.svg">
<img class="nofilter" src="{static}/img/snake.svg" alt="Red balls bouncing in a box"/>
</a>
<figcaption>Simple animation using SVG</figcaption>
</figure>

### SVG is vector

SVG images are vector images, i.e., there's no concept of 'pixel' in SVG.
Vector images can be infinitely zoomed into without loss of quality.
For non-photographic images (like diagrams), this leads to a very compact representation.
This advantage carries over to SVG animations as well.

Similarly, SVG animations don't have the concept of frames; they are 'vectored in time'.
One can display them at frame rates as large as what the display device supports.

### SVG is text-based

SVG is text-based, i.e., one has to write code in a text file
instead of using a graphical editor.
Therefore, it has the same advantages that [TikZ](https://github.com/pgf-tikz/pgf)
has for making figures in a TeX document:
diffing and version-control are easy, and we can optionally get automation
(i.e., writing a program that outputs an SVG instead of writing an SVG by hand)
using, for example, Python and [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/).

### Converting to video

To convert the SVG animation to a traditional format (like MP4),
you can run the animation in your browser and record your screen.
But if your computer is not fast enough to run the SVG animation at
a good frame-rate, then the recorded video will be jittery.

I couldn't find an appropriate SVG to video converter on the internet,
so I had to implement my own converter:
<https://github.com/sharmaeklavya2/svg-to-video>.
The output of my converter doesn't have any jitter.
Unfortunately, it is very slow
([for reasons beyond my control](https://github.com/puppeteer/puppeteer/issues/476)):
it takes around 75 ms per frame on my Ubuntu and 240 ms per frame on my MacBook.

A disadvantage of SVG animations is that they're hard to pause, resume and seek
like normal videos. This can make it hard to create long animations, since you'll
have to wait for the whole animation to finish before you can see the end.
But you can work around that by using
[animation-play-state](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-play-state)
and [animation-delay](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-delay)
with [custom CSS properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties).
In fact, this is how my svg-to-video program works;
it pauses the animation using `animation-play-state: paused`,
it repeatedly makes slight increments to `animation-delay` to seek to different times,
and takes a screenshot at each instant.
