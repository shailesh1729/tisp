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



```{prf:example} Affine functional
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

```{prf:example} Absolute value
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
{prf:ref}`norm <def-la-norm>` on a vector space $\VV$.
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

```{prf:example} Max function
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

## Characterization of Convex Functions

### Convexity on lines in domain

```{prf:theorem} $f$ is convex = $f$ is convex on lines in domain
:label: res-cvxf-convx-on-lines

A function $f$ is convex if and only if for any
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

### Epigraph

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

A function $f$ is convex if and only if its epigraph
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

```{prf:definition} Proper convex function
:label: def-cvxf-proper-function

An extended real-valued convex function 
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
Putting another way, a proper convex function
is obtained by taking a finite convex function $f$
defined on a nonempty set $C \subseteq \VV$
and then extending it to all of $\VV$ by 
setting $f(\bx) = +\infty$ for all $\bx \notin C$.

It is easy to see that the codomain for a proper
convex function can be changed from $\ERL$
to $\RERL$ to clarify that it never takes
the value $-\infty$.


```{prf:definition} Improper convex function
:label: def-cvxf-improper-function

An extended real-valued convex function 
$f : \VV \to \ERL$ is called *improper*
if it is not proper.
```

Most of our study is focused on proper functions.
However, improper functions sometimes do arise
naturally. 


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

We continue further with 
real valued functions over $\RR^n$ 
which are twice differentiable.

```{prf:theorem} Second order characterization of convexity
:label: res-cvxf-hessian-convexity-relation

Let $f : \RR^n \to \RR$ be twice differentiable;
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

For real functions, the Hessian is simply the
second derivative $f''$.

```{prf:corollary} Convexity characterization for twice differentiable real functions
:label: res-cvxf-2nd-derivative-convexity-relation

Let $f : \RR \to \RR$ be twice differentiable;
i.e., second derivative $f''$ exists 
at every point in $\dom f$ which is open.

Then, $f$ is convex if and only if
$\dom f$ is an interval and its second derivative is non-negative
for every $x \in \dom f$:

$$
f''(x) \geq 0 \quad \Forall x \in \dom f.
$$ 
```



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

```{prf:example} Identity
:label: ex-cvxf-real-identity

Let $f : \RR \to \RR$ be:

$$
f(x) = x.
$$

We have $f'(x) = 1$ and $f''(x) = 0$.

$f$ is both convex and concave. 
```

```{prf:example} Exponential
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


```{prf:example} Logarithm
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


```{prf:example} Negative entropy
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

```{prf:example} Quadratic over linear form
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


```{prf:example} Log sum exponential
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
