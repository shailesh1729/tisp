(sec:ms:subspaces)=
# Subspace Topology

Let $(X, d)$ be a metric space. Let $Y \subseteq X$. 
Recall from {prf:ref}`def-ms-metric-subspace`
that $(Y, d)$ is a metric subspace with the
distance function $d$ restricted to $Y \times Y$.

```{prf:remark}
Let $Y$ be a metric subspace of $X$ and $S \subseteq Y$.
The interior, closure and boundary of $S$ w.r.t. $X$ 
and w.r.t. $Y$ may be different.

If a subspace hasn't been specified, by default, we shall
assume that we are computing the interior, closure and 
boundary w.r.t. the metric space $X$.
```

## Open Balls

```{prf:theorem} Open balls in the metric subspace
:label: res-ms-subspace-open-balls 

Let $(Y, d)$ be a metric subspace of $(X, d)$.
Let $B_X(p, r)$ denote an open ball of radius $r$
at $p \in X$.
Let $B_Y(p, r)$ denote an open ball of radius $r$
at $p \in Y$.
Then

$$
B_Y(p, r) = B_X(p, r) \cap Y.
$$
```

```{prf:proof}
We recall that

$$
B_X(p,r)  = \{y \in X \ST d(p, y) < r\}.
$$
Similarly,

$$
B_Y(p,r) = \{y \in Y \ST d(p, y) < r\}.
$$

We first show that $B_Y(p, r) \subseteq B_X(p, r) \cap Y$

1. Let $y \in B_Y(p, r)$.
1. Then $y \in Y \subseteq X$ and $d(p, y) < r$.
1. Hence $y \in B_X(p, r) \cap Y$.

We now show that $B_X(p, r) \cap Y \subseteq B_Y(p, r)$.
1. Let $y \in B_X(p, r) \cap Y$.
1. Then $y \in Y$ and $y \in X$ and $d(p, y) < r$.
1. Hence $y \in Y$ and $d(p, y) < r$.
1. Hence $y \in B_Y(p, r)$.
```

## Open Sets

```{prf:theorem} Open sets in the metric subspace
:label: res-ms-subspace-open 

Let $(Y,d)$ be a metric subspace of $(X,d)$. Let $S \subseteq Y$.
Then $S$ is open in $(Y,d)$ if and only if $S = O \cap Y$ where $O$ 
is an open subset of $(X,d)$.
```

```{prf:proof}
A subset $S$ of $Y$ is open in $(Y, d)$ if for every
$x \in S$, there exists an open ball $B_Y(x, r) \subseteq S \subseteq Y$.

Assume that $S = O \cap Y$ where $O$ is open in $X$.

1. Let $x \in S$.
1. Then $x \in O$ and $x \in Y$.
1. Since $O$ is open in $X$, hence there is an open ball $B_X(x, r) \subseteq O$.
1. Then $B_X(x, r) \cap Y \subseteq O \cap Y = S$.
1. By {prf:ref}`res-ms-subspace-open-balls`, 

   $$
   B_X(x, r) \cap Y = B_Y(x, r)
   $$
   is an open ball in the metric subspace $(Y, d)$ of radius $r > 0$ around
   $x \in Y$.
1. Hence $S$ is open in $(Y, d)$.

For the converse, assume that $S$ is open in $Y$.
1. For every $x \in S$, there is an open ball $B_Y(x, r_x) \subseteq S$.
1. Hence $\bigcup_{x \in S} B_Y(x, r_x) \subseteq S$.
1. Also, $x \in B_Y(x, r_x)$ implies that $S \subseteq \bigcup_{x \in S} B_Y(x, r_x)$.
1. Thus, $S = \bigcup_{x \in S} B_Y(x, r_x)$.
1. By {prf:ref}`res-ms-subspace-open-balls`

   $$
   B_Y(x, r_x) = B_X(x, r_x) \cap Y
   $$
   for every $x \in S$.
1. Define $T = \bigcup_{x \in S}B_X(x, r_x)$.
1. Then $T$ is a union of open balls of $X$.
1. Hence $T$ is open in $X$.
1. Also 

   $$
   S &= \bigcup_{x \in S} B_Y(x, r_x) \\
   &=  \bigcup_{x \in S}(B_X(x, r_x) \cap Y) \\
   &= (\bigcup_{x \in S} B_X(x, r_x)) \cap Y \\
   &= T \cap Y.
   $$
1. Hence $S = T \cap Y$ where $T$ is an open set of $(X, d)$.
```

```{prf:example}
:label: ex-ms-semiclosed-set-as-open-in-subspace

* $[0, 1)$ is open in the metric space $\RR_+$.
```

## Subspace Topology

Recall from {prf:ref}`def-ms-topology`
that a topology on a set $S$ is a collection
of sets $T$ such that
1. Empty set and the whole set are elements of $T$.
1. $T$ is closed under arbitrary union.
1. $T$ is closed under finite intersection.


```{prf:theorem} The subspace topology
:label: res-ms-subspace-topology

Let $(Y, d)$ be a metric subspace of $(X, d)$.
The open sets of the $(Y, d)$ form a topology.

1. $\EmptySet$ is open in $(X, d)$.
1. Hence $\EmptySet \cap Y = \EmptySet$ is open in $(Y, d)$.
1. $X$ is open in $(X, d)$.
1. Hence $X \cap Y = Y$ is open in $(Y, d)$.
1. Let $\{ A_i \ST i \in I \}$ be a family of open sets of $(Y, d)$.
1. Then $A_i = B_i \cap Y$ for every $i \in I$ with $B_i$ open in $X$.
1. Let $B  = \bigcup B_i$. Then $B$ is open in $(X, d)$.
1. But $\bigcup A_i = \bigcup( B_i \cap Y) = (\bigcup B_i) \cap Y = B \cap Y$.
1. Since $B$ is open in $(X, d)$, hence $B \cap Y$ is open in $(Y, d)$.
1. Let $\{ A_1, \dots, A_n \}$ be a finite collection of open sets of $(Y, d)$.
1. Then $A_i = B_i \cap Y$ for every $i \in [1,\dots,n]$ such that
   $B_i$ is open in $(X, d)$.
1. Then $\bigcap A_i = \bigcap (B_i \cap Y) = (\bigcap B_i) \cap Y$.
1. Since $\bigcap B_i$ is open in $(X, d)$ (a finite intersection),
   hence $\bigcap A_i$ is open in $(Y, d)$.
```




## Closed Sets

```{prf:theorem} Closed sets in subspace topology
:label: res-ms-subspace-closed 

Let $Y$ be a metric subspace of $X$. Let $S \subseteq Y$.

$S$ is closed in $Y$ if and only if
$S = C \cap Y$ where
$C$ is a closed subset of $X$.
```

```{prf:proof} 

Let $S$ be closed in $Y$.

1. Then, $Y \setminus S$ is open in $Y$.
1. By definition of subspace topology,
   
   $$
   Y \setminus S = Y \cap O
   $$
   where $O$ is some open subset of $X$.
1. Then,

   $$
   S &= Y \setminus (Y \setminus S) \\
   &= Y \setminus (Y \cap O) \\
   &= Y \setminus O \\
   &= Y \cap (X \setminus O).
   $$
1. But $C = X \setminus O$ is closed in $X$.
```
