# Important Vector Spaces

In this section, we will list some important
vector spaces which occur frequently in analysis
and optimization.



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
