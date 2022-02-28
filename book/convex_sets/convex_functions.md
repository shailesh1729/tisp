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


## Convexity of a Function

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
````



```{figure} ../images/convex_function.png
---
name: convex_function
---
Graph of a convex function. The line segment
between any two points on the graph lies 
above the graph.
```

For a convex function, every chord lies above the graph of the function. 


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

```{prf:example} Absolute value is convex
:label: ex-cvxf-real-abs

Let $f : \RR \to \RR$ be:

$$
f(x) = |x|.
$$
with $\dom f = \RR$.

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
```

```{prf:theorem} All norms are convex
:label: res-cvxf-norms-convex

Let $\| \cdot \| \to \RR$ be a 
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

```{prf:theorem} Function convexity = Epigraph convexity
:label: res-cvxf-convexity-epigraph

Let $\VV$ be a real vector space.
A function $f: \VV \to \RR$ is convex if and only if its epigraph
$\epi f$ is a convex set.
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




## Extended Value Extensions
Tracking domains of convex functions is difficult.
It is often convenient to extend a convex function
$f : \VV \to \RR$ with a domain $\dom f \subset \VV$
to all of $\VV$ by defining it to be $\infty$ 
outside its domain. 

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


```{prf:theorem}
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
   $f(\bx_i) = \infty$ and the Jensen's inequality holds vacuously.
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



## First Order Conditions

Let us look at the special case of 
real valued functions over $\RR^n$ 
which are differentiable.

````{prf:theorem} First order characterization of convexity
:label: res-cvxf-gradient-convexity-relation

Let $f : \RR^n \to \RR$ be a real valued function
which is {prf:ref}`differentiable <def-mvc-differentiable-function>`
at each point in $\dom f$ which is open.

Then $f$ is convex if and only if $\dom f$ is convex
and 

```{math}
:label: eq-cvxf-first-order-convexity-condition
f(\by) \geq f(\bx) + \nabla f(\bx)^T (\by - \bx)
```
holds true for all $\bx, \by \in \dom f$.
````


```{prf:proof}
To prove {eq}`eq-cvxf-first-order-convexity-condition`,
we first show that a differentiable real function $f: \RR \to \RR$
is convex if and only if  

$$
f(y) \geq f(x) + f'(x)(y - x)
$$
holds true for all $x, y \in \dom f$.


Assume that $f$ is convex. Hence, $\dom f$ is convex too.

1. Let $x,y \in \dom f$.
1. Since $\dom f$ is convex, hence 
   $ (1-t) x + t y = x + t(y-x) \in \dom f$ for all $t \in [0, 1]$.
1. By convexity of $f$, we have:

   $$
   f(x + t(y-x)) \leq (1-t) f(x) + t f(y).
   $$
1. If we divide by $t$ on both sides, we obtain:

   $$
   f(y) \geq f(x) + \frac{f(x + t(y-x)) - f(x)}{t}.
   $$
1. Taking the limit as $t \to 0^+$, we obtain:

   $$
   f(y) \geq f(x) + f'(x)(y-x).
   $$

For the converse, assume that $\dom f$ is convex and

$$
f(y) \geq f(x) + f'(x)(y - x)
$$
holds true for all $x, y \in \dom f$.

1. Recall that in $\RR$ the only convex sets are 
   intervals. Thus, $\dom f$ is an open interval.
1. Choose any $x, y \in \dom f$ such that $x \neq y$.
1. Choose $t \in [0,1]$.
1. Let $z = t x + (1-t)y$.
1. By hypothesis, we have:
   
   $$
   f(x) \geq f(z) + f'(z) (x - z)
   $$
   and

   $$
   f(y) \geq f(z) + f'(z) (y - z).
   $$
1. Multiplying the first inequality with $t$ and second
   with $(1-t)$ and adding them yields:
   
   $$
   t f(x) + (1-t) f(y) \geq f(z) = f(tx + (1-t)y).
   $$
1. Thus, $f$ is convex.


We now prove for the general case with $f : \RR^n \to \RR$.
Recall from {prf:ref}`res-cvxf-convx-on-lines`
that for any $\bx, \by \in \dom f$ 
the restriction of $f$ on the line passing through $\bx$ and $\by$
is given by:

$$
g(t) = f(t\by + (1-t) \bx) = f(\bx + t(\by - \bx)).
$$

Note that, by chain rule ({prf:ref}`ex-f-rest-line-chain-rule`):

$$
g'(t) = \nabla f(t\by + (1-t) \bx)^T (\by - \bx)
$$

Assume $f$ is convex.
1. Let $\bx, \by \in \dom f$ such that $\bx \neq \by$.
1. Let $g$ be the restriction of $f$ on the line passing through
   $\bx, \by$ as described above.
1. Due to {prf:ref}`res-cvxf-convx-on-lines`, $g$ is convex.
1. By the argument for real functions above:

   $$
   g(t') \geq g(t) + g'(t)(t' - t)
   $$
   holds true for all $t, t' \in \dom g$.
1. In particular, with $t'=1$ and $t=0$, we have:

   $$
   g(1) \geq g(0) + g'(0).
   $$
1. But $g'(0) = \nabla f(\bx)^T (\by - \bx)$.
1. Also, $g(1) = f(\by)$ and $g(0) = f(\bx)$.
1. Thus, we get:

   $$
   f(\by) \geq f(\bx) + \nabla f(\bx)^T (\by - \bx)
   $$
   as desired.


For the converse, assume that this inequality holds
for all $\bx, \by \in \dom f$ and $\dom f$ is convex.

1. Pick some $\bx, \by \in \dom f$ with $\bx \neq \by$.
1. Let $g$ be the restriction of $f$ on the line passing through
   $\bx, \by$ as described above.
1. Pick $t_1, t_2 \in \dom g$.
1. Then, $\bz_1 = t_1\by + (1-t_1) \bx$ and 
   $\bz_2 = t_2\by + (1-t_2) \bx$
   are in $\dom f$.
1. Consider $g(t_1) = f(t_1\by + (1-t_1) \bx) = f(\bz_1)$
   and $g(t_2) = f(t_2\by + (1-2_1) \bx) = f(\bz_2)$.
1. Note that $g'(t_2) =  \nabla f(t_2\by + (1-t_2) \bx)^T (\by - \bx) = \nabla f(\bz_2)^T (\by - \bx)$.
1. By hypothesis, we have:

   $$
   f(\bz_1) \geq f(\bz_2) + \nabla f(\bz_2)^T (\bz_1 - \bz_2).
   $$
1. But $\bz_1  - \bz_2 = (t_1 - t_2) (\by - \bx)$.
1. Thus, we get:

   $$
   g'(t_1) \geq g'(t_2) + g'(t_2)(t_1 - t_2).
   $$
1. This holds for every $t_1, t_2 \in \dom g$.
1. But then, $g$ is convex by previous argument for
   real functions.
1. Since this is valid for every restriction of $f$ 
   to a line passing through its domain, hence
   by {prf:ref}`res-cvxf-convx-on-lines` $f$ is convex.
```


## Second Order Conditions

For functions which are twice differentiable,
convexity can be expressed in terms of the positive-semidefiniteness of
their Hessian matrices.

We start with a result on convexity of real functions on open intervals.

```{prf:theorem} Convexity characterization for twice differentiable real functions on open intervals
:label: res-cvxf-2nd-derivative-convexity-interval

Let $f : \RR \to \RR$ be twice continuously differentiable on an open interval
$(\alpha, \beta)$;
i.e., second derivative $f''$ exists and is continuous
at every point the open interval $(\alpha, \beta)$.

Then, $f$ is convex if and only if
its second derivative $f''$ is non-negative
for every $x \in (\alpha, \beta)$:

$$
f''(x) \geq 0 \quad \Forall x \in (\alpha, \beta).
$$ 
```

```{prf:proof}
Assume that $f''$ is nonnegative on $(\alpha, \beta)$.

1. Then, $f'$ is nondecreasing on $(\alpha, \beta)$.
1. For any $x, y \in (\alpha, \beta)$ with $x < y$ 
   and $r \in (0,1)$,
   let $z = (1-r)x  + r y$.
1. We have $z \in (x,y)$; i.e. $x < z < y$. Consequently,

   $$
   & f(z) - f(x) = \int_x^z f'(t) dt \leq f'(z) (z - x);\\
   &f(y) - f(z) = \int_z^y f'(t) dt \geq f'(z) (y - z).
   $$
1. Since $z-x = r(y - x)$ and $y -z = (1-r)(y - x)$, we have

   $$
   f(z) \leq f(x) + r f'(z) (y -x);\\
   f(z) \leq f(y) - (1-r) f'(z) (y -x ).
   $$
   We wish to eliminate $f'(z)$ from these inequalities.
1. Multiplying the two inequalities by $(1-r)$ and $r$ respectively,
   and adding them together, we obtain:

   $$
   (1-r)f(z) + r f(z) \leq (1-r)f(x) + r f(y).
   $$
1. But $(1-r)f(z) + r f(z) = f(z) = f((1-r)x + r y)$.
1. Thus, $f((1-r)x + r y) \leq (1-r)f(x) + r f(y)$.
1. This inequality is valid for the case where $x > y$ also.
1. Thus, $f$ is convex over $(\alpha, \beta)$.


For the converse, assume that $f''$ is not non-negative on $(\alpha, \beta)$.
1. Then, since $f''$ is continuous in $(\alpha, \beta)$, 
   hence $f''$ is negative in some subinterval
   $(\alpha', \beta')$.
1. Choose $x, y$ such that $\alpha' < x < y < \beta'$. Choose some $r \in (0,1)$.
1. Following an argument parallel to above, we have

   $$
   f((1-r)x  + r y) > (1-r) f(x) + r f(y).
   $$
1. Thus, there exist $x, y \in (\alpha, \beta)$ where the inequality 
   {eq}`eq-convexity-inequality` is not valid.
1. Consequently, $f$ is non-convex.
```

We continue further with 
real valued functions over $\RR^n$ 
which are twice differentiable.


```{prf:theorem} Second order characterization of convexity in Euclidean spaces
:label: res-cvxf-hessian-convexity-relation

Let $f : \RR^n \to \RR$ be twice continuously differentiable;
i.e., its {prf:ref}`Hessian <def-mvp-hessian>`
or second derivative $\nabla^2 f$ exists 
at every point in $\dom f$ which is open.

Then, $f$ is convex if and only if
$\dom f$ is convex and its Hessian is positive semidefinite
for every $\bx \in \dom f$:

$$
\nabla^2 f(\bx) \succeq \ZERO \quad \Forall \bx \in \dom f.
$$ 
```

```{prf:proof}
The convexity of $f$ on its domain $C = \dom f$ is equivalent
to the convexity of the restriction of $f$ to each line segment
in $C$ due to {prf:ref}`res-cvxf-convx-on-lines`.

We first note that if $f$ is convex then $C$ is convex
and if $C$ is not convex, then $f$ is not convex. So, 
for the rest of the argument, we shall assume that $C$ is convex.

Consequently, for any $\by \in C$ and a nonzero $\bz \in \RR^n$
the intersection of the line $\{ \bx = \by + t \bz \ST t \in \RR\}$
and $C$ is an open line segment as $C$ is open and convex.

1. Let $\by \in C$.
1. Let $\bz \in \RR^n$ be an arbitrary (nonzero) direction.
1. Let $L = \{ \bx = \by + t \bz \ST t \in \RR\}$ be a line passing
   through $\by$ in the direction $\bz$. 
1. Consider the open real interval $S = \{t \ST \by + t \bz \in C\}$.
   Since $L \cap C$ is an open line segment in $\RR^n$, hence
   $S$ is indeed an open interval in $\RR$.
1. Consider the parameterized restriction of $f$ on the open interval $S$ as:

   $$
   g(t) = f(\by + t \bz), \Forall t \in S.
   $$
1. A simple calculation shows that

   $$
   g''(t) = \langle \bz, \nabla^2 f(\bx) \bz \rangle
   $$
   where $\bx = \by + t \bz$.
1. By {prf:ref}`res-cvxf-2nd-derivative-convexity-interval`,
   $g$ is convex for each $\by \in C$ and nonzero $\bz \in \RR^n$ if and only if
   $\langle \bz, \nabla^2 f(\bx) \bz \rangle \geq 0$ for every $\bz \in \RR^n$
   and $\bx \in C$.
1. Thus, $f$ is convex if and only if 
   $\nabla^2 f(\bx) \succeq \ZERO \quad \Forall \bx \in C$.
```

For real functions, the Hessian is simply the
second derivative $f''$.




```{prf:corollary} Second order characterization of concavity
:label: res-cvxf-hessian-concavity-relation

Let $f : \RR^n \to \RR$ be twice differentiable;

Then, $f$ is concave if and only if
$\dom f$ is convex and its Hessian is negative semidefinite
for every $\bx \in \dom f$:

$$
\nabla^2 f(\bx) \preceq \ZERO \quad \Forall \bx \in \dom f.
$$ 
```


```{prf:example} Convexity of a quadratic function
:label: ex-cvxf-quadratic-func-convexity

Let $\bP \in \SS^n$ be a symmetric matrix. 
Let $\bq \in \RR^n$ and $r \in \RR$. 
Consider the quadratic functional $f: \RR^n \to \RR$ given as:

$$
f(\bx) = \frac{1}{2} \bx^T \bP \bx + \bq^T \bx + r.
$$

As shown in {prf:ref}`ex-mvc-hessian-quadratic-form`, 
the Hessian of $f$ is:

$$
\nabla^2 f (\bx) = \bP \quad \Forall \bx \in \RR^n.
$$
Thus, $f$ is convex if and only if $\bP \succeq \ZERO$ 
(i.e., it is positive semidefinite).

In fact $f$ is strictly convex if and only if $P \succ \ZERO$.
```

```{prf:example} Identity is convex and concave
:label: ex-cvxf-real-identity

Let $f : \RR \to \RR$ be:

$$
f(x) = x.
$$

We have $f'(x) = 1$ and $f''(x) = 0$.

$f$ is both convex and concave. 
```

```{prf:example} Exponential is convex
:label: ex-cvxf-real-exponential

Let $f : \RR \to \RR$ be:

$$
f(x) = e^{ax}
$$
with $\dom f = \RR$.

We have $f'(x) = a e^{ax}$ and $f''(x) = a^2 e^{ax}$. 

For any $a,x \in \RR$, $a^2 e^{ax} > 0$. 
Thus, $f$ is strictly convex.
```



```{prf:example} Powers
:label: ex-cvxf-real-power-x-a


Let $f : \RR \to \RR$ be:

$$
f(x) = x^a
$$
with $\dom f = \RR_{++}$.

Now, $f'(x) = a x^{a-1}$ and $f''(x) = a (a - 1) x^{a-2}$.

1. We have $x > 0$.
1. For $a \geq 1$, $f''(x) \geq 0$. 
   $f$ is convex for $a \geq 1$.
1. For $a \leq 0$, $a (a -1) \geq 0$. 
   Thus, $f''(x) \geq 0$. $f$ is convex for $a \leq 0$.
1. For $0 \leq a \leq 1$, $a (a-1) \leq 0$. Thus, $f''(x) \leq 0$. 
   $f$ is concave on $0 \leq a \leq 1$.
```


```{prf:example} Powers of absolute value
:label: ex-cvxf-real-power-absolute-x-a


Let $f : \RR \to \RR$ be:

$$
f(x) = |x|^a
$$
with $\dom f = \RR_{++}$.
```

```{prf:example} Reciprocal powers
:label: ex-cvxf-real-reciprocal-power-x-r

Let $f : \RR \to \RR$ be:

$$
f(x) = \frac{1}{x^r} = x^{-r}.
$$
with $\dom f = \RR_{++}$.

Now, $f'(x) = (-r) x^{-r-1}$ and $f''(x) = (-r)(-r - 1) x^{-r-2} = r(r+1) x^{-(r+2)}$.

1. We have $x > 0$.
1. For $r \geq 0$, $f''(x) \geq 0$. 
   $f$ is convex for $r \geq 0$.
```


```{prf:example} Logarithm is concave
:label: ex-cvxf-real-logarithm

Let $f : \RR \to \RR$ be:

$$
f(x) = \ln x.
$$
with $\dom f = \RR_{++}$.

Now, $f'(x) = \frac{1}{x}$ and $f''(x) = \frac{-1}{x^2}$.

1. $f''(x) < 0$ for all $x > 0$.
1. Thus, $f$ is concave for all $x > 0$.
```


```{prf:example} Negative entropy is convex
:label: ex-cvxf-real-negative-entropy

Let $f : \RR \to \RR$ be:

$$
f(x) = x \ln x.
$$
with $\dom f = \RR_{++}$.

Now, $f'(x) = \ln x + 1$ and $f''(x) = \frac{1}{x}$.

1. $f''(x) > 0$ for all $x > 0$.
1. Thus, $f$ is convex for all $x > 0$.
```

```{prf:example} Quadratic over linear form is convex
:label: ex-cvxf-r-r-quad-lin

Let $f : \RR \times \RR \to \RR$ be given by:

$$
f(x, y) = \frac{x^2}{y}
$$
with $\dom f = \{ (x, y) \ST y > 0\}$.

From {prf:ref}`ex-mvc-derivatives-quad-lin-func`, 
the Hessian is:


$$
\nabla^2 f(x, y) = 
\frac{2}{y^3} \begin{bmatrix}
y^2 & - x y\\
- x y & x^2
\end{bmatrix}
= \frac{2}{y^3} 
\begin{bmatrix} y\\ - x \end{bmatrix}
\begin{bmatrix} y\\ - x \end{bmatrix}^T .
$$

Recall that for any $\bx \in \RR^n$, the matrix $\bx \bx^T$
is positive semi-definite. 
Hence,

$$
\begin{bmatrix} y\\ - x \end{bmatrix}
\begin{bmatrix} y\\ - x \end{bmatrix}^T
$$
is positive semi-definite.

For $y > 0$, $\frac{2}{y^3} > 0$. Combining:

$$
\nabla^2 f(x, y) \succeq \ZERO.
$$

Thus, $f$ is convex.
```


```{prf:example} Log sum exponential is convex
:label: ex-cvxf-log-sum-exp

Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) = \ln \left ( \sum_{i=1}^n e^{x_i} \right )
$$
with $\dom f = \RR^n$.

From {prf:ref}`ex-mvc-hessian-log-sum-exp`, we have

$$
\nabla^2 f(\bx) = \frac{1}{(\bone^T \bz)^2} \left ((\bone^T \bz) \Diag (\bz) - \bz \bz^T \right )
$$

where 

$$
\bz = \begin{bmatrix}
e^{x_1} \\ 
\vdots \\
e^{x_n}
\end{bmatrix}.
$$

To show that $\nabla^2 f(\bx)$ is p.s.d., it suffices to
show that $(\bone^T \bz) \Diag (\bz) - \bz \bz^T$ is p.s.d..

Now for any $\bv \in \RR^n$. 

$$
&\bv^T \left ( (\bone^T \bz) \Diag (\bz) - \bz \bz^T \right ) \bv\\
&= (\bone^T \bz) (\bv^T \Diag (\bz) \bv) - \bv^T  \bz \bz^T \bv \\
&= (\bone^T \bz) (\bv^T \Diag (\bz) \bv) - (\bv^T  \bz)^2 \\
&= \left (\sum_{i=1}^n z_i \right ) 
\left (\sum_{i=1}^n v_i^2 z_i \right)
- \left (\sum_{i=1}^n v_i z_i \right )^2.
$$

If we define vectors $\ba$ and $\bb$ with
$a_i  = v_i \sqrt{z_i}$ and $b_i = \sqrt{z_i}$,
then by 
{prf:ref}`Cauchy-Schwartz inequality <res-la-ip-cauchy-chwartz-inequality>`
, we have:

$$
(\ba^T \ba)(\bb^T \bb) \geq (\ba^T \bb)^2
\iff (\ba^T \ba)(\bb^T \bb) - (\ba^T \bb)^2 \geq 0.
$$

But this is exactly the expression above.
Thus, $\nabla^2 f(\bx) \succeq \ZERO$.

Hence, $f$ is convex.
```


```{prf:example} Log determinant function is concave
:label: ex-cvxf-log-det

Let $f : \SS^n \to \RR$ be:

$$
f(\bX) = \log \det X.
$$
with $\dom f = \SS^n_{++}$ (the set of symmetric positive definite matrices).

Let any line in $\SS^n$ be given by:

$$
\bX = \bZ + t \bV 
$$
where $\bZ, \bV \in \SS^n$.

Consider the restriction of $f$ on a line:

$$
g(t) = \log \det (\bZ + t \bV) 
$$
to the interval of values where $\bZ + t \bV \succ \ZERO$ 
(since $\dom f = \SS^n_{++}$ ).
In other words, 

$$
\dom g = \{t \in \RR \ST \bZ + t \bV \succ \ZERO \}.
$$

Without any loss of generality, we can assume that $t=0 \in \dom g$;
i.e. $\bZ \succ \ZERO$.

Recall that:
1. $\det (AB) = \det(A) \det(B)$ for square matrices.
1. $ \det (A) = \prod_{i=1}^n \lambda_i $ for symmetric matrices with $\lambda_i$ 
   being their eigen values.
1. If $\lambda_i$ are eigen values of $A$, then the eigen values of $I + t A$ are
   $1 + t \lambda_i$.


Now

$$
g(t) &= \log \det (\bZ + t \bV) \\
&= \log \det (\bZ^{\frac{1}{2}} (\bZ^{\frac{1}{2}} + t \bZ^{-\frac{1}{2}} \bV) )\\
&= \log \det (\bZ^{\frac{1}{2}} (I + t \bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}) \bZ^{\frac{1}{2}})\\
&= \log \det(\bZ^{\frac{1}{2}}) + \log \det (I + t \bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}})
  + \log \det(\bZ^{\frac{1}{2}})\\
&= \log \det(\bZ) + \log \det (I + t \bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}).
$$

1. Let $\lambda_i$ be the eigen values of $\bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}$. 
1. Then, $1 + t \lambda_i$ are eigen values of $I + t\bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}$.
1. Thus, $\log \det (I + t\bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}) = \sum_{i=1}^n \log \det (1 + t\lambda_i)$.


Thus,

$$
g(t) = \sum_{i=1}^n \log \det (1 + t\lambda_i) + \log \det(\bZ).
$$
Note that $\log \det(\bZ)$ doesn't depend on $t$.
Similarly, $\lambda_i$ only depend on $\bZ$ and $\bV$, hence they don't depend on $t$.

Differentiating $g$ w.r.t. $t$, we get:

$$
g'(t) = \sum_{i=1}^n \frac{\lambda_i}{1 + t \lambda_i}.
$$

Differentiating again, we get:

$$
g''(t) = -\sum_{i=1}^n \frac{\lambda_i^2}{(1 + t \lambda_i)^2}.
$$

Since $g''(t) \leq 0$, hence $f$ is concave.
```

## Scaling and Addition of Convex Functions

Here we show some basic results about operations
that preserve convexity

```{prf:theorem} Nonnegative multiplication
:label: res-cvxf-nonnegative-mult-cvx

If $f$ is convex, then so is $\alpha f$ for all $\alpha \geq 0$.
```
```{prf:proof}

Assume $f$ is convex.
Note that $\dom f = \dom \alpha f$. 
Thus, $\dom \alpha f$ is convex since $\dom f$ is convex.

Now, let $\bx, \by \in \dom f$ and $t \in [0,1]$. Then

$$
& f(t\bx + (1-t) \by) \leq t f(\bx) + (1-t)f(\by)\\
& \implies  \alpha f(t\bx + (1-t) \by) \leq \alpha (t f(\bx) + (1-t)f(\by)) \Forall \alpha \geq 0\\
& \implies (\alpha f)(t\bx + (1-t) \by) \leq  t (\alpha f)(\bx) + (1-t) (\alpha f)(\by) \Forall \alpha \geq 0.
$$
Thus, $\alpha f$ is convex for every $\alpha \geq 0$.
```


```{prf:theorem} Convex function sum
:label: res-cvxf-func-sum

If $f$ and $g$ are convex, then so is $f + g$
with $\dom (f + g) = \dom f \cap \dom g$.
```
```{prf:proof}
We discussed earlier that $\dom (f + g) = \dom f \cap \dom g$
as $f + g$ is defined only for the points where both $f$ and $g$
are defined.

Recall from {prf:ref}`res-cvx-intersection`
that intersection of convex sets is convex.
Thus, $\dom (f + g)$ is convex since $\dom f$ and $\dom g$
are both convex.

Now let $\bx, \by \in \dom (f + g)$ and $t \in [0, 1]$.

1. Since $f$ is convex, hence
   
   $$
   f(t\bx + (1-t) \by) \leq t f(\bx) + (1-t) f(\by).
   $$
1. Since $g$ is convex, hence
   
   $$
   g(t\bx + (1-t) \by) \leq t g(\bx) + (1-t) g(\by).
   $$
1. Adding the two inequalities, we get:

   $$
   & f(t\bx + (1-t) \by) + g(t\bx + (1-t) \by) \leq 
   t f(\bx) + (1-t) f(\by) + t g(\bx) + (1-t) g(\by)\\
   & \implies 
   (f + g)(t\bx + (1-t) \by) \leq t (f + g)(\bx) + (1-t) (f + g)(\by).
   $$
1. Thus, $f+g$ is convex.
```

```{prf:theorem} Conic combinations of convex functions
:label: res-cvxf-func-conic-combs

If $f_1, \dots, f_n$ are convex, then for any
$t_1, \dots, t_n \geq 0$, the 
{prf:ref}`conic combination <def-conic-combination>`
of functions given by:

$$
f = t_1 f_1 + \dots + t_n f_n
$$
is also convex.
```

The conic combinations are also called nonnegative weighted
sums.

```{prf:proof}
Due to {prf:ref}`res-cvxf-nonnegative-mult-cvx`,
$t_i f_i$ are convex since $f_i$ are convex and $t_i \geq 0$.

Due to {prf:ref}`res-cvxf-func-sum`, sum
of two convex functions is convex.

It can be easily shown by mathematical induction
that sum of $n$ convex functions is convex too.

Thus, $f$ is convex.
```

```{prf:theorem}
:label: res-cvxf-total-funcs-cvx-cone

The set of convex functions 
in the {prf:ref}`vector space of real valued functions <def-la-is-real-valued-functions-space>`
form a convex cone.
```

Note that the set of real valued functions forms a vector
space over $\RR$ with the standard definitions of
function scalar multiplication and function addition.
We are examining the convexity of the set of functions
under this vector space.


```{prf:proof}
Since every conic combination of convex functions
is convex, hence the set of convex functions is
a convex cone.
```

```{prf:theorem} Concave function sum
:label: res-cvxf-concave-func-sum

If $f$ and $g$ are concave, then so is $f + g$
with $\dom (f + g) = \dom f \cap \dom g$.
```
```{prf:proof}
We proceed as follows:

1. Let $f$ and $g$ be concave.
1. $-f$ and $-g$ are convex.
1. By {prf:ref}`res-cvxf-func-sum`, $(-f) + (-g) = -(f + g)$
   is convex.
1. Thus, $f+g$ is concave.
```

```{prf:theorem} Conic combinations of cave functions
:label: res-cvxf-concave-func-conic-combs

If $f_1, \dots, f_n$ are concave, then for any
$t_1, \dots, t_n \geq 0$, the 
{prf:ref}`conic combination <def-conic-combination>`
of functions given by:

$$
f = t_1 f_1 + \dots + t_n f_n
$$
is also concave.
```

```{prf:proof}
We proceed as follows:

1. If $f_1, \dots, f_n$ are concave then $-f_1, \dots, -f_n$ are convex.
1. By {prf:ref}`res-cvxf-func-conic-combs`, 
   $(-t_1 f_1) + \dots + (-t_n f_n)$ is convex.
1. Thus, $-(t_1 f_1 + \dots + t_n f_n)$ is convex.
1. Thus, $t_1 f_1 + \dots + t_n f_n$ is concave. 
```

## Sublevel Sets

Recall from {prf:ref}`def-bra-sub-level-set`
that the $\alpha$-sublevel set for a 
real valued function $f : \VV \to \RR$ is given by

$$
C_{\alpha} = \{ \bx \in \dom f \,|\, f(\bx) \leq \alpha \}.
$$


```{prf:theorem}
:label: res-cvxf-convexity-sublevel-sets

If $f : \VV \to \RR$ is convex, 
then its sublevel sets are convex.
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


## Hypograph

The {prf:ref}`hypograph <def-bra-hypograph>`
of a function $f: \VV \to \RR$ is given by:

$$
\hypo f = \{ (\bx,t) \in \VV \oplus \RR \ST \bx \in \dom f, f(\bx) \geq t \}.
$$

Just like function convexity is connected to epigraph convexity,
similarly function concavity is connected to hypograph convexity.


```{prf:theorem} Function concavity = Epigraph convexity
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

## Composition with Affine Mapping


```{prf:theorem} Affine transformations preserve convexity
:label: res-cvx-affine-composition

Let $\VV$ and $\WW$ be real vector spaces.
Let $T : \VV \to \WW$ be a linear transformation.
Let $\bb \in \WW$.
Let $f : \WW \to \RR$ be a function.
Define $g : \VV \to \RR$ as:

$$
g(\bx) = f(T(\bx) + \bb)
$$
with $\dom g = \{\bx \in \VV \ST T(\bx) + \bb \in \dom f \}$.

If $f$ is convex, then so is $g$.
If $f$ is concave, then so is $g$.
```


```{prf:proof}

Assume $f$ is convex.

1. If we define $A : \VV \to \WW$ as $A(\bx) = T(\bx) + \bb $
   then $\dom g = A^{-1}(\dom f)$.
1. $A$, so defined, is an affine transformation.
1. By {prf:ref}`res-cvx-convex-set-inverse-affine-image`,
   $\dom g$ is convex since $\dom f$ is convex. 
1. Let $\bx, \by \in \dom g$.
1. $g(\bx) = f(T(\bx) + \bb)$. Define $\bu = T(\bx) + \bb$.
1. $g(\by) = f(T(\by) + \bb)$. Define $\bv = T(\by) + \bb$.
1. By definition, $\bu, \bv \in \dom f$.
1. Let $t \in [0,1]$.
1. Since $f$ is convex, hence

   $$
   f(t\bu + (1-t) \bv) \leq t f(\bu) + (1-t)f(\bv).
   $$
1. Now 

   $$
   g(t\bx + (1-t) \by)
   &= f(T(t\bx + (1-t) \by) + \bb)\\
   &= f(tT(\bx) + (1-t) T(\by) + (t + (1-t))\bb)\\
   &= f(t(T(\bx) + \bb) + (1-t) (T(\by) + \bb))\\
   &= f(t\bu + (1-t) \bv )\\
   &\leq t f(\bu) + (1-t) f(\bv)\\
   &= t g(\bx) + (1-t) g(\by).
   $$
1. Thus, $g$ satisfies the 
   convexity defining inequality {eq}`eq-convexity-inequality`.
1. Thus, $g$ is convex.

A similar argument shows that if $f$ is concave
then so is $g$.
```


## Pointwise Supremum

```{prf:theorem} Pointwise maximum of two convex functions
:label: res-cvx-ptws-max-2

Let $f_1$ and $f_2$ be convex functions. Define
their pointwise maximum as

$$
f(\bx) = \max \{f_1(\bx), f_2(\bx) \}
$$
with $\dom f = \dom f_1 \cap \dom f_2$.
Then, $f$ is convex.
```

```{prf:proof}
$\dom f$ is an intersection of convex sets. Hence, it is convex.

Let $\bx, \by \in \dom f$ and $t \in [0,1]$.

$$
f(t \bx + (1-t) \by)
&= \max \{f_1(t \bx + (1-t) \by), f_2(t \bx + (1-t) \by) \}\\
&\leq \max \{t f_1(\bx) + (1-t) f_1(\by), t f_2(\bx) + (1-t) f_2(\by) \}\\
&\leq t \max \{f_1(\bx), f_2(\bx) \} + (1-t)\max \{f_1(\by), f_2(\by) \}\\
&= t f(\bx) + (1-t) f(\by).
$$
Thus, $f$ is convex.
```


```{prf:theorem} Pointwise maximum of multiple convex functions
:label: res-cvx-ptws-max-n

Let $f_1, f_2, \dots, f_n$ be convex functions. Define
their pointwise maximum as

$$
f(\bx) = \max \{f_1(\bx), \dots, f_n(\bx) \}
$$
with $\dom f = \dom f_1 \cap \dots \cap \dom f_n$.
Then, $f$ is convex.
```

```{prf:proof}
The result has been proved for the base case of 2 functions
in {prf:ref}`res-cvx-ptws-max-2`.

Assume that it is true for $n$ functions. We
can easily show it true for $n+1$ functions since

$$
\max \{f_1(\bx), \dots, f_{n+1}(\bx) \}
= \max \{\max \{f_1(\bx), \dots, f_n(\bx) \}, f_{n+1}(\bx) \}.
$$

Thus, by principle of mathematical induction, the result
is true for all $n$.
```

```{prf:theorem} Pointwise supremum of a family of convex functions
:label: res-cvx-ptws-supremum

Let $I$ be an index set.
Let $\{ f_i : \VV \to \RR \}_{i \in I}$ be a family of convex functions. 
Define their pointwise supremum as

$$
f(\bx) = \sup \{f_i(\bx)\}_{i \in I}
$$
with 

$$
\dom f = \bigcap_{i \in I} \dom f_i.
$$
Then, $f$ is convex.
Moreover,

$$
\epi f = \bigcap_{i \in I} \epi f_i.
$$
```

```{prf:proof}
We  shall first verify the epigraph equality.

1. Let $(\bx, t) \in \epi f$.
1. Then, $f(\bx) \leq t$.
1. Thus, $f_i(\bx) \leq t$ for all $i \in I$ 
   since $f(\bx) = \sup \{f_i(\bx)\}_{i \in I}$.
1. Thus, $(\bx, t) \in \epi f_i$ for all $i \in I$.
1. Thus, $\epi f \subseteq \bigcap_{i \in I} \epi f_i$.


Now, for the converse:

1. Let $(\bx, t) \in \bigcap_{i \in I} \epi f_i$.
1. Thus, $(\bx, t) \in \epi f_i$ for all $i \in I$.
1. Thus, $f_i(\bx) \leq t$ for all $i \in I$.
1. Taking the supremum over $i \in I$ on the L.H.S., we obtain:

   $$
   \sup \{f_i(\bx)\}_{i \in I} = f(\bx) \leq t.
   $$
1. Thus, $(\bx, t) \in \epi f$.
1. Thus, $\bigcap_{i \in I} \epi f_i \subseteq \epi f$.

Combining the two, we get:

$$
\epi f = \bigcap_{i \in I} \epi f_i.
$$

1. Since $f_i$ are convex functions, hence $\epi f_i$ are convex sets
   due to {prf:ref}`res-cvxf-convexity-epigraph`.
1. Thus, $\epi f$ is a convex set due to {prf:ref}`res-cvx-arbitrary-intersection`.
1. But then, $f$ is convex
   again due to {prf:ref}`res-cvxf-convexity-epigraph`.
```


```{prf:definition} Piecewise linear function
:label: def-cvxf-piecewise-linear-func

Let $\ba_1, \dots, \ba_n \in \VV$.
Let $b_1, \dots, b_n \in \RR$.

A function $f: \VV \to \RR$ given by:

$$
f(\bx) = \max \{\langle \bx, \ba_i \rangle + b_i  \}_{i \in 1, \dots, n}
$$
is called a *piecewise linear* or *piecewise affine* function.
```


```{prf:theorem}
:label: res-cvxf-piecewise-linear-convex

Piecewise linear functions are convex.
```

```{prf:proof}
Each of the functions $f_i (\bx) = \langle \bx, \ba_i \rangle + b_i$
is affine functionals. 
Thus, $f_i$ are convex ({prf:ref}`res-cvxf-affine-functional-convex`).
$f$ is a pointwise maximum of $n$ convex functions.
Hence, $f$ is convex ({prf:ref}`res-cvx-ptws-max-n`).
```

