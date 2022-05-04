(sec:convex:sets)=
# Convex Sets

Throughout this section, we assume that $\VV$ is a 
real vector space. Wherever necessary, 
it is equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \| : \VV \to \RR$
or a {prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle : \VV \times \VV \to \RR$. 
It is also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$.


## Line Segments

```{prf:definition} Line segment
:label: def-line-segment

Let $\bx_1$ and $\bx_2$ be two points in $\VV$. Points of the form

$$
\by = (1 - \theta) \bx_1 + \theta \bx_2 \text{ where } 0 \leq \theta \leq 1
$$ 
form a (closed) *line-segment* between $\bx_1$ and $\bx_2$. 
The closed line segment is denoted by $[\bx_1, \bx_2]$.

$$
[\bx_1, \bx_2] \triangleq \{ (1 - \theta) \bx_1 + \theta \bx_2 \ST 0 \leq \theta \leq 1 \}.
$$ 

Similarly, we define an *open line segment* as:

$$
(\bx_1, \bx_2) \triangleq \{ (1 - \theta) \bx_1 + \theta \bx_2 \ST 0 < \theta < 1 \}.
$$ 

The *half-open segment* $(\bx_1, \bx_2]$ is defined as:

$$
(\bx_1, \bx_2] \triangleq \{ (1 - \theta) \bx_1 + \theta \bx_2 \ST 0 < \theta \leq 1 \}.
$$ 

The *half-open segment* $[\bx_1, \bx_2)$ is defined as:

$$
[\bx_1, \bx_2) \triangleq \{ (1 - \theta) \bx_1 + \theta \bx_2 \ST 0 \leq \theta < 1 \}.
$$ 
```

## Convex Sets


````{prf:definition} Convex set
:label: def-convex-set

A set $C \subseteq \VV$ is *convex* if the line segment between 
any two points in $C$ lies in $C$. i.e.

$$
\theta \bx_1 + (1 - \theta) \bx_2 \in C 
\Forall \bx_1, \bx_2 \in C \text{ and } 0 \leq \theta \leq 1.
$$
````

The empty set is vacuously convex. 
The entire vector space  $\VV$ is convex
since it contains all the line segments between
any pair of points in the space.

```{prf:observation}
Since a convex set contains the line segment between any
two points, any line segment is convex by definition.
```

Geometrically, a convex set has no holes, hollows, pits or dimples.
A set is convex if from each point in the set, it is possible 
to see every other point without having the line of sight pass
outside the set.

```{prf:example} Real line
On the real line $\RR$, the empty set, sing points,
intervals (closed, open, half open), half lines, 
and the entire real line are convex sets. 
There are no other convex sets possible.
```

```{prf:theorem}
:label: res-convex-linear-subspace

Any linear subspace is convex.
```

```{prf:proof}
Let $\EE$ be a linear subspace of $\VV$.
Then $\EE$ is closed under addition
and scalar multiplication. 
Thus, for any $\bx, \by \in \EE$ and $0 \leq t \leq 1$,

$$
t \bx + (1-t)\by \in \EE.
$$

Thus, $\EE$ is convex.
```

```{prf:theorem}
:label: res-convex-affine-set

Any {prf:ref}`affine set <def-affine-set>` is convex.
```
```{prf:proof}
Let $C \subseteq \VV$ be an affine set.
By definition, for any $\bx, \by \in C$
and any $t \in \RR$,
$t \bx + (1-t)\by \in C$.
It is valid in particular for $0 \leq t \leq 1$.
Thus, $C$ is convex.
```

```{prf:theorem}
:label: res-convex-hyperplane

Any {prf:ref}`hyperplane <def-hyperplane>` is convex
since it is affine.
```

```{prf:theorem}
:label: res-convex-half-space

{prf:ref}`Half spaces <def-halfspace>` are convex.
```

```{prf:proof}
Consider $H_+$ defined as:

$$
    H_+ = \{ x : \langle \ba, \bx \rangle \geq b \}
$$

Let $\bx, \by \in H_+$. Then:

$$
\langle \ba, \bx \rangle \geq b
\text{ and }
\langle \ba, \by \rangle \geq b.
$$

For some $0 \leq t \leq 1$:

$$
\langle \ba, t \bx + (1 - t) \by \rangle
= t \langle \ba, \bx \rangle + (1 - t)\langle \ba, \by \rangle
\geq t b + (1 -t )b  = b.
$$

Thus, $\bx + (1 - t) \by \in H_+$.
Analogous proofs apply for other types of half spaces.
```

## Rays

```{prf:definition} Ray
:label: def-convex-ray

A *ray* $R$ is defined as 

$$
R \triangleq \{ \bx_0 + t \bv \ST t \geq 0 \}
$$ 
where $\bv \neq \bzero$ indicates the direction of ray 
and $\bx_0$ is the base or origin of ray.
```

```{prf:theorem}
:label: res-convex-ray

A ray is convex.
```
```{prf:proof}

Let a ray be given as:

$$
R = \{ \bx_0 + t \bv \ST t \geq 0 \}.
$$

Let $\bu, \bv \in R$. Thus, there is $t_u, t_v \geq 0$
such that:

$$
\bu = \bx_0 + t_u \bv \text{ and }
\bv = \bx_0 + t_v \bv.
$$

Now, for some $0 \leq r \leq 1$,

$$
r \bu + (1 - r) \bv 
&= r (\bx_0 + t_u \bv) + (1 - r) (\bx_0 + t_v \bv)\\
&= \bx_0 + (r t_u + (1 - r) t_v) \bv.
$$
Since $r t_u + (1 - r) t_v \geq 0$, hence
$r \bu + (1 - r) \bv  \in R$.
```

## Balls


```{prf:theorem}
:label: res-convex-open-ball

An {prf:ref}`open ball <def-ms-open-ball>` $B(\ba, r)$ is convex
for any {prf:ref}`norm <def-la-norm>` $\| \cdot \| : \VV \to \RR$.
```

```{prf:proof}
Recall that an open ball in a normed linear space
is defined as:

$$
B(\ba,r) = \{ \bx \in \VV \ST \| \bx - \ba \| < r \}.
$$

Let $\bx, \by \in B(\ba,r)$ and let $0 \leq t \leq 1$.
Then,

$$
t \bx + (1-t)\by  - \ba 
= t (\bx - \ba) + (1-t) (\by - \ba).
$$

By triangle inequality:

$$
\| t (\bx - \ba) + (1-t) (\by - \ba) \|
&\leq \| t (\bx - \ba) \| + \| (1-t) (\by - \ba) \|\\
&= t \| \bx - \ba \| + (1 -t) \| \by - \ba \|\\
&< t r + (1 - t)r = r.
$$

Thus,

$$
\| t \bx + (1-t)\by  - \ba \| < r
\implies t \bx + (1-t)\by \in B(\ba,r).
$$
```

```{prf:theorem}
:label: res-convex-closed-ball

A {prf:ref}`closed ball <def-ms-closed-ball>` $B[\ba, r]$ is convex
for any {prf:ref}`norm <def-la-norm>` $\| \cdot \| : \VV \to \RR$.
```

```{prf:proof}
Recall that a closed ball in a normed linear space
is defined as:

$$
B[\ba,r] = \{ \bx \in \VV \ST \| \bx - \ba \| \leq r \}.
$$

Let $\bx, \by \in B(\ba,r)$ and let $0 \leq t \leq 1$.
Then,

$$
t \bx + (1-t)\by  - \ba 
= t (\bx - \ba) + (1-t) (\by - \ba).
$$

By triangle inequality:

$$
\| t (\bx - \ba) + (1-t) (\by - \ba) \|
&\leq \| t (\bx - \ba) \| + \| (1-t) (\by - \ba) \|\\
&= t \| \bx - \ba \| + (1 -t) \| \by - \ba \|\\
&\leq t r + (1 - t)r = r.
$$

Thus,

$$
\| t \bx + (1-t)\by  - \ba \| \leq r
\implies t \bx + (1-t)\by \in B[\ba,r].
$$
```

## Convex Combinations


````{prf:definition} Convex combination
:label: def-convex-combination

We call a point of the form $\theta_1 \bx_1  + \dots + \theta_k \bx_k$, where
$\theta_1 + \dots + \theta_k  = 1$ and $\theta_i \geq 0, i=1,\dots,k$,
a *convex combination* of the points $\bx_1, \dots, \bx_k$.
````
It is like a weighted average of the points $\bx_i$.
A weights $\theta_i$ in a convex combination can be
interpreted as probabilities or proportions.


```{prf:example} Center of mass
:label: ex-convex-combination-center-mass

Consider a system of particles $p_i$, $i=1,\dots,n$ 
each with mass $m_i$ and location in space as $\bx_i$.
The center of mass $\bx$ satisfies the equation:

$$
\sum_{i=1}^n m_i (\bx_i - \bx) = 0.
$$

Solving this equation gives us:

$$
\bx = \sum_{i=1}^n \frac{m_i}{m} \bx_i
$$
where $m = \sum_{i=1}^n m_i$.

If we assign $\theta_i = \frac{m_i}{m}$, we notice that
$\theta_i \geq 0$ and $\sum_{i=1}^n \theta_i = 1$. 
We can now write the center of mass as:

$$
\bx = \sum_{i=1}^n \theta_i \bx_i
$$
which is a convex combination of the locations $\bx_i$ 
where $\theta_i$ gives the proportion of contribution
of each particle according to its mass.
```

```{prf:remark} Convex combinations and unit simplex
:label: rem-cvx-conv-comb-coef-unit-simplex

We recall that the unit simplex in $\RR^n$ is given by

$$
\Delta_n = \{ \bt \in \RR^n \ST  
   \langle \bt, \bone \rangle = 1, \bt \succeq \bzero \}
= \{\bt \in \RR^n \ST  t_1 + \dots + t_n = 1, t_1, \dots, t_n \geq 0 \}.
$$
Thus, the coefficients for convex combinations of $n$ points
are drawn from $\Delta_n$.
```

````{prf:theorem} Closure under convex combinations
:label: res-cvx-convex-set-convex-combinations

A set is convex if and only if it contains all convex combinations of its points.

Let $\VV$ be a real vector space and $C$ be a subset of $\VV$.
Then, $C$ is convex if and only if for any $m \in \Nat$,
for any $\bx_1, \dots, \bx_m \in C$, and for every $\bt \in \Delta_m$,
$t_1 \bx_1 + \dots + t_m \bx_m \in C$. 
````

```{prf:proof}
We know that a set $C$ is convex is equivalent to 
saying that it contains all 2 point convex combinations;
i.e, for any $\bx_1, \bx_2 \in C$, $t_1, t_2 \geq 0$ and $t_1 + t_2 = 1$,

$$
t_1 \bx_1 + t_2 \bx_2 \in C. 
$$

We first show that if $C$ is convex, it contains all its
(finite) convex combination by induction.

1. By definition $C$ contains all its 2 point convex combinations.
1. As induction hypothesis, assume that $C$ contains all
   convex combinations of $m-1$ or fewer points where $m > 2$.
1. Consider a convex combination of $m$ points

   $$
   \sum_{i=1}^m t_i \bx_i 
   $$
   where $\bx_i \in C$, $t_i \geq 0$, $\sum t_i = 1$.
1. Since $\sum t_1 = 1$, hence at least one of $t_i < 1$. 
1. Without loss of generality, assume $t_m < 1$.
1. Note that $t_m < 1$ means that $1 - t_m > 0$. 
1. Define $\by = \sum_{i=1}^{m-1} t'_i \bx_i$ where
   $t'_i = \frac{t_i}{1 - t_m}$.
1. Note that $t'_i \geq 0$. Also, $\sum_{i=1}^{m-1} t'_i = 1$
   since $\sum_{i=1}^{m-1} t_i = 1 - t_m$.
1. Thus, $\by$ is an $m-1$ point convex combination of $C$.
1. By induction hypothesis, $\by \in C$.
1. Now, $(1-t_m) \by = \sum_{i=1}^{m-1} t_i \bx_i$.
1. Hence, $\bx = (1 - t_m) \by + t_m \bx_m$.
1. It is a 2 point convex combination of $\by$ and $\bx_m$.
1. Since both $\by, \bx_m \in C$, hence $\bx \in C$.
1. Thus, $C$ contains all its $m$ point convex combinations.

For the converse, note that if $C$ contains all its
convex combinations, then it contains, in particular,
all its two point convex combinations. Hence, $C$
is convex.
```

```{prf:theorem}
:label: res-cvx-convex-comb-convex-combs

A convex combination of convex combinations is a convex combination.
```

```{prf:proof}
Let $S \subseteq \VV$. Note that $S$ is arbitrary (no convexity assumed).

1. Consider $n$ points $\by_i$, $i=1,\dots, n$ described as below.
1. Let $\by_i = \sum_{j=1}^{m_j}t_{i,j} \bx_{i,j}$ be convex combinations
   of $m_j$ points: 
   * $\bx_{i,1}, \dots, \bx_{i,m_j} \in S$.
   * $t_{i,j} \geq 0$. 
   * $\sum_{j=1}^{m_j} t_{i, j} = 1$.
1. Consider the convex combination $\by = \sum_{i=1}^n r_i \by_i$.
   * $r_i \geq 0$.
   * $\sum r_i = 1$.
1. We need to show that $\by$ is a convex combination of points of $S$.

Towards this:

$$
\by &= \sum_{i=1}^n r_i \by_i\\
&= \sum_{i=1}^n r_i \sum_{j=1}^{m_j}t_{i,j} \bx_{i,j}\\
&= \sum_{i=1}^n \sum_{j=1}^{m_j} r_i t_{i,j} \bx_{i,j}.
$$

Consider the terms:

$$
s_{i, j} =  r_i t_{i,j}.
$$

Since $r_i \geq 0$ and $t_{i, j} \geq 0$, hence $s_{i, j } \geq 0$.

Now, consider their sum:

$$
\sum_{i=1}^n \sum_{j=1}^{m_j} s_{i, j} 
&= \sum_{i=1}^n \sum_{j=1}^{m_j} r_i t_{i,j} \\
&= \sum_{i=1}^n r_i \sum_{j=1}^{m_j} t_{i,j}\\
&= \sum_{i=1}^n r_i = 1\\
$$

Thus, $\sum_{i,j} s_{i, j} = 1$.

Hence,

$$
\by = \sum_{i,j} s_{i, j} x_{i, j}
$$
is a convex combination of points of $S$.
```

## Convex Hull

````{prf:definition} Convex hull
:label: def-convex-hull

The *convex hull* of an arbitrary set $S \subseteq \VV$ denoted as
$\ConvexHull(S)$, is the set of all convex combinations of points in $S$.

$$
    \ConvexHull(S) = \{ \theta_1 \bx_1 + \dots + \theta_k \bx_k | \bx_k \in S, \theta_i \geq 0, i = 1,\dots, k,
    \theta_1 + \dots + \theta_k = 1\}.
$$

````

````{prf:theorem}
:label: res-cvx-convex-hull-convex

The convex hull $\ConvexHull(S)$ of a set $S$ is always convex.
````

```{prf:proof}
Let $\bx, \by \in \ConvexHull(S)$, $t \in [0,1]$ and 
the point $\bz = t \bx + (1-t) \by$.
We need to show that $\bz \in \ConvexHull(S)$.

1. $\bx, \by$ are convex combinations of points of $S$.
1. $\bz$ is a convex combination of $\bx$ and $\by$.
1. Hence, $\bz$ is a convex combination of convex combinations of points in $S$.
1. By {prf:ref}`res-cvx-convex-comb-convex-combs`, 
   a convex combination of convex combinations is a convex combination.
1. Thus, $\bz$ is a convex combination of points of $S$.
1. But $\ConvexHull(S)$ contains all convex combinations of points of $S$ by definition.
1. Hence, $\bz \in \ConvexHull(S)$.
1. Thus, $\ConvexHull(S)$ is convex.
```



````{prf:theorem}
:label: res-cvx-convex-hull-smallest

The convex hull of a set $S$ is the smallest convex set containing it. In other words,
let $C$ be any convex set such that $S \subseteq C$. Then $\ConvexHull(S) \subseteq C$.
````

```{prf:proof}
Let $C$ be a convex set such that $S \subseteq C$.

1. Let $\bx \in \ConvexHull(S)$.
1. Then, $\bx$ is a convex combination of points of $S$.
1. $C$ is convex and $S \subseteq C$.
1. Hence, $C$ contains every convex combination of points of $S$.
1. Thus, in particular $\bx \in C$.
1. Since $\bx \in \ConvexHull(S)$ was arbitrary, hence $\ConvexHull(S) \subseteq C$.
```

We could have started as defining the convex hull of $S$ being
the smallest convex set containing $S$ and arrived at the conclusion
that $\ConvexHull(S)$ contains all convex combinations of $S$.
Some authors prefer to define $\ConvexHull(S)$ as the smallest convex
set containing $S$. Both definitions are equivalent.


```{prf:theorem} Carathéodory theorem
:label: res-cvx-conv-hull-caratheodory

Let $\VV$ be an $n$-dimensional real vector space. 
Let $S \subseteq \VV$. Let $\bx \in \ConvexHull(S)$.

Then, there exists a set of $n+1$ points $\bx_0, \dots, \bx_n \in S$
such that 

$$
\bx \in \ConvexHull (\{ \bx_0, \dots, \bx_n\});
$$
i.e., there exists a $\bt \in \Delta_{n+1}$ such that 

$$
\bx = \sum_{i=0}^n t_i \bx_i.
$$
```

```{prf:proof}
We note that $\bx \in \ConvexHull(S)$.

1. Thus, there exists a set of $k+1$ points in $S$
   and $\bt \in \Delta_{k+1}$
   such that

   $$
   \bx = \sum_{i=0}^k t_i \bx_i.
   $$
1. We can assume $t_i > 0$ for all $i=0, \dots, k$ 
   since otherwise, we can drop the vectors corresponding
   to the zero coefficients from the convex combination.
1. If $k \leq n$, there is nothing to prove.
1. Hence, consider the case where $k > n$.
1. We now describe a process which can reduce the number
   of points in the convex combination by one.
1. The $k$ vectors $\bx_1 - \bx_0, \dots, \bx_k - \bx_0$ are 
   linearly dependent as $k > n$ and $\VV$ is $n$-dimensional.
1. Thus, there is a nontrivial linear combination of these 
   vectors 

   $$
   r_1 (\bx_1 - \bx_0) + \dots + r_k (\bx_k - \bx_0) = \bzero.
   $$
1. Let $r_0 = -r_1 - \dots - r_k$. Then, we have a
   nontrivial combination

   $$
   \sum_{i=0}^k r_i \bx_i = \bzero
   $$
   with $\sum r_i = 0$.
1. In particular, there exists at least one index $j$ for which $r_j < 0$.
1. Let $\alpha \geq 0$.
1. Then,

   $$
   \bx = \sum_{i=0}^k t_i \bx_i + \alpha \sum_{i=0}^k r_i \bx_i
   = \sum_{i=0}^k (t_i + \alpha r_i) \bx_i
   $$
   with $\sum (t_i + \alpha r_i) = \sum t_i + \alpha \sum r_i = 1$.
1. Thus, it is a convex combination for $\bx$ if 
   $t_i + \alpha r_i \geq 0$ for every $i=0, \dots, k$.
1. Let 

   $$
   \alpha = \underset{i \ST r_i < 0}{\min}\left \{ - \frac{t_i}{r_i} \right \}.
   $$
1. $\alpha$ is well defined since there is at least one $r_j < 0$.
   Let $j$ be the index for which $\alpha$ was obtained.
1. Then, $t_j + \alpha r_j = 0$.
1. Also, we can see that $t_i + \alpha r_i \geq 0$ for all $i=0,\dots,k$.
1. Thus, we have found a convex combination for $\bx$ where
   the coefficient for $\bx_j$ is 0.
1. Thus, we have obtained a convex combination for $\bx$ with
   $k-1$ points.
1. Repeating this process up to $k-n$ times, we can obtain a convex combination
   of $\bx$ consisting of $n+1$ or less points.
```

## Dimension

```{prf:definition} Dimension of a convex set
:label: def-cvx-convex-set-dim

The dimension of a convex set is defined to be
the dimension of its 
{prf:ref}`affine hull <def-affine-hull>`.

If $C$ is a convex set, then:

$$
\dim C = \dim \affine C.
$$
```
Recall that the dimension of an affine
set is equal to the dimension of the
linear subspace associated with it
({prf:ref}`def-affine-dimension`).

1. A circle will have a dimension of 2 even 
   if it is in $\RR^3$.
1. A sphere will have a dimension of three.


## Simplices 

```{prf:theorem} Convex hull of a finite set of points
:label: res-cvx-convex-hull-finite-set

Let $S = \{ \bx_0, \dots, \bx_m \}$ be a finite set of
points of $\VV$. Then, $\ConvexHull(S)$ consists of
all the points of the form 

$$
t_0 \bx_0 + \dots t_m \bx_m, \quad 
t_0 \geq 0, \dots, t_m \geq 0, \sum_{i=0}^m t_i = 1.
$$
```

In $\RR^n$, this is known as a {prf:ref}`polytope <def-convex-polytope>`.

A Simplex is a convex hull of a finite set of
affine independent points. The simplex provides
a powerful coordinate system for the points
within it in terms of barycentric coordinates.

````{prf:definition} $k$-simplex
:label: def-convex-simplex

Let $k+1$ points $\bv_0, \dots, \bv_k \in \VV$ be 
{prf:ref}`affine independent <def-affine-independence>`.

The *simplex* determined by them is given by

$$
C = \ConvexHull \{ \bv_0, \dots, \bv_k\}
= \{ t_0 \bv_0 + \dots + t_k \bv_k \ST 
    \bt \succeq 0, \bone^T \bt = 1\}
$$

where $\bt = [t_1, \dots, t_k]^T$ and
$\bone$ denotes a vector of appropriate size $(k)$ 
with all entries one.

In other words, $C$ is the convex hull of the set 
$\{\bv_0, \dots, \bv_k\}$.
````
A simplex is a convex set since it is a convex hull of its vertices.
$k$ stands for the dimension of the simplex.
{prf:ref}`Recall <def-cvx-convex-set-dim>` that the
dimension of a convex set is the dimension of its
affine hull.

```{prf:example} Simplex examples
:label: ex-cvx-simplex-examples

In $\RR^n$:

* A 0-simplex is a point.
* A 1-simplex is a line segment (2 points).
* A 2-simplex is a triangle (3 points).
* A 3-simplex is a tetrahedron (4 points).
* A 4-simplex is a 5-cell (5 points).
```

```{prf:theorem} Barycentric coordinates
:label: res-cvx-simplex-barycentric-rep

Each point of a $k$ simplex is *uniquely* expressible
as a convex combination of the vertices. 
```

```{prf:proof}

Let $C = \ConvexHull\{\bv_0, \bv_1, \dots, \bv_k \}$.

1. Let $\bv \in C$.
1. Then, $\bv = \sum_{i=0}^k t_i \bv_i$ with $t_i \geq 0$ 
   and $\sum t_i = 1$.
1. For contradiction, assume there was another representation:
   $\bv = \sum_{i=0}^k r_i \bv_i$ with $r_i \geq 0$ 
   and $\sum r_i = 1$.
1. Then,

   $$
   \sum_{i=0}^k t_i \bv_i = \sum_{i=0}^k r_i \bv_i
   \implies \sum_{i=0}^k (t_i - r_i) \bv_i = \bzero.
   $$
1. But $\{\bv_0, \bv_1, \dots, \bv_k \}$ are affine independent.
1. Hence, $t_i = r_i$.
1. Thus, the representation is unique.
```

```{prf:definition} Simplex midpoint
:label: def-convex-simplex-midpoint

The point $\sum_{i=0}^k \frac{1}{k+1}{\bv_i}$ 
in a simplex $C = \ConvexHull\{\bv_0, \dots, \bv_k \}$
is known as its *midpoint* or *barycenter*.
```

```{prf:theorem}
:label: res-cvx-convex-set-dimension-simplex-size

The dimension of a convex set $C$ is the maximum 
of the dimensions of the various simplices 
included in $C$.
```
```{prf:proof}
We need to show that there is a simplex
$S \subset C$ such that $\dim S = \dim C$.


1. Let $A$ be any finite affine independent subset of $C$.
1. Since $C$ is convex, hence 
   $A \subseteq C \implies \ConvexHull(A) \subseteq C$.
1. Thus, $C$ contains the simplices constructed from 
   any set of finite affine independent points in $C$.
1. Thus, if $A = \{\bv_0, \dots, \bv_k\}$ is a set of 
   $k+1$ affine independent points of $C$, then
   $\ConvexHull(A) \subseteq C$ implies that $k \leq \dim C$.
1. Thus, if $S$ is a $k$-simplex such that $S \subseteq C$,
   then $\dim S = k \leq \dim C$.
1. Let $m$ be the maximum of the dimensions of the
   various simplices contained in $C$.
1. Then, there exist affine independent points 
   $\bv_0, \dots, \bv_m \in C$ such that 
   the simplex $S = \ConvexHull\{ \bv_0, \dots, \bv_m\} \subseteq C$.
1. Let $M$ be the affine hull of $S$; i.e. $M = \affine S$.
1. Then, $\dim M = m$ and $M \subseteq \affine C$.
1. If $C \setminus M$ were nonempty, then there would be
   an element $\bv \in C \setminus M$ which would be
   affine independent of $\{ \bv_0, \dots, \bv_m\}$.
1. That would lead to a set of $m+2$ affine independent
   points in $C$.
   That would mean that $C$ contains a simplex of 
   dimension $m+1$. 
   A contradiction.
1. Hence, $C \setminus M = \EmptySet$.
1. Thus, $C \subseteq M$.
1. Since $\affine C$ is the smallest affine set
   that contains $C$, hence $\affine C = M$.
1. Thus, $\dim C = m$.
```

## Symmetric Reflections


The {prf:ref}`symmetric reflection <def-vs-symmetric-reflection>`
of a convex set is convex
since convexity is preserved under scalar multiplication.
See {prf:ref}`res-cvx-convexity-scalar-multiplication` below.

If a {prf:ref}`symmetric <def-vs-symmetric-set>` convex set 
contains a nonzero vector $\bx$, then it contains
the entire line segment between $-\bx$ and $\bx$.


## Infinite Convex Combinations

We can generalize convex combinations to include infinite sums.
````{prf:theorem}
:label: res-cvx-infinite-convex-combination

Let $\theta_1, \theta_2, \dots$ satisfy

$$
    \theta_i \geq 0, i = 1,2,\dots, \quad \sum_{i=1}^{\infty} \theta_i = 1,
$$

and let $\bx_1, \bx_2, \dots \in C$, where $C \subseteq \VV$ is convex. Then

$$
    \sum_{i=1}^{\infty} \theta_i \bx_i \in C,
$$

if the series converges.
````

We can generalize it further to density functions.
````{prf:theorem}
:label: res-cvx-convex-density

Let $p : \VV \to \RR$ satisfy $p(x) \geq 0$ for all  $x \in C$
and

$$
    \int_{C} p(x) d x = 1
$$

Then

$$
    \int_{C} p(x) x d x \in C
$$

provided the integral exists.
````

Note that $p$ above can be treated as a probability density function if
we define $p(x) = 0 \Forall x \in \VV \setminus C$.



## Convexity Preserving Operations

In the following, we will discuss several operations which
transform a convex set into another convex set, and thus
preserve convexity.

Understanding these operations is useful for determining
the convexity of a wide variety of sets.

Usually, it is easier to prove that a set is convex by showing
that it is obtained by a convexity preserving operation from
a convex set compared to directly verifying the convexity property
i.e. 

$$
t \bx_1 + (1 - t) \bx_2 \in C \Forall \bx_1, \bx_2 \in C, t \in [0,1].
$$

### Intersection and Union

````{prf:theorem} Intersection of convex sets
:label: res-cvx-intersection

If $S_1$ and $S_2$ are convex sets then $S_1 \cap S_2$ is convex.
````

````{prf:proof}
Let $\bx_1, \bx_2 \in S_1 \cap S_2$. We have to show that

$$
t \bx_1 + (1 - t) \bx_2 \in S_1 \cap S_2, \Forall t \in [0,1].
$$

Since $S_1$ is convex and $\bx_1, \bx_2 \in S_1$, hence

$$
t \bx_1 + (1 - t) \bx_2 \in S_1, \Forall t \in [0,1].
$$

Similarly

$$
t \bx_1 + (1 - t) \bx_2 \in S_2, \Forall t \in [0,1].
$$

Thus

$$
t \bx_1 + (1 - t) \bx_2 \in S_1 \cap S_2, \Forall t \in [0,1].
$$

which completes the proof.
````

We can generalize it further.

````{prf:theorem} Intersection of arbitrary collection of convex sets
:label: res-cvx-arbitrary-intersection

Let $\{ A_i\}_{i \in I}$ be a family of sets such that $A_i$ is convex
for all $i \in I$.  Then $\cap_{i \in I} A_i$ is convex.
````

````{prf:proof}
Let $\bx_1, \bx_2$ be any two arbitrary elements in $\cap_{i \in I} A_i$.

$$
&\bx_1, \bx_2 \in \cap_{i \in I} A_i\\
\implies & \bx_1, \bx_2 \in A_i \Forall i \in I\\
\implies &t \bx_1 + (1 - t) \bx_2 \in A_i \Forall t \in [0,1] \Forall i \in I
\text{ since $A_i$ is convex }\\
\implies &t \bx_1 + (1 - t) \bx_2 \in \cap_{i \in I} A_i.
$$

Hence $\cap_{i \in I} A_i$ is convex.
````

```{prf:corollary} Arbitrary intersection of closed half spaces
:label: res-cvx-arbitrary-intersection-half-spaces

Let $I$ be an index set. Let $\ba_i \in \VV$ and $b_i \in \RR$
for every $i \in I$. Then, the set:

$$
C = \{ \bx \in \VV \ST \langle \bx, \ba_i \rangle \leq b_i \Forall i \in I\}
$$
is convex.
```
```{prf:proof}
Since each of the half spaces is convex, hence so is their
intersection.
```
This result is applicable for open half spaces 
and hyperplanes too too. It also applies 
for a mixture of hyperplanes and half-spaces.


```{prf:corollary} 
:label: res-cvx-linear-equalities-inequalities

The solution set of a system of linear equations and inequalities
in $\RR^n$ is convex.
```

```{prf:proof}
We proceed as follows:

* The solution set of each linear equation is a hyperplane.
* The solution set of each linear inequality is a half-space
  (closed or open).
* The solution set of a system of linear equations and 
  inequalities is the intersection of these 
  hyperplanes and half-spaces.
* Each hyperplane and each half-space is convex.
* Hence, their intersection is convex.
```

```{prf:theorem} Intersection and union of two sets
:label: res-cvx-convex-pair-largest-smallest

Let $C_1$ and $C_2$ be convex in $\VV$.
Then, the largest convex set contained in both is $C_1 \cap C_2$.
And, the smallest convex set containing both is $\ConvexHull (C_1 \cup C_2)$.
```
```{prf:proof}
Let $C$ be a convex set contained in both $C_1$ and $C_2$. Then,
$C \subseteq C_1 \cap C_2$.
But $C_1 \cap C_2$ is convex ({prf:ref}`res-cvx-intersection`).
Hence, $C_1 \cap C_2$ is the largest convex set contained in both $C_1$
and $C_2$.


Let $C$ be a convex set which contains both $C_1$ and $C_2$.
Then, $C_1 \cup C_2 \subseteq C$.
The smallest convex set containing $C_1 \cup C_2$ is its
convex hull given by $\ConvexHull(C_1 \cup C_2)$
({prf:ref}`res-cvx-convex-hull-smallest`).
```


```{prf:theorem} Intersection and union of arbitrary sets
:label: res-cvx-convex-collection-largest-smallest

Let $I$ be an index set and $\FFF = \{ C_i \}_{i \in I}$
be a family of convex sets in $\VV$. 
Then, the largest convex set contained in every set of $\FFF$ is:

$$
\bigcap_{i \in I}C_i.
$$
And, the smallest convex set containing every set of $\FF$ is 

$$
\ConvexHull \left (\bigcup_{i \in I} C_i \right ).
$$
```
```{prf:proof}
Let $C$ be a convex set contained in every set of  $\FFF$. Then,
$C \subseteq \bigcap_{i \in I}C_i$.
But $\bigcap_{i \in I}C_i$ is convex ({prf:ref}`res-cvx-arbitrary-intersection`).
Hence, $\bigcap_{i \in I}C_i$ is the largest convex set contained in 
every set of $\FFF$.


Let $C$ be a convex set which contains every set of $\FF$.
Then, $\bigcup_{i \in I} C_i \subseteq C$.
The smallest convex set containing every set of $\FF$ is its
convex hull given by $\ConvexHull(\bigcup_{i \in I} C_i)$
({prf:ref}`res-cvx-convex-hull-smallest`).
```


### Affine Functions

Let us start with some simple results.

```{prf:theorem} Convexity and translation
:label: res-cvx-convexity-translation

Convexity is preserved under translation. 

$C$ (a subset of $\VV$) is convex
if and only if $C + \ba$ is convex for every $\ba \in \VV$.
```


```{prf:proof}
Let $C \subseteq \VV$.

1. Assume $C$ is convex.
1. Then, for every $\bx, \by \in C$ and every $t \in [0,1]$, 
   $t \bx + (1-t) \by \in C$.
1. Let $\ba \in \VV$.
1. Let $\bu, \bv \in C + \ba$.
1. Then, $\bu = \bx + \ba$ and $\bv = \by + \ba$ for some $\bx, \by \in C$.
1. Then, 
   
   $$
   t \bu + (1-t) \bv 
   &= t (\bx + \ba) + (1-t ) (\by + \ba)\\
   &= t \bx + (1-t) \by + \ba. 
   $$
1. But $t \bx + (1-t) \by \in C$ since $C$ is convex.
1. Then, $t \bx + (1-t) \by + \ba \in C + \ba$.
1. Thus, $t \bu + (1-t) \bv \in C + \ba$.
1. Thus, $C + \ba$ is convex.

We can follow the same argument in the opposite direction
to establish that $C + \ba$ is convex implies $C$ is convex.
```

```{prf:theorem} Convexity and scalar multiplication
:label: res-cvx-convexity-scalar-multiplication

Convexity is preserved under scalar multiplication. 

$C$ (a subset of $\VV$) is convex
if and only if $ \alpha C$ is convex for every $\alpha \in \RR$.
```


```{prf:proof}
Let $C \subseteq \VV$.

1. Assume $C$ is convex.
1. Let $\alpha \in \RR$.
1. Let $\bu, \by \in \alpha C$.
1. Then, $\bu = \alpha \bx$ and $\bv = \alpha \by$ 
   for some $\bx, \by \in C$.
1. Let $t \in [0,1]$.
1. $t\bu + (1-t)\bv = \alpha (t \bx + (1-t)\by)$.
1. But $t \bx + (1-t)\by \in C$ since $C$ is convex.
1. Hence, $\alpha (t \bx + (1-t)\by)$ in $\alpha C$.
1. Hence, $t\bu + (1-t)\bv \in \alpha C$.
1. Thus, $\alpha C$ is convex. 

Similar argument in opposite direction establishes
that $\alpha C$ is convex implies $C$ is convex.
```

Recall that an
{prf:ref}`affine function <def-la-affine-operator>`
$f : \VV \to \EE$ from a real vector space $\VV$ to
another real vector space $\EE$ is a function which satisfies

$$
f(t \bx + (1-t)\by) = tf(\bx) + (1 -t) f(\by)
$$ 
for every $t \in \RR$. 

Recall from {prf:ref}`res-la-op-affine-linear-p-offset`
that an affine function can be written as 
a linear transformation followed by a translation:

$$
f(\bx) = T (\bx) + \bb
$$
where $T$ is a {prf:ref}`linear operator <def-la-linear-transformation>`.

````{prf:example}
An affine function $f : \RR^n \to \RR^m$ takes
the form of a matrix multiplication plus a vector addition:

$$
f(\bx) = \bA \bx + \bb
$$

where $\bA \in \RR^{m \times n}$ and $\bb \in \RR^m$.
````



````{prf:theorem} Image under affine function
:label: res-cvx-convex-set-affine-image

Let $S \subseteq \VV$ be convex and 
$f : \VV \to \EE$ be an affine function. 
Then the image of $S$ under $f$ given by

$$
    f(S) = \{ f(\bx) | \bx \in S\}
$$
is a convex set.
````

```{prf:proof}
We proceed as follows:

1. Let $\bu, \bv \in f(S)$. 
1. Then, $\bu = f(\bx)$ and $\bv = f(\by)$
   for some $\bx, \by \in S$.
1. Let $0 \leq t \leq 1$.
1. Then, $\bz = t \bx + (1-t)\by \in S$ since $S$
   is convex.
1. Since $f$ is affine, hence
   
   $$
   f(\bz) = f(t \bx + (1-t)\by )
   = t f(\bx) + (1-t)f(\by)
   = t \bu + (1-t)\bv.
   $$
1. Since $\bz \in S$, 
   hence $f(\bz) = t \bu + (1-t)\bv \in f(S)$.
1. We have shown that for any $\bu, \bv \in f(S)$
   and any $0 \leq t \leq 1$, 
   $t \bu + (1-t)\bv \in f(S)$.
1. Thus, $f(S)$ is convex.
```

It applies in the reverse direction also.
````{prf:theorem} Inverse image under affine function
:label: res-cvx-convex-set-inverse-affine-image

Let $f : \VV \to \EE$ be affine and 
$S \subseteq \EE$ be convex.
Then the inverse image of $S$ under $f$ given by

$$
f^{-1}(S) = \{ \bx \in \VV \ST f(\bx) \in S\}
$$
is convex.
````

```{prf:proof}
Denote $R = f^{-1}(S)$. We need to show that
if $S$ is convex then $R$ is convex too.

We proceed as follows:

1. Let $\bx, \by \in R$. 
1. Let $\bu = f(\bx)$ and $\bv = f(\by)$.
1. $\bu, \bv \in S$.
1. Let $0 \leq t \leq 1$.
1. Then, $\bw = t \bu + (1-t)\bv \in S$ since $S$
   is convex.
1. Let $\bz = t \bx + (1-t) \by$. 
1. Since $f$ is affine, hence
   
   $$
   \bw = t \bu + (1-t)\bv
   = t f(\bx) + (1-t) f(\by)
   = f(t \bx + (1-t) \by)
   = f(\bz).
   $$
1. Since $\bw \in S$, hence $\bz \in R$
   as $\bw = f(\bz)$.
1. We have shown that for any $\bx, \by \in R$
   and any $0 \leq t \leq 1$, 
   $t \bx + (1-t)\by \in R$.
1. Thus, $R$ is convex.
```

````{prf:example} Affine functions preserving convexity

Let $S \in \RR^n$ be convex.

* For some $\alpha \in \RR$,
  $\alpha S$ is convex. This is the *scaling* operation.
* For some $\ba \in \RR^n$, $S + \ba$
  is convex. This is the *translation* operation.
* Let $n = m + k$. 
  Then, let $\RR^n = \RR^m \times \RR^k$.
  A vector $\bx \in S$ can be written as $\bx = (\bx_1, \bx_2)$
  where $\bx_1 \in \RR^m$ and $\bx_2 \in \RR^k$.
  Then

  $$
    T = \{ \bx_1 \in \RR^m \ST 
        (\bx_1, \bx_2) \in S \text{ for some } \bx_2 \in \RR^k\}
  $$
  is convex. This is the *projection* operation.
  It projects vectors from $\RR^n$ to $\RR^m$ by
  dropping last $k$ entries.
````
```{prf:example} System of linear equations
Consider the system of linear equations $\bA \bx = \by$
where $A \in \RR^{m \times n}$.

If $\by$ ranges over a convex set, then the corresponding
set of solutions also ranges over a convex set
due to {prf:ref}`res-cvx-convex-set-inverse-affine-image`.

The {prf:ref}`nonnegative orthant <def-convex-nonnegative-orthant>`
$\RR^n_+$ is a convex set.

Let $Y = \RR^m_+ + \ba$ for some $\ba \in \RR^m$; i.e.,

$$
Y = \{ \by \ST \by \succeq \ba \}.
$$

Then, $\bA^{-1} Y$ is the set of vectors satisfying the inequality

$$
\bA \bx \succeq \ba.
$$

Thus, the solution set of a system of linear inequalities
of the form $\bA \bx \succeq \ba$ is convex.

Now, if $X = \RR^n_+$, then $\bA X$ is the set of vectors
$\by \in \RR^m$ such that the equation $\bA \bx = \by$ 
has a nonnegative solution ($\bx \succeq \bzero$).
Since $X$ is convex,  so is $\bA X$.
```

```{prf:theorem} Orthogonal projection of convex set
:label: res-cvx-convex-set-orthogonal-projection

The {prf:ref}`orthogonal projection <def-la-orthogonal-projector>`
of a convex set $C$ on a 
subspace $V$ is another convex set.
```

```{prf:proof}
We recall that orthogonal projection is a 
{prf:ref}`linear mapping <res-la-ip-subspace-orth-proj>`
and thus an affine function. 
By {prf:ref}`res-cvx-convex-set-affine-image`, image
of a convex set under an affine function is convex.
Hence proved.
```


### Set Addition

````{prf:theorem} Convexity and set addition
:label: res-cvx-convexity-set-addition

Let $C_1$ and $C_2$ be two convex subsets of $\VV$. Then
$C_1 + C_2$ is convex.
````

```{prf:proof}
We proceed as follows:

1. Let $\bx, \by \in C_1 + C_2$. 
1. Then, $\bx = \bx_1 + \bx_2$ for some $\bx_1 \in C_1$ 
   and some $\bx_2 \in C_2$.
1. Similarly, $\by = \by_1 + \by_2$ for some $\by_1 \in C_1$ 
   and some $\by_2 \in C_2$.
1. Let $0 \leq t \leq 1$.
1. Then:
   
   $$
   t \bx + (1 - t) \by 
   = t (\bx_1 + \bx_2) + (1-t)(\by_1 + \by_2)
   = t \bx_1 + (1 - t) \by_1 + t \bx_2 + (1 - t) \by_2. 
   $$
1. But, $\bz_1 = t \bx_1 + (1 - t) \by_1 \in C_1$ since
   $C_1$ is convex.
1. Similarly, $\bz_2 = t \bx_2 + (1 - t) \by_2 \in C_2$ since
   $C_2$ is convex.
1. Hence, $t \bx + (1 - t) \by = \bz_1 + \bz_2 \in C_1 + C_2$.
1. Thus, $C_1 + C_2$ is convex.
```
One way to think geometrically about set addition is as the
union of all translates of $C_1$ given by $C_1 + \bx$
as $\bx$ varies over $C_2$.

```{prf:theorem}
:label: res-cvx-convex-set-as-set-cvx-comb

A set $C$ is convex if and only if 

$$
(1-t) C + t C = C \Forall t \in [0,1].
$$
```
```{prf:proof}

Assume $C$ is convex:

1. $(1-t) C + t C = \{ t \bx + (1-t) \by \ST \bx, \by \in C \}$.
1. Thus, $(1-t) C + t C \subseteq C$.
1. For every $\bx \in C$, $(1-t)\bx \in (1-t)C$
   and $t \bx \in t C$.
1. Thus, $(1-t)\bx + t \bx = \bx \in (1-t) C + t C$.
1. Thus, $C \subseteq (1-t) C + t C$.
1. Combining, we get $(1-t) C + t C = C$.

Assume $(1-t) C + t C = C$ for every $t \in [0,1]$.

1. Let $\bx, \by \in C$ and $t\in [0,1]$.
1. Then, $(1-t)\bx \in (1-t)C$
   and $t \by \in t C$. 
1. Hence, $(1-t)\bx + t \by \in (1-t) C + t C = C$.
1. Thus, $C$ is convex.
```


```{prf:theorem} Convexity and linear combination
:label: res-cvx-convexity-linear-combination

Convexity is preserved under linear combinations. 

Let $C_1, \dots, C_k$ be convex. 
Let $t_1, \dots, t_k \in \RR$.
Then, their linear combination:

$$
C = t_1 C_1 + \dots  + t_k C_k
$$
is convex.
```

```{prf:proof} 
Due to {prf:ref}`res-cvx-convexity-scalar-multiplication`,
$t_i C_i$ are convex for $i=1,\dots,k$.

By (finite) repeated application of {prf:ref}`res-cvx-convexity-set-addition`,
their sum is also convex.
```


```{prf:theorem} Nonnegative scalar multiplication distributive law
:label: res-cvx-convex-set-conic-dist

Let $C$ be convex and $t_1, t_2 \geq 0$. Then

$$
(t_1 + t_2)C = t_1 C + t_2 C.
$$
```
```{prf:proof}
From {prf:ref}`res-vs-set-arithmetic-props`, we know that:

$$
(t_1 + t_2)C \subseteq t_1 C + t_2 C.
$$

We now show that $t_1 C + t_2 C \subseteq (t_1 + t_2)C$.

1. If both $t_1 = t_2 = 0$, then we have trivial equality.
1. If either of $t_1$ or $t_2$ is 0, then also we have trivial equality.
1. Now, consider the case $t_1, t_2 > 0$.
1. Define $t = t_1 + t_2 > 0$ and $r = \frac{t_1}{t}$.
1. Then, $1-r = \frac{t_2}{t}$.
1. Then, since $C$ is convex, hence $r C + (1-r) C \subseteq C$.
1. Multiplying by $t$ on both sides, we get: 
   $t_1 C + t_2C \subseteq (t_1 + t_2) C$. 
```

For the special case of $t_1 = r$ and $t_2 = 1 - r$ with $r \in [0,1]$, we get:

$$
C = r C + (1- r)C.
$$

Some implications are $C + C = 2C$, $C+C+C=3C$ and so forth
if $C$ is convex.


```{prf:theorem} Convex combinations over arbitrary unions
:label: res-cvx-arb-cvx-un-cvx-comb

Let $I$ be an index set and 
$\FFF = \{C_i \}_{i \in I}$ be a family of convex
sets in $\VV$. Let $C$ be given as:

$$
C = \ConvexHull\left (\bigcup_{i \in I} C_i \right);
$$
i.e., $C$ is the convex hull of the union of the 
family of sets $\FFF$. 
Then,

$$
C = \bigcup \left \{\sum_{i \in I} t_i C_i \right \} 
$$
where the union is taken over all finite convex combinations 
(i.e. over all nonnegative choices of $t_i$ such that only
finitely many $t_i$ are nonzero and they add up to 1).
```

```{prf:proof}

We proceed as follows:

1. Let $\bx \in C$.
1. Then, $\bx$ is a convex combination of elements in $\bigcup_{i \in I} C_i$.
1. Thus, $\bx = \sum_{i=1}^m a_i \by_i$ where
   $\by_i \in \bigcup_{i \in I} C_i$, $a_i \geq 0$ and $\sum a_i = 1$.
1. Drop all the terms from $\bx$ where $a_i = 0$.
1. If $\by_i, \by_j$ belong to some same $C_k$, then, we can replace
   $a_i \by_i + a_j \by_j$ with some $a \by  = a_i \by_i + a_j \by_j$ 
   where $a = a_i + a_j$. 
   Note that, with these assumptions,
   $\by = \frac{a_i}{a_i + a_j} \by_i + \frac{a_j}{a_i + a_j} \by_j$
   is a convex combination of $\by_i$ and $\by_j$, hence $\by \in C_k$
   since $C_k$ is convex.
1. Thus, terms from a single $C_k$ in $\bx$ can be reduced by a single term.
1. Thus, we can simplify $\bx$ such that
   
   $$
   \bx = \sum_{j=1}^p b_j \bx_j
   $$
   such that each $\bx_j$ belongs to a different $C_{i_j}$ with $i_j \in I$, 
   $b_j > 0$ and $\sum b_j = 1$.
1. Thus, $C$ is a union of finite convex combinations of the form

   $$
   b_1 C_{i_1} + \dots + b_p C_{i_p}
   $$
   where $i_1, \dots, i_p \in I$ are different indices
   and $b_j > 0$, $\sum b_j = 1$.
1. This is the same set as $\bigcup \left \{\sum_{i \in I} t_i C_i \right \}$
   except for notational differences.
```

```{prf:corollary} Convex hull of union
:label: res-cvx-hull-union-cvx-combs

Let $C_1$ and $C_2$ be convex sets.
Let $C$ be the convex hull of their union:

$$
C = \ConvexHull (C_1 \cup C_2).
$$
Then,

$$
C = \bigcup_{t \in [0,1]} \left [ (1 - t) C_1 + t C_2 \right ].
$$
```

### Partial Addition

Recall the notion of 
{prf:ref}`direct sum <def-vs-direct-sum-vector-spaces>`
of two vector spaces $\VV$ and $\WW$ over $\RR$
given by $\VV \oplus \WW$.

```{prf:theorem} Partial addition on convex sets
:label: res-cvx-convex-set-partial-addition

Let $\VV$ and $\WW$ be real vector spaces.
Let $\VV \oplus \WW$ be their direct sum.
Let $C_1$ and $C_2$ be convex sets in $\VV \oplus \WW$.
Let $C$ be the set of vectors $\bx = (\by, \bz)$ 
such that there exist vectors $\bz_1, \bz_2 \in \WW$ 
with $(\by, \bz_1) \in C_1$, $(\by, \bz_2) \in C_2$
and $\bz_1 + \bz_2 = \bz$.
Then, $C$ is a convex set in $\VV \times \WW$.
```

```{prf:proof}
Let $(\by, \bz) \in C$ such that there exist vectors $\bz_1, \bz_2 \in \WW$ 
with $(\by, \bz_1) \in C_1$, $(\by, \bz_2) \in C_2$ and $\bz_1 + \bz_2 = \bz$.

Let $(\by', \bz') \in C$ such that there exist vectors $\bz'_1, \bz'_2 \in \WW$ 
with $(\by', \bz'_1) \in C_1$, $(\by', \bz'_2) \in C_2$ and $\bz'_1 + \bz'_2 = \bz'$.

Let $t \in [0,1]$. Consider the vector 
$(\by'', \bz'') = t(\by, \bz) + (1-t)(\by', \bz')$. 

1. $\by'' = t \by + (1-t) \by'$.
1. $\bz'' = t \bz + (1-t) \bz' = t(\bz_1 + \bz_2) + (1-t)(\bz'_1 + \bz'_2)$.
1. Let $\bz_1'' = t \bz_1 + (1-t) \bz_1'$.
1. Let $\bz_2'' = t \bz_2 + (1-t) \bz_2'$.
1. Since $(\by, \bz_1), (\by', \bz'_1) \in C_1$ and $C_1$ is convex,
   hence $(\by'', \bz''_1) \in C_1$.
1. Since $(\by, \bz_2), (\by', \bz'_2) \in C_2$ and $C_2$ is convex,
   hence $(\by'', \bz''_2) \in C_2$.
1. But then, we note that $\bz'' = \bz''_1 + \bz''_2$.
1. Thus, $(\by'', \bz''_1) \in C_1$ and $(\by'', \bz''_2) \in C_2$
   implies that $(\by'', \bz'') \in C$.
1. Thus, $C$ is convex.
```

We can write a version of the theorem above for $\RR^n$.

```{prf:corollary} Partial addition on convex sets in Euclidean space
:label: res-cvx-convex-set-partial-addition-rn

Let $C_1$ and $C_2$ be convex sets in $\RR^{n + m}$.
Let $C$ be the set of vectors $\bx = (\by, \bz)$ 
such that there exist vectors $\bz_1, \bz_2 \in \RR^m$ 
with $(\by, \bz_1) \in C_1$, $(\by, \bz_2) \in C_2$
and $\bz_1 + \bz_2 = \bz$.
Then, $C$ is a convex set in $\RR^{n+m}$.
```


The relationship between $C$ and $C_1,C_2$ is known as
*partial addition*. 

* When $\VV = \{ \bzero\}$ we are left with the result that
  $C_1, C_2$ convex implies $C_1 + C_2$ is convex.
* When $\WW  = \{\bzero\}$, we are left with the result that 
  $C_1, C_2$ convex implies $C_1 \cap C_2$ is convex.
* In between, we have a spectrum of results where
  for a vector in $C$, 
  part of the representation must be common between
  $C_1$ and $C_2$ while the remaining part must be
  the sum of corresponding parts of vectors in $C_1$ 
  and $C_2$.
* In other words, if a vector space can be decomposed
  as a direct sum of two subspaces, then we have
  intersection or representation in one subspace while addition 
  in the other.
* This partial addition (binary) operation is commutative
  as well as associative.


Partial additions appear naturally 
in convex cones in $\VV \oplus \RR$
generated by a convex set in $\VV$.
See {prf:ref}`res-cvx-convex-cross-section-cone`
and discussion thereafter.


### Cartesian Product/Direct Sum

```{prf:theorem} Direct sum of convex sets
:label: res-cvx-convex-set-direct-sum

Let $\VV$ and $\WW$ be real vector spaces.
Let $C \subseteq \VV$ and $D \subseteq \WW$ be convex
subsets of $\VV$ and $\WW$ respectively.
Then, $C \oplus D$ is a convex subset of $\VV \oplus \WW$.

More generally, if $\VV_1, \dots, \VV_k$ are real vector spaces
and $C_i \subseteq \VV_i$ are convex subsets for $i=1,\dots,k$, then
$C = C_1 \oplus \dots \oplus C_k$ is convex in
the direct sum of vector spaces
$\VV_1 \oplus \dots \oplus \VV_k$.
```

```{prf:proof}
If either $C$ or $D$ is empty, then $C \oplus D$ is empty,
hence convex. We shall thus assume that both $C$ and $D$ are
nonempty.

1. Let $\bz_1, \bz_2 \in C \oplus D$ and $t \in (0, 1)$.
1. Then, $\bz_1 = (\bx_1, \by_1)$ and $\bz_2 = (\bx_2, \by_2)$ 
   such that $\bx_1, \bx_2 \in C$ and $\by_1, \by_2 \in D$.
1. Since $C$ and $D$ are convex, hence
   $\bx = t \bx_1 + (1-t) \bx_2 \in C$ 
   and $\by = t \by_1 + (1- t) \by_2 \in D$.
1. Now, 
   
   $$
   \bz &= t \bz_1 + (1 - t) \bz_2\\ 
   &= t(\bx_1, \by_1) + (1-t)(\bx_2, \by_2)\\
   &= (t \bx_1 + (1-t) \bx_2, t \by_1 + (1- t) \by_2)\\
   &= (\bx, \by).
   $$
1. Since $\bx \in C$ and $\by \in D$, 
   hence $\bz = (\bx, \by)\in C \oplus D$.
1. Thus, $C \oplus D$ is closed under convex combination.
1. Thus, $C \oplus D$ is convex.

The generalization for multiple real vector spaces is
easily verifiable through induction.
```


```{prf:theorem} Projection of a direct sum
:label: res-cvx-convex-set-direct-sum-projection

Let $\VV$ and $\WW$ be real vector spaces.
Let $C \subseteq \VV$ and $D \subseteq \WW$.
Assume that $C \oplus D$ is a convex subset of $\VV \oplus \WW$.
Then, $C$ and $D$ are convex subsets of $\VV$ and $\WW$ respectively.

More generally, if $\VV_1, \dots, \VV_k$ are real vector spaces
and $C_i \subseteq \VV_i$ are subsets for $i=1,\dots,k$, such that
$C = C_1 \oplus \dots \oplus C_k$ is convex in
the direct sum of vector spaces
$\VV_1 \oplus \dots \oplus \VV_k$;
then $C_i$ are convex subsets of $\VV_i$ for $i=1,\dots,k$.
```

```{prf:proof}
Consider the case of two vector spaces $\VV$ and $\WW$.

1. Let $\bx_1, \bx_2 \in C$ and $t \in (0,1)$.
1. Pick any $\by \in D$.
1. Then, $(\bx_1, \by), (\bx_2, \by) \in C \oplus D$.
1. Since $C \oplus D$ is convex, hence 
   
   $$
   t (\bx_1, \by) + (1-t) (\bx_2, \by)
   = (t \bx_1 + (1-t) \bx_2, \by) \in C \oplus D.
   $$
1. Thus, $t \bx_1 + (1-t) \bx_2 \in C$.
1. Thus, $C$ is convex.
1. Similarly $D$ is also convex.

The argument can be extended by mathematical induction for
multiple vector spaces.
```

## Extreme Points

```{prf:definition} Extreme points of convex sets
:label: def-cvx-extreme-point

Let $VV$ be a real vector space and let $C$ 
be a subset of $\VV$.

A point $\bx \in S$ is called an *extreme point* 
of $S$ if there do not exist $\bx_1, \bx_2 \in S$
with $\bx_1 \neq \bx_2$ and $t \in (0, 1)$ such that

$$
\bx = t \bx_1 + (1-t) \bx_2.
$$
In other words, $\bx$ cannot be expressed as a nontrivial convex
combination of two different points in $S$.

The set of extreme points of a set $S$ is denoted by
$\extreme S$.
```



```{prf:example} Extreme points
:label: ex-cvx-extreme-point

1. Let $C = [0,1] \subseteq \RR$.
   Then, $0$ and $1$ are extreme points of $C$.
1. Let $C = (0, 1) \subseteq \RR$.
   $C$ doesn't have any extreme point.
1. In a triangle, the three vertices are extreme points.
1. In a convex polytope, all the vertices are extreme points.
```

A more intricate example of the set
of extreme points for the set
$P = \{ \bx \in \RR^n \ST \bA \bx = \bb, \bx \succeq \bzero \}$
is discussed in {prf:ref}`res-cvx-cone-bfs-extreme`.
