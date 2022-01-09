# Cones

````{prf:definition} Cone
:label: def-cone

A set $C$ is called a *cone* or *nonnegative homogeneous*, if for every $x \in C$
and $\theta \geq 0$, we have $\theta x \in C$.

````

By definition we have $0 \in C$.


## Convex cones

````{prf:definition} Convex cone
:label: def-convex-cone

A set $C$ is called a *convex cone* if it is convex and a cone.
In other words, for every $x_1, x_2 \in C$ and $\theta_1, \theta_2 \geq 0$,
we have

$$
    \theta_1 x_1 + \theta_2 x_2 \in C
$$
````


````{prf:definition} Conic combination
:label: def-conic-combination

A point of the form $\theta_1 x_1 + \dots + \theta_k x_k $ with
$\theta_1 , \dots, \theta_k \geq 0$ is called a *conic combination*
(or a *non-negative linear combination*) of $x_1,\dots, x_k$.

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

````{prf:example} Convex cones

*  A ray with its base at origin is a convex cone.
*  A line passing through zero is a convex cone.
*  A plane passing through zero is a convex cone.
*  Any subspace is a convex cone.

````

```{prf:example} A subspace is a convex cone

Let $V \subseteq \RR^n$ be a subspace. We show that it is also 
a convex cone.

Let $v_1, v_2 \in V$ and $\theta_1, \theta_2 \geq 0$, then

$$
v = \theta_1 v_1 + \theta_2 v_2
$$

is a linear combination of $v_1$ and $v_2$. Hence $v \in V$. 
Thus, $V$ is a convex cone.
```

## Pointed cones

```{prf:definition} Pointed cone
:label: def-pointed-cone

A cone $C \subset \RR^n$ is called pointed if $x \in C$ and $-x \in C$ implies $x = 0$. 
```
In other words, a pointed cone, doesn't contain a line.

```{prf:definition} Nonnegative orthant
:label: def-nonnegative-orthant

The nonnegative orthant is defined as:

$$
\RR^n_+ \triangleq \{ x \in \RR^n \ST x_i \geq 0, \Forall 1 \leq i \leq n \}.
$$
In other words, for $x \in \RR^n_+$, every component is non-negative.
```

```{prf:example} The nonnegative orthant is a pointed convex cone.

Let $x, y \in \RR^n_+$. Let $\alpha, \beta \geq 0$ and consider their 
conic combination

$$
z = \alpha x + \beta y.
$$

It is obvious that all components of $z$ are also nonnegative. Hence
$z \in \RR^n_+$. Thus, $\RR^n_+$ is closed under conic combinations.
Hence, $\RR^n_+$ is a convex cone.

Finally, $\RR^n_+$ is pointed as for any $x \in \RR^n_+$, $-x \in \RR^n_+$
only if $x = 0$.
```

## Conic hulls

````{prf:definition} Conic hull
:label: def-conic-hull

The *conic hull* of a set $S$ is the set of all conic combinations
of points in $S$. i.e.

$$
    \{\theta_1 x_1 + \dots \theta_k x_k | x_i \in S, \theta_i \geq 0, i = 1, \dots, k \}
$$

````

````{prf:remark}
Conic hull of a set is the smallest convex cone that contains the set.
````


## Proper cones

````{prf:definition} Proper cone
:label: def-proper-cone

A cone $K \in \RR^N$ is called a *proper cone* if it satisfies the following:

*  $K$ is *convex*.
*  $K$ is *closed*.
*  $k$ is *solid* i.e. it has a nonempty interior.
*  $K$ is *pointed*.
````

```{prf:example} Non-empty interior

Consider the following sets in $\RR^2$:

$$
C_1 = \{ (x_1, x_2) \ST x_1 \geq 0, x_2 = 0\}
$$

$$
C_2 = \{ (x_1, x_2) \ST x_1, x_2 \geq 0\}
$$

Both are closed convex cones. 
$C_1$ doesn't have an interior. All points in $C_1$ are on the 
boundary of $C_1$. 

$C_2$ has a non-empty interior. e.g., the point 
$(1,1) \in C_2$ is not on the boundary.
```