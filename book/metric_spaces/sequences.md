(sec:ms:sequences)=
# Sequences

Let $(X, d)$ be a metric space.


## Sequences

````{prf:definition}
:label: def-ms-sequence

A {prf:ref}`sequence <def-st-sequence>` in a metric space $(X,d)$ is a 
function $x : \Nat \to X$. It maps every natural number to
an element in the set $X$.

If $A$ is a subset of $X$, then a sequence of $A$ means
a function $x: \Nat \to A$. 
````

A sequence can be thought of as an ordered (countable) list of 
points in $X$. We often write a sequence $x : \Nat \to X$ as
$\{ x_n \}$ which means the list $\{x_1, x_2, x_3, \dots \}$
where $x_n = x(n)$. In this sense, $x_n$ denotes the $n$-th
entry in the sequence.

1. A sequence need not enumerate all elements of $X$.
1. An element may be repeated multiple times in a sequence.


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

### Limit Uniqueness

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


### Choice of Metric

Let $X$ be a set and $d_1$ and $d_2$ be two different
metrics defined on $X$. A sequence which converges
in the metric space $(X, d_1)$ may not converge
in the metric space $(X, d_2)$ unless the metrics
are equivalent.

```{prf:example} Sequence convergence on different metrics
:label: ex-ms-seq-converge-two-metrics

Consider the space of all continuous real valued
functions defined on the interval $[0,1]$
denoted by $C[0,1]$.

We introduce two different metrics on $C[0,1]$.

1. The metric $d_1$ is defined as

   $$
   d_1(f, g) = \int_0^1 |f(x) - g(x)| d x.
   $$
1. The metric $d_{\infty}$ is defined as

   $$
   d_{\infty}(f, g) = \sup_{x \in [0,1]} \{|f(x) - g(x)| \}.
   $$

We now introduce a sequence which converges
in $(C[0,1], d_1)$ but doesn't in $(C[0,1], d_{\infty})$.

1. Consider the sequence of functions $\{ f_n \}$
   where $f_n(x) = e^{-n x}$.
1. It is clear that $f_n \in C[0,1]$.
1. The sequence of functions converges point-wise
   to a function $f_p$ given by

   $$
   f_p(x) = \begin{cases}
   0 & x \neq 0 ; \\
   1 & x = 0.
   \end{cases}
   $$
1. As we can see that $f_p \notin C[0,1]$
   as the function is not continuous (from the right)
   at $x=0$.
1. We introduce the zero function
   $\bzero : [0,1] \to \RR$ defined as 

   $$
   \bzero(x) = 0 \quad \Forall x \in [0,1].
   $$
1. Clearly $\bzero \in C[0,1]$.
1. Note that 

   $$
   d_1(f_n, \bzero) = \int_0^1 |f_n(x) - 0| d x
   = \int_0^1 e^{-n x} d x
   = \frac{1 - e^{-n}}{n}.
   $$
1. Clearly $d_1(f_n, \bzero) \to 0$ as $n \to \infty$.
1. Hence $\{ f_n \}$ converges to $\bzero$ in $(X, d_1)$.

We now show that $\{ f_n \}$ doesn't converge to
any function in $(C[0,1], d_{\infty})$.

1. We first note that

   $$
    d_{\infty} (f_n, \bzero)
    = \sup_{x \in [0, 1]}\{ |f_n(x) - 0 | \}
    = \sup_{x \in [0, 1]}\{ e^{-n x} \}
    = 1.
   $$
1. Hence $\{ f_n \}$ doesn't converge to $\bzero$.
1. For contradiction, let $f$ be the limit of  $\{ f_n \}$.
1. Since $f$ is not identically zero and is continuous,
   hence it must be non-zero throughout an open interval
   $(c,d)$.
1. Thus $|f(x)| \geq M \Forall x \in (c,d)$ for some $M > 0$.
1. Since for any fixed $x \in (c,d)$, 
   $\lim e^{-n x} = 0$, hence there exists $n_1 \in \Nat$ 
   such that $|e^{-n x}| < M $ for every $x \in (c, d)$.
1. Now,

   $$
   |f(x) - e^{-n x}| \geq | |f(x)| - |e^{-nx}| |.
   $$
1. For $n > n_1$, we get 

   $$
   |f(x) - e^{-n x}| \geq |f(x)| - e^{-nx}.
   $$
1. Therefore

   $$
   \sup_{x \in (c,d)} \{ |f(x) - e^{-n x}| \}
   \geq M - e^{- n c} \Forall n > n_1.
   $$
1. Taking the limit

   $$
   \lim_{n \to \infty}\sup_{x \in (c,d)} \{ |f(x) - e^{-n x}| \}
   \geq M.
   $$
1. Therefore

   $$
   \lim_{n \to \infty} d_{\infty} (f_n , f)
   = \lim_{n \to \infty}\sup_{x \in (c,d)} \{ |f(x) - f_n(x) | \}
   \geq M.
   $$
1. We arrive at a contradiction as the distance doesn't approach
   the limit to 0.
1. Thus the sequence $\{ f_n \}$ doesn't converge to
   any function $f \in C[0, 1]$.
```



### Closure Points

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

### Accumulation Points

```{prf:theorem} Accumulation point and distinct sequences
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

### Closedness

```{prf:theorem} Closedness = Convergence of sequences
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

### Distance between Sequences

```{prf:theorem} Sequence distance in the limit
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

Recall from {prf:ref}`def-st-sub-sequence` that
a subsequence of a sequence $\{ x_n \}$
is a sequence $\{ y_n \}$ for which there exists 
a strictly increasing sequence
$\{ k_n \}$ of natural numbers 
(i.e. $1 \leq k_1 < k_2  < k_3 < \ldots)$
such that $y_n = x_{k_n}$ holds for each $n$.

A natural question that arises is that
if a subsequence converges then does the
sequence also converge. Alternatively,
if a sequence converges then do all of its
subsequences converge? 

It turns out that if a subsequence converges
then it is not necessary that the sequence
itself will converge. However, if a sequence
converges, then all its subsequences
converge to the same limit.

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


## Equivalent Metrics


```{prf:theorem} Metric equivalence and convergent sequences
:label: res-ms-eq-metric-conv-sequences

Let $d_a$ and $d_b$ be two different metrics on the same set $X$. 
Then, $d_a$ and $d_b$ are equivalent if and only if
they lead to identical set of convergent sequences;
i.e., a sequence is convergent in $(X, d_a)$ if and only
if it is also convergent in $(X, d_b)$ and it has same
limit in both metric spaces.

In other words, a sequence $\{ x_n \}$ of $X$ satisfies 
$\lim d_a(x_n, x) = 0$ if and only if $\lim d_b(x_n, x) = 0$.
```

```{prf:proof}
Assume that the two metric spaces $(X, d_a)$ and $(X, d_b)$ 
have same topology. Thus, they have same open sets.


1. Let $\{x_n \}$ be a convergent sequence of $(X, d_a)$ converging to $x$.
1. Now, let $\epsilon > 0$ be arbitrary and 
   consider the open ball $B_b(x, \epsilon)$.
1. By {prf:ref}`res-ms-eq-metric-balls-in-balls`, there exists
   an $r > 0$ such that $B_a(x, r) \subseteq B_b(x, \epsilon)$.
1. Since $\{ x_n \}$ is convergent in $(X, d_a)$, hence
   there exists $n_0 \in \Nat$ such that
   $x_n \in B_a(x, r) \subseteq B_b(x, \epsilon)$ for all $n > n_0$.
1. Thus, for every $\epsilon > 0$, there exists $n_0 \in \Nat$
   such that $x_n \in B_b(x, \epsilon)$ for all $n > n_0$.
1. Thus, $\{x_n \}$ is convergent in $(X, d_b)$ with limit $x$.
1. Similar reasoning shows that if a sequence is convergent in $(X, d_b)$
   then it is convergent in $(X, d_a)$ too.
1. Thus, the convergent sequences in both metric spaces are identical
   and have same limits.

Now, assume that the convergent sequences in both metric spaces 
$(X, d_a)$ and $(X, d_b)$
are identical and have same limits.

1. Let $C$ be a closed set of $(X, d_a)$. 
1. Let $x \in C$. Then, $x$ is a closure point of $C$ in $(X, d_a)$.
1. Then, there exists a sequence $\{ x_n \}$ of $C$ such that
   $\lim x_n = x$ in $(X, d_a)$.
1. But by our hypothesis, convergent sequences are identical in both 
   metric spaces.
1. Hence $\lim x_n = x$ in $(X, d_b)$ also.
1. Hence, $x$ is a closure point of $C$ in $(X, d_b)$ too.
1. Thus, every element of $C$ is a closure point of $C$ in $(X, d_b)$.
1. Thus, $C$ is closed in $(X, d_b)$.
1. A similar argument shows that if $C$ is closed in $(X, d_b)$ then it is 
   closed in $(X, d_a)$ too.
1. Thus, both metrics determine the same set of closed sets on $X$.
1. Thus, both metrics determine the same set of open sets on $X$.
1. Thus, they determine the same topology.
1. Thus, the two metrics are equivalent.
```

Procedure to show that two metrics are equivalent.

* Choose an arbitrary sequence $\{x_n\}$ which converges
  in $(X, d_a)$ to a limit  (say $x$). 
* Show that $\lim d_b(x_n, x) = 0$.
* Now, choose an arbitrary sequence $\{x_n\}$ which converges
  in $(X, d_b)$ to a limit  (say $x$). 
* Show that $\lim d_a(x_n, x) = 0$.
