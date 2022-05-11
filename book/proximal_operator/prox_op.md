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

## 1-dim Examples of Proximal Operators

Some key ideas that will be repeatedly used in the computation 
of the proximal operator in this section.
Assume that $f$ is a convex function with $S = \dom f$
and is differentiable over an open set $U \subseteq S$.
This happens when $\dom f$ is not an open set,
$f$ is differentiable in the interior of $\dom f$
but not at the boundary points.

1. if $f'(u) = 0$ for some $u \in U$, then $u$ must
   be one of its minimizers 
   ({prf:ref}`res-cvxopt-diff-zero-grad-minimizer`).
1. If a minimizer of $f$ exists and is not attained
   at any point of differentiability, then it
   must be attained at a point of nondifferentiability
   ({prf:ref}`res-cvxopt-minimizer-nondifferentiability`).
1. Since for a convex function $f$, the existence of a
   unique proximal mapping is guaranteed, hence
   the minimizer of the function $h_{\bx}$ exists.
1. Then the minimizer of $h_{\bx}$ is either
   at a point of differentiability where the
   gradient vanishes or at the boundary where
   it is nondifferentiable.

```{prf:example} Linear over $\RR_+$
:label: ex-prox-linear-rplus

Let $\mu \in \RR$.
Let $f : \RR \to \RERL$ be given by

$$
f(x) = \begin{cases}
\mu x, & x \geq 0; \\
\infty, & x < 0.
\end{cases}
$$

The proximal operator is given by

$$
\prox_f(x) = [x - \mu]_+.
$$
```
```{prf:proof}
.

1. $\dom f = \RR_+$.
1. $f$ is differentiable over $\RR_{++}$.
1. Let 
   
   $$
   h_x(u) = = f_x(u) +  \frac{1}{2} (u - x)^2 
   = \begin{cases}
   \mu u + \frac{1}{2} (u - x)^2, & u \geq 0; \\
   \infty, & u < 0.
   \end{cases}
   $$
1. $h_x$ is a proper convex function with $\dom h_x = \RR_+$.
1. $h_x$ is differentiable over $\RR_{++}$.
1. $h'_x(u) = \mu + u - x$ for all $u > 0$.
1. Setting it to zero, we get $u = x - \mu$.
1. Thus, if $x > \mu$, then the minimizer is $u = x - \mu$.
1. Otherwise, $h_x$ obtains its minimum value at $u=0$
   which is the only point of nondifferentiability in its domain.
1. Thus, if $x \leq \mu$, then the minimizer is $u=0$.
```

```{prf:example} Scaled absolute value
:label: ex-prox-scaled-abs-value

Let $t \in \RR_+$.
Let $f : \RR \to \RR$ be given by

$$
f(x) = t | x |.
$$

The proximal operator is given by

$$
\prox_f(x) = [|x| - t]_+ \sgn (x).
$$
```
```{prf:proof}
.

1. Let

   $$
   h_x(u) = t | u | +  \frac{1}{2} (u - x)^2.
   $$
1. $h_x$ is differentiable everywhere except at $u = 0$.
1. At $u \neq 0$, $h'_x(u) = \sgn(u) t + u - x$.
1. If the minimizer is obtained at $u > 0$, then
   $t + u - x = 0$ giving us $u= x -t$.
1. Thus, a minimizer at $u > 0$ is attained if $x > t$.
1. If the minimizer is obtained at $u < 0$, then
   $-t + u - x = 0$ giving us $u = x + t$.
1. Thus, a minimizer at $u < 0$ is attained if $x < -t$.
1. Consequently, if $x \in [-t, t]$, then the
   minimizer of $h_x$ must be at the only point of
   nondifferentiability, namely $u=0$.
1. This gives us

   $$
   \prox_f(x) = \begin{cases}
   x - t, & x > t\\
   x + t, & x < -t \\
   0, &  -t \leq x \leq t.
   \end{cases}
   $$
1. The conditions $x > t$ and $x < -t$
   can be combined as $|x| > t$.
1. The condition $-t \leq x \leq t$ simplifies
   to $|x| \leq |t|$.
1. We can see that the three cases for $\prox_f(x)$
   can be simplified to the expression

   $$
   \prox_f(x) = [|x| - t]_+ \sgn (x).
   $$
```

```{prf:example} Scaled cube over $\RR_+$
:label: ex-prox-scaled-cube-plus

Let $t > 0$.
Let $f : \RR \to \RERL$ be given by

$$
f(x) = \begin{cases}
t x^3, & x \geq 0; \\
\infty, & x < 0.
\end{cases}
$$

The proximal operator is given by

$$
\prox_f(x) = \frac{-1 + \sqrt{1 + 12 t [x]_+}}{6 t}.
$$
```
```{prf:proof}
.

1. We construct the auxiliary function

   $$
   h_x(u) = f_x(u) +  \frac{1}{2} (u - x)^2 
   = \begin{cases}
   t u^3 +  \frac{1}{2} (u - x)^2, & u \geq 0; \\
   \infty, & u < 0.
   \end{cases}
   $$
1. $h_x$ is differentiable for $u > 0$.
1. $h'_x(u) = 3 t u^2 + u - x$ for $u > 0$.
1. Note that if $x \leq 0$ then
   $h'_x(u) > 0$ for every $u > 0$.
1. Hence $h'_x(u) = 0$ does not have a positive
   root for $x \leq 0$.
1. For $x > 0$, setting $h_x(u)$ to zero,
   we get $3 u^2 + u - x = 0$
   whose positive solution is:

   $$
   u = \frac{-1 + \sqrt{1 + 12 t x}}{6 t}.
   $$
1. We can see that $h'_x(u) = 0$ has a
   positive solution if and only if $x > 0$.
1. If $x \leq 0$, then the derivative never
   vanishes for any $u > 0$.
1. Hence the minimum of $h_x$ is attained
   at the only point of nondifferentiability
   $u=0$.
1. Thus, the minimizer of $h_x(u)$ for $x \leq 0$
   is $u=0$.
1. Hence

   $$
   \prox_f(x) = \begin{cases}
   \frac{-1 + \sqrt{1 + 12 t x}}{6 t}, & x > 0 \\
   0, & x \leq 0.
   \end{cases}
   $$
1. Note that 
   
   $$
   \frac{-1 + \sqrt{1 + 12 t [x]_+}}{6 t}= \begin{cases}
   \frac{-1 + \sqrt{1 + 12 t x}}{6 t}, & x > 0 \\
   0, & x \leq 0.
   \end{cases}
   $$
1. This concludes the proof.
```

```{prf:example} Scaled negative logarithm
:label: ex-prox-scaled-neg-log

Let $t > 0$.
Let $f : \RR \to \RERL$ be given by

$$
f(x) = \begin{cases}
- t \ln x, & x > 0; \\
\infty, & x \leq 0.
\end{cases}
$$

The proximal operator is given by

$$
\prox_f(x) = \frac{x + \sqrt{x^2 + 4 t} }{2}.
$$
```

```{prf:proof}
.

1. We construct the auxiliary function

   $$
   h_x(u) = f_x(u) +  \frac{1}{2} (u - x)^2 
   = \begin{cases}
   - t \ln x +  \frac{1}{2} (u - x)^2, & u > 0; \\
   \infty, & u \leq 0.
   \end{cases}
   $$
1. $h_x$ is differentiable for $u > 0$.
1. $h'_x(u) = - \frac{t}{u} + (u - x)$ for $u > 0$.
1. $\tilde{u} > 0$ is a minimizer if

   $$
   & - \frac{t}{\tilde{u}} + (\tilde{u} - x) = 0 \\
   & \implies \tilde{u}^2 - x \tilde{u} -t = 0 \\
   & \implies \tilde{u} = \frac{x + \sqrt{x^2 + 4 t}}{2}.
   $$
1. We note that $x + \sqrt{x^2 + 4 t} > 0$ for every $x \in \RR$.
1. Hence $\tilde{u} > 0$ as desired.
1. Hence $\prox_f(x) = \frac{x + \sqrt{x^2 + 4 t}}{2}$.

As we can see, $\dom h_x$ is the open set $\RR_{++}$
and $h_x$ is differentiable at every point in its
domain. Since $h_x$ must have a unique minimizer,
hence $h'_x(u) = 0$ must have a unique positive solution.
```


```{prf:example} Indicator function for an interval
:label: ex-prox-indicator-interval

Let $r \in [0, \infty]$.
Let $f : \RR \to \RERL$ be given by

$$
f(x) = I_{[0,r] \cap \RR}(x).
$$

The proximal operator is given by

$$
\prox_f(x) = \min \{ \max \{x, 0 \}, r \}.
$$
```

```{prf:proof}
.

1. Let

   $$
   h_x(u) = I_{[0,r] \cap \RR}(x) +  \frac{1}{2} (u - x)^2.
   $$
1. Let $\tilde{u}$ denote the minimizer of $h_x(u)$.
1. Let $w$ denote the function $w(u) =  \frac{1}{2} (u - x)^2$.
1. First consider the case where $r < \infty$.
1. Then $h_x(u) = w(u)$ over $[0, r]$ and $\infty$ otherwise.
1. $\dom h_x = [0, r]$. $\interior \dom h_x = (0, r)$.
   The boundary points are $0$ and $r$.
1. The minimizer of $w(u)$ is $u = x$.
1. Therefore if $0 \leq x \leq r$, then $\tilde{u} = x$.
1. For the cases where $x \notin [0, r]$, the minimizer
   must be one of the boundary points.
1. If $x < 0$, then $w(u)$ is an increasing function over
   $[0, r]$.
1. Hence for $x < 0$, $\tilde{u} = 0$.
1. If $x > r$, then $w(u)$ is a decreasing function over $[0,r]$.
1. Hence for $x > r$, $\tilde{u} = r$.
1. Thus, if $r < \infty$, then the proximal operator
   is given by

   $$
   \prox_f(x) = \begin{cases}
   x, & 0 \leq x \leq r \\
   0, & x < 0 \\
   r, & x > r
   \end{cases}
   = \min \{ \max \{x, 0 \}, r \}.
   $$
1. For $r = \infty$, $f(x) = I_{[0, \infty)}(x)$.
1. Thus, $h_x(u) = w(u)$ for $u \geq 0$.
1. Hence the minimizer $\tilde{u} = x$ for $x \geq 0$ and
   $\tilde{u} = 0$ for $x < 0$.
1. In other words, 

   $$
   \prox_f(x) = [x]_+ = \max\{x, 0\}
   = \min \{ \max \{x, 0 \}, \infty \}.
   $$
1. Combining these two cases

   $$
   \prox_f(x) = \min \{ \max \{x, 0 \}, r \}.
   $$
```


## n-dim Examples of Proximal Operators




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

