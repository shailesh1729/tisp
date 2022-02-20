(sec:la:real-euclidean-space)=
# The Euclidean Space

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



```{prf:definition} $\bQ$ inner product
:label: def-la-q-inner-product

Let $\bQ$ be an $n \times n$ real symmetric positive definite
matrix. The $\bQ$ inner product is defined as:

$$
\langle \bx, \by \rangle_Q \triangleq \bx^T \bQ \by.
$$
```

$\bQ$ inner product reduces to standard dot product
when $\bQ = \bI$.

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
```



### $\ell_p$ Norms

In addition to standard Euclidean norm, we define a family of norms indexed by $p \in [1, \infty]$ known as
$\ell_p$ norms over $\RR^n$.


````{prf:definition} $\ell_p$ norm
:label: def-la-euclidean-lp_norm

Let $p \in [1, \infty]$. For any $n \in \Nat$,
the $l_p$ norm denoted as $\| \cdot \|_p : \RR^n \to \RR$ 
mapping any vector $\bx \in \RR^n$ to a non-negative number
is defined as:

$$
\| \bx \|_p = \begin{cases}
\left ( \sum_{i=1}^{n} | x_i |^p  \right ) ^ {\frac{1}{p}} & \text{ if } & p \in [1, \infty)\\
\underset{1 \leq i \leq n}{\max} |x_i| & \text{ if } &  p = \infty
\end{cases}\, .
$$
````
```{div}
We mention the special cases. $p=1$ gives us:

$$
\|\bx\|_1 = \sum_{i=1}^n |x_i|= |x_1| + |x_2| + \dots  + | x_n|.
$$

$p=2$ gives us:

$$
\| \bx \|_2 = \left ( \sum_{i=1}^{n} | x_i |^2  \right ) ^ {\frac{1}{2}}
$$
which is same as the standard
{prf:ref}`Euclidean norm <def-la-euclidean-norm>`. 

$p=\infty$ gives us:

$$
\|\bx\|_{\infty} = \underset{1 \leq i \leq n}{\max} |x_i|.
$$


We need to justify that $\ell_p$ norm defined as above is indeed a norm.
Before that, we state the Hölder's inequality for the Euclidean space.
```

````{prf:theorem} Hölder's inequality

Let $\bu, \bv \in \RR^n$. 
Let $p \in [1, \infty]$ and let $q$ be its 
{prf:ref}`conjugate exponent <def-bra-conjugate-exponent>`.

We have:

```{math}
:label: eq-la-finite-holder-inequality
\| \bu \bv \|_1 \leq \| \bu \|_p \| \bv \|_q
```

where $\bu \bv$ denotes the element-wise multiplication given by:

$$
\bu \bv = (u_1 v_1, \dots, u_n v_n).
$$
````

```{prf:proof}
If $\bu = \bzero$ or $\bv = \bzero$, then {eq}`eq-la-finite-holder-inequality`
follows immediately. 

Now, consider the case where $\bu \neq \bzero$ and $\bv \neq \bzero$.

If $p=1$, then $q = \infty$. We have:

$$
\| \bu \bv \|_1 = \sum_{i=1}^n |u_i v_i| 
\leq \underset{1 \leq j \leq n}{\max} |v_j| \sum_{i=1}^n |u_i | 
= \| \bu \|_1 \| \bv \|_{\infty}.
$$
The same argument applies for the case of $p=\infty$ and $q=1$ too.
For the case of $p,q \in (1,\infty)$, we have:

$$
\| \bu \|_p = \left (\sum_{k=1}^{n} | u_k |^p  \right ) ^ {\frac{1}{p}}
\text {and }
\| \bv \|_q = \left (\sum_{k=1}^{n} | v_k |^q  \right ) ^ {\frac{1}{q}}.
$$

We recall the
{prf:ref}`Hölder's inequality <res-bra-holder-inequality>` for real numbers.
For any $n \in \Nat$, 
$a_1, \dots, a_n \geq 0$, 
$b_1, \dots, b_n \geq 0$, $p, q$ being
conjugate exponents, we have:

$$
\sum_{k=1}^n a_k b_k \leq \left ( \sum_{k=1}^n a_k^p \right )^{\frac{1}{p}}
\left ( \sum_{k=1}^n b_k^q \right )^{\frac{1}{q}}.
$$

Let $a_k = |u_k|$ and $b_k = |v_k|$. Then

$$
\| \bu \bv \|_1 = \sum_{k=1}^n |u_k v_k| 
\leq \sum_{k=1}^n |u_k | |v_k| 
\leq \left ( \sum_{k=1}^n |u_k |^p \right )^{\frac{1}{p}}
\left ( \sum_{k=1}^n |v_k|^q \right )^{\frac{1}{q}}
= \| \bu \|_p \| \bv \|_q.
$$
```

We are now ready to prove that $\ell_p$ norm is indeed a norm.

```{prf:theorem}
For any $n \in \Nat$ and any $p \in [1, \infty]$, the function
$\| \cdot \|_p$ as defined in {prf:ref}`def-la-euclidean-lp_norm`
is a {prf:ref}`norm <def-la-norm>`.
```

```{prf:proof}
[Positive definiteness]
By definition, if $\bu \neq \bzero$, then $\| \bu \|_p > 0$.
Similarly, $\| \bu \|_p = 0$ implies $\bu = \bzero$.

[Positive homogeneity]
Let $\alpha \in \RR$. If $p < \infty$, then

$$
\| \alpha \bu \|_p = \left (\sum_{k=1}^{n} | \alpha u_k |^p  \right ) ^ {\frac{1}{p}}
= | \alpha | \left (\sum_{k=1}^{n} | u_k |^p  \right ) ^ {\frac{1}{p}}
= | \alpha | \| \bu \|_p.
$$

For $p=\infty$, 

$$
\| \alpha \bu \|_{\infty} = \underset{1 \leq i \leq n}{\max} |\alpha u_i|
= | \alpha | \underset{1 \leq i \leq n}{\max} |u_i|
= |\alpha | \| \bu \|_{\infty}.
$$


[Triangle inequality]
Let $\bu, \bv \in \RR^n$. If $p=1$, then

$$
\| \bu + \bv \|_1 = \sum_{i=1}^n | u_i + v_i |
\leq \sum_{i=1}^n | u_i | + |v_i | = \| \bu \|_1 + \| \bv \|_1.
$$

If $p=\infty$, then:

$$
\| \bu + \bv \|_{\infty} = \underset{1 \leq i \leq n}{\max} | u_i + v_i|
\leq \underset{1 \leq i \leq n}{\max} (| u_i| + |v_i|)
\leq \underset{1 \leq i \leq n}{\max} |u_i| + \underset{1 \leq i \leq n}{\max} |v_i|
= \| \bu \|_{\infty} + \| \bv \|_{\infty}.
$$

We are left with the case $p \in (1, \infty)$.


$$
\begin{aligned}
\| \bu + \bv \|_p^p  &= \sum_{i=1}^n |u_i + v_i |^p \\
&=  \sum_{i=1}^n |u_i + v_i | |u_i + v_i |^{p-1}\\
&\leq \sum_{i=1}^n |u_i | |u_i + v_i |^{p-1} 
+ \sum_{i=1}^n |v_i | |u_i + v_i |^{p-1}.
\end{aligned}
$$

By Hölder's inequality:

$$
\begin{aligned}
\sum_{i=1}^n |u_i | |u_i + v_i |^{p-1} &\leq 
\left (\sum_{i=1}^n |u_i |^p \right )^{\frac{1}{p}}
\left (\sum_{i=1}^n |u_i + v_i|^{(p-1)q} \right )^{\frac{1}{q}}\\
&= \| \bu \|_p \left (\sum_{i=1}^n |u_i + v_i|^p \right )^{\frac{1}{q}}\\
&= \| \bu \|_p \| \bu + \bv \|_p^{\frac{p}{q}}.
\end{aligned}
$$

Note that $(p-1)q = p$ since $p,q$ are conjugate exponents.

Similarly:

$$
\sum_{i=1}^n |v_i | |u_i + v_i |^{p-1} \leq
\| \bv \|_p \| \bu + \bv \|_p^{\frac{p}{q}}. 
$$

Combining, we get:

$$
\| \bu + \bv \|_p^p  \leq (\| \bu \|_p + \| \bv \|_p)  \| \bu + \bv \|_p^{\frac{p}{q}}.
$$

Note that:

$$
p - \frac{p}{q} = p \left (1 - \frac{1}{q} \right ) = p \frac{1}{p} = 1.
$$

Thus, dividing both sides by $\| \bu + \bv \|_p^{\frac{p}{q}}$, we get:

$$
\| \bu + \bv \|_p \leq \| \bu \|_p + \| \bv \|_p
$$
as desired.
```

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


```{prf:definition} $\bQ$ norm
The $\bQ$ norm induced by $\bQ$ inner product is given by

$$
\| \bx \|_Q = \sqrt{\bx^T \bQ \bx}.
$$
```

### Equivalence of norms

```{prf:theorem}
:label: res-la-euclidean-l1-l2-eq 

The $\ell_1$ and $\ell_2$ norms on $\RR^n$ are
{prf:ref}`equivalent <def-la-ns-equivalent-norms>`.
In particular, for any $\bx \in \RR^n$

$$
\frac{1}{\sqrt{n}} \| \bx \|_1 \leq \| \bx \|_2 \leq \| \bx \|_1. 
$$

Alternatively,

$$
\| \bx \|_2 \leq \| \bx \|_1 \leq \sqrt{n} \| \bx \|_2. 
$$
```

```{prf:proof}

By Cauchy-Schwarz inequality

$$
\| \bx \|_1 = \sum_{i=1}^n | x_i | 
= \sum_{i=1}^n | x_i | . 1 
\leq \| \bx \|_2 \| \bone \|_2 = \sqrt{n} \| \bx \|_2
$$
where $\bone$ is the vector of all ones.
Thus,

$$
\frac{1}{\sqrt{n}} \| \bx \|_1 \leq \| \bx_2 \|.
$$

Also,

$$
\| \bx \|_2^2 = \sum_{i=1}^n | x_i|^2 
\leq \left (\sum_{i=1}^n |x_i| \right )^2
= \| \bx \|_1^2.
$$

Thus,

$$
\| \bx \|_2 \leq \| \bx \|_1.
$$

Thus, the two norms are equivalent.
```



```{prf:theorem}
:label: res-la-euclidean-l2-linf-eq 

The $\ell_2$ and $\ell_{\infty}$ norms on $\RR^n$ are
{prf:ref}`equivalent <def-la-ns-equivalent-norms>`.
In particular, for any $\bx \in \RR^n$

$$
\frac{1}{\sqrt{n}} \| \bx \|_2 \leq \| \bx \|_{\infty} \leq \| \bx \|_2. 
$$

Alternatively,

$$
\| \bx \|_{\infty} \leq \| \bx \|_2 \leq \sqrt{n} \| \bx \|_{\infty}. 
$$
```

```{prf:proof}
Let $\| \bx \|_{\infty} = \sup \{ |x_i|\}$.

1. Then, $|x_i| \leq \| \bx \|_{\infty}$.
1. Thus, $|x_i|^2 \leq \| \bx \|_{\infty}^2$.
1. Taking the sum $\| \bx \|_2^2 \leq  n \| \bx \|_{\infty}^2$.
1. Taking the square root $\| \bx \|_2 \leq \sqrt{n}\| \bx \|_{\infty}$.

For the other side, we note that 

$$
\| \bx \|_{\infty}^2 = \left (\sup \{ |x_i|\} \right )^2
\leq \sum_{i=1}^n |x_i|^2 = \| \bx \|_2^2.
$$

Thus, $\| \bx \|_{\infty} \leq \| \bx \|_2$.
Thus, the two norms are equivalent.
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

