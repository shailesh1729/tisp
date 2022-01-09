# Introduction


```{prf:definition} Distance function/Metric
:label: def-ms-distance-function

Let $X$ be a nonempty set. 
A {prf:ref}`function <def-st-total-function>` $d : X \times X \to \RR$ 
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


```{prf:example} $\RR^n$ Euclidean space
The $d_2$ metric over $\RR^n$:

$$
d_2 (x, y) \triangleq \left ( \sum_{i=1}^n |x_i - y_i|^2 \right )^{\frac{1}{2}}
$$
is known as the *Euclidean distance* and 
the metric space $(\RR^n, d_2)$ is known as the 
*n-dimensional Euclidean (metric) space*.

The standard metric for $\RR^n$ is the Euclidean metric.
```

```{prf:proposition} Triangle inequality alternate form
Let $(X, d)$ be a metric space. Let $x,y,z \in X$.

$$
|d (x, z)  - d(y, z)| \leq d(x,y).
$$
```

```{prf:proof}
From triangle inequality:

$$
d (x, z) \leq d(x, y) + d (y, z) \implies d (x, z) - d(y, z) \leq d (x, y).
$$

Interchanging $x$ and $y$ gives:

$$
d (y, z) - d (x, z) \leq d (y, x) = d (x, y).
$$

Combining the two, we get:

$$
|d (x, z)  - d(y, z)| \leq d(x,y).
$$
```

```{prf:example}
Let $X$ be a nonempty set:

Define:

$$
d(x,y) = \begin{cases}
0 & x = y \\
1 & x \neq y
\end{cases}.
$$

$(X, d)$ is a metric space. This distance is called *discrete distance* 
and the metric space is called a *discrete metric space*.
```

```{prf:definition} Metric subspace
Let $(X, d)$ be a metric space. Let $Y \subset X$ be a nonempty
subset of $X$. Then, $Y$ can be viewed as a metric space
in its own right with the distance function $d$ restricted
to $Y \times Y$, denoted as $d|_{Y \times Y}$. We then say
that $(Y, d|_{Y \times Y})$ or simply $Y$ is a 
*metric subspace* of $X$.
```

```{prf:example}
$[0,1]$ is a metric subspace of $\RR$ with the standard
metric $d(x, y) = |x -y|$ restricted to $[0,1]$. 
In other words, the distance between any two points
$x, y \in [0, 1]$ is calculated by viewing $x,y$ as 
points in $\RR$ and using the standard metric for $\RR$.
```


```{prf:example} $\ERL$ A metric space for the extended real line

Consider the mapping $\varphi : \ERL \to [-1, 1]$ given by:

$$
\varphi(x) = \begin{cases}
\frac{t}{1 + |t|} & x \in \RR \\
-1 & x = -\infty \\
1 & x = \infty
\end{cases}.
$$

$\varphi$ is a bijection from $\ERL$ onto $[-1, 1]$. 

$[-1, 1]$ is a metric space with the standard metric
for the real line $d_{\RR}(x, y) = |x - y|$ restricted to $[-1, 1]$.


Consider a function $d: \ERL \times \ERL \to \RR$ defined as

$$
d (s, t) = | \varphi(s) - \varphi(t)|.
$$

The function $d$ satisfies all the requirements of a metric. 
It is the standard metric on $\ERL$.
``` 

```{prf:example} $\ell^p$ Real sequences
For any $1 \leq p < \infty$, we define:

$$
\ell^p = \left \{ \{ a_n \} \in \RR^{\Nat} \ST \sum_{i=1}^{\infty} |a_i|^p  \right \}
$$
as the set of real sequences $\{ a_n \}$ such that the series 
$\sum a_n^p$ is absolutely summable.

It can be shown that the set $\ell^p$ is closed under sequence 
addition.

Define a map $d_p : \ell^p \times \ell^p \to \RR$ as 

$$
d_p (\{a_n \}, \{ b_n \}) = \sum_{i=1}^{\infty} |a_i - b_i|^p.
$$

$d_p$ is a valid distance function over $\ell^p$. We metrize $\ell^p$
with $d_p$ as the standard metric. 
```

```{prf:example} Finite products of metric spaces

Let $(X_1, d_1), (X_2, d_2), \dots, (X_n, d_n)$ be $n$ metric spaces.

Let $X = X_1 \times X_2 \times \dots \times X_n$. 
Define a map $\rho : X \times X \to \RR$ as:

$$
\rho ((a_1, a_2, \dots, a_n), (b_1, b_2, \dots, b_n)) 
= \sum_{i=1}^n d_i (a_i, b_i).
$$  

$\rho$ is a distance function on $X$. The metric space
$(X, \rho)$ is called the *product* of metric spaces $(X_i, d_i)$.
```


