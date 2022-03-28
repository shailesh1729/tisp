(sec:cvx:relint)=
# Topology of Convex Sets

This section focuses on some topological properties
of convex sets.
Throughout this section, we assume that $\VV$ is a 
finite dimensional real normed linear space equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \| : \VV \to \RR$.
It is also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$.
Wherever necessary,
it is also equppied with an 
{prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle : \VV \times \VV \to \RR$. 


Primary references for this section are
{cite}`beck2014introduction,bertsekas2003convex,boyd2004convex,rockafellar2015convex`.

In a finite dimensional real normed linear space:

- Linear subspaces are closed.
- Hyperplanes are closed.
- Affine subspaces are closed.
- Interiors of proper linear/affine subspaces are empty.
- Linear/affine transformations are continuous.
- Bijective linear/affine transformations are homeomorphisms.
- Bijective linear/affine transformations preserve interiors and closures.


Following the discussion in {ref}`sec:la:normed-spaces`,
$B$ shall denote the open unit ball $B(\bzero, 1)$.
$\bar{B}$ shall denote the closed unit ball $B[\bzero, 1]$.
The open ball $B(\bx, r)$ (for some $r > 0$) can be written as
$\bx + r B$. 
Similarly, the closed ball $B[\bx, r]$ can be written as
$\bx + r \bar{B}$.


We shall use several set and vector arithmetic identities
and inequalities in the discussion below. We list them here 
for quick reference. See {ref}`sec:la:set-arithmetic`
for detailed discussion.

Let $C,D,E$ be subsets of $\VV$.
Let $\bx, \bv, \bz \in \VV$ be arbitrary vectors.

From {prf:ref}`res-vs-set-vec-arithmetic`

$$
C = (C + \bz) - \bz.
$$


$$
C \subseteq D \iff C + \bz \subseteq D + \bz.
$$


From {prf:ref}`res-vs-set-intersect-sum-dist`,

$$
(C \cap D) + E \subseteq (C + E) \cap (D + E).
$$

For any set $A \subseteq \VV$, the set of points $\bx$
whose distance from $A$ is less than $r$ for some $r > 0$
is given by:

$$
A + r B = \bigcup_{\ba \in A} \ba + r B 
= \{\bx \ST \exists \ba \in A, d(\ba, \bx) < r \}.
$$

Recall from {prf:ref}`res-la-closure-point-ball` that
$\bx \in \closure A$ if and only if

$$
\bx \in A + r B \Forall r > 0.
$$ 
Similarly, recall from {prf:ref}`res-la-interior-point-ball` 
that $\bx \in \interior A$ if and only if 

$$
\exists r > 0 \text{ such that } \bx + r B \subseteq A.
$$


## Closure


```{prf:theorem} Closure of a convex set
:label: res-cvx-closure-convex-set-convex

Let $\VV$ be a real normed linear space.
Let $C$ be a convex set of $\VV$.
Then, its closure is convex.
```

```{prf:proof}
If $C$ is empty, then its closure is empty and is
therefore convex. Now, assume $C$ to be nonempty.

1. Let $\bx, \by \in \closure C$.
1. Let $t \in (0, 1)$.
1. Let $\bz = t \bx + (1-t) \by$.
1. We need to show that $\bz \in \closure C$.
1. Since both $\bx, \by$ are closure points of $C$,
   hence there exist sequences 
   $\{ \bx_n \}$ and $\{ \by_n \}$ of $C$ such that
   $\lim \bx_n = \bx$ and $\lim \by_n = \by$.
1. Then, $\bz_n = t \bx_n + (1-t) \by_n \in C$ 
   since $\bx_n, \by_n \in C$ and $C$ is convex.
1. By limit arithmetic 

   $$
   \lim \bz_n = \lim (t \bx_n + (1-t) \by_n)
   = t \lim \bx_n + (1-t) \lim \by_n
   = t \bx + (1-t)\by = \bz.
   $$
1. Thus, $\bz = \lim \bz_n$.
1. Since $\{ \bz_n \}$ is also a sequence of $C$,
   hence $\bz \in \closure C$.
1. Thus, for any $\bx, \by \in \closure C$ 
   and $t \in (0, 1)$, $ t \bx + (1-t) \by \in \closure C$.
1. Thus, $\closure C$ is convex.
```

## Interior

```{prf:theorem} Interior of convex sets
:label: res-cvx-interior-convex-set-convex

Let $\VV$ be a real normed linear space.
Let $C$ be a nonempty convex set of $\VV$.
Then, its interior is convex.
```

```{prf:proof}
Let $D = \interior C$. Assume that $C$ is convex.

1. Let $\bx, \by \in D$ and $t \in (0,1)$.
   We need to show that $\bz = t \bx + (1-t)\by \in D$.
1. Since $\bx \in D$, there exists an 
   open ball $B(\bx, r) \subseteq C$.
1. Let Consider the open ball $B(\bz, t r)$ radius $tr$ around $\bz$.
1. Let $\bv \in B(\bz, t r)$.
1. Let
   
   $$
   \bu = \frac{1}{t} \bv - \frac{1-t}{t} \by.
   $$
   We can choose such a point $\bu \in \VV$ since $t$ is nonzero.
1. Then,
   $\bv = t \bu + (1-t) \by$.
1. Note that

   $$
   \| t (\bu - \bx) \| 
   &= \| t\bu - t \bx \| \\
   &= \| \bv - (1-t)\by - (\bz - (1-t)\by) \|\\
   &= \| \bv - \bz \| \\
   & < t r
   $$
   since $\bv \in B(\bz, tr)$.
1. Thus, $\| \bu - \bx \| < r$.
1. Thus, $\bu \in B(\bx, r)$.
1. Thus, $\bv \in C$ as it is a convex combination of $\bu$ and $\by$.
1. Since this holds true for every $\bv \in B(\bz, tr)$,
   hence $B(\bz, t r) \subseteq C$.
1. Thus, there is an open ball of radius $tr$ around $\bz$ contained in $C$.
1. Thus, $\bz \in \interior C = D$.
1. We have shown that for any $\bx, \by \in D$ and $t \in (0,1)$,
   $\bz = t \bx + (1-t)\by \in D$.
1. Thus, $D$ is convex.
```
We provide a shorter but more technical proof.

```{prf:proof}
Let $D = \interior C$. Assume that $C$ is convex.

1. Fix some $t \in (0, 1)$.
1. Since $C$ is convex, hence $tC + (1-t)C \subseteq C$.
1. Hence, $tD + (1-t)D \subseteq C$.
1. Since $D$ is open, hence $tD$ is open
   ({prf:ref}`res-la-ns-scaling-homeomorphism`).
1. Then, $tD + (1-t)D$ is also open
   as sum of an open set with any set is open
   ({prf:ref}`res-la-sum-open-sets`).
1. But $D$ is the largest open set contained in $C$.
1. Thus, $tD + (1-t)D \subseteq D$.
1. Thus, $D$ contains all its convex combinations.
1. Thus, $D$ is convex.
```

```{prf:proof}
Another proof can be built based on the
general line segment property proved in
{prf:ref}`res-cvx-convex-interior-segment` below.

1. Let $\bx, \by \in \interior C$. 
1. Let $t \in (0, 1)$.
1. Then, by line segment property $t \bx  + (1 -t) \by \in \interior C$.
1. Thus, $\interior C$ is closed under convex combination.
1. Thus, $\interior C$ is convex.
```

```{prf:theorem} Affine hull of convex sets with empty interior
:label: res-cvx-convex-set-empty-interior

Let $\VV$ be an $n$-dimensional real normed linear space.
Let $C$ be a nonempty convex set of $\VV$. 
If $C$ has an empty interior, then it must
lie in an affine subspace of dimension less than $n$.

Conversely, if $\dim \affine C < n$, then, $C$
has an empty interior. 
```

```{prf:proof}
We first show that if $C$ has an empty interior, then
$\dim \affine C < n$.

1. Let $A = \affine C$.
1. Let $\dim A = d$.
1. If $d < n$, there is nothing to prove.
1. For contradiction, assume $d=n$.
1. Then, it is possible to pick $n+1$ affine independent
   points from $C$.
1. Let $\bv_0, \dots, \bv_n$ be one such set of affine
   independent points of $C$.
1. Since $C$ is convex, it contains the convex hull
   $H = \ConvexHull \{\bv_0, \dots, \bv_n \}$;
   i.e., $H \subseteq C$.
1. In an $n$ dimensional space, the convex hull
   of a $n+1$ affine independent points has
   a nonempty interior.
1. Thus, the interior of $C$ must be nonempty.
1. This is a contradiction, hence $\dim A < n$ must be true.

Now, assume that $\dim \affine C < n$.

1. $A$ is a proper subspace of $\VV$.
1. Then $A$ has an empty interior
   as per {prf:ref}`res-la-affine-subspace-empty-interior`.
1. $\interior C \subseteq \interior A$ since $C \subseteq A$.
1. Thus, $\interior C = \EmptySet$.
```

```{prf:example} Convex sets with empty interiors
:label: ex-cvx-convex-sets-empty-int-1

1. Let $\VV = \RR^2$. Let $A = [0,1] \times \{0\}$.
   It is the line segment from $x=0$ to $x=1$ with $y=0$
   on $x$-axis.
   No open ball of $\RR^2$ is contained inside $A$. 
   Hence, $\interior A = \EmptySet$.
1. Let $C$ be any singleton (a point). It is nonempty
   and its interior is empty.
1. Let $\VV = \RR^3$. Any polygon lying within the $x-y$ plane
   has an empty interior.
```

```{prf:corollary} Convex sets, empty interior, interior of closure
:label: res-cvx-convex-empty-int-cl-int

Let $\VV$ be an $n$-dimensional real normed linear space.
Let $C$ be a nonempty convex set of $\VV$. 
If $C$ has an empty interior then so does its closure.

$$
\interior C = \EmptySet \implies \interior \closure C = \EmptySet.
$$
```

```{prf:proof}
We proceed as follows:

1. Let $A = \affine C$.
1. Since $\interior C = \EmptySet$ hence $\dim A = d < n$
   due to {prf:ref}`res-cvx-convex-set-empty-interior` above.
1. Now $\closure C \subseteq A$ since $A$ is closed
   ({prf:ref}`res-la-affine-closed`).
1. Thus, $\interior \closure C \subseteq \interior A$.
1. But then $A$ has an empty interior
   as per {prf:ref}`res-la-affine-subspace-empty-interior`.
1. Thus, $\interior \closure C = \EmptySet$.
```


```{prf:theorem} General line segment property for convex sets
:label: res-cvx-convex-interior-segment

Let $\VV$ be a real normed linear space.
Let $C$ be a nonempty convex subset of $\VV$. 
Let $\bx \in \interior C$
and $\by \in \closure C$. Then, 

$$
(1-t) \bx + t \by \in \interior C \Forall t \in [0,1).
$$
```

```{prf:proof}
Let $C$ be a convex set. Fix some $t \in [0,1)$.

1. Let $\bz = (1-t) \bx + t \by$. 
   It suffices to show that there is an open ball
   $\bz + rB \subseteq C$.
1. Since $\by \in \closure C$, hence for every $r > 0$, 
   we have $\by \in C + r B$.
1. Then,

   $$
   \bz + r B &= (1-t)\bx + t \by + r B \\
   &\subseteq (1-t)\bx + t (C + r B) + r B \\
   &= (1-t)\bx + (1 + t) rB + t C\\
   & = (1 -t)(\bx + r (1+t)(1-t)^{-1} B) + t C.
   $$
1. Since $\bx \in \interior C$, hence we can take $r$ to be so small 
   such that

   $$
   \bx + r (1+t)(1-t)^{-1} B \subseteq C.
   $$
1. But then

   $$
   (1 -t)(\bx + r (1+t)(1-t)^{-1} B) + t C 
   &\subseteq (1 -t) C + t C\\ 
   &\subseteq C
   $$
   since $C$ is convex and $t \in [0,1)$.
1. Thus, we established that there exists an $r > 0$ 
   such that $\bz + r B \subseteq C$.
1. Hence, $\bz \in \interior C$.
```


```{prf:theorem} Closure of interior
:label: res-cvx-convex-interior-closure

Let $\VV$ be a real normed linear space.
For any convex set $C \subseteq \VV$, 

$$
\closure \interior C = \closure C.
$$
```

```{prf:proof}
Since $\interior C \subseteq C$, hence
$\closure \interior C \subseteq \closure C$.


For the other direction, we proceed as follows:

1. Let $\by \in \closure C$.
   We need to show that $\by \in \closure \interior C$.
1. Choose some $\bx \in \interior C$.
1. By {prf:ref}`res-cvx-convex-interior-segment`, 
   the line segment between $\bx$ and $\by$
   (excluding $\by$) lies in $\interior C$.
1. For every $n \in \Nat$, let

   $$
   \by_n = \frac{1}{n} \bx + \left (1 - \frac{1}{n} \right ) \by.
   $$
1. Then, $\by_n \in \interior C$ by line segment property.
1. Thus, $\{ \by_n \}$ is a sequence of $\interior C$.
1. But then, $\lim_{n \to \infty} \by_n = \by$.
1. Hence, $\by$ is an accumulation point of $\interior C$.
1. Thus, $\by \in \closure \interior C$.
1. Thus, $\closure C \subseteq \closure \interior C$.

Combining the two inclusions, we get:

$$
\closure \interior C = \closure C.
$$ 
```


```{prf:theorem} Interior of closure
:label: res-cvx-convex-closure-interior

Let $\VV$ be an $n$-dimensional real normed linear space.
For any convex set $C \subseteq \VV$ 

$$
\interior C = \interior \closure C.
$$
```


```{prf:proof}
The statement is trivial for $C = \EmptySet$. We shall
assume that $C$ is nonempty. Further,
if $\interior C = \EmptySet$, then $\interior \closure C = \EmptySet$
due to {prf:ref}`res-cvx-convex-empty-int-cl-int` above.
We shall assume that $\interior C$ is nonempty.

Since $C \subseteq \closure C$, hence 
$\interior C \subseteq \interior \closure C$.


For the converse, assume that $\bx \in \interior \closure C$.
Our goal is to show that $\bx \in \interior C$. 

1. We have, $\bx \in \closure C$ and there exists $r > 0$ such that

   $$
   (\bx + r B) \subseteq \closure C.
   $$
1. Choose a point $\by \in \interior C$.
1. Let $t = \frac{r}{2\| \bx - \by \|}$.
1. Define
   
   $$
   \bz = (1 + t) \bx - t \by.
   $$
1. Note that

   $$
   d(\bz, \bx) &= \| \bz - \bx \|\\
   &= \|(1 + t) \bx - t \by - \bx \|\\
   &= t \| \bx - \by \| = \frac{r}{2}.
   $$
1. Hence, $\bz \in B(\bx, r) \subseteq \closure C$.
1. We have found the points $\by \in \interior C$ and $\bz \in \closure C$.
1. Now note that, 

   $$
   \bx = \frac{t}{1+t} \by + \frac{1}{1+t} \bz.
   $$
1. Thus, $\bx$ is a convex combination of $\by$ and $\bz$.
1. Since $t > 0$,  hence $\bx$ lies in the line segment 
   between $\bz$ and $\by$.
1. Hence, $\bx \in \interior C$ 
   due to {prf:ref}`res-cvx-convex-interior-segment`
   (line segment property for interior of convex sets).

Thus, we have shown that $\interior \closure C \subseteq \interior C$
as desired.
```


## Compact Sets


```{prf:theorem} Convex hull of compact sets
:label: res-cvxf-convex-hull-compact

Let $\VV$ be an $n$-dimensional real normed linear space. Let $S \subseteq \VV$
be a compact subset of $\VV$.
Then, $\ConvexHull(S)$ is compact.

In other words, convex hull of a compact set is compact.
```
Note that this property doesn't hold in infinite dimensional spaces.

```{prf:proof}

Let $H = \ConvexHull(S)$.

We first show that $H$ is bounded.

1. Since $S$ is compact, hence there exists $M > 0$
   such that $\| \bx \| \leq M$ for all $\bx \in S$.
1. Let $\by \in H$.
1. Then, by {prf:ref}`res-cvx-conv-hull-caratheodory`, 
   there exist $\bx_0, \dots, \bx_n \in S$ and
   $t \in \Delta_{n+1}$ such that
   
   $$
   \by = t_0 \bx_0 + \dots + t_n \bx_n.
   $$
1. Therefore,

   $$
   \| \by \| &= \|t_0 \bx_0 + \dots + t_n \bx_n \| \\
   &\leq t_0 \| \bx_0 \| + \dots + t_n \| \bx_n \| \\
   &\leq (t_0 + \dots + t_n) M = M.
   $$
1. Thus, $H$ is bounded.

We now show that $H$ is closed.

1. Let $\{ \bv_k \}$ be a convergent sequence of $H$.
1. Let $\bv = \lim_{k \to \infty} \bv_k$ be the limit of this
   sequence with $\bv \in \VV$.
1. We need to show that $\bv \in H$.
1. For every $k \in \Nat$, by {prf:ref}`res-cvx-conv-hull-caratheodory`, 
   there exist $\bx_0^k, \dots, \bx_n^k \in S$ and
   $\bt^k \in \Delta_{n+1}$ such that
   
   $$
   \bv_k = t_0^k \bx_0^k + \dots + t_n^k \bx_n^k.
   $$
1. Consider the vector space $\WW = \RR^{n+1} \oplus \VV \oplus \dots \oplus \VV$
   ($\VV$ repeated $n+1$ times).
1. Then, $R = \Delta_{n+1} \oplus S \oplus \dots \oplus S \subseteq \WW$.
1. Since $\Delta_{n+1}$ is compact in $\RR^{n+1}$ and
   $S$ is compact in $\VV$, hence
   $R$ is compact in the product topology of $\WW$.
1. Now, let $\by_k = (\bt^k, \bx_0^k, \dots, \bx_n^k) \in R$ for every $k$.
1. Thus, $\{ \by_k \}$ is a sequence of the compact set $R$.
1. By {prf:ref}`def-ms-compact-characterization`,
   every sequence of a compact set $R$ has a convergent
   subsequence that converges in $R$.
1. Let $\{ \by_{k_j} \}$ with $k_1 < k_2 < \dots$ be such
   a convergent subsequence of $\{ \by_k \}$.
1. Let the limit of this sequence be

   $$
   \by = \lim_{j \to \infty} \by_{k_j}
   = (\bt, \bx_0, \dots, \bx_n)
   $$
   with $\bt \in \Delta_{n +1}$ and $\bx_0, \dots, \bx_n \in S$
   since $\by \in R$.
1. This further implies that
   $\bt = \lim_{j \to \infty} \bt^{k_j}$
   and $\bx_i = \lim_{j \to \infty} \bx_i^{k_j}$ 
   for every $i \in 0,\dots,n$.
1. In turn, $t_i = \lim_{j \to \infty} t_i^{k_j}$ 
   for every $i=0, \dots, n$.
1. Since $\{ \bv_k \}$ is convergent, hence
   every subsequence of $\{ \bv_k \}$ has the same limit.
1. In particular, $\bv =  \lim_{j \to \infty} \bv_{k_j}$.
1. Then,

   $$
   \bv =  \lim_{j \to \infty} \bv_{k_j}
    = \lim_{j \to \infty} \sum_{i=0}^n t_i^{k_j} \bx_i^{k_j}
    = \sum_{i=0}^n t_i \bx_i.
   $$
1. But then, $\bv$ is a convex combination of points in $S$.
1. Thus, $\bv \in H$.
1. Thus, $H$ is closed.

Finally, by {prf:ref}`res-la-ndim-compact-closed-bounded`,
every closed and bounded set of a real $n$-dim normed
space is compact. Hence, $H$ is compact.
```


```{prf:theorem} Krein Milman theorem
:label: res-cvx-krein-milman

Let $\VV$ be an $n$-dimensional real normed linear space. 
Let $S \subseteq \VV$ be a compact convex subset of $\VV$.
Then,

$$
S = \ConvexHull(\aextreme(S)).
$$
In other words, a compact convex set is the convex hull of its
extreme points.
```

## Cones

```{prf:theorem} Conic hulls of a finite set of points are closed
:label: res-cvx-closed-conic-hull

Let $\VV$ be an $n$-dimensional real normed linear space.
Let $\ba_1, \dots, \ba_k \in \VV$. Then, their
conic hull given by

$$
H = \ConicHull ( \{ \ba_1, \dots, \ba_k \})
$$
is closed.
```

```{prf:proof}
Let $S = \{ \ba_1, \dots, \ba_k \}$.

1. By the {prf:ref}`conic representation theorem <res-cvx-conic-rep-unique>`,
   each point of $H$ can be represented as a conic combination
   of a linearly independent subset of $S$.
1. Since the number of points in $S$ is finite, hence
   the number of linearly independent subsets of $S$ is
   finite.
1. Let there be $N$ linearly independent subsets of $S$.
   Denote them by $S_1, \dots, S_N$.
1. Then,

   $$
   H = \bigcup_{i=1}^N \ConicHull (S_i).
   $$
1. If $\ConicHull (S_i)$ are closed, then 
   $H$ is closed as it is a finite union of closed sets.
1. Thus, it suffices to show that $H_i = \ConicHull (S_i)$
   are closed for every $i \in 1,\dots,N$.

Accordingly, let us assume that $S = \{ \ba_1, \dots, \ba_k \}$
is a linearly independent set of vectors (with $k \leq n$)
and $H = \ConicHull(S)$.

1. Let $\WW = \span S = \span \{ \ba_1, \dots, \ba_k \}$.
1. Then, $S$ is a basis for $\WW$.
1. Let $T : \WW \to \RR^k$ be a coordinate mapping given by
   
   $$
   T (\bx) = \bt \in \RR^m \text{ such that } 
   \bx = t_1 \ba_1 + \dots + t_k \ba_k
   $$
   for every $\bx \in \WW$.
   The mapping is well defined since $S$ is a basis for $\WW$.
   Thus, every $\bx \in \WW$ is a unique linear combination 
   of elements in the basis $S$.
1. It is easy to see that $T$ is a linear mapping.
   Moreover, $T$ is an isomorphism.
1. Thus, $T : (\WW , \| \cdot \|) \to (\RR^k, \| \cdot \|_2)$ is continuous
   due to {prf:ref}`res-la-ns-finite-continuous-transformation`.
1. Also, we can see that

   $$
   H = T^{-1} (\RR^k_+).
   $$
1. But $\RR^k_+$ is a closed set of $\RR^k$.
1. Thus, $H = T^{-1} (\RR^k_+)$ is closed since $T$ is continuous.
```


## Relative Interior

One way to think about relative interiors is 
to think in terms of subspace topology.
If $\VV$ is a normed linear space, then
it is a metric space. For any set $C \subseteq \VV$
let $A = \affine C$. Then, we can consider the
subspace topology by restricting the norm
$\| \cdot \| : \VV \to \RR$ to the affine hull $A$.
In terms of subspace topology,
if some set $X$ is open in $\VV$, then
$X \cap A$ is relatively open in $A$.

A set $C$ may have an empty interior
and yet may have a nonempty relative interior.
For example, consider a face of a cube in
$\RR^3$. While the cube has a nonempty interior,
the face has an empty interior as no open ball
is contained inside the face.
But, in terms of the subspace topology of the
affine hull of the face, the face indeed
as a nonempty relative interior.

Often, a convex set lies in a low dimensional
(affine or linear) subspace of the ambient vector space.
Thus, the interior of the convex set is empty.
At the same time, the relative interior of the set
(w.r.t. its affine hull) need not be empty.
It plays a similar topological role as the interior of a set.
We develop some fundamental results on the relative
interiors of convex sets in the sequel.


```{prf:definition} Relative interior point
:label: def-cvx-relative-interior-point

Let $\VV$ be a real normed linear space.
Let $C \subseteq \VV$. We say that $\bx \in C$ 
is a *relative interior point* of $C$ if
there exists an open ball $B(\bx, r)$ for some $r > 0$
such that 

$$
B(\bx, r) \cap \affine C \subseteq C.
$$
```

Note that, the open ball $B(\bx, r)$ itself need not be
contained inside $C$.


```{prf:definition} Relative interior
:label: def-cvx-relative-interior

The *relative interior* of a set $C$, denoted by $\relint C$
is the set of 
all its relative interior points.

$$
\relint C \triangleq \{\bx \in C \ST \exists r > 0, 
B(\bx, r) \cap \affine C \subseteq C \}.
$$
```
The basic definition of relative interior doesn't require
$\VV$ to be finite dimensional. 
However, several results in the sequel do depend
on $\VV$ being finite dimensional. We will 
clearly state this as and when required.


```{prf:example} Relative interior of a line segment
:label: ex-cvx-relint-line-segment


Let $\bx, \by \in \VV$ be distinct points. The line segment between
$\bx$ and $\by$ is given by

$$
S = \{ t \bx + (1-t) \by \ST t \in  [0, 1] \}.
$$

The relative interior of $S$ is given by

$$
\relint S = \{ t \bx + (1-t) \by \ST t \in  (0, 1) \}.
$$

To see this, we note that the affine hull of $S$ is the line

$$
L = \{ t \bx + (1-t) \by \ST t \in  \RR \}.
$$

Then, for every point $\bz = t \bx + (1-t) \by$ with $t \in (0, 1)$,
there exists $r > 0$ such that $B(\bz, r) \cap L \subseteq S$.
```


```{prf:example} Relative interior of an arc
:label: ex-cvx-relint-arc

Consider the set of points given by 

$$
S = \left \{ (\cos(t), \sin (t)) \ST 0 \leq t \leq \frac{\pi}{2} \right \}.
$$
in the ambient space $\RR^2$.
The affine hull of $S$ is the entire plane $\RR^2$.

Now, for any $\bx \in S$, $r > 0$, 

$$
B(\bx, r) \cap \affine (S) = B(\bx, r) \cap \RR^2 = B(\bx, r).
$$
It is an open ball in $\RR^2$ and hence never a subset of $S$.

Thus, $\relint S = \EmptySet$.
```


```{prf:theorem} Relative interiors are subset
:label: res-cvx-relint-subset

Let $\VV$ be a normed linear space.

For any set $C$ of $\VV$

$$
\relint C \subseteq C.
$$
```

```{prf:proof}
This follows directly from the definition of
relative interior.
```

```{prf:theorem} Relative interior of singleton
:label: res-cvx-relint-singleton

Let $\VV$ be a normed linear space.
Let $C = \{ \bx \}$ be a singleton subset of $\VV$. 
Then,

$$
\relint C = \relint \{ \bx \} = \{ \bx \}.
$$
```

```{prf:proof}
We proceed as follows:

1. The singleton sets are affine. 
1. Thus,  $\affine C = C$. 
1. Now, for any $r > 0$, 
   
   $$
   B(\bx, r) \cap C = \{ \bx \} = C \subseteq C.
   $$
1. Thus, $\bx \in \relint C$. 
1. Since $\relint C \subseteq C$, hence $\relint C = \{ \bx \}$.
```


Basic arithmetic of balls relative to the affine hull
will be useful later on.
```{prf:theorem} Relative ball arithmetic
:label: res-cvx-rel-ball-arithmetic
Let $\VV$ be a real normed linear space.
Let $A$ be an affine set and $\bx \in A$.
Let $L$ be the linear subspace parallel to $A$ given by
$L = A - A = A - \bx$. Let $r > 0$.
Then,

$$
(B(\bx, r) \cap A) - \bx = B(\bzero, r) \cap L.
$$
Alternatively,

$$
B(\bx, r) \cap A  = (B(\bzero, r) \cap L) + \bx.
$$

For any $\bx, \by \in A$,

$$
(B(\bx, r) \cap A) - \bx = (B(\by, r) \cap A) - \by. 
$$
```
In the simplified notation,

$$
((\bx + r B) \cap A) - \bx = r B \cap L.
$$

Alternatively,

$$
(\bx + r B) \cap A = (r B \cap L) + \bx.
$$

And for any $\bx, \by \in A$

$$
((\bx + r B) \cap A) - \bx = ((\by + r B) \cap A) - \by.
$$


```{prf:proof}
We first show that $(B(\bx, r) \cap A) - \bx \subseteq B(\bzero, r) \cap L
$.

1. Let $\bv \in (B(\bx, r) \cap A) - \bx$.
1. Then, $\bv + \bx \in B(\bx, r) \cap A$.
1. Thus, $\bv + \bx \in B(\bx, r)$ and $\bv + \bx \in A$.
1. Thus, $\bv \in B(\bzero, r)$ and $\bv \in A - \bx = L$.
1. Thus, $\bv \in B(\bzero, r) \cap L$.

We now show the converse.

1. Let $\bv \in B(\bzero, r) \cap L$.
1. Then, $\bv \in B(\bzero, r)$ and $\bv \in L$.
1. Then, $\bv + \bx \in B(\bx, r)$ and $\bv + \bx \in L + \bx = A$.
1. Then, $\bv + \bx \in B(\bx, r) \cap A$.
1. Thus, $\bv \in (B(\bx, r) \cap A) - \bx$.
1. Thus, $B(\bzero, r) \cap L \subseteq (B(\bx, r) \cap A) - \bx$.

We have shown that

$$
(B(\bx, r) \cap A) - \bx = B(\bzero, r) \cap L.
$$

Similarly, for any other $\by \in A$

$$
(B(\by, r) \cap A) - \by = B(\bzero, r) \cap L.
$$

Thus, 

$$
(B(\bx, r) \cap A) - \bx = (B(\by, r) \cap A) - \by. 
$$
```

```{prf:theorem} Relative interior and interior
:label: res-cvx-relint-interior
Let $\VV$ be a normed linear space.
For any subset $C$ of $\VV$

$$
\interior C \subseteq \relint C.
$$

If $\affine C = \VV$, then 

$$
\interior C = \relint C.
$$
```

```{prf:proof}
Let $\bx \in \interior C$.

1. Then, there exists $r > 0$ such that $B(\bx, r) \subseteq C$.
1. But $B(\bx, r) \subseteq C$ implies that 
   $B(\bx, r) \cap \affine C \subseteq C$.
1. Thus, $\bx \in \relint C$ also holds.
1. Thus, $\interior C \subseteq \relint C$.

Now consider the case where $\affine C = \VV$.
1. Then $B(\bx, r) \cap \affine C = B(\bx, r)$
   since $B(\bx, r) \subseteq \VV$.
1. Then, $\bx$ is a relative interior point of $C$ if 
   $B(\bx, r) \subseteq C$ for some $r > 0$.
1. But then, $\bx$ is an interior point of $C$.
1. Thus, $\relint C = \interior C$.
```

### Containment Relationship

In general $A \subseteq B$ implies that
$\interior A \subseteq \interior B$ and 
$\closure A \subseteq \closure B$. 
However, this is not the case with relative interiors.

```{prf:remark}
:label: res-cvx-relint-non-inclusive

An inclusion $A \subseteq B$ does not imply 
$\relint A \subseteq \relint B$.

Consider $C$ to be a cube in $\RR^3$ and
$A$ to be one of its faces.
The relative interiors of both $A$ and $C$ are nonempty
but disjoint.
```

However, if the affine hulls of $A$ and $B$ are same,
then $A \subseteq B$ does imply that $\relint A \subseteq \relint B$.

```{prf:theorem} Relative interior and containment
:label: res-cvx-relint-subset-rel


Let $A, B \subseteq \VV$.
If $A \subseteq B \subseteq \affine A$, 
then $\relint A \subseteq \relint B$.
```

```{prf:proof}
By {prf:ref}`res-affine-hull-tight-containment`,
$\affine A = \affine B$.

Now, let us focus on the relative interiors.

1. Let $\bx \in \relint A$.
1. Then, there exists $r > 0$ such that

   $$
   B(\bx, r) \cap \affine A \subseteq A.
   $$
1. Replace $\affine A$ by $\affine B$ and use the fact that $A \subseteq B$.
   Thus,

   $$
   B(\bx, r) \cap \affine B \subseteq B.
   $$
1. Thus, $\bx \in \relint B$.

Thus, $\relint A \subseteq \relint B$.
```


```{prf:theorem} Relative interior of closure
:label: res-cvx-closure-relint

Let $\VV$ be a real finite dimensional normed linear space.
For any set $C \subseteq \VV$ 

$$
\relint C \subseteq \relint \closure C.
$$
```

```{prf:proof}
The statement is trivial for $C = \EmptySet$. We shall
assume that $C$ is nonempty.

1. $C \subseteq \closure C$
1. Since $\VV$ is finite dimensional, 
   hence by {prf:ref}`res-la-affine-hull-closure`, 
   $\affine (\closure C) = \affine C$.
1. Thus, $C \subseteq \closure C \subseteq \affine C$.
1. Thus, by {prf:ref}`res-cvx-relint-subset-rel`,
   we have $\relint C \subseteq \relint \closure C$.
```

### Relatively Open Sets

```{prf:definition} Relatively open set
:label: def-cvx-relatively-open

We say that a set $C$ is *relatively open* if $C$
is open relative to its affine hull $\affine C$.
In other words, $C$ is *relatively open* if

$$
\relint C = C.
$$
```

```{prf:theorem} Affine sets are relatively open
:label: res-cvx-affine-relative-open

Let $\VV$ be a real normed linear space.
Any affine set in $\VV$ is relatively open.
In other words, if $A$ is affine, then

$$
\relint A = A.
$$
```
Note that this result doesn't require $\VV$ to be
finite dimensional.

```{prf:proof}
Let $A$ be an affine set. Then, $\affine A = A$.
Thus, for any $\bx \in A$

$$
B(\bx, r) \cap \affine A = B(\bx, r) \cap A \subseteq A.
$$
Thus, every $\bx \in A$ is a relative interior point of $A$.
Thus,

$$
\relint A = A.
$$ 
```

```{prf:corollary} Hyperplanes are relatively open
:label: res-cvx-hyperplane-relative-open

The relative interior of a hyperplane is the hyperplane itself. 
A hyperplane is relatively open.
```
This is a consequence of the fact that every hyperplane
is affine.


An affine set in a finite dimensional vector space 
is also closed since it is an
intersection of hyperplanes and every hyperplane
is a closed set. See {prf:ref}`res-la-affine-closed`


### Relative Interior of Relative Interior

```{prf:theorem} Relative interior is relatively open
:label: res-cvx-relint-relint

For any set $C$, 

$$
\relint (\relint C) = \relint C.
$$
Thus, $\relint C$ is relatively open.
```

```{prf:proof}
By definition $\relint (\relint C) \subseteq \relint C$.
Thus, we need to show that $\relint C \subseteq \relint (\relint C)$.

1. Let $A = \affine C$.
1. Let $\bx \in \relint C$.
1. Then, there exists $\epsilon = 2 r > 0$ such that 
   
   $$
   (\bx + 2 r B) \cap A \subseteq C.
   $$
1. We can write $\bx + 2 rB$ as 

   $$
   \bx + 2 r B = (\bx + r B ) + r B.
   $$
1. Thus, the previous inclusion can be written as 
   
   $$
   ( (\bx + r B) + r B) 
   \cap A \subseteq C.
   $$
1. Let $U = (\bx + r B) \cap A$.
1. Note that $U \subseteq C$.
1. Let $\by \in U$.
1. Then, $\by \in A$ and $\by \in (\bx + r B)$.
1. From previous inclusion, we can say that for every $\by \in U$

   $$
   (\by + r B) \cap A \subseteq C.
   $$
1. Thus, $\by \in \relint C$ for every $\by \in U$.
1. Thus, $U \subseteq \relint C$.
1. Thus, 

   $$
   U = (\bx + r B) \cap A \subseteq \relint C.
   $$
1. By definition of relative interior, $\bx \in \relint (\relint C)$.

We have shown that $\relint C \subseteq \relint (\relint C)$.
```

### Relative Boundary

```{prf:definition} Relative boundary
:label: def-cvx-relative-boundary

The *relative boundary* of a set $C$, denoted by $\relbd C$
is given by

$$
\relbd C \triangleq \closure C \setminus \relint C.
$$
```

## Translations

```{prf:theorem} Translations preserve relative interiors
:label: res-cvx-relint-translation-pres

Let $\VV$ be a normed linear space.
Let $\ba \in \VV$ be some fixed vector.
Let a translation map $g_a : \VV \to \VV$ be defined as

$$
g_a = \bx + \ba \Forall \bx \in \VV.
$$

Then, for any set $A \subseteq \VV$,

$$
g_a (\relint A) = \relint (g_a (A)).
$$

In other words,

$$
\relint (A + \ba) = (\relint A)  + \ba.
$$
```



```{prf:proof}

Let $\bx \in \relint (A + \ba)$.

1. Then, there exists $r > 0$ such that

   $$
   (\bx + r B ) \cap \affine (A + \ba) \subseteq A + \ba.
   $$
1. Let $\by = \bx - \ba$. 
1. Since $\bx \in A + \ba$ hence $\by \in A$.
1. Consider the set:

   $$
   R = (\by + r B) \cap \affine A.
   $$
1. We have

   $$
   R + \ba &= ((\by + r B) \cap \affine A) + \ba\\
   &\subseteq ((\by + r B) + \ba) \cap ((\affine A) + \ba)\\
   &= (\bx + r B) \cap (\affine (A + \ba))\\
   &\subseteq A + \ba.
   $$
   1. Recall that $(C \cap D) + E \subseteq (C + E) \cap (D + E)$.
   1. $(\affine A) + \ba = \affine (A + \ba)$ since
      translation which is an affine transformation
      preserves affine hulls ({prf:ref}`res-la-aff-func-aff-hull`).
1. Thus, $R + \ba \subseteq A + \ba$.
1. Thus, $R \subseteq A$.
1. Thus, $\by \in \relint A$.
1. Thus, $\bx - \ba \in \relint A$.
1. Thus, $\bx \in \relint A + \ba$.

Thus, $\relint (A + \ba) \subseteq \relint A + \ba$.

For the converse, assume that
$\bx \in \relint A + \ba$.

1. Then, $\bx - \ba \in \relint A$.
1. Let $\by = \bx - \ba$.
1. Then, there exists $r > 0$ such that

   $$
   (\by + r B ) \cap \affine A \subseteq A.
   $$
1. Consider the set

   $$
   R = (\bx + r B) \cap \affine (A + \ba).
   $$

1. We have

   $$
   R - \ba &= ((\bx + r B) \cap \affine (A + \ba)) - \ba\\
   &\subseteq ((\bx + r B) - \ba) \cap ((\affine (A + \ba)) - \ba)\\
   &= (\by + r B) \cap (\affine (A + \ba) - \ba)\\
   &= (\by + r B) \cap \affine A\\
   &\subseteq A.
   $$
1. Thus, $R - \ba \subseteq A$.
1. Thus, $R \subseteq A + \ba$.
1. Thus, $\bx \in \relint (A + \ba)$.

Thus, $\relint A + \ba \subseteq \relint (A + \ba)$.

Together, we have

$$
\relint A + \ba = \relint (A + \ba)
$$
```

## Relative Interiors of Convex Sets

Relative interiors play the role of interiors for convex sets.
Much of the following discussion is focused on the relative
interiors of convex sets (in finite dimensional real normed linear spaces).


```{prf:theorem} Relative interior of a convex set is convex
:label: res-cvx-convex-relint-is-convex

Let $\VV$ be a real normed linear space.
If $C$ is a convex set of $\VV$, then its relative interior
is a convex set.
```
```{prf:proof}
If $C = \EmptySet$, then, $\relint C = \EmptySet$ is convex.
So, assume that $C$ is nonempty.

1. Let $A = \affine C$ be the affine hull of $C$. 
1. Let $U = \relint C$ be the relative interior of $C$.
1. Let $L = A - A$ be the linear subspace parallel to $A$.
1. Choose $\bx, \by \in U$. Then, $\bx, \by \in U \subseteq C \subseteq A$.
1. Then, there exist open balls $B(\bx, r_x)$ and $B(\by, r_y)$
   such that

   $$
   B(\bx, r_x) \cap A \subseteq C
   \text{ and }
   B(\by, r_y) \cap A \subseteq C
   $$
1. Let $t \in (0,1)$.
1. Let $\bz = t \bx + (1-t)\by$. Note that $\bz \in C \subseteq A$
   since $\bx, \by \in C$ and $\bz$ is their convex combination.
1. Choose $r = \min(r_x, r_y)$.
   We shall show that

   $$
   B(\bz, r) \cap A \subseteq C.
   $$
   Thus, we shall show that $\bz \in \relint C$.
1. Towards this, pick any $\bw \in  B(\bz, r) \cap A$.
1. Let $\bw = \bz + \ba$.
1. $\bw = \bz + \ba \in B(\bz, r) \implies \ba \in B(\bzero, r)$.
1. $\bw = \bz + \ba \in A \implies \ba \in A - \bz = L$.
1. Thus, $\| \ba \| < r$ and $\ba \in L$.
1. Let $\bu = \bx + \ba$.
1. Then, $\bu \in L + \bx = A$ and $\bu \in B(\bx, r) \subseteq B(\bx, r_x)$.
1. Thus, $\bu \in B(\bx, r_x) \cap A \subseteq C$. 
1. Let $\bv = \by + \ba$.
1. Then, $\bv \in L + \by = A$ and $\bv \in B(\by, r) \subseteq B(\by, r_y)$.
1. Thus, $\bv \in B(\by, r_y) \cap A \subseteq C$. 
1. Now,

   $$
   \bw = \bz + \ba = t \bx + (1-t)\by + \ba 
   = t (\bx + \ba) + (1-t) (\by + \ba)
   = t \bu + (1-t) \bv.
   $$
1. Thus, $\bw$ is a convex combination of $\bu$ and $\bv$.
1. Since both $\bu$ and $\bv$ are in $C$,
   hence $\bw \in C$ as $C$ is convex.
1. We have shown that for every $\bw \in B(\bz, r) \cap A$, 
   $\bw \in C$.
1. Consequently, 

   $$
   B(\bz, r) \cap A \subseteq C.
   $$
1. Thus, $\bz \in \relint C = U$.
1. Thus, for every $\bx, \by \in U$ and $t \in (0,1)$,
   $\bz = t \bx  + (1-t) \by \in U$.
1. Thus, $U$ is convex.
```


### Nonempty Relative Interiors

```{prf:theorem} Nonempty relative interiors
:label: res-cvx-nonempty-relint

Let $\VV$ be a real normed linear space.
If $C$ is a nonempty convex set, then its relative interior
is nonempty.
```

```{prf:proof}

Let $A = \affine C$ and let $\dim A = k$.

1. Choose $k+1$ affine independent points of $C$:
   $\bv_0, \dots, \bv_k$.
1. Let $H = \ConvexHull \{\bv_0, \dots, \bv_k \}$ be their convex hull.
1. Since $C$ is convex, it contains the convex hull $H$;
   i.e., $H \subseteq C$.
1. $H$ contains all convex combinations of  $\{\bv_0, \dots, \bv_k \}$.
1. In particular, it contains the point:

   $$
   \bv = \frac{1}{k+1} (\bv_0 + \dots + \bv_k).
   $$
1. Note that $\bv \in H \subseteq C$.
1. Note that $A = \affine C = \affine \{\bv_0, \dots, \bv_k \} = \affine H$.
1. Thus, we can select a sufficiently small $r > 0$ 
   such that all points in $B(\bv, r) \cap A$ are contained in $H$.
1. But then, $B(\bv, r) \subseteq H \subseteq C$.
1. Thus, $\bv \in C$ and $B(\bv, r) \cap A \subseteq C$. 
1. Thus, $\bv \in \relint C$.
1. Thus, the relative interior of $C$ is nonempty.
```


### Line Segment Property

```{prf:theorem} Line segment property of relative interior
:label: res-cvx-convex-relint-segment

Let $\VV$ be a real $n$-dimensional normed linear space.
Let $C$ be a nonempty convex subset of $\VV$. 
Let $\bx \in \relint C$
and $\by \in \closure C$. Then, 

$$
(1-t) \bx + t \by \in \relint C \Forall t \in [0,1).
$$
```

```{prf:proof}
This is a restatement of the line segment property 
for interior of a convex set as described in 
{prf:ref}`res-cvx-convex-interior-segment`.
If $\relint C = \interior C$,
then the proof of {prf:ref}`res-cvx-convex-interior-segment`
applies directly.

This argument can be extended for the case where
$\relint C \neq \interior C$ by considering the
subspace topology w.r.t. $\affine C$.
```

The proof below is based on {cite}`bertsekas2003convex`.

```{prf:proof}
Let $A = \affine C$.
Let $L$ be the linear subspace parallel to $A$.
Note that for $t=0$, $(1-t)\bx + t \by = \bx$
which belongs to $\relint C$ by hypothesis.
Thus, we shall only consider $t \in (0,1)$ in the argument below.

Assume first that $\by \in C$. 

1. Since $\bx \in \relint C$, there exists $r > 0$ such that
   $B(\bx, r) \cap A \subseteq C$.
1. Pick any $t \in (0, 1)$.
1. Let $\bz = (1-t) \bx + t \by$.
1. Let $s = (1 - t) r$. Clearly, $s > 0$.
1. Consider the open ball $B(\bz, s)$.
   We shall show that $B(\bz, s) \cap A \subseteq C$.
1. Let $\bu \in B(\bz, s) \cap A$.
1. If $\bu = \bz$, then $\bu \in C$ since $C$ is convex.
1. Otherwise, we can write $\bu = \bz + p \bv$ 
   where $\bv$ is a unit norm vector and $0 < p < s$.
1. Then, $\bv \in L$ since $\bz + p \bv \in A$ and $\bz \in C \subseteq A$.
1. We can write 

   $$
   \bu = \bz + p \bv = (1-t) \bx + t \by + p \bv
   = (1-t) \left (\bx + \frac{p}{1-t} \bv \right ) + t \by.
   $$
1. Let $\bw = \bx + \frac{p}{1-t} \bv$.
1. Since $p < s$, hence $\frac{p}{1 - t} < \frac{s}{1-t} = r$.
1. Thus, $\bw \in B(\bx, r)$.
1. Also, $\bx \in C$ and $\bv \in L$ implies that $\bw \in A$.
1. Thus, $\bw \in B(\bx, r) \cap A \subseteq C$.
1. Now $\bu = (1-t) \bw + t \by$ is a convex combination of $\bw, \by \in C$.
1. Hence $\bu \in C$.
1. Thus, for every $\bu \in B(\bz, s) \cap A$, $\bu \in C$.
1. Thus, $\bz \in \relint C$.
1. Thus, $(1-t) \bx + t \by \in \relint C \Forall t \in [0,1)$.

We now consider the case where $\by \notin C$ but $\by \in \closure C$.

1. There exists a sequence $\{ \by_k \}$ of $C$ such that 
   $\by = \lim \by_k$.
1. Since $\bx \in \relint C$, there exists $r > 0$ such that
   $B(\bx, r) \cap A \subseteq C$.
1. Pick any $t \in (0, 1)$.
1. Let $\bz = (1-t) \bx + t \by$.
1. Let $\bz_k = (1-t)\bx + t \by_k$.
1. Then, by the earlier argument $\bz_k \in \relint C$
   since $\bx \in \relint C$, $\by_k \in C$ and $t \in (0,1)$.
1. Specifically, for every $k$, $B(\bz_k, (1-t) r) \cap A \subseteq C$.
1. By limit arithmetic

   $$
   \lim \bz_k = (1-t)\bx + t \lim \by_k = (1-t)\bx + t \by = \bz.
   $$
1. Let $s = \frac{1}{2} (1-t)r$.
1. Then, there exists $n_0 \in \Nat$ such that for all $k > n_0$,
   $\| \bz - \bz_k \| < s$.
1. Consider the set $B(\bz, s) \cap A$.
1. Let $\bu \in B(\bz, s) \cap A$.
1. Then for every $k > n_0$, 

   $$
   \| \bu - \bz_k \| \leq \| \bu - \bz \| + \| \bz - \bz_k \| 
   < s + s = (1-t)r.
   $$
1. Thus, $\bu \in B(\bz_k, (1-t) r) \cap A \subseteq C$ for every $k > n_0$.
1. Thus, $B(\bz, s) \cap A \subseteq C$.
1. Thus, $\bz \in \relint C$.
```

One way to interpret this result is as follows.
If we draw a line segment between a point
in the relative interior of a convex set $C$
and a point on the boundary of $C$, then 
every point on the segment (except the boundary point)
lies inside the relative interior of $C$.

```{prf:theorem} Characterization of relative interior in terms of line segments
:label: res-cvx-relint-line-segment-characterization

Let $\VV$ be a real $n$-dimensional normed linear space.
Let $C$ be a nonempty convex subset of $\VV$.
Then, $\bx \in \relint C$ if and only if every line segment in $C$ having
$\bx$ as one endpoint can be prolonged beyond $\bx$ without leaving $C$;
i.e., for every $\by \in C$ there exists $s > 1$ such that

$$
\bx + (s -1) (\bx - \by) \in C.
$$
```
At $s=0$, we get the point $\by$. At $s=1$, we get the point $\bx$.
At $s=\frac{1}{2}$, we get the point $\frac{1}{2} (\bx + \by)$. Thus,
the formula represents a line starting from $\by$ going in the direction
$\bx - \by$ towards $\bx$. For $s > 1$, it further extends beyond
$\bx$. This is sensible since $\bx \in \relint C$ hence the line
can be extended beyond $\bx$. It is definitely not possible to extend
the line beyond $\by$ if $\by \in C \setminus \relint C$.


```{prf:proof}

Let $A = \affine C$. Let $L$ be the linear subspace parallel to $A$.

1. Assume that $\bx \in \relint C$.
1. Then, there exists $r > 0$ such that $B(\bx, r) \cap A \subseteq C$.
1. Let $\by \in C$. 
1. Then $\bv = \bx - \by \in L$.
1. Let $\bu = \frac{r}{2 \| \bv \|} \bv$.
1. Since $\bx \in C \subseteq A$ and $\bu \in L$, hence $\bx + \bu \in A$.
1. $\| \bu \| = \frac{r}{2} < r$. Hence, $\bx + \bu \in B(\bx, r)$.
1. Thus, $\bx + \bu \in B(\bx, r) \cap A \subseteq C$.
1. Clearly,

   $$
   \bx + \bu = \bx + \frac{r}{2 \| \bx - \by \|} (\bx - \by).
   $$
1. Let $s = 1 + \frac{r}{2 \| \bx - \by \|}$.
1. Then, $\bx + (s - 1) (\bx - \by)  = \bx + \bu \in C$.


For the converse, assume that the said condition holds for some $\bx \in C$.

1. By {prf:ref}`res-cvx-nonempty-relint`, $\relint C$ is nonempty.
1. Let $\by \in \relint C$.
1. If $\by = \bx$ then $\bx \in \relint C$ and there is nothing to prove.
1. Now consider the case where $\by \neq \bx$.
1. By hypothesis, since $\by \in C$, hence there exists $s > 1$ such that

   $$
   \bz = \bx + (s - 1) (\bx - \by) \in C.
   $$
   Going from $\by$ to $\bx$, the point $\bz$ is behind $\bx$. 
   Thus, $\bx$ is between $\bz$ and $\by$.
1. Let $t = \frac{1}{s}$. Then, $t \in (0, 1)$.
1. Now,

   $$
   \bz = \bx + \left (\frac{1}{t} - 1 \right ) (\bx - \by) \\
   & \iff t \bz = t \bx + (1 - t) (\bx - \by) \\
   & \iff t \bz = \bx  - (1-t) \by \\
   & \iff \bx  = t \bz + (1-t) \by.
   $$
   We have shown that $\bx$ is a convex combination of $\by$ and $\bz$.
1. Thus, $\by \in \relint C$, $\bz \in C$ and $t \in (0, 1)$.
1. By {prf:ref}`line segment property <res-cvx-convex-relint-segment>`,
   $\bx \in \relint C$.
```

Several topological properties follow.

### Affine Hull of Relative Interior

```{prf:theorem} Affine hull of relative interior
:label: res-cvx-convex-relint-aff-hull

Let $\VV$ be a real $n$-dimensional normed linear space.
For any nonempty convex set $C \subseteq \VV$, 

$$
\affine \relint C = \affine C.
$$
In other words, the affine hull of the relative interior of a convex set is
same as the affine hull of the set.
```


```{prf:proof}
Let $A = \affine C$. Let $R = \relint C$.

1. From {prf:ref}`res-cvx-convex-relint-is-convex`, $R$ is convex.
1. From {prf:ref}`res-cvx-nonempty-relint`, $R$ is nonempty.
1. Let $m = \dim A$.
1. If $m=0$ then $C = A = \{ \bx \}$ is a singleton.
   Also, by {prf:ref}`res-cvx-relint-singleton`, $R = C = A$. 
   Thus, $\affine R = \affine C$.
1. We now consider the case where $m > 0$.
1. Then, there exist $m+1$ affine independent vectors $\bx_0, \dots, \bx_m \in C$
   such that 

   $$
   A = \affine C = \span \{ \bx_0, \dots, \bx_m \}.
   $$
1. Pick some $\bx \in R$. Since $R$ is nonempty, hence we can pick such $\bx$.
1. Consider the points $\by_i = \frac{1}{2} \bx + \frac{1}{2} \bx_i$ for $i=0, \dots, m$.
1. By {prf:ref}`line segment property <res-cvx-convex-relint-segment>`,
   $\by_i \in R$ since $\bx \in R$ and $\bx_i \in C$.
1. We now claim that $\{ \by_0, \dots, \by_m \}$ are affine independent.
   1. For contradiction, assume that they are affine dependent.
   1. Then, $\bu_i = \by_i - \by_0$ for $i=1,\dots, m$ are linearly dependent.
   1. Thus, there exists a nontrivial linear combination

      $$
      \sum_{i=1}^m t_i \bu_i  = \bzero.
      $$
   1. But

      $$
      \sum_{i=1}^m t_i \bu_i & = \sum_{i=1}^m t_i (\by_i - \by_0)\\
      & = \sum_{i=1}^m t_i \left (
         \frac{1}{2} \bx + \frac{1}{2} \bx_i - \frac{1}{2} \bx - \frac{1}{2} \bx_0
         \right )\\
      & = \frac{1}{2}\sum_{i=1}^m t_i (\bx_i - \bx_0) = \bzero.
      $$
   1. Thus, $\bx_i - \bx_0$ for $i=1,\dots,m$ are linearly dependent.
   1. Thus, $bx_i$ for $i=0,\dots,m$ are affine dependent
      which contradicts our hypothesis.
1. Thus $R$ has $m+1$ affine independent points given by $\{ \by_0, \dots, \by_m \}$.
1. Thus, $\affine R = A$.
```


### Simplex

```{prf:theorem} Relative interior of a simplex
:label: res-cvx-simplex-relint

Let $k+1$ points $\bv_0, \dots, \bv_k \in \VV$ be 
{prf:ref}`affine independent <def-affine-independence>`.
Let the *simplex* determined by them be given by

$$
C = \convex \{ \bv_0, \dots, \bv_k\}
= \{ t_0 \bv_0 + \dots + t_k \bv_k \ST 
    \bt \succeq \bzero, \bone^T \bt = 1\}.
$$

Then, the relative interior of $C$ is given by

$$
\relint C
= \{ t_0 \bv_0 + \dots + t_k \bv_k \ST 
    \bt \succ \bzero, \bone^T \bt = 1\}
$$

The relative boundary of $C$ is given by


$$
\relbd C
= \{ t_0 \bv_0 + \dots + t_k \bv_k \ST 
   \bt \succeq \bzero, \bone^T \bt = 1, t_i = 0 \text{ for some } i \}.
$$
```

```{prf:proof}
TBD
```


```{prf:theorem} Barycenter of a simplex is a relative interior point
:label: res-cvx-simplex-barycenter-relint

Let $k+1$ points $\bv_0, \dots, \bv_k \in \VV$ be 
{prf:ref}`affine independent <def-affine-independence>`.
Let the *simplex* determined by them be given by

$$
C = \convex \{ \bv_0, \dots, \bv_k\}
= \{ t_0 \bv_0 + \dots + t_k \bv_k \ST 
    \bt \succeq 0, \bone^T \bt = 1\}
$$

Let the barycenter of the simplex by given by
$\bv = \sum_{i=0}^k \frac{1}{k+1}{\bv_i}$.
Then, $\bv \in \relint C$.

In other words, the barycenter of a simplex lies in the relative interior.
```
```{prf:proof}
We first claim that the distance of the barycenter from each of the
vertices of the simplex is positive.

1. Let $d_i = \| \bv_i - \bv \|$ for $i=0,\dots,k$.
1. For contradiction, assume that $d_i = 0$ for some $i$.
1. Without loss of generality, assume that it holds for $i=0$.
   We can shuffle the vertices for this.
1. Then,

   $$
   \bv_0 = \sum_{j=0}^k \frac{1}{k+1}{\bv_j} \\
   &\iff (k+1) \bv_0 = \sum_{j=0}^k \bv_j \\
   &\iff \sum_{j=0}^k \bv_j - (k+1) \bv_0 = \bzero \\
   &\iff \sum_{j=1}^k \bv_j - k \bv_0 = \bzero \\
   &\iff \sum_{j=1}^k (\bv_j - \bv_0) = \bzero.
   $$
1. Thus, the vectors $\bv_1 - \bv_0, \dots, \bv_k - \bv_0$ are linearly dependent.
1. That means $\bv_0, \dots, \bv_k$ are affine dependent. A contradiction.
1. Hence, $d_i > 0$ for every $i=0,\dots,k$.

Let $A = \affine C$.
We now let $r = \min \{ d_0, \dots, d_m \}$. 
We claim that $B(\bv, r) \cap A \subseteq C$.

1. Let $\bu \in B(\bv, r) \cap A$.
1. Since $\bu \in A$ and $ \{ \bv_0, \dots, \bv_k\}$ provide an affine
   basis for $A$, hence, there is a unique affine representation for $\bu$
   given by

   $$
   \bu = \sum_{i=0}^k u_i \bv_i, \sum_{i=0}^k u_i = 1.
   $$

TBD
```


```{prf:theorem} Relative interior of convex hull of linearly independent points
:label: res-cvx-convex-hull-relint-rel-open

Let $\VV$ be a real normed linear space.
Let $S = \{\bv_1, \dots, \bv_m \}$ be a set of $m$ linearly independent
vectors. 

$$
X = \left \{ \bx \ST \bx = \sum_{i=1}^m t_i \bv_i, \sum_{i=1}^m t_i < 1, 
t_i > 0, i=1,\dots,m 
   \right \}.
$$
Let $A = \span S$. Then, $X$ is open relative to $A$.
```

```{prf:proof}
It is clear that $X \subseteq A$.
By $X$ being open relative to $A$ we mean that
for every $\bx \in X$, there exists $r > 0$ such that
$B(\bx, r) \cap A \subseteq X$.

We first establish that $X$ is convex.

1. Let $\bx, \by \in X$ and $t \in (0, 1)$.
1. Then, 

   $$
   \bx = \sum_{i=1} x_i \bv_i 
   \text{ and }
   \by = \sum_{i=1} y_i \bv_i 
   $$
   such that $x_i , y_i > 0$, $\sum_{i=1} x_i < 1$, $\sum_{i=1} y_i < 1$.
1. Let $\bz = t \bx + (1-t) \by$.
1. Then,

   $$
   \bz = \sum_{i=1}^m (t x_i + (1-t) y_i) \bv_i.
   $$
1. Then $t x_i + (1-t) y_i > 0$ since $t > 0, 1-t > 0, x_i > 0, y_i > 0$.
1. Also

   $$
   \sum_{i=1}^m (t x_i + (1-t) y_i) = t \sum_{i=1}^m x_i + (1-t) \sum_{i=1}^m y_i
   < t + 1 - t = 1.
   $$
1. Thus, $\bx \in X$. 
1. Thus, $X$ is convex.

We next show that $\bc = \frac{1}{m} (\bx_1 + \dots + \bx_m) \in \relint X$.

We now show that $X$ is relatively open.

1. Let $\bx \in X$. Then

   $$
   \bx = \sum_{i=1}^m t_i \bv_i \ST \sum_{i=1}^m t_i < 1, t_i > 0, i=1,\dots,m.
   $$
1. Let $t = \sum_{i=1}^m t_i$ and $s = 1 - t$. Then, $s > 0$.
1. Let $r = \frac{s}{2 m}$.
1. Let $p_i = t_i + r$. Then, $p_i > 0$ and

   $$
   \sum_{i=1}^m p_i = \sum_{i=1}^m t_i + \sum_{i=1}^m r
   = t + \frac{s}{2} = t + \frac{1 - t}{2} < 1. 
   $$

TBD.
```



### Closure of Relative Interior

```{prf:theorem} Closure of relative interior
:label: res-cvx-convex-relint-closure

Let $\VV$ be a real finite dimensional normed linear space.
For any convex set $C \subseteq \VV$, 

$$
\closure \relint C = \closure C.
$$
```

```{prf:proof}
Since $\relint C \subseteq C$, hence
$\closure \relint C \subseteq \closure C$.


For the other direction, we proceed as follows:

1. Let $\by \in \closure C$.
1. Choose some $\bx \in \relint C$.
1. By {prf:ref}`res-cvx-convex-relint-segment`, 
   the line segment between $\bx$ and $\by$
   (excluding $\by$) lies in $\relint C$.
1. Hence, $\by$ is a limit point of $\relint C$.
1. Thus, $\by \in \closure \relint C$.
1. Thus, $\closure C \subseteq \closure \relint C$.

Combining the two inclusions, we get:

$$
\closure \relint C = \closure C.
$$ 
```

### Relative Interior of Closure

```{prf:theorem} Relative interior of closure
:label: res-cvx-convex-closure-relint

Let $\VV$ be a real finite dimensional normed linear space.
For any convex set $C \subseteq \VV$, 

$$
\relint \closure C = \relint C.
$$
```

```{prf:proof}
The statement is trivial for $C = \EmptySet$. We shall
assume that $C$ is nonempty.

By {prf:ref}`res-cvx-closure-relint`
$\relint C \subseteq \relint \closure C$
holds true for any set $C$.


For the converse, assume that $\bx \in \relint \closure C$.
Our goal is to show that $\bx \in \relint C$. 
Towards this, we have to find points $\by \in \relint C$
and $\bz \in \closure C$ such that $\bx$ lies
on the line segment between $\by$ and $\bz$. 
Since, $C$ is nonempty and convex, it is easy
to pick a point $\by \in \relint C$. Then,
on the path from $\by$ to $\bx$, the point
$\bz$ must be behind $\bx$ and yet not too far 
behind $\bx$ so that we can ensure that $\bz$
is indeed in $\closure C$. That is where
we use the fact that there is a ball 
around $\bx$ whose intersection with $\affine C$
is totally inside $\closure C$.

1. We have, $\bx \in \closure C$ and there exists $r > 0$ such that

   $$
   (\bx + r B) \cap \affine (\closure C) \subseteq \closure C.
   $$
1. Recall from {prf:ref}`res-la-affine-hull-closure` that 
   $\affine (\closure C) = \affine C$.
1. Thus, there exists $r > 0$ such that

   $$
   (\bx + r B) \cap \affine C \subseteq \closure C.
   $$
1. By {prf:ref}`res-cvx-nonempty-relint`, the relative
   interior of $C$ is nonempty.
1. Choose a point $\by \in \relint C$.
1. Let $t = \frac{r}{2\| \bx - \by \|}$.
1. Define
   
   $$
   \bz = (1 + t) \bx - t \by.
   $$
1. $\bz$ is an affine combination of $\bx$ and $\by$.
   Since $\bx \in \closure C$ and $\by \in \relint C \subseteq \closure C$,
   hence $\bz \in \affine (\closure C) = \affine C$.
1. Also note that

   $$
   d(\bz, \bx) &= \| \bz - \bx \|\\
   &= \|(1 + t) \bx - t \by - \bx \|\\
   &= t \| \bx - \by \| = \frac{r}{2}.
   $$
1. Hence, $\bz \in B(x, r)$.
1. Thus, $\bz \in B(x, r) \cap \affine C \subseteq \closure C$.
1. Thus, $\bz \in \closure C$.
1. We have found the points $\by \in \relint C$ and $\bz \in \closure C$.
1. Now note that, 

   $$
   \bx = \frac{t}{1+t} \by + \frac{1}{1+t} \bz.
   $$
1. Thus, $\bx$ is a convex combination of $\by$ and $\bz$.
1. Since $t > 0$,  hence $\bx$ lies in the line segment 
   between $\bz$ and $\by$.
1. By the 
   {prf:ref}`line segment property <res-cvx-convex-relint-segment>`, 
   the line segment between $\bz$ and $\by$
   (excluding $\bz$) lies in $\relint C$.
1. Hence, $\bx \in \relint C$.

Thus, we have shown that $\relint \closure C \subseteq \relint C$
as desired.
```

### Identical Closures and Relative Interiors

```{prf:theorem} Same closure means same relative interior
:label: res-cvx-convex-same-cl-same-relint

Let $\VV$ be a real finite dimensional normed linear space.

Let $C_1$ and $C_2$ be convex subsets of $\VV$.
Then,

$$
\closure C_1 = \closure C_2 \iff \relint C_1 = \relint C_2.
$$

In other words, if closures are same, then relative interiors
must be same too and vice versa.
```

```{prf:proof}
From {prf:ref}`res-cvx-convex-relint-closure`, 
$\closure \relint C = \closure C$
and from {prf:ref}`res-cvx-convex-closure-relint`,
$\relint \closure C = \relint C$ 
for any convex set $C$.

Assume $\closure C_1 = \closure C_2$.
Then, 

$$
\relint C_1 = \relint \closure C_1 = \relint \closure C_2
= \relint C_2.
$$

Now, assume $\relint C_1 = \relint C_2$.
Then,

$$
\closure C_1 = \closure \relint C_1
= \closure \relint C_2 = \closure C_2.
$$
We are done.
```

### Finite Intersections

```{prf:theorem} Finite intersections preserve closure
:label: res-cvx-convex-intersect-finite-closure

Let $\VV$ be a real finite dimensional normed linear space.

Let $C_1, \dots, C_n$ be convex subsets of $\VV$
such that $\cap_i \relint C_i \neq \EmptySet$.
Then,

$$
\closure \left( \bigcap_{i=1}^n C_i \right)
= \bigcap_{i=1}^n \closure C_i.
$$ 
```


```{prf:theorem} Finite intersections preserve relative interior
:label: res-cvx-convex-intersect-finite-interior

Let $\VV$ be a real finite dimensional normed linear space.

Let $C_1, \dots, C_n$ be convex subsets of $\VV$
such that $\cap_i \relint C_i \neq \EmptySet$.
Then,

$$
\relint \left( \bigcap_{i=1}^n C_i \right)
= \bigcap_{i=1}^n \relint C_i.
$$ 
```


```{prf:theorem} Intersection with affine set preserves relative interior and closure
:label: res-cvx-convex-affine-intersect-pres-relint-cl

Let $\VV$ be a real finite dimensional normed linear space.
Let $C$ be a convex set of $\VV$ and $M$ be an affine set
of $\VV$ such that $M$ has a nonempty intersection with
$\relint C$. Then,

$$
\relint (M \cap C) = M \cap \relint C.
$$

Also,

$$
\closure (M \cap C) = M \cap \closure C.
$$
```

```{prf:proof}
Since $\VV$ is finite dimensional, hence

$$
\relint M = \closure M = M
$$
due to {prf:ref}`res-la-affine-closed` 
and {prf:ref}`res-cvx-affine-relative-open`.

Now, by {prf:ref}`res-cvx-convex-intersect-finite-interior`:

$$
\relint (M \cap C)  = (\relint M) \cap (\relint C) 
= M \cap \relint C.
$$

Similarly, by {prf:ref}`res-cvx-convex-intersect-finite-closure`,

$$
\closure (M \cap C)  = (\closure M) \cap (\closure C) 
= M \cap \closure C.
$$
```

Here is another possible condition under which the 
containment of relative interior holds.

```{prf:theorem} Containment of relative interior
:label: res-cvx-nonbd-cl-subset-interior

Let $\VV$ be a real finite dimensional normed linear space.
Let $C_1$ and $C_2$ be convex sets of $\VV$ such that
$C_2 \subseteq \closure C_1$ but
$C_2 \not\subseteq \closure C_1 \setminus \relint C_1$.
Then,

$$
\relint C_2 \subseteq \relint C_1.
$$
In other words, if $C_2$ is a subset of the closure of
$C_1$ but $C_2$ is not contained totally inside the
relative boundary of $C_1$, then 
relative interior of $C_2$ is a subset of the relative
interior of $C_1$.
```

```{div}
Here is an example situation.

1. Let $H$ be a hyperplane.
1. Let $H_+$ be a corresponding nonnegative closed halfspace. 
1. Then, the boundary (also relative boundary)
   of $H_+$ is $H$. 
1. The interior (also relative interior)
   of $H_+$ is the positive open halfspace $H_{++}$.
1. Let $C$ be contained inside $H_+$ such that 
   $C \not\subseteq H$. In other words, $C$ is
   not totally contained inside the boundary of $H_+$
   which is $H$.
1. Then, $\relint C \subseteq H_{++}$.
1. Here $C_1 = H_{++}$ and $C_2 = C$.
1. Note that $C \not\subseteq H_{++}$ but
   $C \subseteq \closure H_{++} = H_+$.
1. $\closure C_1 \setminus \relint C_1 = \closure H_{++} \setminus \relint H_{++} = H_+ \setminus H_{++} = H$.
```

```{prf:proof}
Due to {prf:ref}`res-cvx-convex-closure-relint`

$$
\relint \closure C_1 = \relint C_1.
$$
```

### Sum of Sets

```{prf:theorem} Relative interior of sum of two sets
:label: res-cvx-convex-sum-relint

Let $\VV$ be a real finite dimensional normed linear space.
Let $C_1$ and $C_2$ be convex sets of $\VV$.
Then,

$$
\relint (C_1 + C_2) = \relint C_1 + \relint C_2.
$$
```

```{prf:theorem} Closure of sum of two sets
:label: res-cvx-convex-sum-closure

Let $\VV$ be a real finite dimensional normed linear space.
Let $C_1$ and $C_2$ be convex sets of $\VV$.
Then,

$$
\closure (C_1 + C_2) \supseteq \closure C_1 + \closure C_2.
$$
```

### Affine Transformations

```{prf:theorem}
:label: res-cvx-relint-aff-map-pres

Let $\VV$ be a finite dimensional normed linear space.
A bijective affine transformation $T : \VV \to \VV$ 
preserves relative interiors.

$$
T (\relint A) = \relint (T (A)).
$$
```



