(sec:opt:convex-differentiable-objective)=
# Differentiable Objective Functions

In this section, we focus on objective functions of type
$f : \RR^n \to \RR$ which are convex and differentiable.
Our goal is to minimize $f$ over a convex set $C \subseteq \dom f$.

Main references for this section are
{cite}`beck2014introduction,boyd2004convex`.


## Stationary Points

We first look at functions which are differentiable over a
convex set. Here, we don't require that the function itself
be convex. Thus, we may not characterize the global 
optimality of a point. However, we can still
characterize the local optimality of a point.


In {prf:ref}`def-opt-stationary-point`, we defined
stationary points for a real valued function as
points where the gradient vanishes; i.e. $\nabla f(\bx) = \bzero$.

In this section, we wish to restrict the domain of feasible
points to a convex set $C$ and consider the problem

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C
$$
where $f$ is differentiable over the convex set $C$.

We now introduce the notion of stationary points for
the given optimization problem of minimizing $f$ over $C$.

```{prf:definition} Stationary point for an optimization problem
:label: def-opt-over-c-stationary-point

Let $f : \RR^n \to \RR$ be a real valued function which
is differentiable over a convex set $C$.

Then, $\ba \in C$ is called a *stationary point* of the
problem of minimizing $f$ over $C$ if 

$$
\nabla f(\ba)^T (\bx - \ba) \geq 0 \Forall \bx \in C.
$$
```
If $C = \RR^n$, then the condition will reduce to
$\nabla f(\ba) = \bzero$.


```{prf:theorem} Local minimum points are stationary points
:label: res-opt-over-c-local-min-stationary

Let $f : \RR^n \to \RR$ be a real valued function which
is differentiable over a convex set $C$.
Consider the optimization problem

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C.
$$
If $\ba \in C$ is a local minimum, then $\ba$ must be
a stationary point. 
```

```{prf:proof}
Let $\ba$ be a local minimum and for contradiction assume
that it is not a stationary point.

1. Then, there exists $\bx \in C$ such that
   $\nabla f(\ba)^T (\bx - \ba) < 0$.
1. Let $t \in [0,1]$ be a parameter.
1. Let $\bz_t = t \bx + (1-t) \ba$.
1. Since $C$ is convex, hence $\bz_t \in C$.
1. Differentiating $f(\bz_t)$ w.r.t. $t$ at $t=0$, we obtain

   $$
   \left . \frac{d}{d t} f(\bz_t) \right |_{t=0} = \nabla f(\ba)^T (\bx - \ba) < 0.
   $$
1. Thus, for small enough $t$, $f(\bz_t) < f(\ba)$.
1. This contradicts the hypothesis that $\ba$ is a local minimum.
1. Thus, all local minimum points must be stationary points.
```


```{prf:example} Unconstrained minimization
:label: ex-opt-diff-obj-unconstrained-minimization

Let $f : \RR^n \to \RR$ be a real valued function which
is differentiable.
Consider the unconstrained optimization problem

$$
\text{minimize }  f(\bx).
$$

In this case, the feasible set is $C = \RR^n$.

1. If $\ba$ is a stationary point for this problem, then
   
   $$
   \nabla f(\ba)^T (\bx - \ba) \geq 0 \Forall \bx \in \RR^n.
   $$
1. In particular, if we choose $\bx = \ba - \nabla f(\ba)$, we get

   $$
   \nabla f(\ba)^T (\bx - \ba) = \nabla f(\ba)^T (- \nabla f(\ba))
   = - \|  \nabla f(\ba) \|^2 \geq 0.
   $$
1. This is true only if $\nabla f(\ba) = \bzero$.
1. Thus, for unconstrained minimization, the gradient vanishes at stationary points.
```

```{prf:theorem} Stationary point as an orthogonal projection
:label: res-opt-over-c-stationary-orth-proj

Let $f : \RR^n \to \RR$ be a real valued function which
is differentiable over a convex set $C$.
Consider the optimization problem

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C.
$$
Let $s > 0$.
Then $\ba \in C$ is a stationary point of the optimization
problem if and only if

$$
\ba = P_C (\ba - s \nabla f(\ba)).
$$
```

```{prf:proof}

Recall from {prf:ref}`res-cvx-projection-characterization` that
$\bz \in C$ is the projection of $\bx$ if and only if

$$
\langle \by - \bz, \bx - \bz \rangle \leq 0 \Forall \by \in C.
$$

1. Replace $\bz = \ba$ and $\bx  = \ba - s \nabla f(\ba)$. We get

   $$
   & \langle \by - \ba, \ba - s \nabla f(\ba) - \ba \rangle \leq 0 \Forall \by \in C\\
   & \iff  s\langle \by - \ba, \nabla f(\ba) \rangle \geq 0 \Forall \by \in C\\
   & \iff \nabla f(\ba)^T (\by - \ba) \geq 0 \Forall \by \in C.
   $$
1. But this is the same condition as the definition for a stationary point.
```


## First Order Optimality Criteria

We now pay our attention to the case where $f$ is convex
as well as differentiable. In this case, a point is a global
optimal point if and only if it is a stationary point.

````{prf:theorem} Optimality criterion for differentiable objective function
:label: res-cvxopt-diff-convex-optimal-criterion

Let $f : \RR^n \to \RR$ be a differentiable convex function. 
Let $C \subseteq \dom f$ be a convex set. 
Consider the minimization problem

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C.
$$
Then, $\bx \in C$ is an optimal point if and only if 

```{math}
:label: eq-cvx-opt-diff-opt-criterion
\nabla f(\bx)^T (\by - \bx) \geq 0 \Forall \by \in C.
```

In other words, $\bx$ is optimal if and only if it is a stationary point.
````

```{prf:proof}
By {prf:ref}`res-cvxf-gradient-convexity-relation`

$$
f(\by) \geq f(\bx) + \nabla f(\bx)^T (\by - \bx)
$$
for every $\bx, \by \in \dom f$.

Assume that some $\bx \in C$ satisfies the optimality criterion
in {eq}`eq-cvx-opt-diff-opt-criterion`.

1. Let $\by \in C$.
1. Then, by differentiability

   $$
   f(\by) \geq f(\bx) + \nabla f(\bx)^T (\by - \bx).
   $$
1. By hypothesis $\nabla f(\bx)^T (\by - \bx) \geq 0$.
1. Thus, $f(\by) \geq f(\bx)$.
1. Since this is true for every $\by \in C$, hence
   $\bx$ is an optimal point for the minimization problem.

Now for the converse, assume that $\bx \in C$ is an optimal point.

1. For contradiction, assume that {eq}`eq-cvx-opt-diff-opt-criterion`
   doesn't hold.
1. Then, there exists $\by \in C$ such that

   $$
   \nabla f(\bx)^T (\by - \bx) < 0.
   $$
1. Let $t \in [0, 1]$ be a parameter.
1. Let $\bz(t) = t \by + (1-t) \bx$.
1. Since $C$ is convex, hence $\bz(t) \in C$.
1. Differentiating $f(\bz(t))$ w.r.t. $t$ at $t=0$, we obtain

   $$
   \left . \frac{d}{d t} f(\bz(t)) \right |_{t=0} = \nabla f(\bx)^T (\by - \bx) < 0.
   $$
1. Thus, for small enough $t$, $f(\bz(t)) < f(\bx)$. 
1. Thus, $\bx$ cannot be an optimal point for the minimization problem.
1. This contradicts our hypothesis that $\bx$ is an optimal point.
1. Hence, {eq}`eq-cvx-opt-diff-opt-criterion` must hold for every $\by \in C$.
```


````{prf:theorem} Optimality criterion for unconstrained problem with differentiable objective function
:label: res-cvxopt-diff-convex-optimal-unconstrained

Let $f : \RR^n \to \RR$ be a differentiable convex function. 
Consider the unconstrained minimization problem

$$
\text{minimize } f(\bx)
$$
Then, $\bx \in \RR^n$ is an optimal point if and only if 
$\nabla f(\bx) = \bzero$.
````

```{prf:proof}
In this case, the set of feasible points is $C = \dom f$.

1. Since $f$ is differentiable, hence $C$ is an open set.
1. By {prf:ref}`res-cvxopt-diff-convex-optimal-criterion`,
   $\bx$ is an optimal point if and only if

   $$
   \nabla f(\bx)^T (\by - \bx) \geq 0 \Forall \by \in C.
   $$
1. If $\nabla f(\bx) = \bzero$, then this inequality is satisfied.
   Hence, $\bx$ must be an optimal point.
1. Now, assume that $\bx$ is an optimal point.
1. Since $\bx \in C$ and $C$ is open, hence there exists
   a closed ball $B[\bx, r] \subseteq C$.
1. Let $\by = \bx - t \nabla f(\bx)$.
1. For sufficiently small $t > 0$, $\by \in B[\bx, r] \subseteq C$.
1. Then, 

   $$
   \nabla f(\bx)^T (\by - \bx)  = \nabla f(\bx)^T (-t  \nabla f(\bx))
   = -t \|  \nabla f(\bx) \|_2^2 \geq 0
   $$
   must hold true for $t > 0$.
1. This means that $\|  \nabla f(\bx) \|_2 \leq 0$ must be true.
1. Thus $\nabla f(\bx) = \bzero$ must be true.
```

We next show how the condition in {eq}`eq-cvx-opt-diff-opt-criterion`
simplifies for specific optimization problem structures.


### Equality Constraints

```{prf:theorem} Differentiable objective minimization with equality constraints
:label: res-cvxopt-diff-obj-linear-constraints

Let $f : \RR^n \to \RR$ be a differentiable convex function
with $\dom f = \RR^n$.
Consider the minimization problem: 

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bA \bx = \bb
$$
where $\bA \in \RR^{p \times n}$ and $\bb \in \RR^p$ represent
$p$ linear equality constraints.
Assume that the problem is feasible.

Then, $\bx$ is an optimal point for the minimization problem
if and only if there exists a vector $\bv \in \RR^p$ such that

$$
\nabla f (\bx) + \bA^T \bv = \bzero.
$$
```

```{prf:proof}
The feasible set is given by $C = \{ \bx \ST \bA \bx = \bb \}$.
We recall from {prf:ref}`res-cvxopt-diff-convex-optimal-criterion`, that
$\bx$ is an optimal point if and only if
$\nabla f(\bx)^T (\by - \bx) \geq 0 \Forall \by \in C$.

1. Thus, $\bx$ is feasible if and only if
   $\nabla f(\bx)^T (\by - \bx) \geq 0$ for every $\by$ satisfying
   $\bA \by = \bb$.
1. Since both $\bx$ and $\by$ are feasible, hence $\bA (\by - \bx) = \bzero$.
1. Thus, $\bz = \by - \bx \in \NullSpace(\bA)$.
1. In fact, $\by \in C$ if and only if $\by = \bx + \bz$ for some
   $\bz \in \NullSpace(\bA)$. 
1. Thus, the optimality criteria reduces to
   $\nabla f(\bx)^T \bz \geq 0$ for every $\bz \in \NullSpace(\bA)$.
1. Note that $\nabla f(\bx)^T \bz$ is a linear function of $\bz$
   as $\nabla f(\bx)$ is a fixed vector.
1. If a linear function is nonnegative on a subspace, then it must
   be identically zero on the subspace.
1. Thus, $\nabla f(\bx)^T \bz = 0$ for every $\bz \in \NullSpace(\bA)$. 
1. In other words, $\bx$ is optimal if and only if
   $\nabla f(\bx) \perp \NullSpace(\bA)$.
1. Recall that $\NullSpace(\bA)^{\perp} = \ColSpace(\bA^T)$;
   i.e., the null space of $\bA$ is orthogonal complement of the
   column space (range) of $\bA^T$.
1. Thus, $\bx$ is optimal if and only if 
   $\nabla f(\bx) \in \ColSpace(\bA^T)$.
1. In other words, $\bx$ is optimal if and only if there exists
   a vector $\bv \in \RR^p$ such that

   $$
   \nabla f (\bx) + \bA^T \bv = \bzero.
   $$
```

This result is a Lagrange multiplier optimality condition to be
discussed in more detail in later sections.

### Nonnegative Orthant Constraints

```{prf:example} Differentiable objective minimization over nonnegative orthant
:label: ex-cvxopt-diff-obj-nng-orthant


Let $f : \RR^n \to \RR$ be a differentiable convex function
with $\dom f = \RR^n$.
Consider the minimization problem: 

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \succeq \bzero.
$$

1. The feasible set is the nonnegative orthant $\RR^n_+$.
1. $\bx$ is optimal if and only if
   $\bx \succeq \bzero$ and
   $\nabla f (\bx)^T (\by - \bx) \geq 0$ for every $\by \succeq \bzero$.
1. The term $\nabla f (\bx)^T \by$ is unbounded below on $\by \in \RR^n_+$
   unless $\nabla f (\bx) \in \RR^n_+$.
1. Thus, $\nabla f (\bx)$ must be nonnegative. 
1. Then, the minimum value for $\nabla f (\bx)^T \by$ is 0.
1. Consequently, the optimality condition reduces to
   $-\nabla f (\bx)^T \bx \geq 0$
   or $\nabla f (\bx)^T \bx \leq 0$.
1. But $\bx \succeq \bzero$ and $\nabla f (\bx) \succeq \bzero$.
1. Thus, we must have $\nabla f (\bx)^T \bx = 0$.`
1. We note that 

   $$
   \nabla f (\bx)^T \bx = \sum_{i=1}^n (\nabla f (\bx))_i x_i.
   $$
1. Thus, it is a sum of products of nonnegative numbers.
1. So each term in the sum must be 0.
1. Thus, $(\nabla f (\bx))_i x_i = 0$ must hold true for every
   $i=1,\dots,n$.
1. Thus, the optimality condition can be rephrased as

   $$
   \bx \succeq \bzero
   \text{ and }
   \nabla f (\bx) \succeq \bzero
   \text{ and }
   (\nabla f (\bx))_i x_i = 0 \Forall i=1,\dots,n.
   $$

The condition $(\nabla f (\bx))_i x_i = 0$ for every $i$ is known
as *complementarity*. It means that for every $i$ either
$x_i$ or $(\nabla f (\bx))_i$ or both must be 0.
In other words, both $x_i$ and $(\nabla f (\bx))_i$ cannot be
nonzero at the same time.

Thus, the sparsity patterns of $\bx$ and $\nabla f (\bx)$ are
*complementary*. In other words,

$$
\supp (\bx) \cap \supp (\nabla f (\bx)) = \EmptySet
$$
where $\supp (\bx)$ denotes the index set of nonzero entries of $\bx$.
```

### Unit Sum Set Constraint

```{prf:example} Minimization over unit sum set
:label: ex-cvxopt-diff-obj-unit-sum-set


Let $f : \RR^n \to \RR$ be a differentiable convex function
with $\dom f = \RR^n$.
Consider the minimization problem: 

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bone^T \bx  = 1.
$$

1. The feasible set is given by

   $$
   C = \{ \bx \in \RR^n \ST \bone^T \bx = 1 \} 
    = \{ \bx \in \RR^n \ST \sum_{i=1}^n x_i = 1 \}.
   $$
1. This set is also known as the *unit sum set*.
1. A point $\ba \in C$ is optimal if and only if

   $$
   \nabla f(\ba)^T (\bx - \ba) \geq 0 \Forall \bx \in C.
   $$
   Let us call this condition (I).
1. This is equivalent to the condition:

   $$
   \frac{\partial f}{\partial x_1} (\ba) 
   =  \frac{\partial f}{\partial x_2} (\ba)
   = \dots 
   = \frac{\partial f}{\partial x_n} (\ba).
   $$
   Let us call this condition (II).
1. We shall show that (I) and (II) are equivalent.

We first show that (II) implies (I).

1. Assume that some $\ba \in C$ satisfies (II)  with

   $$
   \alpha = \frac{\partial f}{\partial x_1} (\ba) 
   =  \frac{\partial f}{\partial x_2} (\ba)
   = \dots 
   = \frac{\partial f}{\partial x_n} (\ba).
   $$

1. Then, for any $\bx \in C$, 

   $$
   \nabla f(\ba)^T (\bx - \ba)
   &= \sum_{i=1}^n \frac{\partial f}{\partial x_i} (\ba) (x_i - a_i) \\
   &= \alpha  \sum_{i=1}^n (x_i - a_i) \\
   &= \alpha (\sum_{i=1}^n x_i - \sum_{i=1}^n a_i) \\
   &= \alpha (1 - 1) = 0. 
   $$
1. Thus, we see that $\nabla f(\ba)^T (\bx - \ba) \geq 0$ indeed
   and (I) is satisfied.


Now, assume that (I) is satisfied for some $\ba \in C$.

1. For contradiction, assume that $\ba$ doesn't satisfy (II).
1. Then, their exist $i,j \in [1,\dots,n]$ such that

   $$
   \frac{\partial f}{\partial x_i} (\ba) 
   > \frac{\partial f}{\partial x_j} (\ba).
   $$
1. Pick a vector $\bx \in C$ with following definition

   $$
   x_k = \begin{cases}
   a_k & k \notin \{i, j \} \\
   a_k - 1 & k = i \\
   a_k + 1 & k = j.
   \end{cases}
   $$
1. Note that

   $$
   \sum_{i=1}^n x_k = \sum_{i=1}^n a_k = 1.
   $$
   Thus, $\bx \in C$ holds.
1. Now,

   $$
   \nabla f(\ba)^T (\bx - \ba)
   &= \sum_{k=1}^n \frac{\partial f}{\partial x_k} (\ba) (x_k - a_k) \\
   \nabla f(\ba)^T (\bx - \ba)
   &= \frac{\partial f}{\partial x_i} (\ba) (x_i - a_i)
   + \frac{\partial f}{\partial x_j} (\ba) (x_j - a_j) \\
   &= - \frac{\partial f}{\partial x_i} (\ba) + \frac{\partial f}{\partial x_j} (\ba)\\
   < 0.
   $$
1. This violates the hypothesis that (I) holds true.
1. Thus, (II) must be true.
1. Thus, (I) implies (II).
```


### Unit Ball Constraint

```{prf:example} Minimization over unit ball
:label: ex-cvxopt-diff-obj-unit-ball


Let $f : \RR^n \to \RR$ be a convex function
which is differentiable over $B[\bzero, 1]$.
Consider the minimization problem: 

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \| \bx \|  \leq 1.
$$

1. The feasible set is given by

   $$
   C = B[\bzero, 1] = \{  \bx \ST \| \bx \| \leq 1 \}.
   $$
1. A point $\ba \in B[\bzero, 1]$ is an optimal point
   if and only if

   $$
   \nabla f(\ba)^T (\bx - \ba) \geq 0 \Forall \bx \in B[\bzero, 1].
   $$
1. This is equivalent to saying that

   $$
   \underset{\| \bx \| \leq 1}{\inf} (\nabla f(\ba)^T \bx - \nabla f(\ba)^T \ba ) \geq 0.
   $$
1. Recall from {prf:ref}`res-opt-min-linear-func-unit-ball`
   that for any $\bv \in \RR^n$, the optimal value of the problem

   $$
   \inf \{ \bv^T \bx  \ST  \| \bx \| \leq 1 \}
   $$
   is $-\| \bv \|$.
1. Thus,

   $$
   \underset{\| \bx \| \leq 1}{\inf} \nabla f(\ba)^T \bx = - \| \nabla f(\ba) \|.
   $$
1. Thus, the inequality simplifies to

   $$
   - \nabla f(\ba)^T \ba \geq  \| \nabla f(\ba) \|.
   $$
1. At the same time, by Cauchy Schwartz inequality,

   $$
   - \nabla f(\ba)^T \ba \leq  \| \nabla f(\ba) \| \| \ba \|
   \leq \| \nabla f(\ba) \|
   $$
   since $\ba \in B[\bzero, 1]$.
1. Thus, the inequality must be an equality, giving us,
   $\ba$ is an optimal point 

   $$
   - \nabla f(\ba)^T \ba =  \| \nabla f(\ba) \|.
   $$

We now have following possibilities for this condition.

1. If $\nabla f(\ba) = \bzero$, then the condition holds
   and $\ba$ is indeed an optimal point. 
1. Otherwise, if $\nabla f(\ba) \neq \bzero$, then $\| \ba \| = 1$ must be true.
   1. For contradiction, if we assume that $ \| \ba \| < 1$.
   1. Then, by Cauchy Schwartz inequality

      $$
      - \nabla f(\ba)^T \ba \leq  \| \nabla f(\ba) \| \| \ba \|
      < \| \nabla f(\ba) \|,
      $$
      a contradiction.
1. Thus, if $\nabla f(\ba) \neq \bzero$, then $\ba$ is an optimal point
   if and only if $ \| \ba \| = 1$ and

   $$
   - \nabla f(\ba)^T \ba =  \| \nabla f(\ba) \| = \| \nabla f(\ba) \| \| \ba \|.
   $$
1. But this is possible only when there exists $t \leq 0$ such that

   $$
   \nabla f(\ba) = t \ba.
   $$
1. Thus, if $\nabla f(\ba) \neq \bzero$, then $\ba$ is an optimal point
   if and only if $ \| \ba \| = 1$ and there exists $t \leq 0$ such that
   $\nabla f(\ba) = t \ba$.
```

## Gradient Method

We first consider the problem of unconstrained minimization of
a continuously differentiable function $f$.

Typical iterative algorithms which aim to find
the solution $\bx$ for the minimization problem
start with an initial guess $\bx_0$ and perform
a step of the form

$$
\bx_{k+1} = \bx_k + t_k \bd_k
$$
where $\bx_k$ is the current guess (starting from $\bx_0$),
$\bd_k$ is a direction in which we move to make the next
guess and $t_k$ is a step size in that direction. 
$\bx_{k+1}$ is the next guess obtained from current
guess. 
We say that an algorithm has made progress if
$f(\bx_{k+1}) < f(\bx_k)$.

This brings us to the notion of a descent direction.

```{prf:definition} Descent direction
:label: def-opt-descent-direction

Let $f : \VV \to \RR$ be a continuously differentiable
function over $\VV$. A nonzero vector $\bd$ is called
a descent direction of $f$ at $\bx$ if the
directional derivative $f'(\bx; \bd)$ is negative.

In other words,

$$
f'(\bx; \bd) = \langle \bd, \nabla f(\bx) \rangle < 0.
$$
```
If the directional derivative is negative, then it
is clear that for a small enough step in this direction,
the value of $f$ will decrease.

```{prf:lemma} Descent property of descent direction
:label: res-opt-descent-dir-property

Let $f : \VV \to \RR$ be a continuously differentiable
function over $\VV$.
Let $\bx \in \VV$.
Assume that $\bd$ is a descent direction for $f$. 
Then, there exists $\epsilon > 0$  such that

$$
f(\bx + t \bd) < f(\bx)
$$
for any $t \in (0, \epsilon]$.
```

```{prf:proof}
This follows from the negativity of the directional derivative.

1. Recall from {prf:ref}`def-cvxf-directional-derivative` that

   $$
   f'(\bx; \bd) = \lim_{t \to 0^+} \frac{f(\bx + t \bd) - f(\bx)}{t}.
   $$
1. Since $\bd$ is a descent direction, hence $f'(\bx; \bd) < 0$.
1. Thus, 

   $$
   \lim_{t \to 0^+} \frac{f(\bx + t \bd) - f(\bx)}{t} < 0.
   $$
1. Thus, there exists $\epsilon > 0$ such that
 
   $$
   \frac{f(\bx + t \bd) - f(\bx)}{t} < 0
   $$
   for every $t \in (0, \epsilon]$.
```


## Gradient Projection Method

In this subsection, we present a method to solve the
optimization problem

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C
$$
where $C$ is a convex set and $f$ is differentiable over $C$.

Recall from {prf:ref}`res-opt-over-c-stationary-orth-proj`, that
$\ba$ is a stationary point for the problem of minimizing 
$f$ over a convex set $C$ if and only if

$$
\ba = P_C (\ba - s \nabla f(\ba)).
$$

This stationarity condition is the basis for the gradient projection method
presented below.


```{prf:algorithm} The gradient projection method
:label: alg-opt-diff-obj-gradient-projection

Inputs

1. $\epsilon > 0$ - tolerance parameter

Initialization

1. Pick $\bx_0 \in C$ arbitrarily.

General iteration: for $k=0,1,2,\dots$, execute the following steps

1. Pick a step size $t_k$ by a line search procedure.
1. Update: $\bx_{k+1} \leftarrow P_C (\bx_k - t_k \nabla f(\bx_k))$.
1. Check for convergence: If $\| \bx_{k+1} - \bx_k \| \leq \epsilon$, then
   STOP.

Return $\bx_{k+1}$ as the output.
```

```{div}

In the case of unconstrained minimization:

1. $C = \RR^n$
1. $P_C (\bx_k - t_k \nabla f(\bx_k)) = \bx_k - t_k \nabla f(\bx_k)$.
1. $\bx_{k+1} = \bx_k - t_k \nabla f(\bx_k)$.
1. We see that gradient projection reduces to gradient descent.


Another way to look at the algorithm is:

1. $\by_{k+1} = \bx_k - t_k \nabla f(\bx_k)$ computes the
   next candidate solution assuming no constraints.
1. $\bx_{k+1} = P_C(\by_{k+1})$ step projects the next candidate
   solution back to the feasible set $C$.
1. Thus, we have a gradient step followed by a projection step.
```

### Convergence

If we can establish conditions under which each iteration of
the gradient projection algorithm leads to sufficient decrease
in the value of the objective function, then we can guarantee
that the algorithm will converge in a finite number of steps.

```{prf:lemma} Sufficient decrease lemma for constrained problems
:label: res-opt-grad-proj-suff-dec

Consider the optimization problem:

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C.
$$

Assume that $C$ is a nonempty closed convex set,
$f$ is continuously differentiable over $C$, and $\nabla f$ 
is Lipschitz continuous with a constant $L$ over $C$,
Then, for any $\bx \in C$, and $t \in (0, \frac{2}{L})$, 
the following inequality holds.

$$
f(\bx) - f(\by) \geq t \left ( 1  - \frac{L t}{2} \right )
\left \| \frac{1}{t}(\bx - \by)  \right \|^2.
$$
where $\by = P_C(\bx - t \nabla f(\bx))$.
```

```{prf:proof}


```
