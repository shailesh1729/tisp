(sec:la:normed-spaces)=
# Normed Spaces

Norms are a generalization of the notion of length.

We restrict our attention to real vector spaces and complex vector spaces.
Thus, the field $\FF$ can be either $\RR$ or $\CC$.

## Norm

````{prf:definition} Norm
:label: def-la-norm

A *norm* over a $\FF$-vector space $\VV$ is any map
$\| \| : V \to \RR$ mapping $ \bv \mapsto \| \bv\|$
satisfying following properties:

1. [Positive definiteness]

   $$
    \| \bv\| \geq 0 \quad \forall \bv \in \VV \text{  and  } \| \bv\| = 0 \iff \bv = 0.
   $$
1. [Scalar multiplication]

   $$
    \| \alpha \bv \| = | \alpha | \| \bv \| \quad \forall \alpha \in \FF; \forall \bv \in \VV.
   $$
1. [Triangle inequality]

   $$
    \| \bv_1 + \bv_2 \| \leq \| \bv_1 \| + \| \bv_2 \| \quad \forall \bv_1, \bv_2 \in \VV.
   $$
````

````{prf:definition}
:label: def-la-normed-linear-space

An $\FF$-vector space $\VV$ equipped with a norm $\| \| : \VV \to \RR$ is known
as a *normed linear space*.
````
