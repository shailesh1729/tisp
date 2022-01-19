# Completeness
The material in this section is primarily based on
{cite}`aliprantis1998principles,gopal2020introduction`.

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
:label: res-ms-closed-subset-complete 

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
:label: res-ms-complete-nested-closed-nonempty

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

```{prf:definition} Nowhere dense/Rare
:label: def-ms-nowhere-dense-set

A subset $A$ of $(X,d)$ is *nowhere dense* if its closure 
has an empty interior; i.e., 

$$
\interior \closure A = \EmptySet.
$$

It is also called a *rare* set.
```

```{prf:theorem}
:label: res-ms-complement-closure-rare-dense

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

```{prf:corollary}
:label: res-ms-open-dense-complement-rare

If a set is open and dense, then its complement is rare (nowhere dense).
```

```{prf:proof}
Let $A$ be open and dense. 

1. $B = X \setminus A$ is closed.
1. Thus, $\closure B = B$. 
1. Hence, $X \setminus (\closure B) = X \setminus B = A$.
1. But $A$ is dense, hence $B$ must be nowhere dense
   due to {prf:ref}`res-ms-complement-closure-rare-dense`.
```

```{prf:theorem}
:label: res-ms-rare-complement-dense

The complement of a rare (nowhere dense) set is dense.
```
```{prf:proof}
Let $A \subseteq X$ be rare (nowhere dense).

1. The interior of its closure is empty.
1. Thus, its closure $\closure A$ contains no open sets.
1. Thus, $A$ contains no open sets.
1. Thus, every open set in $X$ intersects with $X \setminus A$.
1. Thus, $X \setminus A$ is dense.
```

```{prf:proposition}
:label: res-ms-rare-subset-rare

The subset of a rare (nowhere dense) set is rare. 
```

```{prf:proof}
Let $A \subseteq B$ and $B$ be nowhere dense.
Now

$$
A \subseteq B \implies \closure A \subseteq \closure B
\implies \interior \closure A \subseteq \interior \closure B.
$$

Since $B$ is nowhere dense, hence $\interior \closure B$ is
empty. 
This in turn implies that $\interior \closure A$ is empty.
Thus, $A$ is nowhere dense.
```

```{prf:proposition}
:label: res-ms-boundary-closed-rare

The boundary of a closed set is nowhere dense (rare).
```

```{prf:proof}

Let $A$ be closed. Thus, $A = \closure A$.
Since $\boundary A = \closure A \setminus \interior A$,
hence $\boundary A \subseteq A$ for a closed set.

1. Assume $\boundary A$ has a nonempty interior.
1. Let $x$ be an interior point of $\boundary A$.
1. Since $x \in \boundary A \subseteq A$, hence $x$ is an interior point of $A$.
1. But boundary of $A$ doesn't includes its interior points.
1. Hence, a contradiction.
1. Thus, $\boundary A$ has an empty interior.
1. Finally $\interior \closure \boundary A$ = \interior \boundary A = \EmptySet$ 
   since $\boundary A$ is closed.
1. Thus, $\boundary A$ is rare.
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


## Meager Sets


```{prf:definition} Meager set
A union of countably many rare (nowhere dense) sets is said to be
of *first category* or a *meager* set.

In other words, a subset $A$  is called *meager* 
(or of *first category*) if there 
exists a sequence $\{ A_n \}$ of nowhere dense subsets such that

$$
A = \bigcup_{n=1}^{\infty} A_n.
$$
```

```{prf:definition} Co-meager set
The complement of a meager set is called *co-meager*.
```

```{prf:definition} Non-meager set
A subset that is not meager is said to be *non-meager*
or of *second category*.
```


```{prf:example}

Consider the metric space $\RR$.

1. Singleton sets are rare (nowhere dense) in $\RR$ as they are 
   closed and their interior is empty.
1. The set of natural numbers $\Nat$ is rare since it is closed 
   and its interior is empty (no open intervals in $\Nat$).
1. The set $\QQ$ is not rare since its closure is entire $\RR$.
   It is meager since it is a countable union of rare singleton sets.
1. The set of irrational numbers $\II$ is co-meager as $\II = \RR \setminus \QQ$.
1. The set $\RR$ is non-meager.  
```


```{prf:theorem}
The subset of a meager set is meager.
```
```{prf:proof}
Let $A$ be a meager set and let $B \subseteq A$. Then,

$$
A = \bigcup_{n=1}^{\infty} A_n
$$
where $A_n$ are rare (nowhere dense).

But then

$$
B = B \cap A = B \cap \bigcup_{n=1}^{\infty} A_n
= \bigcup_{n=1}^{\infty} A_n \cap B.
$$

Since subset of a nowhere dense set is nowhere dense,
hence $B_n = A_n \cap B$ are nowhere dense.
Hence

$$
B = \bigcup_{n=1}^{\infty} B_n
$$
is meager (as it is a countable union of nowhere dense sets).
```

```{prf:theorem}
The union of countably many meager sets is meager.
```
```{prf:proof}
Recall from {prf:ref}`res:st:countable-union-countable-sets`
that countable union of countable sets is countable.

1. Let $\{M_n\}$ be a countable collection of meager sets.
1. Then, each $M_n$ is a countable union of rare sets.
1. Write $M_n$ as $\bigcup_i A_{n, i}$.
1. Thus, 

   $$
   M = \bigcup_n M_n = \bigcup_n \bigcup_i A_{n, i}
   = \bigcup_{n, i} A_{n, i}.
   $$ 
1. The family $\{ A_{n, i} \}$ is countable.
1. Thus, $M$ is a countable union of rare sets.
1. Thus, $M$ is meager.
```

```{prf:corollary}
Since co-meager sets are complements of meager sets:

1. Superset of a co-meager set is co-meager.
1. Countable intersection of co-meager sets is co-meager.
```

## Baire Category Theorem


```{prf:theorem} Baire category theorem
:label: res-ms-baire-category-theorem

A (nonempty) complete metric space is non-meager in itself.
```

In other words:

* A (nonempty) complete metric space is not a countable union of rare sets.


```{prf:proof}

Our proof strategy is following:

1. For contradiction, we assume that $X$ is meager with $X = \bigcup_i A_i$. 
1. We form a Cauchy sequence from points $x_i \notin A_i$.
1. Since $X$ is complete, we claim its convergence $x = \lim x_i$.
1. We further show that the limit point $x$ cannot belong to any $A_i$.

Let us assume that $X$ is a complete metric space which is 
meager in itself; i.e., there exists a countable collections
of rare sets (rare in $X$) such that $X$ is their union.

$$
X = \bigcup_{k=1}^{\infty} A_k
$$
where $A_k$ are rare (nowhere dense); i.e. $\interior \closure A_k = \EmptySet$.

Recall from {prf:ref}`res-ms-complement-closure-rare-dense` that 
$B_k = X \setminus \closure A_k$ are dense in $X$.
Also, $B_k$ are open since they are complement of closed sets.
Also, recall from {prf:ref}`res-ms-dense-open-intersect`
that a dense set has a nonempty intersection with every nonempty open set.


1. $B_1 = X \setminus \closure A_1$ is a nonempty open set.
1. Thus, there exists an interior point $x_1$ in $B_1$ with
   an open ball $B(x_1, \epsilon_1) \subseteq B_1$ 
   where we can make $\epsilon_1 < \frac{1}{2}$.
1. $B_2$ is nonempty, open and dense. 
   Thus, $C_2 = B_2 \cap B\left (x_1, \frac{\epsilon_1}{2}\right)$ is nonempty and open.
1. Thus, we can choose $x_2 \in C_2$ such that
   $x \in B(x_2, \epsilon_2) \subseteq C_2$ with $\epsilon_2 \leq \frac{\epsilon_1}{2}$.
1. Proceeding inductively in this manner, we obtain a sequence $\{ x_n \}$ such that
   
   $$
   x_n \in B(x_n, \epsilon_n) \subseteq B_n \cap 
   B\left (x_{n-1}, \frac{\epsilon_{n-1}}{2} \right).
   $$
1. We have $A_n \cap B(x_n, \epsilon_n) = \EmptySet$. 
   $\epsilon_n \leq \frac{\epsilon_{n-1}}{2}$ with $\epsilon_1 < \frac{1}{2}$.
1. By definition, $x_m \in B\left (x_n, \frac{\epsilon_n}{2} \right)$ for every $m > n$.
1. Thus, $d(x_m, x_n) < \frac{\epsilon_n}{2}$ for every $m > n$.
1. Since $\epsilon_1 < \frac{1}{2}$, hence $\epsilon_n < \frac{1}{2^{n+1}}$.
1. Thus, $d(x_m, x_n) \to 0$ as $m,n \to \infty$. 
1. Thus, $\{x_n\}$ is a Cauchy sequence.
1. Since $X$ is complete, hence every Cauchy sequence is convergent. 
1. Thus there exists $x \in X$ such that $x = \lim x_n$. 
   To which $A_k$ does $x$ belong then?
1. Fix some $n \in \Nat$. For every $m>n$ we have:

   $$
   d(x, x_n) \leq d(x, x_m) + d(x_n, x_m) < d(x, x_m) + \frac{\epsilon_n}{2}.
   $$
1. Thus taking the limit $m \to \infty$ leading to $d(x, x_m) \to 0$, 
   we get 

   $$
   d(x, x_n) \leq \frac{\epsilon_n}{2} < \epsilon_n.
   $$
1. Hence $x \in B(x_n, \epsilon_n)$ for all $n \in \Nat$.
1. Since $A_n \cap B(x_n, \epsilon_n) = \EmptySet$, hence $x \notin A_n$ for all $n$.
1. But then $x \notin X$ since $X = \bigcup_n A_n$. A contradiction.
1. Hence, $X$ must be non-meager.
```

```{prf:theorem}
If $(X, d)$ is complete and $X = \bigcup_{n=1}^{\infty} A_n$,
then at least one $A_n$ is non-rare; i.e.,
$\interior \closure A_n \neq \EmptySet$ for some $n$.
```

```{prf:proof}
If every $A_n$ were rare, then $X$ would be a meager set.
But as per {prf:ref}`Baire category theorem <res-ms-baire-category-theorem>`,
$X$ must be non-meager since it is complete. 

Hence, at least one $A_n$ would be non-rare.
```

```{prf:proposition}
The set of irrational numbers is non-meager.
```

```{prf:proof}
Recall that $\RR = \QQ \cup \II$ where $\II$ is the set of irrational numbers.

1. $\RR$ is complete. Hence $\RR$ is non-meager.
1. $\QQ$ is meager as it is a countable union of singletons which are rare sets.
1. Countable union of meager sets is meager.
1. Thus, if $\II$ was meager, then $\RR$ would be meager which is not true.
1. Hence, $II$ must be non-meager.
```


```{prf:theorem} Interior of a meager set
:label: res-ms-complete-meager-interior-empty

A meager set has an empty interior in a complete metric space.
```

```{prf:proof}
Let $M \subseteq X$ be meager. Then, we can write $M$ as

$$
M = \bigcup_{n=1}^{\infty} A_n
$$
such that $A_n$ are rare in $X$.


Let $B_n = X \setminus \closure A_n$. 
Then $B_n$ are dense, nonempty and open in $X$.
Hence $B_n \cap U$ is nonempty and open 
for every nonempty open set $U \subseteq X$.

1. Let $U$ be an arbitrary nonempty open set in $X$.
1. There exists $x_1 \in B_1 \cap U$ such that 
   $x_1 \in B(x_1, \epsilon_1) \subseteq B_1 \cap U$
   where $\epsilon_1 < \frac{1}{2}$.
1. $B_2$ is dense and open so 
   $C_2 = B_2 \cap B\left(x_1, \frac{\epsilon_1}{2}\right)$ 
   is nonempty and open.
1. We can choose a point $x_2 \in B(x_2, \epsilon_2) \subseteq C_2$
   where $\epsilon_2 \leq \frac{\epsilon_1}{2}$.
1. Proceeding in this manner, we choose points

   $$
   x_n \in B(x_n, \epsilon_n) \subseteq B_n \cap B\left (x_{n-1}, \frac{\epsilon_{n-1}}{2}\right)
   $$
   to form a sequence $\{ x_n \}$.
1. The sequence $\{ x_n \}$ is Cauchy, $X$ is complete, hence 
   $x = \lim x_n$ exists in $X$.
1. Also, $x \in B(x_n, \epsilon_n)$ for all $n$.
1. In particular $x \in B(x_1, \epsilon_1) \subseteq U$
   and $x \in B(x_n, \epsilon_n) \subseteq B_n$.
1. Thus, $x \in B_n \cap U$ for all $n$.
1. Thus,
   
   $$
   \begin{aligned}
   & x \in U \cap \left ( \bigcap_{n} B_n \right )\\
   & \implies x \in U \cap \left ( \bigcap_{n} (X \setminus \closure A_n) \right )\\
   & \implies x \in U \cap \left ( X \setminus  \left ( \bigcup_{n} (\closure A_n) \right ) \right )\\
   & \implies x \in U \cap \left ( X \setminus  \left ( \bigcup_{n} A_n \right ) \right )\\
   & \implies x \in U \cap ( X \setminus M ).
   \end{aligned} 
   $$
1. Thus, $U$ has a nonempty intersection with $X \setminus M$.
1. Since $U$ is arbitrary, hence $X \setminus M$ intersects 
   with every nonempty open set in $X$.
1. Thus, $X \setminus M$ is dense in $X$ 
   ({prf:ref}`res-ms-dense-open-intersect`). 
1. Thus, $M$ has an empty interior
   ({prf:ref}`res-ms-dense-complement-interior-empty`).
```

```{prf:corollary}
If a set in a complete metric space has a non-empty interior, then it
is not meager.
```

```{prf:example}

$\QQ$ in $\RR$

1. The set $\QQ$ is meager in $\RR$. 
1. $\RR$ is complete.
1. The interior of $\QQ$ in $\RR$ is empty.
1. The closure of $\QQ$ is $\RR$. 
1. Thus, while a meager set may have an empty interior, 
   its closure need not have an empty interior.
   This is different from rare sets whose closure 
   has an empty interior. 

$\QQ$ in $\QQ$

1. $\QQ$ by itself is not a complete metric space.
1. Singletons are rare sets in $\QQ$.
1. Thus, $\QQ$ is meager in $\QQ$ as it is a countable union of rare sets. 
1. However, the interior of $\QQ$ is not empty. In fact it is whole of $QQ$.
1. {prf:ref}`res-ms-complete-meager-interior-empty` does not apply since
   $\QQ$ is not a complete metric space.
```

```{prf:theorem}
The set $[0,1]$ is uncountable.
```
```{prf:proof}
We prove this using 
{prf:ref}`Baire category theorem <res-ms-baire-category-theorem>`.

1. $[0,1]$ is a complete metric space with the standard metric.
1. Assume $[0,1]$ to be countable.
1. Then, $[0,1] = \{ x_n \}_{n \in \Nat}$ is an enumeration of $[0,1]$.
1. The singleton set $\{x_n \}$ is rare in $[0,1]$.
1. Then $[0,1]$ being a countable union of rare sets would be
   meager.
1. But Baire category theorem says that a complete metric space
   is non-meager.
1. We have a contradiction.
1. Thus, $[0,1]$ must be uncountable.
```

## Baire Spaces

```{prf:definition} Baire space
A metric space is called a *Baire space* if every nonempty 
open set is not a meager set.
```

```{prf:theorem}
Every complete metric space is a Baire space.
```
```{prf:proof}
Let $A$ be a nonempty open subset of a complete metric space $(X,d)$.
If it was meager, then it would have an empty interior 
({prf:ref}`res-ms-complete-meager-interior-empty`).
Thus, it must be non-meager.

Hence $X$ is a Baire space.
```


```{prf:theorem} Characterization of Baire space
:label: res-ms-baire-space-characterization

For a metric space $X$, the following statements are equivalent:

1. $X$ is a Baire space.
1. Every countable intersection of open dense sets is also dense.
1. If $X = \bigcup_{n=1}^{\infty} F_n$ and each $F_n$ is a closed set, then
   the open set $\bigcup_{n=1}^{\infty} \interior F_n$ is dense.
```

```{prf:proof}

(1) $\implies$ (2)

1. Assume $X$ is a Baire space.
1. Let $\{ A_n\}$ be a sequence of open dense sets in $X$.
1. Let $A  = \bigcap_{n=1}^{\infty}A_n$. We need to show that $A$ is dense.
1. We will show that $A$ has a nonempty intersection
   with every nonempty open set of $X$. 
   Thus, claim that $A$ is dense due to 
   {prf:ref}`res-ms-dense-open-intersect`.
1. Let $\OOO \subseteq X$ be an arbitrary nonempty open set.
1. Assume, for contradiction that $A \cap \OOO = \EmptySet$.
1. Then, $X = X \setminus \EmptySet = X \setminus (A \cap \OOO) = (X \setminus A) \cup (X \setminus O)$.
1. Thus, 

   $$
   \begin{aligned}
   \OOO &= X \cap \OOO = ((X \setminus A) \cup (X \setminus O)) \cap \OOO 
   = (X \setminus A) \cap \OOO\\
   &=  \left (X \setminus \left ( \bigcap_{n=1}^{\infty}A_n \right ) \right) \cap \OOO\\
   &= \bigcup_{n=1}^{\infty} ((X \setminus A_n) \cap \OOO).
   \end{aligned}
   $$

1. Due to {prf:ref}`res-ms-open-dense-complement-rare`, $X \setminus A_n$ are rare.
1. Due to {prf:ref}`res-ms-rare-subset-rare`, $(X \setminus A_n) \cap \OOO$ are rare.
1. Thus, $\OOO$ being a countable union of rare sets, is meager.
1. But, in a Baire space, every nonempty open set is not meager.
1. We have a contradiction. 
1. Thus, $A \cap \OOO$ must be nonempty.
1. Thus, $A$ has a nonempty intersection with every nonempty open set in $A$.
1. Thus, $A$ is dense in $X$.


(2) $\implies$ (3)

1. We assume that every countable intersection of open dense sets is dense.
1. Let $\{ F_n \}$ be a sequence of closed sets in $X$ satisfying
   $X = \bigcup_{n=1}^{\infty} F_n$.
1. Let $A_n = \interior F_n$ and let $A = \bigcup_{i=1}^{\infty} A_n$.
   By definition, $A$ is open.
1. Since $F_n$ is closed, hence $E_n = F_n \setminus (\interior F_n)$ 
   is its boundary. 
1. Due to {prf:ref}`res-ms-boundary-closed-rare`, $E_n$ 
   is rare.
1. Thus, the set $E = \bigcup_{n=1}^{\infty}E_n$ is a meager set.
1. Since $E_n$ is closed and rare, hence $X \setminus E_n$ is open and dense
   ({prf:ref}`res-ms-rare-complement-dense`).
1. By our hypothesis (2), the set 
  
   $$
   X \setminus E = X \setminus \left ( \bigcup_{n=1}^{\infty}E_n \right )
   =  \bigcap_{n=1}^{\infty} (X \setminus  E_n)
   $$

   is also a dense set as it is a countable intersection of open dense sets $X \setminus E_n$.
1. Now, notice that:

   $$
   \begin{aligned}
   X \setminus A &= X \setminus \left ( \bigcup_{i=1}^{\infty} A_n \right)\\
   &= \bigcup_{n=1}^{\infty} F_n \setminus \left ( \bigcup_{i=1}^{\infty} (\interior F_n) \right)\\
   &\subseteq \bigcup_{n=1}^{\infty} [F_n \setminus (\interior F_n)]\\
   &= \bigcup_{n=1}^{\infty} E_n\\
   &= E.
   \end{aligned}
   $$

 1. And $X \setminus A \subseteq E$ implies $X \setminus E \subseteq A$.
 1. Since $X \setminus E$ is dense, hence $A$ is also dense.

(3) $\implies$ (1). We need to show that every nonempty open set is non-meager.

1. Let $V$ be a nonempty open set. Assume $V$ to be meager.
1. Then $V$ is a countable union of rare sets:

   $$
   V = \bigcup_{n=1}^{\infty} A_n
   $$
   where $A_n$ are rare, thus $\interior \closure A_n = \EmptySet$.

1. We can write $X$ as:

   $$
   \begin{aligned}
   X &= (X \setminus V) \cup V\\ 
     &= (X \setminus V) \cup A_1 \cup A_2 \cup \dots\\
     &= (X \setminus V) \cup (\closure A_1) \cup (\closure A_2) \cup \dots.
   \end{aligned}
   $$
   The last expression is correct since $\closure A_n \subseteq X$.

1. In this form, $X$ is a countable union of closed sets.
1. By our hypothesis (3), the open set:

   $$
   (\interior (X \setminus V)) \cup (\interior (\closure A_1))
   \cup (\interior (\closure A_2)) \cup \dots
   = \interior (X \setminus V)
   $$
   is dense in $X$. 
   Here, we used the fact that $A_n$ are rare.
1. Since $\interior (X \setminus V) \subseteq X \setminus V$, hence
   $X \setminus V$ is also dense in $X$.
1. In particular $V \cap (X \setminus V) \neq \EmptySet$ since
   a dense set has a nonempty intersection with every nonempty 
   open set ({prf:ref}`res-ms-dense-open-intersect`).
1. But this is impossible since $V \cap (X \setminus V) = \EmptySet$. 
1. Thus, $V$ cannot be not a meager set.
1. We have established that any nonempty open $V$ is not a meager set. 
1. Hence, $X$ is a Baire space. 
```

## Completion

```{prf:theorem}
:label: res-ms-uniform-continuous-complete-extension 

Let $(X, d)$  be a metric space and let $(Y, \rho)$ be
a complete metric space. 
If $f : X \to Y$ with $A = \dom f$ is a 
{prf:ref}`uniformly continuous <def-ms-uniform-continuity>`
function on $A$ then $f$ has a unique uniformly continuous 
{prf:ref}`extension <def-st-function-extension>` 
to the {prf:ref}`closure <def-ms-closure>` of $A$.
```

```{prf:proof}
If a sequence $\{x_n\}$ of $A$ converges to a closure point $x = \lim x_n$,
then the sequence $\{f(x_n)\}$ of $Y$ converges to some limit $y = \lim f(x_n)$.

1. Let $x \in \closure A$.
1. There exists a sequence $\{ x_n \}$ of $A$ such that $\lim x_n = x$.
1. Consider the sequence $\{ f (x_n) \}$ of $Y$.
1. Choose $\epsilon > 0$.
1. Since $f$ is uniformly continuous on $A$, hence 
   there exists $\delta > 0$ such that
   $\rho(f(x), f(y)) < \epsilon$ whenever $d(x,y)< \delta$.
1. Since $\{ x_n \}$ is convergent and hence Cauchy, we can pick
   $n_0$ such that $d(x_m, x_n) < \delta$ for all $m, n > n_0$.
1. Thus, $\rho(f(x_m), f(x_n)) < \epsilon$ for all $m, n > n_0$.
1. Thus, $\{ f(x_n) \}$ is a Cauchy sequence of $Y$.
1. Since $Y$ is complete, hence every sequence converges.
1. Thus, there is a limit $y = \lim f(x_n)$.

For any sequence $\{x_n\}$ of $A$ converging to $x = \lim x_n$, the
corresponding sequence  $\{f(x_n)\}$ of $Y$  has the same limit.


1. Assume that $x = \lim x_n = \lim y_n$ where $\{x_n \}$ and $\{ y_n\}$ are
   two different sequences converging to $x$.
1. Let $u = \lim f(x_n)$ and $v = \lim f(y_n)$. We claim that $u = v$.
1. Consider the sequence $\{ z_n \}$ defined as $z_{2n} = x_n$ and 
   $z_{2n-1} = y_n$. 
1. It is easy to show that $\{z_n \}$ converges to $x$.
1. Then, $\lim f(z_n)$ exists in $Y$. 
1. If a sequence converges, then all its subsequences converge to
   the same limit.
1. Thus, $\lim f(x_n) = \lim f(y_n) = \lim f(z_n)$.
1. Thus, $u = v$.
1. Therefore $\lim f(x_n)$ is independent of the choice
   of sequence $\{ x_n \}$ as long as $x = \lim x_n$.


We define a function $f^* : X \to Y$ with
$\dom g = \closure A$ given the function $f : X \to Y$ 
with $\dom f = A$ as:

$$
f^*(x) = \lim f(x_n) 
$$
where $\{x_n\}$ is any sequence converging to $x \in \closure A$;
i.e., $x = \lim x_n$.

$f^*$ is well defined since $\lim f(x_n)$ is independent 
of the choice of the sequence $\{ x_n \}$  converging to $x \in \closure A$. 

We next establish that $f^*$ is uniformly continuous. 

1. Let $\epsilon > 0$.
1. We can choose $\delta > 0$ such that $\rho(f(x), f(y)) < \epsilon$
   whenever $d(x,y) < \delta$ for any $x,y \in A$.
1. Now let, $x,y \in \closure A$ satisfying $d(x,y) < \delta$. 
1. Let $\{x_n\}$ and $\{y_n\}$ be convergent sequences of $A$
   with $\lim x_n = x$ and $\lim y_n = y$.
1. Then $\lim d(x_n, y_n) = d(x, y)$ due to 
   {prf:ref}`res-ms-sequence-distance-limit`.
1. Since $d(x,y) < \delta$, 
   we can pick $n_0$ such that $d(x_n, y_n) < \delta$
   for all $n > n_0$.
1. But since $x_n, y_n \in A$ and $f$ is 
   uniformly continuous, we have,
   $\rho(f(x_n), f(y_n)) < \epsilon$ for all $n > n_0$.
1. Since $\{f(x_n)\}$ and $\{f(y_n)\}$ are convergent
   sequences of $Y$, hence
   $\lim \rho(f(x_n), f(y_n)) = \rho(f(x), f(y))$
   again due to {prf:ref}`res-ms-sequence-distance-limit`.
1. Thus, $\rho(f(x), f(y)) \leq \epsilon$.
1. Thus, $f^*$ is uniformly continuous on $\closure A$.
```


```{prf:definition} Completion of a metric space
A complete metric space $(Y, \rho)$ is called
a *completion* of a metric space $(X, d)$ if there
exists an {prf:ref}`isometry <def-ms-isometry>` 
$f: (X, d) \to (Y, \rho)$ with $\dom f = X$
such that $f(X)$ is 
{prf:ref}`dense <def-ms-dense-set>` in $Y$.
```

If we think of $X$ and $f(X)$ as identical
(up to an isometry), then we can think of
$X$ as a subset of $Y$.


```{prf:theorem}
:label: res-ms-completions-isometric

Any two completions of a metric space are
{prf:ref}`isometric <def-ms-isometric-spaces>`.
```

```{prf:proof}
Let $(Y_1, \rho_1)$ and $(Y_2, \rho_2)$ be
two different completions of $(X,d)$.

1. Then there are isometries $f : X \to Y_1$ 
   and $g : X \to Y_2$ with $\dom f = \dom g = X$.
1. $g$ is an isometry with $\dom g = X$ and $\range g = g(X)$.
1. $f^{-1}$ is an isometry with $\dom f^{-1} = f(X)$
   and $\range f^{-1} = X$.
1. Then, $h = g \circ f^{-1}$ is an isometry 
   from $Y_1$ to $Y_2$ with 
   $\dom h = f(X)$ and  $\range h = g(X)$.
1. $f(X)$ is dense in $Y_1$. Hence $\closure f(X) = Y_1$.
1. $h$ is uniformly continuous (since it is an isometry).
1. $Y_2$ is complete.
1. Then, 
   due to {prf:ref}`res-ms-uniform-continuous-complete-extension`,
   there exists a uniformly continuous extension $h^*$
   of $h$ to all of $Y_1$.

We have established that $h^*$ is uniformly continuous. 

We next show that $h^*$ is an isometry.

1. Let $u,v \in Y_1$ and $z = h^*(u)$ and $w = h^*(v)$.
1. There is a sequence $\{ x_n \}$ of $X$ such that $\lim f(x_n) = u$.
1. There is a sequence $\{ y_n \}$ of $X$ such that $\lim f(y_n) = v$.
1. Let $u_n = f(x_n)$ and $v_n = g(y_n)$.
1. Let $z_n = g(u_n)$ and $w_n = g(y_n)$.
1. We have $\lim z_n = z$ and $\lim w_n = w$.
1. Since $f$ is an isometry, hence $d(x_n, y_n) = \rho_1(u_n, v_n)$.
1. Since $g$ is an isometry, hence $d(x_n, y_n) = \rho_2(z_n, w_n)$.
1. Thus, $\rho_1(u_n, v_n) =  \rho_2(z_n, w_n)$.
1. Taking limits, we get $\rho_1(u, v) = \rho_2(z, w)$.
1. Thus, $h^*$ is an isometry. 
1. Since it is an isometry, hence it is injective. 

We next show that $h^*$ is surjective (onto).

1. Let $v \in Y_2$.
1. There exists a sequence $\{ x_n \}$ such that $\lim g(x_n) = v$. 
1. There exists $u \in Y_1$ such that $\lim f(x_n) = u$.
1. Let $f(x_n) = u_n$ and $g(x_n) = v_n$. 
1. Then, $h(u_n) = (g \circ f^{-1})(u_n) = g(x_n) = v_n$. 
1. Thus, $h^*(u_n) = v_n$.
1. Then, since $h^*$ is uniformly continuous,
   $\lim u_n = u$ \implies $\lim h^*(u_n) = \lim v_n = v = h^*(u)$.
1. Thus, for every $v \in Y_2$, there exists $u \in Y_1$ such that
   $h^*(u) = v$.
1. Thus, $h^*(u)$ is surjective.


Together since $h^*$ is an isometric which is onto,
hence $Y_1$ and $Y_2$ are isometric.
```

```{prf:remark}
:label: res-ms-mapping-closure-completion

If $f : (X, d) \to (Y, \rho)$ is an isometry with $\dom f = X$ and
$Y$ is a complete metric space, then
$\closure f(X)$ is a completion of $X$.
```

```{prf:proof}
Let Z = $\closure f(X)$. Then $Z$ is a closed subset of $Y$.
By {prf:ref}`res-ms-closed-subset-complete`, $(Z, \rho)$
is a complete subspace.

Now define $g : (X, d) \to (Z, \rho)$ as:

$$
g(x) = f(x).
$$

Then, $g$ is an isometry and $g(X)$ is dense in $Z$.
Thus, $Z$ is a completion of $X$.
```

```{prf:theorem}
Every metric space has a unique (up to an isometry) completion.
```

```{prf:proof}
We prove this theorem by constructing a metric space which is
a completion of a given metric space. 

1. Let $(X,d)$ be a metric space.
1. Fix an element $a \in X$.
1. Now, for every $x \in X$, we introduce a function
   $f_x : X \to \RR$ defined as:

   $$
   f_x(y) = d(x,y) - d(y,a) \Forall y \in X.
   $$

   Note that $\dom f_x = X$.

1. From the triangular inequality we have:

   $$
   |f_x(y)| = |d(x,y) - d(y,a) | \leq d(x,a) \Forall y \in X.
   $$
1. Thus, for a given $x$ and fixed $a$, the parametrized 
   function $f_x$ is bounded by $d(x,a)$.
1. Thus, $f_x \in B(X)$, the space of bounded functions from $X$ to $\RR$.
1. We established in {prf:ref}`ex-ms-bounded-functions-metric-space` that
   the metric space $B(X)$ is a complete metric space.

We next show that the mapping $f: X \to B(X)$ given by 
$x \mapsto f_x$ is an isometry.
Recall that the distance between two functions $g, h \in B(X)$
is given by:

$$
D(g, h) = \sup\{ | g(x) - h(x) | \ST x \in X\}.
$$

Now for some $x,z \in X$ with corresponding function
$f_x , f_z \in B(X)$, for any $y \in X$, we have:

$$
\begin{aligned}
|f_x(y) - f_z(y)| &= | d(x, y) - d(y, a) - [d(z,y) - d(y,a)] |\\
&= |d(x,y) - d(z,y) | \leq d(x, z).
\end{aligned}
$$

At the same time:

$$
|f_x(z) - f_z(z)| = | d(x, z) - d(z, z)| = d(x, z).
$$

Thus, 

$$
D(f_x, f_z) = \sup\{ | f_x(y) - f_z(y) | \ST y \in X\} = d(x, z).
$$

Thus, $f$ is an isometry.
Since $(B(X), D)$ is a complete metric space, hence
as per {prf:ref}`res-ms-mapping-closure-completion`,
$(\closure f(X), D)$ is a completion of $X$.

We have already established in
{prf:ref}`res-ms-completions-isometric` that 
any two completions of $X$ are isometric to each other.
Thus, the completion is unique up to an isometry.
```