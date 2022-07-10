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

````{prf:theorem} $\ell_1$ norm as product of vector with its sign
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

````{prf:theorem} Equivalence of $\ell_1$ and $\ell_2$ norms
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

````{prf:theorem} Equivalence of $\ell_2$ and $\ell_{\infty}$ norms
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
````{prf:theorem} Relationship between $p$-norms
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

````{prf:theorem}
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

````{prf:theorem}
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

We first present some results which connect the $l_1$, $l_2$ and $l_{\infty}$ norms of vectors
in $\Sigma_K$.
```

````{prf:theorem} Relation between norms of sparse vectors
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

## Compressible Signals


In this subsection, we first look at some general results and definitions
related to $K$-term approximations of arbitrary signals $\bx \in \CC^N$.
We then define the notion of a compressible signal and study properties related to it.

 
### K-term Approximation of General Signals

```{index} Signal; restriction, Signal; mask
```
````{prf:definition} Restriction of a signal
:label: def:ssm:signal_restriction

Let $\bx \in \CC^N$.
Let $T \subset \{ 1, 2, \dots, N\}$ be any index set.
Further let

$$
T = \{t_1, t_2, \dots, t_{|T|}\}
$$
such that

$$
t_1 < t_2 < \dots < t_{|T|}.
$$
Let $\bx_T \in \CC^{|T|}$ be defined as 

```{math}
:label: eq:ssm:signal_restriction
\bx_T = \begin{pmatrix}
x_{t_1} & x_{t_2}  & \dots & x_{t_{|T|}}
\end{pmatrix}.
```
Then $\bx_T$ is a *restriction* of the signal $\bx$ on the index set $T$.

Alternatively let $\bx_T \in \CC^N$ be defined as

```{math}
:label: eq:ssm:signal_mask

\bx_{T}(i) = \begin{cases}
\bx(i) & \text{ if } i \in T;\\
0 & \text{ otherwise}.
\end{cases}
```
In other words, $\bx_T \in \CC^N$ keeps the entries in $\bx$
indexed by $T$ while sets all other entries to 0.
Then we say  that $\bx_T$ is obtained by *masking* $\bx$ with $T$.
````
As an abuse of notation, we will use any of the two definitions
whenever we are referring to $\bx_T$.
The definition being used should be obvious from the context.

````{prf:example} Restrictions on index sets
:label: ex-ssm-signal-restriction-1

$$
\bx = \begin{pmatrix}
-1 & 5 & 8 & 0 & 0 & -3 & 0 & 0 & 0 & 0
\end{pmatrix} \in \CC^{10}.
$$
Let

$$
T = \{ 1, 3, 7, 8\}.
$$
Then

$$
\bx_T = \begin{pmatrix}
-1 & 0 & 8 & 0 & 0 &  0 & 0 & 0 & 0 & 0
\end{pmatrix} \in \CC^{10}.
$$
Since $|T| = 4$, sometimes we will also write

$$
\bx = \begin{pmatrix}
-1 & 8 & 0 & 0
\end{pmatrix} \in \CC^4.
$$
````

```{index} Signal; $K$-term approximation
```
````{prf:definition} $K$-term signal approximation
:label: def:ssm:k_term_signal_approximation

Let $\bx \in \CC^N$ be an arbitrary signal.
Consider any index set $T \subset \{1, \dots, N \}$
with $|T| = K$.
Then $\bx_T$ is a *$K$-term approximation* of $\bx$.
````

Clearly for any $\bx \in \CC^N$
there are $\binom{N}{K}$ possible $K$-term approximations of $\bx$.

````{prf:example} $K$-term approximation
:label: ex-ssm-k-term-approx-1

Let 

$$
\bx = \begin{pmatrix}
-1 & 5 & 8 & 0 & 0 & -3 & 0 & 0 & 0 & 0
\end{pmatrix} \in \CC^{10}.
$$

Let $T= \{ 1, 6 \}$. Then

$$
\bx_T = \begin{pmatrix}
-1 & 0 & 0 & 0 & 0 & -3 & 0 & 0 & 0 & 0
\end{pmatrix}
$$
is a $2$-term approximation of $\bx$. 

If we choose $T= \{7,8,9,10\}$,
the corresponding $4$-term approximation of $\bx$ is

$$
 \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}.
$$
````

````{prf:definition} $K$-largest entries approximation
:label: def:ssm:largest_entries_signal

Let $\bx \in \CC^N$ be an arbitrary signal.
Let $\lambda_1, \dots, \lambda_N$ be
indices of entries in $\bx$ such that

$$
| x_{\lambda_1} | \geq | x_{\lambda_2} | \geq \dots \geq | x_{\lambda_N} |.
$$
In case of ties, the order is resolved lexicographically;
i.e., if $|x_i| = |x_j|$ 
and $i < j$ then $i$ will appear first in the sequence $\{ \lambda_k \}$.

Consider the index set $\Lambda_K = \{ \lambda_1, \lambda_2, \dots, \lambda_K\}$. 
The restriction of $\bx$ on $\Lambda_K$ given by $x_{\Lambda_K}$
contains the $K$ largest entries $\bx$
while setting all other entries to 0. This is known
as the *$K$ largest entries approximation* of $\bx$. 

This signal is denoted henceforth as $\bx|_K$; 
i.e.

```{math}
:label: eq-ssm-best-k-term-approx

\bx|_K = \bx_{\Lambda_K}
```
where $\Lambda_K$ is the index set corresponding
to $K$ largest entries in $\bx$ (magnitude wise).
````

````{prf:example} Largest entries approximation
:label: ex-ssm-k-largest-entries-approx-1

Let 

$$
\bx  = \begin{pmatrix}
-1 & 5 & 8 & 0 & 0 & -3 & 0 & 0 & 0 & 0
\end{pmatrix}.
$$
Then

$$
\bx|_1 = \begin{pmatrix}
0 & 0 & 8 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}.
$$

$$
\bx|_2 = \begin{pmatrix}
0 & 5 & 8 & 0 & 0 & 0 & 0 & 0 & 0 & 0
\end{pmatrix}.
$$

$$
\bx|_3 = \begin{pmatrix}
0 & 5 & 8 & 0 & 0 & -3 & 0 & 0 & 0 & 0
\end{pmatrix}
$$

$$
\bx|_4 = \bx.
$$
All further $K$ largest entries approximations are same as $\bx$.
````

A pertinent question at this point is:
which $K$-term approximation of $\bx$ is the best 
$K$-term approximation?
Certainly in order to compare two approximations we need
some criterion. 
Let us choose $\ell_p$ norm as the criterion.
The next result gives an interesting result for
best $K$-term approximations in $\ell_p$ norm sense.

````{prf:theorem} Best $K$-term approximation for $\ell_p$ norms
:label: lem:ssm:best_k_term_approximation

Let $\bx \in \CC^N$.
Let the best $K$ term approximation of $\bx$ be obtained by the
following optimization program:

```{math}
:label: eq:best_k_term_approximation_optimization_problem

& \underset{T \subset \{1, \dots, N\}}{\text{maximize}}
& & \| \bx_T \|_p \\
& \text{subject to }
& & |T| = K.
```
where $p \in [1, \infty]$.

Let an optimal solution for this optimization problem be denoted by 
$\bx_{T^*}$. 
Then

$$
\| \bx|_K \|_p = \| \bx_{T^*} \|_p;
$$
i.e., the $K$-largest entries approximation of $\bx$
is an optimal solution to 
{eq}`eq:best_k_term_approximation_optimization_problem`.
````
````{prf:proof}
For $p=\infty$, the result is obvious.
In the following, we focus on $p \in [1, \infty)$.

We note that maximizing $\| \bx_T \|_p$ is equivalent to maximizing
$ \| \bx_T \|_p^p$.

Let $\lambda_1, \dots, \lambda_N$ be
indices of entries in $x$ such that

$$
| x_{\lambda_1} | \geq | x_{\lambda_2} | \geq \dots \geq | x_{\lambda_N} |.
$$
Further let $\{ \omega_1, \dots, \omega_N\}$ be any permutation of $\{1, \dots, N \}$.
Clearly

$$
\| \bx|_K \|_p^{p} = \sum_{i=1}^K |\bx_{\lambda_i}|^{p}  \geq \sum_{i=1}^K |\bx_{\omega_i}|^{p}.
$$

Thus if $T^*$ corresponds to an optimal solution of
{eq}`eq:best_k_term_approximation_optimization_problem`
then 

$$
\| \bx|_K \|_p^{p}  = \| \bx_{T^*} \|_p^{p}.
$$
Thus $\bx|_K$ is an optimal solution to
{eq}`eq:best_k_term_approximation_optimization_problem`.
````

This result helps us establish that whenever we are looking for a best $K$-term 
approximation of $\bx$ under any $\ell_p$ norm, all we have to do is to pickup
the $K$-largest entries in $\bx$.


````{prf:definition} Restriction of a matrix
:label: def:ssm:matrix_restriction

Let $\Phi \in \CC^{M \times N}$.
Let $T \subset \{ 1, 2, \dots, N\}$ be any index set.
Further let

$$
T = \{t_1, t_2, \dots, t_{|T|}\}
$$
such that

$$
t_1 < t_2 < \dots < t_{|T|}.
$$
Let $\Phi_T \in \CC^{M \times |T|}$ be defined as 

```{math}
:label: eq:ssm:matrix_restriction

\Phi_T = \begin{bmatrix}
\phi_{t_1} & \phi_{t_2}  & \dots & \phi_{t_{|T|}}
\end{bmatrix}.
```
Then $\Phi_T$ is a *restriction* of the matrix $\Phi$ on the index set $T$.

Alternatively let $\Phi_T \in \CC^{M \times N}$ be defined as

```{math}
:label: eq:ssm:matrix_mask

(\Phi_{T})_i = \left\{
    \begin{array}{ll}
        \phi_i & \mbox{if $i \in T$};\\
        \bzero & \mbox{otherwise}.
    \end{array}
  \right.
```
In other words, $\Phi_T \in \CC^{M \times N}$
keeps the columns in $\Phi$ 
indexed by $T$ while sets all other columns to $\bzero$.
Then we say that $\Phi_T$ is obtained by *masking* $\Phi$ with $T$.
````
As an abuse of notation, we will use any of the two definitions
whenever we are referring to $\Phi_T$. The definition 
being used should be obvious from the context.

````{prf:theorem}
:label: lem:ssm:restriction_simplification_sparse_vector

Let $\supp(\bx) = \Lambda$. Then 

$$
\Phi \bx = \Phi_{\Lambda} \bx_{\Lambda}.
$$
````

````{prf:proof}
This follows from:

$$
\Phi \bx = \sum_{i=1}^N x_i \phi_i 
= \sum_{\lambda_i \in \Lambda} x_{\lambda_i} \phi_{\lambda_i}
= \Phi_{\Lambda} x_{\Lambda}.
$$
````
The result remains valid whether we use
the restriction or the mask version of $\bx_{\Lambda}$ 
notation as long as same version is used
for both $\Phi$ and $\bx$.

````{prf:corollary}
:label: cor:ssm:matrix_vector_product_disjoint_set_seperation

Let $S$ and $T$ be two disjoint index sets such that
for some $\bx \in \CC^N$

$$
\bx = x_T + x_S
$$
using the mask version of $x_{\Lambda}$ notation.
Then the following holds

$$
\Phi \bx = \Phi_T \bx_T + \Phi_S \bx_S.
$$
````

````{prf:proof}
Straightforward application of 
 {prf:ref}`lem:ssm:restriction_simplification_sparse_vector`:

$$
\Phi \bx = \Phi \bx_T + \Phi \bx_S = \Phi_T \bx_T + \Phi_S \bx_S.
$$
````

````{prf:theorem}
:label: lem:ssm:restriction_on_matrix_vector_product

Let $T$ be any index set. Let $\Phi \in \CC^{M \times N}$
and $\by \in \CC^M$.
Then

$$
[\Phi^H \by]_T = \Phi_T^H \by.  
$$
````
````{prf:proof}
Note that

$$
\Phi^H \by = 
\begin{bmatrix}
\langle \phi_1 , \by \rangle\\
\vdots \\
\langle \phi_N , \by \rangle\\
\end{bmatrix}
$$
Now let 

$$
T = \{ t_1, \dots, t_K \}.
$$
Then

$$
[\Phi^H \by]_T = 
\begin{bmatrix}
\langle \phi_{t_1} , \by \rangle\\
\vdots \\
\langle \phi_{t_K} , \by \rangle\\
\end{bmatrix}
= \Phi_T^H \by.
$$
````
The result remains valid whether we use
the restriction or the mask version of $\Phi_T$ 
notation.


 
### Compressible Signals

We will now define the notion of a compressible signal in terms of the decay rate
of magnitude of its entries when sorted in descending order.

```{index} Signal; compressible
```
````{prf:definition} Compressible signal
:label: def:ssm:p_compressible_signal

Let $\bx \in \CC^N$ be an arbitrary signal.
Let $\lambda_1, \dots, \lambda_N$ be
indices of entries in $\bx$ such that

$$
| x_{\lambda_1} | \geq | x_{\lambda_2} | \geq \dots \geq | x_{\lambda_N} |.
$$
In case of ties, the order is resolved lexicographically, i.e. if $|x_i| = |x_j|$ 
and $i < j$ then $i$ will appear first in the sequence $\{ \lambda_k \}$.
Define

```{math}
:label: eq:x_sorted_in_magnitude_descending

\widehat{\bx} = (x_{\lambda_1}, x_{\lambda_2}, \dots, x_{\lambda_N}).
```

The signal $\bx$ is called *$p$-compressible* with magnitude $R$
if there exists $p \in (0, 1]$ such that

```{math}
:label: eq:p_compressible_signal_entry

| \widehat{x}_i |\leq R \cdot i^{-\frac{1}{p}} \quad \forall i=1, 2,\dots, N.
```
````

````{prf:theorem} $1$-compressible signals
:label: lem:ssm:compressible_p_1

Let $\bx$ be be $p$-compressible  with $p=1$. Then

$$
\| \bx \|_1 \leq R (1 + \ln (N)).
$$
````
````{prf:proof}
Recalling $\widehat{x}$ from
{eq}`eq:x_sorted_in_magnitude_descending`
it is straightforward to see that

$$
\|\bx\|_1 = \|\widehat{\bx}\|_1
$$
since the $\ell_1$ norm doesn't depend on the ordering of entries in $\bx$.

Now since $\bx$ is $1$-compressible,
hence from {eq}`eq:p_compressible_signal_entry` we have

$$
|\widehat{x}_i | \leq R \frac{1}{i}.
$$
This gives us

$$
\|\widehat{x}\|_1  \leq \sum_{i=1}^N R \frac{1}{i} = R \sum_{i=1}^N \frac{1}{i}.
$$
The sum on the R.H.S. is the $N$-th Harmonic number
(sum of reciprocals of first $N$ natural numbers).
A simple upper bound on Harmonic numbers is

$$
H_k \leq 1  + \ln(k).
$$
This completes the proof.
````
We now demonstrate how a compressible signal is well approximated by a sparse signal.

````{prf:theorem} Sparse approximation of compressible signals
:label: lem:ssm:compressible_p_sparse_approximation

Let $\bx$ be a $p$-compressible signal and let 
$\bx|_K$ be its best $K$-term approximation. 
Then the $\ell_1$ norm of approximation error satisfies 

```{math}
:label: eq:compressible_p_sparse_approximation_error_l1_norm
\| \bx - \bx|_K\|_1 \leq C_p \cdot R \cdot K^{1 - \frac{1}{p}}
```
with

$$
C_p = \left (\frac{1}{p} - 1 \right)^{-1}.
$$
Moreover the $\ell_2$ norm of approximation error satisfies

```{math}
:label: eq:compressible_p_sparse_approximation_error_l2_norm
\| \bx - \bx|_K\|_2 \leq D_p \cdot R \cdot K^{1 - \frac{1}{p}}
```
with 

$$
D_p = \left (\frac{2}{p} - 1 \right )^{-1/2}.
$$
````
````{prf:proof}
Expanding the $\ell_1$ approximation error

$$
\| \bx - \bx|_K\|_1 = \sum_{i=K+1}^N |x_{\lambda_i}| 
\leq R \sum_{i=K+1}^N i^{-\frac{1}{p}}.
$$
We now approximate the R.H.S. sum with an integral.

$$
 \sum_{i=K+1}^N i^{-\frac{1}{p}} 
 \leq \int_{x=K}^N x^{-\frac{1}{p}} d x
 \leq  \int_{x=K}^{\infty} x^{-\frac{1}{p}} d x.
$$
Now

$$
\int_{x=K}^{\infty} x^{-\frac{1}{p}} d x = 
\left [ \frac{x^{1-\frac{1}{p}}}{1-\frac{1}{p}} \right ]_{K}^{\infty}
= C_p K^{1 - \frac{1}{p}}.
$$
We can similarly show the result for $\ell_2$ norm.
````

```{prf:example} Sparse approximation for $\frac{1}{2}$-compressible signals
:label: ex-ssm-k-sparse-approx-half-compressible

Let $p = \frac{1}{2}$. Then

$$
C_p = \left (\frac{1}{p} - 1 \right)^{-1} = 1
\text{ and }
D_p = \left (\frac{2}{p} - 1 \right )^{-1/2} = \frac{1}{\sqrt{3}}.
$$

Hence

$$
\| \bx - \bx|_K\|_1 \leq \frac{R}{K}
$$
and

$$
\| \bx - \bx|_K\|_2 \leq  \frac{1}{\sqrt{3}} \frac{R}{K}.
$$
Both $\ell_1$ and $\ell_2$ approximation error bounds decrease
as $K$ increases at the same rate.
```
