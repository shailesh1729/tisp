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
1. A hyperplane in $\VV \oplus \RR$ in $\VV \oplus \RR$
   is associated with a nonzero normal vector of the form $(\ba, b)$
   where $\ba \in \VV$ and $b \in \RR$.

   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST \langle \bx, \ba \rangle  + t b = c \}.
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

```{div}
Let us see how these definitions can be interpreted.
Consider the case where $\ba = \bzero$.

1. The hyperplane description reduces to

   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST  t b = c \}.
   $$
1. It simplifies to

   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST  t = \frac{c}{b} \}
   $$
   since $b$ must be nonzero.
1. Along the $\VV$ axes, the points in set $H$ can take any value
   but along the $\RR$ axis, they must take a fixed value given by
   $\frac{c}{b}$.
1. We can see that $H$ is a hyperplane which is parallel to $\VV \times \{ 0 \}$.
1. For the specific case where $c = 0$, $H = \VV \times \{ 0 \}$.
1. Hence they are called horizontal hyperplanes.
1. Note that $H$ intersects with the $\RR$ axis at the point
   $(\bzero, \frac{c}{b})$.

Now consider the case where $b = 0$.

1. The hyperplane description reduces to

   $$
   H = \{ (\bx, t) \in \VV \oplus \RR \ST  \langle \bx, \ba \rangle = c \}.
   $$
1. The set $H_v = \{ \bx \in \VV \ST  \langle \bx, \ba \rangle = c \}$
   describes a hyperplane of $\VV$.
1. $H$ is constructed by allowing $H_v$ to slide along the $\RR$ axis
   as any value is allowed in the last coordinate (vertical axis). 
1. Hence this is called a vertical hyperplane.
```

```{prf:observation} Intersection of nonvertical hyperplane with $\RR$ axis
If a hyperplane $H$ with the normal vector $(\ba, b)$ is nonvertical
(i.e., b \neq 0), then it intersects with the $\RR$ axis at a unique point.

1. Indeed the $\RR$ axis is identified with the set of points 

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
   that contain $C$ in its closed half spaces above.
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
