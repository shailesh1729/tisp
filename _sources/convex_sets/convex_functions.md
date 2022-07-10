(sec:cvxf:convex-functions)=
# Convex Functions

Throughout this section, we assume that $\VV, \WW$ are 
real vector spaces. Wherever necessary, 
they are equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \|$
or an {prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle$. 
They are also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$
as needed.


We suggest the readers to review the notions
of graph, epigraph, sublevel sets of real
valued functions in {ref}`sec:bra:real-valued-functions`.
Also pay attention to the notion of extended real valued
functions, their effective domains, graphs and level sets.

## Convexity of a Function

```{index} Convex function
```
````{prf:definition} Convex function
:label: def-convex-function

Let $\VV$ be a real vector space.
A real valued function $f: \VV \to \RR$ is *convex* if 
$\dom f$ is a convex set and for all $\bx_1,\bx_2 \in \dom f$, 
and $t \in [0, 1]$, we have:

```{math}
:label: eq-convexity-inequality
f(t \bx_1 + (1-t) \bx_2) \leq t f(\bx_1) + (1-t) f(\bx_2).
```

An extended valued function $f : \VV \to \ERL$ is *convex*
if $\dom f$ is a convex set and for every $\bx_1,\bx_2 \in \VV$, 
and $t \in [0, 1]$, we have:

$$
f(t \bx_1 + (1-t) \bx_2) \leq t f(\bx_1) + (1-t) f(\bx_2).
$$
````



```{figure} ../images/convex_function.png
---
name: convex_function_2
---
Graph of a convex function. The line segment
between any two points on the graph lies 
above the graph.
```

For a convex function, every chord lies above the graph of the function. 

### Strictly Convex Functions

```{index} Convex function; strict
```
```{prf:definition} Strictly convex function
:label: def-strictly-convex-function

Let $\VV$ be a real vector space.
A convex function $f: \VV \to \RR$ is *strictly convex* 
if for all $\bx_1,\bx_2 \in \dom f$, 
where $\bx_1$ and $\bx_2$ are distinct, 
and $t \in (0, 1)$, we have:

$$
f(t \bx_1 + (1-t) \bx_2) < t f(\bx_1) + (1-t) f(\bx_2).
$$
In other words, the inequality is a strict inequality 
whenever the point $\bx = t \bx_1 + (1-t) \bx_2$ is
distinct from $\bx_1$ and $\bx_2$ both.
```

### Concave Functions

```{index} Concave function
```
```{prf:definition} Concave function
:label: def-concave-function

We say that a function $f$ is *concave* if $-f$ is convex.
A function $f$ is *strictly concave* if $-f$ is 
strictly convex.
```


```{prf:example} Linear functional
:label: ex-cvxf-linear-functional

A *linear functional* on $\VV$ in an inner product space 
has the form of an inner product parameterized by 
a vector $\ba \in \VV$ as 

$$
f_{\ba} (\bx) \triangleq \langle \bx, \ba \rangle \Forall \bx \in \VV.
$$
i.e. the inner product of $\bx$ with $\ba$.
```

```{prf:theorem}
:label: res-cvxf-linear-functional-convex

All linear functionals on a real vector space are convex as well as concave.
```
```{prf:proof}
For any $\bx, \by \in \VV$ and $t \in [0,1]$:

$$
f_{\ba} (t \bx + (1-t) \by)
&= \langle t \bx + (1-t) \by, \ba \rangle \\
&= t \langle \bx, \ba \rangle +   (1-t)\langle \bx, \ba \rangle
\quad \text{inner products are linear}\\
&= t f_{\ba} (\bx) + (1-t) f_{\ba} (\by).
$$
Thus, $f_{\ba}$ is convex. We can also see that $-f_{\ba}$ is 
convex too. Hence, $f_{\ba}$ is concave too.
```

### Arithmetic Mean

```{prf:example} Arithmetic mean is convex and concave
:label: ex-cvxf-arithmetic-mean

Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) = \frac{x_1 + \dots + x_n}{n}.
$$

Arithmetic mean is a linear function. In fact

$$
f(\alpha \bx + \beta \by) 
&= \frac{1}{n} \left (\sum_{i=1}^n (\alpha x_i + \beta y_i) \right )\\
&= \alpha \frac{x_1 + \dots + x_n}{n} + \beta \frac{y_1 + \dots + y_n}{n}\\
&= \alpha f(\bx) + \beta f(\by)
$$
for all $\alpha,\beta \in \RR$.

Thus, for $t \in [0,1]$

$$
f(t \bx + (1-t) \by) = t f(\bx) + (1-t) f(\by).
$$
Thus, arithmetic mean is both convex and concave.
```

### Affine Function

```{prf:example} Affine functional
:label: ex-cvxf-affine-func-1

An *affine functional* is a special type of 
{prf:ref}`affine function <def-la-affine-operator>`
which maps a vector from $\VV$ to a scalar in 
the associate field $\FF$.


On real vector spaces, an *affine functional* on $\VV$ 
is defined in terms of 
a vector $\ba \in \VV$ and a scalar $b \in \RR$ as 

$$
f_{\ba, b} (\bx) \triangleq \langle \bx, \ba \rangle + b \Forall \bx \in \VV
$$
i.e. the inner product of $\bx$ with $\ba$ followed by a translation
by the amount of $b$.
```


```{prf:theorem} 
:label: res-cvxf-affine-functional-convex

All affine functionals on a real vector space are convex as well as concave.
```
```{prf:proof}
A simple way to show this is to recall that for any 
{prf:ref}`affine function <def-la-affine-operator>` $T$,

$$
T (t \bx + (1 - t) \by) = t T(\bx) + (1 - t) T(\by)
$$ 
holds true for any $\bx, \by \in \VV$ and $t \in \FF$.

In the particular case of real affine functionals,
for any $\bx, \by \in \VV$ and $t \in [0,1]$, the
previous identity reduces to:

$$
f_{\ba, b} (t \bx + (1 - t) \by) = t f_{\ba, b}(\bx) + (1 - t) f_{\ba, b}(\by).
$$ 
This establishes that $f_{\ba, b}$ is both convex and concave.

Another way to prove this is by following the definition 
of $f_{\ba, b}$ above:

$$
f_{\ba, b} (t \bx + (1 - t) \by) 
&= \langle t \bx + (1 - t) \by, \ba \rangle + b\\
&= t \langle \bx, \ba \rangle +   (1-t)\langle \bx, \ba \rangle + b\\
&= t \langle \bx, \ba \rangle +   (1-t)\langle \bx, \ba \rangle + tb + (1-t)b\\
&= (t \langle \bx, \ba \rangle +  + tb) +  ((1-t)\langle \bx, \ba \rangle + (1-t)b)\\
&= t (\langle \bx, \ba \rangle + b) +  (1-t)(\langle \bx, \ba \rangle + b)\\
&= t f_{\ba, b}(\bx) + (1-t) f_{\ba, b} (\by).
$$
```

### Absolute Value

````{prf:example} Absolute value is convex
:label: ex-cvxf-real-abs

Let $f : \RR \to \RR$ be:

$$
f(x) = |x|.
$$
with $\dom f = \RR$.

```{figure} images/func_abs_value_1d.png
---
name: cvx:func:abs:value
---
```

Recall that $|x|$ is a norm on the real line $\RR$. 
Thus, it satisfies the triangle inequality:

$$
|x + y | \leq |x | + |y| \Forall x, y \in \RR.
$$

In particular, for any $t \in [0,1]$

$$
|t x + (1-t)y | \leq |t x | + | (1- t) y| 
= |t| | x| + |1 - t| | y |
= t |x| + (1-t) | y |.
$$

Thus $f$ satisfies the convexity defining inequality 
{eq}`eq-convexity-inequality`: 

$$
f(t x + (1-t) y) \leq t f(x) + (1- t) f(y) \Forall x, y \in \RR.
$$
Hence, $f$ is convex.
````

### Norms

```{prf:theorem} All norms are convex
:label: res-cvxf-norms-convex

Let $\| \cdot \| : \VV \to \RR$ be a 
{prf:ref}`norm <def-la-norm>` on a real vector space $\VV$.
Then, it satisfies the triangle inequality:

$$
\|\bx + \by \| \leq \|\bx \| + \|\by\| \Forall \bx, \by \in \VV.
$$

In particular, for any $t \in [0,1]$

$$
\|t \bx + (1-t)\by \| \leq \|t \bx \| + \| (1- t) \by\| 
= |t| \| \bx \| + |1 - t| \| \by \|
= t \|\bx \| + (1-t) \| \by \|.
$$

Thus $f$ satisfies the convexity defining inequality 
{eq}`eq-convexity-inequality`. 
Hence, $f$ is convex.
```

```{figure} images/func_l2_norm_r2_contour3d.png
---
name: cvx:func:l2:norm:contour:3d
---
$\ell_2$ norm for $\RR^2$. $\| \cdot \|_2 : \RR^2 \to \RR$ 3D contour plots.
```
```{figure} images/func_l2_norm_r2_contour2d.png
---
name: cvx:func:l2:norm:contour:2d
---
$\ell_2$ norm for $\RR^2$. $\| \cdot \|_2 : \RR^2 \to \RR$ 2D contour plots.
```

```{figure} images/func_l1_norm_r2_contour3d.png
---
name: cvx:func:l1:norm:contour:3d
---
$\ell_1$ norm for $\RR^2$. $\| \cdot \|_1 : \RR^2 \to \RR$ 3D contour plots.
```
```{figure} images/func_l1_norm_r2_contour2d.png
---
name: cvx:func:l1:norm:contour:2d
---
$\ell_1$ norm for $\RR^2$. $\| \cdot \|_2 : \RR^1 \to \RR$ 2D contour plots.
```

### Max Function

```{prf:example} Max function is convex
:label: ex-cvxf-euclidean-n-max

Let $f : \RR^n \to \RR$ be:

$$
f(\bx) = \max \{x_1, \dots, x_n \}.
$$
with $\dom f = \RR^n$.


Let $\bx, \by \in \RR^n$ and $t \in [0,1]$.

1. Let $x = f(\bx) = \max \{ x_1, \dots, x_n \}$ and $y =  f(\by) = \max \{ y_1, \dots, y_n\}$.
1. Then, for every $k=1,\dots,n$, we have: $x_k \leq x$ and $y_k \leq y$.
1. Thus, $t x_k + (1-t) y_k \leq t x + (1-t) y$.
1. Taking maximum on the left hand side, we obtain:

   $$
   \max_{k=1}^n (t x_k + (1-t) y_k) \leq t x  + (1-t) y.
   $$
1. But $f(t \bx + (1-t) \by ) = \max_{k=1}^n (t x_k + (1-t) y_k)$.
1. Thus, $f$ satisfies the convexity defining
   inequality {eq}`eq-convexity-inequality`:

   $$
   f(t \bx + (1-t) \by ) \leq t f(\bx) + (1-t) f(\by).
   $$
1. Thus, $f$ is convex.
```

### Geometric Mean

```{prf:example} Geometric mean is concave
:label: ex-cvxf-geom-mean

Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) =  \left ( \prod_{i=1}^n x_i \right )^{\frac{1}{n}}
$$
with $\dom f = \RR^n_{++}$.


Recall from
{prf:ref}`AM-GM inequality <res-bra-unweighted-am-gm-inequality>`:

$$
\left (\prod_{i=1}^n a_i \right )^{\frac{1}{n}} \leq 
\frac{1}{n} \left ( \sum_{i=1}^n a_i \right ).
$$

1. Let $\bx, \by \in \RR^n_{++}$ and $t \in [0,1]$.
1. Let $\bz = t \bx + (1-t) \by$. 
1. Note that $\bz \in \RR^n_{++}$ too, hence every component
   of $\bz$ is positive.
1. With $a_i  = \frac{x_i}{z_i}$, and applying
   AM-GM inequality:

   $$
   \frac{f(\bx)}{f(\bz)} = \left ( \prod_{i=1}^n \frac{x_i}{z_i} \right )^{\frac{1}{n}}
   \leq \frac{1}{n} \left ( \sum_{i=1}^n \frac{x_i}{z_i} \right ).
   $$
1. With $a_i  = \frac{y_i}{z_i}$, and applying
   AM-GM inequality:

   $$
   \frac{f(\by)}{f(\bz)} = \left ( \prod_{i=1}^n \frac{y_i}{z_i} \right )^{\frac{1}{n}}
   \leq \frac{1}{n} \left ( \sum_{i=1}^n \frac{y_i}{z_i} \right ).
   $$
1. Multiplying the first inequality by $t$ and the second by $(1-t)$ and
   adding them, we get:

   $$
   \frac{t f(\bx) + (1-t) f(\by)}{f(\bz)} \leq
   \frac{1}{n} \left ( \sum_{i=1}^n\frac{t x_i}{z_i} +  \frac{(1-t) y_i}{z_i} \right ).
   $$
1. Recall that $z_i = t x_i + (1-t) y_i$. Thus, the inequality above simplifies to:

   $$
   &\frac{t f(\bx) + (1-t) f(\by)}{f(\bz)} \leq 1 \\
   &\iff t f(\bx) + (1-t) f(\by) \leq f(\bz) = f(t \bx + (1-t) \by).
   $$
1. Thus, $f$ is concave.
```

### Powers 

```{prf:example} Powers of absolute value
:label: ex-cvxf-real-power-absolute-x-p


Let $f : \RR \to \RR$ be:

$$
f(x) = |x|^p
$$
with $\dom f = \RR$.

For $p=1$, the absolute value function $f(x) = |x|$ is convex.

Consider the case where $p > 1$. Let $q$ be its conjugate
exponent given by $\frac{1}{p} + \frac{1}{q} = 1$.

Let $x, y \in \RR$ and $s, t \in (0, 1)$ with $s + t= 1$.

1. By triangle inequality:
   
   $$
   | s x + t y | \leq  s | x| + t |y|.
   $$
1. We can write this as:

   $$
   s | x| + t |y|
   = \left ( s^{\frac{1}{p}} |x| \right ) s^{\frac{1}{q}} 
   + \left ( t^{\frac{1}{p}} |y| \right ) t^{\frac{1}{q}}.
   $$

1. By {prf:ref}`Hölder's inequality <res-bra-holder-inequality>`,
   for some $a_1, a_2, b_1, b_2 \geq 0$

   $$
   a_1 b_1 + a_2 b_2 \leq (a_1^p + a_2^p)^{\frac{1}{p}} 
   + (b_1^q + b_2^q)^{\frac{1}{q}}. 
   $$

1. Let $a_1 = s^{\frac{1}{p}} |x|$, $a_2 =  t^{\frac{1}{p}} |y|$,
   $b_1 = s^{\frac{1}{q}}$ and $b_2 = t^{\frac{1}{q}}$.
1. Applying Hölder's inequality,

   $$
   | s x + t y | 
   \leq s | x| + t |y| 
   \leq (s |x|^p + t |y|^p)^{\frac{1}{p}} (s + t)^{\frac{1}{q}}
   = (s |x|^p + t |y|^p)^{\frac{1}{p}}.
   $$
1. Taking power of $p$ on both sides, we get:

   $$
   | s x + t y |^p \leq s |x|^p + t |y|^p.
   $$
1. Which is the same as
   
   $$
   f(s x + t y) \leq s f(x) + t f(y).
   $$
1. Thus, $f$ is convex.
```


### Empty Function

```{prf:observation} Empty function is convex
:label: res-cvxf-empty-func-convex

Let $f: \VV \to \RR$ be such that $\dom f = \EmptySet$.
Then $f$ is convex.
```

```{prf:proof}
The empty set $\dom f$ is vacuously convex. 
The defining inequality {eq}`eq-convexity-inequality`
is vacuously true for $f$ since its domain is empty.
```

This observation may sound uninteresting however
it is important in the algebra of convex functions.
{prf:ref}`def-bra-rvpf-algebra` provides
definitions for sum of two partial functions
and scalar multiplication with a partial
function. If two convex functions $f$ and $g$
are such that $\dom f \cap \dom g = \EmptySet$,
then their sum $f+g$ is empty function. 
The observation above says that $f+g$ is still
a convex function.


{prf:ref}`Jensen's inequality <res-cvxf-jensen-inequality>`,
discussed later in the section, generalizes the notion of
convexity of a function to arbitrary convex combinations
of points in its domain.

## Convexity on Lines in Domain

```{prf:theorem} $f$ is convex = $f$ is convex on lines in domain
:label: res-cvxf-convx-on-lines

Let $\VV$ be a real vector space.
A function $f : \VV \to \RR$ is convex if and only if for any
$\bx \in \dom f$ and any $\bv \in \VV$, the function 
$g(t) = f(\bx + t\bv)$ is convex (on its domain
    , $\{ t \in \RR \ST \bx + t\bv \in \dom f\}$).

In other words, $f$ is convex if and only if 
it is convex when restricted to any line that
intersects its domain.
```

```{prf:proof} 
For any arbitrary $f$, and for any 
$\bx \in \dom f, \bv \in \VV$  
we have defined $g : \RR \to \RR$ as:

$$
g(t)  \triangleq f(\bx + t\bv)
$$
with the domain:

$$
\dom g = \{t \ST \bx + t \bv \in \dom f\}.
$$

Assume $f$ to be convex. To show that $g$ is convex,
we need to show that $\dom g$ is convex and $g$
satisfies the convexity inequality.


1. Let $t_1, t_2 \in \dom g$.
1. It means that there are $\by = \bx + t_1 \bv \in \dom f$ 
   and $\bz = \bx + t_2 \bv \in \dom f$,
1. and $g(t_1) = f(\by)$ and $g(t_2) = f(\bz)$.
1. Let $r \in [0,1]$ and $t = rt_1 + (1-r)t_2$.
1. Note that:
   
   $$
   \bx + t \bv 
   &= \bx + (rt_1 + (1-r)t_2) \bv\\
   &= r\bx + (1-r)\bx + rt_1 \bv + (1-r)t_2 \bv\\
   &= r (\bx + t_1 \bv) + (1-r)(\bx + t_2 \bv)\\
   &= r \by + (1-r) \bz.
   $$
1. Since $\dom f$ is convex, hence $r \by + (1-r) \bz \in \dom f$.
1. Thus, $g$ is defined at $t = rt_1 + (1-r)t_2$ for all $r \in [0,1]$.
1. We have shown that if $t_1, t_2 \in \dom g$, 
   then $t = rt_1 + (1-r)t_2 \in \dom g$ for all $r \in [0,1]$.
1. Thus, $\dom g$ is convex.
1. Now,
   
   $$
   g(t) 
   &= g(r t_1 + (1-r)t_2)\\
   &= f(r \by + (1-r) \bz)\\
   &\leq r f(\by) + (1-r) f(\bz)\\
   &= r g(t_1) + (1-r) g(t_2).
   $$
1. We showed that for any $t_1, t_2 \in \dom g$ and $r \in [0,1]$,

   $$
   g (r t_1 + (1-r) t_2 )\leq r g(t_1) + (1-r) g(t_2).
   $$
1. Thus, $g$ is convex.

For the converse, we need to show that 
if for any $\bx \in \dom f$ and any $\bv \in \VV$,
$g$ is convex, then $f$ is convex.

Assume for contradiction that $f$ is not convex.
Then, either $\dom f$ is not convex or 
there exists some $\bx, \by \in \dom f$ and $t \in [0,1]$
such that:

$$
f((1-t)\bx + t\by) > (1 - t) f(\bx) + t f(\by).
$$
We show that both of these conditions lead to contradictions.

1. Assume $\dom f$ is not convex.
1. Then, there exists $\bx, \by \in \dom f$ such that for some $t \in [0,1]$: 
   
   $$
   (1 - t)\bx + t \by \notin \dom f.
   $$
1. Let $\bv = \by - \bx$.
1. Note that $(1 - t)\bx + t \by = \bx + t \bv$.
1. Picking $g$ for this particular choice of $\bx$ and $\bv$, we note that
   $g$ is defined at $t=0$ and $t=1$ since they corresponding to the points
   $\bx$ and $\by$ respectively in $\dom f$.
1. Since $g$ is convex by hypothesis, hence, $g$ is defined at every
   $t \in [0,1]$.
1. This contradicts the fact that $g$ is not defined at some $t \in [0,1]$.
1. Thus, $\dom f$ must be convex.

We now accept that $\dom f$ is convex, but 
there exists some $\bx, \by \in \dom f$ and $t \in [0,1]$
such that:

$$
f((1-t)\bx + t\by) > (1 - t) f(\bx) + t f(\by).
$$

1. Again, let $\bv = \by - \bx$ and note that 
   $(1 - t)\bx + t \by = \bx + t \bv$.
1. Pick $g$ for this choice of $\bx$ and $\bv$.
1. We have $g(t) = f(\bx + t \bv)$.
1. In particular, $g(0) = f(\bx)$ and $g(1) = f(\by)$.
1. Since $g$ is convex, hence for every $t \in [0,1]$,
   
   $$
   f((1-t)\bx + t\by) 
   &= f(\bx + t \bv)\\
   &= g(t)\\
   &= g ((1-t)0 + t 1)\\
   &\leq (1-t)g(0) + t g(1)\\
   &= (1-t)f(\bx) + t f(\by).
   $$
1. We have a contradiction.
1. Thus, $f$ must be convex.
```

A good application of this result is in showing the
concavity of the log determinant function in
{prf:ref}`ex-cvxf-log-det` below.

## Epigraph

The {prf:ref}`epigraph <def-bra-epigraph>`
of a function $f: \VV \to \RR$ is given by:

$$
\epi f = \{ (\bx,t) \in \VV \oplus \RR \ST \bx \in \dom f, f(\bx) \leq t \}.
$$
$\VV \oplus \RR$ is the 
{prf:ref}`direct sum <def-cvx-real-vector-space-r-prod>`
of $\VV$ and $\RR$ having appropriate vector space 
structure.

```{figure} images/pic_epigraph_x_sqr.png
---
name: cvx:func:epigraph:x:sqr
---
Epigraph of the function $f(x) = x^2$.
```


The definition of epigraph also applies for extended
real valued functions $f: \VV \to \ERL$.

### Convex Functions

```{prf:theorem} Function convexity = Epigraph convexity
:label: res-cvxf-convexity-epigraph

Let $\VV$ be a real vector space.
A function $f: \VV \to \RR$ is convex if and only if its epigraph
$\epi f$ is a convex set.

This statement is also valid for extended real valued functions.
```

```{prf:proof}
Let $C = \epi f$.

Assume $f$ is convex.

1. Let $(\bx_1, t_1), (\bx_2, t_2) \in \epi f$.
1. Then, $f(\bx_1) \leq t_1$ and $f(\bx_2) \leq t_2$. 
1. Let $r \in [0,1]$.
1. Consider the point $(\bx, t) = r(\bx_1, t_1) + (1-r)(\bx_2, t_2)$.
1. We have $\bx = r \bx_1 + (1 -r)(\bx_2)$.
1. And $t = r t_1 + (1-r)t_2$.
1. Then, $ r f(\bx_1) + (1-r) f(\bx_2) \leq r t_1 + (1-r)t_2 = t$.
1. Since $f$ is convex, 
   hence $f(\bx) = f(r \bx_1 + (1 -r)(\bx_2)) \leq r f(\bx_1) + (1-r)f(\bx_2)$.
1. But then, $f(\bx) \leq t$.
1. Thus, $(\bx, t) \in \epi f$.
1. Thus, $(\bx_1, t_1), (\bx_2, t_2) \in \epi f$ 
   implies $r(\bx_1, t_1) + (1-r)(\bx_2, t_2) \in \epi f$ for all $r \in [0,1]$.
1. Thus, $\epi f$ is convex.

Assume $\epi f$ is convex.

1. Let $\bx_1, \bx_2 \in \dom f$.
1. Let $t_1 = f(\bx_1)$ and $t_2 = f(\bx_2)$.
1. Then, $(\bx_1, t_1), (\bx_2, t_2) \in \epi f$.
1. Let $r \in [0,1]$.
1. Let $\bx = r \bx_1 + (1-r)\bx_2$.
1. Since $\epi f$ is convex, hence $r(\bx_1, t_1) + (1-r)(\bx_2, t_2) \in \epi f$.
1. i.e., $(r \bx_1 + (1-r)\bx_2, r t_1 + (1-r)t_2) \in \epi f$.
1. Thus, $\bx = r \bx_1 + (1-r)\bx_2 \in \dom f$.
1. Thus, $\dom f$ is convex.
1. And, $f(\bx) \leq r t_1 + (1-r)t_2$.
1. But $r t_1 + (1-r)t_2 = r f(\bx_1) + (1-r)f(\bx_2)$.
1. Thus, $f(r \bx_1 + (1-r)\bx_2) \leq r f(\bx_1) + (1-r)f(\bx_2)$.
1. Thus, $f$ is convex as $\bx_1, \bx_2 \in \dom f$ and $r \in [0,1]$ 
   were arbitrary. 
```

Note that $\dom f$ is the projection of $\epi f$
from $\VV \oplus \RR$ to $\VV$.
Due to {prf:ref}`res-cvx-convex-set-affine-image`,
$\epi f$ convex implies $\dom f$ convex
as the projection is a linear operation.


```{prf:theorem} Convex function from convex set by minimization
:label: res-cvxf-func-from-cvx-set-inf

Let $C$ be a nonempty convex set in $\VV \oplus \RR$. 
Let $f: \VV \to \ERL$ be the function defined by

$$
f(\bx) = \inf \{ w \in \RR \ST (\bx, w) \in C \} \quad  \Forall \bx \in \VV.
$$
Then $f$ is convex.
```

```{prf:proof}
We show the convexity of $f$ by showing the convexity of its
epigraph.

1. Let $(\bx, s)$ and $(\by, t)$ be two points in $\epi f$.
1. Then $f(\bx) \leq s$ and $f(\by) \leq t$.
1. By the definition of $f$ (infimum rule),
   for every $k \in \Nat$, there exists
   $(\bx, s_k) \in C$ such that $s_k \leq s + \frac{1}{k}$.
1. Similarly, for every $k \in \Nat$, there exists
   $(\by, t_k) \in C$ such that $t_k \leq t + \frac{1}{k}$.
1. Consider the sequences $\{ (\bx, s_k) \}$ and $\{ (\by, t_k) \}$.
1. By the convexity of $C$, for every $r \in [0,1]$ and every $k$

   $$
   (r \bx +  (1 -r) \by, r s_k + (1-r) t_k) \in C.
   $$
1. Hence for every $k$

   $$
   f(r \bx +  (1 -r) \by) \leq r s_k + (1-r) t_k.
   $$
1. Taking the limit $k \to \infty$, we have

   $$
   f(r \bx +  (1 -r) \by) \leq r s + (1-r) t.
   $$
1. Hence $(r \bx +  (1 -r) \by, r s + (1-r) t) \in \epi f$ for every $r \in [0,1]$.
1. Hence $\epi f$ is convex.
1. Hence $f$ is convex.
```


### Nonnegative Homogeneous Functions

Recall that a real valued function $f : \VV \to \RR$ is 
nonnegative homogeneous if 
for every $t \in \RR_+$, $f(t \bx) = t f(\bx)$.

```{prf:theorem} Nonnegative homogeneity = Epigraph is cone
:label: res-cvxf-pose-hom-cone

A function $f : \VV \to \RR$ is nonnegative homogeneous if and
only if its epigraph $\epi f$ is a cone in $\VV \oplus \RR$.
```

```{prf:proof}
Let $f$ be nonnegative homogeneous.

1. Let $(\bx, f(\bx)) \in \epi f$.
1. Let $t \geq 0$.
1. Then, $t(\bx, f(\bx)) = (t\bx, t f(\bx)) = (t\bx, f(t\bx))$.
1. But $(t\bx, f(t\bx)) \in \epi f$ since $f$ is nonnegative homogeneous.
1. Thus, $\VV \oplus \RR$ is closed under nonnegative scalar multiplication.
1. Thus, $\epi f$ is a cone.

Assume $\epi f$ is a cone.

1. Let $\bx \in \dom f$.
1. Then, $(\bx, f(\bx)) \in \epi f$.
1. Since $(\bzero, 0) \in \epi f$ as $\epi f$ is a cone, hence
   $f(0 \bx) = 0 f(\bx) = 0$.
1. Now, let $t > 0$.
1. Since $\epi f$ is a cone then, $t(\bx, f(\bx)) \in \epi f$.
1. Then, $t(\bx, f(\bx)) = (t\bx, t f(\bx)) \in \epi f$.
1. By definition of epigraph, $f(t\bx) \leq t f(\bx)$.
1. We claim that $f(t \bx) = t f(\bx)$ must hold true.
1. Assume for contradiction that $f(t \bx) = s f(\bx)$ where $s < t$.
1. Then, $(t\bx, s f(\bx)) \in \epi f$.
1. Since $\epi f$ is a cone, hence dividing by $t$, we get,
   $(\bx, \frac{s}{t} f(\bx)) \in \epi f$.
1. But then, $f(\bx) \leq \frac{s}{t} f(\bx) < f(\bx)$ which is a contradiction.
1. Hence, $f(t \bx) = t f(\bx)$ must hold true.
```

### Nonnegative Homogeneous Convex Functions

```{prf:theorem} Nonnegative homogeneous convex function epigraph characterization
:label: res-cvxf-nonneg-hom-cvx-cone-epi

Let $\VV$ be a real vector space.
A real valued function $f: \VV \to \RR$ is nonnegative homogeneous and convex
if and only if its epigraph
$\epi f$ is a convex cone.
```

```{prf:proof}

By {prf:ref}`res-cvxf-pose-hom-cone`, $f$ is nonnegative homogeneous if and
only if $\epi f$ is a cone.

By {prf:ref}`res-cvxf-convexity-epigraph`, $f$ is convex if and only if
$\epi f$ is convex.

Thus, $f$ is nonnegative homogeneous and convex if and only if
its epigraph $\epi f$ is a convex cone.
```


```{prf:theorem} Nonnegative homogeneous convex function is subadditive
:label: res-cvxf-nonneg-hom-convex-subadditive

Let $\VV$ be a real vector space.
A nonnegative homogeneous function $f: \VV \to \RR$ is convex
if and only if it is subadditive:

$$
f(\bx + \by) \leq f(\bx) + f(\by) \Forall \bx, \by \in \dom f.
$$
```

```{prf:proof}

Assume that $f$ is nonnegative homogeneous and convex.

1. By {prf:ref}`res-cvxf-nonneg-hom-cvx-cone-epi`, $\epi f$ is a convex cone.
1. Then, by {prf:ref}`res-convex-cone-characterization` $\epi f$ is closed under
   addition and nonnegative scalar multiplication.
1. Pick any $\bx, \by \in \dom f$. 
1. Then $(\bx, f(\bx)), (\by, f(\by)) \in \epi f$.
1. Then, their sum $(\bx + \by, f(\bx) + f(\by)) \in \epi f$.
1. This means that $f(\bx + \by) \leq f(\bx) + f(\by)$ by definition of epigraph.


Now for the converse, assume that $f$ is nonnegative homogeneous and subadditive.

1. By {prf:ref}`res-cvxf-pose-hom-cone`, $\epi f$ is a cone. 
1. Consequently, it is closed under nonnegative scalar multiplication.
1. Pick any $\bx, \by \in \dom f$.
1. Let $(\bx, \alpha), (\by, \beta) \in \epi f$.
1. Then, $f(\bx) \leq \alpha$ and $f(\by) \leq \beta$.
1. Now, $(\bx + \by, f(\bx + \by)) \in \epi f$.
1. Since $f$ is subadditive, hence $f(\bx + \by) \leq f(\bx) + f(\by) \leq \alpha + \beta$.
1. Thus, $(\bx + \by, \alpha + \beta) \in \epi f$.
1. We have shown that for any  $(\bx, \alpha), (\by, \beta) \in \epi f$,
   $(\bx + \by, \alpha + \beta) \in \epi f$.
1. Thus, $\epi f$ is closed under vector addition.
1. Since $\epi f$ is closed under vector addition and nonnegative scalar multiplication,
   hence $\epi f$ is a convex cone.
1. But then, by {prf:ref}`res-cvxf-nonneg-hom-cvx-cone-epi`, $f$ is convex.
```

```{prf:corollary}
:label: res-cvxf-nonneg-hom-convex-negation

Let $\VV$ be a real vector space.
Let $f: \VV \to \RR$ be a nonnegative homogeneous convex function.
Then,

$$
f(-\bx) \geq -f(\bx) \Forall \bx \in \dom f.
$$
```
```{prf:proof}
Since $f$ is nonnegative homogeneous convex, hence $f$ is
subadditive. 

Thus,

$$
f(\bx - \bx) \leq f(\bx) + f(-\bx).
$$

But,

$$
f(\bx - \bx) = f(\bzero) = f(0 \bzero) = 0 f(\bzero) = 0.
$$

Thus,

$$
f(\bx) + f(-\bx) \geq 0.
$$

Thus,

$$
f(-\bx) \geq -f(\bx).
$$
```


```{prf:theorem} Linearity of nonnegative homogeneous functions
:label: res-cvxf-nonneg-hom-convex-linear

Let $\VV$ be a real vector space.
Let $f: \VV \to \RR$ be a nonnegative homogeneous convex function.
Then, $f$ is linear on a subspace $L$ of $\VV$
if and only if $f(-\bx) = -f(\bx)$ for every $\bx \in L$.

If $L$ is finite dimensional, then
this is true if merely $f(-\bb_i) = -f(\bb_i)$ for all the
vectors in some basis $\bb_1, \dots, \bb_n$ for $L$. 
```


```{prf:proof}
We are given that $f$ is nonnegative homogeneous convex.


Assume that $f$ is linear over $L$. 
Then by definition of linearity, $f(-\bx) = -f(\bx)$ for every $\bx \in L$.


Now, for the converse, assume that $f(-\bx) = -f(\bx) \Forall \bx \in L$.

1. Let $\bx, \by \in L$.
1. Then, $f(\bx + \by) \leq f(\bx) + f(\by)$ since $f$ is subadditive.
1. Also, 

   $$
   f(\bx + \by) = -f(-(\bx + \by)) = -f(-\bx + (-\by)).   
   $$
1. But 

   $$
   f(-\bx + (-\by)) \leq f(-\bx) + f(-\by) = -f(\bx) - f(\by) = - (f(\bx) + f(\by)).
   $$
1. Thus,

   $$
   f(\bx + \by) = -f(-\bx + (-\by)) \geq f(\bx) + f(\by).
   $$
1. Combining, we get $f(\bx + \by) = f(\bx) + f(\by)$. 
   Thus, $f$ is additive over $L$.
1. For any $t < 0$, 

   $$
   f(t \bx) = - f(-t \bx) = - (-t) f(\bx) = t f(\bx).
   $$
1. Thus, for any $t \in \RR$, $f(t \bx) = t f(\bx)$.
1. Thus, $f$ is homogeneous over $L$.
1. Since $f$ is additive and homogeneous over $L$, hence $f$ is linear.


Finally, assume that $L$ is finite dimensional and has a basis
$\bb_1, \dots, \bb_n$.

1. By previous argument $f$ is homogeneous on the basis vectors; i.e.,
   $f(t \bb_i) = t f(\bb_i)$ for any $t \in \RR$ and any basis vector.
1. Let $\bx \in L$.
1. Then, $\bx = \sum_{i=1}^n a_i \bb_i$.
1. Since $f$ is subadditive, hence

   $$
   f(a_1 \bb_1) + \dots + f(a_n \bb_n) 
   & \geq f(a_1 \bb_1 + \dots + a_n \bb_n)\\
   &= f(\bx) \\
   &\geq - f(-\bx)\\
   &= - f(-a_1 \bb_1 - \dots - a_n \bb_n)\\
   &\geq - f(-a_1 \bb_1) - \dots - f(-a_n \bb_n)\\
   &=f(a_1 \bb_1) + \dots + f(a_n \bb_n).
   $$
1. This can hold only if all the inequalities are equalities in the previous
   derivation. 
1. Thus, $f(\bx) = - f(-\bx)$ or $-f(\bx) = f(-\bx)$ for every $\bx \in L$.
1. Then, following the previous argument, $f$ is linear over $L$.
```

## Extended Value Extensions
Tracking domains of convex functions is difficult.
It is often convenient to extend a convex function
$f : \VV \to \RR$ with a domain $\dom f \subset \VV$
to all of $\VV$ by defining it to be $\infty$ 
outside its domain. 

```{index} Convex function; extended value extension
```
```{prf:definition} Extended value extension
:label: def-cvxf-extended-value-extension

The {prf:ref}`extended value extension <def-bra-extended-value-extension>`
of a convex function $f: \VV \to \RR$ is defined as
$\tilde{f} : \VV \to \ERL$ given by:

$$
\tilde{f}(\bx) \triangleq \begin{cases} 
f(\bx) & \text{for} & \bx \in \dom f \\
\infty & \text{for} & \bx \notin \dom f.
\end{cases}
$$
```

We mention that the defining inequality {eq}`eq-convexity-inequality` 
for a convex function $f$
remains valid (rather gets extended) for its extended value extension too.
If $f$ is convex over $\dom f$, then
for any $\bx_1, \bx_2 \in \VV$, and $0 < t < 1$, we have 

$$
\tilde{f}(t \bx_1 + (1-t) \bx_2) \leq t \tilde{f}(\bx_1) + (1-t) \tilde{f}(\bx_2).
$$

1. At $t=0$ and $t=1$, this is always an equality.
1. Since $\dom f$ is convex, hence if both $\bx_1, \bx_2 \in \dom f$,
   then $t \bx_1 + (1-t) \bx_2 \in \dom f$ too. 
1. The inequality then reduces to {eq}`eq-convexity-inequality`.
1. If either $\bx_1$ or $\bx_2$ is not in $\dom f$, then the R.H.S.
   becomes $\infty$ and the inequality stays valid.

```{index} Convex function; effective domain
```
```{prf:definition} Effective domain
:label: def-cvxf-effective-domain

The {prf:ref}`effective domain <def-bra-extension-domain>`
of an extended valued function $\tilde{f} : \VV \to \ERL$ is defined as:

$$
\dom \tilde{f} = \{ \bx \in \VV \ST \tilde{f}(\bx) < \infty \}.
$$
```

An equivalent way to define the effective domain is:

$$
\dom \tilde{f} = \{\bx \in \VV \ST 
\exists t \in \RR \text{ with } (\bx, t) \in \epi f \}.
$$


```{prf:theorem} Effective domain and sum of functions
:label: res-cvx-evf-sum-domain

If $f$ and $g$ are two extended valued functions, 
then $\dom (f + g) = \dom f \cap \dom g$.
```

```{prf:proof}

We proceed as follows:

1. At any $\bx \in \dom f \cap \dom g$, both
   $f(\bx)$ and $g(\bx)$ are finite.
1. Thus, $f(\bx) + g(\bx)$ is finite.
1. Hence, $\bx \in \dom (f + g)$.
1. At any $\bx \in \VV \setminus (\dom f \cap \dom g)$, 
   either $f(\bx) = \infty$ or $g(\bx) = \infty$.
1. Thus, $(f + g)(\bx) = f(\bx) + g(\bx) = \infty$.
1. Thus, $\bx \notin \dom (f + g)$.
```

Several commonly used convex functions have vastly different
domains. If we work with these functions directly, then
we have to constantly worry about identifying the domain
and manipulating the domain as per the requirements
of the operations we are considering. 
This quickly becomes tedious.

An alternative approach is to work with the
extended value extensions of all functions.
We don't have to worry about tracking the function
domain. The domain can be identified whenever needed
by removing the parts from $\VV$ where the function
goes to $\infty$.

In this book, unless otherwise specified, 
we shall assume that the functions are
being treated as their extended value extensions. 

## Proper Functions

```{index} Convex function; proper
```
```{prf:definition} Proper function
:label: def-cvxf-proper-function

An extended real-valued function 
$f : \VV \to \ERL$ is called *proper*
if its domain is nonempty, it never
takes the value $-\infty$ and is
not identically equal to $\infty$.

$$
\exists \bx \in \VV \text{ such that } f(\bx) < \infty
\text{ and }
f(\bx) > -\infty \Forall \bx \in \VV.
$$

In other words, $\epi f$ is nonempty 
and contains no vertical lines. 
``` 
Putting another way, a proper function
is obtained by taking a real valued function $f$
defined on a nonempty set $C \subseteq \VV$
and then extending it to all of $\VV$ by 
setting $f(\bx) = +\infty$ for all $\bx \notin C$.

It is easy to see that the codomain for a proper
function can be changed from $\ERL$
to $\RERL$ to clarify that it never takes
the value $-\infty$.


```{index} Convex function; improper
```
```{prf:definition} Improper function
:label: def-cvxf-improper-function

An extended real-valued function 
$f : \VV \to \ERL$ is called *improper*
if it is not proper.
```

For an improper function $f$:

* $\dom f$ may be empty. 
* $f$ might take a value of $-\infty$ at some $\bx \in \VV$.

Most of our study is focused on proper functions.
However, improper functions sometimes do arise
naturally in convex analysis. 

```{prf:example} An improper function
:label: ex-cvxf-improper-f

Consider a function $f: \RR \to \ERL$ as described below:

$$
f(x) = \begin{cases}
-\infty & \text{ if } & | x | < 1 \\
0 & \text{ if } & |x| = 1 \\
\infty & \text{ if } & | x | > 1 .
\end{cases}
$$
Then, $f$ is an improper function.
```


## Indicator Functions

```{prf:definition} Indicator function
:label: def-cvxf-indicator-function

Let $C \subseteq \VV$. Then, its 
*indicator function* is given by
$I_C(\bx) = 0 \Forall \bx \in C$. 
Here, $\dom I_C = C$.

The extended value extension of an indicator
function is given by:

$$
\tilde{I_C}(\bx) \triangleq \begin{cases} 
0 & \text{for} & \bx \in C \\
\infty & \text{for} & \bx \notin C.
\end{cases}
$$
```

```{prf:theorem} Indicator functions and convexity
:label: res-cvxf-indicator-func-convex-set

An indicator function is convex if and only if its domain is a convex set.
```

```{prf:proof}
Let $C$ be convex. Let $I_C$ be its indicator function. 
Let $\bx, \by \in C$. Then, for any $t \in [0,1]$

$$
I_C(t \bx + (1-t) \by) = 0 \leq t I_C(\bx) + (1-t) I_C(\bx) = 0.
$$
since $t \bx + (1-t) \by \in C$ as $C$ is convex. 

Thus, $I_C$ is convex.

If $C$ is not convex, then $\dom I_C$ is not convex.
Hence, $I_C$ is not convex.
```


```{prf:theorem} Restricting the domain of a function
:label: res-cvxf-func-sum-indicator

Let $f$ be a proper function. Then,

$$
\dom (f + I_C)  =  \dom f \cap C.
$$
Also, 

$$
(f + I_C )(\bx) = f(\bx) \Forall \bx \in \dom f \cap C. 
$$
```
The statement is obvious. And quite powerful.

* The problem of minimizing a function $f$ over a set $C$
  is same as minimizing $f + I_C$ over $\VV$.


## Sublevel Sets

Recall from {prf:ref}`def-bra-sub-level-set`
that the $\alpha$-sublevel set for a 
real valued function $f : \VV \to \RR$ is given by

$$
C_{\alpha} = \{ \bx \in \dom f \,|\, f(\bx) \leq \alpha \}.
$$

The strict sublevel sets for a real valued function $f: \VV \to \RR$
can be defined as

$$
O_{\alpha} = \{ \bx \in \dom f \,|\, f(\bx) < \alpha \}.
$$


The sublevel sets can be shown to be intersection
of a set of strict sublevel sets.

```{prf:theorem} Sublevel set as intersection
:label: res-cvxf-sublevel-set-as-intersection

Let $\VV$ be a real vector space. Let $f : \VV \to \RR$ be 
a real valued function.
Let

$$
O_{\alpha} = \{ \bx \in \dom f \,|\, f(\bx) < \alpha \}
$$
denote the strict sublevel set of $f$ for $\alpha$.
Let

$$
C_{\alpha} = \{ \bx \in \dom f \,|\, f(\bx) \leq \alpha \}
$$
denote the sublevel set of $f$ for $\alpha$.
Then,

$$
C_{\alpha} = \bigcap_{\mu > \alpha} O_{\mu}.
$$
```

```{prf:proof}

We show that $C_{\alpha} \subseteq \bigcap_{\mu > \alpha} O_{\mu}$.

1. Let $\bx \in C_{\alpha}$.
1. Then, $f(\bx) \leq \alpha$.
1. Thus, $f(\bx) < \mu$ for every $\mu > \alpha$.
1. Thus, $\bx \in O_{\mu}$ for every $\mu > \alpha$.
1. Thus, $C_{\alpha} \subseteq \bigcap_{\mu > \alpha} O_{\mu}$.


We now show that $C_{\alpha} \supseteq \bigcap_{\mu > \alpha} O_{\mu}$.

1. Let $\bx \in \bigcap_{\mu > \alpha} O_{\mu}$.
1. Then, $f(\bx) < \mu$ for every $\mu > \alpha$.
1. Taking the infimum on the R.H.S. over the set $\{ \mu \in \RR \ST \mu > \alpha \}$,
   we obtain 

   $$
   f(\bx) \leq \inf \{ \mu \in \RR \ST \mu > \alpha \} = \alpha. 
   $$
1. Thus, $\bx \in C_{\alpha}$.
1. Thus, $\bigcap_{\mu > \alpha} O_{\mu} \subseteq C_{\alpha}$.
```


```{prf:theorem} Convexity of sublevel sets
:label: res-cvxf-convexity-sublevel-sets

If $f : \VV \to \RR$ is convex, 
then its sublevel sets given by

$$
C_{\alpha} = \{ \bx \in \dom f \,|\, f(\bx) \leq \alpha \}
$$
are convex.
```

```{prf:proof}
Assume $f$ is convex.

1. Let $\bx, \by \in C_{\alpha}$.
1. Then, $f(\bx) \leq \alpha$ and $f(\by) \leq \alpha$.
1. Let $t \in [0,1]$.
1. Let $\bz = t \bx + (1-t)\by$.
1. Since $f$ is convex, hence:

   $$
   f(\bz) \leq t f(\bx) + (1-t) f(\by) \leq t \alpha + (1-t) \alpha = \alpha.
   $$
1. Thus, $f(\bz) \leq \alpha$.
1. Thus, $\bz \in C_{\alpha}$.
1. Thus, $C_{\alpha}$ is convex.
```

The converse is not true.
A function need not be convex even if all its
sublevel sets are convex.


```{prf:example}
:label: ex-cvxf-log-concave-sublevel-convex

Consider the function $f(x) = \ln x$. 
It is concave ({prf:ref}`ex-cvxf-real-logarithm`).

Its sublevel sets are convex as they are intervals.
```


```{prf:theorem} Convexity of strict sublevel sets
:label: res-cvxf-convexity-open-sublevel-sets

If $f : \VV \to \RR$ is convex, 
then its strict sublevel sets given by

$$
O_{\alpha} = \{ \bx \in \dom f \,|\, f(\bx) < \alpha \}
$$
are convex.
```

```{prf:proof}
Assume $f$ is convex.

1. Let $\bx, \by \in O_{\alpha}$.
1. Then, $f(\bx) < \alpha$ and $f(\by) < \alpha$.
1. Let $t \in (0,1)$.
1. Let $\bz = t \bx + (1-t)\by$.
1. Since $f$ is convex, hence:

   $$
   f(\bz) \leq t f(\bx) + (1-t) f(\by) < t \alpha + (1-t) \alpha = \alpha.
   $$
1. Thus, $f(\bz) < \alpha$.
1. Thus, $\bz \in O_{\alpha}$.
1. Thus, $O_{\alpha}$ is convex.
```

An alternate proof for showing the convexity of the
sublevel sets is to show it as an intersection of strict sublevel sets.


```{prf:theorem} Intersection of sublevel sets of convex functions
:label: res-cvxf-convexity-intersect-sublevel-sets

Let $\VV$ be a real vector space.
Let $I$ be an arbitrary index set.
Let $f_i : \VV \to \RERL$ be convex functions for every $i \in I$.
Let $\alpha_i \in \RR$ for every $i \in I$.
Then,

$$
C = \{ \bx  \ST f_i(\bx) \leq \alpha_i, \Forall i \in I \}
$$
is a convex set.
```

```{prf:proof}
For each $i \in I$, consider the set

$$
C_i = \{ \bx  \ST f_i(\bx) \leq \alpha_i\}.
$$
Then, $C_i$ is a sublevel set of $f_i$ which is convex. Hence, $C_i$ is convex.
Now, we can see that 

$$
C = \bigcap_{i \in I}C_i
$$
Thus, $C$ is an intersection of convex sets. Hence, $C$ is convex.
```

```{prf:example} Convexity of sublevel sets of the quadratic
:label: ex-cvxf-quadratic-sublevel

Let $\bQ \in \SS^n$ be a positive semidefinite matrix. Let $\ba \in \RR^n$ and $c \in \RR$.

Consider the sets of the form

$$
\{\bx \in \RR^n \ST \frac{1}{2} \langle \bx, \bQ \bx \rangle + \langle \bx, \ba \rangle + c \leq 0 \}.
$$

This is a sublevel set of the quadratic function 
$f(\bx) = \frac{1}{2} \langle \bx, \bQ \bx \rangle + \langle \bx, \ba \rangle + c$. 

Since $f$ is convex, hence the set is convex.

Sets of this form include the solid ellipsoids, paraboloids as well as spherical balls.
Here is an example of the spherical ball of the norm induced by the inner product.

$$
\{\bx \ST \| \bx \| \leq 1 \}  = \{ \bx \ST \langle \bx, \bx \rangle - 1 \leq 0 \}.
$$
```

## Hypograph

The {prf:ref}`hypograph <def-bra-hypograph>`
of a function $f: \VV \to \RR$ is given by:

$$
\hypo f = \{ (\bx,t) \in \VV \oplus \RR \ST \bx \in \dom f, f(\bx) \geq t \}.
$$

Just like function convexity is connected to epigraph convexity,
similarly function concavity is connected to hypograph convexity.


```{prf:theorem} Function concavity = Hypograph convexity
:label: res-cvxf-concavity-hypograph

A function $f$ is concave if and only if its hypograph
$\hypo f$ is a convex set.
```

```{prf:proof}

$f$ is concave if and only if $-f$ is convex
if and only if the epigraph of $-f$ is convex
if and only if the hypograph of $f$ is convex.
```


## Super-level Sets

Recall from {prf:ref}`def-bra-super-level-set`
that the $\alpha$-sublevel set for a 
real valued function $f : \VV \to \RR$ is given by

$$
D_{\alpha} = \{ \bx \in \dom f \,|\, f(\bx) \geq \alpha \}.
$$


```{prf:theorem}
:label: res-cvxf-concavity-super-level-sets

If $f : \VV \to \RR$ is concave, 
then its super-level sets are convex.
```

```{prf:proof}
Assume $f$ is concave.

1. Let $\bx, \by \in D_{\alpha}$.
1. Then, $f(\bx) \geq \alpha$ and $f(\by) \geq \alpha$.
1. Let $t \in [0,1]$.
1. Let $\bz = t \bx + (1-t)\by$.
1. Since $f$ is concave, hence:

   $$
   f(\bz) \geq t f(\bx) + (1-t) f(\by) \geq t \alpha + (1-t) \alpha = \alpha.
   $$
1. Thus, $f(\bz) \geq \alpha$.
1. Thus, $\bz \in D_{\alpha}$.
1. Thus, $D_{\alpha}$ is convex.
```

The converse is not true.
A function need not be concave even if all its
super-level sets are convex.


```{prf:example}
:label: ex-cvxf-am-gm-large-alpha

Let geometric mean be given by:

$$
g(\bx) =  \left ( \prod_{i=1}^n x_i \right )^{\frac{1}{n}}
$$
with $\dom g = \RR^n_{+}$
(with the interpretation that $0^{\frac{1}{n}} = 0$).


Let arithmetic mean be given by:

$$
a(\bx) = \frac{1}{n}\sum_{i=1}^n x_i.
$$

Consider the set:

$$
A = \{ \bx \in \RR^n_+ \ST g(\bx) \geq \alpha a(\bx) \}.
$$

$A$ is the set of nonnegative vectors where the geometric
mean of the components is at least $\alpha$ times larger
than the arithmetic mean.


1. In {prf:ref}`ex-cvxf-geom-mean` we establish that
   $g$ is concave.
1. In {prf:ref}`ex-cvxf-arithmetic-mean` we established that
   $a$ is convex as well as concave.
1. Thus, $-\alpha a$ is concave.
1. Thus, $g - \alpha a$ is concave (with $\dom g - \alpha a = \RR^n_+$).
1. Note that $A$ can be redefined as:

   $$
   A = \{ \bx \in \RR^n_+ \ST g(\bx) - \alpha a(\bx) \geq 0 \}.
   $$
1. Thus, $A$ is a $0$-super-level set of $g - \alpha a$.
1. Since $g - \alpha a$ is concave, hence $A$ is convex.
```

## Closed Convex Functions

Recall from {ref}`sec:ms:real-valued-functions` that
a function is closed if all its sublevel sets are closed.
A function is closed if and only if its epigraph is closed.
A function is closed if and only if it is lower semicontinuous.

In general, if a function is continuous, then it is lower
semicontinuous and hence it is closed.

In this subsection, we provide examples of convex functions which
are closed.

### Affine Functions

```{prf:theorem} Affine functions are closed
:label: res-cvxf-affine-closed

Let $f: \VV \to \RR$ be given by

$$
f(\bx) = \langle \bx, \ba \rangle + b
$$
where $\ba \in \VV^*$ and $b \in \RR$.
Then $f$ is closed.
```

```{prf:proof}
We prove closedness by showing that the epigraph of $f$ is closed.

1. Let $\{ \bx_k, t_k \}$ be a converging sequence of $\epi f$.
1. Let $(\bx, t) = \lim_{k \to \infty} (\bx_k, t_k)$.
1. We have $f(\bx_k) \leq t_k$ for every $k$.
1. In other words

   $$
   \langle \bx_k, \ba \rangle + b \leq t_k \Forall k \in \Nat.
   $$
1. Taking the limit on both sides, we get

   $$
   \langle \bx, \ba \rangle + b \leq t.
   $$
1. Hence $f(\bx) \leq t$.
1. Hence $(\bx, t) \in \epi f$.
1. Hence $\epi f$ is closed.
```

### Norms

```{prf:theorem} All Norms are closed
:label: res-cvxf-norm-closed

Let $\| \cdot \|: \VV \to \RR$ be a norm on a real vector space $\VV$. 
Then $\| \cdot \|$ is closed.
```

```{prf:proof}
The sublevel sets are given by $S_t = \{ \bx \in \VV \ST \| \bx \| \leq t \}$.
They are nothing but the closed balls of radius $t$ around $\bzero$ and
by definition closed.
Hence all sublevel sets are closed.
Thus $\| \cdot \|$ is closed.
```


## Support Functions

```{index} Support function
```
```{prf:definition} Support function for a set
:label: def-cvxf-support-function

Let $\VV$ be a real inner product space. Let $C$ be a subset of $\VV$.
The *support function* $\sigma_C : \VV \to \RERL$ is defined as

$$
\sigma_C (\bx) =  \sup \{\langle \bx, \by \rangle \ST \by \in C \}.
$$

Since $\VV$ and $\VV^*$ are isomorphic, support function
$\sigma_C : \VV^* \to \RERL$
for a set $C \subseteq \VV^*$ is similarly defined as

$$
\sigma_C (\bx) =  \sup \{\langle \by, \bx \rangle \ST \by \in C \}.
$$
```

```{prf:example} Finite sets
:label: ex-cvxf-support-finite-set

Let $C = \{ \bb_1, \dots, \bb_m \}$ be a finite subset of $\VV$.
Then,

$$
\sigma_C (\bx) = \max \{ \langle \bx, \bb_1\rangle, \dots, \langle \bx, \bb_m\rangle \}.
$$
This follows directly from the definition.
```


### Convexity

```{prf:theorem} Convexity of support function
:label: res-cvxf-support-fun-convex

Let $\VV$ be a real inner product space. Let $C$ be a nonempty subset of $\VV$.
Then, the support function $\sigma_C : \VV \to \RERL$ is convex.
```

```{prf:proof}
Fix a $\by \in C$ and consider the function $\sigma_{\by} : \VV \to \RR$ given by

$$
\sigma_{\by} (\bx) = \langle \bx, \by \rangle.
$$ 

$\sigma_{\by}$ is linear and accordingly convex. Then,

$$
\sigma_C (\bx) = \sup_{\by \in C} \sigma_{\by} (\bx)
$$
is a pointwise supremum of convex functions.
By {prf:ref}`res-cvx-ptws-supremum`, $\sigma_C$ is convex.
```

We note that the convexity of the support function $\sigma_C$
has nothing to do with the convexity of the underlying set $C$.

### Closedness

```{prf:theorem} Closedness of support function
:label: res-cvxf-support-fun-closed

Let $\VV$ be a real inner product space. Let $C$ be a nonempty subset of $\VV$.
Then, the support function $\sigma_C : \VV \to \RERL$ is closed.
```

```{prf:proof}
Recall that a function is closed if all its sublevel sets are closed.

1. Let $a \in \RR$.
1. Consider the sublevel set $S_a = \{ \bx \in \VV \ST \sigma_C(\bx) \leq a \}$.
1. Then,

   $$
   S_a = \{ \bx \in \VV \ST \sup_{\by \in C} \langle \bx, \by \rangle \leq a \} 
   $$
1. Thus,

   $$
   S_a = \{ \bx \in \VV \ST \langle \bx, \by \rangle \leq a  \Forall \by \in C \} 
   $$
1. Define $A_y$ as 
    
   $$
   A_y = \{ \bx \in \VV \ST \langle \bx, \by \rangle \leq a \}.
   $$
1. Then,

   $$
   S_a = \bigcap_{\by \in C} A_y.
   $$
1. Now, $A_y$ is a closed set since  $\langle \bx, \by \rangle$ is a continuous function.
1. Thus, $S_a$ is an intersection of closed sets.
1. Thus, $S_a$ is closed.
1. Thus, all sublevel sets of $\sigma_C$ are closed.
1. Thus, $\sigma_C$ is closed.
```

### Equality of Underlying Sets

```{prf:theorem} Equality of underlying sets for support functions
:label: res-cvxf-support-func-equality-convex

Let $A, B \subseteq \VV$ be nonempty, closed and convex sets.
Then, $A = B$ if and only if $\sigma_A = \sigma_B$.
```

```{prf:proof}
If $A = B$ then obviously $\sigma_A = \sigma_B$.
Now, assume that $\sigma_A = \sigma_B$.

1. For contradiction, assume that $A \neq B$.
1. Without loss of generality, assume that there exists $\by \in A$
   such that $\by \notin B$.
1. Since $\by \notin B$ and $B$ is a closed convex set, hence,
   by {prf:ref}`res-cvxf-cl-convex-set-strict-separation`,
   there exists a hyperplane $H$ strongly separating $\by$ from
   $B$.
1. Thus, there exists $\bp \in \VV^*$ and $\alpha \in \RR$ such that

   $$
   \langle \bx , \bp \rangle \leq \alpha < \langle \by, \bp \rangle
   \Forall \bx \in B.
   $$
1. Taking supremum over $B$ on the L.H.S., we obtain

   $$
   \sigma_B(\bp) \leq \alpha < \langle \by, \bp \rangle 
   \leq \sigma_A(\bp).
   $$
1. Thus, there exists $\bp \in \VV^*$ such that

   $$
   \sigma_B(\bp) < \sigma_A(\bp).
   $$
1. This contradicts our hypothesis that $\sigma_A$ and $\sigma_B$ 
   are identical.
1. Thus, $A = B$ must hold.
```

### Closure and Convex Hull

The next result shows that support function
for a set and its closure or its convex hull
are identical. This is why, we required
$A,B$ to be closed and convex in the previous result.


```{prf:theorem} Support functions and closure or convex hull of underlying set
:label: res-cvxf-supp-closure-hull

Let $A \subseteq \VV$. Then,

1. $\sigma_A = \sigma_{\closure A}$.
1. $\sigma_A = \sigma_{\convex A}$.
```

```{prf:proof}
We first consider the case of closure.

1. $A \subseteq \closure A$.
1. Thus, $\sigma_A (\by) \leq \sigma_{\closure A}(\by) \Forall \by \in \VV^*$.
1. Let us now show the reverse inequality.
1. Let $\by \in \VV^*$.
1. Then, there exists a sequence $\{ \bx_k \}$ of $\closure A$ such that

   $$
   \lim_{k \to \infty} \langle \bx_k, \by \rangle = \sigma_{\closure A} (\by).
   $$
1. Now for every $\bx_k \in \closure A$, there exists a 
   point $\bz_k \in A$ such that $d(\bx_k, \bz_k) \leq \frac{1}{k}$.
1. Thus, $\lim_{k \to \infty} (\bz_k - \bx_k) = \bzero$.
1. Since $\bz_k \in A$, hence

   $$
   \sigma_A(\by) \geq \langle \bz_k, \by \rangle 
   = \langle \bx_k, \by \rangle + \langle \bz_k - \bx_k, \by \rangle.
   $$
1. Taking the limit $k \to \infty$ on the R.H.S., we obtain

   $$
   \sigma_A(\by) \geq \sigma_{\closure A}(\by) + 0 = \sigma_{\closure A}(\by).
   $$
1. Thus, $\sigma_A(\by) = \sigma_{\closure A}(\by)$ must hold true.
1. Since this is true for every $\by \in \VV^*$, hence
   $\sigma_A = \sigma_{\closure A}$.


Now, consider the case of convex hull.

1. By definition, $A \subseteq \convex A$.
1. Thus, $\sigma_A (\by) \leq \sigma_{\convex A}(\by) \Forall \by \in \VV^*$.
1. Let $\by \in \VV^*$.
1. Then, there exists a sequence $\{ \bx_k \}$ of $\convex A$ such that

   $$
   \lim_{k \to \infty} \langle \bx_k, \by \rangle = \sigma_{\convex A} (\by).
   $$
1. Since $\bx_k \in \convex A$, hence, there exists
   $\bz_1^k, \dots, \bz_{n_k}^k \in A$ and $\bt^k \in \Delta_{n_k}$ such that

   $$
   \bx_k = \sum_{i=1}^{n_k} t_i^k \bz_i^k.
   $$
1. By linearity of the inner product

   $$
   \langle \bx_k, \by \rangle 
   &= \left \langle \sum_{i=1}^{n_k} t_i^k \bz_i^k, \by \right \rangle\\
   &= \sum_{i=1}^{n_k}  t_i^k \langle \bz_i^k, \by \rangle\\
   &\leq \sum_{i=1}^{n_k}  t_i^k \sigma_A(\by)\\
   &= \sigma_A(\by).
   $$
1. Taking the limit $k \to \infty$ on the L.H.S., we obtain

   $$
   \sigma_{\convex A} (\by) = \lim_{k \to \infty} \langle \bx_k, \by \rangle
   \leq \sigma_A(\by).
   $$
1. Thus, $\sigma_A(\by) = \sigma_{\convex A}(\by)$ must hold true.
1. Since this is true for every $\by \in \VV^*$, hence
   $\sigma_A = \sigma_{\convex A}$.
```

### Arithmetic Properties

Following properties of support functions are useful in
several applications.

```{prf:theorem} Arithmetic properties of support functions
:label: res-cvxf-support-func-Homogeneity

1. (Nonnegative homogeneity) For any nonempty set $C \subseteq \VV$ and
   a vector $\bx \in \VV$ and $t \geq 0$,

   $$
   \sigma_C (t \bx) = t \sigma_C (\bx).
   $$

1. (Subadditivity) For any nonempty set $C \subseteq \VV$ and
   a vector $\bu, \bv \in \VV$,

   $$
   \sigma_C(\bu + \bv) \leq \sigma_C (\bu) + \sigma_C (\bv).
   $$
1. (Nonnegative scaling of the underlying set)
   For any nonempty set $C \subseteq \VV$ and
   a vector $\bx \in \VV$ and $t \geq 0$

   $$
   \sigma_{t C} (\by) = t \sigma_C(\by).
   $$

1. (Additivity over Minkowski sum of sets)
   For any two nonempty subsets $A, B \subseteq \VV$
   and $\bx \in \VV$

   $$
   \sigma_{A + B} (\bx) = \sigma_A(\bx) + \sigma_B(\bx).
   $$
```

```{prf:proof}

(1) Nonnegative homogeneity
 
$$
\sigma_C (t \bx) &= \sup_{\by \in C} \langle t \bx, \by \rangle \\
&= \sup_{\by \in C} t \langle  \bx, \by \rangle \\
&= t \sup_{\by \in C} \langle  \bx, \by \rangle \\
&= t \sigma_C(\bx).
$$
Here, we used the fact that $\sup$ commutes with nonnegative scalars.

(2) Subadditivity

$$
\sigma_C (\bu + \bv) &= \sup_{\by \in C} \langle \bu + \bv, \by \rangle \\
&= \sup_{\by \in C} (\langle \bu, \by \rangle + \langle \bu, \by \rangle) \\
&\leq \sup_{\by \in C} \langle \bu, \by \rangle + \sup_{\by \in C} \langle \bv, \by \rangle \\
&= \sigma_C (\bu) + \sigma_C(\bv).
$$

(3) Nonnegative scaling of the underlying set

$$
\sigma_{ t C} (\bx) &= \sup_{\by \in t C} \langle \bx, \by \rangle \\
&= \sup_{\by \in C} \langle  \bx, t \by \rangle \\
&= \sup_{\by \in C} t \langle  \bx, \by \rangle \\
&= t \sup_{\by \in C} \langle  \bx, \by \rangle \\
&= t \sigma_C(\bx).
$$

(4) Minkowski sum

$$
\sigma_{ A + B} (\bx) &= \sup_{\by \in A + B} \langle \bx, \by \rangle \\
&= \sup_{\bu \in A, \bv \in B} \langle \bx , \bu + \bv \rangle \\
&= \sup_{\bu \in A, \bv \in B} (\langle \bx , \bu \rangle + \langle \bx , \bv \rangle ) \\
&= \sup_{\bu \in A} \langle \bx , \bu \rangle + \sup_{\bv \in B} \langle \bx , \bv \rangle\\
&= \sigma_A (\bx) + \sigma_B(\bx).
$$
```

### Cones

Recall from {prf:ref}`def-cone` that a set $C$ is called a cone
if for every $\bx \in C$ and every $t \geq 0$, $t \bx \in C$.
Also, recall from {prf:ref}`def-cvx-polar-cone` that the polar
cone of a set $C$ is given by

$$
C^{\circ} = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \leq 0
\Forall \bx \in C \}.
$$

```{prf:theorem} Support function of a cone
:label: res-cvxf-support-cone

Let $C$ be a given cone.
Then, 

$$
\sigma_C(\by) = I_{C^{\circ}} (\by) \Forall \by \in \VV^*.
$$
In words, the support function of a cone $C$ is the
indicator function of the polar cone of $C$.
```

```{prf:proof}
We proceed as follows

1. Assume that $\by \in C^{\circ}$.
1. Then, $\langle \bx, \by \rangle \leq 0 \Forall \bx \in C$.
1. In particular, $\bzero \in C$ since $C$ is a cone.
1. Accordingly, $\langle \bzero, \by \rangle = 0$.
1. Thus,

   $$
   \sigma_C(\by) = \sup_{\bx \in C} \langle \bx, \by \rangle = 0.
   $$
1. Now consider $\by \notin C^{\circ}$.
1. Then, there exists $\bu \in C$ such that $\langle \bu, \by \rangle > 0$.
1. Since $C$ is a cone, hence $t \bu \in C$ for all $t \geq 0$.
1. Accordingly,

   $$
   \sigma_C(\by) = \sup_{\bx \in C} \langle \bx, \by \rangle
   \geq \langle t \bu, \by \rangle \Forall t \geq 0.
   $$
1. Taking the limit $t \to \infty$, we see that

   $$
   \sigma_C(\by)  = \infty.
   $$
1. Thus, $\sigma_C(\by) = 0$ for all $\by \in C^{\circ}$
   and $\sigma_C(\by)  = \infty$ otherwise.
1. Thus, $\sigma_C = I_{C^{\circ}}$.
```

```{prf:example} Support function of nonnegative orthant
:label: res-cvxf-support-nng-orthant

Let $\VV = \RR^n$ and $C = \RR^n_+$. $C$ is the
nonnegative orthant which is a closed convex cone.
Its polar cone is given by

$$
C^{\circ} = \RR^n_-
$$
which is the nonpositive orthant $\{\bx \in \RR^n \ST \bx \preceq \bzero \}$.
By {prf:ref}`res-cvxf-support-cone`,

$$
\sigma_{\RR^n_+} (\by) = I_{\RR^n_-} (\by).
$$
```

### Affine Sets

```{prf:theorem} Support function for an affine set
:label: res-cvxf-support-affine-set

Let $\BB \in \RR^{m \times n}$ and $\bb \in \RR^m$.
Define the set $C \subseteq \RR^n$ as

$$
C = \{\bx \in \RR^n \ST \bB \bx = \bb \}.
$$
Assume that $C$ is nonempty and let $\bx_0 \in C$
be one of the solutions of the system of equations $\bB \bx = \bb$.
Then

$$
\sigma_C(\by) = \langle \bx_0, \by \rangle + I_{\range (\bB^T)} (\by).
$$
```

```{prf:proof}
We proceed as follows.

1. By definition of support function

   $$
   \sigma_C(\by) = \sup \{  \langle \bx, \by \rangle \ST \bB \bx  = \bb \}.
   $$
1. Introduce a variable $\bz = \bx - \bx_0$.
1. Then $\bx = \bz + \bx_0$.
1. Accordingly

   $$
   \sigma_C(\by) &= \sup \{  \langle \bz + \bx_0, \by \rangle 
      \ST \bB (\bz + \bx_0)  = \bb \} \\
   &= \langle \bx_0, \by \rangle  
   + \sup \{  \langle \bz, \by \rangle \ST \bB \bz = \bzero \} \\
   &= \langle \bx_0, \by \rangle  + \sigma_D (\by)
   $$
   where $D = \{\bx \ST \bB \bx = \bzero \}$.
1. We note that the statement $\bB \bx = \bzero$ is equivalent to
   $\bB \bx \succeq \bzero$ and $\bB \bx \preceq \bzero$.
1. In other words, $D = \{ \bx \in \RR^n \ST \bA \bx \preceq \bzero \}$
   where $\bA = \begin{bmatrix}\bB \\ - \bB \end{bmatrix}$.
1. The set $D$ is a convex polyhedral cone.
1. By {prf:ref}`res-cvxf-support-cone`, the support function
   of a cone is the indicator function of its polar cone.
1. By {prf:ref}`res-cvx-polar-polyhedral-cone`, the 
   polar cone is given by

   $$
   D^{\circ} = \{ \bB^T \bt_1 - \bB^T \bt_2 \ST \bt_1, \bt_2 \succeq \bzero \}.
   $$
1. It is easy to see that $D^{\circ}  = \range (\bB^T)$.
   1. Every vector $\bt \in \RR^m$ can be split into two vectors 
      $\bt_1, \bt_2 \in \RR^m_+$
      such that $\bt = \bt_1 - \bt_2$.
   1. Accordingly $\bB^T \bt = \bB^T \bt_1 - \bB^T \bt_2$.
1. This gives us

   $$
   \sigma_C(\by) = \langle \bx_0, \by \rangle  + I_{D^{\circ}} (\by).
   $$
```


### Norm Balls

```{prf:theorem} Support functions for unit balls
:label: res-cvxf-support-unit-ball

Let $\VV$ be a real vector space endowed with a norm
$\| \cdot \|: \VV \to \RR$.
Consider the (closed) unit ball given by

$$
C = B_{\| \cdot \|}[\bzero, 1] = \{\bx \in \VV \ST \| \bx\| \leq 1 \}.
$$

Then, the support function is given by

$$
\sigma_C (\by) = \| \by \|_*
$$

where $\| \cdot \|_*: \VV \to \RR$ represents the dual norm.
```


```{prf:proof}
This flows directly from the definitions
of support function and {prf:ref}`dual norm <res-la-rip-dual-norm>`.

$$
\sigma_C (\by) = \sup\{ \langle \bx, \by \rangle \ST \bx \in C \}
= \sup\{ \langle \bx, \by \rangle \ST \| \bx \| \leq 1 \}
= \| \by \|_*.
$$
```

## Gauge Functions


```{index} Gauge function
```
```{prf:definition} Gauge function for a set
:label: def-cvxf-gauge-function

Let $\VV$ be a real vector space. Let $C$ be a nonempty subset of $\VV$.
The *gauge function* $\gamma_C : \VV \to \RERL$ is defined as

$$
\gamma_C (\bx) =  \inf \{r \geq 0 \ST \bx \in r C \}.
$$
If $\bx \notin r C$ for any $r \geq 0$, then $\gamma_C(\bx) = \infty$.
This is consistent with the convention that $\inf \EmptySet = \infty$.

The gauge function is also known as *Minkowski functional*.
```

```{prf:property} Nonnegativity
The Gauge function is always nonnegative.

```

```{prf:property} Value at origin

$$
\gamma_C (\bzero) = 0.
$$
```

```{prf:property} Subadditive 
If $C$ is convex, then the gauge function is subadditive.

$$
\gamma_C (\bx + \by) \leq  \gamma_C (\bx) + \gamma_C(\by).
$$
```
```{prf:proof}

We proceed as follows.

1. If $\gamma_C (\bx) = \infty$ or $\gamma_C(\by) = \infty$, then
   the inequality is satisfied trivially. So assume that both are finite.
1. Then, the sets $X = \{r \geq 0 \ST \bx \in r C \}$ and $Y = \{r \geq 0 \ST \by \in r C \}$
   are not empty.
1. Thus, we can choose some $s \geq \gamma_C (\bx)$ from $X$ 
   and $t \geq \gamma_C(\by)$ from $Y$.
1. If $s=0$ or $t=0$, then $\bzero \in C$. Consequently, 
   
   $$
   \gamma_C (\bx + \by) = \gamma_C (\bx) = \gamma_C (\by) = 0 
   \leq \gamma_C (\bx) + \gamma_C(\by) \leq s + t.
   $$
   and the inequality is satisfied.
1. Now, consider the case where $s > 0$ and $t > 0$.
1. Then, $\frac{\bx}{s} \in C$ and $\frac{\by}{t} \in C$.
1. Now,

   $$
   \frac{\bx + \by}{s + t} = \frac{s}{s + t} \frac{\bx}{s} + \frac{t}{s + t}\frac{\by}{t}.
   $$
1. Thus, $\frac{\bx + \by}{s + t}$ is a convex combination of  $\frac{\bx}{s}$
   and $\frac{\by}{t}$.
1. Since $C$ is convex, hence $\frac{\bx + \by}{s + t} \in C$. 
1. Thus, $s + t \in \{ r \geq 0 \ST (\bx + \by) \in rC  \}$.
1. Thus, $\gamma_C (\bx + \by) \leq s + t$.
1. Thus, for every $s \geq \gamma_C (\bx)$ and every $t \geq \gamma_C(\by)$,
   $\gamma_C (\bx + \by) \leq s + t$.
1. Taking infimum on the R.H.S. over $s \in X$ and $t \in Y$, we obtain,
   $\gamma_C (\bx + \by) \leq  \gamma_C (\bx) + \gamma_C(\by)$.
```


```{prf:property} Homogeneous 
The Gauge function is homogeneous.

$$
\gamma_C (s \bx) =  |s| \gamma_C (\bx) \Forall s \in \RR.
$$
```



```{prf:property} Seminorm 
The Gauge function is a seminorm.
```



```{prf:example} Norm as a gauge function
:label: ex-cvxf-norm-gauge-function

Let $\VV$ be a normed linear space with the norm $\| \cdot \| : \VV \to \RR$.

Let $\overline{B} = \{\bx \in \VV \ST \| \bx \| \leq 1 \}$ be the unit closed ball.

Then, 

$$
\gamma_{\overline{B}} (\bx) = \inf \{r \geq 0 \ST \bx \in r \overline{B} \} = \| \bx \|.
$$
The gauge function for the closed unit ball is simply the norm itself.
```


## Jensen's Inequality

Jensen's inequality stated below is another formulation for 
convex functions. 

````{prf:theorem} Jensen's inequality
:label: res-cvxf-jensen-inequality

A proper function $f: \VV \to \RERL$ is convex if and only if 

```{math}
:label: eq-cvxf-jensen-inequality
f(t_1 \bx_1 + \dots + t_k \bx_k) \leq t_1 f(\bx_1) + \dots + t_k f(\bx_k)
```
holds true for every $\bx_1, \dots, \bx_k \in \VV$
whenever $t_1, \dots, t_k \geq 0$ and $t_1 + \dots + t_k = 1$.
This inequality is known as the *Jensen's inequality*.
````

```{prf:proof}
The Jensen's inequality reduces to {eq}`eq-convexity-inequality`
for $k=2$. Thus, the statement is true by definition for $k=2$.
For $k > 2$, we shall present an inductive proof. 

Assume $f$ is convex. Then $\dom f$ is convex and
for all $\bx_1,\bx_2 \in \dom f$, 
and $t \in [0, 1]$, we have:

$$
f(t \bx_1 + (1-t) \bx_2) \leq t f(\bx_1) + (1-t) f(\bx_2).
$$


1. Let $\bx_1, \dots, \bx_k \in \VV$.
1. If any of $\bx_i \notin \dom f$ for some $i \in 1,\dots,k$, then
   $f(\bx_i) = \infty$ and the Jensen's inequality holds trivially.
1. Thus, we shall assume that $\bx_1, \dots, \bx_k \in \dom f$.
1. Since $\dom f$ is convex, hence their convex combination
   $t_1 \bx_1 + \dots + t_k \bx_k \in \dom f$.
1. Inductively, assume that the Jensen's inequality holds for $k-1$; i.e.,
   
   $$
   f(r_1 \bx_1 + \dots + r_{k-1} \bx_{k-1}) \leq r_1 f(\bx_1) + \dots + r_{k-1} f(\bx_{k-1})
   $$ 
   holds true whenever $r_1, \dots, r_{k-1} \geq 0$ and $r_1 + \dots + r_{k-1} = 1$.
1. WLOG, assume that $t_k < 1$. Thus, $1 - t_k > 0$.
1. Define $\by = \sum_{i=1}^{k-1} t'_i \bx_i$ where
   $t'_i = \frac{t_i}{1 - t_k}$.
1. Note that $t'_i \geq 0$. Also, $\sum_{i=1}^{k-1} t'_i = 1$
   since $\sum_{i=1}^{k-1} t_i = 1 - t_k$.
1. We can now write:
   
   $$
   f(t_1 \bx_1 + \dots + t_k \bx_k) 
   &= f((1 - t_k) \by +  t_k \bx_k )\\
   &\leq (1 - t_k)f (\by) + t_k f(\bx_k)\\
   &= (1 - t_k)  f(t'_1 \bx_1 + \dots t'_{k-1} \bx_{k-1}) + t_k f(\bx_k)\\
   &\leq (1 - t_k) ( t'_1 f(\bx_1)  + \dots + t'_{k-1} f(\bx_{k-1})) + t_k f(\bx_k)\\
   &= t_1 f(\bx_1) + \dots + t_{k-1} f(\bx_{k-1}) + t_k f(\bx_k).
   $$
1. Thus, $f$ satisfies Jensen's inequality.


For the converse, assume that $f$ satisfies Jensen's inequality.
Let $\bx_1, \bx_2 \in \dom f$ and $t \in [0,1]$. Then, 
by Jensen's inequality for $k=2$,

$$
f(t \bx_1 + (1-t) \bx_2) \leq t f(\bx_1) + (1-t) f(\bx_2) < \infty.
$$
Thus, $t \bx_1 + (1-t) \bx_2 \in \dom f$. Thus, $\dom f$ is convex.
Also, $f$ satisfies {eq}`eq-convexity-inequality`. Hence, $f$ is convex.
```

Jensen's inequality is essential in proving 
a number of famous inequalities. 

```{prf:example}  Logarithm and Jensen's inequality
:label: res-cvxf-log-jensen

In {prf:ref}`ex-cvxf-real-logarithm`, we show that
$\ln(x)$ is concave. Consequently, $-\ln(x)$ is convex.

Now, let $x_1, \dots, x_n \in \RR_{++}$ be positive 
real numbers and let $t_1, \dots, t_n \geq 0$ such that
$t_1 + \dots + t_n = 1$. Then, by Jensen's inequality

$$
-\ln (t_1 x_1 + \dots + t_n x_n) \leq - t_1 \ln x_1 - \dots - t_n \ln x_n.
$$

Multiplying by $-1$ and taking exponential on both sides, we obtain

$$
t_1 x_1 + \dots + t_n x_n \geq x_1^{t_1} \dots x_n^{t_n}.
$$

For a particular choice of $t_1 = \dots = t_n = \frac{1}{n}$, we obtain

$$
\frac{1}{n}(x_1 + \dots + x_n) \geq \sqrt[n]{x_1 \dots x_n}
$$
which is the AM-GM inequality suggesting that arithmetic mean is greater
than or equal to the geometric mean for a group of positive real numbers.
```


````{prf:theorem} Jensen's inequality for nonnegative homogeneous convex functions
:label: res-cvxf-jensen-inequality-nonneg-hom

If $f: \VV \to \RERL$ is a nonnegative homogeneous proper convex function,
then 

```{math}
:label: eq-cvxf-jensen-nonneg-hom
f(t_1 \bx_1 + \dots + t_k \bx_k) \leq t_1 f(\bx_1) + \dots + t_k f(\bx_k)
```
holds true for every $\bx_1, \dots, \bx_k \in \VV$
whenever $t_1, \dots, t_k \geq 0$.
````

```{prf:proof}

Let $\bx_1, \dots, \bx_k \in \VV$.
If any of $\bx_i \notin \dom f$ for some $i \in 1,\dots,k$, then
$f(\bx_i) = \infty$ and the inequality holds trivially.
Thus, we shall assume that $\bx_1, \dots, \bx_k \in \dom f$.

By {prf:ref}`res-cvxf-nonneg-hom-convex-subadditive`, $f$ is subadditive.
Thus,

$$
f(t_1 \bx_1 + \dots + t_k \bx_k) \leq f(t_1 \bx_1) + \dots + f(t_k \bx_k).
$$

The nonnegative homogeneity gives us

$$
f(t_1 \bx_1) + \dots + f(t_k \bx_k) = t_1 f(\bx_1) + \dots + t_k f(\bx_k).
$$

We are done.
```




## Quasi-Convex Functions


```{index} Quasi convex function
```
```{prf:definition} Quasi convex function
:label: def-cvxf-quasi-convex-function

Let $\VV$ be a real vector space.
Let  $f : \VV \to \RR$ be a real valued function.
Let the sublevel sets of $f$ be given by

$$
C_{\alpha} = \{ \bx \in \dom f \,|\, f(\bx) \leq \alpha \}.
$$

If the sublevel sets $C_{\alpha}$ of $f$ are convex for every $\alpha \in \RR$,
then $f$ is called a *quasi-convex* function.
```

