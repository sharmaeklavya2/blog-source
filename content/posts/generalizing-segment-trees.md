title: Generalizing Segment Trees
slug: generalizing-segment-trees
tags: CS, Algorithms, Math, Abstract Algebra
date: 2019-07-20
mathengine: mathjax
ExtraCSS: css/collapsible.css
summary: Generalizing segment trees by expressing range query outputs as elements of a monoid and update operations as endomorphisms.


A segment tree is a data structure which stores an array of size $n$
and allows $O(\log{n})$-time range queries and $O(\log n)$-time range updates on it.
I devised a method of generalizing segment trees using
concepts from abstract algebra: monoids and endomorphisms.
This generalization not only gave me conceptual clarity
but also allowed me to write a
[segment tree C++ library](https://gist.github.com/sharmaeklavya2/99ed35efbb639bbe7d7b46b89b74fea0)
that can be used for any application without modifying the code for queries and updates.

This blog post explains what monoids and endomorphisms are,
and the intuition which led me to use these abstractions to generalize segment trees.
I will also explain how to perform range updates using lazy propagation.

Prerequisite concepts for this blog post:

* What a segment tree is.
* How to build a segment tree.
* How to perform range queries on a segment tree.
* How to perform point updates on a segment tree.

You can read about the above prerequisite concepts in the
[article on Segment Trees by codelucid](https://codelucid.wordpress.com/2015/05/27/segment-trees/).

[TOC]


## Generalizing problems

Before we generalize segment trees, let's try to generalize some simple problems
which can be solved using segment trees. These example problems are used throughout this article.

1.  **Problem SUMREPL**:
    You are given an array $a$ of $n$ numbers, indexed from 0 to $n-1$.
    You will be asked to perform $q$ operations. Each operation will be one of the following:
    * given $l$ and $r$, output $\sum_{i=l}^r a[i]$.
    * given $l$, $r$ and $y$, replace $a[i]$ by $y$ for all $l \le i \le r$.

2.  **Problem MINMAX**:
    You are given an array $a$ of $n$ numbers, indexed from 0 to $n-1$.
    You will be asked to perform $q$ operations. Each operation will be one of the following:
    * given $l$ and $r$, output $\min_{i=l}^r a[i]$.
    * given $l$ and $r$, output $\max_{i=l}^r a[i]$.
    * given $l$, $r$ and $y$, add $y$ to $a[i]$ for all $l \le i \le r$.
    * given $l$, $r$ and $z$, multiply $a[i]$ by $z$ for all $l \le i \le r$.

3.  **Problem CHAROCC**:
    You are given an array $a$ of $n$ strings, indexed from 0 to $n-1$.
    Each string consists of lowercase English characters (`a` to `z`).
    The sum of the lengths of the strings is $m$.
    You will be asked to perform $q$ operations. Each operation will be one of the following:
    * given integers $l$ and $r$ and character $c$, output the number of
        occurrences of $c$ in the concatenation of $a[l], a[l+1], \ldots, a[r]$.
    * given integers $l$ and $r$ and character $c$, append $c$ to $a[i]$ for all $l \le i \le r$.
        For example, if $a[i]$ is `"car"` and $c$ is `'t'`, then $a[i]$ should be changed to `"cart"`.

You can see that in all these problems, we are given an array of size $n$.
The elements of the array can be anything: numbers, strings or something else.
In these examples, there are 2 kinds of operations - queries and updates.
In all operations, we're asked to operate on a subarray $b = a[l..r]$.
We'll generalize these operations to 2 concepts - query function and update function.

### Query function

In queries, we're asked to apply a function $f$ on $b$.
We'll call this function the 'query function'.
In SUMREPL, this function is summation: $f(b) = \sum_{x \in b} x$.

In MINMAX, the query function is 'min' for some queries and 'max' for others.
Instead, we can use the query function
$f(b) = (\min_{x \in b} x, \max_{x \in b})$, which returns an ordered pair.
For every query, we'll compute both min and max and return the appropriate part.

In CHAROCC, the query is parametrized by $c$.
So we'll compute the result for all lowercase English characters.
Formally, let $\Gamma$ be the sequence of characters in lowercase English
and let $e(s, c)$ be the number of occurrences of the character $c$ in string $s$.
Then $f(b) = [\sum_{x \in b} e(x, c)]_{c \in \Gamma}$.
Here $f(b)$ is an array of length 26.

For these 3 examples, we now have a common abstraction to use: the query function.
The query function's domain is a set of finite arrays of some type.
Let us denote the codomain of the query function by $S$,
which we'll call the 'query output type'.

### Update function

In every update operation, we're given a function $g$, called the update function.
We have to replace $a[i]$ by $g(a[i])$ for $l \le i \le r$.

For SUMREPL, the update function is $g_y$, where $g_y(x) = y$.
For MINMAX, the update function is either $g_y(x) = x + y$ or $g_z(x) = xz$.

Now the generalized problem looks like this:

**Problem RANGEOP**:
You are given an array $a$ of $n$ elements, indexed from 0 to $n-1$.
You are also given a query function $f$.
You will be asked to perform $q$ operations. Each operation will be one of the following:

* given integers $l$ and $r$, output $f(a[l..r])$.
* given integers $l$ and $r$ and a function $g$,
    replace $a[i]$ by $g(a[i])$ for all $l \le i \le r$.

## Generalizing the query function

In problem RANGEOP, $f$ can be any arbitrary function.
But there are additional constraints if the problem has to be solved using segment trees.

### Substructure and the binary operator

To be able to solve a problem using segment trees,
the query function should follow a property called 'substructure'.
This means that we can compute $f(a)$ using this procedure:

1.  Choose any prefix $b$ of $a$. Let $a = b + c$ ($+$ denotes array concatenation).
2.  Compute $f(b)$ and $f(c)$.
3.  Combine $f(b)$ and $f(c)$ to get $f(a)$.

Examples:

* In SUMREPL, $f(b + c) = f(b) + f(c)$.
* In MINMAX, $f(b + c)$ $= (\min(f(b)_0, f(c)_0), \max(f(b)_1, f(c)_1))$.
Here $(x, y)_0 = x$ and $(x, y)_1 = y$.

Non-examples:

* Finding the median of an array doesn't have substructure
because the medians of $b$ and $c$ cannot be used to compute the median of $b + c$.
* $f(a) = a[0]^{a[1]^{a[2]^{\ldots a[n-1]}}}$.

We can express the substructure recurrence relations using a binary operator $\circ$,
so that $f(b + c) = f(b) \circ f(c)$.
$\circ$ is a function from $S \times S$ to $S$, where $S$ is the output type of the query function.

* For SUMREPL, $x \circ y = x + y$.
* For MINMAX, $x \circ y = (\min(x_0, y_0), \max(x_1, y_1))$.
* For CHAROCC, $x \circ y$ is obtained by element-wise addition of arrays $x$ and $y$.

### Associativity

Depending on which prefix of $a$ we choose, there can be multiple ways of computing $f(a)$.
For example, there are 2 ways of computing $f([x, y, z])$:

* choosing $[x]$ as prefix: $f([x, y, z]) = f([x]) \circ f([y, z])$ $ = f([x]) \circ (f([y]) \circ f([z]))$
* choosing $[x, y]$ as prefix: $f([x, y, z]) = f([x, y]) \circ f([z])$ $ = (f([x]) \circ f([y])) \circ f([z])$

Since the output should not depend on the choice of prefix,
$\circ$ should be associative over the range of $f$.

Since $\circ$ is associative, $f(a)$ $= f([a[0]]) \circ f([a[1]]) \circ \ldots \circ f([a[n-1]])$.

### Identity

Let's define $e = f([\,])$.
Since $f(a) = f(a + [\,]) = f(a) \circ e$ and $f(a) = f([\,] + a) = e \circ f(a)$,
we call $e$ the 'identity element' of $S$ for $\circ$.

$f$ may not be defined for an empty array ($f(a) = a[0]$ is an example).
When this happens, we can still define $f([\,]) = e$.
$e$ need not have any real significance; it is just a symbol
(this is similar to how $\sqrt{-1} = i$).
We also define $x \circ e = e \circ x = x$ for all $x \in S$.

### Monoids

A monoid $M = (S, \circ)$ is a set along with a binary operator defined on that set
which follows these axioms:

* Closure: $\forall x \in S, \forall y \in S,$
$x \circ y \in S$
* Associativity: $\forall x \in S, \forall y \in S, \forall z \in S,$
$(x \circ y) \circ z = x \circ (y \circ z)$
* Existence of identity: $\exists e \in S, \forall x \in S,$
$e \circ x = x \circ e = x$.
Here $e$ is called the identity of the monoid.

We can see that our query output type $S$ and our binary operator $\circ$ follow the above axioms.
Therefore, $(S, \circ)$ is a monoid.

### Monoid elements as segment tree values

Every node $u$ of a segment tree represents a segment (contiguous subarray) of the input array.
For example, the root represents the whole array,
the root's children represent the left and right halves of the array,
and the leaves represent segments with only one element in them.
Let's denote $u$'s segment by $\operatorname{segment}(u)$.

In every node $u$ of the segment tree, we will store the value $f(\operatorname{segment}(u))$.
Let's denote this by $\operatorname{value}(u)$.

To build and query a generalized segment tree, we will need to specify the following:

* $e$: The identity element of the monoid.
This is the output of empty queries.
For SUMREPL, $e = 0$. For MINMAX, $e = (\infty, -\infty)$.

* $f_0(x) = f([x])$: Specification of how to apply $f$ to a single-element array.
This is used to create leaf nodes of the segment tree.
For SUMREPL, $f_0(x) = x$. For MINMAX, $f_0(x) = (x, x)$.

* $\circ$: The binary operator.
This is used to create internal nodes of the segment tree.
For SUMREPL, $x \circ y = x + y$.
For MINMAX, $x \circ y = \min(x_0, y_0), \max(x_1, y_1)$.

In code, we can create a class for monoid elements.
The above traits of the monoid can be specified as methods/constructors of the class.

<!-- TODO: Add C++ class for MinMaxMonoidElem -->

## Generalizing update functions

### Node update function

Suppose I construct a segment tree on the input array $a$ of size $n$
(where the query function is $f$ and the corresponding binary operator is $\circ$).
Let the value at the root be $s$. We know that $s = f(a)$.
Now I apply a function $g$ to all elements of $a$.
For notational convenience, let $g(a) = [g(a[0]), g(a[1]), \ldots, g(a[n-1])]$.
After this, I update the segment tree and the value at the root is now $t$.

Given $s$ and $g$, can you find $t$?
This question effectively means that you should be able to update a segment tree
node without looking at its descendants.
We're looking for a function $h$ where $h(f(b)) = f(g(b))$ for all arrays $b$.
Let's call $h$ a 'node update function'.

There's no straightforward algorithm for deriving $h$ from $g$, but it's usually easy.
For example, for the MINMAX problem with $g(x) = x + 20$, $h(x) = (x_0 + 20, x_1 + 20)$.
This is how we verify $h$:
\begin{align*}
& h(f(a))
\\ &= h((\min(a), \max(a)))
\\ &= (\min(a) + 20, \max(a) + 20)
\\ &= (\min(a + 20), \max(a + 20))
\\ &= f(g(a))
\end{align*}

Here $a + 20$ is the array obtained by adding 20 to every element of $a$.

### Endomorphism

For a monoid $(S, \circ)$, a function $h: S \mapsto S$ is an endomorphism iff
both of these conditions hold:

* $h(e) = e$. Here $e$ is the identity of $S$.
* $h(x \circ y) = h(x) \circ h(y)$.

For example, $h(x) = x + 20$ is an endomorphism on the monoid $(\mathbb{Z}, \min)$ because
* $h(e) = h(\infty) = \infty + 20 = \infty = e$.
* $h(x \circ y) = \min(x, y) + 20$ $= \min(x + 20, y + 20) = h(x) \circ h(y)$.

### Node update function is an endomorphism

\\[ h(e) = h(f([\,])) = f(g([\,])) = f([\,]) = e \\]

\begin{align*}
& h(f(b) \circ f(c))
\\ &= h(f(b + c))
\\ &= f(g(b + c))
\\ &= f(g(b) + g(c))
\\ &= f(g(b)) \circ f(g(c))
\\ &= h(f(b)) \circ h(f(c))
\end{align*}

Therefore, $h$ is an endomorphism on the range of $f$.

## Lazy propagation

In computer science, laziness means procrastination.

When we're told to execute an update on a segment tree, we don't actually do the whole update.
We just note down which subtrees need to be updated.
Then when we're supposed to answer a query, we update only the part of the segment tree
which is needed to answer the query.

I'll explain this with an example for MINMAX
with the initial array $[10, 20, 30, 40, 50, 60, 70]$.
The image below shows the initial segment tree.
It presents 2 attributes of every segment tree node $u$:

* the indexes of the first and last elements of $\operatorname{segment}(u)$.
* $\operatorname{value}(u)$.

<figure>
<img src="{static}/img/segtree-lazy-update/0.dot.svg" />
<figcaption>Initial segment tree</figcaption>
</figure>

### Updation

Now we get an update with $l=2, r=6, g(x) = x + 20$.
This corresponds to $h(x) = (x_0 + 20, x_1 + 20)$.
Define $d(a, b)(x) = (ax_0 + b, ax_1 + b)$.
Therefore, $h = d(1, 20)$.

To execute this update, we first find the maximal subtrees which span this range.
These are the subtrees at `2..3` and `4..6`.
We'll update the values at `2..3` and `4..6` by applying $h$ to their values.
We'll then note down that their children are yet to be updated with $h = d(1, 20)$.
We'll also update all the ancestors of the affected nodes by recomputing their values.

<figure>
<img src="{static}/img/segtree-lazy-update/1.dot.svg" />
<figcaption>
Segment tree after update
<span class="math">\(l=2, r=6, g(x) = x + 20\)</span>.<br />
Blue nodes were updated. Red nodes were not updated but they have a pending update.
</figcaption>
</figure>

### Querying

If a query arrives for $l=2, r=5$, we would like to return
$\operatorname{value}(\texttt{2..3}) \circ \operatorname{value}(\texttt{4..5})$.
But before that, we'll have to update $\operatorname{value}(\texttt{4..5})$.
To do this, we apply $h$ to $\operatorname{value}(\texttt{4..5})$
and mark its children as pending for updation.
Since the pending update moved from `4..5` to its child,
we say that the pending update 'propagated'.

<figure>
<img src="{static}/img/segtree-lazy-update/2.dot.svg" />
<figcaption>
Segment tree after the query <span class="math">\(l=2, r=5\)</span>.<br />
The value returned by the query is written beside each node.
</figcaption>
</figure>

### Combining updates

Suppose we get the update $l=0, r=6, g(x) = x + 10$.
We will update the root node and add $d(1, 10)$ to the children.

<figure>
<img src="{static}/img/segtree-lazy-update/3.dot.svg" />
<figcaption>
Segment tree after update
<span class="math">\(l=0, r=6, g(x) = x + 10\)</span>.<br />
Blue nodes were updated. Red nodes were not updated but they have a pending update.
</figcaption>
</figure>

Now we get another update $l=0, r=6, g(x) = 3x$. This corresponds to $h = d(3, 0)$.
We can update the root node, and add $d(3, 0)$ to the children.
But the children already have a pending update of $d(1, 10)$.
To resolve this, we will compose the functions, i.e. we'll find a single
function which is equal to successively applying $d(1, 10)$ and then $d(3, 0)$.

\begin{align*}
& d(3, 0)(d(1, 10)(x))
\\ &= d(3, 0)(x + 10)
\\ &= 3(x + 10) = 3x + 30
\\ &= d(3, 30)(x)
\end{align*}

<figure>
<img src="{static}/img/segtree-lazy-update/4.dot.svg" />
<figcaption>
Segment tree after update
<span class="math">\(l=0, r=6, g(x) = 3x\)</span>.<br />
Blue nodes were updated. Red nodes were not updated but they have a pending update.
</figcaption>
</figure>

More generally, $d(a_1, b_1) \cdot d(a_2, b_2) = d(a_1a_2, a_1b_2 + b_1)$.

## Generic implementation of segment trees

### Representing node update functions

We will need to come up with a succinct representation for node update functions.
In the example above, the function $d(a, b)$ can be specified by the ordered pair $(a, b)$.
The choice of representation will depend on the type of update functions expected.

Then we need to specify the following to describe node update functions:

* Function application: How to compute $h(x)$ given $x$.

* The identity function: The function $h(x) = x$.
In the above example, $d(1, 0)$ is the identity function.
It should also be possible to check whether a function is the identity function.

* Function composition: A rule for how to compose 2 node update functions.
In the above example, the composition of $(a_1, b_1)$ and $(a_2, b_2)$ is $(a_1a_2, a_1b_2 + b_1)$.

### Implementation

We will use 2 arrays: `values` and `pending`.
`values[i]` is the value of the $i^{\textrm{th}}$ node.
`pending[i]` is the pending node update function of the $i^{\textrm{th}}$ node.
Initially, `values` is constructed from the input array
and `pending[i]` is the identity function for every node $i$.

You can see [my C++ segment tree library](https://gist.github.com/sharmaeklavya2/99ed35efbb639bbe7d7b46b89b74fea0)
for an example of how to write generic segment trees.

## Bringing problems to standard form

To use the generic segment tree implementation, we should be able describe
query outputs as elements of a monoid and the update function as an endomorphism.
Let's look at some examples:

**SUMREPL**:

* $f(a) = \left(n, \sum_{i=1}^n a[i]\right)$, where $a$ is an array of size $n$.
Therefore, identity is $(0, 0)$, $f_0(x) = (1, x)$
and $(n_1, x) \circ (n_2, y) = (n_1 + n_2, x + y)$.
* For the update function $g(x) = y$, the node update function is $h_y((n, x)) = (n, ny)$.
The identity function is $id$, which cannot be expressed as $h_y$ for any $y$.
Function composition: $h_s \cdot h_t = h_s$.

**CHAROCC**:

* Each node of the segment tree stores the frequency of every lowercase English letter.
Identity element is an array with all zeros.
Creating a leaf node from a string involves computing frequencies of each character.
The binary operator $\circ$ is defined as element-wise addition of the arrays.
* A node update function is represented as an array $b$ of length 26.
Applying the function involves elementwise addition of $b$ to a segment tree node value.
Functions are composed by adding their arrays element-wise.
The identity function has all elements 0.
The update function with character $c$ corresponds to an array
where the entry of $c$ is 1 and all other entries are 0.

**KADANE**:

You are given an array $a$ of $n$ integers, indexed from 0 to $n-1$.
The query function $f$ is the largest contiguous subarray sum.
You will be asked to perform $q$ operations. Each operation will be one of the following:

* given integers $l$ and $r$, output $f(a[l..r])$.
* given integers $l$, $r$ and $y$, replace $a[i]$ by $y$ for all $l \le i \le r$.

This problem is left as an exercise.
You must come up with a suitable monoid for representing segment tree values
and a suitable node update function.

<div class="collapsible">
    <label for="checkbox0" class="collapsor-lbl"> Minor hint </label>
    <div class="focus-capturer" tabindex="0">
        <input id="checkbox0" class="collapsor" type="checkbox" />
        <div class="collapsible-content">
            <p>See the proof of correctness of Kadane's algorithm.
            Use divide-and-conquer instead of an incremental approach.</p>
        </div>
    </div>
</div>

<div class="collapsible">
    <label for="checkbox1" class="collapsor-lbl"> Major hint </label>
    <div class="focus-capturer" tabindex="0">
        <input id="checkbox1" class="collapsor" type="checkbox" />
        <div class="collapsible-content">
            <p>Each segment tree node stores 4 values for its segment:</p>
            <ol>
                <li>Sum of the elements of the segment</li>
                <li>Largest prefix sum of the segment</li>
                <li>Largest suffix sum of the segment</li>
                <li>Largest subarray sum of the segment</li>
            </ol>
        </div>
    </div>
</div>
