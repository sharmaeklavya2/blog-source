title: Pricing Mechanisms and the Riemann-Stieltjes Integral
slug: auctions-and-integration
tags: Math
date: 2025-07-01
mathengine: katex-full
summary: While studying pricing mechanisms, trying to formalize simple results led me down the rabbit hole of Riemann-Stieltjes integrals.


$$@
\def\Pcal{\mathcal{P}}
\def\rhat{\widehat{r}}
$$

Imagine we are trying to sell a sack of rice. We want to make as much money from this sale as possible. What should we do? This is an important problem in the field of *mechanism design*, which is a part of *game theory*. I was studying this problem in a very simple setting, and came across some very interesting math while doing so. In this article, I will share my mathematical journey. I won't talk much about the *mechanism design* part to keep this article accessible to a broad audience.

[TOC]

## Posted-Price Mechanisms

Let's consider the simplest case where there is
exactly one person in the world who wants to buy what we're selling.
One of the simplest and most obvious mechanisms is a *posted-price mechanism*.
Here we set a price $p$ for the item. We then offer two options to the buyer:

1.  **purchase**: The buyer gets the item and pays us $p$ dollars.
2.  **decline**: The buyer doesn't get the item and we don't get any money.

We expect the buyer to pick the option that's more preferable to them.
Specifically, the buyer has a value $v$ for the item.
If $v ≥ p$, they will purchase it, otherwise they will decline.

If we knew $v$, we would set the price as $v$, so that we can earn
as much money as possible. Unfortunately, we often do not know $v$.
But sometimes we know a probability distribution over $v$
(e.g., based on past data or experience),
and we want to maximize the expected value of our revenue.

Let us take an example.
Suppose $v$ is 2 with probability $1/3$ and 4 with probability $2/3$.

* If the price is more than 4, the buyer would not want to purchase, so our revenue would be $0$.
* If the price is at most 2, the buyer will definitely purchase, so our revenue would be $p$.
* If the price is more than 2 and at most 4, the buyer will purchase with probability $2/3$,
and our expected revenue would be $(2/3) \cdot p$.

If we set $p = 4$, our revenue would be $8/3$,
and it is easy to see that there is no other way to set the price $p$
such that the revenue is more than $8/3$.
Hence, $p = 2$ is the optimal price and the optimal expected revenue is $8/3$.

In general, our revenue is $p$ with probability $\Pr(v ≥ p)$
and $0$ with probability $\Pr(v < p)$.
Hence, the expected value of our revenue is $p \cdot \Pr(v ≥ p)$.
We should set $p$ to a value such that this expression is maximized.

## Truthful Single-Parameter Mechanisms

Now let's consider a totally different kind of mechanism, called a single-parameter mechanism.
We give the buyer $a(v)$ fraction of the good and charge them $r(v)$ dollars.
Here $a: \mathbb{R}_{≥ 0} \to [0, 1]$ is called the *allocation function*
and $r: \mathbb{R}_{≥ 0} \to \mathbb{R}_{≥ 0}$ is called the *revenue function*.
We require $r(0)$ to be 0.

Now you may wonder, "To charge them $r(v)$ dollars, we would need to know the value of $v$.
How would we know that?". That's a good question, but answering that is
beyond the scope of this article. If you're curious, read Tim Roughgarden's
lectures 3 and 5 on Algorithmic Game Theory <a href="#cite-tr20lec">[1]</a>.
For now, assume that we can know the value of $v$
if the mechanism $(a, r)$ is *truthful*, i.e.,
for every $0 ≤ x_1 < x_2$, we have
$$a(x_1) ≤ \frac{s(x_2) - s(x_1)}{x_2 - x_1} ≤ a(x_2),$$
where $s(x) \defeq xa(x) - r(x)$.

Observe that posted-price mechanisms can also be viewed as single-parameter mechanisms.
If the item has price $p$, then $a(v) = \boolone(v ≥ p)$ and $r(v) = p\boolone(v ≥ p)$.
(Here $\boolone(P)$ is defined to be 1 if proposition $P$ is true and 0 if $P$ is false.)
One can check that posted-price mechanisms are also truthful.

Now comes the main question:
**Are there truthful single-parameter mechanisms that can give us
a larger expected revenue than posted price mechanisms?**
In other words, we want to find a mechanism $(a, r)$ such that $\E(r(v))$ is maximized.
Here $v$ is a random variable from a known distribution.

## An Informal Solution

I'll first solve this problem without regards to mathematical rigor.
This will provide the necessary intuition.
We will then look at how to formalize these arguments,
and that's where things get really interesting if you like real analysis.

We first give a characterization of all truthful mechanisms.

<strong id="thm-truthful">Lemma 1</strong>:
Mechanism $(a, r)$ is truthful iff $a$ is non-decreasing
and $$r(x) = xa(x) - \int_0^x a(y)dy.$$

*Proof*. Suppose $(a, r)$ is truthful. Then, by definition, $a$ must be non-decreasing.
By making $x_2$ get arbitrarily close to $x_1$,
we get $s'(x_1) = a(x_1)$ (i.e., the derivative of $s$ at $x_1$ is $a(x_1)$).
$r(0) = 0$ implies $s(0) = 0$. Hence, $s(x) = \int_0^x a(y)dy$,
and so, $r(x) = xa(x) - \int_0^x a(y)dy$.

Now suppose $a$ is non-decreasing and $r(x) = xa(x) - \int_0^x a(y)dy$.
Then $s(x) = \int_0^x a(y)dy$, so for any $0 ≤ x_1 < x_2$, we get
$$s(x_2) - s(x_1) = \int_{x_1}^{x_2} a(x)dx ∈ [a(x_1)(x_2 - x_1), a(x_2)(x_2 - x_1)].
\quad \Box$$

Now let's compute the expected revenue.
Assume that the cumulative distribution of $v$ is $F$
and the probability density function of $v$ is $f$,
i.e., $F(x) \defeq \Pr(v ≤ x)$ and $f(x) \defeq dF(x)/dx$.

<strong id="thm-expected-revenue">Lemma 2</strong>:
The expected revenue of a truthful mechanism $(a, r)$ is
$$\int_0^∞ x(1-F(x))a'(x)dx.$$

*Proof*. First, using integration by parts, we get
$$\int_0^x ya'(y)dy = xa(x) - \int_0^x a(y)dy = r(x).$$
Then,
$$\begin{aligned}
\E(r(v)) &= \int_0^∞ \left(\int_0^u xa'(x)dx\right)f(u)du
\\ &= \int_0^∞ xa'(x) \left(\int_x^∞ f(u)du\right)dx
\\ &= \int_0^∞ xa'(x)(1-F(x)) dx.
\end{aligned}$$
(Here we swapped the integration order.) $\quad\Box$

<strong id="thm-revenue-max">Lemma 3</strong>:
$(a, r)$ is a revenue-maximizing truthful mechanism
iff $a(x) = \boolone(x ≥ p)$ and $r(x) = \boolone(x ≥ p)$,
where $p$ is the value for which $p(1-F(p))$ is maximum.

(Does this solution look familiar? This is exactly the posted-price mechanism at price $p$!
Hence, no truthful single-parameter mechanism does better than the best posted-price mechanism.)

*Proof*.
We need to find a non-decreasing allocation function $a$
for which $\int_0^∞ x(1-F(x))a'(x)dx$ is maximized.
This means $a'(x) ≥ 0$ for all $x$ and $\int_0^∞ a'(x)dx ≤ 1$.

This is similar to the problem where we are given a vector $b \in \mathbb{R}^n$
and we must find a vector $x \in \mathbb{R}_{≥ 0}^n$
such that $\sum_{i=1}^n x_i ≤ 1$ and $b^Tx$ is maximized.
The solution is to find the index $i^*$ at which $b$ is maximum,
i.e., $b_{i^*} ≥ b_i$ for all $i$, and then set $x_i = \boolone(i = i^*)$.
Then $b^Tx$ would equal $\max_{i=1}^n b_i$.

We just carry over this idea from sums to integrals.
We first find $p \in \mathbb{R}_{≥ 0}$ such that $p(1-F(p))$ is maximized.
Then we want to *concentrate all the mass* at $p$, i.e.,
$a'(p)$ is extremely large and $a'(x) = 0$ for all $x \neq p$.
This is the same as saying $a(x) = \boolone(x ≥ p)$.
Using <a href="#thm-truthful">Lemma 1</a>, we get $r(x) = xa(x) - \int_0^x a(y)dy = p\boolone(x ≥ p)$.
Then the pair $(a, r)$ gives us the maximum revenue
among all truthful single-parameter mechanisms. $\quad\Box$

Another result, which would be useful later, is that in truthful mechanisms,
the revenue function is non-decreasing.

<strong id="thm-revenue-nondec">Lemma 4</strong>:
If $(a, r)$ is a truthful mechanism, then $r(x)$ is non-decreasing in $x$.

*Proof*.
Since $(a, r)$ is truthful, for all $0 ≤ x_1 < x_2$, we get
$$a(x_1) ≤ \frac{s(x_2)-s(x_1)}{x_2-x_1} ≤ a(x_2)$$
$$\implies x_1(a(x_2)-a(x_1)) ≤ r(x_2) - r(x_1) ≤ x_2(a(x_2)-a(x_1)).$$
Since $a$ is non-decreasing in truthful mechanisms,
we get that $r(x_2) - r(x_1) ≥ 0$ for all $0 ≤ x_1 < x_2$.
Hence, $r$ is non-decreasing. $\quad\Box$

## Need for Mathematical Rigor

You may have noticed a lot of problems with the proofs above.

* In <a href="#thm-truthful">Lemma 1</a>'s proof, we assumed that $s'(x_1)$ is well-defined, i.e., $s$ is differentiable at $x_1$.
* In Lemmas <a href="#thm-expected-revenue">2</a> and <a href="#thm-revenue-max">3</a>, we assumed that $a$ is differentiable.
(But for posted-price mechanisms, we *know* that $a$ is not differentiable!)
* We assumed that $v$ is a continuous random variable.
What if $v$ is a discrete random variable, or it is neither discrete nor continuous?

Even though the above proofs are wrong, I think the facts are still true,
we just have to find proper proofs.

There is one more problems with the above proofs:
we need to define integration appropriately.

High school math generally defines integrals like this:
$\int_a^b f(x)dx$ is defined to be $F(b) - F(a)$,
where $F$ is the *anti-derivative* of $f$,
i.e., $F'(x) = f(x)$ for all $x \in [a, b]$.
But this definition is problematic.

For posted-price mechanisms, $a(x) = \boolone(x ≥ p)$.
To compute $r(x)$, we must find $\int_0^x a(y)dy$.
We can't use the high-school definition since there is no differentiable function
whose derivative at $y$ is $a(y)$ for all $y \in [0, x]$.
Intuitively, $\int_0^x a(y)dy$ should be $(x-p)\boolone(x ≥ p)$,
but this function is not differentiable at $p$
(the left derivative is 0 and the right derivative is 1).

We have used integrals extensively in the proofs above,
but for them to make sense, we must first define integration appropriately.
I had taken a course in real analysis at UIUC, so this wasn't hard for me:
one can just use Darboux integrals or Riemann integrals here,
and that would easily fix <a href="#thm-truthful">Lemma 1</a>.

But fixing Lemmas <a href="#thm-expected-revenue">2</a>
and <a href="#thm-revenue-max">3</a> is really tough.

## Preliminaries: sup and inf

If you have taken a course in real analysis, you can skip this section
(and maybe the next one too). Otherwise,
to understand the rest of the post, you must have a good grasp over
[infimum and supremum](https://en.wikipedia.org/wiki/Infimum_and_supremum),
which I will explain here.

Some sets do not have a minimum. E.g., the smallest element in
the interval $[3, 4]$ is 3, but $(3, 4]$ does not have a smallest element.
In situations where we require a set to have a minimum but it doesn't have one,
we can generally use the *infimum* instead.

Let $X \subseteq \mathbb{R}$ and $a \in \mathbb{R}$.
$a$ is called a *lower bound* on $X$ if $a ≤ x$ for all $x \in X$.
A number $b$ is called the *greatest lower bound* of $X$
(aka the *infimum* of $X$, denoted as $\inf(X)$)
if $b ≥ a$ for every lower bound $a$ of $X$.
E.g., the greatest lower bound of $(3, 4]$ is 3.

Does every set $X \subseteq \mathbb{R}$ have an infimum?
If $X$ is empty, then no. But what if $X$ is non-empty?
$X$ may not have any lower bound, e.g., the set $(-∞, 1]$.
In that case we say that $\inf(X) = -∞$.
But what if $X$ has a lower bound?
Then yes, $X$ always has an infimum, and this is an axiom of real numbers:
*If a non-empty set $X$ of real numbers has a lower bound, then it has a greatest lower bound.*

We can similarly define the least upper bound of $X$,
also called the *supremum* of $X$, denoted as $\sup(X)$.
If $X \neq \emptyset$, then $\sup(X)$ always exists:
$\sup(X) = ∞$ if $X$ has no upper bound, and $\sup(X)$ is a real number otherwise.

## Darboux Integrals and the Proof of Lemma 1

A standard way to define integration is through Darboux integrals.
You will find this in many textbooks and lecture notes on real analysis
<a href="#cite-dg-dbx">[2]</a>.

For any integer $n ≥ 0$, define $[n]$ as the set $\{1, 2, \ldots, n\}$.

**Definition 1** (Darboux integral):

* Let $f: [a, b] \to \mathbb{R}$ be a function.
* Let $P \defeq (x_0, x_1, \ldots, x_n)$ be a sequence of numbers
    where $a = x_0 < x_1 < \ldots < x_n = b$.
    The lower and upper *Darboux sums* of $f$ on $P$,
    denoted by $L_f(P)$ and $U_f(P)$, respectively, are defined as follows:
    If $a = b$, then $L_f(P) = U_f(P) = 0$. Otherwise,
    $$\begin{aligned}
    L_f(P) &\defeq \sum_{i=1}^n (x_i - x_{i-1})\left(\inf_{x \in [x_{i-1}, x_i]} f(x)\right),
    \\ U_f(P) &\defeq \sum_{i=1}^n (x_i - x_{i-1})\left(\sup_{x \in [x_{i-1}, x_i]} f(x)\right).
    \end{aligned}$$
* Let $\Pcal(a, b) \defeq \{(x_0, \ldots, x_n): n \in \mathbb{N}, a = x_0 < \ldots < x_n = b\}$.
    Then $\Pcal(a, b)$ is called the set of *partitions* of $[a, b]$.
* The lower and upper *Darboux integrals* of $f$ are
    $$\begin{aligned}
    L_f(a, b) &\defeq \sup_{P \in \Pcal(a, b)} L_f(P),
    \\ U_f(a, b) &\defeq \inf_{P \in \Pcal(a, b)} U_f(P).
    \end{aligned}$$
* If $L_f(a, b) = U_f(a, b)$, then $f$ is said to be
    *Darboux integrable* on $[a, b]$,
    and we denote $L_f(a, b)$ and $U_f(a, b)$ by $\int_a^b f(x)dx$ or $\int_a^b f$.

Here are some useful properties of Darboux integrals
of the function $f: [a, b] \to \mathbb{R}$.
Proofs can be found in standard texts on real analysis
(e.g., <a href="#cite-dg-dbx">[2]</a>).

1.  $U_f(a, b) ≥ L_f(a, b)$.
2.  For $a ≤ b ≤ c$, we have
    $L_f(a, b) = L_f(a, c) + L_f(c, b)$ and $U_f(a, b) = U_f(a, c) + U_f(c, b)$.
3.  Suppose $α ≤ f(x) ≤ β$ for all $x \in [a, b]$.
    Then $α(b-a) ≤ L_f(a, b) ≤ U_f(a, b) ≤ β(b-a)$.
4.  If $f$ is non-decreasing, then $f$ is integrable over $[a, b]$.

Armed with these results, we are ready to prove <a href="#thm-truthful">Lemma 1</a> rigorously.

*Proof of Lemma 1*.<br>
Suppose $a$ is non-decreasing and $r(x) = xa(x) - \int_0^x a(y)dy$ for all $x ≥ 0$.
We have to prove that $(a, r)$ is truthful.
For any $0 ≤ x_1 < x_2$, we get
$$\frac{s(x_2) - s(x_1)}{x_2 - x_1} = \frac{\int_{x_1}^{x_2} a(y)dy}{x_2 - x_1}
\in [a(x_1), a(x_2)].$$
Hence, $(a, r)$ is truthful.

Suppose $(a, r)$ is truthful. Then $a$ is non-decreasing,
and for all $0 ≤ y < z$, we have
$$a(y) ≤ \frac{s(z)-s(y)}{z-y} ≤ a(z),$$
where $s(x) \defeq xa(x) - r(x)$.

Pick any $t \in \mathbb{R}_{≥0}$. Let $P = (x_0, \ldots, x_n) \in \Pcal(0, t)$.
Then for all $i \in [n]$, we get
$$a(x_{i-1})(x_i - x_{i-1}) ≤ s(x_i)-s(x_{i-1}) ≤ a(x_i)(x_i - x_{i-1}).$$
Hence,
$$\begin{aligned}
L_a(P) &= \sum_{i=1}^n (x_i - x_{i-1})\left(\inf_{x \in [x_{i-1}, x_i]} a(x)\right)
\\ &= \sum_{i=1}^n (x_i - x_{i-1})a(x_{i-1})
\\ &= \sum_{i=1}^n (s(x_i) - s(x_{i-1})) = s(t) - s(0),
\end{aligned}$$
and
$$\begin{aligned}
U_a(P) &= \sum_{i=1}^n (x_i - x_{i-1})\left(\sup_{x \in [x_{i-1}, x_i]} a(x)\right)
\\ &= \sum_{i=1}^n (x_i - x_{i-1})a(x_i)
\\ &= \sum_{i=1}^n (s(x_i) - s(x_{i-1})) = s(t) - s(0).
\end{aligned}$$
Since $r(0) = 0$, we get $s(0) = 0$, and thus, $U_a(P) = L_a(P) = s(t)$.
Hence, $U_a(0, t) ≤ U_a(P) = s(t)$ and $L_a(0, t) ≥ L_a(P) = s(t)$.

Since $a$ is non-decreasing, $a$ is integrable over $[0, t]$,
and so, $U_a(0, t) = L_a(0, t) = s(t)$.
Hence, for any $x ≥ 0$, we have $r(x) = xa(x) - \int_0^x a(y)dy$.
$\quad\Box$

## The Weighted Darboux Integral

Proving <a href="#thm-expected-revenue">Lemma 2</a> is trickier.
We need to somehow deal with $a'(x)$ in the lemma statement.

My original idea was to modify the Darboux integral.
For any function $f: [a, b] \to \mathbb{R}$
and any non-decreasing function $W: [a, b] \to \mathbb{R}$,
to change $\int_a^b f(x)dx$ to $\int_a^b f(x)W'(x)dx$,
in $L_f(P)$ and $U_f(P)$, I changed $(x_i - x_{i-1})$ to $(W(x_i) - W(x_{i-1}))$.

I initially thought that I had come up with a nice generalization of Darboux integrals,
which I named *weighted Darboux integrals*,
but I later realized that this idea has been studied before by
<a href="https://en.wikipedia.org/wiki/Riemann%E2%80%93Stieltjes_integral">Riemann and Stieltjes</a>.

**Definition 2** (Weighted Darboux integral):

* Let $f, W: [a, b] \to \mathbb{R}$ be functions where $W$ is non-decreasing.
* Let $P \defeq (x_0, x_1, \ldots, x_n)$ where $a = x_0 < x_1 < \ldots < x_n = b$.
    Then the lower and upper *weighted Darboux sums* of $f$ on $P$ with weight $W$,
    denoted by $L_{f,W}(P)$ and $U_{f,W}(P)$, respectively, are defined as follows:
    If $a = b$, then $L_{f,W}(P) = U_{f,W}(P) = 0$. Otherwise,
    $$\begin{aligned}
    L_{f,W}(P) &\defeq \sum_{i=1}^n (W(x_i) - W(x_{i-1}))\left(\inf_{x \in (x_{i-1}, x_i)} f(x)\right),
    \\ U_{f,W}(P) &\defeq \sum_{i=1}^n (W(x_i) - W(x_{i-1}))\left(\sup_{x \in (x_{i-1}, x_i)} f(x)\right).
    \end{aligned}$$
* Let $\Pcal(a, b) \defeq \{(x_0, \ldots, x_n): n \in \mathbb{N}, a = x_0 < \ldots < x_n = b\}$.
    $\Pcal(a, b)$ is called the set of *partitions* of $[a, b]$.
* The lower and upper *weighted Darboux integrals* of $f$ with weight $W$ are
    $$\begin{aligned}
    L_{f,W}(a, b) &\defeq \sup_{P \in \Pcal(a, b)} L_{f,W}(P),
    \\ U_{f,W}(a, b) &\defeq \inf_{P \in \Pcal(a, b)} U_{f,W}(P).
    \end{aligned}$$
* If $L_{f,W}(a, b) = U_{f,W}(a, b)$, then $f$ is said to be
    $W$-<em>Darboux integrable</em> on $[a, b]$,
    and we denote $L_{f,W}(a, b)$ and $U_{f,W}(a, b)$ by $\int_a^b f(x)dW(x)$.
* When $W$ is the identity function, we write $L_f$ and $U_f$
    instead of $L_{f,W}$ and $U_{f,W}$, respectively.
    If $L_f(a, b) = U_f(a, b)$, we denote them by $\int_a^b f(x)dx$.

Once again, we can prove some simple properties
for $f, W: [a, b] \to \mathbb{R}$, where $W$ is non-decreasing:

1.  $U_{f,W}(a, b) ≥ L_{f,W}(a, b)$.
2.  For $a ≤ b ≤ c$, we have
    $L_{f,W}(a, b) = L_{f,W}(a, c) + L_{f,W}(c, b)$
    and $U_{f,W}(a, b) = U_{f,W}(a, c) + U_{f,W}(c, b)$.
3.  Suppose $α ≤ f(x) ≤ β$ for all $x \in [a, b]$.
    Then $α(W(b)-W(a)) ≤ L_{f,W}(a, b) ≤ U_{f,W}(a, b) ≤ β(W(b)-W(a))$.

Unfortunately, every non-decreasing function may not be integrable now
if the weight function $W$ is discontinuous.

<strong id="ex1">Example 1</strong>:

* Let $g(x) = 0$ for $x < 1/2$, $g(1/2) = 1/2$, and $g(x) = 1$ for $x > 1/2$.
* Let $W(x) = 0$ for $x < 1/2$ and $W(x) = 1$ for $x ≥ 1/2$.

Pick any partition $P = (x_0, \ldots, x_n) \in \Pcal(0, 1)$.
We now have two cases:

1.  $x_{i-1} < 1/2 < x_i$ for some $i$.
    Then $L_{g,W}(P) = 0$ and $U_{g,W}(P) = 1$.
2.  $x_i = 1/2$ for some $i$. Then $L_{g,W}(P) = 0$ and $U_{g,W}(P) = 1/2$.

Hence, $L_{g,W}(0, 1) = 0$ and $U_{g,W}(0, 1) = 1/2$,
so $g$ is not $W$-integrable over $[0, 1]$.

But why is this example concerning?
We can prove that if either $g$ or $W$ is continuous, and $g$ is non-decreasing,
then $g$ is $W$-integrable, so in <a href="#thm-truthful">Lemma 1</a>,
$\int_0^x a(y)dy$ is still well-defined.

However, I was thinking of using weighted Darboux integrals to define expected value.
For a positive random variable $X$ with cumulative distribution function $F$
(i.e., $F(x) \defeq \Pr(X ≤ x)$), one could define $\E(g(X))$ as
$$\lim_{T \to ∞} \int_0^T g(x)dF(x).$$

Let $X$ be a random variable that takes value $1/2$ with probability 1
(i.e., it's not random at all). Then its cumulative distribution function is $W$
from <a href="#ex1">Example 1</a>.
Then one would expect $\E(g(X))$ to equal $g(1/2)$, which is $1/2$,
but the integral defining $\E(g(X))$ doesn't exist by <a href="#ex1">Example 1</a>.

Also, in <a href="#thm-expected-revenue">Lemma 2</a>, I want the integral
$$\int_0^T x(1-F(x))da(x)$$
to exist for all $T ≥ 0$, but I can't think of a way of guaranteeing that
(unless we change the definition of weighted Darboux integrals.)

## A Second Attempt at Weighted Darboux Integrals

Let's try to define Darboux integrals again, but this time,
we will explicitly take discontinuities into account.

Let $f: [a, b] \to \mathbb{R}$ be a non-decreasing function.
For any $c \in (a, b]$, let $f^-(c) \defeq \sup_{x \in (a, c)} f(x)$,
and for any $c \in [a, b)$, let $f^+(c) \defeq \inf_{x \in (c, b)} f(x)$.

One can easily show that $f^+(c) ≥ f(c)$ for all $c \in [a, b)$,
$f^-(c) ≤ f(c)$ for all $c \in (a, b]$,
and $f^+(x_1) ≤ f((x_1+x_2)/2) ≤ f^-(x_2)$ for all $a ≤ x_1 < x_2 ≤ b$.

**Definition 3** (Jump-aware weighted Darboux integral):

* Let $f, W: [a, b] \to \mathbb{R}$ be functions where $W$ is non-decreasing.
* Let $P \defeq (x_0, x_1, \ldots, x_n)$ where $a = x_0 < x_1 < \ldots < x_n = b$.
    Then the jump, lower, and upper *weighted Darboux sums* of $f$ on $P$ with weight $W$,
    denoted by $J_{f,W}(P)$, $L_{f,W}(P)$, and $U_{f,W}(P)$, respectively,
    are defined as follows:
    If $a = b$, then $J_{f,W}(P) = L_{f,W}(P) = U_{f,W}(P) = 0$. Otherwise,
    $$\begin{aligned}
    J_{f,W}(P) &\defeq f(x_0)(W^+(x_0) - W(x_0))
        + \sum_{i=1}^{n-1} f(x_i)(W^+(x_i) - W^-(x_i))
        \\ &\quad + f(x_n)(W(x_n) - W^-(x_n)),
    \\ L_{f,W}(P) &\defeq J_{f,W}(P)
        + \sum_{i=1}^n (W^-(x_i) - W^+(x_{i-1}))\left(\inf_{x \in (x_{i-1}, x_i)} f(x)\right),
    \\ U_{f,W}(P) &\defeq J_{f,W}(P)
        + \sum_{i=1}^n (W^-(x_i) - W^+(x_{i-1}))\left(\sup_{x \in (x_{i-1}, x_i)} f(x)\right).
    \end{aligned}$$
* Let $\Pcal(a, b) \defeq \{(x_0, \ldots, x_n): n \in \mathbb{N}, a = x_0 < \ldots < x_n = b\}$.
    $\Pcal(a, b)$ is called the set of *partitions* of $[a, b]$.
    The lower and upper *weighted Darboux integrals* of $f$ with weight $W$ are
    $$\begin{aligned}
    L_{f,W}(a, b) &\defeq \sup_{P \in \Pcal(a, b)} L_{f,W}(P),
    & U_{f,W}(a, b) &\defeq \inf_{P \in \Pcal(a, b)} U_{f,W}(P).
    \end{aligned}$$
* If $L_{f,W}(a, b) = U_{f,W}(a, b)$, then $f$ is said to be
    $W$-*Darboux integrable* on $[a, b]$,
    and we denote $L_{f,W}(a, b)$ and $U_{f,W}(a, b)$ by $\int_a^b f(x)dW(x)$.

Most simple properties that one might expect weighted Darboux integrals to have,
the jump-aware weighted Darboux integrals have them too.
See my notes <a href="#cite-es-wdbx">[4]</a> for formal statements and proofs.

Additionally, one can show that all monotone functions are integrable in this model
<a href="#cite-es-wdbx">[4]</a>.
It also evaluates $\int_0^1 g(x)dW(x)$ as $1/2$ in <a href="#ex1">Example 1</a>.
So far, this new definition of weighted Darboux integrals seems to have
fixed the problems that the previous definition had.
Now let's get back to trying to formalize <a href="#thm-expected-revenue">Lemma 2</a>.

## Formalizing Lemma 2

First, let's show that integration by parts holds in our model,
because we use it in the first step of our proof.
We would like to show that for two non-decreasing functions
$f, g: [a, b] \to \mathbb{R}$, we have
$$\int_a^b f(x)dg(x) + \int_a^b g(x)df(x) = f(b)g(b) - f(a)g(a).$$
Unfortunately, this isn't true, even when $f = g$.

<strong id="ex2">Example 2</strong>:
Let $g(x) = 0$ if $x < 1/2$, $g(1/2) = 1/5$, and $g(x) = 1$ for $x > 1/2$.
Then one can show that $\int_0^1 g(x)dg(x) = 1/5$,
but $2/5 = 2\int_0^1 g(x)dg(x) ≠ g(1)^2 - g(0)^2 = 1$.

Fortunately, I could prove that integration by parts holds if
either $f$ or $g$ is continuous <a href="#cite-es-wdbx">[4]</a>.
And in [Lemma 2](#thm-expected-revenue), we apply integration by parts on $x$ and $a(x)$,
and $x$ is continuous. So things still work out (for now),
and we get that $r(x) = \int_0^y yda(y)$ for all $x \ge 0$.

First, we would like to ensure that $\E(r(v))$ is well-defined.
Or at least, we want to ensure that $\int_0^T r(x)dF(x)$ exists for all $T ≥ 0$,
where $F$ is the cumulative distribution function of $v$.
This integral exists since $r$ is non-decreasing by [Lemma 4](#thm-revenue-nondec).

Next, I wanted to prove that we can exchange the order of integration.
But I couldn't prove it.

And then it struck me; [Lemma 2](#thm-expected-revenue) is wrong!
Consider posted price mechanisms. There, the expected revenue is $p\Pr(v ≥ p)$.
But for all $T > p$, $\int_0^T x(1-F(x))da(x)$ evaluates to $p(1-F(p)) = p\Pr(v > p)$.
Maybe we should use $x(1-G(x))$ instead of $x(1-F(x))$
in [Lemma 2](#thm-expected-revenue)'s statement, where $G(x) \defeq \Pr(v < x)$?
(Note that $G(x) = F^-(x)$ for all $x > 0$ and $G^+(x) = F(x)$ for all $x ≥ 0$.
$G(0) = 0$, but $F^-(0)$ is not defined.)

I discovered an edge case that was spoiling the definition of expected value.
For a positive random variable $X$, defining $\E(g(X))$ as
$\lim_{T \to ∞} \int_0^T g(x)dF(x)$, where $F(x) \defeq \Pr(X ≤ x)$ seems to work fine,
but if $X$ is non-negative, and can take a value of 0 with positive probability,
then this definition doesn't work.
We can fix it by adding the term $F(0)g(0)$ to the integral,
or we can define $\E(g(X))$ as
$\lim_{T \to ∞} \int_0^T g(x)dG(x)$, where $G(x) \defeq \Pr(X < x)$.

With these fixes, [Lemma 2](#thm-expected-revenue) seems to be true for posted price mechanisms,
i.e., for $a(x) = \boolone(x ≥ p)$ and $r(x) = p\boolone(x ≥ p)$,
we get $\E(r(v)) = p\Pr(v ≥ p)$ and $\int_0^T x(1-G(x))da(x) = p\Pr(v ≥ p)$ for all $T > p$.

However, [Lemma 2](#thm-expected-revenue) is still wrong.
Consider a different mechanism: for any $p, γ \in (0, 1)$, define
$$a(x) = \begin{cases}0 & x < p \\ γ & x = p \\ 1 & x > p\end{cases}.$$
Then
$$r(x) = \begin{cases}0 & x < p \\ pγ & x = p \\ p & x > p\end{cases}.$$
Suppose $v$ is $p$ with probability 1. Then $\E(r(v)) = pγ$.
However, for any function $h: \mathbb{R}_{≥0} \to \mathbb{R}$ and any $T ≥ 1$,
we have $\int_0^T h(x)da(x) = h(p)$.
For this integral to equal $\E(r(v))$, we must have $h(p) = pγ$.
Hence, we cannot have $h(x)$ be $x(1-F(x))$ or $x(1-G(x))$
or anything independent of $a(x)$.

## Fixing Lemma 2

We will soon see that [Lemma 2](#thm-expected-revenue) doesn't hold only if
$a^+(x) > a(x)$ for some $x ≥ 0$.

Let $(a, r)$ be a truthful mechanism.
Then $a$ is non-decreasing and $r(x) = xa(x) - \int_0^x a(y)dy$ for all $x ≥ 0$
by [Lemma 1](#thm-truthful).
Let $b = a^+$ be a different allocation function.
Note that $b$ is also non-decreasing.
Let $\rhat(x) = xb(x) - \int_0^x b(y)dy$ for all $x \ge 0$.
Then $(b, \rhat)$ is also a truthful mechanism by [Lemma 1](#thm-truthful).

<strong id="thm-hat-dom">Lemma 5</strong>:
$\rhat(x) ≥ r(x)$ for all $x ≥ 0$.

*Proof*. $\rhat(x) - r(x) = x(b(x)-a(x)) - \int_0^x y(b(y)-a(y))dy$.
Let $g(x) \defeq x(b(x) - a(x))$ for all $x ≥ 0$.
We will show that $U_g(0, T) ≤ 0$ for all $T ≥ 0$, which would complete the proof.

Pick any $n \ge 1$. Let $x_i = T(i/n)$ for $0 ≤ i ≤ n$.
Then $P = (x_0, \ldots, x_n) \in \Pcal(0, T)$, and
$$\begin{aligned}
U_g(P) &= \sum_{i=1}^n (x_i - x_{i-1})\left(\sup_{x \in (x_{i-1}, x_i)} y(b(y)-a(y))\right)
\\ &\le (T^2/n)\sum_{i=1}^n \sup_{x \in (x_{i-1}, x_i)} (b(y)-a(y))
\\ &\le (T^2/n)\sum_{i=1}^n (b(x_i)-a^+(x_{i-1}))
\\ &= (T^2/n)(a^+(T) - a^+(0)).
\end{aligned}$$
By making $n$ arbitrarily large, we can make $U_g(P)$ infinitesimally small.
Hence, $U_g(0, T) = \inf_{P \in \Pcal(0, T)} U_g(P) ≤ 0$.
Hence, $\rhat(x) ≥ r(x)$ for all $x ≥ 0$. $\quad\Box$

<strong id="thm-plus-plus">Lemma 6</strong>:
Let $f: \mathbb{R}_{≥0} \to \mathbb{R}$ and let $g = f^+$.
Then $g$ is right-continuous, i.e., $g^+(c) = g(c)$ for all $c ≥ 0$.

*Proof*.
Pick any $ε > 0$. Then $\exists z \in (c, b)$ such that $f(z) < f^+(c) + ε$.
Now, $g(c) ≤ g^+(c) ≤ g((c+z)/2) = f^+((c + z)/2) ≤ f(z) < f^+(c) + ε = g(c) + ε$.
Since we can make $ε$ as small as we want, we get $g^+(c) = g(c)$. $\quad\Box$

Lemmas [5](#thm-hat-dom) and [6](#thm-plus-plus) tell us that
for every allocation function, there is a right-continuous allocation function
whose revenue is greater or equal.
Hence, from now on, we assume that the allocation function is right-continuous.

In my notes <a href="#cite-es-wdbx">[4]</a>,
I prove that the product of two bounded integrable functions is also integrable.
Moreover, I prove the following result, that helps us do double integration.

<strong id="thm-dbl-integration">Lemma 7</strong>:
Let $V, W: [a, b] \to \mathbb{R}$ be non-decreasing functions
and $V$ be right continuous, i.e., $V^+(x) = V(x)$ for all $x \in [a, b)$.
Let $f: [a, b] \to [0, M]$ for some $M \in \mathbb{R}_{\ge 0}$
such that $L_{f,V}(a, b) = U_{f,V}(a, b)$.
Let $r: [a, b] \to \mathbb{R}_{\ge 0}$, where
$r(x) \defeq \int_a^x f(y)dV(y)$.
(Then $r$ is monotonic by $f$'s non-negativity,
so $r$ is $W$-integrable over $[a, b]$.)

Let $h(x) \defeq f(x)(W(b)-W^-(x))$ for all $x \in (a, b]$,
and let $h(a) \defeq f(x)(W(b)-W(a))$.
(Then $h$ is $V$-integrable over $[a, b]$,
since $f$ is $V$-integrable and $W$ is non-increasing.)
Then $\int_a^b r(x)dW(x) = \int_a^b h(x)dV(x)$.

Using [Lemma 7](#thm-dbl-integration),
we get that if $(a, r)$ is truthful and $a$ is right-continuous,
then the expected revenue is
$$\E(r(v)) = \sup_{T \ge 0} \int_0^T r(x)dF(x)
= \sup_{T \ge 0} \int_0^T x(F(T)-F^-(x))da(x).$$
(Recall that $F$ is the cumulative distribution function of $v$.)
Hence, [Lemma 2](#thm-expected-revenue) holds after slight modification.

## Lemma 3

Let's now get to [Lemma 3](#thm-revenue-max).

Define $r_{\max} \defeq \sup_{p \ge 0} p(1-F^-(p))$.
Then for any truthful mechanism $(a, r)$ where $a$ is right-continuous, we get
$$\begin{aligned}
\E(r(v)) &= \sup_{T \ge 0} \int_0^T x(F(T)-F^-(x))da(x)
\le \sup_{T \ge 0} \int_0^T r_{\max}da(x)
\\ &= \sup_{T \ge 0} r_{\max}(a(T)-a(0)) \le r_{\max}.
\end{aligned}$$

Hence, the expected revenue of any truthful mechanism is at most $r_{\max}$.
Moreover, if $(a, r)$ is the posted-price mechanism with price $p$,
then $\E(r(v)) = p(1-F^-(p))$, so the maximum revenue we can get
using posted-price mechanisms is $r_{\max}$.
Hence, posted-price mechanisms are optimal.

## Conclusion

This took several days to figure out and almost drove me mad.
The informal proof is so simple, yet the formal proof is so long
and requires deep insight into real analysis.

## References

<ol>
<li class="citation" id="cite-tr20lec">
<span class="cite-authors"><a href="https://timroughgarden.org/">Tim Roughgarden</a>.</span>
<span class="cite-title">
<a href="https://www.cambridge.org/us/universitypress/subjects/computer-science/algorithmics-complexity-computer-algebra-and-computational-g/twenty-lectures-algorithmic-game-theory">
Twenty Lectures on Algorithmic Game Theory.</a></span>
<br>
<span class="cite-source">Cambridge University Press,</span>
<span class="cite-year">2016,</span>
<span class="cite-isbn">ISBN: 9781316781173.</span>
<br>
<span class="cite-note">Link to free versions:
<ul>
<li><a href="https://timroughgarden.org/f13/l/l1.pdf">Lecture 1: Introduction and Examples</a></li>
<li><a href="https://timroughgarden.org/f13/l/l2.pdf">Lecture 2: Mechanism Design Basics</a></li>
<li><a href="https://timroughgarden.org/f13/l/l3.pdf">Lecture 3: Myerson's Lemma</a></li>
<li><a href="https://timroughgarden.org/f13/l/l4.pdf">Lecture 4: Algorithmic Mechanism Design</a></li>
<li><a href="https://timroughgarden.org/f13/l/l5.pdf">Lecture 5: Revenue-Maximizing Auctions</a></li>
<li><a href="https://timroughgarden.org/f13/l/l6.pdf">Lecture 6: Simple Near-Optimal Auctions</a></li>
</ul>
</span>
</li>
<li class="citation" id="cite-dg-dbx">
<span class="cite-authors"><a href="https://www3.nd.edu/~dgalvin1/">David Galvin</a>.</span>
<span class="cite-title">
<a href="https://www3.nd.edu/~dgalvin1/10860/10860_S20/">
Section 10: The Darboux Integral.</a></span>
<br>
<span class="cite-source">Lecture notes for Math 10860 (Honors Calculus II)
at the University of Notre Dame,</span>
<span class="cite-year">Spring 2020.</span>
</li>
<li class="citation" id="cite-jf-rv2">
<span class="cite-authors"><a href="https://personal.math.ubc.ca/~feldman/">Joel Feldman</a>.</span>
<span class="cite-title">
<a href="https://personal.math.ubc.ca/~feldman/m321/">
Lecture notes for Math 321 (Real Variables II)</a>,</span>
<br>
<span class="cite-source">University of British Columbia,</span>
<span class="cite-year">2016.</span>
</li>
<li class="citation" id="cite-es-wdbx">
<span class="cite-authors"><a href="https://sharmaeklavya2.github.io/">Eklavya Sharma</a>.</span>
<span class="cite-title">
<a href="https://sharmaeklavya2.github.io/notes/math/wdbx-integral.pdf">
My notes on weighted Darboux integrals</a>.</span>
</li>
</ol>
