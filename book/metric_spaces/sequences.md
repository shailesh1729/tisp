(sec:ms:sequences)=
# Sequences

Let $(X, d)$ be a metric space.


## Sequences

````{prf:definition}
:label: def-ms-sequence

A {prf:ref}`sequence <def-st-sequence>` in a metric space $(X,d)$ is a 
function $f : \Nat \to X$.
````
A sequence can be thought of as an ordered (countable) list of 
points in $X$.


## Convergence


````{prf:definition} Convergence
:label: def-ms-convergence

A sequence $\{ x_n \}$ in a metric space $(X,d)$ 
is said to *converge* to $x \in X$ 
if for every $\epsilon > 0$,
there exists a natural number $n_0$ (depending upon $\epsilon$) 
such that

$$
    d (x_n,x) < \epsilon \Forall n > n_0.
$$

The point $x$ is called the *limit* of the sequence $\{ x_n \}$, 
and we write $x_n \to x$ or $x = \lim x_n$.
````
In other words, $x_n \in B(x, \epsilon)$ for all $n > n_0$.

````{prf:remark}
The sequence $\{x_n\}$ gives a sequence of real numbers
$\{ y_n \}$ where $y_n = d(x_n, x)$. 

Thus, $\{ x_n \}$ converges if $\lim d(x_n, x) = 0$.
````


````{prf:theorem} Sequence Limit Uniqueness
:label: res-ms-sequence-limit-uniqueness

A sequence of points can have utmost one limit.
````

````{prf:proof}
If a sequence doesn't converge, then there is nothing to prove. 
Otherwise, suppose a sequence $\{ x_n \}$ converges to 
two limits $x$ and $y$. 
Thus, for every $\epsilon > 0$, there
exist $n_1, n_2 \in \Nat$ such that 
$d(x_n,x) < \epsilon \Forall n > n_1$  and
$d(x_n, y) < \epsilon \Forall n > n_2$. 
Now, choose $n_0 = \max (n_1, n_2)$.
Then, by triangle inequality, for every $n > n_0$

$$
    0 \leq d(x, y) \leq d(x, x_n) + d(x_n, y)  < \epsilon + \epsilon = 2\epsilon.
$$

Since this is true for all $\epsilon > 0$, hence $d(x,y)=0$.
This means that $x = y$ (Identity of indiscernibles).
````

This result and proof is adapted from 
{prf:ref}`res-bra-sequence-limit-uniqueness`.


```{prf:theorem} Characterization of closure points as limits
:label: res-ms-closure-point-as-limit

A point $x \in X$ is a closure point of $A \subseteq X$ if and
only if there is a sequence $\{ x_n \}$ of $A$ such that 
$\lim x_n = x$. 
```

```{prf:proof}

Assume $x$ is a closure point of $A$. We construct a sequence 
which converges to $x$.

1. For each $n \in \Nat$, we can pick a point $x_n \in A$ such that 
   $d(x, x_n) < \frac{1}{n}$. 
   This is possible since $B(x, \frac{1}{n}) \cap A \neq \EmptySet$ 
   for every $n \in \Nat$.
1. Form the sequence $\{ x_n \}$. 
1. Since $\lim d(x, x_n) = 0$, hence $\{x_n \}$ converges to $x$.

Assume a sequence $\{x_n\}$ of $A$ converges to $x$. 

1. For each $r > 0$, there exists some $k$ such that 
   $d(x, x_n) < r$ for all $n > k$. 
1. Thus, $B(x, r) \cap A \neq \EmptySet$ for every $r > 0$.
1. Thus, $x$ is a closure point of $A$.
```

If $x \in A$, we can simply pick the constant sequence $\{ x_n = x \}$.
It's more challenging only when $x \in \closure A \setminus A$.

```{prf:theorem}
:label: res-ms-accum-point-distinct-sequence
 
Let $x$ be an accumulation point of $A$. 
Then, there exists a sequence $\{x_n \}$ of $A$ with
distinct terms, that converges to $x$.
```

```{prf:proof}
We assume that $x$ is an accumulation point of $A$.

1. For every $r> 0$, $B(x,r) \cap (A \setminus \{   x \}) \neq \EmptySet$.
1. Let $r=1$. We can pick $x_1 \in A$ distinct from $x$ from the set
   $B(x,1) \cap (A \setminus \{ x \})$ which is not empty.
1. Assume inductively that distinct $x_1, x_2, \dots, x_n$ have been chosen
   from $A$ (all different from $x$).
1. Let $r = \min \{\frac{1}{n+1}, d(x, x_n) \}$.
1. Pick $x_{n+1}$ from the set $B(x,r) \cap (A \setminus \{ x \})$.
1. By construction, $x_{n+1}$ is distinct from previously chosen points.
1. By induction, we can construct a sequence $\{ x_n \}$ such that 
   each term in the sequence is distinct and $\lim d(x, x_n)=0$.
1. Thus, the sequence converges to $x$.
```

```{prf:theorem}
:label: res-ms-closure-convergence

Let $A$ be a subset of $X$. $A$ is closed if and only if 
every convergent sequence of $A$ converges in $A$.
```

```{prf:proof}

Assume $A$ to be closed.

1. Let $\{x_n\}$ be a convergent sequence of $A$. 
1. By {prf:ref}`res-ms-closure-point-as-limit` $x = \lim x_n$ is a closure
   point of $A$.
1. Since $A$ is closed, hence it contains all its closure points.
1. Thus, $\{x_n\}$ converges in $A$.


Assume that every convergent sequence of $A$ converges in $A$.

1. Let $x$ be a closure point of $A$. 
1. By {prf:ref}`res-ms-closure-point-as-limit`, there exists a
   convergent sequence $\{ x_n \}$ of $A$ that converges to $x$.
1. But since, $\{ x_n \}$ converges in $A$, hence $x \in A$.
1. Thus, $A$ contains all its closure points.
1. Hence, $A$ is closed.
```

```{prf:theorem}
:label: res-ms-sequence-distance-limit

If $\lim x_n = x $ and $\lim y_n = y$, then

$$
\lim_{n \to \infty} d(x_n, y_n) = d(x, y).
$$
```

```{prf:proof}

Recall from the triangle inequality:

$$
| d(x,z) - d(z, y) | \leq d(x,y).
$$

Now

$$
\begin{aligned}
| d(x_n, y_n) - d(x, y) | &\leq | d(x_n, y_n) - d(x, y_n) | + | d(x, y_n) - d (x, y) |\\
&\leq d (x_n, x) +  d(y_n, y).
\end{aligned}
$$

Choose $n_0$ such that for all $n > n_0$,  

$$
d(x_n, x) < \frac{\epsilon}{2} \text { and } d(y_n, y) <  \frac{\epsilon}{2}.
$$ 

Then  $| d(x_n, y_n) - d(x, y) | <  \epsilon$.  

Thus, for every $\epsilon > 0$, there exists $n_0$ such that for all $n > n_0$,
$| d(x_n, y_n) - d(x, y) | <  \epsilon$ holds. Thus,

$$
\lim_{n \to \infty} d(x_n, y_n) = d(x, y).
$$
```

## Subsequences

````{prf:theorem} Subsequence convergence
:label: res-ms-subsequence-convergence

Subsequences of a convergent sequence converge to the same limit 
as the original sequence.
If $\lim_{n \to \infty} x_n = x$, then $\lim_{n \to \infty} y_n = x$ for every
{prf:ref}`subsequence <def-st-sub-sequence>` $\{ y_n \}$ of $\{ x_n \}$.

Conversely, if two different subsequences of $\{ x_n \}$ converge to different limits,
then the sequence  $\{ x_n \}$  does not converge.
````
This result is a generalization of {prf:ref}`res-subsequence-convergence`
for metric spaces.

````{prf:proof}

Let $\{x_n\}$ be a convergent sequence of $X$ and
Let $\{ y_n\}$ be a subsequence of $\{ x_n\}$. 

1. Since $\lim_{n \to \infty} x_n = x$, for every $\epsilon > 0$, 
   there exists $n_0 \in \Nat$ such that
   $d (x, x_n) < \epsilon \Forall n > n_0$.
1. Since $\{ y_n \}$ is a subsequence, there exists 
   a strictly increasing sequence
   $\{ k_n \}$ of natural numbers (i.e. $1 \leq k_1 < k_2  < k_3 < \ldots)$
   such that $y_n = x_{k_n}$ holds for each $n$. 
1. Thus, there exists a $k_0 > 0$ such that
   $k_n \geq n_0 \Forall n > k_0$. Then,
1. $d(x,y_n) < \epsilon \Forall n > k_0$.
1. Thus, $\{ y_n \}$ converges to $x$ too.
````


## Dense Sets

```{prf:theorem}
:label: res-ms-dense-sequence-limit

A subset $A$ is {prf:ref}`dense <def-ms-dense-set>` 
in $X$ if and only if for every $x \in X$, 
there exists a sequence $\{ x_n \}$ of $A$ such that 
$\lim x_n = x$.
```

This is a direct application of {prf:ref}`res-ms-closure-point-as-limit`.
