# Introduction


```{prf:definition} Distance function/Metric
:label: def-ms-distance-function

Let $X$ be a nonempty set. A function $d : X \times X \to \RR$ 
is called a *distance function* or a *metric* if it satisfies the 
following properties for any elements $x,y,z \in X$:

1. Non-negativity: $d(x, y) \geq 0$
1. Identity of indiscernibles: $d(x, y) = 0 \iff x = y$
1. Symmetry: $d(x, y) = d(y, x)$
1. Triangle inequality: $d(x,y) \leq d(x, z) + d(z, y)$
```

```{prf:definition} Metric space
:label: def-ms-metric-space

Let $d$ be a distance function on a set $X$. Then 
we say that $(X, d)$ is a *metric space*. The 
elements of $X$ are called points.
```

* Distance functions are real valued.
* Distance functions map an ordered pair of points in $X$ to
  a real number.
* Distance between two points in the set $X$ can only be 
  non-negative. 
* Distance of a point with itself is 0. 
  In other words, if the distance between two points is 0,
  then the points are identical. i.e. the distance function
  works as a discriminator between the points of the set $X$.
* Symmetry means that the distance from
  a point $x$ to another point $y$ is same as the distance
  from $y$ to $x$.
* Triangle inequality says that the direct distance between two 
  points can never be longer than the distance covered through
  an intermediate point. 
* In general, a set $X$ can be associated with different metrics
  (distance functions) say $d_1$ and $d_2$. In that case, the 
  corresponding metric spaces $(X, d_1)$ and $(X, d_2)$ are different.
* When a set $X$ is equipped with a metric $d$ to create a metric
  space $(X, d)$, we say that $X$ has been *metrized*.  
* If the metric $d$ associated with a set $X$ is obvious from the
  context, we will denote the corresponding metric space $(X,d)$
  by simply $X$. E.g., $|x-y|$ is the standard distance function 
  on the set $\RR$. 
* When we say that let $Y$ be a subset of a metric space $(X,d)$, 
  we mean that $Y \subset X$.  
* Similarly, a point in a metric space $(X,d)$ means the point 
  in the underlying set $X$.


```{note}
Some authors prefer the notation $d : X \times X \to \RR_+$. 
With this notation, the non-negativity property is embedded
in the type signature of the function (i.e. the codomain specification)
and doesn't need to be stated explicitly. 
```


```{prf:example} $\RR^n$ p-distance
For some $1 \leq p \lt \infty$, the function $d_p : \RR^n \times \RR^n \to \RR$:

$$
d_p (x, y) \triangleq \left ( \sum_{i=1}^n |x_i - y_i|^p \right )^{\frac{1}{p}}
$$

is a metric and $(\RR^n, d_p)$ is a metric space.
```


```{prf:remark} $\RR^n$ Euclidean space
The $d_2$ metric over $\RR^n$:

$$
d_2 (x, y) \triangleq \left ( \sum_{i=1}^n |x_i - y_i|^2 \right )^{\frac{1}{2}}
$$
is known as the *Euclidean distance* and 
the metric space $(\RR^n, d_2)$ is known as the 
*n-dimensional Euclidean (metric) space*.

The standard metric for $\RR^n$ is the Euclidean metric.
```