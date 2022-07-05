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
We start our discussion with the analysis of exact-sparse case.

As part of our theoretical analysis, we would like to explore conditions under which
the problems {eq}`eq:bp:exact_sparse_problem` and 
{eq}`eq:bp:bp_l1_norm_minimization` are equivalent i.e. there exists
a unique solution to both of them and the solution is identical.
Under such conditions, the NP-hard problem {eq}`eq:bp:exact_sparse_problem`
can be easily replaced with a tractable {eq}`eq:bp:bp_l1_norm_minimization`
problem which is convex and solvable in polynomial time.

## Two-Ortho-Case
````{div}
Further simplifying, we consider the case where the dictionary $\bDDD$
is a two-ortho-basis

$$
\bDDD = \begin{bmatrix} \Psi & \Phi \end{bmatrix}
$$
with $\Psi$ and  $\Phi$  both being orthonormal bases for $\CC^N$.

1. Clearly, $\bDDD \in \CC^{N \times 2N}$ and $D = 2N$.
1. We denote

    $$
    \Omega = \{ 1, 2, \dots, 2N \}
    $$
    as the index set for the representation vectors $\ba$.
1. The representation $\ba$ of a signal $x$ in $\bDDD$ can be written as

    $$
    \bx = \bDDD \ba 
    = \begin{bmatrix} \Psi & \Phi \end{bmatrix} 
    \begin{bmatrix} \ba^p \\ \ba^q \end{bmatrix}
    = \Psi \ba^p + \Phi \ba^q.
    $$
1. We can assign

    $$
    k_p = \| \ba^{p} \|_0  \quad \text{and} \quad k_q  = \| \ba^{q} \|_0.
    $$
1. Total sparsity of $\ba$ is given by

    $$
    K = \| \ba \|_0 = k_p + k_q.
    $$
1. Whenever $K \ll N$, we have a sparse representation.
1. Further, let $S_p \subseteq \{ 1 , \dots, N \}$
    be the support corresponding to $\ba^p$ part of $\ba$
    (i.e. $S_p = \supp (\ba^p)$)
    and $S_q \subseteq \{ 1 , \dots, N \}$
    be the support corresponding to $\ba^q$ part of $\ba$
    (i.e. $S_q = \supp (\ba^q))$.
1. Clearly, $|S_p| = k_p$ and $|S_q | = k_q$.
1. Note that $S_p$ and $S_q$ need not be disjoint.
1. But, $S_p$ and $S_q + N$ are disjoint.
1. In fact, $\supp(\ba) = S_p \cup (S_q + N)$.
1. $\OneVec_p \in \CC^N$ will denote the indicator vector for $S_p$;
   i.e., $\OneVec_p(i) = 0 \Forall i \notin S_p$ 
   and $\OneVec_p(i) = 1 \Forall i \in S_p$.
1. Similarly, $\OneVec_q \in \CC^N$ will denote
   the indicator  vector for $S_q$.
1. $\OneVec \in \CC^N$ will denote the vector $\{ 1, \dots, 1 \}$.
1. Also, $\OneMat \in \CC^{N \times N}$ will denote a square matrix of all ones.
1. Note that $\OneMat = \OneVec \cdot \OneVec^T$.

We now state our main result for equivalence of solutions of 
{eq}`eq:bp:exact_sparse_problem` and 
{eq}`eq:bp:bp_l1_norm_minimization` for the two ortho-case.
Going forward, 
we will simply use $\mu$ to refer to the coherence of $\bDDD$ (i.e. $\mu (\bDDD)$).
`````

````{prf:theorem}
:label: res:bp:two_ortho_exact_recovery_coherence

Let $\bDDD$ be a two-ortho-basis dictionary
$\bDDD = \begin{bmatrix} \Psi & \Phi \end{bmatrix}$.
Let $\bx = \bDDD \ba$, where $\bx$ is known. 
If a $K$-sparse representation $\ba$ exists 
with $k_p \geq k_q$ such that ($k_p, k_q$) obey

```{math}
:label: eq:bp:bp_exact_sparse_two_ortho_case_condition
2 \mu^2 k_p k_q  + \mu k_p - 1 < 0;
```
then $\ba$ is the unique solution of both problems
{eq}`eq:bp:exact_sparse_problem` and 
{eq}`eq:bp:bp_l1_norm_minimization`.

A weaker condition is: 
If 
```{math}
:label: eq:bp:two_ortho_exact_recovery_coherence_simple
\| \ba \|_0 = K  = k_p + k_q < \frac{\sqrt{2} - 0.5}{\mu};
```
then $\ba$ is a unique ($K$-sparse) solution to both
{eq}`eq:bp:exact_sparse_problem` and 
{eq}`eq:bp:bp_l1_norm_minimization`.
````

````{prf:proof}
We first show that $\ba$ is a unique solution of {eq}`eq:bp:exact_sparse_problem`.

1. Towards the end of this proof, we show that
   {eq}`eq:bp:bp_exact_sparse_two_ortho_case_condition` $\implies$
   {eq}`eq:bp:two_ortho_exact_recovery_coherence_simple`.
1. Due to {eq}`eq:bp:two_ortho_exact_recovery_coherence_simple`, 
   
   $$
    \| \ba \|_0 = K = k_p + k_q < \frac{\sqrt{2} - 0.5}{\mu} 
    = \frac{0.414}{\mu} < \frac{1}{\mu}.
   $$
1. Thus, if $\ba$ satisfies {eq}`eq:bp:bp_exact_sparse_two_ortho_case_condition`,
   then it is necessarily the sparsest possible representation
   of $\bx$ in $\bDDD$
   due to {prf:ref}`res-ssm-sparse-unique-2onb`.
1. All other representations are denser
   (i.e. have more non-zero entries).
1. Hence $\ba$ is a unique solution of {eq}`eq:bp:exact_sparse_problem`.

We next show that $\ba$ is also a unique solution of
{eq}`eq:bp:bp_l1_norm_minimization`.

1. $\ba$ is a feasible vector to {eq}`eq:bp:bp_l1_norm_minimization`
   since $\bx = \bDDD \ba$
   though it need not be an optimal solution.
1. We have to find criteria under which $\ba$ is optimal
   and no other feasible vector $\bb$ is optimal.
1. Since $\ba$ is the unique solution to {eq}`eq:bp:exact_sparse_problem`,
   hence $\| \bb \|_0 > \| \ba \|_0$ for every other
   feasible $\bb$ for {eq}`eq:bp:bp_l1_norm_minimization`.
1. We consider the set of alternative feasible vectors
   to {eq}`eq:bp:bp_l1_norm_minimization` given by
   
   $$
    C = \left \{ \bb \ST \bb \neq \ba, \| \bb \|_1 
        \leq \| \ba \|_1, \| \bb \|_0 > \| \ba \|_0 \text{ and } 
        \bDDD (\ba - \bb) = \bzero 
    \right \}.
   $$
   This set contains all feasible vectors to
   {eq}`eq:bp:bp_l1_norm_minimization` which are
   1. different from $\ba$
   1. have larger support (larger $\ell_0$-"norm")
   1. satisfy the linear system of equations $\bx = \bDDD \ba$
   1. have $\ell_1$ norm less than or equal to $\ba$.
1. If this set is nonempty, then there exists a solution to basis pursuit
   which is not same as $\ba$.
1. If this set is empty, then the solutions of
   {eq}`eq:bp:exact_sparse_problem` and 
   {eq}`eq:bp:bp_l1_norm_minimization`  coincide
   and are both unique. 
1. Writing $\be = \bb - \ba \iff \bb = \be + \ba$, we have
   
   $$
    \| \bb \|_1 \leq \| \ba \|_1 \iff  \| \be + \ba \|_1 - \| \ba \|_1 \leq 0.
   $$
1. Thus, we can rewrite $C$ as 
   
   $$
   C_s = \{ \be \ST \be \neq \bzero,
    \| \be + \ba \|_1 - \| \ba \|_1 \leq 0 \text{ and } \bDDD \be = \bzero\}.
   $$
1. In order to show that $C$ is empty, 
   we will show that a larger set containing $C_s$
   is also empty.
1. Essentially, we wish to consider a larger set whose emptiness can be
   checked easily against {eq}`eq:bp:bp_exact_sparse_two_ortho_case_condition`. 
1. If that larger set is empty due to
   {eq}`eq:bp:bp_exact_sparse_two_ortho_case_condition`,
   then $C$ would also be empty and we would have completed the proof.

Emptiness of $C_s$

1. We start by the requirement $\| \be + \ba \|_1 - \| \ba \|_1 \leq 0$.
1. Let $\ba = \begin{bmatrix} {\ba^p} \\ {\ba^q} \end{bmatrix}$ 
   and $\be = \begin{bmatrix} {\be^p} \\ {\be^q} \end{bmatrix}$ ,
   where $p$ and $q$ refer to parts corresponding to the orthonormal bases
   $\Psi$ and $\Phi$ respectively
   (as described at the beginning of this section).
1. Note that even if $\ba^p$ and $\ba^q$ are sparse,
   $\be^p$ and $\be^q$ need not be.
1. In fact, support of $\be^p$ and $\be^q$ could be very different from
   $S_p$ and $S_q$.
1. We can now write
   
   $$
    0 \geq \| \be + \ba \|_1 - \| \ba \|_1 
    &= \left ( \sum_{i=1}^N |e^p_i + a^p_i | - | a^p_i | \right )
    + \left ( \sum_{i=1}^N |e^q_i + a^q_i | - | a^q_i | \right ) \\
    &= \sum_{i \notin S_p} |e^p_i | + \sum_{i \notin S_q} |e^q_i | \\
    &+  \left ( \sum_{i \in S_p} |e^p_i + a^p_i | - | a^p_i | \right )
    + \left ( \sum_{i \in S_q} |e^q_i + a^q_i | - | a^q_i | \right ).
   $$
   We are splitting the sum as follows.
   1. We first split the sum into $\be^p, \ba^p$ and $\be^q, \ba^q$ parts.
   1. We split the sum on the $p$ part to sum over indices in $S_p$
      and indices not in $S_p$.
   1. We split the sum on the $q$ part to sum over indices in $S_q$
      and indices not in $S_q$.
   1. For $i \notin S_p$, $a^p_i = 0$ leading to
      $|e^p_i + \ba^p_i | - | \ba^p_i | = |e^p_i |$.
   1. Ditto for $i \notin S_q$.
1. We recall from triangle inequality on complex numbers that

   $$
   |x + y | \geq |y| - |x| \Forall x, y \in \CC
   $$ 
   which implies $|x + y| - |y|  \geq - |x|$. 
1. Thus, 
   
   $$
     |e^p_i + a^p_i | - | a^p_i | \geq - | e^p_i  |  \Forall i \in S_p
   $$
   and
   
   $$
     |e^q_i + a^q_i | - | a^q_i | \geq - | e^q_i  |  \Forall i \in S_q.
   $$
1. With this, the above condition can be relaxed as
   
   $$
    0 \geq \| \be + \ba \|_1 - \| \ba \|_1
    \geq \sum_{i \notin S_p} |e^p_i | + \sum_{i \notin S_q} |e^q_i| 
    - \sum_{i \in S_p} |e^p_i | - \sum_{i \in S_q} |e^q_i|.
   $$
1. Every $\be$ satisfying this inequality will also satisfy the condition
   $\| \be + \ba \|_1 - \| \ba \|_1 \leq 0$. 
1. To simplify notation we can write
   
   $$
    \sum_{i \in S_p} |e^p_i | = \OneVec_p^T | \be^p | 
    \text{ and } 
    \sum_{i \in S_q} |e^q_i|  = \OneVec_q^T | \be^q |.
   $$
1. Then we have
   
   $$
    \|\be^p \|_1 = \sum_{i \in S_p} |e^p_i | + \sum_{i \notin S_p} |e^p_i |
    \iff \sum_{i \notin S_p} |e^p_i |
    = \|\be^p \|_1 - \sum_{i \in S_p} |e^p_i | = \|\be^p \|_1  - \OneVec_p^T | \be^p |.
   $$
1. Similarly,
   
   $$
    \sum_{i \notin S_q} |e^q_i | =  \|\be^q \|_1  - \OneVec_q^T | \be^q |.
   $$
1. Thus,
   
   $$
    \sum_{i \notin S_p} |e^p_i | + \sum_{i \notin S_q} |e^q_i| 
    - \sum_{i \in S_p} |e^p_i | - \sum_{i \in S_q} |e^q_i| 
    = \|\be^p \|_1  - 2 \OneVec_p^T | \be^p |
    + \|\be^q \|_1  - 2 \OneVec_q^T | \be^q |.
   $$
1. We can now define the set
   
   $$
    C_s^1  = \{ \be \ST \be \neq \bzero,
        \|\be^p \|_1 + \|\be^q \|_1 - 2 \OneVec_p^T | \be^p |
      - 2 \OneVec_q^T | \be^q | \leq 0  \text{ and } \bDDD \be = \bzero\}.
   $$
1. Clearly, $C_s \subseteq C_s^1$ and
   if $C_s^1$ is empty, then $C_s$ will also be empty.
1. Note that this formulation of $C_s^1$ is dependent only on the support of
   $\ba$ and not on values in $\ba$.
1. We now turn back to the requirement $\bDDD \be = \bzero$ and relax it further.
1. We note that,
   
   $$
    \bDDD \be 
    = \begin{bmatrix} \Psi & \Phi \end{bmatrix} 
    \begin{bmatrix} \be^p \\ \be^q \end{bmatrix} 
    = \Psi \be^p 
    + \Phi \be^q = \bzero.
   $$
1. Multiplying by $\Psi^H$ we get
   
   $$
   \be^p + \Psi^H \Phi \be^q = \bzero \iff  \be^p = - \Psi^H \Phi \be^q
   $$
   since $\Psi^H \Psi = \bI$ (unitary matrix).
1. Similarly multiplying with $\Phi^H$, we obtain
   
   $$
    \Phi^H \Psi \be^p + \be^q = \bzero \iff \be^q = - \Phi^H \Psi \be^p.
   $$
1. Note that entries in $\Psi^H \Phi$ and $\Phi^H \Psi$ are 
   inner products between columns of $\bDDD$, hence their magnitudes
   are upper bounded by $\mu$ (coherence).
1. Denote $\bB = \Psi^H \Phi$
   and consider the product $\bv = \Psi^H \Phi \be^q = \bB \be^q$.
1. Then
   
   $$
    v_i = \sum_{j = 1}^N B_{i j} e^q_j.
   $$
1. Thus, 
   
   $$
    | v_i | = \left | \sum_{j = 1}^N B_{i j} e^q_j \right | 
    \leq \sum_{j = 1}^N | B_{i j} e^q_j | 
    \leq \mu \sum_{j = 1}^N  | e^q_j | 
    = \mu\OneVec^T | \be^q |.
   $$
1. Applying this result on $\be^p$ we get, 
   
   $$
    | \be^p  | = | \Psi^H \Phi \be^q | \preceq \mu \OneMat | \be^q |.
   $$
1. Similarly,
   
   $$
    | \be^q  | = | \Phi^H \Psi \be^p | \preceq \mu \OneMat | \be^p |.
   $$
1. Note that since $\OneMat = \OneVec \cdot \OneVec^T$, it is a rank-1 matrix.
1. We now construct a set $C_s^2$ as 
   
   $$
    C_s^2 = \left \{ \be  \left |  
    \begin{aligned}
    \be \neq \bzero\\
    \|\be^p \|_1 + \|\be^q \|_1 - 2 \OneVec_p^T | \be^p |
      - 2 \OneVec_q^T | \be^q | \leq 0\\
    | \be^p  | \preceq \mu \OneMat | \be^q |\\
    \text { and }| \be^q  | \preceq \mu \OneMat | \be^p |
    \end{aligned}
    \right.
    \right \}.
   $$
1. Clearly, $C_s^1 \subseteq C_s^2$
   since for every $\be \in C_s^1$,
   $\bDDD \be = \bzero \implies \be \in C_s^2$.
1. We now define $\bf^p = | \be^p | $ and $\bf^q = | \be^q |$
   as the absolute value vectors.
1. Correspondingly, let us define
   
   $$
   \bf = | \be | = \begin{bmatrix} \bf^p \\ \bf^q \end{bmatrix}.
   $$
1. Clearly, $ \| \be^p \|_1 = \OneVec^T \bf^p$
   and $ \| \be^q \|_1 = \OneVec^T \bf^q$.
1. Further $\bf^p \succeq \ZeroVec$; i.e., every entry in $\bf^p$ is nonnegative.
1. Similarly, $\bf^q \succeq \ZeroVec$.
1. We can then introduce a set $C_f$ as 
   
   $$
    C_f = \left \{ \bf  \left | 
    \begin{aligned}
    \bf \neq \bzero\\
    \OneVec^T \bf^p + \OneVec^T \bf^q - 2 \OneVec_p^T \bf^p
      - 2 \OneVec_q^T \bf^q \leq 0\\
    \bf^p \preceq \mu \OneMat \bf^q\\
    \bf^q \preceq \mu \OneMat \bf^p\\
    \text { and } \bf^p \succeq \ZeroVec, \bf^q \succeq \ZeroVec
    \end{aligned}
    \right.
    \right \}.
   $$
1. It is easy to see that if $\be \in C_s^2$ then $\bf = |\be| \in C_f$.
1. Thus, if $C_f$ is empty, then $C_s^2$ should be empty too.
1. We note that if $\bf \in C_f$, then for all $c > 0$, 
   $c \bf \in C_f$.
1. Thus, in order to study (the emptiness of) $C_f$, it is
   sufficient to study unit $\ell_1$-norm vectors $\bf \in C_f$;
   i.e., there is no unit $\ell_1$-norm vector in $C_f$, if and only if
   $C_f$ is empty.
1. Now 
   
   $$
    \| \bf \|_1 = \OneVec^T \bf  = \OneVec^T \bf^p + \OneVec^T \bf^q
   $$
   since $\bf \succeq \ZeroVec$.  
1. This leads to:
   
   $$
    \| \bf \|_1 =  1 \iff \OneVec^T \bf^p + \OneVec^T \bf^q = 1.
   $$
1. We construct the new set of unit $\ell_1$-norm vectors
   
   $$
    C_r = \left \{ f  \left | 
    \begin{aligned}
    \bf \neq \bzero\\
    1 - 2 \OneVec_p^T \bf^p
      - 2 \OneVec_q^T \bf^q \leq 0\\
    \bf^p \preceq \mu \OneMat \bf^q\\
    \bf^q \preceq \mu \OneMat \bf^p\\
    \OneVec^T \bf^p + \OneVec^T \bf^q = 1 \\
    \text { and } \bf^p \succeq \ZeroVec, \bf^q \succeq \ZeroVec
    \end{aligned}
    \right.
    \right \}.
   $$
1. We have $C_r = \EmptySet \iff C_f = \EmptySet$.
1. Note that the constraint 
   $1 - 2 \OneVec_p^T \bf^p - 2 \OneVec_q^T \bf^q \leq 0$
   can be rewritten as
   
   $$
    \OneVec_p^T \bf^p + \OneVec_q^T \bf^q \geq \frac{1}{2}.
   $$
1. The set $C_r$ is much easier to analyze since
   * If has no explicit dependency on $\bDDD$.
     $\bDDD$ is represented only by a single parameter, its coherence $\mu$.
   * All constraints are simple linear constraints. Thus finding
    the elements of $C_f$ can be formulated as a
    linear programming (feasibility) problem.
   * The order of non-zero entries inside $\bf^p$ and $\bf^q$ doesn't have
     any influence on the requirements for $\bf$ to belong to $C_r$.
     Thus, without loss of generality,
     we can focus on vectors for which the first
     $k_p$ entries are non-zero in $\bf^p$ and first $k_q$ entries are
     non-zero in $\bf^q$ respectively.
1. We next verify that $C_r$ must be empty under
   {eq}`eq:bp:bp_exact_sparse_two_ortho_case_condition`.

Emptiness of $C_r$

1. In order to find vectors in $C_r$, we can solve the following linear program.

   ```{math}
    :label: eq:bp:bp:exact_matching_linear_program
    & \underset{\bf^p, \bf^q}{\text{maximize }}
    & & \OneVec_p^T \bf^p + \OneVec_q^T \bf^q \\
    & \text{subject to }
    & & \bf^p \preceq \mu \OneMat \bf^q\\
    & & & \bf^q \preceq \mu \OneMat \bf^p\\
    & & & \OneVec^T (\bf^p + \bf^q) = 1\\
    & & & \bf^p \succeq \ZeroVec, \bf^q \succeq \ZeroVec.
    ```
1. $\bf = \bzero$ is a feasible vector for this linear program,
   hence a solution does exist for this program.
1. What is interesting is the value of the objective function for the optimal solution.
1. Let ${\bf^p}^*, {\bf^q}^*$ be (an) optimal solution for this linear
   program.
1. If $\OneVec_p^T {\bf^p}^* + \OneVec_q^T {\bf^q}^* \geq \frac{1}{2}$,
   then $\bf^*$ satisfies all the requirements of $C_r$ and $C_r$ is indeed
   not empty.
1. This doesn't guarantee that $C$ will also be non-empty though.
1. On the contrary, if $\OneVec_p^T {\bf^p}^* + \OneVec_q^T {\bf^q}^* < \frac{1}{2}$,
   then $C_r$ is indeed empty (as one of the requirements cannot be met).
1. Hence $C_f$ is also empty leading to $C \subset C_f$ being empty too.
1. Thus, a condition which leads to
   
   $$
   \OneVec_p^T {\bf^p}^* + \OneVec_q^T {\bf^q}^* < \frac{1}{2}
   $$
   is a sufficient condition for equivalence of {eq}`eq:bp:exact_sparse_problem`
   and {eq}`eq:bp:bp_l1_norm_minimization`.
1. Consider a feasible $\bf$ for
   {eq}`eq:bp:bp:exact_matching_linear_program`.
1. Let $\| \bf^p \|_1 = \OneVec^T \bf^p = c $.
1. Since $\OneVec^T (\bf^p + \bf^q) = 1$,
   hence $\| \bf^q \|_1 = \OneVec^T \bf^q = 1 - c$.
1. We note that
   
   $$
    \OneMat \bf^p = \OneVec \cdot \OneVec^T \bf^p 
    = \| \bf^p \|_1 \OneVec  = c \OneVec.
   $$
1. Similarly, 
   
   $$
    \OneMat \bf^q = (1 - c ) \OneVec. 
   $$
1. Thus, the first two constraints change into 
   
   $$
    \bf^p  \preceq  ( 1 - c) \mu \OneVec \\
    \bf^q  \preceq  c \mu \OneVec.
   $$
1. Since the objective is to maximize
   $\OneVec_p^T \bf^p + \OneVec_q^T \bf^q$,
   it is natural to maximize non-zero entries in
   $\bf^p$ and $\bf^q$ corresponding to $S_p$ and $S_q$. 
1. A straight-forward option is to choose first $k_p$ entries in
   $\bf^p$ to be $(1 - c) \mu$ and first $k_q$ entries in $\bf^q$
   to be $c \mu$.
1. Other entries can be chosen  arbitrarily to meet the requirement that
   $\OneVec^T (\bf^p + \bf^q) = 1$.
1. With this choice, we have
   
   $$
    \OneVec_p^T \bf^p + \OneVec_q^T \bf^q
    = k_p (1 - c ) \mu + k_q c \mu 
    = \mu (k_p  - c (k_p - k_q)).
   $$
1. We recall that we have chosen $k_p \geq k_q$.
1. Thus, the expression is maximized if $c$ is chosen to be as small as possible.
1. The choice of $c$ must meet following conditions on $\ell_1$-norms. 
   (Basically the sum of first $k_p$ terms of $\bf_p$
    must not be more than the $\ell_1$ norm of $\bf^p$.
    Same for $\bf^q$).
    
    $$
    \| \bf^p \|_1  = \OneVec^T \bf^p = c \geq k_p (1 - c ) \mu \\
    \| \bf^q \|_1  = \OneVec^T \bf^q = 1 - c \geq  k_q c \mu.
    $$
1. Simplifying these inequalities we get
   
   $$
    c \geq k_p (1 - c ) \mu \implies c \geq \frac{k_p \mu}{ 1 + k_p \mu}\\
    1 - c \geq  k_q c \mu \implies c \leq \frac{1}{ 1 + k_q \mu}.
   $$
1. Since these two conditions must be satisfied,
   hence we require $k_p, k_q$ to meet

   $$
    \frac{k_p \mu}{ 1 + k_p \mu} 
    \leq \frac{1}{ 1 + k_q \mu} \implies k_p k_q \leq \frac{1}{\mu^2}.
   $$
1. We will verify later that this condition is met if 
   {eq}`eq:bp:bp_exact_sparse_two_ortho_case_condition` holds.
1. Assuming the condition is met, obviously the smallest possible value of $c$
   is given by $\frac{k_p \mu}{ 1 + k_p \mu}$.
1. The maximum value of objective function then becomes
   
   $$
    \OneVec_p^T \bf^p + \OneVec_q^T \bf^q 
    &=  \mu (k_p  - c (k_p - k_q)) \\
    &=  \mu \left (k_p  - \frac{k_p \mu}{ 1 + k_p \mu} (k_p - k_q)\right )\\
    &= \frac{k_p \mu + k_p k_q \mu^2}{ 1 + k_p \mu}.
   $$
1. Finally, for BP to succeed, we require this expression to be strictly less than half.
1. This gives us
   
   $$
    \frac{k_p \mu + k_p k_q \mu^2}{ 1 + k_p \mu} < \frac{1}{2}
    \implies 2 k_p k_q \mu^2 + k_p \mu - 1 < 0
   $$
   which is the sufficient condition for BP to succeed in the theorem.

We now show that {eq}`eq:bp:bp_exact_sparse_two_ortho_case_condition`
$\implies$ the weaker condition
{eq}`eq:bp:two_ortho_exact_recovery_coherence_simple`.
1. From {eq}`eq:bp:bp_exact_sparse_two_ortho_case_condition` we can write $k_q$ as
   
   $$
    2 k_p k_q \mu^2 + k_p \mu - 1 < 0 \implies 2 k_p k_q \mu^2 < 1 - k_p \mu
    \implies k_q < \frac{1 - k_p \mu}{2 k_p \mu^2}.
   $$
1. Thus,
   
   $$
    \| \ba \|_0 = k_p + k_q &< k_p + \frac{1 - k_p \mu}{2 k_p \mu^2} \\
    &= \frac{2 \mu^2 k_p^2 + 1 - \mu k_p}{2 \mu^2 k_p}\\
    &= \frac{1}{\mu} \cdot \frac{2 \mu^2 k_p^2 + 1 - \mu k_p}{2 \mu k_p}.
   $$
1. We define $u = \mu k_p$ and rewrite above as
   
   $$
    \| \ba \|_0 < \frac{1}{\mu} \frac{2 u^2 - u + 1}{2 u}.
   $$
1. The weaker condition can now be obtained by minimizing
   the upper bound on R.H.S. of this equation.
1. We define
   
   $$
    f(u)  = \frac{2 u^2 - u + 1}{2 u}.
   $$
1. Differentiating and equating with 0, we get
   
   $$
    f'(u) = \frac{2 u^2 - 1}{ 2 u^2} = 0.
   $$
1. The optimal value is obtained when $u  = \pm \sqrt{0.5}$. 
1. Since both $\mu$ and $k_p$ are positive quantities,
   hence the negative value for $u$ is rejected and we get $u = \sqrt{0.5}$. 
1. This gives us
   
   $$
    \| \ba \|_0 <  \frac{1}{\mu} \frac{2  - \sqrt{0.5}}{2 \sqrt{0.5}}
    = \frac{\sqrt{2}- 0.5}{\mu}.
   $$
1. Lastly, the property that arithmetic mean is greater than or equal to
   geometric mean gives us
   
   $$
    k_p k_q \leq \frac{(k_p + k_q)^2}{4} 
    < \frac{(\sqrt{2}- 0.5)^2}{4\mu^2} < \frac{1}{\mu^2}.
   $$
````


## General Case

We now consider the case where $\bDDD \in \CC^{N \times D}$ is
an arbitrary (redundant) dictionary.
We will require that $\bDDD$ is full row rank.
If $\bDDD$ is not a full row rank  matrix then some of
its columns (atoms) can be removed to make it so.

We develop sufficient conditions under which solutions of 
{eq}`eq:bp:exact_sparse_problem` and 
{eq}`eq:bp:bp_l1_norm_minimization` match for the general case
{cite}`donoho2003optimally,elad2010sparse`.

````{prf:theorem}
:label: res:bp:general_exact_recovery_coherence

Let $\bDDD$ be an arbitrary full rank redundant dictionary.
Let $\bx = \bDDD \ba$, where $\bx$ is known. 
If a sparse representation $\ba$ exists obeying

```{math}
:label: eq:bp:general_exact_recovery_coherence

\| \ba \|_0 < \frac{1}{2} \left ( 1 + \frac{1}{\mu} \right ),
```
then $\ba$ is the unique solution of both {eq}`eq:bp:exact_sparse_problem` and 
{eq}`eq:bp:bp_l1_norm_minimization`.
````
````{prf:proof}
Due to {prf:ref}`thm:ssm:uniqueness_coherence`,
$\ba$ is a unique solution for {eq}`eq:bp:exact_sparse_problem`
since $\ba$ satisfies {eq}`eq:bp:general_exact_recovery_coherence`.
We need to show that it is also a unique solution to
{eq}`eq:bp:bp_l1_norm_minimization`

1. For any other feasible $\bb$ for {eq}`eq:bp:bp_l1_norm_minimization`,
   we have $\| \bb \|_0 > \| \ba \|_0$ since it is unique
   sparsest solution of $\bx = \bDDD \ba$.
1. We start with defining a set of alternative feasible vectors to
   {eq}`eq:bp:bp_l1_norm_minimization`:

    $$
    C = \left \{ \bb  \left | 
    \begin{aligned}
    \bb \neq \ba \\
    \| \bb \|_1 \leq \| \ba \|_1\\
    \| \bb \|_0 > \| \ba \|_0\\
    \text{ and } \bDDD (\bb - \ba) = \bzero
    \end{aligned}
    \right.
    \right \}.
    $$
    This set contains all possible representations that
    1. are different from $\ba$
    1. have larger support
    1. satisfy $\bDDD \bb = \bx$
    1. have a better (or at least as good) $\ell_1$-norm.
1. We need to show that if {eq}`eq:bp:general_exact_recovery_coherence` holds,
   then the set $C$ will be empty.
1. Otherwise, BP would choose a solution different than $\ba$.
1. The condition $\| \bb \|_0 > \| \ba \|_0$ is redundant
   under the assumption {eq}`eq:bp:general_exact_recovery_coherence`.
1. Following the proof of {prf:ref}`res:bp:two_ortho_exact_recovery_coherence`,
   we define
   
   $$
    \be = \bb - \ba.
   $$
1. We can then rewrite $C$ as 
   
   $$
    C_s = \{\be \ST \be \neq \bzero, 
        \| \be + \ba \|_1 - \| \ba \|_1 \leq 0, 
        \text{ and } \bDDD \be = \bzero \}.
   $$
1. Again, we will enlarge the set $C_s$ and show that even
   the larger set is empty
   when {eq}`eq:bp:general_exact_recovery_coherence` holds. 
1. We start with the requirement $\| \be + \ba \|_1 - \| \ba \|_1 \leq 0$. 
1. A simple permutation of columns of $\bDDD$ can bring the nonzero
   entries in $\ba$ to the beginning.
1. Thus, without loss of generality,
   we assume that first $K$ entries in $\ba$
   are nonzero and the rest are zero.
1. We can now rewrite the requirement as
   
   $$
    \| \be + \ba \|_1 - \| \ba \|_1 
    = \sum_{j=1}^K \left ( |e_j + a_j | - | a_j | \right ) 
    + \sum_{j > K} | e_j | \leq 0.
   $$
1. Using the inequality $| x + y | - | y | \geq - | x |$,
   we can relax above condition as
   
   $$
    - \sum_{j = 1}^K | e_j | + \sum_{j > K} | e_j | \leq 0.
   $$
1. Let $\OneVec_K$ denote a vector with $K$ ones
   at the beginning and rest zeros.
1. Then, 
   
   $$
    \sum_{j = 1}^K | e_j | = \OneVec_K^T | \be |. 
   $$
1. Further,
   
   $$
    \sum_{j > K} | e_j | 
    = \| \be \|_1 - \sum_{j = 1}^K | e_j |  
    = \OneVec^T | \be | - \OneVec_K^T | \be |.
   $$
1. Thus, we can rewrite above inequality as
   
   $$
     \OneVec^T | \be | - 2 \OneVec_K^T | \be | \leq 0.
   $$
1. We can now define 
   
   $$
    C_s^1  = 
    \{\be \ST \be \neq \bzero, 
        \OneVec^T | \be | - 2 \OneVec_K^T | \be | \leq 0, 
        \text{ and } \bDDD \be = \bzero \}.
   $$
1. Clearly $C_s \subseteq C_s^1$.
1. We will now relax the requirement of $\bDDD \be = \bzero$.
1. Multiplying by $\bDDD^H$, we get
   
   $$
    \bDDD^H \bDDD \be = \bzero.
   $$
1. If $\be \in C_s^1$, it will also satisfy this equation.
1. Moreover, if $\be$ satisfies this, then $\be$
   belongs to the null space of $\bDDD^H \bDDD$.
1. Since $\bDDD$ is full rank, hence $\be$ has to be in the
   null space of $\bDDD$ also.
1. Thus the two conditions $\bDDD \be = \bzero$ and 
   $\bDDD^H \bDDD e = \bzero$ are equivalent.
1. We note that off-diagonal entries in $\bDDD^H \bDDD$ are bounded by $\mu$
   while the main diagonal consists of all ones.
1. So, we can write
   
   $$
    & \bDDD^H \bDDD \be = \bzero \\
    \iff & (\bDDD^H \bDDD - \bI + \bI ) \be = \bzero \\
    \iff & -\be = (\bDDD^H \bDDD - \bI ) \be.
   $$
1. Suppose $\bv = \bG \bu$. Then $v_i = \sum_{j} G_{i j} u_j$.
1. Thus 
   
   $$
    | v_i | = | \sum_{j} G_{i j} u_j | 
    \leq \sum_{j} | G_{i j} u_j | = \sum_{j} | G_{i j} | | u_j |.
   $$
1. This gives us $| \bv | \preceq | \bG | | \bv |$ 
   where $\preceq$ indicates component wise inequality. 
1. Taking an entry-wise absolute value on both sides, we get
   
   $$
    | \be | =  |(\bDDD^H \bDDD - \bI ) \be | 
    \preceq  |\bDDD^H \bDDD - \bI || \be | 
    \preceq \mu (\OneMat - \bI) | \be |.
   $$
1. The last part is due to the fact that all entries in the vector
   $| \be | $ and the matrix $ | \bDDD^H \bDDD - \bI |$ 
   are non-negative and the entries in $| \bDDD^H \bDDD - \bI|$
   are dominated by $\mu $.
1. Further,
   
   $$
    & | \be | \preceq 
    \mu (\OneMat - \bI) | \be |  \\
    \iff & (1 + \mu) | \be | \preceq \mu \OneMat  | \be | = \mu \| \be \|_1 \OneVec\\
    \iff & | \be | \preceq \frac{\mu \| \be \|_1}{1 + \mu}  \OneVec.
   $$
1. In the above we used the fact that
   $\OneMat | \be | = \OneVec \OneVec^T | \be | = \OneVec \| \be \|_1$.
1. We can now define a new set
   
   $$
    C_s^2 = \left \{ 
    \be \left | 
    \begin{aligned}
    & \be \neq \bzero, \\
    &\OneVec^T | \be | - 2 \OneVec_K^T | \be | \leq 0 \\
    & \text{ and } | \be | \preceq \frac{\mu \| \be \|_1}{1 + \mu}  \OneVec
    \end{aligned}
    \right. \right \}.
   $$
1. Clearly, $C_s^1 \subseteq C_s^2$.
1. We note that $C_s^2$ is unbounded since if $\be \in C_s^2$, then
   $c \be \in C_s^2 \Forall c \neq 0$.
1. Thus, in order to study its behavior, it is sufficient
   to consider the set of vectors with unit norm vectors $\| \be \|_1 = 1$.
1. We construct the new set as
   
   $$
    C_r = \left \{\be  \left | 
        \| \be \|_1 = 1,
        1 - 2 \OneVec_K^T | \be | \leq 0 \text { and } 
        | \be | \preceq \frac{\mu }{1 + \mu}  \OneVec \right. \right \}.
   $$
1. Note that we replaced $\OneVec^T | \be | = \| \be \|_1 = 1$
   in formulating the description of $C_r$ and
   the condition $\be \neq \bzero$ is automatically enforced since 
   $\| \be \|_1 = 1$.
1. Clearly $C_s^2 = \EmptySet \iff C_r = \EmptySet$.
1. In order to satisfy the requirement
   $1 - 2 \OneVec_K^T | \be | \leq 0$,
   we need to have $\OneVec_K^T | \be |$
   as large as possible.
1. Since this quantity only considers first $K$ 
   entries in $\be$,
   hence the energy in $\be$ should be concentrated inside the first $K$ entries
   to maximize this quantity.
1. However, entries in $\be$ are restricted by the third requirement
   in $C_r$.
1. We can maximize it by choosing
   
   $$
    | e_j | = \frac{\mu }{1 + \mu}
   $$ 
   for first $K$ entries in $e$.
1. We then get
   
   $$
    1 - 2 \OneVec_K^T | \be |   = 1 - 2 K \frac{\mu }{1 + \mu} \leq 0.
   $$
1. This gives us
   
   $$
    & 1 - 2 K \frac{\mu }{1 + \mu} \leq 0 \\
    \iff & 1 + \mu \leq 2 K \mu \\
    \iff & 2K \geq \frac{1 + \mu}{\mu}\\
    \iff & K \geq \frac{1}{2} \left (  1 + \frac{1}{\mu} \right).
   $$
1. This is a necessary condition for $C_r$ to be non-empty.
1. Thus, if 
   
   $$
    K <  \frac{1}{2} \left (  1 + \frac{1}{\mu} \right)
   $$
   then, the requirement $1 - 2 \OneVec_K^T | \be | \leq 0$
   is not satisfied and $C_r$ is empty.
1. Consequently, $C$ is empty and the theorem is proved.
````



We present another result which is based on
$\mu_{1/2}(\bG)$ {prf:ref}`def:proj:coherence:mu_half_G`
measure of the Gram matrix of the dictionary.
This result is due to {cite}`donoho2003optimally`.


````{prf:theorem}
:label: res:bp:general_exact_recovery_mu_half_G

Let $\bx = \bDDD \ba$ and $\| \ba \|_0 < \mu_{1/2}(\bG)$, then
then $\ba$ is the unique solution of both
{eq}`eq:bp:exact_sparse_problem` and 
{eq}`eq:bp:bp_l1_norm_minimization`.
````
````{prf:proof}
Unique solution of {eq}`eq:bp:exact_sparse_problem`.

1. Let $\Lambda = \supp(\ba)$ and $K = |\Lambda|$.
1. We have $K = \| \ba \|_0 < \mu_{1/2}(\bG)$.
1. By {prf:ref}`res:proj:coherence:spark_lower_bound_mu_half`

   $$
   \spark(\bDDD) \geq 2 \mu_{1/2}(G) +1
   \implies \spark(\bDDD) > 2 K + 1
   \implies K <  \frac{1}{2}\spark(\bDDD).
   $$
1. By {prf:ref}`thm:ssm:uniqueness_spark`, $\ba$
   is the unique sparsest solution.

Unique solution of {eq}`eq:bp:bp_l1_norm_minimization`

1. We need to show that for any $\ba'$ satisfying
   $\bx = \bDDD \ba'$, we must have
   $\| \ba' \|_1 > \| \ba \|_1$.
1. We will show that any vector in the null space of $\bDDD$
   exhibits less than $50$% concentration
   on $\Lambda$; i.e., for every $\bh \in \NullSpace(\bDDD)$
    
   $$
    \sum_{k \in \Lambda} | h_k | < \frac{1}{2} \| \bh \|_1.
   $$
1. Now
   
   $$
    \bDDD \bh  = \bzero \implies \bG \bh = \bDDD^H \bDDD \bh  = \bzero.
   $$
1. Subtracting both sides with $\bh$ we get
   
   $$
   \bG \bh - \bh = (\bG  - \bI) \bh = -\bh.
   $$
1. Let $\bF$ denote an $K \times D$ matrix formed from the rows of $\bG - \bI$
   corresponding to the indices in $\Lambda$.
1. Then
   
   $$
    (\bG - \bI) \bh = -\bh 
    \implies \| \bF \bh \|_1 = \sum_{k \in \Lambda} | h_k |.
   $$
   $h_k$ for some $k \in \Lambda$ is the negative of the inner product
   of some row in $\bF$ with $\bh$.
1. We know that
   
   $$
    \| \bF \bh \|_1 \leq \| \bF \|_1 \| \bh \|_1
   $$
   where $\| \bF \|_1$ is the max-column-sum norm of $\bF$. 
1. This gives us
   
   $$
    \| \bF \|_1 \| \bh \|_1 \geq \sum_{k \in \Lambda} | h_k |.
   $$
1. In any column of $\bF$ the number of entries is $K$. 
1. One of them is 0 (corresponding to the diagonal entry in $\bG$).
1. Thus, leaving it the rest of the entries are $K -1$.
1. By assumption $\mu_{1/2}(G) > K$.
1. Thus any set of entries in a column which is
   less than or equal to $K$ entries cannot 
   have a sum exceeding $\frac{1}{2}$.
1. This gives an upper bound on the max-column-sum of $\bF$; i.e.,
   
   $$
    \| \bF \|_1 < \frac{1}{2}.
   $$
1. Thus, we get
   
   $$
     \sum_{k \in \Lambda} | h_k | \leq \| \bF \|_1 \| \bh \|_1 
     < \frac{1}{2} \| \bh \|_1
   $$
   for every $\bh \in \NullSpace(\bDDD)$.
1. The rest follows from the fact that for any other $\ba'$
   such that
   $\bx = \bDDD \ba' = \bDDD \ba$,
   we know that
   
   $$
    \| \ba' \|_1 > \| \ba \|_1
   $$
   whenever
   
   $$
    \sum_{k \in \Lambda} | h_k |  < \frac{1}{2} \| \bh \|_1
   $$
   where $\bh = \ba - \ba'$ (thus $\bDDD \bh = \bzero$).
````

## BPIC
In the subsection, we present a stability guarantee result for BPIC.

````{prf:theorem}
:label: res:bp:bpic_stability_guarantee

Consider an instance of the {eq}`eq:bp:bpic_l1_norm_minimization` problem
defined by the triplet $(\bDDD, \bx, \epsilon)$.
Suppose that a vector $\ba \in \CC^D$ is a feasible
solution to {eq}`eq:bp:bpic_l1_norm_minimization` satisfying the sparsity constraint

$$
\| \ba \|_0  < \frac{1}{4} \left (1  + \frac{1}{\mu (\bDDD)} \right). 
$$
The solution $\widehat{\ba}$ of {eq}`eq:bp:bpic_l1_norm_minimization`
must satisfy

$$
\|\widehat{\ba} - \ba \|_2^2 
\leq \frac{4 \epsilon^2}{ 1 - \mu (\bDDD) ( 4 \| \ba \|_0 - 1)}.
$$
````

````{prf:proof}
As before, we define $\bb = \widehat{\ba} - \ba$.

1. Then

    $$
    \| \bDDD \bb \|_2 
    = \|\bDDD (\widehat{\ba} - \ba) \|_2 
    = \|\bDDD  \widehat{\ba} - \bx + \bx -\bDDD \ba \|_2  \leq 2 \epsilon.
    $$
1. We now rewrite the inequality in terms of the Gram matrix
   $\bG  = \bDDD^H \bDDD$. 

    $$
    4 \epsilon^2 \geq  &= \|\bDDD \bb  \|_2^2 = \bb^H \bG \bb\\
    &= \bb^H (\bG - \bI + \bI) \bb \\
    &= \| \bb \|_2^2 +\bb^H (\bG - \bI ) \bb.
    $$
1. It is easy to show that:

    $$
    - | \bb |^T | \bA | | \bb | \leq \bb^H \bA \bb \leq | \bb |^T | \bA | | \bb |
    $$
    whenever $\bA$ is Hermitian.
    1. To see this just notice that $\bb^H \bA \bb$ is a real quantity.
    1. Hence $\bb^H \bA \bb = \pm | \bb^H \bA \bb |$.
    1. Now, using triangle inequality we can easily show that
       $| \bb^H \bA \bb | \leq | \bb|^T | \bA | | \bb |$.
1. Since $\bG- \bI$ is Hermitian, hence

    $$
    \bb^H (\bG - \bI) \bb \geq - | \bb |^T | \bG - \bI | | \bb |.
    $$
1. Now 

    $$
    | \bb |^T | \bG - \bI | | \bb | 
    = \sum_{i, j}|b_i | |\bd_i^H \bd_j - \delta_{i j} | | b_j | 
    \leq \mu (\bDDD) \sum_{i, j, i \neq j} |b_i | | b_j |
    = \mu (\bDDD) | \bb |^T (\OneMat - \bI) | \bb |.
    $$
1. Only the off-diagonal terms of $\bG$ remain in the sum,
   which are all dominated by $\mu (\bDDD)$.
1. Thus we get
    
    $$
    4 \epsilon^2 &\geq  \| \bb \|_2^2 - | \bb |^T (\OneMat - \bI) | \bb |\\
    &= (1 + \mu (\bDDD)) \| \bb \|_2^2 - \mu (\bDDD) | \bb |^T \OneMat | \bb |\\
    &= (1 + \mu (\bDDD)) \| \bb \|_2^2 - \mu (\bDDD) \| \bb \|_1^2.
    $$
    This is valid since $v^H \OneMat \bv = \| \bv \|_1^2$. 
1. Since $\widehat{\ba}$ is optimal solution of
   {eq}`eq:bp:bpic_l1_norm_minimization`, hence
   
   $$
    \| \widehat{\ba} \|_1 = \| \bb + \ba \|_1 
    \leq \| \ba \|_1 \implies 
    \| \bb + \ba \|_1 - \| \ba \|_1 \leq 0.
   $$
1. Let $\Lambda = \supp(\ba)$ and $K = |\Lambda|$. 
1. By a simple permutation of columns of $\bDDD$,
   we can bring the entries in $\ba$ 
   to the first $K$ entries making
   $\Lambda = \{1, \dots, K\}$.
1. We will make this assumption going forward without loss of generality.
1. Let $\OneVec_K$ be corresponding support vector
   (of ones in first K places and 0 in rest). 
1. From our previous analysis, we recall that
   
   $$
    \| \bb + \ba \|_1 - \| \ba \|_1 
    \geq \| \bb \|_1 - 2 \OneVec_K^T | \bb |. 
   $$
1. Thus
   
   $$
    \| \bb \|_1 - 2 \OneVec_K^T | \bb |\leq 0
    \implies \| \bb \|_1 \leq 2 \OneVec_K^T | \bb |.
   $$
1. $ \OneVec_K^T | \bb |$ is the sum of first $K$ terms of $|\bb|$. 
1. Considering $\bb_{\Lambda}$ as a vector $\in \CC^K$ and
   using the $\ell_1$-$\ell_2$ norm relation
   $\| \bv \|_1 \leq \sqrt{K} \| \bv \|_2 
   \Forall \bv \in \CC^N$, we get
   
   $$
    \OneVec_K^T | \bb | = \| \bb_{\Lambda} \|_1
    \leq \sqrt{K} \| \bb_{\Lambda} \|_2 \leq  \sqrt{K} \| \bb \|_2.
   $$
1. Thus,
   
   $$
    \| \bb \|_1 \leq 2 \OneVec_K^T | \bb | \leq 2 \sqrt{K} \| \bb \|_2.
   $$
1. Putting this back in the previous inequality
   
   $$
    4 \epsilon^2 
    &\geq (1 + \mu (\bDDD)) \| \bb \|_2^2 - \mu (\bDDD) \| \bb \|_1^2\\
    &\geq (1 + \mu (\bDDD)) \| \bb \|_2^2 - \mu (\bDDD) 4 K \| \bb \|_2^2 \\
    &= (1  - (4 K - 1) \mu (\bDDD)) \| \bb \|_2^2.
   $$
1. We note that this inequality is valid only if 
   
   $$
    1  - (4 K - 1) \mu (\bDDD) > 0.
   $$
1. This condition can be reformulated as
   
   $$
    \| \ba \|_0  = K < \frac{1}{4} \left (1  + \frac{1}{\mu (\bDDD)} \right). 
   $$
1. Rewriting the bound on $\| \bb \|_2^2$ we get
   
   $$
    \| \bb \|_2^2 \leq \frac{4 \epsilon^2}{(1  - (4 K - 1) \mu (\bDDD)) }
   $$
   which is the desired result.
````

## BPDN

In this subsection we will examine the $\ell_1$ penalty problem
{eq}`eq:bp:bpdn_l1_norm_minimization_gamma` more closely.

````{math}
:label: bp:bpdn:l_1_penalty_problem
\widehat{\ba} 
= \text{arg } \underset{\ba \in \CC^D}{\min}
\frac{1}{2} \| \bx -  \bDDD \ba \|_2^2 + \gamma \| \ba \|_1.
````

We will focus on following issues:

*  Some results from convex analysis useful for our study
*  Conditions for the minimization of {eq}`bp:bpdn:l_1_penalty_problem`
   over coefficients $\ba$ supported on a subdictionary $\bDDD_{\Lambda}$
*  Conditions under which the unique minimizer for a subdictionary
   is also the global minimizer for {eq}`bp:bpdn:l_1_penalty_problem`
*  Application of {eq}`bp:bpdn:l_1_penalty_problem` for sparse signal
   recovery
*  Application of {eq}`bp:bpdn:l_1_penalty_problem` for identification
   of sparse signals in presence of noise
*  Application of {eq}`bp:bpdn:l_1_penalty_problem` for identification
   of sparse signals in presence of Gaussian noise

We recall some definitions and results from convex analysis which will help us
understand the minimizers for {eq}`bp:bpdn:l_1_penalty_problem` problem.

Convex analysis for real valued functions the vector space $(\CC^n, \RR)$
is developed using the bilinear inner product defined as

$$
\langle \bx, \by \rangle_B = \Re (\by^H \bx).
$$
The subscript $B$ is there to distinguish it from the standard inner
product for the complex coordinate space $\langle \bx, \by \rangle = \by^H \bx$.
The two inner products are related as

$$
\langle \bx, \by \rangle_B = \Re (\langle \bx, \by \rangle).
$$

We consider real valued functions over the inner product space
$\XX = (\CC^D, \langle \cdot, \cdot \rangle_B)$.
Note that the dimension of $\XX$ is $2 D$.

A real valued convex function $f : \XX \to \RR$ satisfies
the standard convexity inequality

$$
f (\theta \bx + (1 - \theta) \by ) 
\leq \theta f (\bx) + (1 - \theta) f(\by) \Forall 0 \leq \theta \leq 1.
$$
The objective function for the problem {eq}`bp:bpdn:l_1_penalty_problem` is

```{math}
:label: bp:bpdn:l_1_penalty_objective_function
L(\ba) = \frac{1}{2} \| \bx -  \bDDD \ba \|_2^2 + \gamma \| \ba \|_1.
```
Clearly, $L$ is a real valued function over $\XX$ and it is easy to so that
it is a convex function. Moreover  $L(\ba) \geq 0$ always.

We suggest the readers to review the material in {ref}`sec:cvxf:subgradients`.
For any function $f : \XX \to \RR$, its *subdifferential set* is defined as

$$
\partial f(\bx) \triangleq 
\{ \bg \in \XX \ST f(\by) 
\geq f(\bx) + \langle \by - \bx, \bg \rangle_B \Forall \by \in \XX\}.
$$
The elements of subdifferential set are called *subgradients*.
If $f$ possesses a gradient at $\bx$, then it is the unique subgradient at $\bx$. i.e.

$$
\partial f(\bx)  = \{\nabla f(\bx) \}
$$
where $\nabla f(\bx)$ is the gradient of $f$ at $\bx$. 

For convex function, the subdifferential of a sum
is the (Minkowski) sum of the subdifferentials
({prf:ref}`res-cvxf-subdiff-function-sum-convex`); i.e.,

$$
\partial (f(\bx) + g(\bx)) = \partial f(\bx) + \partial g(\bx)
= \{\bh_1 + \bh_2 \ST \in \bh_1 \in \partial f(\bx), \bh_2 \in \partial g(\bx) \}.
$$

By Fermat's optimality condition
({prf:ref}`res-cvxf-subdiff-fermat-optimality`),
if $f$ is a closed, proper convex function,
then $\bx$ is a global minimizer of $f$ if and only if
$\bzero \in \partial f(\bx)$.  

```{div}
We would be specifically interested in the subdifferential for the function $\| \ba \|_1$. 
```

````{prf:theorem}
:label: res:bp:l1_norm_subdifferential

Let $\bz \in \XX$.
The vector $\bg \in \XX$ lies in the subdifferential
$\partial \| \bz \|_1$ if and only if

*  $| g_k | \leq 1 \text{ whenever } z_k = 0$.
*  $g_k = \sgn (z_k) \text{ whenever } z_k \neq 0$.
````
The proof is skipped.
```{div}
We recall that the signum function for complex numbers is defined as

$$
\sgn(r e^{i \theta}) = \left\{
    \begin{array}{ll}
        e^{i \theta} & \mbox{if $r > 0$};\\
        0 & \mbox{if $r = 0$}.
    \end{array}
  \right.
$$
The subdifferential for $\ell_1$ norm function for $\RR^n$ is
developed in {prf:ref}`ex-cvxf-subdiff-l1-norm-origin`.
We note that $\ell_1$ norm is differentiable at nonzero vectors.
Also, we can see that:

1. $\| \bg \|_{\infty} = 1$ when $\bz \neq \bzero$.
1. $\| \bg \|_{\infty} \leq 1$ when $\bz = \bzero$.
```

### Restricted Minimizers

````{div}
1. Suppose $\Lambda$ index a subdictionary $\bDDD_{\Lambda}$.
1. $\bDDD_{\Lambda}$ is a linearly independent collection of atoms.
1. Hence a unique $\ell_2$ best approximation $\widehat{\bx}_{\Lambda}$
   of $\bx$ using the atoms in $\bDDD_{\Lambda}$
   can be obtained using the least square techniques.
1. We define the orthogonal projection operator
   
   $$
    \bP_{\Lambda} = \bDDD_{\Lambda}\bDDD_{\Lambda}^{\dag}.
   $$
1. And we get
   
   $$
    \widehat{\bx}_{\Lambda}  = \bP_{\Lambda} \bx.
   $$
1. The approximation is orthogonal to the residual;
   i.e., $(\bx - \widehat{\bx}_{\Lambda}) \perp \widehat{\bx}_{\Lambda}$.
1. There is a unique coefficient vector $\bc_{\Lambda}$ supported on $\Lambda$
   that synthesizes the approximation $\widehat{\bx}_{\Lambda}$. 
   
   $$
    \bc_{\Lambda} = \bDDD_{\Lambda}^{\dag} \bx
    = \bDDD_{\Lambda}^{\dag} \widehat{\bx}_{\Lambda}.
   $$
1. We also have
   
   $$
    \widehat{\bx}_{\Lambda} = \bP_{\Lambda} \bx = \bDDD_{\Lambda} \bc_{\Lambda}.
   $$
````

````{prf:theorem} Minimization of $L$ over vectors supported on $\Lambda$
:label: res:bp:bpdn:l1_local_minimizer_condition

Let  $\Lambda$ index a linearly independent collection of atoms in $\bDDD$
and let $\ba^*$ minimize the objective function $L(\ba)$
in {eq}`bp:bpdn:l_1_penalty_objective_function`
over all coefficient vectors
supported on $\Lambda$ (i.e. $\supp(\ba) \subseteq \Lambda$).
A necessary and sufficient condition on such a minimizer is that 

```{math}
:label: eq:d7564ff5-947f-4a93-b563-4b5c18ff05ea
\bc_{\Lambda} - \ba^*  = \gamma (\bDDD_{\Lambda}^H \bDDD_{\Lambda})^{-1} \bg
```
where $\bc_{\Lambda} = \bDDD_{\Lambda}^{\dag} \bx$
and the vector $\bg$ is drawn from $\partial \| \ba^* \|_1$.
Moreover, the minimizer $\ba^*$ is unique.
````

````{prf:proof}
Since we are restricted $\ba$ to be supported on $\Lambda$ (i.e. $\ba \in \CC^{\Lambda}$),
hence 

$$
\bDDD \ba = \bDDD_{\Lambda} \ba_{\Lambda}.
$$
The objective function simplifies to

$$
L(\ba) = \frac{1}{2} \| \bx -  \bDDD_{\Lambda} \ba_{\Lambda} \|_2^2 + 
\gamma \| \ba_{\Lambda} \|_1.
$$

1. We define $\widehat{\bx}_{\Lambda}  = \bP_{\Lambda} \bx$.
1. Now, both $\widehat{\bx}_{\Lambda}$ and $\bDDD_{\Lambda} \ba_{\Lambda}$
   belong to the column space of $\bDDD_{\Lambda}$
   while $\bx - \widehat{\bx}_{\Lambda}$ is orthogonal to it.
1. Hence
   
   $$
    \bx - \widehat{\bx}_{\Lambda} \perp \widehat{\bx}_{\Lambda} - \bDDD \ba.
   $$
1. Thus, using the Pythagorean theorem, we get
   
   $$
    \| \bx -  \bDDD \ba \|_2^2 
    = \| \bx - \widehat{\bx}_{\Lambda} + \widehat{\bx}_{\Lambda} - \bDDD \ba \|_2^2 
    = \|\bx - \widehat{\bx}_{\Lambda} \|_2^2 + \| \widehat{\bx}_{\Lambda} - \bDDD \ba\|_2^2.
   $$
1. We can rewrite $L(\ba)$ as 
   
   $$
    L(\ba) = \frac{1}{2} \|\bx - \widehat{\bx}_{\Lambda} \|_2^2
    + \frac{1}{2} \| \widehat{\bx}_{\Lambda} - \bDDD \ba\|_2^2 + \gamma \| \ba \|_1.
   $$
1. Define
   
   $$
    F(\ba) = \frac{1}{2} \| \widehat{\bx}_{\Lambda} - \bDDD \ba\|_2^2 + \gamma \| \ba \|_1.
   $$
1. Then
   
   $$
    L(\ba) = \frac{1}{2} \|\bx - \widehat{\bx}_{\Lambda} \|_2^2 + F(\ba).
   $$
1. Note that the term $\|\bx - \widehat{\bx}_{\Lambda} \|_2^2$ is constant.
   It is the squared norm of the least square error.
1. Thus, minimizing $L(\ba)$ over the coefficient vectors supported on $\Lambda$
   is equivalent to minimizing $F(\ba)$ over the same support set.
1. Note that
   
   $$
    \bDDD \ba = \bDDD_{\Lambda} \ba_{\Lambda}
    \text{ and } \| \ba \|_1 = \| \ba_{\Lambda} \|_1.
   $$
1. We can write $F(\ba)$ as
   
   $$
    F(\ba) = \frac{1}{2} \| \widehat{\bx}_{\Lambda} - \bDDD_{\Lambda} \ba_{\Lambda}\|_2^2
    + \gamma \| \ba_{\Lambda} \|_1.
   $$
1. Note that $F(\ba)$ depends only on entries in $\ba$ which are part of the support $\Lambda$.
1. We can replace the variable  $\ba_{\Lambda}$ with $\ba \in \CC^{\Lambda}$
   and rewrite $F(\ba)$ as

   $$
    F(\ba) = \frac{1}{2} \| \widehat{\bx}_{\Lambda} - \bDDD_{\Lambda} \ba\|_2^2
    + \gamma \| \ba \|_1 \Forall \ba \in \CC^{\Lambda}.
   $$
1. Since atoms indexed by $\Lambda$ are linearly independent,
   hence $\bDDD_{\Lambda}$ has full column rank.
1. Thus, the quadratic term $\| \widehat{\bx}_{\Lambda} - \bDDD_{\Lambda} \ba\|_2^2$
   is strictly convex. 
1. Since $\| \ba \|_1$ is also convex, $F(\ba)$ therefore is strictly convex
   and its minimizer is unique. 
1. Since $F$ is strictly convex and unconstrained,
   hence $\bzero \in \partial F(\ba^*)$ is a necessary and sufficient
   condition for the coefficient vector $\ba^*$ to minimize $F(\ba)$.
1. The gradient of the first (quadratic) term is
   
   $$
    \left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right) \ba  - \bDDD_{\Lambda}^H \widehat{\bx}_{\Lambda}.
   $$
1. For the second term we have to consider its subdifferential
   $\partial \| \ba \|_1$.
1. Thus, at $\ba^*$ it follows that
   
   $$
    \left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right) \ba^*  - \bDDD_{\Lambda}^H \widehat{\bx}_{\Lambda} + \gamma \bg = \bzero.
   $$ 
   where $\bg$ is some subgradient in $\partial \| \ba^* \|_1$.
1. Premultiplying with $\left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right)^{-1}$
   we get
   
   $$
    &\ba^*  - \bDDD_{\Lambda}^{\dag} \widehat{\bx}_{\Lambda}
    + \gamma \left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right)^{-1} \bg  = \bzero\\
    &\implies \bDDD_{\Lambda}^{\dag} \widehat{\bx}_{\Lambda} - \ba^* = \gamma \left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right)^{-1} \bg.
   $$
1. Finally, we recall that $\bDDD_{\Lambda}^{\dag} \widehat{\bx}_{\Lambda} = \bc_{\Lambda}$.
1. Thus, we get the desired result
   
   $$
    \bc_{\Lambda} - \ba^*  = \gamma \left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right)^{-1} \bg.
   $$
````


Some bounds follow as a result of this theorem.
Readers are suggested to review the material in
{ref}`sec:la:matrix:norms`.

````{prf:theorem}
:label: res:bp:norm_upper_bounds_optimal_vs_projector

Suppose that $\Lambda$ index a subdictionary $\bDDD_{\Lambda}$
and let $\ba^*$ minimize
the function $L$ over all coefficient vectors
supported on $\Lambda$.
Then following bounds are in force:

$$
\| \bc_{\Lambda} - \ba^* \|_{\infty}
\leq \gamma \|\left (\bDDD_{\Lambda}^H 
    \bDDD_{\Lambda} \right)^{-1}\|_{\infty}.
$$

$$
\| \bDDD_{\Lambda} (\bc_{\Lambda} - \ba^*) \|_2
\leq \gamma \| \bDDD_{\Lambda}^{\dag} \|_{2 \to 1}.
$$
````
````{prf:proof}
We start with

```{math}
:label: eq:2826c54e-96c6-4ef3-8be9-fff688e713b3
\bc_{\Lambda} - \ba^*  = \gamma 
\left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right)^{-1} \bg.
```
1. we take the $\ell_{\infty}$ norm on both sides and
   apply some norm bounds
   
   $$
    \| \bc_{\Lambda} - \ba^* \|_{\infty} 
    &= \| \gamma \left 
    (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right)^{-1} \bg \|_{\infty}\\
    &\leq \gamma \|\left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right)^{-1} \|_{\infty} 
    \| \bg \|_{\infty}\\
    &\leq \gamma \|\left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right)^{-1} \|_{\infty}.
   $$
   The last inequality is valid since from {prf:ref}`res:bp:l1_norm_subdifferential`
    we have: $\| \bg \|_{\infty} \leq 1$.
1. Now let us premultiply {eq}`eq:2826c54e-96c6-4ef3-8be9-fff688e713b3`
   with $\bDDD_{\Lambda}$ and apply $\ell_2$ norm

   $$
    \|\bDDD_{\Lambda} ( \bc_{\Lambda} - \ba^*) \|_2 
    &= \|\gamma \bDDD_{\Lambda} 
    \left (\bDDD_{\Lambda}^H \bDDD_{\Lambda} \right)^{-1} \bg \|_2\\
    &= \gamma \|  (\bDDD_{\Lambda}^{\dag})^H \bg \|_2 \\
    &\leq \|  (\bDDD_{\Lambda}^{\dag})^H \|_{\infty \to 2} \| \bg \|_{\infty} \\
    &= \|  \bDDD_{\Lambda}^{\dag} \|_{2 \to 1} \| \bg \|_{\infty} \\
    &\leq \|  \bDDD_{\Lambda}^{\dag} \|_{2 \to 1}.
   $$
1. In this derivation we used facts like
   $\| \bA \|_{p \to q} = \| \bA^H \|_{q' \to p'}$,
   $\| \bA \bx \|_q \leq \| \bA \|_{p \to q} \| \bx \|_p$
   and $\| \bg \|_{\infty} \leq 1$.
````

### The Correlation Condition

So far we have established a condition which
ensures that $\ba^*$ is a unique minimizer
of $L$ given that $\ba$ is supported on $\Lambda$. 
We now establish a sufficient condition under which
$\ba^*$ is also a global minimizer for $L(\ba)$.

````{prf:theorem} Correlation condition for global minimizer
:label: res:bp:bpdn_correlation_condition_global_minimizer

Assume that $\Lambda$ indexes a subdictionary.
Let $\ba^*$ minimize the function $L$
over all coefficient vectors supported on $\Lambda$.
Suppose that

```{math}
:label: eq:897d5134-9f27-4017-a926-9e522045c3ae

\| \bDDD^H (\bx - \widehat{\bx}_{\Lambda}) \|_{\infty} \leq 
\gamma \left [ 
1 - \underset{\omega \notin \Lambda}{\max} |\langle\bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg  \rangle| 
\right]
```
where $\bg \in \partial \| \ba^* \|_1$ is determined by {eq}`eq:d7564ff5-947f-4a93-b563-4b5c18ff05ea`.
Then $\ba^*$ is the unique global minimizer of $L$.
Moreover, the condition

```{math}
:label: eq:6a6bdfe2-48c9-4f66-ab7f-e1645fabaa8f
\| \bDDD^H (\bx - \widehat{\bx}_{\Lambda}) \|_{\infty} \leq 
\gamma \left [ 
1 - \underset{\omega \notin \Lambda}{\max}\|\bDDD_{\Lambda}^{\dag}  \bd_{\omega}\|_1 
\right]
```
guarantees that $\ba^*$ is the unique global minimizer of $L$.
````

````{prf:proof}
Let $\ba^*$ be the unique minimizer of $L$ over
coefficient vectors supported on $\Lambda$.
Then, the value of the objective function $L(\ba)$ increases
if we change any coordinate of $\ba^*$ indexed in $\Lambda$. 

What we need is a condition which ensures that the value of objective function
also increases if we change any other component of $\ba^*$
(not indexed by $\Lambda$).
1. If this happens, then $\ba^*$ will become a local minimizer of $L$.
1. Further, since $L$ is convex, $\ba^*$ will also be global minimizer. 


Towards this, let $\omega$ be some index not in $\Lambda$
and $\be_{\omega} \in \CC^D$ be corresponding unit vector.
Let $\delta \be_{\omega}$ be a small perturbation introduced in $\omega$-th coordinate.
($\delta \in \CC$ is a small scalar, though need not be positive real).
We need find a condition which ensures

$$
L (\ba^* + \delta \be_{\omega}) - L (\ba^*) > 0 \Forall \omega \notin \Lambda.
$$

1. Let us expand the L.H.S. of this inequality:

   $$
    &L (\ba^* + \delta \be_{\omega}) - L (\ba^*) =\\
    &\quad \left [ \frac{1}{2} \| \bx -  \bDDD \ba^* - \delta \bd_{\omega}\|_2^2 - \frac{1}{2} \| \bx -  \bDDD \ba^* \|_2^2 \right ] \\
    &\quad + \gamma\left [\| \ba^*  + \delta \be_{\omega}\|_1 -  \| \ba^* \|_1\right ].
   $$
   Here we used the fact that $\bDDD \be_{\omega} = \bd_{\omega}$.
1. Note that since $\ba^*$ is supported on $\Lambda$ and $\omega \notin \Lambda$, hence
   
   $$
    \| \ba^*  + \delta \be_{\omega}\|_1 = \| \ba^*\|_1  +  \|\delta \be_{\omega}\|_1.
   $$
1. Thus
   
   $$
    \| \ba^*  + \delta \be_{\omega}\|_1 -  \| \ba^* \|_1 = |\delta|.
   $$
1. We should also simplify the first bracket.
   
   $$
    \| \bx -  \bDDD \ba^* \|_2^2 
    &= (\bx -  \bDDD \ba^*)^H (\bx -  \bDDD \ba^*) \\
    &= \bx^H \bx + {\ba^*}^H \bDDD^H \bDDD \ba^* 
    - \bx^H \bDDD \ba^* -  {\ba^*}^H \bDDD^H \bx.
   $$
1. Similarly
   
   $$
    \| \bx -  \bDDD \ba^* - \delta \bd_{\omega}\|_2^2
    &= (\bx -  \bDDD \ba^* - \delta \bd_{\omega})^H 
    (\bx -  \bDDD \ba^* - \delta \bd_{\omega})\\
    &= \bx^H \bx + {\ba^*}^H \bDDD^H \bDDD \ba^* 
    - \bx^H \bDDD \ba^* -  {\ba^*}^H \bDDD^H \bx\\
    &- (\bx -  \bDDD \ba^*)^H \delta \bd_{\omega} 
    - \delta \bd_{\omega}^H (\bx -  \bDDD \ba^*) + \| \delta  \bd_{\omega}\|_2^2.
   $$
1. Canceling the like terms we get
   
   $$
    \| \delta  \bd_{\omega}\|_2^2 - 2 \Re (\langle \bx -  \bDDD \ba^*,  \delta \bd_{\omega} \rangle).
   $$
1. Thus,
   
   $$
    &L (\ba^* + \delta \be_{\omega}) - L (\ba^*) =\\
    &\quad \frac{1}{2} \| \delta  \bd_{\omega}\|_2^2 - \Re (\langle \bx -  \bDDD \ba^*,  \delta \bd_{\omega} \rangle) + \gamma |\delta|.
   $$
1. Recall that since $\ba^*$ is supported on $\Lambda$,
   hence $\bDDD \ba^* = \bDDD_{\Lambda} \ba^*$.
1. We can further split the middle term by adding and subtracting
   $\bDDD_{\Lambda} \bc_{\Lambda}$.
   
   $$
    \Re (\langle \bx -  \bDDD_{\Lambda} \ba^*,  \delta \bd_{\omega} \rangle) 
    &= \Re (\langle \bx - \bDDD_{\Lambda} \bc_{\Lambda} + \bDDD_{\Lambda} \bc_{\Lambda} -  \bDDD_{\Lambda} \ba^*,  \delta \bd_{\omega} \rangle)\\
    &= \Re (\langle \bx - \bDDD_{\Lambda} \bc_{\Lambda},  \delta \bd_{\omega} \rangle)  + 
    \Re (\langle \bDDD_{\Lambda} (\bc_{\Lambda} - \ba^*),  \delta \bd_{\omega} \rangle) 
   $$
1. Thus, we can write
   
   $$
    L (\ba^* + \delta \be_{\omega}) - L (\ba^*) = 
    \frac{1}{2} \| \delta  \bd_{\omega}\|_2^2 - \Re (\langle \bx - \bDDD_{\Lambda} \bc_{\Lambda},  \delta \bd_{\omega} \rangle)  
    - \Re (\langle \bDDD_{\Lambda} (\bc_{\Lambda} - \ba^*),  \delta \bd_{\omega} \rangle) + \gamma |\delta|.
   $$
1. The term $\frac{1}{2} \| \delta  \bd_{\omega}\|_2^2$ is strictly positive giving us
   
   $$
    L (\ba^* + \delta \be_{\omega}) - L (\ba^*) >
    - \Re (\langle \bx - \bDDD_{\Lambda} \bc_{\Lambda},  \delta \bd_{\omega} \rangle)  
    - \Re (\langle \bDDD_{\Lambda} (\bc_{\Lambda} - \ba^*),  \delta \bd_{\omega} \rangle) + \gamma |\delta|.
   $$
1. Using lower triangle inequality we can write
   
   $$
    L (\ba^* + \delta \be_{\omega}) - L (\ba^*) >
    \gamma |\delta|
    - |\langle \bx - \bDDD_{\Lambda} \bc_{\Lambda},  \delta \bd_{\omega} \rangle|  
    - |\langle \bDDD_{\Lambda} (\bc_{\Lambda} - \ba^*),  \delta \bd_{\omega} \rangle|.
   $$
1. Using linearity of inner product, we can take out $|\delta|$:
   
   ```{math}
    :label: eq:e50c94b1-d1c3-47c3-9c36-ac384b1a48da

    L (\ba^* + \delta \be_{\omega}) - L (\ba^*) >
     |\delta| \left [ \gamma
    - |\langle \bx - \bDDD_{\Lambda} \bc_{\Lambda},  \bd_{\omega} \rangle|  
    - |\langle \bDDD_{\Lambda} (\bc_{\Lambda} - \ba^*), \bd_{\omega} \rangle| \right ].
   ```
1. Let us simplify this expression. Since $\ba^*$ is a unique minimizer over
   coefficients in $\CC^{\Lambda}$,
   hence using {prf:ref}`res:bp:bpdn:l1_local_minimizer_condition`
   
   $$
    &\bc_{\Lambda} - \ba^*  = \gamma (\bDDD_{\Lambda}^H \bDDD_{\Lambda})^{-1} \bg\\
    \iff &\bDDD_{\Lambda} (\bc_{\Lambda} - \ba^*) = \gamma \bDDD_{\Lambda}(\bDDD_{\Lambda}^H \bDDD_{\Lambda})^{-1} \bg
    = (\bDDD_{\Lambda}^{\dag})^H \bg.
   $$
   where $\bg \in \partial \| \ba^*\|_1$.
1. Thus
   
   $$
    |\langle \bDDD_{\Lambda} (\bc_{\Lambda} - \ba^*), \bd_{\omega} \rangle|
    = \gamma |\langle (\bDDD_{\Lambda}^{\dag})^H \bg, \bd_{\omega} \rangle|
    = \gamma |\langle \bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg \rangle|
   $$
   using the fact that $\langle \bA \bx, \by \rangle = \langle \bx, \bA^H \by \rangle$.
1. Also, we recall that $\widehat{\bx}_{\Lambda} = \bDDD_{\Lambda} \bc_{\Lambda}$. 
1. Putting the back in {eq}`eq:e50c94b1-d1c3-47c3-9c36-ac384b1a48da` we obtain:
   
   ```{math}
    :label: eq:183f4aac-4abf-43c1-8d8b-f0196da487fc
    L (\ba^* + \delta \be_{\omega}) - L (\ba^*) >
    |\delta| \left [\gamma -  \gamma |\langle \bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg \rangle| 
    - |\langle \bx - \widehat{\bx}_{\Lambda},  \bd_{\omega} \rangle|\right ].
   ```
1. In {eq}`eq:183f4aac-4abf-43c1-8d8b-f0196da487fc`, the L.H.S. is non-negative
   (our real goal) whenever the term in the bracket on the R.H.S. is non-negative
   (since $|\delta|$ is positive).
1. Therefore we want that
   
   $$
    \gamma -  \gamma |\langle \bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg \rangle| 
    - |\langle \bx - \widehat{\bx}_{\Lambda},  \bd_{\omega} \rangle| \geq 0.
   $$
1. This can be rewritten as
   
   $$
    |\langle \bx - \widehat{\bx}_{\Lambda},  \bd_{\omega} \rangle| \leq \gamma \left [ 1 - |\langle \bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg \rangle| \right ].
   $$
1. Since this condition should hold for every $\omega \notin \Lambda$,
   hence we maximize the L.H.S. and minimize the R.H.S. over  $\omega \notin \Lambda$.
1. We get
   
   $$
    \underset{\omega \notin \Lambda}{\max}|\langle \bx - \widehat{\bx}_{\Lambda},  \bd_{\omega} \rangle|
    \leq \underset{\omega \notin \Lambda}{\min} \gamma \left [ 1 - |\langle \bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg \rangle|\right ]
    = \gamma \left [1 - \underset{\omega \notin \Lambda}{\max}|\langle \bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg \rangle|\right ].
   $$
1. Recall that $ \bx - \widehat{\bx}_{\Lambda}$ is orthogonal to the space spanned
   by atoms in $\bDDD_{\Lambda}$.
1. Hence
   
   $$
    \underset{\omega \notin \Lambda}{\max}|\langle \bx - \widehat{\bx}_{\Lambda},  \bd_{\omega} \rangle| 
    = \underset{\omega}{\max}|\langle \bx - \widehat{\bx}_{\Lambda},  \bd_{\omega} \rangle|
    = \| \bDDD^H (  \bx - \widehat{\bx}_{\Lambda}) \|_{\infty}.
   $$
1. This gives us the desired sufficient condition
   
   $$
    \| \bDDD^H (  \bx - \widehat{\bx}_{\Lambda}) \|_{\infty} 
    \leq \gamma \left [1 - \underset{\omega \notin \Lambda}{\max}|\langle \bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg \rangle|\right ].
   $$
1. This condition still uses $\bg$. We know that $\| \bg \|_{\infty} \leq 1$.
1. Let us simplify as follows: 
   
   $$
    |\langle \bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg \rangle|
    &= | (\bDDD_{\Lambda}^{\dag} \bd_{\omega})^H \bg |\\
    &=  \| (\bDDD_{\Lambda}^{\dag} \bd_{\omega})^H \bg \|_{\infty}\\
    &\leq \| (\bDDD_{\Lambda}^{\dag} \bd_{\omega})^H \|_{\infty} \| \bg \|_{\infty}\\
    &= \| (\bDDD_{\Lambda}^{\dag} \bd_{\omega})\|_1 \| \bg \|_{\infty}\\
    &\leq \| (\bDDD_{\Lambda}^{\dag} \bd_{\omega})\|_1.
   $$
1. Another way to understand this is as follows. For any vector $\bv \in \CC^D$
   
   $$
    | \langle \bv, \bg \rangle | 
    &= | \sum_{i=1}^D \overline{g_i} v_i | \\
    &\leq \sum_{i=1}^D |g_i | | v_i | \\
    &\leq \left [\sum_{i=1}^D | v_i | \right ] \| \bg \|_{\infty}\\
    &\leq \| \bv \|_1.
   $$
1. Thus

   $$
    |\langle \bDDD_{\Lambda}^{\dag} \bd_{\omega}, \bg \rangle| \leq \|\bDDD_{\Lambda}^{\dag} \bd_{\omega}\|_1.
   $$
1. Thus, it is also sufficient that
   
   $$
    \| \bDDD^H (  \bx - \widehat{\bx}_{\Lambda}) \|_{\infty} 
    \leq \gamma \left [1 - \underset{\omega \notin \Lambda}{\max} \| (\bDDD_{\Lambda}^{\dag} \bd_{\omega})\|_1 \right ].
   $$
````
