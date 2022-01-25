# Convex Functions

Throughout this section, we assume that $\VV, \WW$ are 
real vector spaces. Wherever necessary, 
they are equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \|$
or an {prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle$. 
They are also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$
as needed.



```{prf:definition} Convex function
:label: def-convex-function

A real valued function $f: \VV \to \RR$ is *convex* if 
$\dom f$ is a convex set and for all $\bx_1,\bx_2 \in \dom f$, 
and $t \in [0, 1]$, we have:

$$
f(t \bx_1 + (1-t) \bx_2) \leq t f(\bx_1) + (1-t) f(\bx_2).
$$
```



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
