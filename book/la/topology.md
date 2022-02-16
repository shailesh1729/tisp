(sec:la:normed-space-topology)=
# Topology of Normed Linear Spaces
{prf:ref}`Recall <def-la-norm-induced-metric>` that
if $\VV$ is equipped with a norm $\| \cdot \| : \VV \to \RR$, 
it induces a {prf:ref}`metric <def-ms-distance-function>` 
$d: \VV \times \VV \to \RR$ given by:

$$
d (x, y) = \| x - y \|.
$$

$\VV$ equipped with this metric becomes a 
{prf:ref}`metric space <def-ms-metric-space>`.

The topology of a general metric space is discussed in detail in
{ref}`sec:ms:metric-topology` and sections thereafter.
In this section, we discuss results which are specific
to normed linear spaces as they take advantage of 
the additional structure provided by the vector space.

1. There is a special zero vector $\bzero \in \VV$.
   It provides a reference point to define unit balls.
1. Vectors in $\VV$ can be added, subtracted and scaled.
   Thus, general balls can be described in terms of unit
   balls.
1. It is possible to introduce the notion of translation
   of sets. Recall that the metric induced by the norm
   is {prf:ref}`translation invariant <res-la-ns-metric-translation-invariant>`. 
1. Sets of vectors in a vector space can be added/subtracted/scaled 
   since the underlying vectors can be.
   This produces a number of interesting phenomena.

## Balls

An {prf:ref}`open ball <def-ms-open-ball>` in
a normed space is defined analogously as:

$$
B(\ba,r) = \{ \bx \in \VV \ST \| \bx - \ba \| < r \}.
$$

A {prf:ref}`closed ball <def-ms-closed-ball>` in
a normed space is defined analogously as:

$$
B[\ba,r] = \{ \bx \in \VV \ST \| \bx - \ba \| \leq r \}.
$$

We sometimes use the notation
$B_{\| \cdot \|}(\ba,r)$
and $B_{\| \cdot \|}[\ba,r]$
to identify the specific norm being used to
describe the open and closed balls.

```{prf:definition} Unit ball
:label: def-la-unit-ball

A ball centered at origin $\bzero \in \VV$ is 
called a *unit ball* if its radius is $1$. 
$B[\bzero, 1]$ denotes a *closed unit ball*
and $B(\bzero, 1)$ denotes an *open unit ball*.
The open unit ball is often written simply as $B$.
```

```{prf:observation}
Following the notation in {prf:ref}`def-vs-set-arithmetic`,
a closed ball can be expressed in terms of closed unit ball as:

$$
B[\bx, r] = \bx + r B[\bzero, 1].
$$

Similarly, any open ball can be expressed in terms of 
the open unit ball as:

$$
B(\bx, r) = \bx + r B(\bzero, 1).
$$
```

In the following, $B$ means the open unit ball $B(\bzero, 1)$.

## Interior

```{prf:theorem} Interior points in a normed space
:label: res-la-interior-point-ball

Let $A$ be a subset of a normed linear space $\VV$.
Then, $\bx \in \interior A$ if and only if there 
exists $r > 0$ such that 

$$
\bx + r B \subseteq A.
$$ 
```
```{prf:proof}
From {prf:ref}`def-ms-interior-point`,
$\bx$ is an interior point of $A$ if
there exists an $r > 0$ such that the open ball
$B(\bx, r) \subseteq A$.
But, as per algebraic notation $B(\bx, r) = \bx + r B$.
```

```{prf:theorem} Interior in a normed space
:label: res-la-interior

Let $A$ be a subset of a normed linear space $\VV$.
The interior of $A$ is given by

$$
\interior A = \{ \bx \ST \exists r > 0, \bx + r B \subseteq A \}.
$$ 
```

```{prf:proof}
This follows from the fact that the interior is a collection
of all the interior points of $A$.
```

## Closure

```{prf:theorem} Closure points in a normed space
:label: res-la-closure-point-ball

Let $A$ be a subset of a normed linear space $\VV$.
Then, $\bx \in \closure A$ if and only if

$$
\bx \in A + r B \Forall r > 0.
$$ 
```

```{prf:proof}

Recall that 

$$
A + r B = \bigcup_{\ba \in A} \ba + rB.
$$
Thus, $\bx \in A + r B$ if and only if 
there exists $\ba \in A$ such that $\bx \in \ba + r B$.

Assume that $\bx \in A + r B \Forall r > 0$.

1. Thus, for every $r > 0$, there exists $\ba \in A$ (depending on $r$)
   such that $\bx \in \ba + r B = B(\ba, r)$.
1. Thus, for every $r > 0$, there exists $\ba \in A$ (depending on $r$)
   such that $d(\bx, \ba) < r$.
1. Thus, for every $r > 0$, there exists $\ba \in A$ (depending on $r$) 
   such that $\ba \in B(\bx, r)$.
1. Thus, $A \cap B(\bx, r) \neq \EmptySet$ for every $r > 0$.
1. Thus, $\bx$ is a closure point of $A$.

For the converse, assume that $\bx$ is a closure point of $A$.

1. Then, $A \cap B(\bx, r) \neq \EmptySet$ for every $r > 0$.
1. Thus, for every $r > 0$, there exists $\ba \in A$ (depending on $r$)
   such that $\ba \in B(\bx, r)$.
1. Thus, for every $r > 0$, there exists $\ba \in A$ (depending on $r$)
   such that $d(\bx, \ba) < r$.
1. Thus, for every $r > 0$, there exists $\ba \in A$ (depending on $r$)
   such that $\bx \in B(\ba, r) = \ba + r B$.
1. Thus, for every $r > 0$, 
   $\bx \in A + r B$.
```

```{prf:theorem} Closure in a normed space
:label: res-la-closure

Let $A$ be a subset of a normed linear space $\VV$.
Then, the closure of $A$ is given by

$$
\closure A = \bigcap_{r > 0} (A + r B).
$$ 
```

```{prf:proof}
From previous result, a point $\bx$ is a closure point of $A$ 
if and only if 

$$
\bx \in \bigcap_{r > 0} (A + r B).
$$
The result follows from the fact that the closure of $A$
is the collection of all its closure points.
```


## Open Sets

```{prf:theorem}
:label: res-la-sum-open-sets

If $A$ and $B$ are open, then their sum $A+B$ is open.
```
```{prf:proof}

Let $x \in B$. Then the set $x + A$ is open since $A$ is open.
Then,

$$
A + B = \bigcup_{x \in B} x + A
$$
is a union of open sets. Hence, it is open.
```

## Closed Sets

```{prf:theorem}
:label: res-la-sum-closed-compact

If $A$ is closed and $B$ is compact, then their sum $A+B$ is closed.
```
```{prf:proof}
Let $\{z_n\}$ with $z_n = a_n + b_n \in A + B$ be a convergent sequence of $A+B$
where $a_n \in A$ and $b_n \in B$.

1. $\{a_n \}$ is a sequence of $A$.
1. $\{b_n \}$ is a sequence of $B$.
1. Let $\lim z_n = z$.
1. Since $B$ is compact, $\{b_n\}$ has a convergent subsequence, 
   say $\{b_{k_n}\}$ ({prf:ref}`def-ms-compact-characterization`).
1. Let $\lim b_{k_n} = l \in B$.
1. Now consider the sequence $\{a_{k_n}\}$ given by $a_{k_n} = z_{k_n} - b_{k_n}$.
1. $\{z_{k_n}\}$ is convergent since it is a subsequence of a convergent sequence
   ({prf:ref}`res-ms-subsequence-convergence`).
1. Since $\{z_{k_n}\}$ and $\{b_{k_n}\}$ are both convergent, 
   hence $\{a_{k_n}\}$ is also convergent.
1. Let $\lim a_{k_n} = m$. 
1. Since $A$ is closed. Hence $m \in A$
   ({prf:ref}`res-ms-closure-convergence`).
1. Now, $\lim a_{k_n} = \lim z_{k_n} - \lim b_{k_n}$ gives us $m = z - l$.
1. Thus, $z = m + l$.
1. But $m \in A$ and $l \in B$.
1. Hence, $z \in A + B$.
1. Thus, every convergent sequence of $A + B$ converges in $A+B$.
1. Thus, $A+B$ is closed. ({prf:ref}`res-ms-closure-convergence`).

```


## Linear Subspaces

```{prf:theorem}
:label: res-la-subspace-closed

Every subspace of a normed linear space $\VV$ is a closed set.
```

```{prf:theorem}
:label: res-la-proper-subspace-empty-interior

Every proper subspace of a normed linear space $\VV$
has an empty interior.
```


