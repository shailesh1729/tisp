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


````{prf:definition} Pre-Hilbert space
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

