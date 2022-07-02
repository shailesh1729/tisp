# Dictionaries II

This section continues the development of
dictionaries for sparse and redundant representations.


 
## Spark
We present some more results on spark of a dictionary.

### Upper Bounds for Spark

Whenever a set of atoms in a dictionary are linearly dependent,
the dependence corresponds to some vector in its null space. Thus,
identifying the spark of a dictionary essentially amounts of
sifting through the vectors in its null space and finding
one with smallest $\ell_0$-"norm". 
This can be cast as an optimization problem:

```{math}
:label: eq:proj:spark:minimum_l0_nullspace_problem

& \underset{\bv}{\text{minimize}}
& & \| \bv \|_0 \\
& \text{subject to }
& & \bDDD \bv = \bzero.
```
````{div}
Note that the solution $\bv^*$ of this problem is not unique. 
If $\bv^*$ is a solution that $c \bv^*$ for any $c \neq 0$
is also a solution.
Spark is the optimum value of the objective function $\| \bv \|_0$.
We now define a sequence of optimization problems for $k = 1, \dots, D$

```{math}
:label: eq:proj:spark:minimum_l0_nullspace_problem_k
 & \underset{\bv}{\text{minimize}}
 & & \| \bv \|_0 \\
 & \text{subject to }
 & & \bDDD \bv = \bzero, v_k = 1.
```
1. The $k$-th problem constrains the solution to choose atom $\bd_k$ 
   from the dictionary.
1. Since the minimal set of linearly
   dependent atoms in $\bDDD$ will contain at least two vectors,
   hence $\spark(\bDDD)$ would correspond to the optimal value
   of one (or more) of the problems
   {eq}`eq:proj:spark:minimum_l0_nullspace_problem_k`.
1. Formally, if we denote $\bv_k^{0, *}$ as an optimal vector for the problem 
   {eq}`eq:proj:spark:minimum_l0_nullspace_problem_k`,
   then
   
   $$
    \spark(\bDDD) = \underset{1 \leq k \leq D}
    {\text{minimize }}\| \bv_k^{0, *}\|_0.
   $$
1. Thus, solving {eq}`eq:proj:spark:minimum_l0_nullspace_problem` is
   equivalent to solving all $D$ problems specified by
   {eq}`eq:proj:spark:minimum_l0_nullspace_problem_k` and then
   finding the minimum $\ell_0$-"norm" among them.
1. The problems {eq}`eq:proj:spark:minimum_l0_nullspace_problem_k`
   are still computationally intractable.

We now change each of the $\ell_0$-"norm"
{eq}`eq:proj:spark:minimum_l0_nullspace_problem_k`
minimization problems to $\ell_1$-"norm" minimization problems.

```{math}
:label: eq:proj:spark:minimum_l1_nullspace_problem_k
 & \underset{\bv}{\text{minimize }}
 & & \| \bv \|_1 \\
 & \text{subject to }
 & & \bDDD \bv = \bzero, v_k = 1.
```
1. We have a convex objective and convex (linear)
   constraints. These are tractable problems.
1. Let us indicate an optimal solution of
   {eq}`eq:proj:spark:minimum_l1_nullspace_problem_k`
    as $\bv_k^{1, *}$.
1. Since $\bDDD \bv_k^{1, *} = \bzero$,
   hence $\bv_k^{1, *}$ is
   feasible for {eq}`eq:proj:spark:minimum_l0_nullspace_problem_k`.
1. Thus,
   
   $$
   \| \bv_k^{0, *}\|_0 \leq  \| \bv_k^{1, *}\|_0.
   $$
1. This gives us the relationship
   
   $$
   \spark(\bDDD) \leq \underset{1 \leq k \leq D}{\text{minimize }}
   \| \bv_k^{1, *}\|_0.
   $$
````
We formally state the upper bound on $\spark(\bDDD)$ in the following theorem
{cite}`donoho2003optimally`.

````{prf:theorem}
:label: res:proj:spark:upper_bound_l1_problems

Let $\bDDD$ be a dictionary. Then

$$
\spark(\bDDD) \leq \underset{1 \leq k \leq D}{\text{minimize }} \| \bv_k^{1, *}\|_0
$$
where $\bv_k^{1, *}$ is a solution of the problem {eq}`eq:proj:spark:minimum_l1_nullspace_problem_k`. 
````


(sec:dic:dirac_dct_dictionary)=
## Dirac-DCT dictionary

````{prf:definition}
:label: def:dic:dirac_dct_dictionary

The Dirac-DCT dictionary is a two-ortho dictionary consisting of 
the union of the Dirac and the DCT bases.
````
This dictionary is suitable for real signals since both
Dirac and DCT are totally real bases $\in \RR^{N \times N}$. 

The dictionary is obtained by combining the $N \times N$ identity matrix
(Dirac basis)
with the $N \times N$ DCT matrix for signals in $\RR^N$.

Let $\Psi_{\text{DCT}, N}$ denote the DCT matrix for $\RR^N$.
Let $\bI_N$ denote the identity matrix for $\RR^N$. 
Then

$$
\bDDD_{\text{DCT}} = \begin{bmatrix}
\bI_N & \Psi_{\text{DCT}, N}
\end{bmatrix}.
$$
Let

$$
\Psi_{\text{DCT}, N} = \begin{bmatrix}
\psi_1 & \psi_2 & \dots & \psi_N
\end{bmatrix}
$$
The $k$-th column of $\Psi_{\text{DCT}, N}$ is given by

```{math}
:label: eq:dict:dct_matrix_kth_column

\psi_k(n) = \sqrt{\frac{2}{N}} \Omega_k \cos \left (\frac{\pi}{2 N} (2 n - 1) (k - 1) \right ), n = 1, \dots, N,
```
with $\Omega_k = \frac{1}{\sqrt{2}}$ for $k=1$
and $\Omega_k = 1$ for $2 \leq k \leq N$. 

Note that for $k=1$, the entries become

$$
\sqrt{\frac{2}{N}} \frac{1}{\sqrt{2}} \cos 0 = \sqrt{\frac{1}{N}}.
$$
Thus, the $\ell_2$ norm of $\psi_1$ is 1.
We can similarly verify the $\ell_2$ norm of other columns also.
They are all one.

````{prf:theorem}
:label: res:dic:dirac_dct_dictionary_coherence

The Dirac-DCT dictionary has coherence $\sqrt{\frac{2}{N}}$.
````
````{prf:proof}
The coherence of a two ortho basis where one basis is Dirac basis is given by the
magnitude of the largest entry in the other basis.

1. For $\Psi_{\text{DCT}, N}$, the largest value is obtained when $\Omega_k = 1$
    and the $\cos$ term evaluates to 1. 
1. Clearly, 
   
   $$
    \mu (\bDDD_{\text{DCT}}) = \sqrt{\frac{2}{N}}.
   $$
````


````{prf:theorem}
:label: res:dic:dirac_dct_dictionary_babel

The $p$-Babel function for Dirac-DCT dictionary is given by

$$
\mu_p(k) = k^{\frac{1}{p}} \mu \Forall 1\leq k \leq N.
$$
In particular, the standard Babel function
is given by

$$
\mu_1(k) = k\mu
$$
````
````{prf:proof}
TODO prove it.
````


