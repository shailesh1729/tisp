(sec:opt:duality)=
# Duality


## The Geometry of the $\VV \oplus \RR$ Space

```{div}

As we concern ourselves with the optimization of proper functions
of type $f: \VV \to \RERL$, it is pertinent for us to
introduce some terminology to explore the geometry
of the $\VV \oplus \RR$ space. We recall 
that $\epi f \subseteq \VV \oplus \RR$.

1. The $\VV$ part forms the horizontal axes for the
product space $\VV \oplus \RR$.
1. The $\RR$ part forms the vertical axis.
1. We write the vectors in $\VV \oplus \RR$ as $(\bx, t)$
   where $\bx \in \VV$ and $t \in \RR$.
1. A hyperplane in $\VV \oplus \RR$
   is associated with a nonzero normal vector of the form $(\ba, b)$
   where $\ba \in \VV$ and $b \in \RR$.

   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST \langle \bx, \ba \rangle  + t b = c \}.
   $$
   Since the normal vector must be nonzero, hence either $\ba$
   or $b$ or both must be nonzero.
1. If a specific point $(\bx_0, t_0) \in H$, then

   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST \langle \bx, \ba \rangle  + t b = 
   \langle \bx_0, \ba \rangle + t_0 b \}.
   $$
```


```{prf:definition} Vertical, horizontal and nonvertical hyperplanes
:label: def-opt-vert-horz-hyperplane

Let $H$ be a hyperplane of $\VV \oplus \RR$ with a normal vector
$(\ba, b)$.

1. The hyperplane is called *horizontal* if $\ba = \bzero$.
1. The hyperplane is called *vertical* if $b = 0$.
1. The hyperplane is called *nonvertical* if $b \neq 0$.
```

Let us see how these definitions can be interpreted.
```{prf:example} Horizontal hyperplanes
:label: ex-opt-horizontal-hyperplanes-1

Consider the case where $\ba = \bzero$.

1. The hyperplane description reduces to

   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST  t b = c \}.
   $$
1. It simplifies to

   $$
   H = \left \{ (\bx, t) \in \VV \oplus \RR \ST  t = \frac{c}{b} \right \}
   $$
   since $b$ must be nonzero.
1. Along the $\VV$ axes, the points in set $H$ can take any value
   but along the vertical axis, they must take a fixed value given by
   $\frac{c}{b}$.
1. We can see that $H$ is a hyperplane which is parallel to $\VV \times \{ 0 \}$.
1. For the specific case where $c = 0$, $H = \VV \times \{ 0 \}$.
1. Hence they are called horizontal hyperplanes.
1. Note that $H$ intersects with the vertical axis at the point
   $(\bzero, \frac{c}{b})$.
```

```{prf:example} Vertical hyperplanes
:label: ex-opt-vertical-hyperplanes-1

Now consider the case where $b = 0$.

1. The hyperplane description reduces to

   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST  \langle \bx, \ba \rangle = c \}.
   $$
1. The set $H_v = \{ \bx \in \VV \ST  \langle \bx, \ba \rangle = c \}$
   describes a hyperplane of $\VV$.
1. $H$ is constructed by allowing $H_v$ to slide along the vertical axis
   as any value is allowed in the last coordinate (vertical axis). 
1. Hence this is called a vertical hyperplane.
```

```{prf:observation} Intersection of nonvertical hyperplane with vertical axis
:label: res-opt-non-vert-hyperplane-intersection-r-axis

If a hyperplane $H$ with the normal vector $(\ba, b)$ is nonvertical
(i.e., $b \neq 0$), then it intersects with the vertical axis at a unique point.

1. Indeed the vertical axis is identified with the set of points 

   $$
   L = \{ (\bx, t) \in \VV \oplus \RR  \ST \bx = \bzero \}.
   $$
1. The hyperplane is given by

   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST \langle \bx, \ba \rangle + t b = c \}.
   $$
1. Then the point of intersection is given by $(\bzero, t)$ where

   $$
   t = \frac{c}{b}.
   $$
1. In particular, assume that $(\bx, s) \in H$.
1. Then by definition of $H$,

   $$
   c = \langle \bx, \ba \rangle + s b.
   $$
1. Hence

   $$
   t = \frac{1}{b} \langle \bx, \ba \rangle + s.
   $$
```

```{prf:definition} Vertical line
:label: def-opt-vertical-line

A *vertical line* in $\VV \oplus \RR$ is a set of the
form $\{ (\bx, t) \ST t \in \RR \}$ where $\bx \in \VV$
is a fixed vector.
```

1. A vertical hyperplane is a union of vertical lines.
1. A vertical halfspace is also a union of vertical lines.
1. If $f$ is a proper function, then its epigraph doesn't contain a vertical line.

It enables us to wonder if the epigraph of a proper
function is contained entirely in a closed halfspace
corresponding to some nonvertical hyperplane.

```{prf:theorem} Convex sets and nonvertical supporting hyperplanes
:label: res-opt-cvx-set-non-vert-supp-plane

Let $C$ be a nonempty convex subset of $\VV \oplus \RR$
that contains no vertical lines.
Then

1. $C$ is contained in a closed halfspace corresponding
   to a nonvertical hyperplane; i.e., there exists
   a vector $\ba \in \VV$,  a scalar $b \in \RR$,
   and a scalar $c \in \RR$ such that 

   $$
   \langle \bx, \ba \rangle + t b \geq c
   \Forall (\bx, t) \in C.
   $$
1. If a point $(\bar{\bx}, \bar{t})$ doesn't belong to $\closure C$, there exists
   a nonvertical hyperplane strongly separating $(\bar{\bx}, \bar{t})$
   and $C$.
```

```{prf:proof}
(1) We prove this claim by contradiction.

1. Assume that every hyperplane such that $C$ is
   contained in one of its closed half-spaces is vertical.
1. Then every hyperplane such that $\closure C$ is
   contained in one of its closed half spaces is vertical.
1. By {prf:ref}`res-cvx-closed-convex-halfspace-intersection`,
   $\closure C$ is the intersection of all closed half-spaces
   that contain it.
1. Hence, we have

   $$
   \closure C = \bigcap_{i \in I}\{ (\bx, t) \ST \langle \bx, \ba_i \rangle
    \geq c_i  \}
   $$
   where $I$ is an index set for the family of the hyperplanes
   that contain $\closure C$ in its closed half spaces above.
   Since the hyperplanes are vertical, hence $b_i = 0$ for ever $i \in I$.
1. Let $(\tilde{\bx}, \tilde{t}) \in \closure C$.
1. Then the vertical line $\{ (\tilde{\bx}, t)  \ST t \in \RR \}$
   also belongs to $\closure C$ as it satisfies the expression
   above.
1. Hence, the vector $(\bzero, 1)$ is a direction of recession
   for $\closure C$. In fact it belongs to its lineality space.
   In other words, $(\bzero, -1)$ is also a direction of recession
   for $\closure C$.
1. By {prf:ref}`res-cvx-convex-closure-relint`,
   
   $$
   \relint \closure C = \relint C
   $$
   since $C$ is a convex set.
1. By {prf:ref}`res-cvx-recession-cone-relint`, the recession
   cones of $\closure C$ and $\relint C$ are equal.
1. Hence $(\bzero, 1)$ and $(\bzero, -1)$ are also directions
   of recession for $\relint C$.
1. Hence for every  $(\tilde{\bx}, \tilde{t}) \in \relint C$,
   the vertical line $\{ (\tilde{\bx}, t)  \ST t \in \RR \}$
   also belongs to $\relint C$ and hence to $C$.
1. This contradicts the hypothesis that $C$ doesn't contain
   a vertical line.


(2) This follows from strict separation theorem.

1. Since $(\bar{\bx}, \bar{t}) \notin \closure C$,
   hence, due to {prf:ref}`res-cvxf-cl-convex-set-strict-separation`,
   there exists a hyperplane strongly separating $\closure C$
   and $(\bar{\bx}, \bar{t})$.
1. If this hyperplane is nonvertical, then there is nothing
   more to do.
1. We now consider the case where this strongly separating
   hyperplane is vertical.
1. Let this separating hyperplane be given by
   
   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST  \langle \bx, \bar{\ba} \rangle = \bar{c} \}
   $$
   such that

   $$
   \langle \bx, \bar{\ba} \rangle > \bar{c} > \langle \bar{\bx}, \bar{\ba} \rangle
   \Forall (\bx, t) \in \closure C.
   $$
1. Our goal is to combine this vertical hyperplane with a suitably constructed
   nonvertical hyperplane so that the combined nonvertical hyperplane
   also strongly separates $C$ and $(\bar{\bx}, \bar{t})$.
1. By part (1), there exists a nonvertical hyperplane such that $C$
   is totally contained in one of its closed half spaces.
1. Hence there exists $(\hat{\ba}, \hat{b}) \in \VV \oplus \RR$
   with $\hat{b} \neq 0$ and $\hat{c} \in \RR$ such that

   $$
   \langle \bx, \hat{\ba} \rangle + t \hat{b} \geq \hat{c}
   \Forall (\bx, t) \in \closure C.
   $$
1. Multiply this inequality with some $\epsilon > 0$ and add with the
   previous inequality to get

   $$
   \langle \bx, \bar{\ba} + \epsilon \hat{\ba} \rangle + \epsilon t \hat{b} > 
   \bar{c} + \epsilon \hat{c}
   \Forall (\bx, t) \in \closure C, \Forall \epsilon > 0.
   $$
1. Since $\bar{c} > \langle \bar{\bx}, \bar{\ba} \rangle$, it is possible
   to select a small enough $\epsilon > 0$ such that

   $$
   \bar{c} + \epsilon \hat{c} > 
   \langle \bar{\bx}, \bar{\ba} + \epsilon \hat{\ba} \rangle
   + \epsilon \bar{t} \hat{b}.
   $$
1. Thus, for the small enough $\epsilon > 0$, we have

   $$
   \langle \bx, \bar{\ba} + \epsilon \hat{\ba} \rangle + \epsilon t \hat{b} > 
   \bar{c} + \epsilon \hat{c} > 
   \langle \bar{\bx}, \bar{\ba} + \epsilon \hat{\ba} \rangle
   + \epsilon \bar{t} \hat{b}
   \Forall (\bx, t) \in \closure C.
   $$
1. Letting $\tilde{\ba} = \bar{\ba} + \epsilon \hat{\ba}$,
   $\tilde{b} = \epsilon \hat{b}$ and
   $\tilde{c} = \bar{c} + \epsilon \hat{c}$, we have

   $$
   \langle \bx, \tilde{\ba} \rangle + t \tilde{b} > 
   \tilde{c} > 
   \langle \bar{\bx}, \tilde{\ba} \rangle
   + \bar{t} \tilde{b}
   \Forall (\bx, t) \in \closure C.
   $$
1. This describes the strongly separating nonvertical hyperplane between
   $\closure C$ and $(\bar{\bx}, \bar{t})$.
```



```{prf:definition} Upper closed halfspace
:label: def-opt-upper-closed-halfspace

Let $H$ be a nonvertical hyperplane.
The closed halfspace of $H$ whose recession cone
includes the vertical halfline $\{(\bzero, t) \ST t \geq 0 \}$
is known as its *upper* closed halfspace.
```

If you are in the upper closed halfspace and keep going up,
you will stay in the upper closed halfspace. If you go down,
you will hit the hyperplane.

```{prf:definition} Lower closed halfspace
:label: def-opt-lower-closed-halfspace

Let $H$ be a nonvertical hyperplane.
The closed halfspace of $H$ whose recession cone
includes the vertical halfline $\{(\bzero, t) \ST t \leq 0 \}$
is known as its *lower* closed halfspace.
```

If you are in the lower closed halfspace and keep going down,
you will stay in the lower closed halfspace. If you go up,
you will hit the hyperplane.


## Min Common/Max Crossing Duality

```{div}
We introduce two simple optimization problems.

1. Consider a set $M$ in $\VV \oplus \RR$.
1. Assume that $M$ intersects with the vertical axis;
   i.e., $R = \{ (\bzero, t) \ST t \in \RR \}$.
1. The *min common point* problem attempts to find
   the point $\bx \in M \cap R$ whose component
   along vertical axis is the minimum.
1. Now consider the set of nonvertical hyperplanes
   such that $M$ lies in their upper closed
   halfspaces.
1. Each such hyperplane intersects with the vertical axis.
1. Such points are called the crossing points between
   the nonvertical hyperplane and the vertical axis.
1. Consider the set of all such crossing points.
1. The *max crossing point* problem attempts to
   find the point whose vertical component is
   the largest (highest).
1. Let $\bp^*$ be the minimum common point.
1. Let $\bq^*$ be the maximum crossing point.
1. Let $p^*$ and $q^*$ denote the component
   along the vertical axis for $\bp^*$ and
   $\bq^*$ respectively.
1. In general, $p^*$ lies above $q^*$. 
   We shall show this later formally.
1. We call $p^*$ as minimum common level
   and $q^*$ as maximum crossing level.
1. Then $p^* \geq q^*$. This is known as
   *weak duality*.
1. The gap $p^* - q^*$ which is a nonnegative
   quantity is known as the *duality gap*.
1. Under certain conditions $p^* = q^*$.
   In other words, if the set $M$ meets specific
   conditions, then the optimal value for the
   min common point problem (the primal problem)
   as well as the max crossing point problem
   (the dual problem) are identical.
1. When $p^* = q^*$, then the duality gap
   is $0$. This is known as *strong duality*.
1. When strong duality holds, then the min common point
   problem and the max crossing point problem are
   equivalent in the sense that they have the same solution.
```

We are now ready to define these problems formally.

### Min Common Problem

```{prf:definition} Min common problem
:label: def-opt-min-common-problem

Given a set $M \subseteq \VV \oplus \RR$, the
*min common problem* is defined as

$$
& \text{minimize }  &  & p \\
& \text{subject to } & & (\bzero, p) \in M
$$

Its optimal value is denoted by $p^*$; i.e.,

$$
p^* = \inf_{(\bzero, p) \in M} p.
$$
```

### Max Crossing Problem

Recall that a nonvertical hyperplane
has a normal $(\ba, b)$ such that $b \neq 0$.
Then $(\frac{\ba}{b}, 1)$ is also a normal vector
for this hyperplane.
Hence one way to describe the set of
nonvertical hyperplanes is the set of hyperplanes
with normal vectors of the form $(\ba, 1)$.
Following {prf:ref}`res-opt-non-vert-hyperplane-intersection-r-axis`,
if a nonvertical hyperplane $H$ intersects the vertical axis
at some $(\bzero, q)$, then

$$
q = \langle \bx, \ba \rangle + t
$$
where $(\bx, t) \in H$.
Thus, the hyperplane can be characterized by $\ba$ and $q$ as

$$
H_{\ba, q} = \{ (\bx, t) \ST \langle \bx, \ba \rangle + t = q \}.
$$
The corresponding upper closed half halfspace is given by

$$
H^u_{\ba, q} = \{ (\bx, t) \ST \langle \bx, \ba \rangle + t  \geq q \}
$$
since $t \geq q$ for every point on the vertical axis in $H^u_{\ba, q}$.
The coordinate along the vertical axis for all the points on the vertical axis
in the upper half space must be more than or equal to $q$.

If the set $M$ lies in the upper closed half space of a hyperplane
characterized by $\ba$ and $q$, then

$$
\langle \bx, \ba \rangle + t  \geq q \Forall (\bx, t) \in M. 
$$

Hence, the maximum crossing level $q$ over all hyperplanes
$H_{\ba, q}$ with the same normal $(\ba, 1)$ is given by

$$
q(\ba) = \inf_{(\bx, t) \in M} \{ \langle \bx, \ba \rangle + t \}.
$$

The problem of maximizing the crossing level over all
nonvertical hyperplanes is to maximize over all $\ba \in \VV$,
the maximum crossing level corresponding to $\ba$.

```{prf:definition} Maximum crossing level problem
:label: def-opt-max-cross-level-problem

Given a set $M \subseteq \VV \oplus \RR$, the
*max crossing problem* is defined as

$$
& \text{maximize }  &  & q (\ba) \\
& \text{subject to } & & \ba \in \VV
$$
where $q(\ba) = \inf_{(\bx, t) \in M} \{ \langle \bx, \ba \rangle + t \}$.
Its optimal value is denoted by $q^*$; i.e.,

$$
q^* = \sup_{\ba \in \VV} q(\ba).
$$
```

The function $q$ is the cost function (objective function)
of the max crossing problem. It turns out that
$q$ is concave and upper semicontinuous.

```{prf:theorem} Concavity and upper semicontinuity of $q$
:label: res-opt-max-crossing-cost-concave

The cost function $q$ of the max crossing problem is
concave and upper semicontinuous over $\VV$.
```


```{prf:proof}
Concavity

1. For each $(\bx, t)$, the function $\ba \mapsto \langle \bx, \ba \rangle + t$
   is an affine function.
1. Thus $q$ is an infimum of a family of affine functions over $(\bx, t) \in \VV \oplus \RR$.
1. Hence $q$ is concave.


Upper semicontinuity

1. We note that $-q(\ba) = \sup_{(\bx, t) \in M} \{ - \langle \bx, \ba \rangle - t \}$.
1. Hence $-q$ is a supremum of affine functions.
1. Affine functions are closed ({prf:ref}`res-cvxf-affine-closed`).
1. Pointwise supremum of closed functions is closed
   ({prf:ref}`res-ms-ptws-sup-closed-functions-closed`).
1. Hence $-q$ is a closed function.
1. By {prf:ref}`res-ms-func-lsc-closed-func`, $-q$ is lower semicontinuous
   since it is closed.
1. Hence $q$ is upper semicontinuous.
```




## Fenchel's Duality Theorem

Consider the minimization problem

```{math}
:label: eq-opt-fenchel-primal
\inf_{\bx \in \VV} f(\bx) + g(\bx).
```

The problem can be rewritten as

$$
\inf_{\bx, \bz \in \VV} \{ f(\bx) + g(\bz) \ST \bx = \bz \}.
$$

Construct the Lagrangian for this problem.

$$
L (\bx, \bx; \by ) &= f(\bx) + g(\bz)  + \langle \bz - \bx, \by \rangle\\
&= -[\langle \bx, \by \rangle - f(\bx)]  - [\langle \bz, -\by \rangle - g(\bz)].
$$

The dual objective is constructed by minimizing the Lagrangian with the
primal variables $\bx, \bz$.

$$
q(\by) = \inf_{\bx, \bz} L(\bx, \bz; \by) = - f^*(\by) - g^*(- \by).
$$

We thus obtain the following dual problem, known as the *Fenchel's dual*:

```{math}
:label: eq-opt-fenchel-dual
\sup_{\by \in \VV^*} \{ - f^*(\by) - g^*(- \by) \}.
```

Fenchel's duality theorem provides the conditions under which strong duality
holds for the pair of problems {eq}`eq-opt-fenchel-primal` and {eq}`eq-opt-fenchel-dual`.

```{prf:theorem} Fenchel's duality theorem
:label: res-opt-fenchel-duality-theorem

Let $f,g : \VV \to \RERL$ be proper convex functions.
If $\relint \dom f \cap \relint \dom g \neq \EmptySet$, then 

$$
\underset{\bx \in \VV}{\inf} \{f(\bx) + g(\bx) \}
= \underset{\by \in \VV^*}{\sup} \{ - f^*(\by) - g^*(-\by) \}.
$$
The supremum of R.H.S. (the dual problem) is attained whenever it is finite.
```
