# Combinatorics

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

