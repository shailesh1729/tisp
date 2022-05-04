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
:label: res-la-euclidean-holder-inequality

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

```{prf:theorem} $\ell_p$ norms are norms
:label: res-la-euclid-lp-norm-just

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

### Equivalence of Norms

$\RR^n$ is a finite dimensional vector space
and all norms on $\RR^n$ are equivalent. 
However, reaching this conclusion requires
some hoofs to go through. Here is the roadmap.

```{div}
1. We first establish that $\ell_1$ and $\ell_2$ norms are equivalent.
1. We then establish that $\ell_2$ and $\ell_{\infty}$ norms are equivalent.
1. We recall the Heine-Borel theorem for Euclidean metric and show that
   closed and bounded sets of $(\RR^n, \| \cdot \|_2)$ are compact.
1. We then take advantage of the fact that equivalent norms
   lead to same topologies (open, closed and compact sets) as well
   as bounded sets and show that closed and bounded sets
   of $(\RR^n, \| \cdot \|_1)$ are also compact.
1. We are then in a position to demonstrate that all norms on $\RR^n$
   are indeed equivalent.
```


```{prf:theorem} Equivalence of $\ell_1$ and $\ell_2$ norms
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



```{prf:theorem} Equivalence of $\ell_2$ and $\ell_{\infty}$ norms
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


```{prf:theorem} Equivalence of $\ell_1$, $\ell_2$, and $\ell_{|infty}$ norms
:label: res-la-euclidean-l1-l2-linf-eq 

The $\ell_1$, $\ell_2$ and $\ell_{\infty}$ norms on $\RR^n$ are
equivalent.
```

```{prf:proof}
We proceed as follows:

1. By {prf:ref}`res-la-euclidean-l1-l2-eq`, $\ell_1$ and $\ell_2$ 
   norms are equivalent.
1. By {prf:ref}`res-la-euclidean-l2-linf-eq`, $\ell_2$ and $\ell_{\infty}$
   norms are equivalent.
1. By {prf:ref}`res-la-ns-norm-equivalence-rel`, equivalence
   of norms is an equivalence relation.
1. Hence, by transitivity, $\ell_1$ and $\ell_{\infty}$
   norms are equivalent.
```

```{prf:theorem} Heine Borel theorem
:label: res-la-euclidean-l2-norm-closed-bounded-compact

A subset of the normed linear space
$(\RR^n, \| \cdot \|_2)$ is compact
if and only if it is a closed and bounded set.
```

```{prf:proof} 
The distance metric induced by  $\| \cdot \|_2$
is the Euclidean distance.

This result is follows directly from 
{prf:ref}`res-ms-heine-borel-euclidean`.
```


```{prf:theorem} Closed and bounded sets under $\ell_1$ norm
:label: res-la-euclidean-l1-norm-closed-bounded-compact

A subset of the normed linear space
$(\RR^n, \| \cdot \|_1)$ is compact
if and only if it is a closed and bounded set.
```

```{prf:proof}
We just need to show that if a set is closed
and bounded in $(\RR^n, \| \cdot \|_1)$, 
then it is compact in $(\RR^n, \| \cdot \|_1)$.

1. The norms $\| \cdot \|_1$ and $\| \cdot \|_2$ are equivalent
   ({prf:ref}`res-la-euclidean-l1-l2-linf-eq`).
1. Hence, the metrics induced by them are (strongly) equivalent
   ({prf:ref}`res-la-ns-norm-eq-metric-eq`).
1. Thus, the open sets and closed sets in
    $(\RR^n, \| \cdot \|_1)$
   and $(\RR^n, \| \cdot \|_2)$ are identical.
1. Hence, the compact sets in $(\RR^n, \| \cdot \|_1)$
   and $(\RR^n, \| \cdot \|_2)$ are identical
   ({prf:ref}`res-ms-eq-metric-compactness`).
1. Also the bounded sets in  $(\RR^n, \| \cdot \|_1)$
   and $(\RR^n, \| \cdot \|_2)$ are identical
   due to {prf:ref}`res-la-ns-norm-eq-same-bounded`.
1. Now, let $A$ be a closed and bounded set in $(\RR^n, \| \cdot \|_1)$.
1. Then, $A$ is closed and bounded in $(\RR^n, \| \cdot \|_2)$.
1. But then by {prf:ref}`Heine Borel theorem <res-la-euclidean-l2-norm-closed-bounded-compact>`,
   $A$ is compact in $(\RR^n, \| \cdot \|_2)$.
1. But then, $A$ is compact in $(\RR^n, \| \cdot \|_1)$ also.
```


```{prf:theorem} Equivalence of norms on the Euclidean space
:label: res-la-ns-norms-euclidean-eq

Let $n \in \Nat$. 
All norms on $\RR^n$ are equivalent.
```

```{prf:proof}
The $\ell_1$ norm $\| \cdot \|_1 : \RR^n \to \RR$ is given by:

$$
\| \bx \|_1 = \sum_{i=1}^n | x_i |.
$$

We shall show that any norm $\| \cdot \| : \RR^n \to \RR$
is equivalent to $\| \cdot \|_1 : \RR^n \to \RR$.
Then, since norm equivalence is an equivalence relation
({prf:ref}`res-la-ns-norm-eq-metric-eq`), hence
all norms are equivalent. 

In particular, if $\| \cdot \|_a$ and $\| \cdot \|_b$
are two different norms on $\RR^n$, then
$\| \cdot \|_a \sim \| \cdot \|_1$ and $\| \cdot \|_b \sim \| \cdot \|_1$
implies that $\| \cdot \|_a \sim \| \cdot \|_b$ due to
{prf:ref}`res-la-ns-norm-eq-metric-eq`.

Towards this end, let's show that 
any norm $\| \cdot \|$ is indeed equivalent to  $\| \cdot \|_1$.

We first show that there exists a constant $c_1 > 0$ such that

$$
\| \bx \| \leq c_1 \| \bx \|_1 \Forall \bx \in \RR^n.
$$

1. Let $\{ \be_i \}$ be the standard basis for $\RR^n$.
1. Let $c = \max \{ \| \be_i \|, i=1,\dots, n\}$.
1. Then, for any $\bx \in \RR^n$, we have

   $$
   \| \bx \| &= \left \| \sum_{i=1}^n x_i \be_i \right \|\\
   &\leq \sum_{i=1}^n \| x_i \be_i \| \\
   &= \sum_{i=1}^n | x_i| \| \be_i \| \\
   &\leq \sum_{i=1}^n | x_i| c \\
   &= c \| \bx \|_1.
   $$


We now show that there exists a constant $c_2 > 0$ such that

$$
\| \bx \|_1 \leq c_2 \| \bx \| \Forall \bx \in \RR^n.
$$

1. Define a function $g : (\RR^n, \| \cdot \|_1) \to \RR$ as

   $$
   g(\bx) = \| \bx \| \Forall \bx \in \RR^n.
   $$
1. Then, for any $\bx, \by \in \RR^n$,

   $$
   | g(\bx) - g(\by)| = | \| \bx \| - \| \by \| | \leq \| \bx - \by \|
   \leq c \| \bx - \by \|_1. 
   $$
1. Thus, $g$ is Lipschitz continuous on the 
   normed linear space $(\RR^n, \| \cdot \|_1)$.
1. Therefore, $g$ is continuous.
1. Now, let $S = \{\by \in \RR^n \ST \| \by \|_1  = 1 \}$.
1. $S$ is a closed set in $(\RR^n, \| \cdot \|_1)$ since it is the
   boundary of the unit ball.
1. $S$ is also bounded since $\| \by \|_1 \leq 1$ for every $\by \in S$.
1. Then, by {prf:ref}`res-la-euclidean-l1-norm-closed-bounded-compact`
   $S$ is compact in $(\RR^n, \| \cdot \|_1)$.
1. Hence, due to {prf:ref}`res-ms-compact-real-valued-min-max-attain`
   $g$ attains a minimum value at some $\by \in S$
   over the compact set $S$.
1. Let the minimum value of $g$ over $S$ be say $m$ at some $\by_0 \in S$.
1. Note that $\bzero \notin S$ by definition since $\| \bzero \| \neq 1$.
1. Thus,
   
   $$
   m = g(\by_0) = \| \by_0 \| > 0.
   $$
1. Thus, for all $\by \in S$, we have $\| \by \| \geq m > 0$.
1. Now, for any nonzero $\bx \in \RR^n$, the $\ell_1$ normalized vector,
   $\by = \frac{\bx }{\| \bx \|_1} \in S$.
1. But then

   $$
   & \| \by \| \geq m\\ 
   &\implies \left \| \frac{\bx }{\| \bx \|_1}  \right \| \geq m\\
   &\implies \| \bx \| \geq m \| \bx \|_1 \\
   &\implies \| \bx \|_1 \leq \frac{1}{m} \| \bx \|
   $$
   holds for every nonzero $\bx \in \RR^n$.
1. Also, the inequality $\| \bx \|_1 \leq \frac{1}{m} \| \bx \|$
   is satisfied trivially by $\bzero$.


We have shown that for $c_1 = c > 0$ and $c_2 = \frac{1}{m} > 0$   

$$
\| \bv \| \leq c_1 \| \bv \|_1
\text{ and } 
\| \bv \|_1 \leq c_2 \| \bv \|
$$
holds true for every $\bv \in \RR^n$.

Thus, the two norms
$\| \cdot \|$ and  $\| \cdot \|_1$ 
are indeed equivalent.
```


## Distances
```{prf:definition} Euclidean distance
:label: def-la-euclidean-distance

Distance between two vectors is defined as:

$$
d(\bx,\by) = \| \bx  - \by \| = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}.
$$

This distance function is known as *Euclidean metric*. 

This makes  $\RR^n$  a *metric space*.
```


## General Euclidean Space

We can generalize the definition of a Euclidean space
to a more abstract case.

```{prf:definition} General Euclidean space
:label: def-la-gen-euclidean-space

A finite dimensional real vector space $\VV$
equipped with an inner product $\langle \cdot, \cdot \rangle$
is called a *Euclidean space* if it is endowed
with the norm $\| \cdot \| : \VV \to \RR$ given by

$$
\| \bx \| = \sqrt{ \langle \bx, \bx \rangle}.
$$
The norm induced by the inner product is known as
the *Euclidean norm*.
```


```{div}
There are several properties emerging from this definition.

1. Let $\VV$ be a Euclidean space.
1. The field of scalars is $\RR$.
1. Assume that $n = \dim \VV$.
1. The inner product is a real inner product.
1. $\VV$ is isomorphic to $\RR^n$.
1. If we choose a basis $\BBB = \{ \be_1, \dots, \be_n \}$
   for $\VV$, then the coordinates for each
   vector $\bv \in \VV$ form an element of $\RR^n$.
1. This forms a direct bijective mapping between $\VV$ and $\RR^n$.
1. $\| \bx \|^2 = \langle \bx, \bx \rangle$.
1. The Euclidean norm makes it a normed linear space.
1. Recall from {prf:ref}`res-la-ndim-complete` that
  a finite dimensional normed linear space is complete.
1. Thus, $\VV$ is a {prf:ref}`Banach space <def-la-banach-space>`.
1. $\VV$ is an inner product space which is complete.
1. Hence $\VV$ is also a {prf:ref}`Hilbert space <def-la-ip-hilbert-space>`.
1. $\RR^n$ provides additional features like $\ell_p$ norms.
   Corresponding norms can be induced on $\VV$ by a coordinate mapping.
```
