# Continuity

Let $(X,d)$ and $(Y, \rho)$ be metric spaces.

## Continuous Functions

We restrict our attention to 
{prf:ref}`total <def-st-total-function>` functions.

```{prf:definition} Continuous function
:label: def-ms-continuous-function

A (total) function $f: X \to Y$ between the two metric spaces
is said to be *continuous at a point* $a \in X$ if
for every $\epsilon > 0$, there exists $\delta > 0$
(depending on $\epsilon$) such that

$$
\rho (f(x), f(a)) < \epsilon \text{ whenever } d(x, a) < \delta.
$$

$f$ is said to be *continuous* on $X$ if $f$ is continuous
at every point of $X$.
```

In other words, there is an open ball $B_X(a, \delta)$ 
around $a$ 
which maps within the open ball $B_Y(f(a), \epsilon)$ around $f(a)$.

```{prf:theorem} Characterization of continuous functions
:label: res-ms-continuous-function-characterization

Let $f: X \to Y$ be a (total) function between two metric spaces.
The following statements are equivalent:

1. $f$ is continuous on $X$.
1. $f^{-1}(\OOO)$ is open subset of $X$ whenever $\OOO$ is an open set of $Y$.
1. If $\lim x_n = x$ holds in $X$, then $\lim f(x_n) = f(x)$ holds in $Y$.
1. $f(\closure A) \subseteq \closure f(A)$ holds for every subset $A$ of $X$.
1. $f^{-1}(C)$ is a closed subset of $X$ whenever $C$ is a closed subset of $Y$.
```

```{prf:proof}

(1) $\implies$ (2). We prove this by showing that 
every point in  $f^{-1}(\OOO)$ is its interior point.

1. Let $\OOO$ be open in $Y$. Let $a \in f^{-1}(\OOO)$.
1. Thus, $f(a) \in \OOO$. 
1. Since $\OOO$ is open, there exists $r > 0$ such that $B_Y(f(a), r) \subseteq \OOO$.
1. Since $f$ is continuous at $a$, there exists $\delta > 0$ (depending on $r$)
   such that 

   $$
   d(x, a) < \delta \implies \rho(f(x), f(a)) < r.
   $$
1. i.e., for any $x \in B_X(a, \delta)$, 
   $f(x) \in B_Y(f(a), r) \subseteq \OOO$.
1. Thus, $x \in f^{-1}(\OOO)$ for any $x \in B_X(a, \delta)$.
1. This means that $B_X(a, \delta) \subseteq f^{-1}(\OOO)$.
1. Thus, $a$ is an interior point of $f^{-1}(\OOO)$.
1. Since every point in $f^{-1}(\OOO)$ is its interior point, 
   hence $f^{-1}(\OOO)$ is open.


(2) $\implies$ (3)

1. Let $\lim x_n = x$ in $X$ and $r > 0$.
1. Let $\OOO = B_Y(f(x), r)$.
1. By (2), $f^{-1}(\OOO)$ is open in $X$.
1. Since $x \in f^{-1}(\OOO)$, there exists some $\delta > 0$ 
   such that $B_X(x, \delta) \subseteq f^{-1}(\OOO)$.
1. Since $\lim x_n = x$, there exists $k \in \Nat$ such that
   $x_n \in B_X(x, \delta)$ for all $n > k$.
1. Thus, $x_n \in f^{-1}(\OOO)$ for all $n > k$.
1. Thus, $f(x_n) \in \OOO$ for all $n > k$.
1. i.e., for every $r > 0$, there exists $k \in \Nat$ such that
   $f(x_n) \in B_Y(f(x), r)$ for all $n > k$.
1. Thus, $\lim f(x_n) = f(x)$.


(3) $\implies$ (4). We will show that every point in $f(\closure A)$
belongs to $\closure f(A)$.

1. Let $A$ be a subset of $X$.
1. Let $y \in f(\closure A)$.
1. Then, there exists $x \in \closure A$ such that $y = f(x)$.
1. Since $x$ is a closure point of $A$, 
   there exists a sequence $\{ x_n \}$ of $A$ that converges to $x$.
1. Since $x_n \in A$, hence $f(x_n) \in f(A)$.
1. Thus, $\{ f(x_n) \}$ is a sequence of $f(A)$.
1. Since $\lim x_n = x$, hence, by (3), $\lim f(x_n) = f(x) = y$.
1. Thus, $y$ is a closure point of $f(A)$.
1. Thus, $y \in f(\closure A) \implies y \in \closure f(A)$.
1. Thus, $f(\closure A) \subseteq \closure f(A)$.


(4) $\implies$ (5)

1. Let $C$ be a closed subset of $Y$.
1. Thus, $C = \closure C$.
1. Let $A = f^{-1}(C)$.
1. Using (4), $f(\closure A) \subseteq \closure f(A) = \closure C = C$.
1. Thus, $\closure A \subseteq f^{-1}(C) = A$. 
1. Since $A \subseteq \closure A$ always, hence $A = \closure A$.
1. Thus, $A = f^{-1}(C)$ is a closed subset of $X$.

(5) $\implies$ (1). We will show that $f$ is continuous 
at any $x \in X$.

1. Let $a \in X$. Let $\epsilon > 0$.
1. Consider the open ball $B_Y(f(a), \epsilon)$.
1. Consider the closed set $C = Y \setminus B_Y(f(a), \epsilon)$.
1. $C$ can be written as:

   $$
   C = \{y \in Y \ST \rho(f(a), y) \geq \epsilon \}.
   $$
1. Using (5), $f^{-1}(C)$ is closed in $X$.
1. Since $f(a) \notin C$, hence $a \notin f^{-1}(C)$.
1. Thus, $a \in X \setminus f^{-1}(C)$ which is an open subset of $X$.
1. Thus, there exists $\delta > 0$ such that 
   $B_X(a, \delta) \subseteq X \setminus f^{-1}(C)$.
1. Note that $x \in X \setminus f^{-1}(C)$ implies that 
   $\rho(f(a), f(x)) < \epsilon$. 
   For if $\rho(f(a), f(x)) \geq \epsilon$ then $f(x) \in C$ then $x \in f^{-1}(C)$.
1. Thus, $x \in B_X(a, \delta)$ implies that $f(x) \in B_Y(f(a), \epsilon)$.
1. Thus, for every $\epsilon > 0$, there exists $\delta > 0$ such that
   $d(x, a) < delta$ implies $\rho(f(x), f(a)) < \epsilon$.
1. Thus, $f$ is continuous at $a$.
1. Since $a$ is arbitrary, hence $f$ is continuous on $X$.
```

```{prf:proposition}
{prf:ref}`Composition <def-st-total-function-composition>` 
of continuous (total) functions is continuous. 
```

```{prf:proof}
Let $(X_1, d_1), (X_2, d_2), (X_3, d_3)$ be metric spaces.
Let $f: X_1 \to X_2$ and $g: X_2 \to X_3$ be continuous.
Define $h : X_1 \to X_3$ as $h = g \circ f$.

Let $\{ x_n \}$ be a sequence of $X_1$.

1. Then, $\{y_n = f(x_n)\}$ is a sequence of $X_2$.
1. And, $\{z_n = g(y_n)) \}$ is a sequence of $X_3$.

Assume that $\lim x_n = x$. Let $y = f(x)$ and $z = g(y)$.

1. Since $f$ is continuous, 
   hence $\lim x_n =x  \implies \lim y_n = y$
   due to {prf:ref}`res-ms-continuous-function-characterization`.
1. Since $g$ is continuous, hence 
   $\lim y_n = y \implies \lim z_n = z$.
1. Thus, $\lim x_n = x \implies \lim z_n = z$.
1. Since this is valid for any convergent sequence of $X$, 
   $g \circ f$ is continuous;
   again due to {prf:ref}`res-ms-continuous-function-characterization`.
```

## Homeomorphism

```{prf:definition} Homeomorphism
:label: def-ms-homeomorphism

Two metric spaces $(X,d)$ and $(Y, \rho)$ are called *homeomorphic*
if there exists a bijective function $f : X \to Y$ such that
$f$ and $f^{-1}$ are both continuous.
Such a mapping $f$ is called a *homeomorphism*.
```

Procedure to show that two metric spaces are homeomorphic:

1. Pick a suitable bijective function $f : X \to Y$.
1. Show that $f$ is continuous.
1. Show that $f^{-1}$ is continuous.


## Equivalent Metrics

```{prf:definition} Metric equivalence
:label: def-ms-equivalent-metric

Let $d_1$ and $d_2$ be two different metrics on $X$. 
We say that $d_1$ and $d_2$ are equivalent if 
a sequence $\{ x_n \}$ of $X$ satisfies 
$\lim d_1(x_n, x) = 0$ if and only if $\lim d_2(x_n, x) = 0$.

In other words, two metrics are equivalent if they
lead to same convergent sequences with identical limits.
```

Procedure to show that two metrics are equivalent.

* Choose an arbitrary sequence $\{x_n\}$ which converges
  in $(X, d_1)$ to a limit  (say $x$). 
* Show that $\lim d_2(x_n, x) = 0$.
* Now, choose an arbitrary sequence $\{x_n\}$ which converges
  in $(X, d_2)$ to a limit  (say $x$). 
* Show that $\lim d_1(x_n, x) = 0$.


```{prf:proposition}
:label: res-ms-equivalent-metric-homeomorphic-identity

Two metrics $d_1$ and $d_2$ on $X$ are equivalent if 
and only if the identity mapping 
$I : (X, d_1) \to (X, d_2)$ given by 

$$
I (x) = x \Forall x \in X
$$

is a homeomorphism.
```

```{prf:proof}
Identity function is the inverse of itself.

Let $\{x_n \}$ be a sequence of $X$.

Assume that the two metrics are equivalent. 

1. Then, $\lim d_1(x_n, x) = 0 \iff \lim d_2(x_n, x) = 0$.
1. Thus, if $\lim d_1(x_n, x) = 0$ then 
   $\lim d_2(x_n, x) = \lim d_2(I(x_n), I(x)) = 0$ means that 
   $I$ is continuous.
1. Similarly, if $\lim d_2(x_n, x) = 0$ then 
   $\lim d_1(x_n, x) = \lim d_1(I^{-1}(x_n), I^{-1}(x)) = 0$
   means that $I^{-1}$ is continuous.
1. Thus, $I$ is a homeomorphism.


Assume that $I$ is a homeomorphism.

1. $I$ is continuous. Hence $\lim d_1(x_n, x) = 0$ implies 
   $\lim d_2(I(x_n), I(x)) = d_2(x_n, x) = 0$.
1. $I^{-1}$ is continuous. Hence $\lim d_2(x_n, x) = 0$ implies 
   $\lim d_1(I^{-1}(x_n), I^{-1}(x)) = d_1(x_n, x) = 0$.
1. Hence, the metrics $d_1$ and $d_2$ are equivalent.
```