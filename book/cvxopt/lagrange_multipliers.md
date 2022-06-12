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
& \text{minimize }   & & f_0(\bx) \\
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
& \text{minimize }   & & f_0(\bx) \\
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





## A Tangent Cones Perspective

```{div}
Consider an optimization problem of the form

$$
& \text{minimize }  & f(\bx)\\
& \text{subject to } & h_i(\bx) = 0, i=1,\dots,m.
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
