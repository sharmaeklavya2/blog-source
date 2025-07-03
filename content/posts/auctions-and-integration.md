title: Pricing Mechanisms and the Riemann-Stieltjes Integral
slug: auctions-and-integration
tags: Math
date: 2025-07-01
mathengine: katex-full
summary: While studying pricing mechanisms, trying to formalize simple results led me down the rabbit hole of Riemann-Stieltjes integrals.


$$@
\def\Pcal{\mathcal{P}}
$$

Imagine we are trying to sell a sack of rice. We want to make as much money from this sale as possible. What should we do? This is an important problem in the field of *mechanism design*, which is a part of *game theory*. I was studying this problem in a very simple setting, and came across some very interesting math while doing so. In this article, I will share my mathematical journey. I won't talk much about the *mechanism design* part to keep this article accessible to a broad audience.

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

But fixing Lemmas <a href="#thm-expected-revenue">2</a> and <a href="#thm-revenue-max">3</a> is tough.
I still haven't been able to do it.
I'll talk about the approaches I tried and why they didn't work.

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
$X$ may not have any lower bound, e.g., the set $(-\infty, 1]$.
In that case we say that $\inf(X) = -\infty$.
But what if $X$ has a lower bound?
Then yes, $X$ always has an infimum, and this is an axiom of real numbers:
*If a non-empty set $X$ of real numbers has a lower bound, then it has a greatest lower bound.*

We can similarly define the least upper bound of $X$,
also called the *supremum* of $X$, denoted as $\sup(X)$.
If $X \neq \emptyset$, then $\sup(X)$ always exists:
$\sup(X) = \infty$ if $X$ has no upper bound, and $\sup(X)$ is a real number otherwise.

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
Suppose $a$ is non-decreasing and $r(x) = xa(x) - \int_0^x a(y)dy$ for all $x \ge 0$.
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
Hence, for any $x \ge 0$, we have $r(x) = xa(x) - \int_0^x a(y)dy$.
$\quad\Box$

## The Weighted Darboux Integral

Proving <a href="#thm-expected-revenue">Lemma 2</a> is trickier.
We need to somehow deal with $a'(x)$ in the lemma statement.

My original idea was to modify the Darboux integral.
For any function $f: [a, b] \to \mathbb{R}$
and any non-decreasing function $W: [a, b] \to \mathbb{R}$,
to change $\int_a^b f(x)dx$ to $\int_a^b f(x)d'W(x)dx$,
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
    L_{f,W}(a, b) &\defeq \sup_{P \in \Pcal(a, b)} L_{f,W}(P)
    \\ U_{f,W}(a, b) &\defeq \inf_{P \in \Pcal(a, b)} U_{f,W}(P)
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
For a non-negative random variable $X$ with cumulative distribution function $F$
(i.e., $F(x) \defeq \Pr(X \le x)$), one could define $\E(g(X))$ as
$$\lim_{T \to \infty} \int_0^T g(x)dF(x).$$

Let $X$ be a random variable that takes value $1/2$ with probability 1
(i.e., it's not random at all). Then its cumulative distribution function is $W$
from <a href="#ex1">Example 1</a>.
Then one would expect $\E(g(X))$ to equal $g(1/2)$, which is $1/2$,
but the integral defining $\E(g(X))$ doesn't exist by <a href="#ex1">Example 1</a>.

Also, in <a href="#thm-expected-revenue">Lemma 2</a>, I want the integral
$$\int_0^T x(1-F(x))da(x)$$
to exist for all $T \ge 0$, but I can't think of a way of guaranteeing that
(unless we change the definition of weighted Darboux integrals.)

## Conclusion

Well, there's not much to conclude, really.
I tried to formalize a proof, and haven't been able to do so.
Reach out to me if you know how to do this.

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
</ol>
