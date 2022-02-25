(sec:ms:discrete-metric-space)=
# Discrete Metric Space

This section collects results on the discrete metric space.
The discrete space is trivial and not very useful in applications. 
However, it helps clarify many of the theoretical 
underpinnings of the topology of metric spaces.
Hence, its study is quite useful.

```{prf:definition}
:label: def-ms-discrete-space

Let $X$ be a nonempty set:

Define:

$$
d(x,y) = \begin{cases}
0 & x = y \\
1 & x \neq y
\end{cases}\;.
$$

$(X, d)$ is a metric space. This distance is called *discrete distance* 
and the metric space is called a *discrete metric space*.
```

In the rest of the section $X$ will denote the discrete metric
space with the distance function defined above.

## Open and Closed Sets

```{prf:proposition}
:label: res-ms-discrete-singleton-open

Every singleton in a discrete metric space is open.
```

```{prf:proof}

Let $x \in X$. Consider the open ball $B(x, \frac{1}{2})$:

$$
B(x, \frac{1}{2}) = \left \{y \in X \ST d(x,y) < \frac{1}{2} \right \}.
$$

By definition of the discrete metric:

$$
B(x, \frac{1}{2}) = \{ x \}.
$$
Thus, every singleton is an open ball. Hence it is an open set.
```

```{prf:proposition}
:label: res-ms-discrete-subset-open

Every subset of a discrete space is open.
```
```{prf:proof}
Let $A \subseteq X$.  If $A = \EmptySet$ then there is nothing to prove.

For a nonempty $A$, write it as:

$$
A = \bigcup_{x \in A} \{ x \}.
$$

Since every singleton is open and an arbitrary union of open sets is open
hence $A$ is open. 
```


```{prf:proposition}
:label: res-ms-discrete-subset-closed

Every subset of a discrete set is closed.
```
```{prf:proof}
Let $A \subseteq X$. Let $B = X \setminus A$. 
By previous result, $B$ is open. Hence, $A$ must be closed.
```

## Boundedness

```{prf:proposition}
:label: def-ms-ds-ball-diam

The {prf:ref}`diameter <def-ms-diameter>` 
of the open ball $B(x, 1)$ is 0.
```

```{prf:proof}
Note that 

$$
B(x, 1) = \{ x\}.
$$
Thus, $B(x, 1)$ is a singleton set. 

Hence, 

$$
\diam B(x, 1) = \sup \{ d(x,y) \ST x, y \in B(x, 1) \}
= d(x,x) = 0.
$$
```
This result is a counter example to explain that
while $\diam B(x,r) \leq 2 r$ always, it doesn't need
to be equal to $2 r$. 

```{prf:proposition}
:label: def-ms-ds-bounded

The discrete space is bounded.
```
```{prf:proof}
Let $x, y \in X$. 
1. If $x \neq y$, then $d(x,y) = 1$.
1. Thus, $\diam X = \sup d(x,y) = 1$.
1. $X$ is bounded.
```

## Rare Sets

```{prf:proposition}
:label: res-ms-discrete-rare-empty

The only rare (nowhere dense) subset of $X$ is $\EmptySet$.
```

```{prf:proof}
Let $A \subseteq X$. $A$ is open as well as closed.
Hence $\closure A = A$ and $\interior \closure A = \interior A = A$.
Thus, $A$ is rare if and only if $A = \EmptySet$.
```

## Cauchy Sequences

```{prf:proposition}
:label: res-ms-discrete-cauchy-constant

In a discrete metric space, a Cauchy sequence is eventually
constant.
```

```{prf:proof}
Let $\{x_n \}$ be a Cauchy sequence of $X$. 
Then, there exists $k$ such that for all $m,n > k$, 

$$
d(x_m, x_n) < \frac{1}{2}.
$$

But then for all $m,n > k$, $x_m = x_n$. Thus, 
$\{ x_n \}$ must be eventually constant.
```

## Completeness

```{prf:proposition}
:label: res-ms-discrete-complete

A discrete metric space is complete.
```

```{prf:proof}
Since every Cauchy sequence is eventually constant, hence
it converges. Thus the discrete metric space is complete.
```

## Meager Sets

```{prf:proposition}
:label: res-ms-discrete-meager-empty

The only meager set in $X$ is $\EmptySet$.
```

```{prf:proof}
Recall from {prf:ref}`res-ms-complete-meager-interior-empty`
that a meager set has an empty interior.

Since every nonempty subset of $X$ is open hence it doesn't have
an empty interior. 

Thus, the only meager set is $\EmptySet$.
```

## Baire Category Theorem

```{prf:observation}
:label: res-ms-discrete-baire

Let $X$ be a countable set with a discrete metric.

$X$ is complete and it satisfies the Baire category theorem.

Let $\{x_n\}$ be an enumeration of $X$.
Then, we can write $X$ as:

$$
X = \bigcup_{n=1}^{\infty} \{ x_n\}.
$$

Now, although it's a countable union of singletons, 
the singletons themselves are not rare sets. 
Hence, we cannot say that $X$ meager.
```

## Compactness

```{prf:example}
:label: ex-discrete-space-closed-bounded-not-compact

We can construct a closed and bounded set which is not compact.

1. Let $X$ be an infinite set with the 
   {prf:ref}`discrete metric <def-ms-discrete-space>`.
1. Then, $B(x,1) = \{ x\}$ is a singleton for every $x \in X$.
1. $X$ is closed.
1. $X$ is bounded since $d(x, y) \leq 1$ for every $x, y \in X$. Hence $\diam X = 1$.
1. Consider the open cover $X = \bigcup_{x \in X} B(x, 1)$. 
1. This cover cannot be reduced to a finite subcover.
1. Thus, $X$ is not compact even though it is closed and bounded.
```