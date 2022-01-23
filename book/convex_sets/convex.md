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

````{prf:example} Convex sets
:label: def-ray

*  A line segment is convex.
*  A circle [including its interior] is convex.
*  A *ray* is defined as $\{ \bx_0 + \theta \bv | \theta \geq 0 \}$ 
   where $\bv \neq \bzero$ indicates the direction of ray 
   and $\bx_0$ is the base or origin of ray. 
   A ray is convex but not affine.
*  Any affine set is convex.

````


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

````{prf:remark}
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

````{prf:remark}
The convex hull $\ConvexHull(S)$ of a set $S$ is always convex.
````



````{prf:remark}
The convex hull of a set $S$ is the smallest convex set containing it. In other words,
let $C$ be any convex set such that $S \subseteq C$. Then $\ConvexHull(S) \subseteq C$.
````

## Infinite Convex Combinations

We can generalize convex combinations to include infinite sums.
````{prf:lemma}
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
````{prf:lemma}
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
