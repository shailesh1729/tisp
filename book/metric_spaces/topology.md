# Metric Topology

Let $(X,d)$ be a metric space. 

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

```{prf:proposition}
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

```{prf:proposition}
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

```{prf:proposition}
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

## Closed Sets

```{prf:definition} Closed sets
:label: def-ms-closed-set

A subset $S$ of $X$ is said to be *closed* in $X$ 
if $X \setminus S$ is open in $X$.
```

```{prf:proposition}
$\EmptySet$ and $X$ are both open and closed subsets of $X$.
```

```{prf:proof}
$\EmptySet$ is vacuously open since it has no points
thus every point in $\EmptySet$ has an open ball that lies
within $\EmptySet$. Thus, $X$ is closed.

$X$ is open since for every point $x \in X$, every open ball at $x$
lies entirely in $X$ (by definition). Thus, $\EmptySet$ is closed.
```

```{prf:proposition}
Every singleton is a closed set.
```

```{prf:proof}
Let $x \in X$ and consider the singleton set $A = \{x\}$. 
Let $B = X \setminus A$. We show that $B$ is open. Then $A$ is closed.

Let $y \in B$ and let $r = d(x, y)$. Then, the open ball
$B(y, r)$ doesn't contain $x$. Thus, $B(y, r) \subseteq B$. Thus, 
$B$ is open.
```

```{prf:example}
* $(0, 1)$ is open in $\RR$.
* $[0, 1]$ is closed in $\RR$.
* $(0, 1]$ is neither open nor closed in $\RR$.
```
```{prf:proposition}
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

```{prf:proposition}
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
:label: def-ms-interior

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


```{prf:proposition} Interior is set of interior points
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
$A$ is open if and only if $A = \interior A$. 
```

```{prf:proof}
Assume, $A$ is open. 
Then, $A$ is the largest open set contained in $A$.
Hence, $A = \interior A$.

Assume $A = \interior A$. 
Then, since $\interior A$ is open, hence $A$ is open.
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

```{prf:proposition} Closure is set of closure points
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
$A$ is closed if and only if $A = \closure A$. 
```

```{prf:proof}
Assume, $A$ is closed. 
Then, $A$ is the smallest closed set containing $A$.
Hence, $A = \closure A$.

Assume $A = \closure A$. 
Then, since $\closure A$ is closed, hence $A$ is closed.
```

```{prf:proposition}
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

```{prf:proposition}
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

## Boundary

```{prf:definition} Boundary
:label: def-ms-boundary

The *boundary* of a set $S \subseteq X$ (relative to $X$), 
denoted by $\boundary S$ or $\aboundary_X S$ is defined as

$$
\boundary S = \closure S \setminus \interior S.
$$
```


```{prf:remark}
Let $Y$ be a metric subspace of $X$ and $S \subseteq Y$.
The interior, closure and boundary of $S$ w.r.t. $X$ 
and w.r.t. $Y$ may be different.

If a subspace hasn't been specified, by default, we shall
assume that we are computing the interior, closure and 
boundary w.r.t. the metric space $X$.
```


## Subspace Topology

```{prf:proposition}
Let $Y$ be a metric subspace of $X$. Let $S \subseteq Y$.

$S$ is open in $Y$ if and only if $S = O \cap Y$ where $O$ 
is an open subset of $X$.
```

```{prf:proof}
abc
```

```{prf:example}
* $[0, 1)$ is open in the metric space $\RR_+$.
```