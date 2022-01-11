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

Recall that the 
{prf:ref}`diameter <def-ms-diameter>` of a set
is defined to be the supremum of distances between
all pairs of points of the set.

```{prf:theorem}
Let $(X, d)$ be a complete metric space. 
Let $\{A_n\}$ be a sequence of closed, nonempty subsets of $X$ such that
$A_{n+1} \subseteq A_{n}$ for each $n$ and 

$$
\lim_{n \to \infty} \diam A_n = 0.
$$

Then the intersection $\bigcap_{n=1}^{\infty}A_n$ consists of precisely one point.
```
This result is due to G. Cantor. 
A similar result was seen in 
{prf:ref}`nested interval property<res-rl-nested-interval-property>` for real line.

```{prf:proof}

Define:

$$
A = \bigcap_{n=1}^{\infty}A_n.
$$

We shall first prove that $A$ cannot have more than one point.

1. Assume $x, y \in A$.
1. Thus, $x,y \in A_n \Forall n$.
1. Thus, $0 \leq d(x,y) \leq \diam A_n \Forall n$.
1. But then, $\lim_{n \to \infty} \diam A_n = 0$ implies that $d(x, y) = 0$.
1. But, $d(x,y) = 0 \implies x = y$ as $d$ is a metric (Identity of indiscernibles).
1. Thus, if $x,y \in \bigcap_{n=1}^{\infty}A_n$, then $x=y$.
1. Thus, $A$ contains at most one point.

We now show that $A$ cannot be empty.

1. For each $n$ choose $x_n \in A_n$. It is possible due to
   {prf:ref}`axiom of choice <ax-st-axiom-of-choice>`. 
1. Since $A_{n+p} \subseteq A_n$, 
   hence $d(x_{n+p}, x_n) \leq \diam A_n$ holds for every $n, p$.
1. Thus, $\{x_n\}$ is a Cauchy sequence of $X$.
1. Since $X$ is complete, $\{x_n\}$ is convergent.
1. Hence, the limit $x = \lim_{n\to\infty} x_n$ exists and $x \in X$.
1. Since $x_m \in A_n$ for all $m \geq n$, 
   hence $x$ is a closure point of $A_n$ for each $n$ 
   ({prf:ref}`res-ms-closure-point-as-limit`).
1. But since $A_n$ is closed, hence $x \in A_n$ for each $n$.
1. Thus, $x \in A$.
```

## Nowhere Dense Sets

```{prf:definition} Nowhere dense
:label: def-ms-nowhere-dense-set

A subset $A$ of $(X,d)$ is *nowhere dense* if its closure 
has an empty interior; i.e., 

$$
\interior \closure A = \EmptySet.
$$
```

```{prf:remark}
$A$ is nowhere dense if and only if $X \setminus (\closure A)$ 
is dense in $X$.
```
```{prf:proof}
Let $B = \closure A$.

Recall from {prf:ref}`res-ms-int-cl-comp-rel` that:

$$
\begin{aligned}
&X \setminus (\interior B) = \closure (X \setminus B)\\
\iff & \interior B = X \setminus (\closure (X \setminus B)).
\end{aligned}
$$

Now,

$$
\begin{aligned}
& \interior \closure A = \EmptySet \\
\iff & \interior B = \EmptySet \\
\iff & X \setminus (\closure (X \setminus B)) = \EmptySet\\
\iff & \closure (X \setminus B) = X\\
\iff & \closure (X \setminus (\closure A)) = X\\
\iff & X \setminus (\closure A) \text{ is dense in $X$}.
\end{aligned}
$$
```

```{prf:example}
The set of integers $\ZZ$ is nowhere dense in $\RR$.
```


## Cantor Set

```{prf:definition} Cantor set
:label: def-ms-cantor-set

*Cantor set* $C$ is a subset of $[0,1]$. It is constructed as follows:

1. Let $C_0 = [0,1]$. 
1. Trisect $C_0$  into 
   $[0, \frac{1}{3}], (\frac{1}{3}, \frac{2}{3}) , [\frac{2}{3}, 1]$.
1. Remove the middle open interval $(\frac{1}{3}, \frac{2}{3})$ and
   form $C_1 = [0, \frac{1}{3}]\cup [\frac{2}{3}, 1]$.
1. Note that $C_1$ is a disjoint union of $2=2^1$ closed intervals.
1. Trisect each closed interval of $C_1$ and remove the middle 
   open interval from each one of the trisections in an identical manner.
1. Let $C_2 = [0, \frac{1}{9}] \cup [\frac{2}{9}, \frac{1}{3}] \cup [\frac{2}{3}, \frac{7}{9}] \cup [\frac{8}{9}, 1]$.
1. Note that $C_2$ is a union of $4=2^2$ disjoint closed intervals 
   each of length $\frac{1}{9} = \frac{1}{3^2}$.
1. Inductively build $C_{n+1}$ from $C_n$ using this procedure. 
1. Note that $C_n$ is a union of $2^n$ disjoint closed intervals 
   of length $\frac{1}{3^n}$ each.
1. When $C_{n+1}$ is constructed from $C_n$, we get $2^{n+1}$ 
   disjoint intervals of length $\frac{1}{3^{n+1}}$ each.
1. Clearly $C_{n+1} \subseteq C_{n}$ by construction for all $n$.
1. Define the Cantor set as:

   $$
   C \triangleq \bigcap_{n=1}^{\infty} C_n.
   $$
```

We next discuss different properties of the Cantor set.

```{prf:property} Characterization in ternary expansions
:label: res-ms-cantor-set-ternary-expansion


Consider the set $E \subset [0,1]$ whose 
every element has a ternary (base 3) expansion
of only 0s and 2s; i.e., for every $x \in E$, we have a representation:

$$
x = .d_1 d_2 d_3 \dots  \text{ where } d_i \in \{0, 2 \}
$$

Then, $E=C$. In other words:

$$
C = E \triangleq \left \{ \sum_{n=1}^{\infty} \frac{d_n}{3^n}, 
\text{ where } d_n \in \{ 0, 2\} \right \}.
$$

```

```{prf:proof}
In the ternary (base 3), representation, each number $x\in[0, 1]$
can be written as:

$$
x = .d_1 d_2 d_3 \dots  \text{ where } d_i \in \{0, 1, 2 \}
$$

such that

$$
x = \sum_{i=1}^{\infty} \frac{d_i}{3^i}.
$$

For example

$$
1 = .2222222... = 2 \sum_{i=1}^{\infty} \frac{1}{3^i} 
= 2\frac{1/3}{2/3} = 2\frac{1}{2} = 1.
$$

It is possible that a number has two different ternary expansions.
We can see that $\frac{1}{3} \in C_k$ for every $k$. 
Hence, $\frac{1}{3} \in C$.Interestingly, 

$$
\frac{1}{3} = .1  = .022222... .
$$
has two different ternary representations. 
One is a finite representation, and the other
is an infinite representation involving only 0s and 2s.
We say that $\frac{1}{3} \in C$ as it has a ternary 
representation consisting of only 0s and 2s.

We have to prove two things:

1. $E \subseteq C$. Every number in $[0,1]$ which has a ternary expansion 
   containing only 0s and 2s belongs to $C$.
1. $C \subseteq E$. Every number in $C$ has a ternary expansion
   containing only of 0s and 2s.


Note that if $A = [a, a + \frac{1}{3^n}]$ is a closed interval contained in $C_n$
then:

1. $[a, a + \frac{1}{3^{n+1}}]$ is the first closed interval drawn from $A$ in $C_{n+1}$.
1. $[a+ \frac{2}{3^{n+1}}, a + \frac{1}{3^{n}}]$ is the second closed interval drawn from $A$ in $C_{n+1}$.


$E \subseteq C$

1. Let $x = .d_1 d_2 \dots$ with $d_i \in \{0, 2\}$.
1. Start with $A_0 = [0,1]$.
1. Given $A_0$:
   1. If $d_1 = 0$, then let $A_1$ be the first closed interval drawn from $A_0$ : $[0, \frac{1}{3}]$ contained in $C_1$.
   1. Otherwise, if $d_1 = 2$, then let $A_1$ the second closed interval drawn from $A_0$ : $[\frac{2}{3}, 1]$ contained in $C_1$.
1. Given $A_{n-1} = [a, a + \frac{1}{3^{n-1}}]$, 
   1. If $d_n = 0$, then let $A_n$ be the first closed interval drawn from $A_{n-1}$ contained in $C_n$.
   1. Otherwise (if $d_n = 2$), then let $A_n$ be the second closed interval drawn from $A_{n-1}$ contained in $C_n$. 
1. Inductively, we can keep picking closed interval $A_n$ contained in $C_n$ 
   for every digit in the ternary expansion of $x$.
1. Thus, $x \in C$.

$C \subseteq E$

1. For every $x \in C$, we can construct a ternary expansion as follows.
1. If $x \in [0, \frac{1}{3}]$, then $d_1 = 0$.
1. Otherwise if $x \in [\frac{2}{3}, 1]$, then $d_1 = 2$.
1. Subsequently, whenever the first closed interval is chosen, then $d_n = 0$
   and whenever the second closed interval is chosen, then $d_n = 2$.
1. Thus, $x$ has a ternary expansion consisting entirely of 0s and 2s.
1. Thus, $x \in E$.
```

```{prf:property}
Cantor set doesn't contain any open interval.
```
```{prf:proof}
Note that the total length of disjoint closed intervals in $C_n$ is
$\frac{2^n}{3^n} = \left ( \frac{2}{3} \right )^n$.

1. Assume that there is an open interval $(a,b) \subseteq C$.
1. Then, the length of the interval is $b-a > 0$.
1. But then there exists an $n$ such that $\left ( \frac{2}{3} \right )^n < b - a$.
1. Then, for all $k \geq n$, $(a,b)$ cannot be contained in $C_k$.
1. We arrive at a contradiction.
```

```{prf:property}
Cantor set has an empty interior.
```
```{prf:proof}
Assume $C$ has a nonempty interior and $x \in \interior C$.

1. Then there is a neighborhood $(x - \epsilon , x + \epsilon) \subset C$.
1. But, $C$ doesn't contain any open intervals.
1. We arrive at a contradiction.

Thus, $C$ has an empty interior.

```

```{prf:property}
Cantor set is a closed nowhere dense subset of $\RR$.
```
```{prf:proof}
$C$ is an (infinite) intersection of closed sets. Hence $C$ is closed. $\closure C = C$.
$C$ has an empty interior. Thus, $C$ is nowhere dense.
```

```{prf:property}
The total length of the removed intervals from $[0,1]$ to get $C$ equals 1.
```

```{prf:proof}
At the n-th step, we remove $2^{n-1}$ open intervals of length $3^{-n}$ each.

Thus, total length removed in n-th step is $\frac{1}{2} \left ( \frac{2}{3} \right )^n$.

Thus, total length removed is:

$$
\sum_{n=1}^{\infty} \frac{1}{2} \left ( \frac{2}{3} \right )^n 
= \frac{1}{2} \frac{2/3}{1 - 2/3} = 1.
$$
```


```{prf:property}
Cantor set is uncountable. In particular:

$$
\card {C} = \card {2^{\Nat}} = \card{\RR} = \mathfrak{c}.
$$
```
Recall that $\mathfrak{c}$ denotes the cardinality of the
continuum ({prf:ref}`def-cardinality-continuum`). 
The notation $2^{\Nat}$ was introduced in
{prf:ref}`res-st-power-set-binary-func` to describe power sets.
{prf:ref}`res-st-real-line-cardinality` established that

$$
2^{\Nat} \sim \Power(\Nat) \sim \RR.
$$

```{prf:proof}
Recall that two sets are called {prf:ref}`equivalent <def-st-equivalent-sets>`
($A \sim B$) if there is a bijective mapping between them.

Recall from {prf:ref}`res-ms-cantor-set-ternary-expansion` that:

$$
C = \left \{ \sum_{n=1}^{\infty} \frac{d_n}{3^n}, 
\text{ where } d_n \in \{ 0, 2\} \right \}.
$$
1. Thus, each $x \in C$ can be identified with a sequence $d : \Nat \to \{ 0, 2\}$
   given by $d = \{ d_n \}$. 
1. Thus, we have a bijective mapping between $C$ and the set $\{0, 2\}^{\Nat}$.
1. Thus, $C \sim \{0, 2\}^{\Nat}$.
1. This, in turn can be identified with a sequence $c : \Nat \to \{0, 1\}$ 
   where $c = \{ c_n \}$ with $c_n = 0$ if $d_n = 0$ and $c_n = 1$ if $d_n = 2$.
1. This gives us a bijective mapping between $\{0, 2\}^{\Nat}$ and $\{0, 1\}^{\Nat}$.
1. Recall that $2^{\Nat} = \{0, 1\}^{\Nat}$ with 
   $2 = \{0, 1\}$ ({prf:ref}`res-st-power-set-binary-func`).
1. Thus $C \sim  2^{\Nat}$ and 

   $$
   \card C = \card 2^{\Nat} = \card \RR = \mathfrak{c}.
   $$
```