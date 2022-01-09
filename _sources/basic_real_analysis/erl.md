The Extended Real Line
=========================

```{prf:definition} Extended real line

The *extended real number system* or *extended real line* 
is obtained from the real number system $\RR$ by adding 
two infinity elements $+\infty$ and $-\infty$, where the
infinities are treated as actual numbers. 

It is denoted as $\ERL$ or $\RR \cup \{-\infty, +\infty\}$.

The symbol $+\infty$ is often written simply as $\infty$.
```

In order to make $\ERL$ a useful number system, we need
to define the comparison and arithmetic rules of the new
infinity symbols w.r.t. existing elements in $\RR$ and between
themselves.

## Order

```{prf:definition} Extended valued comparison rules

We define the following rules of comparison between real numbers
and infinities:

- $ a < \infty \Forall a \in \RR$
- $ a > -\infty \Forall a \in \RR$
- $ -\infty < \infty $

In other words $ -\infty < a < \infty \Forall a \in \RR$.
```

Following notations are useful:

- $\RR = (-\infty, \infty)$
- $\RR \cup \{ \infty\} = (-\infty, \infty]$
- $\RR \cup \{ -\infty\} = [-\infty, \infty)$
- $\RR \cup \{ -\infty, \infty\} = [-\infty, \infty]$


## Arithmetic

```{prf:definition} Extended valued arithmetic

The arithmetic between real numbers and the infinite values
is defined as below:

$$
\begin{aligned}
& a + \infty = \infty + a = \infty \quad (-\infty < a < \infty)\\
& a - \infty = -\infty + a = -\infty \quad (-\infty < a < \infty)\\
& a \times \infty = \infty \times a  = \infty \quad (0 < a < \infty)\\
& a \times (-\infty) = (-\infty) \times a  = -\infty \quad (0 < a < \infty)\\
& a \times \infty = \infty \times a  = -\infty \quad (-\infty < a < 0)\\
& a \times (-\infty) = (-\infty) \times a  = \infty \quad (-\infty < a < 0)\\
& \frac{a}{\pm \infty} = 0\quad (-\infty < a < \infty)
\end{aligned}
$$

The arithmetic between infinities is defined as follows:

$$
\begin{aligned}
&\infty + \infty = \infty\\
&(-\infty) + (-\infty) = -\infty\\
&\infty \times \infty = \infty\\
&(-\infty) \times (-\infty) = \infty\\
&(-\infty) \times \infty = -\infty\\
&\infty \times (-\infty) = -\infty
\end{aligned}
$$

Usually, multiplication of infinities with zero is left undefined.
But for the purposes of mathematical analysis and optimization, 
it is useful to  define as follows: 

$$
0 \times \infty = \infty \times 0 = 0 \times (-\infty) = (-\infty) \times 0 = 0.
$$
```


## Sequences, Series and Convergence

```{prf:definition} Convergence to infinities
:label: def-bra-erl-convergence-infinity

A sequence $\{ x_n\}$ of $\RR$ *converges to* $\infty$ if for every $M > 0$,
there exists $n_0$ (depending on M) such that $x_n > M$ for all $n > n_0$.

We denote this by:

$$
\lim x_n = \infty.
$$

A sequence $\{ x_n\}$ of $\RR$ *converges to* $-\infty$ if for every $M < 0$,
there exists $n_0$ (depending on M) such that $x_n < M$ for all $n > n_0$.

We denote this by:

$$
\lim x_n = -\infty.
$$
```

We can reformulate {prf:ref}`res-bra-sequence-monotone-bounded-convergence` as:

```{prf:theorem} Convergence of monotone sequences
:label: res-bra-sequence-monotone-convergence

Every monotone sequence of real numbers converges to a number in $\ERL$.
```

```{prf:proof}
Let $\{x_n\}$ be an increasing sequence. If it is bounded then by
{prf:ref}`res-bra-sequence-monotone-bounded-convergence`, it converges
to a real number. 

Assume it to be unbounded (from above). Then, for every $M > 0$, there exists
$n_0$ (depending on M) such that $x_n > M$ for all $n > n_0$.
Then, by {prf:ref}`def-bra-erl-convergence-infinity`, it converges to
$\infty$.

Let $\{x_n\}$ be a decreasing sequence. If it is bounded then by
{prf:ref}`res-bra-sequence-monotone-bounded-convergence`, it converges
to a real number. 

Assume it to be unbounded (from below). Then, for every $M < 0$, there exists
$n_0$ (depending on M) such that $x_n < M$ for all $n > n_0$.
Then, by {prf:ref}`def-bra-erl-convergence-infinity`, it converges to
$-\infty$.

Thus, every monotone sequence either converges to a real number or it
converges to one of the infinities.
```

```{prf:remark}
Consider a {prf:ref}`series <def-bra-infinite-series>`
$\sum x_n$. If the sequence of partial sums converges
to $\infty$, we say that $\sum x_n = \infty$ i.e. the sum of the series is
infinite. Similarly, if the sequence of partial sums converges to 
$-\infty$, we say that $\sum x_n = -\infty$.
```

```{prf:remark}
Every series of non-negative real numbers converges in $\ERL$.
```

```{prf:proof}
The sequence of partial sums is an increasing sequence. 
By {prf:ref}`res-bra-sequence-monotone-convergence`, it converges
either to a real number or to $\infty$.
```

