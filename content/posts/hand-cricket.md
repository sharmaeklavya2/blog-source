title: Analyzing Hand Cricket using Game Theory
slug: hand-cricket
tags: Math, Game theory
date: 2023-02-07
modified: 2023-10-09
mathengine: katex-full
summary: Hand cricket is a popular game among children in India. I analyzed it using game theory and got my findings published at FSTTCS, a well-known CS theory conference!


$$@
\def\simplex{\Delta}
$$

*Hand cricket*, also known as *Odd or Even*, is a popular two-player game among children in India.
It is a hand game, i.e., the game is played using hand gestures, similar to rock-paper-scissors.
As the name suggests, hand cricket is inspired by [Cricket](https://en.wikipedia.org/wiki/Cricket).

I used to play hand cricket a lot in childhood: an estimated 300 hours in total.
But back then it never occurred to me that maybe I can use math to figure out how to play this game well.
I searched the internet to see if anyone has analyzed this game already,
but I didn't come across anything.
This game doesn't even have a Wikipedia page! This is a shame.
I decided to help fix this by giving it the attention it deserves,
at least from the game theory research community.

I and my friend [Aniket Murhekar](https://aniket2.web.illinois.edu/) showed that
(a generalization of) hand cricket has a unique Nash equilibrium.
We got this result published at [FSTTCS](https://www.fsttcs.org.in)!
Link to research paper: [arXiv:2309.15870](https://arxiv.org/abs/2309.15870).

## Description of the Game

An informal description of hand cricket can be found on
[this instructibles page](https://www.instructables.com/How-to-Play-Hand-Cricket/),
or on [this iOS app's website](https://theshubhamarya.github.io/HandCricket/).
Here I describe it formally to make it amenable to mathematical analysis.

Hand cricket is a game played by two players: a *batter* and a *bowler*.
The game is parametrized by a sequence $S \defeq [s_1, s_2, \ldots, s_n]$
of non-negative real numbers, called the *score vector*.

The game consists of multiple rounds (called *bowls* in cricket terminology).
In each round, the batter and the bowler simultaneously pick a number from $1$ to $n$.
Suppose the batter selects $i$ and the bowler selects $j$.
If $i = j$ (called *collision* or *bowling out*),
the game ends and no more rounds are played.
Otherwise, if $i \neq j$, then the game proceeds to the next round.

In each round, if the batter picks action $i$, then she scores $s_i$ points.
The batter wants to maximize her total score and the bowler wants to minimize it.

I had come across variants of this game in childhood. I won't discuss them here,
but our research paper mentions them. In fact, in our paper,
we solve a generalization of this game that captures all variants I know of.

## Results

Each player would have to play randomly, otherwise her opponent may be able to
find out her strategy and defeat her.

We showed that a Nash equilibrium always exists for this game, and there is only one Nash equilibrium.
Basically, this means that there is a unique pair $(x, y)$ of randomized strategies
and a number $\rho$ such that:

1.  If the batter uses strategy $x$, then the expected value of the total score is at least $\rho$,
    regardless of what strategy the bowler uses.
2.  If the batter doesn't use strategy $x$, then it's possible for the bowler to use a strategy
    that gives expected total score less than $\rho$.
3.  If the bowler uses strategy $y$, then the expected value of the total score is at most $\rho$,
    regardless of what strategy the batter uses.
4.  If the bowler doesn't use strategy $y$, then it's possible for the batter to use a strategy
    that gives expected total score more than $\rho$.

Moreover, the Nash equilibrium is given by eigenvectors of an appropriate matrix,
and we give an efficient algorithm to compute the Nash equilibrium.

## How popular is hand cricket?

Hand cricket was very popular at my school (in Delhi).
Later I found that many of my friends, from all around India, have played hand cricket.

I decided to look more into this. I posted a survey on two WhatsApp groups I was part of,
and here are the results:

1.  BITS Pilani CS undergrads (96 students, 30 responded, 56 didn't respond):
    1.  Have played it: 27
    2.  Have heard of it but not played it: 1
    3.  Never heard of it: 2
2.  UIUC Fall 2021 grad students (245 students, 29 responded, 216 didn't respond):
    1.  Have played it: 26
    2.  Have heard of it but not played it: 1
    3.  Never heard of it: 2

## How this project started

I started working on this problem in January 2023 as a hobby project.
Then I told Aniket about it and we started working together.

I was taking the course [CS 598 TH1](https://courses.illinois.edu/schedule/2023/spring/CS/598)
(Recent Advances in Theoretical Computer Science) in spring 2023, where I had to do a research project.
I and Aniket teamed up for the project and we were thinking of working on a variant of bin packing.
Obviously, I wasn't going to suggest hand cricket as a course project, because it seemed too
silly for *actual* research (and also it didn't fit the theme of the course).
But I was forced to do so when the deadline was close enough
and we hadn't done anything for the course project.
Hand cricket didn't seem as silly at that point, since by then we had
generalized our hand cricket results to arbitrary payoff matrices.
The course instructor, Prof. Ruta Mehta, accepted it, and I got to work on it as part of the course!
She seemed happy with our results, and she suggested that we may be able to
publish our results in some *okayish* (paraphrased) conference if we could improve them a bit.

I continued working on hand cricket during the summer.
It turned out to be a very interesting problem with beautiful math underneath.
We submitted it to FSTTCS. I guessed FSTTCS would be more likely to have Indian reviewers,
so they may care about hand cricket more.
We used standard game-theoretic terminology in our paper instead of cricket terminology,
though we did mention hand cricket as one of the main applications.
Even our title had nothing to do with hand cricket:
'Nash Equilibrium of Two-Player Matrix Games Repeated Until Collision'.
The paper was accepted and the reviews were good.
None of the reviewers mentioned hand cricket, which I have mixed feelings about:

1.  How can they not know about such a popular game?!
2.  They liked our paper despite no apparent interest in hand cricket!

I enjoyed working on this problem a lot. Aniket has been an awesome collaborator.
I'm grateful to Prof. Ruta Mehta for forcing me to work on something other than fair division,
being supportive of my foray into hand cricket, and reviewing our manuscript.
My advisor, Prof. Jugal Garg, also offered valuable comments on our manuscript.
