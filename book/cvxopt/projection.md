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
as defined in {prf:ref}`def-pocs-projection-mapping` is firmly nonexpansive.

In other words,

$$
\langle P_C(\bx) - P_C(\by), \bx- \by \rangle \geq 
\| P_C(\bx) - P_C (\by) \|^2
$$
holds true for every $\bx, \by \in \VV$.
```


## Squared Distance Function

```{prf:definition} Squared distance function to a nonempty, closed and convex set
:label: def-pocs-sq-dist-closed-convex-set

Let $C$ be a nonempty, closed and convex subset of $\VV$.
The squared distance to set $C$ function
denoted as $\varphi_C : \VV \to \RR$ is defined as:

$$
\varphi_C(\bx) \triangleq \frac{1}{2} d_C^2(\bx) 
= \frac{1}{2}\| \bx - P_C(\bx) \|^2.
$$

We also define $\psi_C : \VV  \to \RR$ as:

$$
\psi_C(\bx) \triangleq \frac{1}{2} \left (\| \bx \|^2 - d_C^2(\bx) \right) 
= \underset{\by \in C}{\sup}\left [ \langle y, x \rangle - \frac{1}{2} \| y \|^2 \right ]. 
$$
```

```{prf:theorem}
:label: res-pocs-sq-proj-is-convex

Let $C$ be a nonempty, closed and convex subset of $\VV$.
Then, the function $\psi_C$ as defined in {prf:ref}`def-pocs-sq-dist-closed-convex-set`
is convex.
```



## Gradients and Subgradients

The gradient of $\varphi_C$ is given by:

$$
\nabla \varphi_C(\bx) = \bx - P_C(\bx)  \Forall \bx \in \VV.
$$

The gradient of $\psi_C$ is given by:

$$
\nabla \psi_C(\bx) = P_C(\bx).
$$


```{div}
We note that $\varphi_C = g \circ d_C$ where 
$g(t) = \frac{1}{2}[t]_+^2$.

We can get the subdifferentials for $d_C$ by applying the chain rule.

$d_C$ is differentiable at $\bx \notin C$.

$$
\partial d_C (\bx) = \begin{cases} 
 \left \{ \frac{\bx - P_C(\bx)}{d_C(\bx)}\right \}, & \bx \notin C\\
N_C(\bx) \cap B[\bzero, 1], & \bx \in C
\end{cases}.
$$
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



