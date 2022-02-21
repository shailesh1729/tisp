(sec:ms:continuity)=
# Functions and Continuity
The material in this section is primarily based on
{cite}`aliprantis1998principles,gopal2020introduction`.


Let $(X,d)$ and $(Y, \rho)$ be metric spaces.

Recall that for a function $f: (X,d) \to (Y, \rho)$:

1. If $f$ is a {prf:ref}`partial <def-st-function>`
   function, then $\dom f \subseteq X$.
1. If $f$ is a {prf:ref}`total <def-st-total-function>`
   function, then $\dom f = X$. 

We will primarily focus on total functions while
some definition and results are valid for partial functions too.

## Open and Closed Mappings

```{prf:definition} Open mapping
:label: def-ms-open-mapping

A (total) function $f : (X, d) \to (Y, \rho)$ is called 
an *open mapping* if $f(A)$ is open whenever $A$ is open.

In other words, $f$ maps open sets to open sets.
```

```{prf:definition} Closed mapping
:label: def-ms-closed-mapping

A (total) function $f : (X, d) \to (Y, \rho)$ is called 
a *closed mapping* if $f(A)$ is closed whenever $A$ is closed.

In other words, $f$ maps closed sets to closed sets.
```

## Bounded Functions

```{prf:definition} Bounded functions
:label: def-ms-bounded-function

A (total) function $f : (X, d) \to (Y, \rho)$ is called 
a *bounded* if its image $f(X)$ is 
{prf:ref}`bounded <def-ms-boundedness-set>` (in the metric space sense).

In other words, there exists a number $M > 0$ such that

$$
\rho(f(x), f(y)) \leq M \Forall x, y \in X.
$$
```
Compare this definition with the definition for
bounded real valued functions in {prf:ref}`def-bra-bounded-function`.

## Continuous Functions


```{prf:definition} Continuous function
:label: def-ms-continuous-function

A function $f: X \to Y$ between the two metric spaces
is said to be *continuous at a point* $a \in \dom f$ 
if for every $\epsilon > 0$, there exists $\delta > 0$
(depending on $\epsilon$ and $a$) such that
for all $x \in \dom f$

$$
d(x, a) < \delta \implies \rho (f(x), f(a)) < \epsilon
$$
holds true.

$f$ is said to be *continuous* on $A \subseteq \dom f$ if $f$ is continuous
at every point of $A$.
```

In other words, there is an open ball $B_X(a, \delta)$ 
around $a$ 
which maps within the open ball $B_Y(f(a), \epsilon)$ around $f(a)$.

The "continuity at a point" definition above is valid for 
both partial and total functions.

1. If $a$ is an isolated point in $\dom f$, then $f$ is continuous
   at $a$. 
1. If $a$ is an accumulation point in $\dom f$ then, 
   $\lim_{x \to a} f(x) = f(a)$ must hold true for $f$ to be
   continuous at $x=a$. 

```{prf:remark}
If $f$ is continuous on $A$ then $A \subseteq \dom f$.
If $f$ is continuous on $X$ then $\dom f = X$.
```

```{note}
If $f : (X,d) \to (Y, \rho)$ is not defined for all of $X$, then
we can consider the restriction of $f$ to $A  =\dom f$
and work with $\tilde{f}: (A,d) \to (Y, \rho)$ given by 
$\tilde{f}(x) = f(x) \Forall x \in A$
where $(A,d)$ is a metric subspace of $(X, d)$. 
Then $f'$ is a total function.
```

```{prf:example} Distance from a set
:label: ex-ms-cont-set-distance

Recall from {prf:ref}`def-ms-point-set-distance`
that the distance from a nonempty set $A \subseteq X$ of any point $x\in X$ 
is defined as:

$$
d(x, A) = \inf \{ d(x,a) \Forall a \in A \}.
$$

If we fix $A$, then we can define a function 
$d_A : X \to \RR$ as:

$$
d_A(x) = d(x, A).
$$
The function is well defined since the set 
$\{ d(x,a) \Forall x \in A \}$ is bounded from below
and thus has a unique greatest lower bound.

We now show that $d_A$ is continuous.

We first establish some basic inequalities.
For any $x,y \in X$ and $a \in A$ we have:

$$
d(a,x) \leq d(a,y) + d(x,y)
$$

Thus, 

$$
d(a, y) \geq d(a, x) - d(x,y).
$$
Since $d(a,x) \geq d_A(x)$, we get:

$$
d(a,y) \geq d_A(x) - d(x,y).
$$

Since this inequality is valid for every $a \in A$, taking the
infimum on the L.H.S, we get:

$$
d_A(y) \geq d_A(x) - d(x,y) \iff d_A(x) - d_A(y) \leq d(x,y).
$$

Interchanging $x$ with $y$, we get:

$$
d_A(y) - d_A(x) \leq d(y, x) = d(x,y).
$$

Combining the two, we get:

$$
|d_A(x)  - d_A(y)| \leq d(x,y).
$$

Now for any $\epsilon > 0$, choosing $\delta = \epsilon$, we get that

$$
d (x, y) < \delta \implies |d_A(x)  - d_A(y)| < \delta = \epsilon.
$$

Hence, $d_A$ is continuous on $X$.
```

## Continuity Characterization

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

```{prf:theorem}
:label: res-ms-cont-func-cl-f-cl-a-eq-cl-f-a

Let $f: X \to Y$ be a continuous function between two metric spaces.
Let $A \subseteq X$. Then,

$$
\closure f(\closure A) = \closure f(A).
$$
```

```{prf:proof}
Since $f$ is continuous, hence by {prf:ref}`res-ms-continuous-function-characterization` (4)

$$
f(\closure A) \subseteq \closure f(A).
$$

Now, $\closure f(A)$ is a closed set. Hence,
due to {prf:ref}`res-ms-closed-superset-closure-superset`

$$
\closure f(\closure A) \subseteq \closure f(A).
$$

Now, note that:

$$
f(A) \subseteq f(\closure A)
$$
since $A \subseteq \closure A$.

But then, taking closure on both sides, we get:

$$
\closure f(A) \subseteq \closure f(\closure A).
$$

Combining the inclusions, we obtain:

$$
\closure f(\closure A) = \closure f(A).
$$
```

```{prf:theorem} Continuity and composition
:label: res-ms-cont-func-composition

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

```{prf:theorem} Level sets of continuous functions
:label: res-ms-level-set-cont-func

Let $f: X \to Y$ be a continuous function between two metric spaces.
Then, the level sets of $f$ given by

$$
A_y = \{x \in X \ST f(x) = y \}
$$
are closed.
```

```{prf:proof}
By definition:

$$
A_y = f^{-1}(\{ y \}).
$$

Now, $\{ y \}$ is a singleton set in $Y$, hence closed in $Y$
due to {prf:ref}`res-ms-singleton-closed`.

Then, by {prf:ref}`res-ms-continuous-function-characterization` (5), 
$f^{-1}(\{ y \})$ is closed. 
```

## Discontinuity

```{prf:definition} Discontinuity
:label: def-ms-point-discontinuity

A function $f: X \to Y$ between the two metric spaces
is said to be *discontinuous at a point* $a \in \dom f$ 
if there exists $\epsilon > 0$, such that
for every $\delta > 0$
there exists $x \in \dom f$
with $d(x, a) < \delta$ and $\rho (f(x), f(a)) \geq \epsilon$. 
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


```{prf:theorem}
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


## Uniform Continuity

```{prf:definition} Uniform continuity
:label: def-ms-uniform-continuity

A function $f: (X, d) \to (Y, \rho)$ between two
metric spaces is called *uniformly continuous* on $A \subseteq \dom f$
if for every $\epsilon > 0$, there exists some $\delta > 0$
(depending on $\epsilon$) such that

$$
\rho(f(x), f(y)) < \epsilon \text{ whenever } d(x, y) < \delta \text{ and } x, y \in A.
$$
```

```{prf:remark}
If $f$ is uniformly continuous on $A \subseteq \dom f$, then $f$ is continuous on $A$.
```

For real valued functions, the standard metric on $\RR$ is
$d(x,y) = |x - y|$. The uniform continuity definition
simplifies accordingly as:

```{prf:remark} Uniform continuity for real valued functions
:label: def-ms-uniform-cont-real-valued

A real valued function $f: (X, d) \to \RR$ is called 
*uniformly continuous* on $A \subseteq \dom f$
if for every $\epsilon > 0$, there exists some $\delta > 0$
(depending on $\epsilon$) such that

$$
|f(x) - f(y)| < \epsilon 
\text{ whenever } d(x, y) < \delta \text{ and } x, y \in A.
$$
```


## Isometry

```{prf:definition}
:label: def-ms-isometry

A function $f : (X, d) \to (Y, \rho)$ is an isometry if 
for all $x, y \in \dom f$,  we have:

$$
\rho(f(x), f(y)) = d(x, y).
$$
```

```{prf:theorem}
:label: res-ms-isometry-one-one
Any isometry is injective.
```
```{prf:proof}

We proceed as follows:

1. Let $f$ to be an isometry from $(X, d)$ to $(Y, \rho)$.
1. Let $x_1, x_2 \in \dom f$ with $x_1 \neq x_2$.
1. Then, $d(x_1, x_2) > 0$ since $d$ is a metric. 
1. Since $f$ is an isometry, hence
   $\rho(f(x_1), f(x_2)) = d(x_1, x_2) > 0$.
1. Thus, $f(x_1) \neq f(x_2)$ since $\rho$ is a metric.
1. Thus, $x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$.
1. Thus, $f$ is injective.
```

```{prf:theorem}
:label: res-ms-isometry-continuous

Any isometry between two metric spaces is uniformly continuous.
```

```{prf:proof}
Let $f$ be an isometry. Let $\epsilon > 0$. 
Choose $\delta = \epsilon$. Then, for any $x,y \in \dom f$,

$$
d(x,y) < \delta \implies \rho(f(x), f(y)) < \delta = \epsilon
$$
since $f$ is an isometry.
Thus, $f$ is uniformly continuous on $\dom f$.
```

```{prf:definition}
:label: def-ms-isometric-spaces

Two metric spaces $(X, d)$ and $(Y, \rho)$ are called
*isometric* if there exists an isometry 
$f : X \to Y$ such that $\dom f = X$ and $\range f = Y$.

Such an isometry is bijective.
```


```{prf:theorem}
:label: res-ms-isometric-homeomorphic

Two metric spaces which are isometric are necessarily
homeomorphic. 
```

```{prf:proof}
Let $(X,d)$ and $(Y, \rho)$ be isometric.
Then, there exists an isometry $f$ from $X$ to $Y$
which is bijective. 
Since $f$ is an isometry, it is continuous. 
It is easy to see that $f^{-1}$ is also 
an isometry and is continuous. 
Thus, the metric spaces are homeomorphic.
```


## Bounded Metric

This section is dedicated to the development of 
a bounded metric on any metric space.

```{prf:theorem} Bounded metric
:label: res-ms-bounded-metric

If $d$ is a metric on a set $X$, then the function
$\rho$ given by

$$
\rho(x, y) = \frac{d(x,y)}{1 + d(x,y)}
$$

is also a metric on $X$. Besides, $(X, \rho)$ is 
{prf:ref}`bounded <def-ms-boundedness-space>` and 
$\rho$ is {prf:ref}`equivalent <def-ms-equivalent-metric>`
to $d$.
```

We structure the proof into three parts:

1. Show that $\rho$ is a metric.
1. Show that $(X, \rho)$ is bounded.
1. Show that $\rho$ and $d$ are equivalent.

```{prf:proof} 
$\rho$ is a
{prf:ref}`metric <def-ms-distance-function>`.

(1) Non-negativity: Since $d(x,y) \geq 0$, hence $\rho(x, y) \geq 0$
as it is a ratio of a non-negative number with a positive number.

(2) Identity of indiscernibles:

1. Assume $\rho(x, y) = 0$. 
1. Then $d(x,y)=0$. 
1. Thus $x=y$ since $d$ is a metric.
1. Now, assume $x=y$. 
1. Then $d(x,y)=0$.
1. Thus, $\rho(x,y)=0$. 


(3) Symmetry:

$$
\rho(y, x) = \frac{d(y,x)}{1 + d(y,x)} = \frac{d(x,y)}{1 + d(x,y)} = \rho(x, y).
$$


(4) Triangle inequality. This will require some work.

Consider the function $f: \RR \to \RR$:

$$
f(t) = \frac{t}{1+t}
$$
with $\dom f = \RR_+$.


Its derivative is 

$$
f'(t) = \frac{1}{(1+t)^2}.
$$

$f'(t) \geq 0$ for $t \in \RR_+$. Thus, $f$ is an increasing function
on $t \geq 0$. In particular:

$$
d(x, y)\leq d(x, z) + d(z, y) \implies f(d(x,y)) \leq f(d(x, z) + d(z, y)).
$$

Now, we proceed as follows:

$$
\begin{aligned}
\rho(x, y) &= f(d(x,y)) \\
&\leq f(d(x, z) + d(z, y))\\
&= \frac{d(x, z) + d(z, y)}{1 + d(x, z) + d(z, y)}\\
&= \frac{d(x, z)}{1 + d(x, z) + d(z, y)} + \frac{d(z, y)}{1 + d(x, z) + d(z, y)}\\
&\leq \frac{d(x, z)}{1 + d(x, z)} + \frac{d(z, y)}{1 + d(z, y)}\\
&= \rho(x,z) + \rho(z,y).
\end{aligned}
$$
```

```{prf:proof} 
$\rho$ is a bounded

It is easy to see that

$$
\sup \rho(x, y) = 1.
$$

Thus, $(X, \rho)$ is bounded.
```

```{prf:proof} $\rho$ is equivalent to $d$

We first show that the identity mapping $I : (X, d) \to (X, \rho)$ is continuous.

Let $a \in X$ and choose $\epsilon > 0$. 
Recall that $\rho$ is bounded with $\rho(x,y) < 1$. 

Thus, if $\epsilon \geq 1$, we can choose any $\delta > 0$ leading 
to $\rho(x,y) < \epsilon$  whenever $d(x,y) < \delta$.

Now, consider the case $\epsilon < 1$.

$$
\begin{aligned}
&\rho(x, a) < \epsilon\\
&\iff \frac{d(x,a)}{1 + d(x,a)} < \epsilon\\
&\iff 1 - \frac{d(x,a)}{1 + d(x,a)} > 1 - \epsilon\\
&\iff \frac{1}{1 + d(x,a)} > 1 - \epsilon\\
&\iff 1 + d(x, a) < \frac{1}{1 - \epsilon}\\
&\iff  d(x,a) < \frac{\epsilon}{1 - \epsilon}. 
\end{aligned}
$$

Now, choosing $\delta = \frac{\epsilon}{1 - \epsilon}$, we note that
$\delta > 0$ for $0 < \epsilon < 1$.

Thus, for every $\epsilon > 0$, there exists $\delta > 0$ 
such that $\rho(x, a) < \epsilon$ whenever $d(x, a) < \delta$.

Hence, $I$ is continuous. A similar argument also shows that
$I^{-1}$ is continuous.

Thus, $I$ is homeomorphism and the metric spaces 
$(X, d)$ and $(X, \rho)$ are homeomorphic. 

Hence, due to {prf:ref}`res-ms-equivalent-metric-homeomorphic-identity`,
the two metrics are equivalent.
```


