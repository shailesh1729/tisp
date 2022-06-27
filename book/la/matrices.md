(sec:la:matrices)=
# Matrices I

This section provides some basic definitions, notation and results on the
theory of matrices.

## Basic Definitions

```{prf:definition} Matrix
:label: def-la-mat-matrix

An $m \times n$ *matrix* $\bA$ is a rectangular array 
of numbers.

$$
\bA = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1 n}\\
a_{21} & a_{22} & \dots & a_{2 n}\\
\vdots & \vdots & \ddots & \vdots \\
a_{m s1} & a_{m 2} & \dots & a_{m n}\\
\end{bmatrix}.
$$
The numbers in a matrix are called its *elements*.

The matrix consists of $m$ *rows* and $n$ *columns*.
The entry in $i$-th row and $j$-th column is referred
with the notation $a_{i j}$. 

If all the elements of a matrix are real, then we 
call it a *real matrix*.

If any of the elements of the matrix is *complex*,
then we call it a *complex matrix*.

A matrix is often written in short as $\bA = (a_{ij})$.
```

Matrices are denoted by bold capital letters $\bA$, $\bB$ etc..
They can be rectangular with $m$ rows and $n$ columns.
Their *elements* or *entries* are referred to with small letters
$a_{i j}$, $b_{i j}$ etc. where $i$ denotes the $i$-th
row of matrix and $j$ denotes the $j$-th column of matrix.

```{prf:definition} The set of matrices
:label: def-la-mat-matrix-set

The set of all real matrices of shape $m \times n$ is
denoted by $\RR^{m \times n}$.

The set of all complex matrices of shape $m \times n$ is
denoted by $\CC^{m \times n}$.
```

````{prf:definition} Square matrix
:label: def:mat:square_matrix

An $m \times n$ matrix is called *square matrix* if $m = n$.
````

````{prf:definition} Tall matrix
:label: def:mat:tall_matrix

An $m \times n$ matrix is called *tall matrix* if $m > n$ i.e. 
the number of rows is greater than columns.
````

````{prf:definition} Wide matrix
:label: def:mat:wide_matrix

An $m \times n$ matrix is called *wide matrix* if $m < n$ i.e. 
the number of columns is greater than rows.
````


```{prf:definition} Vector
:label: def-la-mat-vector

A *vector* is an $n$-tuple of numbers written as:

$$
\bv = (v_1, v_2, \dots, v_n).
$$
If all the numbers are real, then it is called a
real vector belonging to the set $\RR^n$.
If any of the numbers is complex, then it is called
a complex vector belonging to the set $\CC^n$.
The numbers in a vector are called its *components*.

Sometimes, we may use a notation without commas.

$$
\bv = \begin{pmatrix}v_1 &  v_2 & \dots & v_n \end{pmatrix}.
$$
```

```{prf:definition} Column vector
:label: def-la-mat-col-vec

A matrix with shape $m \times 1$ is called a *column vector*.
```

```{prf:definition} Row vector
:label: def-la-mat-row-vec

A matrix with shape $1 \times n$ is called a *row vector*.
```

```{note}
It should be easy to see that $\RR^{m \times 1}$ and $\RR^m$ are
same sets.
Similarly, $\RR^{1\times n}$ and $\RR^n$ are same sets.

A row or column vector can easily be written as an $n$-tuple.
```

````{prf:definition} Main diagonal
:label: def:mat:main_diagonal

Let $\bA= [a_{i j}]$ be an $m \times n$ matrix.
The main diagonal consists of entries $a_{i j}$ where $i = j$;
i.e., the main diagonal is 
$\{a_{11}, a_{22}, \dots, a_{k k} \}$ where $k = \min(m, n)$.

Main diagonal is also known as 
*leading diagonal*,
*major diagonal*
*primary diagonal* or
*principal diagonal*.

The entries of $\bA$ which are not on the main diagonal are known as 
*off diagonal* entries.
````

````{prf:definition} Diagonal matrix
:label: def:mat:diagonal_matrix

A *diagonal matrix* is a matrix (usually a square matrix) whose entries outside 
the main diagonal are zero. 

Whenever we refer to a diagonal matrix which is not square, we will use the term
*rectangular diagonal matrix*.

A square diagonal matrix $A$ is also written as $\Diag(a_{11}, a_{22}, \dots, a_{n n})$
which lists only the diagonal (non-zero) entries in $\bA$.
````

If not specified, the square matrices will be of size $n \times n$
and rectangular matrices will be of size $m \times n$. 
If not specified the vectors (column vectors) will be of size $n \times 1$ 
and belong to either $\RR^n$ or $\CC^n$. Corresponding row vectors
will be of size $1 \times n$.

## Matrix Operations

```{prf:definition} Matrix addition
:label: def-la-mat-matrix-addition

Let $\bA$ and $\bB$ be two matrices with same shape $m \times n$.
Then, their addition is defined as:

$$
\bA + \bB = (a_{ij}) + (b_{ij}) \triangleq (a_{ij} + b_{ij}). 
$$
```


```{prf:definition} Scalar multiplication
:label: def-la-mat-matrix-scalar-mult

Let $\bA$ be a matrix of shape $m \times n$ and $\lambda$ be
a scalar. The product of the matrix $\bA$ with the scalar $\lambda$
is defined as:

$$
\lambda \bA = \bA \lambda \triangleq (\lambda a_{ij}).
$$ 
```

```{prf:theorem} Properties of matrix addition and scalar multiplication
:label: res-la-mat-matrix-add-mult-props

Let $\bA, \bB, \bC$ be matrices of shape $m \times n$.
Let $\lambda, \mu$ be scalars. 
Then:

1. Matrix addition is commutative: $\bA + \bB = \bB + \bA$.
1. Matrix addition is associative: $\bA + (\bB + \bC) = (\bA + \bB) + \bC$.
1. Addition in scalars distributes over scalar multiplication: 
   $(\lambda + \mu)\bA = \lambda \bA + \mu \bA$.
1. Scalar multiplication distributes over addition of matrices: 
   $\lambda (\bA + \bB) = \lambda \bA + \lambda \bB$.
1. Multiplication in scalars commutes with scalar multiplication:
   $(\lambda \mu) \bA = \lambda (\mu \bA)$.
1. There exists a matrix with all elements being zero denoted by $\ZERO$
   such that $\bA + \ZERO = \ZERO + \bA = \bA$.
1. Existence of additive inverse:
   $\bA + (-1)\bA = \ZERO$.
```


```{prf:definition} Matrix multiplication
:label: def-la-mat-matrix-mult


If $\bA$ is an $m \times n$ matrix and $\bB$ is an $n \times p$
matrix (thus, $\bA$ has same number of columns as $\bB$ has rows),
then we define the *product* of $\bA$ and $\bB$ as:

$$
\bA \bB \triangleq \left ( \sum_{k=1}^n a_{ik} b_{kj} \right ).
$$
This binary operation is known as *matrix multiplication*.
The product matrix has the shape $m \times p$.
Its $i,j$-th element is $\sum_{k=1}^n a_{ik} b_{kj}$
obtained by multiplying the $i$-th row of $A$ with the $j$-th column
of $B$ element by element and then summing over them.
```


```{prf:theorem} Properties of matrix multiplication
:label: res-la-mat-matrix-mult-props

Let $\bA, \bB, \bC$ be matrices of appropriate shape.

1. Matrix multiplication is associative: 
   $\bA (\bB \bC) = (\bA \bB)\bC$.
1. Matrix multiplication distributes over matrix addition:
   $\bA (\bB + \bC) = \bA \bB + \bA \bC$
   and $(\bA + \bB) \bC = \bA \bC + \bB \bC$.
```



## Transpose

The transpose of a matrix $\bA$ is denoted by $\bA^T$
while the Hermitian transpose is denoted by $\bA^H$.
For real matrices $\bA^T  = \bA^H$.

For statements which are valid both for real and complex matrices, sometimes we might say
that matrices belong to $\FF^{m \times n}$ while the scalars belong to the field $\FF$ 
and vectors belong to $\FF^n$ where $\FF$ refers to either the field of
real numbers or the field of complex numbers.
Most results from matrix analysis are written only for $\CC^{m \times n}$ while
still being applicable for $\RR^{m \times n}$.

Identity matrix for $\FF^{n \times n}$ is denoted as $\bI_n$ or simply $\bI$
whenever the size is clear from context. 

Sometimes we will write a matrix in terms of its column vectors. We will use
the notation

$$
\bA  = \begin{bmatrix} \ba_1 & \ba_2 & \dots & \ba_n \end{bmatrix}
$$
indicating $n$ columns.

When we write a matrix in terms of its row vectors, we will use the notation

$$
\bA = \begin{bmatrix} \ba_1^T \\ \ba_2^T \\ \vdots \\ \ba_m^T \end{bmatrix}
$$
indicating $m$ rows with $\ba_i$ being column vectors whose transposes form the 
rows of $\bA$.

## Dot Products

The inner product or dot product of two column / row vectors
$\bu$ and $\bv$ belonging to $\RR^n$ is defined as

```{math}
 :label: eq:mat:column:inner_product
\bu \cdot \bv = \langle \bu, \bv \rangle = \sum_{i=1}^n u_i v_i.
```

The inner product or dot product of two column / row vectors
$\bu$ and $\bv$ belonging to $\CC^n$ is defined as

```{math}
:label: eq:mat:column:inner_product:complex
\bu \cdot \bv = \langle \bu, \bv \rangle = \sum_{i=1}^n u_i \overline{v_i}.
```

## Block Matrices
````{prf:definition} Block matrix
:label: def:mat:block_matrix

A *block matrix* is a matrix whose entries themselves are matrices with following constraints

*  Entries in every row are matrices with same number of rows.
*  Entries in every column are matrices with same number of columns.

Let $\bA$ be an $m \times n$ block matrix. Then

$$
\bA = \begin{bmatrix}
\bA_{11} & \bA_{12} & \dots & \bA_{1 n}\\
\bA_{21} & \bA_{22} & \dots & \bA_{2 n}\\
\vdots & \vdots & \ddots & \vdots\\
\bA_{m 1} & \bA_{m 2} & \dots & \bA_{m n}\\
\end{bmatrix}
$$
where $\bA_{i j}$ is a matrix with $r_i$ rows and $c_j$ columns.

A block matrix is also known as a *partitioned matrix*.
````

````{prf:example} $2x2$ block matrices
:label: ex-mat-2x2-block-matrix

Quite frequently we will be using $2x2$ block matrices.

$$
\bP = \begin{bmatrix}
\bP_{11} & \bP_{12} \\
\bP_{21} & \bP_{22}
\end{bmatrix}.
$$
An example

$$
P  =
\left[
\begin{array}{c c | c}
a & b & c \\
d & e & f \\
\hline
g & h & i
\end{array}
\right]
$$
We have

$$
\bP_{11} = 
\begin{bmatrix}
a & b \\
d & e
\end{bmatrix} \;
\bP_{12}  = 
\begin{bmatrix}
c \\
f
\end{bmatrix} \;
\bP_{21}  = 
\begin{bmatrix}
g &
h
\end{bmatrix} \;
\bP_{22}  = 
\begin{bmatrix}
i
\end{bmatrix}
$$

*  $\bP_{11}$ and $\bP_{12}$ have $2$ rows.
*  $\bP_{21}$ and $\bP_{22}$ have $1$ row.
*  $\bP_{11}$ and $\bP_{21}$ have $2$ columns.
*  $\bP_{12}$ and $\bP_{22}$ have $1$ column.
````

````{prf:lemma} Shape of a block matrix
:label: res-mat-block-matrix-shape

Let $\bA = [\bA_{ij}]$ be an $m \times n$ block matrix with 
$\bA_{ij}$ being an $r_i \times c_j$ matrix.
Then $\bA$ is an $r \times c$ matrix where

$$
r = \sum_{i=1}^m r_i
$$
and

$$
c = \sum_{j=1}^n c_j.
$$
````
Sometimes it is convenient to think of a regular matrix as a block matrix whose
entries are $1 \times 1$ matrices themselves.

````{prf:definition} Multiplication of block matrices
:label: def:mat:multiplication_block_matrix

Let $\bA = [\bA_{ij}]$ be an $m \times n$ block matrix with
$\bA_{ij}$ being a $p_i \times q_j$ matrices.
Let $\bB = [\bB_{jk}]$ be an $n \times p$ block matrix with
$\bB_{jk}$ being a $q_j \times r_k$ matrices.

Then the two block matrices are *compatible* for multiplication
and their multiplication 
is defined by $\bC = \bA \bB = [\bC_{i k}]$ where 

$$
\bC_{i k} = \sum_{j=1}^n \bA_{i j} \bB_{j k}
$$
and $\bC_{i k}$ is a $p_i \times r_k$ matrix.
````

````{prf:definition} Block diagonal matrix
:label: def:mat:block_diagonal_matrix

A *block diagonal matrix* is a block matrix whose off diagonal entries are zero matrices.
````
