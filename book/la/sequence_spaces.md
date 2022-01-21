# Sequence Spaces

We shall assume the field of scalars $\FF$ to be either $\RR$ or $\CC$.

## The Space of all Sequences

Recall that a {prf:ref}`sequence <def-st-sequence>` is
a map $\bx : \Nat \to \FF$ and is written as $\{ x_n \}$.
The set of all sequences of $\FF$ is denoted by $\FF^{\Nat}$
or just $\FF^{\infty}$ in Cartesian product notation.

```{prf:definition} Vector addition of sequences
Let $\bx = \{ x_n \}$ and $\by = \{ y_n \}$ be any two
sequences in $\FF^{\infty}$.

Their vector addition is defined as:

$$
\bx + \by \triangleq \{ x_n + y_n \}.
$$
```

```{prf:definition} Scalar multiplication of sequence
Let $\bx = \{ x_n \}$ be any
sequence in $\FF^{\infty}$
and let $\alpha \in \FF$.

The scalar multiplication of $\alpha$ with $\bx$ is defined as:

$$
\alpha \bx \triangleq \{ \alpha x_n\}.
$$
```

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
A sequence $\{x_n\}$ of $\FF$ is called absolute summable if

$$
\sum_{n=1}^{\infty} |x_n| < \infty.
$$
```


```{prf:theorem}
If sequences $\{x_n \}$ and $\{ y_n\}$ are absolutely summable, 
then their sum $\{ x_n + y_n \}$ is absolutely summable with

$$
\sum_{n=1}^{\infty} |x_n + y_n| \leq \sum_{n=1}^{\infty} |x_n|  + \sum_{n=1}^{\infty} |y_n|. 
$$

Also for any $\alpha \in \FF$, the sequence  $\{ \alpha x_n \}$ is 
absolutely summable with:

$$
\sum_{n=1}^{\infty} | \alpha x_n| =  | \alpha| \sum_{n=1}^{\infty} |  x_n|.
$$
```

```{prf:definition} $\ell_1$ The space of absolutely summable sequences
Let $\ell_1$ denote the set of all absolutely summable sequences of $\FF$.
Then $\ell_1$ equipped with the vector addition and scalar multiplication
defined above is a vector space. 
```

```{prf:definition} Norm for the $\ell_1$ space

The standard norm for the $\ell_1$ space is defined 
for any $\bx \in \ell_1$ as:

$$
\| \bx \|_1 = \sum_{n=1}^{\infty} |x_n|.
$$

The $\ell_1$ space equipped with the norm $\| \cdot \|_1$
is a normed linear space.
```


```{prf:theorem}
$\ell_1$ is complete. 
In other words, every Cauchy sequence of sequences in $\ell_1$
converges to a sequence of $\ell_1$.
Thus, it is a Banach space.
```

