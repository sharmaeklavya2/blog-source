title: The Math behind Juggling
slug: juggling-theory
tags: Juggling, Math
date: 2020-09-22
mathengine: katex-full
summary: This article explains how math can be applied to juggling, a seemingly non-mathematical area. This gives us more insight into what really goes on in a juggling pattern and helps us automate the process of finding new juggling patterns.


This article explains the surprising link between math and juggling.
Juggling theory is a beautiful example of how we can get more insight in
a seemingly non-mathematical area by building a theory and proving stuff.

Most of this article doesn't assume any specialized mathematical background.
Towards the end, basics of graph theory and number theory are used.

[TOC]

## What is juggling?

Juggling is a recreational activity where a person manipulates multiple objects
(usually balls, rings or clubs) by repeatedly throwing and catching them.
If you haven't seen professional juggling before, I highly recommend watching this
<a href="https://youtu.be/wP8tbLBls_M?t=32">amazing performance by Anthony Gatto</a>.

There are different *patterns* in juggling.
The animations below depict three well-known patterns:
cascade, shower and fountain.

<div class="gallery">
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/3.gif.mp4" alt="cascade juggling pattern"></video>
    <figcaption>Cascade</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="200"
        src="{static}/img/siteswaps/51.gif.mp4" alt="shower juggling pattern"></video>
    <figcaption>Shower</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/4.gif.mp4" alt="fountain juggling pattern"></video>
    <figcaption>Fountain</figcaption>
</figure>
</div>

The fundamental problem in juggling theory is how to succinctly describe a juggling pattern.
I used GIF animations above to explain to you what cascade, shower and fountain mean,
but we are interested in a way of representing juggling patterns
that is much smaller (just a few characters long),
reveals the *structure* of the pattern, and can be read and analyzed by machines.
In 1981, Paul Klimek invented a way of associating a sequence of integers
to each juggling pattern. This sequence of integers is called a *siteswap*,
and it captures important properties of a jugging pattern.
In this article, I'll show how to succinctly represent juggling patterns,
and siteswaps form the most important part of this representation.

An amazing by-product of having such a representation is the ability to
automate the process of inventing new patterns
by brute-force enumeration of integer sequences.
Previously, only non-beginner jugglers could invent patterns using hit-and-trial.

Another advantage of siteswaps is that they can be used as input to
programs that create animations of juggling patterns.
In fact, this is exactly how I created all the animations in this article,
using <a href="https://jugglinglab.org/">Juggling Lab</a>.

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
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/3.gif.mp4" alt="cascade juggling pattern"></video>
    <figcaption>Cascade</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/522.gif.mp4" alt="cascade juggled slowly"></video>
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
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/522.gif.mp4" alt="cascade juggling in lazy style"></video>
    <figcaption>Lazy cascade</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/900.gif.mp4" alt="cascade juggling in hot-potato style"></video>
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
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/3.gif.mp4" alt="cascade juggling pattern"></video>
    <figcaption>Cascade</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/3-cross.gif.mp4" alt="crossed-arm cascade juggling pattern"></video>
    <figcaption>Crossed-arm cascade</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/3-out.gif.mp4" alt="reverse cascade juggling pattern"></video>
    <figcaption>Reverse cascade</figcaption>
</figure>
</div>

Reverse cascade is similar to the normal cascade,
except that instead of throwing from the inside and catching on the outside,
we throw from the outside and catch on the inside.
(A careful observation will reveal that the reverse cascade is actually a time-reversed
version of the normal cascade.)

By using more complicated hand-positions, we can get awesome variations
of the cascade, that don't really look like the cascade.

<div class="gallery">
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/3-mills.gif.mp4" alt="mills-mess juggling pattern"></video>
    <figcaption>Mills mess</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/3-wind.gif.mp4" alt="windmill juggling pattern"></video>
    <figcaption>Windmill</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/3-cherry.gif.mp4" alt="cherry-picker juggling pattern"></video>
    <figcaption>Cherry picker</figcaption>
</figure>
</div>

As stated before, hand positioning is independent of other features of the pattern.
As an example, here are some hand positions applied to the fountain pattern:

<div class="gallery">
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/4.gif.mp4" alt="4 juggling pattern"></video>
    <figcaption>Fountain</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/4-out.gif.mp4" alt="4-out juggling pattern"></video>
    <figcaption>Reverse fountain</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/4-mills.gif.mp4" alt="4-mills juggling pattern"></video>
    <figcaption>Fountain mills mess</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/4-wind.gif.mp4" alt="4-wind juggling pattern"></video>
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
but that's not always true. We will, however, enforce non-multiplexing in our model for simplicity.)

If all the other features (ticks per second, dwell, hand position) are fixed,
then a juggling pattern can be uniquely determined by specifying two things for each throw:
how high should the object be thrown, and whether the object is thrown to the same
hand or to the other hand.
(In the fountain pattern, all throws are made to the same hand,
and in cascade all throws are made to the other hand.)

To specify how high an object is thrown, we associate a number with the throw,
called *order* (also called *throw-order*).
The order of a throw is defined to be the flight-time of a throw in ticks, plus the dwell.
So if an object is thrown at time $t$ with order $x$,
that object will be thrown next at time $t+x$.
This implies that throw-orders must be integers.

Actually, we don't need to specify whether an object is thrown
to the same hand or not, because that can be inferred from the throw order.

**Lemma 1**: An object is thrown to the same hand iff the throw-order is even.

*Proof*. Define the parity of an integer $y$ to be 1 if $y$ is odd and 0 if $y$ is even.
Since hands throw alternately, the parity of the throwing time decides whether
the object is thrown from the left hand or the right hand.
Suppose an object is thrown at time $t$ with order $x$.
Then it is thrown to the same hand iff the parities of $t$ and $t+x$ are the same,
which happens iff $x$ is even. $\Box$

**Assumption**: *patterns are periodic.*
So, we only need to state the smallest repeating subsequence
of the infinite sequence of throw orders.
This finite-sized subsequence is called a siteswap.
The length of this subsequence is called the period of the siteswap.

Looking at a pattern and figuring out its siteswap
can be tricky at first, especially if you're new to juggling.
I'll show some examples so that you get the hang of it.

## Siteswap examples

Let's start with the simplest pattern: cascade.

<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/3-analyze.gif.mp4" alt="3-analyze juggling pattern"></video>
    <figcaption>Cascade</figcaption>
</figure>

First, note that all throws are identical.
So all throws have the same throw-order.

Suppose the blue ball is thrown at time $t$.
At time $t+1$ the red ball is thrown, at time $t+2$ the green ball is thrown,
and at time $t+3$ the blue ball is thrown again.
Therefore, the time between consecutive throws of the blue ball is 3 ticks.
Hence, all throws have order 3.
This gives us the siteswap `[3]` for this pattern.

Let's now look at a pattern, which, as far as I know, doesn't have a common name.
It's identified solely by its siteswap.

<div class="gallery">
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="280"
        src="{static}/img/siteswaps/345.gif.mp4" alt="345 juggling pattern"></video>
    <figcaption>Normal</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="280"
        src="{static}/img/siteswaps/345-analyze.gif.mp4" alt="345-analyze juggling pattern"></video>
    <figcaption>Slo-mo</figcaption>
</figure>
</div>

We'll repeat the same trick as last time. Just keep noting down the colors of the throws.
Denote the colors gray, red, green, blue by characters `_`, `r`, `g`, `b`, respectively.
Then the colors of the throws is the string `_bg_rb_gr` repeated indefinitely.
Now for each throw, find the next throw of the same color,
and compute the difference of their throw-times to the get the throw-order.
This gives us the sequence `[3, 4, 5]` repeated indefinitely.

    _bg_rb_gr_bg_rb_gr_bg_rb_gr
    34534534534534534534534

Therefore, our siteswap is `[3, 4, 5]`.
Usually people just concatenate the numbers together and write `345` instead of `[3, 4, 5]`.
This is not a problem, since throw orders above 9 rarely arise in practice,
and even if they do, we can use `a` for 10, `b` for 11, and so on.

## When is a siteswap valid?

If we take an arbitrary sequence of integers, will it be the siteswap of some juggling pattern?
As we'll see, the answer turns out to be "no". But why?
Try to think about it before reading further.
(Hint: Is `43` a valid siteswap? If yes, what does it look like?
If no, why is it invalid?)

Turns out that to throw a ball, there must be a ball in your hand.
If your throw-orders at odd ticks are odd and throw-orders at even ticks are even,
balls will land in your hands only on even ticks,
so at odd ticks, eventually you won't have any balls left to throw.
But there's more. You also need to ensure that the number of balls
landing in your hand at each tick is not more than 1.
Otherwise, you'll have more balls than you can throw.
Think of these two constraints as the equivalent of *conservation of mass*.

So how can we find out if a sequence of integers is a valid siteswap?
I'll get straight to the point, like this:

**Permutation Theorem**: Let $a = [a_0, a_1, \ldots, a_{n-1}]$ be a sequence of $n$ non-negative integers.
Define the function $g_a: \mathbb{Z}_n \mapsto \mathbb{Z}_n$ as $g_a(i) = (i + a_i) \bmod n$.
Then $a$ is a valid siteswap iff $g_a$ is a bijection
(i.e., $[g_a(0), g_a(1), \ldots, g_a(n-1)]$ is a permutation of $\mathbb{Z}_n$).

For those unfamiliar with notation, $\mathbb{Z}_n$ denotes the set $\{0, 1, \ldots, n-1\}$,
and $x \bmod y$ denotes the remainder obtained by dividing $x$ by $y$.

> In the permutation theorem, you mentioned that $a$ is a sequence of *non-negative* integers.
> Can throw-orders be 0? What would that even mean?
> <footer>observant reader</footer>

Good question! That's a technical detail that I conveniently brushed under the rug.
I'll address this at the end of the article.
For now, you can assume that $a$ only has positive integers
and throw orders can only be positive.
The proofs work for the general case that includes zero-order throws.

The permutation theorem gives us the following $O(n)$-time algorithm (python code ahead):

    :::python
    def is_valid(a):
        n = len(a)
        freq = [0] * n  # a list of n zeros
        for i in range(n):  # i from 0 to n-1
            b_i = (i + a[i]) % n
            freq[b_i] += 1
        for j in freq:
            if j != 1:
                return False
        return True

We'll now try to prove the permutation theorem. To do that, we first need to get a good
characterization of what a valid siteswap is.
Essentially, we're trying to remove the *juggling* from the problem
and reduce it to a pure math problem.

Let $a$ be a sequence of $n$ non-negative integers.
We'll now define a function $f_a: \mathbb{Z} \mapsto \mathbb{Z},$
that takes as input a *throw time* and outputs the corresponding *catch time*.
$$f_a(x) = x + a[x \bmod n]$$
Here $a[i] = a_i$.

Now we need to prove two things:

* At any time $y$, we have a ball to throw, i.e.
$\forall y \in \mathbb{Z},$ $\exists x \in \mathbb{Z},$ $f_a(x) = y$.
* We don't have collisions, i.e. there shouldn't be multiple balls landing
in your hand at the same time:
$\forall x_1, x_2 \in \mathbb{Z},$ $(f_a(x_1) = f_a(x_2)$ $\implies x_1 = x_2)$.

Does this look familiar? This is exactly the definition of a bijection!
The first conditions says that $f_a$ should be onto,
and the second condition says that $f_a$ should be one-to-one.
Therefore, we get that $a$ is a valid siteswap iff $f_a$ is a bijection.

Now the permutation theorem reduces to this lemma:

**Lemma 2**: Let $a$ be a sequence of $n$ non-negative integers.
Then $f_a$ is a bijection iff $g_a$ is a bijection.

Lemma 2 has no reference to juggling. It's a purely mathematical fact.
Now that we're in familiar territory, you should try proving it yourself
before you read my proof below.

> Mathematics shares one feature with juggling:
> for maximum enjoyment, you have to try it yourself.
> <footer>Joe Buhler and Ron Graham<sup><a href="#cite-buhler-graham">[1]</a></sup></footer>

### Easy part of the proof

Since the domain and co-domain of $g_a$ are identical and finite,
$g_a$ is a bijeciton iff $g_a$ is one-to-one.

**Lemma 3**: If $f_a$ is one-to-one, then $g_a$ is one-to-one.

*Proof*. Assume $g_a$ is not one-to-one. Then $\exists i_1, i_2 \in \mathbb{Z}_n$ such that
$i_1 \neq i_2$ and $g_a(i_1) = g_a(i_2)$.

$$\begin{aligned}
& g_a(i_1) = g_a(i_2)
\\ &\implies (i_1 + a[i_1]) \bmod n = (i_2 + a[i_2]) \bmod n
\\ &\implies \exists k \in \mathbb{Z}, i_1 + a[i_1] = i_2 + a[i_2] + kn
\\ &\implies \exists k \in \mathbb{Z}, f_a(i_1) = f_a(i_2 + kn)
\end{aligned}$$
This is a contradiction, since $f_a$ is one-to-one.
Hence, $g_a$ is one-to-one. $\Box$

**Lemma 4**: $g_a$ is one-to-one implies $f_a$ is one-to-one.

*Proof*. Assume $f_a$ is not one-to-one.
Then $\exists u_1 \neq u_2$ such that $f_a(u_1) = f_a(u_2)$.
Let $i_1 = u_1 \bmod n$ and $i_2 = u_2 \bmod n$.

*Case 1*: $i_1 = i_2$.<br>
$f_a(u_1) = f_a(u_2)$ $\implies u_1 + a[i_1] = u_2 + a[i_2]$ $\implies u_1 = u_2.$
This is a contradiction, since $u_1 \neq u_2$.

*Case 2*: $i_1 \neq i_2$.
$$\begin{aligned}
& f_a(u_1) = f_a(u_2)
\\ &\implies u_1 + a[i_1] = u_2 + a[i_2]
\\ &\implies i_1 + a[i_1] \equiv i_2 + a[i_2] \pmod{n}
\\ &\implies g_a(i_1) = g_a(i_2)
\end{aligned}$$
This is a contradiction, since $g_a$ is one-to-one.
Hence, $f_a$ is one-to-one. $\Box$

### Not-so-easy part of the proof

**Lemma 5**: If $f_a$ is one-to-one, then $f_a$ is onto.

*Proof*.
There are 3 crucial insights in this proof.
The first is that we can represent $f_a$ as a graph of infinite size.
Formally, let $G_a$ be a graph whose vertex set is $\mathbb{Z}$.
For each $x \in \mathbb{Z}$, there is an edge from $x$ to $f_a(x)$.
Hence, the out-degree of each vertex is 1.
$f_a$ is one-to-one means that the in-degree of each vertex is at most 1.
We want to show that $f_a$ is onto, i.e. every vertex has in-degree at least 1.
(Actually, there's a name for $G_a$ when $a$ is a valid siteswap:
it's called a *ladder diagram*.)

It is easy to see that if $(u, v)$ is an edge in $G_a$,
then for any $k \in \mathbb{Z}$, $(u - kn, v - kn)$ is also an edge in $G_a$.
This is the second crucial idea of this proof.

The third crucial idea is to assign two labels to each number:
a major label $M(x) = \lfloor x/n \rfloor$ and a minor label $m(x) = x \bmod n$.
We then partition $\mathbb{Z}$ by the major label.
Therefore, there are an infinite number of partitions and each partition has $n$ numbers.

For an arbitrary integer $r$, consider the set $S$ of integers having major label $r$.
There are $n$ edges that come out of $S$, i.e. $n$ edges have their source vertex in $S$.
We now ask: how many edges enter $S$
(i.e. how many edges have their target vertex in $S$)?
We'll now show that at least $n$ edges enter $S$.
Since $f_a$ is one-to-one, this would prove that the number of edges entering $S$
is equal to $n$ and each vertex in $S$ has in-degree exactly 1.

Let $S = \{u_0, u_1, \ldots, u_{n-1}\},$ where $u_i = rn + i$.
Let $v_i = f_a(u_i) = u_i + a[i]$.
Suppose the major label of $v_i$ is $s_i$.
Then the major label of $v_i' = v_i - (s_i-r)n$ is $r$, so $v_i' \in S$.
Let $u_i' = u_i - (s_i-r)n$. Then the minor label of $u_i'$ is $i$.

Since $(u_i, v_i)$ is an edge of $G_a$, $(u_i', v_i')$ is also an edge in $G_a$
(as per the second crucial idea).
This edge enters $S$. Also, the integers $u_0', u_1', \ldots, u_{n-1}'$ are all distinct,
since the minor label of $u_i'$ is $i$.
Therefore, at least $n$ edges enter $S$. $\Box$

## Other things about siteswaps

### Average theorem

**Average Theorem**: Let $a$ be a siteswap of period $n$.
Then the number of objects being juggled is $(\sum_{i=1}^n a_i)/n$.

The proof of the average theorem is quite involved, so I'm not going to put it here.
It uses the same ideas as in the proof of the permutation theorem.
It also gives a quick sanity check of a siteswap's validity:
the average should be an integer.

For the sport programmers reading this who are looking for a challenge,
you may want to solve the problem
<a href="https://www.codechef.com/ICL2017/problems/ICL1703">ICL1703</a> on Codechef,
which is a generalization of the average theorem when multiplexing is allowed.
I have abstracted out juggling terminology from this problem,
so you don't need to know anything about juggling to understand it.
I have also written the
<a href="https://discuss.codechef.com/t/icl1703-editorial/14270">solution</a> to it.

### Special throw orders

We assumed that we will throw a ball on every tick.
We can relax this assumption, without violating conservation of mass,
by allowing instances when no ball falls into your hand
and so you don't throw anything.
This situation is called a zero-order throw.
Here are some examples:

<div class="gallery">
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/50505.gif.mp4" alt="snake juggling pattern"></video>
    <figcaption>Snake (50505)</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="220"
        src="{static}/img/siteswaps/330.gif.mp4"
        alt="cascade juggling pattern with 1 ball mising; siteswap 330"></video>
    <figcaption>Cascade with 1 ball <br>missing (330)</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/40.gif.mp4" alt="juggling 2 balls in 1 hand"></video>
    <figcaption>2-in-1 (40)</figcaption>
</figure>
</div>

Sometimes you may want to keep holding on to a ball in your hand instead of throwing it.
This can be achieved via order-2 throws (think why it makes sense).

<div class="gallery">
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/552.gif.mp4" alt="552 juggling pattern"></video>
    <figcaption>552</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/42.gif.mp4" alt="juggling 2 balls in one hand"></video>
    <figcaption>2-in-1 (42)</figcaption>
</figure>
</div>

All the math in this article can be made to work with throws of order 0 and 2.

### Extensions

We assumed that in each tick, only one hand throws and hands throw alternately.
This assumption is called asynchronicity.
This is the most restrictive assumption that we have made.
There are many nice patterns that don't fit in this model.
Fortunately, all of the theory we saw here can be ported to the synchronous model,
and synchronous patterns have their own, somewhat different, siteswap notation.

<div class="gallery">
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/box.gif.mp4" alt="box juggling pattern"></video>
    <figcaption>Box</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/columns.gif.mp4" alt="columns juggling pattern"></video>
    <figcaption>Columns</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="280"
        src="{static}/img/siteswaps/6x4x.gif.mp4" alt="5-ball half-shower juggling pattern"></video>
    <figcaption>5-ball half-shower</figcaption>
</figure>
</div>

Further generalizations include multiplexing,
i.e. allowing multiple balls in a single hand, and passing,
i.e. multiple people juggling together.
Siteswap notation and the associated theory extends to these too.

<div class="gallery">
<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="240"
        src="{static}/img/siteswaps/multiplex-shower.gif.mp4"
        alt="multiplex-shower juggling pattern"></video>
    <figcaption>Multiplexed shower</figcaption>
</figure>
<figure>
    <video class="dark-invert" autoplay loop muted width="240" height="200"
        src="{static}/img/siteswaps/3-pass.gif.mp4" alt="2-count passing cascade with 2 jugglers"></video>
    <figcaption>Passing cascade</figcaption>
</figure>
</div>

### Uses and limitations of mathematical analysis

We can invent new juggling patterns by brute-force enumeration of integer sequences
up to a certain length and then using the permutation theorem to filter out invalid sequences.
Each siteswap output by this process corresponds to a valid juggling pattern.
This is great, and rumors say that `441` was invented like this.

<figure>
    <video class="dark-invert" autoplay loop muted width="160" height="220"
        src="{static}/img/siteswaps/441.gif.mp4" alt="441 juggling pattern"></video>
    <figcaption>Half box (441)</figcaption>
</figure>

However, this approach has limitations.
A lot of patterns look very similar to each other.
Out of the many patterns output by this algorithm,
only some may be aesthetically pleasing,
that too after carefully choosing an appropriate hand positioning.
So in practice, highly skilled humans outperform machines in inventing *interesting* patterns.

But that doesn't mean this theory is useless!
There are other uses of juggling theory,
like animation programs, transitioning across patterns,
generating patterns under constraints, etc.
Also, an understanding of juggling theory can help jugglers
invent interesting patterns more easily.
This is how I invented `615150` and `6051`,
and these patterns helped me learn to
[juggle 3 balls in 1 hand]({filename}/posts/3-in-1.md).

You can try inventing your own patterns, and then easily see what they look like using
<a href="https://jugglinglab.org/">Juggling Lab</a>
or its <a href="https://jugglinglab.org/html/animinfo.html">GIF server</a>.

## Want to learn how to juggle?

Juggling is a very enjoyable hobby. If you feel motivated,
see my other article, [Juggling 101]({filename}/posts/juggling-101.md), on how to learn juggling.

I started learning juggling a few months before I joined BITS Pilani as an undergraduate student.
By the end of my third semester, I had learned around 30 different patterns.
You can see my progress on
<a href="https://www.youtube.com/watch?v=xYrnQMHfDNE&list=PLACN_dyOcd_WSIzGV-4hVCQyQFmzKH1kb">
YouTube</a>.

## References

<ol>
<li class="citation" id="cite-buhler-graham">
<!--<span class="cite-name">buhler-graham</span><br>-->
<span class="cite-authors">Joe Buhler and Ron Graham.</span>
<cite class="cite-title">
<a href="http://www.math.ucsd.edu/~fan/ron/papers/04_05_juggling.pdf">
Juggling patterns, passing, and posets.</a></cite><br>
<span class="cite-source">In Mathematical Adventures for Students and Amateurs (2004): 99&ndash;116.</span>
</li>
</ol>
