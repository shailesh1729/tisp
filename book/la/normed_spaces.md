(sec:la:normed-spaces)=
# Normed Linear Spaces

A norm is a real number attached to every vector.
Norm is a generalization of the notion of length.
Adding a norm to a vector space makes it a normed
linear space with rich topological properties
as a norm induces a 
{prf:ref}`distance function <def-ms-distance-function>` (a metric)
on the vector space converting it into a 
{prf:ref}`metric space <def-ms-metric-space>`
with an algebraic structure.
A normed linear space that is 
{prf:ref}`complete <def-ms-complete-metric-space>` is called
a Banach space.


We restrict our attention to real vector spaces and complex vector spaces.
Thus, the field $\FF$ can be either $\RR$ or $\CC$.

## Norm

````{prf:definition} Norm
:label: def-la-norm

A *norm* over a $\FF$-vector space $\VV$ is any real valued function
$\| \| : \VV \to \RR$ mapping $ \bv \mapsto \| \bv\|$
satisfying following properties:

1. [Positive definiteness]

   $$
   \| \bv\| \geq 0 \quad \forall \bv \in \VV \text{  and  } \| \bv\| = 0 \iff \bv = \bzero.
   $$
1. [Positive homogeneity]

   $$
    \| \alpha \bv \| = | \alpha | \| \bv \| \quad \forall \alpha \in \FF; \forall \bv \in \VV.
   $$
1. [Triangle inequality]

   $$
    \| \bv_1 + \bv_2 \| \leq \| \bv_1 \| + \| \bv_2 \| \quad \forall \bv_1, \bv_2 \in \VV.
   $$
````

```{prf:remark}
$$
\| - \bv \| = \| (-1) \bv \| = | - 1 | \| \bv \| = \| \bv \| \Forall \bv \in \VV.
$$
```

```{prf:theorem} Triangle inequality II
:label: res-la-ns-triangle-inequality-2

$$
| \| \bx \| - \| \by \| | \leq  \| \bx - \by \| \Forall \bx, \by \in \VV.
$$
```

```{prf:proof}
Putting $\bv_1 = \bx$ and $\bv_2 = \by - \bx$ in the triangle inequality, we get:

$$
\begin{aligned}
& \| \bx + \by - \bx \| \leq \| \bx \| + \| \by - \bx \| \\
& \iff \| \by \| \leq \| \bx \| + \| \by - \bx \| \\
& \iff \| \by \| - \| \bx \| \leq \| \by - \bx \| = \| \bx - \by \|.
\end{aligned}
$$

Interchanging $\bx$ and $\by$ in previous inequality, we get:

$$
\| \bx \| - \| \by \| \leq \| \bx - \by \|.
$$

Combining the two inequalities, we get:

$$
| \| \bx \| - \| \by \| | \leq  \| \bx - \by \| \Forall \bx, \by \in \VV.
$$
```

```{prf:theorem} Triangle inequality for distances
:label: def-la-ns-distance-triangle-inequality

The triangle inequality is equivalent to the following property:

$$
\| \bx - \by \| \leq \| \bx - \bz \| + \| \bz - \by \| \Forall \bx, \by, \bz \in \VV.
$$
```

```{prf:proof}

Start with 

$$
\| \bv_1 + \bv_2 \| \leq \| \bv_1 \| + \| \bv_2 \|.
$$

Put $\bv_1 = \bx - \bz $ and $\bv_2 = \bz - \by$. We get:

$$
\| \bx - \bz  + \bz - \by \| \leq \| \bx - \bz  \| + \| \bz - \by \|
\iff
\| \bx - \by \| \leq \| \bx - \bz \| + \| \bz - \by \|.
$$

For the converse, start with:

$$
\| \bx - \by \| \leq \| \bx - \bz \| + \| \bz - \by \|
$$

Put $\bv_1 = \bx - \bz$ and $\bv_2 = \bz - \by$. Then, $\bv_1 + \bv_2 = \bx - \by$.
We get:

$$
\| \bv_1 + \bv_2 \| \leq \| \bv_1 \| + \| \bv_2 \|.
$$
```

## Normed Linear Space

````{prf:definition} Normed linear space
:label: def-la-normed-linear-space

An $\FF$-vector space $\VV$ equipped with a norm $\| \| : \VV \to \RR$ is known
as a *normed linear space*. Other common terms are 
*normed vector space* or simply *normed space*.
````

```{prf:remark}
We will assume that the vector space is non-trivial;
i.e., different from $\{ \bzero \}$.
```

### Metric

```{prf:definition} Metric induced by a norm
:label: def-la-norm-induced-metric

Every norm $\| \cdot \| : \VV \to \RR$ induces a 
{prf:ref}`metric <def-ms-distance-function>` defined as:

$$
d(\bx , \by) = \| \bx - \by \| \Forall  \bx, \by \in \VV.
$$
```

```{prf:theorem}

The metric $d : \VV \times \VV \to \RR$ 
induced by a norm $\| \cdot \| : \VV \to \RR$ is indeed
a metric satisfying all the properties of a 
{prf:ref}`metric <def-ms-distance-function>`( distance function).
```

```{prf:proof}
We proceed as follows:

1. Non-negativity: $d(\bx, \by) \geq 0$ since $\| \cdot \|$ is positive definite.
1. Identity of indiscernibles. 
   1. Assume $d(\bx, \by) = 0$. 
   1. Then, $\| \bx - \by \| = 0$.
   1. Thus, $\bx = \by$ since $\| \cdot \|$ is positive definite.
   1. Now, assume $\bx = \by$. 
   1. Then, $d(\bx, \by) = \| \bx - \by \| = \| \bzero \| = 0$ since $\| \cdot \|$ is positive definite.
1. Symmetry: $d(\bx, \by) = \| \bx - \by \| = \| (-1)(\by - \bx) \| = |-1| \| \by - \bx \| = d(\by, \bx)$ using the positive homogeneity property of $\| \cdot \|$.
1.  Triangle inequality: See {prf:ref}`def-la-ns-distance-triangle-inequality` above.
```

```{prf:remark}
We will use the notation $\| \cdot \|$ to denote both the
norm and the metric induced by the norm.
```

```{prf:definition} Metric space $\VV$
The normed space $\VV$ equipped with the metric 
induced by the norm as defined in {prf:ref}`def-la-norm-induced-metric`
becomes a *metric space*  $(\VV, \| \cdot \|)$.

If the norm and induced metric are clear from the context,
then we shall simply write it as $\VV$.
```

```{prf:theorem} Translation invariance
:label: res-la-ns-metric-translation-invariant

The metric induced by a norm is translation invariant.

For any $\bu, \bv, \bw \in \VV$:

$$
d(\bu, \bv) = d(\bu + \bw, \bv  + \bw). 
$$
```

```{prf:proof}
Expanding from definition:

$$
d(\bu + \bw, \bv  + \bw) = \| \bu + \bw - (\bv  + \bw) \|
= \| \bu  - \bv \| = d(\bu, \bv).
$$
```

### Continuity

```{prf:theorem}
A function $\| \cdot \| : \VV \to \RR$ satisfying
all the properties of a {prf:ref}`norm <def-la-norm>`
is {prf:ref}`uniformly continuous <def-ms-uniform-continuity>`
in the metric space induced by the norm.
```

```{prf:proof}
Let $\bx, \by \in \VV$. 
Assume $d(\bx, \by) < \delta$.
Choose $\epsilon = \delta$.
Now, due to {prf:ref}`res-la-ns-triangle-inequality-2`:

$$
d(\bx, \by) = \| \bx - \by \| \geq | \| \bx \| - \| \by \| |.
$$

Thus,

$$
d(\bx, \by) < \delta \implies | \| \bx \| - \| \by \| | < \delta = \epsilon.
$$

Thus, $\| \cdot \|$ is uniformly continuous.
```

## Boundedness

```{prf:definition} Bounded set
:label: def-la-ns-bounded-set

A subset $A$ of $\VV$ is called *norm bounded* or simply *bounded*
if there exist $M > 0$ such that:

$$
\| \bx \| \leq M \Forall \bx \in A.
$$
```
Compare the definition with the definition of
{prf:ref}`bounded sets <def-ms-boundedness-set>` in metric spaces.

## Sequences

```{prf:definition} Convergence in norm
:label: def-la-ns-convergence-norm

A {prf:ref}`sequence <def-ms-sequence>` 
$\{ \bx_n \}$ of a normed space $\VV$ is said to 
*converge in norm* to $\bx \in \VV$ if 

$$
\lim_{n \to \infty} \| \bx - \bx_n \|  = 0;
$$
i.e., if $\{\bx_n \}$ converges to $\bx$ with respect to the
metric induced by the norm.
We write this as:

$$
\lim_{n \to \infty} \bx_n = \bx.
$$
```


## The Calculus of Limits

Let $\{ \bx_n \}$ and $\{ \by_n \}$ be convergent sequences of $\VV$.
Our concern here is to understand what happens to the limits if
the sequences are combined.

Our presentation here is similar to 
the presentation for sequences of real numbers
in {ref}`sec:bra:sequences:calculus:limits`.

Let $\lim \{\bx_n\} = \bx$ and $\lim \{\by_n\}  = \by$. Then:

```{prf:theorem} Scaling a sequence
:label: res-la-ns-seq-calculus-scaling

$$
\lim \{\alpha \bx_n \} = \alpha \bx \Forall \alpha \in \FF.
$$
```

```{prf:proof}
If $\alpha = 0$, then we have a constant sequence and the result is trivial.
So assume that $\alpha \neq 0$. Then:

$$
    \|\alpha \bx_n - \alpha \bx \| = | \alpha |  \| \bx_n - \bx \|.
$$

Let $\epsilon > 0$ and choose $n_0 \in \Nat$
such that $\| \bx - \bx_n \| < \frac{\epsilon}{ | \alpha | }$
for all $n > n_0$. Then

$$
    \|\alpha \bx_n - \alpha \bx \| = | \alpha |  \| \bx_n - \bx \| 
    < | \alpha | \frac{\epsilon}{ | \alpha | } = \epsilon \Forall n > n_0.
$$
```

```{prf:corollary} Negating a sequence
:label: res-la-ns-seq-calculus-negation

$$
\lim \{-\bx_n \} = -\bx.
$$
```

We get this result by choosing $\alpha = -1$.


```{prf:theorem} Addition of sequences
:label: res-la-ns-seq-calculus-addition

$$
\lim \{\bx_n  + \by_n\} =  \bx + \by.
$$
```
```{prf:proof}
From triangle inequality we get:

$$
    \| \bx_n + \by_n - (\bx + \by) | \leq \| \bx_n - \bx \| + \| \by_n - \by \|.
$$

For any $\epsilon > 0$, choose $n_1$ such that 
$\| \bx_n - \bx \| < \frac{\epsilon}{2} \Forall n > n_1$.

Similarly, choose $n_2$ such that 
$\| \by_n - \by \| < \frac{\epsilon}{2} \Forall n > n_2$.

Now choose $n_0 = \max (n_1, n_2)$. Then:

$$
 \| \bx_n + \by_n - (\bx + \by) \|  
 \leq \| \bx_n - \bx \| + \| \by_n - \by \| 
 < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
 \Forall n > n_0.
$$
```

```{prf:corollary} Subtraction of sequences
:label: res-la-ns-seq-calculus-subtraction

$$
\lim \{\bx_n  - \by_n\} =  \bx - \by.
$$
```
Negate $\{ \by_n \}$ and add to $\{\bx_n \}$.

## Cauchy Sequences

```{prf:theorem}
Every {prf:ref}`Cauchy sequence <def-ms-cauchy-sequence>` 
in a normed space is bounded.
```
The proof is very similar to the proof for the 
boundedness of Cauchy sequences in real line
({prf:ref}`res-bra-cauchy-sequence-bounded`).

```{prf:proof}
Let $\{ \bx_n \}$ be a sequence of a normed space $\VV$.

1. Choose $\epsilon = 1$. 
1. Then there exists $n_0 \in \Nat$ 
   such that $\| \bx_n - \bx_m \| < 1$ whenever $m, n \geq n_0$.
1. In particular, the statement is valid when $m  = n_0$. 
   i.e. $\| \bx_n - \bx_{n_0} \| < 1$.

1. But,

   $$
   \begin{aligned}
   & \| \bx_n - \bx_{n_0} \| < 1\\
   & \implies | \| \bx_n \| - \| \bx_{n_0 } \| | < 1\\ 
   & \implies \|\bx_n \| < 1  + \| \bx_{n_0 } \| \Forall n \geq n_0.
   \end{aligned}
   $$

1. Choosing $M = \max(\|x_1\|, \dots, \|\bx_{n_0-1}\|, \|\bx_{n_0}\| + 1)$, 
   it is clear that $\| x_n \| \leq M$
1. Hence $\{ \bx_n \}$ is bounded.
```

## Banach Spaces

```{prf:definition} Banach space
A normed space $\VV$ that is
{prf:ref}`complete <def-ms-complete-metric-space>`
with respect to the metric induced by its norm
is called a *Banach space*.

In other words, $\VV$ is a Banach space if
every Cauchy sequence of $\VV$ converges in $\VV$.
```

```{prf:example} Examples of Banach spaces

The spaces in examples below have been described
in detail elsewhere. Follow the links.

1. The {prf:ref}`Euclidean space <def-la-euclidean-space>` 
   $\RR^n$ is complete with respect to the
   {prf:ref}`Euclidean norm <def-la-euclidean-norm>`.
   Thus, it is a Banach space. 

1. The {prf:ref}`space<def-la-is-bounded-functions-space>`
   of bounded real valued functions $B(X)$ over a nonempty
   set $X$ equipped with 
   {prf:ref}`sup norm <def-la-is-bx-sup-norm>`
   is {prf:ref}`complete <res-la-is-bx-complete>`.
```