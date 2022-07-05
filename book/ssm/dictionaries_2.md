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



 
## Coherence
In this subsection we develop some more bounds using coherence of a dictionary.
As usual, we will be considering an overcomplete dictionary
$\bDDD \in \CC^{N \times D}$ consisting
of $D$ atoms.
The coherence of $\bDDD$ is denoted by $\mu (\bDDD)$.
In short we will simply write it as $\mu$.
A subdictionary will be indexed by an index set $\Lambda$
consisting of linearly independent atoms. 

````{prf:theorem}
:label: res:proj:coherence:2_infty_norm_pseudo_inverse_upper_bound

Suppose that $(K - 1) \mu < 1$ and assume that $| \Lambda | \leq K$.
Then 

$$
\| \bDDD_{\Lambda}^{\dag} \|_{2 \to \infty} 
\leq \frac{1}{\sqrt{ 1 - ( K - 1) \mu}}.
$$
Equivalently, the rows of $\bDDD_{\Lambda}^{\dag}$ have $\ell_2$ norms
no greater than $\frac{1}{\sqrt{ 1 - ( K - 1) \mu}}$.
````
````{prf:proof}
We recall that the operator norm $\| \bDDD_{\Lambda}^{\dag} \|_{2 \to \infty}$
computes the  maximum $\ell_2$ norm among the rows of $\bDDD_{\Lambda}^{\dag}$.
TODO COMPLETE ITS PROOF.
````

The following definition is due to {cite}`donoho2003optimally,chen2006theoretical`.

````{prf:definition}
:label: def:proj:coherence:mu_half_G

Let $\bG = \bDDD^H \bDDD$ be the Gram matrix for dictionary $\bDDD$.
We define $\mu_{1/2}(\bG)$ as the smallest number $m$
such that the sum of magnitudes of a
collection of $m$ off-diagonal entries in a single row
or column of the Gram matrix $\bG$ is at least $\frac{1}{2}$.
````
This quantity was introduced in {cite}`donoho2003optimally` for developing
more accurate bounds compared to bounds based on coherence. At that
time the idea of Babel function was not available. A careful examination reveals
that $\mu_{1/2}(\bG)$ can be related to Babel function.

````{prf:theorem}
:label: res:mu_half_g_coherence_bound

$$
\mu_{1/2}(\bG) \geq \frac{1}{2\mu}.
$$
````
````{prf:proof}
Since $\mu$ is the maximum absolute value of any off diagonal term in
$\bG = \bDDD^H \bDDD$, hence sum of any $m$ terms, say $T$, is bounded by 

$$
T \leq m \mu.
$$
Thus

$$
T \geq \frac{1}{2} \implies m \mu \geq \frac{1}{2} \implies m \geq \frac{1}{2\mu}.
$$
Since $\mu_{1/2}(\bG)$ is the minimum number of
off diagonal terms whose sum exceeds $1/2$, hence

$$
\mu_{1/2}(\bG) \geq \frac{1}{2\mu}.
$$
````

The following result is due to {cite}`donoho2003optimally`.
````{prf:theorem}
:label: res:proj:coherence:spark_lower_bound_mu_half

$$
\spark(\bDDD) \geq 2 \mu_{1/2}(G) +1.
$$
````
````{prf:proof}
We proceed as follows.

1. Let $\bh \in \NullSpace(\bDDD)$.
1. Then
   
   $$
    \bDDD \bh  = \bzero \implies \bG \bh = \bDDD^H \bDDD \bh  = \bzero.
   $$
1. Subtracting both sides with $\bh$ we get
   
   $$
    \bG \bh - \bh = (\bG  - \bI) \bh = -\bh.
   $$
1. Let $\Lambda = \supp(\bh)$.
1. By taking columns indexed by $\Lambda$
   from $\bG - \bI$ and corresponding entries in $\bh$,
   we can write:
   
   $$
    (\bG - \bI)_{\Lambda} \bh_{\lambda} = - \bh.
   $$
1. Taking $\ell_{\infty}$ norm on both sides we get
   
   $$
    \| \bh \|_{\infty} = \| (\bG - \bI)_{\Lambda} \bh_{\lambda} \|_{\infty}.
   $$
1. We know that
   
   $$
    \| (\bG - \bI)_{\Lambda} \bh_{\lambda} \|_{\infty} 
    \leq \| (\bG - \bI)_{\Lambda} \|_{\infty} \| \bh_{\lambda} \|_{\infty}
   $$
1. It is easy to see that:
   
   $$
    \| \bh_{\lambda} \|_{\infty} = \| \bh \|_{\infty}.
   $$
1. Thus
   
   $$
    \| \bh \|_{\infty} \leq 
    \| (\bG - \bI)_{\Lambda} \|_{\infty} \| \bh \|_{\infty}.
   $$
1. This gives us
   
   $$
    \| (\bG - \bI)_{\Lambda} \|_{\infty} \geq 1.
   $$
1. But $\| (\bG - \bI)_{\Lambda} \|_{\infty}$ is nothing
   but the maximum sum of magnitudes
   of off diagonal entries in $\bG$ along a row in $\bG_{\Lambda}$.
1. Consider any row in $(\bG - \bI)_{\Lambda}$.
1. One of the entries in the row
   (on the main diagonal of $\bG - \bI$) is 0.
1. Thus, there are a maximum of
   $|\Lambda | - 1$ nonzero entries in the row.
1. $\Lambda$ is smallest when $|\Lambda | = \spark(\bDDD)$.
1. For such a $\Lambda$, there exists a row in $\bG$
   such that the sum of  $\spark(\bDDD) - 1$
   off diagonal entries in the row exceeds 1.
1. Let $n$ denote the minimum number of
   off diagonal elements on a row or
   a column of $\bG$ such that the sum of their magnitudes exceeds one. 
1. Clearly
   
   $$
    \spark(\bDDD) - 1 \geq n.
   $$
1. It is easy to see that
   
   $$
    n \geq 2 \mu_{1/2} (\bG)
   $$
   i.e. minimum number of off diagonal elements summing up to 1 or more
   is at least twice the minimum number of off diagonal elements 
   summing up to $\frac{1}{2}$
   or more on any row (or column due to Hermitian property).
1. Thus
   
   $$
    \spark(\bDDD) - 1 \geq 2 \mu_{1/2} (G).
   $$
1. Rewriting, we get
  
   $$
    \spark(\bDDD) \geq 2 \mu_{1/2} (G) + 1.
   $$
````


 
(sec:proj:babel)=
## Babel function

In this subsection, we provide a more general development
of Babel function for a pair of dictionaries. 

1. When we consider a single dictionary, we will use $\bDDD$
   as the dictionary. 
1. When considering a pair of dictionaries of equal size,
   we would typically label them as $\Phi$ and $\Psi$ with
   both $\Phi, \Psi \in \CC^{N \times D}$.
1. We will  assume that the dictionaries are full rank as they
   span the signal space $\CC^N$.
1. Why a pair of dictionaries?
   1. We consider $\Phi$ as a modeling dictionary from which the sparse signals

      $$
      \bx \approx \Phi \ba
      $$
      are built. 
    1. $\Psi$ on the other hand is the sensing dictionary which 
       will be used to compute correlations with the signal $\bx$ 
       and try to estimate the approximation $\ba$.
    1. Ideally, $\Phi$ and $\Psi$ should be same.
    1. But in real life, we may not know $\Phi$ correctly.
    1. Hence, $\Psi$ would be a dictionary slightly different from $\Phi$.
    

## p-Babel Function


See {cite}`gribonval2008atoms` for reference.

````{prf:definition} $p$-Babel function over $\Lambda$
:label: def:proj:babel:p_babel_function

Consider an index set $\Lambda \subset \{1, \dots, D \}$ indexing
a subset of atoms in $\Phi$ and $\Psi$.
The *$p$-Babel function*  over ${\Lambda}$ is defined as

```{math}
:label: eq:proj:e1817ba8-e5b2-448b-a3e5-e793f5d9bf3c

\mu_p(\Phi, \Psi, \Lambda) \triangleq 
\underset{l \notin \Lambda}{\sup}
\left (\sum_{j \in \Lambda} 
    |\langle \phi_j, \psi_l \rangle |^p \right )^{\frac{1}{p}}.
```
````

What is going on here? 

````{div}
1. Consider the row vector
   
   $$
    \bv^l  = \psi_l^H \Phi_{\Lambda}.
   $$
1. This vector contains inner products of modeling atoms in
   $\Phi$ indexed by $\Lambda$ with the sensing atom $\psi_l$.
1. Now
   
   $$
    \| \bv^l \|_p = 
    \left ( \sum_{i} | v^l_i |^p \right )^{\frac{1}{p}}
    =  \left ( \sum_{j \in \Lambda} 
        | \langle \phi_j, \psi_l \rangle |^p \right )^{\frac{1}{p}}
   $$
1. This is the term in
   {eq}`eq:proj:e1817ba8-e5b2-448b-a3e5-e793f5d9bf3c`.
1. Thus
   
   $$
    \mu_p(\Phi, \Psi, \Lambda) 
    = \underset{l \notin \Lambda}{\sup} \| v^l \|_p.
   $$
1. $\| v^l \|_p$ is a measure of the correlation of the sensing atom
   $\psi_l$ with a group of modeling atoms in $\Phi$
   indexed by $\Lambda$ using the $p$-norm.
1. $\mu_p(\Phi, \Psi, \Lambda)$ attempts to find out a
   sensing atom from $\Psi$ outside the index set $\Lambda$
   which is most correlated to the group of modeling atoms
   in $\Phi$ indexed by $\Lambda$ and returns the maximum
   correlation value.
1. Different choices of $p$-norm lead to different correlation values.

We can also measure a correlation of sensing and modeling 
atoms inside the index set $\Lambda$.

````{prf:definition} Complementary $p$-Babel function over $\Lambda$
:label: def:proj:babel:complementary_p_babel_function

A complement to the $p$-Babel function measures the amount of correlation between atoms *inside* the support $\Lambda$:

```{math}
:label: eq:proj:2337484b-4a0b-4946-9d65-6f935f8e46c5

\mu_p^{\text{in}}(\Phi, \Psi, \Lambda) \triangleq 
\underset{i \in \Lambda}{\sup} \, \mu_p 
\left (\Phi_{\Lambda}, \Psi_{\Lambda}, \Lambda \setminus \{i \} \right). 
```
````

$\mu_p(\Phi_{\Lambda}, \Psi_{\Lambda}, \Lambda \setminus \{i \})$
computes the correlation of $i$-th sensing atom in $\Psi$ with the
modeling atoms in $\Phi$ indexed by $\Lambda \setminus \{i \}$ i.e.
all modeling atoms in $\Lambda$ except the $i$-th modeling atom.

Finally $\mu_p^{\text{in}}(\Phi, \Psi, \Lambda)$ finds the maximum
correlation of any sensing atom inside $\Lambda$ with modeling
atoms inside $\Lambda$ (leaving the corresponding modeling atom).

So far, we have focused our attention to a specific index set $\Lambda$.
We now consider all index sets with $|\Lambda | \leq K$. 

````{prf:definition} $p$ Babel function
:label: def:proj:babel:p_babel_function_K

The Babel function for a pair of dictionaries $\Phi$ and $\Psi$ 
as a function of the sparsity level $K$ is defined as

```{math}
:label: eq:proj:babel:p_babel_function_K

\mu_p(\Phi, \Psi, K) \triangleq
\underset{|\Lambda| \leq K}{\sup}\, 
\mu_p(\Phi, \Psi, \Lambda).
```
Correspondingly, the complement of Babel function is defined as

```{math}
:label: eq:proj:babel:p_babel_function_K_complement

\mu_p^{\text{in}}(\Phi, \Psi, K) \triangleq 
\underset{|\Lambda| \leq K}{\sup}\, 
\mu_p^{\text{in}}(\Phi, \Psi, \Lambda).
```
````

````{div}
It is straightforward to see that

```{math}
:label: eq:f44d0438-9436-4d05-9635-9b2d2a5b8e33

\mu_p^{\text{in}}(\Phi, \Psi, K) \leq \mu_p(\Phi, \Psi, K-1). 
```
````

Now consider the special case where $\bDDD=\Phi=\Psi$. 
In other words, the sensing and modeling dictionaries are same.

We obtain

```{math}
:label: eq:proj:babel:f90d30fc-6bd1-484d-ad33-254daf19ce67

\mu_p(\bDDD, \Lambda) = \underset{l \notin \Lambda}{\sup}
\left (\sum_{j \in \Lambda} |\langle \bd_j, \bd_l \rangle |^p \right )^{\frac{1}{p}}.
```

```{math}
:label: eq:proj:babel:6d675f22-e08b-4125-aed4-1480714efea1

\mu_p^{\text{in}}(\bDDD, \Lambda) =  
\underset{i \in \Lambda}{\sup} \, 
\mu_p \left (\bDDD_{\Lambda}, \Lambda \setminus \{i \} \right). 
```

```{math}
:label: eq:proj:babel:26acec65-b64e-4572-afc6-a0fa59b5e1d9

\mu_p(\bDDD, K) = \underset{|\Lambda| \leq K}{\sup}\, \mu_p(\bDDD, \Lambda).
```

```{math}
:label: eq:proj:babel:6e58b448-6e90-495b-87ec-f97f5752d0bf

\mu_p^{\text{in}}(\bDDD, K) = 
\underset{|\Lambda| \leq K}{\sup}\, 
\mu_p^{\text{in}}(\bDDD, \Lambda).
```
Further by choosing $p=1$, we get

```{math}
:label: eq:proj:babel:4b31df5c-4096-47fc-84dc-e9f51bb503c5

\mu_1(\bDDD, \Lambda) = \underset{l \notin \Lambda}{\sup}
\left (\sum_{j \in \Lambda} |\langle \bd_j, \bd_l \rangle | \right ).
```

```{math}
:label: eq:proj:babel:74e456e6-4d82-48df-ae1a-27f5e89411a6

\mu_1^{\text{in}}(\bDDD, \Lambda) =  
\underset{i \in \Lambda}{\sup} \, 
\mu_1 \left ( \bDDD_{\Lambda}, \Lambda \setminus \{i \} \right). 
```

```{math}
:label: eq:proj:babel:b15e1fe8-2589-4ee8-b28c-fb7f49cc1bba
\mu_1(\bDDD, K) = \underset{|\Lambda| \leq K}{\sup}\, \mu_1(\bDDD, \Lambda).
```

```{math}
:label: eq:proj:babel:3e6b3ee3-1ec2-4f61-98aa-2f49aaa1e8ff

\mu_1^{\text{in}}(\bDDD, K) = 
\underset{|\Lambda| \leq K}{\sup}\, 
\mu_1^{\text{in}}(\bDDD, \Lambda).
```

Finally compare this definition of $\mu_1(\bDDD, K)$ with the
standard definition of {prf:ref}`Babel function <def:babel_function>`
as

```{math}
:label: eq:proj:babel:2eb9efae-0c57-485b-92aa-94e93a1b943f

\mu_1(K) = \underset{|\Lambda| = K}{\max} \; \underset {\psi}{\max} 
\sum_{\Lambda} | \langle \psi, \bd_{\lambda} \rangle |,
```
where the vector $\psi$ ranges over the atoms indexed by
$\Omega \setminus \Lambda$.

We also know that $\mu_1(K)$ is an increasing function of $K$.
Thus,  replacing $|\Lambda| = K$ with $|\Lambda| \leq K$
doesn't make any difference to the value of $\mu_1(K)$.

Careful observation shows that the definitions of 
$\mu_1(K)$ in {eq}`eq:proj:babel:2eb9efae-0c57-485b-92aa-94e93a1b943f`
and $\mu_1(\bDDD, K)$ in
{eq}`eq:proj:babel:b15e1fe8-2589-4ee8-b28c-fb7f49cc1bba`
are exactly the same.

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


