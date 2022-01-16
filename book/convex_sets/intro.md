# Convex Sets


## Chapter Objectives

* Affine sets and subspaces
* Convex set definitions
* Different types of convex sets
* Properties of convex sets
* Convexity preserving operations
* Generalized inequalities on convex cones


## Real Vector Spaces

We shall concern ourselves with subsets of real vector spaces.
The scalar field associated with real vector spaces is $\RR$.
The vector spaces are denoted by $\VV$ or $\EE$.

* We shall exclusively work with finite dimensional vector spaces.
* The vector space is endowed with a *real* inner product whenever required.
* The vector space is endowed with a norm induced by the inner product whenever required.  

Examples of inner product spaces:

- Euclidean space $\RR^n$
- Space of matrices $\RR^{m \times n}$
- Space of symmetric matrices $\SS^n$.


## Sets in Vector Spaces

```{prf:definition} Arithmetic on sets
:label: def-vs-set-arithmetic

Let $C$, $D$ be subsets of $\VV$. Let $z \in \VV$. Let $\lambda \in \RR$.
Let $\Lambda \subseteq \RR$.

The addition of sets is defined as:

$$
C + D \triangleq \{ x + y \ST x \in C, y \in D \}.
$$

The subtraction of sets is defined as:

$$
C - D \triangleq \{ x - y \ST x \in C, y \in D \}.
$$

Addition of a set with a vector is defined as:

$$
z + C \triangleq \{ z + x \ST x \in C\} = \{ z \} + C.
$$

Subtraction of set with a vector is defined as:

$$
C - z \triangleq \{ x - z \ST x \in C\} = C - \{ z \}.
$$

Scalar multiplication of a set with a scalar is defined as:

$$
\lambda C \triangleq \{ \lambda x \ST x \in C \}.
$$

Multiplication of a set of scalars with a set of vectors is defined as:

$$
\Lambda C \triangleq \bigcup_{\lambda \in \Lambda} \lambda C.
$$

Multiplication of a set of scalars with a vector is defined as:

$$
\Lambda z \triangleq \Lambda \{ z \} = \{ \lambda z \ST \lambda \in \Lambda\}.
$$
```


## Span

```{prf:definition}
:label: def-vs-span

Let $C$ be a nonempty subset of $\VV$. 
The intersection of all the linear subspaces of $\VV$ 
containing $C$ is called the *span* of $C$ and is denoted
by $\span C$.
```