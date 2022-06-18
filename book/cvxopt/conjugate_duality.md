(sec:opt:conjugate:duality)=
# Conjugate Duality

## Fenchel's Duality Theorem

Consider the minimization problem

```{math}
:label: eq-opt-fenchel-primal
\inf_{\bx \in \VV} f(\bx) + g(\bx).
```

The problem can be rewritten as

$$
\inf_{\bx, \bz \in \VV} \{ f(\bx) + g(\bz) \ST \bx = \bz \}.
$$

Construct the Lagrangian for this problem.

$$
L (\bx, \bx; \by ) &= f(\bx) + g(\bz)  + \langle \bz - \bx, \by \rangle\\
&= -[\langle \bx, \by \rangle - f(\bx)]  - [\langle \bz, -\by \rangle - g(\bz)].
$$

The dual objective is constructed by minimizing the Lagrangian with the
primal variables $\bx, \bz$.

$$
q(\by) = \inf_{\bx, \bz} L(\bx, \bz; \by) = - f^*(\by) - g^*(- \by).
$$

We thus obtain the following dual problem, known as the *Fenchel's dual*:

```{math}
:label: eq-opt-fenchel-dual
\sup_{\by \in \VV^*} \{ - f^*(\by) - g^*(- \by) \}.
```

Fenchel's duality theorem provides the conditions under which strong duality
holds for the pair of problems {eq}`eq-opt-fenchel-primal` and {eq}`eq-opt-fenchel-dual`.

```{prf:theorem} Fenchel's duality theorem
:label: res-opt-fenchel-duality-theorem

Let $f,g : \VV \to \RERL$ be proper convex functions.
If $\relint \dom f \cap \relint \dom g \neq \EmptySet$, then 

$$
\underset{\bx \in \VV}{\inf} \{f(\bx) + g(\bx) \}
= \underset{\by \in \VV^*}{\sup} \{ - f^*(\by) - g^*(-\by) \}.
$$
The supremum of R.H.S. (the dual problem) is attained whenever it is finite.
```
