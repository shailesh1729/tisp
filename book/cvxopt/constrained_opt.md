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
````

## General Optimality Conditions

Recall from Fermat's optimality condition
({prf:ref}`res-cvxf-subdiff-fermat-optimality`)
that for the unconstrained minimization problem,
$\ba$ is a minimizer of $f$ if and only if
$\bzero$ is a subgradient of $f$ at $\ba$.

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
   1. Pick any $j \in 1,\dots,n$ such that $j \neq i$.
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
   1. In other words, $g_i = \mu$ for all $i \in 1,\dots,n$ such that $x_i^* > 0$.
   1. Now consider some $k \in 1,\dots,n$ such that $x_k = 0$.
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
   1. Thus, $g_i \geq \mu$ for all $i \in 1,\dots,n$ such that $x^*_i = 0$.
   1. Thus, we have established that $\bg$ indeed satisfies {eq}`eq-opt-cvx-unit-simplex-cond`.
```
