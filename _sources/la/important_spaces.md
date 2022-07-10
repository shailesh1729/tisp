# Important Vector Spaces

In this section, we will list some important
vector spaces which occur frequently in analysis
and optimization.

## The Vector Space of Symmetric Matrices

Recall from {prf:ref}`def-la-symmetric-matrix`
that the set of real symmetric
matrices is given by

$$
\SS^n = \{\bX \in \RR^{n \times n} | \bX = \bX^T\}.
$$

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

## The Vector Space of Real Valued Functions

```{prf:definition} The vector space of (total) real valued functions
:label: def-la-is-real-valued-functions-space

Let $X$ be a non-empty set. 
Let $\FFF (X, \RR)$ be the set of 
{prf:ref}`real valued total functions <def-bra-rvf-set>` on $X$.
The set $\FFF (X, \RR)$ is a vector space
over the scalar field of $\RR$
with the definitions following 
{prf:ref}`def-bra-real-valued-function-vector-space`:

Vector addition: If $f,g \in \FFF (X, \RR)$, then $h = f + g$ is defined as:

$$
h(\bx) \triangleq f(\bx) + g(\bx) \Forall \bx \in X.
$$

Scalar multiplication: if $\alpha \in \RR$ and $f \in \FFF (X, \RR)$, then $h = \alpha f$ is defined as:

$$
h (\bx) \triangleq \alpha f(\bx) \Forall X.
$$

Additive identity: There exists a function $\bzero \in \FFF (X, \RR)$ given by:

$$
\bzero(\bx) = 0 \Forall \bx \in X.
$$
```

## The Vector Space of Bounded Functions

It was discussed earlier in 
{prf:ref}`ex-ms-bounded-functions-metric-space`.

Recall from {prf:ref}`def-bra-bounded-function`
that a real valued (total) function $f: X \to \RR$ is called
bounded if there exists a number $M \geq 0$ (depending on $f$)
such that 

$$
    |f(x)| \leq M \Forall x \in X.
$$

```{prf:definition} The vector space of bounded functions
:label: def-la-is-bounded-functions-space

Let $X$ be a non-empty set. 
Let $B(X)$ be the set of bounded functions on $X$.
The set $B(X)$ is a vector space of bounded functions
over the scalar field of $\RR$
with the following operations:

Vector addition: If $f,g \in B(X)$, then $h = f + g$ is defined as:

$$
h(x) \triangleq f(x) + g(x) \Forall x \in X.
$$

Scalar multiplication: if $\alpha \in \RR$, then $h = \alpha f$ is defined as:

$$
h (x) \triangleq \alpha f(x) \Forall x \in X.
$$
```

```{prf:definition} Sup norm for the space of bounded functions
:label: def-la-is-bx-sup-norm

The standard norm for $B(X)$ is defined for any $f \in B(X)$ as:

$$
\| f \| \triangleq  \sup \{ |f(x) | \Forall x \in X\}.
$$

This norm is known as *sup norm* and often written as $\| f \|_{\infty}$.
```

```{prf:definition} Metric induced by the norm

The standard metric induced by the standard norm for $B(X)$
is defined for any $f,g \in B(X)$ as:

$$
d(f,g) \triangleq \| f - g \| = \sup \{ | f(x) - g(x) | \Forall x \in X \}.
$$
```

```{prf:theorem} $B(X)$ is complete
:label: res-la-is-bx-complete

The normed vector space $B(X)$ is complete. 
Thus, $B(X)$ is a Banach space.
```
```{prf:proof}
See {prf:ref}`ex-ms-bounded-functions-metric-space`
for the detailed proof.
```
