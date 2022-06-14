(sec:opt:lagrange:multipliers)=
# Lagrange Multipliers

Main references for this section are
{cite}`beck2014introduction,boyd2004convex,bertsekas2003convex`.

The material in this section builds up on the
material from previous sections. 
While the material in {ref}`sec:opt:convex-differentiable-objective`
and {ref}`sec:opt:constrained:optimization:2`
doesn't make specific assumptions on the structure
of the constraint set (beyond say convexity and closedness),
the material in {ref}`sec:opt:linear:constraints:2`
deals with a specific structure where the constraint set
consists of a system of linear inequalities and equalities.
This section focuses on the case where the constraint set
consists of a system of smooth inequalities and equalities.

The necessary
and/or sufficient conditions for the optimization
problems presented in this section admit the
existence of a set of nonnegative (for inequality
constraints) and real (for equality constraints)
scalars known as Lagrange multipliers satisfying
a specific system of equations.

1. We generalize the linear
   inequality and equality constraints
   in {ref}`sec:opt:linear:constraints:2`
   to allow for smooth inequality and equality
   constraints.
1. We first consider problems involving minimization
   of a smooth function over a set of smooth
   inequalities.
   1. We describe the notion of feasible descent
      directions.
   1. We show that at local minimizers, there are no
      feasible descent directions. 
   1. We then develop the necessary
      Fritz-John conditions for the existence of
      a local minimizer.
   1. We add further constraint qualifications to
      develop the necessary KKT conditions for the
      existence of a local minimizer.
1. We then consider the problems involving minimization
   of a smooth function over a set of sooth
   inequalities and equalities. We present the KKT
   conditions for the existence of a local minimizer.
1. We then add convexity in the mix for the cost
   function and constraint functions.

## Inequality Constrained Problems

We start by developing the KKT conditions for the
problem of minimizing a smooth function over a
set of inequality constraints.

The problem is given as
```{math}
:label: eq-opt-lm-smooth-smooth-ineq
& \text{minimize }  & & f(\bx) & \\
& \text{subject to } & & g_i(\bx) \leq 0, i=1,\dots,m &
```
where $f, g_1, \dots, g_m : \VV \to \RR$ are
continuously differentiable functions over $\VV$.

The constraint set is given by

$$
C = \{\bx \in \VV \ST  g_i(\bx) \leq 0, i=1,\dots,m \}.
$$


### Feasible Descent Directions

Recall from {prf:ref}`def-opt-descent-direction`
that a descent direction is a direction along
which the directional derivative of the cost
function is negative; i.e.,
$f'(\bx; \bd) < 0$.
If $f$ is continuously differentiable, this
translates to

$$
f'(\bx; \bd) = \langle \bd, \nabla f(\bx) \rangle < 0.
$$
Recall from {prf:ref}`def-opt-feasible-direction`
that given a vector $\bx \in C$, 
a direction $\bd \in \VV$
is said to be a *feasible direction* of $C$ at $\bx$ if
there exists a $\overline{t} > 0$ such that

$$
\bx + t \bd \in C \text{ for every } t \in [0, \overline{t}].
$$

We now introduce the notion of a feasible descent direction.
```{prf:definition} Feasible descent direction
:label: def-opt-feasible-descent-direction

Consider the problem of minimizing a cost function
$f : \VV \to \RERL$
over a constraint set $C \subseteq \dom f$.
A nonzero vector $\bd$ is called a *feasible descent direction*
at $\bx \in C$ if $f'(\bx; \bd) < 0$
and there exists
$\overline{t} > 0$ such that

$$
\bx + t \bd \in C \text{ for every } t \in [0, \overline{t}].
$$
In other words, a feasible descent direction
at $\bx \in C$ is a feasible direction
and a decent direction.

1. If $f$ is continuously differentiable then
   we must have $\langle \bd, \nabla f(\bx) \rangle < 0$.
1. If $C$ is convex, then we just need to have
   $\bx + \overline{t}\bd \in C$. By virtual of
   convexity of $C$, every
   $\by \in [\bx, \bx + \overline{t}\bd ] \in C$.
```

```{prf:lemma} Local minimum and feasible descent directions
:label: res-opt-local-min-feasible-descent-dirs

Consider the problem of minimizing a cost function
$f : \VV \to \RERL$
over a constraint set $C \subseteq \dom f$.
If $\bx^*$ is a local minimizer then there are
no feasible descent directions at $\bx^*$.
```

```{prf:proof}
We prove this by contradiction.

1. Let $\bx^*$ be a local minimizer.
1. Assume that $\bd \neq \bzero$ is a feasible descent direction.
1. Then there is an $\epsilon_1 > 0$ such that
   $\bx^* + t \bd \in C$ for every $t \in [0, \epsilon_1]$.
1. Also, $f'(\bx; \bd) < 0$.
1. By {prf:ref}`def-cvxf-directional-derivative`,
   there exists $\epsilon_2 > 0$ such that

   $$
   \frac{f(\bx^* + t \bd) - f(\bx^*)}{t} < 0
   \quad \Forall  0 < t < \epsilon_2.
   $$
1. Equivalently, $f(\bx^* + t \bd) < f(\bx^*)$
   for all $0 < t < \epsilon_2$.
1. Let $\epsilon = \min(\epsilon_1, \epsilon_2)$.
1. Then for every $t \in (0, \epsilon)$, we have
   $\bx + t \bd \in C$ and $f(\bx^* + t \bd) < f(\bx^*)$.
1. This contradicts the hypothesis that $\bx^*$ is a
   local minimizer.
1. Hence, there are no feasible descent directions
   at $\bx^*$.
```

### Necessary Conditions for Local Optimality

Revising the problem {eq}`eq-opt-lm-smooth-smooth-ineq`:

1. A constraint $g_i$ is called active at $\bx$ if $g_i(\bx) = 0$.
1. A constraint $g_i$ is called inactive at $\bx$ if $g_i(\bx) < 0$.
1. The set of active constraints at a point $\bx$ is denoted by

   $$
   I(\bx) = \{ i \in 1,\dots,m \ST g_i(\bx) = 0 \}.
   $$

We first restate the {prf:ref}`res-opt-local-min-feasible-descent-dirs`
for the minimization with inequality constraints problem
{eq}`eq-opt-lm-smooth-smooth-ineq`.
The key idea is the lack of feasible descent directions
at a local minimizer.

1. $f'(\bx; \bd) < 0$ will indicate that $\bd$ is a feasible
   direction.
1. If a constraint is inactive, then it remains valid
   in the neighborhood of the local minimizer
   due to continuity of $g_i$.
1. If a constraint is active, then moving in some
   directions will lead to invalidation of the constraint
   while moving in some directions will keep the constraint
   valid.
1. In particular, if $g_i'(\bx; \bd) < 0$, then moving
   along $\bd$ keeps the $i$-th active constraint valid.
1. Hence, along a feasible descend direction, the directional
   derivatives of the cost function and the active constraint
   functions must be negative.

```{prf:lemma} Local minimum and feasible descent directions for inequality constraints
:label: res-opt-inequality-local-min-feasible-descent-dirs

Let $\bx^*$ be a local minimizer of the
optimization problem {eq}`eq-opt-lm-smooth-smooth-ineq`:

$$
& \text{minimize }  & & f(\bx) & \\
& \text{subject to } & & g_i(\bx) \leq 0, i=1,\dots,m &
$$
where $f, g_1, \dots, g_m : \VV \to \RR$ are
continuously differentiable functions over $\VV$.
Let $I(\bx^*)$ denote the set of active constraints:

$$
I(\bx^*) = \{ i \ST g_i(\bx^*) = 0 \}.
$$
Then there doesn't exist a vector $\bd \in \VV$
such that

$$
& \langle \bd, \nabla f(\bx^*) \rangle = f'(\bx^*; \bd) < 0,\\
& \langle \bd, \nabla g_i(\bx^*) \rangle = g_i'(\bx^*; \bd) < 0, \quad i \in I(\bx^*).
$$
```
This result states that local optimality
is equivalent to the infeasibility of
a certain system of strict inequalities.

```{prf:proof}
We prove this by contradiction.

1. Let $\bx^*$ be a local minimizer.
1. Assume that $\bd \neq \bzero$ be a direction
   satisfying the constraints above.
1. Then there exists an $\epsilon_0 > 0$
   such that $f(\bx^* + t \bd) < f(\bx^*)$
   for every $t \in (0, \epsilon_0)$.
1. Similarly, there exist $\epsilon_i > 0$
   such that $g_i(\bx^* + t \bd) < g_i(\bx^*) = 0$
   for every $t \in (0, \epsilon_i)$ for every $i \in I(\bx^*)$.
1. Let $\epsilon = \min\{\epsilon_0, \dots, \epsilon_m \}$.
1. Then for every $t \in (0, \epsilon)$, we have
   $f(\bx^* + t \bd) < f(\bx^*)$
   and $g_i (\bx^* + t \bd) < 0$ for every $i \in I(\bx^*)$.
1. By the continuity of $g_i$ for all $i$, 
   and the fact that $g_i(\bx^*) < 0$ for every $i \notin I(\bx^*)$,
   there exists a $\delta > 0$ such that for every $t \in (0, \delta)$,
   $g_i(\bx^* + t \bd) < 0$ for every $i \notin I(\bx^*)$.
1. Hence, we conclude that for every $t \in (0, \min(\epsilon, \delta))$,
   we have $f(\bx^* + t \bd) < f(\bx^*)$
   and $g_i (\bx^* + t \bd) < 0$ for every $i \in 1,\dots,m$.
1. But this contradicts the local optimality of $\bx^*$.
```

### Fritz-John Conditions

Recall that Farkas' and Gordan's theorems
of the alternative present different pairs
of systems where if one system is infeasible
then the other must be feasible and vice versa.
We can apply Gordan's theorem to the infeasible
system of strict inequalities in
{prf:ref}`res-opt-inequality-local-min-feasible-descent-dirs`
to develop the so-called Fritz-John conditions.

```{prf:theorem} Fritz-John conditions
:label: res-opt-inequality-fritz-john

Let $\bx^*$ be a local minimizer of the
optimization problem

$$
& \text{minimize }  & & f(\bx) & \\
& \text{subject to } & & g_i(\bx) \leq 0, i=1,\dots,m &
$$
where $f, g_1, \dots, g_m : \VV \to \RR$ are
continuously differentiable functions over $\VV$.
Then there exist nonnegative scalar multipliers
$t_0, t_1, \dots, t_m \geq 0$ which are not all
zero such that

$$
& t_0 \nabla f(\bx^*) + \sum_{i=1}^m t_i \nabla g_i(\bx^*) = \bzero, \\
& t_i g_i(\bx^*) = 0, i=1, \dots, m.
$$
```

```{prf:proof}
From {prf:ref}`res-opt-inequality-local-min-feasible-descent-dirs`,
we have that the following system is infeasible.

$$
& \langle \bd, \nabla f(\bx^*) \rangle < 0,\\
& \langle \bd, \nabla g_i(\bx^*) \rangle < 0, \quad i \in I(\bx^*).
$$

1. Let $n = \dim \VV$.
1. Let there be an isomorphic mapping between $\VV$ and $\RR^n$.
1. For every $\bx \in \VV$, let $\bx$ also denote the corresponding vector in $\RR^n$.
1. Assume that there are $k$ active constraints at $\bx^*$.
1. Construct a $k+1 \times n$ matrix $\bA$ as follows:

   $$
   \bA  = \begin{bmatrix}
   \nabla f(\bx^*)^T \\
   \nabla f_{i_1}(\bx^*)^T \\
   \vdots \\
   \nabla f_{i_k}(\bx^*)^T
   \end{bmatrix}
   $$
   where $i_1, \dots, i_k$ denote the indices of active constraints.
1. Then the above system of strict inequalities can be stated as
   $\bA \bd \prec \bzero$.
1. This system of equations is infeasible.
1. Then by {prf:ref}`Gordan's theorem <res-opt-gordan-theorem>`,
   the system

   $$
   \bt \neq \bzero, \bA^T \bt = \bzero, \bt \succeq \bzero
   $$
   where $\bt \in \RR^{k+1}$ is feasible.
1. We write $\bt =(t_0, t_{i_1}, \dots, t_{i_k})$.
1. The equation $\bA^T \bt = \bzero$ expands to

   $$
   t_0 \nabla f(\bx^*) + \sum_{i \in I(\bx^*)} t_i \nabla g_i(\bx^*) = \bzero.
   $$
1. $\bt \neq \bzero$ means that at least one of $t_0, t_{i_1}, \dots, t_{i_k} \neq 0$.
1. $\bt \succeq \bzero$ means that  $t_0, t_{i_1}, \dots, t_{i_k} \geq 0$.
1. Now, let $t_i = 0$ for all remaining $i \notin I(\bx^*)$.
1. Then for active constraints, we have $g_i(\bx^*) = 0$
   and for inactive constraints, we have $t_i = 0$.
1. Hence for all constraints, we have $t_i g_i(\bx^*) = 0$.
1. Hence there exist nonnegative scalar multipliers
   $t_0, t_1, \dots, t_m \geq 0$ which are not all
   zero such that

   $$
   & t_0 \nabla f(\bx^*) + \sum_{i=1}^m t_i \nabla g_i(\bx^*) = \bzero, \\
   & t_i g_i(\bx^*) = 0, i=1, \dots, m.
   $$
```

```{div}
The key issue with Fritz-John conditions is that
it allows $t_0 = 0$. The case $t_0 = 0$ is
not particularly useful since it leads to

$$
\sum_{i \in I(\bx^*)} t_i \nabla g_i(\bx^*) = \bzero.
$$
with $t_i \geq 0$ and not all $t_i$ being zero.
This means that the gradients of the active
constraints are linearly dependent.

1. The case of linearly dependent gradients has nothing to do with
   the objective function.
1. A number of points might satisfy the Fritz-John
   conditions and yet not be local minimum points.
1. We can modify the Fritz-John conditions and insist that
   the gradients of the active constraints be linearly independent.
1. This leads to what are called the KKIT conditions.
```

### KKT Conditions

```{prf:theorem} KKT conditions
:label: res-opt-inequality-kkt

Let $\bx^*$ be a local minimizer of the
optimization problem

$$
& \text{minimize }  & & f(\bx) & \\
& \text{subject to } & & g_i(\bx) \leq 0, i=1,\dots,m &
$$
where $f, g_1, \dots, g_m : \VV \to \RR$ are
continuously differentiable functions over $\VV$.
Let $I(\bx^*)$ denote the set of active constraints:

$$
I(\bx^*) = \{ i \ST g_i(\bx^*) = 0 \}.
$$
Assume that the gradients of the active constraints
$\{\nabla g_i(\bx^*) \}_{i \in I(\bx^*)}$ are 
linearly independent.


Then there exist nonnegative scalar multipliers
$t_1, \dots, t_m \geq 0$ which are not all
zero such that

$$
& \nabla f(\bx^*) + \sum_{i=1}^m t_i \nabla g_i(\bx^*) = \bzero, \\
& t_i g_i(\bx^*) = 0, i=1, \dots, m.
$$
```

```{prf:proof}
This is a simple extension of {prf:ref}`res-opt-inequality-fritz-john`.

By Fritz-John conditions, there exist nonnegative scalar multipliers
$r_0, r_1, \dots, r_m \geq 0$ which are not all
zero such that

$$
& r_0 \nabla f(\bx^*) + \sum_{i=1}^m r_i \nabla g_i(\bx^*) = \bzero, \\
& r_i g_i(\bx^*) = 0, i=1, \dots, m.
$$

1. If $r_0 = 0$, then the set of gradients of active constraints
   will become linearly dependent.
1. Hence, we must have $r_0 > 0$.
1. Let $t_i = \frac{r_i}{r_0}$ for every $i=1,\dots,m$.
1. The result follows.
```

## Inequality and Equality Constrained Problems

We now generalize the KKT conditions to include
problems of the form which include both inequality
constraints and equality constraints

```{math}
:label: eq-cvx-opt-lm-ineq-eq
& \text{minimize }   & & f(\bx) \\
& \text{subject to } & & g_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
```
where $f, g_1, \dots, g_m, h_1, \dots, h_p : \VV \to \RR$ are
continuously differentiable functions over $\VV$.

The constraint set is given by

$$
C = \{\bx \in \VV \ST  g_i(\bx) \leq 0, i=1,\dots,m
\text{ and }  h_j(\bx) = 0, j=1,\dots,p \}.
$$

1. An equality constraint must always be met at
   a feasible point. Hence there is no need to
   distinguish between active and inactive equality
   constraints. All inequality constraints are active.
1. A constraint of the form $h_j(\bx) = 0$ can be
   converted into two inequality constraints
   $h_j(\bx) \leq 0$ and $-h_j(\bx)\leq 0$.


```{prf:theorem} KKT conditions for problems with smooth inequality and equality constraints
:label: res-opt-ineq-eq-kkt

Let $\bx^*$ be a local minimizer of the
optimization problem {eq}`eq-cvx-opt-lm-ineq-eq`

$$
& \text{minimize }   & & f(\bx) \\
& \text{subject to } & & g_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
$$
where $f, g_1, \dots, g_m, h_1, \dots, h_p : \VV \to \RR$ are
continuously differentiable functions over $\VV$.
Let $I(\bx^*)$ denote the set of active inequality constraints:

$$
I(\bx^*) = \{ i \ST g_i(\bx^*) = 0 \}.
$$
Assume that the gradients of the active inequality constraints
$\{\nabla g_i(\bx^*) \}_{i \in I(\bx^*)}$
and all the equality constraints
$\{ \nabla h_j(\bx^*) \}_{j=1,\dots,p}$
are linearly independent.

Then there exist nonnegative scalar multipliers
$t_1, \dots, t_m \geq 0$
and real scalar multipliers $r_1, \dots, r_p \in \RR$
which are not all zero such that

$$
& \nabla f(\bx^*) + \sum_{i=1}^m t_i \nabla g_i(\bx^*)
+ \sum_{j=1}^p r_j \nabla h_j(\bx^*) = \bzero, \\
& t_i g_i(\bx^*) = 0, i=1, \dots, m.
$$
```

### KKT Points and Regular Points

All the results up to this point define a set of
necessary conditions in the form of a system of
equations on the constraint functions and their
gradients which must be satisfied by every
local minimizer of the optimization problem.
Besides the local minimizers, other points may
also satisfy this system of equations.
We now introduce the notion of KKT points
which satisfy these equations.

```{prf:definition} KKT point
:label: def-opt-kkt-point

Consider the optimization problem {eq}`eq-cvx-opt-lm-ineq-eq`
where $f, g_1, \dots, g_m, h_1, \dots, h_p : \VV \to \RR$ are
continuously differentiable functions over $\VV$.

A feasible point $\bx^*$ is called a *KKT point*
if there exist nonnegative scalar multipliers
$t_1, \dots, t_m \geq 0$
and real scalar multipliers $r_1, \dots, r_p \in \RR$
which are not all zero such that

$$
& \nabla f(\bx^*) + \sum_{i=1}^m t_i \nabla g_i(\bx^*)
+ \sum_{j=1}^p r_j \nabla h_j(\bx^*) = \bzero, \\
& t_i g_i(\bx^*) = 0, i=1, \dots, m.
$$
```
All the necessary KKT conditions so far can be simply
restarted as *a local minimizer must be a KKT point*
if the gradients of active inequality constraints and 
all equality constraints at the point are
linearly independent.
We introduce the notion of *regularity* to capture
the linear independence aspect.


```{prf:definition} Regularity
:label: def-opt-kkt-regularity

Consider the optimization problem {eq}`eq-cvx-opt-lm-ineq-eq`
where $f, g_1, \dots, g_m, h_1, \dots, h_p : \VV \to \RR$ are
continuously differentiable functions over $\VV$.

A feasible point $\bx^*$ is called *regular* if
the gradients of the active inequality constraints
$\{\nabla g_i(\bx^*) \}_{i \in I(\bx^*)}$
and all the equality constraints
$\{ \nabla h_j(\bx^*) \}_{j=1,\dots,p}$
are linearly independent.
```

With the terminology of these definitions,
{prf:ref}`res-opt-ineq-eq-kkt` reduces to:
if a regular point is a local minimizer
then it must be a KKT point.

The notion of regularity is a kind of
constraint qualification.


```{prf:example} Regular points, KKT points, Local minimizers
:label: ex-opt-lm-sum-2-circle-bd-kkt

Consider the problem:

$$
& \text{minimize }   & & x_1 + x_2 \\
& \text{subject to } & & x_1^2 + x_2^2 = 1.
$$

The problem structure

1. The ambient space is $\RR^2$.
1. We have the cost function: $f(\bx) = x_1 + x_2$.
1. The cost function is smooth and convex, in fact linear.
1. We don't have any inequality constraints.
1. We have one equality constraint.
1. The equality constraint function is given by $h(\bx) = x_1^2 + x_2^2 - 1$.
1. The equality constraint is $h(\bx) = 0$.
1. $h$ is a smooth function but it is not a convex function.
1. The constraint set is a contour of $h$.
1. The set of feasible points is given by $C = \{ \bx \ST h(\bx ) = 0 \}$.
1. The constraint set is not convex.
1. Hence, it is not a convex optimization problem.
1. However, the constraint set is compact.
1. Hence, due to {prf:ref}`res-ms-compact-real-valued-min-max-attain`,
   the function $f$ indeed attains a minimum as well as a
   maximum value on the $C$.

Gradients

1. We have $\nabla f(\bx) = (1, 1)$.
1. We have $\nabla h(\bx) = (2 x_1, 2 x_2)$.

Irregular points

1. The KKT conditions are applicable only on regular points.
1. We first identify the points which are irregular.
1. The irregular points are points at which the gradients
   of all active inequality constraints and equality constraints
   are linearly dependent.
1. Since, we have a single equality constraint, hence
   the irregular points are those points at which $\nabla h(\bx) = \bzero$.
1. This is given by a single point $(x_1, x_2) = (0, 0)$.
1. But $(0, 0) \notin C$ since $h((0,0)) = -1 \neq 0$.
1. Hence, the constraint set $C$ doesn't contain any irregular points.
1. In other words, every feasible point is a regular point.
1. Hence the KKT conditions are necessary for local optimality.
1. In other words, if a point is a local minimizer then it must be a KKT point.

KKT points

1. To identify the KKT points, we form the Lagrangian

   $$
   L(\bx, r) = f(\bx) + r h(\bx) = x_1 + x_2 + r (x_1^2 + x_2^2 -1).
   $$
1. The KKT conditions are:

   $$
   & \nabla_x L(\bx, r) = \nabla f(\bx) + r \nabla h(\bx) = 0,\\
   & h(\bx) = 0.
   $$
1. They expand to

   $$
   & 1 + 2 r x_1 = 0,\\
   & 1 + 2 r x_2 = 0,\\
   & x_1^2 + x_2^2 - 1  = 0.
   $$
1. From the first two equations, we have $r \neq 0$ and $x_1 = x_2 = \frac{-1}{2r}$.
1. Plugging it into the third equation, we get

   $$
   \left ( \frac{-1}{2r} \right )^2 + \left ( \frac{-1}{2r} \right )^2 = 1. 
   $$
1. This simplifies to $r^2 = \frac{1}{2}$.
1. Hence, we have $r = \pm \frac{1}{\sqrt{2}}$.
1. This gives us two different KKT points
   $(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$
   and $(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}})$.

The optimal solution
1. By compactness, we know that the minimizer does exist.
1. By regularity, we know that the minimizer must be a KKT point.
1. We have two candidates available.
1. We have $f((-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}})) = -\sqrt{2}$
   and $f((\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})) = \sqrt{2}$.
1. Hence the minimizer is given by

   $$
   \bx^* = \left (-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}} \right )
   $$
   as it has the smaller value of $f$.
```


## The Convex Case

We now restrict our attention to the case where
the cost and constraint functions are convex.
In this case, the KKT conditions are also sufficient.

```{prf:theorem} Sufficient KKT conditions for convex problems (smooth and convex cost and inequality constraints, affine equality constraints)
:label: res-opt-convex-ineq-affine-eq-kkt

Let $\bx^*$ be a feasible solution of the
optimization problem

$$
& \text{minimize }   & & f(\bx) \\
& \text{subject to } & & g_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
$$
where $f, g_1, \dots, g_m : \VV \to \RR$ are
continuously differentiable convex functions over $\VV$
and $h_1, \dots, h_p : \VV \to \RR$ are affine functions.

Suppose that there exist nonnegative scalar multipliers
$t_1, \dots, t_m \geq 0$
and real scalar multipliers $r_1, \dots, r_p \in \RR$
which are not all zero such that

$$
& \nabla f(\bx^*) + \sum_{i=1}^m t_i \nabla g_i(\bx^*)
+ \sum_{j=1}^p r_j \nabla h_j(\bx^*) = \bzero, \\
& t_i g_i(\bx^*) = 0, i=1, \dots, m.
$$
Then $\bx^*$ is an optimal solution of the minimization problem above.
```

```{prf:proof}
We are given that $\bx^*$ is a feasible point satisfying the
KKT conditions.

1. Define the function

   $$
   s(\bx) = f(\bx) + \sum_{i=1}^m t_i g_i(\bx) + \sum_{j=1}^p r_j h_j(\bx).
   $$
1. Since $f$ and $g_i$ are convex and $h_j$ are affine, hence $s$ is convex.
1. Since all of them are continuously differentiable, hence $s$ is also
   continuously differentiable.
1. We have

   $$
   \nabla s(\bx) =  \nabla f(\bx) + \sum_{i=1}^m t_i \nabla g_i(\bx)
   + \sum_{j=1}^p r_j \nabla h_j(\bx).
   $$
1. We are given that $\nabla s(\bx^*) = 0$.
1. By {prf:ref}`res-cvxopt-diff-convex-optimal-unconstrained`,
   $\bx^*$ is a minimizer of $s$ over $\VV$.
1. Hence $s(\bx^*) \leq s(\bx)$ for every $\bx \in \VV$.
1. By hypothesis $t_i g_i(\bx^*) = 0$ for every $i=1,\dots,m$.
1. Hence $\sum_{i=1}^m t_i g_i(\bx^*) = 0$.
1. Since $\bx^*$ is a feasible point,
   hence $h_j(\bx^*) = 0$ for every $j=1,\dots,p$.
1. Hence $\sum_{j=1}^p h_j(\bx^*) = 0$.
1. Hence

   $$
   f(\bx^*) 
   &= f(\bx^*) + \sum_{i=1}^m t_i g_i(\bx^*)  + \sum_{j=1}^p h_j(\bx^*)\\
   &= s(\bx^*) \\
   &\leq s(\bx)\\
   &= f(\bx) + \sum_{i=1}^m t_i g_i(\bx) + \sum_{j=1}^p r_j h_j(\bx)\\
   &\leq f(\bx).
   $$
   The last inequality comes from the fact that
   $t_i \geq 0$, $g_i(\bx) \leq 0$ and $h_j(\bx) = 0$ for every
   feasible $\bx$.
1. Hence for every feasible $\bx$, we have $f(\bx^*) \leq f(\bx)$.
1. Hence $\bx^*$ is an optimal point.
```

### Slater's Conditions

In {prf:ref}`res-opt-ineq-eq-kkt`, we saw that
KKT conditions become necessary for the local optimality
of a feasible point only if the feasible point is regular.
The regularity was a constraint qualification for
the nonconvex smooth optimization problem.

In the convex case, a different condition than
regularity can guarantee the necessity of KKT
conditions. They are known as *Slater's conditions*.

```{prf:definition} Slater's conditions
:label: def-opt-kkt-slater-condition

Let $g_1, \dots, g_m : \VV \to \RR$ be convex.
We say that the *Slater's condition* is satisfied for
a set of convex inequalities

$$
g_i(\bx) \leq 0, \quad i=1,\dots,m
$$
if there exists a point $\widehat{\bx} \in \VV$ such that

$$
g_i(\widehat{\bx}) < 0, \quad i=1,\dots,m.
$$

In other words, the Slater's condition requires the
existence of a point which strictly satisfies all the
convex inequality constraints.
```

Slater's condition is much easier to check since it
requires the existence of a single point which strictly satisfies
all the convex inequalities.


```{prf:theorem} Necessity of KKT conditions under Slater's condition
:label: res-opt-convex-ineq-slater

Let $\bx^*$ be an optimal solution of the
optimization problem

$$
& \text{minimize }   & & f(\bx) \\
& \text{subject to } & & g_i(\bx) \leq 0, & \quad i=1,\dots,m
$$
where $f, g_1, \dots, g_m : \VV \to \RR$ are
continuously differentiable functions over $\VV$.
In addition, assume that $g_1, \dots, g_m$ are convex.
Suppose that there exists a point $\widehat{\bx} \in \VV$ such that

$$
g_i(\widehat{\bx}) < 0, \quad i=1,\dots,m.
$$

Then there exist nonnegative scalar multipliers
$t_1, \dots, t_m \geq 0$
which are not all zero such that

$$
& \nabla f(\bx^*) + \sum_{i=1}^m t_i \nabla g_i(\bx^*) = \bzero, \\
& t_i g_i(\bx^*) = 0, i=1, \dots, m.
$$
```

```{prf:proof}
This is also derived from Fritz-John conditions
{prf:ref}`res-opt-inequality-fritz-john`.

By Fritz-John conditions, there exist nonnegative scalar multipliers
$r_0, r_1, \dots, r_m \geq 0$ which are not all
zero such that

$$
& r_0 \nabla f(\bx^*) + \sum_{i=1}^m r_i \nabla g_i(\bx^*) = \bzero, \\
& r_i g_i(\bx^*) = 0, i=1, \dots, m.
$$
We need to show that $r_0 > 0$. After that
we can pick $t_i = \frac{r_i}{r_0}$ for every $i=1,\dots,m$
to get the desired result.

1. For contradiction, assume that $r_0 = 0$.
1. Then we have

   $$
   \sum_{i=1}^m r_i \nabla g_i(\bx^*) = \bzero.
   $$
1. By the gradient inequality, we have

   $$
   g_i(\bx) \geq g_i(\bx^*) + \langle \bx - \bx^*, \nabla g_i(\bx^*) \rangle,
   \quad i=1,\dots,m.
   $$
1. Specifically, for the point $\widehat{\bx}$, we have

   $$
   0 >  g_i(\widehat{\bx}) \geq g_i(\bx^*) + \langle \widehat{\bx} - \bx^*, \nabla g_i(\bx^*) \rangle,
   \quad i=1,\dots,m.
   $$
1. Multiplying the $i$-th inequality by $r_i \geq 0$ and summing over
   $i=1,\dots,m$, we get

   $$
   0 > \sum_{i=1}^m r_i g_i(\bx^*) + 
   \langle \widehat{\bx} - \bx^*, \sum_{i=1}^m r_i \nabla g_i(\bx^*) \rangle.
   $$
   This inequality is strict since not all $r_i$ are $0$ and $r_0 = 0$.
1. Since $\sum_{i=1}^m r_i \nabla g_i(\bx^*) = \bzero$, it reduces to

   $$
   0 > \sum_{i=1}^m r_i g_i(\bx^*).
   $$
1. But $r_i g_i(\bx^*) = 0$ for every $i=1,\dots,m$. Hence we must have

   $$
   \sum_{i=1}^m r_i g_i(\bx^*) = 0.
   $$
1. A contradiction. Hence $r_0 > 0$ must be true.
```

## A Tangent Cones Perspective

```{div}
Consider an optimization problem of the form

$$
& \text{minimize }  & & f(\bx)\\
& \text{subject to } & & h_i(\bx) = 0, i=1,\dots,m.
$$
Assume that $f: \VV \to \RR$ and $h_i : \VV \to \RR$
for $i=1,\dots,m$
are smooth functions.

The constraint set can be written as

$$
C = \{ \bx \ST  h_i(\bx) = 0, i=1,\dots,m \}.
$$

1. Assume that $\bx^*$ is a minimizer of this problem.
1. By {prf:ref}`res-opt-tangent-cone-local-minimum`,
   we must have

   $$
   - \nabla f(\bx^*) \in T_C(\bx^*)^{\circ}.
   $$

Let us now motivate the Lagrange multipliers
using a simple problem of linear inequalities.

1. Consider the specific case where 

   $$
   h_i(\bx) = \langle \bx, \ba_i \rangle - b_i.
   $$
1. Consider a matrix $\bA$ which consists of
   $\ba_1^T, \dots, \ba_m^T$ as rows.
1. Put together $b_1, \dots, b_m$ as a vector $\bb$.
1. Then the constraint set can be expressed as

   $$
   C = \{ \bx \ST \bA \bx = \bb \}.
   $$
1. Assume that $\bx^* \in C$ is the local minimizer of $f$.
1. By {prf:ref}`ex-opt-tangent-cone-linear-system`,

   $$
   T_C(\bx^*) = \{ \bx \ST \bA \bx = \bzero \}
   $$
   which is the nullspace of $\bA$.
1. By {prf:ref}`ex-cvx-polar-cone-nullspace`,

   $$
   T_C(\bx^*)^{\circ} = T_C(\bx^*)^{\perp} =  \range \bA^T.
   $$
1. Hence, by the optimality condition, we have

   $$
   - \nabla f(\bx^*) \in \range \bA^T.
   $$
1. Hence, there exists $\bt^* \in \RR^m$ such that

   $$
   \nabla f(\bx^*) + \bA^T \bt^* = 0.
   $$
1. This is equivalent to

   $$
   \nabla f(\bx^*) + \sum_{i=1}^m t_i^* \ba_i = 0.
   $$
1. Since $\nabla h_i (\bx^*) = \ba_i$, hence this is equivalent to

   $$
   \nabla f(\bx^*) + \sum_{i=1}^m t_i^* \nabla h_i (\bx^*) = 0.
   $$

This motivates us to define the Lagrangian of $f$ as

$$
L(\bx, \bt) = f(\bx) + \sum_{i=1}^m t_i h_i(\bx).
$$

The basic Lagrangian theorem states that under
suitable conditions, if $\bx^*$ is a
local minimum of $f$ under the constraint set $C$
then there exist scalars $t_1^*, \dots, t_m^*$
called *Lagrangian multipliers* such that

$$
\nabla f(\bx^*) + \sum_{i=1}^m t_i^* \nabla h_i (\bx^*) = 0.
$$
1. There are $n$ unknowns in $\bx^*$ and $m$ unknowns in $\bt^*$.
1. Thus, we have a total of $m + n$ unknowns.
1. The relation above gives us a system of $n$ equations.
1. Together with the $m$ equalities $h_i(\bx^*) = 0$, 
   we have a system of $m + n$ equations with $m + n$ unknowns.
1. Thus, the problem of solving a constrained optimization
   problem is transformed into a problem of solving a system
   of nonlinear equations.
1. Now, suppose that the tangent cone at $\bx^*$ can be written
   as

   $$
   T_C(\bx^*) = \{\bx \ST \langle \bx, \nabla h_i(\bx^*) \rangle = 0,
   i=1,\dots,m \}.
   $$
1. Letting $\ba_i = \nabla h_i(\bx^*)$ and following the argument
   above, we must have

   $$
   \nabla f(\bx^*) + \sum_{i=1}^m t_i^* \nabla h_i (\bx^*) = 0.
   $$
1. Thus, if the tangent cone can be represented as above, then
   if $\bx^*$ is a local minimizer, then the Lagrangian multipliers
   $t_1^*, \dots, t_m^*$ must exist.
```

## Enhanced Fritz-John Conditions

We now introduce a more difficult optimization problem

```{math}
:label: eq-opt-efj-problem
& \text{minimize }  & & f(\bx)\\
& \text{subject to } & & \bx \in C
```
where the constraint set $C$ consists of equality and
inequality constraints as well as an additional abstract
set constraint $X$:

```{math}
:label: eq-opt-efj-constraints
C = X \cap \{\bx \ST g_i(\bx) \leq 0, i=1,\dots,m\}
\cap \{\bx \ST h_j(\bx) = 0, j=1,\dots,p\}.
```
We assume that $f$, $g_i$ and $h_j$ are smooth
functions from $\VV$ to $\RR$
and $X$ is a nonempty closed set.

```{prf:definition} Lagrangian function
:label: def-opt-efj-lagrangian-func

For the optimization problem {eq}`eq-opt-efj-problem`,
the *Lagrangian function* is defined as

$$
L(\bx, \bt, \br) = f(\bx) + \sum_{i=1}^m t_i g_i(\bx)
+ \sum_{j=1}^p r_j h_j(\bx)
$$
where $\bt \in \RR^m$ and $\br \in \RR^p$.
```

### Lagrange Multiplier Vectors

````{prf:definition} Lagrange multiplier vectors
:label: def-opt-constraint-set-efj-lm

We say that a constraint set $C$ as defined in
{eq}`eq-opt-efj-constraints`
*admits Lagrange multipliers* at a point
$\bx^* \in C$ if for every smooth cost
function $f$ for which $\bx^*$ is a local minimum
of the problem {eq}`eq-opt-efj-problem`, there
exist vectors $\bt^* = (t_1^*, \dots, t_m^*)$
and $\br^* = (r_1^*, \dots, r_p^*)$ that
satisfy the following conditions:

```{math}
:label: eq-opt-efj-grad-mult-sum-tan-cone
\left \langle \by, 
\left ( 
   \nabla f(\bx^*) + \sum_{i=1}^m t_i^* \nabla g_i(\bx^*)
   + \sum_{j=1}^p r_j^* \nabla h_j(\bx^*)
\right )
\right \rangle \geq 0,
\quad \Forall \by \in T_X(\bx^*),
```

```{math}
:label: eq-opt-efj-nng-ineq-mult
t_i^* \geq 0, \Forall i=1,\dots,m,
```

```{math}
:label: eq-opt-efj-comp-slack
t_i^* = 0,  \Forall i \ST g_i(\bx^* ) < 0.
```
A pair $(\bt^*, \br^*)$ satisfying these conditions
is called a *Lagrange multiplier vector* corresponding
to $f$ and $\bx^*$.
````

```{div}
1. We also call the Lagrange multiplier vector
   as simply Lagrange multipliers.
1. The condition {eq}`eq-opt-efj-nng-ineq-mult`
   is the *nonnegativity condition* of the
   Lagrangian multipliers for the inequality
   constraints.
1. The condition {eq}`eq-opt-efj-comp-slack`
   is the *complementary slackness* condition.
1. From {eq}`eq-opt-efj-grad-mult-sum-tan-cone`,
   we can see that for each $\by \in T_X(\bx^*)$, the set of 
   Lagrange multiplier vectors corresponding
   to a given $f$ and $\bx^*$ is a closed half-space.
1. Hence, the set of 
   Lagrange multiplier vectors corresponding
   to a given $f$ and $\bx^*$
   is an intersection of closed half spaces.
1. Hence the set of Lagrange multiplier vectors
   is closed and convex. Although it may possibly
   be empty.
1. The condition {eq}`eq-opt-efj-grad-mult-sum-tan-cone`
   is referred to as the *Lagrangian stationarity condition*.
1. It can be viewed as the necessary condition for $\bx^*$
   to be a local minimizer of the function
   $L(\bx, \bt^*, \br^*)$.
   See {prf:ref}`res-opt-tangent-cone-local-minimum`.
1. When $X = \VV$, then $T_X(\bx^*) = \VV$, and this condition
   reduces to

   $$
   \nabla f(\bx^*) + \sum_{i=1}^m t_i^* \nabla g_i(\bx^*)
   + \sum_{j=1}^p r_j^* \nabla h_j(\bx^*) = \bzero.
   $$
1. When $X$ is convex, then {eq}`eq-opt-efj-grad-mult-sum-tan-cone`
   reduces to

   $$
   \left \langle \bx - \bx^*, 
   \left ( 
      \nabla f(\bx^*) + \sum_{i=1}^m t_i^* \nabla g_i(\bx^*)
      + \sum_{j=1}^p r_j^* \nabla h_j(\bx^*)
   \right )
   \right \rangle \geq 0,
   \quad \Forall \bx \in X.
   $$
   1. $X$ is convex. Hence $\alpha (\bx - \bx^*)$ for $\alpha > 0$
      is a feasible direction for every $\bx \in X$.
   1. Hence, if this inequality holds, then
      {eq}`eq-opt-efj-grad-mult-sum-tan-cone` holds for every
      $\bd \in F_C(\bx)$.
   1. Since $X$ is convex, hence $\closure F_C(\bx) = T_C(\bx)$.
   1. If the inequality {eq}`eq-opt-efj-grad-mult-sum-tan-cone`
      holds for every $\bd \in F_C(\bx)$,
      then it will also hold for a closure point of $F_C(\bx)$.
   1. In other words, if $\langle \bx, \ba \rangle \geq 0$
      for every $\bx \in A$, then for any convergent sequence $\{ \bx_k \}$
      of $A$, we have $\lim_{k \to \infty} \langle \bx_k, \ba \rangle \geq 0$.
      Hence the inequality holds for every closure point also.
1. The Lagrangian stationary condition can also be equivalently
   written as

   $$
   -\left ( 
      \nabla f(\bx^*) + \sum_{i=1}^m t_i^* \nabla g_i(\bx^*)
      + \sum_{j=1}^p r_j^* \nabla h_j(\bx^*)
   \right ) \in T_X(\bx^*)^{\circ}.
   $$
   In other words, the negative gradient of the Lagrangian
   function must lie in the polar cone of the tangent cone
   of $X$ at $\bx^*$.
1. Recall from {prf:ref}`res-opt-bno-normal-cone-polar-tangent-cone` that

   $$
   T_X(\bx^*)^{\circ} \subseteq \tilde{N}_X(\bx^*)
   $$
   where $\tilde{N}_X(\bx^*)$ is the normal cone of $X$ at $\bx^*$
   (in the sense of {cite}`bertsekas2003convex`).
1. Hence the negative gradient of the Lagrangian
   function must be a normal direction
   ({prf:ref}`def-opt-bno-normal-dir`) at $\bx^*$.
1. If $X$ is regular at $\bx^*$ ({prf:ref}`res-opt-bno-regular-set`), then
   we also have

   $$
   T_X(\bx^*)^{\circ} = \tilde{N}_X(\bx^*).
   $$
```

### Enhanced Fritz-John Conditions

We are now ready to present the Enhanced Fritz-John conditions
as the necessary conditions for the existence of the
local minimizer of the problem {eq}`eq-opt-efj-problem`.

```{prf:theorem} Enhanced Fritz-John conditions
:label: res-opt-enhanced-fritz-john-cond

Let $\bx^*$ be a local minimizer of the
problem {eq}`eq-opt-efj-problem`-{eq}`eq-opt-efj-constraints`.
Then there exist scalars
$t_0^*,t_1^*, \dots, t_m^*, r_1^*,\dots, r_p^*$
satisfying the following conditions.

1. The gradients satisfy the relation:

   $$
   -\left ( 
      t_0^* \nabla f(\bx^*) + \sum_{i=1}^m t_i^* \nabla g_i(\bx^*)
      + \sum_{j=1}^p r_j^* \nabla h_j(\bx^*)
   \right ) \in \tilde{N}_X(\bx^*).
   $$
1. Nonnegativity: $t_i^* \geq 0$ for every $i=0,\dots,m$.
1. The scalars $t_0^*,t_1^*, \dots, t_m^*, r_1^*,\dots, r_p^*$ are not equal
   to $0$.
1. Complementary violation condition: 
   If the index set $I \cup J$ is not empty, where

   $$
   I = \{i > 0 \ST t_i^* > 0 \}, \quad
   J = \{j  \ST r_j^* \neq 0 \},
   $$
   there exists a sequence $\{ \bx_k \}$ of $X$ that converges
   to $\bx^*$ and is such that for all $k$

   $$
   & f(\bx_k) < f(\bx^*),\\
   & t_i^* g_i (\bx_k) > 0 \Forall i \in I,\\
   & r_j^* h_j(\bx_k) > 0 \Forall j \in J,\\
   & g_i^+(\bx_k) = o(w(\bx_k)) \Forall i \notin I,\\
   & |h_j(\bx_k) | = o(w(\bx_k)) \Forall j \notin J,\\
   $$
   where $g_i^+(\bx) = \max \{ 0, g_i(\bx) \}$ and

   $$
   w(\bx) = \min \left \{
   \min_{i \in I} g_i^+(\bx),
   \min_{j \in J} |h_j(\bx) |
      \right \}.
   $$
```

```{prf:proof}
The proof is based on a quadratic penalty function approach.
For each $k \in \Nat$, we define a penalty function as

$$
F^k(\bx) = f(\bx) + \frac{k}{2} \sum_{i=1}^m (g_i^+(\bx))^2
+ \frac{k}{2} \sum_{j=1}^p (h_j(\bx))^2 
+ \frac{1}{2} \| \bx - \bx^* \|^2.
$$

1. At a feasible point $g_i^+(\bx) = 0$ for every $i=1,\dots,m$
   since $g_i(\bx) \leq 0$.
1. At a feasible point $h_j(\bx) = 0$ for every $j=1,\dots,p$.
1. Hence $F^k(\bx) = f(\bx) + \frac{1}{2} \| \bx - \bx^* \|^2$
   at every feasible point $\bx \in C$.
1. The term $\frac{1}{2} \| \bx - \bx^* \|^2$ is a quadratic
   penalty term penalizing how far we are from the local minimum
   $\bx^*$.
1. The term $\frac{1}{2} (g_i^+(\bx))^2$ is a penalty term
   denoting how strongly the $i$-th inequality constraint is violated.
1. The term $\frac{1}{2} (h_j(\bx))^2$ is a penalty term
   denoting how strongly the $j$-th equality constraint is violated.
1. We have $F^k(\bx) \leq f(\bx)$ for every $\bx \in \VV$.
1. At the local minimizer, we have

   $$
   F^k(\bx^*) = f(\bx^*).
   $$
1. $F^k$ is a continuously differentiable function.
1. We note that

   $$
   \nabla (g_i^+(\bx))^2 = 2 g_i^+(\bx) \nabla g_i(\bx);\\
   \nabla (h_j(\bx))^2  = 2 h_j(\bx) \nabla h_j(\bx).
   $$
1. Hence

   $$
   \nabla F^k(\bx) = \nabla f(\bx) + k \sum_{i=1}^m g_i^+(\bx) \nabla g_i(\bx)
   + k \sum_{j=1}^p h_j(\bx) \nabla h_j(\bx) 
   + (\bx - \bx^*).
   $$

We now introduce the *penalized* problem

$$
& \text{minimize }  & & F^k(\bx)\\
& \text{subject to } & & \bx \in X \cap S
$$
where

$$
S = \{ \bx \ST \|\bx - \bx^* \| \leq \epsilon \}
$$
and $\epsilon > 0$ is a positive scalar such that
$f(\bx^*) \leq f(\bx)$ for all feasible $\bx \in C$
with $\bx \in S$. Such a positive scalar exists
since $\bx^*$ is a local minimizer of $f$. 

1. The set $S$ is compact and the set $X$ is closed.
1. Hence $X \cap S$ is compact.
1. Hence there exists an optimal minimizer of the
   above problem for every $k$.
1. Let $\bx^k$ be a minimizer of $F^k(\bx)$
   over $X \cap S$.
1. Then we have $F^k(\bx^k) \leq F^k(\bx^*)$ for every $k$
   since $\bx^* \in X \cap S$.
1. This is equivalent to

   $$
   F^k(\bx^k) = f(\bx^k) + \frac{k}{2} \sum_{i=1}^m (g_i^+(\bx^k))^2
   + \frac{k}{2} \sum_{j=1}^p (h_j(\bx^k))^2 
   + \frac{1}{2} \| \bx^k - \bx^* \|^2 \leq f(\bx^*)
   $$
   for every $k$.
1. Since $f$ is continuous and $X \cap S$ is compact, hence
   $f(\bx^k)$ is bounded for every $k$.
1. It follows that 

   $$
   & \lim_{k \to \infty} g_i^+(\bx^k) = 0, \quad i=1,\dots,m,\\
   & \lim_{k \to \infty} |h_j(\bx^k)| = 0, \quad j=1,\dots,p,
   $$
   otherwise the term on the L.H.S. of the previous inequality
   will become unbounded and tend to $\infty$ as $k \to \infty$.
1. Hence every limit point $\tilde{\bx}$
   of the sequence $\{ \bx^k \}$ is feasible;
   i.e., $\tilde{\bx} \in C$.
1. Also, since $X \cap S$ is compact, hence every limit
   point $\tilde{\bx}$
   of the sequence $\{ \bx^k \}$ belongs to $X \cap S$.
1. From the inequality $F^k(\bx^k) \leq f(\bx^*)$, we can also see
   that

   $$
   f(\bx^k) + \frac{1}{2} \| \bx^k - \bx^* \|^2 \leq f(\bx^*)
   \quad \Forall k.
   $$
1. Taking the limit as $k \to \infty$, we obtain

   $$
   f(\tilde{\bx}) + \frac{1}{2} \| \tilde{\bx} - \bx^* \|^2 \leq f(\bx^*)
   $$
   for every limit point $\tilde{\bx}$.
1. Since $\tilde{\bx} \in S$ (near local minimizer)
   and $\tilde{\bx} \in C$ (feasible), we have

   $$
   f(\bx^*) \leq f(\tilde{\bx}).
   $$
1. Combining with the previous inequality, it gives us
   
   $$
   \frac{1}{2} \| \tilde{\bx} - \bx^* \|^2  = 0.
   $$
1. Hence, we must have $\bx^* = \tilde{\bx}$.
   Hence, the sequence $\{ \bx_k \}$ has a only one limit point.
1. Thus, the sequence $\{ \bx^k \}$ converges to $\bx^*$.
1. By the definition of the closed ball $S$,
   $\bx^*$ is an interior point of $S$.
1. Since $\lim \bx^k = \bx^*$ it follows that
   $\bx^k$ is an interior point of $S$ for every $k$
   greater than some $k_0$.
1. Hence, due to {prf:ref}`res-opt-tangent-cone-local-minimum`,

   $$
   - \nabla F^k(\bx^k) \in T_C(\bx^k)^{\circ}
   $$
   holds true for every $k > k_0$.
1. We can write $\nabla F^k (\bx^k)$ as

   $$
   \nabla F^k(\bx^k) = \nabla f(\bx^k) + \sum_{i=1}^m \chi^k_i \nabla g_i(\bx^k)
   + \sum_{j=1}^p \xi^k_j \nabla h_j(\bx^k) 
   + (\bx^k - \bx^*)
   $$
   where $\chi^k_i = k g_i^+(\bx^k)$ and $\xi^k_j = k h_j(\bx^k)$.
1. Note that by definition $\chi^k_i \geq 0$ for every $i=1,\dots,m$.
1. Accordingly, we have

   $$
   - \left ( \nabla f(\bx^k) + \sum_{i=1}^m \chi^k_i \nabla g_i(\bx^k)
   + \sum_{j=1}^p \xi^k_j \nabla h_j(\bx^k) 
   + (\bx^k - \bx^*) \right ) \in  T_C(\bx^k)^{\circ}
   $$
   for every $k > k_0$.
1. We define

   $$
   \delta^k = \sqrt{1 + \sum_{i=1}^m (\chi^k_i)^2 + \sum_{j=1}^p (\xi^k_j)^2 }.
   $$
1. By definition $\delta^k \geq 1$.
1. We now introduce

   $$
   & t_0^k = \frac{1}{\delta^k},\\
   & t_i^k = \frac{\chi^k_i}{\delta^k}, i=1,\dots,m,\\
   & r_j^k = \frac{\xi^k_j}{\delta^k}, j=1,\dots,p.   
   $$
1. By dividing by $\delta^k$ in the previous relation, we obtain

   $$
   \bz^k = - \left ( t_0^k \nabla f(\bx^k) + \sum_{i=1}^m t_i^k \nabla g_i(\bx^k)
   + \sum_{j=1}^p r_j^k \nabla h_j(\bx^k) 
   + \frac{1}{\delta_k}(\bx^k - \bx^*) \right ) \in  T_C(\bx^k)^{\circ}
   $$
   for every $k > k_0$
   since $T_C(\bx^k)^{\circ}$ is a cone.
1. Note that by construction, we have

   $$
   (t_0^k)^2 + \sum_{i=1}^m (t_i^k)^2 + \sum_{j=1}^p (r_j^k)^2 = 1.
   $$
1. Hence the sequence $\{ (t_0^k, t_1^k, \dots, t_m^k, r_1^k, \dots, r_p^k) \}$
   is a bounded sequence of $\RR^{1 + m + p}$.
1. Hence, it must have a subsequence that converges to some limit
   $\{ (t_0^*, t_1^*, \dots, t_m^*, r_1^*, \dots, r_p^*) \}$.
1. Let  

   $$
   \bz^* = - \left ( t_0^* \nabla f(\bx^*) + \sum_{i=1}^m t_i^* \nabla g_i(\bx^*)
   + \sum_{j=1}^p r_j^* \nabla h_j(\bx^*) \right ). 
   $$
1. Along this subsequence, we have $\bx^k \to \bx^*$,
   $\bz^k \to \bz^*$ and $\bz^k \in T_X(\bx^k)^{\circ}$
   for every $k > k_0$.
1. Hence, following the definition of the normal cone
   ({prf:ref}`def-opt-bno-normal-cone`),
   after disregarding the first $k_0$ terms of the sequences,
   
   $$
   \bz^* \in \tilde{N}_X(\bx^*).
   $$

(2) Nonnegativity

1. Since $\delta^k \geq 1$, hence $0 < t_0^k = \frac{1}{\delta^k} \leq 1$.
1. Hence $t_0^* \geq 0$.
1. Since $\chi^k_i \geq 0$ for every $i=1,\dots,m$, hence $t_i^k \geq 0$ for every $i=1,\dots,m$.
1. Hence $t_i^* \geq 0$ for every $i=1,\dots,m$.

(3) Not all zero

1. We have established that for every $k$, 

   $$
   (t_0^k)^2 + \sum_{i=1}^m (t_i^k)^2 + \sum_{j=1}^p (r_j^k)^2 = 1.
   $$
1. Taking the limit over the subsequence, we have

   $$
   (t_0^*)^2 + \sum_{i=1}^m (t_i^*)^2 + \sum_{j=1}^p (r_j^*)^2 = 1.
   $$
1. Hence, all of them cannot be zero.


(4) Complementary violation conditions

1. Assume that $I \cup J$ is not empty.
1. Let $\bKKK = \{ k_1, k_2, \dots, \}$ denote the index set of
   the convergent subsequence of $\{ (t_0^k, t_1^k, \dots, t_m^k, r_1^k, \dots, r_p^k) \}$.
1. Let $i \in I$.
   1. We have $t_i^* > 0$.
   1. Then for all sufficient large $k$ in $\bKKK$, we have $t_i^k t_i^* > 0$
      as $t_i^k$ should be sufficiently close to $t_i^*$.
   1. From the definitions of $t_i^k$ and $\chi_i^k$, we must have
       $t_i^k g_i^+(\bx^k) > 0$ for all sufficient large $k$ in $\bKKK$.
   1. By definition, $g_i^+(\bx^k) \geq 0$ and $g_i^+(\bx^k) > 0$
      when $g_i(\bx^k) > 0$.
   1. Hence we must have
       $t_i^k g_i(\bx^k) > 0$ for all sufficient large $k$ in $\bKKK$.
1. Let $j \in J$.
   1. We have $r_j^* \neq 0$.
   1. Then for all sufficiently large $k$ in $\bKKK$, we have $r_j^k \approx r_j^*$.
      Hence $r_j^k \neq 0$ and $r_j^k$ has the same sign as $r_j^*$.
   1. Hence for all sufficiently large $k$ in $\bKKK$, we have
      $r_j^k r_j^* > 0$.
   1. from the definitions of $r_j^k$ and $\xi_j^k$, we see that
      for all sufficiently large $k$ in $\bKKK$, we must have  $r_j^k h_j(\bx^k) > 0$.
1. Hence for all sufficiently large $k$ in $\bKKK$, we have

   $$
   t_i^k g_i(\bx^k) > 0 \Forall i \in I
   \text{ and }
   r_j^k h_j(\bx^k) > 0 \Forall j \in J.
   $$
1. This means that $ g_i^+(\bx^k) > 0$ for every $i \in I$
   and $h_j(\bx^k) \neq 0$ for every $j \in J$ for all sufficiently large $k$ in $\bKKK$.
1. This establishes that for all sufficiently large $k$ in $\bKKK$, we have
   $\bx^k \neq \bx^*$. Otherwise the inequality and equality constraints cannot be violated.
1. Recall that we established that

   $$
   F^k(\bx^k) = f(\bx^k) + \frac{k}{2} \sum_{i=1}^m (g_i^+(\bx^k))^2
   + \frac{k}{2} \sum_{j=1}^p (h_j(\bx^k))^2 
   + \frac{1}{2} \| \bx^k - \bx^* \|^2 \leq f(\bx^*)
   $$
   for every $k$.
1. Hence for all sufficiently large $k$ in $\bKKK$, we must have

   $$
   f(\bx^k) < f(\bx^*)
   $$
   since at least one of $(g_i^+(\bx^k))^2$ and $(h_j(\bx^k))^2$ is positive for every
   sufficiently large $k$.
1. We form the desired sequence $\{ \bx_l \}$ satisfying all the necessary
   criteria by picking up all the entries corresponding to sufficiently large $k$
   in $\bKKK$ from $\{ \bx^k \}$.
1. It remains to show the order property of terms $h_j(\bx^k)$ 
   and $g_i^+(\bx^k)$.
1. For the remaining argument, without loss of generality, we shall
   assume that $\{ \bx^k \}$ is the subsequence chosen above.

TBD the argument below is not complete.

1. We see that

   $$
   (\delta^k)^2 &= 1 + \sum_{i=1}^m (\chi^k_i)^2 + \sum_{j=1}^p (\xi^k_j)^2 \\
   &= 1 + \sum_{i=1}^m (k g_i^+(\bx^k))^2 + \sum_{j=1}^p (k h_j(\bx^k))^2 \\
   & \geq 1 + k w(\bx^k)^2. 
   $$

1. For every $i \notin I$, we have $t_i^* = 0$.
1. Hence $\lim_{k \to \infty} t_i^k = 0$.
1. Hence $\lim_{k \to \infty} \frac{\chi^k_i}{\delta^k} = 0$.
1. Hence

   $$
   \lim_{k \to \infty} \frac{(\chi^k_i)^2}{1 + \sum_{i=1}^m (\chi^k_i)^2 + \sum_{j=1}^p (\xi^k_j)^2} = 0.
   $$
1. Hence

   $$
   \lim_{k \to \infty} \frac{(k g_i^+(\bx^k))^2}{1 + \sum_{i=1}^m (k g_i^+(\bx^k))^2 + \sum_{j=1}^p (h_j(\bx^k))^2} = 0.
   $$
1. We have

   $$
   0 \leq \frac{(k g_i^+(\bx^k))^2}{1 + \sum_{i=1}^m (k g_i^+(\bx^k))^2 + \sum_{j=1}^p (h_j(\bx^k))^2}
   \leq \frac{(k g_i^+(\bx^k))^2}{1 + k w(\bx^k)^2}.
   $$
```