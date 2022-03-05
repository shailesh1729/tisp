(sec:ms:metric-topology)=
# Metric Topology

In this section, we shall assume $(X,d)$ to be a metric space;
i.e., $X$ is a set endowed with a metric $d : X \times X \to \RR$.


## Topology

```{prf:definition} Topology
:label: def-ms-topology

For a given set $X$, let $T$ be a family of
subsets of $X$. The family $T$ is called
a topology if

1. Both the empty set $\EmptySet$ and $X$ are elements of $T$.
1. Any union of elements of $T$ is an element of $T$.
1. Any intersection of a finitely many elements of $T$ 
   is an element of $T$. 

In other words, $T$ contains $\EmptySet$ and $X$,
is closed under arbitrary union and is closed under
finite intersection. 
```
The elements of a topology $T$ are called open sets
of the topology. Their complements are called closed
sets. It is possible to introduce different topologies
to the same set $X$.
A set equipped with a topology is called a topological
space. A topological structure enables us to define
all kinds of continuity. 

There are several properties of geometrical objects
which don't depend on the exact shape of an object and
are preserved under continuous deformations like
stretching, twisting, crumpling and bending. 
Some of these properties include the dimension, 
compactness, connectedness, etc.. 

A metric $d$ imposes a topological structure on a set $X$.
This section develops the topological structure of
metric spaces. 


## Balls

```{prf:definition} Open ball
:label: def-ms-open-ball

Given a point $x \in X$ and $r > 0$, the set

$$
    B(x,r)  \triangleq \{y \in X \ST d(x, y) < r\}
$$

is called an *open ball* at $x$ with radius $r$ in $X$. 
```

This definition is a generalization of the concept of
{prf:ref}`neighborhood <def-bra-neighborhood>` on a real line.


```{prf:definition} Closed ball
:label: def-ms-closed-ball

Given a point $x \in X$ and $r > 0$, the set

$$
    B[x,r]  \triangleq \{y \in X \ST d(x, y) \leq r\}
$$

is called a *closed ball* at $x$ with radius $r$ in $X$. 
```

## Open Sets

```{prf:definition} Open sets
:label: def-ms-open-set

A subset $S$ of $X$ is said to be *open* in $X$ 
if for every $x \in S$ there exists an "open ball" entirely
within $S$. 

In other words, there exists an $r > 0$ such that
$B(x, r) \subseteq S$. 
```

```{prf:theorem}
:label: res-ms-open-ball-open-set

Every open ball is an open set.
```

```{prf:proof}
Let $x \in X$ and consider the open ball 

$$
    A = B (x, \epsilon)  = \{y \in X \ST d(x, y) < \epsilon\}
$$

for some $\epsilon > 0$. We need to show that for every point
in $A$, there exists an open ball entirely contained in $A$.

Let $p \in A$. Let $r = \epsilon - d(x,p)$. By definition $r > 0$.

Consider the open ball:

$$
    S = B(p, r)  = \{y \in X \ST d(p, y) < r\}.
$$

For any $y \in S$, 

$$
d(x, y) \leq  d(x, p) + d(p, y) < d(x, p) + r  = \epsilon.
$$
Thus, $y \in A$. Thus, $S \subseteq A$. Thus, there exists
an open ball around $p$ which is entirely contained in $A$. 
```

```{prf:theorem}
:label: res-ms-union-open-sets

Arbitrary unions of open sets are open sets.
```

```{prf:proof}
We prove this by showing that for every element in an
arbitrary union of open sets, there exists an open ball around 
it entirely contained inside the union.

1. Let $\{ A_i \}_{i \in I}$ be a family of open subsets of $X$.
1. Let $A = \bigcup_{i \in I}A_i$. 
1. Let $x \in A$. 
1. Then, there exists an $i \in I$ such that $x \in A_i$. 
1. Since $A_i$ is open, there exists an open ball 
   $B(x, r) \subseteq A_i \subseteq A$.
1. Hence, $A$ is open.
```

```{prf:theorem}
:label: res-ms-finite-intersect-open-sets

Finite intersections of open sets are open sets.
```

```{prf:proof}
We prove this by showing that for every element in a
finite intersection of open sets, there exists an open ball around 
it entirely contained inside the intersection.

1. Let $\{A_1, A_2, \dots, A_n\}$ be a finite collection of open subsets of $X$.
1. Let $A = \bigcap_{i=1}^n A_i$.
1. Let $x \in A$. Then $x \in A_i \Forall 1 \leq i \leq n$.
1. Thus, for each $1 \leq i \leq n$, there exists an open ball $B(x, r_i) \subseteq A_i$.
1. Let $r = \min \{ r_1, r_2, \dots, r_n \}$. Since $r_i > 0$, hence $r > 0$.
1. Thus, we can construct an open ball $B(x, r)$ at $x$.
1. Note that $B(x, r) \subseteq B(x, r_i) \subseteq A_i$.
1. In other words, $B(x, r) \subseteq A_i \Forall 1 \leq i \leq n$.
1. Thus, $B(x, r) \subseteq A$.
1. Thus, for every $x \in A$, there exists an open ball at $x$ entirely contained in $A$.
1. Thus, $A$ is open.
```

```{prf:remark}
:label: res-ms-empty-whole-open

The empty set $\EmptySet$ and $X$ are both open. 

$\EmptySet$ is vacuously open since it contains
no elements. Consequently, the requirement that an open 
ball surrounding every element of $\EmptySet$
be contained within $\EmptySet$ is vacuously true.

$X$ is open since for every $x \in X$, any open ball $B(x,r)$
is entirely contained within $X$ by definition.
```

```{prf:theorem} Metric topology
:label: res-ms-metric-topology

Let $(X, d)$ be a metric space. Then, the family of 
{prf:ref}`open sets <def-ms-open-set>` determined by
the metric $d$ satisfies all the requirements of
a {prf:ref}`topology <def-ms-topology>`.
This topology is known as the *metric topology* 
determined by the metric $d$ on the set $X$.
```
```{prf:proof}
By {prf:ref}`res-ms-empty-whole-open`, $\EmptySet$ and $X$ are open.

By {prf:ref}`res-ms-union-open-sets`, arbitrary union of
open sets is also an open set.

By {prf:ref}`res-ms-finite-intersect-open-sets`, a finite
intersection of open sets is also an open set.

Thus, the family of open sets determined by a metric $d$ is
closed under arbitrary union and finite intersection.

Hence, it is a topology.
```

## Closed Sets

```{prf:definition} Closed sets
:label: def-ms-closed-set

A subset $S$ of $X$ is said to be *closed* in $X$ 
if $X \setminus S$ is open in $X$.
```

```{prf:theorem} Trivially closed and open sets
:label: res-ms-empty-whole-clopen

$\EmptySet$ and $X$ are both open and closed subsets of $X$.
```

```{prf:proof}
$\EmptySet$ is vacuously open since it has no points
thus every point in $\EmptySet$ has an open ball that lies
within $\EmptySet$. Thus, $X$ is closed.

$X$ is open since for every point $x \in X$, every open ball at $x$
lies entirely in $X$ (by definition). Thus, $\EmptySet$ is closed.
```

```{prf:theorem} Singletons are closed
:label: res-ms-singleton-closed

Every singleton is a closed set.
```

```{prf:proof}
Let $x \in X$ and consider the singleton set $A = \{x\}$.

Let $B = X \setminus A$. We show that $B$ is open. Then $A$ is closed.

1. Let $y \in B$
1. Let $r = d(x, y)$. 
1. Then, the open ball
   $B(y, r)$ doesn't contain $x$. 
1. Thus, $B(y, r) \subseteq B$. 
1. Thus, $B$ is open.
```

```{prf:example}
:label: ex-clopen-examples-1

* $(0, 1)$ is open in $\RR$.
* $[0, 1]$ is closed in $\RR$.
* $(0, 1]$ is neither open nor closed in $\RR$.
```

```{prf:proposition}
:label: res-ms-nat-is-closed

The set of natural numbers $\Nat$ is closed in $\RR$.
```

```{prf:proof}
We prove it by showing that its complement is open.
The set $\RR \setminus \Nat$ can be written as a union of open intervals:

$$ 
\RR \setminus \Nat = \bigcup \left \{ (-\infty, 1), (1, 2), (2, 3), 
\dots, (n, n+1), \dots \right \}.
$$ 

1. Each open interval is an open set.
1. The arbitrary union of open sets is open.
1. Thus, $\RR \setminus \Nat$ is open.
1. Thus, $\Nat$ is closed. 

```

```{prf:theorem}
:label: res-ms-intersection-closed-sets

Arbitrary intersections of closed sets are closed sets.
```

```{prf:proof}
We proceed as follows:

1. Let $\{ A_i \}_{i \in I}$ be a family of closed subsets of $X$.
1. Then $\{ X \setminus A_i \}_{i \in I}$ is a family of open subsets of $X$.
1. Then, their union $\bigcup_{i \in I} (X \setminus A_i)$ is an open set.
1. Hence, its complement $X \setminus \bigcup_{i \in I} (X \setminus A_i)$ is a closed set.
1. But, by De Morgan's law: $X \setminus \bigcup_{i \in I} (X \setminus A_i) = \bigcap_{i \in I} A_i$.
1. Thus, $ \bigcap_{i \in I} A_i$ is a closed set.
```

```{prf:theorem}
:label: res-ms-finite-union-closed

Finite unions of closed sets are closed sets.
```

```{prf:proof}
We proceed as follows:

1. Let $\{A_1, A_2, \dots, A_n\}$ be a finite collection of closed subsets of $X$.
1. Then, $\{X \setminus A_1, X \setminus A_2, \dots, X \setminus A_n\}$ are open.
1. Then, their union $\bigcup_{i=1}^n X \setminus A_i$  is  open.
1. Then, its complement $X \setminus \bigcup_{i=1}^n X \setminus A_i$ is closed.
1. By De Morgan's law:
   $X \setminus \bigcup_{i=1}^n X \setminus A_i = \bigcap_{i=1}^n A_i$.
1. Thus, $\bigcap_{i=1}^n A_i$ is a closed set.
```

## Interior

```{prf:definition} Interior point
:label: def-ms-interior-point

A point $x$ is called an interior point of a set $A \subseteq X$ if there
exists an open ball $B(x, r)$ such that $B(x, r) \subseteq A$. 
```

By definition an interior point of a set belongs to the set too.
$x \in B(x, r) \subseteq A$. 

```{prf:definition} Interior
:label: def-ms-interior

Let $A \subseteq X$. The largest open set in $X$ that is contained
in $A$ is called the *interior* of $A$ (relative to $X$)
and is denoted by $\interior A$ or $\ainterior_X A$.
```
Note that $\interior A \subseteq A$.

```{prf:proposition}
:label: res-ms-open-subset-interior-subset

Let $O \subseteq A$ be an open set. Then $O \subseteq \interior A$. 

In words, every open set that is contained in $A$, is 
contained in its interior.
```

```{prf:proof}
Since $O$ and $\interior A$ are open sets, hence their union
$O \cup \interior A$ is open. But $O \subseteq A$ and 
$\interior A \subseteq A$ implies $O \cup \interior A \subseteq A$.
Also, $\interior A \subseteq O \cup \interior A$. 
But $\interior A$ is the largest open subset of $A$. Thus,
$\interior A = O \cup \interior A$. Thus, $O \subseteq \interior A$.
```


```{prf:theorem} Interior is set of interior points
:label: res-ms-interior-as-set-points

The interior of a set $A$ is the collection of all the interior points 
of $A$.
```

```{prf:proof}
Let $I$ be the collection of all interior points of $A$. 
Thus, $I \subseteq A$. Our claim is that $I = \interior A$.

We first show that  $I \subseteq \interior A$.
Let $x \in I$. 
Then, there exists an open ball $B(x, r_x) \subseteq A$.
Then, the union $C = \bigcup_{x \in I} B(x, r_x) \subseteq A$.
But $C$ is an arbitrary union of open sets. Hence $C$ is open.
But every open subset of $A$ is a subset of $\interior A$. 
Thus,  $C \subseteq \interior A$. 
Also $I \subseteq C \implies I \subseteq \interior A$.

For the converse, we proceed as follows. 

$\interior A$ is open. 
Thus, for every $x \in \interior I$, 
there exists an open ball $B(x, r_x) \subseteq I \subseteq A$.
Thus, $x$ is an interior point of $A$. 
In other words, $\interior A \subseteq I$.
```

This result is simply a different characterization of the
interior of $A$. We could have started with the definition
that the interior is the set of all interior points and then
proved that it is the largest open set contained in $A$.


```{prf:proposition}
:label: res-ms-open-set-interior

$A$ is open if and only if $A = \interior A$. 
```

```{prf:proof}
Assume, $A$ is open. 
Then, $A$ is the largest open set contained in $A$.
Hence, $A = \interior A$.

Assume $A = \interior A$. 
Then, since $\interior A$ is open, hence $A$ is open.
```

```{prf:theorem}
:label: res-ms-interior-inclusion

If $A \subseteq B$ then $\interior A \subseteq \interior B$.
```
```{prf:proof}
We have:

$$
\interior A \subseteq A \subseteq B.
$$
But $\interior A$ is open. 
Hence, by {prf:ref}`res-ms-open-subset-interior-subset`:

$$
\interior A \subseteq \interior B.
$$

Alternate proof.

1. Let $x$ be an interior point of $A$.
1. Then $x$ is an interior point of $B$ too since $A \subseteq B$.
1. Thus, $x \in \interior B$.
1. Thus $ \interior A \subseteq \interior B$.
```


## Closure

```{prf:definition} Closure point
:label: def-ms-closure-point

A point $x \in X$ is called a *closure point* of a subset $A$ of $X$ 
if every open ball at $x$ contains (at least) one point in $A$.

In other words:

$$
B(x, r) \cap A \neq \EmptySet \Forall r > 0.
$$
```

```{prf:proposition}
:label: res-ms-members-closure-points

Every point in $A$ is a closure point of $A$.
```

```{prf:proof}
Let $x \in A$. Then $x \in B(x, r)$ for every $r > 0$. 
Thus, $x \in B(x, r) \cap A$ for every $r > 0$.
Thus, $B(x, r) \cap A$ is not empty for every $r > 0$.
Thus, $x$ is a closure point of $A$.
```

```{prf:definition} Closure
:label: def-ms-closure

Let $A \subseteq X$. The smallest closed set in $X$ that contains
$A$ is called the *closure* of $A$ (relative to $X$)
and is denoted by $\closure A$ or $\aclosure_X A$.
```

```{prf:proposition}
:label: res-ms-closed-superset-closure-superset

Let $C$ be a closed subset of $X$ such that $A \subseteq C$.
Then $\closure A \subseteq C$.

In words, every closed set that contains $A$, contains
its closure.
```

```{prf:proof}
Consider the set $D = C \cap \closure A$. Since, intersection
of two closed sets is closed, hence $D$ is closed. 
Since $A \subseteq C$ and $A \subseteq \closure A$, hence
$A \subseteq D$. At the same time, $D \subseteq \closure A$.
Thus, we have $A \subseteq D \subseteq \closure A$.
But $\closure A$ is the smallest closed set containing $A$.
Hence, $D = \closure A$ must be true.
But $D \subseteq C$. Hence $\closure A \subseteq C$.
```

```{prf:theorem} Closure is set of closure points
:label: res-closure-set-closure-points

The closure of a set $A$ is the collection of all the closure points 
of $A$.
```

```{prf:proof}
Let $D$ be the set of all closure points of $A$. 

We first show that $D$ is a closed set.

1. Let $x \notin D$ (i.e. $x \in X \setminus D$). 
1. Then, there exists an open ball $B(x, r)$ 
   such that $B(x, r) \cap A = \EmptySet$.
1. For any $y \in B(x, r)$, then, there exists an open ball $B(y, s)$
   such that $B(y, s) \subseteq B(x, r)$ (since $B(x,r)$ is an open set).
1. Thus, $B(y, s)\cap A = \EmptySet$. 
1. Hence, $y \notin D$.
   In other words, the open ball $B(x, r)$ doesn't contain 
   any closure point of $A$.
1. Thus, $B(x, r) \subseteq X \setminus D$.
1. Thus, for every point $x \in X \setminus D$, there exists an open ball
   $B(x, r) \subseteq X \setminus D$. 
1. Thus, $X \setminus D$ is open.
1. Consequently, $D$ is closed.

Next, we show that $\closure A \subseteq D$.

1. Since every point of $A$ is a closure point, hence $A \subseteq D$.
1. Since $\closure A$ is a subset of any closed set containing $A$, 
   hence $\closure A \subseteq D$.

Last, we show that $D \subseteq \closure A$.
In fact, we show a stronger result that $D \subseteq C$ 
for any closed $C \supseteq  A$.

1. Let $C$ be a closed set such that $A \subseteq C$.
1. Then, $X \setminus C$ is open.
1. For any $x \in X \setminus C$, there exists an open ball 
   $B(x, r) \subseteq X \setminus C$. 
1. Thus, $B(x, r) \cap C = \EmptySet$.
1. In particular, $B(x, r) \cap A = \EmptySet$ (since $A \subseteq C$).
1. Thus, $x$ is not a closure point of $A$ (i.e. $x \notin D$).
1. Thus, no point in $X \setminus C$ is a closure point.
1. Thus, every closure point belongs to $C$.
1. Thus, $D \subseteq C$.
1. We have established that $D$ is a subset of any closed set that contains $A$.
1. In particular, $D \subseteq \closure A$ since $\closure A$ is closed 
   and $A \subseteq \closure A$ (by definition). 

Together, $D = \closure A$.
```

This result is simply a different characterization of the
closure of $A$. We could have started with the definition
that the closure is the set of all closure points and then
proved that it is the smallest closed set containing $A$.

```{prf:proposition}
:label: res-ms-closed-set-closure

$A$ is closed if and only if $A = \closure A$. 
```

```{prf:proof}
Assume, $A$ is closed. 
Then, $A$ is the smallest closed set containing $A$.
Hence, $A = \closure A$.

Assume $A = \closure A$. 
Then, since $\closure A$ is closed, hence $A$ is closed.
```

```{prf:theorem}
:label: res-ms-closed-ball-closed-set

A closed ball is a closed set.
```

```{prf:proof}
Let $x \in X$. Let $r > 0$. Let

$$
C = B[x, r] = \{y \in X \ST d(x, y) \leq r\}
$$
be a closed ball.
We proceed by showing that its complement is open:

1. Let $y \in X \setminus C$. Then $d(x, y) > r$.
1. Let $r_1 = d(x, y) - r > 0$. 
1. Consider the open ball $B(y, r_1)$.
1. For any $z \in B(y, r_1)$:

   $$
   d(x, y) \leq d(x, z) + d(z, y) < d(x, z) + r_1
   \implies d(x, z) > d(x, y) - r_1 = r. 
   $$
1. Thus, $z \notin C$, i.e. $z \in X \setminus C$.
1. Thus, $B(y, r_1) \subseteq X \setminus C$.
1. In other words, for every point in $X \setminus C$, there
   exists an open ball contained in $X \setminus C$.
1. Thus, $X \setminus C$ is an open set.
1. Thus, $C$ is closed.
```

```{prf:theorem}
:label: res-ms-int-cl-comp-rel

Let $A \subseteq X$. Then

$$
X \setminus (\interior A) = \closure (X \setminus A).
$$

In words, complement of interior is the closure of the complement.
```

```{prf:proof}

We proceed as follows:

1. Let $x \in X \setminus (\interior A)$, 
   i.e., $x$ is not an interior point of $A$.
1. Then, for every $r > 0$, $B(x, r)$ is not a subset of $A$.
1. Thus, for every $r > 0$, $B(x, r) \cap X \setminus A$ is not empty.
1. Thus, $x$ is a closure point of $X \setminus A$.
1. Thus, $X \setminus (\interior A) \subseteq \closure (X \setminus A)$.

The same logic for the converse:

1. Let $x \in \closure (X \setminus A)$, 
   i.e., $x$ is a closure point of $X \setminus A$.
1. Thus, for every $r > 0$, $B(x, r) \cap (X \setminus A)$ is not empty.
1. Thus, for every $r > 0$,  $B(x, r)$ is not a subset of $A$.
1. Thus, $x$ is not an interior point of $A$.
1. Thus, $\closure (X \setminus A) \subseteq X \setminus (\interior A)$.

Together, the equality is established. 
```

```{prf:theorem}
:label: res-ms-closure-inclusion

If $A \subseteq B$ then $\closure A \subseteq \closure B$.
```
```{prf:proof}
We have: $A \subseteq \closure A$ and 
$A \subseteq B \subseteq \closure B$.
But then by {prf:ref}`res-ms-closed-superset-closure-superset`
every closed set that contains $A$ contains its closure.
Thus:

$$
 \closure A \closure B.
$$

Alternate proof.

1. Let $x$ be a closure point of $A$.
1. Then $x$ is a closure point of $B$ too since $A \subseteq B$.
1. Thus, $x \in \closure B$.
1. Thus $ \closure A \subseteq \closure B$.
```

```{prf:theorem}
:label: res-ms-closure-union-contains

Closure of union contains union of closures.
```
```{prf:proof}
Let $\AA$ be a family of subsets of $X$.
Let

$$
K = \bigcup_{A \in \AA} A.
$$

Let 

$$
L = \bigcup_{A \in \AA} \closure A.
$$

1. Let $x \in L$.
1. Then $x \in \closure A$ for some $A \in \AA$.
1. Then $x$ is a closure point of some $A \in \AA$.
1. Then $x$ is a closure point of $K$.
1. Thus, $x \in \closure K$.

We arrive at the result:

$$
\bigcup_{A \in \AA} \closure A \subseteq \closure \left ( \bigcup_{A \in \AA} A \right ).
$$
```

```{prf:theorem}
:label: res-ms-closure-finite-union-equal

Closure of a finite union is equal to the union of closures.

$$
\bigcup_{i=1}^n (\closure A_i) = \closure \left ( \bigcup_{i=1}^n A_i \right).
$$
```

```{prf:proof}
Let $\{ A_1, A_2, \dots, A_n\}$ be a finite family of subsets of $X$.

Let 

$$
K = \bigcup_{i=1}^n A_i.
$$

Let 

$$
L = \bigcup_{i=1}^n (\closure A_i).
$$

From the previous result, we have established that

$$
L \subseteq \closure K.
$$

We now seek to prove that $\closure K \subseteq L$.

1. $\closure A_i$ are closed.
1. $L$ is a finite union of closed sets.
1. Hence, $L$ is closed due to {prf:ref}`res-ms-finite-union-closed`.
1. $A_i \subseteq \closure A_i$.
1. Thus, $\bigcup A_i \subseteq \bigcup \closure A_i$.
1. Thus, $K \subseteq L$.
1. Thus, $\closure K \subseteq L$ 
   due to {prf:ref}`res-ms-closed-superset-closure-superset`.
```

## Boundary

```{prf:definition} Boundary point
:label: def-ms-boundary-point

A point $x \in X$ is called a *boundary point* of $A$ if
every open ball $B(x, r)$ at $x$ contains points from 
$A$ as well as $X \setminus A$. 

In other words, $B(x, r) \cap A \neq \EmptySet$ 
and $B(x, r) \cap X \setminus A \neq \EmptySet$
for every $r> 0$. 
```

```{prf:definition} Boundary
:label: def-ms-boundary

The *boundary* of a set $A \subseteq X$ (relative to $X$), 
denoted by $\boundary A$ or $\aboundary_X A$ is defined as
the set of all boundary points of $A$.
```

```{prf:theorem}
:label: res-ms-bd-cl-int-relation

$$
\boundary A = \closure A \setminus \interior A.
$$
```

```{prf:proof}
Let $x$ be a boundary point of $A$. 

1.  $B(x, r) \cap A \neq \EmptySet$ for every $r > 0$.
1. Thus $x$ is a closure point of $A$.
1. $B(x, r) \cap X \setminus A \neq \EmptySet$ for every $r > 0$.
1. Thus, there is no $r > 0$ such that $B(x,r) \subseteq A$.
1. Thus, $x$ is not an interior point of $A$.
1. Thus, $x \in \closure A \setminus \interior A$.
1. Thus, $\boundary A \subseteq \closure A \setminus \interior A$.

Let $x \in \closure A \setminus \interior A$.

1. $x$ is a closure point.
1. Thus, $B(x, r) \cap A \neq \EmptySet$ for every $r > 0$.
1. $x$ is not an interior point.
1. Thus, there is no $r > 0$ such that $B(x,r) \subseteq A$.
1. Thus, for every $r> 0$, $B(x,r) \cap X \setminus A \neq \EmptySet$.
1. Combining, $x$ is a boundary point.
1. Thus, $\closure A \setminus \interior A \subseteq \boundary A$.
```

```{prf:proposition}
:label: res-ms-bd-is-closed

Boundary of a set is closed.
```

```{prf:proof}
By definition: 

$$
\boundary A = \closure A \setminus \interior A = \closure A \cap (X \setminus \interior A).
$$

1. $\interior A$ is open. Hence $X \setminus \interior A$ is closed.
1. $\closure A$ is closed.
1. Thus, $\boundary A$ is an intersection of two closed sets.
1. Thus, $\boundary A$ is closed ({prf:ref}`res-ms-intersection-closed-sets`). 
```

## Frontier


```{prf:definition} Frontier point
:label: def-ms-frontier-point

A *frontier point* of a set $A$ is a boundary point
that belongs to $A$.
```

```{prf:definition} Frontier
:label: def-ms-frontier

The set of all frontier points of a set $A$,
denoted by $\frontier A$, is called
its *frontier*.
```

```{note}
Some authors treat boundary points as frontier points. 
They treat boundary and frontier as synonymous.
There is no consistent terminology for the set 
$A \setminus \interior A$. 
Our definitions distinguish between boundary points
and frontier points.
```

```{prf:proposition}
:label: res-ms-front-int-bd-rel

$$
\frontier A = A \setminus \interior A = \boundary A \cap A.
$$
```
```{prf:proof}
$\frontier A = \boundary A \cap A$ is by definition as 
a frontier point is a boundary point which belongs to $A$.

If $x \in A$ is an interior point then it's not a boundary point.
All other points in $A$ are boundary points. Hence,

$$
\frontier A = A \setminus \interior A.
$$
```

```{prf:proposition}
:label: res-ms-closed-front-bd

For a closed set, the frontier and boundary are same.
```
```{prf:proof}
Every boundary point belongs to the closed set.
```

```{prf:proposition}
:label: res-ms-closed-front

The frontier of a closed set is closed.
```

```{prf:proof}
For a closed set $\frontier A = \boundary A$. The 
boundary of any set is closed. 
```

## Accumulation

```{prf:definition} Deleted neighborhood
:label: def-ms-del-neighborhood

Let $x \in X$. The *deleted neighborhood* of radius $r$
around $x$ is defined as the open ball of radius $r$ around $x$ 
excluding $x$ itself.

$$
B_d(x, r) = B(x, r) \setminus x.
$$
```


```{prf:definition} Accumulation point
:label: def-ms-accumulation-point

A point $x \in X$ is called an *accumulation point* of a set $A \subseteq X$,
if every open ball $B(x,r)$ contains a point in $A$ distinct from $x$.

$$
B(x, r) \cap A \setminus \{ x \} \neq \EmptySet \Forall r > 0.
$$

In other words, every deleted neighborhood of $x$ contains
a point from $A$.

$$
B_d(x, r) \cap A \neq \EmptySet \Forall r > 0.
$$
```

Note that an accumulation point need not belong to the set $A$.

```{prf:remark} 
:label: res-ms-acc-closure-pnt

Every accumulation point is a closure point.
```


Although, every closure point need not be an accumulation point.

```{prf:definition} Derived set
:label: def-ms-derived-set

The set of accumulation points of a set $A$ is called its *derived set* 
and is denoted by $A'$.
```

```{prf:definition} Isolated point
:label: def-ms-isolated-point

A point $x \in A$ is called isolated if there is an open ball
$B(x, r)$ which doesn't contain any other point of $A$.

In other words, there exists an $r > 0$ such that:

$$
B(x, r) \cap A \setminus \{ x \} = \EmptySet.
$$
```

```{prf:proposition} 
:label: res-ms-closure-pt-acc-isolated

A closure point is either an accumulation point or an isolated point.
```

```{prf:proof}
Let $x \in \closure A$. Assume that $x$ is not an accumulation point.

We need to show that $x \in A$ and $x$ is isolated.

1. Since $x$ is not an accumulation point, there exists $r > 0$ such that 
   $B(x, r) \cap A \setminus \{ x \} = \EmptySet$.
1. Since $x$ is a closure point, hence 
   $B(x,r) \cap A$ is not empty.
1. Then, $B(x, r) \cap A$ must be $\{ x \}$. 
1. Thus, $x \in A$.
1. Finally, since $B(x, r) \cap A \setminus \{ x \} = \EmptySet$, 
   $x$ is an isolated point of $A$.
```


```{prf:proposition} 
:label: res-ms-closure-set-derived-rel

$$
\closure A = A \cup A'.
$$
```
This is a restatement of the previous result.

```{prf:theorem}
:label: res-ms-closed-set-accumulation-all

A set is closed if and only if it contains all its accumulation points.
```

```{prf:proof}
$A' \subseteq A \implies A \cup A' = A$. But $A \cup A' = \closure A$.
Thus, $A' \subseteq A \implies A = \closure A$.

$A = \closure A \implies  A =  A \cup A' \implies A' \subseteq A$.
```

Recall that $d(x,A)$ denotes the
{prf:ref}`distance <def-ms-point-set-distance>` 
between a set $A$ and a point $x$.

```{prf:theorem}
:label: res-ms-set-accumulation-point-distance

If $x$ is an accumulation point of $A$ then 
$d(x, A) = 0$.
```

```{prf:proof}

Let $x$ be an accumulation point of $A$.

1. If $x \in A$ then $d(x,A) = 0$. 
1. So consider the case where $x \notin A$.
1. For every $r > 0$, there exists $a \in A$ 
   such that $d(x, a) < r$.
1. Thus, $d(x,A) < r$ for every $ r > 0$.
1. At the same time, $d(x,A) \geq 0$.
1. Thus, $d(x, A) = 0$.
```


## Interior II

```{prf:theorem}
:label: res-ms-int-intersect-int

Interior of a finite intersection is the intersection of interiors.

$$
\interior \bigcap_{i=1}^n A_i = \bigcap_{i=1}^n (\interior A_i).
$$
```

```{prf:proof}
Define:

$$
A = \bigcap_{i=1}^n A_i.
$$

From {prf:ref}`res-ms-int-cl-comp-rel`:

$$
\begin{aligned}
\interior A &= X \setminus \left ( \closure (X \setminus A) \right )\\
&= X \setminus \left ( \closure \left (
   X \setminus \left ( \bigcap_{i=1}^n A_i \right)
   \right) \right )\\
&= X \setminus \left ( \closure \left (
     \bigcup_{i=1}^n \left ( X \setminus A_i \right)
   \right) \right )\\
&= X \setminus \left (
     \bigcup_{i=1}^n  ( \closure  (X \setminus A_i) )
   \right)\\
&= X \setminus \left (
     \bigcup_{i=1}^n  (X \setminus (\interior A_i) )
   \right)\\
&= X \setminus \left (
     X \setminus \left ( \bigcap_{i=1}^n  (\interior A_i) \right )
   \right)\\
&= \bigcap_{i=1}^n  (\interior A_i).
\end{aligned}
$$

In this derivation, we have made use of the facts that:

1. complement of interior equals closure of complement
   ({prf:ref}`res-ms-int-cl-comp-rel`).
1. closure of a finite union is a union of the closures
   ({prf:ref}`res-ms-closure-finite-union-equal`).
```


## Dense Sets

```{prf:definition} Dense subsets
:label: def-ms-dense-set

A subset $A$ of $X$ is called *dense* in $X$ if 
$\closure A = X$.
```


```{prf:theorem}
:label: res-ms-dense-open-intersect

A set $A$ is dense if and only if $O \cap A \neq \EmptySet$ holds
for every nonempty open set $O$ in $X$. 
```

```{prf:proof}

Assume $A$ is dense and $O$ is open and non-empty.

1. Let $x \in O$.
1. There exists $r > 0$ such that $B(x, r) \subseteq O$.
1. Since $x \in \closure A$, $B(x, r) \cap A \neq \EmptySet$.
1. Thus, $O \cap A$ is not empty. 

Assume $A \cap O \neq \EmptySet$ for every open and nonempty $O$.

1. Let $x \in X$. If $x \in A$ then $x$ is a closure point of $A$.
   So assume $x \in X \setminus A$.
1. Let $r> 0$ and consider the open ball $B(x,r)$.
1. Since $B(x,r)$ is nonempty and open, hence $B(x, r) \cap A \neq \EmptySet$.
1. Thus, $x$ is a closure point of $A$.
1. Thus, $A$ is dense in $X$.
```


```{prf:theorem}
:label: res-ms-dense-complement-interior-empty

Complement of a dense set has an empty interior.
```
```{prf:proof}
Recall from {prf:ref}`res-ms-int-cl-comp-rel` that:

$$
X \setminus (\interior A) = \closure (X \setminus A).
$$

Now, let $B$ be dense and $A = X \setminus B$. 
Then, 

$$
\begin{aligned}
& X \setminus (\interior A) = \closure (X \setminus A)\\
& \iff X \setminus (\interior A) = \closure B\\
& \iff X \setminus (\interior A) = X \\
& \iff \interior A = X \setminus X = \EmptySet.
\end{aligned}
$$
Thus, $A$ has an empty interior.
```

Dense sets can be characterized in terms
of convergent sequences. This is
discussed in {prf:ref}`res-ms-dense-sequence-limit`.

## Equivalent Metrics

```{prf:definition} Equivalent metrics
:label: def-ms-equivalent-metric

Let $d_a : X \times X \to \RR$ and $d_b: X \times X \to \RR$ 
be two different metrics on $X$. 
Then, the metrics are said to be *equivalent* if they determine the
same {prf:ref}`topology <def-ms-topology>` on $X$. 
In other words, the family of open sets in $(X, d_a)$
is identical to the family of open sets in $(X, d_b)$;
i.e., $\OOO$ is an open set in $(X, d_a)$ if and only if 
$\OOO$ is an open set in $(X, d_b)$. 
```

```{prf:theorem} Balls inside balls
:label: res-ms-eq-metric-ball-in-ball

Let $d_a : X \times X \to \RR$ and $d_b: X \times X \to \RR$ 
be two different metrics on $X$ which are equivalent.
Let $B_a(x, r)$ and $B_b(x, r)$ denote the open 
balls at $x \in X$ of radius $r$ 
in metric spaces $(X, d_a)$ and $(X, d_b)$ respectively. 

Then, for every $x \in X$ and for every $r > 0$, 
there exists $r' > 0$ such that

$$
B_a (x, r') \subseteq B_b(x, r).
$$
Similarly, for every $x \in X$ and for every $r > 0$, 
there exists $r'' > 0$ such that

$$
B_b (x, r'') \subseteq B_a(x, r).
$$
```

```{prf:proof}
Let $x \in X$ and for every $r > 0$.

1. Consider the open ball $O = B_b(x, r)$.
1. Then, $O$ is an open set of $(X, d_b)$.
1. Since both metrics determine same topology,
   hence $O$ is also an open set of $(X, d_a)$.
1. Since $x \in O$, hence $x$ is an interior point
   of $O$ in $(X, d_a)$.
1. Thus, there exists $r' > 0$ such that
   
   $$
   B_a(x, r') \subseteq O = B_b(x, r).
   $$

We proceed similarly for the other way round.

1. Consider the open ball $O = B_a(x, r)$.
1. Then, $O$ is an open set of $(X, d_a)$.
1. Since both metrics determine same topology,
   hence $O$ is also an open set of $(X, d_b)$.
1. Since $x \in O$, hence $x$ is an interior point
   of $O$ in $(X, d_b)$.
1. Thus, there exists $r'' > 0$ such that
   
   $$
   B_b(x, r'') \subseteq O = B_a(x, r).
   $$
```

We can actually prove a stronger result.

```{prf:theorem} Metric equivalence characterization as balls inside balls
:label: res-ms-eq-metric-balls-in-balls
Let $d_a : X \times X \to \RR$ and $d_b: X \times X \to \RR$ 
be two different metrics on $X$.
Let $B_a(x, r)$ and $B_b(x, r)$ denote the open 
balls at $x \in X$ of radius $r$ 
in metric spaces $(X, d_a)$ and $(X, d_b)$ respectively. 


The two metrics $d_a$ and $d_b$ are equivalent if and
only if 


for every $x \in X$ and for every $r > 0$, 
there exists $r' > 0$ such that
$B_a (x, r') \subseteq B_b(x, r)$

and 

for every $x \in X$ and for every $r > 0$, 
there exists $r'' > 0$ such that
$B_b (x, r'') \subseteq B_a(x, r)$. 
```

```{prf:proof}
One part of this result was proved in 
{prf:ref}`res-ms-eq-metric-ball-in-ball`.

We now assume that
for every $x \in X$ and for every $r > 0$, 
there exists $r' > 0$ such that
$B_a (x, r') \subseteq B_b(x, r)$
and 
for every $x \in X$ and for every $r > 0$, 
there exists $r'' > 0$ such that
$B_b (x, r'') \subseteq B_a(x, r)$. 


1. Let $O$ be an open set of $(X, d_a)$.
1. Let $x \in O$. 
1. Then, $x$ is an interior point of $O$ in $(X, d_a)$.
1. There exists an open ball $B_a(x, r) \subseteq O$.
1. Then, there exists an open ball 
   $B_b (x, r'') \subseteq B_a(x, r) \subseteq O$.
1. Thus, $x$ is an interior point of $O$ in $(X, d_b)$ too.
1. Thus, $O$ is an open set in $(X, d_b)$ too.
1. Similarly, we can show that if $O$ is an open set in
   $(X, d_b)$ then it is an open set in $(X, d_a)$ too.

Thus, both metric spaces determine same topology. Hence,
they are equivalent.
```


```{prf:theorem} Equivalent metrics as equivalence relation
:label: res-ms-eq-metrics-eq-rel

Let $X$ be an arbitrary set.
Consider the set of metrics on $X$ denoted as $D$:

$$
D \triangleq \{ d : X \times X \to \RR \ST d \text{ is a metric } \}.
$$
Let $d_a, d_b$ by any two metrics in $D$.
Let $d_a \sim d_b$ if the two metrics are equivalent.
Then, $\sim$ is an equivalence relation on the set of metrics $D$.
```

```{prf:proof}
[Reflexivity]

1. Let $d$ be an arbitrary metric on $X$.
1. Then, $d \sim d$ since it determines same topology.


[Symmetry]

1. Let $d_a$ and $d_b$ be two metrics on $X$.
1. If they are equivalent, then they introduce same topology.
1. Thus, $d_a \sim d_b$ implies $d_b \sim d_a$.

[Transitivity]

1. Let $d_a \sim d_b$ and $d_b \sim d_c$.
1. Then, all three $d_a, d_b, d_c$ determine the same topology
   on $X$.
1. Thus, $d_a \sim d_c$ holds too.
```


```{prf:definition} Strongly equivalent metrics
:label: def-ms-strong-equivalent-metric

Let $d_a : X \times X \to \RR$ and $d_b: X \times X \to \RR$ 
be two different metrics on $X$. 
Then, the metrics are said to be *strongly equivalent* 
if there exist constants $M,M' > 0$ such that

$$
d_a(x, y) \leq  M d_b(x, y)
\text{ and }
d_b(x, y) \leq  M' d_a(x, y) \Forall x, y \in X.
$$
```

```{prf:theorem}
:label: res-ms-strong-eq-metric-eq

Two strongly equivalent metrics are equivalent.
```

```{prf:proof}
Let $d_a : X \times X \to \RR$ and $d_b: X \times X \to \RR$ 
be two metrics on $X$ which are equivalent. 


1. Let $O$ be an open set of $(X, d_a)$.
1. Let $x \in O$ be an interior point.
1. Then, there exists an open ball $B_a(x, r) \subseteq O$.
1. Consider the open ball $B_b(x, \frac{r}{M})$.
1. For any point $y \in B_b(x, \frac{r}{M})$

   $$
   & d_b(x, y) < \frac{r}{M}\\
   & \implies M d_b(x, y) < r\\
   & \implies d_a(x, y) \leq  M d_b(x, y) < r.
   $$
1. Thus, $y \in B_a(x, r)$.
1. Thus, $B_b(x, \frac{r}{M}) \subseteq B_a(x, r) \subseteq O$.
1. Thus, $x$ is an interior point of $O$ in $(X, d_b)$.
1. Thus, $O$ is an open set in $(X, d_b)$.
1. Similarly, if $O$ is an open set in $(X, d_b)$
   then it is an open set in $(X, d_a)$.
1. Thus, both metric spaces determine the same topology of open sets.
1. Thus, they are equivalent.
```


## Connectedness

```{prf:definition} Connectedness
:label: def-ms-connected-space

A metric space $(X, d)$ is called *connected*
if it cannot be expressed as a union of 
two non-empty disjoint open sets. 
```

```{prf:example} Connected vs non-connected spaces
:label: ex-ms-connected-space-1

1. $\RR$ is connected.
1. $(0,1) \cup (1,2)$ is not connected.
```

```{prf:definition} Connected subsets
:label: def-ms-connected-subset

Let $(X, d)$ be a metric space.
A subset $A \subseteq X$ is called *connected* 
if the metric subspace $(A, d)$ is connected.
```


## Counter Examples

This subsection is a collection of some examples
which illustrate some salient aspects of topology.


```{prf:example} Empty Interior
:label: ex-empty-int-closure-nonempty

Consider the set $\RR$ with the usual metric.
The subset $\QQ$ of rational numbers has 
an empty interior. 
But $\closure \QQ = \RR$. Thus, the closure of $\QQ$ 
doesn't have an empty interior.
```

