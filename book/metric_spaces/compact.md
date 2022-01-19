# Compactness

The material in this section is primarily based on
{cite}`aliprantis1998principles,gopal2020introduction`.


```{div}
Recall from {prf:ref}`def-st-cover` that for a subset $A \subseteq X$,
a cover is a family $\{ A_i \}_{i \in I}$ of subsets of $X$ such that

$$
A \subseteq \bigcup_{i \in I} A_i.
$$
```
## Open Covers

```{prf:definition} Open cover
:label: def-ms-open-cover

A family of open subsets $\{ A_i \}_{i \in I}$ of subsets of $(X,d)$
is an *open cover* of $A$ if it covers $A$.
```



```{prf:theorem} Lindelöf

Every open cover of a subset of $\RR^m$ can be reduced to 
an at-most countable subcover.
```

```{prf:proof}
We call a point $a = (a_1, \dots, a_m) \in \RR^m$ a rational point
if every component of $a$ is a rational number.

1. Let $A$ be a subset of $\RR^m$.
1. Let $\{ \OOO_i \}_{i \in I}$ be an open cover of $A$ (possibly uncountable).
1. Thus, $A \subseteq \bigcup_{i \in I} \OOO_i$.
1. For each $x \in A$, 
   1. Choose an index $i_x \in I$ such that $x \in \OOO_{i_x}$.
   1. Pick a rational point $a_x \in \RR^m$ and a rational positive number $r_x$
      such that $x \in B(a_x, r_x) \subseteq \OOO_{i_x}$.
1. Consider the collection $C = \{ B(a_x, r_x) \ST x \in A \}$.
1. Since the set of rational points is countable and the set of rational numbers is countable,
   hence the set of all open balls centered at rational points with rational radii is countable.
1. Hence, $C$ which is a subset of open balls with rational points as centers and
   rational radii, is at most countable.
1. Thus, $C$ is an at most countable open cover of $A$.
1. Since each $B(a_x, r_x)$ is a subset of an $\OOO_{i_x}$, hence
   there exists an at most countable subcover of $\{ \OOO_i\}_{i \in I}$ for $A$.
```


## Compact Sets


```{prf:definition} Compact set
:label: def-ms-compact-set

Let $(X, d)$ be a metric space. A subset $A$ of $X$ is called
*compact* if every open cover of $A$ can be reduced to a
finite subcover. 
```


```{prf:definition} Compact metric space
:label: def-ms-compact-metric-space

Let $(X,d)$ be a metric space. If $X$ is itself a
compact set, then $(X,d)$ is called a *compact metric space*.
```

## Characterization of Compactness

We have defined compactness as a property where every open
cover can be reduced to a finite subcover. 
The characterization of a property involves identifying
other properties which are equivalent in the sense that
property A $\iff$ property B. If one is true then 
the other must be true and vice versa.

We will see later that compactness of a set $A$ is equivalent 
to the property that every sequence of $A$ has a subsequence
that converges to a point in $A$. However, before we go there,
let us examine some implications of this
property that every sequence of a set $A$ has a subsequence that
converges within the set $A$. These results will be
useful later in the characterization of compact sets.


```{prf:lemma} Lebesgue number
:label: res-ms-open-cover-lebesgue-number

Let $A \subseteq \bigcup_{i \in I} \OOO_i$ be an open cover of $A$. 

If every sequence in $A$ has a subsequence which converges to a point of $A$,
then, there exists a number $\delta > 0$ such that for each $x \in A$, we have
$B(x, \delta) \subseteq \OOO_i$ for at least one $i \in I$.

Any such number $\delta > 0$ is called a *Lebesgue number* of $A$
for the open cover $\{\OOO_i \}_{i \in I}$.
```

```{prf:proof}
Assume the claim is false. 

1. Then, for each $\delta > 0$, there exists some $x \in A$ such that
   $B (x, \delta)$ is not a subset of any $\OOO_i$.
1. In particular, for each $n$, there exists some $x_n \in A$ such that
   $B (x_n, \frac{1}{n}) \cap (X \setminus \OOO_i) \neq \EmptySet$ holds
   for each $i \in I$.
1. Consider the sequence $\{ x_n \}$. 
1. By the hypothesis, every
   sequence has a subsequence that converges to a point of $A$.
1. Let $x \in A$ be the limit of such a subsequence of $\{ x_n \}$.
1. Since $x \in A$, $x \in \OOO_i$ for at least one $i \in I$.
1. Pick some $i \in I$ such that $x \in \OOO_i$. 
1. Choose some $r > 0$ such that $x \in B(x, r) \subseteq \OOO_i$. 
   1. Recall that $\OOO_i$ is open and $x$ is its interior point. So such an $r > 0$
      can be chosen.
1. Now, select some $n$ such that $\frac{1}{n} < \frac{r}{2}$ and $d(x, x_n) < \frac{r}{2}$.
1. It follows that $B(x_n, \frac{1}{n}) \subseteq B(x, r) \subseteq \OOO_i$.
1. But this contradicts with the selection of $x_n$ such that $B (x_n, \frac{1}{n})$ is
   not contained in any $\OOO_i$.
1. Thus, a $\delta > 0$ must exist satisfying the condition that for each $x \in A$, 
   $B(x, \delta) \subseteq \OOO_i$ for at least one $i \in I$.
```


```{prf:lemma} Existence of finite cover of open balls
:label: res-ms-compact-set-existence-of-finite-cover

Let $A \subseteq X$ of a metric space $(X,d)$.
If every sequence in $A$ has a subsequence which converges to a point of $A$,
then, 
for every $r > 0$ there exist $x_1, \dots, x_n \in A$ such that

$$
A \subseteq \bigcup_{j=1}^n B(x_j, r).
$$
```
This lemma simply claims that we can construct a finite open cover
of open balls for $A$ for every $r > 0$. 
```{prf:proof}
Assume the claim to be false. Choose $r > 0$ such that it is not possible to 
select a finite number of points from $A$ such that 

$$
A \subseteq \bigcup_{j=1}^n B(x_j, r).
$$

1. Pick some $x_1 \in A$. 
1. Choose some $x_2 \in A \setminus B(x_1, r)$. We can choose $x_2$ since 
   $A$ doesn't have a finite open ball cover.
1. Assuming that $x_1, x_2, \dots,  x_n$ have been chosen inductively, 
   choose $x_{n+1}$ from the set $A \setminus \bigcup_{i=1}^n B(x_i, r)$.
1. By design, $d(x_n, x_m) \geq r$ holds for every $n \neq m$. 
1. Then, no subsequence of $\{ x_n \}$ can converge.
1. This contradicts with the hypothesis that every sequence has a subsequence
   that converges in $A$.
1. Hence, the claim must be true. 
```


```{prf:theorem} Characterization of compactness
:label: def-ms-compact-characterization

Let $A$ be a subset of a metric space $(X,d)$. 
The following statements are equivalent.

1. $A$ is compact.
1. Every infinite subset of $A$ has an accumulation point in $A$.
1. Every sequence in $A$ has a subsequence which converges to a point of $A$.
```


```{prf:proof}
(1) $\implies$ (2)

1. Let $S$ be an infinite subset of $A$.
1. Assume, by way of contradiction, that $S$ has no accumulation point in $A$.
1. Then for every $x \in A$, there exists a deleted neighborhood of $x$ 
   that is disjoint with $S$.
1. That is, $\forall x \in A, \exists r_x > 0 \ST B (x, r_x) \cap ( S \setminus \{ x \}) = \EmptySet$.
1. Then, $B(x, r_x) \cap S$ can either be empty or it can at most contain $x$.
1. Thus, $B(x, r_x) \cap S \subseteq \{ x\}$.
1. Consider the open cover $C = \bigcup_{x \in A} B(x, r_x)$.
1. It is easy to see that $A \subseteq C$.
1. Since $A$ is compact (by hypothesis), there exists a finite set
   $\{ x_1, \dots, x_n \} \subseteq A$ such that
   $A \subseteq \bigcup_{i=1}^n B(x_i, r_{x_i})$.
1. But then 

   $$
   S = A \cap S = \bigcup_{i=1}^n [B(x_i, r_{x_i}) \cap S] \subseteq \{ x_1, \dots, x_n \}.
   $$
1. Thus, $S$ must be a finite set containing at most $n$ elements.
1. We arrive at a contradiction as $S$ is infinite.
1. Hence, $S$ has an accumulation point in $A$.


(2) $\implies$ (3)

1. We assume that every infinite subset of $A$ has an accumulation point in $A$.
1. Let $\{x_n \}$ be an arbitrary sequence of $A$.
1. If $\{x_n \}$ is constant, then every subsequence is constant and convergent.
1. If $\{x_n \}$ takes a finite number of distinct values, then there is at least
   one value which must occur infinite times. Thus, at least one subsequence is
   a constant sequence and hence convergent.
1. We are left with the case where $\{ x_n \}$ contains infinite distinct values.
1. Then, we can choose a subsequence $\{ y_n \}$ of $\{ x_n \}$ which consists of
   all distinct values; i.e., $y_n \neq y_m$ whenever $n \neq m$.
   1. Let $k_1 = 1$.
   1. Assuming $k_1, \dots, k_n$ have been selected, 
      choose $k_{n+1} > k_n$ such that $x_{k_{n+1}} \neq x_{k_i}$ for $1 \leq i \leq n$.
   1. This is possible since $\{x_n \}$ has infinite distinct values and 
      so far only $n$ distinct values have been chosen.
   1. Now, let $y_n = x_{k_n}$.
   1. It is clear that $\{y_n\}$ is a subsequence of $\{x_n\}$ consisting of
      all distinct values.
1. Consider the set $Y = \{ y_1, y_2, \dots \}$ (not the sequence but the set).
1. By our hypothesis (2), since $Y$ is an infinite subset of $A$, hence it must
   have an accumulation point in $A$.
1. Let $x$ be an accumulation point of $Y$.
1. Assume that $x \neq y_n$ for each $n$. If $x = y_k$ for some $k$, then drop the
   first $k$ elements of $\{ y_n \}$.
1. This ensures that $d(x, y_n) > 0$ for every $n$. 
1. We will now select a subsequence of $\{ y_n \}$ that converges to $x$.
1. Towards this, choose $m_1$ such that $d(y_{m_1}, x) < 1$.
1. Now, inductively, assuming that $m_1 < m_2, \dots < m_n$ have been chosen,
   choose $m_{n+1}$ such that

   $$
   d(y_{m_{n+1}}, x) < r_{n+1} = \min \{\frac{1}{n+1}, d(y_1, x), d(y_2, x), \dots, d(y_{m_n}, x) \}.
   $$

1. Since $d(x, y_n) > 0$, hence $r_{n+1} > 0$. 
1. Since $x$ is an accumulation point of $Y$, hence for every $r > 0$, there exists a 
   point $y \in Y$ such that $d(x, y) < r$.
1. Thus, it is possible to pick a suitable $m_{n+1}$ such that $d(y_{m_{n+1}}, x) < r_{n+1}$. 
1. Also, by design, $m_{n+1}$ must be greater than $m_n$
   as $r_{n+1} < d(y_i, x) \Forall 1 \leq i \leq m_n$.
1. Thus, $\{ y_{m_n} \}$ is a subsequence of $\{ y_n \}$.
1. Hence, $\{y_{m_n}\}$ is a subsequence of $\{ x_n \}$ too.
1. Since $d(x, y_{m_n}) < \frac{1}{n}$, it follows that $\lim y_{m_n} = x$.
1. Thus, $\{ x_n \}$ has a convergent subsequence which converges to a point of $A$.

(3) $\implies$ (1)

1. Let $A \subseteq \bigcup_{i \in I} \OOO_i$ be an arbitrary open cover of $A$. 
1. We can pick a Lebesgue number $\delta > 0$ such that for each $x \in A$, 
   we have $B(x, \delta) \subseteq \OOO_i$ for at least one $i \in I$
   thanks to {prf:ref}`res-ms-open-cover-lebesgue-number`.
1. Now, thanks to {prf:ref}`res-ms-compact-set-existence-of-finite-cover`, we
   can pick $x_1, \dots, x_n \in A$ such that:

   $$
   A \subseteq \bigcup_{j=1}^n B(x_j, \delta).
   $$
1. Now, for each $j$ pick some $i_j \in I$ such that $B(x_j, \delta) \subseteq \OOO_{i_j}$.
1. Then,

   $$
   A \subseteq \bigcup_{j=1}^n B(x_j, \delta) \subseteq \bigcup_{j=1}^n \OOO_{i_j}.
   $$
1. Thus, the open cover of $A$ has a finite subcover.
1. Thus, $A$ is compact.
```

## Implications of Compactness

```{prf:theorem} Compact sets are closed and bounded
:label: res-ms-compact-is-closed-bounded

A compact set is closed and bounded.
```
```{prf:proof}
Assume $A$ to be compact. We shall show that $A$ must be bounded.

1. Choose an open cover for $A$ as $A \subseteq \bigcup_{x \in A}B(x, 1)$.
1. Since $A$ is compact, hence there exist finite set of points $\{ x_1, \dots x_n \} \subseteq A$
   such that $A \subseteq \bigcup_{i=1}^n B(x_i, 1)$.
1. Let $M = \max \{ d(x_i, x_j) \ST 1 \leq i, j \leq n\}$.
1. For any $x, y \in A$, choose $i, j$ such that $x \in B(x_i, 1)$ and $y \in B(x_j, 1)$.
1. Then, by triangle inequality, we have:

   $$
   d(x, y) \leq d(x, x_i) + d(x_i, x_j) + d(x_j, y) < M + 2 < \infty.
   $$
1. Thus, $\diam A = \sup d(x,y)$ is finite and $A$ is bounded.


We now show that if $A$ is compact then $A$ must be closed too. 
Towards this, we show that $A$ contains all its closure points. 

1. Let $x \in \closure A$. 
1. Due to {prf:ref}`res-ms-closure-point-as-limit`, there exists
   a sequence $\{ x_n \}$ of $A$ with $\lim x_n = x$.
1. Due to {prf:ref}`def-ms-compact-characterization`, $\{x_n\}$ has
   a subsequence that converges to a point of $A$ (since $A$ is compact by hypothesis).
1. As per {prf:ref}`res-ms-subsequence-convergence`, subsequences of
   a convergent sequence converge to the same limit. 
1. Thus, $x$ must be in $A$.
1. Thus, $\closure A \subseteq A$. Thus, $\closure A = A$. Thus, $A$ is closed.
```

Although every compact set is closed and bounded, the converse need
not be true. See {prf:ref}`ex-discrete-space-closed-bounded-not-compact`
for an example of closed and bounded set (in discrete space)
which is not compact.

In the specific case of Euclidean spaces, all closed and
bounded sets are compact too. 
See {prf:ref}`Heine-Borel theorem <res-ms-heine-borel-euclidean>` below.


```{prf:theorem} Continuous images of compact sets are compact
:label: res-ms-compact-continuous-map

Let $f: (X, d) \to (Y, \rho)$ be a continuous function. 
Let $A$ be a compact subset of $X$ with $A \subseteq \dom f$.
Then $f(A)$ is a compact subset of $Y$.
```

```{prf:proof}
We prove this by showing that any open cover of $f(A)$ 
can be reduced to a finite subcover.

1. Let $f(A) \subseteq \bigcup_{i \in I} \OOO_i$ be an open cover for $f(A)$.
1. Then $A \subset \bigcup_{i \in I} f^{-1} (\OOO_i)$.
1. Since $f$ is continuous, 
   hence $f^{-1} (\OOO_i)$ is an open subset of $X$ for every $i \in I$.
1. Since $A$ is compact, there exist indices $i_1, \dots, i_n$ such that
   $A \subseteq \bigcup_{j=1}^n f^{-1}(\OOO_{i_j})$.
1. Then

   $$
   f(A) \subseteq f\left ( \bigcup_{j=1}^n f^{-1}(\OOO_{i_j}) \right ) 
   = \bigcup_{j=1}^n f(f^{-1}(\OOO_{i_j}))
   \subseteq  \bigcup_{j=1}^n \OOO_{i_j}.
   $$
1. Thus, $A$ is compact.
```

```{prf:theorem}
Every closed subset of a compact space is compact.
```
```{prf:proof}
Let $(X, d)$ be a compact metric space and let $A$ be a closed subset of $X$.

1. Let $\{\OOO_i\}_{i \in I}$ be an open cover of $A$. 
   We have, $A \subseteq \bigcup_{i \in I}\OOO_i$.
1. $X = A \cup (X \setminus A)$.
1. Then, $X \subseteq (X \setminus A) \cup \bigcup_{i \in I} \OOO_i$.
1. Since all $\OOO_i$ are subsets of $X$, hence we can write it as:
   $X = (X \setminus A) \cup \bigcup_{i \in I} \OOO_i$.
1. Since $A$ is closed, hence $X \setminus A$ is open.
1. Thus, $(X \setminus A) \cup \bigcup_{i \in I} \OOO_i$ is an open cover of $X$.
1. But $X$ is compact. Hence, there exist finite indices $i_1, \dots, i_n$ such that
   $X = (X \setminus A) \cup \OOO_{i_1} \cup \dots \cup \OOO_{i_n}$.
1. But then $A \subseteq X$  and $A \cap (X \setminus A) = \EmptySet$ imply that:
   $A \subseteq \OOO_{i_1} \cup \dots \cup \OOO_{i_n}$.
1. Thus, $A$ is compact.   
```


## Euclidean Spaces

Recall that $\RR^m$ are called Euclidean spaces with the standard metric:

$$
d (x, y) \triangleq \left ( \sum_{i=1}^m |x_i - y_i|^2 \right )^{\frac{1}{2}}.
$$

By $0 \in \RR^m$ we shall mean the vector $(0, \dots, 0)$.

The compact subsets of a Euclidean space are precisely those
sets which are closed and bounded.

```{prf:theorem} Heine-Borel theorem
:label: res-ms-heine-borel-euclidean

A subset of a Euclidean space is compact if and
only if it is closed and bounded.
```
Compare this to {prf:ref}`Heine-Borel theorem <res-rl-heine-borel>` for the real line.
We established there that for a closed and bounded subset of $\RR$, 
any open cover can be reduced to a finite subcover. There, we defined
closed and bounded sets as compact sets. Our treatment of compactness
in this section is more general. 

We start here with the definition that a compact set is one for which
any open cover can be reduced to a finite subcover. 
We then show in this theorem that in the special case of 
Euclidean spaces $\RR^m$, the compact subsets are identical to the
closed and bounded subsets of $\RR^m$.

```{prf:proof}
We have shown in {prf:ref}`res-ms-compact-is-closed-bounded` that
every compact set is closed and bounded.

For the converse, we assume $A$ is a closed and bounded subset of $\RR^m$.
We will show that every sequence of $A$ has a subsequence converging in $A$.

1. Since $A$ is bounded, we can pick $M > 0$ such that $d(x, y) \leq M$ for all $x, y \in A$.
1. Fix an element $y \in A$.
1. Let $a = (a_1, \dots, a_m) \in A$ be some arbitrary point of $A$. Then

   $$
   |a_i | \leq d(a, 0) \leq d(a, y) + d(y, 0) \leq M + d(y, 0)
   $$
   holds for every $1 \leq i \leq m$. 
1. Thus, the set of real numbers consisting of the $i$-th coordinates 
   of the elements of $A$ is a bounded set.
1. Choose an arbitrary sequence $\{ x_n \}$ of $A$.
1. Recall from {prf:ref}`Bolzano Weierstrass theorem <res-bolzano-weierstrass-theorem>` for real numbers
   that every bounded sequence of real numbers has a convergent subsequence.
1. Note that if we form the sequence of real numbers from 
   any particular coordinate of $\{x_n\}$, (say first coordinates or second coordinates)
   then the sequence is bounded by $M + d(y, 0)$.
1. Every such sequence of real numbers (from a fixed coordinate of $\{x_n\}$) will
   have a convergent subsequence.
1. Thus, there is a subsequence $\{x^1_n\}$ of $\{x_n\}$ whose first coordinates 
   form a sequence in $\RR$ that converges in $\RR$.
1. Now, we choose $\{x^2_n\}$ as a subsequence of $\{x^1_n\}$ so that the
   corresponding sequence of second coordinates of $\{x^2_n\}$ converge in $\RR$.
1. Proceeding in this manner, after $m$ steps, we have a subsequence
   $\{x^m_n\}$ of $\{x_n\}$ with the property that for each $1 \leq i \leq m$,
   the sequence of its $i$-th coordinates forms a convergent subsequence in $\RR$.
1. Since each of the coordinates of $\{x^m_n\}$ converges in $\RR$,
   hence, $\{x^m_n\}$ converges in $\RR^m$. 
1. But since $A$ is closed, hence $\{x^m_n\}$ converges to a point of $A$.
1. Thus, every sequence of $A$ has a convergent subsequence in $A$. 
1. Thus, by {prf:ref}`def-ms-compact-characterization`, $A$ is compact. 
```

Note that the property *convergence in individual coordinates
implies convergence in $\RR^m$* is due to the specific choice
of Euclidean metric.


```{prf:theorem}
Let $f : (X, d) \to \RR$ be a real valued function.
If $f$ is continuous then $f$ attains a maximum and minimum value on 
every compact subset of $\dom f$.
```
```{prf:proof}
Let $A$ be a compact subset of $\dom f$. 

1. Then, $f(A)$ is compact in $\RR$ due to {prf:ref}`res-ms-compact-continuous-map`.
1. Then, $f(A)$ is closed and bounded due to {prf:ref}`Heine-Borel theorem <res-ms-heine-borel-euclidean>`.
1. Since $f(A)$ is bounded, hence it has an infimum and supremum.
1. Since $f(A)$ is closed, hence its infimum and supremum lie inside $f(A)$ itself.
1. Thus, $f$ attains a maximum and minimum value in $A$.
```