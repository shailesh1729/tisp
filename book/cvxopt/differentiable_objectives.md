# Convex Differentiable Objective Functions

In this section, we focus on objective functions of type
$f : \RR^n \to \RR$ which are convex and differentiable.
Our goal is to minimize $f$ over a convex set $C \subseteq \dom f$.

ain references for this section are
{cite}`beck2014introduction,boyd2004convex`.


## First Order Optimality Criteria

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
1. Recall that for any $\bv \in \RR^n$, the optimal value of the problem

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
1. Thus, the inequality must be an equality, giving us

   $$
   - \nabla f(\ba)^T \ba =  \| \nabla f(\ba) \|.
   $$