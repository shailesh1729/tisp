# Special Topics

This section covers details on specific functions
from the perspective of metric spaces


## Distance from a Point

```{prf:theorem} Distance function is uniformly continuous
:label: res-ms-dist-func-uniform-continuous

Let $(X,d)$ be a metric space. Fix some point $a \in X$.
Define a function $f: X \to \RR$ as:

$$
f(x) = d(x, a) \Forall x \in X.
$$
Then, $f$ is
{prf:ref}`uniformly continuous <def-ms-uniform-cont-real-valued>`
on $X$.
```

```{prf:proof}
Let $x, y \in X$.
Recall from 
{prf:ref}`triangle inequality <res-ms-triangle-ineq-2nd-form>` that:

$$
|d (x, a)  - d(y, a)| \leq d(x,y).
$$

1. Let $\epsilon > 0$.
1. Choose $\delta = \epsilon$.
1. Assume $d(x, y) < \delta$. 
1. Then

   $$
   |f(x) - f(y)| = |d (x, a)  - d(y, a)| \leq d(x,y) < \delta = \epsilon.
   $$
1. Thus, $d(x,y) < \delta \implies |f(x) - f(y)| < \epsilon$.
1. Thus, $f$ is uniformly continuous.
```


## Distance from a Set

Recall from {prf:ref}`def-ms-point-set-distance`
that the distance between a point $x \in X$ and
a set $A \subseteq X$ is given by:

$$
d(x, A) = \inf \{ d(x,a) \Forall a \in A \}.
$$

```{prf:proposition} Distance from a singleton set
:label: res-ms-singleton-dist

For every $x, y \in X$, 

$$
d(x, \{ y \}) = d(x, y).
$$
```
```{prf:proof}
Let $A = \{ y \}$ be a singleton set.
Then

$$
d(x, A) = d(x, \{ y \})  = \inf\{ d(x, y) \} = d(x, y).
$$
```

```{prf:proposition} Distance from a subset
:label: res-ms-subset-dist

Let $\EmptySet \neq A \subseteq B \subseteq X$. 
Then, for any $x \in X$

$$
d(x, A) \geq d(x, B).
$$
```

```{prf:proof}
We note that since $A \subseteq B$, hence:

$$
\{ d(x,a) \Forall a \in A \} \subseteq \{ d(x,a) \Forall a \in B \}.
$$
The infimum over a larger set is smaller. Hence,

$$
d(x, B) \leq d(x, A).
$$
```

```{prf:proposition} Distance from a containing subset
:label: res-ms-set-dist-within

Let $x \in A \subseteq X$. Then

$$
d(x, A) = 0.
$$
```

```{prf:proof}
We note that:

$$
d(x, x) \in \{ d(x,a) \Forall a \in A \}
$$
since $x \in A$.

Thus, 

$$
d(x,A) = d(x, x) = 0.
$$
```

```{prf:theorem} Continuity of set distance function
:label: res-ms-set-distance-continuous

Let $A \subseteq X$ be nonempty.
Then, the function $f: X \to \RR$ given by:

$$
f(x) = d(x, A) = \inf \{ d(x,a) \Forall a \in A \}
$$
is continuous. 
```

We provided a proof in {prf:ref}`ex-ms-cont-set-distance`.
We rephrase it here.
```{prf:proof}
Let $a \in X$.
We shall show that $f$ is continuous at $a$.

1. Let $r > 0$.
1. Consider the open ball/interval $V = B(f(a), r)$ in $\RR$.
1. Consider the open ball in $X$ given by $U = B(a, r)$.
1. Let $x \in U$ and let $y \in A$.
1. Then, using triangle inequality:
   
   $$
   d(a, y) + d(x, a) \geq d(x, y)
   $$
   and

   $$
   d(a, x) + d(x, y) \geq d(a, y).
   $$
1. Taking the infimum over $y \in A$ in both the inequalities,
   we get:

   $$
   d(a, A) + d(x, a) \geq d(x, A)
   $$
   and

   $$
   d(x, a) + d(x, A) \geq d(a, A).
   $$

1. Rewriting it further, we get:

   $$
   d(x, A) \leq d(a, A) + d(x, a) 
   $$
   and

   $$
   d(a, A) - d(x, a) \leq d(x, A).
   $$

1. Since $d(a,x) < r$, hence, we obtain:

   $$
   d(a, A) - r < d(x, A) < d(a, A) + r.
   $$

1. Substituting $f(x) = d(x, A)$ and $f(a) = d(a, A)$,

   $$
   f(a) - r < f(x) < f(a) + r.
   $$
1. Thus, $f(x) \in B(f(a), r) = V$.
1. In other words, $f(U) \subseteq V$.

We have shown that for every $r > 0$, there exists
$\delta = r$ such that 
$x \in B(a, \delta)$ implies $f(x) \in B(f(a), r)$.
Thus, $f$ is continuous at $a$.
```


```{prf:theorem} Open neighborhoods of a set
:label: res-ms-set-distance-open-neighborhoods

Let $A \subseteq X$ be nonempty.
Let $\epsilon > 0$ and consider the set $A_{\epsilon}$ given by

$$
A_{\epsilon} = \{x \in X \ST d(x, A) < \epsilon \}.
$$
Then $A_{\epsilon}$ is open for every $\epsilon > 0$.
```


```{prf:proof}
We established in {prf:ref}`res-ms-set-distance-continuous`
that $f(x) = d(x, A)$ is continuous.
The set $A_{\epsilon}$ is the inverse image of the open interval
$(-\epsilon, \epsilon)$ in $\RR$.
Since $f$ is continuous, hence the inverse image of an 
open interval is an open set.

Following is a direct proof.

1. Let $x \in A_{\epsilon}$. 
1. Then, there is $y \in A$ such that $d(x, y) < \epsilon$.
1. Let $\delta > 0$ be small enough such that $d(x,y) + \delta < \epsilon$.
1. Consider the open ball $B(x, \delta)$. 
1. For all $z \in B(x, \delta)$, we have:

   $$
   d(z, y) \leq d(z, x) + d(x, y) < \delta + d(x,y) < \epsilon.
   $$
1. Thus, $d(z, A) < \epsilon$ since $y \in A$.
1. Thus, $z \in A_{\epsilon}$.
1. Thus, $B(x, \delta) \subseteq A_{\epsilon}$.
1. Thus, $A_{\epsilon}$ is open.
```

```{prf:theorem} Closure and set distance
:label: res-ms-closure-zero-dist

Let $A \subseteq X$ be a nonempty set.
Then, for any $x \in X$, 
$d(x, A) = 0$ if and only if $x \in \closure A$.

In other words, the distance of a point from a set is
zero if and only if the point is a closure point of the set.
```

```{prf:proof}
Let $x \in \closure A$. 

1. Then either $x \in A$ or $x \in \boundary A$. 
1. If $x \in A$, then by {prf:ref}`res-ms-set-dist-within`,
   $d(x,A) = 0$.
1. Now, assume $x \notin A$ and $x \in \boundary A$.
1. Let $r > 0$. 
1. Since $x \in \boundary A$, hence there exists
   $y \in A$ such that $d(x, y) < r$.
1. Therefore, 

   $$
   d(x, A) = \inf \{d (x, y) \ST y \in A \} < r.
   $$
1. Since this is true for every $r > 0$, hence $d(x, A) = 0$.

Now assume that $x \notin \closure A$. 

1. Thus, there exists an open ball $B(x, r)$ for some $r > 0$
   such that $B(x, r) \cap A = \EmptySet$.
1. Therefore, for every $a \in A$, $d(x, a) \geq r > 0$. 
1. Therefore, 

   $$
   d(x, A) = \inf \{ d(x, a) \ST a \in A \} \geq r > 0.
   $$
```


```{prf:corollary}
:label: res-ms-closed-zero-dist

Let $A \subseteq X$ be a nonempty closed set.
Then, for any $x \in X$, 
$d(x, A) = 0$ if and only if $x \in A$.
```

```{prf:proof}
A closed set contains all its closure points.
Thus, $d(x, A) = 0$ if and only if $x$ is a closure point of $A$
if and only if $x \in A$.
```

```{prf:theorem} Distance minimizer in a compact set
:label: res-ms-set-distance-compact-min

Let $A$ be a nonempty compact subset of $X$.
Let $x \in X$. Then, there exists an $a \in A$ such that

$$
d(x, A) = d(x, a).
$$
```

```{prf:proof}
For a fixed $x \in X$, consider the
real valued function $f : X \to \RR$ given by:

$$
f(y) = d(y, x) \Forall y \in X.
$$
Then, $f$ is continuous as it is a distance function
from a singleton set $\{ x \}$. 

Hence, $f(A)$ attains a minimum value at some $a \in A$.
See {prf:ref}`res-ms-compact-real-valued-min-max-attain`.
```


```{prf:theorem} Distance minimizer in a closed set
:label: res-ms-set-distance-closed-min

Let $X$ be a Euclidean metric space.
Let $A \subseteq X$ be a nonempty closed set.
Let $x \in X$. Then, there exists an $a \in A$ such that

$$
d(x, A) = d(x, a).
$$

In other words, the infimum of the distance between
$x$ and points of $A$ is realized at a point in $A$.
```


```{prf:proof}
Since $A$ is nonempty, we can pick some $b \in A$ and
compute $r = d(x, b)$.
Clearly,

$$
d(x,A) \leq d(x, b) = r.
$$

Consider the set 

$$
C = \{a \in A  \ST d(x, a) \leq d(x, b) = r\} = A \cap B[x,r].
$$
In other words, $C$ is the intersection of $A$ and the closed
ball $B[x,r]$ centered at $x$ and of radius $r$.
Since $A$ is closed and $B[x,r]$ is closed, hence
$C$ is closed.

It is easy to see that

$$
d(x,A) = d(x, C).
$$

For any points $u,v \in C$, we have:

$$
d(u, v) \leq d(u, x) + d(x, v) \leq r + r = 2 r.
$$
Thus, $C$ is closed and {prf:ref}`bounded <def-ms-boundedness-set>`.
By {prf:ref}`Heine-Borel theorem <res-ms-heine-borel-euclidean>`,
$C$ is compact.

Now, for a fixed $x \in X$, consider the
function $f : X \to \RR$ given by:

$$
f(y) = d(y, x) \Forall y \in X.
$$
Then, $f$ is continuous. 

1. By {prf:ref}`res-ms-compact-continuous-map`, $f(C)$ is compact
   (continuous images of compact sets are compact).
1. But $f(C) \subseteq \RR$.
1. Hence, $f(C)$ is closed and bounded as $\RR$ is Euclidean
   (Heine-Borel theorem).
1. Hence, $f(C)$ attains a minimum value at some $a \in C$.
   See {prf:ref}`res-ms-compact-real-valued-min-max-attain`.
```
