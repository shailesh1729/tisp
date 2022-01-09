# Introduction

## Proximal Mapping

```{prf:definition} Proximal mapping
:label: def-prox-proximal-mapping

For a function $f : \EE \to \RERL$, the *proximal mapping* of $f$ is given by

$$
\prox_f(\bx) \triangleq \underset{\bu \in \EE}{\argmin} \left \{
    f(\bu) + \frac{1}{2} \| \bu - \bx \|^2
    \right\} \Forall \bx \in \EE.
$$

* It is a point to set mapping.
* It maps each point $\bx \in \EE$ to a subset of points in $\EE$ which
  minimize the R.H.S..
* The set of points which minimize the R.H.S. are known as *proximal points*
  for a given $\bx$ w.r.t. the function $f$.
* The set of *proximal points* may be empty, singleton or have more than one points. 
```

```{prf:example} Zero function
Consider $f : \RR \to \RR$ defined as $f(x) = 0$.

$$
\prox_f(x) = \underset{u \in \RR}{\argmin} \left \{ 0 + \frac{1}{2} | u  - x |^2  \right \} 
= \{ x\}.
$$
```

```{prf:example} Constant value function
Let $f : \RR \to \RR$ defined as $f(x) = c$ where $c \in \RR$.

$$
\prox_f(x) = \underset{u \in \RR}{\argmin} \left \{ c + \frac{1}{2} | u  - x |^2  \right \} 
= \{ x\}.
$$
```

```{prf:example} 1D Linear function I
Let $f : \RR \to \RR$ be given as $f(x) = x$.

Define: 

$$
g(u) =  f(u) + \frac{1}{2} | u  - x |^2 = u + \frac{1}{2} (u  - x)^2. 
$$

Differentiating, we get:

$$
g'(u) = 1 + (u - x).
$$

Setting $g'(u) = 0$, we get:

$$
1 + u - x = 0 \implies u = x - 1.
$$

The second derivative $g''(u) = 1$ confirms that it is indeed the minimizer.

Thus,

$$
\prox_f(x) = \{ x - 1 \}.
$$
```

```{prf:example} 1D Linear function II
Let $f : \RR \to \RR$ be given as $f(x) = \lambda x$ with $\lambda \in \RR$.

Define: 

$$
g(u) =  f(u) + \frac{1}{2} | u  - x |^2 = \lambda u + \frac{1}{2} (u  - x)^2. 
$$

Differentiating, we get:

$$
g'(u) = \lambda + (u - x).
$$

Setting $g'(u) = 0$, we get:

$$
\lambda + u - x = 0 \implies u = x - \lambda.
$$

The second derivative $g''(u) = 1$ confirms that it is indeed the minimizer.

Thus,

$$
\prox_f(x) = \{ x - \lambda \}.
$$
```

```{prf:example} 1D Affine function
Let $f : \RR \to \RR$ be given as $f(x) = \alpha x + \beta$ with $\alpha, \beta \in \RR$.

Define: 

$$
g(u) =  f(u) + \frac{1}{2} | u  - x |^2 = \alpha u + \beta + \frac{1}{2} (u  - x)^2. 
$$

Differentiating, we get:

$$
g'(u) = \alpha + (u - x).
$$

Setting $g'(u) = 0$, we get:

$$
\alpha + u - x = 0 \implies u = x - \alpha.
$$

The second derivative $g''(u) = 1$ confirms that it is indeed the minimizer.

Thus,

$$
\prox_f(x) = \{ x - \alpha \}.
$$
```

```{prf:theorem} Nonemptiness under closedness and coerciveness

Let $f : \EE \to \RERL$ be a proper closed function. Assume that 
the function

$$
\bu \mapsto f(\bu) +  \frac{1}{2} \| \bu - \bx \|^2
$$

for any $\bx \in \EE$ is coercive. 

Then the set $\prox_f(\bx)$ is nonempty for any $\bx \in \EE$.
```

```{prf:proof}
Define:

$$
h(\bu) \triangleq f(\bu) +  \frac{1}{2} \| \bu - \bx \|^2.
$$

* $h$ is a sum of two closed functions. Hence $h$ is a closed function.
* It is given that $h$ is coercive.
* $h$ is proper since $f$ is proper.
* A proper closed and coercive function $g$ attains a minimal value 
  over any $S \subseteq \EE$ satisfying $S \cap \dom g$.
* With $S = \EE$, we have that $h$ attains a minimal value over $\EE$.
* Thus, the set of minimizers for $h$ is not empty. 
```

## Proximal Operator

```{prf:theorem} First prox theorem

Let $f : \EE \to \RERL$ be a proper, closed and function. Then, $\prox_f(\bx)$ is
a singleton for any $\bx \in \EE$.  
```

```{prf:proof}
Define:

$$
\tilde{f}(\bu, \bx) \triangleq f(\bu) + \frac{1}{2} \| \bu - \bx \|^2.
$$

Then 

$$
\prox_f(\bx) = \underset{\bu \in \EE}{\argmin} \tilde{f}(\bu, \bx).
$$

Consider $\tilde{f}(\cdot, \bx)$ for a fixed valued of $\bx$:

* $f$ is a closed and convex function.
* $\frac{1}{2} \| \cdot - \bx \|^2$ is a closed and strongly convex function.
* Hence, their sum $\tilde{f}(\cdot, \bx)$ is a closed and strongly convex function.
* Since $f$ is proper, hence $\tilde{f}(\cdot, \bx)$ is also proper.
* Thus, $\tilde{f}(\cdot, \bx)$ is a proper, closed and strongly convex function.
* Thus, there exists a unique minimizer for $\tilde{f}(\cdot, \bx)$. 
* Thus, the set $\prox_f(\bx)$ is a singleton.
```

```{prf:definition} Proximal operator
:label: def-prox-proximal-operator

Let $f : \EE \to \RERL$ be a proper closed function. Since 
the point to set mapping $\prox_f : \EE \to 2^{\EE}$ maps 
every point in $\EE$ to a singleton subset of $\EE$, we abuse
the notation and redefine $\prox_f: \EE \to \EE$ as a point to
point mapping. We call this mapping as a *proximal operator* of $f$. 

In other words, we write $\prox_f(\bx) = \by$ rather than $\prox_f(\bx) = \{\by\}$.
```
