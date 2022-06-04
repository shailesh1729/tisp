(sec:opt:duality)=
# Basic Duality


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

### Different Types of Hyperplanes

```{index} Hyperplane; vertical
```
```{index} Hyperplane; horizontal
```
```{index} Hyperplane; nonvertical
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

### Horizontal Hyperplanes

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

### Vertical Hyperplanes

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

### Nonvertical Hyperplanes

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

### Vertical Lines

```{index} Line; vertical
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

### Nonvertical Supporting Hyperplanes

```{prf:theorem} Convex sets and nonvertical supporting hyperplanes
:label: res-opt-cvx-set-non-vert-supp-plane

Let $C$ be a nonempty convex subset of $\VV \oplus \RR$
that contains no vertical lines.
Then

1. $C$ is contained in a closed halfspace corresponding
   to a nonvertical hyperplane; i.e., there exists
   a vector $\ba \in \VV$,  a nonzero scalar $b \in \RR$,
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



```{index} Halfspace; upper and closed
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

```{index} Halfspace; lower and closed
```
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

```{index} Min common problem
```
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

```{index} Max crossing problem
```
```{prf:definition} Max crossing problem
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
1. Thus $q$ is an infimum of a family of affine functions over $(\bx, t) \in M$.
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


### Weak Duality

```{prf:theorem} Weak duality theorem
:label: res-opt-min-common-weak-duality

For the min common and max crossing problems we have

$$
q^* \leq p^*.
$$
```

```{prf:proof}

Recall that

$$
q(\ba) = \inf_{(\bx, t) \in M} \{ \langle \bx, \ba \rangle + t \}.
$$

Then

$$
\inf_{(\bx, t) \in M} \{ \langle \bx, \ba \rangle + t \}
\leq 
\inf_{(\bzero, t) \in M} \{ \langle \bzero, \ba \rangle + t \}
= \inf_{(\bzero, t) \in M} \{ t \}
= p^*.
$$

Thus we have

$$
q(\ba) \leq p^* \Forall \ba \in \VV.
$$
Taking the supremum over $\ba \in \VV$ on the L.H.S., we obtain

$$
q^* = \sup_{\ba \in \VV} q(\ba) \leq p^*.
$$
```


### Strong Duality

```{div}
We are now interested in conditions under which
there is no duality gap and $p^* = q^*$. 
We shall assume in general that the min common problem
is feasible and $p^* < \infty$.
```

```{prf:remark} Optimal point of min common problem is a closure point
:label: res-opt-min-common-optimal-closure

Assume that the min common problem is feasible and let
$p^* < \infty$. Then the point $(\bzero, p^*)$ is a
closure point of $M$.

1. We have $p^* = \inf_{(\bzero, t) \in M} \{ t \}$.
1. Thus for every $\epsilon > 0$ there exists
   $(\bzero, t) \in M$ such that $t < p^* + \epsilon$.
1. Thus for every $\epsilon > 0$, there exists a point
   $(\bzero, t) \in M$ such that $\| (\bzero, t) - (\bzero, p^*)\| < \epsilon$.
1. Hence $(\bzero, p^*)$ is a closure point of $M$.
```

```{prf:observation} Closed and convex $M$
:label: res-opt-min-max-strong-duality-closed-convex

If $M$ is closed and convex and admits a nonvertical supporting hyperplane
at $(\bzero, p^*)$, then the strong duality holds and
$p^* = q^*$. Also, the optimal values of both the min common problem
and max crossing problem are attained.

1. Since $M$ is closed, hence $(\bzero, p^*) \in M$
   since $(\bzero, p^*)$ is a closure point of $M$.
1. Hence the optimal value of min common problem is attained at
   $(\bzero, p^*)$.
1. Let $H$ be the nonvertical supporting hyperplane at $(\bzero, p^*)$.
1. Then intersection of $H$ with the vertical axis is at $(\bzero, p^*)$.
1. Hence $q^* \geq p^*$.
1. But by weak duality $q^* \leq p^*$.
1. Hence $q^* = p^*$.
1. Clearly the optimal value of max crossing problem is attained at
   $(\bzero, p^*)$ for the hyperplane $H$.
```

This is the most favorable case where strong duality holds
as well as the optimal values of both problems are attained.
We next provide a result that provides a necessary and sufficient
condition for the strong duality however does not address the
issue of attainment of the optimal values.

### First Min Common / Max Crossing Theorem

```{prf:theorem} Min common/max crossing theorem I
:label: res-opt-min-max-strong-duality-1

Consider the min common and max crossing problems.
Assume the following:

1. $p^* < \infty$; i.e., the min common problem is feasible.
1. The set

   $$
   \overline{M} = \{ (\bx, t) \in \VV \oplus \RR \ST \text{ there exists } 
   \bar{t} \in \RR \text{ with } 
   \bar{t} \leq t \text{ and } (\bx, \bar{t}) \in M \}
   $$
   is convex.

Then we have $q^* = p^*$ if and only if for every sequence
$\{ (\bx_k, t_k) \}$ of $M$ with $\bx_k \to \bzero$, there holds

$$
p^* \leq \liminf_{k \to \infty} t_k.
$$
```

The set $\overline{M}$ is an extension of the set $M$ going upwards
along the vertical axis. In other words, all points above
$M$ are included in $\overline{M}$. In other words, the direction
$(\bzero, 1)$ is added to the recession cone.
$\overline{M}$ is unbounded along the $(\bzero, 1)$ direction.


```{prf:proof}
We first consider the trivial case where $p^* = -\infty$.

1. By weak duality ({prf:ref}`res-opt-min-common-weak-duality`),
   $q^* \leq p^*$.
1. Hence $q^* = -\infty$.
1. Hence $q(\ba) = -\infty$ for every $\ba \in \VV$.
1. The conclusion follows trivially.

We now consider the general case where $p^* \in \RR$.
First assume that $p^* \leq \liminf_{k \to \infty} t_k$
holds for every sequence
$\{ (\bx_k, t_k) \}$ of $M$ with $\bx_k \to \bzero$.

1. Since $M \subseteq \overline{M}$ and
   $(\bzero, p^*)$ is a closure point of $M$,
   hence $(\bzero, p^*)$ is also a closure point of $\overline{M}$.
1. We first claim that the set $\overline{M}$ doesn't contain any vertical lines.
   1. For contradiction, assume that $\overline{M}$ contains a vertical line.
   1. The set $\closure \overline{M}$ also contains a vertical line then.
   1. Then $(\bzero, -1)$ is a direction of recession of $\closure \overline{M}$.
   1. Hence $(\bzero, -1)$ is also a direction of recession of $\relint \overline{M}$.
   1. Since $(\bzero, p^*)$ is a closure point of $\overline{M}$, hence
      it is also a closure point of $\relint \overline{M}$.
   1. Hence, there exists a sequence $\{ (\bx_k, t_k) \}$
      of $\relint \overline{M}$ converging to $(\bzero, p^*)$.
   1. Since $(\bzero, -1)$ is a direction of recession of $\relint \overline{M}$,
      hence the sequence $\{ (\bx_k, t_k -1) \}$ belongs to $\relint \overline{M}$.
   1. Hence its limit $(\bzero, p^* - 1) \in \closure \overline{M}$.
   1. By definition of $\overline{M}$, for every $k$, 
      there exists a point $(\bx_k \overline{t_k}) \in M$ 
      such that $\overline{t_k} \leq t_k - 1$.
   1. Hence there exists a sequence $\{ (\bx_k, \overline{t_k} ) \}$ of $M$
      with $\overline{t_k} \leq t_k - 1$ for all $k$ so that
      $\liminf_{k \to \infty} \overline{t_k} \leq p^* - 1$.
   1. This contradicts the assumption that  $p^* \leq \liminf_{k \to \infty} t_k$
      since $\bx_k \to \bzero$.
1. We next show that the vector $(\bzero, p^* - \epsilon)$
   does not belong to $\closure \overline{M}$ for any $\epsilon > 0$.
   1. Assume for contradiction that for some $\epsilon > 0$, 
      the vector $(\bzero, p^* - \epsilon) \in \closure \overline{M}$.
   1. Then there is a sequence $\{ (\bx_k, t_k) \}$ of $\overline{M}$
      converging to $(\bzero, p^* - \epsilon)$.
   1. By definition of $\overline{M}$, for every $k$, there exists
      a point  $(\bx_k \overline{t_k}) \in M$ 
      such that $\overline{t_k} \leq t_k$.
   1. Hence there exists a sequence $\{ (\bx_k, \overline{t_k} ) \}$ of $M$
      with $\overline{t_k} \leq t_k$ for all $k$ so that
      $\liminf_{k \to \infty} \overline{t_k} \leq p^* - \epsilon$.
   1. This contradicts the assumption that  $p^* \leq \liminf_{k \to \infty} t_k$
      since $\bx_k \to \bzero$.
1. Since $\overline{M}$ does not contain any vertical lines and the
   vector $(\bzero, p^* - \epsilon)$ doesn't belong to $\closure \overline{M}$,
   hence, due to {prf:ref}`res-opt-cvx-set-non-vert-supp-plane`,
   there exists a nonvertical hyperplane strongly separating
   $(\bzero, p^* - \epsilon)$ and $\overline{M}$ for every $\epsilon > 0$.
1. This hyperplane crosses the vertical axis at a unique vector
   $(\bzero, \xi)$ which must lie between $(\bzero, p^* - \epsilon)$
   and $(\bzero, p^*)$; i.e., $p^* - \epsilon \leq \xi \leq p^*$.
1. By definition of max crossing problem, $\xi \leq q^*$.
1. Hence we have $p^* - \epsilon \leq q^* \leq p^*$ for every $\epsilon > 0$.
1. Since $\epsilon$ can be arbitrarily small, it follows that
   $p^* = q^*$.

Conversely, we assume that the strong duality holds.

1. Let $\{ (\bx_k, t_k) \}$ be any sequence of $M$ such that
   $\bx_k \to \bzero$.
1. By definition of $q(\ba)$,

   $$
   q(\ba) = \inf_{(\bx, t) \in M} \{ \langle \bx, \ba \rangle + t \}
   \leq \langle \bx_k, \ba \rangle + t_k \Forall k, \Forall \ba \in \VV. 
   $$
1. Taking the limit on R.H.S. to $k \to \infty$, we obtain

   $$
   q(\ba) \leq \liminf_{k \to \infty} t_k \Forall \ba \in \VV.
   $$
1. Taking the supremum on the L.H.S. over $\ba \in \VV$, we have
   
   $$
   p^* = q^* = \sup_{\ba \in \VV} q(\ba) \leq \liminf_{k \to \infty} t_k.
   $$
```

This result doesn't guarantee the attainment of either
the min common optimal point or the max crossing optimal
point. The next result includes additional conditions
which ensures that the optimal point of max crossing problem
is attained. 

### Second Min Common / Max Crossing Theorem

```{prf:theorem} Min common/max crossing theorem II
:label: res-opt-min-max-strong-duality-2

Consider the min common and max crossing problems.
Assume the following:

1. $-\infty < p^*$.
1. The set

   $$
   \overline{M} = \{ (\bx, t) \in \VV \oplus \RR \ST \text{ there exists } 
   \bar{t} \in \RR \text{ with } 
   \bar{t} \leq t \text{ and } (\bx, \bar{t}) \in M \}
   $$
   is convex.
1. The set 

   $$
   D = \{ \bu  \in \VV \ST \text{ there exists } t \in \RR
   \text{ with } (\bu, t) \in \overline{M} \}
   $$
   contains the origin in its relative interior.

Then $q^* = p^*$ and the optimal solution set of the
max crossing problem 

$$
Q^* = \{ \ba \in \VV \ST q(\ba) = q^* \}
$$
has the form

$$
Q^* = (\affine D)^{\perp} + \tilde{Q}
$$
where $\tilde{Q}$ is a nonempty, convex and compact set
and $(\affine D)^{\perp}$ is the orthogonal complement
of $\affine D$ (which is a subspace by assumption 3 since
it contains the origin).

Furthermore, $Q^*$ is nonempty and compact if and
only if $D$ contains the origin in its interior.
```

Note that $D$ is the set of all possible horizontal
coordinates of points in $M$.
$\bx \in D$ if and only if there exists some $(\bx, t) \in \overline{M}$
if and only if there exists some $(\bx, s) \in M$ with $s \leq t$.
Since $\overline{M}$ is convex and $D$ is a projection
of $\overline{M}$ on $\VV$, hence $D$ is also convex.

```{prf:proof}
We first show that the strong duality holds and
$Q^*$ is nonempty, closed and convex.

1. Condition (3) implies that there exists
   some $(\bzero, t) \in \overline{M}$.
1. By definition of $\overline{M}$,
   there exists some $(\bzero, \overline{t}) \in M$
   such that $\overline{t} \leq t$.
1. Hence $p^* < \infty$.
1. Then, by condition (1), $p^* \in \RR$;
   i.e., the min crossing level is a real number.
1. The vertical axis $\{ (\bzero, t) \ST t \in \RR \}$
   belongs to $\affine \overline{M}$.
1. $p^*$ is the optimal min common value.
1. Hence $(\bzero, p^*)$ is not a relative interior
   point of $\overline{M}$.
1. Accordingly, $(\bzero, p^*) \notin \relint \overline{M}$.

1. By {prf:ref}`res-cvx-proper-sep-set-point`, there exists a hyperplane
   that separates $\overline{M}$ and the point $(\bzero, p^*)$
   properly; i.e., it contains the point $(\bzero, p^*)$,
   contains $\overline{M}$ in one of its half-spaces
   and doesn't contain $\overline{M}$ fully.
1. Hence, there exists a vector $(\ba, r)$ such that

   $$
   \langle \bx, \ba \rangle + t r \geq p^* r  \Forall (\bx, t) \in \overline{M} 
   $$
   and

   $$
   \sup_{(\bx, t) \in \overline{M}} \langle \bx, \ba \rangle + t r >  p^* r.
   $$
   See {prf:ref}`res-cvx-proper-sep-set-point-def`.
1. Since for every $(\overline{\bx}, \overline{t}) \in M$, the
   set $\overline{M}$ contains the half-line
   $\{ (\overline{\bx}, t) \ST \overline{t} \leq t \}$,
   it follows from the first inequality that
   $r \geq 0$ must hold true.
1. $r = 0$ leads to a contradiction.
   1. Assume that $r = 0$.
   1. Then the first inequality reduces to

      $$
      \langle \bx, \ba \rangle \geq 0 \Forall \bx \in D.
      $$
   1. The linear functional $\langle \bx, \ba \rangle$ attains
      its minimum over the set $D$ at $\bzero \in D$ which
      is a relative interior point of $D$ by condition (3).
   1. Since $D$ is convex (projection of convex $\overline{M}$
      on $\VV$), and the linear functional $\langle \bx, \ba \rangle$
      (a concave function)
      attains its minimum at a relative interior point,
      hence, due to {prf:ref}`res-cvxopt-concave-min-relint-const`,
      the function must be constant over $D$.
   1. Hence we have

      $$
      \langle \bx, \ba \rangle = 0 \Forall \bx \in D.
      $$
   1. But this contradicts the second (strict) inequality of the proper separation
      result since $\overline{M}$ cannot be contained entirely inside the
      hyperplane.
   1. We arrive at a contradiction.
   1. Hence $r \neq 0$ and the separating hyperplane is nonvertical.
1. By appropriate normalization, if necessary, we can assume that $r=1$.
1. The proper separation inequalities simplify to

   $$
   \langle \bx, \ba \rangle + t \geq p^*  \Forall (\bx, t) \in \overline{M} 
   $$
   and

   $$
   \sup_{(\bx, t) \in \overline{M}} \langle \bx, \ba \rangle + t >  p^*.
   $$
1. We now note that

   $$
   p^* &\leq \inf_{(\bx, t) \in \overline{M}} \langle \bx, \ba \rangle + t \\
   &\leq \inf_{(\bx, t) \in M} \langle \bx, \ba \rangle + t \\
   &= q(\ba) \\
   &\leq q^*.
   $$
1. Since by weak duality, we always have $q^* \leq p^*$, hence all the inequalities
   must be equalities in the previous relation.
1. Thus we have

   $$
   q(\ba) = q^* = p^*.
   $$
1. Hence $Q^*$ is nonempty as $\ba \in Q^*$.
1. We can also write $Q^*$ as 

   $$
   Q^* = \{ \ba \in \VV \ST q(\ba) \geq q^* \}.
   $$
1. Since $q$ is concave and upper semicontinuous, hence its
   superlevel sets are closed and convex.
1. Hence $Q^*$ being a superlevel set of $q$ is convex and closed. 


We next show that $Q^* = (\affine D)^{\perp} + \tilde{Q}$.

TBD
```


## Minimax and Maximin Problems

We consider functions of the form
$\phi : \VV \oplus \WW \to \RR$ with
$\dom \phi = X \times Z$.
$\VV$ and $\WW$ are real vector spaces.
$X \subseteq \VV$ and $Z \subseteq \WW$
are nonempty sets.


```{index} Minimax problem
```
```{prf:definition} Minimax problem
:label: def-minimax-problem

A  *minimax* problem takes the form

$$
& \text{minimize }  & \sup_{\bz \in Z} \phi(\bx, \bz)\\
& \text{subject to } & \bx \in X
$$
```

```{index} Maximin problem
```
```{prf:definition} Maximin problem
:label: def-maximin-problem

A *maximin* problem takes the form


$$
& \text{maximize }  & \inf_{\bx \in X} \phi(\bx, \bz)\\
& \text{subject to } & \bz \in Z.
$$
```

We next provide a few examples.

### Zero Sum Games

```{prf:example} Zero sum games

We consider a two player game with the following design.

1. Player A can choose one out of $n$ possible moves.
1. Player B can choose one out of $m$ possible moves.
1. Both players make their moves simultaneously.
1. $\bA \in \RR^{n \times m}$ is a payoff matrix.
1. If move $i$ is selected by player A and
   move $j$ is selected by player B, then
   A gives the specified amount $a_{i j}$ to B.
1. Note that $a_{i j} \in \RR$ can be zero, positive or negative.
1. The players use mixed strategy.
1. Player A selects a probability distribution
   $\bx = (x_1, \dots, x_n)$ over her $n$ possible moves.
1. Player B selects a probability distribution
   $\bz = (z_1, \dots, z_m)$ over her $m$ possible moves.
1. Since the probability of selecting move $i$ by player A
   and move $j$ by player B is $x_i z_j$, hence the 
   expected amount to be paid by A to B is

   $$
   \sum_{i j} x_i a_{i j} z_j = \bx^T \bA \bz.
   $$
1. Each player adopts a worst case viewpoint, 
   whereby she optimizes her choice against the
   worst possible selection by the other player.
1. Player A must minimize $\max_{\bz} \bx^T \bA \bz$
   so that she has to pay as low as possible to B.
   1. Suppose A selects the strategy $\bx$.
   1. The amount she has to pay to B for B's selection of strategy $\bz$
      is $\bx^T \bA \bz$.
   1. The maximum amount she has to pay across all possible strategies chosen by B is
      $\max_{\bz} \bx^T \bA \bz$.
   1. By selecting $\bx$, her goal is to minimize the maximum payoff.
1. Player B must maximize $\min_{\bx} \bx^T \bA \bz$.
   1. Suppose B selects a strategy $\bz$.
   1. Then the payoff she gets by a strategy $\bx$ of A
      is $\bx^T \bA \bz$.
   1. The minimum she can get for her choice of $\bz$ is
      $\min_{\bx} \bx^T \bA \bz$.
   1. By selecting $\bz$ her goal is to maximize the minimum payoff.

1. Here $X = \Delta_n \subseteq \RR^n$, the unit simplex of $\RR^n$.
1. Similarly, $Z = \Delta_m \subseteq \RR^m$, the unit simplex of $\RR^m$.
1. $\phi(\bx, \bz) = \bx^T \bA \bz$.
1. The worst case pay off for player A is

   $$
   \inf_{\bx \in X} \sup_{\bz \in Z }\bx^T \bA \bz.
   $$
1. The worst case pay off for player B is

   $$
   \sup_{\bz \in Z} \inf_{\bx \in X }\bx^T \bA \bz.
   $$
1. Under suitable conditions, we can guarantee that

   $$
   \sup_{\bz \in Z} \inf_{\bx \in X }\bx^T \bA \bz 
   = \inf_{\bx \in X} \sup_{\bz \in Z }\bx^T \bA \bz.
   $$ 
```

### Lagrangian Functions

```{prf:example} Lagrangian functions and duality theory

Consider the optimization problem of the form

$$
& \text{minimize }   & f(\bx) \\
& \text{subject to } & g_i(\bx) \leq 0, & \quad i=1,\dots,m
$$
where $f, g_1, \dots, g_m : \VV \to \RR$ are given objective
and inequality constraint functions.

We construct the Lagrangian function

$$
L (\bx, \bz ) = f(\bx) + \sum_{i=1}^m z_i g_i(\bx)
$$
with $\dom L = X \oplus Z$
where $X = \dom f \cap \dom g_1 \cap \dots \cap \dom g_m$
and $Z = \RR^m_+$ (the nonnegative orthant where $\bz \succeq \bzero$).

We construct the *primal problem* as below:

$$
& \text{minimize }   & \sup_{\bz \succeq \bzero } L (\bx, \bz ) \\
& \text{subject to } & \bx \in X.
$$

1. Choose any $\bx \in X$.
1. If any of the constraints $g_i(\bx) \leq 0$ is violated, then
   $g_i(\bx) > 0$ and hence
   $\sup_{\bz \succeq \bzero } L (\bx, \bz ) = \infty$.
   We can easily achieve this by taking $z_i \to \infty$.
1. If none of the constraints are invalidated, then by picking
   $\bz = \bzero$, we have
   $\sup_{\bz \succeq \bzero } L (\bx, \bz ) = f(\bx)$.
1. Hence the problem is equivalent to the original problem.


We can now construct the *dual problem* as below:

$$
& \text{maximize }   & \inf_{\bx \in X } L (\bx, \bz ) \\
& \text{subject to } & \bz \succeq \bzero.
$$

Thus the primal problem is a minimax problem
and the dual problem is a maximin problem
with the Lagrangian playing the role of $\phi$.

Under suitable conditions, the two problems have equal optimal value.
```

### Minimax Equality

In the following, we will explore conditions under which

```{math}
:label: eq-minimax-equality

\sup_{\bz \in Z} \inf_{\bx \in X } \phi(\bx, \bz)
= \inf_{\bx \in X} \sup_{\bz \in Z } \phi(\bx, \bz)
```
and the infimum and the supremum are attained.

The key result is the *saddle point theorem*
which guarantees the equality in {eq}`eq-minimax-equality`
as well as the attainment of the infimum/supremum assuming
convexity/concavity on $\phi$
and compactness on $X$ and $Z$.

The compactness assumptions are restrictive.
For example, in the duality theory, the
Lagrange multipliers $\bz \succeq \bzero$ belong
to the nonnegative orthant which is not compact.

The *minimax theorem* gives conditions
guaranteeing the minimax equality {eq}`eq-minimax-equality`,
although it need not guarantee the attainment of the
infimum and the supremum.

### Minimax Inequality

````{prf:observation} Minimax inequality
:label: res-minimax-inequality

We always have

```{math}
:label: eq-minimax-inequality
\sup_{\bz \in Z} \inf_{\bx \in X } \phi(\bx, \bz)
\leq \inf_{\bx \in X} \sup_{\bz \in Z } \phi(\bx, \bz).
```

In other words, the optimal value of the
maximin problem is less than or equal to
the optimum value of the minimax problem.
````
```{prf:proof}
We note that for every $\bz \in Z$, we have

$$
\inf_{\bx \in X } \phi(\bx, \bz)
\leq \inf_{\bx \in X} \sup_{\bz \in Z } \phi(\bx, \bz).
$$

Taking the supremum on the L.H.S., we obtain the desired
inequality.
```

Thus, in order to show {eq}`eq-minimax-equality`, it is
sufficient to show that the reverse inequality holds.

### Saddle Points

```{index} Saddle point; minimax
```
```{prf:definition} Saddle point
:label: def-minimax-saddle-point

A pair of vectors $\bx^* \in X$ and $\bz^* \in Z$ is called
a saddle point of $\phi$ if

$$
\phi(\bx^*, \bz) \leq \phi(\bx^*, \bz^*) \leq \phi(\bx, \bz^*), 
\quad \Forall \bx \in X, \Forall \bz \in Z.
$$
```

```{prf:remark} Saddle point inequalities
:label: res-minimax-saddle-point-ineq

The pair $(\bx^*, \bz^*) \in \VV \oplus \WW$ is a saddle point
if and only if $\bx^* \in X$, $\bz^* \in Z$ and 

$$
\sup_{\bz \in Z} \phi(\bx^*, \bz) = \phi(\bx^*, \bz^*) = \inf_{\bx \in X} \phi(\bx, \bz^*).
$$

This equality further implies that

$$
&\inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) \\
& \leq \sup_{\bz \in Z} \phi(\bx^*, \bz) = \phi(\bx^*, \bz^*) = \inf_{\bx \in X} \phi(\bx, \bz^*) \\
& \leq \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz).
$$
In short

$$
\inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) 
\leq \phi(\bx^*, \bz^*)
\leq  \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz).
$$

Combined with the minimax inequality {eq}`eq-minimax-inequality`,
it shows that if a saddle point exists, then the
minimax equality {eq}`eq-minimax-equality` holds.
```


```{prf:theorem} Saddle point = minimax equality
:label: res-minimax-saddle-point-minimax-equality

A pair $(\bx^*, \bz^*)$ is a saddle point of $\phi$
if and only if
the minimax equality {eq}`eq-minimax-equality` holds
and
$\bx^*$ is an optimal solution of the
minimax problem

$$
& \text{minimize }  & \sup_{\bz \in Z} \phi(\bx, \bz)\\
& \text{subject to } & \bx \in X
$$
while $\bz^*$ is the optimal solution of the maximin
problem

$$
& \text{maximize }  & \inf_{\bx \in X} \phi(\bx, \bz)\\
& \text{subject to } & \bz \in Z.
$$
```

```{prf:proof}
Suppose that $\bx^*$ is the optimal solution of the
minimax problem and $\bz^*$ is the optimal solution of the maximin
problem.

1. From the minimax problem we obtain

   $$
   \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz)
   = \sup_{\bz \in Z} \phi(\bx^*, \bz)
   \geq  \phi(\bx^*, \bz^*).
   $$
1. From the maximin problem we obtain

   $$
   \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz)
   = \inf_{\bx \in X}  \phi(\bx, \bz^*) \leq \phi(\bx^*, \bz^*).
   $$
1. Combining these inequalities, we have

   $$
   & \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz)
   = \inf_{\bx \in X}  \phi(\bx, \bz^*) \\ 
   &\leq \phi(\bx^*, \bz^*) \\
   &\leq \sup_{\bz \in Z} \phi(\bx^*, \bz)
   = \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz).
   $$
1. If the minimax equality {eq}`eq-minimax-equality` holds,
   then equality holds throughout above giving us

   $$
   \inf_{\bx \in X}  \phi(\bx, \bz^*) =  \phi(\bx^*, \bz^*)
   = \sup_{\bz \in Z} \phi(\bx^*, \bz).
   $$
1. Hence $(\bx^*, \bz^*)$ is a saddle point of $\phi$
   as per {prf:ref}`res-minimax-saddle-point-ineq`.

Conversely, assume that
$(\bx^*, \bz^*)$ is a saddle point of $\phi$.

1. From {prf:ref}`res-minimax-saddle-point-ineq`, 
   we have

   $$
   &\inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) \\
   & \leq \sup_{\bz \in Z} \phi(\bx^*, \bz) 
   = \phi(\bx^*, \bz^*) 
   = \inf_{\bx \in X} \phi(\bx, \bz^*) \\
   & \leq \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz).
   $$
1. The minimax inequality {eq}`eq-minimax-inequality` gives
   us

   $$
   \sup_{\bz \in Z} \inf_{\bx \in X } \phi(\bx, \bz)
   \leq \inf_{\bx \in X} \sup_{\bz \in Z } \phi(\bx, \bz).
   $$
1. Thus, all the inequalities in the previous relationship
   must be equalities. We have

   $$
   &\inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) \\
   & = \sup_{\bz \in Z} \phi(\bx^*, \bz) 
   = \phi(\bx^*, \bz^*) 
   = \inf_{\bx \in X} \phi(\bx, \bz^*) \\
   & = \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz).
   $$
1. Hence the minimax equality holds.
1. It also implies that $\bx^*$ is an optimal solution of the
   minimax problem and $\bz^*$ is the 
   optimal solution of the maximin problem.
```

```{prf:observation} Saddle points as a Cartesian product
:label: res-minimax-saddle-points-product

When the set of saddle points is nonempty, it can be written
as a Cartesian product $X^* \times Z^*$ where
$X^*$ is the set of optimal solutions of the minimax problem
and the $Z^*$ is the set of optimal solutions of the maximin
problem.

In other words, $\bx^*$ and $\bz^*$ can be chosen independently
from the sets $X^*$ and $Z^*$ respectively to form a
saddle point.
This is a direct consequence of
{prf:ref}`res-minimax-saddle-point-minimax-equality`.


If the minimax equality {eq}`eq-minimax-equality` does not
hold, then there is no saddle point even if the minimax
and maximin problems have optimal solutions.
```


## Min Common/Max Crossing Framework for Minimax

Recall that the minimax problem is given by

$$
\inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz).
$$

We add a linear perturbation to $\phi$ and introduce
a function $\psi : \WW \to \ERL$ as

$$
\psi(\bu) = \inf_{\bx \in X} \sup_{\bz \in Z} \{ \phi(\bx, \bz) - \langle \bu, \bz \rangle \}.
$$

We can see that

$$
\psi(\bzero) = \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz).
$$

The linear perturbation term impacts the optimum value of the
minimax problem.
We shall show that if $\psi$ changes in a "regular" manner,
then the minimax equality is guaranteed.

### Framework Definition

```{index} Minimax problem; Min common/max crossing framework
```
````{prf:definition} Min common / max crossing framework for minimax problem
:label: def-minimax-min-common-framework

We define the set $M$ required for the min common/max crossing framework
as

$$
M = \epi \psi
$$
where $\psi : \WW \to \ERL$ is given by

```{math}
:label: eq-minimax-psi
\psi(\bu) = \inf_{\bx \in X} \sup_{\bz \in Z} \{ \phi(\bx, \bz) - \langle \bu, \bz \rangle \}.
```

1. Recall that min common value is given by
   
   $$
   p^* = \inf_{(\bzero, p) \in M} p.
   $$
1. Note that for $\bu = \bzero$, 
   $M$ contains all the points $(\bzero, t)$ such that
   $\psi(\bzero) \leq t$.
1. In particular, $(\bzero, \psi(\bzero)) \in M$
   and if $(\bzero, t) \in M$ then $\psi(\bzero) \leq t$.
1. Hence $p^*$ is given by
   
   $$
   p^* = \psi(\bzero) = \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz).
   $$
1. Since $M$ is an epigraph, hence the sets $M$ and $\overline{M}$ are
   identical in the min common/max crossing framework.
1. If $\psi$ is convex, then $M = \epi \psi$ is convex as desired
   in several results of the min common/max crossing framework.

The corresponding max crossing problem is given by:

$$
& \text{maximize }  &  & q (\ba) \\
& \text{subject to } & & \ba \in \WW
$$
1. We note that 

   ```{math}
   :label: eq-minimax-q-a
   q(\ba) 
   &= \inf_{(\bu, t) \in \epi \psi} \{ \langle \bu, \ba \rangle + t \}\\
   &=  \inf_{(\bu, t) \in \psi(\bu) \leq t}  \{ \langle \bu, \ba \rangle + t \} \\
   &= \inf_{\bu \in \WW} \{\psi(\bu) + \langle \bu, \ba \rangle \}.
   ```
1. Its optimal value is denoted by $q^*$; i.e.,

   $$
   q^* = \sup_{\ba \in \WW} q(\ba).
   $$
````

### Connection

```{prf:observation} Connection between minimax equality and min common/max crossing framework
:label: res-minimax-common-crossing-relation

1. By putting the definition of $\psi(\bu)$ in the expression
   for $q(\ba)$, we obtain

   $$
   q(\ba) 
   &= \inf_{\bu \in \WW} \{\psi(\bu) + \langle \bu, \ba \rangle \} \\
   &= \inf_{\bu \in \WW} \{
      \inf_{\bx \in X} \sup_{\bz \in Z} \{ \phi(\bx, \bz) - \langle \bu, \bz \rangle \} 
      + \langle \bu, \ba \rangle \} \\
   &= \inf_{\bu \in \WW} \inf_{\bx \in X} \sup_{\bz \in Z} 
      \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle \}.
   $$
1. In particular, for every $\ba \in Z$, if we set $\bz = \ba$ in this relation,
   we can see that

   $$
   \inf_{\bx \in X}  \phi(\bx, \ba) \leq q(\ba) \Forall \ba \in Z.
   $$
1. From the weak duality principle, we have $q^* \leq p^*$.
1. We have established that $p^* = \psi(\bzero)$.
1. We can now see that

   $$
   \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz)
   &= \sup_{\ba \in Z} \inf_{\bx \in X} \phi(\bx, \ba)\\
   & \leq \sup_{\ba \in Z} q(\ba) \\
   & \leq \sup_{\ba \in \WW} q(\ba) \\
   &= q^* \\
   &\leq p^* \\
   &= \psi(\bzero) \\
   &= \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz).
   $$
1. This is nothing but the minimax inequality {eq}`eq-minimax-inequality`.
1. We can see that if the minimax equality {eq}`eq-minimax-equality` holds,
   then all inequalities in the previous relation turn into equalities
   and we have $q^* = p^*$.
1. In other words, if the minimax equality holds, then the optimal
   values of the min common and max crossing problems are equal.
```

### Convexity of $\psi$

```{prf:lemma} Convexity of $\phi$ w.r.t. $\bx$ and convexity of $\psi$
:label: res-minimax-psi-convex-phi-x-convex

Let $X$ be a nonempty convex subset of $\VV$
and $Z$ be a nonempty subset of  $\WW$.
Let $\phi: \VV \oplus \WW \to \RR$ be a function
with $\dom \phi = X \times Z$.
Assume that for each $\bz \in Z$, the function
$\phi(\cdot, \bz) : \VV \to \RR$ is convex.
Then the function $\psi$ as defined in {eq}`eq-minimax-psi`
is convex.
```

```{prf:proof}
Recall that

$$
\psi(\bu) = \inf_{\bx \in X} \sup_{\bz \in Z} \{ \phi(\bx, \bz) - \langle \bu, \bz \rangle \}.
$$

1. Fix some $\bz \in Z$.
1. Consider the function
   $f_z(\bx, \bu) = \phi(\bx, \bz) - \langle \bu, \bz \rangle$.
1. Clearly, $f_z$ is convex for each $\bz \in Z$ by hypothesis.
1. Taking the pointwise supremum over $\bz \in Z$,
   the function

   $$
   F (\bx, \bu) = \begin{cases}
   \sup_{\bz \in Z} \{ \phi(\bx, \bz) - \langle \bu, \bz \rangle \}
   & \bx \in X;\\
   \infty & \bx \notin X.
   \end{cases}
   $$
   is also convex (over $\bx$ and $\bu$).
1. We now have

   $$
   \psi(\bu) = \inf_{\bx \in \VV} F (\bx, \bu).
   $$
1. Since partial minimization preserves convexity, hence
   $\psi$ is convex.
```

### Minimax Equality Strong Duality Equivalence Conditions

```{prf:lemma} Closedness and convexity of $-\phi$ w.r.t. $\bz$ and minimax equality
:label: res-neg-phi-z-convex-closed

Let $X$ be a nonempty convex subset of $\VV$
and $Z$ be a nonempty subset of  $\WW$.
Let $\phi: \VV \oplus \WW \to \RR$ be a function
with $\dom \phi = X \times Z$.
Assume that for each $\bx \in X$, the function
$-\phi(\bx, \cdot) \to \RR$ is closed and
convex.
Then the function $q : \WW \to \ERL$ given by

$$
q(\ba) = \inf_{(\bu, t) \in \epi \psi} \{ \langle \bu, \ba \rangle + t \},
\quad \ba \in \WW,
$$
where $\psi$ as defined in {eq}`eq-minimax-psi`, satisfies

$$
q(\ba) = \begin{cases}
\inf_{\bx \in  X} \phi (\bx, \ba) & \ba \in Z;\\
-\infty & \ba \notin Z.
\end{cases}
$$

Furthermore, we have $q^* = p^*$ if and only if the
minimax equality {eq}`eq-minimax-equality` holds.
```

```{prf:proof}
We shall show the following one by one.

1. $q(\ba) \geq \inf_{\bx \in X} \phi(\bx, \ba) \Forall \ba \in Z$.
1. $q(\ba) \leq \inf_{\bx \in X} \phi(\bx, \ba) \Forall \ba \in Z$.
1. $q(\ba) = -\infty \Forall \ba \notin Z$.


(1)

1. We have already established in {eq}`eq-minimax-q-a` that

   $$
   q(\ba) = \inf_{\bu \in \WW} \{\psi(\bu) + \langle \bu, \ba \rangle \}.
   $$
1. By using the definition of $\psi$, we further established that

   $$
   q(\ba) = \inf_{\bu \in \WW} \inf_{\bx \in X} \sup_{\bz \in Z} 
         \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle \}.
   $$
1. By rearranging the order of infimum operations, we have

   $$
   q(\ba) = \inf_{\bx \in X} \inf_{\bu \in \WW} \sup_{\bz \in Z} 
         \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle \}.
   $$
1. For any $\ba \in Z$ we have

   $$
   \sup_{\bz \in Z} 
         \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle \}
   &\geq \phi(\bx, \ba) + \langle \ba - \ba, \bu \rangle \\
   &= \phi(\bx, \ba)
   \quad \Forall \bx \in X, \Forall \bu \in \WW.
   $$
1. This in turn implies that

   $$
   q(\ba) \geq \inf_{\bx \in X} \phi(\bx, \ba) \Forall \ba \in Z.
   $$


(2)


1. Let $r_x : \WW \to \RR$ be given by

   $$
   r_x(\bz) = -\phi(\bx, \bz).
   $$
1. By hypothesis $r_x$ is closed and convex.
1. Let $\ba \in Z$.
1. Fix some $\bx \in X$.
1. Since $r_x$ is a closed and convex function,
   hence $\epi r_x$ is a closed and convex set.
1. Since $\ba \in Z$, hence the point
   $(\ba, r_x(\ba)) \in \epi r_x$.
1. For some $\epsilon > 0$, consider the point
   $(\ba, r_x(\ba) - \epsilon)$.
1. Clearly $(\ba, r_x(\ba) - \epsilon) \notin \epi r_x$.
1. By definition of $r_x$, $r_x(\bz)$ is finite for all $\bz \in Z$,
   $Z$ is nonempty and $\epi r_x$ is closed.
1. Since $r_x(\bz)$ is finite for all $\bz \in Z$, the
   epigraph doesn't contain any vertical lines.
1. Hence, due to {prf:ref}`res-opt-cvx-set-non-vert-supp-plane`,
   there exists a nonvertical hyperplane that
   strongly separates the point $(\ba, r_x(\ba) - \epsilon)$
   from $\epi r_x$.
1. Hence there exists a normal vector
   $(\bu, 1)$ and a scalar $c$ such that

   $$
   \langle \ba, \bu \rangle + (r_x(\ba) - \epsilon)
   < c < \langle \bu, \bz \rangle + r_x(\bz) \Forall \bz \in Z.
   $$
1. Substituting $r_x(\bz) =  -\phi(\bx, \bz)$, we get

   $$
   \langle \ba, \bu \rangle + (-\phi(\bx, \ba) - \epsilon)
   < \langle \bu, \bz \rangle - \phi(\bx, \bz). 
   $$
1. Rearranging, we get

   $$
   \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle
   < \phi(\bx, \ba) + \epsilon \Forall \bz \in Z.
   $$
1. Letting $\epsilon \downarrow 0$, we have

   $$
   \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle
   \leq \phi(\bx, \ba) \Forall \bz \in Z.
   $$
1. We further note that

   $$
   \inf_{\bu \in \WW} \sup_{\bz \in Z} 
         \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle \}
   \leq \sup_{\bz \in Z} 
         \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle \}
   \leq  \phi(\bx, \ba).     
   $$
1. Taking infimum over $\bx \in X$ on the L.H.S., we obtain

   $$
   q(\ba) = \inf_{\bx \in X} \inf_{\bu \in \WW} \sup_{\bz \in Z} 
         \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle \}
   \leq \inf_{\bx \in X} \phi(\bx, \ba)
   $$
   as desired.

(3)

1. Take any $\ba \notin Z$.
1. Fix an arbitrary $\bx \in X$.
1. Consider a sequence $\{ t_k \}$ such that $t_k \to \infty$.
1. Since $\ba \notin Z$, hence $(\ba, t_k) \notin \epi r_x$ for every $k$.
1. Again applying {prf:ref}`res-opt-cvx-set-non-vert-supp-plane`,
   for each $k$, there exists a nonvertical hyperplane
   strongly separating $(\ba, t_k)$ from $\epi r_x$.
1. Hence for each $k$, there exists a normal vector $(\bu_k , 1)$
   such that

   $$
   \langle \ba, \bu_k \rangle + t_k <\langle \bz, \bu_k \rangle - \phi(\bx, \bz) 
   \Forall \bz \in Z.
   $$
1. Rearranging, we have

   $$
   \phi(\bx, \bz) + \langle \ba - \bz, \bu_k \rangle < -t_k,
   \quad \Forall \bz \in Z, \Forall k.
   $$
1. Thus, we have

   $$
   \inf_{\bu \in \WW} \sup_{\bz \in Z} 
         \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle \}
   \leq \sup_{\bz \in Z} 
         \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu_k \rangle \}
   \leq -t_k \quad \Forall k.
   $$
1. Taking the limit on the R.H.S. as $k \to \infty$, we can see that

   $$
    \inf_{\bu \in \WW} \sup_{\bz \in Z} 
         \{ \phi(\bx, \bz) + \langle \ba - \bz, \bu \rangle \} = -\infty
     \quad \Forall \bx \in X.
   $$
1. Finally, taking the infimum over $\bx \in X$, we can see that

   $$
   q(\ba) = -\infty.
   $$

By {prf:ref}`res-minimax-common-crossing-relation`,
if minimax equality holds, then $q^* = p^*$.
For the converse, we now assume that $q^* = p^*$.
Then

$$
& \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) \\
&= \psi(\bzero)
=  p^*
= q^* \\
&= \sup_{\ba \in \WW} q(\ba)
= \sup_{\bz \in Z} q(\bz) \\
&= \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz).
$$
Thus the minimax equality holds.
```

## Minimax Theorems


### First Theorem

```{prf:theorem} Minimax theorem I
:label: res-minimax-theorem-1

Let $X$ be a nonempty convex subset of $\VV$
and $Z$ be a nonempty subset of  $\WW$.
Let $\phi: \VV \oplus \WW \to \RR$ be a function
with $\dom \phi = X \times Z$.
Assume that for each $\bz \in Z$,
the function $\phi (\cdot, \bz) : \VV \to \RR$
is convex, and for each $\bx \in X$, the
function $-\phi(\bx, \cdot) : \WW \to \RR$
is closed and convex.
Assume further that

$$
\inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) < \infty.
$$
Then, the minimax equality {eq}`eq-minimax-equality` holds;
i.e.,

$$
\sup_{\bz \in Z} \inf_{\bx \in X } \phi(\bx, \bz)
= \inf_{\bx \in X} \sup_{\bz \in Z } \phi(\bx, \bz),
$$
if and only if the function $\psi$ as defined in {eq}`eq-minimax-psi`
is lower semicontinuous at $\bu = \bzero$; i.e.,

$$
\psi(\bzero) \leq \liminf_{k \to \infty} \psi(\bu_k)
$$
for every sequence $\{ \bu_k \}$ with $\bu_k \to \bzero$.
```

```{prf:proof}
The proof consists of establishing the correspondence
between the conditions in this result and the conditions
in the first min common/max crossing theorem
({prf:ref}`res-opt-min-max-strong-duality-1`).

1. We choose the set $M$ as described in {prf:ref}`def-minimax-min-common-framework`,
   to be the epigraph of the function $\psi$.

   $$
   M = \overline{M} =  \epi \psi = \{ (\bu, t) \in \WW \oplus \RR \ST 
      \psi(\bu) \leq t \}.
   $$
1. We have shown in {prf:ref}`def-minimax-min-common-framework`
   that $p^* = \psi(\bzero) = \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz)$.
1. By hypothesis, $p^* < \infty$.
1. Hence the first assumption of {prf:ref}`res-opt-min-max-strong-duality-1`
   is satisfied.
1. Following {prf:ref}`res-minimax-psi-convex-phi-x-convex`, $\psi$
   is convex.
1. Hence $M = \epi \psi$ is also convex.
1. Hence the second assumption of {prf:ref}`res-opt-min-max-strong-duality-1`
   is satisfied.
1. Finally, the condition

   $$
   \psi(\bzero) \leq \liminf_{k \to \infty} \psi(\bu_k)
   $$
   is equivalent to the condition of {prf:ref}`res-opt-min-max-strong-duality-1`
   that for every sequence
   $\{ (\bu_k, t_k) \}$ of $M$ with $\bu_k \to \bzero$.

   $$
   p^* \leq \liminf_{k \to \infty} t_k
   $$
   holds true.
   1. We have $t_k \geq \psi(\bu_k)$. 
   1. Hence

      $$
      \liminf_{k \to \infty} t_k \geq \liminf_{k \to \infty} \psi(\bu_k)
      \geq \psi(\bzero) = p^*. 
      $$
1. Following {prf:ref}`res-opt-min-max-strong-duality-1`, 
   this condition holds if and only if $p^* = q^*$.
1. Since $-\phi(\bx, \cdot)$ is closed and convex, hence
   following {prf:ref}`res-neg-phi-z-convex-closed`,
   this condition holds if and only if
   minimax equality holds.
```


### Second Theorem

We can adapt the argument of first minimax theorem
to include conditions on the lines of
the second min common/max crossing theorem
{prf:ref}`res-opt-min-max-strong-duality-2`.

```{prf:theorem} Minimax theorem II
:label: res-minimax-theorem-2

Let $X$ be a nonempty convex subset of $\VV$
and $Z$ be a nonempty subset of  $\WW$.
Let $\phi: \VV \oplus \WW \to \RR$ be a function
with $\dom \phi = X \times Z$.
Assume that for each $\bz \in Z$,
the function $\phi (\cdot, \bz) : \VV \to \RR$
is convex, and for each $\bx \in X$, the
function $-\phi(\bx, \cdot) : \WW \to \RR$
is closed and convex.
Assume further that

$$
-\infty  < \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz)
$$
and that $\bzero$ lies in the relative interior of
the effective domain of the function $\psi$
as defined in {eq}`eq-minimax-psi`.
Then, the minimax equality {eq}`eq-minimax-equality` holds;
i.e.,

$$
\sup_{\bz \in Z} \inf_{\bx \in X } \phi(\bx, \bz)
= \inf_{\bx \in X} \sup_{\bz \in Z } \phi(\bx, \bz),
$$
and the supremum over $Z$ in the left hand side is finite
and is attained.
Furthermore, the set of $\bz \in Z$ attaining this
supremum is compact if and only if $\bzero$
lies in the interior of the effective domain
of $\psi$.
```

## Saddle Point Theorems

```{div}
1. From the first minimax theorem
   ({prf:ref}`res-minimax-theorem-1`), we can see that
   minimax equality is satisfied if and only if
   the function $\psi$ is lower semicontinuous
   at $\bu = \bzero$.
1. If $\psi$ is closed, then it will be
   lower semicontinuous.
1. The proof of {prf:ref}`res-minimax-psi-convex-phi-x-convex`
   shows that $\psi$ can be written as a partial minimization
   of $F$

   $$
   \psi(\bu) = \inf_{\bx \in \VV} F (\bx, \bu).
   $$
   where $F: \VV \oplus \WW \to \RERL$ is given by

   $$
   F (\bx, \bu) = \begin{cases}
   \sup_{\bz \in Z} \{ \phi(\bx, \bz) - \langle \bu, \bz \rangle \}
   & \bx \in X;\\
   \infty & \bx \notin X.
   \end{cases}
   $$
1. The results in {ref}`sec:cvx:func:partial:min:closedness` can
   be used to guarantee the closedness of $\psi$.
1. These results can also guarantee that the infimum of $F$
   over $\bx$ is attained.
1. In particular $\psi(\bzero)$ will be finite and hence
   guaranteeing that the optimal value of the minimax
   problem is finite. 
```


```{prf:definition} Auxiliary functions for the minimax problem
:label: def-minimax-aux-funcs

Let $X$ be a nonempty convex subset of $\VV$
and $Z$ be a nonempty subset of  $\WW$.
Let $\phi: \VV \oplus \WW \to \RR$ be a function
with $\dom \phi = X \times Z$.

For each $\bz \in Z$, the function $\eta_z : \VV \to \RERL$ is defined
as

$$
\eta_z(\bx) = \begin{cases}
\phi(\bx, \bz) & \bx \in X;\\
\infty & \bx \notin X.
\end{cases}
$$


For each $\bx \in X$, the function $\rho_x : \WW \to \RERL$ is defined
as

$$
\rho_x(\bz) = \begin{cases}
- \phi(\bx, \bz) & \bz \in Z;\\
\infty & \bz \notin Z.
\end{cases}
$$

The function $\eta: \VV \to \RERL$ is defined as

$$
\eta (\bx) = \sup_{\bz \in Z} \eta_z (\bx), \quad \bx \in \VV.
$$
The function $\rho: \WW \to \RERL$ is defined as

$$
\rho (\bz) = \sup_{\bx \in X} \rho_x (\bz), \quad \bz \in \WW.
$$
```

```{div}
Following remarks are in order.

1. If $\eta_z$ is closed and convex for each $\bz \in Z$,
   then $\eta$ is closed and convex
   due to {prf:ref}`res-cvx-ptws-supremum`. 
1. If $\rho_x$ is closed and convex for each $\bx \in X$,
   then $\rho$ is closed and convex
   due to {prf:ref}`res-cvx-ptws-supremum`.
1. By definition, $\eta(\bx) > -\infty$ for every $\bx \in X$.
1. $\eta$ can be proper only if $\eta(\bx) < \infty$ for some $\bx \in X$.
1. Equivalently, for the optimal minimax value

   $$
   \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) < \infty
   $$
   must hold for $\eta$ to be proper.
1. Similarly, $\rho (\bz) > -\infty$ for every $\bz \in Z$.
1. $\rho$ can be proper only if $\rho(\bz) < \infty$ for some $\bz \in Z$.
1. This is possible only if

   $$
   \inf_{\bz \in Z} \sup_{\bx \in X} (- \phi (\bx, \bz)) < \infty.
   $$
1. Equivalently, for the optimal maximin value

   $$
   -\infty < \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz)
   $$
   must hold true.
1. The set of minimizers of $\eta$ are the optimal points for the
   minimax problem: $X^*$.
1. The set of minimizers of $\rho$ are the optimal points of the
   maximin problem: $Z^*$.
```

### Minimax Equality and Attainment of Minimax Solution

In the following results, we provide conditions under which
the minimax equality is attained and the the set of
optimal solutions for the minimax problem is nonempty.


```{prf:theorem} Compact sublevel sets of $\eta$
:label: res-minimax-exist-compact-sublevel-sets-eta

Assume the following:

1. $\eta_z$ is closed and convex for every $\bz \in Z$.
1. $\rho_x$ is closed and convex for every $\bx \in X$.
1. The optimal minimax value is less than infinity

   $$
   \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) < \infty.
   $$
1. The sublevel sets of $\eta$ are compact.

Then the minimax equality {eq}`eq-minimax-equality` holds and
the set of optimal points for the minimax problem $X^*$ is
nonempty and compact. 
```


```{prf:proof}
.

1. Under the assumptions above, the function $\eta$
   is proper, closed and convex.
1. By definition $F(\bx, \bu) > -\infty$ for every $\bx, \bu$.
1. Note that $F(\bx, \bzero) = \eta(\bx)$.
1. Since $\eta$ is proper, hence
   there exists $\bx \in X$ such that
   $F(\bx, \bzero) < \infty$.
1. Hence $F$ is also proper.
1. $F$ is also closed and convex.

   1. Fix some $\bz \in Z$.
   1. Consider the function
      $f_z(\bx, \bu) = \eta_z(\bx) - \langle \bu, \bz \rangle$.
   1. $\eta_z$ is closed and convex for every $\bz$ by hypothesis.
   1. Hence $f_z$ is closed and convex for every $\bz$.
   1. Taking the pointwise supremum over $\bz \in Z$,
      $F$ is closed and convex.
1. The sets
 
   $$
   \{ \bx \ST F(\bx, \bzero) \leq t \}
   = \{ \bx \ST \eta(\bx) \leq t \}
   $$
   are the sublevel sets of $\eta$ which are compact
   for every $t$ by hypothesis.
1. We can easily select a scalar for which the
   sublevel set of $\eta$ is also nonempty since
   $\eta$ is proper.
1. Hence, due to {prf:ref}`res-cvxf-partial-minimization-closedness-1`,
   the function $\psi$ which is
   a partial minimization of $F$ over $\bx$
   is proper, closed and convex.
1. Since $\psi$ is closed, hence it is lower semicontinuous.
1. In particular, $\psi$ is l.s.c. at $\bu = \bzero$.
1. Hence due to {prf:ref}`res-minimax-theorem-1`,
   the minimax equality holds. 
1. Since $X^*$ is the set of minimizers of $\eta$,
   $\eta$ is proper and closed,
   and the sublevel sets of $\eta$ are compact, 
   hence $X^*$ is nonempty and compact
   due to Weierstrass' theorem
   ({prf:ref}`res-opt-weierstrass-theorem`).
```


```{prf:theorem} Recession and constancy space of $\eta$
:label: res-minimax-exist-recession-constancy-eta

Assume the following:

1. $\eta_z$ is closed and convex for every $\bz \in Z$.
1. $\rho_x$ is closed and convex for every $\bx \in X$.
1. The optimal minimax value is less than infinity

   $$
   \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) < \infty.
   $$
1. The recession cone and constancy space of the function
   $\eta$ are equal.

Then the minimax equality {eq}`eq-minimax-equality` holds and
the set of optimal points for the minimax problem $X^*$ is
nonempty. 
```



```{prf:theorem} $F$ domain as a set of linear inequalities
:label: res-minimax-exist-F-proper-closed-C-lin-ineq

Assume the following:

1. $\eta_z$ is closed and convex for every $\bz \in Z$.
1. $\rho_x$ is closed and convex for every $\bx \in X$.
1. The optimal minimax value is less than infinity

   $$
   \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) < \infty.
   $$
1. The function

   $$
   F (\bx, \bu) = \begin{cases}
   \sup_{\bz \in Z} \{ \phi(\bx, \bz) - \langle \bu, \bz \rangle \}
   & \bx \in X;\\
   \infty & \bx \notin X
   \end{cases}
   $$
   has the form

   $$
   F (\bx, \bu) = \begin{cases}
   \overline{F}(\bx, \bu)
   & (\bx, \bu) \in C;\\
   \infty & (\bx, \bu) \notin C
   \end{cases}
   $$
   where $\overline{F}$ is a proper, closed, and convex
   function on $\VV \oplus \WW$ and $C$ is specified
   by linear inequalities; i.e,

   $$
   C = \{ (\bx, \bu) \ST \bA \bx + \bB \bu \preceq \bb \},
   $$
   where $\bA, \bB$ are matrices and $\bb$ is a vector.
1. Every common direction of recession of $C$ and $\overline{F}$
   is a direction along which $\overline{F}$ is constant.


Then the minimax equality {eq}`eq-minimax-equality` holds and
the set of optimal points for the minimax problem $X^*$ is
nonempty. 
```


```{prf:theorem} Quadratic form $\phi$
:label: res-minimax-exist-quadratic-form-phi

Assume the following:

1. $\VV = \RR^n$ and $\WW = \RR^m$. 
1. The function $\phi$ has a quadratic form

   $$
   \phi(\bx, \bz) = \bx^T \bQ \bx + \bc^T \bx + \bz^T \bM \bx 
   - \bz^T \bR \bz - \bd^T \bz
   $$
   where $\bQ$ and $\bR$ are symmetric matrices,
   $\bM$ is a matrix, and
   $c$ and $d$ are vectors.
1. $Z = \RR^m$.
1. $X$ is a set of the form

   $$
   X = \{ \bx \ST \bx^T \bQ_j \bx + \ba^T_j \bx + b_j \leq 0, j=1, \dots, r \}
   $$
   where $\bQ_j$ are symmetric positive semidefinite matrices,
   $\ba_j$ are vectors and $b_j$ are scalars. 
1. $\eta_z$ is closed and convex for every $\bz \in Z$.
1. $\rho_x$ is closed and convex for every $\bx \in X$.
1. The optimal minimax value satisfies

   $$
   -\infty < \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) < \infty.
   $$

Then the minimax equality {eq}`eq-minimax-equality` holds and
the set of optimal points for the minimax problem $X^*$ is
nonempty. 
```

### Existence of Saddle Points

```{prf:theorem} Compact sublevel sets of $\eta$ and $\rho$
:label: res-minimax-saddle-compact-sublevel-eta-rho

Assume the following:

1. $\eta_z$ is closed and convex for every $\bz \in Z$.
1. $\rho_x$ is closed and convex for every $\bx \in X$.
1. Assume that either

   $$
   \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) < \infty
   $$
   or

   $$
   -\infty < \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz)
   $$
   holds true.
1. The sublevel sets of $\eta$ and $\rho$ are compact.

Then the set of saddle points of $\phi$ is nonempty
and compact. 
```

```{prf:proof}
First assume that $\inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) < \infty$.

1. By applying {prf:ref}`res-minimax-exist-compact-sublevel-sets-eta`,
   minimax equality holds and $X^*$ is nonempty.
1. Hence $\inf_{\bx \in X} \sup_{\bz \in Z } \phi(\bx, \bz)$ is finite.
1. Due to minimax equality:

   $$
   -\infty < \sup_{\bz \in Z} \inf_{\bx \in X } \phi(\bx, \bz)
   = \inf_{\bx \in X} \sup_{\bz \in Z } \phi(\bx, \bz) < \infty.
   $$
1. We reverse the roles of $\bx$ and $\bz$ and the sign of $\phi$
   and apply {prf:ref}`res-minimax-exist-compact-sublevel-sets-eta`
   again to show that $Z^*$ is nonempty and compact set.
1. The set of saddle points is a Cartesian product of $X^*$
   and $Z^*$.
1. Since both $X^*$ and $Z^*$ are nonempty and compact,
   hence $X^* \times Z^*$ is also nonempty and compact.

Now assume that $-\infty < \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz)$.
1. Then $\inf_{\bz \in Z} \sup_{\bx \in X} (-\phi(\bx, \bz)) < \infty$. 
1. we can then reverse the role of $\bx$ and $\bz$ in the preceding argument.
```


```{prf:theorem} Recession cones and constancy spaces of $\eta$ and $\rho$
:label: res-minimax-saddle-recession-constancy-eta-rho

Assume the following:

1. $\eta_z$ is closed and convex for every $\bz \in Z$.
1. $\rho_x$ is closed and convex for every $\bx \in X$.
1. Assume that either

   $$
   \inf_{\bx \in X} \sup_{\bz \in Z} \phi(\bx, \bz) < \infty
   $$
   or

   $$
   -\infty < \sup_{\bz \in Z} \inf_{\bx \in X} \phi(\bx, \bz)
   $$
   holds true.
1. The recession cones and constancy spaces of $\eta$ and $\rho$
   are equal to each other:

   $$
   R_{\eta} = L_{\eta} 
   \text{ and }
   R_{\rho} = L_{\rho}.
   $$

Then the set of saddle points of $\phi$ is nonempty. 
```


### Saddle Point Theorem

The analysis in this section culminates into the following result.

```{prf:theorem} Saddle point theorem
:label: res-minimax-saddle-point-theorem

Assume that
$\eta_z$ is closed and convex for every $\bz \in Z$
and $\rho_x$ is closed and convex for every $\bx \in X$.
Then the set of saddle points of $\phi$ is nonempty
and compact under any of the following conditions.

1. $X$ and $Z$ are compact.
1. $Z$ is compact and there exists a vector $\overline{\bz} \in Z$
   and a scalar $c$ such that the sublevel set

   $$
   \{ \bx \in X \ST \phi(\bx, \overline{\bz}) \leq c \}
   $$
   is nonempty and compact.
1. $X$ is compact and there exists a vector $\overline{\bx} \in X$
   and a scalar $c$ such that the superlevel set

   $$
   \{ \bz \in Z \ST \phi(\overline{\bx}, \bz) \geq c \}
   $$
   is nonempty and compact.
1. There exist vectors $\overline{\bx} \in X$
   and $\overline{\bz} \in Z$ and a scalar $c$ such that the sets

   $$
   \{ \bx \in X \ST \phi(\bx, \overline{\bz}) \leq c \}
   \text{ and }
   \{ \bz \in Z \ST \phi(\overline{\bx}, \bz) \geq c \}
   $$
   are nonempty and compact.
```

