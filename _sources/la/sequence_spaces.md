(sec:la:sequence-spaces)=
# Sequence Spaces

We shall assume the field of scalars $\FF$ to be either $\RR$ or $\CC$.

## The Space of all Sequences

Recall that a {prf:ref}`sequence <def-st-sequence>` is
a map $\bx : \Nat \to \FF$ and is written as $\{ x_n \}$.
The set of all sequences of $\FF$ is denoted by $\FF^{\Nat}$
or just $\FF^{\infty}$ in Cartesian product notation.

```{prf:definition} Zero sequence
:label: def-la-ss-zero-sequence

The zero sequence is defined as:

$$
\bzero = (0, 0, 0, \dots).
$$
```

```{prf:definition} Vector addition of sequences
:label: def-la-ss-sequence-addition

Let $\bx = \{ x_n \}$ and $\by = \{ y_n \}$ be any two
sequences in $\FF^{\infty}$.

Their vector addition is defined as:

$$
\bx + \by \triangleq \{ x_n + y_n \}.
$$
```

```{prf:definition} Scalar multiplication of sequence
:label: def-la-ss-sequence-scaling

Let $\bx = \{ x_n \}$ be any
sequence in $\FF^{\infty}$
and let $\alpha \in \FF$.

The scalar multiplication of $\alpha$ with $\bx$ is defined as:

$$
\alpha \bx \triangleq \{ \alpha x_n\}.
$$
```

```{prf:theorem}
:label: res-la-ss-closure-vec-add-scal-mult

The set of sequences $\FF^{\infty}$ is closed under
vector addition and scalar multiplication defined above.
```
This is obvious from definition.


```{prf:definition} Vector space of all sequences
:label: def-la-space-sequences

The set $\FF^{\infty}$ equipped with the 
vector addition and scalar multiplication 
defined above is a vector space. 
It is known as the *space of all sequences*.
```

```{prf:definition} Sequence space
:label: def-la-sequence-space

Any linear subspace of the space of all sequences $\FF^{\infty}$
is known as a *sequence space*.
```

## The Space of Absolutely Summable Sequences

```{prf:definition} Absolutely summable sequence
:label: def-la-abs-summable-seq

A sequence $\{x_n\}$ of $\FF$ is called absolute summable if

$$
\sum_{n=1}^{\infty} |x_n| < \infty.
$$
```


```{prf:theorem} Closure under addition
:label: res-la-ss-sequence-addition-closure

If sequences $\{x_n \}$ and $\{ y_n\}$ are absolutely summable, 
then their sum $\{ x_n + y_n \}$ is absolutely summable with

$$
\sum_{n=1}^{\infty} |x_n + y_n| \leq \sum_{n=1}^{\infty} |x_n|  + \sum_{n=1}^{\infty} |y_n|. 
$$
```

```{prf:proof}
Consider the partial sum:

$$
S_n = \sum_{k=1}^{n} |x_k + y_k|
\leq \sum_{k=1}^{n} (|x_k| + |y_k|)
= \sum_{k=1}^{n} |x_k| + \sum_{k=1}^{n} |y_k|.
$$

Taking the limit

$$
\lim_{n \to \infty} S_n  \leq \lim_{n \to \infty}\sum_{k=1}^{n} |x_k| + 
\lim_{n \to \infty} \sum_{k=1}^{n} |y_k|
= \sum_{n=1}^{\infty} |x_n|  + \sum_{n=1}^{\infty} |y_n|.
$$
Thus, the sequence $\{x_n + y_n\}$ is absolutely summable.
```

```{prf:theorem} Closure under scalar multiplication
:label: res-la-ss-sequence-scaling-closure

If the sequence $\{x_n \}$ is absolutely summable,
then for any $\alpha \in \FF$, the sequence  $\{ \alpha x_n \}$ is 
absolutely summable with:

$$
\sum_{n=1}^{\infty} | \alpha x_n| =  | \alpha| \sum_{n=1}^{\infty} |  x_n|.
$$
```

```{prf:proof}
Consider the partial sum:

$$
S_m = \sum_{n=1}^{m}| \alpha x_n| = \sum_{n=1}^{m} | \alpha | |  x_n| 
= | \alpha | \sum_{n=1}^{m} |  x_n|.
$$

Taking the limit:

$$
\lim_{m \to \infty} S_m =  | \alpha | \lim_{m \to \infty} \sum_{n=1}^{m} |  x_n|
= | \alpha | \sum_{n=1}^{\infty} |  x_n|.
$$
Hence $\{ \alpha x_n \}$  is absolutely summable.
```

```{prf:definition} $\ell^1$ The space of absolutely summable sequences
:label: def-la-ss-abs-sum-seq-space


Let $\ell^1$ denote the set of all absolutely summable sequences of $\FF$.
Then $\ell^1$ equipped with the vector addition and scalar multiplication
defined above is a vector space. 
```
The definition is justified since:

* $\ell^1$ is closed under vector addition.
* $\ell^1$ is closed under scalar multiplication.
* The zero-sequence $(0, 0, 0, \dots)$ is absolutely summable and belongs to $\ell^1$.



```{prf:definition} Norm for the $\ell^1$ space
:label: def-la-ss-l1-norm

The standard norm for the $\ell^1$ space is defined 
for any $\bx \in \ell^1$ as:

$$
\| \bx \|_1 = \sum_{n=1}^{\infty} |x_n|.
$$

The $\ell^1$ space equipped with the norm $\| \cdot \|_1$
is a normed linear space.
```

```{prf:theorem}
:label: res-la-ss-seq-l1-norm-just

The norm defined for $\ell^1$  space in {prf:ref}`def-la-ss-l1-norm` is
indeed a norm.
```
```{prf:proof}
[Positive definiteness]
It is clear that the norm of the zero sequence $\| \bzero \|_1 = 0$.
Now suppose that $\sum_{n=1}^{\infty} | x_n | = 0$. The sum of 
a non-negative sequence is zero only if each term is 0. Thus,
$\{x_n \} = \bzero$.

[Positive homogeneity]
Let $\bx = \{ x_n \}$ be absolutely summable. 
From {prf:ref}`res-la-ss-sequence-scaling-closure`,
we have:

$$
\| \alpha \bx \|_1 = \sum_{n-1}^{\infty} | \alpha x_n | 
= |\alpha | \sum_{n-1}^{\infty} |x_n| = | \alpha | \| \bx \|_1.
$$


[Triangle inequality]
Let $\bx = \{ x_n \}$ and $\by = \{ y_n \}$ be absolutely summable.
From {prf:ref}`res-la-ss-sequence-addition-closure`, we have:

$$
\| \bx + \by \|_1 = \sum_{n=1}^{\infty} | x_n + y_n | 
\leq \sum_{n=1}^{\infty} |x_n|  + \sum_{n=1}^{\infty} |y_n|
= \| \bx \|_1 + \| \by \|_1.
$$
```

```{prf:theorem}
:label: res-la-ss-l1-space-complete

$\ell^1$ is complete. 
In other words, every Cauchy sequence of sequences in $\ell^1$
converges to a sequence of $\ell^1$.
Thus, it is a Banach space.
```

