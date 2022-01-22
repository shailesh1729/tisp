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

## Open Sets

```{prf:theorem}
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