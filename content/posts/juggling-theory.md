title: The role of math in juggling
slug: juggling-theory
tags: Juggling, Math
status: draft
date: 2020-08-30
mathengine: mathjax
ExtraCSS: css/pygments-manni.css
summary: This post explains how math and computer science can be applied to juggling, a seemingly non-mathematical field. This gives us more insight into what really goes on in a juggling pattern and helps us automate the process of finding new juggling patterns. It is also used to give input to juggling animation software.


This post explains the surprising link between math and juggling.
Juggling theory is a beautiful example of how we can get more insight in
a seemingly non-mathematical area by building a theory and proving stuff.

This post doesn't assume any mathematical background, except that
the last few theorems employ elementary graph theory and number theory.

## What is Juggling?

Juggling is a recreational activity where a person manipulates multiple objects
(usually balls, rings or clubs) by repeatedly throwing and catching them.
If you haven't seen professional juggling before, I highly recommend watching this
<a href="https://youtu.be/wP8tbLBls_M?t=362" target="_blank">amazing performance by Anthony Gatto</a>.

There are different *patterns* in juggling.
The animations below depict three well-known patterns:
cascade, shower and fountain.

<div class="gallery">
<figure>
    <img src="{static}/img/siteswaps/3.gif" />
    <figcaption>Cascade</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/51.gif" />
    <figcaption>Shower</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/4.gif" />
    <figcaption>Fountain</figcaption>
</figure>
</div>

The fundamental problem in juggling theory is how to succinctly describe a juggling pattern.
I used GIF animations above to explain to you what cascade, shower and fountain mean,
but we are interested in a way of representing juggling patterns
that is much smaller (just a few characters long),
reveals the *structure* of the pattern
and can be read and analyzed by machines.
In 1981, Paul Klimek invented a way of representing juggling patterns
as a sequence of integers. His notation is called *siteswap*.

An amazing by-product of having such a notation is the ability to
automate the process of inventing new patterns
by brute-force enumeration of integer sequences.
Previously, only non-beginner jugglers could invent patterns using hit-and-trial.

Another advantage of siteswaps is that they can be used as input to
programs that create animations of juggling patterns.
In fact, that is exactly how I created the above GIFs,
using <a href="https://jugglinglab.org/" target="_blank">Juggling Lab</a>.

## The features of a juggling pattern

There are some assumptions that we'll impose on juggling patterns.
These set of assumptions define our *model*.
Here we will look at a model that is powerful enough to capture most of the well-known patterns
and at the same time is simple enough to analyze.

Our first assumption is that we'll only look at patterns in the *steady state*,
i.e. we won't worry about how the juggler *started* juggling.
Alternatively, we can assume that the juggler started juggling at time $t=-\infty$
and will continue to juggle till time $t=\infty$.

A juggling pattern consists of several features that are orthogonal,
i.e. the features can be varied independently of each other.
We'll discuss some of the important features here, one of which is siteswap.
We'll start with features that are easy to understand,
and then move on to more complex but more important features.

### Speed

Every pattern can be made slower by throwing the objects higher.

<div class="gallery">
<figure>
    <img src="{static}/img/siteswaps/3.gif" />
    <figcaption>Cascade</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/522.gif" />
    <figcaption>Slow cascade</figcaption>
</figure>
</div>

**Assumption**: *all throws are made at integral units of time.*

A unit of time is called a *tick* or a *beat*.
The speed of a pattern is defined by the duration of a tick in seconds.

### Dwell

The amount of time the juggler holds an object in his/her hand is called *dwell*.
Dwell is measured in ticks.
Using a large dwell is called *lazy style*
and using a small dwell is called *hot-potato style*.

<div class="gallery">
<figure>
    <img src="{static}/img/siteswaps/522.gif" />
    <figcaption>Lazy cascade</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/900.gif" />
    <figcaption>Hot-potato cascade</figcaption>
</figure>
</div>

For simplicity of presentation, assume that the dwell is the same for all throws/catches.

### Hand position

A pattern can be modified by changing the positions of hands during throws and catches.
Hand positions can be specified using a coordinate system.
(A standard practice is that the coordinate system for the right hand
is the mirror image of the coordinate system for the left hand.)

<div class="gallery">
<figure>
    <img src="{static}/img/siteswaps/3.gif" />
    <figcaption>Cascade</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/3-cross.gif" />
    <figcaption>Crossed-arm cascade</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/3-out.gif" />
    <figcaption>Reverse cascade</figcaption>
</figure>
</div>

Reverse cascade is similar to the normal cascade,
except that instead of throwing from the inside and catching on the outside,
we throw from the outside and catch on the inside.
(A careful observation will reveal that the reverse cascade is actually a time-reversed
version of the normal cascade.)

The above examples use static hand positioning, i.e.
all throw positions are the same and all catch positions are the same.
We can get nice variations of the cascade, which don't really look like the cascade,
by using dynamic hand positioning.

<div class="gallery">
<figure>
    <img src="{static}/img/siteswaps/3-mills.gif" />
    <figcaption>Mills mess</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/3-wind.gif" />
    <figcaption>Windmill</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/3-cherry.gif" />
    <figcaption>Cherry picker</figcaption>
</figure>
</div>

As stated before, hand positioning is independent of other features of the pattern.
As an example, here are some hand positions applied to the fountain pattern:

<div class="gallery">
<figure>
    <img src="{static}/img/siteswaps/4.gif" />
    <figcaption>Fountain</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/4-out.gif" />
    <figcaption>Reverse fountain</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/4-mills.gif" />
    <figcaption>Fountain mills mess</figcaption>
</figure>
<figure>
    <img src="{static}/img/siteswaps/4-wind.gif" />
    <figcaption>Fountain windmill</figcaption>
</figure>
</div>

### Siteswap

If you look at the first three animations (cascade, shower, fountain),
they have the same hand-positioning and can be made to have the same speed and dwell.
Yet these patterns look very different.
The feature that differentiates them is the order in which objects are thrown and caught.
This information is captured by siteswap.
This is where things start getting mathematical!

**Assumption**: *hands throw alternately*, i.e. at even ticks, the left hand throws
and at odd ticks, the right hand throws. This assumption is called *asynchronicity*.

**Assumption**: *a hand can only hold 1 object at a time.*
This restriction is called *non-multiplexing*.
(Most non-jugglers assume that non-multiplexing is mandatory for juggling,
but that's not always true.)

If all the other features (ticks per second, dwell, hand position) are fixed,
then a juggling pattern can be uniquely determined by specifying two things for each throw:

* The order of the throw, which is the flight-time of a throw in ticks,
plus the dwell. **Assumption**: *throw orders are integers.*
* Whether the object is thrown to the same hand or to a different hand.

It's not hard to observe that the order of a throw is odd
iff it is thrown to a different hand.
This is because if an object is thrown at time $t$ and has order $x$,
then it will be thrown next at time $t+x$.
Since hands throw alternately, an odd $x$ will change the throwing hand.
Therefore, to specify a throw, we only need to specify the order of every throw.

**Assumption**: *patterns are periodic.*
So, we only need to state the smallest repeating subsequence
of the infinite sequence of throw orders.
This finite-sized subsequence is called a siteswap.
The length of this subsequence is called the period of the siteswap.

Looking at a pattern and figuring out its siteswap
can be tricky at first, especially if you're new to juggling.
I'll show some examples, and explain what a ladder diagram is,
so that you get comfortable with the concept of siteswap.

## Siteswap examples (Incomplete)

## What is a valid siteswap? (Incomplete)

If we take an arbitrary sequence of integers, will it be the siteswap of some juggling pattern?
As we'll see, the answer turns out to be "no". But why?
At each tick, we just have to throw according to the throw-order.
There's no complex decision-making involved here.
What could go wrong? Try to think about it before reading further.

Turns out that to throw a ball, there must be a ball in your hand.
If your throw-orders at odd ticks are odd and throw-orders at even ticks are even,
balls will land in your hands only on even ticks,
so at odd ticks, eventually you won't have any balls left to throw.
But there's more. You also need to ensure that the number of balls
landing in your hand at each tick is not more than 1.
Otherwise, you'll have more balls than you can throw.

So how can we find out if a sequence of integers is a valid siteswap?
I'll get straight to the point, like this:

**Theorem 1**: Let $a = [a_0, a_1, \ldots, a_{n-1}]$ be a sequence of $n$ non-negative integers.
Let $\mathbb{Z}_n = \{0, 1, \ldots, n-1\}$.
For each $i \in \mathbb{Z}_n$, let $b_i = (i + a_i) \bmod n$.
Then $a$ is a valid siteswap iff $b$ is a permutation of $\mathbb{Z}_n$.

Theorem 1 gives us the following $O(n)$-time algorithm (python code ahead):

    :::python
    def is_valid(a):
        freq = [0] * len(a)
        for i in range(n):
            b_i = (i + a[i]) % n
            freq[b_i] += 1
        for j in freq:
            if j != 1:
                return False
        return True

We'll now try to prove theorem 1. To do that, we first need to get a good
characterization of what a valid siteswap is.
Essentially, we're trying to remove the *juggling* from the problem
and reduce it to a pure math problem.

Let $a$ be a sequence of $n$ non-negative integers.
We'll now define a function $f_a: \mathbb{Z} \mapsto \mathbb{Z}$,
that takes as input a *throw time* and outputs the corresponding *catch time*.
\\[ f_a(x) = x + a[x \bmod n] \\]

Here $a[i]$ is the $i^{\textrm{th}}$ integer in $a$ and $x \bmod n$
is the remainder obtained after dividing $x$ by $n$.

Now we need to prove two things:

* At any time $y$, we have a ball to throw, i.e.
$\forall y \in \mathbb{Z}, \exists x \in \mathbb{Z}, f_a(x) = y$.
* We don't have collisions, i.e. there shouldn't be multiple balls landing
in your hand at the same time:
$\forall x_1, x_2 \in \mathbb{Z}, (f_a(x_1) = f_a(x_2) \implies x_1 = x_2)$.

Does this look familiar? This is exactly the definition of a bijection!
The first conditions says that $f_a$ should be onto,
and the second condition says that $f_a$ should be one-to-one.
Therefore, we get that $a$ is a valid siteswap iff $f_a$ is a bijection.

Define the predicate $P$ as:<br>
*$P(a)$: For $b_i = (i + a[i]) \bmod n$, $b$ is a permutation of $\mathbb{Z}_n$.*<br>
Now theorem 1 reduces to this lemma:

**Lemma 2**: Let $a$ be a sequence of $n$ non-negative integers.
Then $f_a$ is a bijection iff $P(a)$.

Lemma 2 has no reference to juggling. It's a purely mathematical fact.
Now that we're in familiar territory, you should try proving it yourself
before you read my proof below.
This is because math has one thing in common with juggling:
for maximum enjoyment, you must try it yourself.

### Easy part of the proof

**Lemma 3**: If $f_a$ is a bijection, then $P(a)$ holds.

**Lemma 4**: $P(a)$ implies that $f_a$ is one-to-one.

### Hard part of the proof

**Lemma 5**: If $f_a$ is one-to-one, then $f_a$ is onto.

## Other properties of a siteswap (Incomplete)

**Theorem**: Let $a$ be a siteswap of period $n$.
Then the number of objects being juggled is $(\sum_{i=1}^n a_i)/n$.

The proof of the above theorem is quite involved. Read the editorial of problem
<a href="https://www.codechef.com/ICL2017/problems/ICL1703" target="_blank">ICL1703</a> on Codechef.

## Other stuff (Incomplete)

* How to start a pattern
* Transitions.
* Throw-orders 0 and 2.
* Synchronous and multiplexing.
