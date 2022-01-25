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

````{prf:theorem}
:label: res-cvx-convex-set-convex-combinations

A set is convex if and only if it contains all convex combinations of its points.
````


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



````{prf:remark}
The convex hull of a set $S$ is the smallest convex set containing it. In other words,
let $C$ be any convex set such that $S \subseteq C$. Then $\ConvexHull(S) \subseteq C$.
````

## Relative Interior

```{prf:theorem} Line segment property of relative interior
:label: res-cvx-convex-relint-convex

Let $C$ be a nonempty convex set. Let $\bx \in \relint C$
and $\by \in \closure C$. Then, 

$$
t \bx + (1-t) \by \in \relint C \Forall t \in (0,1].
$$
```

```{prf:proof}
Let $C$ be a convex set. Fix some $t \in [0,1]$. 
We need to show that $\bz = t \bx + (1-t)\by \in \relint C$.
Recall that $\affine C$ denotes the affine hull of $C$.

1. Since $\by \in \closure C$, hence for all $\epsilon > 0$, 
   we have 

```

## Infinite Convex Combinations

We can generalize convex combinations to include infinite sums.
````{prf:theorem}
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

### Intersection

````{prf:theorem}
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

````{prf:theorem}
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

### Affine Functions

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



````{prf:theorem}
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
````{prf:theorem}
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

### Set Addition

````{prf:theorem}
Let $S_1$ and $S_2$ be two convex subsets of $\VV$. Then
$S_1 + S_2$ is convex.
````

```{prf:proof}
We proceed as follows:

1. Let $\bx, \by \in S_1 + S_2$. 
1. Then, $\bx = \bx_1 + \bx_2$ for some $\bx_1 \in S_1$ 
   and some $\bx_2 \in S_2$.
1. Similarly, $\by = \by_1 + \by_2$ for some $\by_1 \in S_1$ 
   and some $\by_2 \in S_2$.
1. Let $0 \leq t \leq 1$.
1. Then:
   
   $$
   t \bx + (1 - t) \by 
   = t (\bx_1 + \bx_2) + (1-t)(\by_1 + \by_2)
   = t \bx_1 + (1 - t) \by_1 + t \bx_2 + (1 - t) \by_2. 
   $$
1. But, $\bz_1 = t \bx_1 + (1 - t) \by_1 \in S_1$ since
   $S_1$ is convex.
1. Similarly, $\bz_2 = t \bx_2 + (1 - t) \by_2 \in S_2$ since
   $S_2$ is convex.
1. Hence, $t \bx + (1 - t) \by = \bz_1 + \bz_2 \in S_1 + S_2$.
1. Thus, $S_1 + S_2$ is convex.
```
