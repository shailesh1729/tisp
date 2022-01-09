# Symmetric Matrices

````{prf:definition} Symmetric matrix
:label: def-symmetric-matrix

A *symmetric matrix* is a matrix $X \in \RR^{n \times n}$
which satisfies $X = X^T$.

We define the *set of symmetric $n\times n$ matrices* as

$$
    \SS^n = \{X \in \RR^{n \times n} | X = X^T\}.
$$
````

````{prf:proposition}
$\SS^n$ is a vector space with dimension $\frac{n(n+1)}{2}$.
````
It suffices to show that any linear combination of symmetric
matrices is also symmetric. The dimension of this vector 
space comes from the number of entries in a symmetric matrix
which can be independently chosen.

```{prf:definition} Matrix inner product
:label: def-matrix-inner-product

An inner-product on the vector space of $n \times n$ real matrices 
can be defined as

$$
\langle A, B \rangle \triangleq \sum_i \sum_j A_{i,j} B_{i, j} 
 = \Trace (A^T B) = \Trace (B^T A).
$$

This is known as the *Frobenius inner product*.
```

## Positive semi-definite matrices

````{prf:definition} Positive semidefinite matrix
:label: def-positive-semidefinite-symmetric-matrix

A symmetric matrix $X \in \SS^n$ is called *positive semi-definite* if
$v^T X v \geq 0$ for all $v \in \RR^n$.

The notation $X \succeq 0$ means $v^T X v \geq 0 \Forall v \in \RR^n$
or the matrix $X$ is positive semi-definite.

We define the *set of symmetric positive semidefinite matrices* as

$$
    \SS_+^n = \{X \in \SS^n | X \succeq 0 \}.
$$
````
## Positive definite matrices

````{prf:definition} Positive definite matrix
:label: def-positive-definite-symmetric-matrix

A symmetric matrix $X \in \SS^n$ is called *positive definite* if
$v^T X v > 0$ for all non-zero $v \in \RR^n$.

The notation $X \succ 0$ means $v^T X v  > 0 \Forall v \in \RR^n, v \neq 0$
or the matrix $X$ is positive definite.

We define the *set of symmetric positive definite matrices* as

$$
    \SS_{++}^n = \{X \in \SS^n | X \succ 0 \}.
$$
````

## Positive semi-definite cone

````{prf:proposition}
The set $\SS_+^n$ is a convex cone.
````

````{prf:proof}
Let $A, B \in \SS_+^n$ and $\theta_1, \theta_2 \geq 0$. We have to show that
$\theta_1 A + \theta_2 B \in \SS_+^n$.

$$
    A \in \SS_+^n \implies v^T A v \geq 0 \Forall v \in \RR^n.
$$

$$
    B \in \SS_+^n \implies v^T B v \geq 0 \Forall v \in \RR^n.
$$

Now

$$
    v^T (\theta_1 A + \theta_2 B) v = \theta_1 v^T A v + \theta_2 v^T B v \geq 0 \Forall v \in \RR^n.
$$

Hence $\theta_1 A + \theta_2 B \in \SS_+^n$.
````
