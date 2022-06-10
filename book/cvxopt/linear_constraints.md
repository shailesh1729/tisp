# Linear Constraints

This section focuses on optimization problems
where the constraints are linear
(either equality or inequality constraints).
We present the optimality conditions in the
form of special cases of KKT conditions.


In the sequel, we present optimality
conditions for the following optimization problems

1. Necessary optimality conditions for the
   minimization of a smooth cost function
   with linear inequality constraints.
1. Necessary and sufficient optimality conditions
   for the minimization of a convex and smooth
   cost function with linear inequality constraints.


## Gordon's Theorem

```{prf:theorem} Gordon's theorem
:label: res-opt-gordon-theorem

Let $\bA \in \RR^{m \times n}$.
Then exactly one of the following two systems has a solution.

1. $\bA \bx \prec \bzero$.
1. $\bp \neq \bzero, \bA^T \bp = \bzero, \bp \succeq \bzero$.
```

```{prf:proof}
(1) $\implies$ not (2)

1. Assume that (1) has a solution given by $\bx$.
1. For contradiction, assume that (2) also has a solution.
1. Hence, there exists a nonzero $\bp$ such that
   $\bA^T \bp = \bzero$ and $\bp \succeq \bzero$.
1. Multiplying the equality $\bA^T \bp = \bzero$ from left
   by $\bx$, we get

   $$
   \bx^T \bA^T \bp = (\bA \bx)^T \bp = 0.
   $$
1. Since $\bA \bx \prec \bzero$ and $\bp \succeq \bzero$,
   hence every term in $\bA \bx$ is negative and
   every term in $\bp$ is nonnegative.
1. Hence $(\bA \bx)^T \bp = 0$ is possible only if
   $\bp = \bzero$. A contradiction.
1. Hence (2) doesn't have a solution.


not (1) $\implies$ (2)

1. Assume that (1) doesn't have a solution.
1. The system (1) is equivalent to the system

   $$
   & \bA \bx + s \bone \preceq \bzero;\\
   & s > 0.
   $$
1. Define $\tilde{\bA} = \begin{bmatrix} \bA & \bone \end{bmatrix}$.
1. Let $\bc = \be_{n + 1}$ (i.e., $(0, 0, \dots, 0, 1)$.
1. Then the above system is equivalent to

   $$
   \tilde{\bA} \begin{bmatrix} \bx \\ s \end{bmatrix}
   \preceq \bzero, \quad
   \bc^T \begin{bmatrix} \bx \\ s \end{bmatrix} > 0.
   $$
1. The infeasibility of (1) is thus equivalent
   to the infeasibility of the system

   $$
   \tilde{\bA}  \bw \preceq \bzero, \quad
   \bc^T \bw > 0
   $$
   where $\bw \in \RR^{n+1}$.
1. Since this system is infeasible, hence
   by {prf:ref}`Farkas' lemma <res-cvx-farkas-lemma>`,
   the system

   $$
   \tilde{\bA}^T \bz = \bc, \quad \bz \succeq \bzero
   $$
   must have a solution.
1. In other words, there exists $\bz \succeq \bzero$
   such that

   $$
   \bA^T \bz = \bzero, \quad \bone^T \bz = 1.
   $$
1. Since $\bone^T \bz = 1$, hence $\bz \neq \bzero$.
1. Thus, there exists $\bz \neq \bzero$, with $\bz \succeq \bzero$
   such that $\bA^T \bz = \bzero$.
1. Hence, the system (2) has a solution $\bz$.
```


## Smooth Cost Function, Linear Inequality Constraints

````{prf:theorem} KKT necessary optimality conditions for linearly constrained problems
:label: res-opt-kkt-smooth-lin-ineq

Consider an optimization problem of the form

```{math}
:label: eq-opt-smooth-lin-ineq
& \text{minimize }  & & f(\bx) & \\
& \text{subject to } & & \langle \bx, \ba_i \rangle \leq b_i, i=1,\dots,m &.
```
where $f$ is continuously differentiable over $\RR^n$,
$\ba_1, \dots, \ba_m \in \RR^n$ and $b_1, \dots, b_m \in \RR$.
Assume that $\bx^*$ is a local minimum of this optimization problem.
Then there exist nonnegative scalars $t_1, \dots, t_m \geq 0$
such that 

```{math}
:label: eq-opt-smooth-lin-ineq-gradient-eq
\nabla f(\bx^*) + \sum_{i=1}^m t_i \ba_i = \bzero
```
and 

```{math}
:label: eq-opt-smooth-lin-ineq-complementarity
t_i (\langle \bx^*, \ba_i \rangle - b_i ) = 0, \quad i=1,\dots,m.
```
````

```{prf:proof}
We are given that $\bx^*$ is a local minimum point of {eq}`eq-opt-smooth-lin-ineq`.

1. Let $C$ denote the constraint set

   $$
   C = \{\bx \in \RR^n \ST  \langle \bx, \ba_i \rangle \leq b_i, i=1,\dots,m \}.
   $$
1. By {prf:ref}`res-opt-over-c-local-min-stationary`, $\bx^*$ must
   be a stationary point.
1. Hence for every $\bx \in C$, we have

   $$
   \langle \bx - \bx^* , \nabla f(\bx^*) \rangle \geq 0.
   $$
1. Introduce a change of variable $\by = \bx - \bx^*$ in the
   stationary point criterion.
1. We must have $\langle \by, \nabla f(\bx^*) \rangle \geq 0$
   for every $\by$ satisfying $\langle \by + \bx^* , \ba_i \rangle \leq b_i$
   for every $i=1,\dots,m$.
1. Equivalently, we must have $\langle \by, \nabla f(\bx^*) \rangle \geq 0$
   for every $\by$ satisfying
   
   $$
   \langle \by, \ba_i \rangle \leq b_i - \langle \bx^*, \ba_i \rangle,
   \quad \Forall i=1,\dots,m.
   $$
1. The $i$-th linear inequality  constraint is called active at $\bx^*$
   if $\langle \bx, \ba_i \rangle = b_i$.
1. The $i$-the constraint is called inactive if
   $\langle \bx, \ba_i \rangle < b_i$.
1. Let the set of active constraints be denoted by

   $$
   I(\bx^*) = \{i \ST \langle \bx^*, \ba_i \rangle = b_i \}.
   $$
1. If the $i$-th constraint is active, then
   $\langle \by + \bx^* , \ba_i \rangle \leq b_i$ is equivalent to
   $\langle \by, \ba_i \rangle \leq 0$.
1. If the $i$-th constraint is inactive, then
   $\langle \by + \bx^* , \ba_i \rangle \leq b_i$ is equivalent to
   $\langle \by, \ba_i \rangle \leq b_i - \langle \bx^*, \ba_i \rangle$
   a positive quantity.
1. Thus, we must have $\langle \by, \nabla f(\bx^*) \rangle \geq 0$
   whenever $\by$ satisfies

   $$
   & \langle \by, \ba_i \rangle \leq 0, & i \in I(\bx^*), \\ 
   & \langle \by, \ba_i \rangle \leq b_i - \langle \bx^*, \ba_i \rangle, 
   & i \notin I(\bx^*). 
   $$
1. We claim that the second set of inequalities are redundant.
   1. Suppose that we pick a $\by$ such that
      $\langle \by, \ba_i \rangle \leq 0, \Forall i \in I(\bx^*)$.
   1. At $\bx^*$, we have $b_i - \langle \bx^*, \ba_i \rangle > 0$
      for every $i \notin I(\bx^*)$.
   1. Then it is possible to choose a small enough $\alpha > 0$ such that
      $\langle \alpha \by, \ba_i \rangle \leq b_i - \langle \bx^*, \ba_i \rangle$
      for every $i$.
      1. We can choose an $\alpha_i$ for every $i$ as follows.
      1. If $\langle \by, \ba_i \rangle \leq 0$, then let $\alpha_i = 1$.
      1. If $\langle \by, \ba_i \rangle > 0$, then let

         $$
         \alpha_i = \frac{b_i - \langle \bx^*, \ba_i \rangle}{\langle \by, \ba_i \rangle}.
         $$
      1. Let $\alpha = \min\{ \alpha_1, \dots, \alpha_m \}$.
   1. We can now see that

      $$
      & \langle \by, \ba_i \rangle \leq 0 \Forall i \in I(\bx^*)\\
      \implies & \langle \alpha \by, \ba_i \rangle
      \leq b_i - \langle \bx^*, \ba_i \rangle \Forall i=1,\dots,m.
      $$
   1. But then by stationarity of $\bx^*$, we must have
      $\langle \alpha \by, \nabla f(\bx^*) \rangle \geq 0$.
   1. Since $\alpha > 0$, hence we must have
      $\langle \by, \nabla f(\bx^*) \rangle \geq 0$.
1. Hence, we must have  $\langle \by, \nabla f(\bx^*) \rangle \geq 0$
   whenever $\by$ satisfies

   $$
   \langle \by, \ba_i \rangle \leq 0, \quad \Forall i \in I(\bx^*).
   $$
1. We are ready to apply the Farkas' lemma {prf:ref}`res-cvx-farkas-lemma`.

   1. Form $\bA$ by combining $-\ba_i$ for every $i \in I(\bx^*)$ as columns.
   1. Let $\bv = \nabla f(\bx^*)$.
   1. We have $\bA^T \by \succeq 0 \implies \by^T \bv\geq 0$.
   1. Hence the system $\bA^T \by \succeq 0, \by^T \bv < 0$ is infeasible.
   1. Hence there exists $\bt \succeq \bzero$ such that $\bA \bt = \bv$.
1. Hence there exists $t_i \geq 0$ for every $i \in I(\bx^*)$ such that
   
   $$
   - \nabla f(\bx^*) = \sum_{i \in I(\bx^*)} t_i \ba_i.
   $$
1. By defining $t_i = 0$ for every $i \notin I(\bx^*)$, we have

   $$
   t_i (\langle \bx^*, \ba_i \rangle - b_i) = 0  \quad \Forall i=1,\dots,m
   $$
   and

   $$
   \nabla f(\bx^*) + \sum_{i=1}^m t_i \ba_i = \bzero
   $$
   as desired.
```


## Convex and Smooth Cost Function, Linear Inequality Constraints

````{prf:theorem} KKT necessary and sufficient optimality conditions for linearly constrained problems
:label: res-opt-kkt-smooth-convex-lin-ineq

Consider an optimization problem of the form

$$
& \text{minimize }  & & f(\bx) & \\
& \text{subject to } & & \langle \bx, \ba_i \rangle \leq b_i, i=1,\dots,m &.
$$

where $f$ is a convex continuously differentiable over $\RR^n$,
$\ba_1, \dots, \ba_m \in \RR^n$ and $b_1, \dots, b_m \in \RR$.
Let $\bx^*$ be a feasible solution of this optimization problem.
Then $\bx^*$ is an optimal solution
if and only if
there exist nonnegative scalars $t_1, \dots, t_m \geq 0$
such that 

$$
\nabla f(\bx^*) + \sum_{i=1}^m t_i \ba_i = \bzero
$$
and 

$$
t_i (\langle \bx^*, \ba_i \rangle - b_i ) = 0, \quad i=1,\dots,m.
$$
````

```{prf:proof}
Assume that $\bx^*$ is an optimal solution.
Then it is also a local minimizer.
Then the necessary conditions follow from
{prf:ref}`res-opt-kkt-smooth-lin-ineq`.


For the converse, assume that $\bx^*$ is a feasible solution
and the conditions for the scalars $t_1, \dots, t_m$ are
satisfied.

1. Consider any feasible solution $\bx$.
1. Define a function

   $$
   h(\bx) = f(\bx) + \sum_{i=1}^m t_i (\langle \bx, \ba_i \rangle - b_i).
   $$
1. By differentiating w.r.t. $\bx$, we have

   $$
   \nabla h(\bx) = \nabla f(\bx) + \sum_{i=1}^m t_i \ba_i.
   $$
1. By hypothesis we have, $\nabla h(\bx^*) = 0$.
1. Since $h$ is convex, hence by
   {prf:ref}`res-cvxopt-diff-convex-optimal-unconstrained`,
   $\bx^*$ is a minimizer of $h$ over $\RR^n$.
1. By hypothesis, we have
   $t_i (\langle \bx^*, \ba_i \rangle - b_i ) = 0, \quad i=1,\dots,m$.
1. Hence

   $$
   \sum_{i=1}^m t_i (\langle \bx^*, \ba_i \rangle - b_i ) = 0.
   $$
1. For any feasible point, we have 
   $\langle \bx, \ba_i \rangle \leq b_i$ for every $i$.
1. Since by hypothesis $t_i \geq 0$, hence for any feasible point,
   
   $$
   \sum_{i=1}^m t_i (\langle \bx, \ba_i \rangle - b_i ) \leq 0.
   $$
1. Hence
   
   $$
   f(\bx^*) 
   &= f(\bx^*) + \sum_{i=1}^m t_i (\langle \bx^*, \ba_i \rangle - b_i )\\
   &= h(\bx^*) \\
   &\leq h(\bx)\\
   &= f(\bx) + \sum_{i=1}^m t_i (\langle \bx, \ba_i \rangle - b_i )\\
   &\leq f(\bx).
   $$
1. Hence for every feasible solution $\bx$, we have
   $f(\bx^*) \leq f(\bx)$.
1. This proves that $\bx^*$ is a global optimal solution.
```
