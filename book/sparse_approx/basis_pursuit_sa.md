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