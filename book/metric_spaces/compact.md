# Compactness

The material in this section is primarily based on
{cite}`aliprantis1998principles,gopal2020introduction`.

## Covers


```{prf:definition} Cover
:label: def-ms-cover

A family $\{ A_i \}_{i \in I}$ of subsets of $X$ is said to *cover* a set
$A$ if

$$
A \subseteq \bigcup_{i \in I} A_i.
$$
Here $I$ is an index set indexing the sets in the family. $I$ 
could be finite, countable or uncountable.
```

```{prf:remark}
The definition of a *cover* doesn't require $X$ to be a metric space.
$X$ can be any set.
```
```{prf:definition} Subcover
:label: def-ms-subcover

If a subfamily of a cover $\{ A_i \}_{i \in I}$  of $A$ also covers
$A$, then the subfamily is called a *subcover*.
```

## Open Covers

```{prf:definition} Open cover
:label: def-ms-open-cover

A family of open subsets $\{ A_i \}_{i \in I}$ of subsets of $(X,d)$  
is an *open cover* of $A$ if it covers $A$.
```



```{prf:theorem} Lindelöf

Every open cover of a subset of $\RR^n$ can be reduced to 
an at-most countable subcover.
```

```{prf:proof}
We call a point $a = (a_1, \dots, a_n) \in \RR^n$ a rational point
if every component of $a$ is a rational number.

1. Let $A$ be a subset of $\RR^n$.
1. Let $\{ \OOO_i \}_{i \in I}$ be an open cover of $A$ (possibly uncountable).
1. Thus, $A \subseteq \bigcup_{i \in I} \OOO_i$.
1. For each $x \in A$, 
   1. Choose an index $i_x \in I$ such that $x \in \OOO_{i_x}$.
   1. Pick a rational point $a_x \in \RR^n$ and a rational positive number $r_x$
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


```{prf:lemma} Existence of finite open cover
:label: res-ms-compact-set-existence-of-finite-cover

Let $A \subseteq X$ of a metric space $(X,d)$.
If every sequence in $A$ has a subsequence which converges to a point of $A$,
then, 
for every $r > 0$ there exist $x_1, \dots, x_n \in A$ such that

$$
A \subseteq \bigcup_{j=1}^n B(x_j, r).
$$
```
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