(sec:proximal:intro)=
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
* The function $h_{\bx} : \VV \to \RR$ given by

  $$
  h_{\bx}(\bu) = f(\bu) + \frac{1}{2} \| \bu - \bx \|^2
  $$
  is the objective function for the computation of the proximal points
  for a given point $\bx \in \VV$.
* The proximal points of $\bx$ are the minimizers of the problem
  of unconstrained minimization of $h_{\bx}$.
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

This is a very simple example. The proximal point
for every point is the same point. 
Note that the gradient of the zero function
is zero everywhere. So every point in the
domain of $f$ is an optimal point from
the perspective of maximization or minimization.
Thus the proximal mapping doesn't need move
to a different point.

### Zero Everywhere Except at $x=0$ Functions

Let us look at real functions which are
zero everywhere except at $x=0$. 
There are two possibilities.
$f(x)$ is positive or negative at $x=0$.
The two examples below illustrate the
point to set nature of proximal mappings.
We show different situations where
the number of proximal points for a given
point is one, two or zero.


```{prf:example} Negative value at $x=0$
:label: ex-prox-map-neg-val-at-zero

Let $t > 0$.
Let $f: \RR \to \RR$ be given as

$$
f(x) = \begin{cases}
0 & x \neq 0;\\
- t & x = 0.
\end{cases}
$$

The proximal mapping is given by

$$
\prox_f(x) = \begin{cases}
\{ 0 \}, & |x| < \sqrt{2 t},\\
\{ x \} & |x| > \sqrt{2 t}, \\
\{ 0, x \} & | x | = \sqrt {2 t}.
\end{cases}
$$
```

This example clearly demonstrates the point to set mapping
nature of the proximal mapping. While for most values
of $x$, the proximal mapping is a singleton, but
for $|x| = \sqrt{ 2 t}$, the proximal mapping consists
of a set of two different values.

```{prf:proof}
We start by constructing the objective function

$$
h_x(u) = f(u) + \frac{1}{2} (u  - x )^2
= \begin{cases}
\frac{1}{2} (u  - x )^2 & u \neq 0;\\
- t + \frac{1}{2} x^2 & u = 0.
\end{cases}
$$

Consider the case where $x \neq 0$.

1. The minimum value of $\frac{1}{2} (u  - x )^2$ is $0$ attained at $u=x$
   and it is valid since $u = x \neq 0$.
1. The value of $- t + \frac{1}{2} x^2$ is attained at $u=0$.
1. There are three possibilities.
1. If $0 > - t + \frac{1}{2} x^2$, then the unique minimizer
   of $h_x$ is at $u=0$.
   The condition can be written as $|x| < \sqrt{2 t}$ and $x \neq 0$.
1. If $0 < - t + \frac{1}{2} x^2$, then the unique minimizer
   of $h_x$ is at $u=x$.
   The condition can be written as $|x| > \sqrt{2 t}$.
1. If $0 = - t + \frac{1}{2} x^2$, then $u=0$ and $u=x$ are
   both minimizers of $h_x$.
   The condition can be written as $|x| = \sqrt{2 t}$.

Now the case of $x=0$.

1. The term $- t + \frac{1}{2} x^2$ reduces to $-t < 0$ at $u=0$.
1. The term $\frac{1}{2}(u  - x )^2$ reduces to $\frac{1}{2} u^2 > 0$ for all $u \neq 0$.
1. Thus, the minimizer is at $u=0$.
1. We note that the minimizer agrees with the result obtained for the
   case of $|x| < \sqrt{2 t}$ above where $x \neq 0$.

In conclusion, we see that

1. For $|x | < \sqrt{2 t}$, the minimizer is $u=0$.
1. For $|x| > \sqrt{2 t}$, the minimizer is $u=x$.
1. For $|x| = \sqrt{2 t}$, there are two minimizers, $u=0$ and $u=x$.
```


```{prf:example} Positive value at $x=0$
:label: ex-prox-map-pos-val-at-zero

Let $t > 0$.
Let $f: \RR \to \RR$ be given as

$$
f(x) = \begin{cases}
0 & x \neq 0;\\
t & x = 0.
\end{cases}
$$

The proximal mapping is given by

$$
\prox_f(x) = \begin{cases}
\{ x \}, & x \neq 0;\\
\EmptySet & x = 0.
\end{cases}
$$
```

This example illustrates the fact that the proximal mapping
may be empty in some cases. In other words, for some points,
there are no proximal points.

```{prf:proof}
We start by constructing the function

$$
h_x(u) = f(u) + \frac{1}{2} (u  - x )^2
= \begin{cases}
\frac{1}{2} (u  - x )^2 & u \neq 0;\\
t + \frac{1}{2} x^2 & u = 0.
\end{cases}
$$

Consider the case where $x \neq 0$.

1. The minimum value of $\frac{1}{2} (u  - x )^2$ is $0$ attained at $u=x$
   and it is valid since $u = x \neq 0$.
1. The term $t + \frac{1}{2} x^2  > 0$ for $u=0$.
1. Thus the minimizer is at $u=x$ for all $x \neq 0$.

Now consider the case where $x=0$.

1. The function $h_x$ reduces to

   $$
   h_x(u) = \begin{cases}
      \frac{1}{2} u^2 & u \neq 0;\\
      t & u = 0.
      \end{cases}
   $$
1. We can see that $\inf_{u \in \RR} h_x(u) = 0$.
1. However, $h_x$ doesn't attain the value $0$ for any $u \in \RR$.
1. Hence, the set of minimizers is empty.


In conclusion, this function 

1. has a unique minimizer $u=x$ for all $x \neq 0$.
1. has no minimizer for $x=0$.
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

Readers are suggested to look at some of the
examples in the {ref}`sec:proximal:examples` below
before proceeding with the proximal calculus rules.

## Proximal Calculus

This section deals with the rules which enable
us to compute the proximal mappings for a function
if we know the proximal mappings of underlying
building blocks.

### Separable Functions

```{prf:theorem} Proximal mappings of separable functions
:label: res-prox-separable-func-mapping

Suppose that $f: \VV_1 \oplus \dots \oplus \VV_m \to \RERL$
is given by

$$
f(\bx_1, \dots, \bx_m) = \sum_{i=1}^m f_i(\bx_i) 
\Forall \bx_i \in \VV_i, \quad i=1,\dots, m.
$$

Then for every $\bx_1 \in \VV_1, \dots, \bx_m \in \VV_m$,

$$
\prox_f(\bx_1, \dots, \bx_m)
= \prox_{f_1}(\bx_1) \times \dots \times \prox_{f_m}(\bx_m).
$$
```

Note that the theorem is presented in terms of
sets. The L.H.S. $\prox_f(\bx_1, \dots, \bx_m)$ is a set.
Similarly, R.H.S. is a Cartesian product of proximal mappings
$\prox_{f_i}(\bx_i)$ which are individually sets.


```{prf:proof}
We start with the definition of the proximal mapping
and expand it in terms of the separable functions.
We note that the quadratic term
$\frac{1}{2} \| \cdot - \bx \|^2$ is also separable.


$$
\prox_f(\bx) &= \argmin_{\bu} \left \{
    f(\bu) + \frac{1}{2} \| \bu - \bx \|^2
    \right\} \\
&=  \argmin_{\bu_1, \dots, \bu_m} \left \{
    \sum_{i=1}^m f_i(\bu_i) + 
    \frac{1}{2} \sum_{i=1}^m \| \bu_i - \bx_i \|^2
    \right\} \\
&=  \argmin_{\bu_1, \dots, \bu_m} \left \{
    \sum_{i=1}^m \left (f_i(\bu_i) + 
    \frac{1}{2} \| \bu_i - \bx_i \|^2
     \right ) \right\} \\
&= \prod_{i=1}^m \argmin_{\bu_i}\left \{
   f_i(\bu_i) +  \| \bu_i - \bx_i \|^2 
   \right \}\\
&= \prod_{i=1}^m \prox_{f_i}(\bx_i).
$$
Here the $\prod$ symbol denotes the Cartesian product.
```

```{prf:corollary} Proximal operator for separable convex functions
:label: res-prox-op-separable-conv-func

Let $f: \RR^n \to \RERL$ be a proper, closed and convex function.
Assume that $\RR^n = \RR^{n_1} \oplus \dots \oplus \RR^{n_m}$
with $n = n_1 + \dots + n_m$.

Let $f$ be separable over $\RR^{n_1} \oplus \dots \oplus \RR^{n_m}$
and given by

$$
f(\bx_1, \dots, \bx_m) = \sum_{i=1}^m f_i(\bx_i) 
\Forall \bx_i \in \RR^{n_i}, \quad i=1,\dots, m.
$$
Further assume that $f_i$ are proper, closed and convex
functions themselves.

Then for every $\bx_1 \in \RR^{n_1}, \dots, \bx_m \in \RR^{n_m}$,

$$
\prox_f(\bx_1, \dots, \bx_m)
= (\prox_{f_1}(\bx_1), \dots, \prox_{f_m}(\bx_m)).
$$

In the special case, where $f$ is separable over each
coordinate; i.e.

$$
f(\bx) = \sum_{i=1}^n f_i(x_i)
$$

then

$$
\prox_f(\bx) = (\prox_{f_1}(x_1),\dots, \prox_{f_n}(x_n)).
$$
```

```{prf:proof}
Since $f$ and $f_i$ are proper, closed and convex, hence
due to {prf:ref}`res-prox-first-prox-theorem`,
the proximal mappings $\prox_f(\bx)$ and
$\prox_{f_i}(\bx_i)$ are singletons.
In this case, the Cartesian product reduces
to the concatenation of coordinates. 
```

Applications:
{prf:ref}`ex-prox-scaled-l1-norm`.


### Scaling and Translation

```{prf:theorem} Scaling and translation of input
:label: res-prox-input-scale-translate

Let $g: \VV \to \RERL$ be a proper function.
Let $t \neq 0$ be a scaling parameter and
$\ba \in \VV$ be a translation parameter.
Define $f: \VV \to \RERL$ as

$$
f(\bx) = g(t \bx + \ba).
$$ 

Then given $\prox_g$, the $\prox_f$ is

$$
\prox_f(\bx) = \frac{1}{t} [\prox_{t^2 g}(t \bx + \ba) - \ba].
$$
```

```{prf:proof}
Starting from the definition of the proximal mapping

$$
\prox_f(\bx) &= \argmin_{\bu \in \VV} \left \{
    f(\bu) + \frac{1}{2} \| \bu - \bx \|^2
    \right\} \\
&= \argmin_{\bu \in \VV} \left \{
    g(t \bu + \ba) + \frac{1}{2} \| \bu - \bx \|^2
    \right\}.
$$
1. The objective function of this minimization problem is

   $$
   g(t \bu + \ba) + \frac{1}{2} \| \bu - \bx \|^2.
   $$
1. We introduce a change of variable $\bz = t \bu + \ba$
   to construct an equivalent minimization problem.
   See {prf:ref}`res-opt-eq-form-change-variables` for the
   construction of equivalent optimization problems by change of variable.
1. Then $\bu = \frac{1}{t}(\bz - \ba)$.
1. The objective function changes to

   $$
   & g(\bz) + \frac{1}{2} \left \| \frac{1}{t}(\bz - \ba) - \bx \right \|^2 \\
   &= \frac{1}{t^2}\left [
   (t^2 g)(\bz) + \frac{1}{2} \left \| \bz - (t\bx + \ba) \right \|^2
   \right].
   $$
1. The minimizers of this objective function (over $\bz$) are given by

   $$
   \bz \in \prox_{t^2 g}(t \bx + \ba).
   $$
   Note that the scaling term $\frac{1}{t^2}$ in the objective function
   doesn't impact the set of minimizers. It only impacts the optimal value.
1. Since $\bu = \frac{1}{t}(\bz - \ba)$,
   hence minimizers of the original objective function are given by

   $$
   \bu \in \frac{1}{t} [\prox_{t^2 g}(t \bx + \ba) - \ba].
   $$
```


```{prf:theorem} Proximal mapping for $t g ( \cdot / t)$
:label: res-prox-in-out-same-scale

Let $g: \VV \to \RERL$ be a proper function.
Let $t \neq 0$ be a scaling parameter.
Define $f: \VV \to \RERL$ as

$$
f(\bx) = t g\left (\frac{\bx}{t} \right).
$$
Then

$$
\prox_f (\bx) = t \, \prox_{g / t} (\bx / t).
$$
```

```{prf:proof}
Starting from the definition of the proximal mapping

$$
\prox_f(\bx) &= \argmin_{\bu \in \VV} \left \{
    f(\bu) + \frac{1}{2} \| \bu - \bx \|^2
    \right\} \\
&= \argmin_{\bu \in \VV} \left \{
    t g\left (\frac{\bu}{t} \right ) + \frac{1}{2} \| \bu - \bx \|^2
    \right\}.
$$

1. The objective function is

   $$
   t g(\frac{\bu}{t}) + \frac{1}{2} \| \bu - \bx \|^2.
   $$
1. Introduce a change of variable $\bz = \frac{\bu}{t}$.
1. Then $\bu = t \bz$.
1. The objective function changes to

   $$
   & t g(\bz) + \frac{1}{2} \| t \bz - \bx \|^2 \\
   & = t^2 \left [
   \frac{g(\bz)}{t} + \frac{1}{2} \left \| \bz - \frac{\bx}{t} \right \|^2
   \right ].
   $$
1. The minimizers of this objective function are given by

   $$
   \bz \in \prox_{g / t} (\bx / t).
   $$
1. The minimizers of the original objective function are then given by

   $$
   \bu \in t \, \prox_{g / t} (\bx / t).
   $$
```


### Quadratic Perturbation


```{prf:theorem} Quadratic perturbation
:label: res-prox-quadratic-perturbation

Let $g: \VV \to \RERL$ be a proper function.
Define $f: \VV \to \RERL$ as

$$
f(\bx) = g(\bx) + \frac{c}{2} \| \bx \|^2 + \langle \bx, \ba \rangle + d
$$
where $c > 0$, $\ba \in \VV$ and $d \in \RR$.
Then

$$
\prox_f (\bx) = \prox_{\frac{1}{c+1} g} \left ( \frac{\bx - \ba}{ c + 1} \right ).
$$
```

```{prf:proof}
Starting from the definition of the proximal mapping

$$
\prox_f(\bx) &= \argmin_{\bu \in \VV} \left \{
    f(\bu) + \frac{1}{2} \| \bu - \bx \|^2
    \right\} \\
&= \argmin_{\bu \in \VV} \left \{
    g(\bu) + \frac{c}{2} \| \bu \|^2 + \langle \bu, \ba \rangle + d + \frac{1}{2} \| \bu - \bx \|^2
    \right\} \\
&= \argmin_{\bu \in \VV} \left \{
    g(\bu) + \frac{c+1}{2} \| \bu \|^2 + \langle \bu, \ba - \bx \rangle + \frac{1}{2} \| \bx \|^2 + d
    \right\} \\
&= \argmin_{\bu \in \VV} \left \{
    g(\bu) + \frac{c+1}{2} \left (\| \bu \|^2 - 
      2 \left \langle \bu, \frac{\bx - \ba}{c + 1} \right \rangle \right )
    \right\} \\
&= \argmin_{\bu \in \VV} \left \{
    g(\bu) + \frac{c+1}{2} \left \|\bu -  \left (\frac{\bx - \ba}{ c + 1} \right ) \right \|^2
    \right\}\\
&= \argmin_{\bu \in \VV} \left \{
    \left (\frac{1}{c + 1}g \right )(\bu) 
    + \frac{1}{2} \left \|\bu -  \left (\frac{\bx - \ba}{ c + 1} \right ) \right \|^2
    \right\}\\
&= \prox_{\frac{1}{c+1} g} \left ( \frac{\bx - \ba}{ c + 1} \right ).
$$

Since the quantities $\bx$, $\ba$ and $d$ are constant w.r.t. $\bu$, hence
we have removed or added terms which solely depend on these quantities
from the objective function as and
when required in the derivation above.
```

Applications: {prf:ref}`ex-prox-linear-z-a-interval`.


### Composition with Affine Mapping

```{prf:theorem} Composition with affine mapping
:label: res-prox-composition-affine

Let $g: \RR^m \to \RERL$ be a proper, closed and convex function.
Let $f: \VV \to \RERL$ be given by

$$
f(\bx) = g(\bAAA(\bx) + \bb)
$$
where $\bb \in \RR^m$  and $\bAAA : \VV \to \RR^m$ is a linear transformation
satisfying the property

$$
\bAAA \circ \bAAA^T = \alpha \bI 
$$
for some constant $\alpha > 0$ and $\bI: \VV \to \VV$
is the identity transformation.

Then for any $\bx \in \VV$,

$$
\prox_f(\bx) = \bx + \frac{1}{\alpha} \bAAA^T
(\prox_{\alpha g}(\bAAA(\bx) + \bb) - \bAAA(\bx) - \bb).
$$ 
```

```{prf:proof}
Starting from the definition of the proximal mapping

$$
\prox_f(\bx) &= \argmin_{\bu \in \VV} \left \{
    f(\bu) + \frac{1}{2} \| \bu - \bx \|^2
    \right\} \\
&= \argmin_{\bu \in \VV} \left \{
    g(\bAAA(\bu) + \bb) + \frac{1}{2} \| \bu - \bx \|^2
    \right\}.
$$

1. Introduce a variable $\bz = \bAAA(\bu) + \bb$.
1. The optimization problem transforms to

   $$
   & \min_{\bu \in \VV, \bz \in \RR^m} & g(\bz) + \frac{1}{2} \| \bu - \bx \|^2 \\
   & \text{ subject to } & \bz  = \bAAA(\bu) + \bb$.
   $$
1. Since $g$ is proper, closed and convex, hence this problem has a unique solution.
   TODO. HOW? 
1. Let the optimal solution be given by $\bz^* \bu^*$. 
```


(sec:proximal:examples)=
## Examples
Remainder of this section will be dedicated for the
computation of proximal mappings or operators
for different functions. Most of these functions
are convex (with the exception of a few).
The proximal mappings will be computed either
from the first principles (by solving the
minimization problem of $f(u) + \frac{1}{2}\| \bu - \bx \|^2$)
or by making use of the proximal calculus rules developed above.


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

## 1-dim Examples


### Indicator Functions

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

1. We construct the objective function

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

### Linear

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
   h_x(u) = = f(u) +  \frac{1}{2} (u - x)^2 
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


```{prf:example} Linear over an interval $[0, a]$
:label: ex-prox-linear-z-a-interval

Let $\mu \in \RR$ and let $a \in [0, \infty]$.
Let $f : \RR \to \RERL$ be given by

$$
f(x) = \begin{cases}
\mu x, & x \in [0, a]; \\
\infty, & \text{ otherwise}.
\end{cases}
$$

The proximal operator is given by

$$
\prox_f(x) = \min \{ \max \{x - \mu, 0 \}, a \}.
$$
```

```{prf:proof}
We note that

$$
f(x) = I_{[0,a] \cap \RR}(x) + \mu x.
$$

1. From {prf:ref}`ex-prox-indicator-interval`, the proximal operator for the
   indicator function is given by

   $$
   \prox_{I_{[0,a] \cap \RR}}(x) = \min \{ \max \{x, 0 \}, a \}.
   $$
1. We can write $f$ as a quadratic perturbation of $I_{[0,a] \cap \RR}$ given by

   $$
   f(x) = I_{[0,a] \cap \RR}(x) + \frac{0}{2} x^2 + \mu x + 0. 
   $$
1. Following {prf:ref}`res-prox-quadratic-perturbation`,

   $$
   \prox_f(x) = \prox_{I_{[0,a] \cap \RR}}(x - \mu)
   = \min \{ \max \{x - \mu, 0 \}, a \}.
   $$
```


### Absolute Value

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

### Cube

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

1. We construct the objective function

   $$
   h_x(u) = f(u) +  \frac{1}{2} (u - x)^2 
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


### Logarithms

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

1. We construct the objective function

   $$
   h_x(u) = f(u) +  \frac{1}{2} (u - x)^2 
   = \begin{cases}
   - t \ln u +  \frac{1}{2} (u - x)^2, & u > 0; \\
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


## Affine Functions

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

## Convex Quadratic Functions


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


## Norms

### $\ell_1$ Norm

```{prf:example} Scaled $\ell_1$ norm
:label: ex-prox-scaled-l1-norm

Let $\gamma > 0$.
Let $f : \RR^n \to \RR$ be given by

$$
f(\bx) = \gamma \| \bx \|_1 = \sum_{i=1}^n \gamma |x_i|.
$$

Then, the proximal operator is given by

$$
\prox_f(\bx) = \st_{\gamma}(\bx)
$$

where the univariate soft-thresholding operator 
$\st_{\gamma} : \RR \to \RR$ is defined as

$$
\st_{\gamma}(x) = \begin{cases}
 x - \gamma & \text{for} & x > \gamma \\
 x + \gamma & \text{for} & x < -\gamma \\
 0 & \text{for} & |x| \le \gamma
\end{cases}
$$

and the multivariate soft-thresholding operator
$\st_{\gamma} : \RR^n \to \RR^n$
is defined by the component wise application of
the univariate soft thresholding operator

$$
\st_{\gamma}(\bx) = (\st_{\gamma}(x_j))_{j=1}^n.
$$
```

```{prf:proof}
We note that 

$$
f(\bx) = \sum_{i=1}^n g(x_i)
$$
where $g(x) = \gamma | x|$.

By {prf:ref}`ex-prox-scaled-abs-value`,

$$
\prox_g(x) =  [|x| - \gamma]_+ \sgn (x)
= \st_{\gamma}(x).
$$

By {prf:ref}`res-prox-op-separable-conv-func`,

$$
\prox_f(\bx) = (\st_{\gamma}(x_i))_{i=1}^n
= \st_{\gamma}(\bx).
$$
```

### $\ell_0$ "Norm"

```{prf:example} Scaled $\ell_0$ "norm"
:label: ex-prox-scaled-l0-norm

Let $\gamma > 0$.
Let $f : \RR^n \to \RR$ be given by

$$
f(\bx) = \gamma \| \bx \|_0 = \sum_{i=1}^n  g(x_i)
$$
where

$$
g(x) = \begin{cases}
\gamma, & x \neq 0;\\
0, & x = 0.
\end{cases} 
$$

Then, the proximal operator is given by

$$
\prox_f(\bx) = \HHH_{\sqrt{2\gamma}}(x_1) \times \dots 
\times \HHH_{\sqrt{2\gamma}}(x_n)
$$

where the univariate hard-thresholding operator 
$\HHH_{t} : \RR \to 2^{\RR}$
for any $t > 0$ is defined as

$$
\HHH_t(x) = \begin{cases}
 \{ 0 \} & |x| < t \\
 \{ x \} &  |x| > t \\
 \{0, x \} & |x| = t
\end{cases}.
$$
```
Note this this version of hard thresholding
operator is a point to set mapping. In this
case, the operator leads to two possible
values when $|x| = t$.
The $\ell_0$-"norm" is not a convex function.
Hence its proximal mapping is not always
a singleton.

```{prf:proof}
We note that $g(x) = h(x) + \gamma$

where

$$
h(x) = \begin{cases}
0, & x \neq 0;\\
-\gamma, & x = 0.
\end{cases} 
$$

1. Following {prf:ref}`ex-prox-map-neg-val-at-zero`,


   $$
  \prox_h(x) = \begin{cases}
  \{ 0 \}, & |x| < \sqrt{2 \gamma},\\
  \{ x \} & |x| > \sqrt{2 \gamma}, \\
  \{ 0, x \} & | x | = \sqrt {2 \gamma}.
  \end{cases}
  $$
1. Since the proximal operator is not affected by a constant offset,
   hence $\prox_g = \prox_h$.
1. We can see that $\prox_g = \HHH_{\sqrt{2 \gamma}}$.
1. It is clear that the proximal mappings are not unique.
1. By {prf:ref}`res-prox-separable-func-mapping`,
   
   $$
   \prox_f(\bx) = \prox_g(x_1) \times \dots \times \prox_g(x_n)
   = \HHH_{\sqrt{2\gamma}}(x_1) \times \dots 
    \times \HHH_{\sqrt{2\gamma}}(x_n)
   $$
   as desired.
```


## Logarithms

```{prf:example} Negative sum of logs
:label: ex-prox-neg-sum-log

Let $\gamma > 0$.
Let $f : \RR^n \to \RERL$ be given by

$$
f(\bx) = \begin{cases}
- \gamma\sum_{i=1}^n  \ln x_i & \bx \succ \bzero;\\
\infty & \text{ otherwise }.
\end{cases}
$$

Then, the proximal operator is given by

$$
\prox_f(\bx) = \left (
   \frac{x_i + \sqrt{x_i^2 + 4 \gamma} }{2}
   \right)_{i=1}^n.
$$
```


```{prf:proof}
We note that 

$$
f(\bx) = \sum_{i=1}^n g(x_i)
$$
where

$$
g(x) =  \begin{cases}
- \gamma \ln x, & x > 0; \\
\infty, & x \leq 0.
\end{cases}
$$

From {prf:ref}`ex-prox-scaled-neg-log`,

$$
\prox_g(x) = \frac{x + \sqrt{x^2 + 4 t} }{2}.
$$

By {prf:ref}`res-prox-op-separable-conv-func`,

$$
\prox_f(\bx) = (\prox_g(x_i))_{i=1}^n.
$$
```
