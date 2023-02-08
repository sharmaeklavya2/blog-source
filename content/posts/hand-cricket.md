title: Hand Cricket: A Game Theoretic Perspective
slug: hand-cricket
tags: Math
date: 2023-02-07
mathengine: katex-full
summary: Hand cricket is a popular game among Indian children. Here I try to analyze hand cricket from the perspective of non-cooperative game theory.


$$@
\def\simplex{\mathbb{S}}
$$

*Hand cricket*, also known as *Odd or Even*, is a popular two-player game among Indian children.
It is a hand game, i.e., the game is played using hand gestures, similar to rock-paper-scissors.
As the name suggests, hand cricket is inspired by [Cricket](https://en.wikipedia.org/wiki/Cricket).
An informal description of hand cricket can be found on
[this instructibles page](https://www.instructables.com/How-to-Play-Hand-Cricket/),
or on [this iOS app's website](https://theshubhamarya.github.io/HandCricket/).

I used to play hand cricket a lot in childhood.
But back then it never occurred to me that maybe I can use math to figure out how to play this game well.
I searched the internet to see if anyone has analyzed this game already,
but I didn't come across anything.
This game doesn't even have a proper wikipedia page!
This is a shame. We must fix this by giving it the mathematical treatment it deserves.

In this article, I formally define the game and the associated mathematical problem.
I haven't yet succeeded in solving the problem. I've written down the progress I made.
I have never formally studied game theory, so perhaps I'm just ill-equipped to solve it.

## Formal Description of the Game

Hand cricket is a two-player game.
The game is parametrized by a triple $(S, W, B)$.
$S \defeq [s_1, s_2, \ldots, s_n]$ is a sequence of non-negative real numbers, called the *score vector*.
$W \in \mathbb{Z}_{\ge 1}$ is called the *number of wickets*.
$B \in \mathbb{Z}_{\ge 1} \cup \{\infty\}$ is called the *number of bowls*.
Usually, hand cricket is played with $W = 1$, $B = \infty$, and $s_i = i$.

The game consists of two halves, called *innings*.
In the first inning, one of the players is a *batter* and the other is the *bowler*.
In the second inning, they switch their roles, i.e.,
the batter becomes the bowler and the bowler becomes the batter.
Which among the two players get to bat in the first inning is often decided
using a random protocol, called the *toss*.
For the sake of brevity, I won't describe the toss here.
Instead, let us assume that the choice is made uniformly randomly.

The *state* of an inning is denoted by the tuple $(b, s, w)$, where
$b$ is called the *number of remaining bowls*,
$s$ is called the *batter's score*,
and $w$ is called the *number of remaining wickets*.
At the beginning of each inning, the state is $(B, 0, W)$.

In each inning, the batter and the bowler repeatedly make simultaneous moves
(called *bowls* in cricket terminology) as long as $b$ and $w$ are positive.
In each move, each player selects a number from $1$ to $n$.
Suppose the batter selects $i$ and the bowler selects $j$.
Then the state changes as follows:

$$(b, s, w) \to \begin{cases}(b-1, s+s_i, w) & \textrm{ if } i \neq j
\\ (b-1, s, w-1) & \textrm{ if } i = j \end{cases}.$$

(I use the convention that $\infty - 1$ is $\infty$.)
The event $i = j$ is called *bowling out*.
The inning ends when either $b$ or $w$ becomes 0.
When an inning ends at state $(b, s, w)$, the batter gets a score of $s$.
After both innings, the player with a larger score wins.
If both players have the same score, it's a tie.

## Preliminaries

For any positive integer $n$, let $[n] \defeq \{1, 2, \ldots, n\}$
and $\simplex_n \defeq \{x \in \mathbb{R}_{\ge 0}^n: \sum_{i=1}^n x_i = 1\}$.

We can assume that all entries in the score vector are positive,
since it doesn't make sense for a batter to play a move that gives zero score.
(Nevertheless, I have seen variants of hand cricket being played by little children
where they sometimes play zero-score moves.)

## Maximizing Expected Score for $B = \infty$

Let us look at a variant of the game where there is just one inning,
and it has already been decided which player will be the batter.
The batter wants to maximize their expected score and the bowler wants to minimize it.
Let us restrict our attention to the special case where $B = \infty$.
Let us name this game *infinite ESM hand cricket*,
where ESM abbreviates Expected Score Maximization.

Infinite ESM hand cricket intuitively seems to be a reasonable surrogate
to the first inning when $B = \infty$.
(By contrast, in the second inning, the batter wants to maximize the probability
of scoring more than a given target.)

**Definition**:
Let $x \in \simplex_n$. Then the *memoryless strategy* $x$ is this:
make each move independently, and in each move pick $i$ with probability $x_i$.

Suppose the batter and bowler commit to playing memoryless strategies only.
We want to analyze how they should pick their strategies.
Let $e(x, y)$ be the batter's expected total score
when the batter plays strategy $x$ and the bowler plays strategy $y$,
where $x, y \in \simplex_n$.

**Lemma**:
If $x^Ty = 0$, then $e(x, y) = \infty$. Otherwise,
$\displaystyle e(x, y) = W\frac{\sum_{i=1}^n s_ix_i(1-y_i)}{x^Ty}$.

*Proof*.
$x^Ty = 0$ iff $x$ and $y$ have disjoint supports.
Hence, if $x^Ty = 0$, then the batter can never be bowled out
and will keep scoring indefinitely, which gives $e(x, y) = \infty$.

In the first move, let $I$ and $J$ be the numbers picked by the batter and the bowler, respectively.
Then $I$ and $J$ are multinoulli random variables.
For any integer $k \in [W]$, let $Z_k$ be the random variable denoting
the batter's total score after they have been bowled out $k$ times.
Then for any $k \in [W] - \{1\}$, $Z_k - Z_{k-1}$ has the same distribution as $Z_1$.
Hence, $e(x, y) = \E(Z_W) = W\E(Z_1)$ by linearity of expectation.

$$\begin{aligned}
\E(Z_1) &= \sum_{i=1}^n \E(Z_1 \mid I=i \land J\neq i)\Pr(I=i \land J\neq i)
\\ &= \sum_{i=1}^n (s_i + \E(Z_1))x_i(1-y_i)
\\ &= \sum_{i=1}^n s_ix_i(1-y_i) + \E(Z_1)(1 - x^Ty).
\end{aligned}$$
Hence, $\E(Z_1) = \left(\sum_{i=1}^n s_ix_i(1-y_i)\right)/x^Ty$.
$\quad\Box$

Since $e(x, y)$ is proportional to $W$, we can assume without loss of generality that $W = 1$.

**Open Problem**:
Does infinite ESM hand cricket have a Nash equilibrium
where both players use a memoryless strategy?
If yes, can we compute it or get a closed-form expression for it?
Is the Nash equilibrium unique? If no, which one is *better*?

<span class="danger">I don't know how to solve this problem.</span>
Any help would be appreciated!

Intuitively, it seems to me that studying memoryless strategies is enough,
i.e., other strategies can't possibly do better.
But I don't know how to prove it.
