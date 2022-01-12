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


## Baire Category Theorem


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

```{prf:theorem} Baire category theorem
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


```{prf:example}

$\QQ$ in $\RR$

1. The set $\QQ$ is meager in $\RR$. 
1. $\RR$ is complete.
1. The interior of $\QQ$ in $\RR$ is empty.

$\QQ$ in $\QQ$

1. $\QQ$ by itself is not a complete metric space.
1. Singletons are rare sets in $\QQ$.
1. Thus, $\QQ$ is meager in $\QQ$ as it is a countable union of rare sets. 
1. However, the interior of $\QQ$ is not empty. In fact it is whole of $QQ$.
1. {prf:ref}`res-ms-complete-meager-interior-empty` does not apply since
   $\QQ$ is not a complete metric space.
```


## Baire Spaces

```{prf:definition} Baire space
A metric space is called a *Baire space* if every nonempty 
open set is not a meager set.
```



```{prf:theorem} Characterization of Baire space
For a metric space $X$, the following statements are equivalent:

1. $X$ is a Baire space.
1. Every countable intersection of open dense sets is also dense.
1. If $X = \bigcup_{n=1}^{\infty} F_n$ and each $F_n$ is a closed set, then
   the open set $\bigcup_{n=1}^{\infty} \interior F_n$ is dense.
```
