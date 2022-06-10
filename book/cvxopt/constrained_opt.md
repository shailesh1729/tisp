# Constrained Optimization II


In this section, we present several results
for the general problem of optimizing
a cost function over a constraint set.

Throughout this section, we assume that
$\VV$ is an $n$-dimensional real vector space
endowed with an inner product
$\langle \cdot, \cdot \rangle : \VV \times \VV \to \RR$
and a norm $\| \cdot \| : \VV \to \RR$.


## General Constrained Optimization

````{div}
Let $f : \VV \to \RERL$ be a proper function
with $S = \dom f$.
Let $C \subseteq \VV$ be a nonempty set.

We are concerned with the optimization problems
of the form

```{math}
:label: eq-cvx-const-cvx-opt-form
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C.
```
````

We provide optimality conditions for three specific type of problems.

1. A continuously differentiable function $f$ over an arbitrary
   constraint set $C$.
1. A convex, possibly nonsmooth, cost function $f$ and a convex
   constraint set $C$.
1. A cost function consisting of the sum of a smooth (continuously differentiable)
   function and a convex function and an arbitrary constraint set.

For the development of the results in this section, we will
need the supporting machinery of the following notions:

* Feasible directions and the cone of feasible directions
* Tangent directions and tangent cone
* Normal directions and normal cone

For a nonconvex optimization problem, the optimality
conditions provide the necessary conditions for a
feasible point to be a local optimal solution.

For convex problems, the optimality conditions
provide the necessary and sufficient conditions
for a feasible point to be a global optimal solution.

## Feasible Directions

At any point in the constraint set $C$, a feasible
direction is a direction along which if we move slightly,
then we can stay within $C$.

```{index} Feasible direction
```
```{prf:definition} Feasible direction
:label: def-opt-feasible-direction

Consider the optimization problem {eq}`eq-cvx-const-cvx-opt-form`.
Given a vector $\bx \in C$, a direction $\bd \in \VV$
is said to be a *feasible direction* of $C$ at $\bx$ if
there exists a $\overline{t} > 0$ such that

$$
\bx + t \bd \in C \text{ for every } t \in [0, \overline{t}].
$$ 
The set of all feasible directions of $C$ at $\bx$ is
denoted by $F_C(\bx)$.
```

```{prf:observation} The cone of feasible directions
:label: res-opt-feasible-dir-set-cone

The set of feasible directions at $\bx$ is a cone.

1. We can see that $\bzero \in F_C(\bx)$.
1. Also, if $\bd \in F_C(\bx)$ then for any $r > 0$,
   $r \bd \in F_C(\bx)$ also holds true.
```

### Convexity

```{prf:theorem} Convexity of the cone of feasible directions
:label: res-opt-feasible-cone-convexity

Let $C$ be a nonempty subset of $\VV$. 
Let $\bx \in C$.
If $C$ is convex then $F_C(\bx)$ is convex.
```

```{prf:proof}
We are given that $C$ is convex.

1. For any point $\by \in C$, the line segment $[\bx, \by] \in C$.
1. Hence the set $F_C(\bx)$ consists of all the vectors of the
   form $t(\by - \bx)$ where $t > 0$ and $\by \in C$.
1. Let $\bd_1, \bd_2 \in F_C(\bx)$ and $r \in (0,1)$.
1. Then there exist $\by_1, \by_2 \in C$ and $t_1, t_2 > 0$ such that
   
   $$
   \bd_1 = t_1 (\by_1 - \bx),
   \bd_2 = t_2 (\by_2 - \bx).
   $$ 
1. Then 

   $$
   \bd = r \bd_1 + (1-r) \bd_2
   &=  r t_1 (\by_1 - \bx) + (1 - r) t_2 (\by_2 - \bx) \\
   &= (r t_1 + (1-r) t_2)
   \left (\frac{r t_1}{r t_1 + (1-r) t_2} \by_1
   + \frac{ (1- r) t_2}{r t_1 + (1-r) t_2} \by_2 - \bx \right ).
   $$
1. Let $s = \frac{r t_1}{r t_1 + (1-r) t_2}$.
1. Then $s \in (0, 1)$ and $1-s = \frac{ (1- r) t_2}{r t_1 + (1-r) t_2}$.
1. Hence $\by = s \by_1 + (1-s) \by_2 \in C$ due to convexity of $C$.
1. Hence $\bd = (r t_1 + (1-r) t_2) (\by - \bx)$.
1. Hence $\bd$ is a feasible direction.
1. Hence $F_C(\bx)$ is convex.
```


## Tangent Cones

### Tangent Direction

```{index} Tangent direction
```
```{prf:definition} Tangent direction
:label: def-opt-tangent-direction

Let $C$ be a nonempty subset of $\VV$. 
Let $\bx \in C$. A vector $\bt \in \VV$
is called a *tangent* of $C$ at $\bx$
if either $\bt = \bzero$ or 
there exists a sequence $\{ \bx_k \}$
of $C$ such that $\bx_k \neq \bx$ 
for every $k$, and

$$
\bx_k \to \bx,
\frac{\bx_k - \bx}{ \| \bx_k - \bx\|} \to \frac{\bt}{\| \bt \|}.
$$
```

1. For a nonzero direction $\bt$, the term 
   $\frac{\bt}{\| \bt \|}$ is a *normalized direction*.
1. Since $\bx_k \neq \bx$ for every $k$, hence
   $\bx_k - \bx \neq \bzero$ for every $k$.
1. The term $\frac{\bx_k - \bx}{ \| \bx_k - \bx\|}$
   is also a normalized direction.
1. Hence the sequence $\{ \frac{\bx_k - \bx}{ \| \bx_k - \bx\|}\}$
   is a sequence of normalized directions.
1. Thus a nonzero direction $\bt$ is a tangent at $\bx$
   if it is possible to approach $\bx$ with a feasible
   sequence $\{ \bx_k \}$ such that the
   normalized direction sequence $\{ \frac{\bx_k - \bx}{ \| \bx_k - \bx\|} \}$
   converges to $\frac{\bt}{\| \bt \|}$.

### Tangent Cone

```{prf:theorem} The cone of tangent directions
:label: res-opt-tangent-set-cone

Let $C$ be a nonempty subset of $\VV$. 
Let $\bx \in C$.
The set of tangent directions of $C$ at $\bx$ is a cone.
```

```{prf:proof}
We can see that by definition $\bzero$ is a tangent direction.

1. Let $\bt \neq \bzero$ be a tangent direction.
1. Let $\alpha > 0$.
1. Then 

   $$
   \frac{\alpha \bt }{ \| \alpha \bt \|}
   = \frac{\bt}{ \| \bt \|}
   = \frac{\bx_k - \bx}{ \| \bx_k - \bx\|}
   $$
   for some sequence $\{ \bx_k \}$ converging to $\bx$
   with $\bx_k \neq \bx$ for every $k$.
1. Hence $\alpha \bt$ is also a tangent direction.
1. Hence the set of tangent directions is a cone.
```

```{index} Tangent cone
```
```{prf:definition} Tangent cone
:label: def-opt-tangent-cone

Let $C$ be a nonempty subset of $\VV$. 
Let $\bx \in C$.
The set of all tangent directions of $C$ at $\bx$
is called the *tangent cone* of $C$ at $\bx$
and is denoted by $T_C(\bx)$.
```

### Characterization

```{prf:theorem} Characterization of tangent directions
:label: res-opt-tangent-charac

Let $C$ be a nonempty subset of $\VV$. 
Let $\bx \in C$.
A vector $\bt \in \VV$ is a tangent of $C$ at $\bx$
if and only if there exists a sequence
$\{ \bx_k \}$ of $C$ and a positive scalar sequence
$\{ r_k \}$ such that $r_k \to 0$ and
$\frac{\bx_k - \bx}{r_k} \to \bt$.
```

```{prf:proof}
Let $\bt$ be a tangent of $C$ at $\bx$.

1. If $\bt = \bzero$, then we can take $\bx_k = \bx$ for every $k$
   and $r_k = \frac{1}{k}$ for every $k$.
1. Then $r_k \to 0$ and $\frac{\bx_k - \bx}{r_k} \to \bzero$.
1. Now consider the case where $\bt \neq \bzero$.
1. By definition of tangent, there exists a sequence
   $\{ \bx_k \}$ of $C$ with $\bx_k \neq \bx$,
   $\bx_k \to \bx$ and
   $\frac{\bx_k - \bx}{ \| \bx_k - \bx\|} \to \frac{\bt}{\| \bt \|}$.
1. Let $r_k = \frac{\| \bx_k - \bx \|}{\| \bt \|}$.
1. Clearly $r_k > 0$ and $r_k \to 0$ since $\bx_k \to \bx$.
1. Also 
   
   $$
   \frac{\bx_k - \bx}{r_k} = \| \bt \| \frac{\bx_k - \bx}{\| \bx_k - \bx \|}.
   $$
1. Since by definition of tangent

   $$
   \frac{\bx_k - \bx}{ \| \bx_k - \bx\|} \to \frac{\bt}{\| \bt \|},
   $$
   hence 

   $$
   \frac{\bx_k - \bx}{r_k} \to \bt
   $$
   as desired.

Conversely, suppose $\bt$ is such that there exist
sequences $\{ \bx_k \}$ and $\{ r_k \}$ with the given
properties.

1. If $\bt = \bzero$ then it is a tangent.
1. Now consider the case where $\bt \neq \bzero$
1. Since $r_k \to 0$ and $(\bx_k - \bx) / r_k \to \bt$
   hence we must have $\bx_k \to \bx$.
1. It is also possible to choose a subsequence of $\{ \bx_k \}$
   such that $\bx_{k_l} \neq \bx$ for every $k_l$.
   Otherwise, $(\bx_k - \bx) / r_k \to \bzero$ but we are given
   that $\bt \neq \bzero$.
1. WLOG assume that $\bx_k \neq \bx$ for every $k$.
1. Then 

   $$
   \frac{\bx_k - \bx}{ \| \bx_k - \bx\|}
   = \frac{(\bx_k - \bx) / r_k}{ \| \bx_k - \bx\| / r_k}
   \to \frac{\bt}{ \| \bt \|}.
   $$
1. Hence $\bt$ must be a tangent direction.
```

### Closedness

```{prf:theorem} Closedness of tangent cone
:label: res-opt-tangent-cone-closed

Let $C$ be a nonempty subset of $\VV$. 
Let $\bx \in C$.
Then $T_C(\bx)$ is closed.
```

```{prf:proof}
.

1. Let $\{ \bt_k \}$ be a sequence of $T_C(\bx)$
   such that $\lim \bt_k = \bt \in \VV$.
1. If $\bt = \bzero$, then $\bt \in T_C(\bx)$
   and we are done.
1. Hence consider the case where $\bt \neq \bzero$.
1. WLOG, assume that $\bt_k \neq \bzero$ for every $k$.
1. By the definition of the tangent, for every $k$,
   there is a sequence $\{ \bx_k^i \}$ of $C$
   with $\bx_k^i \neq \bx$ such that

   $$
   \lim_{i \to \infty} \bx_k^i = \bx,
   \lim_{i \to \infty}
   \frac{\bx_k^i - \bx}{\| \bx_k^i - \bx \|} = \frac{\bt_k}{\| \bt_k \|}.
   $$
1. For each $k$, choose and $i_k$ such that
   $i_1 < i_2 < \dots < i_k$ and

   $$
   \lim_{k \to \infty} \bx_k^{i_k} = \bx,
   \lim_{k \to \infty}
   \left \| \frac{\bx_k^{i_k} - \bx}{\| \bx_k^{i_k} - \bx \|}  - \frac{\bt_k}{\| \bt_k \|}
   \right \|.
   $$
1. For all $k$, we have

   $$
   \left \| \frac{\bx_k^{i_k} - \bx}{\| \bx_k^{i_k} - \bx \|}  - \frac{\bt}{\| \bt \|}
   \right \|
   \leq    \left \| \frac{\bx_k^{i_k} - \bx}{\| \bx_k^{i_k} - \bx \|}  - \frac{\bt_k}{\| \bt_k \|}
   \right \|
   + \left \|
   \frac{\bt_k}{\| \bt_k \|} - \frac{\bt}{\| \bt \|}
   \right \|.
   $$
1. Taking the limit of $k \to \infty$, we have

   $$
   \left \| \frac{\bx_k^{i_k} - \bx}{\| \bx_k^{i_k} - \bx \|}  - \frac{\bt}{\| \bt \|}
   \right \| = 0.
   $$
1. Hence $\by \in T_C(\bx)$.
```

### Feasible Directions and Tangent Cone


```{prf:theorem} Feasible cone and tangent cone
:label: res-opt-feasible-tangent-cone

Let $C$ be a nonempty subset of $\VV$. 
Let $\bx \in C$.
The following hold true regarding the
cone of feasible directions $F_C(\bx)$
and the tangent cone $T_C(\bx)$.

1. $F_C(\bx) \subseteq T_C(\bx)$.
1. $\closure F_C(\bx) \subseteq T_C(\bx)$.
1. If $C$ is convex, then

   $$
   \closure F_C(\bx) = T_C(\bx).
   $$
```
```{prf:proof}
(1) Every feasible direction is a tangent direction.

1. Let $\bd$ be a feasible direction.
1. Then there exists a $\overline{t} > 0$ such that

   $$
   \bx + t \bd \in C \Forall t \in [0, \overline{t}].
   $$
1. Let $r_k = \frac{\overline{t}}{k}$ for every $k \in \Nat$.
1. Then $r_k > 0$ for every $k$ and $r_k \to 0$.
1. Let $\bx_k = \bx + r_k \bd$.
1. Then $\bx_k \in C$, $\bx_k \neq \bx$ for every $k$ and $\bx_k \to \bx$.
1. Also $\frac{\bx_k - \bx}{r_k} = \bd$ for every $k$.
1. Hence $\frac{\bx_k - \bx}{r_k} \to \bd$.
1. Hence $\bd$ is a tangent direction due to
   {prf:ref}`res-opt-tangent-charac`.
1. Hence $F_C(\bx) \subseteq T_C(\bx)$.

(2) Closure

1. By {prf:ref}`res-opt-tangent-cone-closed`, $T_C(\bx)$ is closed.
1. We have shown that $F_C(\bx) \subseteq T_C(\bx)$.
1. The closure of a set is the smallest closed set containing it.
1. Hence $\closure F_C(\bx) \subseteq T_C(\bx)$.

(3) Convexity and Closure

1. We are given that $C$ is convex.
1. By claim (2), we have $\closure F_C(\bx) \subseteq T_C(\bx)$.
1. It will suffice to show the reverse inclusion
   $T_C(\bx) \subseteq \closure F_C(\bx)$.
1. Let $\bd \in T_C(\bx)$.
1. By {prf:ref}`res-opt-tangent-charac`, there exists a sequence
   $\{ \bx_k \}$ of $C$ with $\bx_k \to \bx$ and a positive scalar
   sequence $\{ r_k \}$ with $r_k \to 0$ such that
   $\frac{\bx_k - \bx}{r_k} \to \bd$.
1. Since $C$ is convex, hence the direction $\frac{\bx_k - \bx}{r_k}$
   is a feasible direction of $C$ for every $k$.
1. Hence $\{\frac{\bx_k - \bx}{r_k} \}$ is a converging sequence
   of feasible directions.
1. Hence $\bd \in \closure F_C(\bx)$.
1. Hence $T_C(\bx) \subseteq \closure F_C(\bx)$. 
```

### Convexity

```{prf:theorem} Convexity of the tangent cone
:label: res-opt-tangent-cone-convexity

Let $C$ be a nonempty subset of $\VV$. 
Let $\bx \in C$.
If $C$ is convex then $T_C(\bx)$ is convex.
```

```{prf:proof}
.

1. By {prf:ref}`res-opt-feasible-cone-convexity`, $F_C(\bx)$ is convex.
1. By {prf:ref}`res-opt-feasible-tangent-cone`,

   $$
   T_C(\bx) = \closure F_C(\bx)
   $$
   since $C$ is convex.
1. By {prf:ref}`res-cvx-closure-convex-set-convex`, the
   closure of a convex set is convex.
1. Hence $T_C(\bx)$ is convex.
```

### Polar Cone of Tangent Cone

Recall from {prf:ref}`def-cvx-normal-cone`
that the normal cone to a set $C$ at a point $\ba \in C$
is given by

$$
N_C(\ba) = \{ \bv \in \VV^* \ST 
   \langle \bx - \ba , \bv \rangle \leq 0 
   \Forall \bx \in C \}.
$$

```{prf:theorem} Characterization of the polar cone of the tangent cone for a convex set
:label: res-opt-polar-tangent-cone-normal-cone

Let $C$ be a nonempty convex set.
Then for every $\bx \in C$, we have
$\bz \in T_C(\bx)^{\circ}$ if and only if

$$
\langle \by - \bx , \bz \rangle \leq 0 \Forall \by \in C.
$$

In particular, we have

$$
T_C(\bx)^{\circ} = N_C(\bx),
N_C(\bx)^{\circ} = T_C(\bx)
$$
where $N_C(\bx)$ is the normal cone of $C$ at $\bx$.
```

```{prf:proof}

First consider that $\bz \in T_C(\bx)^{\circ}$.



1. We note that $F_C(\bx) \subseteq T_C(\bx)$.
1. Since $C$ is convex, hence $\by - \bx \in F_C(\bx)$ for every $\by \in C$.
1. Hence $\by - \bx \in T_C(\bx)$ for every $\by \in C$.
1. Hence $\langle \by - \bx, \bz \rangle \leq 0$ for every $\by \in C$
   from the definition of the polar cone of $T_C(\bx)$.

Now assume that some $\bz \in \VV^*$ satisfies

$$
\langle \by - \bx , \bz \rangle \leq 0 \Forall \by \in C.
$$
1. For contradiction, assume that $\bz \notin T_C(\bx)^{\circ}$.
1. Then there exists some $\by \in T_C(\bx)$ such that
   $\langle \by, \bz \rangle > 0$.
1. Since $\closure F_C(\bx) = T_C(\bx)$, hence there exists
   a sequence $\{ \by_k \}$ of $F_C(\bx)$ such that $\by_k \to \by$.
1. $\by_k$ is a feasible direction at $\bx$ for every $k$.
1. Due to convexity of $C$, $\by_k = r_k (\bx_k - \bx)$ for every $k$
   where $\bx_k \in C$ and $r_k > 0$.
1. Since $\langle \by, \bz \rangle > 0$, hence
   for sufficiently large $k$, we should have
   $\langle \by_k, \bz \rangle > 0$.
1. In other words, for sufficiently large $k$, we have
   $r_k \langle \bx_k - \bx, \bz \rangle > 0$.
1. Since $r_k > 0$, hence it reduces to
   $\langle \bx_k - \bx, \bz \rangle > 0$.
1. But this is a contradiction to the hypothesis.
1. Hence we must have $\bz \in T_C(\bx)^{\circ}$.


This characterization of polar cone of tangent cone implies that

$$
T_C(\bx)^{\circ} = N_C(\bx).
$$

Since $T_C(\bx)$ is a closed and convex cone
for a convex $C$,
hence due to {prf:ref}`res-cvx-polar-cone-theorem`, we have

$$
N_C(\bx)^{\circ} = (T_C(\bx)^{\circ})^{\circ} = T_C(\bx).
$$
```


### Examples

```{prf:example} Tangent cone for a linear system of equations
:label: ex-opt-tangent-cone-linear-system


Let $C = \{ \bx \in \RR^n \ST \bA \bx =  \bb \}$
where $\bA \in \RR^{m \times n}$ and $\bb \in \RR^m$.


Since $C$ is convex, the strategy for computation of tangent cone
is as follows.

1. Identify the set of all feasible directions at the point.
1. Compute the closure of the set of feasible directions at the point.

We note that $C$ is an affine subspace.

1. Note that the subspace $L$ parallel to $C$ is given by

   $$
   L = \{ \bx \in \RR^n \ST \bA \bx =  \bzero \}.
   $$

1. Let $\bx \in C$.
1. Every direction in the subspace $L$ is a feasible direction.
   1. Let $\bd \in L$.
   1. Then $\bA (\bx + \bd) = \bb$.
   1. Hence $\bd$ is a feasible direction.
1. It is easy to see that there are no other feasible directions.
1. Hence $F_C(\bx) = L$.
1. Since $\RR^n$ is finite dimensional, hence $L$ is closed.
1. Since $T_C(\bx) = \closure F_C(\bx)$, hence
   $T_C(\bx) = L$.

```

```{prf:example} Tangent cone for an affine subspace
:label: ex-opt-tangent-cone-affine-subspace

Let $A \subseteq \VV$ be an affine subspace.

1. We note that $A$ is closed and convex.
1. Let $L$ be the linear subspace parallel to $A$.
1. Pick some $\bx \in A$.
1. Then for any $\bt \in L$, we have
   $\bx + \bt \in A$.
1. Hence every direction in $L$ is a feasible direction.
1. It is also easy to see that no other direction is a feasible direction.
1. Hence $F_C(\bx) = L$.
1. Since $T_C(\bx) = \closure F_C(\bx)$, hence
   $T_C(\bx) = L$.

The tangent cone at any point in an affine subspace
is the subspace parallel to the affine subspace.
```

```{prf:example} Tangent cone of a closed unit ball
:label: ex-opt-tangent-cone-unit-ball

Consider the set $C = B[\bzero, 1] \subseteq \VV$ given by

$$
B[\bzero, 1] = \{ \bx \ST \| \bx \| \leq 1  \}.
$$

Since $C$ is convex, the strategy for computation of tangent cone
is as follows.

1. Pick a point.
1. Identify the set of all feasible directions at the point.
1. Compute the closure of the set of feasible directions at the point.

There are two possible cases for the points in $C$
that require separate treatment.
1. $\bx \in \interior C$.
1. $\bx \in \boundary C$.

(1) Interior points

1. Let $\bx \in \interior C$.
1. Then it is easy to see that every direction is a feasible direction
   along which we can find another point in $C$.
1. Hence $F_C(\bx) = \VV$.
1. Then $T_C(\bx) = \closure F_C(\bx) = \VV$.


(2) Boundary points

1. Let $\bx \in \boundary C$.
1. We can see that only those directions are feasible that point
   towards some point in $C$. Any direction pointing towards
   the exterior of $C$ is not a feasible direction.
   1. The directions which make an acute angle with $\bx$
      point away from the ball.
   1. The directions which make an obtuse angle with $\bx$
      point inside the ball.
1. We shall now formally prove this.
1. Since $\bx \in \boundary C$, hence $\| \bx \| = 1$.
1. Let $\by \in F_C(\bx)$.
1. Then we must have $\bx + t \by \in C$ for sufficiently small
   $t > 0$.
1. Hence $\by \in F_C(\bx)$ if and only if there exists
   a $\overline{t} > 0$ such that for every $t \in (0, \overline{t}]$
   we have $\| \bx + t \by \| \leq 1$.
1. Expanding, we have

   $$
   \| \bx \|^2 + 2 t \langle \bx, \by \rangle + t^2 \| \by \|^2  \leq 1
   \Forall t \in (0, \overline{t}].
   $$
1. Since $\| \bx \| =1$, hence this reduces to

   $$
   2 t \langle \bx, \by \rangle + t^2 \| \by \|^2  \leq 0
   \Forall t \in (0, \overline{t}].
   $$
1. There are only two possibilities for this relation to hold true
   since $\| \by \| \geq 0$.
   1. Either $\by = \bzero$.
   1. Or $\langle \bx, \by \rangle < 0$ and
      $t \leq \frac{-2 \langle \bx, \by \rangle}{ \| \by \|^2}$.
   1. From the second case, we have 

      $$
      \overline{t} = \frac{-2 \langle \bx, \by \rangle}{ \| \by \|^2}.
      $$
1. Hence $F_C(\bx) = \{ \by \ST \langle \bx, \by  \rangle < 0 \} \cup \{ \bzero \}$.
1. From $T_C(\bx) = \closure F_C(\bx) = \VV$, we have

   $$
   T_C(\bx) = \{ \by \ST \langle \bx, \by  \rangle \leq 0 \}.
   $$
```


```{prf:example} Tangent cone of a closed half space
:label: ex-opt-tangent-cone-half-space

Consider the set $C \subseteq \VV$ given by

$$
C = \{ \bx \ST \langle \bx, \ba \rangle \leq b \}.
$$

There are two possible cases for the points in $C$:
1. $\bx \in \interior C$.
1. $\bx \in \boundary C$.

(1) Interior points

1. Let $\bx \in \interior C$.
1. Then it is easy to see that every direction is a feasible direction
   along which we can find another point in $C$.
1. Hence $F_C(\bx) = \VV$.
1. Then $T_C(\bx) = \closure F_C(\bx) = \VV$.

(2) Boundary points

1. Let $\bx \in \boundary C$.
1. Then we have $ \langle \bx, \ba \rangle = b$.
1. Let $\bd \in F_C(\bx)$.
1. This is equivalent to 
   
   $$
   \langle \bx + t \bd, \ba \rangle \leq b
   $$
   for some $t > 0$.
1. This is equivalent to $\langle \bd, \ba \rangle \leq 0$.
1. Hence

   $$
   F_C(\bx) = \{ \bd \ST \langle \bd, \ba \rangle \leq 0 \}.
   $$
1. This is also a closed half-space.
1. Hence $T_C(\bx) = \closure F_C(\bx) = F_C(\bx)$.
1. We can see that $T_C(\bx)$ is the closed half-space
   corresponding to the linear subspace parallel
   to the hyperplane 

   $$
   H = \{ \bx \ST \langle \bx, \ba \rangle = b \}
   $$
   given by

   $$
   L = \{ \bx \ST \langle \bx, \ba \rangle = 0 \}.
   $$
1. In other words,

   $$
   T_C(\bx) = C - \bz
   $$
   where $\bz \in H$.
```


## Optimality Conditions

### Minimization on an Arbitrary Constraint Set

When the constraint set is nonconvex, then the tangent cone
can be used as a suitable approximation to the constraint
set at the point of local optimality. The tangent cone
provides additional structure of being a cone and being
closed.

```{prf:theorem} Tangent cone and local optimality
:label: res-opt-tangent-cone-local-minimum

Let $f: \VV \to \RERL$ be a function with $S = \dom f$.
Let $\ba$ be a local minimum of $f$ over a subset $C$ of $S$.
Assume that $f$ is continuously differentiable over an open
set $O$ containing the local minimum $\ba$. Assume that $O \subseteq C$.
Then

$$
\langle \by, \nabla f(\ba) \rangle \geq 0, \Forall \by \in T_C(\ba).
$$

Equivalently, we must have

$$
- \nabla f(\ba) \in T_C(\ba)^{\circ};
$$
i.e., the negative of the gradient at the local minimum belongs to the
{prf:ref}`polar cone <def-cvx-polar-cone>`
of the tangent cone or the gradient at the local minimum belongs to the
{prf:ref}`dual cone <def-dual-cone>`
of the tangent cone.
```
This necessary condition means that the the value of function increases
along every tangent direction in its local neighborhood.

For a smooth $f: \VV \to \RR$ the condition simplifies as follows.
Let $\ba$ be a local minimum of $f$ over a subset $C$ of $\VV$.
Then

$$
\langle \by, \nabla f(\ba) \rangle \geq 0, \Forall \by \in T_C(\ba).
$$

```{prf:proof}
For the zero tangent direction at $\ba$,
the condition is met trivially.
Let $\bt$ be a nonzero tangent direction at $\ba$.

1. Then there exists a sequence $\{ \bx_k \}$ of $C$
   and a sequence $\{\br_k \}$ of $\VV$ such that
   $\bx_k \neq \ba$ for every $k$,
   $\br_k \to \bzero$, $\bx_k \to \ba$ and

   $$
   \frac{\bx_k - \ba}{\| \bx_k - \ba \|} =  \frac{\bt}{\| \bt \|} + \br_k.
   $$
   The term $\br_k$ is the residual between the $k$-th normalized direction
   and the normalized tangent direction.
1. WLOG assume that $\bx_k \in O \Forall k$. Otherwise drop finitely many
   terms from $\{ \bx_k \}$ to achieve this.
1. For every $k$, we have

   $$
   \bx_k - \ba = \frac{\| \bx_k - \ba \|}{\| \bt \|}(\bt + \| \bt \| \br_k).
   $$
1. Since $\bx_k \in O$ for every $k$, hence $f$ is continuously
   differentiable at every $\bx_k$ and at every point on the line
   segment $[\ba, \bx_k]$.
1. By mean value theorem, we have

   $$
   f(\bx_k) = f(\ba) + \langle \bx_k - \ba, \nabla f(\tilde{\bx}_k) \rangle
   $$
   where $\tilde{\bx}_k$ lies on the line segment $[\ba, \bx_k]$.
1. Since $\bx_k \to \ba$, hence $\tilde{\bx}_k \to \ba$ holds too.
1. Substituting for $\bx_k - \ba$, we get

   $$
   f(\bx_k)
   &= f(\ba) + \left \langle \frac{\| \bx_k - \ba \|}{\| \bt \|} \bt_k, 
   \nabla f(\tilde{\bx}_k) \right \rangle  \\
   &= f(\ba) +  \frac{\| \bx_k - \ba \|}{\| \bt \|} 
   \langle \bt_k , \nabla f(\tilde{\bx}_k) \rangle
   $$
   where $\bt_k = \bt + \| \bt \| \br_k$.
1. Note that $\bt_k \to \bt$ since $\br_k \to \bzero$.
1. Suppose for contradiction that $\langle \bt, \nabla f(\ba) \rangle < 0$.
1. Since $\tilde{\bx}_k \to \ba$ and $\bt_k \to \bt$, hence it follows that
   for all sufficiently large $k$, we have
   $\langle \bt_k, \nabla f(\tilde{\bx}_k) \rangle < 0$.
1. Hence, from the previous relation, we have
   $f(\bx_k) < f(\ba)$ for all sufficiently large $k$.
1. Thus contradictions the local optimality of $\ba$.
1. Hence we must have $\langle \bt, \nabla f(\ba) \rangle \geq 0$.

An equivalent statement is that

$$
\langle \by, -\nabla f(\ba) \rangle \leq 0, \Forall \by \in T_C(\ba).
$$
This means that $-\nabla f(\ba) \in T_C(\ba)^{\circ}$.
Since the polar cone is the negative of the dual cone, hence
$\nabla f(\ba) \in T_C(\ba)^*$.
```

```{prf:observation} Local minimum and descent directions
:label: res-opt-smooth-local-minimum-descent

Recall that a direction $\bd$ that satisfies
$\langle \bd, \nabla f(\ba) \rangle < 0$ is called a descent
direction at $\ba$. Recall from {prf:ref}`res-mvc-first-order-approx`
that

$$
f(\bx) = f(\ba) + \langle \bx - \ba, \nabla f(\ba) \rangle + o (\| \bx - \ba \|).
$$
Thus for some $\bx = \ba + t \bd$ where $t > 0$, we have

$$
f(\bx) = f(\ba) + t \langle \bd, \nabla f(\ba) \rangle + o (\| \bx - \ba \|).
$$
Hence for sufficiently small $t > 0$, we have $f(\bx) < f(\ba)$.

Thus, {prf:ref}`res-opt-tangent-cone-local-minimum` says that
if $\ba$ is a local minimum of $f$ over $C$, then there is
no descent direction within the tangent cone $T_C(\ba)$.
```


### Minimization on a Convex Constraint Set

```{prf:theorem} Local optimality with a convex constraint set
:label: res-opt-smooth-local-minimum-convex-const

Let $f: \VV \to \RERL$ be a function with $S = \dom f$.
Let $\ba$ be a local minimum of $f$ over a convex subset $C$ of $S$.
Assume that $f$ is continuously differentiable over an open
set $O$ containing the local minimum $\ba$. Assume that $O \subseteq C$.
Then

$$
\langle \bx - \ba, \nabla f(\ba) \rangle \geq 0, \Forall \bx \in C.
$$
If $f$ is real valued (with $\dom f = \VV$)
and $C = \VV$, this reduces to $\nabla f(\ba) = \bzero$.
```
This result is similar to {prf:ref}`res-cvxopt-diff-convex-optimal-criterion`
however applicable to all functions
that are continuously differentiable in the neighborhood of their local minimum.


```{prf:proof}
Since $C$ is convex, hence by {prf:ref}`res-opt-feasible-tangent-cone`,
$\closure F_C(\bx) = T_C(\bx)$ for every $\bx \in C$.

1. By {prf:ref}`res-opt-tangent-cone-local-minimum`, we have

   $$
   \langle \by, \nabla f(\ba) \rangle \geq 0, \Forall \by \in T_C(\ba).
   $$
1. In other words

   $$
   \langle \by, \nabla f(\ba) \rangle \geq 0, \Forall \by \in \closure F_C(\ba).
   $$
1. For any $\bx \in C$, we have $\bx - \ba \in F_C(\ba)$ since $C$ is convex.
1. Hence

   $$
   \langle \bx - \ba, \nabla f(\ba) \rangle \geq 0, \Forall \bx \in C.
   $$

The special case of $C = \VV$ is as follows.
1. Choose an orthogonal basis $\be_1, \dots, \be_n$ for $\VV$.
1. By picking $\bx = \ba + \be_i$ and $\bx = \ba - \be_i$, we see that
   
   $$
   \langle \be_i \nabla f(\ba) \rangle = 0 \Forall i.
   $$
1. Hence $\nabla f(\ba) = \bzero$.
```



### Convex Functions on a Convex Set

Recall from Fermat's optimality condition
({prf:ref}`res-cvxf-subdiff-fermat-optimality`)
that for the unconstrained minimization problem,
$\ba$ is a minimizer of $f$ if and only if
$\bzero$ is a subgradient of $f$ at $\ba$.

A similar result can be obtained for the
constrained optimization problem in terms
of the subgradients of $f$ and the normal
cone of $C$.

```{prf:theorem} Optimality conditions for convex constrained optimization
:label: res-opt-cvx-const-cvx-optimal

Let $f : \VV \to \RERL$ be a proper and convex
function. Let $C \subseteq \VV$ be a convex
set for which $\relint \dom f \cap \relint C \neq \EmptySet$.
Then, $\bx^* \in C$ is an optimal solution
of {eq}`eq-cvx-const-cvx-opt-form` if and only if

$$
\text{ there exists } \bg \in \partial f(\bx^*)
\text{ for which } - \bg \in N_C(\bx^*).
$$

Equivalently, $\bx^*$ minimizes $f$ over $C$ if and only if

$$
\bzero \in \partial f(\bx^*) + T_C(\bx^*)^{\circ}.
$$
```

```{prf:proof}

The problem in {eq}`eq-cvx-const-cvx-opt-form`
can be rephrased as 

$$
\min_{\bx \in \VV} f(\bx) + I_C(\bx)
$$
where $I_C$ is the indicator function for the set $C$.

1. Since $\relint \dom f \cap \relint C \neq \EmptySet$,
   hence due to the sum rule of subdifferential calculus
   ({prf:ref}`res-cvxf-subdiff-sum-rule-proper-convex`):

   $$
   \partial (f + I_C) (\bx) = \partial f(\bx) + \partial I_C(\bx).
   $$
1. Recall from {prf:ref}`res-cvxf-subdifferential-indicator` that
   
   $$
   \partial I_C(\bx) = N_C(\bx).
   $$
1. Hence for any $\bx \in \VV$

   $$
   \partial (f + \delta_C) (\bx) = \partial f(\bx) + N_C(\bx).
   $$
1. Invoking Fermat's optimality condition
   ({prf:ref}`res-cvxf-subdiff-fermat-optimality`),
   $\bx^* \in C$ is an optimal solution of {eq}`eq-cvx-const-cvx-opt-form`
   if and only if 

   $$
   \bzero \in \partial f(\bx^*) + N_C(\bx^*).
   $$
1. In other words, there exists $\bg \in \partial f(\bx^*)$
   and $\bh \in N_C(\bx^*)$ such that $\bg + \bh = \bzero$.
1. This is equivalent to saying that there exists a vector
   $\bg \in \partial f(\bx^*)$ such that $-\bg \in N_C(\bx^*)$.
1. This is same as the condition 

   $$
   (- \partial f(\bx^*)) \cap N_C(\bx^*) \neq \EmptySet.
   $$

For the second part:

1. By {prf:ref}`res-opt-polar-tangent-cone-normal-cone`, we have
   $N_C(\bx^*) = T_C(\bx^*)^{\circ}$ since $C$ is convex.
1. By the earlier argument, we have $\bg \in \partial f(\bx^*)$
   and $\bh \in N_C(\bx^*)$ such that 

   $$
   \bg + \bh = \bzero.
   $$
1. This is equivalent to saying that 

   $$
   \bzero \in \partial f(\bx^*) + T_C(\bx^*)^{\circ}.
   $$
```

By using the definition of the normal cone, we can provide an alternative
specification of the necessary and sufficient optimality condition in
a more explicit manner.

```{prf:corollary} Optimality conditions for convex constrained optimization second version
:label: res-opt-cvx-const-cvx-optimal-2

Let $f : \VV \to \RERL$ be a proper and convex
function. Let $C \subseteq \VV$ be a convex
set for which $\relint \dom f \cap \relint C \neq \EmptySet$.
Then, $\bx^* \in C$ is an optimal solution
of {eq}`eq-cvx-const-cvx-opt-form` if and only if

$$
\text{ there exists } \bg \in \partial f(\bx^*)
\text{ for which } \langle \bx - \bx^*, \bg \rangle \geq 0 \Forall \bx \in C.
$$
```

Following is the refinement of {prf:ref}`res-opt-smooth-local-minimum-convex-const`
for continuously differentiable functions at the global minimum.

```{prf:corollary} Minimization of convex and smooth function on a convex set
:label: res-opt-cvx-const-cvx-optimal-3

Let $f : \VV \to \RERL$ be a proper and convex
function. Let $C \subseteq \VV$ be a convex
set for which $\relint \dom f \cap \relint C \neq \EmptySet$.
Assume that $f$ is continuously differentiable at a point $\bx^* \in C$.

Then, $\bx^* \in C$ is an optimal solution
of {eq}`eq-cvx-const-cvx-opt-form` if and only if

$$
\langle \bx - \bx^*, \nabla f(\bx^*) \rangle \geq 0 \Forall \bx \in C.
$$
```

### Sum of Smooth and Convex Functions on an Arbitrary Constraint Set

```{prf:theorem} Minimization of sum of smooth and convex function
:label: res-opt-min-sum-smooth-convex-constrained

Let $\ba$ be a local minimum of a function $f: \VV \to \RR$
over a set $C$. Assume that the tangent cone $T_C(\ba)$ is convex.
Assume that $f$ has the form

$$
f(\bx) = f_1(\bx) + f_2(\bx)
$$
where $f_1 : \VV \to \RR$ is convex and $f_2 : \VV \to \RR$ is smooth.
Then

$$
- \nabla f_2(\ba) \in \partial f_1(\ba) + T_C(\ba).
$$
```

### Optimization Over Unit Simplex

In this section, we consider the problem of minimizing a function
over the unit simplex $\Delta_n$.

Recall from {prf:ref}`def-convex-unit-simplex` that the unit
simplex is given by

$$
\Delta_n = \{\bx \in \RR^n 
    \ST \langle \bx, \bone \rangle = 1, \bx \succeq \bzero \}.
$$
In other words, for every $\bx \in \Delta_n$, every component
is nonnegative and their sum is 1.


````{prf:theorem} Optimality conditions over unit simplex
:label: res-opt-cond-cvx-over-unit-simplex

Let $f : \RR^n \to \RERL$ be a proper and convex
function. 

Consider the optimization problem

```{math}
:label: eq-opt-cvx-unit-simplex-prob
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in \Delta_n.
```
Assume that $\relint \dom f \cap \relint \Delta_n \neq \EmptySet$.
Then, $\bx^* \in \Delta_n$ is an optimal solution
if and only if there exists $\bg \in \partial f(\bx^*)$
and $\mu \in \RR$ such that

```{math}
:label: eq-opt-cvx-unit-simplex-cond
g_i \begin{cases}
 = \mu, & x_i^* > 0;\\
 \geq \mu, & x_i^* = 0.
\end{cases}
```
````

```{prf:proof}
Assume that for some $\bx^* \in \Delta_n$,
there exists a $\bg \in \partial f(\bx^*)$ and $\mu$
satisfying {eq}`eq-opt-cvx-unit-simplex-cond`.

1. Note that $\sum_{i=1}^n \bx_i^* = 1$ simplifies to $\sum_{i \ST x_i > 0} x_i^* = 1$.
1. Now, for any $\bx \in \Delta_n$

    $$
    \bg^T(\bx - \bx^*) 
    &= \sum_{i=1}^n g_i (x_i - x_i^*) \\
    &= \sum_{i \ST x_i^* > 0} g_i (x_i - x_i^*) + \sum_{i \ST x_i^* = 0} g_i x_i \\
    &\geq \sum_{i \ST x_i^* > 0} \mu (x_i - x_i^*) + \sum_{i \ST x_i^* = 0} \mu x_i \\
    &= \mu \sum_{i=1}^n x_i - \mu \sum_{i \ST x_i^* > 0} x_i^* \\
    &= \mu 1  - \mu 1 = \mu - \mu = 0.
    $$

1. Thus,

    $$
    \bg^T(\bx - \bx^*)\geq 0 \Forall \bx \in \Delta_n.
    $$
1. Thus, due to {prf:ref}`res-opt-cvx-const-cvx-optimal-2`,
   $\bx^*$ is indeed an optimal point.

For the converse, assume that $\bx^*$ is an optimal point. 
1. Then, due to {prf:ref}`res-opt-cvx-const-cvx-optimal-2`,
   there exists $\bg \in \partial f(\bx^*)$
   such that $\bg^T(\bx - \bx^*)\geq 0 \Forall \bx \in \Delta_n$.
1. We need to find a value of $\mu$ such that $\bg$
   satisfies {eq}`eq-opt-cvx-unit-simplex-cond`.
1. We consider the following three cases.
   1. $\bx^* = \bzero$.
   1. Only one entry in $\bx^*$ is nonzero and others are zero.
   1. Two or more entries in $\bx^*$ are nonzero.
1. If $\bx^* = \bzero$ then we can choose $\mu = \min \{ g_1, \dots, g_n \}$
   satisfying {eq}`eq-opt-cvx-unit-simplex-cond`.
1. Suppose that only the $i$-th entry of $\bx^*$ is nonzero and remaining
   entries are zero.
   1. Since $\bx^* \in \Delta_n$ hence $\sum_{j=1}^n x_j^* = 1$ implies that
      $x_i^* = 1$.
   1. Let $\mu = g_i$.
   1. Pick any $j \in \{1,\dots,n \}$ such that $j \neq i$.
   1. Let $\bx = \be_j$; i.e., the unit vector whose $j$-th component is 1
      and other components are zero.
   1. Then,

      $$
      & \bg^T (\bx - \bx^*) \geq 0 \\
      \implies & \bg^T \bx - \bg^T \bx^* \geq 0 \\
      \implies &  g_j - g_i \geq 0 \\
      \implies & g_j \geq g_i = \mu.
      $$
    1. Thus, with $\mu = g_i$, {eq}`eq-opt-cvx-unit-simplex-cond` is satisfied.

1. For the third case, let $i$ and $j$ denote two different indices
   for which $x_i^* > 0$ and $x_j^* > 0$.
   1. Pick a vector $\bx \in \Delta_n$ satisfying
   
      $$
      x_k = \begin{cases}
      x_k^*, & k \notin \{i, j \}; \\
      x_i^* - \frac{x_i^*}{2}, & k = i ; \\
      x_j^* + \frac{x_i^*}{2}, & k = j .
      \end{cases}
      $$
      We can verify that $\bx \in \Delta_n$.
   1. Then, the inequality $\bg^T(\bx - \bx^*) \geq 0$
      simplifies to 

      $$
      - \frac{x_i^*}{2} g_i  + \frac{x_i^*}{2} g_j \geq 0.
      $$
   1. Since $x_i^* > 0$, hence this simplifies to $g_i \leq g_j$.
   1. Switching the role of $i$ and $j$ and following an identical
      argument, we get $g_i \geq g_j$.
   1. This means that $g_i = g_j$ must hold true.
   1. The argument is independent of the choice of $i,j$ for which
      $x_i^*, x_j^* > 0$.
   1. Thus $g_i = g_j$ holds true
      for every $i,j$ such that $x_i^*, x_j^* > 0$..
   1. This implies that all the components of $\bg$ corresponding
      to the positive components of $\bx^*$ must have the same
      value.
   1. Let this common value be $\mu$. 
   1. In other words, $g_i = \mu$ for all $i=1,\dots,n$ such that $x_i^* > 0$.
   1. Now consider some $k \in \{1,\dots,n\}$ such that $x_k = 0$.
   1. Let $\bx = \be_k$.
   1. Note that $\sum_{i=1}^n \bx_i^* = 1$ simplifies to $\sum_{i \ST x_i > 0} x_i^* = 1$.
   1. Then, 

      $$
      & \bg^T (\bx - \bx^* ) \geq 0 \\
      \implies & \bg^T \bx - \bg^T \bx^* \geq 0 \\
      \implies & g_k - \sum_{i \ST x_i^* > 0} g_i x_i^*  \geq 0\\  
      \implies & g_k - \mu \sum_{i \ST x_i^* > 0} x_i^*  \geq 0\\  
      \implies & g_k - \mu \geq 0\\ 
      \implies & g_k \geq \mu.
      $$
   1. Thus, $g_i \geq \mu$ for all $i=1,\dots,n$ such that $x^*_i = 0$.
   1. Thus, we have established that $\bg$ indeed satisfies {eq}`eq-opt-cvx-unit-simplex-cond`.
```

```{prf:example} Optimization over the unit simplex
:label: ex-opt-unit-simplex-1

Consider the function $f : \RR^n \to \RERL$ given by

$$
f(\bx) = \begin{cases}
\sum_{i=1}^n x_i \ln x_i - \sum_{i=1}^n y_i x_i, & \bx \succeq \bzero;\\
\infty & \text{ otherwise}.
\end{cases}
$$
The vector $\by = (y_1, \dots, y_n) \in \RR^n$ is fixed.
Consider the optimization problem

$$
\min \{ f(\bx) \ST \bx \in \Delta_n \}.
$$

1. $f$ is a proper convex function.
1. We can see that $\dom f = \RR^n_+$.
1. $\interior \dom f = \relint \dom f = \RR^n_{++}$. 
1. It is easy to see that $\relint \dom f \cap \relint \Delta_n \neq \EmptySet$.
1. $f$ is differentiable at $\bx \in \interior \dom f$.
1. The partial derivatives of $f$ are given by

   $$
   \frac{\partial f}{\partial x_i} (\bx) = 1 + \ln x_i - y_i.
   $$
1. Thus, $\partial f(\bx) = \{ \nabla f(\bx) \}$ at every $\bx \succ \bzero$.
1. Assume that there is an optimal solution satisfying $\bx^* \succ \bzero$.
1. By {prf:ref}`res-opt-cond-cvx-over-unit-simplex`, there exists $\bg \in \partial f(\bx^*)$
   and $\mu \in \RR$
   satisfying {eq}`eq-opt-cvx-unit-simplex-cond`.
1. Since $\bx \succ \bzero$, {eq}`eq-opt-cvx-unit-simplex-cond`
   simplifies to $g_i = \mu$ for all $i=1,\dots,n$.
1. Since $f$ is differentiable, hence the only subgradient is $\nabla f(\bx^*)$.
1. Thus, there exists $\mu \in \RR$ such that 
 
   $$
   \frac{\partial f}{\partial x_i} (\bx^*) = \mu.
   $$
1. This implies

   $$
   1 + \ln x_i^* - y_i = \mu.
   $$
1. Therefore, for every $i$

   $$
   x_i^* = e^{\mu - 1 + y_i} = \alpha e^{y_i}
   $$
   where $\alpha = e^{\mu - 1}$.
1. Since $\bx^* \in \Delta_n$, hence $\sum_{i=1}^n x_i^* = 1$.
1. Thus,

   $$
   & \sum_{i=1}^n \alpha e^{y_i} = 1 \\
   \iff & \alpha = \frac{1}{\sum_{i=1}^n e^{y_i}}.
   $$
1. Therefore 

   $$
   x_i^* = \frac{e^{y_i}}{\sum_{j=1}^n e^{y_j}} \Forall i = 1,\dots,n.
   $$
1. We note that $\bx^*$ obtained above satisfies all the conditions 
   in {prf:ref}`res-opt-cond-cvx-over-unit-simplex`.
1. Since these conditions are also sufficient, hence $\bx^*$ is indeed
   the optimal solution for this minimization problem.
1. Let us compute the optimal value of the minimization problem.
1. We note that
    
   $$
   \ln x_i^* = \mu - 1 + y_i.
   $$
1. Hence 

   $$
   & f(\bx^*) = \sum_{i=1}^n x_i^* \ln x_i^* - \sum_{i=1}^n y_i x_i^* \\
   &= \sum_{i=1}^n x_i^* ( \mu - 1 + y_i) - \sum_{i=1}^n y_i x_i^* \\
   &= \sum_{i=1}^n x_i^* ( \mu - 1) \\
   &= ( \mu - 1)  \sum_{i=1}^n x_i^* \\
   & = \mu -1.
   $$
1. In terms of $\by$,

   $$
   f(\bx^*) = \mu -1 = \ln \alpha
   = - \ln \left ( \sum_{i=1}^n e^{y_i} \right ).
   $$
1. The optimal value is the negative of the log-sum-exp of $\by$.

This optimization problem is used in the
computation of the conjugate function for the
negative entropy function. 
See {prf:ref}`res-cvxf-conjugate-neg-entropy-unit-simplex`.
```

