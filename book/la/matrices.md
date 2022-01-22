(sec:la:matrices)=
# Matrices


```{prf:definition} Matrix
An $m \times n$ *matrix* $\bA$ is a rectangular array 
of numbers.

$$
\bA = \begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n}\\
a_{21} & a_{22} & \dots & a_{2n}\\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}\\
\end{bmatrix}.
$$
The numbers in a matrix are called its *elements*.

The matrix consists of $m$ *rows* and $n$ *columns*.
The entry in $i$-th row and $j$-th column is referred
with the notation $a_{ij}$. 

If all the elements of a matrix are real, then we 
call it a *real matrix*.

If any of the elements of the matrix is *complex*,
then we call it a *complex matrix*.

A matrix is often written in short as $\bA = (a_{ij})$.
```

```{prf:definition} The set of matrices
The set of all real matrices of shape $m \times n$ is
denoted by $\RR^{m \times n}$.

The set of all complex matrices of shape $m \times n$ is
denoted by $\CC^{m \times n}$.
```

```{prf:definition} Vector
A *vector* is an $n$-tuple of numbers written as:

$$
\bv = (v_1, v_2, \dots, v_n).
$$
If all the numbers are real, then it is called a
real vector belonging to the set $\RR^n$.

If any of the numbers is complex, then it is called
a complex vector belonging to the set $\CC^n$.

The numbers in a vector are called its *components*.
```

```{prf:definition} Column vector
A matrix with shape $m \times 1$ is called a *column vector*.
```

```{prf:definition} Row vector
A matrix with shape $1 \times n$ is called a *row vector*.
```

```{note}
It should be easy to see that $\RR^{m \times 1}$ and $\RR^m$ are
same sets.
Similarly, $\RR^{1\times n}$ and $\RR^n$ are same sets.

A row or column vector can easily be written as an $n$-tuple.
```


```{prf:definition} Matrix addition

Let $\bA$ and $\bB$ be two matrices with same shape $m \times n$.
Then, their addition is defined as:

$$
\bA + \bB = (a_{ij}) + (b_{ij}) \triangleq (a_{ij} + b_{ij}). 
$$
```


```{prf:definition} Scalar multiplication
Let $\bA$ be a matrix of shape $m \times n$ and $\lambda$ be
a scalar. The product of the matrix $\bA$ with the scalar $\lambda$
is defined as:

$$
\lambda \bA = \bA \lambda \triangleq (\lambda a_{ij}).
$$ 
```

```{prf:theorem} Properties of matrix addition and scalar multiplication

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
Let $\bA, \bB, \bC$ be matrices of appropriate shape.

1. Matrix multiplication is associative: 
   $\bA (\bB \bC) = (\bA \bB)\bC$.
1. Matrix multiplication distributes over matrix addition:
   $\bA (\bB + \bC) = \bA \bB + \bA \bC$
   and $(\bA + \bB) \bC = \bA \bC + \bB \bC$.
```