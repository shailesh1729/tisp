# Linear Constraints

This section focuses on optimization problems
where the constraints are linear
(either equality or inequality constraints).
We present the optimality conditions in the
form of special cases of KKT conditions.


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
