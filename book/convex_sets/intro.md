# Convex Sets


## Chapter Objectives

* Affine sets and subspaces
* Convex set definitions
* Different types of convex sets
* Properties of convex sets
* Convexity preserving operations
* Generalized inequalities on convex cones


We recall that 

```{div}
* $\RR$ denotes the real line
* $\ERL$ denotes the extended real line
* $\RR_+$ denotes the set of nonnegative reals.
* $\RR_{++}$ denotes the set of positive reals.
```


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


## Operators

```{prf:definition} Homogeneous operator
Let $\XX$ and $\YY$ be real vector spaces. 
An operator $T : \XX \to \YY$ is called *homogeneous* if
for every $\bx \in \XX$ and for every $\lambda \in \RR$

$$
T(\lambda \bx) = \lambda T (\bx).
$$
```

```{prf:definition} Positively homogeneous operator
Let $\XX$ and $\YY$ be real vector spaces. 
An operator $T : \XX \to \YY$ is called *positively homogeneous* if
for every $\bx \in \XX$ and for every $\lambda \in \RR_{++}$

$$
T(\lambda \bx) = \lambda T (\bx).
$$
```

```{prf:definition} Additive operator
Let $\XX$ and $\YY$ be real vector spaces. 
An operator $T : \XX \to \YY$ is called *additive* if
for every $\bx,\by \in \XX$

$$
T (\bx + \by) = T(\bx) + T(\by).
$$
```

```{prf:definition} Linear operator
Let $\XX$ and $\YY$ be real vector spaces. 
An operator $T : \XX \to \YY$ is called *linear* if
for every $\bx,\by \in \XX$ and for every $\lambda \in \RR$

$$
T (\lambda \bx + \by) = \lambda T(\bx) + T(\by).
$$
```

```{prf:definition} Affine operator
Let $\XX$ and $\YY$ be real vector spaces. 
An operator $T : \XX \to \YY$ is called *affine* if
for every $\bx,\by \in \XX$ and for every $\lambda \in \RR$

$$
T (\lambda \bx + (1 - \lambda) \by) = \lambda T(\bx) + (1 - \lambda) T(\by).
$$
```


```{prf:remark}
$T$ is affine if and only if the mapping $\bx \mapsto T(\bx) - T(\bzero)$
is linear.
```


## Topology 

If $\VV$ is equipped with a norm $\| \cdot \| : \VV \to \RR$, 
it induces a {prf:ref}`metric <def-ms-distance-function>` 
$d: \VV \times \VV \to \RR$ given by:

$$
d (x, y) = \| x - y \|.
$$

$\VV$ equipped with this metric becomes a 
{prf:ref}`metric space <def-ms-metric-space>`.

The topology of a metric space is discussed in detail in
{ref}`sec:ms:metric-topology` and sections thereafter.

```{prf:definition} Closed unit ball
A ball centered at origin $\bzero \in \VV$ is 
called a *unit ball* if its radius is $1$. 
$B[\bzero, 1]$ denotes a *closed unit ball*
and $(\bzero, 1)$ denotes an *open unit ball*.
```

```{prf:observation}
Following the notation in {prf:ref}`def-vs-set-arithmetic`,
a closed ball can be expressed in terms of closed unit ball as:

$$
B[\bx, r] = \bx + r B[\bzero, 1].
$$

Similarly, any open ball can be expressed in terms of 
the open unit ball as:

$$
B(\bx, r) = \bx + r B(\bzero, 1).
$$
```
