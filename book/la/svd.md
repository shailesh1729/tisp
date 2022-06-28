(sec:la:svd)=
# Singular Values

In previous section we saw diagonalization of square matrices
which resulted in an eigen value
decomposition of the matrix.
This matrix factorization is very useful yet it is not applicable
in all situations.
In particular, the eigen value decomposition is useless if the square matrix
is not diagonalizable or if the matrix is not square at all.
Moreover, the decomposition
is particularly useful only for real symmetric or Hermitian matrices
where the diagonalizing
matrix is an $\FF$-unitary matrix
(see {prf:ref}`def:mat:f_unitary_matrix`).
Otherwise, one has to consider the inverse of the diagonalizing matrix also.

Fortunately there happens to be another decomposition which applies to all matrices and
it involves just $\FF$-unitary matrices.

## Singular value

````{prf:definition} Singular value
:label: def:mat:singular_value

A non-negative real number $\sigma$ is a *singular value*
for a matrix $\bA \in \FF^{m \times n}$ if and only if
there exist unit-length vectors $\bu \in \FF^m$ and $\bv \in \FF^n$
such that

$$
\bA \bv = \sigma \bu 
$$
and

$$
\bA^H \bu = \sigma \bv
$$
hold.
The vectors $\bu$ and $\bv$ are called *left-singular*
and *right-singular* vectors for $\sigma$ respectively.
````
We first present the basic result of singular value decomposition.
We will not prove this
result completely although we will present proofs of some aspects.

````{prf:theorem} Existence of singular values
:label: thm:mat:singular_value_decomposition

For every $\bA \in \FF^{m \times n}$ with $k = \min(m , n)$, 
there exist two $\FF$-unitary matrices $\bU \in \FF^{m \times m}$  
and $\bV \in \FF^{n \times n}$ and a sequence of real numbers 

$$
\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_k \geq 0
$$
such that

```{math}
:label: eq:mat:svd:equation_form_1
\bU^H \bA \bV = \Sigma 
```
where

$$
\Sigma = \Diag(\sigma_1, \sigma_2, \dots, \sigma_k) \in \FF^{ m \times n}.
$$
The non-negative real numbers $\sigma_i$ are the *singular values* of $\bA$
as per {prf:ref}`def:mat:singular_value`.

The sequence of real numbers $\sigma_i$ doesn't depend on the
particular choice of $\bU$ and $\bV$.
````
$\Sigma$ is rectangular with the same size as $\bA$.
The singular values of $\bA$ lie
on the principle diagonal of $\Sigma$.
All other entries in $\Sigma$ are zero.

It is certainly possible that some of the singular values are 0 themselves.

````{prf:remark}
:label: rem-mat-svd-form-2

Since $\bU^H \bA \bV = \Sigma $ hence

```{math}
:label: eq:mat:svd:equation_form_2
\bA = \bU \Sigma \bV^H.
```
````

````{prf:definition} Singular value decomposition
:label: def:mat:singular_value_decomposition

The decomposition of a matrix $\bA \in \FF^{m \times n}$ given by

```{math}
:label: eq:mat:singular_value_decomposition

\bA = \bU \Sigma \bV^H
```
is known as its *singular value decomposition*.
````
````{prf:remark}
:label: rem-mat-svd-form-real

When $\FF$ is $\RR$ then the decomposition simplifies to

```{math}
:label: eq:mat:svd:equation_form_3

\bU^T \bA \bV = \Sigma 
```
and

$$
\bA = \bU \Sigma \bV^T.
$$
````

````{prf:remark}
:label: rem-mat-svd-max-singular-values

There can be at most $k= \min(m , n)$ distinct singular values of $\bA$.
````

````{prf:remark}
:label: rem-mat-svd-form-4

We can also write
```{math}
:label: eq:mat:svd:equation_form_4

\bA \bV = \bU \Sigma.
```
````

````{prf:remark} SVD as a sum of rank 1 matrices
:label: rem-mat-svd-rank-1-sum

Let us expand 

$$
\bA = \bU \Sigma \bV^H
= 
\begin{bmatrix}
\bu_1 & \bu_2 & \dots & \bu_m
\end{bmatrix}
 \begin{bmatrix}
 \sigma_{ij}
\end{bmatrix}
\begin{bmatrix}
\bv_1^H \\ \bv_2^H \\ \vdots \\ \bv_n^H
\end{bmatrix}
=  
\sum_{i=1}^m \sum_{j=1}^n \sigma_{i j} \bu_i  \bv_j^H.
$$
````

````{prf:remark}
:label: rem-mat-svd-expand-2

Alternatively, let us expand 

$$
\Sigma = \bU^H \bA \bV  
= 
 \begin{bmatrix}
\bu_1^H \\ \bu_2^H \\ \vdots \\ \bu_m^H
\end{bmatrix}
\bA
\begin{bmatrix}
\bv_1 & \bv_2 & \dots & \bv_m
\end{bmatrix}
=  \begin{bmatrix} \bu_i^H \bA \bv_j \end{bmatrix}
$$
This gives us

$$
\sigma_{i j} = \bu_i^H \bA \bv_j.
$$
````

Following lemma verifies that $\Sigma$ indeed consists of singular values of $\bA$ 
as per {prf:ref}`def:mat:singular_value`.

````{prf:lemma}
:label: res-mat-svd-just-singular-vals

Let $\bA = \bU \Sigma \bV^H$ be a singular value decomposition of $\bA$.
Then the main diagonal entries of $\Sigma$ are singular values.
The first $k = \min(m, n)$ column vectors in
$\bU$ and $\bV$ are left and right singular vectors of $\bA$.
````
````{prf:proof}
We have

$$
\bA \bV = \bU \Sigma.
$$
1. Let us expand R.H.S.

    $$
        \bU \Sigma = 
        \begin{bmatrix}\sum_{j=1}^m \bu_{i j} \sigma_{j k} \end{bmatrix}
        = [u_{i k} \sigma_k]
        = \begin{bmatrix}
        \sigma_1 \bu_1 & \sigma_2 \bu_2 & \dots & \sigma_k \bu_k & \bzero & \dots & \bzero
        \end{bmatrix}
    $$
    where $\bzero$ columns in the end appear $n - k$ times.
1. Expanding the L.H.S. we get

    $$
        \bA \bV  = \begin{bmatrix}
        \bA \bv_1 & \bA \bv_2 & \dots & \bA \bv_n
        \end{bmatrix}.
    $$
1. Thus by comparing both sides we get

    $$
        \bA \bv_i = \sigma_i \bu_i \; \text{ for } \; 1 \leq i \leq k
    $$
    and

    $$
        \bA \bv_i = \bzero \text{ for } k < i \leq n.
    $$
1. Now let us start with
   
   $$
    \bA = \bU \Sigma \bV^H 
    \implies  \bA^H = \bV \Sigma^H \bU^H 
    \implies  \bA^H \bU  = \bV \Sigma^H.
   $$
1. Let us expand R.H.S.
   
    $$
    \bV \Sigma^H = 
    \begin{bmatrix}\sum_{j=1}^n v_{i j} \sigma_{j k} \end{bmatrix}
    = [v_{i k} \sigma_k]
    = \begin{bmatrix}
    \sigma_1 \bv_1 & \sigma_2 \bv_2 & \dots & \sigma_k \bv_k & \bzero & \dots & \bzero
    \end{bmatrix}
    $$
    where $\bzero$ columns appear $m - k$ times.
1. Expanding the L.H.S. we get
    
    $$
    \bA^H \bU   = \begin{bmatrix}
    \bA^H \bu_1 & \bA^H \bu_2 & \dots & \bA^H \bu_m
    \end{bmatrix}.
    $$
1. Thus by comparing both sides we get
   
   $$
    \bA^H \bu_i = \sigma_i \bv_i \; \text{ for } \; 1 \leq i \leq k
   $$
   
   and

   $$
    \bA^H \bu_i = \bzero \text{ for } k < i \leq m.
   $$

We now consider the three cases.

1. For $m = n$, we have $k = m =n$.  And we get
   
   $$
    \bA \bv_i = \sigma_i \bu_i,  
    \bA^H \bu_i = \sigma_i \bv_i \; \text{ for } \; 1 \leq i \leq m.
   $$
   Thus $\sigma_i$ is a singular value of $\bA$ and
   $\bu_i$ is a left singular vector while
   $\bv_i$ is a right singular vector.
1. For $m < n$, we have $k = m$. We get for first $m$ vectors in $\bV$
   
   $$
   \bA \bv_i = \sigma_i \bu_i,  
   \bA^H \bu_i = \sigma_i \bv_i \; \text{ for } \; 1 \leq i \leq m.
   $$
   Finally for remaining $n-m$ vectors in $\bV$, we can write
   
   $$
    \bA \bv_i = \bzero.
   $$
   They belong to the null space of $\bA$.
1. For $m > n$, we have $k = n$. We get for first $n$ vectors in $\bU$
   
   $$
   \bA \bv_i = \sigma_i \bu_i,  
   \bA^H \bu_i = \sigma_i \bv_i \; \text{ for } \; 1 \leq i \leq n.
   $$
   Finally for remaining $m - n$ vectors in $\bU$, we can write
   
   $$
    \bA^H \bu_i = \bzero.
   $$
````

````{prf:lemma}
:label: res-mat-svd-sig-sqr-1

$\Sigma \Sigma^H$ is an $m \times m$ matrix given by

$$
\Sigma \Sigma^H =  \Diag(\sigma_1^2, \sigma_2^2, \dots, \sigma_k^{2}, 0, 0,\dots, 0)
$$
where the number of $0$'s following $\sigma_k^{2}$ is $m  - k$.
````

````{prf:lemma}
:label: res-mat-svd-sig-sqr-2

$\Sigma^H \Sigma$ is an $n \times n$ matrix given by

$$
\Sigma^H \Sigma =  \Diag(\sigma_1^2, \sigma_2^2, \dots, \sigma_k^{2}, 0, 0,\dots, 0)
$$
where the number of $0$'s following $\sigma_k^{2}$ is $n  - k$.
````
````{prf:lemma} Rank from singular value decomposition
:label: lem:mat:singular:rank_svd

Let $\bA \in \FF^{m \times n}$ have a singular value decomposition given by

$$
\bA = \bU \Sigma \bV^H.
$$
Then

$$
r = \Rank(A) = \Rank(\Sigma).
$$
In other words, the rank of $\bA$ is number of nonzero singular values of $\bA$.
Since the singular values are ordered in descending order in $\bA$ hence, 
the first $r$ singular values $\sigma_1, \dots, \sigma_r$ are nonzero.
````
````{prf:proof}
This is a straight forward application of
{prf:ref}`lem:mat:rank:full_rank_post_multiplier`
and {prf:ref}`lem:mat:rank:full_rank_pre_multiplier`.
Further since only nonzero values in $\Sigma$ appear
on its main diagonal hence its rank 
is number of nonzero singular values $\sigma_i$.
````
````{prf:corollary}
:label: cor:mat:singular:svd_block_matrix

Let $r = \Rank(\bA)$. Then $\Sigma$ can be split as a block matrix

$$
\Sigma = 
\left [
\begin{array}{c | c}
\Sigma_r & \ZERO\\
\hline
\ZERO & \ZERO
\end{array}
\right ]
$$
where $\Sigma_r$ is an $r \times r$ diagonal matrix of the nonzero singular values
$\Diag(\sigma_1, \sigma_2, \dots, \sigma_r)$.
All other sub-matrices in $\Sigma$ are $\ZERO$.
````


````{prf:lemma} Eigen values of the Gram matrix
:label: lem:mat:singular:aH_a_eigen_values

The eigen values of Hermitian matrix $\bA^H \bA \in \FF^{n \times n}$ are
$\sigma_1^2, \sigma_2^2, \dots, \sigma_k^{2}, 0, 0,\dots, 0$ with $n - k$ $0$'s after $\sigma_k^{2}$.
Moreover the eigen vectors are the columns of $\bV$.
````
````{prf:proof}
Expanding the Gram matrix:

$$
\bA^H \bA 
= \left ( \bU \Sigma \bV^H \right)^H \bU \Sigma \bV^H  
= \bV \Sigma^H \bU^H \bU \Sigma \bV^H = \bV \Sigma^H \Sigma \bV^H.
$$
1. We note that $\bA^H \bA$ is Hermitian.
1. Hence $A^HA$ is diagonalized by $\bV$.
1. The diagonalization of $\bA^H \bA$
   is $\Sigma^H \Sigma$.
1. Thus the eigen values of $\bA^H \bA$  are 
   $\sigma_1^2, \sigma_2^2, \dots, \sigma_k^{2}, 0, 0,\dots, 0$
   with $n - k$ $0$'s after $\sigma_k^{2}$.
1. Clearly
   
   $$
    (\bA^H \bA) \bV = \bV (\Sigma^H \Sigma).
   $$
1. Thus columns of $\bV$ are the eigen vectors of $\bA^H \bA$.
````


````{prf:lemma} Eigen values of the frame operator
:label: lem:mat:singular:a_aH_eigen_values

The eigen values of Hermitian matrix $\bA \bA^H \in \FF^{m \times m}$
are $\sigma_1^2, \sigma_2^2, \dots, \sigma_k^{2}, 0, 0,\dots, 0$
with $m - k$ $0$'s after $\sigma_k^{2}$.
Moreover the eigen vectors are the columns of $\bV$.
````
````{prf:proof}
Expanding the frame operator:

$$
\bA \bA^H 
= \bU \Sigma \bV^H \left ( \bU \Sigma \bV^H \right)^H 
= \bU \Sigma \bV^H \bV \Sigma^H \bU^H 
= \bU \Sigma \Sigma^H \bU^H.
$$
1. We note that $\bA^H \bA$ is Hermitian.
1. Hence $\bA^H \bA$ is diagonalized by $\bV$.
1. The diagonalization of $\bA^H \bA$ is $\Sigma^H \Sigma$.
1. Thus the eigen values of $\bA^H \bA$  are
   $\sigma_1^2, \sigma_2^2, \dots, \sigma_k^{2}, 0, 0,\dots, 0$
   with $m - k$ $0$'s after $\sigma_k^{2}$.
1. Clearly
   
   $$
    (\bA \bA^H) \bU = \bU (\Sigma \Sigma^H).
   $$
1. Thus columns of $\bU$ are the eigen vectors of $\bA \bA^H$.
````

````{prf:observation}
:label: rem-mat-svd-gram-frame-evals

The Gram matrices $\bA \bA^H$ and $\bA^H \bA$
share the same eigen values except for some extra $0$s.
Their eigen values are the squares of singular values of $\bA$ and some extra $0$s.
In other words singular values of $\bA$ are the square roots of nonzero
eigen values of the Gram matrices
$\bA \bA^H$ or $\bA^H \bA$.
````

## The Largest Singular Value

````{prf:lemma}
:label: lem:mat:singular:largest_singular_value_norm_bound_sigma

For every $\bu \in \FF^n$ the following holds

$$
\| \Sigma \bu \|_2 \leq  \sigma_1 \| \bu \|_2.
$$
Also for every $\bu \in \FF^m$ the following holds

$$
\| \Sigma^H \bu \|_2 \leq  \sigma_1 \| \bu \|_2.
$$
````

````{prf:proof}
Let us expand the term $\Sigma \bu$.

$$
\begin{bmatrix}
\sigma_1 & 0 & \dots & \dots & 0 \\
0 & \sigma_2 & \dots & \dots & 0 \\
\vdots & \vdots & \ddots & \dots & 0\\
0 & \vdots & \sigma_k & \dots & 0 \\
0 & 0 & \vdots & \dots & 0
\end{bmatrix}
\begin{bmatrix}
u_1 \\
u_2 \\
\vdots \\
u_k \\
\vdots \\
u_n
\end{bmatrix}
= \begin{bmatrix}
\sigma_1 u_1 \\
\sigma_2 u_2 \\
\vdots \\
\sigma_k u_k \\
0 \\
\vdots \\
0
\end{bmatrix}
$$

Now since $\sigma_1$ is the largest singular value, hence

$$
|\sigma_i u_i| \leq |\sigma_1 u_i| \Forall 1 \leq i \leq k.
$$
Thus

$$
\sum_{i=1}^n |\sigma_1 u_i|^2  \geq \sum_{i=1}^n |\sigma_i u_i|^2
$$
or

$$
\sigma_1^2 \| \bu \|_2^2 \geq \| \Sigma \bu \|_2^2.
$$
The result follows. 

A simpler representation of $\Sigma \bu$ can be given using
the block representation of $\Sigma$ in
{prf:ref}`cor:mat:singular:svd_block_matrix`.

Let $r = \Rank(\bA)$.  Then

$$
\Sigma = 
\left [
\begin{array}{c | c}
\Sigma_r & \ZERO\\
\hline
\ZERO & \ZERO
\end{array}
\right ].
$$
We split entries in $\bu$ as

$$
\bu = [(u_1, \dots, u_r )( u_{r + 1} \dots u_n)]^T.
$$
Then 

$$
\Sigma \bu = 
\left [
\begin{array}{c}
\Sigma_r 
\begin{bmatrix}
u_1 &
\dots&
u_r
\end{bmatrix}^T\\
\ZERO \begin{bmatrix}
u_{r + 1} &
\dots&
u_n
\end{bmatrix}^T
\end{array}
\right ]
= 
\begin{bmatrix}
\sigma_1 u_1 & \sigma_2 u_2 & \dots & \sigma_r u_r & 0 & \dots & 0 
\end{bmatrix}^T
$$ 
Thus 

$$
\| \Sigma \bu \|_2^2
= \sum_{i=1}^r |\sigma_i u_i |^2 
\leq \sigma_1 \sum_{i=1}^r |u_i |^2 
\leq \sigma_1 \|\bu\|_2^2.
$$
2nd result can also be proven similarly.
````

````{prf:lemma} Upper bounds on norms of matrix vector product
:label: lem:mat:singular:largest_singular_value_l2_norm_bound_A_A^H

Let $\sigma_1$ be the largest singular value of an $m \times n$ matrix $\bA$.
Then

$$
\| \bA \bx \|_2 \leq \sigma_1 \| \bx \|_2 \Forall \bx \in \FF^n.
$$
Moreover

$$
\| \bA^H \bx \|_2 \leq \sigma_1 \| \bx \|_2 \Forall \bx \in \FF^m.
$$
````

````{prf:proof}
We have

$$
\| \bA \bx \|_2 = \|  \bU \Sigma \bV^H \bx \|_2  = \| \Sigma \bV^H \bx \|_2
$$
since $\bU$ is unitary.
Now from previous result we have 

$$
\| \Sigma \bV^H \bx \|_2 
\leq  \sigma_1 \| \bV^H \bx \|_2 =  \sigma_1 \| \bx \|_2
$$
since $\bV^H$ also unitary.
Thus we get the result

$$
\| \bA \bx \|_2  \leq \sigma_1 \| \bx \|_2 \Forall \bx \in \FF^n.
$$
Similarly

$$
\| \bA^H \bx \|_2 = \|  \bV \Sigma^H \bU^H  \bx \|_2  
= \| \Sigma^H \bU^H \bx \|_2
$$
since $\bV$ is unitary.
Now from previous result we have 

$$
\|  \Sigma^H \bU^H \bx \|_2 \leq  
\sigma_1 \| \bU^H \bx \|_2 =  \sigma_1 \| \bx \|_2
$$
since $\bU^H$ also unitary. Thus we get the result

$$
\| \bA^H \bx \|_2  \leq \sigma_1 \| \bx \|_2 \Forall \bx \in \FF^m.
$$
````

There is a direct connection between the largest singular value and $2$-norm
of a matrix (see {prf:ref}`sec:mat:p_norm`).
````{prf:corollary}
:label: res-mat-svd-2-norm-1st-sv

The largest singular value of $\bA$ is nothing but its $2$-norm; i.e.,

$$
\sigma_1 = \underset{\| \bu \|_2 = 1}{\max} \| \bA \bu \|_2.
$$
````



## SVD and Pseudo Inverse
````{prf:lemma}
:label: lem:mat:singular:sigma_pseudo_inverse

Let $\bA = \bU \Sigma \bV^H$ and let 
$r  = \Rank (\bA)$.
Let $\sigma_1, \dots, \sigma_r$ be
the $r$ nonzero singular values of $\bA$.
Then the Moore-Penrose pseudo-inverse of
$\Sigma$ is an $n \times m$ matrix $\Sigma^{\dag}$
given by

$$
\Sigma^{\dag} = 
\left [
\begin{array}{c | c}
\Sigma_r^{-1} & \ZERO\\
\hline
\ZERO & \ZERO
\end{array}
\right ]
$$
where $\Sigma_r = \Diag(\sigma_1, \dots, \sigma_r)$.

$\Sigma^{\dag}$ is obtained by transposing $\Sigma$ and inverting
all its nonzero (positive real) values.
````
````{prf:proof}
Straight forward application of 
{prf:ref}`lem:mat:moore_penrose_rectangular_diagonal_pseudo_inverse`.
````

````{prf:corollary}
:label: cor:mat:sigma_pseudo_inverse_rank

The rank of $\Sigma$ and its pseudoinverse $\Sigma^{\dag}$ are same; i.e.,

$$
\Rank (\Sigma) = \Rank(\Sigma^{\dag}).
$$
````
````{prf:proof}
The number of nonzero diagonal entries in $\Sigma$ and $\Sigma^{\dag}$ are same.
````

````{prf:lemma}
:label: lem:mat:singular:matrix_pseudo_inverse

Let $\bA$ be an $m \times n$ matrix and let $\bA = \bU \Sigma \bV^H$ be its
singular value decomposition.
Let $\Sigma^{\dag}$ be the pseudoinverse
of $\Sigma$ as per {prf:ref}`lem:mat:singular:sigma_pseudo_inverse`.
Then the Moore-Penrose pseudo-inverse of $\bA$ is given by

$$
\bA^{\dag} = \bV \Sigma^{\dag} \bU^H.
$$
````
````{prf:proof}
As usual we verify the requirements for a Moore-Penrose pseudo-inverse
as per {prf:ref}`def:mat:moore_penrose_pseudo_inverse`. We note that
since $\Sigma^{\dag}$ is the pseudo-inverse of $\Sigma$ it already 
satisfies necessary criteria.

First requirement:

$$
\bA \bA^{\dag} \bA = \bU \Sigma \bV^H  \bV \Sigma^{\dag} \bU^H \bU \Sigma \bV^H
= \bU \Sigma \Sigma^{\dag} \Sigma \bV^H = \bU \Sigma \bV^H = \bA.
$$
Second requirement:

$$
\bA^{\dag} \bA \bA^{\dag}
= \bV \Sigma^{\dag} \bU^H  \bU \Sigma \bV^H  \bV \Sigma^{\dag} \bU^H
= \bV  \Sigma^{\dag} \Sigma \Sigma^{\dag} \bU^H 
= \bV \Sigma^{\dag} \bU^H = \bA^{\dag}.
$$
We now consider

$$
\bA \bA^{\dag} = \bU \Sigma \bV^H  \bV \Sigma^{\dag} \bU^H 
= \bU \Sigma \Sigma^{\dag} \bU^H.
$$
Thus

$$
\left ( \bA \bA^{\dag} \right )^H 
= \left ( \bU \Sigma \Sigma^{\dag} \bU^H \right )^H
= \bU \left ( \Sigma \Sigma^{\dag} \right )^H \bU^H 
= \bU \Sigma \Sigma^{\dag} \bU^H = \bA \bA^{\dag}
$$
since $\Sigma \Sigma^{\dag}$ is Hermitian.
Finally we consider

$$
\bA^{\dag} \bA = \bV \Sigma^{\dag} \bU^H \bU \Sigma \bV^H  
= \bV \Sigma^{\dag}  \Sigma \bV^H.
$$ 
Thus

$$
\left ( \bA^{\dag} \bA  \right )^H 
= \left ( \bV \Sigma^{\dag}  \Sigma \bV^H\right )^H 
= \bV \left ( \Sigma^{\dag}  \Sigma \right )^H \bV^H 
= \bV \Sigma^{\dag}  \Sigma \bV^H = \bA^{\dag} \bA
$$
since $\Sigma^{\dag}  \Sigma$ is also Hermitian.
This completes the proof.
````

Finally we can connect the singular values of $A$ with the
singular values of its pseudo-inverse. 

````{prf:corollary} Rank of pseudoinverse
:label: cor:mat:singular_matrix_pseudo_inverse_rank

The rank of any $m \times n$ matrix $\bA$ and its
pseudoinverse $\bA^{\dag}$ are same. i.e.

$$
\Rank (\bA) = \Rank(\bA^{\dag}).
$$
````
````{prf:proof}
We have $\Rank(A) = \Rank(\Sigma)$. 
Also its easy to verify that $\Rank(\bA^{\dag}) = \Rank(\Sigma^{\dag})$.
So using {prf:ref}`cor:mat:sigma_pseudo_inverse_rank` completes the proof.
````

````{prf:lemma} Singular values of the pseudoinverse
:label: lem:mat:singular_pseudo_inverse_singular_values

Let $\bA$ be an $m \times n$ matrix and let $\bA^{\dag}$  be its $n \times m$ 
pseudoinverse as per {prf:ref}`lem:mat:singular:matrix_pseudo_inverse`. 
Let $r = \Rank(\bA)$.
Let $k = \min(m, n)$ denote the number of singular values
while $r$ denote the number of nonzero singular values of $\bA$.
Let $\sigma_1, \dots, \sigma_r$ be the nonzero singular values of $\bA$.
Then the number of singular values of $\bA^{\dag}$ is same as that
of $\bA$ and the nonzero singular values of $\bA^{\dag}$ are 

$$
\frac{1}{\sigma_1} , \dots, \frac{1}{\sigma_r}
$$
while all other $k - r$ singular values of $\bA^{\dag}$ are zero.
````
````{prf:proof}
$k= \min(m, n)$ denotes the number of singular values for both
$\bA$ and  $\bA^{\dag}$.

1. Since rank of $\bA$ and  $\bA^{\dag}$  are same, hence the number of 
   nonzero singular values is same.
1. Now look at 
   
   $$
   \bA^{\dag}  = \bV \Sigma^{\dag} \bU^H
   $$
   where
   
   $$
   \Sigma^{\dag} = 
    \left [
    \begin{array}{c | c}
    \Sigma_r^{-1} & \ZERO\\
    \hline
    \ZERO & \ZERO
    \end{array}
    \right ].
    $$
1. Clearly $\Sigma_r^{-1} = \Diag(\frac{1}{\sigma_1} , \dots, \frac{1}{\sigma_r})$.
1. Thus expanding the R.H.S. we can get
   
   $$
   \bA^{\dag} = \sum_{i=1}^r \frac{1}{\sigma_{i}} \bv_i  \bu_i^H
   $$
   where $\bv_i$ and $\bu_i$ are first $r$ columns of $\bV$ and $\bU$ respectively.
1. If we reverse the order of first $r$ columns of $\bU$ and $\bV$ and reverse
   the first $r$ diagonal entries of $\Sigma^{\dag}$
   , the R.H.S. remains the same while we are able to express $\bA^{\dag}$ in 
   the standard singular value decomposition form.
1. Thus $\frac{1}{\sigma_1} , \dots, \frac{1}{\sigma_r}$ are indeed
   the nonzero singular values of $\bA^{\dag}$.
````


(sec:mat:sngular:full_column_rank_matrices)=
## Full Column Rank Matrices
In this subsection we consider some specific results related to
the singular value decomposition of a full column rank matrix. 

1. We will consider $\bA$ to be an $m \times n$ matrix in $\FF^{m \times n}$
   with $m \geq n$ and $\Rank(\bA) = n$. 
1. Let $\bA = \bU \Sigma \bV^H$ be its singular value decomposition. 
1. From {prf:ref}`lem:mat:singular:rank_svd` we observe that
   there are $n$ nonzero singular values of $\bA$.
1. We will call these singular values as $\sigma_1, \sigma_2, \dots, \sigma_n$. 
1. We will define 
   
   $$
   \Sigma_n = \Diag(\sigma_1, \sigma_2, \dots, \sigma_n).
   $$
1. Clearly $\Sigma$ is an $2\times 1$ block matrix given by
   
   $$
    \Sigma = 
    \left [
    \begin{array}{c}
    \Sigma_n\\
    \hline
    \ZERO
    \end{array}
    \right ]
    $$
    where the lower $\ZERO$ is an $(m - n) \times n$ zero matrix.
1. From here we obtain that $\Sigma^H \Sigma$ is an $n \times n$ matrix given by
   
   $$
    \Sigma^H \Sigma = \Sigma_n^2
   $$
   where
   
   $$
    \Sigma_n^2 = \Diag(\sigma_1^2, \sigma_2^2, \dots, \sigma_n^2).
   $$

````{prf:lemma}
:label: lem:mat:singular:full_column_rank_sigma_h_sigma_invertible

Let $\bA$ be a full column rank matrix with singular value decomposition
$\bA = \bU \Sigma \bV^H$.
Then $\Sigma^H \Sigma = \Sigma_n^2 = \Diag(\sigma_1^2, \sigma_2^2, \dots, \sigma_n^2)$
and $\Sigma^H \Sigma$ is invertible.
````
````{prf:proof}
Since all singular values are nonzero hence $\Sigma_n^2$ is invertible. Thus

$$
\left (\Sigma^H \Sigma \right )^{-1} 
= \left ( \Sigma_n^2  \right )^{-1}
=  \Diag\left(\frac{1}{\sigma_1^2}, \frac{1}{\sigma_2^2}, 
    \dots, \frac{1}{\sigma_n^2} \right).
$$
````

````{prf:lemma}
:label: res-mat-svd-fcr-sigma-norm-proj-bounds

Let $\bA$ be a full column rank matrix with singular value decomposition
$\bA = \bU \Sigma \bV^H$. 
Let $\sigma_1$ be its largest singular value and
$\sigma_n$ be its smallest singular value.
Then

$$
\sigma_n^2 \| \bx \|_2 \leq 
\| \Sigma^H \Sigma \bx \|_2 \leq \sigma_1^2 \| \bx \|_2  \Forall \bx \in \FF^n.
$$
````
````{prf:proof}
Let $\bx \in \FF^n$.

1. We have
   
   $$
     \| \Sigma^H \Sigma \bx \|_2^2 
     = \| \Sigma_n^2 \bx \|_2^2 = \sum_{i=1}^n |\sigma_i^2 x_i|^2.
   $$
1. Now since 
   
   $$
    \sigma_n \leq \sigma_i \leq \sigma_1;
   $$
1. hence
   
   $$
    \sigma_n^4  \sum_{i=1}^n |x_i|^2 
    \leq \sum_{i=1}^n |\sigma_i^2 x_i|^2 
    \leq \sigma_1^4 \sum_{i=1}^n |x_i|^2.
   $$
1. Thus
   
   $$
    \sigma_n^4 \| \bx \|_2^2 
    \leq  \| \Sigma^H \Sigma \bx \|_2^2 
    \leq \sigma_1^4 \| \bx \|_2^2.
   $$
1. Applying square roots, we get
   
   $$
    \sigma_n^2 \| \bx \|_2 
    \leq  \| \Sigma^H \Sigma \bx \|_2 
    \leq \sigma_1^2 \| \bx \|_2  
    \Forall \bx \in \FF^n.
   $$
````
We recall from {prf:ref}`cor:mat:gram_full_column_rank_invertible`
that the Gram matrix of its column vectors $\bG = \bA^H \bA$ is
full rank and invertible.

````{prf:lemma} Norm bounds for Gram matrix vector product
:label: lem:mat:singular:full_column_rank_gram_embedding_l2_norm_bound

Let $\bA$ be a full column rank matrix with
singular value decomposition $\bA = \bU \Sigma \bV^H$. 
Let $\sigma_1$ be its largest singular value and
$\sigma_n$ be its smallest singular value.
Then

$$
\sigma_n^2 \| \bx \|_2 
\leq \| \bA^H \bA \bx \|_2 
\leq \sigma_1^2 \| \bx \|_2  \Forall \bx \in \FF^n.
$$
````
````{prf:proof}
Expanding the Gram matrix

$$
\bA^H \bA = (\bU \Sigma \bV^H)^H (\bU \Sigma \bV^H) = \bV \Sigma^H \Sigma \bV^H. 
$$
Let $\bx \in \FF^n$. Let

$$
\bu = \bV^H \bx  \implies \| \bu \|_2 = \| \bx \|_2.
$$
Let 

$$
\bw = \Sigma^H \Sigma \bu.
$$
Then from previous lemma we have

$$
\sigma_n^2 \| \bu \|_2 
\leq  \| \Sigma^H \Sigma \bu \|_2 = \|\bw \|_2 \leq \sigma_1^2 \| \bu \|_2 .
$$
Finally

$$
\bA^ H \bA \bx = \bV \Sigma^H \Sigma \bV^H \bx = \bV \bw.
$$
Thus

$$
\| \bA^H \bA \bx \|_2  = \| \bw \|_2.
$$
Substituting we get

$$
\sigma_n^2 \|\bx \|_2 
\leq \| \bA^H \bA \bx \|_2 
\leq \sigma_1^2 \| \bx \|_2  \Forall \bx \in \FF^n.
$$
````

There are bounds for the inverse of Gram matrix also.
First let us establish the inverse of Gram matrix.
````{prf:lemma} SVD of inverse Gram matrix
:label: lem:mat:singular:full_column_rank_inverse_gram_matrix

Let $\bA$ be a full column rank matrix with singular value decomposition
$\bA = \bU \Sigma \bV^H$. 
Let the singular values of $\bA$ be $\sigma_1, \dots, \sigma_n$.
Let the Gram matrix of columns of $\bA$ be $\bG = \bA^H \bA$. Then 

$$
\bG^{-1} = \bV \Psi \bV^H
$$
where

$$
\Psi = \Diag \left(\frac{1}{\sigma_1^2}, \frac{1}{\sigma_2^2}, 
    \dots, \frac{1}{\sigma_n^2} \right).
$$
````
````{prf:proof}
We have 

$$
\bG = \bV \Sigma^H \Sigma \bV^H.
$$
Thus

$$
\bG^{-1} 
= \left (\bV \Sigma^H \Sigma \bV^H \right )^{-1} 
= \left ( \bV^H \right )^{-1} \left ( \Sigma^H \Sigma \right )^{-1} \bV^{-1} 
= \bV  \left ( \Sigma^H \Sigma \right )^{-1}  \bV^H.
$$
From {prf:ref}`lem:mat:singular:full_column_rank_sigma_h_sigma_invertible` we have

$$
\Psi = \left ( \Sigma^H \Sigma \right )^{-1} 
= \Diag \left (\frac{1}{\sigma_1^2}, \frac{1}{\sigma_2^2}, 
    \dots, \frac{1}{\sigma_n^2} \right).
$$
This completes the proof.
````

We can now state the bounds:

````{prf:lemma} Norm bounds for inverse Gram matrix vector product
:label: lem:mat:singular:full_column_rank_inverse_gram_embedding_l2_norm_bound

Let $\bA$ be a full column rank matrix with singular value decomposition
$\bA = \bU \Sigma \bV^H$. 
Let $\sigma_1$ be its largest singular value and
$\sigma_n$ be its smallest singular value.
Then

$$
\frac{1}{\sigma_1^2} \| \bx \|_2 \leq \| \left(\bA^H \bA \right)^{-1} \bx \|_2
\leq \frac{1}{\sigma_n^2} \| \bx \|_2  \Forall \bx \in \FF^n.
$$
````
````{prf:proof}
From {prf:ref}`lem:mat:singular:full_column_rank_inverse_gram_matrix` we have

$$
\bG^{-1} = \left ( \bA^H \bA \right)^{-1} = \bV \Psi \bV^H
$$
where

$$
\Psi = \Diag \left(\frac{1}{\sigma_1^2}, \frac{1}{\sigma_2^2}, 
    \dots, \frac{1}{\sigma_n^2} \right).
$$
Let $\bx \in \FF^n$. Let

$$
\bu = \bV^H \bx  \implies \| \bu \|_2 = \| \bx \|_2.
$$
Let

$$
\bw = \Psi \bu.
$$
Then 

$$
\| \bw \|_2^2 = \sum_{i=1}^n \left | \frac{1}{\sigma_i^2} u_i \right |^2.
$$
Thus

$$
\frac{1}{\sigma_1^2} \| \bu \|_2 
\leq  \| \Psi \bu \|_2 
= \|\bw \|_2 
\leq \frac{1}{\sigma_n^2} \| \bu \|_2 .
$$
Finally

$$
\left (\bA^ H \bA \right)^{-1} \bx = \bV \Psi \bV^H \bx = \bV \bw.
$$
Thus

$$
\| \left (\bA^ H \bA \right)^{-1} \bx \|_2  = \|\bw \|_2.
$$
Substituting we get the result.
````


(sec:mat:low_rank_approximation)=
## Low Rank Approximation of a Matrix

````{prf:definition} Low rank matrix
:label: def:mat:low_rank_matrix

An $m \times n$ matrix $\bA$ is called *low rank* if 

$$
\Rank(\bA) \ll \min (m, n).
$$
````
A matrix is low rank if the number of nonzero singular values
for the matrix is much smaller than its dimensions.

Following is a simple procedure for making a low rank approximation
of a given matrix $\bA$.

*  Perform the singular value decomposition of $\bA$ given by
   $\bA = \bU \Sigma \bV^H$.
*  Identify the singular values of $\bA$ in $\Sigma$.
*  Keep the first $r$ singular values (where $r \ll \min(m, n)$
   is the rank of the approximation).
*  Set all other singular values to 0 to obtain $\widehat{\Sigma}$.
*  Compute $\widehat{A} = U \widehat{\Sigma} V^H$.
