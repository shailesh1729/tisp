(sec:ssm:srr)=
# Sparse and Redundant Representations

## Dictionaries

```{index} Dictionary, Atom
```
````{prf:definition} Dictionary
:label: def-ssm-dictionary

A *dictionary* for $\CC^N$ is a finite collection $\bDDD$ of unit-norm vectors
which span the whole space.

The elements of a dictionary are called *atoms* and they are denoted by $\phi_{\omega}$
where $\omega$ is drawn from an index set $\Omega$.

The dictionary is written as 

$$
\bDDD = \{\phi_{\omega} : \omega \in \Omega \}
$$
where

$$
\| \phi_{\omega} \|_2 = 1 \Forall \omega \in \Omega
$$
and every signal $\bx \in \CC^N$ can be expressed as

$$
\bx = \sum_{\omega \in \Omega} c_{\omega} \phi_{\omega}.
$$
We use the letter $D$ to denote the number of elements in the dictionary; i.e.,

$$
D = | \Omega |.
$$
````
This definition is adapted from {cite}`tropp2004greed`.

The indices may have an interpretation, such as the time-frequency or time-scale localization
of an atom, or they may simply be labels without any underlying meaning.

Note that the dictionary need not provide a unique representation for any vector $\bx \in \CC^N$,
but it provides at least one representation for each $\bx \in \CC^N$.

When $D=N$ we have a set of unit norm vectors which span the whole of $\CC^N$.
Thus we have a basis (not-necessarily an orthonormal basis).
A dictionary cannot have $D < N$. The more interesting case is when $D > N$.

## Redundant Dictionaries and Sparse Signals

With $D > N$, clearly there are more atoms than necessary to provide
a representation of every signal $\bx \in \CC^N$.
Thus such a dictionary is able provide multiple representations to same vector $\bx$.
We call such dictionaries *redundant dictionaries* or *over-complete dictionaries*.

In contrast a basis with $D=N$ is called a *complete dictionary*.
A special class of signals is those signals which have a sparse representation in a given 
dictionary $\bDDD$.

````{prf:definition} $(\bDDD,K)$-sparse signals
:label: def-ssm-d-k-sparse-signal

A signal $\bx \in \CC^N$ is called $(\bDDD,K)$-sparse if it can be 
expressed as a linear combination of at-most $K$ atoms from the dictionary 
$\bDDD$.
````
Normally, for sparse signals, we have $K \ll D$.
It is usually expected that $K \ll N$ also holds.

Let $\Lambda \subset \Omega$ be a subset of indices with $|\Lambda|=K$.

Let $\bx$ be any signal in $\CC^N$ such that $\bx$ can be expressed as

$$
\bx = \sum_{\lambda \in \Lambda} b_{\lambda} \phi_{\lambda} \quad \text{where } b_{\lambda}  \in \CC.
$$

Note that this is not the only possible representation of $\bx$ in $\bDDD$. This is
just one of the possible representations of $\bx$. The special feature of this representation
is that it is $K$-sparse i.e. only at most $K$ atoms from the dictionary are being used.

Now there are $\binom{D}{K}$ ways in which we can choose a set of $K$ atoms from the 
dictionary $\bDDD$. 

Thus the set of $(\bDDD,K)$-sparse signals is given by

$$
\Sigma_{(\bDDD,K)} = \{\bx \in \CC^N \ST  
\bx = \sum_{\lambda \in \Lambda} b_{\lambda} \phi_{\lambda}, 
\quad \Lambda \subseteq \Omega, | \Lambda | = K \}.
$$
    
This set $\Sigma_{(\bDDD,K)}$ is dependent on the chosen dictionary $\bDDD$.
In the sequel, we will simply refer to it as $\Sigma_K$.

````{prf:example} $K$-sparse signals for standard basis
:label: ex-ssm-k-sparse-signal-set-standard-basis

For the special case where $\bDDD$ is nothing but the standard basis of $\CC^N$, then

$$
\Sigma_K = \{ \bx  \in \CC^N \ST \| \bx \|_0 \leq K\};
$$
i.e., the set of signals which have $K$ or less non-zero elements.
````

````{prf:example} $K$-sparse signals for orthonormal basis
:label: ex-ssm-k-sparse-signal-set-onb

In contrast if we choose an orthonormal basis $\Psi$ such that every
$\bx \in \CC^N$ can be expressed as

$$
\bx = \Psi \ba
$$
then with the dictionary $\bDDD = \Psi$, the set of $K$-sparse signals is given by

$$
\Sigma_K = \{ \bx = \Psi \ba \ST \| \ba \|_0 \leq K\}.
$$
````

We also note that for a specific choice of $\Lambda \subseteq \Omega$
with $|\Lambda| = K$, the set of vectors

$$
\{\bx \in \CC^N \ST 
\bx = \sum_{\lambda \in \Lambda} b_{\lambda} \phi_{\lambda} \}
= \span \{\phi_{\lambda} \ST \lambda \in \Lambda \} 
$$
form a subspace of $\CC^N$.

So we have $\binom{D}{K}$ $K$-sparse subspaces contained in the dictionary $\bDDD$.
And the $K$-sparse signals lie in the *union of these subspaces*. 


(sec:ssm:sparse:approximation:problem)=
## Sparse Approximation Problem

In sparse approximation problem, we attempt to approximate a given signal $\bx \in \CC^N$ as
a linear combination of $K$ atoms from the dictionary $\bDDD$ where $K \ll N$ and
typically $N \ll D$;
i.e., the number of atoms in a dictionary $\bDDD$ is typically much larger
than the ambient signal space dimension $N$.

Naturally, we wish to obtain a best possible sparse representation of $\bx$
over the atoms $\phi_{\omega} \in \bDDD$ which minimizes the approximation error. 

Let $\Lambda$ denote the index set of atoms which are used to create a $K$-sparse 
representation of $\bx$ where $\Lambda \subset \Omega$ with $|\Lambda| = K$.

Let $\bx_{\Lambda}$ denote an approximation of $\bx$
over the set of atoms indexed by $\Lambda$.

Then we can write  $\bx_{\Lambda}$ as

$$
\bx_{\Lambda} = \sum_{\lambda \in \Lambda} b_{\lambda} \phi_{\lambda} 
\quad \text{where } b_{\lambda}  \in \CC.
$$

````{div}
We put all complex valued coefficients $b_{\lambda}$  in the sum into a list $\bb_{\Lambda}$.
The approximation error is given by

$$
\be  = \| \bx - \bx_{\Lambda} \|_2.
$$

Clearly we would like to minimize the approximation error over all possible choices of $K$ atoms
and corresponding set of coefficients $\bb_{\Lambda}$.

Thus the sparse approximation problem can be cast as a minimization problem given by

```{math}
:label: eq-ssm-sparse-approximation

\underset{|\Lambda| = K}{\text{min}} \, \underset{\bb_{\Lambda}}{\text{min}} 
\left \| \bx -  \sum_{\lambda \in \Lambda} b_{\lambda} \phi_{\lambda} \right \|_2.
```

If we choose a particular $\Lambda$, then the inner minimization problem becomes
a straight-forward least squares problem. 
But there are $\binom{D}{K}$ possible choices of $\Lambda$ and solving the
inner least squares problem for each of them becomes prohibitively expensive.

We reemphasize here that in this formulation we are using a *fixed* dictionary $\bDDD$
while the vector $\bx \in \CC^N$ is *arbitrary*.

This problem is known as $(\bDDD, K)$-SPARSE approximation problem.

A related problem is known as $(\bDDD, K)$-EXACT-SPARSE problem 
where it is known a-priori that $\bx$ is a linear combination of at-most $K$ atoms
from the given dictionary $\bDDD$ i.e. $\bx$ is a $K$-sparse signal as 
defined above for the dictionary $\bDDD$.

This formulation simplifies the minimization problem {eq}`eq-ssm-sparse-approximation` since
it is known a priori that for $K$-sparse signals, a $0$ approximation error can be achieved.
The only problem is to find a set of subspaces from the $\binom{D}{K}$ possible $K$-sparse
subspaces which are able to provide a $K$-sparse representation of $\bx$ and among them
choose one. It is imperative to note that even the $K$-sparse representation need not
be unique.

Clearly the EXACT-SPARSE problem is simpler than the SPARSE approximation problem.
Thus if EXACT-SPARSE problem is NP-Hard then so is the harder SPARSE-approximation problem.
It is expected that solving the EXACT-SPARSE problem will provide insights into solving the
SPARSE problem.

In {prf:ref}`res-ssm-sparse-unique-2onb` we identified conditions
under which a sparse representation for a given vector $\bx$ in a two-ortho-basis is unique. 
It would be useful to get similar conditions for general dictionaries. such conditions
would help us guarantee the uniqueness of EXACT-SPARSE problem.
````

 
## Synthesis and Analysis

The atoms of a dictionary $\bDDD$ can be organized into a $N \times D$ matrix as follows:

$$
\Phi \triangleq \begin{bmatrix}
\phi_{\omega_1} & \phi_{\omega_2} & \dots & \phi_{\omega_D}
\end{bmatrix}.
$$
where $\Omega = \{\omega_1, \omega_2, \dots, \omega_N\}$ is the index set for the atoms
of $\bDDD$.
We recall that $\phi_{\omega} \in \CC^N$, hence they have a column
vector representation in the standard basis for $\CC^N$.
The order of columns doesn't matter as long as it remains fixed once chosen.

Thus in matrix terminology a representation of $\bx \in \CC^N$ in the dictionary can
be written as

$$
    \bx = \Phi \bb
$$
where $\bb \in \CC^D$ is a vector of coefficients to produce a superposition $\bx$
from the atoms of dictionary $\bDDD$. 
Clearly with $D > N$, $\bb$ is not unique.
Rather for every vector
$\bz \in \NullSpace(\Phi)$, we have:

$$
\Phi (\bb + \bz) = \Phi \bb + \Phi \bz = \bx + \bzero = \bx.
$$

```{index} Synthesis matrix
```
````{prf:definition} Synthesis matrix
:label: def:ssm:dictionary:synthesis_matrix

The matrix $\Phi$ is called a *synthesis matrix* since $\bx$
is synthesized from the columns of
$\Phi$ with the coefficient vector $\bb$.
````
We can also view the synthesis matrix $\Phi$ as a linear operator from $\CC^D$ to $\CC^N$.

There is another way to look at $\bx$ through $\Phi$. 

```{index} Analysis matrix
```
````{prf:definition} Analysis matrix
:label: def-ssm-dict-analysis-matrix

The conjugate transpose $\Phi^H$ of the synthesis matrix $\Phi$ is called the *analysis matrix*.
It maps a given vector $\bx \in \CC^N$ to a list of inner products with the dictionary:

$$
\bc = \Phi^H \bx 
$$
where $\bc \in \CC^D$.
````
Note that in general $\bx \neq \Phi (\Phi^H \bx)$ unless $\bDDD$ is an orthonormal basis.


````{prf:definition} $(\bDDD, K)$ EXACT SPARSE problem
:label: def-ssm-d-k-exact-sparse-problem

With the help of synthesis matrix $\Phi$, the $(\bDDD, K)$ EXACT SPARSE problem
can now be written as

```{math}
:label: eq-ssm-d-k-exact-sparse-problem

& \underset{\ba}{\text{minimize}} 
& &  \| \ba \|_0 \\
& \text{subject to }
& &  \bx = \Phi \ba\\
& \text{and }
& &  \| \ba \|_0 \leq K
```
````

If $\bx \notin \Sigma_K$, then the EXACT SPARSE problem is infeasible.
Otherwise, we are looking to find the sparsest possible solution.

````{prf:definition} $(\bDDD, K)$ SPARSE approximation problem
:label: def-ssm-d-k-sparse-approx-prob

With the help of synthesis matrix $\Phi$, the $(\bDDD, K)$ SPARSE approximation
problem can now be written as

```{math}
:label: eq-ssm-d-k-sparse-approx-problem

& \underset{\ba}{\text{minimize}} 
& &  \| \bx - \Phi \ba \|_2 \\
& \text{subject to }
& &  \| \ba \|_0 \leq K.
```
````

This problem can be visualized as a projection of $\bx$ on to
the set $\Sigma_K$. Hence, it always has a solution.



 
## P-Norms
 
There are some simple and useful results on relationships between 
different $p$-norms listed in this section. We also discuss
some interesting properties of $l_1$-norm specifically.

```{index} Sign vector; complex
```
````{prf:definition} Complex sign vector
:label: def:ssm:sign_vector

Let $\bv \in \CC^N$. Let the entries in $\bv$ be represented as

$$
v_k = r_k \exp (i \theta_k)
$$
where $r_k = | v_k |$ with the convention that $\theta_k = 0$
whenever $r_k = 0$.

The sign vector for $\bv$ denoted by $\sgn(\bv)$ is defined as

$$
\sgn(\bv)  = \begin{bmatrix}\sgn(v_1) \\ \vdots \\ \sgn(v_N)  \end{bmatrix}
$$
where

$$
\sgn(v_k) = \begin{cases}
\exp (i \theta_k) & \text{ if } r_k \neq 0;\\
0 & \text{ if } r_k = 0.
\end{cases}
$$
````

````{prf:lemma} $\ell_1$ norm as product of vector with its sign
:label: res:ssm:l1_norm_as_inner_product_with_sign_vector

For any $\bv \in \CC^N$: 

$$
\| \bv \|_1 = \sgn(\bv)^H \bv = \langle \bv , \sgn(\bv) \rangle.
$$
````
````{prf:proof}
This follows from:

$$
\| \bv \|_1 = \sum_{k=1}^N r_k 
= \sum_{k=1}^N \left [r_k e^{i \theta_k} \right ] e^{- i \theta_k} 
= \sum_{k=1}^N v_k e^{- i \theta_k} = \sgn(\bv)^H \bv.
$$
Note that whenever $v_k = 0$,
corresponding $0$ entry in $\sgn(\bv)$ has no effect on the sum.
````

````{prf:lemma} Equivalence of $\ell_1$ and $\ell_2$ norms
:label: lem:ssm:l1_norm_l2_bounds

Suppose $\bv \in \CC^N$.  Then

$$
\| \bv \|_2 \leq \| \bv\|_1 \leq \sqrt{N} \| \bv \|_2.
$$
````

````{prf:proof}
For the lower bound, we go as follows

$$
\| \bv \|_2^2 
= \sum_{i=1}^N | v_i|^2  
\leq \left ( \sum_{i=1}^N | v_i|^2  + 2 \sum_{i, j, i \neq j} | v_i | | v_j| \right )
= \left ( \sum_{i=1}^N | v_i| \right )^2 = \| \bv \|_1^2.
$$
This gives us

$$
\| \bv \|_2 \leq \| \bv \|_1.
$$
We can write $\ell_1$ norm as

$$
\| \bv \|_1 = \langle \bv, \sgn (\bv) \rangle.
$$
By Cauchy-Schwartz inequality we have

$$
\langle \bv, \sgn (\bv) \rangle \leq  \| \bv \|_2  \| \sgn (\bv) \|_2. 
$$ 
Since $\sgn(\bv)$ can have at most $N$ non-zero values, each with magnitude 1,

$$
\| \sgn (\bv) \|_2^2 \leq N 
\implies \| \sgn (\bv) \|_2 \leq \sqrt{N}.
$$
Thus, we get

$$
\| \bv \|_1  \leq \sqrt{N} \| \bv \|_2.
$$
````

````{prf:lemma} Equivalence of $\ell_2$ and $\ell_{\infty}$ norms
:label: res:ssm:l2_upper_bound_max_norm

Let $\bv \in \CC^N$. Then

$$
\| \bv \|_2 \leq \sqrt{N} \| \bv \|_{\infty}.
$$
````
````{prf:proof}
This follows from:

$$
\| \bv \|_2^2 
= \sum_{i=1}^N | v_i |^2 
\leq N \underset{1 \leq i \leq N}{\max} ( | v_i |^2) 
= N \| \bv \|_{\infty}^2.
$$
Thus

$$
\| \bv \|_2 \leq \sqrt{N} \| \bv \|_{\infty}.
$$
````
````{prf:lemma} Relationship between $p$-norms
:label: res:ssm:p_q_norm_bounds

Let $\bv \in \CC^N$.
Let $1 \leq p, q \leq \infty$.
Then

$$
\| \bv \|_q \leq \| \bv \|_p \text{ whenever } p \leq q.
$$
````
````{prf:proof}
TBD
````

````{prf:lemma}
:label: res:ssm:one_vec_l1_norm

Let $\bone \in \CC^N$ be the vector of all ones; i.e., $\bone = (1, \dots, 1)$.
Let $\bv \in \CC^N$ be some arbitrary vector.
Let $| \bv |$ denote the vector of
absolute values of entries in $\bv$;
i.e., $|v|_i = |v_i| \Forall 1 \leq i \leq N$.
Then

$$
\| \bv \|_1 = \bone^T | \bv | = \bone^H | \bv |.
$$ 
````
````{prf:proof}
This follows from:

$$
\bone^T | \bv | = \sum_{i=1}^N  | v |_i =   \sum_{i=1}^N  | v_i | = \| \bv \|_1.
$$
Finally since $\bone$ consists only of real entries, hence its transpose and Hermitian 
transpose are same.
````

````{prf:lemma}
:label: res:ssm:ones_matrix_l1_norm

Let $\OneMat \in \CC^{N \times N}$ be a square matrix of all ones. Let $\bv \in \CC^N$ 
be some arbitrary vector.
Then

$$
|\bv|^T \OneMat | \bv | = \| \bv \|_1^2.
$$
````
````{prf:proof}
We know that

$$
\OneMat = \bone \bone^T
$$
Thus,

$$
|\bv|^T \OneMat | \bv |  
= |\bv|^T  \bone \bone^T | \bv |  
= (\bone^T | \bv | )^T (\bone^T | \bv |) 
=  \| \bv \|_1 \| \bv \|_1 = \| \bv \|_1^2.
$$
We used the fact that $\| \bv \|_1 = \bone^T | \bv |$.
````

````{prf:theorem} An upper bound on the $k$-th largest value
:label: res:ssm:k_th_largest_entry_l1_norm

$k$-th largest (magnitude) entry in a vector
$\bx \in \CC^N$ denoted by $x_{(k)}$ obeys

```{math}
:label: eq:ssm:k_th_largest_entry_l1_norm

| x_{(k)} | \leq  \frac{\| \bx \|_1}{k}.
```
````

````{prf:proof}
Let $n_1, n_2, \dots, n_N$ be a permutation of $\{ 1, 2, \dots, N \}$ such that

$$
|x_{n_1} | \geq  | x_{n_2} | \geq \dots \geq  | x_{n_N} |.
$$
Thus, the $k$-th largest entry in $\bx$ is $x_{n_k}$.
It is clear that

$$
\| \bx \|_1 = \sum_{i=1}^N | x_i | = \sum_{i=1}^N |x_{n_i} |.
$$
Obviously

$$
|x_{n_1} | \leq \sum_{i=1}^N |x_{n_i} | = \| \bx \|_1.
$$
Similarly

$$
k |x_{n_k} | = |x_{n_k} | + \dots + |x_{n_k} |
\leq |x_{n_1} | + \dots + |x_{n_k} | 
\leq \sum_{i=1}^N |x_{n_i} | 
\leq  \| \bx \|_1.
$$
Thus

$$
|x_{n_k} |  \leq \frac{\| \bx \|_1}{k}.
$$
````

## Sparse Signals

```{div}
In this subsection we explore some useful properties of $\Sigma_K$, 
the set of $K$-sparse signals in standard basis
for $\CC^N$.

We recall that

$$
\Sigma_K  = \{ \bx \in \CC^N \ST \| \bx \|_0 \leq K \}.
$$

We established before that this set is a union of $\binom{N}{K}$ subspaces of $\CC^N$ each of which
is is constructed by an index set $\Lambda \subset \{1, \dots, N \}$ with $| \Lambda | = K$ choosing
$K$ specific dimensions of $\CC^N$. 

We first present some lemmas which connect the $l_1$, $l_2$ and $l_{\infty}$ norms of vectors
in $\Sigma_K$.
```

````{prf:lemma} Relation between norms of sparse vectors
:label: lem:u_sigma_k_norms

Suppose $\bu \in \Sigma_K$.
Then

$$
\frac{\| \bu\|_1}{\sqrt{K}} \leq \| \bu \|_2 \leq \sqrt{K} \| \bu \|_{\infty}.
$$
````

````{prf:proof}
Due to {prf:ref}`res:ssm:l1_norm_as_inner_product_with_sign_vector`,
we can write $\ell_1$ norm as

$$
\| \bu \|_1 = \langle \bu, \sgn (\bu) \rangle.
$$
By Cauchy-Schwartz inequality we have

$$
\langle \bu, \sgn (\bu) \rangle \leq  \| \bu \|_2  \| \sgn (\bu) \|_2 
$$ 
Since $\bu \in \Sigma_K$,
$\sgn(\bu)$ can have at most $K$ non-zero values each with magnitude 1.
Thus, we have

$$
\| \sgn (\bu) \|_2^2 \leq K \implies \| \sgn (\bu) \|_2 \leq \sqrt{K}.
$$
Thus we get the lower bound

$$
\| \bu \|_1 \leq \| \bu \|_2 \sqrt{K}
\implies \frac{\| \bu \|_1}{\sqrt{K}} \leq \| \bu \|_2.
$$

Now $| u_i | \leq \max(| u_i |) = \| \bu \|_{\infty}$.
So we have

$$
\| \bu \|_2^2 = \sum_{i= 1}^{N} | u_i |^2 \leq  K \| \bu \|_{\infty}^2
$$
since there are only $K$ non-zero terms in the expansion of $\| \bu \|_2^2$.
This establishes the upper bound:

$$
\| \bu \|_2 \leq \sqrt{K} \| \bu \|_{\infty}.
$$
````


