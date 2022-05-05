# Convex Constrained Optimization


In this section, we present several results
for the general problem of optimizing
a convex function over a convex set.

Throughout this section, we assume that
$\VV$ is an $n$-dimensional real vector space
endowed with an inner product
$\langle \cdot, \cdot \rangle : \VV \times \VV \to \RR$
and a norm $\| \cdot \| : \VV \to \RR$.

````{div}
Let $f : \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $C \subseteq \VV$ be a convex set.

We are concerned with the optimization problems
of the form

```{math}
:label: eq-cvx-const-cvx-opt-form
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C.
```

Recall from Fermat's optimality condition
({prf:ref}`res-cvxf-subdiff-fermat-optimality`)
that for the unconstrained minimization problem,
$\ba$ is a minimizer of $f$ if and only if
$\bzero$ is a subgradient of $f$ at $\ba$.
````

A similar result can be obtained for the
constrained optimization problem in terms
of the subgradients of $f$ and the normal
cone of $C$.
Recall from {prf:ref}`def-cvx-normal-cone`
that the normal cone to a set $C$ at a point $\ba \in C$
is given by

$$
N_C(\ba) = \{ \bv \in \VV^* \ST 
   \langle \bx - \ba , \bv \rangle \leq 0 
   \Forall \bx \in C \}.
$$

```{prf:theorem} Necessary and sufficient optimality conditions for convex constrained optimization
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
```
