(sec:ssm:dictionaries)=
# Dictionaries

In this section we review various properties associated with a dictionary $\bDDD$ which are
useful in understanding the behavior and capabilities of a dictionary.

```{div}
We recall that a dictionary $\bDDD$ consists of a finite number of unit norm vectors in $\CC^N$ called
atoms  which span the signal space $\CC^N$.
Atoms of the dictionary are indexed by an index set $\Omega$; i.e.,

$$
\bDDD = \{ \bd_{\omega} : \omega \in \Omega \}
$$
with $|\Omega| = D$ and $N \leq D$
with $\| d_{\omega} \|_2 = 1$ for every atom.

The vectors $\bx \in \CC^N$ can be represented by a synthesis matrix consisting of
the atoms of $\bDDD$ by a vector $\ba \in \CC^D$ as

$$
\bx = \bDDD \ba.
$$
Note that we are using the same symbol $\bDDD$ to represent the dictionary
as a set of atoms as well as the corresponding synthesis matrix.
We can write the matrix $\bDDD$ consisting of its columns as

$$
\bDDD = 
\begin{bmatrix}
\bd_1 & \dots & \bd_D
\end{bmatrix}
$$
This shouldn't be causing any confusion.
When we write the subscript as $\bd_{\omega}$
where $\omega \in \Omega$
we are referring to the atoms of the dictionary $\bDDD$
indexed by the set $\Omega$, while
when we write the subscript as $\bd_i$
we are referring to a column of corresponding synthesis matrix.
In this case, $\Omega$ will simply mean
the index set $\{ 1, \dots, D \}$.
Obviously $|\Omega| = D$ holds still. 

Often, we will be working with a subset of atoms in a dictionary.
Usually such a subset
of atoms will be indexed by an index set $\Lambda \subseteq \Omega$. $\Lambda$ will take the form of
$\Lambda \subseteq \{\omega_1, \dots, \omega_D\}$ or
$\Lambda \subseteq \{1, \dots, D\}$ depending upon
whether we are talking about
the subset of atoms in the dictionary
or a subset of columns from the corresponding
synthesis matrix.

Often we will need the notion of a subdictionary {cite}`tropp2006just` described below.
```

## Subdictionaries

```{index} Subdictionary
```
````{prf:definition} Subdictionary
:label: def:ssm:subdictionary

A subdictionary is a linearly independent collection of atoms. 
Let $\Lambda \subset \{\omega_1, \dots, \omega_D\}$
be the index set for the
atoms in the subdictionary.
We denote the subdictionary as $\bDDD_{\Lambda}$.
We also use $\bDDD_{\Lambda}$
to denote the corresponding matrix with
$\Lambda \subset \{1, \dots, D\}$.
````

````{prf:remark} Rank of subdictionary
:label: res-ssm-subdictionary-rank

A subdictionary is full rank.
````
This is obvious since it is a collection of linearly independent atoms.

For subdictionaries, often we will say
$K = | \Lambda |$ and 
$\bG = \bDDD_{\Lambda}^H \bDDD_{\Lambda}$ as its
Gram matrix.
Sometimes, we will also be considering $\bG^{-1}$.
$\bG^{-1}$ has a useful interpretation
in terms of the *dual vectors* for the atoms in
$\bDDD_{\Lambda}$ {cite}`tropp2004just`.

```{div}
Let $\{ \bd_{\lambda} \}_{\lambda \in \Lambda}$
denote the atoms in $\bDDD_{\Lambda}$. 
Let $\{ \bc_{\lambda} \}_{\lambda \in \Lambda}$
be chosen such that

$$
\langle \bd_{\lambda} , \bc_{\lambda} \rangle = 1
$$
and

$$
\langle \bd_{\lambda} , \bc_{\omega} \rangle = 0
\text { for } \lambda, \omega \in \Lambda, \lambda \neq \omega.
$$
Each dual vector $\bc_{\lambda}$ is orthogonal to atoms in the subdictionary at different indices
and is long enough so that
its inner product with $\bd_{\lambda}$ is one.
The dual system somehow
inverts the sub-dictionary.
In fact the dual vectors are nothing but the columns of the 
matrix $\bB = (\bDDD_{\Lambda}^{\dag})^H$.
Now, a simple calculation shows that:

$$
\bB^H \bB 
= (\bDDD_{\Lambda}^{\dag}) (\bDDD_{\Lambda}^{\dag})^H 
= (\bDDD_{\Lambda}^H \bDDD_{\Lambda})^{-1} \bDDD_{\Lambda}^H \bDDD_{\Lambda} (\bDDD_{\Lambda}^H \bDDD_{\Lambda})^{-1} 
= (\bDDD_{\Lambda}^H \bDDD_{\Lambda})^{-1} = \bG^{-1}.
$$
Therefore, the inverse Gram matrix lists the inner products
between the dual vectors. 

Sometimes we will be discussing tools
which apply for general matrices. We will use
the symbol $\Phi$ for representing general matrices.
Whenever the dictionary is 
an orthonormal basis, we will use the symbol $\Psi$.
```

(sec:ssm:spark)=
## Spark

```{index} Dictionary; spark, Matrix; spark
```
````{prf:definition} Spark
:label: def:spark

The *spark* of a given matrix $\Phi$ 
is the smallest number of columns of $\Phi$ that
are linearly dependent.
If all columns are linearly independent, then
the spark is defined to be number of columns plus one.
````
Note that the definition of spark applies to all matrices
(wide, tall or square). It is not
restricted to the synthesis matrices for a dictionary.

Correspondingly, the spark of a dictionary is defined as the minimum number of atoms
which are linearly dependent.

We recall that *rank* of a matrix is defined as the maximum number of columns which
are linearly independent.
Definition of spark bears remarkable resemblance yet its very hard 
to obtain as it requires a combinatorial search over all possible 
subsets of columns of $\Phi$.

````{prf:example} Spark
:label: ex-ssm-spark-1

1. Spark of the $3 \times 3$ identity matrix

   $$
    \begin{pmatrix}
        1 & 0 & 0\\
        0 & 1 & 0 \\
        0 & 0 & 1
    \end{pmatrix}
   $$
   is 4 since all columns are linearly independent.
1. Spark of the $2 \times 4$ matrix 
   
   $$
    \begin{pmatrix}
        1 & 0 & -1 & 0\\
        0 & 1 & 0 & -1
    \end{pmatrix}
   $$
   is 2 since column 1 and 3 are linearly dependent.
1. If a matrix has a column with all zero entries, 
   then the spark of such a matrix is 1.
   This is a trivial case
   and we will not consider such matrices in the sequel.
1. In general for an $N \times D$ synthesis matrix, 
   $\spark(\bDDD) \in [2, N+1]$.
````

A naive combinatorial algorithm to calculate the spark of a matrix is given below.

````{prf:algorithm} A naive algorithm for computing the spark of a matrix
:label: alg:ssm:spark_combinatorial_search

Inputs:
1. $\Phi$: a matrix

Outputs:
1. $s$: Spark of $\Phi$

Algorithm:

1. Let $R \leftarrow \rank (\Phi)$.
1. For every $j  \leftarrow 1,\dots, R$:
   1. Identify $\binom{D}{j}$ ways of choosing $j$ columns
      from $D$ columns of $\Phi$.
   1. For every choice of $j$ columns:
      1. If columns are linearly dependent:
         1. $s \leftarrow j$.
         1. Return.
1. All columns are linearly independent.
1. $s \leftarrow R  + 1$.
````
### Spark and Nullspace

````{prf:remark} Spark and sparsity of null space vectors
:label: res-ssm-spark-nullspace-vec-sparsity

The $\ell_0$-"norm" of vectors belonging to null space of a matrix
$\Phi$ is greater than or equal to $\spark(\Phi)$:

$$
\| \bx \|_0 \geq \spark(\Phi) \Forall \bx \in \NullSpace(\Phi).
$$
````
````{prf:proof}
We proceed as follows:

1. If $\bx \in \NullSpace(\Phi)$ then $\Phi \bx = \bzero$.
1. Thus non-zero entries in $\bx$ pick a set of columns in $\Phi$ 
   which are linearly dependent. 
1. Clearly $\| \bx \|_0$ indicates the number of columns in the set which are
   linearly dependent. 
1. By definition, spark of $\Phi$ indicates the minimum number of columns
   which are linearly dependent. 
1. Hence the result:

   $$
    \| \bx \|_0 \geq \spark(\Phi) \Forall \bx\in \NullSpace(\Phi).
   $$
````

### Uniqueness-Spark

Spark is useful in characterizing the uniqueness of the solution
of a $(\bDDD, K)$-EXACT-SPARSE problem (see {prf:ref}`def-ssm-d-k-exact-sparse-problem`).
We now present a criteria based on spark which characterizes
the uniqueness of a sparse solution to the problem $\by = \Phi \bx$.

````{prf:theorem} Uniqueness of a sparse solution for an underdetermined system via spark
:label: thm:ssm:uniqueness_spark

Consider a solution $\bx^*$ to the underdetermined system
$\by = \Phi \bx$.
If $\bx^*$ obeys

$$
\| \bx^* \|_0 < \frac{\spark(\Phi)}{2}
$$
then it is necessarily the sparsest solution.
````

````{prf:proof}
Let $\bx'$ be some other solution to the problem. Then 

$$
\Phi \bx' = \Phi \bx^* 
\implies \Phi (\bx' - \bx^*)  = \bzero 
\implies (\bx' - \bx^*) \in \NullSpace(\Phi).
$$
Due to {prf:ref}`res-ssm-spark-nullspace-vec-sparsity` we have

$$
\| \bx' - \bx^* \|_0 \geq \spark(\Phi).
$$
Now 

$$
\| \bx' \|_0 + \| \bx^* \|_0 \geq \| \bx' - \bx^* \|_0 \geq \spark(\Phi).
$$
Hence, if $\| \bx^* \|_0 < \frac{\spark(\Phi)}{2}$, then we have

$$
\| \bx' \|_0  > \frac{\spark(\Phi)}{2}
$$
for any other solution $\bx'$ to the equation $\by = \Phi \bx$. 
Thus $\bx^*$ is necessarily the sparsest possible solution.
````

This result is quite useful as it establishes a global optimality criterion for the
$(\bDDD, K)$-EXACT-SPARSE problem.

As long as $K < \frac{1}{2}\spark(\Phi)$ this theorem guarantees that
the solution to  $(\bDDD, K)$-EXACT-SPARSE problem
is unique.
This is quite surprising result for a non-convex combinatorial optimization
problem.
We are able to guarantee a global uniqueness for the solution based
on a simple check on the sparsity of the solution.

Note that we are only saying that if a sufficiently sparse solution is found
then it is unique.
We are not claiming that it is possible to find such a solution.

Obviously, the larger the spark, we can guarantee uniqueness for signals
with higher sparsity levels.
So a natural question is: 
*How large can spark of a dictionary be*?
We consider few examples.

````{prf:example} Spark of Gaussian dictionaries
:label: ex-ssm-spark-gaussian

Consider a dictionary $\bDDD$ whose atoms $\bd_{i}$ are random vectors 
independently drawn from normal distribution.

1. Since a dictionary requires all its atoms to be unit-norms,
   hence we divide the each of the random vectors with their norms.
1. We know that with probability $1$ any set of $N$ independent Gaussian random vectors
   is linearly independent. 
1. Also, since $\bd_i \in \RR^N$ hence a set of $N+1$ atoms is always linearly dependent. 
1. Thus $\spark(\bDDD) = N +1$.

Thus, if a solution to EXACT-SPARSE problem contains $\frac{N}{2}$ or fewer non-zero
entries then it is necessarily unique with probability 1. 
````

````{prf:example} Spark of Dirac Fourier basis
:label: ex-ssm-spark-dirac-fourier

For 

$$
\bDDD = \begin{bmatrix} \bI  & \bF \end{bmatrix} \in \CC^{N \times 2N} 
$$ 
it can be shown that

$$
\spark(\bDDD) = 2 \sqrt{N}.
$$
In this case, the sparsity level of a unique solution must be less than $\sqrt{N}$.
````



## Coherence
Finding out the spark of a dictionary $\bDDD$ is NP-hard since it involves considering combinatorially 
large number of selections of columns from $\bDDD$.
In this section we consider
the *coherence* of a dictionary which is computationally tractable and quite useful 
in characterizing the solutions of sparse approximation problems.

```{index} Coherence
```
````{prf:definition} Coherence of a dictionary
:label: def:ssm:coherence
The *coherence* of a dictionary $\bDDD$ is defined as
the maximum absolute inner product between two distinct atoms in the dictionary:

$$
\mu = \underset{j \neq k}{\max} | \langle \bd_{\omega_j}, \bd_{\omega_k} \rangle |
= \underset{j \neq k}{\max} | (\bDDD^H \bDDD)_{j k} |.
$$
````
If the dictionary consists of two orthonormal bases,
then coherence is also known as *mutual coherence*
or *proximity*; see {prf:ref}`def-ssm-mutual-coherence-two-ortho-bases`.

We note that $d_{\omega_i}$ is the $i$-th column of synthesis matrix $\bDDD$. 
Also $\bDDD^H \bDDD$ is the *Gram matrix* for $\bDDD$ whose elements are nothing
but the inner-products of columns of $\bDDD$.

```{div}
We note that by definition $\| d_{\omega} \|_2 = 1$ hence 
$\mu \leq 1$ and since absolute values are considered hence $\mu \geq 0$.
Thus, $0 \leq \mu \leq 1$. 

For an orthonormal basis $\Psi$ all atoms are orthogonal to each other, hence

$$
| \langle \psi_{\omega_j}, \psi_{\omega_k} \rangle |= 0 \text{ whenever } j \neq k.
$$
Thus $\mu = 0$ for an orthonormal basis.

In the following, we will use the notation $|\bA|$ to denote a matrix consisting
of absolute values of entries in a matrix $\bA$; i.e.,

$$
|  \bA |_{i j}  = |  \bA _{i j} |.
$$
The off-diagonal entries of the Gram matrix are captured by the 
matrix $\bDDD^H \bDDD - I$.
Note that all diagonal entries in $\bDDD^H \bDDD - I$
are zero since atoms of $\bDDD$ are unit norm.
Moreover, each of the entries in $ | \bDDD^H \bDDD - I |$
is dominated by $\mu(\bDDD)$.

The inner product between any two atoms 
$| \langle \bd_{\omega_j}, \bd_{\omega_k} \rangle |$
is a measure of how much they look alike or how much they are correlated. 
Coherence just picks up the two vectors
which are most alike and returns their correlation.
In a way $\mu$ is quite a blunt measure of the quality of a dictionary,
yet it is quite useful.

If a dictionary is uniform in the sense that there is not much variation in 
$| \langle \bd_{\omega_j}, \bd_{\omega_k} \rangle |$, then $\mu$ captures
the behavior of the dictionary quite well.
```

```{index} Incoherent dictionary, Dictionary; incoherent
```
````{prf:definition} Incoherent dictionary
:label: def:ssm:incoherent_dictionary

We say that a dictionary is *incoherent* if the coherence of the dictionary is small.
````
We are looking for dictionaries which are incoherent. In the sequel we will see how
incoherence plays a role in sparse approximation.

````{prf:example} Coherence of two ortho bases
:label: ex-ssm-coherence-2-onb-2

We established in {prf:ref}`res-ssm-2-onb-coherence-bounds` that
coherence of two ortho-bases is bounded by

$$
\frac{1}{\sqrt{N}} \leq \mu \leq 1.
$$
In particular we showed in {prf:ref}`res-ssm-coherence-dirac-fourier` that
coherence of Dirac Fourier basis is $\frac{1}{\sqrt{N}}$.
````

````{prf:example} Coherence: Multi-ONB dictionary
:label: ex-ssm-coherence-multi-onb

A dictionary of concatenated orthonormal bases is called a multi-ONB.
For some $N$, it is
possible to build a multi-ONB which contains $N$ or even $N+1$ bases yet retains 
the minimal coherence $\mu = \frac{1}{\sqrt{N}}$ possible.
````

````{prf:theorem} Coherence lower bound
:label: res-ssm-coherence-lb

A lower bound on the coherence of a general dictionary is given by

$$
\mu \geq \sqrt{\frac{D-N}{N(D-1)}}.
$$
````

```{index} Grassmannian frame
```
````{prf:definition} Grassmannian frame
:label: def:ssm:grassmannian_frame

If each atomic inner product meets this bound,
the dictionary is  called an *optimal Grassmannian frame*.
````

The definition of coherence can be extended to arbitrary matrices
$\Phi \in \CC^{N \times D}$.

```{index} Coherence; arbitrary matrices
```
````{prf:definition} Coherence for arbitrary matrices
:label: def:ssm:coherence_matrix

The *coherence* of a matrix $\Phi \in \CC^{N \times D}$ is defined as
the maximum absolute *normalized* inner product between
two distinct columns in the matrix.
Let 

$$
\Phi = \begin{bmatrix} \phi_1 & \phi_2 & \dots & \phi_D \end{bmatrix}.
$$
Then coherence of $\Phi$ is given by

```{math}
:label: eq:ssm:dict:coherence:arbitrary_matrix

\mu(\Phi) = \underset{j \neq k}{\text{max}} \frac{ | \langle \phi_j, \phi_k \rangle |} {\| \phi_j \|_2  \| \phi_k \|_2}
```
It is assumed that none of the columns in $\Phi$ is a zero vector. 
````

### Lower Bounds for Spark
Coherence of a matrix is easy to compute.
More interestingly it also provides a lower bound on the
spark of a matrix.

````{prf:theorem} Lower bound on spark in terms of coherence
:label: lem:ssm:spark_lower_bound_coherence

For any matrix $\Phi \in \CC^{N \times D}$ (with non-zero columns)
the following relationship holds

$$
\spark(\Phi) \geq 1 + \frac{1}{\mu(\Phi)}.
$$
````
````{prf:proof}
We note that scaling of a column of $\Phi$ doesn't change either the spark
or coherence of $\Phi$.
Therefore, we assume that the columns of $\Phi$ are normalized.

1. We now construct the Gram matrix of $\Phi$ given by $\bG = \Phi^H \Phi$. 
1. We note that
   
   $$
   \bG_{k k} = 1 \quad  \Forall 1 \leq k \leq D
   $$
   since each column of $\Phi$ is unit norm.
1. Also
   
   $$
   |G_{k j}| \leq \mu(\Phi)  \quad \Forall 1 \leq k, j \leq D , k \neq j.
   $$
1. Consider any $p$ columns from $\Phi$ and construct its Gram matrix. 
1. This is nothing but a leading minor of size $p \times p$ from the matrix $\bG$.
1. From the Gershgorin disk theorem, if this minor is diagonally dominant, i.e. if
   
   $$
    \sum_{j \neq i} |G_{i j}| < | G_{i i}| \Forall i
   $$
   then this sub-matrix of $\bG$ is positive definite and
   so corresponding $p$ columns from $\Phi$ are linearly independent. 
1. But
   
   $$
   |G_{i i}| = 1
   $$
   and

   $$
    \sum_{j \neq i} |G_{i j}| \leq (p-1) \mu(\Phi) 
   $$
   for the minor under consideration.
1. Hence for $p$ columns to be linearly independent
   the following condition is sufficient

   $$
    (p-1) \mu (\Phi) < 1.
   $$
1. Thus if
   
   $$
    p < 1 + \frac{1}{\mu(\Phi)},
   $$
   then every set of $p$ columns from $\Phi$ is linearly independent.
1. Hence, the smallest possible set of linearly dependent columns must satisfy
   
   $$
   p \geq 1 + \frac{1}{\mu(\Phi)}.
   $$
1. This establishes the lower bound that
   
   $$
    \spark(\Phi) \geq 1 + \frac{1}{\mu(\Phi)}.
   $$
````
This bound on spark doesn't make any assumptions on the structure of the dictionary.
In fact, imposing additional structure on the dictionary can give better bounds.
Let us look at an example for a two ortho-basis  {cite}`donoho2003optimally`.

````{prf:theorem} Lower bound on spark for two ortho bases
:label: res:ssm:spark_lower_bound_two_ortho_basis

Let $\bDDD$ be a two ortho-basis. Then

$$
\spark (\bDDD) \geq \frac{2}{\mu(\bDDD)}.
$$
````
````{prf:proof}
From {prf:ref}`res-ssm-2onb-nullspace-vec-sparsity` we know that for any
vector $\bv \in \NullSpace(\bDDD)$

$$
\| \bv \|_0 \geq \frac{2}{\mu(\bDDD)}.
$$
But

$$
\spark(\bDDD) = \underset{\bv \in \NullSpace(\bDDD)} {\min}( \| \bv \|_0).
$$
Thus

$$
\spark(\bDDD) \geq \frac{2}{\mu(\bDDD)}.
$$
````
For maximally incoherent two orthonormal bases, we know that $\mu = \frac{1}{\sqrt{N}}$.
A perfect example is the pair of Dirac and Fourier bases. In this case
$\spark(\bDDD) \geq 2 \sqrt{N}$.
 
### Uniqueness-Coherence
We can now establish a uniqueness condition for sparse solution of $\by = \Phi \bx$. 

````{prf:theorem} Uniqueness of a sparse solution of an underdetermined system via coherence
:label: thm:ssm:uniqueness_coherence

Consider a solution $\bx^*$ to the under-determined system $\by = \Phi \bx$.
If $\bx^*$ obeys

$$
\| \bx^* \|_0 < \frac{1}{2} \left (1 + \frac{1}{\mu(\Phi)} \right )
$$
then it is necessarily the sparsest solution.
````

````{prf:proof}
This is a straightforward application of {prf:ref}`thm:ssm:uniqueness_spark` 
and {prf:ref}`lem:ssm:spark_lower_bound_coherence`.
````

It is interesting to compare the two uniqueness theorems:
{prf:ref}`thm:ssm:uniqueness_spark` 
and {prf:ref}`thm:ssm:uniqueness_coherence`.

{prf:ref}`thm:ssm:uniqueness_spark` uses spark, is sharp and is far more powerful
than {prf:ref}`thm:ssm:uniqueness_coherence`. 

```{div}
Coherence can never be smaller than $\frac{1}{\sqrt{N}}$, therefore the bound on
$\| \bx^* \|_0$ in  {prf:ref}`thm:ssm:uniqueness_coherence` can never be larger than
$\frac{\sqrt{N} + 1}{2}$.

However, spark can be easily as large as $N$ and then bound on $\| \bx^* \|_0$ can
be as large as $\frac{N}{2}$.

We recall from {prf:ref}`res-ssm-sparse-unique-2onb` that the bound for
sparsity level of sparest solution in two-ortho basis 
$\Eta = \begin{bmatrix}\Psi & \Chi \end{bmatrix}$  is given by 

$$
\| \bx^* \|_0 < \frac{1}{\mu(\Eta)}
$$
which is a larger bound than {prf:ref}`thm:ssm:uniqueness_coherence`
for general dictionaries by a factor of 2.

Thus, we note that coherence gives a weaker bound than spark for
supportable sparsity levels
of unique solutions.
The advantage that coherence has is that it is easily computable and
doesn't require any special structure on the dictionary (two ortho basis has a special structure).
```
 
### Singular Values of Subdictionaries

````{prf:theorem} Singular values of subdictionaries and coherence
:label: res:ssm:subdictionary_eigenvalue_coherence

Let $\bDDD$ be a dictionary and $\bDDD_{\Lambda}$ be a subdictionary. 
Let $\mu$ be the coherence of $\bDDD$. Let $K = | \Lambda |$.
Then
the eigen values of $\bG = \bDDD_{\Lambda}^H \bDDD_{\Lambda}$ satisfy:

$$
1 - (K - 1)   \mu  \leq \lambda \leq 1 + (K - 1)   \mu.
$$
Moreover, the singular values of the sub-dictionary $\bDDD_{\Lambda}$ satisfy

$$
\sqrt{1 - (K - 1)   \mu}  \leq \sigma (\bDDD_{\Lambda}) \leq \sqrt{1 + (K - 1)   \mu}.
$$
````
````{prf:proof}
We recall from Gershgorin's circle theorem that for
any square matrix $\bA \in \CC^{K \times K}$, 
every eigen value $\lambda$ of $\bA$ satisfies 

$$
| \lambda  - a_{ii} | 
\leq \sum_{j \neq i} |a_{i j}| \text{ for some } i \in \{ 1, \dots, K\}.
$$
1. Now consider the matrix $\bG =  \bDDD_{\Lambda}^H \bDDD_{\Lambda}$ 
   with diagonal elements equal to 1
   and off diagonal elements bounded by the coherence $\mu$.
1. Then
   
   $$
    | \lambda  - 1 | \leq \sum_{j \neq i} |G_{i j}|  \leq \sum_{j \neq i} \mu = (K - 1) \mu.
   $$
1. Thus,
   
   $$
    - (K - 1) \mu  
    \leq \lambda  - 1 \leq (K - 1) \mu \iff  1 - (K - 1)   \mu  
    \leq \lambda \leq 1 + (K - 1)   \mu.
   $$
1. This gives us a lower bound on the smallest eigen value.
   
   $$
    \lambda_{\min} (\bG) \geq 1 - (K - 1) \mu.
   $$
1. Since $\bG$ is positive definite ($\bDDD_{\Lambda}$ is full-rank),
   hence its eigen values
   are positive. Thus, the above lower bound is useful only if
   
   $$
   1 - (K - 1) \mu > 0 \iff 1 >  (K - 1) \mu \iff \mu < \frac{1}{K - 1}.
   $$
1. We also get an upper bound on the eigen values of $\bG$ given by
   
   $$
    \lambda_{\max} (G) \leq 1 + (K - 1) \mu.
   $$
1. The bounds on singular values of $\bDDD_{\Lambda}$ are obtained as a 
   straight-forward extension by taking square roots on the expressions.
```` 
### Embeddings using Subdictionaries

````{prf:theorem} Norm bounds for embeddings with real dictionaries
:label: res:ssm:real_dict_norm_bound_coherence

Let $\bDDD$ be a real dictionary and $\bDDD_{\Lambda}$ be a subdictionary
with $K = |\Lambda|$.
Let $\mu$ be the coherence of $\bDDD$.
Let $\bv \in \RR^K$ be an
arbitrary vector.
Then

$$
| \bv |^T [I - \mu (\OneMat - I)] | \bv | 
\leq \| \bDDD_{\Lambda} \bv \|_2^2 
\leq | \bv |^T [I + \mu (\OneMat - I)] | \bv |
$$
where $\OneMat$ is a $K\times K$ matrix of all ones.
Moreover

$$
(1 - (K - 1)   \mu) \| \bv \|_2^2 
\leq \| \bDDD_{\Lambda} \bv \|_2^2 
\leq (1 + (K - 1)   \mu)\| \bv \|_2^2. 
$$
````
````{prf:proof}
We can see that

$$
\| \bDDD_{\Lambda} \bv \|_2^2 =  \bv^T \bDDD_{\Lambda}^T \bDDD_{\Lambda} \bv.
$$
1. Expanding we have
   
   $$
    \bv^T \bDDD_{\Lambda}^T \bDDD_{\Lambda} \bv 
    = \sum_{i=1}^K \sum_{j=1}^K v_i  \bd_{\lambda_i}^T \bd_{\lambda_j} v_j.
   $$
1. The terms in the R.H.S. for $i = j$ are given by
   
   $$
    v_i  \bd_{\lambda_i}^T \bd_{\lambda_i} v_i  = | v_i |^2. 
   $$
1. Summing over $i = 1, \dots, K$, we get 
   
   $$
    \sum_{i=1}^K | v_i |^2 = \| \bv \|_2^2 = \bv^T \bv 
    = | \bv |^T | \bv | = | \bv |^T \bI | \bv |.
   $$
1. We are now left with $K^2 - K$ off diagonal terms.
1. Each of these terms is bounded by
   
   $$
    - \mu |v_i| |v_j | 
    \leq v_i \bd_{\lambda_i}^T \bd_{\lambda_j} v_j \leq \mu |v_i| |v_j |.
   $$
1. Summing over the $K^2 - K$ off-diagonal terms we get:
   
   $$
   \sum_{i \neq j}  |v_i| |v_j | 
   = \sum_{i, j}  |v_i| |v_j | - \sum_{i = j}  |v_i| |v_j | 
   =  | \bv |^T(\OneMat - \bI ) | \bv |. 
   $$
1. Thus,
   
   $$
     - \mu | \bv |^T (\OneMat - \bI ) | \bv | \leq 
     \sum_{i \neq j} v_i  \bd_{\lambda_i}^T \bd_{\lambda_j} v_j 
     \leq  \mu | \bv |^T (\OneMat - \bI ) | \bv |.
   $$
1. Thus,
   
   $$
    | \bv |^T \bI | \bv |- \mu | \bv |^T (\OneMat - \bI ) | \bv | 
    \leq \bv^T \bDDD_{\Lambda}^T \bDDD_{\Lambda} \bv
    \leq | \bv |^T \bI | \bv |+ \mu | \bv |^T (\OneMat - \bI )| \bv |.
   $$
1. We get the result by slight reordering of terms:
   
   $$
    | \bv |^T [\bI - \mu (\OneMat - \bI)] | \bv | 
    \leq \| \bDDD_{\Lambda} \bv \|_2^2 
    \leq | \bv |^T [\bI + \mu (\OneMat - \bI)] | \bv |.
   $$
1. We note that due to {prf:ref}`res:ssm:ones_matrix_l1_norm`
   
   $$
    | \bv |^T \OneMat | \bv | =  \| \bv \|_1^2.
   $$
1. Thus, the inequalities can be written as
   
   $$
    (1 + \mu) \|\bv \|_2^2 - \mu \| \bv \|_1^2 
    \leq \| \bDDD_{\Lambda} \bv \|_2^2 
    \leq (1 - \mu) \| \bv \|_2^2 + \mu \| \bv \|_1^2.
   $$
1. Alternatively,
   
   $$
    \| \bv \|_2^2  - \mu \left (\| \bv \|_1^2 - \| \bv \|_2^2 \right ) 
    \leq \| \bDDD_{\Lambda} \bv \|_2^2 
    \leq 
    \| \bv \|_2^2  + \mu \left (\| \bv \|_1^2 - \| \bv \|_2^2\right ) .
   $$
1. Finally, due to {prf:ref}`lem:ssm:l1_norm_l2_bounds` 
   
   $$
    \| \bv \|_1^2 \leq K \| \bv \|_2^2 
    \implies \| \bv \|_1^2 - \| \bv \|_2^2 \leq (K - 1) \| \bv \|_2^2.
   $$
1. This gives  us
   
   $$
    ( 1- (K - 1) \mu ) \| \bv \|_2^2 
    \leq \| \bDDD_{\Lambda} \bv \|_2^2 
    \leq ( 1 + (K - 1) \mu ) \| \bv \|_2^2 .
   $$
````

We now present the above theorem for the complex case. The proof is
based on singular values. This proof is simpler and more general 
than the one presented above. 

````{prf:theorem} Norm bounds for embeddings with complex dictionaries
:label: res:ssm:subdict_norm_bound_coherence

Let $\bDDD$ be a dictionary and $\bDDD_{\Lambda}$ be a sub-dictionary
with $K = |\Lambda|$.
Let $\mu$ be the coherence of $\bDDD$.
Let $\bv \in \CC^K$ be an
arbitrary vector.
Then

$$
(1 - (K - 1)   \mu) \| \bv \|_2^2 
\leq \| \bDDD_{\Lambda} \bv \|_2^2 
\leq (1 + (K - 1)   \mu)\| \bv \|_2^2. 
$$
````
````{prf:proof}
Recall that 

$$
\sigma_{\min}^2(\bDDD_{\Lambda}) \| \bv \|_2^2  
\leq \| \bDDD_{\Lambda} \bv \|_2^2 \leq 
\sigma_{\max}^2(\bDDD_{\Lambda}) \| \bv \|_2^2.
$$
The {prf:ref}`res:ssm:subdictionary_eigenvalue_coherence` tells us:

$$
1 - (K - 1)   \mu  \leq \sigma^2 (\bDDD_{\Lambda}) \leq 1 + (K - 1)   \mu.
$$
Thus,

$$
\sigma_{\min}^2(\bDDD_{\Lambda}) \| \bv \|_2^2  
\geq (1 - (K - 1)   \mu) \| \bv \|_2^2
$$
and

$$
\sigma_{\max}^2(\bDDD_{\Lambda}) \| \bv \|_2^2 \leq (1 + (K - 1)   \mu)\| \bv \|_2^2.
$$
This gives us the result

$$
(1 - (K - 1)   \mu) \| \bv \|_2^2 
\leq \| \bDDD_{\Lambda} \bv \|_2^2 
\leq (1 + (K - 1)   \mu)\| \bv \|_2^2. 
$$
````