# Real Vector Spaces

We recall that 

```{div}
* $\RR$ denotes the real line
* $\ERL$ denotes the extended real line
* $\RR_+$ denotes the set of nonnegative reals.
* $\RR_{++}$ denotes the set of positive reals.
```

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

## Affine Sets

Affine sets for a general vector space $\VV$ over field $\FF$
have been discussed in {ref}`sec:la:affine_sets`.
We recall the definitions and adapt them for real
vector spaces.


For any $\bx$ and $\by$ in $\VV$, points of the form
$t \bx + (1 - t) \by$ where $t \in \RR$
form a *line*.

Any subset $C \subseteq \VV$ is *affine* if $C = t C + (1-t)C$ 
for all $t \in \RR$. 
An affine set contains all its lines. 
Other terms used for affine sets are *affine manifolds*,
*affine varieties*, *linear varieties* or *flats*.
Empty set is affine. 
The whole vector space $\VV$ is affine.
Singletons (sets with a single point) are affine.
Any line is affine.

A point of the form $\bx = t_1 \bx_1 + \dots + t_k \bx_k$ where 
$t_1 + \dots + t_k = 1$ with $t_i \in \RR$ and $\bx_i \in \VV$, 
is called an *affine combination* of the points $\bx_1,\dots,\bx_k$.
An affine set contains all its affine combinations.
An affine combination of affine combinations is an affine combination.

Let $C$ be a nonempty affine set and 
$\bx_0$ be any element in $C$. Then the set

$$
V = C - \bx_0 = \{ \bx  - \bx_0 | \bx \in C\}
$$
is a linear subspace of $\VV$. 
$C$ can be written as $C = V + \bx_0$.
A nonempty affine set is a translated linear subspace.
The linear subspace associated with $C$ is independent of 
the choice of $\bx_0$ in $C$.
A nonempty affine set is called an *affine subspace*.
The *affine dimension* of an affine subspace is the 
dimension of the associated linear subspace.

The set of all affine combinations of points in some arbitrary nonempty set 
$S \subseteq \VV$ 
is called the *affine hull* of $S$ and denoted as $\affine S$:
An affine hull is an affine subspace.
The affine hull of a nonempty set $S$ is the smallest affine subspace containing $S$. 

A set of vectors $\bv_0, \bv_1, \dots, \bv_k \in \VV$ is called *affine independent*,
if the vectors $\bv_1 - \bv_0, \dots, \bv_k - \bv_0$ are linearly independent.


(sec:convex:hyperplane)=
## Hyper Planes

Hyperplanes for general vector spaces are
described in {prf:ref}`def-la-hyperplane-functional`
in terms of linear functionals. Here, we focus
specifically on hyperplanes in a real inner product space.

````{prf:definition} Hyperplane
:label: def-hyperplane

A *hyperplane*  is a set of the form

$$
       H_{\ba, b} =  \{ x : \langle \ba, \bx \rangle = b \}
$$
where $\ba \in \VV, \ba \neq \bzero$ and $b \in \RR$.
The vector $\ba$ is called the *normal vector* to the hyperplane.
````


*  Algebraically, it is a solution set of a 
   nontrivial linear equation. 
   Thus, it is an affine set.
*  Geometrically, it is a set of points with a 
   constant inner product to a given vector $\ba$.
* The representation of $H_{\ba, b}$ is unique up to
  a common nonzero multiple. In other words,

  $$
  H_{\ba, b} = H_{\alpha \ba, \alpha b} \Forall \alpha \neq 0.
  $$
* Every other normal of $H_{\ba, b}$ is either a
  positive or negative multiple of $\ba$.
* Thus, we can think of $H_{\ba, b}$ having two sides,
  one along the normal $\ba$ and one opposite to the normal.

```{prf:theorem} Hyperplane second form
Let $\bx_0$ be an arbitrary element in $H_{\ba, b}$. Then

$$
H_{\ba, b} = \{ \bx \ST \langle a, \bx-\bx_0 \rangle = 0\}.
$$ 
```

```{prf:proof}
Given $\bx_0 \in H$,

$$
             &\langle \ba, \bx_0 \rangle = b\\
    \implies &\langle \ba, \bx \rangle = \langle \ba, \bx_0 \rangle \Forall \bx \in H\\
    \implies &\langle \ba, \bx - \bx_0 \rangle = 0 \Forall \bx \in H\\
    \implies &H = \{ \bx \ST \langle a, \bx-\bx_0 \rangle = 0\}.
$$
```

Recall that 
{prf:ref}`orthogonal complement <def-la-orthogonal-complement-vector>`
of $\ba$ is defined as

$$
a^{\perp} = \{ \bv \in \VV \ST  \ba \perp \bv \};
$$
i.e., the set of all vectors that are orthogonal to $\ba$.

```{prf:theorem} Hyperplane third form
Let $\bx_0$ be an arbitrary element in $H_{\ba, b}$. Then

$$
H_{\ba, b} = \bx_0 + \ba^{\perp}.
$$
```

```{prf:proof}
Consider the set

$$
S = \bx_0 + \ba^{\perp}. 
$$

Every element  $\bx \in S$
can be written as $\bx = \bx_0 + \bv$ 
such that $\langle \bv, \ba \rangle = 0$.
Thus,

$$
\langle \bx , \ba \rangle = \langle \bx_0 , \ba \rangle = b. 
$$

Thus, $S \subseteq H$.

For any $\bx \in H$:

$$
\langle \ba, \bx - \bx_0 \rangle = b - b = 0. 
$$
Thus, $\bx - \bx_0 \in \ba^{\perp}$. 
Thus, $\bx \in \bx_0 + \ba^{\perp} = S$.
Thus, $H \subseteq S$.

Combining:

$$
H = S = \bx_0 + \ba^{\perp}. 
$$
```
Thus, the hyperplane consists of an offset $\bx_0$ plus 
all vectors orthogonal to the (normal) vector $\ba$.

```{prf:observation}
A hyperplane is an {prf:ref}`affine subspace <def-affine-subspace>`
since $\ba^{\perp}$ is a linear subspace and 
$H$ is the linear subspace plus an offset $\bx_0$.
```

## Half Spaces

````{prf:definition} halfspace
:label: def-halfspace

A hyperplane divides $\VV$ into two *halfspaces*.
The two (closed) halfspaces are given by

$$
    H_+ = \{ \bx : \langle \ba, \bx \rangle \geq b \}
$$

and

$$
    H_- = \{ \bx : \langle \ba, \bx \rangle \leq b \}
$$

The halfspace $H_+$ extends in the direction of $\ba$ while
$H_-$ extends in the direction of $-\ba$.
````


*  A halfspace is the solution set of one (nontrivial) linear inequality.
*  The halfspace can be written alternatively as 

$$
    H_+  = \{ \bx \ST \langle \ba, \bx - \bx_0 \rangle \geq 0\}\\
    H_-  = \{ \bx \ST \langle \ba, \bx - \bx_0 \rangle \leq 0\}
$$


where $\bx_0$ is any point in the associated hyperplane $H$.
*  Geometrically, points in $H_+$ make an acute angle with $\ba$ 
   while points in $H_-$ make an obtuse angle with $\ba$.


````{prf:definition} Open halfspace
:label: def-open-halfspace
The sets given by

$$
    \Interior{H_+} = \{ \bx | \langle \ba, \bx \rangle > b\}\\
    \Interior{H_-} = \{ \bx | \langle \ba, \bx \rangle < b\}
$$

are called *open halfspaces*. They are the interior
of corresponding closed halfspaces.
````

## Relative Interior

```{prf:definition} Relative interior point
:label: def-cvx-relative-interior-point

Let $C \subseteq \VV$. We say that $\bx \in C$ 
is a *relative interior point* of $C$ if
there exists an open ball $B(x, r)$ for some $r > 0$
such that 

$$
B(x, r) \cap \affine C \subseteq C.
$$
```

Note that, the open ball $B(x, r)$ itself need not be
contained inside $C$.

```{prf:definition} Relative interior
:label: def-cvx-relative-interior

The *relative interior* of a set $C$, denoted by $\relint C$
is the set of 
all its relative interior points.
```

$C$ may have an empty interior
and yet may have a nonempty relative interior.

```{prf:definition} Relative boundary
:label: def-cvx-relative-boundary

The *relative boundary* of a set $C$, denoted by $\relbd C$
is given by

$$
\relbd C \triangleq \closure C \setminus \relint C.
$$
```


## The $\VV \oplus \RR$ Vector Space

While studying convex cones, 
we often find dealing with the set $\VV \times \RR$.
Since $\RR$ is a vector space over $\RR$ by itself
(see {prf:ref}`ex-field-is-vector-space`),
hence we have a 
{prf:ref}`direct sum <def-vs-direct-sum-vector-spaces>` 
$\VV \oplus \RR$ vector space.  
We provide an extended vector space structure below
(providing inner product and norm features)
which aligns with the vector space structure of $\RR^{n+1}$
if $\VV = \RR^n$. 

```{prf:definition} Direct sum $\VV \oplus \RR$
:label: def-cvx-real-vector-space-r-prod

Let $\VV$ be a real vector space. 
A vector space structure can be introduced to the set $\VV \times \RR$
as per the following definitions.

1. [Additive identity] Let $\bzero$ be the additive identity for $\VV$.
   Then, the additive identity for $\VV \times \RR$ is given by 
   $(\bzero, 0)$.
1. [Vector addition] Let $(\bx, s)$ and $(\by, t)$ be in $\VV \times \RR$.
   Then, their sum is defined as:

   $$
   (\bx, s) + (\by, t) \triangleq (\bx + \by, s + t).
   $$

1. [Scalar multiplication] Let $(\bx, s) \in \VV \times \RR$ and
   $\alpha \in \RR$. Then, the scalar multiplication is defined as:

   $$
   \alpha (\bx, s) \triangleq (\alpha \bx, \alpha s).
   $$
1. [Inner product] If $\VV$ is an inner product space, then 
   with $(\bx, s)$ and $(\by, t)$ be in $\VV \times \RR$, 
   the inner product is defined as:

   $$
   \langle (\bx, s), (\by, t) \rangle
   \triangleq \langle \bx, \by \rangle + st.
   $$
1. [Norm] If $\VV$ is a normed linear space, then
   for any $(\bx, s) \in \VV \times \RR$, the norm
   is defined as:

   $$
   \| (\bx, s) \| \triangleq \sqrt{\| \bx \|^2 + s^2}.
   $$

$\VV \times \RR$ equipped with these definitions
is a vector space over $\RR$ in its own right
and is called the *direct sum*
of $\VV$ and $\RR$ denoted by $\VV \oplus \RR$.
```

Readers can verify that these definitions satisfy
all the properties of real vector spaces, 
normed linear spaces and inner product spaces.