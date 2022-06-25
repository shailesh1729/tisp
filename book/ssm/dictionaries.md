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

Often we will need the notion of a sub-dictionary {cite}`tropp2006just` described below.
```

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

Spark is useful in characterizing the uniqueness of the solution
of a $(\bDDD, K)$-EXACT-SPARSE problem (see {prf:ref}`def-ssm-d-k-exact-sparse-problem`).

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