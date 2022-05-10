# Proximal Mappings and Operators

Throughout this section $\VV$ represents a
{prf:ref}`Euclidean space <def-la-gen-euclidean-space>`;
i.e., an $n$-dimensional space endowed with
an inner product $\langle \cdot, \cdot \rangle$
and the Euclidean norm $\| \cdot \| = \sqrt{\langle \cdot, \cdot \rangle}$.


## Proximal Mapping

```{prf:definition} Proximal mapping
:label: def-prox-proximal-mapping

For a function $f : \VV \to \RERL$, the *proximal mapping* of $f$ is given by

$$
\prox_f(\bx) \triangleq \underset{\bu \in \VV}{\argmin} \left \{
    f(\bu) + \frac{1}{2} \| \bu - \bx \|^2
    \right\} \Forall \bx \in \VV.
$$

* It is a point to set mapping.
* It maps each point $\bx \in \VV$ to a subset of points in $\VV$ which
  minimize the R.H.S..
* The set of points which minimize the R.H.S. are known as *proximal points*
  for a given $\bx$ w.r.t. the function $f$.
* The set of *proximal points* may be empty, singleton or have more than one points. 
```

### Zero Function

```{prf:example} Zero function
:label: ex-prox-zero-function

Consider $f : \RR \to \RR$ defined as $f(x) = 0$.

$$
\prox_f(x) = \underset{u \in \RR}{\argmin} \left \{ 0 + \frac{1}{2} | u  - x |^2  \right \} 
= \{ x\}.
$$
```

### Constant Value Function

```{prf:example} Constant value function
:label: ex-prox-constant-function

Let $f : \RR \to \RR$ defined as $f(x) = c$ where $c \in \RR$.

$$
\prox_f(x) = \underset{u \in \RR}{\argmin} \left \{ c + \frac{1}{2} | u  - x |^2  \right \} 
= \{ x\}.
$$
```

### 1D Linear Function I

```{prf:example} 1D Linear function I
:label: ex-prox-1d-linear-function-1

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

### 1D Linear Function II

```{prf:example} 1D Linear function II
:label: ex-prox-1d-linear-function-2

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

### 1D Affine Function

```{prf:example} 1D Affine function
:label: ex-prox-1d-affine-function

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

### Nonemptiness Conditions

It is imperative to identify conditions under which
a proximal mapping is nonempty.

```{prf:theorem} Nonemptiness under closedness and coerciveness
:label: res-prox-nonemptiness-under-closedness-coerciveness

Let $f : \VV \to \RERL$ be a proper and closed function. Assume that 
the function

$$
\bu \mapsto f(\bu) +  \frac{1}{2} \| \bu - \bx \|^2
$$

for any $\bx \in \VV$ is coercive. 

Then the set $\prox_f(\bx)$ is nonempty and compact for any $\bx \in \VV$.
```

Recall from {prf:ref}`def-opt-coercive-function` that
a function $h$ is coercive if for every sequence $\{ \bx_n \}$
such that $ \lim_{k \to \infty} \| \bx_k \| = \infty$,
we have $\lim_{k \to \infty} h(\bx_k) = \infty$.

```{prf:proof}
Define:

$$
h(\bu) \triangleq f(\bu) +  \frac{1}{2} \| \bu - \bx \|^2.
$$

1. Then $\prox_f(\bx) = \underset{\bu \in \VV}{\argmin} h(\bu)$.
1. $h$ is a sum of two closed functions. Hence $h$ is a closed function
   due to {prf:ref}`res-ms-sum-closed-functions`.
1. It is given that $h$ is coercive.
1. $h$ is proper since $f$ is proper and $\frac{1}{2} \| \bu - \bx \|^2$
   is real valued.
1. Thus, $h$ is proper, closed and coercive.
1. Due to the Weierstrass' theorem ({prf:ref}`res-opt-weierstrass-theorem`),
   a proper, closed and coercive function $g$ has a nonempty
   and compact set of minimizers.
```

## Proximal Operator

Under suitable conditions, $\prox_f(\bx)$ is always a singleton
for every $\bx \in \VV$. Then the proximal mapping can be
thought of as a function $\prox_f : \VV \to \VV$ mapping
every point in $\VV$ to a proximal point.


```{prf:theorem} First prox theorem
:label: res-prox-first-prox-theorem

Let $f : \VV \to \RERL$ be a proper, closed and convex function. Then, $\prox_f(\bx)$ is
a singleton for every $\bx \in \VV$.  
```

```{prf:proof}
Define:

$$
h_{\bx}(\bu) \triangleq f(\bu) + \frac{1}{2} \| \bu - \bx \|^2.
$$

Then 

$$
\prox_f(\bx) = \underset{\bu \in \VV}{\argmin} h_{\bx}(\bu).
$$


1. $f$ is a closed and convex function.
1. $d_{\bx}(\bu) = \frac{1}{2} \| \bu - \bx \|^2$ is a closed and strongly convex function
   ({prf:ref}`res-cvxf-quadratic-strong-convex`).
1. Hence, their sum $h_{\bx}$ is a closed and strongly convex function
   ({prf:ref}`res-cvxf-sum-strong-convex-convex`).
1. Since $f$ is proper, and $d_{\bx}$ is real valued, hence $h_{\bx}$ is also proper.
1. Thus, $h_{\bx}$ is a proper, closed and strongly convex function.
1. Due to {prf:ref}`res-cvxf-strong-convex-minimizer`,
   there exists a unique minimizer for $h_{\bx}$. 
1. Thus, the set $\prox_f(\bx) = \argmin h_{\bx}(\bu)$ is a singleton.
```

With this result, we are ready to introduce the proximal operator.

```{prf:definition} Proximal operator
:label: def-prox-proximal-operator

Let $f : \VV \to \RERL$ be a proper, closed and convex function. Since 
the point to set mapping $\prox_f : \VV \to 2^{\VV}$ maps 
every point in $\VV$ to a singleton subset of $\VV$
due to {prf:ref}`res-prox-first-prox-theorem`, we abuse
the notation and redefine $\prox_f: \VV \to \VV$ as a point to
point mapping. We call this mapping as a *proximal operator* of $f$. 

In other words, we write $\prox_f(\bx) = \by$ rather than $\prox_f(\bx) = \{\by\}$.

Thus, for a proper, closed and convex function $f$,
the operator $\prox_f: \VV \to \VV$ maps each point
$\bx \in \VV$ to a unique minimizer of the
function $h_{\bx}(\bu) = f(\bu) + \frac{1}{2} \| \bu - \bx \|^2$.
```


## Simple Examples of Proximal Operators


### Affine

```{prf:example} Affine function
:label: ex-prox-affine

Let $f(\bx) = \langle \bx, \ba \rangle + b$ where $\ba \in \VV$ and $b \in \RR$.

$$
h_{\bx}(\bu) = \langle \bu, \ba \rangle + b + \frac{1}{2} \| \bu - \bx \|^2.
$$

1. Differentiating $h_{\bx}$, we get
   $\nabla h_{\bx}(\bu) = \ba + \bu - \bx$.
1. Setting it to zero, we see that $\bu = \bx - \ba$ is the minimizer.

Hence

$$
\prox_f(\bx) = \bx - \ba.
$$
```

### Convex Quadratic


```{prf:example} Convex quadratic
:label: ex-prox-convex-quadratic

Let $f : \RR^n \to \RR$ be given by
$f(\bx) = \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c$
where $\bA \in \SS^n_+$, $\bb \in \RR^n$ and $c \in \RR$.

$$
h_{\bx}(\bu) = \frac{1}{2} \bu^T \bA \bu + \bb^T \bu + c + \frac{1}{2} \| \bu - \bx \|^2.
$$

1. Differentiating $h_{\bx}$, we get

   $$
   \nabla h_{\bx}(\bu) = \bA \bu + \bb + \bu - \bx.
   $$
1. Setting this to zero, we see that

   $$
   & \bA \bu + \bb + \bu - \bx = \bzero\\
   \iff & (\bA + \bI) \bu = \bx - \bb \\
   \iff & \bu = (\bA + \bI)^{-1}(\bx - \bb).
   $$

Hence

$$
\prox_f(\bx) = (\bA + \bI)^{-1}(\bx - \bb).
$$
```

