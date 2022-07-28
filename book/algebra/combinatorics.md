(sec:alg:combinatorics)=
# Enumerative Combinatorics

Main references for this section are
{cite}`van2001course,flajolet2009analytic,morris2017combinatorics`.

## Basic Counting


### Product Rule

```{prf:theorem} Product rule
:label: res-comb-product-rule

Suppose an experiment has two aspects.
First aspect can vary in $n_1$ ways.
Second aspect can vary in $n_2$ ways.
Assume that the two aspects are independent.
Then the total number of outcomes is

$$
n = n_1 n_2.
$$

If there are $k$ different aspects each of
which can vary in $n_i$ ways for $i \in 1,\dots,k$,
then the total number of outcomes is

$$
n = n_1 n_2 \dots n_k = \prod_{i=1}^k n_i.
$$
```

Examples

1. If there are three possible coffee choices and
   two possible doughnut choices then the number
   of different combinations of coffee and doughnut
   are six.
1. If a t-shirt comes in three different sizes
   and four different colors, then there are
   twelve different varieties of the same t-shirt.


### Sum Rule

```{prf:theorem} Sum rule
:label: res-comb-sum-rule

Suppose that the outcome of an experiment consists
of two different cases $A$ and $B$ which are mutually
exclusive of each other. In other words, if $A$
occurs then $B$ cannot occur and vice-versa.
Suppose that there are $n_1$ possible outcomes
under the case $A$ and $n_2$ possible outcomes
under the case $B$. Then the total number of
outcomes is

$$
n = n_1 + n_2.
$$
In general, if the outcome of an experiment has
$k$ distinct cases which are mutually exclusive
and if for each $i$-th case, there are $n_i$
possible outcomes, then the total number of
outcomes is

$$
n = n_1 + n_2 + \dots + n_k = \sum_{i=1}^k n_i.
$$
```

Examples

1. Suppose a house has two floors. The first
   floor has $3$ rooms and the second floor has $5$
   rooms. Then the number of ways you can select
   a room is $3 + 5 = 8$.
1. Suppose a team has $3$ men and $4$ women members.
   Then the number of ways you can select a team
   member is $3 + 4 = 7$.
1. Suppose we have to pick either a single letter
   or a single digit. There are $26$ possible letters
   and $10$ possible digits. Thus, there are $36$
   possible outcomes.




## Permutations

Permutations are different arrangements of a given finite set
of objects.

```{prf:definition} Permutation
:label: def-comb-permutation

A *permutation* of $n$ distinct objects is an arrangement of those
objects in a definite order. If $r \in \{1, \dots, n \}$ then
an $r$-*permutation* of $n$ objects is an arrangement of $r$
of the $n$ objects in a definite order.
```

```{prf:example} Permutations of A,B,C
:label: ex-comb-permutations-abc

Following are the possible permutations of the three
letters A,B,C.

1. A, B, C
1. A, C, B
1. B, A, C
1. B, C, A
1. C, A, B
1. C, B, A

As we can see there are $6$ different permutations.
```

```{prf:example} $2$-permutations of A,B,C,D
:label: ex-comb-2-permutations-abcd

Following are the possible ways to pick and arrange
2 letters out of the set {A, B, C, D}.

1. A, B
1. A, C
1. A, D
1. B, A
1. B, C
1. B, D
1. C, A
1. C, B
1. C, D
1. D, A
1. D, B
1. D, C

There are 12 possible $2$-permutations.
```

```{prf:theorem} Number of $r$ permutations
:label: res-comb-r-perm-count

The number of $r$ permutations of $n$ objects,
denoted by $P(n, r)$, is given by

$$
P(n, r) = n (n -1) \dots (n - r + 1).
$$
```

```{prf:proof}
We proceed as follows.

1. There are $n$ ways of choosing the first object.
1. Once the first object has been chosen, there are $n-1$
   ways of choosing the second object.
1. Continuing in the same manner, once $p$ objects have been
   chosen, there are $n-p$ ways of choosing the $p+1$-th
   object.
1. At the end, when $r-1$ objects have been chosen, then
   there are $n-(r-1)=n-r+1$ ways of choosing the 
   last object.
1. By the product rule, the total number of arrangements is

   $$
   n (n -1) \dots (n -r +1).
   $$
```

```{prf:definition} Factorial
:label: def-comb-factorial

The factorial of $n$, denoted as $n!$ is defined as

$$
n! = n (n-1) \dots 1.
$$
By convention, we define $0! = 1$.
```

1. It is clear that the number of permutations of $n$ objects
   is $n!$.
1. We can also see that the number of $r$-permutations of $n$
   objects is given by the formula

   $$
   P(n, r) = \frac{n!}{(n-r)!}.
   $$


```{prf:example} Round table seating arrangement problem

You are a family of three. You have invited five guests
for a party. Your dining table can seat all the eight
people. As hosts, you don't want to sit together on the
table. The guests can be seated arbitrarily. How many
seating arrangements are possible?

1. We note that only the relative arrangements of
   people matters.
1. Let your family members be called A, B, C.
1. Let the guests be labeled as 1,2,3,4,5.
1. We shall identify an arrangement starting
   from where A is sitting and then going clockwise.
1. An example arrangement is A,1,2,B,3,4,C,5.
1. Note that neither B nor C can be at the end
   as that would lead to them sitting next to A.
1. Since A is always at the beginning of an
   arrangement, we can drop it.
1. Let us replace all the guests by *.
1. Then the arrangement looks like
   *, *, B, *, *, C, *.
1. Forget about the seats for the moment
   and just look at this arrangement.
1. We see that B and C must be placed
   between the guests so that they
   are not sitting next to each other.
1. We can think of slots between guests
   and denote them by |.
1. Then the guests and slots between them
   can be represented as * | * | * | * | *.
1. There are 4 slots between 5 guests.
1. We can see that we can place B and C
   into either of these 4 slots.
1. The number of ways the 2 slots out of 4 can be
   selected is $P(4,2) = 4 \times 3 = 12$.
1. Once the slots have been picked up 
   by B and C, the guests can
   arrange themselves in $5!=120$ different
   ways.
1. By the product rule, the total number
   of arrangements is $12 \times 120 = 1440$.
```

## Combinations

```{prf:definition} $r$-combination
:label: def-comb-combination

Assume that we have $n$ distinct objects (where $n \in \Nat$).
An $r$-*combination* of $n$ objects is a subset consisting of
$r$ of those objects where $0 \leq r \leq n$.

The number of $r$ combinations of $n$ objects is denoted by
$\binom{n}{r}$ or $C(n, r)$.
```

1. There is only 1 way of to choose all $n$ objects.
   Hence $C(n, n) = 1$.
1. There is only 1 way to choose none of the $n$ objects.
   Hence $C(n, 0) = 1$.
1. There are $n$ ways to choose one of the $n$ objects.
   Hence $C(n, 1) = n$.
1. There are $n$ ways to choose $n-1$ of the $n$ objects
   as it is equivalent to drop one of the $n$ objects.
   Hence $C(n, n-1) = n$.


```{prf:theorem} Number of $r$-combinations
:label: res-comb-n-c-r

The number of $r$-combinations of $n$ objects is given
by

$$
C(n, r) = \binom{n}{r} = \frac{n!}{r! (n-r)!}.
$$
```

```{prf:proof}
This follows from the fact that each $r$-combination
results in $r!$ $r$-permutations.

1. By {prf:ref}`res-comb-r-perm-count` the number
   of $r$-permutations of $n$ objects is

   $$
   P(n, r) = \frac{n!}{(n-r)!}.
   $$
1. Let $k = C(n, r)$.
1. Then for each of the unordered subsets of $r$ elements,
   there are $r!$ ways that we can arrange them in a specific
   order.
1. Hence

   $$
   r! k = P(n, r)
   $$
   by the product rule.
1. Hence we have

   $$
   C(n, r) = k = \frac{P(n, r)}{r!} = \frac{n!}{r! (n-r)!}.
   $$
```


```{prf:example}
:label: ex-comb-comb-1

What is the number of ways to choose 3 hearts
from a deck of cards at least one of which is
an ace or a king?

1. There are 13 cards of the suit of hearts.
1. The selection includes a king but no ace.
   Number of ways to choose 2 other cards
   is $C(11, 2)$.
1. The selection includes an ace but no king.
   Number of ways to choose 2 other cards
   is $C(11, 2)$.
1. The selection includes both king and ace.
   Number of ways to choose the third card
   is $C(11, 1)$.
1. Total number of ways is

   $$
   C(11, 2) + C(11, 2) + C(11, 1)
   = 55 + 55 + 11
   = 121.
   $$

Here is another way to divide the
problem in two cases.

1. The selection includes an ace.
   In this case the number of
   ways the remaining two cards
   can be selected is $C(12, 2)$.
1. The selection includes a king
   but not an ace. The number of
   ways the remaining two cards
   can be chosen is $C(11,  2)$.
1. Hence total number of cases
   is

   $$
   C(12, 2) + C(11, 2) = 66 + 55 = 121.
   $$

Here is a third approach.

1. Ace is included: $C(12, 2)$ ways.
1. King is included: $C(12, 2)$ ways.
1. Both of these cases include the
   case where both ace and king are included.
1. The number of ways both ace and king
   can be selected is $C(11, 1)$.
1. Since this is double counted, hence we
   need to subtract it from total number
   of cases.
1. Thus, we get

   $$
   C(12, 2) + C(12, 2) - C(11, 1)
   = 66 + 66 - 11 = 132 - 11 = 121.
   $$
````


## Binomial Theorem

```{index} Binomial coefficient
```
```{prf:definition} Binomial coefficient
:label: def-comb-binom-coef

For any nonnegative $n$ and any integer
$r$ with $0 \leq r \leq n$, the
*binomial coefficient* is defined as

$$
{n \choose r} = \frac{n!}{r! (n-r)!}.
$$
```
This is another name for the number of $r$-combinations
of $n$ objects.


```{index} Binomial theorem
```
```{prf:theorem} Binomial theorem
:label: res-comb-binomial-theorem

For any $a$ and $b$ and any nonnegative integer $n$, we have

$$
(a + b)^n = \sum_{r=0}^n \binom{n}{r} a^r b^{n - r}.
$$

As a special case, we have


$$
(1 + x)^n = \sum_{r=0}^n \binom{n}{r} x^r.
$$

Setting $x=1$, we get

$$
2^n = \sum_{r=0}^n \binom{n}{r}.
$$
```

```{prf:proof}
Consider the simpler cases first:

1. For $n=0$, both L.H.S. and R.H.S. reduce to $1$.
1. For $n=1$, the L.H.S. is $a + b$. The R.H.S. is

   $$
   {1 \choose 0}b + {1 \choose 1}a  = b + a = a + b.
   $$

We now consider the general case.

1. We can write

   $$
   (a + b)^n  = (a + b) \dots (a + b).
   $$
1. There are $n$ factors of $(a + b)$ on the R.H.S..
1. Consider the term $a^r b^{n - r}$.
1. This is attained by choosing $a$ from $r$
   factors and $b$ from remaining $n-r$ factors.
1. There are $\binom{n}{r}$ ways to choose $r$
   out of $n$ factors from which $a$ can be picked.
1. Thus, the coefficient of $a^r b^{n - r}$ in
   the expansion of $(a + b)^n$ is $n \choose r$.
1. The smallest power of $a$ in the expansion is $0$
   and the largest power is $n$.
1. Thus, we have

    $$
    (a + b)^n = \sum_{r=0}^n \binom{n}{r} a^r b^{n - r}.
    $$
1. The special case is obtained by setting $a=x$ and $b=1$.
```

```{prf:theorem}
:label: res-comb-binomial-cor-1


For any natural number $n$ we have

$$
\sum_{r=0}^n r \binom{n}{r}(-1)^{r -1} = 0.
$$
```

```{prf:proof}
From the binomial theorem we have:

$$
(1 + x)^n = \sum_{r=0}^n \binom{n}{r} x^r.
$$

Differentiating on both sides, we get

$$
n(1 + x)^{n-1} = \sum_{r=0}^n r \binom{n}{r} x^{r-1}.
$$


Putting $x=0$, we get

$$
0 = \sum_{r=0}^n r \binom{n}{r} (-1)^{r-1}.
$$
```


## Bijections


Recall from {prf:ref}`def-st-equivalent-sets`
that two sets are equivalent if there exists
a bijection (a bijective function) between them.
In that case, the sets are said to have the
same cardinality.
In this section, we are dealing
with finite sets only.
Recall from {prf:ref}`def-finite-set`
that a set is called finite if there is a bijection
between the set and a
{prf:ref}`segment <def-st-segment-natural-numbers>`
of natural numbers.
Thus, there exists a bijection between two finite
sets, then they have the same number of elements.
This gives us a powerful method of counting
the number of elements in a finite set. If we
can find a bijection between a given set and
a set whose number of elements is known, then
we know the number of elements of the given
set is also known. This technique is known
as the *bijective technique*. 


We use this technique to provide a proof
for the number of subsets of a finite set.

```{prf:theorem} Number of subsets of a finite set
:label: res-comb-finite-set-subsets-count

Let $A$ be a set of $n$ elements. Then the
number of subsets of $A$ is $2^n$.
```

````{prf:proof}
We develop a bijection between subsets
of $A$ and binary strings of length $n$.

1. Let $A = \{a_1, \dots, a_n \}$.
1. Let each bit of a binary string $b_1 b_2 \dots b_n$
   correspond to an element of $A$ ($a_i \to b_i$).
1. For each subset $X$ of $A$, the let the corresponding
   binary string be formed as follows:
   1. If $a_i \in X$, then $b_i = 1$.
   1. Otherwise, $b_i = 0$.
1. It is easy to see that this is a bijection between
   the set of subsets of $A$ and the set of binary
   strings of length $n$.
1. The number of possible binary strings of length $n$
   is $2^n$ since each bit can take exactly $2$ values.
1. Hence, due to the equivalence of the two sets, the
   number of subsets of $A$ is $2^n$.

Following is an example of mapping between
subsets of the set $\{ x, y, z \}$ and 
binary strings of length $3$.

```{list-table}
:header-rows: 1

* - subset
  - $b_1$
  - $b_2$
  - $b_3$
* - $\EmptySet$
  - 0
  - 0
  - 0
* - $\{ x \}$
  - 1
  - 0
  - 0
* - $\{ y \}$
  - 0
  - 1
  - 0
* - $\{ z \}$
  - 0
  - 0
  - 1
* - $\{ x, y \}$
  - 1
  - 1
  - 0
* - $\{ y, z \}$
  - 0
  - 1
  - 1
* - $\{ x, z \}$
  - 1
  - 0
  - 1
* - $\{ x, y, z \}$
  - 1
  - 1
  - 1
``` 
````


## Combinatorial Proofs

```{index} Combinatorial proof
```
```{prf:theorem} Combinatorial proofs
:label: res-comb-combinatorial-proof

If $f(n)$ and $g(n)$ are functions that count
the number of solutions to some problem involving
$n$ objects, then $f(n) =  g(n)$ for every $n$.
```

```{index} Combinatorial identity
```
```{prf:theorem} Combinatorial identity
:label: def-comb-combinatorial-identity

Let there be two functions $f, g : \ZZ_+ \to \ZZ$.
Suppose there exists a problem about $n$ objects
such that the number of solutions to the problem
in one way is given by $f(n)$ and the number of
solutions to the same problem in another way
is given by $g(n)$ for every $n$. Then
this is a *combinatorial proof* of the
identity 

$$
f(n) = g(n).
$$
The equation $f(n) = g(n)$ is known as 
a *combinatorial identity*.
```

```{note}
The concept of combinatorial proofs
and identity is also applicable to
the problems with multiple variables.
```


```{prf:theorem}
:label: res-comb-ncr-ncn-r

$$
{n \choose r} = {n \choose n - r}.
$$
```

```{prf:proof}

Consider the problem of choosing $r$ objects from
a set of $n$ objects.

1. By definition, the number of ways $r$ objects
   can be chosen from a set of $n$ objects is
   given by $n \choose r$.
1. Choosing $r$ objects from a set of $n$ objects
   is equivalent to leaving the remaining $n-r$ objects
   from the set. 
1. The number of ways to leave $n-r$ objects out of $n$ objects
   is $n \choose n - r$.
1. Hence we have the combinatorial identity

   $$
    {n \choose r} = {n \choose n - r}.
   $$
```

```{prf:example}
:label: ex-comb-ncr-sum-2-pow-n

For every natural number $n$, we have

$$
\sum_{r=0}^n {n \choose r} = 2^n.
$$

We already showed this result in {prf:ref}`res-comb-binomial-theorem`.
Let us look at a combinatorial proof.

1. By {prf:ref}`res-comb-finite-set-subsets-count`, 
   the number of subsets of a set of $n$ elements is $2^n$.
1. Another way of counting the number of subsets of $n$
   elements is as follows.
   1. Each subset has $r$ elements where $0 \leq r \leq n$.
   1. The number of subsets of $r$ elements is $n \choose r$.
   1. Hence total number of subsets is
      $\sum_{r=0}^n {n \choose r}$.
1. By {prf:ref}`res-comb-combinatorial-proof`, the two must
   be equal.
```

```{prf:example}
:label: ex-comb-n-n-least-1

Consider two sets $A$ and $B$ each of which
consist of $n$ objects. Assume that
the sets $A$ and $B$ are disjoint.
We wish to select $r$ objects from $A$ and $B$ together
with the condition that at least $1$ object
must be chosen from the set $B$.
Following are different ways of counting.

Method 1

1. There are $2 n \choose r$ ways of choosing
   $r$ objects out of the $2 n$ objects we have.
1. There are $n \choose r$ ways in which
   no object from the set $B$ has been selected.
1. Hence, the number of ways to select at least
   one object from $B$ is given by

   $$
   {2 n \choose r} - {n \choose r}.
   $$

Method 2
1. We can consider the following $r$ different cases.
   $i$ objects from the set $B$ have been chosen
   where $1 \leq i \leq r$.
1. For the $i$-th case, the total number of ways
   to choose $i$ objects from the set $B$ and
   the remaining $r-i$ objects from the set $A$
   is given by

   $$
   {n \choose i}{n \choose r -i}.
   $$
1. Hence, the total number of ways of choosing $r$
   objects from $A$ and $B$ with at least one object
   from $B$ is

   $$
   \sum_{i=1}^r {n \choose i}{n \choose r -i}.
   $$
1. By {prf:ref}`res-comb-combinatorial-proof`, 
   we get the combinatorial identity

   $$
   \sum_{i=1}^r {n \choose i}{n \choose r -i}
   = {2 n \choose r} - {n \choose r}.
   $$
```


```{prf:example} Recursive rule for computing $r$-combinations
:label: ex-comb-recursive-rule-r-comb

Consider the problem of choosing $r$ objects from
a set of $n$ objects.
By definition, the number of ways we can choose
$r$ objects is $n \choose r$.
Following is another way to count the same.

1. Let us label the objects as $1,2, \dots, n$.
1. We consider $n$ different cases as follows.
1. Each subset can be identified by the largest
   label inside it.
1. In the $k$-th case, we consider all the subsets
   where the largest label is $k$.
1. Since this object is decided, the number of ways
   of choosing the remaining $r-1$ objects from the
   $k-1$ objects whose labels are smaller than $k$
   is given by $k - 1 \choose r - 1$.
1. Since any such subset must have at least $r$ objects,
   hence the minimum possible value of $k$ is $r$.
1. The maximum possible value of $k$ is $n$.
1. Hence, the total number of elements is given by

   $$
   \sum_{k=r}^n {k - 1 \choose r - 1}.
   $$
1. We get the identity

   $$
   {n \choose r} = \sum_{k=r}^n {k - 1 \choose r - 1}.
   $$
1. By replacing $k-1$ with $i$, we get another version

   $$
   {n \choose r} = \sum_{i=r-1}^{n-1} {i \choose r - 1}.
   $$

This identity enables us to compute $n \choose r$
if $i \choose r - 1$ is known for all values of
$r-1 \leq i \leq n-1$.
```

## Counting with Repetitions

We now consider a different type of problem.
Rather than selecting objects from a given
set of $n$ distinct objects, we assume that there
are $n$ types of objects available and
we are free to choose as many objects
of a particular type as we want.
Thus, we allow for the repetition of objects
of the same type.

```{prf:example} Two digit numbers
:label: ex-comb-rep-1

How many 2 digit numbers are possible?

1. On the first digit, we can have one of the nine nonzero digits.
1. On the second digit, we can have any of the ten digits.
1. Hence, total number of two digit numbers is:

   $$
   9 \times 10 = 90.
   $$
1. Readers can verify that this includes all the numbers from
   $10$ to $99$.
1. We allow for repetition (e.g. $11, 22, 33$).
```

```{prf:example} Four digit pins
:label: ex-comb-rep-pins

We often use $4$ digit pins for different applications.
In this case, $0$ may be allowed as the first digit.
Then the number of possible $4$ digit pins is
$10^4 = 10,000$.
```


### Combinations with Repetitions

```{prf:theorem} $r$-combinations with repetitions
:label: res-comb-r-comb-rep

The number of ways of choosing $r$ objects from
$n$ types of objects (with replacement or repetition)
is

$$
{n + r - 1 \choose r}.
$$
```

```{prf:proof}

The $n$ categories of objects can be separated
by $n-1$ bars like below

$$
a_1 | a_2 | \dots | a_{n-1} | a_{n}.
$$

1. We have $n$ slots (or urns) for the $n$ categories.
1. There are $n-1$ bars between them.
1. Suppose that $r$ objects that have been chosen
   can be split as $r_1$ objects of the category $a_1$,
   $r_2$ objects of categories $a_2$ and so on.
1. Then we have

   $$
   r = r_1 + r_2 + \dots + r_n.
   $$
1. Note that some of the $r_i$ may be zero also.
1. Let each object be represented by the symbol $-$ (dash).
1. Then the arrangement may look something like

   $$
   -- | - | | --- | - | \dots | | | | ----| --
   $$
1. $r_1$ dashes followed by a bar, then $r_2$ dashes
   followed by a bar and so on.
1. Different arrangements of $r$ dashes and $n-1$
   bars lead to different ways of selecting $r$
   objects from $n$ categories of objects.
1. We can think of the arrangement as a string
   of dashes and bars.
1. Then, the problem is equivalent to the counting
   the number of strings consisting of $r$ dashes
   and $n-1$ bars.
1. The total length of such strings is $n + r - 1$.
1. The number of strings with $r$ dashes is
   $n + r -1 \choose r$.
1. This is also same as the number of strings
   with $n-1$ bars which is $n + r - 1 \choose n - 1$.
```


### Multiset Permutations

```{prf:theorem} Multiset permutations
:label: res-comb-multiset-permutation

Let $A$ be a multiset of $n$ objects of $m$ types.
Assume that $A$ contains $r_1$ objects of type $1$,
$r_2$ objects of type $2$ and so on. Accordingly

$$
n = r_1 + r_2 + \dots + r_m.
$$

Then, the number of permutations of these $n$ objects
is 

$$
\frac{n!}{r_1! r_2 ! \dots r_m!}.
$$
```

```{prf:proof}
Approach 1

1. If all $n$ objects were distinct, then the number of
   permutations will have been $n!$.
1. Now, when $r_1$ of these objects are indistinguishable
   from each other, then all $r_1!$ permutations of these
   $r_1$ objects are identical.
1. Hence, making the $r_1$ objects indistinguishable reduces
   the number of arrangements to $\frac{n!}{r_1!}$.
1. Similarly, making the next $r_2$ objects indistinguishable
   from each other reduces
   the number of arrangements to $\frac{n!}{r_1! r_2!}$.
1. Continuing in the fashion, making the last $r_m$ objects
   indistinguishable from each other reduces
   the number of arrangements to $\frac{n!}{r_1! r_2 ! \dots r_m!}$.


Approach 2

1. In any arrangement of $n$ objects, there are $n$ slots.
1. The number of ways we can choose $r_1$ slots to place
   first $r_1$ objects of type $1$ (which are indistinguishable)
   is given by $n \choose r_1$.
1. The number of ways we can choose the next $r_2$ slots to
   place next $r_2$ objects of type $2$ (which are indistinguishable)
   is given by $n - r_1 \choose r_2$.
1. Continuing in the same manner, the number of ways to choose
   the last $r_m$ slots to place the last $r_m$ objects of type $m$
   (which are indistinguishable) is given by
   $n - r_1 - \dots - r_{m - 1} \choose r_m$.
1. By the product rule, the total number of ways is

   $$
   {n \choose r_1}{n - r_1 \choose r_2}\dots {n - r_1 - \dots - r_{m - 1} \choose r_m}.
   $$
1. This expands to

   $$
   & \frac{n!}{r_1! (n-r_1)!}
   \frac{(n - r_1)!}{r_2! (n-r_1 - r_2)!}
   \dots   
   \frac{(n - r_1 - \dots - r_{m-1})!}{r_m! 0!}\\
   & = \frac{n!}{r_1! r_2 ! \dots r_m!}.
   $$
```



```{prf:example} Volunteer selection
:label: ex-comb-volunteer selection

You have 3 projects A, B and C. You have a team of
20 volunteers available.

- Project A needs 3 people.
- Project B needs 5 people.
- Project C needs 9 people.

How many ways, can you assign volunteers to
projects?


1. We can introduce a fourth category D of 
   volunteers who are not assigned to
   any project.
1. The D category has $20 - 3 - 5 - 9 = 3$ volunteers.
1. Thus, we need to split 20 volunteers into
   4 groups of sizes 3,5,9, and 3 respectively.
1. A particular assignment might look like

   $$
   AAABBBBBCCCCCCCCCDDD.
   $$
1. Another assignment might look like

   $$
   CDCABCABCCBBCCCDADCB.
   $$
1. We can see that the assignment consists of
   permutations of 20 labels which are of 4 types
   (A, B, C, D).
1. Hence the number of permutations is given by

   $$
   \frac{20!}{3! 5! 9! 3!}.
   $$
```


### Multinomial Theorem

```{prf:definition} Multinomial coefficient
:label: def-comb-multinomial-coefficient

For nonnegative integers $r_1, r_2, \dots, r_m$
such that $\sum_{i=1}^m r_i = n$, the multinomial
coefficient is defined as

$$
{n \choose r_1, r_2, \dots, r_m}
= \frac{n!}{r_1! r_2 ! \dots r_m!}.
$$
```

It is clear that the multinomial coefficient is
equal to the number of permutations of $n$
objects of $m$ types where $r_1$ objects are of type $1$,
$r_2$ objects are of type $2$ and so on.

Also note that for $n=0$, we have $r_i=0$ and
the multinomial coefficient becomes

$$
\frac{0!}{0! 0! \dots 0!} = 1.
$$

````{prf:theorem} Multinomial theorem
:label: res-comb-multinomial-theorem

For arbitrary $x_1, x_2, \dots, x_m$ and some nonnegative integer
$n$, we have

```{math}
:label: eq-comb-multinomial-theorem
(x_1 + x_2 + \dots + x_m)^n 
= \sum_{k_1 + k_2 + \dots + k_m  = n}
{n \choose k_1, k_2, \dots, k_m}
\prod_{1 \leq r  \leq m}x_r^{k_r}.
```
The number of terms of the sum on the R.H.S. is given by

$$
{n + m - 1 \choose n}.
$$
````

```{prf:proof}
Consider the basic cases first.

1. For $m=1$, the result is trivial as there is exactly one
   term on the R.H.S. given by $x_1^n$.
1. For $m=2$, {eq}`eq-comb-multinomial-theorem` reduces to

   $$
   (x_1 + x_2)^n 
   &= \sum_{k_1 + k_2 = n}{n \choose k_1, k_2}x_1^{k_1} x_2^{k_2}\\
   &= \sum_{k=0}^n {n \choose k}x_1^k x_2^{n - k}.
   $$
   We replaced $k_1$ by $k$ and $k_2$ by $n-k$.
1. This is the binomial theorem already proven in
   {prf:ref}`res-comb-binomial-theorem`.
1. For $n=0$, both L.H.S. and R.H.S. reduce to $1$.

We now consider the general case.
1. Each term on the R.H.S. is of the form

   $$
   C \prod_{1 \leq r  \leq m}x_r^{k_r}
   $$
   such that $k_1 + \dots + k_m = n$
   and $C$ is some coefficient.
1. There are $m$ types of variables $x_1, \dots, x_m$.
1. In the product, there are total $n$ variables.
1. The number of ways $n$ objects of $m$ types can
   be selected is given by

   $$
   n + m - 1 \choose n
   $$
   due to {prf:ref}`res-comb-r-comb-rep`.
1. This establishes the number of terms on the R.H.S..
1. It remains to calculate $C$.
1. We can see that $\prod_{1 \leq r  \leq m}x_r^{k_r}$
   arises on the R.H.S. from the different permutations
   of $r_1$ variables of type $x_1$,
   $r_2$ variables of type $x_2$ and so on
   up to $r_m$ variables of type $x_m$.
1. The number of permutations of $n$ variables of $m$
   types $x_1, \dots, x_m$ with counts
   $r_1, \dots, r_m$ is given by

   $$
   \frac{n!}{r_1! r_2 ! \dots r_m!}
   $$
   due to {prf:ref}`res-comb-multiset-permutation`.
1. Hence

   $$
   C = {n \choose r_1, r_2, \dots, r_m}
   $$
   as per the definition of the
   {prf:ref}`multinomial coefficient <def-comb-multinomial-coefficient>`.
```

## Recursion

```{index} Recursively defined sequence
```
```{prf:definition} Recursively defined sequence
:label: def-comb-recursive-sequence

We say that a sequence $\{t_n \} = t_1, t_2, \dots, t_n, \dots$
is *recursively defined* if for every integer $n$ greater than
or equal to some bound $b \geq 0$, the value of $t_n$ depends
on at least some of the values $t_1, \dots, t_{n -1}$.
The values for $t_1, \dots, t_{b-1}$ are given explicitly.
These are referred to as the *initial conditions* for the
recursively defined sequence. The equation that defines
$t_n$ from $t_1, \dots, t_{n-1}$ is called a
*recursive relation*. 
```

```{index} Fibonacci sequence
```
```{prf:definition} Fibonacci sequence
:label: def-comb-fibonacci-sequence

The famous *Fibonacci sequence*,
denoted by $f_0, f_1, f_2, \dots$,
is defined as follows:

1. $f_0 = 1$.
1. $f_1 = 1$.
1. for every $n \geq 2$, we have

   $$
   f_n = f_{n-1} + f_{n - 2}.
   $$
```
The sequence is attributed to the Italian mathematician
Leonardo Pisano ("Fibonacci") of the 13th century.
However, it has been known to Indian mathematicians
as early as the 6th century.

For recursive sequences, we aim to solve
the following types of problems:

1. Devise a formula for $t_n$ such that one
   doesn't have to compute every term in the
   recursion to compute $t_n$.
1. If such a closed form solution is not possible,
   then develop some upper or lower bounds
   on the value of $t_n$.


## Induction

The principle of mathematical induction plays a major
role in many important results in enumerative combinatorics.
This is especially relevant for recursively defined
sequences.
We suggest the readers to review the definitions and results
in {ref}`sec:int:math:induction`. 


```{prf:example}
:label: res-comb-fact-n-2-power-ineq

We shall show that

$$
n! \geq 2^n - 2
$$
for every integer $n \geq 2$.

1. Base case: for $n=2$ we have $2! = 2 = 2^2 - 2$.
1. Inductive hypothesis: assume that the statement is
   true for some $k \geq 2$; i.e.,

   $$
   k! \geq 2^k - 2.
   $$
1. Inductive step:
   1. For $k+1$, we have

      $$
      (k+1)! = (k+1) k! \geq (k + 1) (2^k - 2).
      $$
   1. Since $k \geq 2$, hence $k+1 \geq 3$.
   1. Hence
      
      $$
      (k+1)! \geq 3 (2^k - 2)
      = 2 \cdot 2^k + 2^k - 6
      = 2^{k+1} + 2^k - 6.
      $$
   1. Since $k \geq 2$, hence $2^k \geq 4$.
   1. Hence $2^k -6 \geq 4 - 6 = -2$.
   1. Hence

      $$
      (k+1)! \geq 2^{k+1} + 2^k - 6
      \geq 2^{k+1} - 2.
      $$
   1. Thus, the inequality is true for $k+1$ also.
1. Hence, by mathematical induction, the inequality
   holds for every $n \geq 2$.
```


```{prf:example} Sum of first $n$ natural numbers
:label: ex-comb-sum-first-n

The sum for first $n$ natural numbers is given by

$$
1 + 2 + \dots + n = \frac{n (n + 1)}{2}.
$$
We show this equality using a recursively
defined sequence.

1. Let $s_1 = 1$.
1. Let $s_n = s_{n - 1} + n$ for every $n \geq 2$.
1. We can see that $\{ s_n \}$ is a recursively
   defined sequence where the $n$-th term represents
   the sum of first $n$ natural numbers.

We now prove that $s_n =  \frac{n (n + 1)}{2}$
using mathematical induction.

1. For $n=1$, $s_1 = 1 = \frac{1 \cdot 2}{2}$.
1. Assume that the equality is true for some $n$.
1. Then for $n+1$, we have

   $$
   s_{n + 1} = s_n + (n+1)
   &= \frac{n (n + 1)}{2} + n + 1 \\
   &= \frac{n (n + 1) + 2 (n + 1)}{2} \\
   &= \frac{(n + 1)(n + 2)}{2}.
   $$
1. We can see that the equality holds for $n+1$ also.
1. Hence, by mathematical induction, it holds for all $n \geq 1$.
```

### Strong Induction

The following examples require the principle
of strong induction ({prf:ref}`res-int-strong-induction`).

```{prf:example}
:label: ex-comb-ind-2-pow-n

Consider the sequence $\{ t_n \}$ defined as follows:

1. $t_1 = 2$.
1. For every $n \geq 2$,

   $$
   t_n = \sum_{i=1}^{n-1} t_i.
   $$

We can see that

1. $t_2 = t_1 = 2$.
1. $t_3 = t_1 + t_2 = 2 + 2 = 4$.
1. $t_4 = t_1 + t_2 + t_3 = 2 + 2 + 4 = 4 + 4 = 8$.

We now claim that $t_n = 2^{n-1}$ for every $n \geq 2$.
We shall use the strong induction principle
({prf:ref}`res-int-strong-induction`).

1. We are given that $t_1 = 2$.
1. By strong induction hypothesis, let us assume that
   $t_i = 2^{i  - 1}$ for every $i$ with $2 \leq i \leq k$.
1. By the recursive relation, we have

   $$
   t_{k + 1} &= \sum_{i=1}^k t_i \\
   &= t_1 + \sum_{i=2}^k t_i  \\
   &= 2 + \sum_{i=2}^k 2^{i-1} \\
   &= 1 + 2^0 + \sum_{i=1}^{k-1} 2^i\\
   &= 1 + \sum_{i=0}^{k-1} 2^i\\
   &= 1 + 2^k - 1\\
   &= 2^k.
   $$
1. Thus, the equality is true for $k+1$ also.
1. Hence, by principle of strong induction, it is true
   for every $n \geq 2$.
```

```{prf:example} Stacking $n$ disks

You are given $n$ disks. You need to arrange them
into a single tower of disks. You can make small
individual towers of disks and then stack one tower
on top of the some other one.
You are free to make as many towers of disks as you need. 
Each move consists of stacking one tower over the other.
Once a tower has been formed, you are not allowed to
break it. How many moves will it take to
form the single tower?

We claim that it will take $n-1$ moves.

1. Base case: for $n=1$, there is a single disk and it is
   the tower in itself. Hence nothing more is to be done.
   Number of moves required is $0$.
1. Strong induction hypothesis: Assume that
   for some $n=k$, you can make the tower of $i$ disks in $i-1$
   moves for every $i \in 1,\dots,k$.
1. Induction step: Consider the problem of stacking $k+1$ disks.
   1. We can see that the last step consists of stacking
      the last remaining two towers into a single tower.
   1. Assume that the two remaining towers $A$ and $B$ have $j$ and
      $k+1 - j$ disks respectively.
   1. Both towers consist of at least $1$ disk.
   1. Hence neither tower can have $k+1$ disks.
   1. Clearly, $j \leq k$ and $k + 1 - j \leq k$.
   1. It will take $j-1$ moves to form the tower $A$ by induction hypothesis.
   1. It will take $k - j$ moves to form the tower
      $B$ by induction hypothesis.
   1. It will take $1$ more move to stack $A$ and $B$ together.
   1. Hence total number of moves required is

      $$
      j - 1 + k - j + 1 = k.
      $$
   1. Hence to stack a tower of $k+1$ disks, we need $k$ moves.
1. We can see that by strong induction, for every $n$, it takes
   $n-1$ moves to stack the $n$ disks into a single tower.
```

## Pigeonhole Principle

Pigeonhole principle is one of the most powerful
counting arguments.

```{index} Pigeonhole principle
```
```{prf:theorem} Pigeonhole principle
:label: res-comb-pigeonhole-principle

If there are $n$ objects that fall into $m$ different
categories and $n > m$, then at least two of the objects
fall into the same category.
```

If there are $m$ pigeonholes and $n$ pigeons with
$n > m$, then at least one pigeonhole must hold more
than one pigeons. The name of this principle comes
from the example of pigeons as objects and pigeonholes
as categories.

```{prf:proof}
We argue as follows.

1. Consider the first $m$ objects.
1. If any two of these objects belong to the same
   category, then we are done.
1. Otherwise, there is exactly one object for each of
   the $m$ categories from this set of first $m$ objects.
1. There are $n - m > 0$ objects still left. Hence
   there is at least one more object.
1. This object must fall into one of the $m$ categories.
1. This category will then have at least $2$ items.
```


```{prf:example} Sock-picking
:label: ex-comb-pigeonhole-sock-picking

Assume that a drawer contains socks
of two colors (blue and black). 
The socks can be worn on either foot.
We are pulling the socks from the
drawer without looking at them.
What is the minimum number of socks
we need to pull so that we are
guaranteed to have a pair of same color?

1. Socks are the objects.
1. Each color can be considered as a category.
1. There are thus $m=2$ categories.
1. We need more than one sock in at least one category.
1. If $n > m = 2$, then we have at least one color
   for which we have two or more socks.
1. Minimum value of $n$ satisfying $n > m$ is $3$.
1. Thus, we need to draw at least $3$ socks to
   guarantee that we have one pair of same color.
```

```{prf:example} Hand-shaking
:label: ex-comb-pigeonhole-hand-shaking

Let there be $n$ people in a room with $n >1$
They are shaking hands with each other.
Then there is always a pair of people who
will shake hands with the same number of people.

1. One person can shake hands with
   at the minimum $0$ number of people
   and at the maximum $n-1$ number of people.
1. We define the categories as the number of
   people to which one has shaken hands.
1. Thus, the categories are labeled $0,1,2,\dots,n-1$.
1. We can see that there are $n$ categories and $n$ people.
1. However, the category $0$ and category $n-1$ cannot both
   have a person simultaneously. 
   1. Suppose there is someone who has shaken hands with no one.
   1. Then there cannot be anyone who has shaken hands with everyone.
   1. Hence if category $0$ is nonempty, then category $n-1$ must be empty.
   1. Now suppose there is someone who has shaken hands with everyone.
   1. Then there cannot be anyone who has shaken hands with no one.
   1. Hence if category $n-1$ is nonempty, then category $0$ must be empty.
1. Thus, either $0$ or $n-1$ or both must be empty.
1. Hence the $n$ people must be fitted into at most $n-1$ categories.
1. By pigeonhole principle, at least one of these categories must have
   more than one person.
```

```{prf:example} Hair counting
:label: ex-comb-pigeonhole-hair-count

At any given time there live at least two people in California
with the same number of hairs on their heads.


1. The current population of California is around $40$ million.
1. Typical human head has an average of about $150,000$ hairs.
1. An upper bound on the number of hairs on human head is $1$ million.
1. Hence by pigeonhole principle, there must be people in California
   with the same number of hairs on their heads.
```

```{prf:example} Subset sum
:label: ex-comb-pigeonhole-subset-sum

Consider the set $S = \{1,2,3,4,5,6,7,8,9 \}$. 
We claim that every $6$ element subset of $S$
must contain at least two numbers whose sum is $10$.

1. Let us first identify which pairs of numbers sum to $10$.
1. We can see that $1+9=2+8=3+7=4+6=10$. There are $4$ such pairs.
1. We now split the $9$ numbers to $5$ categories as follows:
   1. $1,9 \to A$
   2. $2,8 \to B$
   3. $3,7 \to C$
   4. $4,6 \to D$
   5. $5 \to E$.
1. Consider any subset of $S$ of $6$ elements. 
1. Let its members be $\{ n_1, n_2, n_3, n_4, n_5, n_6 \}$.
1. Put these numbers into the $5$ categories above
   based on rule that a number should go into the category mapped for it.
1. There are $5$ categories and $6$ numbers.
1. By pigeonhole principle, at least one of the categories should have
   more than one number.
1. Category $E$ cannot have two numbers. It can only have $5$.
1. Hence, at least one of $A, B, C, D$ has two numbers.
1. But each of these categories consist of two numbers whose sum is $10$.
1. Hence every $6$ element subset of $S$
   must contain at least two numbers whose sum is $10$.
```

## Generating Functions

A generating function is a way of encoding an
infinite sequence of numbers $\{ t_n \}$ by
treating them as the coefficients of a formal
power series.


```{prf:definition} Ordinary generating function
:label: def-comb-ogf

The *ordinary generating function* of a sequence
$t_0, t_1, \dots, t_n, \dots$ is given by

$$
G(t_n; x) \triangleq \sum_{n=0}^{\infty} t_n x^n
= t_0 + t_1 x^1 + t_2 x^2 + \dots + t_n x^n + \dots.
$$
```

A generating function is not evaluated for any specific
value of $x$. It is a formal structure which enables
us to manipulate the sequences more conveniently.

```{prf:definition} Exponential generating function
:label: def-comb-egf

The *exponential generating function* of a sequence
$t_0, t_1, \dots, t_n, \dots$ is given by

$$
E(t_n; x) \triangleq \sum_{n=0}^{\infty} t_n \frac{x^n}{n!}.
$$
```

### Generalized Binomial Theorem

Recall from {prf:ref}`res-comb-binomial-theorem`
that for a nonnegative integer $n$, we have

$$
(1 + x)^n = \sum_{r=0}^n \binom{n}{r} x^r.
$$
We now wish to generalize it for negative $n$ also.


```{index} Generalized binomial coefficient
```
```{prf:definition} Generalized binomial coefficient
:label: def-comb-gen-binom-coef

For any real $n$ and any nonnegative integer $r$, the
*generalized binomial coefficient* is defined as

$$
{n \choose r} = \frac{n (n-1) \dots (n - r + 1)}{r!}.
$$
```
Note that for a nonnegative $n$ and $r \leq n$, the
definition agrees with the binomial coefficient
as defined in {prf:ref}`def-comb-binom-coef`.


```{prf:theorem} Binomial coefficient for negative integers
:label: res-comb-neg-binom-ceof

If $n$ is a positive integer, then

$$
{-n \choose r} = (-1)^r {n + r - 1 \choose r}.
$$
```

```{prf:proof}
We have

$$
{-n \choose r} = \frac{-n (-n-1) \dots (-n - r + 1)}{r!}.
$$
1. Factoring $-1$ out of each term in the R.H.S. numerator
   gives us

   $$
   & (-1)^r \frac{n (n+1) \dots (n + r - 1)}{r!} \\
   &= (-1)^r \frac{(n + r - 1) \dots  (n+1)  n }{r!}\\
   &= (-1)^r \frac{(n + r - 1) \dots  (n+1)  n (n-1) \dots 1 }{r! (n-1)!}\\
   &= (-1)^r \frac{(n +r - 1)!}{r! (n-1)!} \\
   &= (-1)^r {n + r - 1 \choose r}.
   $$
```

```{prf:theorem} Generalized binomial theorem
:label: res-comb-gen-binom-thm

For any $n \in \RR$, we have

$$
(1 + x)^n = \sum_{r=0}^{\infty} {n \choose r} x^r.
$$
```

```{prf:example}
:label: ex-comb-gen-func-1

We shall show that

$$
(1-x)^{-1} = 1 + x + x^2 + \dots.
$$


1. Let $y = -x$.
1. Then $(1-x)^{-1} = (1 + y)^{-1}$.
1. By {prf:ref}`res-comb-gen-binom-thm`,

   $$
   (1 + y)^{-1} = \sum_{r=0}^{\infty} {-1 \choose r} y^r
   $$
1. By {prf:ref}`res-comb-neg-binom-ceof`

   $$
   {-1 \choose r} = (-1)^r {1 + r - 1 \choose r}
   = (-1)^r  { r \choose r} = (-1)^r.
   $$
1. Hence

   $$
   (1 + y)^{-1} = \sum_{r=0}^{\infty} (-1)^r y^r.
   $$
1. But $y^r = (-x)^r = (-1)^r x^r$.
1. Putting back, we get

   $$
   (1 - x)^{-1} = \sum_{r=0}^{\infty} (-1)^r (-1)^r x^r
   = \sum_{r=0}^{\infty} x^r.
   $$
```


