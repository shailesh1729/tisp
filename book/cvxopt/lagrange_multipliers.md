(sec:opt:lagrange:multipliers)=
# Lagrange Multipliers


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
