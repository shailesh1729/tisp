# Convex Functions

```{prf:definition} Convex function
:label: def-convex-function

A function $f: \RR^n \to \RR$ is *convex* if 
$\dom f$ is a convex set and for all $x_1,x_2 \in \dom f$, 
and $\theta \in [0, 1]$, we have:

$$
f(\theta x_1 + (1-\theta) x_2) \leq \theta f(x_1) + (1-\theta) f(x_2).
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

A convex function $f: \RR^n \to \RR$ is *strictly convex* 
if for all $x_1,x_2 \in \dom f$, 
where $x_1$ and $x_2$ are distinct, 
and $\theta \in (0, 1)$, we have:

$$
f(\theta x_1 + (1-\theta) x_2) < \theta f(x_1) + (1-\theta) f(x_2).
$$
In other words, the inequality is a strict inequality 
whenever the point $x = \theta x_1 + (1-\theta) x_2$ is
distinct from $x_1$ and $x_2$ both.
```

```{prf:definition} Concave function
:label: def-concave-function

We say that a function $f$ is *concave* if $-f$ is convex.
A function $f$ is *strictly concave* if $-f$ is 
strictly convex.
```

```{prf:example} Linear functional
A *linear functional* on $\RR^n$ is defined in terms of 
a vector $a \in \RR^n$ as 

$$
f_a (x) \triangleq \langle a, x \rangle
$$
i.e. the inner product of $a$ with $x$.
```

```{prf:example} Affine functional
An *affine functional* on $\RR^n$ is defined in terms of 
a vector $a \in \RR^n$ and a scalar $b \in \RR$ as 

$$
f_{a, b} (x) \triangleq \langle a, x \rangle + b
$$
i.e. the inner product of $a$ with $x$ followed by a translation.
```


```{prf:remark}
All affine functionals and linear functionals are
convex as well as concave.
```


```{prf:property}
A function $f$ is convex if and only if for all
$x \in \dom f$ and all $v$, the function 
$g(t) = f(x + tv)$ is convex (on its domain
    , $\{ t : x + tv \in \dom f\}$).

In other words, $f$ is convex if and only if 
it is convex when restricted to any line that
intersects its domain.
```
