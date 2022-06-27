(sec:la:matrices:2)=
# Matrices II

This section deals with the concepts of vector spaces
associated with matrices, span, rank, invertible matrices,
similar matrices, gram matrices and pseudo inverses.

## Spaces Associated with a Matrix

````{prf:definition} Column space
:label: def:mat:column_space

The *column space* of a matrix is defined as the vector space spanned by columns of the matrix.
Let $\bA$ be an $m \times n$ matrix with

$$
\bA  = \begin{bmatrix}
\ba_1 & \ba_2 & \dots & \ba_n
\end{bmatrix}
$$

Then the column space is given by

$$
\ColSpace(\bA) = 
\{\bx \in \FF^m \ST \bx  = \sum_{i=1}^n \alpha_i \ba_i \; \text{for some }  \alpha_i \in \FF \}.
$$
````


````{prf:definition} Row space
:label: def:mat:row_space

The *row space* of a matrix is defined as the vector space spanned by rows of the matrix.

Let $\bA$ be an $m \times n$ matrix with

$$
\bA  = \begin{bmatrix}
\ba_1^T  \\ \ba_2^T \\ \vdots \\ \ba_m^T
\end{bmatrix}
$$
Then the row space is given by

$$
\RowSpace(\bA) 
= \{\bx \in \FF^n \ST \bx  = \sum_{i=1}^m \alpha_i \ba_i \; \text{for some }  \alpha_i \in \FF \}.
$$
````


## Rank
````{prf:definition} Column rank
:label: def:mat:column_rank

The *column rank* of a matrix is defined as the maximum number of columns which are linearly
independent.
In other words column rank is the dimension of the column space of a matrix.
````

````{prf:definition} Row rank
:label: def:mat:row_rank

The *row rank* of a matrix is defined as the maximum number of rows which are linearly
independent. In other words row rank is the dimension of the row space of a matrix.
````

````{prf:theorem} Equality of row and column rank
:label: thm:mat:row_column_rank

The *column rank* and *row rank* of a matrix are equal.
````

````{prf:definition} Rank
:label: def:mat:rank

The *rank* of a matrix is defined to be equal to its column rank which is equal to its row rank.
````

````{prf:lemma} Rank bounds
For an $m \times n$ matrix $\bA$

$$
 0 \leq \Rank(A) \leq \min(m, n).
$$
````

````{prf:lemma} Zero rank matrix
:label: res-mat-zero-rank

The rank of a matrix is 0 if and only if it is a zero matrix.
````

````{prf:definition} Full rank matrix
:label: def:mat:full_rank_matrix

An $m \times n$ matrix $\bA$ is called *full rank* if

$$
\Rank (\bA) = \min(m, n).
$$
In other words it is either a full column rank matrix or a full row rank matrix or both.
````
````{prf:lemma} Rank of product of two matrices
:label: lem:mat:rank:product

Let $\bA$ be an $m \times n$ matrix and $\bB$ be an $n \times p$ matrix then

$$
\Rank(\bA \bB) \leq \min (\Rank(\bA), \Rank(\bB)).
$$
````

````{prf:lemma} Full rank post multiplication
:label: lem:mat:rank:full_rank_post_multiplier

Let $\bA$ be an $m \times n$ matrix and $\bB$ be an $n \times p$ matrix.
If $\bB$ is of rank $n$ then

$$
\Rank(\bA \bB) = \Rank(\bA).
$$
````

````{prf:lemma} Full rank pre multiplication
:label: lem:mat:rank:full_rank_pre_multiplier

Let $\bA$ be an $m \times n$ matrix and $\bB$ be an $n \times p$ matrix.
If $\bA$ is of rank $n$ then

$$
\Rank(\bA \bB) = \Rank(\bB).
$$
````
````{prf:lemma} Rank of a diagonal matrix
:label: lem:mat:rank_diagonal_matrix

The rank of a diagonal matrix is equal to the number of nonzero elements on its main diagonal.
````
````{prf:proof}
The columns which correspond to diagonal entries which are zero are zero columns.
Other columns are linearly independent.
The number of linearly independent rows is also the same.
Hence their count gives us the rank of the matrix. 
````

## Invertible Matrices

We say that an $m \times n$ matrix $\bA$ is *left-invertible* if there exists 
an $n \times m$ matrix $\bB$ such that
$\bB \bA = \bI$. 
We say that an $m \times n$ matrix $\bA$ is *right-invertible* if there exists 
an $n \times m$ matrix $\bB$ such that $\bA \bB= \bI$. 

We say that a square matrix $\bA$ is *invertible* when there exists another square matrix
$\bB$ of same size such that $\bA \bB = \bB \bA = \bI$. 
A square matrix is invertible iff it is both left and right invertible.
Inverse of a square invertible matrix is denoted by $\bA^{-1}$.

A special left or right inverse is the pseudo inverse, which is denoted by $\bA^{\dag}$.

Column space of a matrix is denoted by $\ColSpace(\bA)$, the null space by $\NullSpace(\bA)$,
and the row space by $\RowSpace(\bA)$.

We say that a matrix is *symmetric* when $\bA = \bA^T$,
*conjugate symmetric* or  *Hermitian* when $\bA^H =\bA$.

When a square matrix is not invertible, we say that it is *singular*.
A  *non-singular* matrix is invertible.



````{prf:definition} Invertible matrix
:label: def:mat:invertible

A square matrix $\bA$ is called *invertible*
if there exists another square matrix $\bB$ of same size such that

$$
\bA \bB = \bB \bA = \bI.
$$
The matrix $\bB$ is called the *inverse* of $\bA$ and is denoted as $\bA^{-1}$.
````

````{prf:lemma} Invertibility of the inverse
:label: lem:mat:inverse_of_invertible_matrix

If $\bA$ is invertible then its inverse $\bA^{-1}$ is also invertible
and  the inverse of $\bA^{-1}$ is nothing but $\bA$.
````

````{prf:lemma} Invertibility of identity matrix
:label: lem:mat:invertible_identity

Identity matrix $\bI$ is invertible.
````
````{prf:proof}
We can see that

$$
\bI \bI = \bI \implies \bI^{-1} = \bI.
$$
````

````{prf:lemma} Linear independence of columns of invertible matrices
:label: lem:mat:invertible_linear_independence

If $\bA$ is invertible then columns of $\bA$ are linearly independent.
````
````{prf:proof}
Assume $\bA$ is invertible, then there exists a matrix $\bB$ such that

$$
\bA \bB = \bB \bA = \bI.
$$
Assume that columns of $\bA$ are linearly dependent.
Then there exists $\bu \neq \bzero$ such that

$$
\bA \bu = \bzero \implies \bB \bA \bu = \bzero 
\implies  \bI \bu = \bzero 
\implies \bu = \bzero
$$
a contradiction. Hence columns of $\bA$ are linearly independent.
````

````{prf:lemma} Span of columns of invertible matrix
:label: lem:invertible_spanning

If an $n\times n$ matrix  $\bA$ is invertible then columns of $\bA$ span $\FF^n$.
````
````{prf:proof}
Assume $\bA$ is invertible,
then there exists a matrix $\bB$ such that

$$
\bA \bB = \bB \bA = \bI.
$$

1. Now let $\bx \in \FF^n$ be any arbitrary vector.
1. We need to show that there exists $\ba \in \FF^n$ such that
   
   $$
  \bx = \bA \ba.
   $$

1. But
   
   $$
   \bx = \bI \bx = \bA \bB \bx = \bA ( \bB \bx).
   $$
1. Thus if we choose $\ba = \bB \bx$, then
   
   $$
   \bx = \bA \ba.
   $$
1. Thus columns of $\bA$ span $\FF^n$.
````

````{prf:lemma} Columns of invertible matrix as basis
:label: lem:mat:invertible_basis

If $\bA$ is invertible, then columns of $\bA$ form a basis for $\FF^n$.
````
````{prf:proof}
In $\FF^n$ a basis is a set of vectors which is linearly independent and spans $\FF^n$. 
By {prf:ref}`lem:mat:invertible_linear_independence` and
{prf:ref}`lem:invertible_spanning`,
columns of an invertible matrix $\bA$ satisfy both conditions.
Hence they form a basis.
````

````{prf:lemma} Invertibility of transpose
:label: lem:mat:invertible_transpose

If $\bA$ is invertible than $\bA^T$ is invertible.
````
````{prf:proof}
Assume $\bA$ is invertible, then there exists a matrix $\bB$ such that

$$
\bA \bB = \bB \bA = \bI.
$$
Applying transpose on both sides we get

$$
\bB^T \bA^T = \bA^T \bB^T = \bI.
$$
Thus $\bB^T$ is inverse of $\bA^T$ and $\bA^T$ is invertible.
````

````{prf:lemma} Invertibility of Hermitian transpose
:label: lem:mat:invertible_conjugate_transpose

If $A$ is invertible than $A^H$ is invertible.
````
````{prf:proof}
Assume $\bA$ is invertible, then there exists a matrix $\bB$ such that

$$
\bA \bB = \bB \bA = \bI.
$$
Applying conjugate transpose on both sides we get

$$
\bB^H \bA^H = \bA^H \bB^H = \bI.
$$
Thus $\bB^H$ is inverse of $\bA^H$ and $\bA^H$ is invertible.
````


````{prf:lemma} Invertibility of matrix product
:label: lem:mat:invertible_product

If $\bA$ and $\bB$ are invertible then $\bA \bB$ is invertible.
````
````{prf:proof}
We note that 

$$
( \bA \bB) (\bB^{-1}\bA^{-1}) =  \bA ( \bB \bB^{-1}) \bA^{-1} = \bA \bI \bA^{-1} = \bI.
$$
Similarly

$$
(\bB^{-1}\bA^{-1}) (\bA\bB)  = \bB^{-1} (\bA^{-1} \bA ) \bB = \bB^{-1} \bI \bB = \bI.
$$
Thus $\bB^{-1}\bA^{-1}$ is the inverse of $\bA \bB$.
````

````{prf:lemma} Group of invertible matrices
:label: lem:mat:invertible_group

The set of $n \times n$ invertible matrices under the matrix multiplication
operation form a group.
````
````{prf:proof}
We verify the properties of a group

* [Closure]  If $\bA$ and $\bB$ are invertible then $\bA \bB$ is invertible.
  Hence the set is closed.
* [Associativity] Matrix multiplication is associative.
* [Identity element] $\bI$ is invertible and $\bA \bI = \bI \bA = \bA$
  for all invertible matrices.
* [Inverse element] If $\bA$ is invertible then $\bA^{-1}$ is also invertible. 

Thus the set of invertible matrices is indeed a group under matrix multiplication.
````

````{prf:lemma} Rank of an invertible matrix
:label: lem:mat:invertible_rank

An $n \times n$ matrix $\bA$ is invertible if and only if it is full rank i.e.

$$
\Rank(\bA) = n.
$$
````

````{prf:corollary} Equality of rank of a matrix and its inverse
:label: res-mat-rank-mat-inverse

The rank of an invertible matrix  and its inverse are same.
````

## Similar Matrices

````{prf:definition} Similar matrix
:label: def:mat:similar_matrix

An $n \times n$ matrix $\bB$ is *similar* to an $n \times n$ matrix $\bA$
if there exists an $n \times n$ non-singular matrix $\bC$ such that

$$
\bB  = \bC^{-1} \bA \bC.
$$
````

````{prf:lemma} Symmetry of similarity
:label: res-mat-similar-symmetric-rel

If $\bB$ is similar to $\bA$ then $\bA$ is similar to $\bB$.
Thus similarity is a symmetric relation.
````
````{prf:proof}
We have

$$
\bB  = \bC^{-1} \bA \bC \implies \bA = \bC \bB \bC^{-1} 
\implies \bA = (\bC^{-1})^{-1} \bB \bC^{-1}
$$
Thus there exists a matrix $\bD = \bC^{-1}$ such that

$$
\bA = \bD^{-1} \bB \bD.
$$
Thus $\bA$ is similar to $\bB$.
````

````{prf:lemma} Rank of similar matrices
:label: lem:mat:similar_matrix_rank

Similar matrices have same rank.
````

````{prf:proof}
Let $\bB$ be similar to $\bA$.
Then their exists an invertible matrix $\bC$ such that

$$
\bB  = \bC^{-1} \bA \bC.
$$
Since $\bC$ is invertible hence we have $\Rank (\bC) = \Rank(\bC^{-1}) = n$.
Now using {prf:ref}`lem:mat:rank:full_rank_post_multiplier`

$$
\Rank (\bA \bC) = \Rank (\bA)
$$
and using {prf:ref}`lem:mat:rank:full_rank_pre_multiplier`
we have

$$
\Rank(\bC^{-1} (\bA \bC) ) = \Rank (\bA \bC) = \Rank(\bA).
$$
Thus

$$
\Rank(\bB)  = \Rank(\bA).
$$
````

````{prf:lemma} Similarity as equivalence relation
:label: res-mat-similarity-equivalence-relation

Similarity is an equivalence relation on the set of $n \times n$ matrices.
````

````{prf:proof}
Let $\bA, \bB, \bC$ be $n \times n$ matrices.
1. $\bA$ is similar to itself through an invertible matrix $\bI$.
1. If $\bA$ is similar to $\bB$ then $\bB$ is similar to itself.
1. If $\bB$ is similar to $\bA$ via $\bP$ s.t.
   $\bB = \bP^{-1} \bA \bP$ and $\bC$ is similar to $\bB$ 
   via $\bQ$ s.t. $\bC = \bQ^{-1} \bB \bQ$ then
   $\bC$ is similar to $\bA$ via $\bP \bQ$ 
   such that $\bC = (\bP \bQ)^{-1} \bA (\bP \bQ)$.
1. Thus similarity is an equivalence relation on the set of square matrices
   and if $\bA$ is any $n \times n$ matrix then the set
   of $n \times n$ matrices similar to $\bA$ forms an equivalence class. 
````

(sec:mat:gram_matrix)=
## Gram Matrices
````{prf:definition} Gram matrix
:label: def:mat:columns_gram_matrix

The *Gram matrix* of columns of $\bA$ is given by

$$
\bG = \bA^H \bA.
$$
````

````{prf:definition} Frame operator
:label: def:mat:frame_matrix

The *frame operator* is the Gram matrix of rows of $\bA$ is given by

$$
\bF = \bA \bA^H
$$
````

Usually when we talk about Gram matrix of a matrix we are looking at the
Gram matrix of its column vectors.

````{prf:remark} Gram matrix and frame operators for real matrices
:label: res-mat-gram-real-mat

For real matrix $\bA \in \RR^{m \times n}$, the Gram matrix of its column
vectors is given by $\bA^T \bA$ and the frame operator for its row vectors
is given by $\bA \bA^T$. 
````

Following results apply equally well for the real case.

````{prf:lemma} Linear dependence of columns and Gram matrix
:label: lem:mat:gram_dependent_columns

The columns of a matrix are linearly dependent if and only if 
the Gram matrix of its column vectors $\bA^H \bA$ is not invertible.
````
````{prf:proof}
Let $\bA$ be an $m\times n$ matrix and $\bG = \bA^H \bA$
be the Gram matrix of its columns.

1. If columns of $\bA$ are linearly dependent, then there exists a vector
   $\bu \neq \bzero$ such that
   
   $$
    \bA \bu = \bzero.
   $$
1. Thus
   
   $$
   \bG \bu = \bA^H \bA \bu  = \bzero.
   $$
1. Hence the columns of $\bG$ are also linearly dependent.
1. Hence $\bG$ is not invertible.

Conversely let us assume that $\bG$ is not invertible.
1. Thus columns of $\bG$ are dependent.
1. There exists a vector $\bv \neq \bzero$ such that 
   
   $$
   \bG \bv = \bzero.
   $$
1. Now 
   
   $$
   \bv^H \bG \bv =  \bv^H \bA^H \bA \bv = (\bA \bv)^H (\bA \bv) = \| \bA \bv \|_2^2.
   $$
1. From previous equation, we have
   
   $$
   \| \bA \bv \|_2^2 = 0 \implies \bA \bv = \bzero.
   $$
1. Since $\bv \neq \bzero$ hence columns of $\bA$ are also linearly dependent. 
````
````{prf:corollary} Linear independence of columns and Gram matrix
:label: cor:mat:gram_independent_columns

The columns of a matrix are linearly independent if and only if 
the Gram matrix of its column vectors $\bA^H \bA$ is invertible.
````

````{prf:proof}
Columns of $\bA$ can be  dependent only if its Gram matrix is not invertible.
Thus if the Gram matrix is invertible, then the columns of $\bA$ are linearly independent. 

The Gram matrix is not invertible only if columns of $\bA$ are linearly dependent. 
Thus if columns of $\bA$ are linearly independent then the Gram matrix is invertible.
````

````{prf:corollary}
:label: cor:mat:gram_full_column_rank_invertible

Let $\bA$ be a full column rank matrix. Then $\bA^H \bA$ is invertible.
````


````{prf:lemma}
:label: lem:mat:column_gram_matrix_null_space

The null space of $\bA$ and its Gram matrix $\bA^H \bA$ coincide; i.e.,

$$
\NullSpace(\bA) = \NullSpace(\bA^H \bA).
$$
````
````{prf:proof}
Let $\bu \in \NullSpace(\bA)$.
Then 

$$
\bA \bu  = \bzero \implies \bA^H \bA \bu = \bzero.
$$
Thus

$$
\bu \in \NullSpace(\bA^H \bA ) \implies \NullSpace(\bA) \subseteq \NullSpace(\bA^H \bA).
$$

Now let $\bu \in  \NullSpace(\bA^H \bA)$. Then

$$
\bA^H \bA \bu = \bzero \implies \bu^H \bA^H \bA \bu = \bzero 
\implies \| \bA \bu \|_2^2  = 0 \implies \bA \bu = \bzero.
$$
Thus we have

$$
\NullSpace(\bA^H \bA) \subseteq \NullSpace(\bA).
$$
````




````{prf:lemma}
:label: lem:mat:gram_dependent_rows

The rows of a matrix $\bA$ are linearly dependent
if and only if the Gram matrix of its
row vectors $\bA \bA^H$ is not invertible.
````
````{prf:proof}
Rows of $\bA$ are linearly dependent, if and only if columns of $\bA^H$ are linearly dependent. 

There exists a vector $\bv \neq \bzero$ s.t.

$$
\bA^H \bv = \bzero.
$$
Thus

$$
\bG \bv = \bA \bA^H \bv = \bzero.
$$
Since $\bv \neq \bzero$ hence $\bG$ is not invertible.

Converse: assuming that $\bG$ is not invertible,
there exists a vector $\bu \neq \bzero$ s.t.

$$
\bG \bu = \bzero.
$$
Now

$$
\bu^H \bG \bu 
= \bu^H \bA \bA^H \bu = (\bA^H \bu)^H (\bA^H \bu) 
= \| \bA^H \bu \|_2^2 = 0 
\implies \bA^H \bu =  \bzero.
$$
Since $\bu \neq \bzero$ hence columns of $\bA^H$
and consequently rows of $\bA$ are linearly dependent.
````

````{prf:corollary}
:label: cor:mat:gram_independent_rows

The rows of a matrix $\bA$ are linearly independent
if and only if the Gram matrix of its
row vectors $AA^H$ is invertible.
````
````{prf:corollary}
:label: cor:mat:gram_full_row_rank_invertible

Let $\bA$ be a full row rank matrix.
Then $\bA \bA^H$ is invertible.
````

## Pseudo Inverses
````{prf:definition} Moore Penrose pseudo inverse
:label: def:mat:moore_penrose_pseudo_inverse

Let $\bA$ be an $m \times n$ matrix.
An  $n\times m$ matrix $\bA^{\dag}$ is called its
*Moore-Penrose pseudo-inverse* if it satisfies all of the following criteria:

*  $\bA \bA^{\dag} \bA = \bA$.
*  $\bA^{\dag} \bA \bA^{\dag} = \bA^{\dag}$.
*  $\left(\bA \bA^{\dag} \right)^H = \bA \bA^{\dag}$ 
   i.e. $\bA \bA^{\dag}$ is Hermitian.
*  $(\bA^{\dag} \bA)^H = \bA^{\dag} \bA$ i.e. $\bA^{\dag} \bA$ is Hermitian.
````

````{prf:theorem} Existence and uniqueness of Moore Penrose pseudo inverse
:label: thm:mat:existence_uniqueness_moore_penrose_pseudo_inverse

For any matrix $\bA$ there exists precisely one matrix
$\bA^{\dag}$ which satisfies all the requirements in 
{prf:ref}`def:mat:moore_penrose_pseudo_inverse`.
````

We omit the proof for this. The pseudo-inverse can actually be obtained by the
singular value decomposition of $\bA$.
This is shown in {prf:ref}`lem:mat:singular:matrix_pseudo_inverse`.

````{prf:lemma} Moore Penrose pseudo inverse of a diagonal matrix
:label: lem:mat:moore_penrose_square_diagonal_pseudo_inverse

Let $\bD = \Diag(d_1, d_2, \dots, d_n)$ be an $n \times n$ diagonal matrix.
Then its Moore-Penrose pseudo-inverse is 
$\bD^{\dag} = \Diag(c_1, c_2, \dots, c_n)$ where

$$
c_i = \left\{
    \begin{array}{ll}
        \frac{1}{d_i} & \mbox{if $d_i \neq 0$};\\
        0 & \mbox{if $d_i = 0$}.
    \end{array}
  \right.
$$
````
````{prf:proof}
We note that $\bD^{\dag} \bD = \bD \bD^{\dag} 
= \bF = \Diag(f_1, f_2, \dots f_n)$ where 

$$
f_i = \left\{
    \begin{array}{ll}
        1 & \mbox{if $d_i \neq 0$};\\
        0 & \mbox{if $d_i = 0$}.
    \end{array}
  \right.
$$
We now verify the requirements in {prf:ref}`def:mat:moore_penrose_pseudo_inverse`.

$$
\bD \bD^{\dag} \bD = \bF \bD = \bD.
$$

$$
\bD^{\dag} \bD \bD^{\dag} = \bF \bD^{\dag} = \bD^{\dag}.
$$

$\bD^{\dag} \bD = \bD \bD^{\dag} = \bF$ is a diagonal hence Hermitian matrix.
````


````{prf:lemma} Moore Penrose pseudo inverse of a rectangular diagonal matrix
:label: lem:mat:moore_penrose_rectangular_diagonal_pseudo_inverse

Let $\bD = \Diag(d_1, d_2, \dots, d_p)$ be an $m \times n$
*rectangular* diagonal matrix where $p = \min(m, n)$.
Then its Moore-Penrose pseudo-inverse is an $n \times m$ rectangular diagonal matrix
$\bD^{\dag} = \Diag(c_1, c_2, \dots, c_p)$ where

$$
c_i = \left\{
    \begin{array}{ll}
        \frac{1}{d_i} & \mbox{if $d_i \neq 0$};\\
        0 & \mbox{if $d_i = 0$}.
    \end{array}
  \right.
$$
````
````{prf:proof}
We note that

$$
F = D^{\dag} D = \Diag(f_1, f_2, \dots f_n)
$$
is an $n \times n$ matrix where

$$
f_i = \left\{
    \begin{array}{ll}
        1 & \mbox{if $d_i \neq 0$};\\
        0 & \mbox{if $d_i = 0$};\\
        0 & \mbox{if $i > p$}.
    \end{array}
  \right.
$$

$\bG = \bD \bD^{\dag} = \Diag(g_1, g_2, \dots g_n)$ is an $m \times m$ matrix where

$$
g_i = \left\{
    \begin{array}{ll}
        1 & \mbox{if $d_i \neq 0$};\\
        0 & \mbox{if $d_i = 0$};\\
        0 & \mbox{if $i > p$}.
    \end{array}
  \right.
$$
We now verify the requirements in {prf:ref}`def:mat:moore_penrose_pseudo_inverse`.

$$
\bD \bD^{\dag} \bD = \bD \bF = \bD.
$$

$$
\bD^{\dag} \bD \bD^{\dag} = \bD^{\dag} \bG = \bD^{\dag}.
$$

$\bF = \bD^{\dag} \bD$ and 
$\bG = \bD \bD^{\dag}$ are both diagonal hence Hermitian matrices.
````



````{prf:lemma} Moore Penrose pseudo inverse of full column rank matrices
:label: lem:mat:moore_penrose_left_pseudo_inverse

If $\bA$ is full column rank then its Moore-Penrose pseudo-inverse is given by

$$
\bA^{\dag} = (\bA^H \bA)^{-1} \bA^H. 
$$
It is a left inverse of $\bA$.
````

````{prf:proof}
By {prf:ref}`cor:mat:gram_full_column_rank_invertible` $\bA^H \bA$ is invertible.
First of all we verify that it is a left inverse.

$$
\bA^{\dag} \bA = (\bA^H \bA)^{-1} \bA^H \bA = \bI.
$$
We now verify all the properties.

$$
\bA \bA^{\dag} \bA  = \bA \bI = \bA.
$$

$$
\bA^{\dag} \bA \bA^{\dag}   = \bI \bA^{\dag} = \bA^{\dag}.
$$
Hermitian properties:

$$
\left(\bA \bA^{\dag} \right)^H 
= \left(\bA (\bA^H \bA)^{-1} \bA^H \right)^H 
= \left(\bA (\bA^H \bA)^{-1} \bA^H \right)
= \bA \bA^{\dag}.
$$

$$
(\bA^{\dag} \bA)^H = \bI^H = \bI = \bA^{\dag} \bA.
$$
````

````{prf:lemma} Moore Penrose pseudo inverse of full row rank matrices
:label: lem:mat:moore_penrose_right_pseudo_inverse

If $\bA$ is full row rank then its Moore-Penrose pseudo-inverse is given by

$$
\bA^{\dag} = \bA^H (\bA \bA^H)^{-1} . 
$$
It is a right inverse of $\bA$.
````

````{prf:proof}
By {prf:ref}`cor:mat:gram_full_row_rank_invertible` $\bA \bA^H$ is invertible.
First of all we verify that it is a right inverse.

$$
\bA \bA^{\dag} =  \bA  \bA^H (\bA \bA^H)^{-1}= \bI.
$$
We now verify all the properties.

$$
\bA \bA^{\dag} \bA  = \bI \bA = \bA.
$$

$$
\bA^{\dag} \bA \bA^{\dag}   = \bA^{\dag} \bI = \bA^{\dag}.
$$
Hermitian properties:

$$
\left(\bA \bA^{\dag} \right)^H =  \bI^H = \bI = \bA \bA^{\dag}.
$$

$$
(\bA^{\dag} \bA)^H 
=  \left (\bA^H (\bA \bA^H)^{-1} \bA \right )^H 
=  \bA^H (\bA \bA^H)^{-1} \bA 
= \bA^{\dag} \bA.
$$
````


