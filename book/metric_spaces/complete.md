# Completeness

Let $(X,d)$ and $(Y, \rho)$ be metric spaces.


## Cauchy Sequences

```{prf:definition} Cauchy sequence
:label: def-ms-cauchy-sequence

A sequence $\{x_n\}$ of $X$ is called a *Cauchy sequence* 
if for every $\epsilon > 0$, there exists $n_0$ 
(depending on $\epsilon$) such that

$$
d(x_n, x_m) < \epsilon \text{ for every } n, m > n_0.
$$
```

```{prf:proposition}
:label: res-ms-convergent-is-cauchy

Every convergent sequence is a Cauchy sequence.
```
```{prf:proof}
Let $\{x_n\}$ be a convergent with the limit $\lim x_n = x$.
Thus, for every $\epsilon > 0$, there exists $n_0$ 
such that  $d(x_n, x) < \epsilon / 2$ for all $n > n_0$.

Then, for all $m, n > n_0$

$$
d(x_n, x_m) \leq d(x_n, x) + d(x, x_m) < 
\frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.
$$ 

Thus, $\{ x_n\}$ is a Cauchy sequence.
```

```{prf:example} Not every Cauchy sequence is convergent

Consider $X = \RR_{++}$ with metric $d(x,y) = |x-y|$. 
Consider the sequence $x_n = \frac{1}{n}$.
The sequence doesn't converge in $X$ 
(Its limit 0 doesn't belong to $X$).
At the same time, $\{ x_n \}$ is Cauchy.

1. Let $\epsilon > 0$.
1. Let $n_0$ be any natural number larger than $\frac{2}{\epsilon}$.
1. Note that $n_0 > \frac{2}{\epsilon} \iff \epsilon > \frac{2}{n_0}$.
1. Then, for $m, n > n_0$:
   
   $$
   d(x_n, x_m) = |x_n - x_m | \leq x_n + x_m = \frac{1}{n} + \frac{1}{m}
   < \frac{1}{n_0} + \frac{1}{n_0} = \frac{2}{n_0} < \epsilon.
   $$
1. Thus, for every $\epsilon > 0$, there exists $n_0$ such that
   for all $m, n > n_0$, $d(x_n, x_m) < \epsilon$.
1. Hence $\{ x_n\}$ is Cauchy.
```


## Complete Metric Spaces


```{prf:definition} Complete metric space
:label: def-ms-complete-metric-space

A metric space $(X,d)$ is called *complete* if all of its
Cauchy sequences converge in the space.

In other words, $X$ is complete if every Cauchy sequence
$\{ x_n \}$ of $X$ converges to a point $x \in X$.
```

```{prf:example} Complete metric spaces

1. $\RR^n$ with the standard metric $d(x,y) = | x-y|$ is complete.
1. The Euclidean space $\RR^n$, with the standard Euclidean metric 
   ($\ell_2$ distance), is complete.
```

```{prf:example} The metric space of bounded functions
:label: ex-ms-bounded-functions-metric-space

Let $X$ be a non-empty set. 
Let $B(X)$ be the set of
{prf:ref}`bounded (total) functions <def-bra-bounded-function>` 
on $X$.

for any $f, g \in B(X)$, define $D : B(X) \times B(X) \to \RR$ as:

$$
D(f, g) \triangleq \sup \{ | f(x) - g(x)| \ST x \in X \}.
$$
Since both $f$ and $g$ are bounded, hence $D(f,g)$ is a real number.
Thus $\dom D = B(X) \times B(X)$. We claim that $D$ is a metric:

1. $D(f,g)$ is nonnegative as it is the supremum of nonnegative numbers.
1. $D(f, f) = \sup \{ | f(x) - f(x)| \} = 0$. 
   Also, if $D(f,g)=0$ then $f(x)=g(x) \Forall x \in X$. Thus, $f=g$.
1. By definition: $D(f, g) = D(g, f)$.
1. For the triangle inequality, we proceed as follows:

   Let $f,g,h \in B(X)$. For each $x \in X$, we have:

   $$
   |f(x) - g(x)| \leq | f(x) - h(x)| + |h(x) - g(x)| \leq D(f,h) + D(h, g).
   $$

   Now, taking the supremum on the L.H.S. over all $x \in X$, we get:

   $$
   D(f,g) \leq D(f,h) + D(h, g).
   $$


Next, we establish that $(B(X), D)$ is a complete metric space.
Towards this, introduce a zero function $z: X \to \RR$ as $z(x) = 0$.

1. Let $\{ f_n\}$ be a Cauchy sequence of $B(X)$.
1. Thus, for every $\epsilon > 0$, there exists $n_0$ such that
   $D(f_n, f_m) < \epsilon$ for all $m,n > n_0$.
1. In particular, note that, by definition, 
   $|f_n(x) - f_m(x)| \leq D(f_n, f_m)$
   for every $x \in X$.
1. Thus, for any $x \in X$, $|f_n(x) - f_m(x)| < \epsilon$ for all $m,n>n_0$.
1. Thus, $\{ f_n(x)\}$ is a Cauchy sequence of real numbers at each $x = X$.
1. Since, $\RR$ is complete, hence $\{ f_n(x)\}$ converges at each $x = X$.
1. We define a new function $f: X \to \RR$ as $f(x) = \lim f_n(x)$ for each $x=X$.
1. Since $|f_n(x) - f_m(x)| < \epsilon$ for all $m,n>n_0$, hence
   $|f_n(x) - f(x)| \leq \epsilon$ for all $n > n_0$ and all $x \in X$.
1. Thus, $|f(x)| \leq \epsilon + |f_n(x)|$ for all $x \in X$.
1. Thus, since $f_n$ is bounded, hence $f$ is also bounded.
1. Thus, $f \in B(X)$.
1. Finally, $D(f_n, f) = \sup \{ |f_n(x) - f(x)|\}$.
1. Since $|f_n(x) - f(x)| \leq \epsilon$ for all $x \in X$, 
   hence, taking the supremum on the L.H.S., $D(f_n, f) \leq \epsilon$.
1. Since $D(f_n, f) \leq \epsilon$ for all $n > n_0$, hence $\lim f_n = f$.
1. Thus, every Cauchy sequence in $B(X)$ converges in $B(X)$.
1. Thus, $(B(X), D)$ is a complete metric space.
```

## Closed Subsets

```{prf:theorem} 

Let $(X,d)$ be a complete metric space. Then a subset
$A$ of $X$ is closed if and only if $(A, d)$ is a complete
metric space in its own right.
``` 

```{prf:proof}
Let $A$ be closed.

1. Let $\{ x_n \}$ be a Cauchy sequence of $A$.
1. Then, $\{ x_n \}$ is a Cauchy sequence of $X$ (since $A \subseteq X$).
1. Thus, $\{ x_n \}$ is convergent, since $X$ is complete. 
1. Let $\lim x_n = x$.
1. Since $A$ is closed and $\{ x_n \}$ of $A$ is convergent, hence $x \in A$
   due to {prf:ref}`res-ms-closure-convergence`.
1. Thus, every Cauchy sequence of $A$ converges in $A$.
1. Thus, $(A,d)$ is complete.


Let $A$ be complete. We shall show that it contains all its closure points.

1. Let $x \in X$ be a closure point of $A$.
1. By {prf:ref}`res-ms-closure-point-as-limit`, 
   there is a sequence $\{x_n\}$ of $A$ that converges to $x$, i.e., $\lim x_n = x$. 
1. Since $\{ x_n \}$ converges in $X$, 
   hence $\{ x_n \}$ is a Cauchy sequence of $X$ due to {prf:ref}`res-ms-convergent-is-cauchy`.
1. But then, $\{ x_n \}$ is a Cauchy sequence of $A$.
1. Since, $A$ is complete, hence $\{ x_n \}$ converges in $A$.
1. Thus, $x \in A$.
1. Thus, $A$ contains all its closure points. $A$ is closed. 
```