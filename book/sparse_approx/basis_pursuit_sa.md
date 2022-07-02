# Basis Pursuit


## Introduction

We recall following sparse approximation problems.
Given a signal $\bx \in \CC^N$ which is known to have a sparse representation
in a dictionary $\bDDD$,
the exact-sparse recovery problem is:

```{math}
:label: eq:bp:exact_sparse_problem

\widehat{\ba} = \text{arg } \underset{\ba \in \CC^D}{\min} 
\| \ba \|_0 \text{ subject to } \bx = \bDDD \ba.
```

When $\bx \in \CC^N$ doesn't have a sparse representation in $\bDDD$,
a $K$-sparse approximation of $\bx$ in $\bDDD$ 
can be obtained by solving the following problem:

```{math}
:label: eq:bp:sparse_recovery_sparsity_bound

\widehat{\ba} = \text{arg } \underset{\ba \in \CC^D}{\min}
\| \bx - \bDDD \ba \|_2\text{ subject to }  \| \ba \|_0 \leq K.
````
Here $\bx$ is modeled as $\bx = \bDDD \ba + \be$ where $\ba$ denotes
a sparse representation of $\bx$ and $\be$ denotes the approximation error.

````{div}
A different way to formulate the approximation problem is to provide an upper bound
to the acceptable approximation error $\|\be\|_2 \leq \epsilon$
and try to find sparsest possible representation 
within this approximation error bound as

```{math}
:label: eq:bp:sparse_recovery_error_bound

\widehat{\ba} = \text{arg } \underset{\ba \in \CC^D}{\min} 
\| \ba \|_0 \text{ subject to }  \| \bx - \bDDD \ba \|_2 \leq \epsilon.
```
````

`````{div}
*Basis Pursuit* (BP) {cite}`chen1998atomic` suggests the convex relaxation of
{eq}`eq:bp:exact_sparse_problem`
by replacing $\ell_0$-``norm" with $\ell_1$-norm. 

````{math}
:label: eq:bp:bp_l1_norm_minimization
\widehat{\ba} = \text{arg } \underset{\ba \in \CC^D}{\min} 
\| \ba \|_1 \text{ subject to } x = \bDDD \ba.
````
For real signals, it can be implemented as a linear program.
For complex signals, it can be implemented
as a second order cone program.  

In the presence of approximation error {eq}`eq:bp:sparse_recovery_error_bound`, 
where $\bx = \bDDD \ba + \be$ with $\ba$ being
a $K$-sparse approximate representation of $\bx$ in $\bDDD$
we can formulate corresponding $\ell_1$-minimization problem as:

````{math}
:label: eq:bp:bpic_l1_norm_minimization
\widehat{\ba} = \text{arg } \underset{\ba \in \CC^D}{\min} 
\| \ba \|_1 \text{ subject to } \| \bx - \bDDD \ba \|_2 \leq \epsilon
````
where $\epsilon \geq \| \be \|_2$ provides an upper bound on the approximation error. 
This version is known as *basis pursuit with inequality constraints* (BPIC). 

The dual problem constructed using Lagrange multipliers is
````{math}
:label: eq:bp:bpdn_l1_norm_minimization
\widehat{\ba} = \text{arg } \underset{\ba \in \CC^D}{\min} 
\| \ba \|_1 + \lambda \| \bx -  \bDDD \ba \|_2^2.
````
This is known as *basis pursuit denoising*(BPDN).
With appropriate choice of $\lambda$, the
two problems BPIC and BPDN are equivalent.
This formulation attempts to minimize the
$\ell_1$-norm subject to a penalty term over the approximation error.
The Lagrangian  constant $\lambda$ controls
how large the penalty due to approximation error will be.

Note that the constraint $\|\bx - \bDDD \ba \|_2 \leq \epsilon$
is equivalent to
$\|\bx - \bDDD \ba \|_2^2 \leq \epsilon^2$. We have used the squared version to
construct the dual BPDN problem since the term $\| x - \bDDD \ba \|_2^2$ is easier to
differentiate and work with.

Efficient solvers are available to solve
BP, BPIC, BPDN problems using convex optimization techniques. They are usually polynomial time
and involve sophisticated algorithms for implementation. The good part is a guarantee that
a globally unique solution can be found (since the problem is convex). The not so good part is
that convex optimization methods are still quite computationally intensive.

An alternative formulation of BPDN is as follows.
````{math}
:label: eq:bp:bpdn_l1_norm_minimization_gamma
\widehat{\ba} = \text{arg } \underset{\ba \in \CC^D}{\min} 
\frac{1}{2}\| \bx -  \bDDD \ba \|_2^2 + \gamma \| \ba \|_1.
````
The difference in the two formulations is essentially with which term the Lagrangian constant ($\lambda$ or $\gamma$)
is placed.
By choosing $\lambda = 1/ (2 \gamma)$,
the two formulations are essentially the same (with a scale factor
in the objective function).
This formulation attempts to minimize the approximation error
subject to an $\ell_1$-norm penalty.
Thus, the two formulations differentiate w.r.t. which
term is minimized and which term is considered as penalty. 


Basis pursuit is not an algorithm but a principle which says that for most real life problems,
the solution of $\ell_0$-minimization problem is same as the solution of
the corresponding $\ell_1$-minimization problem.
Actual algorithms for solving the basis pursuit formulation of sparse recovery
problem come from convex optimization literature.
`````
