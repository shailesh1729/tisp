# Convex Sets

````{prf:definition}
:label: def-convex-set

A set $C$ is *convex* if the line segment between any two points in $C$ lies in $C$. i.e.

$$
    \theta x_1 + (1 - \theta) x_2 \in C \Forall x_1, x_2 \in C \text{ and } 0 \leq \theta \leq 1.
$$

````



````{prf:definition}
:label: def-convex-combination

We call a point of the form $\theta_1 x_1  + \dots + \theta_k x_k$, where
$\theta_1 + \dots + \theta_k  = 1$ and $\theta_i \geq 0, i=1,\dots,k$,
a *convex combination* of the points $x_1, \dots, x_k$.
````
It is like a weighted average of the points $x_i$.

````{prf:remark}
A set is convex if and only if it contains all convex combinations of its points.
````

````{prf:example} Convex sets
:label: def-ray

*  A line segment is convex.
*  A circle [including its interior] is convex.
*  A *ray* is defined as $\{ x_0 + \theta v | \theta \geq 0 \}$ where
$v \neq 0$ indicates the direction of ray and $x_0$ is the base or origin of ray. A ray
is convex but not affine.
*  Any affine set is convex.

````



````{prf:definition}
:label: def-convex-hull

The *convex hull* of an arbitrary set $S \subseteq \VV$ denoted as
$\ConvexHull(S)$, is the set of all convex combinations of points in $S$.

$$
    \ConvexHull(S) = \{ \theta_1 x_1 + \dots + \theta_k x_k | x_k \in S, \theta_i \geq 0, i = 1,\dots, k,
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

We can generalize convex combinations to include infinite sums.
````{prf:lemma}
Let $\theta_1, \theta_2, \dots$ satisfy

$$
    \theta_i \geq 0, i = 1,2,\dots, \quad \sum_{i=1}^{\infty} \theta_i = 1,
$$

and let $x_1, x_2, \dots \in C$, where $C \subseteq \VV$ is convex. Then

$$
    \sum_{i=1}^{\infty} \theta_i x_i \in C,
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
