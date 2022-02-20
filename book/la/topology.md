(sec:la:normed-space-topology)=
# Topology of Normed Linear Spaces
{prf:ref}`Recall <def-la-norm-induced-metric>` that
if a vector space $\VV$ is equipped with a norm $\| \cdot \| : \VV \to \RR$, 
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


## Linear Transformations

### Boundedness

````{prf:definition} Bounded linear transformation
:label: def-la-bounded-lin-map

Let $(\VV, \| \cdot \|_v)$ and $(\WW, \| \cdot \|_w)$ be
normed linear spaces. Let 
$T : \VV \to \WW$ be a linear transformation. 
We say that $T$ is *bounded* (in the sense of linear transformations)
if the set

```{math}
:label: eq-la-ns-bounded-func
S \triangleq \left \{ \frac{\| T(\bx) \|_w}{\| \bx \|_v}  \ST \bx \in \VV, \bx \neq \bzero \right \}
```
is bounded.
````
Note that the set $S$ in {eq}`eq-la-ns-bounded-func` 
is trivially bounded from below by $0$. 
Thus, by bounded we mean, bounded from above.

The notion of boundedness for linear transformations
is different from the notion of boundedness for
bounded functions in general metric spaces
as defined in {prf:ref}`def-ms-bounded-function`.
There, we posit that the range of the function is bounded.
For bounded linear transformations, the range (in norm) may be unbounded,
yet the ratio of the norms of output and input is bounded.

Since linear transformations commute with scalar multiplication
as in $T(t \bx) = t T(\bx)$, hence the norm of the output is 
unbounded unless $T$ is an identically $\bzero$ linear transformation. 

```{div}
If there exists $\bv \in \VV$ such that $T(\bv) \neq \bzero$, then

$$
\| T(t \bv)\|_w =  | t| \| T (\bv) \|_w \to \infty 
\text{ as } | t | \to \infty.
$$

Thus, the idea of a bounded range is not very
useful for linear transformations. 
```

````{prf:remark} Bounded linear transformation in terms of unit norm vectors
:label: res-la-ns-bounded-lin-func-unit-norm-vecs

For $T, \bx$ as in {eq}`eq-la-ns-bounded-func`, and any nonzero $t \in \FF$, 
we have

$$
\frac{\| T( t \bx) \|_w}{\| t \bx \|_v}
= \frac{\|t  T( \bx) \|_w}{ |t | \| \bx \|_v}
= \frac{| t | \| T( \bx) \|_w}{ |t | \| \bx \|_v}
= \frac{\| T( \bx) \|_w}{ | | \| \bx \|_v}.
$$

In particular, if we choose $t = \frac{1}{\|\bx \|_v}$, then
$\| t \bx \|_v = 1$.

Hence, every element in set $S$ in {eq}`eq-la-ns-bounded-func`
equals $\| T (\bx) \|_w$ for some unit vector $\bx$. 
It follows that

```{math}
:label: eq-la-ns-bounded-func-2
S = \left \{ \frac{\| T(\bx) \|_w}{\| \bx \|_v}  
\ST \bx \in \VV, \bx \neq \bzero \right \}
= \left \{ \| T(\bx) \|_w  
\ST \bx \in \VV, \| \bx \|_v = 1 \right \}.
```
Some authors prefer this description of $S$ as the
definition of bounded linear transformations.
````

```{prf:example} Unbounded linear transformation
:label: ex-la-ns-unbounded-transformation

It is possible to construct unbounded linear transformations
in infinite dimensional normed linear spaces.

We shall consider a {prf:ref}`sequence space <def-la-sequence-space>`
as described below.

Let $V$ be the set of all real sequences with 
finitely many nonzero terms. 

$$
V = \{ \{ x_n \} \ST \exists m \in \Nat \text{ with } 
x_n = 0 \Forall n \geq m \}.
$$
It is easy to verify that $V$ is a linear subspace
of the {prf:ref}`space of all sequences <def-la-space-sequences>`
$\RR^{\infty}$.

For any $\bx \in V$ given by $\bx = \{ x_n \}$,
define the supremum norm as:

$$
\| \bx \| = \sup \{ |x_1 |, |x_2 |, \dots \}.
$$
It is easy to verify that it is indeed a norm.

Define a transformation $T : V \to V$ as 

$$
T(x_1, x_2, x_3, \dots, x_n, 0, 0, \dots) = 
(x_1, 2 x_2, 3 x_3, \dots, n x_n, 0, 0, \dots).
$$
It is easy to verify that $T$ is linear. 

For any sequence $\be_n = (0, 0, \dots, 1, 0, 0, \dots)$ 
with $1$ in n-th position and all other entries 0, 
$\| \be_n \|  = 1$ and $ \| T (\be_n) \| = n$. 
Since we can construct $\be_n$ for every $n \in \Nat$, hence
the set $S$ as defined in {eq}`eq-la-ns-bounded-func-2` 
is unbounded.

Consequently, $T$ is an unbounded linear transformation. 
```

### Continuity

```{prf:theorem} Characterization of continuity for linear transformations
:label: res-la-ns-continuity-lin-map

Let $(\VV, \| \cdot \|_v)$ and $(\WW, \| \cdot \|_w)$ be
normed linear spaces. Let 
$T : \VV \to \WW$ be a linear transformation. 
Then, the following statements are equivalent.

1. $T$ is continuous at one point in $\VV$.
1. $T$ is continuous at $\bzero \in \VV$.
1. $T$ is bounded.
1. $T$ is Lipschitz continuous at $\bzero \in \VV$.
1. $T$ is Lipschitz continuous.
1. $T$ is uniformly continuous.
1. $T$ is continuous.
```

```{prf:proof}
(1) $\implies$ (2)

Assume $T$ is continuous at $\bx_0 \in \VV$. 

1. Let $\epsilon > 0$ and let $\delta > 0$ such that
   if $\| \bx - \bx_0 \|_v < \delta$ then $ \| T(\bx) - T(\bx_0) \|_w < \epsilon$.
1. Then, for all $\by \in B_v(\bzero, \delta)$, we have
   
   $$
   \| (\by + \bx_0) - \bx_0 \|_v     = \| \by \|_v < \delta.
   $$
1. Hence, $\| T(\by + \bx_0) - T(\bx_0) \|_w < \epsilon$.
1. But $T$ is linear. Hence

   $$
   T(\by + \bx_0) - T(\bx_0) 
   = T(\by) = T(\by) - \bzero = T(\by) - T(\bzero).  
   $$
1. Thus, $\| T(\by) - T(\bzero) \|_w < \epsilon$.
1. Thus, for any $\epsilon > 0$, there exists $\delta > 0$ such that
   $\| \by - \bzero \|_v < \delta$ implies $\| T (\by) - T(\bzero) \|_w < \epsilon$.
1. Thus, $T$ is continuous at $\bzero \in \VV$.

(2) $\implies$ (3)

Assume that $T$ is continuous at $\bzero \in \VV$.

1. Then, for any $\by \in \VV$, 

   $$
   \| T(\by) - T(\bzero) \|_w = \| T (\by) - \bzero \|_w
   = \| T (\by) \|_w.
   $$
1. Let $\epsilon = 1$ and choose $\delta > 0$ such that
   if $\| \by \|_v < \delta$ then
   $\| T (\by) \|_w < 1$.
   We can choose such $\delta > 0$ since $T$ is
   continuous at $\bzero$.
1. Let $\bx \in \VV$ be any nonzero vector.
1. Let $\by = \frac{\delta}{2 \| \bx \|_v } \bx$.
1. Then, $\| \by \|_v = \frac{\delta}{2} < \delta$.
1. And $\bx = \frac{2 \| \bx \|_v}{\delta} \by$.
1. Then, 

   $$
   \| T(\bx)\|_w 
   &= \left \| T \left ( \frac{2 \| \bx \|_v}{\delta} \by \right ) \right \|_w\\
   &=  \left \| \frac{2 \| \bx \|_v}{\delta} T (  \by ) \right \|_w\\
   &= \frac{2 \| \bx \|_v}{\delta} \| T (\by) \|_w \\
   &< \frac{2 \| \bx \|_v}{\delta} \times 1 \\
   &= \frac{2 }{\delta} \| \bx \|_v.
   $$
1. Thus, 

   $$
   \frac{\| T(\bx)\|_w }{\| \bx \|_v} < \frac{2 }{\delta}
   $$
   holds true for every nonzero $\bx \in \VV$.
1. Thus, the set in {eq}`eq-la-ns-bounded-func`
   is bounded from above by $\frac{2 }{\delta}$.
1. Thus, $T$ is bounded.


(3) $\implies$ (4)

Assume that $T$ is bounded. 
Let the set $S$ in {eq}`eq-la-ns-bounded-func`
have an upper bound $M > 0$.
Let $\bx \in \VV$ be a nonzero vector. 
Then, 

$$
\| T (\bx) - T(\bzero) \|_w 
&= \| T (\bx)  - \bzero \|_w \\
&= \| T (\bx) \|_w \\
&= \left \| T \left ( \| \bx \|_v \frac{\bx}{\| \bx \|_v} \right) \right \|_w\\
&= \| \bx \|_v  \left \| T \left ( \frac{\bx}{\| \bx \|_v} \right) \right \|_w\\
&\leq \| \bx \|_v M\\
&= M \| \bx  - \bzero \|_v.
$$

Thus, there exists $M > 0$ such that for every nonzero $\bv \in \VV$,

$$
\| T (\bx) - T(\bzero) \|_w  \leq M \| \bx  - \bzero \|_v.
$$
Thus, $T$ is Lipschitz continuous at $\bzero \in \VV$.


(4) $\implies$ (5)

We assume that $T$ is Lipschitz continuous at $\bzero \in \VV$.

Then, let $K, \delta > 0$ such that for every $\by \in \VV$
with $\| \by \|_v < \delta$, we have

$$
\| T (\by) \|_w \leq K \| \by \|_v.
$$

1. Let $\bx \in \VV$ be a nonzero vector.
1. Let $\by = \frac{\delta}{2} \frac{\bx}{\| \bx \|_v}$.
1. Then, $\| \by \|_v = \frac{\delta}{2} < \delta$.
1. Hence, $\| T (\by) \|_w \leq K \| \by \|_v$.
1. Now, using linearity of $T$:

   $$
   \| T(\bx)\|_w 
   &= \left \| T \left ( \frac{2 \| \bx \|_v}{\delta} \by \right ) \right \|_w\\
   &=  \left \| \frac{2 \| \bx \|_v}{\delta} T (  \by ) \right \|_w\\
   &= \frac{2 \| \bx \|_v}{\delta} \| T (\by) \|_w \\
   &\leq \frac{2 \| \bx \|_v}{\delta} K \| \by \|_v \\
   &= K \| \bx \|_v.
   $$
1. Thus, we have $\| T(\bx)\|_w \leq K \| \bx \|_v$
   for every nonzero $\bx \in \VV$.
1. Now, let $\bx, \bz \in \VV$ be distinct. 
1. Using linearity of $T$

   $$
   \| T (\bx) - T(\bz) \|_w 
   &= \| T (\bx - \bz) \|_w\\
   \leq K \| \bx - \bz \|_v.
   $$
1. Hence, $T$ is Lipschitz continuous.


(5) $\implies$ (6)

Assume that $T$ is Lipschitz continuous.

Let $K >0$ such that for every $\bx, \by \in \VV$,

$$
\| T(\bx) - T(\by)\|_w \leq K \| \bx - \by \|_v.
$$

1. Let $\epsilon > 0$. 
1. Choose $\delta = \frac{\epsilon}{K}$.
1. Then, for every $\bx, \by \in \VV$ with
   $\| \bx - \by \|_v < \delta$, we have

   $$
   \| T(\bx) - T(\by)\|_w 
   \leq K \| \bx - \by \|_v 
   < K \delta  = K \frac{\epsilon}{K} = \epsilon.
   $$
1. Hence, $T$ is uniformly continuous.

(6) $\implies$ (7)

A uniformly continuous function is trivially continuous.


(7) $\implies$ (1)

A continuous function is trivially continuous at a point.
```

## Equivalent Norms



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


