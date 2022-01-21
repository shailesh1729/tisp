(sec:la:normed-spaces)=
# Normed Linear Spaces

A norm is a real number attached to every vector.
Norm is a generalization of the notion of length.
Adding a norm to a vector space makes it a normed
linear space with rich topological properties
as a norm induces a 
{prf:ref}`distance function <def-ms-distance-function>` (a metric)
on the vector space converting it into a 
{prf:ref}`metric space <def-ms-metric-space>`
with an algebraic structure.
A normed linear space that is 
{prf:ref}`complete <def-ms-complete-metric-space>` is called
a Banach space.


We restrict our attention to real vector spaces and complex vector spaces.
Thus, the field $\FF$ can be either $\RR$ or $\CC$.

## Norm

````{prf:definition} Norm
:label: def-la-norm

A *norm* over a $\FF$-vector space $\VV$ is any real valued function
$\| \| : \VV \to \RR$ mapping $ \bv \mapsto \| \bv\|$
satisfying following properties:

1. [Positive definiteness]

   $$
   \| \bv\| \geq 0 \quad \forall \bv \in \VV \text{  and  } \| \bv\| = 0 \iff \bv = 0.
   $$
1. [Scalar multiplication]

   $$
    \| \alpha \bv \| = | \alpha | \| \bv \| \quad \forall \alpha \in \RR; \forall \bv \in \VV.
   $$
1. [Triangle inequality]

   $$
    \| \bv_1 + \bv_2 \| \leq \| \bv_1 \| + \| \bv_2 \| \quad \forall \bv_1, \bv_2 \in \VV.
   $$
````

```{prf:proposition} Triangle inequality for distances
The triangle inequality is equivalent to the following property:

$$
\| \bx - \by \| \leq \| \bx - \bz \| + \| \bz - \by \| \Forall \bx, \by, \bz \in \VV.
$$
```

```{prf:proof}

Start with 

$$
\| \bv_1 + \bv_2 \| \leq \| \bv_1 \| + \| \bv_2 \|.
$$

Put $\bv_1 = \bx - \bz $ and $\bv_2 = \bz - \by$. We get:

$$
\| \bx - \bz  + \bz - \by \| \leq \| \bx - \bz  \| + \| \bz - \by \|
\iff
\| \bx - \by \| \leq \| \bx - \bz \| + \| \bz - \by \|.
$$

For the converse, start with:

$$
\| \bx - \by \| \leq \| \bx - \bz \| + \| \bz - \by \|
$$

Put $\bv_1 = \bx - \bz$ and $\bv_2 = \bz - \by$. Then, $\bv_1 + \bv_2 = \bx - \by$.
We get:

$$
\| \bv_1 + \bv_2 \| \leq \| \bv_1 \| + \| \bv_2 \|.
$$
```

## Normed Linear Space

````{prf:definition}
:label: def-la-normed-linear-space

An $\FF$-vector space $\VV$ equipped with a norm $\| \| : \VV \to \RR$ is known
as a *normed linear space*.
````
