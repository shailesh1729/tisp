(sec:opt:pocs)=
# Projection on Convex Sets

```{div}
We will assume $\VV$ to be real $n$-dimensional vector space space with
an inner product $\langle \cdot, \cdot \rangle$ 
, the induced norm $\| \cdot \|$ and corresponding
dual norm $\| \cdot \|_*$ for the dual space $\VV^*$.
```

We are interested in mapping a point $\bx$ to the
nearest point in a set $C$. In general, this problem
may have zero, one or multiple solutions. 
However, in the special case where $C$ is a nonempty,
closed and convex set, then there is exactly one
such point in $C$ which is nearest to a given point $\bx$.
This nearest point is called the projection of $\bx$ 
on to $C$.

Main references for this section are
{cite}`beck2014introduction,bertsekas2003convex`.


## Projection Theorem

```{prf:theorem} Projection theorem
:label: res-pocs-projection-theorem

Let $C$ be a nonempty, closed and convex subset of $\VV$.
For every $\bx \in \VV$, there exists a unique vector
that minimizes $\| \bz - \bx \|$ over all $\bz \in C$.
This vector is called the *projection* of $\bx$ on $C$.
```

```{prf:proof}
We fix some $\bx \in \VV$ and choose an element $\bw \in C$. 

1. Consider the function

   $$
   g(\bz) = \frac{1}{2} \| \bz - \bx \|^2.
   $$
1. Minimizing $\| \bz - \bx \|$ over all $C$ is equivalent
   to minimizing $g(\bz)$ over the set

   $$
   D = \{  \bz \in C \ST \| \bz - \bx \| \leq \| \bw - \bx \| \}.
   $$
1. We note that $D$ is a compact set and
   $g$ is a l.s.c., closed and coercive function.
1. By Weierstrass' theorem {prf:ref}`res-opt-min-rv-func-closed-set`, 
   the set of minimizers for $g$ is nonempty and compact.

We now show that the minimizer is unique.

1. $g$ is a strictly convex function because its Hessian
   matrix is identity matrix which is positive definite.
1. Hence, the minimizer is unique
   due to {prf:ref}`res-cvxopt-strict-local-global-minimum`. 
```

## Orthogonal Projection


```{prf:definition} Orthogonal Projection Mapping
:label: def-pocs-projection-mapping

Let $C$ be a nonempty, closed and convex subset of $\VV$. 
The *orthogonal projection mapping*  $P_C : \VV \to \VV$ is defined by:

$$
P_C(\bx) \triangleq \underset{\by \in C}{\argmin} \| \by - \bx \| 
\Forall \bx \in \VV. 
$$
This mapping is well defined since the projection is unique
for a nonempty, closed and convex set $C$
due to {prf:ref}`res-pocs-projection-theorem`.

The vector $P_C(\bx)$ is called the *projection* of $\bx$ on
the set $C$.
```

## Characterization

```{prf:theorem} Orthogonal projection characterization
:label: res-cvx-projection-characterization

Let $C$ be a nonempty, closed and convex subset of $\VV$.
For every vector $\bx \in \VV$, a vector $\bz \in C$ is
its projection if and only if

$$
\langle \by - \bz, \bx - \bz \rangle \leq 0 \Forall \by \in C.
$$
```

This result is also known as the second projection theorem
{cite}`beck2014introduction`.

```{prf:proof}
Assume that for some $\bz \in C$,
$\langle \by - \bz, \bx - \bz \rangle \leq 0 \Forall \by \in C$ holds true.

1. For any $\by \in C$

   $$
   \| \by - \bx \|^2 &= \| (\by - \bz) - (\bx - \bz) \|^2 \\
   &= \| \by - \bz \|^2 + \| \bz - \bx \|^2 
   - 2 \langle \by - \bz, \bx - \bz \rangle \\
   &\geq  \| \bz - \bx \|^2 
   - 2 \langle \by - \bz, \bx - \bz \rangle.
   $$
1. Thus,

   $$
   \| by - \bx \|^2 \geq  \| \bz - \bx \|^2 \Forall \by \in C.
   $$
1. Thus, $\bz$ is indeed the projection of $\bx$ on $C$.


Conversely, assume that $\bz$ is the projection of $\bx$ on $C$.
1. Let $\by \in C$ be arbitrary. 
1. For any $t \geq 0$, define
   $\by_t = t \by + (1 -t ) \bz$.
1. Then, we have

   $$
   \| \bx - \by_t \|^2
   &= \| t \bx + (1-t) \bx + - t \by - (1 -t ) \bz \|^2 \\  
   &= \| t (\bx - \by) + (1- t) (\bx - \bz) \|^2\\
   &= t^2 \| \bx - \by \|^2  + (1-t)^2 \| \bx - \bz \|^2
   + 2 t (1-t) \langle \bx - \by, \bx - \bz \rangle. 
   $$
1. Viewing $\| \bx - \by_t \|^2$ as a function of $t$ and 
   differentiating w.r.t. $t$, we have

   $$
   \left . \frac{d}{d t} \| \bx - \by_t \|^2 \right |_{t = 0}
   &=  -2 \| \bx - \bz \|^2  + 2 \langle \bx - \by, \bx - \bz \rangle\\
   &= -2 \langle \bx  - \bz, \bx - \bz \rangle + 2 \langle \bx - \by, \bx - \bz \rangle\\
   &=  -2 \langle \by - \bz, \bx - \bz \rangle.
   $$
1. Since $t=0$ minimizes $\| \bx - \by_t \|^2$ over $t \in [0,1]$, we must have

   $$
   \left . \frac{d}{d t} \| \bx - \by_t \|^2 \right |_{t = 0} \geq 0.
   $$
1. Thus, we require that

   $$
   \langle \by - \bz, \bx - \bz \rangle \leq 0
   $$
   must hold true for every $\by \in C$.
```

Following is an alternative proof based on results
from {ref}`sec:opt:convex-differentiable-objective`.
This proof is specific to the case where $\VV = \RR^n$.

```{prf:proof}

Define a function $f: \RR^n \to \RR$ as

$$
f(\by) = \| \by - \bx \|^2.
$$

Then, the projection problem can be cast as an optimization problem

$$
& \text{minimize }  &  & f(\by) \\
& \text{subject to } & & \by \in C.
$$

Note that the gradient of $f$ is given by

$$
\nabla f (\by) = \nabla \langle \by - \bx, \by - \bx \rangle
= \nabla (\langle \by, \by \rangle - 2 \langle \by, \bx \rangle  + \langle \bx, \bx \rangle)
= 2 (\by - \bx).
$$

By {prf:ref}`res-cvxopt-diff-convex-optimal-criterion`, $\bz$ is an optimal solution
if and only if

$$
f(\bz)^T (\by - \bz) \geq 0 \Forall \by \in C.
$$

In other words

$$
2 (\bz - \bx)^T (\by - \bz) \geq 0 \Forall \by \in C.
$$
We can simplify this as

$$
\langle \bx - \bz, \by - \bz \rangle \leq 0 \Forall \by \in C.
$$
```

```{prf:theorem} Orthogonal projection on an affine subspace
:label: res-cvx-projection-affine-subspace

Let $C$ be an affine subspace of $\VV$.
Let $S$ be the linear subspace parallel to $C$.
For every vector $\bx \in \VV$, a vector $\bz \in C$ is
its projection if and only if

$$
\bx - \bz \in S^{\perp}.
$$
```

```{prf:proof}
Since $C$ is an affine subspace of $\VV$, hence
$C$ is nonempty, convex and closed (as $\VV$ is
finite dimensional).

1. By {prf:ref}`res-cvx-projection-characterization`, 
   $\bz$ is the projection of $\bx$ on $C$ if and only if
   for every $\by \in C$, we have

   $$
   \langle \by - \bz, \bx - \bz \rangle \leq 0.
   $$
1. But $\by \in C$ if and only if $\by - \bz \in S$.
1. Hence the condition is equivalent to

   $$
   \langle \bw, \bx - \bz \rangle \leq 0  \Forall \bw \in S.
   $$
1. But then, it must be an equality since $\bw$ and $-\bw$ both
   belong to $S$. Thus, we have

   $$
   \langle \bw, \bx - \bz \rangle = 0  \Forall \bw \in S.
   $$
1. In other words, $\bx - \bz \in S^{\perp}$.
```


## Distance Function

Recall that the distance of a point $\bx \in \VV$
from a set $C$ is defined as

$$
d_C(\bx) \triangleq \underset{\by \in C}{\inf} \| \bx - \by \|.
$$


```{prf:theorem} Distance function for nonempty, closed and convex set
:label: res-pocs-distance-func

Let $C$ be a nonempty, closed and convex subset of $\VV$.
Then the function $d_C : \VV \to \RR$ defining the
distance of a point $\bx \in \VV$ from the set $C$ satisfies

$$
d_C(\bx) = \| \bx - P_C(\bx) \|.
$$
```

```{prf:proof}
By {prf:ref}`res-pocs-projection-theorem`, there exists
a unique point $P_C(\bx)$ which minimizes the distance
between $\bx$ and $C$. Hence

$$
d_C(\bx) = \| \bx - P_C(\bx) \|
$$
must hold true.
```   

```{prf:theorem} Distance function for nonempty, closed and convex set is convex
:label: res-pocs-distance-func-convex

Let $C$ be a nonempty, closed and convex subset of $\VV$.
Let $d_C : \VV \to \RR$ be the distance to the set $C$
function as defined in {prf:ref}`res-pocs-distance-func`.
Then, $d_C$ is convex.
```

```{prf:proof}
Assume, for contradiction, that $d_C$ is not convex.

1. Then, there exist $\bx, \by \in \VV$ and $t \in (0,1)$ such that
   
   $$
   d_C(t \bx + (1-t) \by) > t d_C(\bx) + (1-t)d_C(\by).
   $$
1. Let $\bu = P_C(\bx)$ and $\bv = P_C(\by)$.
   By definition, $\bu, \bv \in C$.
1. Then, 

   $$
   t d_C(\bx) + (1-t)d_C(\by) = t \| \bu - \bx \| + (1-t) \| \bv - \by \|.
   $$
1. Since $C$ is convex, hence, $t \bu + (1-t) \bv \in C$.
1. Since, $d_C(t \bx + (1-t) \by)$ minimizes the distance of $C$ from
   the point $t \bx +  (1-t) \by$, hence

   $$
   \| t \bu + (1-t) \bv - t \bx -  (1-t) \by \| \geq d_C(t \bx + (1-t) \by).
   $$
1. Rewriting, 

   $$
   d_C(t \bx + (1-t) \by) \leq \| t (\bu - \bx) + (1-t) (\bv - \by) \|
   \leq t \| \bu - \bx \| + (1-t) \| \bv - \by \|
   $$
   due to triangle inequality.
1. But, this leads to the contradiction

   $$
   t \| \bu - \bx \| + (1-t) \| \bv - \by \| < d_C(t \bx + (1-t) \by)
   \leq t \| \bu - \bx \| + (1-t) \| \bv - \by \|.
   $$
1. Hence, $d_C$ must be convex.
```


## Nonexpansiveness 

```{prf:definition} Nonexpansiveness property
:label: def-opt-nonexpansiveness-property

Let $\VV$ be a normed linear space.
An operator $T : \VV \to \VV$ is called *nonexpansive* if

$$
\| T (\bx)  - T (\by) \| \leq \| \by - \bx \| \Forall \bx, \by \in \VV.
$$
In other words, the distance between mapped points in $\VV$ is always
less than or equal to the distance between original points in $\VV$.
```

```{prf:theorem} Nonexpansive operators are Lipschitz continuous
:label: res-opt-nonexpansive-continuous

Let $\VV$ a be normed linear space.
A nonexpansive operator $T : \VV \to \VV$ is Lipschitz continuous.
Hence, it is uniformly continuous.
```

```{prf:proof}
Recall from {prf:ref}`def-ms-lipschitz-func` that
if $T$ is a Lipschitz map, then there exists $L > 0$ such that

$$
\| T (\bx) - T (\by) \| \leq L \| \bx - \by \|
$$
for every $\bx, \by \in \VV$.

For a nonexpansive operator, such $L = 1$. 
This $T$ is indeed Lipschitz continuous. 
By {prf:ref}`res-ms-lipschitz-to-uniform-cont`, every
Lipschitz continuous function is uniformly continuous.
```

```{prf:definition} Firm nonexpansiveness property
:label: def-opt-firm-nonexpansiveness-property

Let $\VV$ be a real inner product space.
An operator $T : \VV \to \VV$ is called *firmly nonexpansive* if

$$
\langle T(\bx) - T(\by), \bx- \by \rangle \geq 
\| T(\bx) - T (\by) \|^2
$$
holds true for every $\bx, \by \in \VV$.
```

```{prf:theorem} A firmly nonexpansive operator is nonexpansive
:label: res-opt-firm-nonexpansive-is-nonexpansive

Let $\VV$ be a real inner product space.
Let $T : \VV \to \VV$ be a firmly nonexpansive operator.
Then, $T$ is nonexpansive.
```

```{prf:proof}

For every $\bx, \by \in \VV$, we have

$$
\| T(\bx) - T (\by) \|^2 \leq \langle T(\bx) - T(\by), \bx- \by \rangle.
$$

Applying Cauchy Schwartz inequality on R.H.S., we get

$$
\| T(\bx) - T (\by) \|^2 \leq \| T(\bx) - T(\by) \| \| \bx- \by \|.
$$

Canceling terms, we get:

$$
\| T(\bx) - T (\by) \| \leq \| \bx- \by \|
$$
which is the nonexpansive property.
```


```{prf:theorem} Orthogonal projection is nonexpansive
:label: res-opt-pocs-nonexpansiveness

Let $C$ be a nonempty, closed and convex subset of $\VV$.
Let $P_C : \VV \to \VV$ be the orthogonal projection operator
as defined in {prf:ref}`def-pocs-projection-mapping` is nonexpansive
(and therefore continuous).

In other words,

$$
\| P_C (\bx)  - P_C (\by) \| \leq \| \by - \bx \| \Forall \bx, \by \in \VV.
$$
```

```{prf:proof}
Let $\bx, \by \in \VV$.

1. By {prf:ref}`res-cvx-projection-characterization`, 

   $$
   \langle \bw - P_C(\bx), \bx - P_C(\bx) \rangle \leq 0 \Forall \bw \in C.
   $$
1. In particular $P_C(\by) \in C$. Hence,

   $$
   \langle P_C(\by) - P_C(\bx), \bx - P_C(\bx) \rangle \leq 0.
   $$
1. Similarly, starting with $P_C(\bx)$, we obtain

   $$
   \langle P_C(\bx) - P_C(\by), \by - P_C(\by) \rangle \leq 0.
   $$
1. Adding these two inequalities, we obtain

   $$
   \langle P_C(\by) - P_C(\bx), \bx - P_C(\bx) - \by + P_C(\by) \rangle \leq 0.
   $$
1. By rearranging the terms, we get


  $$
  \langle P_C(\by) - P_C(\bx), P_C(\by) - P_C(\bx) \rangle 
  \leq   \langle P_C(\by) - P_C(\bx), \by - \bx \rangle. 
  $$
1. Applying the Cauchy Schwartz inequality on the R.H.S., we obtain

  $$
  \| P_C(\by) - P_C(\bx) \|^2 \leq \| P_C(\by) - P_C(\bx) \| \| \by - \bx \|.
  $$
1. Thus, $P_C$ is nonexpansive.
1. Since $P_C$ is nonexpansive, hence $P_C$ is continuous also.
```


```{prf:theorem} Orthogonal projection is firmly nonexpansive
:label: res-opt-pocs-firm-nonexpansiveness

Let $C$ be a nonempty, closed and convex subset of $\VV$.
Let $P_C : \VV \to \VV$ be the orthogonal projection operator
as defined in {prf:ref}`def-pocs-projection-mapping`.
Then $P_C$ is a firmly nonexpansive operator.

In other words,

$$
\langle P_C(\bx) - P_C(\by), \bx- \by \rangle \geq 
\| P_C(\bx) - P_C (\by) \|^2
$$
holds true for every $\bx, \by \in \VV$.
```

```{prf:proof}
Recall from {prf:ref}`res-cvx-projection-characterization` that
for any $\bu \in \VV$ and $\bv \in C$

$$
\langle \bv - P_C(\bu), \bu - P_C(\bu) \rangle \leq 0.
$$

1. Substituting $\bu = \bx$ and $\bv = P_C(\by)$, we obtain

   $$
   \langle P_C(\by) - P_C(\bx), \bx - P_C(\bx) \rangle \leq 0.
   $$
1. Substituting $\bu = \by$ and $\bv = P_C(\bx)$, we obtain

   $$
   \langle P_C(\bx) - P_C(\by), \by - P_C(\by) \rangle \leq 0.
   $$
1. Adding the two inequalities gives us

   $$
   & \langle P_C(\bx) - P_C(\by), \by - P_C(\by) - \bx + P_C(\bx) \rangle \leq 0 \\
   & \iff \langle P_C(\bx) - P_C(\by), (\by  - \bx) + (P_C(\bx) - P_C(\by)) \rangle \leq 0\\
   &\iff \| P_C(\bx) - P_C(\by) \|^2 \leq \langle P_C(\bx) - P_C(\by), \bx - \by \rangle
   $$
   as desired.
```

## Squared Distance Function

```{prf:definition} Squared distance function to a nonempty set
:label: def-pocs-sq-dist-set

Let $C$ be a nonempty subset of $\VV$.
The squared distance to set $C$ function
denoted as $\varphi_C : \VV \to \RR$ is defined as:

$$
\varphi_C(\bx) \triangleq \frac{1}{2} d_C^2(\bx). 
$$

We also define $\psi_C : \VV  \to \RR$ as:

$$
\psi_C(\bx) \triangleq \frac{1}{2} \left (\| \bx \|^2 - d_C^2(\bx) \right). 
$$
```

```{prf:theorem} Expression for $\psi_C$
:label: res-pocs-sq-psi-c-expression

Let $C$ be a nonempty subset of $\VV$.
Then, the function $\psi_C$ as defined in {prf:ref}`def-pocs-sq-dist-set`
is given by

$$
\psi_C(\bx) 
= \underset{\by \in C}{\sup}
\left [ \langle \by, \bx \rangle - \frac{1}{2} \| \by \|^2 \right ].
$$
```

```{prf:proof}
We proceed as follows.

1. Expanding on the definition of $d_C^2$

   $$
   d_C^2(\bx) &= \inf_{\by \in C} \| \bx - \by \|^2 \\
   &= \inf_{\by \in C} \langle \bx - \by, \bx - \by \rangle \\
   &= \inf_{\by \in C} (\| \bx \|^2 - 2 \langle \bx, \by \rangle + \| \by \|^2) \\
   &= \inf_{\by \in C} (\| \bx \|^2 - (2 \langle \bx, \by \rangle - \| \by \|^2)) \\
   &= \| \bx \|^2 -  \sup_{\by \in C} (2 \langle \bx, \by \rangle - \| \by \|^2).
   $$
1. Thus,

   $$
   \| \bx \|^2 - d_C^2 (\bx) = 
   \sup_{\by \in C} ( 2 \langle \bx, \by \rangle - \| \by \|^2 ).
   $$
1. Thus,

   $$
   \psi_C(\bx) = \frac{1}{2} \left (\| \bx \|^2 - d_C^2(\bx) \right)
   = \sup_{\by \in C} \left [\langle \bx, \by \rangle - \frac{1}{2} \| \by \|^2 \right ].
   $$
```


```{prf:theorem} $\psi_C$ is convex
:label: res-pocs-sq-psi-c-is-convex

Let $C$ be a nonempty subset of $\VV$.
Then, the function $\psi_C$ as defined in {prf:ref}`def-pocs-sq-dist-set`
is convex.
```
Beauty of this result is the fact that $\psi_C$ is convex
irrespective of whether $C$ is convex or not.

```{prf:proof}
We proceed as follows.

1. For every $\by \in C$, the function $g_y : \VV \to \RR$,
   given by

   $$
   g_y (\bx) = \langle \by, \bx \rangle - \frac{1}{2} \| \by \|^2
   $$
   is an affine function.
1. $g_y$ is convex for every $\by \in C$
   due to {prf:ref}`res-cvxf-affine-functional-convex`.
1. Now, 

   $$
   \psi_C (\by) = \sup{\by \in C} g_y.
   $$
1. Thus, $\psi_C$ is a pointwise supremum of convex functions.
1. Thus, by {prf:ref}`res-cvx-ptws-supremum`, $\psi_C$ is convex.
```

```{prf:theorem} Squared distance function for nonempty, closed and convex sets
:label: res-pocs-sq-dist-closed-convex

Let $C$ be a nonempty, closed and convex subset of $\VV$.
Then, the squared distance function $\varphi_C$ is given by

$$
\varphi_C(\bx) = \frac{1}{2}\| \bx - P_C(\bx) \|^2.
$$
```

This follows directly from {prf:ref}`res-pocs-distance-func-convex`.

## Gradients and Subgradients

```{prf:theorem} Gradient of the squared distance function
:label: res-pocs-grad-sq-dist-func

Let $C$ be a nonempty, closed and convex subset of $\VV$.
The gradient of the squared distance function $\varphi_C$
as defined in {prf:ref}`def-pocs-sq-dist-set`
at $\bx \in \VV$ is given by:

$$
\nabla \varphi_C(\bx) = x - P_C(\bx)  \Forall \bx \in \VV.
$$
```

```{prf:proof}
We proceed as follows.

1. Let $\bx \in \VV$.
1. Let $\bz_x = \bx - P_C(\bx)$.
1. Consider the function 

   $$
   g_x(\bd) = \varphi_C(\bx + \bd) - \varphi_C(\bx) - \langle \bd, \bz_x \rangle.
   $$
1. If 

   $$
   \lim_{\bd \to \bzero} \frac{g_x(\bd)}{ \| \bd \|} = 0
   $$
   then $\bz_x$ is indeed the gradient of $\varphi_C$ at $\bx$.
1. By definition of orthogonal projection, for any $\bd \in \VV$,

   $$
   \| \bx + \bd - P_C(\bx + \bd) \|^2 
   \leq \| \bx + \bd - P_C(\bx) \|^2
   $$
   as $P_C(\bx + \bd)$ is the nearest point to $\bx + \bd$ 
   in $C$. $P_C(\bx)$ is just another point in $C$.

1. Thus, for any $\bd \in \VV$

   $$
   g_x(\bd) 
   &= \varphi_C(\bx + \bd) - \varphi_C(\bx) - \langle \bd, \bz_x \rangle \\
   &= \frac{1}{2} \| \bx + \bd - P_C(\bx + \bd) \|^2
   - \frac{1}{2} \| \bx - P_C(\bx) \|^2
   - \langle \bd, \bz_x \rangle \\
   &\leq \frac{1}{2} \| \bx + \bd - P_C(\bx) \|^2
   - \frac{1}{2} \| \bx - P_C(\bx) \|^2
   - \langle \bd, \bz_x \rangle.
   $$
1. Recall that for a norm induced by the inner product

   $$
   \| \ba + \bb \|^2 = \langle \ba + \bb, \ba + \bb \rangle
   = \| \ba \|^2 + 2 \langle \ba, \bb \rangle + \| \bb \|^2.
   $$
1. Thus, 

   $$
   \| \bx + \bd - P_C(\bx)\|^2 
   &= \| \bd + (\bx - P_C(\bx)) \|^2\\
   &= \| \bd \|^2 + \| \bx - P_C(\bx)\|^2 + 
   2 \langle \bd, \bx - P_C(\bx) \rangle.
   $$
1. Putting it back and simplifying, we obtain

   $$
   g_x(\bd) \leq \frac{1}{2}\| \bd \|^2 + \langle \bd, \bx - P_C(\bx)\rangle
   - \langle \bd, \bz_x \rangle
   = \frac{1}{2}\| \bd \|^2.
   $$
1. Proceeding similarly, we also have

   $$
   g_x(-\bd) \leq \frac{1}{2}\| \bd \|^2.
   $$
1. Since $\varphi_C$ is convex, hence $g_x$ is also convex.
1. Thus,

   $$
   0 = g_x(\bzero) =  g_x \left (\frac{1}{2} \bd + \frac{1}{2} (-\bd)  \right )
   \leq \frac{1}{2} g_x(\bd) + \frac{1}{2} g_x(-\bd).
   $$
1. Thus,

   $$
   g_x(\bd) \geq - g_x(-\bd) \geq - \frac{1}{2}\| \bd \|^2.
   $$
1. Combining, we have

   $$
   - \frac{1}{2}\| \bd \|^2 \leq g_x(\bd) \leq \frac{1}{2}\| \bd \|^2.
   $$
1. Or, in terms of absolute values.

   $$
   |g_x(\bd)| \leq \frac{1}{2}\| \bd \|^2.
   $$
1. Then, 

   $$
   \frac{|g_x(\bd)|}{\| \bd \|} \leq \frac{1}{2}\| \bd \|.
   $$
1. Thus, 

   $$
   \lim_{\bd \to \bzero} \frac{g_x(\bd)}{ \| \bd \|} = 0
   $$
1. Thus, $\bz_x = \bx - P_C(\bx)$ is indeed the gradient
   of $\varphi_C$ at $\bx$.
```





The gradient of $\psi_C$ is given by:

$$
\nabla \psi_C(\bx) = P_C(\bx).
$$


```{prf:remark} Distance function and square distance function relation
:label: rem-pocs-dist-sq-dist-relation

We note that $\varphi_C = g \circ d_C$ where 
$g(t) = \frac{1}{2}[t]_+^2$.

$g$ is a nonincreasing real-valued convex differentiable function.
We also note that 

$$
g'(t) = 2 [t]_+.
$$
```

```{prf:theorem} Subdifferential of the distance function
:label: res-pocs-subdiff-dist-func

Let $C$ be a nonempty, closed and convex subset of $\VV$.
The subdifferential of the distance function $d_C$ is given
by

$$
\partial d_C (\bx) = \begin{cases} 
 \left \{ \frac{\bx - P_C(\bx)}{d_C(\bx)}\right \}, & \bx \notin C\\
N_C(\bx) \cap B[\bzero, 1], & \bx \in C
\end{cases}.
$$
$N_C(\bx)$ denotes the {prf:ref}`normal cone <def-cvx-normal-cone>`
of all vectors normal to the set $C$ at a point $\bx \in C$.

Since $\partial d_C$ is a singleton for $\bx \notin C$,
hence $d_C$ is differentiable at $\bx \notin C$.
```

```{prf:proof}
We can get the subdifferentials for $d_C$ by applying the chain rule.

1. Recall that $\varphi_C = g \circ d_C$ where $g(t) = \frac{1}{2}[t]_+^2$.
1. Thus, by subdifferential chain rule  ({prf:ref}`res-cvxf-subdiff-chain-rule`):

   $$
   \partial \varphi_C (\bx) = g'(d_C(\bx)) \partial d_C(\bx)
   = [d_C(\bx)]_+ \partial d_C(\bx)
   = d_C(\bx) \partial d_C(\bx).
   $$
   We used the fact that $d_C$ is nonnegative.
1. Since $\varphi_C$ is differentiable, hence $\partial \varphi_C(\bx) = \{\bx - P_C(\bx) \}$.
1. If $\bx \notin C$, then, $d_C(\bx) > 0$. 
1. Thus, for $\bx \notin C$

   $$
   \partial d_C(\bx) = \left \{ \frac{\bx - P_C(\bx)}{d_C(\bx)} \right \}.
   $$
1. For $\bx \in C$, $d_C(\bx) = 0$.
1. We need to show that $\partial d_C(\bx) = N_C(\bx) \cap B[\bzero, 1]$ in this case.
1. Consider any $\bd \in \partial d_C(\bx)$.
1. Then, by subgradient inequality

   $$
   d_C(\by) \geq d_C(\bx) + \langle \by - \bx, \bd \rangle
   = \langle \by - \bx, \bd \rangle  \Forall \by \in \VV
   $$
   since $d_C(\bx) = 0$.
1. Then, in particular, for any $\by \in C$
   
   $$
   d_C(\by) = 0  \geq \langle \by - \bx, \bd \rangle.
   $$
1. Thus, $\bd \in N_C(\bx)$.
```

## Conjugates

```{div}

Let $f : \VV \to \RERL$ be:

$$
f(\bx) = \frac{1}{2} \| \bx \|^2 + \delta_C(\bx).
$$

Then, its conjugate is:

$$
f^*(\by) = \frac{1}{2}\| \by \|^2 - \frac{1}{2} d_C^2 (\by) = \psi_C(\by).
$$
```

## Smoothness 

The function $\varphi_C = \frac{1}{2} d_C^2$ is 1-smooth.

The function $\psi_C$ is also 1-smooth.



## POCS Problems

In this section, we present some example optimization
problems which can be converted into an equivalent
projection on a convex set problem.

### Equality Constrained Quadratic Programming

Quadratic programming problems are discussed extensively
in {ref}`sec:opt:quadratic-programming`. 
Here we discuss a specific form of minimizing a quadratic
function subject to linear equality constraints.

```{prf:example} Equality constrained quadratic programming

We consider the quadratic programming problem 

$$
& \text{minimize }   & & \frac{1}{2} \| \bx \|^2 + \bc^T \bx \\
& \text{subject to } & & \bA \bx = \bzero.
$$

where
1. $\bx \in \RR^n$ is the optimization variable.
1. $\bc \in \RR^n$ is a given vector.
1. $\bA \in \RR^{m \times n}$ is an $m \times n$ matrix of rank $m$.
   Assume that $m < n$.

We proceed towards converting this problem into a
projection on a convex set problem as follows.

1. By adding a constant term $\frac{1}{2} \| \bc \|^2$ to the
   objective function, we obtain an equivalent problem.

   $$
   & \text{minimize }   & & \frac{1}{2} \| \bc + \bx \|^2 \\
   & \text{subject to } & & \bA \bx = \bzero.
   $$
1. The set $C = \{ \bx \ST \bA \bx = \bzero \}$ is the
   null space of the matrix $\bA$ which is linear subspace,
   hence a nonempty, closed and convex set.
1. Minimizing $\frac{1}{2} \| \bc + \bx \|^2$ is
   equivalent to minimizing $\| (-\bc) - \bx \|$ subject to
   $\bx \in C$.
1. $\| (-\bc) - \bx \|$ is $d(-\bc, \bx)$, the distance
   between $-\bc$ and a point $\bx$.
1. Thus, we are minimizing the distance of the point $-\bc$
   among $\bx \in C$.
1. This is nothing but the distance of $-\bc$ from the set $C$.
1. Since, $C$ is nonempty, close and convex, hence, there is
   a unique $\bx^*$ which minimizes the distance due to
   the {prf:ref}`projection theorem <res-pocs-projection-theorem>`.
1. Thus, the solution is the projection of the vector $-\bc$
   on the subspace $C$.
1. By {prf:ref}`res-cvx-projection-affine-subspace`, $\bx^*$
   is the unique projection of $-\bc$ on $C$ if and only if
   $-\bc - \bx^* \in C^{\perp}$. 
1. In other words,
   $$
   \langle \bc + \bx^*, \bx \rangle  = 0 \Forall \bx \in C. 
   $$
1. A closed form solution to this problem does exist
   given by

   $$
   \bx^* = - (\bI - \bA^T (\bA \bA^T)^{-1} bA) \bc.
   $$
1. It is indeed the unique solution to this quadratic programming
   problem.
```



