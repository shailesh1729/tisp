(sec:la:inner-product-spaces)=
# Inner Product Spaces

Inner products are a generalization of the notion of dot product.
We restrict our attention to real vector spaces and complex vector spaces.
Thus, the field $\FF$ can be either $\RR$ or $\CC$.

## Inner Product

````{prf:definition} Inner product
:label: def-la-inner-product

An *inner product* over an $\FF$-vector space $\VV$ is any map
$\langle, \rangle : \VV \times \VV \to \FF$
mapping $(\bv_1, \bv_2) \mapsto \langle \bv_1, \bv_2 \rangle$
satisfying following properties:

1. [Positive definiteness]

   $$
    \langle \bv, \bv \rangle \geq 0 \text{  and  } \langle \bv, \bv \rangle = 0 \iff \bv = 0.
   $$
1. [Conjugate symmetry]

   $$
    \langle \bv_1, \bv_2 \rangle = \overline{\langle \bv_2, \bv_1 \rangle} \quad \forall \bv_1, \bv_2 \in \VV.
   $$
*  [Linearity in the first argument]

   $$
    \begin{aligned}
    &\langle \alpha \bv, \bw \rangle = \alpha \langle \bv, \bw \rangle \quad \forall \bv, \bw \in \VV; \forall \alpha \in \FF\\
    &\langle \bv_1 + \bv_2, \bw \rangle = \langle \bv_1, \bw \rangle + \langle \bv_2, \bw \rangle \quad \forall \bv_1, \bv_2,\bw \in \VV
    \end{aligned}
   $$
````

Remarks


* Linearity in first argument extends to any arbitrary linear combination:
  
$$
\left \langle \sum \alpha_i \bv_i, \bw \right \rangle = \sum \alpha_i \langle \bv_i, w \rangle.
$$
* Similarly we have conjugate linearity in second argument for any arbitrary linear combination:
  
$$
\left \langle \bv, \sum \alpha_i \bw_i \right \rangle = \sum \overline{\alpha_i} \langle \bv, \bw_i \rangle.
$$

```{prf:example}
The standard inner product on $\RR^n$ is defined as:

$$
\langle \bx, \by \rangle = \sum_{i=1}^n x_i y_i.
$$

This is often called the *dot product* or *scalar product*.
```

```{prf:example}
The standard inner product on $\CC^n$ is defined as:

$$
\langle \bx, \by \rangle = \sum_{i=1}^n x_i \overline{y_i}.
$$
```

```{prf:example}
Let $\bx, \by \in \RR^2$. Define:

$$
\langle \bx, \by \rangle = x_1 y_1 - x_2 y_1 - x_1 y_2  + 4 x_2 y_2.
$$

Now:

1. $\langle \bx, \bx \rangle = (x_1 - x_2)^2 + 3 x_2^2$.
   Thus, $\bx = \bzero \iff \langle \bx, \bx \rangle = 0$. 
   Thus, it is positive definite.
1. $\langle \by, \bx \rangle = y_1 x_1 - y_2 x_1 - y_1 x_2 + 4 y_2 x_2 = \langle \bx, \by \rangle$.
   It is symmetric.
1. We can also verify that it is linear in the first argument.

Thus, it satisfies all the properties of an inner product. 


Note that, in the matrix notation, we can write this 
inner product as:

$$
\langle \bx, \by \rangle = 
\begin{bmatrix} x_1 & x_2 \end{bmatrix}
\begin{bmatrix} 1 & -1 \\ -1 & 4 \end{bmatrix}
\begin{bmatrix} y_1 \\ y_2 \end{bmatrix}
$$

The matrix

$$
A = \begin{bmatrix} 1 & -1 \\ -1 & 4 \end{bmatrix}
$$
is positive definite.
Its trace is $5$ and its determinant is $3$.
Its eigen values are $4.303, 0.697$.
```

```{prf:example}
Let $\CC^{n \times n}$ be the space of $n \times n$ matrices.
For any $\bA = (a_{ij})$ and $\bB = (b_{ij})$ in $\CC^{n \times n}$,
we define the inner product as:

$$
\langle \bA, \bB \rangle = \sum_{j, k} a_{j k} \overline{b_{j k}}.
$$

It can be easily seen that:

$$
\langle \bA, \bB \rangle = \Trace (\bA \bB^H) = \Trace (\bB^H \bA)
$$
where $\bB^H$ is the conjugate transpose of $\bB$ and $\Trace$ computes
the trace of a matrix (sum of its diagonal values).
```

```{prf:example}
Let $\CC^{n \times 1}$ be the space of column vectors. 
Let $\bQ$ be an arbitrary $n \times n$ invertible matrix over $\CC$. 

For any $\bx, \by \in \CC^{n \times 1}$, define

$$
\langle \bx, \by \rangle  = \by^H \bQ^H \bQ \bx.
$$
We identify the $1 \times 1$ matrix in the R.H.S. with its
single entry as a complex number $\CC$. This is a valid inner product.

When $\bQ = \bI$, the identity matrix, the inner product reduces to:

$$
\langle \bx, \by \rangle  = \by^H \bx.
$$

This is the *standard inner product* on the space of column vectors.
```

```{prf:proposition}
For complex inner products, the inner product is determined identified
by its real part. 
```
```{prf:proof}

Let

$$
\langle \bx, \by \rangle = \Re\langle \bx, \by \rangle + i \Im\langle \bx, \by \rangle.
$$

For any complex number $z = x + i y \in \CC$, we have:

$$
\Re (- i z) = \Re ( -i (x + i y)) = \Re (y - i x) = y = \Im (z).
$$

Since, $\langle \bx, \by \rangle$ is a complex number, hence:

$$
\Im \langle \bx, \by \rangle = \Re (-i \langle \bx, \by \rangle) 
= \Re \langle \bx, i \by \rangle.
$$

Thus,

$$
\langle \bx, \by \rangle = \Re\langle \bx, \by \rangle + i \Re \langle \bx, i \by \rangle.
$$
```

## Real Inner Product

From the perspective of convex analysis, the general inner product is not very useful.
We prefer a special class of inner products whose value is always real.

````{prf:definition} Real inner product
:label: def-la-real-inner-product

A *real inner product* over an $\FF$-vector space $\VV$ is any map
$\langle, \rangle : \VV \times \VV \to \RR$
mapping $(\bv_1, \bv_2) \mapsto \langle \bv_1, \bv_2 \rangle$
satisfying following properties:

1. [Positive definiteness]

   $$
    \langle \bv, \bv \rangle \geq 0 \text{  and  } \langle \bv, \bv \rangle = 0 \iff \bv = 0.
   $$
1. [Symmetry]

   $$
    \langle \bv_1, \bv_2 \rangle = \langle \bv_2, \bv_1 \rangle \quad \forall \bv_1, \bv_2 \in \VV.
   $$
*  [Linearity in the first argument]

   $$
    \begin{aligned}
    &\langle \alpha \bv, \bw \rangle = \alpha \langle \bv, \bw \rangle \quad \forall \bv, \bw \in \VV; \forall \alpha \in \FF\\
    &\langle \bv_1 + \bv_2, \bw \rangle = \langle \bv_1, \bw \rangle + \langle \bv_2, \bw \rangle \quad \forall \bv_1, \bv_2,\bw \in \VV
    \end{aligned}
   $$
````

* Real inner product is always real valued no matter whether  the scalar field is real or complex.
* Since the real inner product is symmetric, hence since it is linear in first argument,
  it is linear in second argument too.

$$
\left \langle \bv, \sum \alpha_i \bw_i \right \rangle = \sum \alpha_i \langle \bv, \bw_i \rangle.
$$


```{prf:example}
Let $z_1, z_2$ be complex numbers:

$$
z_1 \overline{z_2} = (a_1 + i b_1) (a_2 - i b_2) = a_1 a_2 + b_1 b_2 + i (b_1 a_2 - a_1 b_2).
$$

Then

$$
\Re (z_1 \overline{z_2}) = a_1 a_2 + b_1 b_2.
$$

1. $\Re (z \overline{z}) = x^2 + y^2$ is positive definite;
   i.e., $\Re (z \overline{z}) = 0 \iff z = 0 + i 0$.
1. $\Re (z_1 \overline{z_2}) = \Re (z_2 \overline{z_1})$ is symmetric.
1. For any $\alpha \in \RR$ $\Re (\alpha z_1 \overline{z_2}) = \alpha \Re (z_1 \overline{z_2})$.
   Thus, it is linear in first argument.

Now, for any $\bx, \by \in \CC^n$, define:

$$
\langle \bx, \by \rangle = \Re \left ( \sum_{i=1}^n x_i \overline{y_i} \right ).
$$

Following the argument above, it is a real inner product on $\CC^n$.

Interestingly, if $\bu \in \CC^n$ is identified with $\bv \in \RR^{2 n}$ by
stacking the real and imaginary parts, then the real inner product 
defined above for $\CC^n$ is nothing but the standard inner product for
$\RR^{2 n}$.
```


While the presentation in rest of the section will be based on the
general conjugate symmetric inner product, it will be easy to 
extrapolate the results for the special case of real inner products.

## Orthogonality

````{prf:definition} Orthogonal vectors
:label: def-la-orthogonal-vectors

A set of non-zero vectors $\{\bv_1, \dots, \bv_p\}$ is called *orthogonal* if

$$
     \langle \bv_i, \bv_j  \rangle = 0  \text{ if } i \neq j \quad \forall 1 \leq i, j \leq p.
$$
````

````{prf:definition} Orthonormal vectors
:label: def-la-orthonormal-vectors

A set of non-zero vectors $\{\bv_1, \dots, \bv_p\}$ is called *orthonormal* if

$$
\begin{aligned}
 &\langle \bv_i, \bv_j  \rangle = 0  \text{ if } i \neq j \quad \forall 1 \leq i, j \leq p\\
 &\langle \bv_i, \bv_i  \rangle = 1  \quad \forall 1 \leq i \leq p
\end{aligned} \, .
$$

i.e. $\langle \bv_i, \bv_j  \rangle = \delta(i, j)$.
````

Remarks:

*  A set of orthogonal vectors is linearly independent.


````{prf:definition} Inner product space / Pre-Hilbert space
:label: def-la-pre-hilbert-space

An $\FF$-vector space $\VV$ equipped with an inner product 
$\langle, \rangle : \VV \times \VV \to \FF$ is known
as an *inner product space* or a *pre-Hilbert space*.
````



## Projection


````{prf:definition}
:label: def-la-projection

A *projection* is a linear transformation $P$ from a 
vector space $\VV$ to itself such that $P^2=P$;
i.e., if $ P \bv = \bx$, then $P \bx = \bx$. 
````

```{prf:remark}
Whenever $P$ is applied twice (or more) to any vector, 
it gives the same result as if it was applied once.

Thus, $P$ is an *idempotent* operator.
```

````{prf:example} Projection operators

Consider the operator $P : \RR^3 \to \RR^3$ defined as

$$
P = \begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}.
$$

Then application of $P$ on any arbitrary vector is given by

$$
P
\begin{pmatrix}
x \\ y \\z
\end{pmatrix}
=
\begin{pmatrix}
x \\ y \\ 0
\end{pmatrix}
$$

A second application doesn't change it

$$
P
\begin{pmatrix}
x \\ y \\0
\end{pmatrix}
=
\begin{pmatrix}
x \\ y \\ 0
\end{pmatrix}
$$

Thus $P$ is a projection operator.

Often, we can directly verify the property by computing $P^2$ as

$$
P^2 = \begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}
= \begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0 \\
0 & 0 & 0
\end{bmatrix}
= P.
$$
````


## Orthogonal Projection

Consider a projection operator $P : \VV \to \VV$ 
where $\VV$ is an inner product space.

The range of $P$ is given by

$$
\Range(P) = \{\bv \in \VV \ST \bv =  P \bx \text{ for some } \bx \in \VV \}.
$$
The null space of $P$ is given by

$$
\NullSpace(P) = \{ \bv \in \VV | P \bv = \bzero\}.
$$


````{prf:definition}
:label: def-la-orthogonal-projector

A projection operator $P : \VV \to \VV$
over an inner product space $\VV$ 
is called *orthogonal projection operator*
if its range $\Range(P)$ and the null space 
$\NullSpace(P)$ as defined above are orthogonal to each other; 
i.e.

$$
\langle \br, \bn \rangle = \bzero \Forall \br \in \Range(P) , \Forall \bn \in \NullSpace(P).
$$
````

````{prf:proposition}
A projection operator is orthogonal if and only if it is self adjoint.
````


````{prf:example} Orthogonal projection on a line
Consider a unit norm vector $\bu \in \RR^N$.  
Thus $\bu^T \bu = 1$.

Consider

$$
P_{\bu} = \bu \bu^T.
$$

Now

$$
P_{\bu}^2 = (\bu \bu^T) (\bu \bu^T) = \bu (\bu^T \bu) \bu^T = \bu \bu^T = P.
$$

Thus $P$ is a projection operator.

Now,

$$
P_{\bu}^T = (\bu \bu^T)^T = \bu \bu^T = P_{\bu}.
$$

Thus $P_{\bu}$ is self-adjoint. 
Hence, $P_{\bu}$ is an orthogonal projection operator.

Also,

$$
P_{\bu} \bu = (\bu \bu^T) \bu = \bu (\bu^T \bu) = \bu.
$$

Thus $P_{\bu}$ leaves $\bu$ intact;
i.e., Projection of $\bu$ on to $\bu$ is $\bu$ itself.

Let $\bv \in \bu^{\perp}$ i.e. $\langle \bu, \bv \rangle = 0$.

Then,

$$
P_{\bu} \bv = (\bu \bu^T) \bv = \bu (\bu^T \bv) = \bu \langle \bu, \bv \rangle = 0.
$$

Thus $P_{\bu}$ annihilates all vectors orthogonal to $\bu$.

Any vector $\bx \in \RR^N$ can be broken down into two components

$$
\bx = \bx_{\parallel} + \bx_{\perp}
$$
such that
$\langle \bu , \bx_{\perp} \rangle =0$
and $\bx_{\parallel}$ is collinear with $\bu$.

Then,

$$
P_{\bu} \bx = \bu \bu^T \bx_{\parallel} + \bu \bu^T \bx_{\perp} = \bx_{\parallel}.
$$

Thus $P_{\bu}$ retains the projection of $\bx$ on $\bu$ given by $\bx_{\parallel}$.
````

````{prf:example} Projections over the column space of a matrix

Let $\bA \in \RR^{M \times N}$  with $N \leq M$ be a matrix given by

$$
\bA = \begin{bmatrix}
\ba_1 & \ba_2 & \dots & \ba_N
\end{bmatrix}
$$

where $\ba_i \in \RR^M $ are its columns which are linearly independent.

The column space of $\bA$ is given by

$$
C(\bA) = \{ \bA \bx \Forall \bx \in \RR^N \} \subseteq \RR^M.
$$

It can be shown that $\bA^T \bA$ is invertible.

Consider the operator

$$
P_{\bA} = \bA (\bA^T \bA)^{-1} \bA^T.
$$

Now,

$$
P_{\bA}^2 = \bA (\bA^T \bA)^{-1} \bA^T \bA (\bA^T \bA)^{-1} \bA^T = \bA (\bA^T \bA)^{-1} \bA^T = P_{\bA}.
$$

Thus $P_{\bA}$ is a projection operator.

$$
P_{\bA}^T = (\bA (\bA^T \bA)^{-1} \bA^T)^T = \bA ((\bA^T \bA)^{-1} )^T \bA^T = \bA (\bA^T \bA)^{-1} \bA^T = P_{\bA}.
$$

Thus $P_{\bA}$ is self-adjoint.

Hence $P_{\bA}$ is an orthogonal projection operator on the column space of $\bA$.
````



## Parallelogram Identity

````{prf:theorem} Parallelogram identity
:label: res-la-parallelogram-identity

$$
2 \| \bx \|_2^2 + 2 \| \by \|_2^2 =  \|\bx + \by \|_2^2 + \| \bx - \by \|_2^2.  \Forall  \bx, \by \in \VV.
$$
````

````{prf:proof}
Expanding:

$$
\| \bx + \by \|_2^2 = \langle \bx + \by, \bx + \by \rangle
= \langle \bx, \bx \rangle + \langle \by , \by \rangle + \langle \bx , \by \rangle + \langle \by , \bx \rangle.
$$

Also:

$$
\| \bx - \by \|_2^2 = \langle \bx - \by, \bx - \by \rangle
= \langle \bx, \bx \rangle + \langle \by , \by \rangle - \langle \bx , \by \rangle - \langle \by , \bx \rangle.
$$

Thus,

$$
\|\bx + \by \|_2^2 + \| \bx - \by \|_2^2 = 2 (  \langle \bx, \bx \rangle + \langle \by , \by\rangle)
= 2 \| \bx \|_2^2 + 2 \| \by \|_2^2.
$$
````
When inner product is a real number following identity is quite useful.

````{prf:theorem} Parallelogram identity for real inner product
:label: res-la-parallelogram-identity-2

$$
\langle \bx, \by \rangle = \frac{1}{4} \left (
\|\bx + \by \|_2^2 - \| \bx - \by \|_2^2
\right ).  \Forall  \bx, \by \in \VV.
$$
````

````{prf:proof}
Expanding:

$$
\| \bx + \by \|_2^2 = \langle \bx + \by, \bx + \by \rangle
= \langle \bx, \bx \rangle + \langle \by , \by \rangle + \langle \bx , \by \rangle + \langle \by , \bx \rangle.
$$

Also,

$$
\| \bx - \by \|_2^2 = \langle \bx - \by, \bx - \by \rangle
= \langle \bx, \bx \rangle + \langle \by , \by \rangle - \langle \bx , \by \rangle - \langle \by , \bx \rangle.
$$

Thus,

$$
\|\bx + \by \|_2^2 - \| \bx - \by \|_2^2 = 2 ( \langle \bx , \by \rangle + \langle \by , \bx \rangle)
= 4 \langle \bx , \by \rangle
$$
since for real inner products

$$
 \langle \bx , \by \rangle = \langle \by , \bx \rangle.
$$
````


## Polarization identity
When inner product is a complex number, polarization identity is quite useful.

````{prf:theorem} Polarization identity for complex inner product
:label: res-la-polarization-identity

$$
\langle \bx, \by \rangle = \frac{1}{4} \left (
\|\bx + \by \|_2^2 - \| \bx - \by \|_2^2 + i \| \bx + i \by \|_2^2 - i \| \bx -i \by \|_2^2
\right )  \Forall  \bx, \by \in \VV.
$$
````

````{prf:proof}
Expanding

$$
\| \bx + \by \|_2^2 = \langle \bx + \by, \bx + \by \rangle
= \langle \bx, \bx \rangle + \langle \by , \by \rangle + \langle \bx , \by \rangle + \langle \by , \bx \rangle.
$$

Also,

$$
\| \bx - \by \|_2^2 = \langle \bx - \by, \bx - \by \rangle
= \langle \bx, \bx \rangle + \langle \by , \by \rangle - \langle \bx , \by \rangle - \langle \by , \bx \rangle.
$$

And,

$$
\| \bx + i \by \|_2^2 = \langle \bx + i \by, \bx + i \by \rangle
= \langle \bx, \bx \rangle + \langle i \by , i \by \rangle + \langle \bx , i \by \rangle + \langle i \by , \bx \rangle.
$$

And,

$$
\| \bx - i \by \|_2^2 = \langle \bx - i \by, \bx - i \by \rangle
= \langle \bx, \bx \rangle + \langle i \by , i \by \rangle - \langle \bx , i \by \rangle - \langle i \by , \bx \rangle.
$$

Thus,

$$
 \|\bx + \by \|_2^2 - \| \bx - \by \|_2^2 + & i \| \bx + i \by \|_2^2 - i \| \bx -i \by \|_2^2\\
&= 2 \langle \bx, \by \rangle + 2 \langle \by , \bx \rangle + 2 i  \langle \bx , i \by \rangle + 2 i  \langle i\bx , \by \rangle\\
&= 2 \langle \bx, \by \rangle + 2 \langle \by , \bx \rangle + 2 \langle \bx, \by \rangle - 2  \langle \by , \bx \rangle\\
& = 4  \langle \bx, \by \rangle.
$$
````

