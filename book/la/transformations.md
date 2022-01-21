(sec:la:linear-transformations)=
# Linear Transformations
In this section, we will be using symbols $\VV$ and $\WW$
to represent arbitrary vector spaces over a field $\FF$. 

Unless otherwise specified, the two vector spaces won't be related in any way.

Following results can be restated for more general situations where 
$\VV$ and $\WW$ are defined over
different fields, but we will assume that they are defined over the same field $\FF$
for simplicity of discourse.

````{prf:definition} Linear transformation
:label: def-la-linear-transformation

We call a map $\TT : \VV \to \WW$ a *linear transformation* 
from $\VV$ to $\WW$
if for all $\bx, \by \in \VV$ and $\alpha \in \FF$, we  have

1. $\TT(\bx + \by) = \TT(\bx) + \TT(\by)$ and
1. $\TT(\alpha \bx) = \alpha \TT(\bx)$

A linear transformation is also known as a *linear map*
or a *linear operator*.
````

## Properties

````{prf:proposition} Zero maps to zero
If $\TT$ is linear then $\TT(\bzero) = \bzero$.
````

This is straightforward since

$$
    \TT(\bzero + \bzero) = \TT(\bzero) + \TT(\bzero) \implies \TT(\bzero) = \TT(\bzero) + \TT(\bzero) \implies \TT(\bzero) = \bzero.
$$

````{prf:proposition}
$\TT$ is linear $\iff \TT(\alpha \bx + \by) = \alpha \TT(\bx) + \TT(\by)  \Forall \bx, \by \in \VV, \alpha \in \FF$
````

````{prf:proof}
Assuming $\TT$ to be linear we have

$$
    \TT(\alpha \bx + \by) = \TT(\alpha \bx) + \TT(\by) = \alpha \TT(\bx) + \TT(\by).
$$

Now for the converse, assume

$$
    \TT(\alpha \bx + \by) = \alpha \TT(\bx) + \TT(\by)  \Forall \bx, \by \in \VV, \alpha \in \FF.
$$

Choosing both $\bx$ and $\by$ to be  \bzero and $\alpha=1$ we get

$$
    \TT(\bzero + \bzero) = \TT(\bzero) + \TT(\bzero) \implies \TT(\bzero) = \bzero.
$$

Choosing $\by=\bzero$ we get

$$
    \TT(\alpha \bx + \bzero) = \alpha \TT(\bx) + \TT(\bzero) = \alpha \TT(\bx).
$$

Choosing $\alpha = 1$ we get

$$
    \TT(\bx + \by) = \TT(\bx) + \TT(\by).
$$

Thus, $\TT$ is a linear transformation.
````

````{prf:proposition}
If $\TT$ is linear then $\TT(\bx - \by) = \TT(\bx) - \TT(\by)$.
````

$$
    \TT(\bx - \by) = \TT(\bx + (-1)\by) = \TT(\bx) + \TT((-1)\by) = \TT(\bx) +(-1)\TT(\by) = \TT(\bx) - \TT(\by).
$$

````{prf:proposition} Linear transformation preserves linear combinations
$\TT$ is linear $\iff$ for $\bx_1, \dots, \bx_n \in \VV$ and $\alpha_1, \dots, \alpha_n \in \FF$,

$$
    \TT\left (\sum_{i=1}^{n} \alpha_i \bx_i \right ) =  \sum_{i=1}^{n} \alpha_i  \TT(\bx_i).
$$

````
We can use mathematical induction to prove this. 

Some special linear transformations need mention.

````{prf:definition} Identity transformation
:label: def-la-identity-transformation

The *identity transformation* $\mathrm{I}_{\VV} : \VV \to \VV$ is defined as

$$
    \mathrm{I}_{\VV}(x) = x, \Forall x \in \VV.
$$
````


````{prf:definition}
:label: def-la-zero-transformation

The *zero transformation* $\ZERO : \VV \to \WW$ is defined as

$$
    \ZERO(x) = \bzero, \Forall x \in \VV.
$$

Note that $\bzero$ on the R.H.S. is the zero vector or $\WW$.
````

In this definition $0$ is taking up multiple meanings: a linear transformation from
$\VV$ to $\WW$ which maps every vector in $\VV$ to the $\bzero$ vector in $\WW$.

From the context usually it should be obvious whether we are talking about
$0 \in \FF$ or $\bzero \in \VV$ or $\bzero \in \WW$ or
$\ZERO$ as a linear transformation from $\VV$ to $\WW$. 


## Null Space and Range

````{prf:definition} Null space / Kernel
:label: def-la-null-space

The *null space* or *kernel* of a linear transformation $\TT : \VV \to \WW$
denoted by $\NullSpace(\TT)$ or $\Kernel(\TT)$ is defined as

$$
\Kernel(\TT) = \NullSpace(\TT) \triangleq \{ \bx \in \VV \ST \TT(\bx) = \bzero\}.
$$
````

````{prf:theorem}
:label: res-la-null-space-is-subspace

The null space of a linear transformation $\TT : \VV \to \WW$
is a subspace of $\VV$.
````

````{prf:proof}
Let $\bv_1, \bv_2 \in \Kernel(\TT)$. Then

$$
    \TT(\alpha \bv_1 + \bv_2) = \alpha \TT(\bv_1) + \TT(\bv_2) = \alpha \bzero + \bzero = \bzero.
$$

Thus $\alpha \bv_1 + \bv_2 \in \Kernel(\TT)$.
Thus $\Kernel(\TT)$ is a subspace of $\VV$.
````

````{prf:definition}
:label: def-la-kernel-image

The *range* or *image* of a linear transformation $\TT : \VV \to \WW$
denoted by $\Range(\TT)$ or $\Image(\TT)$ is defined as

$$
\Range(\TT) = \Image(\TT) \triangleq \{\TT(\bx) \Forall \bx \in \VV \}.
$$
We note that $\Image(\TT) \subseteq \WW$.
````

````{prf:theorem}
:label: res-la-range-is-subspace

The image of a linear transformation $\TT : \VV \to \WW$
is a subspace of $\WW$.
````

````{prf:proof}
Let $\bw_1, \bw_2 \in \Image(\TT)$.
Then there exist $\bv_1, \bv_2 \in \VV$ such that

$$
    \bw_1 = \TT(\bv_1); \bw_2 = \TT(\bv_2).
$$

Thus

$$
    \alpha \bw_1 + \bw_2 = \alpha \TT(\bv_1) + \TT(\bv_2) = \TT(\alpha \bv_1 + \bv_2).
$$

Thus $\alpha \bw_1 + \bw_2 \in \Image(\TT)$.
Hence $\Image(\TT)$ is a subspace of $\WW$.
````

````{prf:theorem}
:label: res-la-range-span-basis

Let $\TT : \VV \to \WW$ be a linear transformation.
Assume $\VV$ to be finite dimensional.
Let $\BBB = \{\bv_1, \bv_2, \dots, \bv_n\}$ be some basis of $\VV$.
Then

$$
    \Image(\TT) = \span \TT(\BBB) =
    \span \{\TT(\bv_1), \TT(\bv_2), \dots, \TT(\bv_n) \}.
$$

i.e., the image of a basis of $\VV$ under a linear transformation $\TT$
spans the range of the transformation.
````
````{prf:proof}
Let $\bw$ be some arbitrary vector in $\Image(\TT)$.
Then there exists $\bv \in \VV$ such that $\bw = \TT(\bv)$.
Now

$$
    \bv = \sum_{i=1}^n c_i \bv_i
$$
since $\BBB$ forms a basis for $\VV$.
Thus,

$$
    \bw = \TT(\bv) = \TT(\sum_{i=1}^n c_i \bv_i)  = \sum_{i=1}^n c_i (\TT(\bv_i)).
$$

This means that $\bw \in \span \TT(\BBB)$.
````

````{prf:definition} Nullity
:label: def-la-transformation-nullity

For vector spaces $\VV$ and $\WW$ and linear transformation $\TT : \VV \to \WW$ 
if $\kernel \TT$ is finite dimensional then 
*nullity* of $\TT$ is defined as

$$
\nullity \TT \triangleq \dim \kernel \TT;
$$
i.e., the dimension of the null space or kernel of $\TT$.
````

(def:alg:rank)=
````{prf:definition}
:label: def-la-transformation-rank

For vector spaces $\VV$ and $\WW$ and linear $\TT : \VV \to \WW$,
if $\range \TT$ is finite dimensional then *rank* of $\TT$ is
defined as

$$
\rank \TT \triangleq \dim \range \TT;
$$
i.e., the dimension of the range or image of $\TT$.
````

````{prf:theorem} Dimension theorem
:label: res-la-lt-dimension-theorem

For vector spaces $\VV$ and $\WW$ and linear $\TT : \VV \to \WW$
if $\VV$ is finite dimensional, then

$$
\dim \VV = \nullity \TT  + \rank \TT.
$$

This is known as *dimension theorem*.
````

````{prf:theorem}
:label: res-la-lt-injective-nullspace

For vector spaces $\VV$ and $\WW$ and linear $\TT : \VV \to \WW$,
$\TT$ is injective if and only if $\Kernel(\TT) = \{ \bzero\}$.
````

````{prf:proof}
If $\TT$ is injective, then

$$
\bv_1 \neq \bv_2 \implies T(\bv_1) \neq T(\bv_2)
$$

Let $\bv \neq \bzero$. Now $\TT(\bzero) = \bzero \implies \TT(v) \neq \bzero $ since $\TT$ is one-one.
Thus $\kernel \TT = \{ \bzero\}$.

For the converse,
let us assume that $\kernel \TT = \{ \bzero\}$. 
Let $\bv_1, \bv_2 \in \VV$ be
two vectors such that they have the same image.
Then,

$$
    &\TT(\bv_1) = \TT(\bv_2) \\
    \implies &\TT(\bv_1 - \bv_2)   = \bzero \\
    \implies &\bv_1 - \bv_2 \in \kernel \TT\\
    \implies &\bv_1 - \bv_2 = \bzero \\
    \implies &\bv_1 = \bv_2.
$$
Thus $\TT$ is injective.
````

````{prf:theorem} Bijective transformation characterization
:label: res-la-lt-bijective

For vector spaces $\VV$ and $\WW$ of equal finite
dimensions and linear $\TT : \VV \to \WW$, the following are equivalent.

1. $\TT$ is injective.
1. $\TT$ is surjective.
1. $\rank \TT  = \dim  \VV$.
````

````{prf:proof}
From (1) to (2)

Let $\BBB = \{\bv_1, \bv_2, \dots \bv_n \}$ be some basis of $\VV$
with $\dim \VV = n$.

Let us assume that $\TT(\BBB)$ are linearly dependent. 
Thus, there exists a linear relationship

$$
    \sum_{i=1}^{n}\alpha_i \TT(\bv_i) = \bzero
$$
where $\alpha_i$ are not all 0.
Now

$$
    &\sum_{i=1}^{n}\alpha_i \TT(\bv_i) = \bzero \\
    \implies &\TT\left(\sum_{i=1}^{n}\alpha_i \bv_i\right) = \bzero\\
    \implies &\sum_{i=1}^{n}\alpha_i \bv_i \in \kernel \TT\\
    \implies &\sum_{i=1}^{n}\alpha_i \bv_i = \bzero
$$

since $\TT$ is injective (see {prf:ref}`res-la-lt-injective-nullspace`).
This means that $\bv_i$ are linearly dependent.
This contradicts our assumption that $\BBB$ is a basis for $\VV$.

Thus $\TT(\BBB)$ are linearly independent.

Since $\TT$ is injective, hence all vectors in $\TT(\BBB)$
are distinct, hence

$$
    | \TT(\BBB) | = n.
$$

Since $\TT(\BBB)$ span $\image \TT$ and are linearly independent, 
hence they form a basis of $\image \TT$.

But

$$
    \dim \VV = \dim \WW = n
$$
and $\TT(\BBB)$ are a set of $n$ linearly independent vectors in $\WW$.

Hence, $\TT(\BBB)$ form a basis of $\WW$. Thus

$$
    \image \TT   = \span \TT(\BBB) = \WW.
$$

Thus $\TT$ is surjective.

From (2) to (3)

$\TT$ is surjective means $\image \TT = \WW$.
Thus

$$
    \rank \TT  = \dim \WW = \dim \VV.
$$

From (3) to (1)

We know that

$$
    \dim \VV = \rank \TT  + \nullity \TT.
$$

But, it is given that $\rank \TT  = \dim \VV$.
Thus

$$
    \nullity \TT  = 0.
$$

Thus $\TT$ is injective (due to {prf:ref}`res-la-lt-injective-nullspace`).
````


## Bracket Operator
Recall the definition of coordinate vector from {prf:ref}`def-la-coordinate-vector`.
Conversion of a given vector to its coordinate vector representation can be shown
to be a linear transformation.

````{prf:definition} Bracket operator
:label: def-la-bracket-operator

Let $\VV$ be a finite dimensional vector space over a field $\FF$ where
$\dim \VV = n$. 
Let $\BBB  = \{ \bv_1, \dots, \bv_n\}$ be an ordered basis in $\VV$. 
We define a bracket operator from $\VV$ to $\FF^n$ as

$$
    \begin{aligned}
    \Bracket_{\BBB} : &\VV \to \FF^n\\
    & \bx \to [\bx]_{\BBB}\\
    & \triangleq \begin{bmatrix}
    \alpha_1\\
    \vdots\\
    \alpha_n
    \end{bmatrix}
    \end{aligned}
$$
where

$$
    \bx = \sum_{i=1}^n \alpha_i \bv_i
$$
is the unique representation of $\bx$ in $\BBB$.
````

In other words, the bracket operator takes a vector $\bx$ 
from a finite dimensional space $\VV$ to its 
representation in $\FF^n$ for a given basis $\BBB$.

We now show that the bracket operator is linear.

````{prf:theorem} Bracket operator is linear and bijective
:label: res-la-bracket-operator-linear

Let $\VV$ be a finite dimensional vector space over a field $\FF$ where
$\dim \VV = n$. 
Let $\BBB  = \{ \bv_1, \dots, \bv_n\}$ be an ordered basis in $\VV$.
The bracket operator $\Bracket_{\BBB} : \VV \to \FF^n$
as defined in {prf:ref}`def-la-bracket-operator` is a
linear operator.

Moreover $\Bracket_{\BBB}$ is a bijective mapping.
````

````{prf:proof}
Let $\bx, \by \in \VV$ such that

$$
    \bx = \sum_{i=1}^n \alpha_i \bv_i
$$
and

$$
    \by = \sum_{i=1}^n \beta_i \bv_i.
$$

Then

$$
    c \bx + \by = c \sum_{i=1}^n \alpha_i \bv_i + \sum_{i=1}^n \beta_i \bv_i
    = \sum_{i=1}^n (c \alpha_i + \beta_i ) \bv_i.
$$
Thus,

$$
    [c \bx + \by]_{\BBB} =
    \begin{bmatrix}
    c \alpha_1 + \beta_1 \\
    \vdots\\
    c \alpha_n + \beta_n
    \end{bmatrix}
    = c
    \begin{bmatrix}
    \alpha_1 \\
    \vdots\\
    \alpha_n
    \end{bmatrix}
    +
    \begin{bmatrix}
    \beta_1 \\
    \vdots\\
    \beta_n
    \end{bmatrix}
    = c [\bx]_{\BBB} + [\by]_{\BBB}.
$$

Thus $\Bracket_{\BBB}$ is linear.

We can see that by definition $\Bracket_{\BBB}$ is injective. 
Now since $\dim \VV = n = \dim \FF^n$ 
hence $\Bracket_{\BBB}$ is surjective
due to {prf:ref}`res-la-lt-bijective`.
````

## Matrix Representations


It is much easier to work with a matrix representation of
a linear transformation. In this section we describe
how matrix representations of a linear transformation are
developed. 

In order to develop a representation for the map
$\TT : \VV \to \WW$ we first need to choose
a representation for vectors in $\VV$ and $\WW$. 
This can be easily done by choosing a basis in $\VV$ and
another in $\WW$. Once the bases are chosen, then we
can represent vectors as coordinate vectors. 

````{prf:definition} Matrix representation of a linear transformation
:label: def-la-lt-matrix-rep

Let $\VV$ and $\WW$ be finite dimensional vector spaces
with ordered bases $\BBB = \{\bv_1, \dots, \bv_n\}$
and $\Gamma = \{\bw_1, \dots,\bw_m\}$ respectively.
Let $\TT : \VV \to \WW$ be a linear transformation.
For each $\bv_j \in \BBB$ we can find a unique representation
for $\TT(\bv_j)$ in $\Gamma$ given by

$$
    \TT(\bv_j) = \sum_{i=1}^{m} a_{ij} \bw_i \Forall 1 \leq j \leq n.
$$

The $m\times n$ matrix $A$ defined by $A_{ij} = a_{ij}$ is the
*matrix representation* of $\TT$ in the ordered bases
$\BBB$ and $\Gamma$, denoted as

$$
    A = [\TT]_{\BBB}^{\Gamma}.
$$

If $\VV = \WW$ and $\BBB = \Gamma$ then we write

$$
    A = [\TT]_{\BBB}.
$$
````

The $j$-th column of $A$ is the representation of $\TT(v_j)$ in
$\Gamma$.

In order to justify the matrix representation of $\TT$ we
need to show that application of $\TT$ is same as multiplication
by $A$. This is stated formally below.

````{prf:theorem} Justification of matrix representation
:label: res-la-lt-matrix-rep-just

$$
    [\TT (\bv)]_{\Gamma} = [\TT]_{\BBB}^{\Gamma} [\bv]_{\BBB} \Forall \bv \in \VV.
$$

````
````{prf:proof}
Let

$$
    \bv = \sum_{j=1}^{n} c_j \bv_j.
$$

Then

$$
    [\bv]_{\BBB}  =
    \begin{bmatrix}
    c_1\\
    \vdots\\
    c_n
    \end{bmatrix}
$$

Now

$$
    \TT(\bv) &= \TT\left( \sum_{j=1}^{n} c_j \bv_j \right)\\
    &= \sum_{j=1}^{n} c_j \TT(\bv_j)\\
    &= \sum_{j=1}^{n} c_j \sum_{i=1}^{m} a_{ij} \bw_i\\
    &= \sum_{i=1}^{m} \left (  \sum_{j=1}^{n} a_{ij} c_j \right ) \bw_i\\
$$

Thus

$$
    [\TT (\bv)]_{\Gamma} = \begin{bmatrix}
    \sum_{j=1}^{n} a_{1 j} c_j\\
    \vdots\\
    \sum_{j=1}^{n} a_{m j} c_j
    \end{bmatrix}
    = A \begin{bmatrix}
    c_1\\
    \vdots\\
    c_n
    \end{bmatrix}
    = [\TT]_{\BBB}^{\Gamma} [\bv]_{\BBB}.
$$
````


## Vector Space of Linear Transformations
If we consider the set of linear transformations from $\VV$ to $\WW$
we can impose some structure on it and take its advantages.

First of all we will define basic operations like addition and scalar
multiplication on the general set of mappings from a vector
space $\VV$ to another vector space $\WW$.

````{prf:definition} Addition and scalar multiplication on mappings
:label: def-la-lt-operator-addition

Let $\TT$ and $\UU$ be arbitrary mappings from vector space $\VV$
to vector space $\WW$ over the field $\FF$.
Then *addition* of mappings is defined as

$$
    (\TT + \UU)(\bv) = \TT(\bv) + \UU(\bv)  \Forall \bv \in \VV.
$$

*Scalar multiplication* on a mapping is defined as

$$
    (\alpha \TT)(\bv) = \alpha (\TT (\bv)) \Forall \alpha \in \FF, \bv \in \VV.
$$
````
With these definitions we have

$$
    (\alpha \TT + \UU)(\bv) = (\alpha \TT)(\bv) + \UU(\bv) = \alpha (\TT (\bv)) + \UU(\bv).
$$



We are now ready to show that with the addition and scalar multiplication
as defined above, the set of linear transformations from $\VV$ to $\WW$ 
actually forms a vector space.

````{prf:theorem} Linear transformations form a vector space
:label: res-la-lt-as-vector-space

Let $\VV$ and $\WW$ be vector spaces over field $\FF$.
Let $\TT$ and $\UU$ be some linear transformations from $\VV$ to $\WW$. 
Let addition and scalar multiplication of linear transformations
be defined as in {prf:ref}`def-la-lt-operator-addition`.
Then $\alpha \TT + \UU$ where $\alpha \in \FF$ is a linear transformation.

Moreover, the set of linear transformations from $\VV$ to $\WW$ forms
a vector space.
````

````{prf:proof}
We first show that $\alpha \TT + \UU$ is linear.

Let $\bx,\by \in \VV$ and $\beta \in \FF$. 
Then we need to show that

$$
    (\alpha \TT + \UU) (\bx + \by) = (\alpha \TT + \UU) (\bx) + (\alpha \TT + \UU) (\by)\\
    (\alpha \TT + \UU) (\beta \bx) = \beta ((\alpha \TT + \UU) (\bx)).
$$

Starting with the first one:

$$
    (\alpha \TT + \UU)(\bx + \by)
    &= (\alpha \TT)(\bx + \by) + \UU(\bx + \by)\\
    &= \alpha ( \TT (\bx + \by) ) + \UU(\bx) + \UU(\by)\\
    &= \alpha \TT (\bx) + \alpha \TT(\by) + \UU(\bx) + \UU(\by)\\
    &= (\alpha \TT) (\bx) + \UU (\bx) + (\alpha \TT)(\by) + \UU(\by)\\
    &= (\alpha \TT + \UU)(\bx) + (\alpha \TT + \UU)(\by).
$$

Now the next one

$$
    (\alpha \TT + \UU) (\beta \bx)
    &= (\alpha \TT ) (\beta \bx) + \UU (\beta \bx)\\
    &= \alpha (\TT(\beta \bx)) + \beta (\UU (\bx))\\
    &= \alpha (\beta (\TT (\bx))) +  \beta (\UU (\bx))\\
    &= \beta (\alpha (\TT (\bx))) + \beta (\UU(\bx))\\
    &= \beta ((\alpha \TT)(\bx) + \UU(\bx))\\
    &= \beta((\alpha \TT + \UU)(\bx)).
$$

We can now easily verify that the set of linear transformations
from $\VV$ to $\WW$ satisfies all the requirements of a vector space.
Hence it is a vector space (of linear transformations from $\VV$ to $\WW$).
````

````{prf:definition} The vector space of linear transformations
:label: def-la-lt-vector-space

Let $\VV$ and $\WW$ be vector spaces over field $\FF$. Then
the *vector space of linear transformations* from $\VV$ to $\WW$
is denoted by $\LinTSpace(\VV, \WW)$.

When $\VV = \WW$ then it is simply denoted by $\LinTSpace(\VV)$.
````

The addition and scalar multiplication as defined in
{prf:ref}`def-la-lt-operator-addition` carries forward
to matrix representations of linear transformations also.

 (thm:alg:lin_trans_matrix_rep_add_scale)=
````{prf:theorem}
Let $\VV$ and $\WW$ be finite dimensional vector spaces over field $\FF$
with $\BBB$ and $\Gamma$ being their respective bases.
Let $\TT$ and $\UU$ be some linear transformations from $\VV$ to
$\WW$.

Then, the following hold

1. $[\TT + \UU]_{\BBB}^{\Gamma} = [\TT]_{\BBB}^{\Gamma} + [\UU]_{\BBB}^{\Gamma}$.
1. $[\alpha \TT]_{\BBB}^{\Gamma} = \alpha [\TT]_{\BBB}^{\Gamma} \Forall \alpha \in \FF$.
````

