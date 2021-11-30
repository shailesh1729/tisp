# Cones

(def:cone)=
````{prf:definition}
A set $C$ is called a **cone** or **nonnegative homogeneous**, if for every $x \in C$
and $\theta \geq 0$, we have $\theta x \in C$.

````

By definition we have $0 \in C$.

(def:convex_cone)=
````{prf:definition}
A set $C$ is called a **convex cone** if it is convex and a cone.
In other words, for every $x_1, x_2 \in C$ and $\theta_1, \theta_2 \geq 0$,
we have

$$
    \theta_1 x_1 + \theta_2 x_2 \in C
$$

````



(def:conic_combination)=
````{prf:definition}
A point of the form $\theta_1 x_1 + \dots + \theta_k x_k $ with
$\theta_1 , \dots, \theta_k \geq 0$ is called a **conic combination**
(or a **non-negative linear combination**) of $x_1,\dots, x_k$.

````

````{prf:remark}
Let $C$ be a convex cone. Then for every $x_1, \dots, x_k \in C$,
a conic combination $\theta_1 x_1 + \dots + \theta_k x_k $ with
$\theta_i \geq 0$ belongs to $C$.

Conversely if a set $C$ contains all conic combinations of its
points, then it is a convex cone.
````

The idea of conic combinations can be generalized to infinite sums
and integrals.

(def:conic_hull)=
````{prf:definition}
The **conic hull** of a set $S$ is the set of all conic combinations
of points in $S$. i.e.

$$
    \{\theta_1 x_1 + \dots \theta_k x_k | x_i \in S, \theta_i \geq 0, i = 1, \dots, k \}
$$

````

````{prf:remark}
Conic hull of a set is the smallest convex cone that contains the set.
````

````{prf:example} Convex cones

*  A ray with its base at origin is a convex cone.
*  A line passing through zero is a convex cone.
*  A plane passing through zero is a convex cone.
*  Any subspace is a convex cone.

````

We now look at some more important convex sets one by one.
