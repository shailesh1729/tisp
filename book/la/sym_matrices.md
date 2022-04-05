# Symmetric Matrices

````{prf:definition} Symmetric matrix
:label: def-la-symmetric-matrix

A *symmetric matrix* is a matrix $\bX \in \RR^{n \times n}$
which satisfies $\bX = \bX^T$.

We define the *set of symmetric $n\times n$ matrices* as

$$
    \SS^n = \{\bX \in \RR^{n \times n} | \bX = \bX^T\}.
$$
````

## The Vector Space of Symmetric Matrices

````{prf:theorem} The vector space of symmetric matrices
:label: res-la-symmetric-matrix-space

The set $\SS^n$ is a vector space with dimension $\frac{n(n+1)}{2}$.
````

```{prf:proof}
It suffices to show that any linear combination of symmetric
matrices is also symmetric. The dimension of this vector 
space comes from the number of entries in a symmetric matrix
which can be independently chosen.
```

```{prf:definition} Matrix inner product
:label: def-la-matrix-inner-product

An inner-product on the vector space of $n \times n$ real matrices 
can be defined as

$$
\langle \bA, \bB \rangle \triangleq \sum_i \sum_j A_{i,j} B_{i, j} 
 = \Trace (\bA^T \bB) = \Trace (\bB^T \bA).
$$

This is known as the *Frobenius inner product*.
```

```{prf:remark}
:label: res-la-sn-as-ip-space

Equipped with this inner product as 
defined in {prf:ref}`def-la-matrix-inner-product`, $\SS^n$ is a
finite dimensional real inner product space.
```


## Positive Semidefinite Matrices

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
:label: res-la-pd-diag-nng

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




## Positive Definite Matrices

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


## Negative Semidefinite Matrices

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


## Negative Definite Matrices

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


## Indefinite Matrices

````{prf:definition} Indefinite matrix
:label: def-la-indefinite-matrix

A symmetric matrix $\bA \in \SS^n$ is called *negative definite* if
there exist $\bx, \by \in \RR^n$ such that
$\bx^T \bA \bx < 0$ and $\by^T \bA \by > 0$.
````

Indefinite matrices are neither positive semidefinite nor negative semidefinite.


