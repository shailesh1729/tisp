(sec:la:symmetric-matrices)=
# Eigenvalue Decomposition

In this subsection, we discuss the eigenvalue decomposition of
real symmetric matrices.

## Semidefinite, Definite and Indefinite Matrices

### Positive Semidefinite Matrices

````{prf:definition} Positive semidefinite matrix
:label: def-la-psd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *positive semi-definite* if
$\bv^T \bX \bv \geq 0$ for all $\bv \in \RR^n$.

The notation $\bX \succeq \ZERO$ means $\bv^T \bX \bv \geq 0 \Forall \bv \in \RR^n$
or the matrix $\bX$ is positive semi-definite.

We define the *set of symmetric positive semidefinite matrices* as

$$
\SS_+^n = \{\bX \in \SS^n \ST \bX \succeq \ZERO \}.
$$

"positive semidefinite" is often abbreviated as "p.s.d.".
````


```{prf:theorem} 
:label: res-la-ata-as-psd-matrix

Let $\bA \in \RR^{m \times n}$ be an arbitrary matrix. 
Then, $\bA^T \bA$ is a p.s.d. matrix in $\SS^n$ and
$\bA \bA^T$ is a p.s.d. matrix in $\SS^m$.
```

```{prf:proof}

We shall just prove this for $\bA^T \bA$.

1. We note that

   $$
   (\bA^T \bA)^T = \bA^T \bA.
   $$
   Thus,  $\bA^T \bA$ is symmetric.
1. $\bA^T \bA \in \RR^{n \times n}$. Since it is symmetric, hence $\bA^T \bA \in \SS^n$.
1. Let $\bv \in \RR^n$.
1. Then,

   $$
   \bv^T \bA^T \bA \bv  = (\bA \bv)^T (\bA \bv) 
   = \| \bA \bv \|^2 \geq 0
   $$
   where $\| \cdot \|$ is the norm induced by the dot product on
   $\RR^n$.
1. Thus, $\bA^T \bA$ is p.s.d..
```

```{prf:theorem} Non-negativity of the diagonal elements of p.s.d. matrices
:label: res-la-psd-diag-nng

Let $\bA \in \RR^{n \times n}$ be positive semidefinite.
Then, its diagonal elements are non-negative.
```

```{prf:proof}

Let $\bA \in \SS_+^n$.

1. Then, for every nonzero $\bv \in \RR^n$, $\bv^T \bA \bv \geq 0$.
1. In particular, this is true for standard unit vectors.
1. But $\be_i^T \bA \be_i = A_{i,i}$.
1. Hence, $A_{i,i} \geq 0$ must be true.
```



```{prf:definition} Square root of a positive semidefinite matrix
:label: def-la-psd-square-root

Let $\bA \in \SS^n$ be a positive semidefinite matrix. The
*square root* of $\bA$, denoted by $\bA^{\frac{1}{2}}$ is defined
as follows. 

Let $\bA = \bU \bD \bU^T$ be the eigenvalue decomposition of $\bA$.
Let $d_1,\dots,d_n$ be the diagonal elements of $\bD$.
Let $\bE = \Diag(\sqrt{d_1}, \dots, \sqrt{d_n})$. Then, 

$$
\bA^{\frac{1}{2}} \triangleq \bU \bE \bU^T.
$$
The matrix $\bU \bE \bU^T$ is known as the *positive semidefinite square root*.
```
The definition of $\bE$ is justified since $d_i \geq 0$ for a p.s.d. matrix.

We can see that

$$
ç \bA^{\frac{1}{2}} = 
\bU \bE \bU^T \bU \bE \bU^T
= \bU \bE \bE \bU^T = \bU \bD \bU^T = \bA.
$$


### Positive Definite Matrices

````{prf:definition} Positive definite matrix
:label: def-la-pd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *positive definite* if
$\bv^T \bX \bv > 0$ for all non-zero $\bv \in \RR^n$.

The notation $\bX \succ \ZERO$ means $\bv^T \bX \bv  > 0 \Forall \bv \in \RR^n, \bv \neq 0$
or the matrix $\bX$ is positive definite.

We define the *set of symmetric positive definite matrices* as

$$
\SS_{++}^n = \{\bX \in \SS^n \ST \bX \succ 0 \}.
$$

"positive definite" is often abbreviated as "p.d.".
````


```{prf:theorem} Positivity of the diagonal elements of p.d. matrices
:label: res-la-pd-diag-positive

Let $\bA \in \RR^{n \times n}$ be positive definite.
Then, its diagonal elements are positive.
```

```{prf:proof}

Let $\bA \in \SS_{++}^n$.

1. Then, for every nonzero $\bv \in \RR^n$, $\bv^T \bA \bv > 0$.
1. In particular, this is true for standard unit vectors.
1. But $\be_i^T \bA \be_i = A_{i,i}$.
1. Hence, $A_{i,i} > 0$ must be true.
```


```{prf:theorem} Principal minors criterion
:label: res-la-pd-principal-minors-criterion

A matrix $\bA \in \SS^n$ is positive definite if and only if
the determinants of all the principal minors are positive.

In other words, $D_1(\bA) > 0, D_2(\bA) > 0, \dots, D_n(\bA) > 0$
where $D_i(\bA)$ denotes the determinant of the upper left $i \times i$
submatrix (the $i$-th principal minor). 
```

### Negative Semidefinite Matrices

````{prf:definition} Negative semidefinite matrix
:label: def-la-nsd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *negative semi-definite* if
$\bv^T \bX \bv \leq 0$ for all $\bv \in \RR^n$.

The notation $\bX \preceq \ZERO$ means $\bv^T \bX \bv \leq 0 \Forall \bv \in \RR^n$
or the matrix $\bX$ is negative semi-definite.

We define the *set of symmetric negative semidefinite matrices* as

$$
    \SS_-^n = \{\bX \in \SS^n \ST \bX \preceq \ZERO \}.
$$

"negative semidefinite" is sometimes abbreviated as "n.s.d.".
````


### Negative Definite Matrices

````{prf:definition} Negative definite matrix
:label: def-la-nd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *negative definite* if
$\bv^T \bX \bv < 0$ for all non-zero $\bv \in \RR^n$.

The notation $\bX \prec \ZERO$ means $\bv^T \bX \bv  < 0 \Forall \bv \in \RR^n, \bv \neq 0$
or the matrix $\bX$ is negative definite.

We define the *set of symmetric negative definite matrices* as

$$
\SS_{--}^n = \{\bX \in \SS^n \ST \bX \prec 0 \}.
$$

"negative definite" is sometimes abbreviated as "n.d.".
````


### Indefinite Matrices

````{prf:definition} Indefinite matrix
:label: def-la-indefinite-matrix

A symmetric matrix $\bA \in \SS^n$ is called *indefinite* if
there exist $\bx, \by \in \RR^n$ such that
$\bx^T \bA \bx < 0$ and $\by^T \bA \by > 0$.
````

Indefinite matrices are neither positive semidefinite nor negative semidefinite.

```{prf:theorem} Diagonal elements and indefiniteness
:label: res-la-diag-indefinite

Let $\bA \in \SS^n$. If the diagonal elements of $\bA$ are both
positive and negative, then $\bA$ is indefinite.
```

```{prf:proof}
Each diagonal element corresponds to $\be_i^T \bA \be_i$ for a
unit vector $\be_i$.
If the diagonal elements are both positive and negative, then
there exist unit vectors $\be_i$ and $\be_j$ such that
$\be_i^T \bA \be_i < 0$ and $\be_j^T \bA \be_j > 0$. 
Thus, $\bA$ is indefinite.
```

### Eigenvalue Decomposition

```{prf:theorem} Eigenvalue characterization theorem
:label: res-la-evd-definiteness-charac

Let $\bA \in \SS^n$ be an $n\times n$ symmetric matrix.

1. $\bA$ is positive definite if and only if all its eigenvalues are positive.
1. $\bA$ is positive semidefinite if and only if all its eigenvalues are nonnegative.
1. $\bA$ is negative definite if and only if all its eigenvalues are negative.
1. $\bA$ is negative semidefinite if and only if all its eigenvalues are nonpositive.
1. $\bA$ is indefinite if and only if at least one eigenvalue is positive and
   at least one eigenvalue is negative.
```

```{prf:proof}
Let the eigenvalue decomposition of $\bA$ be given by
$\bA = \bU \bD \bU^T$.

We prove (1).

1. Let $\bv \in \RR^n$.
1. Then

   $$
   \bv^T \bA \bv = \bv^T \bU \bD \bU^T \bv
   = \bw^T \bD \bw = \sum_{i=1}^n d_i w_i^2.
   $$
   where $\bw = \bU^T \bv$.
1. Since $\bU$ is nonsingular, hence $\bv^T \bA \bv > 0$ for every $\bv \neq \bzero$
   if and only if $\sum_{i=1}^n d_i w_i^2 > 0$ for every $\bw \neq \bzero$.
1. Plugging $\be_i$ for $\bw$, we see that $d_i > 0$ is a necessary condition.
1. Also, if $d_i > 0$ for every $i$, then, the sum is positive for every nonzero $\bw$
   since at least one $w_i \neq 0$.
   Hence, it is a sufficient condition. 

Similar arguments apply for other statements.
```

### Trace and Determinant

```{prf:corollary} Trace and determinant of positive definite matrices
:label: res-la-pd-trace-det

Let $\bA$ be a symmetric positive definite matrix. Then, $\Trace (\bA)$ and $\det (\bA)$
are positive.
```

```{prf:proof}
Trace is the sum of eigenvalues. Determinant is the product of eigenvalues.
If $\bA$ is symmetric positive definite, then its eigenvalues are positive.
Hence, trace and determinant are positive.
```

```{prf:corollary} Trace and determinant of positive semidefinite matrices
:label: res-la-psd-trace-det

Let $\bA$ be a symmetric positive definite matrix. Then, $\Trace (\bA)$ and $\det (\bA)$
are nonnegative.
```

## Diagonally Dominant Matrices


```{prf:definition} Diagonally dominant matrix
:label: def-la-sym-diagonally-dominant-matrix

Let $\bA \in \SS^n$. 

1. $\bA$ is called *diagonally dominant* if

   $$
   | A_{i i} | \geq \sum_{j \neq i} | A_{i j} | 
   $$
   for every $i=1,\dots,n$.
   In other words, the absolute value of the diagonal entry in a row
   is greater than or equal to the sum of absolute values of non diagonal entries in the row.
1. $\bA$ is called *strictly diagonally dominant* if

   $$
   | A_{i i} | > \sum_{j \neq i} | A_{i j} | 
   $$
   for every $i=1,\dots,n$.
```

```{prf:theorem} Positive semidefiniteness of diagonally dominant matrices
:label: res-la-sym-ddm-psd

Let $\bA \in \SS^n$ be a real symmetric matrix. 

1. If $\bA$ is diagonally dominant whose diagonal entries are nonnegative then
   $\bA$ is positive semidefinite.
1. If $\bA$ is strictly diagonally dominant whose diagonal entries are positive
   then $\bA$ is positive definite.
```

```{prf:proof}

Assume that $\bA$ is diagonally dominant with nonnegative diagonal entries.

1. For contradiction, assume that $\bA$ is not positive semidefinite.
1. Then, there is an eigen value $\lambda < 0$ and corresponding eigenvector $\bu$.
1. Consider the absolute values of entries of $\bu$ given by $(|u_1|, \dots, |u_n|)$.
1. Let $i \in 1,\dots,n$ denote the index of the largest absolute value entry of $\bu$.
1. We also have $\bA \bu = \lambda \bu$.
1. For the $i$-th row, we get the equality

   $$
   & \sum_{j = 1}^n A_{i j} u_j = \lambda u_i \\
   & \iff \sum_{j \neq i} A_{i j} u_j = \lambda u_i - A_{i i} u_i \\
   & \iff \left | \sum_{j \neq i} A_{i j} u_j \right | = | \lambda - A_{i i} | |u_i | \\
   & \implies  | \lambda - A_{i i} | |u_i | 
   \leq \left ( \sum_{j \neq i} | A_{i j} | \right ) | u_i |
   \leq |A_{ i i} | |u_i |.
   $$
1. Thus,  $| \lambda - A_{i i} |  = |A_{ i i} - \lambda | \leq |A_{ i i} |$.
1. But $A_{i i}$ is nonnegative and $\lambda$ is negative, hence this reduces to
   $A_{ i i} - \lambda \leq A_{i i}$ or $\lambda \geq 0$.
1. We have arrived at a contradiction.
1. Thus, $\bA$ must be positive semidefinite.


Now, assume that $\bA$ is strictly diagonally dominant with positive diagonal entries.

1. By first part, it is clear that $\bA$ is p.s.d..
1. We just need to show that all eigenvalues are positive. There are no zero eigenvalues.
1. For contradiction, assume that $0$ is indeed an eigenvalue of $\bA$.
1. Let $\bu \neq \bzero$ be corresponding eigenvector satisfying
   $\bA \bu = \bzero$.
1. Let $i \in 1,\dots,n$ denote the index of the largest absolute value entry of $\bu$.
1. Following the earlier argument

   $$
   | A_{i i}| |u_i | &= \left | \sum_{j \neq i} A_{i j} u_j  \right | \\
   &\leq \left ( \sum_{j \neq i} | A_{i j} | \right ) |u_i| \\
   &< | A_{i i} | |u_i|.
   $$
1. This is impossible. Hence, $\bA$ must be positive definite.
```

