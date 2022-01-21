(sec:la:real-euclidean-space)=
# The Real Euclidean Space

This section consolidates major results for 
the real Euclidean space $\RR^n$ as a ready reference. 
$\RR^2$ (the 2-dimensional plane) and 
$\RR^3$ the 3-dimensional space are the most familiar spaces to us.

$\RR^n$ is a generalization in $n$ dimensions.

````{prf:definition} $\RR^n$ and Euclidean space
:label: def-la-euclidean-space

For any positive integer $n$, the set of all $n$-tuples of
real numbers forms an $n$-dimensional vector space over $\RR$ 
which is denoted as $\RR^n$.
It is sometimes called *real coordinate space*.

An element $\bx$ in $\RR^n$ is written as 

$$
\bx  = (x_1, x_2, \ldots, x_n),
$$
where each $x_i$ is a real number.

Vector space operations on $\RR^n$ are defined by:

$$
&\bx + \by = (x_1 + y_1, x_2 + y_2, \dots, x_n + y_n), \Forall \bx, \by \in \RR^n.\\
& \alpha \bx = (\alpha x_1, \alpha x_2, \dots, \alpha x_n) \Forall \bx \in \RR^n, \alpha \in \RR.
$$

When equipped with the standard inner product and standard norm (defined below),
$\RR^n$ becomes the *Euclidean space*.
````

```{prf:definition} Standard basis
:label: def-la-euclidean-standard-basis

$\RR^n$ comes with the *standard* 
{prf:ref}`ordered basis <def-la-ordered-basis>` 
$\BBB = \{\be_1, \be_2, \dots, \be_n\}$:

$$
\begin{aligned}
& \be_1  = (1,0,\dots, 0),\\
& \be_2  = (0,1,\dots, 0),\\
&\vdots\\
& \be_n  = (0,0,\dots, 1)
\end{aligned}
$$
An arbitrary vector $\bx\in\RR^n$ can be written as

$$
\bx = \sum_{i=1}^{n}x_i \be_i.
$$
```

## Inner Products

```{prf:definition} Standard inner product/ dot product
:label: def-la-euclidean-dot-product

The standard
{prf:ref}`inner product <def-la-inner-product>`
(a.k.a. dot product) on $\RR^n$ is defined as:

$$
\langle \bx, \by \rangle = \sum_{i=1}^{n} x_i y_i 
= x_1 y_1 + x_2 y_2 + \dots + x_n y_n \quad \forall \bx, \by \in \RR^n.
$$
This makes $\RR^n$ an 
{prf:ref}`inner product space <def-la-pre-hilbert-space>`.
```

```{prf:remark}
The dot product is always a real number.
Hence we have symmetry:

$$
\langle x, y \rangle  = \langle y, x \rangle
$$

It is a {prf:ref}`real inner product <def-la-real-inner-product>`.
```

## Norms

We use norms as a measure of strength of a signal 
or size of an error. 
Different norms signify different aspects of the signal.

```{prf:definition} Euclidean norm
:label: def-la-euclidean-norm

The *length* of the vector (a.k.a. *Euclidean norm* 
or $\ell_2$ {prf:ref}`norm <def-la-norm>`) is defined as:

$$
\| \bx \| = \sqrt{\langle \bx, \bx \rangle} = \sqrt{\sum_{i=1}^{n} x_i^2} \quad \forall \bx \in \RR^n.
$$
This makes $\RR^n$  a
{prf:ref}`normed linear space <def-la-normed-linear-space>`.
```

### Angles

```{prf:definition} Angle
:label: def-la-euclidean-angle

The angle $\theta$ between two vectors is given by:

$$
\theta = \cos^{-1} \frac{ \langle \bx, \by \rangle }{\| \bx \| \| \by \|}.
$$




### $\ell_p$ Norms

In addition to standard Euclidean norm, we define a family of norms indexed by $p \in [1, \infty]$ known as
$\ell_p$ norms over $\RR^n$.


````{prf:definition} $\ell_p$ norm
:label: def-la-euclidean-lp_norm

$l_p$ norm is defined as:

$$
\| \bx \|_p = \begin{cases}
 \left ( \sum_{i=1}^{n} | x |_i^p  \right ) ^ {\frac{1}{p}} &  p \in [1, \infty)\\
\underset{1 \leq i \leq n}{\max} |x_i| &  p = \infty
\end{cases}
$$
````

### $\ell_2$ Norm

```{div}
As we can see from definition, $\ell_2$ norm is same as the Euclidean norm.

So we have:

$$
\| \bx \| = \| \bx \|_2.
$$
```



### $\ell_1$ Norm

From above definition, we have 

```{div}
$$
\|\bx\|_1 = \sum_{i=1}^n |x_i|= |x_1| + |x_2| + \dots  + | x_n|.
$$
```


### Quasi-norms

In some cases it is useful to extend the notion of $\ell_p$ norms to the case
where $0 < p < 1$. 

In such cases norm as defined in {prf:ref}`def-la-euclidean-lp_norm` 
doesn't satisfy triangle inequality. 
Hence it is not a proper norm function. 
We call such functions as *quasi-norms*.


### $\ell_0$ "norm"

Of specific mention is $\ell_0$ "norm". 
It isn't even a quasi-norm. 
Note the use of quotes around the word norm to distinguish $l_0$ "norm" 
from usual norms.

````{prf:definition} $\ell_0$ "norm"
:label: def-la-euclidean-l0_norm

$\ell_0$ "norm" is defined as:

$$
\| \bx \|_0 = | \supp(\bx) |
$$

where $\supp(\bx) = \{ i : x_i \neq 0\}$ denotes the support of $\bx$.
````

```{div}
Note that $\| \bx \|_0$ defined above doesn't follow the definition in {prf:ref}`def-la-euclidean-lp_norm`. 

Yet we can show that:

$$
\lim_{p\to 0} \| \bx \|_p^p = | \supp(\bx) |.
$$
which justifies the notation.
```


## Distances
```{prf:definition} Euclidean distance
:label: def-la-euclidean-distance

Distance between two vectors is defined as:

$$
d(\bx,\by) = \| \bx  - \by \| = \sqrt{\sum_{i=1}^{n} (\bx_i - \by_i)^2}.
$$

This distance function is known as *Euclidean metric*. 

This makes  $\RR^n$  a *metric space*.

