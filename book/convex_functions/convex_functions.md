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
and $\theta \in [0, 1]$, we have:

$$
f(\theta \bx_1 + (1-\theta) \bx_2) \leq \theta f(\bx_1) + (1-\theta) f(\bx_2).
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

* For a convex function, every chord lies above 
  the graph of the function. 


```{prf:definition} Strictly convex function
:label: def-strictly-convex-function

A convex function $f: \VV \to \RR$ is *strictly convex* 
if for all $\bx_1,\bx_2 \in \dom f$, 
where $\bx_1$ and $\bx_2$ are distinct, 
and $\theta \in (0, 1)$, we have:

$$
f(\theta \bx_1 + (1-\theta) \bx_2) < \theta f(\bx_1) + (1-\theta) f(\bx_2).
$$
In other words, the inequality is a strict inequality 
whenever the point $\bx = \theta \bx_1 + (1-\theta) \bx_2$ is
distinct from $\bx_1$ and $\bx_2$ both.
```

```{prf:definition} Concave function
:label: def-concave-function

We say that a function $f$ is *concave* if $-f$ is convex.
A function $f$ is *strictly concave* if $-f$ is 
strictly convex.
```

```{prf:example} Linear functional
A *linear functional* on $\VV$ is defined in terms of 
a vector $\ba \in \VV$ as 

$$
f_a (\bx) \triangleq \langle \ba, \bx \rangle
$$
i.e. the inner product of $\ba$ with $\bx$.
```

```{prf:example} Affine functional
An *affine functional* on $\VV$ is defined in terms of 
a vector $\ba \in \VV$ and a scalar $b \in \RR$ as 

$$
f_{\ba, b} (\bx) \triangleq \langle \ba, \bx \rangle + b
$$
i.e. the inner product of $\ba$ with $\bx$ followed by a translation.
```


```{prf:remark}
All affine functionals and linear functionals are
convex as well as concave.
```


```{prf:property}
A function $f$ is convex if and only if for any
$\bx \in \dom f$ and any $\bv \in \VV$, the function 
$g(t) = f(\bx + t\bv)$ is convex (on its domain
    , $\{ t \in \RR \ST \bx + t\bv \in \dom f\}$).

In other words, $f$ is convex if and only if 
it is convex when restricted to any line that
intersects its domain.
```
