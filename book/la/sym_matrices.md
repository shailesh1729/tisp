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

## Positive Semidefinite Matrices

````{prf:definition} Positive semidefinite matrix
:label: def-la-psd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *positive semi-definite* if
$\bv^T \bX \bv \geq 0$ for all $\bv \in \RR^n$.

The notation $\bX \succeq \ZERO$ means $\bv^T \bX \bv \geq 0 \Forall \bv \in \RR^n$
or the matrix $\bX$ is positive semi-definite.

We define the *set of symmetric positive semidefinite matrices* as

$$
    \SS_+^n = \{\bX \in \SS^n | \bX \succeq \ZERO \}.
$$
````
## Positive Definite Matrices

````{prf:definition} Positive definite matrix
:label: def-la-pd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *positive definite* if
$\bv^T \bX \bv > 0$ for all non-zero $\bv \in \RR^n$.

The notation $\bX \succ \ZERO$ means $\bv^T \bX \bv  > 0 \Forall \bv \in \RR^n, \bv \neq 0$
or the matrix $\bX$ is positive definite.

We define the *set of symmetric positive definite matrices* as

$$
    \SS_{++}^n = \{\bX \in \SS^n | \bX \succ 0 \}.
$$
````
