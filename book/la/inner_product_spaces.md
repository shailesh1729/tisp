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

```{prf:theorem} Scaling in second argument
:label: res-la-ip-scaling-second

Let $\langle \cdot, \cdot \rangle : \VV \times \VV \to \FF$ be an inner product.
Then

$$
\langle \bv, \alpha \bw \rangle =  \overline{\alpha} \langle \bv, \bw \rangle.
$$
```

```{prf:proof}
We proceed as follows:

$$
\langle \bv, \alpha \bw \rangle = \overline{\langle \alpha \bw, \bv \rangle}
= \overline{\alpha \langle  \bw, \bv \rangle}
= \overline{\alpha}\overline{\langle  \bw, \bv \rangle}
= \overline{\alpha}\langle \bv, \bw \rangle.
$$
```

```{prf:theorem} Distribution in second argument
:label: res-la-ip-dist-second

Let $\langle \cdot, \cdot \rangle : \VV \times \VV \to \FF$ be an inner product.
Then for any $\bv, \bx, \by \in \VV$:

$$
\langle \bv, \bx + \by \rangle = \langle \bv, \bx \rangle + \langle \bv, \by \rangle.
$$
```

```{prf:proof}
We proceed as follows:

$$
\langle \bv, \bx + \by \rangle = \overline{\langle \bx + \by , \bv \rangle}
= \overline{\langle \bx, \bv \rangle + \langle \by, \bv \rangle}
= \overline{\langle \bx, \bv \rangle} + \overline{\langle \by, \bv \rangle}
= \langle \bv, \bx \rangle + \langle \bv, \by \rangle.
$$

```


```{prf:theorem} Inner product with zero
:label: res-la-ip-product-with-zero

Let $\langle \cdot, \cdot \rangle : \VV \times \VV \to \FF$ be an inner product.
Then,

$$
\langle \bzero , \bv \rangle  = \langle \bv , \bzero \rangle = 0 \Forall \bv \in \VV.
$$
```

```{prf:proof}
We proceed as follows:

$$
\langle \bu , \bv \rangle = \langle \bu + \bzero , \bv \rangle
= \langle \bu , \bv \rangle + \langle \bzero , \bv \rangle.
$$

By cancelling terms, we get:

$$
\langle \bzero , \bv \rangle = 0.
$$

Using the conjugate symmetry, we get:

$$
\langle \bv , \bzero \rangle = \overline{\langle \bzero , \bv \rangle}
= \overline{0} = 0.
$$
```



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

```{prf:theorem}
:label: res-la-ip-complex-real-part

For complex inner products, the inner product is determined identified
by its real part. 
```

This statement may be confusing. Let us unpack what it means.
Let

$$
\langle \bx, \by \rangle = \Re\langle \bx, \by \rangle + i \Im\langle \bx, \by \rangle.
$$

Then, computing the inner product involves computing the
real part as well as computing the complex part. 
What the statement means is that, if we know how to 
compute $\Re\langle \bx, \by \rangle$ for any
$\bx, \by \in \VV$, then, we can use the same
method to compute  $\Im\langle \bx, \by \rangle$
too; but using different inputs. See below.

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
This is applicable on vector spaces where the field of scalars is
$\RR$.

````{prf:definition} Real inner product
:label: def-la-real-inner-product

A *real inner product* over an $\RR$-vector space $\VV$ is any map
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
    &\langle \alpha \bv, \bw \rangle = \alpha \langle \bv, \bw \rangle \quad \forall \bv, \bw \in \VV; \forall \alpha \in \RR\\
    &\langle \bv_1 + \bv_2, \bw \rangle = \langle \bv_1, \bw \rangle + \langle \bv_2, \bw \rangle \quad \forall \bv_1, \bv_2,\bw \in \VV
    \end{aligned}
   $$
````

* Real inner product is always real valued no matter whether  the 
  vectors are real or complex.
* Since the real inner product is symmetric, hence since it is linear in first argument,
  it is linear in second argument too.

$$
\left \langle \bv, \sum \alpha_i \bw_i \right \rangle = \sum \alpha_i \langle \bv, \bw_i \rangle.
$$


```{prf:example} A real inner product for $\CC^n$ over $\RR$
In this example, we are dealing with $n$-tuples of complex numbers
in $\CC^n$ with the field of scalars being $\RR$.
It can be easily checked that $\CC^n$ over $\RR$ is a 
vector space.

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

## Inner Product Space

````{prf:definition} Inner product space / Pre-Hilbert space
:label: def-la-pre-hilbert-space

An $\FF$-vector space $\VV$ equipped with an inner product 
$\langle, \rangle : \VV \times \VV \to \FF$ is known
as an *inner product space* or a *pre-Hilbert space*.
````



## Orthogonality

Orthogonality is the generalization of the notion of
perpendicularity from elementary geometry.

```{prf:definition} Orthogonal vectors
:label: def-la-orthogonal-pair

Any two vectors $\bu , \bv \in \VV$ are called *orthogonal* to each other
if  $\langle \bu, \bv \rangle = 0$. 

We write $\bu \perp \bv$ if $\bu$ and $\bv$ are orthogonal to each other.
```


````{prf:definition} Set of orthogonal vectors
:label: def-la-orthogonal-vectors

A set of non-zero vectors $\{\bv_1, \dots, \bv_p\}$ is called *orthogonal*
or *pairwise orthogonal* if

$$
     \langle \bv_i, \bv_j  \rangle = 0  \text{ if } i \neq j \quad \forall 1 \leq i, j \leq p.
$$
````

```{prf:theorem} Orthogonality implies independence
:label: res-la-ip-orthogonal-independent

A set of orthogonal vectors is linearly independent.
```

```{prf:proof}
Let $\bv_1, \dots \bv_n$ be a set of orthogonal vectors. 
Suppose there is a linear combination:

$$
\alpha_1 \bv_1 + \dots + \alpha_n \bv_n = \bzero.
$$

Taking inner product on both sides with $\bv_j$, we get:

$$
\begin{aligned}
& \langle \alpha_1 \bv_1 + \dots + \alpha_n \bv_n, \bv_j \rangle = \langle \bzero , \bv_j \rangle\\
&\iff 0 + \dots + \alpha_j \langle \bv_j, \bv_j \rangle + \dots + 0 = 0\\
&\iff \alpha_j \langle \bv_j, \bv_j \rangle = 0\\
&\iff \alpha_j =  0.
\end{aligned}
$$

Thus, the only zero linear combination is the trivial combination.
Thus, the vectors are linearly independent.
```

## Norm Induced by Inner Product

```{prf:definition} Norm induced by inner product
:label: def-la-ip-induced-norm

Every inner product $\langle \cdot, \cdot \rangle : \VV \times \VV \to \FF$ 
on a vector space $\VV$
induces a {prf:ref}`norm <def-la-norm>`  $\| \cdot \| : \VV \to \RR$ 
given by:

$$
\| \bv \| = \sqrt{\langle \bv , \bv \rangle} \Forall \bv \in \VV.
$$
```

We shall justify that this function satisfies all the properties of a norm
later. But before that, let us examine some implications of this definition
which are useful in their own right.

Note that it is easy to see that $\| \cdot \|$ is positive definite;
i.e., $\| \bzero \| = 0$ and $\| \bv \| > 0$ if $\bv \neq \bzero$.

Also, it is positively homogeneous, since:

$$
\| \alpha \bv \|  = \sqrt{\langle \alpha \bv , \alpha \bv \rangle}
= \sqrt{\alpha \overline{\alpha} \langle \bv, \bv \rangle} 
= |\alpha| \sqrt{\langle \bv, \bv \rangle} = |\alpha| \| \bv \|.
$$

```{prf:theorem} Pythagoras theorem
:label: res-la-ip-pythagoras

If $\bu \perp \bv$ then

$$
\| \bu + \bv \|^2 = \| \bu \|^2 + \| \bv \|^2.
$$
```

```{prf:proof}
Expanding:

$$
\| \bu + \bv \|^2 = \langle \bu + \bv , \bu + \bv \rangle 
= \langle \bu, \bu \rangle + \langle \bu, \bv \rangle + \langle \bv, \bu \rangle + \langle \bv, \bv \rangle
= \| \bu \|^2 + \| \bv \|^2  
$$
where we used the fact that: $\langle \bu, \bv \rangle = \langle \bv, \bu \rangle = 0$
since  $\bu \perp \bv$.
```

```{prf:theorem} Cauchy Schwartz inequality
:label: res-la-ip-cauchy-chwartz-inequality

For any $\bu, \bv \in \VV$:

$$
| \langle \bu, \bv \rangle | \leq \| \bu \| \| \bv \|.
$$
The equality holds if and only if $\bu$ and $\bv$ are linearly dependent.
```

```{prf:proof}
If either $\bu = \bzero$ or $\bv = \bzero$ then the equality holds.
So, suppose that neither of them are zero vectors.
In particular $\bv \neq \bzero$ means $\| \bv \| > 0$.

Define 

$$
\bw = \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \bv.
$$

Then,

$$
\begin{aligned}
\langle \bw, \bu - \bw \rangle &= 
\left \langle \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \bv, 
\bu  - \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \bv \right \rangle\\
&= \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \left \langle \bv, 
\bu  - \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \bv \right \rangle\\
&= \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \left ( 
\langle \bv, \bu \rangle - 
\left \langle \bv, \bv \right \rangle
\right )\\
&= \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \left ( 
\langle \bv, \bu \rangle - 
\frac{\overline{\langle \bu, \bv \rangle}}{\| \bv \|^2}  \langle \bv, \bv \rangle \right )\\
&= \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \left ( 
\langle \bv, \bu \rangle - 
\frac{\langle \bv, \bu \rangle}{\| \bv \|^2}  \| \bv \|^2 \right )\\
&= 0.
\end{aligned}
$$

Thus, $\bw \perp \bu - \bw$. Therefore, by Pythagorean theorem,

$$
\begin{aligned}
\| \bu \|^2 &= \| \bu - \bw + \bw \|^2\\
&=  \| \bu - \bw \|^2 + \| \bw \|^2\\
&\geq \| \bw \|^2\\
&= \left \| \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \bv \right \|^2\\
&= \left | \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \right |^2 \| \bv \|^2\\
&= \frac{|\langle \bu, \bv \rangle|^2}{\| \bv \|^2}.
\end{aligned}
$$

Multiplying on both sides by $\| \bv \|^2$, we obtain:

$$
\| \bu \|^2 \| \bv \|^2 \geq |\langle \bu, \bv \rangle|^2.
$$

Taking square roots on both sides, 

$$
|\langle \bu, \bv \rangle| \leq \| \bu \| \| \bv \|.
$$

In the derivation above, the equality holds if and only if

$$
\bzero = \bu - \bw = \bu - \frac{\langle \bu, \bv \rangle}{\| \bv \|^2} \bv
$$
which means that $\bu$ and $\bv$ are linearly dependent.

Conversely, if $\bu$ and $\bv$ are linearly dependent, then
$\bu = \alpha \bv$ for some $\alpha \in \FF$, and

$$
\bw = \frac{\langle \alpha \bv, \bv \rangle}{\| \bv \|^2}\bv
=\frac{\alpha \langle \bv, \bv \rangle}{\| \bv \|^2}\bv
= \alpha \bv = \bu
$$
giving us $\bu - \bw = \bzero$. Hence, the equality holds.
```


```{prf:theorem} Inner product induced norm justification
:label: res-la-ip-induced-norm-valid

The function $\| \cdot \| : \VV \to \RR$ induced by the inner product
$\langle \cdot, \cdot \rangle : \VV \times \VV \to \FF$ as defined in
{prf:ref}`def-la-ip-induced-norm` is indeed a norm.
```

```{prf:proof}
We need to verify that $\| \cdot \|$ so defined is indeed a norm.
We have already shown that it is positive definite and positive homogeneous.
We now show the triangle inequality. We will take help of the
Cauchy Schwartz inequality shown above:

$$
\begin{aligned}
\| \bu + \bv \|^2 
&= \langle \bu + \bv , \bu + \bv \rangle\\ 
&= \langle \bu, \bu \rangle + \langle \bu, \bv \rangle + \langle \bv, \bu \rangle + \langle \bv, \bv \rangle\\
&= \| \bu \|^2 + \langle \bu, \bv \rangle + \overline{\langle \bu, \bv \rangle} + \| \bv \|^2\\  
&= \| \bu \|^2 + 2\Re\langle \bu, \bv \rangle + \| \bv \|^2\\  
&\leq \| \bu \|^2 + 2|\langle \bu, \bv \rangle| + \| \bv \|^2\\
&\leq \| \bu \|^2 + 2\|\bu\|\|\bv\| + \| \bv \|^2\\
&=(\| \bu \| + \| \bv \|)^2.
\end{aligned}
$$

Taking square root on both sides, we obtain:

$$
\| \bu + \bv \| \leq \| \bu \| + \| \bv \|.
$$
Thus, $\| \cdot \|$ is indeed a norm.
```
We recap the sequence of results to emphasize the logical flow:

1. We started with just the definition of $\| \cdot \|$ in {prf:ref}`def-la-ip-induced-norm`.
1. We proved positive definiteness from the definition itself.
1. We proved positive homogeneity also from the definition itself.
1. We proved Pythagoras theorem utilizing previously established results for inner products.
1. We proved Cauchy Schwartz inequality using positive definiteness,
   positive homogeneity and Pythagoras theorem.
1. We proved triangle inequality using Cauchy Schwartz inequality.

```{prf:theorem} Inner product space to metric space
:label: res-la-ip-implies-norm-metric

Every inner product space is a normed space. Hence it is also a metric space.
```

```{prf:proof}
An inner product induces a norm which makes the vector space a normed space.
A norm induces a metric which makes the vector space a metric space.
```

## Hilbert Spaces

```{prf:definition} Hilbert space
:label: def-la-ip-hilbert-space

An inner product space $\VV$ that is
{prf:ref}`complete <def-ms-complete-metric-space>`
with respect to the metric induced by the norm
induced by its inner product
is called a *Hilbert space*.

In other words, $\VV$ is a Hilbert space if
every Cauchy sequence of $\VV$ converges in $\VV$.
```

## Orthonormality

````{prf:definition} Set of orthonormal vectors
:label: def-la-orthonormal-vectors

A set of non-zero vectors $\{\be_1, \dots, \be_p\}$ is called *orthonormal* if

$$
\begin{aligned}
 &\langle \be_i, \be_j  \rangle = 0  \text{ if } i \neq j \quad \forall 1 \leq i, j \leq p\\
 &\langle \be_i, \be_i  \rangle = 1  \quad \forall 1 \leq i \leq p
\end{aligned} \, ;
$$
i.e., $\langle \be_i, \be_j  \rangle = \delta(i, j)$.

In other words, the vectors are unit norm ($\| \be_i \| = 1$) and are
pairwise orthogonal ($\be_i \perp \be_j)$ whenever $i \neq j$).
````

Since orthonormal vectors are orthogonal, hence they are linearly independent.

```{prf:definition} Orthonormal basis
A set of orthonormal vectors form an *orthonormal basis* for their span.
```


```{prf:theorem} Expansion of a vector in an orthonormal basis
:label: res-la-ip-onb-expansion

Let $\{\be_1, \dots, \be_n\}$  be an orthonormal basis for $\VV$.
Then, any $\bv \in \VV$ can be written as:

$$
\bv = \langle \bv, \be_1 \rangle \be_1 + \dots +  \langle \bv, \be_n \rangle \be_n.
$$
```


```{prf:proof}
Since $\{\be_1, \dots, \be_n\}$ forms a basis for $\VV$,
hence every every $\bv \in \VV$ can be written as:

$$
\bv = \alpha_1 \be_1 + \dots + \alpha_n \be_n
$$
where $\alpha_1, \dots, \alpha_n \in \FF$.

Taking inner product with $\be_j$ on both sides, we get:


$$
\langle \bv, \be_j \rangle = \alpha_1 \langle \be_1, \be_j \rangle + \dots + \alpha_n \langle \be_n, \be_j \rangle.
$$

Since $\langle \be_i, \be_j \rangle = \delta(i, j)$, 
hence the above reduces to:

$$
\langle \bv, \be_j \rangle = \alpha_j.
$$
```


```{prf:theorem} Norm of a vector in an orthonormal basis
:label: res-la-ip-onb-norm

Let $\{\be_1, \dots, \be_n\}$  be an orthonormal basis for $\VV$.
For any $\bv \in \VV$, let its expansion in the orthonormal basis be:

$$
\bv = \alpha_1 \be_1 + \dots + \alpha_n \be_n.
$$

Then,

$$
\| \bv \|^2 = | \alpha_1|^2 + \dots + | \alpha_n|^2 = \sum_{i=1}^n |\alpha_i|^2.
$$
```

```{prf:proof}
Expanding the expression for norm squared:

$$
\| \bv \|^2 = \langle \bv , \bv \rangle 
= \langle \alpha_1 \be_1 + \dots + \alpha_n \be_n, \alpha_1 \be_1 + \dots + \alpha_n \be_n \rangle
= \sum_{i=1}^n \sum_{j = 1}^n \langle \alpha_i \be_i , \alpha_j \be_j \rangle
= \sum_{i=1}^n | \alpha_i|^2.
$$
```

Here are some interesting questions:

* Can a basis in an inner product space be converted into an orthonormal basis?
* Does a finite dimensional inner product space have an orthonormal basis? 
* Does every finite dimensional subspace of an inner product space have an
  orthonormal basis? 

The answer to these questions is yes. 
We provide a constructive answer by the Gram-Schmidt algorithm described
in the next section.

## The Gram-Schmidt Algorithm

The Gram-Schmidt algorithm (described below) can construct 
an orthonormal basis from an arbitrary basis for the
span of the basis.

```{prf:algorithm} The Gram-Schmidt algorithm

**Inputs** $\bv_1, \bv_2, \dots, \bv_n$, a set of linearly independent vectors

**Outputs** $\be_1, \be_2, \dots, \be_n$, a set of orthonormal vectors

1. $\bw_1 = \bv_1$.
1. $\be_1 = \frac{\bw_1}{\| \bw_1 \|}$.
1. For $j=2, \dots, n$:
   1. $\bw_j = \bv_j - \sum_{i=1}^{j-1} \langle \bv_j, \be_i \rangle \be_i$.
   1. $\be_j = \frac{\bw_j}{\| \bw_j \|}$.
```

```{prf:theorem} Justification for Gram-Schmidt algorithm
:label: res-la-gram-schmidt-correctness

Let $\bv_1, \bv_2, \dots, \bv_n$ be linearly independent.
The Gram-Schmidt algorithm described above generates a set of orthonormal vectors.

Moreover, for each $j = 1, \dots, n$, the set $\be_1, \dots, \be_j$
is an orthonormal basis for the subspace: $\span \{\bv_1, \dots, \bv_j \}$.
```


```{prf:proof}
We prove this by mathematical induction.
Consider the base case for $j=1$. 

1. $\bw_1 = \bv_1$. 
1. $\be_1 = \frac{\bw_1}{\| \bw_1 \|} = \frac{\bv_1}{\| \bv_1 \|}$.
1. Thus, $\| \be_1 \| = 1$. 
1. $\span \{ \be_1 \} = \span \{ \bv_1 \}$ because $\be_1$ is a nonzero scalar multiple of $\bv_1$.


Now, assume that the set $\be_1, \dots, \be_{j-1}$
is an orthonormal basis for $\span \{\bv_1, \dots, \bv_{j-1} \}$.

1. Thus, $\span \{\be_1, \dots, \be_{j-1} \} = \span \{\bv_1, \dots, \bv_{j-1} \}$.
1. Since $\bv_j$ is linearly independent from $\bv_1, \dots, \bv_{j-1}$, hence
   $\bv_j \notin \span \{\bv_1, \dots, \bv_{j-1} \}$.
1. Thus, $\bv_j \notin \span \{\be_1, \dots, \be_{j-1} \}$.
1. Hence, $\bw_j = \bv_j - \sum_{i=1}^{j-1} \langle \bv_j, \be_i \rangle \be_i \neq \bzero$.
   If it was $\bzero$, then $\bv_j$ would be linearly dependent on $\be_1, \dots, \be_{j-1}$.
1. Thus, $\| \bw_j \| > 0$.
1. Thus, $\be_j = \frac{\bw_j}{\| \bw_j \|}$ is well-defined.
1. Also, $\| \be_j \| = 1$ by construction, thus, $\be_j$ is unit-norm.
1. Note that $\bw_j$ is orthogonal to $\be_1, \dots, \be_{j-1}$.
   For any $1 \leq k < j$, we have:

   $$
   \begin{aligned}
   \langle \bw_j, \be_k \rangle &= \left \langle 
   \bv_j - \sum_{i=1}^{j-1} \langle \bv_j, \be_i \rangle \be_i, 
   \be_k \right \rangle\\
   &= \langle \bv_j \be_k \rangle - \sum_{i=1}^{j-1} 
   \langle \bv_j, \be_i \rangle \langle \be_i, \be_k \rangle\\
   &= \langle \bv_j \be_k \rangle - \langle \bv_j, \be_k \rangle \langle \be_k, \be_k \rangle\\
   &= \langle \bv_j \be_k \rangle - \langle \bv_j, \be_k \rangle = 0.
   \end{aligned}
   $$
   since $\be_1, \dots, \be_{j-1}$ are orthonormal.
1. Thus, for any $1 \leq k < j$:

   $$
   \langle \be_j, \be_k \rangle 
   = \left \langle \frac{\bw_j}{\| \bw_j \|}, \be_k \right \rangle
   = \frac{\langle \bw_j, \be_k \rangle}{\| \bw_j \|}
   = 0.
   $$
1. Thus, $\be_j$ is orthogonal to $\be_1, \dots, \be_{j-1}$.
1. Since, all of them are unit norm, hence, $\be_1, \dots, \be_{j-1}, \be_j$ are
   indeed orthonormal.

We also need to show that $\span \{\be_1, \dots, \be_{j} \} = \span \{\bv_1, \dots, \bv_{j} \}$.

1. Note that $\bw_j \in \span \{\bv_j, \be_1, \dots, \be_{j-1} \} = \span \{\bv_1, \dots, \bv_j \}$
   since $\span \{\be_1, \dots, \be_{j-1} \} = \span \{\bv_1, \dots, \bv_{j-1} \}$
   by inductive hypothesis.
1. Thus, $\be_j \in \span \{\bv_1, \dots, \bv_j \}$
   since $\be_j$ is just scaled $\bw_j$.
1. Thus, $\span \{\be_1, \dots, \be_{j} \} \subseteq \span \{\bv_1, \dots, \bv_{j} \}$.
1. For the converse, by definition $\bv_j = \bw_j + \sum_{i=1}^{j-1} \langle \bv_j, \be_i \rangle \be_i$.
1. Hence, $\bv_j \in \span \{\bw_j,  \be_1, \dots, \be_{j-1}\} = \span \{\be_1, \dots, \be_{j} \}$.
1. Thus, $\span \{\bv_1, \dots, \bv_{j} \} \subseteq \span \{\be_1, \dots, \be_{j} \}$.
1. Thus, $\span \{\be_1, \dots, \be_{j} \} = \span \{\bv_1, \dots, \bv_{j} \}$ must be true.
```

```{prf:theorem} Existence of orthonormal basis
:label: res-la-ip-finite-onb-existence

Every finite dimensional inner product space has an orthonormal basis.
```

```{prf:proof}
This is a simple application of the Gram-Schmidt algorithm.

1. Every finite dimensional vector space has a finite basis.
1. Every finite basis can be turned into an orthonormal basis by
   the {prf:ref}`Gram-Schmidt algorithm <res-la-gram-schmidt-correctness>`.
1. Thus, we have an orthonormal basis.
```

```{prf:corollary} 
:label: res-la-ip-finite-subspace-onb-existence

Every finite dimensional subspace of an inner product space has an orthonormal basis.
```


## Orthogonal Complements

```{prf:definition} Orthogonal complement
:label: def-la-orthogonal-complement

Let $S$ be a subset of an inner product space $\VV$. 
The *orthogonal complement* of $S$ is the set of all vectors in $\VV$ that are
orthogonal to every element of $S$. It is denoted by $S^{\perp}$.

$$
S^{\perp} \triangleq \{\bv \in \VV \ST \bv \perp \bs \Forall \bs \in S \}.
$$
```

```{prf:definition} Orthogonal complement of a vector
:label: def-la-orthogonal-complement-vector

Let $\ba \in \VV$. 
The *orthogonal complement* of $\ba$ is
the set of all vectors in $\VV$ that are
orthogonal to $\ba$. 
It is denoted by $\ba^{\perp}$.

$$
\ba^{\perp} \triangleq \{\bv \in \VV \ST \bv \perp \ba \}.
$$
```

```{prf:observation}
:label: res-la-ip-orth-comp-vec-set

$\ba^{\perp}$ is just a notational convenience.

$$
\ba^{\perp} = \{ \ba \}^{\perp} = (\span \{\ba \})^{\perp}.
$$
```

```{prf:theorem} Orthogonal complement is a linear subspace
:label: res-la-ip-orth-comp-subspace

If $\VV$ is an inner product space and $S \subseteq \VV$, then
$S^{\perp}$ is a subspace.
```

```{prf:proof}
To verify that $S^{\perp}$ is a subspace, we need to check the following.

1. It contains the zero vector.
1. It is closed under vector addition.
1. It is closed under scalar multiplication.

We proceed as follows:

1. $\langle \bzero , \bs \rangle = 0$ holds for any $\bs \in S$. 
   Thus, $\bzero \in S^{\perp}$.
1. Let $\bu, \bv \in S^{\perp}$. Then, 
   1. $\langle \bu, \bs \rangle = 0$ and $\langle \bv, \bs \rangle = 0$ for every $s \in S$.
   1. Thus, $\langle \bu + \bv, \bs \rangle = \langle \bu, \bs \rangle + \langle \bv, \bs \rangle = 0 + 0 = 0$
      for every $s \in S$.
   1. Thus, $\bu + \bv \in S^{\perp}$.
1. Similarly, if $\bv \in S^{\perp}$, then
   $\langle \alpha \bv, \bs \rangle = \alpha \langle \bv, \bs \rangle = 0$
   for every $\bs \in S$.

Thus, $S^{\perp}$ is a subspace of $\VV$.
```

```{prf:observation}
The orthogonal complement of the inner product space $\VV$ is its trivial subspace
containing just the zero vector.

$$
\VV^{\perp} = \{ \bzero \}.
$$
```

```{prf:observation}
If $S$ is a subspace of $\VV$, then to show that some vector 
$\bu \in S^{\perp}$, it is sufficient to show that $\bu$ is
orthogonal to all the vectors in some basis of $S$.
```
```{prf:proof}
Let $\be_1, \dots, \be_p$ be a basis for $S$. 

Then, for any $\bs \in S$:

$$
\bs = \sum_{i=1}^p \alpha_p \be_p.
$$

Now, if $\bu$ is orthogonal to every vector in $\be_1, \dots, \be_p$,
then

$$
\langle \bs, \bu \rangle = \sum_{i=1}^p \alpha_p \langle \be_p, \bu \rangle = 0.
$$

Thus, $\bu \perp \bs$. 
Since $\bs$ was arbitrarily chosen from $S$, hence $\bu \in S^{\perp}$.
```


```{prf:theorem} Orthogonal decomposition
:label: res-la-orthogonal-decomposition

Let $\VV$ be an inner product space and $S$ be a finite dimensional subspace of $\VV$.
Then, every $\bv \in \VV$ can be written uniquely in the form:

$$
\bv = \bv_{\parallel}  + \bv_{\perp}
$$
where $\bv_{\parallel} \in S$ and $\bv_{\perp} \in S^{\perp}$.
```

````{prf:proof}
Let $\be_1, \dots, \be_p$ be an orthonormal basis for $S$. 

Define:

```{math}
:label: eq-la-orth-dec-parallel
\bv_{\parallel} \triangleq \sum_{i=1}^p \langle \bv, \be_i \rangle \be_i.
```

And

$$
\bv_{\perp} = \bv - \bv_{\parallel}.
$$

By construction, $\bv_{\parallel}  \in \span \{ \be_1, \dots, \be_p\} = S$.

Now, for every $0 \leq i \leq p$:

$$
\begin{aligned}
\langle \bv_{\perp}, \be_i \rangle 
&= \langle \bv - \bv_{\parallel}, \be_i \rangle\\
&= \langle \bv, \be_i \rangle - \langle \bv_{\parallel}, \be_i \rangle\\
&= \langle \bv, \be_i \rangle - \langle \bv, \be_i \rangle = 0.
\end{aligned}
$$

Thus, $\bv_{\perp} \in S^{\perp}$.


We have shown that the existence of the decomposition of an vector
$\bv$ in components which belong to $S$ and $S^{\perp}$.
Next, we need to show that the decomposition is unique.

For contradiction, assume there was another decomposition:

$$
\bv = \bu_{\parallel}  + \bu_{\perp}
$$
such that $\bu_{\parallel} \in S$ and $\bu_{\perp} \in S^{\perp}$.

Then,

$$
\bv_{\parallel}  + \bv_{\perp} = \bv = \bu_{\parallel}  + \bu_{\perp}
$$
gives us:

$$
\bw = \bv_{\parallel} - \bu_{\parallel} = \bu_{\perp} - \bv_{\perp}.
$$
Thus, $\bw \in S$ as well as $\bw \in S^{\perp}$. 
But then, $\bw \perp \bw$ giving us:

$$
\langle \bw , \bw \rangle = 0 
= \langle \bv_{\parallel} - \bu_{\parallel}, \bv_{\parallel} - \bu_{\parallel}\rangle 
= \| \bv_{\parallel} - \bu_{\parallel} \|^2.
$$
This is possible only if  $\bv_{\parallel} - \bu_{\parallel} = \bzero$, 
thus, $\bv_{\parallel} = \bu_{\parallel}$.
Consequently, $\bu_{\perp} = \bv_{\perp}$ too.

Thus, 

$$
\bv = \bv_{\parallel}  + \bv_{\perp}
$$
is a unique decomposition.
````

```{prf:corollary} Intersection between a subspace and its complement
:label: res-la-intersect-subspace-complement

If $S$ is a finite dimensional subspace of an inner product space $\VV$, then

$$
S \cap S^{\perp} = \{ \bzero \}.
$$

In other words, the only vector common between $S$ and its orthogonal complement
is the zero vector.
```


```{prf:theorem} Vector space as direct sum
:label: res-la-vs-direct-sum-orth-comp

If $S$ is a finite dimensional subspace of an inner product space $\VV$, then

$$
\VV = S \oplus S^{\perp}.
$$

In other words, $\VV$ is a direct sum of $S$ and its
orthogonal complement.
```

```{prf:proof}
From {prf:ref}`res-la-intersect-subspace-complement`, the
intersection between $S$ and $S^{\perp}$ is the zero vector.
Thus, by {prf:ref}`def-vs-direct-sum-subspaces`,
the direct sum between the two spaces
$S \oplus S^{\perp}$ is well defined.

By {prf:ref}`res-la-orthogonal-decomposition`,
every vector $\bv \in \VV$ can be uniquely
decomposed as

$$
\bv = \bv_{\parallel}  + \bv_{\perp}
$$
where $\bv_{\parallel} \in S$ and $\bv_{\perp} \in S^{\perp}$.

Thus, $\VV \subseteq S \oplus S^{\perp}$.

However, since both $S$ and $S^{\perp}$ are
subspaces of $\VV$, hence

$$
\VV = S \oplus S^{\perp}.
$$
```

```{prf:theorem} Dimension of vector space as direct sum
:label: res-la-vs-dim-dir-sum-orth-comp

Let $\VV$ be a finite dimensional inner product space.
If $S$ is a subspace of $\VV$, then

$$
\dim \VV = \dim S + \dim S^{\perp}.
$$
```

```{prf:proof}
Since $\VV$ is finite dimensional, hence
both $S$ and $S^{\perp}$ are finite dimensional
subspaces of $\VV$.

By {prf:ref}`res-la-vs-direct-sum-orth-comp`


$$
\VV = S \oplus S^{\perp}.
$$

Then, due to {prf:ref}`res-la-dim-direct-sum-subspaces`

$$
\dim \VV = \dim S + \dim S^{\perp}.
$$
```

```{prf:theorem} Orthogonal complement of orthogonal complement
:label: res-la-orth-comp-orth-comp

Let $\VV$ be a finite dimensional inner product space.
Let $S$ be a subspace of $\VV$ and let $S^{\perp}$
be its orthogonal complement. Then

$$
\left (S^{\perp} \right )^{\perp} = S.
$$
In other words, in a finite dimensional space,
the orthogonal complement of orthogonal complement
is the original subspace itself.
```
Note that this result is valid only for finite dimensional
spaces since in that case both $S$ and $S^{\perp}$ are
finite dimensional.

```{prf:proof}
Since $\VV$ is finite dimensional, hence
both $S$ and $S^{\perp}$ are finite dimensional.

$$
\left (S^{\perp} \right )^{\perp} = \{\bv \in \VV \ST 
   \bu \perp \bv \Forall \bu \in S^{\perp} \}.
$$

We shall first show that $S \subseteq \left (S^{\perp} \right )^{\perp}$.

1. Let $\bs \in S$. 
1. Then, by definition, $\bs \perp \bu \Forall \bu \in S^{\perp}$.
1. Thus, $\bs \in \left (S^{\perp} \right )^{\perp}$.
1. Thus, $S \subseteq \left (S^{\perp} \right )^{\perp}$.

We now show that $\left (S^{\perp} \right )^{\perp} \subseteq S$.

1. Let $\bu \in \left (S^{\perp} \right )^{\perp}$.
1. By {prf:ref}`res-la-vs-direct-sum-orth-comp`, $\VV = S \oplus S^{\perp}$
   since $S$ is a finite dimensional subspace of $\VV$.
1. Thus, $\bu = \bv + \bw$ such that $\bv \in S$ and $\bw \in S^{\perp}$.
1. Since $\bu - \bv = \bw$, hence $\bu - \bv \in S^{\perp}$.
1. We have already shown above that $S \subseteq \left (S^{\perp} \right )^{\perp}$.
   Hence $\bv \in \left (S^{\perp} \right )^{\perp}$.
1. Thus, $\bu - \bv = \bw \in \left (S^{\perp} \right )^{\perp}$
   since both $\bu$ and $\bv$ belong to $\left (S^{\perp} \right )^{\perp}$.
1. Thus, $\bu - \bv \in \left (S^{\perp} \right )^{\perp} \cap S^{\perp}$
   as $\bw \in S^{\perp}$ by orthogonal decomposition above.
1. But, by {prf:ref}`res-la-intersect-subspace-complement`
   $S^{\perp} \cap \left (S^{\perp} \right )^{\perp} = \{ \bzero \}$
   since $\left (S^{\perp} \right )^{\perp}$ is the
   orthogonal complement of $S^{\perp}$ and $S^{\perp}$ is 
   finite dimensional.
1. Thus, $\bu - \bv = \bzero$.
1. Thus, $\bu = \bv$.
1. Thus, $\bu \in S$.
1. Since $\bu$ was an arbitrary element of 
   $\left (S^{\perp} \right )^{\perp}$, 
   hence $\left (S^{\perp} \right )^{\perp} \subseteq S$.


Combining the two:

$$
\left (S^{\perp} \right )^{\perp} = S.
$$
```

```{prf:theorem} n-1 dimensional subspaces
:label: res-la-vs-hyper-subspace-expression

Let $\VV$ be a finite dimensional inner product space
with $\dim \VV = n$.
Let $S$ be an $n-1$ dimensional subspace of $\VV$. 
Then, there exists a nonzero vector $\bb \in \VV$ such that 

$$
S = \{ \bx \in \VV \ST \bx \perp \bb \}.
$$

In other words, the $n-1$ dimensional subspaces
are the sets of the form $\{ \bx \ST \bx \perp \bb \}$
where $\bb \neq \bzero$.
```

```{prf:proof}
Let $S$ be $n-1$ dimensional. 
Then, from {prf:ref}`res-la-vs-dim-dir-sum-orth-comp` 

$$
\dim \VV = \dim S + \dim S^{\perp}.
$$
This gives us $\dim S^{\perp} = n - (n-1) = 1$.

Since $S^{\perp}$ is one dimensional, we can choose
a non-zero vector $\bb \in S^{\perp}$ as its basis.
Since $\VV$ is finite dimensional, hence

$$
S = \left (S^{\perp} \right )^{\perp}.
$$

Thus, $S$ consists of vectors which are orthogonal to
a basis of $S^{\perp}$. Thus,

$$
S =  \{ \bx \in \VV \ST \bx \perp \bb \}.
$$
```

## Orthogonal Projection

Recall that a {prf:ref}`projection <def-la-projection>` 
operator $P : \VV \to \VV$ 
is an operator which satisfies $P^2 = P$.

The range of $P$ is given by

$$
\Range(P) = \{\bv \in \VV \ST \bv =  P \bx \text{ for some } \bx \in \VV \}.
$$
The null space of $P$ is given by

$$
\NullSpace(P) = \{ \bv \in \VV | P \bv = \bzero\}.
$$


````{prf:definition} Orthogonal projection operator
:label: def-la-orthogonal-projector

A projection operator $P : \VV \to \VV$
over an inner product space $\VV$ 
is called *orthogonal projection operator*
if its range $\Range(P)$ and the null space 
$\NullSpace(P)$ as defined above are orthogonal to each other; 
i.e.

$$
\br \perp \bn \Forall \br \in \Range(P) , \Forall \bn \in \NullSpace(P).
$$
````

```{prf:theorem} Orthogonal projection operator for a subspace
:label: res-la-ip-subspace-orth-proj

Let $S$ be a finite dimensional subspace of $\VV$. 
Let $\{\be_1, \dots, \be_p\}$ be an orthonormal basis of $S$.
Let the operator $P_S: \VV \to \VV$ be defined as:

$$
P_S \bv \triangleq \bv_{\parallel}
$$
where

$$
\bv = \bv_{\parallel} + \bv_{\perp}
$$
is the unique orthogonal decomposition of $\bv$ w.r.t. the subspace $S$
as defined in {prf:ref}`res-la-orthogonal-decomposition`.
Then,

1. $P_S \bv = \sum_{i=1}^p \langle \bv, \be_i \rangle \be_i$.
1. For any $\bv \in \VV$, $\bv - P_S \bv \perp S$.
1. $P_S$ is a linear map.
1. $P_S$ is the identity map when restricted to $S$;
   i.e., $P_S \bs = \bs \Forall \bs \in S$.
1. $\Range(P_S) = S$.
1. $\NullSpace(P_S) = S^{\perp}$.
1. $P_S^2 = P_S$.
1. For any $\bv \in \VV$, $\| P_S \bv \| \leq \| \bv \|$.
1. For any $\bv \in \VV$ and $\bs \in S$:

   $$
   \| \bv - P_S \bv \| \leq \| \bv - \bs \|
   $$
   with equality if and only if $\bs = P_S \bv$.

$P_S$ is indeed an *orthogonal projection* onto $S$.
```
```{prf:proof}
For the sake of brevity, we abbreviate $P = P_S$.

Following {eq}`eq-la-orth-dec-parallel`, indeed:

$$
P = \sum_{i=1}^p \langle \bv, \be_i \rangle \be_i.
$$

For any $\bv \in \VV$ (due to {prf:ref}`res-la-orthogonal-decomposition`):

$$
\bv - P \bv = \bv - \bv_{\parallel} = \bv_{\perp}.
$$
Since $\bv_{\perp} \in S^{\perp}$ hence $\bv - P \bv \perp S$.

[Linear map]
1. Let $\bu, \bv \in \VV$.
1. Let $\bu = \bu_{\parallel} + \bu_{\perp}$ and $\bv = \bv_{\parallel} + \bv_{\perp}$.
1. Consider $\bu + \bv = (\bu_{\parallel} + \bv_{\parallel}) + (\bu_{\perp} + \bv_{\perp})$.
1. Then, $\bu_{\parallel} + \bv_{\parallel} \in S$ and
   $\bu_{\perp} + \bv_{\perp} \in S^{\perp}$.
1. Since, the orthogonal decomposition is unique, hence
   $P (\bu + \bv) = \bu_{\parallel} + \bv_{\parallel} = P \bu + P \bv$.
1. Similarly, for $\alpha \in \FF$, 
   $\alpha \bu = \alpha \bu_{\parallel} + \alpha\bu_{\perp}$.
1. With $\alpha \bu_{\parallel} \in S$ and $\alpha\bu_{\perp} \in S^{\perp}$,
   $P (\alpha \bu) = \alpha \bu_{\parallel} = \alpha P \bu$.

Thus, $P$ is a linear map.

For any $\bs \in S$, we can write it as $\bs = \bs + \bzero$.
With $\bs \in S$ and $\bzero \in S^{\perp}$,
we have: $P \bs = \bs$.

[Range]

1. Since $P$ maps $\bv$ to a component in $S$, hence $\Range(P) \subseteq S$.
1. Since for every $\bs \in S$, there is $\bv \in S$ such that $P \bv  = \bs$
   (specifically $\bv = \bs$),
   hence $S \subseteq \Range(P)$.
1. Combining $\Range(P) = S$.

[Null space]

1. Let $\bv \in \NullSpace(P)$. Write $\bv = \bv_{\parallel} + \bv_{\perp}$.
1. Then, $P \bv = \bv_{\parallel} = \bzero$ as $\bv$ is in the null space of $P$.
1. Hence, $\bv = \bv_{\perp} \in S^{\perp}$.
1. Thus, $\NullSpace(P) \subseteq S^{\perp}$.
1. Now, let $\bv \in S^{\perp}$. 
1. We can write $\bv$ as $\bv = \bzero + \bv$
   where $\bzero \in S$ and $\bv \in S^{\perp}$.
1. Thus, $P \bv = \bzero$.
1. Thus, $S^{\perp} \subseteq \NullSpace(P)$.
1. Combining, $S^{\perp} = \NullSpace(P)$.

[$P^2 = P$]

1. For any $\bv \in \VV$, we have, $P \bv = \bv_{\parallel}$.
1. Since $\bv_{\parallel} \in S$, hence $P \bv_{\parallel} = \bv_{\parallel}$.
1. Thus, $P^2 \bv = P \bv_{\parallel} = \bv_{\parallel} = P v$.
1. Since $\bv$ was arbitrary, hence, $P^2 = P$.


[$\| P \bv \| \leq \| \bv \|$]

1. We have $\bv = \bv_{\parallel} + \bv_{\perp} = P \bv + \bv_{\perp}$.
1. By Pythagoras theorem: $ \| \bv \|^2 =  \| P \bv \|^2 + \| \bv_{\perp}\|^2$.
1. Thus, $ \| \bv \|^2 \geq \| P \bv \|^2$.
1. Taking square root on both sides: $\| P \bv \| \leq \| \bv \|$.

[$\| \bv - P \bv \| \leq \| \bv - \bs \|$]

1. Let $\bv \in \VV$ and $\bs \in S$.
1. Note that $P \bv \in S$ hence $P \bv - \bs \in S$.
1. By definition $\bv - P \bv \in S^{\perp}$.
1. Thus, $\bv - P \bv \perp P \bv - \bs$.
1. We have: $\bv - \bs = (\bv - P \bv) + (P \bv - \bs)$. 
1. Applying Pythagoras theorem:

   $$
   \| \bv - \bs \|^2 = \| \bv - P \bv\|^2 + \| P \bv - \bs \|^2
   \geq \| \bv - P \bv\|^2.
   $$
1. Taking square root on both sides:

   $$
   \| \bv - P \bv \| \leq \| \bv - \bs \|.
   $$
1. Equality holds if and only if $\| P \bv - \bs \|^2 = 0$
   if and only if $P \bv = \bs$.

In order to show that $P$ is an orthogonal projection, we need to show 
that:

1. $P$ is a projection operator.
1. $\br \perp \bn \Forall \br \in \Range(P) , \Forall \bn \in \NullSpace(P)$.

We have shown that:

1. $P^2 = P$. Hence $P$ is a projection operator.
1. $\Range(P)  = S$ and $\NullSpace(P) = S^{\perp}$.
1. By definition, for any $\br \in S$ and $\bn \in S^{\perp}$, $\br \perp \bn$.
1. Thus, $P$ is an orthogonal projection operator.

```

````{prf:theorem} Orthogonal projectors are adjoint
:label: res-la-ip-orth-proj-adjoint

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

