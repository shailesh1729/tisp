(sec:cvx:cone)=
# Cones

Main references for this section are 
{cite}`beck2014introduction,boyd2004convex,rockafellar2015convex`. 


Throughout this section, $\VV$ is a real vector space. 
Some material is specific to $\RR^n$. Rest of the
material is applicable for any real vector space.
Wherever necessary, 
$\VV$ is endowed with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \| : \VV \to \RR$
or a {prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle : \VV \times \VV \to \RR$. 
It is also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$.
The norm in general is not necessarily induced by the inner product
(if the vector space is indeed endowed with an inner product).

We start with the basic definition of a cone.

## Cones

```{index} Cone
```
````{prf:definition} Cone
:label: def-cone

A set $C$ is called a *cone* or *nonnegative homogeneous*, 
if for every $\bx \in C$
and $t \geq 0$, we have $t \bx \in C$.

In other words, a set is a cone if it is closed under
nonnegative scalar multiplication.
````

* By definition we have $\bzero \in C$.
* Some authors ({cite}`rockafellar2015convex`) prefer to restrict 
  the definition to $t > 0$
  thus the origin is not included in the cone by default.
* In our definition, a cone always includes the origin.
* Thus, a cone is always nonempty.
* When we think of cones, ice-cream cones naturally come 
  to mind. Hence, we kind of think that cones happen
  to be pointed (at origin) and emanate in one 
  general direction from there.
  However, our definition above is more general. 
  It allows for lines (passing through origin)
  and linear subspaces to be cones too.
* Pointed cones are a special class of cones
  which are discussed {prf:ref}`below <def-pointed-cone>`.
  An ice-cream cone is a pointed cone.


## Properties of Cones

### Intersection

```{prf:property} Intersection of cones
:label: res-cone-intersection

Let $\{ C_ i \ST i \in I \}$ be a collection of cones.
Then their intersection $\bigcap_{i \in I} C_i$ is a cone. 
```

```{prf:proof}
Let $\bx \in \bigcap_{i \in I} C_i$ and let $t \geq 0$.

1. $\bx \in C_i$ for every $i \in I$.
1. Hence $t \bx \in C_i$ for every $i \in I$ since every $C_i$ is a cone.
1. Hence $t \bx \in \bigcap_{i \in I} C_i$.
1. Hence $\bigcap_{i \in I} C_i$ is a cone.
```

### Cartesian Product

```{prf:property} Cartesian product of cones
:label: res-cone-cartesian-product

Let $\VV$ and $\WW$ be real vector spaces.
Let $C_1 \subseteq \VV$ and $C_2 \subseteq \WW$ be cones.
Then their Cartesian product $C_1 \times C_2$ is a cone. 
```

```{prf:proof}
Let $\bx \in C_1 \times C_2$ and $t \geq 0$.

1. Then there exist $\by \in C_1$ and $\bz \in C_2$ 
   such that $\bx = (\by, \bz)$.
1. Then $t \by \in C_1$ and $t \bz \in C_2$ since both are cones.
1. Hence $(t \by, t \bz) \in C_1 \times C_2$.
1. But $(t \by, t \bz)  = t(\by, \bz) = t \bx$.
1. Hence $t \bx \in C_1 \times C_2$.
1. Hence $C_1 \times C_2$ is a cone.
```


### Set Addition


```{prf:property} Set addition of cones
:label: res-cone-set-addition

Let $C_1, C_2 \subseteq \VV$ be cones.
Then their vector sum $C_1 + C_2$ is a cone. 
```

```{prf:proof}
Let $\bx \in C_1 + C_2$ and $t \geq 0$.

1. Then there exist $\bx_1 \in C_1$ and $\bx_2 \in C_2$ such that
   $\bx = \bx_1 + \bx_2$.
1. Then $t \bx_1 \in C_1$ and $t \bx_2 \in C_2$ since they are cones.
1. Hence $t \bx = t (\bx_1 + \bx_2) = t \bx_1 + t \bx_2 \in C_1 + C_2$.
1. Hence $C_1 + C_2$ is a cone.
```

### Closure

```{prf:property} Closure 
:label: res-cone-closure

Let $C \subseteq \VV$ be a cone.
Then its closure $\closure C$ is a cone. 
```

```{prf:proof}
Let $\bx \in \closure C$ and $t \geq 0$.

1. Then there exists a sequence $\{ \bx_k \}$ of $C$
   such that $\bx_k \to \bx$.
1. Then $t \bx_k \in C$ for every $k$ since $C$ is a cone.
1. Consider the sequence $\{ t \bx_k \}$ of $C$.
1. We have $\lim_{k \to \infty} t \bx_k = t \bx$.
1. Hence $t \bx \in \closure C$.
1. Hence $\closure C$ is a cone.
```


### Linear Transformation

```{prf:property} Linear transformation 
:label: res-cone-lin-op

The image and inverse image of a  cone under a linear transformation
is a cone.
```


```{prf:proof}
Let $\VV$ and $\WW$ be real vector spaces and
$\bT : \VV \to \WW$ be a linear transformation.

Image of a cone is a cone.

1. Let $C \in \VV$.
1. Let $D = \bT(C)$.
1. Let $\bv \in D$ and $t \geq 0$.
1. Then there exists $\bu \in C$ such that $\bv = \bT(\bu)$.
1. Since $C$ is a cone, hence $t \bu \in C$.
1. Then $\bT(t \bu) = t \bT(\bu) = t \bv \in D$.
1. Hence $D$ is a cone.


Inverse image of a cone is a cone.

1. Let $D \in \WW$.
1. Let $C = \bT^{-1}(D)$.
1. Let $\bx \in C$ and $t \geq 0$.
1. Then $\by = \bT (\bx) \in D$.
1. Also $\bT (t \bx) =  t \bT (\bx) = t \by \in D$ since $D$ is a cone.
1. Hence  $t \bx \in C$.
1. Hence $C$ is a cone.
```

## Convex Cones

```{index} Convex cone
```
````{prf:definition} Convex cone
:label: def-convex-cone

A set $C$ is called a *convex cone* if it is convex and a cone.
````

````{prf:example} Convex cones
:label: ex-cvx-convex-cone-examples

*  A ray with its base at origin is a convex cone.
*  A line passing through origin is a convex cone.
*  A plane passing through origin is a convex cone.
*  Any subspace is a convex cone.
````

```{prf:theorem} Subspace as convex cone
:label: res-cvx-subspace-convex-cone

A linear subspace is a convex cone.
```

```{prf:proof}
Let $V \subseteq \VV$ be a subspace. 
We know that $V$ is convex since $V$ contains
all its linear combinations and every 
convex combination is a linear combination.
Now, let $\bv \in V$. Then, $t \bv \in V$
for every $t \geq 0$ since $V$ is closed
under scalar multiplication. Thus, $V$ is a cone too.
Thus, $V$ is a convex cone.
```

```{prf:theorem} Half spaces as convex cone
:label: res-cvx-half-space-convex-cone

Let $\VV$ be a real vector space.
Let $\ba \in \VV^*$. Consider the set

$$
H = \{ \bx \in \VV \ST \langle \bx, \ba \rangle \leq 0 \}.
$$
Then $H$ is a convex cone.
```

```{prf:proof}
Half space as a cone

1. Let $\bx \in H$ and $t \geq 0$.
1. Then $\langle t \bx, \ba \rangle = t \langle \bx, \ba \rangle \leq 0$.
1. Hence $t \bx \in H$.


Half space as convex

1. Let $\bx, \by \in H$ and $t \in [0,1]$.
1. Then 

  $$
  \langle t \bx + (1-t)\by, \ba \rangle = t \langle \bx, \ba \rangle
  + (1-t)\langle \by, \ba \rangle \leq 0.
  $$
1. Hence $H$ is convex.
```


### Characterization

```{prf:theorem} Convex cone characterization
:label: res-convex-cone-characterization

A set is a convex cone if and only if it is closed under addition
and nonnegative scalar multiplication.

In other words, $C$ is a convex cone if and only if
for every $\bx_1, \bx_2 \in C$ and $t_1, t_2 \geq 0$,
the following holds true:

$$
    t_1 \bx_1 + t_2 \bx_2 \in C.
$$
```

```{prf:proof}
Let $C \subseteq \VV$. Let $\bx_1, \bx_2 \in C$.

If $C$ is a convex cone, then:
1. $\bx = \frac{1}{2} \bx_1 + \frac{1}{2} \bx_2 \in C$.
1. But then, $2 \bx = \bx_1 + \bx_2 \in C$ since $C$ is a cone.
1. Thus, $C$ is closed under addition.
1. $C$ being a cone, it is closed under nonnegative scalar multiplication.
1. Combining, we see that $t_1 \bx_1 + t_2 \bx_2 \in C$.

Now, assume that $C$ is closed under addition and
nonnegative scalar multiplication.

1. $C$ is a cone since it is closed under nonnegative scalar multiplication.
1. In particular $t \bx_1 \in C$ for all $t \in [0,1]$
   and $(1-t) \bx_2 \in C$ for all $t \in [0,1]$.
1. Since $C$ is closed under addition, hence $t \bx_1 + (1-t) \bx_2 \in C$
   for all $t \in [0,1]$.
1. Thus, $C$ is convex too. 
```

```{prf:theorem} Set addition characterization
:label: res-convex-cone-set-addition-charac

A cone $C$ is convex if and only if $C + C \subseteq C$.
```

```{prf:proof}
Assume that a cone $C$ satisfies $C + C \subseteq C$.

1. Let $\bx, \by \in C$ and $t \in [0,1]$.
1. Since $C$ is a cone, hence $t \bx$ and $(1-t) \by$ belong to $C$.
1. Hence $t \bx + (1-t) \by \in C + C \subseteq C$.
1. Hence $C$ is convex.

For converse, assume that $C$ is a convex cone.

1. Let $\bx, \by \in C$.
1. Since $C$ is a cone, hence $2 \bx, 2 \by \in C$.
1. Since $C$ is convex, hence

   $$
   \frac{1}{2} 2 \bx + \frac{1}{2} 2 \by = \bx + \by \in C.
   $$
1. Hence $C + C \subseteq C$.
```

### Intersection of Convex Cones


````{prf:theorem} Intersection of arbitrary collection of convex cones
:label: res-cvx-convex-cone-inf-intersect

Let $\{ A_i\}_{i \in I}$ be a family of sets such that 
$A_i$ is a convex cone
for all $i \in I$.  Then $\cap_{i \in I} A_i$ is a convex cone.
````

````{prf:proof}
Let $\bx_1, \bx_2$ be any two arbitrary elements in $A = \cap_{i \in I} A_i$.

$$
&\bx_1, \bx_2 \in A\\
\implies & \bx_1, \bx_2 \in A_i \Forall i \in I\\
\implies &t_1 \bx_1 + t_2 \bx_2 \in A_i \Forall t_1, t_2 \geq 0 \Forall i \in I
\text{ since $A_i$ is a convex cone}\\
\implies &t_1 \bx_1 + t_2 \bx_2 \in A.
$$

Hence $A$ is a convex cone.
````

As a consequence, an arbitrary intersection of 
half-spaces (at origin) and hyperplanes (at origin) is a convex
cone.
Thus, the solution set of a system of linear equations and
inequalities is a convex cone if the equations and 
inequalities are homogeneous.

### Containing and Contained Subspaces

```{prf:theorem} Containing and contained subspaces
:label: res-cvx-convex-cone-containing-contained-subspaces

Let $C$ be a convex cone. Then, there is a smallest linear subspace
containing $C$ given by:

$$
U \triangleq C - C = \{ \bx - \by \ST \bx, \by \in C\} = \affine C.
$$

And, there is a largest linear subspace contained in $C$ given by

$$
L \triangleq (-C) \cap C.
$$
```

```{prf:proof}
We show that $U = C - C$ is a subspace containing $C$.

Since $\bzero \in C$, hence $\bzero = \bzero - \bzero \in U$.
Also, this means that $C - \bzero = C \subseteq U$.

Let $\bu, \bv \in U$. 

1. $\bu = \bx - \by$ for some $\bx, \by \in C$.
1. $\bv = \bz - \bw$ for some $\bz, \bw \in C$.
1. $\bu + \bv = (\bx + \bz) - (\by + \bw)$.
1. Since $C$ is a convex cone, it is closed under addition.
1. Hence, $\bx + \bz, \by + \bw \in C$.
1. Hence, $\bu + \bv \in U$ (as it is a difference of two vectors in $C$).
1. Thus, $U$ is closed under vector addition.

Let $t \in \RR$, $\bu \in U$.

1. $\bu = \bx - \by$ for some $\bx, \by \in C$.
1. $ t \bu = t\bx - t \by$.
1. If $t \geq 0$, then $t \bx, t \by \in C$, thus $t \bu \in U$.
1. If $t < 0$, then $-t\bx, -t\by \in C$. 
   We can write $t \bu = (-t \by) - (-t \bx)$. Thus, $t \bu \in U$.
1. Thus, $U$ is closed under scalar multiplication.

Next, we show that it is the smallest subspace containing $C$.

1. Let $V$ be a subspace that contains $C$
1. Then $V$ contains $-C$ also.
1. Then, $V$ contains $C + (-C) = C- C = U$ also.
1. Thus, $U$ is the smallest subspace containing $C$. 


In summary,
$C$ is closed under addition and nonnegative scalar multiplication.
$C$ contains $\bzero$. To be a subspace, a set must be closed under
multiplication by $-1$ too. $C - C$ is the smallest such subspace.

Since $C$ contains $\bzero$, 
hence its affine hull contains $\bzero$ too.
Thus, its affine hull must be a linear subspace.
The affine hull then is the smallest subspace containing $C$.
Thus, 

$$
\affine C = C - C.
$$


We show that $L = (-C) \cap C$ is a subspace contained in $C$.

[zero vector]

1. Since $\bzero \in C$ and $\bzero \in -C$, hence $\bzero \in L$.

[Scalar multiplication]

1. Let a nonzero $\bx \in L$. Then, $\bx \in C$ and $\bx \in -C$.
1. $\bx \in -C \implies -\bx \in C$.
1. $\bx \in C \implies -\bx \in -C$.
1. This means that $-\bx \in C$ and $-\bx \in -C$ too. 
1. Thus, $-\bx \in L$.
1. In summary $\bx \in L$ implies $\bx, -\bx \in C$ and $\bx, -\bx \in C$.
1. Then, for any $t \geq 0$
   1. $\bx \in C \implies t \bx \in C$.
   1. $-\bx \in C \implies - t\bx \in C$.
   1. $-t \bx \in C \implies t \bx \in -C$.
   1. Thus, $t \bx \in L$.
1. And, for any $t < 0$
   1. $\bx \in C \implies -t \bx \in C$.
   1. $-\bx \in C \implies t \bx \in C$.
   1. $-t \bx \in C \implies t \bx \in -C$.
   1. Thus, $t \bx \in L$.
1. Thus, $L$ is closed under scalar multiplication.

[Vector addition]

1. Let $\bu, \bv \in L$.
1. Then, $\bu, \bv \in C$ and $\bu, \bv \in -C$.
1. Thus, $-\bu, -\bv \in C$.
1. Since $C$ is closed under addition, hence $\bu + \bv \in C$
   and $-\bu - \bv \in C$.
1. But then, $-\bu -\bv \in -C$ and $\bu + \bv \in -C$.
1. Thus, $\bu + \bv \in L$. $-\bu -\bv \in L$ too.
1. Thus, $L$ is closed under addition.

Thus, $L$ is a vector space contained in $C$.
$L$ is the largest such subspace since any subspace contained
in $C$ should be contained in $-C$ too.
```

## Conic Combinations

```{index} Conic combination
```
````{prf:definition} Conic combination
:label: def-conic-combination

A point of the form $t_1 \bx_1 + \dots + t_k \bx_k $ with
$t_1 , \dots, t_k \geq 0$ is called a *conic combination*
(or a *non-negative linear combination*) of $\bx_1,\dots, \bx_k$.
````

* A convex cone is closed under non-negative linear/conic combinations.
* One way to prove that a set is a convex cone is to show that it
  contains all its conic combinations.


````{prf:theorem} Convex cone characterization with conic combinations
:label: res-cvx-convex-cone-conic-combs

Let $C$ be a convex cone. Then for every $\bx_1, \dots, \bx_k \in C$,
every conic combination $t_1 \bx_1 + \dots + t_k \bx_k $ with
$t_i \geq 0$ belongs to $C$.

Conversely, if a set $C$ contains all conic combinations of its
points, then it is a convex cone.

In other words, $C$ is a convex cone if and only if it is
closed under conic combinations.
````

```{prf:proof}

Assume that $C$ is a convex cone.
Then it is closed under addition and nonnegative scalar multiplication.

1. Let $\bx_1, \dots, \bx_k \in C$.
1. Then, $t_1 \bx_1, \dots, t_k \bx_k \in C$ for all $t_1,\dots, t_k \geq 0$
   since $C$ is closed under nonnegative scalar multiplication.
1. Then, $t_1 \bx_1 + \dots + t_k \bx_k \in C$ since $C$ is closed
   under addition.
1. Thus, $C$ contains all its conic combinations.


For the converse, assume that $C$ contains all its conic combinations.

1. Let $\bx \in C$.
1. Then, $t \bx \in C$ for all $t \geq 0$ since $t \bx$
   is a conic combination.
1. Thus, $C$ is a cone.
1. Now, let $\bx, \by \in C$ and $t \in [0,1]$. Then, $1-t \in [0,1]$ too.
1. Thus, $t \bx + (1-t) \by$ is a conic combination of $\bx, \by$.
1. Hence, $t \bx + (1-t) \by \in C$.
1. Thus, $C$ is convex.
1. Combining, $C$ is a convex cone.  
```

Here is another proof that a linear subspace is a convex cone
using the idea of conic combinations.

1. Every subspace contains the $\bzero$ vector. 
1. Every conic combination is also a linear combination.
1. A subspace is closed under linear combinations.
1. Hence, it is also closed under conic combinations.
1. Hence, it is a convex cone.


```{prf:remark} Conic combinations and nonnegative orthant
:label: rem-cvx-conic-comb-coef-nng

We recall that the nonnegative orthant of $\RR^k$ is given by

$$
\RR_+^k = \{ \bt \in \RR^k \ST  \bt \succeq \bzero \}
= \{\bt \in \RR^k \ST  t_1, \dots, t_k \geq 0 \}.
$$
Thus, the coefficients for conic combinations of $k$ points
are drawn from $\RR_+^k$.
```


```{prf:theorem}
:label: res-cvx-conic-comb-conic-comb

A conic combination of conic combinations is a conic combination.
```

```{prf:proof}
Let $S \subseteq \VV$. Note that $S$ is arbitrary (no convexity 
or conic structure assumed).

1. Consider $n$ points $\by_i$, $i=1,\dots, n$ described as below.
1. Let $\by_i = \sum_{j=1}^{m_j}t_{i,j} \bx_{i,j}$ be conic combinations
   of $m_j$ points: 
   * $\bx_{i,1}, \dots, \bx_{i,m_j} \in S$.
   * $t_{i,j} \geq 0$. 
1. Consider the conic combination $\by = \sum_{i=1}^n r_i \by_i$.
   with $r_i \geq 0$.
1. We need to show that $\by$ is a conic combination of points of $S$.

Towards this:

$$
\by &= \sum_{i=1}^n r_i \by_i\\
&= \sum_{i=1}^n r_i \sum_{j=1}^{m_j}t_{i,j} \bx_{i,j}\\
&= \sum_{i=1}^n \sum_{j=1}^{m_j} r_i t_{i,j} \bx_{i,j}.
$$

Consider the terms:

$$
s_{i, j} =  r_i t_{i,j}.
$$

Since $r_i \geq 0$ and $t_{i, j} \geq 0$, hence $s_{i, j } \geq 0$.
Hence,

$$
\by = \sum_{i,j} s_{i, j} x_{i, j}
$$
is a conic combination of points of $S$.
```

The idea of conic combinations can be generalized to infinite sums
and integrals.



## Conic Hulls

```{index} Conic hull
```
````{prf:definition} Conic hull
:label: def-conic-hull

The *conic hull* of a set $S$ is the set of all conic combinations
of points in $S$. i.e.

$$
    \ConicHull(S) \triangleq 
    \{t_1 \bx_1 + \dots t_k \bx_k \ST \bx_i \in S, \bt \in \RR^k_+, 
      i = 1, \dots, k, k \in \Nat\}.
$$
````

```{prf:property}
:label: res-cvx-conic-hull-convex

A conic hull is a convex cone.
```

```{prf:proof}
Let $C$ be the conic hull of a set $S$.

1. Let $\bx, \by \in C$.
1. Then, $\bx, \by$ are conic combinations of $S$.
1. Let $\bz = t_1 \bx + t_2 \by$ with $t_1, t_2 \geq 0$.
1. Then, $\bz$ is a conic combination of conic combinations of $S$.
1. By {prf:ref}`res-cvx-conic-comb-conic-comb`,
   $\bz$ is a conic combination of $S$.
1. Since $C$ contains all conic combinations of $S$, hence $C$ contains $\bz$.
1. Thus, for any $\bx, \by \in C$, $\bz = t_1 \bx + t_2 \by$ with $t_1, t_2 \geq 0$ is in $C$.
1. Thus, $C$ is a convex cone.
```

```{prf:property}
:label: res-cvx-conic-hull-smallest

Conic hull of a set is the smallest convex cone that contains the set.
```

```{prf:proof}

Let $S$ be an arbitrary set and $C$ be its conic hull.

1. We have already shown that $C$ is a convex cone.
1. Assume $D$ to be a convex cone such that $S \subseteq D$.
1. Then, $D$ contains every conic combination of $S$ since a convex cone
   is closed under conic combinations.
1. Thus, $C \subseteq D$ since $C$ is the set of all conic combinations of $S$. 
```

```{prf:theorem} Conic hull of a convex set
:label: res-cvx-conic-hull-convex-set

Let $C$ be a convex set. Let $K$ be defined as:

$$
K \triangleq \{ t \bx \ST t \geq 0, \bx \in C\}.
$$
Then, $K$ is the conic hull of $C$.
```

```{prf:proof}
Let $H$ be the conic hull of $C$; i.e.,
$H$ is the set of all conic combinations of $C$.
We show that $K \subseteq H$ and $H \subseteq K$.

$K \subseteq H$

1. For any $\bx \in C$ and $t \geq 0$, $t \bx$ is a conic
   combination of $C$.
1. Hence $t \bx \in H$.
1. Thus, $K \subseteq H$.

$H \subseteq K$

1. Let $ \bx = t_1 \bx_1 + \dots + t_k \bx_k$ be a conic combination of $C$.
1. Thus, $t_i \geq 0$ and $\bx_i \in C$.
1. By definition of $K$, $\bzero \in K$.
1. If $t_i = 0$ for $0 \leq i \leq k$, then $\bx = \bzero$. So $\bx \in K$.
1. Now consider the case where at least one $t_i > 0$.
1. Let $t = \sum t_i$. Clearly, $t > 0$.
1. Consider $\bz = \frac{t_1}{t} \bx_1 + \dots + \frac{t_k}{t} \bx_k$.
1. Note that $\bz$ is a convex combination of $\bx_1, \dots, bx_k \in C$.
1. Since $C$ is convex, hence $\bz \in C$.
1. Then, $bx = t \bz \in S$ since $t > 0$ and $\bz \in C$.
1. Thus, $K$ contains all conic combinations of $C$.
1. Thus, $H \subseteq K$.
```


```{prf:property} Conic hull of a convex hull
Let $S \subseteq \VV$ be a nonempty set. Let $C = \convex S$.
Then

$$
\cone S = \cone C.
$$
In other words, the conic hull of the convex hull of a set is same
as the conic hull of the set.
```

```{prf:proof}
Since $S \subseteq C$, hence $\cone S \subseteq \cone C$.
We now prove the converse.

1. Let $\bx \in \cone C$.
1. Then $\bx$ is a nonnegative combination of some vectors in $C$.
   There exist a positive integer $p$, $p$ vectors
   $\bx_1, \dots, \bx_p \in C$ and $p$ scalars 
   $t_1, \dots, t_p$ such that

   $$
   \bx = \sum_{i=1}^p t_i \bx_i.
   $$
1. Each $\bx_i$ is a convex combination of some vectors in $S$.
1. Hence $\bx$ is a nonnegative combination of some vectors in $S$.
1. Hence $\bx \in \cone S$.
1. Hence $\cone C \subseteq \cone S$.
```


### Unique Conic Representations

Recall from 
{prf:ref}`Carathéodory theorem <res-cvx-conv-hull-caratheodory>`
that in an $n$ dimensional vector space,
every point in the convex hull of a set
can be represented as a convex combination
of $n+1$ points belonging to the set.

Similar representation is possible in conic hulls too.

```{prf:theorem} Conic representation theorem
:label: res-cvx-conic-rep-unique

Let $\VV$ be an $n$-dimensional real vector space.
Let $S \subseteq \VV$. 
Let $\bx \in \ConicHull(S)$. 
Then, there exist $k$ linearly independent vectors
$\bx_1, \dots, \bx_k \in S$ such that
$\bx \in \ConicHull(\{ \bx_1, \dots, \bx_k\})$;
i.e., there exists $\bt \in \RR^k_+$ such that 

$$
\bx = \sum_{i=1}^k t_i \bx_i.
$$
Since the $k$ vectors are linearly independent,
hence $k \leq n$.
```


```{prf:proof}
The proof is similar to Carathéodory theorem.

1. Let $\bx \in \ConicHull(S)$.
1. Then, there exist $m$ points 
   $\bx_1, \dots, \bx_m \in S$ and
   $\bt \in \RR^m_+$ such that

   $$
   \bx = \sum_{i=1}^m t_i \bx_i.
   $$
1. We can assume that $t_i > 0$ for every $i \in 1,\dots,m$.
   Otherwise, we can simply drop the corresponding points
   from the conic combination.
1. If $\bx_1, \dots, \bx_m$ are linearly independent,
   then $k=m$, $m \leq n$ and we are done.
1. Let us consider the case when they are linearly dependent.
1. Then, there exists a nontrivial linear combination
   equally zero vector:

   $$
   r_1 \bx_1 + \dots + r_m \bx_m = \bzero.
   $$
1. Then, for any $\alpha \in \RR$
   
   $$
   \bx = \sum_{i=1}^m t_i \bx_i + \alpha \sum_{i=1}^m r_i \bx_i
   = \sum_{i=1}^m (t_i + \alpha r_i) \bx_i.
   $$
1. This representation is a conic combination if
   $t_i + \alpha r_i \geq 0$ for every $i=1,\dots,m$.
1. Since $t_i > 0$ for every $i$, hence, this set 
   of inequalities is satisfied for all $\alpha \in A$
   where $A$ is a closed interval with a nonempty interior.
   1. Let $A_i$ be the solution set for $i$-th inequality.
   1. We have $A = \bigcap_i A_i$.
   1. $\alpha = 0$ satisfies every inequality. Thus, $0 \in A_i$.
      Thus, $A \neq \EmptySet$.
   1. If $r_i = 0$, then $A_i = \RR$.
   1. If $r_i > 0$, then $A_i = [-\frac{t_i}{r_i}, \infty)$.
   1. If $r_i < 0$, then $A_i = (-\infty, \frac{t_i}{r_i}]$.
   1. Since not all $r_i = 0$, hence there are several 
      $A_i$ with finite endpoints (either left or right).
   1. Thus, there are three possibilities for $A$:
      $[a,b]$, or $[a, \infty)$ or $(-\infty, b]$.
   1. Both $a$ and $b$ correspond to an endpoint of one of the
      $A_i$.
1. If we pick $\alpha$ as one of the endpoints of $A$,
   then, $t_i + \alpha r_i \geq 0$ for every $i$ 
   and $t_j + \alpha r_j = 0$ for some $j \in 1,\dots,m$.
1. Thus, we obtain a conic representation of $\bx$ of
   at most $m-1$ vectors.
1. This process can be carried out repeatedly until
   we obtain a conic representation of $\bx$ of
   $k$ linearly independent vectors.
1. Since the $k$ vectors $\bx_1, \dots, \bx_k$ so obtained
   are linearly independent, hence $k \leq n$.
```


## Pointed Cones

```{index} Pointed cone
```
```{prf:definition} Pointed cone
:label: def-pointed-cone

A cone $C \subset \VV$ is called pointed if 
$\bx \in C$ and $-\bx \in C$ implies $\bx = \bzero$. 
```
In other words, a pointed cone, doesn't contain a line.

```{prf:example} The nonnegative orthant is a pointed convex cone
:label: ex-cone-nng-orthant-pointed

Recall from {prf:ref}`def-convex-nonnegative-orthant`
that the nonnegative orthant is defined as:

$$
\RR_+^n = \{ \bx \in \RR^n \ST x_i \geq 0, \Forall 1 \leq i \leq n \}.
$$
In other words, for $\bx \in \RR^n_+$, every component is non-negative.

Let $\bx, \by \in \RR^n_+$. Let $\alpha, \beta \geq 0$ and consider their 
conic combination

$$
\bz = \alpha \bx + \beta \by.
$$

It is obvious that all components of $\bz$ are also nonnegative. Hence
$\bz \in \RR^n_+$. Thus, $\RR^n_+$ is closed under conic combinations.
Hence, $\RR^n_+$ is a convex cone.

Finally, $\RR^n_+$ is pointed as 
$\bx \in \RR^n_+$ and $-\bx \in \RR^n_+$ both hold true
only if $\bx = \bzero$.
```

## Proper Cones

```{index} Proper cone
```
````{prf:definition} Proper cone
:label: def-proper-cone

A cone $K \in \VV$ is called a *proper cone* if it satisfies the following:

*  $K$ is *convex*.
*  $K$ is *closed*.
*  $K$ is *solid*; i.e., it has a nonempty interior.
*  $K$ is *pointed*.
````

```{prf:example} Non-empty interior
:label: ex-cone-non-empty-interior-proper

Consider the following sets in $\RR^2$:

$$
C_1 = \{ (x_1, x_2) \ST x_1 \geq 0, x_2 = 0\}
$$

$$
C_2 = \{ (x_1, x_2) \ST x_1, x_2 \geq 0\}
$$

Both are closed convex cones. 
$C_1$ doesn't have an interior. All points in $C_1$ are on the 
boundary of $C_1$. 

$C_2$ has a non-empty interior; e.g., the point 
$(1,1) \in C_2$ is not on the boundary.
```


## Norm Cones

```{index} Norm cone
```
````{prf:definition} Norm cone
:label: def-cvx-norm-cone

Let $\|  \cdot \| : \VV \to \RR$ be any norm on $\VV$.
The *norm cone* associated with the norm $\| \cdot \|$ is given by the set

$$
C \triangleq \{ (\bx,t) \ST \| \bx \| \leq t \}
$$
$C$ lies in the product space $\VV \times \RR$.
````

If $\VV = \RR^n$, then a norm cone belongs to $\RR^{n+1}$.

 ````{prf:theorem}
 :label: res-cvx-norm-cone-is-convex

A norm cone is convex. Moreover, it is a convex cone.
````


````{prf:example} Second order cone
:label: ex-cvx-second-order-cone

The second order cone is the norm cone for the Euclidean norm
in the Euclidean space $\RR^n$, i.e.

$$
C  = \{(\bx,t) \ST \| \bx \|_2 \leq t \}.
$$
From definition, $C  \subseteq \RR^{n+1}$.

This can be rewritten as

$$
C = \left \{
\begin{bmatrix}
\bx \\ t
\end{bmatrix}
\middle |
\begin{bmatrix}
\bx \\ t
\end{bmatrix}^T
\begin{bmatrix}
I & 0 \\
0 & -1
\end{bmatrix}
\begin{bmatrix}
\bx \\ t
\end{bmatrix}
\leq 0 , t \geq 0
\right \}
$$
````

## Dual Cones

```{div}
Dual cones are defined for finite dimensional inner product spaces.
Dual cones technically belong to the dual space $\VV^*$.

Recall that the 
{prf:ref}`dual space <def-la-dual-space>`
$\VV^*$ of a vector space $\VV$ is the set
of all linear functionals on $\VV$.
For finite dimensional spaces, $\VV$ and 
its dual $\VV^*$ are isomorphic.
For an inner product space $\VV$ 
every linear functional in $\VV^*$ 
can be identified with a vector $\bv \in \VV$
by the functional $\langle \cdot, \bv \rangle$
({prf:ref}`res-la-ip-dual-space-isomorphism`).
```

```{index} Dual cone
```
```{prf:definition} Dual cone
:label: def-dual-cone
Let $\VV$ be a finite dimensional inner product space and $\VV^*$
be its dual space.

Let $C \subset \VV$. The set 

$$
C^* \triangleq \{ \by \in \VV^* \ST \langle \bx, \by \rangle \geq 0 
    \Forall \bx \in C \}
$$
is called the *dual cone* of $C$ in $\VV^*$. 
```

```{div}
In the Euclidean space $\RR^n$, the dual cone can be written as:

$$
C^* \triangleq \{ \by \in \RR^n \ST \langle \bx, \by \rangle \geq 0 
    \Forall \bx \in C \}.
$$
```


```{rubric} Geometric interpretation
```

* For a vector $\by$, the set 
  $H_{\by, +} \{ \bx \ST \langle \bx, \by \rangle \geq 0\}$ is 
  a {prf:ref}`halfspace <def-halfspace>` passing through origin.
* $\by$ is the normal vector of the halfspace along 
  (in the direction of) the halfspace.
* If $\by$ belongs to the dual cone of $C$, then for every $\bx \in C$, we have
  $ \langle \bx, \by \rangle \geq 0$. 
* Thus, the set $C$ is contained in the halfspace $H_{\by, +}$.
* In particular, if $C$ is a cone, then it will also touch the boundary of 
  the half space $H_{\by, +}$ as $C$ contains the origin.

### Properties

```{prf:property}
:label: res-cvx-dual-cone-is-cone

Dual cone is a cone.
```

```{prf:proof}

Let $\by \in C^*$. Then, by definition, 

$$
\langle \bx, \by \rangle \geq 0 \Forall \bx \in C.
$$

Thus, for some $\alpha \geq 0$, 

$$
\langle \bx, \alpha \by \rangle 
= \alpha \langle \bx, \by \rangle \geq 0 \Forall \bx \in C.
$$

Thus, for every $\by \in C^*$, $\alpha \by \in C^*$ for all $\alpha \geq 0$.
Thus, $C^*$ is a cone.
```

```{prf:property}
:label: res-cvx-dual-cone-is-convex

Dual cone is convex.
```

```{prf:proof}

Let $\by_1, \by_2 \in C^*$. Let $t \in [0, 1]$ and

$$
\by = t \by_1 + (1 - t) \by_2.
$$

Then for an arbitrary $\bx \in C$,

$$
\langle \bx, \by \rangle 
= \langle \bx, t \by_1 + (1-t) \by_2 \rangle
= t \langle \bx, \by_1 \rangle + (1-t) \langle \bx, \by_2\rangle \geq 0.
$$

Thus, $\by \in C^*$.
Thus, $C^*$ is convex. 
```

We note that dual cone is a convex cone even if the original set $C$
is neither convex nor a cone.


```{prf:property} Containment reversal in dual cone
:label: res-cvx-dual-cone-containment

Let $C_1$ and $C_2$ be two subsets of $\VV$ and let 
$C_1^*$ and $C_2^*$ be their corresponding dual cones.
Then,

$$
C_1 \subseteq C_2 \implies C_2^* \subseteq C_1^*.
$$
```
The dual cone of the subset contains the dual cone of the superset. 

```{prf:proof}
Let $\by \in C_2^*$. Then 

$$

\langle \bx , \by \rangle \geq 0 \Forall \bx \in C_2 \implies 
\langle \bx , \by \rangle \geq 0 \Forall \bx \in C_1 \implies
\by \in C_1^*.
$$ 

Thus, $C_2^* \subseteq C_1^*$.
```

```{prf:property} Closedness
:label: res-cvx-dual-cone-closed

A dual cone is a closed set.
```

```{prf:proof}
The dual cone of a set $C$ is given by

$$
C^* = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \geq 0 
    \Forall \bx \in C \}
$$

Fix a $\bx \in C$ and consider the set

$$
H_{\bx} = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \geq 0 \}.
$$

The set $H_{\bx}$ is a closed half space.

We can now see that

$$
C^* =  \bigcap_{\bx \in C} H_{\bx}.
$$
Thus, $C^*$ is an intersection of closed half spaces.
An arbitrary intersection of closed sets is closed.
Hence $C^*$ is closed.
```


```{prf:property} Interior of dual cone
:label: res-cvx-dual-cone-interior

The interior of the dual cone $C^*$ is given by

$$
\interior C^* = \{ \by \in \VV^* \ST \langle \bx , \by \rangle > 0 
    \Forall \bx \in C \setminus \{ \bzero \} \}.
$$
```

```{prf:proof}
Let 

$$
A = \{ \by \ST \langle \bx , \by \rangle > 0 \Forall \bx \in C \setminus \{ \bzero \} \}.
$$

Let $\by \in A$. By definition $\by \in C^*$;
i.e., $A \subseteq C^*$.

Since $\langle \bx , \by \rangle > 0$ for every nonzero $\bx \in C$, 
hence $\langle \bx, \by +\bu  \rangle > 0$ for every nonzero $\bx \in C$ 
and every sufficiently small $\bu$. Hence, $\by \in \interior C^*$.
We have shown that $A \subseteq \interior C^*$.

Now, let $\by \notin A$ but $\by \in C^*$.
Then, $\langle \bx, \by \rangle = 0$ for some nonzero $\bx \in C$. But then

$$
\langle \bx, \by - t\bx \rangle 
= \langle \bx, \by \rangle - t \langle \bx, \bx \rangle < 0
$$
for all $t > 0$. Thus, $\by \notin \interior C^*$. 

Hence, $A = \interior C^*$.
```

```{prf:property} Non-empty interior implies pointed dual cone
:label: res-cvx-nonempty-pointed-dual-cone

If $C$ has a non-empty interior, then its dual cone $C^*$ is pointed.
```

```{prf:proof}
Let $C$ have a non-empty interior and assume that its dual cone $C^*$ 
is not pointed. Then, there exists a non-zero $\by \in C^*$ such that
$-\by \in C^*$ holds too.

Thus, $\langle \bx, \by \rangle \geq 0$ as well as 
$\langle \bx, -\by \rangle \geq 0$ for every $\bx \in C$,
i.e, $\langle \bx, \by \rangle = 0$ for every $\bx \in C$.
But this means that $C$ lies in a hyperplane $H_{\by, 0}$
and hence has an empty interior. 
A contradiction. 
```


```{prf:theorem} Dual cone of a subspace
:label: res-cvx-subspace-dual-cone

The dual cone of a subspace $V \subseteq \VV$ is its
{prf:ref}`orthogonal complement <def-la-orthogonal-complement>` 
$V^{\perp}$ defined as:

$$
V^{\perp} = \{ \by \ST \langle \bv, \by \rangle = 0 \Forall \bv \in V \}.
$$

More precisely, $V^*$ is isomorphic to $V^{\perp}$ as
the dual cone is a subset of $\VV^*$. 
```

```{prf:proof}
Let $V^*$ be the dual cone of $V$. If $\bv \in V^{\perp}$, then
by definition, $\bv \in V^*$. Thus, $V^{\perp} \subseteq V^*$.

Let us now assume that there is a vector 
$\by \in V^*$ s.t. $\by \notin V^{\perp}$.

Then, there exists $\bv \in V$ such that  $\langle \bv, \by \rangle > 0$.
Since $V$ is a subspace, it follows that $-\bv \in V$. 
But then  

$$
\langle -\bv, \by \rangle = - \langle \bv, \by \rangle < 0.
$$

Thus, $\by$ cannot belong to $V^*$. A contradiction.

Thus, $V^* = V^{\perp}$.
```

### Self Dual Cones

```{index} Self dual cone
```
```{prf:definition} Self dual cone
:label: def-self-dual-cone

A cone $C$ is called self dual if $C^* = C$, i.e., it is its own dual cone.

By equality, we mean that the dual cone $C^*$ is isomorphic to $C$
since technically $C^* \subseteq \VV^*$.
```

```{prf:example} Nonnegative orthant
:label: ex-nonnegative-orthant-self-dual

The non-negative orthant $\RR^n_+$ is self dual.

Let $C = \RR^n_+$. For some $\bu, \bv \in C$,  $\langle \bu, \bv \rangle \geq 0$. 
Thus, $\RR^n_+ \subseteq C^*$.

Now, for some $\bv \notin \RR^n_+$, there is at least one component which is negative.
Without loss of generality, assume that the first component $v_1 < 0$. 

Now consider the vector $\bu = [1, 0, \dots, 0] \in \RR^n_+$. 
$\langle \bv, \bu \rangle < 0$. Thus, $\bv \notin C^*$. 

Thus, $C^* = \RR^n_+$. It is self dual.
```


```{prf:example} Positive semidefinite cone
:label: ex-psd-cone-self-dual

The positive semi-definite cone $\SS^n_+$ is self dual.

Let $C = \SS^n_+$ and $\bY \in C$. We first show that $\bY \in C^*$.

Choose an arbitrary $\bX \in C$.  
Express $\bX$ in terms of its eigenvalue 
decomposition as 

$$
\bX = \sum \lambda_i \bq_i \bq_i^T.
$$  

Since $\bX$ is PSD, hence, $ \lambda_i \geq 0$. 

Then, 

$$
\begin{aligned}
\langle \bY, \bX \rangle 
&= \Trace (\bX \bY) = \Trace (\bY \bX) \\
&= \Trace \left ( \bY \sum \lambda_i \bq_i \bq_i^T \right )\\
&= \sum \lambda_i \Trace \left (\bY \bq_i \bq_i^T \right) \\
&= \sum \lambda_i \Trace \left(\bq_i^T \bY \bq_i \right)\\
&= \sum \lambda_i (\bq_i^T \bY \bq_i).
\end{aligned}
$$

But since $\bY$ is PSD, 
hence $\bq_i^T \bY \bq_i \geq 0$. 
Hence $\langle \bY, \bX \rangle \geq 0$.
Thus, $\bY \in C^*$.

Now, suppose $\bY \notin \SS^n_+$. 
Then there exists a vector $\bv \in \RR^n$
such that $\bv^T \bY \bv < 0$. 
Consider the PSD matrix $\bV = \bv \bv^T$. 

$$
\langle \bY, \bV \rangle 
= \Trace(\bV\bY) = \Trace (\bv \bv^T \bY) 
= \Trace (\bv^T \bY \bv) < 0.
$$

Thus, $\bY \notin C^*$.

This completes the proof that $C^* = C = \SS^n_+$,
i.e., the positive semi-definite cone is self dual.
```

## Polar Cones

```{index} Polar cone
```
```{prf:definition} Polar cone
:label: def-cvx-polar-cone

Let $\VV$ be a finite dimensional inner product space and $\VV^*$
be its dual space.

Let $C \subseteq \VV$.
Then, its polar cone $C^{\circ}$ is defined as

$$
C^{\circ} \triangleq \{ \by \in \VV^* \ST \langle \bx, \by \rangle \leq 0
\Forall \bx \in C \}.
$$
```

We note that polar cones are just the negative of dual cones.
Thus, they exhibit similar properties as dual cones.


### Properties

```{prf:property}
:label: res-cvx-polar-cone-is-cone

Polar cone is a cone.
```

```{prf:proof}

Let $\by \in C^{\circ}$. Then, by definition, 

$$
\langle \bx, \by \rangle \leq 0 \Forall \bx \in C.
$$

Thus, for some $\alpha \geq 0$, 

$$
\langle \bx, \alpha \by \rangle 
= \alpha \langle \bx, \by \rangle \leq 0 \Forall \bx \in C.
$$

Thus, for every $\by \in C^{\circ}$, 
$\alpha \by \in C^{\circ}$ for all $\alpha \geq 0$.
Thus, $C^{\circ}$ is a cone.
```

```{prf:property}
:label: res-cvx-polar-cone-is-convex

Polar cone is convex.
```

```{prf:proof}

Let $\by_1, \by_2 \in C^{\circ}$. Let $t \in [0, 1]$ and

$$
\by = t \by_1 + (1 - t) \by_2.
$$

Then for an arbitrary $\bx \in C$,

$$
\langle \bx, \by \rangle 
= \langle \bx, t \by_1 + (1-t) \by_2 \rangle
= t \langle \bx, \by_1 \rangle + (1-t) \langle \bx, \by_2\rangle \leq 0.
$$

Thus, $\by \in C^{\circ}$.
Thus, $C^{\circ}$ is convex. 
```

We note that polar cone is a convex cone even if the original set $C$
is neither convex nor a cone.


```{prf:property} Containment reversal in polar cone
:label: res-cvx-polar-cone-containment

Let $C_1$ and $C_2$ be two subsets of $\VV$ and let 
$C_1^{\circ}$ and $C_2^{\circ}$ be their corresponding polar cones.
Then,

$$
C_1 \subseteq C_2 \implies C_2^{\circ} \subseteq C_1^{\circ}.
$$
```
The polar cone of the subset contains the polar cone of the superset. 

```{prf:proof}
Let $\by \in C_2^{\circ}$. Then 

$$

\langle \bx , \by \rangle \leq 0 \Forall \bx \in C_2 \implies 
\langle \bx , \by \rangle \leq 0 \Forall \bx \in C_1 \implies
\by \in C_1^{\circ}.
$$ 

Thus, $C_2^{\circ} \subseteq C_1^{\circ}$.
```

```{prf:property} Closedness
:label: res-cvx-polar-cone-closed

A polar cone is a closed set.
```

```{prf:proof}
The polar cone of a set $C$ is given by

$$
C^{\circ} = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \leq 0 
    \Forall \bx \in C \}
$$

Fix a $\bx \in C$ and consider the set

$$
H_{\bx} = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \leq 0 \}.
$$

The set $H_{\bx}$ is a closed half space.

We can now see that

$$
C^{\circ} =  \bigcap_{\bx \in C} H_{\bx}.
$$
Thus, $C^{\circ}$ is an intersection of closed half spaces.
An arbitrary intersection of closed sets is closed.
Hence $C^{\circ}$ is closed.
```


```{prf:property} Interior of polar cone
:label: res-cvx-polar-cone-interior

The interior of the polar cone $C^{\circ}$ is given by

$$
\interior C^{\circ} = \{ \by \in \VV^* \ST \langle \bx , \by \rangle < 0 
    \Forall \bx \in C \setminus \{ \bzero \} \}.
$$
```

```{prf:proof}
Let 

$$
A = \{ \by \ST \langle \bx , \by \rangle < 0 
   \Forall \bx \in C \setminus \{ \bzero \} \}.
$$

Let $\by \in A$. By definition $\by \in C^{\circ}$;
i.e., $A \subseteq C^{\circ}$.

Since $\langle \bx , \by \rangle < 0$ for every nonzero $\bx \in C$, 
hence $\langle \bx, \by +\bu  \rangle < 0$ for every $\bx \in C$ 
and every sufficiently small $\bu$. Hence, $\by \in \interior C^{\circ}$.
We have shown that $A \subseteq \interior C^{\circ}$.

Now, let $\by \notin A$ but $\by \in C^{\circ}$.
Then, $\langle \bx, \by \rangle = 0$ for some nonzero $\bx \in C$. But then

$$
\langle \bx, \by - t\bx \rangle 
= \langle \bx, \by \rangle - t \langle \bx, \bx \rangle > 0
$$
for all $t < 0$. Thus, $\by \notin \interior C^{\circ}$. 

Hence, $A = \interior C^{\circ}$.
```

```{prf:property} Non-empty interior implies pointed polar cone
:label: res-cvx-nonempty-pointed-polar-cone

If $C$ has a non-empty interior, then its polar cone $C^{\circ}$ is pointed.
```

```{prf:proof}
Let $C$ have a non-empty interior and assume that its polar cone $C^{\circ}$ 
is not pointed. Then, there exists a non-zero $\by \in C^{\circ}$ such that
$-\by \in C^{\circ}$ holds too.

Thus, $\langle \bx, \by \rangle \leq 0$ as well as 
$\langle \bx, -\by \rangle \leq 0$ for every $\bx \in C$,
i.e, $\langle \bx, \by \rangle = 0$ for every $\bx \in C$.
But this means that $C$ lies in a hyperplane $H_{\by, 0}$
and hence has an empty interior. 
A contradiction. 
```


## Normal Cones

```{index} Normal cone; normal vector
```
```{prf:definition} Normal vector
:label: def-cvx-convex-set-normal-vector

Let $S$ be an arbitrary subset of $\VV$.
A vector $\bv \in \VV^*$ is said to be *normal*
to $S$ at a point $\ba \in S$
if $\bv$ does not make an acute angle with
any line segment starting from $\ba$ and ending at some $\bx \in S$;
i.e., if

$$
\langle \bx - \ba, \bv \rangle \leq 0 \Forall \bx \in S.
$$ 
```

```{prf:example} Normal vector
:label: ex-cone-normal-vec-1

Let $C$ be a half space given by:

$$
C  = \{ \bx \ST \langle \bx, \bb \rangle \leq s\}.
$$

Let $\ba$ be any point on the boundary hyperplane of $C$
given by $\langle \ba, \bb \rangle = s$.

Then, $\bb$ is normal to $C$ at $\ba$ since for any $\bx \in C$

$$
\langle \bx - \ba , \bb \rangle 
= \langle \bx, \bb \rangle - \langle \ba, \bb \rangle
\leq s - s = 0.
$$
Note that $\bb$ points opposite to the direction of the
halfspace.
```

```{index} Normal cone
```
```{prf:definition} Normal cone
:label: def-cvx-normal-cone

The set of all vectors normal to a set $S$ at 
a point $\ba \in S$, denoted by $N_S(\ba)$, is called the
*normal cone* to $S$ at $\ba$. 

$$
N_S(\ba) \triangleq \{ \bv \in \VV^* \ST 
   \langle \bx - \ba , \bv \rangle \leq 0 
   \Forall \bx \in S \}.
$$

We customarily define $N_S(\ba) = \EmptySet$ for any $\ba \notin S$.
```


```{prf:property}
:label: res-cvx-normal-cone-convex

A normal cone is always a convex cone.
```

```{prf:proof}
Let $S$ be a subset of $\VV$ and let $\ba \in S$.
Let $N$ denote the set of normal vectors to $S$ at $\ba$.
We have to show that $N$ is a convex cone;
i.e., we have to show that $N$ contains all its conic combinations.

For any $\bx \in S$:

$$
\langle \bx - \ba , \bzero \rangle = 0.
$$

Thus, $\bzero \in N$.

Assume $\bu \in N$. 
Then, 

$$
\langle \bx - \ba, \bu \rangle \leq 0 \Forall \bx \in S.
$$

But then for any $t \geq 0$,

$$
\langle \bx - \ba, t\bu \rangle 
= t \langle \bx - \ba, \bu \rangle
\leq 0 \Forall \bx \in S.
$$
Thus, $t \bu \in N$. Thus, $N$ is closed under
nonnegative scalar multiplication.

Now, let $\bu, \bv \in N$. 
Then,

$$
\langle \bx - \ba, \bu + \bv \rangle 
=  \langle \bx - \ba, \bu \rangle
   + \langle \bx - \ba, \bv \rangle
\leq 0 \Forall \bx \in S.
$$
since sum of two nonpositive quantities is nonpositive. 

Thus, $\bu + \bv \in N$.
Thus, $N$ is closed under vector addition.

Combining these two observations, $N$ is closed
under conic combinations. Hence, $N$ is a convex cone.
```

```{prf:property}
:label: res-cvx-normal-cone-closed

A normal cone is closed.


Specifically, if $N_S(\ba)$ is the normal cone 
to a set $S$ at a point $\ba \in S$,
then:

$$
N_S(\ba) 
= \bigcap_{\bx \in S} 
\{ \bv \in \VV^* \ST \langle \bx - \ba , \bv \rangle \leq 0 \}.
$$
```

```{prf:proof}
For some fixed $\ba \in S$ and any fixed $\bx \in \VV$, define:

$$
H_{-}(\bx - \ba) = \{ \bv \in \VV^* \ST \langle \bx - \ba , \bv \rangle \leq 0 \}.
$$
Note that $H_{-}(\bx - \ba)$ is a closed {prf:ref}`half-space <def-halfspace>`
passing through origin of $\VV^*$ extending opposite to the direction $\bx - \ba$.

Let $\bv \in N_S(\ba)$ be a normal vector to $S$ at $\ba$.

1. Then, for every $\bx \in S$, $\langle \bx - \ba, \bv \rangle \leq 0$.
1. Thus,  for every $\bx \in S$, $\bv \in H_{-}(\bx - \ba)$.
1. Thus, $\bv \in \bigcap_{\bx \in S} H_{-}(\bx - \ba)$.
1. Thus, $N_S(\ba) \subseteq \bigcap_{\bx \in S} H_{-}(\bx - \ba)$.

Going in the opposite direction:

1. Let $\bv \in \bigcap_{\bx \in S} H_{-}(\bx - \ba)$.
1. Then, for every $\bx \in S$, $\bv \in H_{-}(\bx - \ba)$.
1. Thus, for every $\bx \in S$, $\langle \bx - \ba , \bv \rangle \leq 0$.
1. Thus, $\bv$ is a normal vector to $S$ at $\ba$.
1. Thus, $\bv \in N_S(\ba)$.
1. Thus, $\bigcap_{\bx \in S} H_{-}(\bx - \ba) \subseteq N_S(\ba)$.

Combining, we get:

$$
N_S(\ba) = \bigcap_{\bx \in S} H_{-}(\bx - \ba).
$$

Now, since $N_S(\ba)$ is an arbitrary intersection of closed
half spaces which are individually closed sets, hence
$N_S(\ba)$ is closed.

Since each half space is convex and intersection of 
convex sets is convex, hence, as a bonus, this proof also
shows that $N_S(\ba)$ is convex.
```

```{prf:theorem} Normal cone of unit ball
:label: res-cvxf-normal-cone-unit-ball

$$
N_{B[\bzero, 1]} (\bx) = \{ \by \in \VV^* \ST \| \by \|_* \leq \langle \bx, \by \rangle \}.
$$
```

```{prf:proof}
The unit ball at origin is given by:

$$
S = B[\bzero, 1] = \{\bx \in \VV  \ST \| \bx \| \leq 1 \}.
$$

Consider $\bx \in S$.
Then, $\by \in N_S(\bx)$ if and only if

$$
& \langle \bz - \bx , \by \rangle \leq 0 \Forall \bz \in S\\
& \iff \langle \bz , \by \rangle \leq \langle \bx, \by \rangle \Forall \bz \in S\\
& \iff \underset{\| \bz \|  \leq 1}{\sup} \langle \bz , \by \rangle
\leq \langle \bx, \by \rangle \\
& \iff \| \by \|_* \leq \langle \bx, \by \rangle.
$$

Therefore, for any $\bx \in S$:

$$
N_S(\bx) = \{ \by \in \VV^* \ST \| \by \|_* \leq \langle \bx, \by \rangle \}.
$$
```

## Barrier Cones

```{index} Barrier cone; barrier vector
```
```{prf:definition} Barrier vector
:label: def-cvx-convex-set-barrier vector

Let $C$ be a convex set of $\VV$. 
A vector $\bv \in \VV^*$ is called a
*barrier* vector to $C$ if for some $\beta \in \RR$,

$$
\langle \bx , \bv \rangle \leq \beta \Forall \bx \in C.
$$
In other words, the set of inner products of points in $C$
with $\bv$ is bounded from above.
```

```{index} Barrier cone
```
```{prf:definition} Barrier cone
:label: def-cvx-convex-set-barrier-cone

The set of all barrier vectors to a convex set $C$
is called its *barrier cone*.
```

```{prf:theorem}
:label: res-cvx-barrier-cone-convex

The barrier cone of a convex set is convex.
```

```{prf:proof}
Let $C$ be a convex set and let $B$ be its barrier cone.
Let $\bu, \bv \in B$. Let $t \geq 0$.

$$
\langle \bx , \bzero \rangle = 0 \leq 0 \Forall \bx \in C.
$$
Thus, $\bzero \in B$.

$$
\langle \bx , \bu \rangle \leq \alpha
\implies \langle \bx , t\bu \rangle \leq t\alpha \Forall \bx \in C.
$$
Thus, the set of inner products with $t \bu$ is bounded
from above by $t \alpha$. Thus, $t \bu \in B$.

$$
\langle \bx , \bu \rangle \leq \alpha 
\text{ and }
\langle \bx , \bv \rangle \leq \beta 
\implies \langle \bx , \bu + \bv \rangle \leq \alpha + \beta \Forall \bx \in C.
$$
Thus, the set of inner products with $\bu + \bv$ is bounded
from above by $\alpha + \beta$. Thus, $\bu + \bv \in B$.

Thus, $B$ is closed under nonnegative scalar multiplication
and vector addition. $B$ is a convex cone.
```



## Properties of Convex Cones

We consider operations on convex cones which
generate convex cones.

```{prf:property} Closure under set intersection
:label: res-cvx-convex-cone-closure-intersection

If $K_1$ and $K_2$ are convex cones, then 
$K = K_1 \cap K_2$ is convex cone.
```

```{prf:proof}
We show that $K$ is closed under nonnegative scalar multiplication.

1. Let $\bx \in K$ and $t \geq 0$. 
1. Then, $\bx \in K_1$ and $\bx \in K_2$.
1. Hence, $t \bx \in K_1$ and $t \bx \in K_2$ since
   both are closed under nonnegative scalar multiplication.
1. Thus, $t\bx \in K$.
1. Hence, $K$ is closed under nonnegative scalar multiplication.  

We show that $K$ is closed under vector addition too.

1. Let $\bx, \by \in K$.
1. Then, $\bx, \by \in K_1$ and $\bx, \by \in K_2$.
1. But then, $\bx + \by \in K_1$ and $\bx + \by \in K_2$
   since both are closed under vector addition.
1. Thus, $\bx + \by \in K$.
1. Hence, $K$ is closed under vector addition.

Thus, $K$ is closed under nonnegative scalar multiplication
and vector addition. $K$ is a convex cone.
```

```{prf:property} Closure under set addition
:label: res-cvx-convex-cone-closure-addition

If $K_1$ and $K_2$ are convex cones, then 
$K = K_1 + K_2$ is convex cone.
```

```{prf:proof}
We show that $K$ is closed under nonnegative scalar multiplication.

1. Let $\bx \in K$ and $t \geq 0$.
1. Then, $\bx = \bx_1 + \bx_2$ where $\bx_1 \in K_1$, and $\bx_2 \in K_2$.
1. Then, $t \bx_1 \in K_1$ and $t \bx_2 \in K_2$ since $K_1$ and $K_2$ are cone.
1. Then, $ t \bx = t(\bx_1 + \bx_2) = t \bx_1 + t \bx_2 \in K$.
1. Thus, $K$ is closed under nonnegative scalar multiplication.

We show that $K$ is closed under vector addition too.

1. Let $\bx, \by \in K$. 
1. Then, $\bx = \bx_1 + \bx_2$ with some $\bx_1 \in K_1$ and $\bx_2 \in K_2$.
1. And, $\by = \by_1 + \by_2$ with some $\by_1 \in K_1$ and $\by_2 \in K_2$.
1. Then, $\bx + \by = (\bx_1 + \by_1) + (\bx_2 + \by_2)$.
1. Now, $\bx_1 + \by_1 \in K_1$ and $\bx_2 + \by_2 \in K_2$ since
   $K_1$ and $K_2$ are closed under addition (they are convex cones).
1. Thus, $\bx + \by \in K$.
1. Thus, $K$ is closed under vector addition.


Thus, $K$ is closed under nonnegative scalar multiplication
and vector addition. $K$ is a convex cone.


We mention that by {prf:ref}`res-cvx-convexity-set-addition`, $K$ is convex.
Hence, we just needed to show that $K$ is a cone too.
```

```{prf:property} Positive scalar multiplication
:label: res-cvx-convex-cone-scaling-same

Let $K$ be a convex cone. Then

$$
t K = K \Forall t > 0.
$$
```
```{prf:proof}
We proceed as follows:


1. Let $t > 0$.
1. Let $\bx \in t K$. 
1. Then, $\frac{1}{t} \bx \in K$. 
1. But then, $t \frac{1}{t}\bx = \bx \in K$ too 
   since $K$ is closed under nonnegative scalar multiplication.
1. Thus, $t K \subseteq K$.
1. Similarly, $\bx \in K$ implies $\bx \in tK$.
1. Thus, $K \subseteq t K$.
1. Hence, $K = t K$ for all $t > 0$.
```

Note that $0K = \{ \bzero \} \neq K$.

```{prf:property} Convex hull of the union
:label: res-cvx-cones-union-hull-sum

If $K_1$ and $K_2$ are convex cones, then 

$$
K_1 + K_2 = \ConvexHull (K_1 \cup K_2).
$$
```

```{prf:proof}
By {prf:ref}`res-cvx-hull-union-cvx-combs`,

$$
\ConvexHull (K_1 \cup K_2) = \bigcup_{t \in [0,1]} 
\left [ (1 - t) K_1 + t K_2 \right ].
$$

Now for $t \in (0,1)$, 
by {prf:ref}`res-cvx-convex-cone-scaling-same`,
$(1-t)K_1 = K_1$ and $t K_2 = K_2$.

Thus, for $t \in (0,1)$:

$$
(1 - t) K_1 + t K_2 = K_1 + K_2.
$$

For, $t=0$ we are left with $K_1$ and for
$t=1$, we are left with $K_2$.

Since $\bzero \in K_1$ and $\bzero \in K_2$,
hence  $K_1 \subseteq K_1 + K_2$ 
and $K_2 \subseteq K_1 + K_2$.
Thus,

$$
\ConvexHull (K_1 \cup K_2) = \bigcup_{t \in [0,1]} 
\left [ (1 - t) K_1 + t K_2 \right ] = K_1 + K_2.
$$
```


```{prf:property} Intersection as union
:label: res-cvx-cones-intersect-union-cvx

If $C_1$ and $C_2$ are convex cones, then 

$$
C_1 \cap C_2 = \bigcup_{t \in [0,1]} (t C_1 \cap (1 - t) C_2).
$$
```

```{prf:proof}
We first show that for every $t \in (0,1)$

$$
t C_1 \cap (1 - t) C_2 = C_1 \cap C_2.
$$

1. Let $\bx \in C_1 \cap C_2$.
1. Then $\bx \in C_1$ and $\bx \in C_2$.
1. Since $0 < t < 1$, hence due to {prf:ref}`res-cvx-convex-cone-scaling-same`,
   $C_1 = t C_1$ and $C_2 = (1-t)C_2$.
1. Hence $\bx \in t C_1$ and $\bx \in (1-t) C_2$.
1. Hence $\bx \in t C_1 \cap (1 - t) C_2$.
1. Hence $C_1 \cap C_2 \subseteq t C_1 \cap (1 - t) C_2$.
1. Conversely, let $\bx \in t C_1 \cap (1 - t) C_2$.
1. Then $\bx \in t C_1$ and $\bx \in (1-t) C_2$.
1. Hence $\bx \in C_1$ and $\bx \in C_2$.
1. Hence $\bx \in C_1 \cap C_2$.
1. Hence $t C_1 \cap (1 - t) C_2 \subseteq C_1 \cap C_2$.

If $t=0$ or $t=1$, then

$$
t C_1 \cap (1 - t) C_2 = \{ \bzero \} \subseteq C_1 \cap C_2
$$
since every convex cone contains the origin. Together,

$$
C_1 \cap C_2 = \bigcup_{t \in [0,1]} (t C_1 \cap (1 - t) C_2).
$$
```




## Polyhedral Cones

```{index} Polyhedral cone
```
```{prf:definition} Polyhedral cone
:label: def-cvx-polyhedral-cone

The conic hull of a finite set of points is known as
a *polyhedral cone*.

In other words, let $\{ \bx_1, \bx_2, \dots, \bx_m \}$
be a finite set of points. Then

$$
C = \cone \{ \bx_1, \bx_2, \dots, \bx_m \} 
$$ 
is known as a polyhedral cone.
```

```{prf:theorem}
:label: res-cvx-polyhedral-cone-closed-convex

A polyhedral cone is nonempty, closed and convex.
```

```{prf:proof}
Since it is the conic hull of a nonempty set, hence 
it is nonempty and convex.

{prf:ref}`res-cvx-closed-conic-hull` shows that
the conic hulls of a finite set of points are
closed.
```

```{prf:remark} Polyhedral cone alternative formulations
:label: res-cvx-polyhedral-cone-definitions

Following are some alternative definitions of a polyhedral cone.

1. A cone is polyhedral if it is the intersection of a finite
   number of half spaces which have $\bzero$ on their boundary.
1. A cone $C$ is polyhedral if there is some matrix
   $\bA$ such that $C = \{ \bx \in \RR^n \ST \bA \bx \succeq \bzero  \}$.
1. A cone is polyhedral if it is the solution set of a system of 
   homogeneous linear inequalities.
```

### Polar Cones

```{prf:theorem} Polar cone of a polyhedral cone
:label: res-cvx-polar-polyhedral-cone

Let the ambient space by $\RR^n$. Let $\bA \in \RR^{m \times n}$.
Let 

$$
C = \{\bx \in \RR^n \ST \bA \bx \preceq \bzero \}.
$$

Then

$$
C^{\circ}  = \{ \bA^T \bt \ST \bt \in \RR^m_+ \}.
$$
```

We note that the set $C$ is a convex cone. It is known
as the convex polyhedral cone.

```{prf:proof}
We note that $\by \in C^{\circ}$ if and only if 
$\bx^T \by \leq 0$ for every $\bx$ satisfying $\bA \bx \preceq \bzero$.

1. Thus, for every $\bx \in \RR^n$, the statement
   $\bA \bx \preceq \bzero \implies \bx^T \by \leq 0$ is true.
1. By Farkas' lemma ({prf:ref}`res-cvx-farkas-lemma-v3`),
   it is equivalent to the statement that
   there exists $\bt \succeq \bzero$ such that $\bA^T \bt = \by$.
1. Thus, 

   $$
   C^{\circ}  = \{ \bA^T \bt \ST \bt \in \RR^m_+ \}.
   $$
```



## Cone Generated by a Convex Set

The direct sum vector space $\VV \oplus \RR$ has
been described in {prf:ref}`def-cvx-real-vector-space-r-prod`.

```{prf:observation} Convex sets as cross sections of cones
:label: res-cvx-convex-cross-section-cone

A convex set $C \subseteq \VV$ can be regarded as a 
cross section of some convex cone
$K \subseteq \VV \oplus \RR$. 

Let $K$ be conic hull of points $(\bx, 1) \in \VV \oplus \RR$ such that $\bx \in C$.
Then, 

$$
K = \{ (t \bx, t) \in \VV \oplus \RR \ST \bx \in C, t \geq 0 \}.
$$

Now consider the hyperplane in $\VV \oplus \RR$ given by:

$$
H = \{ (\by, t) \in \VV \oplus \RR \ST t = 1 \}.
$$

The intersection of $H$ with $K$ can be regarded as $C$.

$$
H \cap K = \{(t\bx, t) \in \VV \oplus \RR \ST \bx \in C, t=1\}
= \{ (\bx, 1) \in \VV \oplus \RR \ST \bx \in C\}.
$$
The projection of $H \cap K$ on $\VV$ is given by $C$
(by dropping the last coordinate).
```


```{prf:remark}
For every convex set $C \subseteq \VV$, there is
precisely one convex cone $K \subseteq \VV \oplus \RR$ 
generated by the set $\{(\bx, 1) \in \VV \oplus \RR \ST \bx \in C \}$
(its conic hull).

These convex cones have only $(\bzero, 0)$ in common
with the half space $\{(\bx, t) \in \VV \oplus \RR \ST t \leq 0 \}$.

We shall call this class of convex cones in $\VV \oplus \RR$
generated by the convex sets in $\VV$ as $\CCC$.
```

An operation that is closed under the class $\CCC$ 
corresponds to an operation on the convex sets in $\VV$;
e.g., if $C_1$ and $C_2$ are convex sets with corresponding
cones $K_1$ and $K_2$, then $C_1 \cap C_2$ is another
convex set corresponding to a different convex cone $K_3$.
It is natural to ask if there is a way to construct
$K_3$ from $K_1$ and $K_2$ directly in $\VV \oplus \RR$.

Each vector $(\bx, t) \in \VV \oplus \RR$
can be split as a direct sum with $\bx \in \VV$ and $t \in \RR$.
Thus, it is possible to define different kinds of 
{prf:ref}`partial sums <res-cvx-convex-set-partial-addition>`
on $\VV \oplus \RR$. 
Recall that partial sums on convex sets preserve the convexity.
It turns out that they can do more. We can define
partial sums which are closed under the family $\CCC$ of
convex cones in $\VV \oplus \RR$ generated by 
the convex sets in $\VV$.

We can define four types of partial sums:

1. Addition in $\VV$, intersection in $\RR$.
1. Addition in $\VV$, addition in $\RR$.
1. Intersection in $\VV$, intersection in $\RR$.
1. Intersection in $\VV$, addition in $\RR$.

Suppose that $K_1$ and $K_2$ are convex cones 
generated by the convex sets $C_1$ and $C_2$ respectively.
Let $K$ be their partial sum. Let us find out
what is the corresponding convex set $C$ in $\VV$ 
based on the type of partial sum in $\VV \oplus \RR$.

[Addition in $\VV$, intersection in $\RR$.]

1. In this case, $(\bx, 1) \in K$ if and only if 
   $\bx = \bx_1 + \bx_2$ for some $(\bx_1, 1) \in K_1$ and
   $(\bx_2, 1) \in K_2$.
1. Thus, the convex set corresponding to $K$ is $C = C_1 + C_2$.

[Addition in $\VV$, addition in $\RR$.]

1. $(\bx, 1) \in K$ if and only if $\bx = \bx_1 + \bx_2$
   and $1 = t_1 + t_2$ with $t_1 \geq 0$ and $t_2 \geq 0$
   for some $(\bx_1, t_1) \in K_1$ and $(\bx_2, t_2) \in K_2$.
1. Thus, $C$ is the union of the sets $t_1 C_1 + t_2 C_2$ over
   $t_1 \geq 0$, $t_2 \geq 0$ and $t_1 + t_2 = 1$.
1. But, this is same as $C = \ConvexHull (C_1 \cup C_2)$
   as per {prf:ref}`res-cvx-arb-cvx-un-cvx-comb`. 

[TODO] Clarify this further. It is not obvious.


[Intersection in $\VV$, intersection in $\RR$]

1. $(\bx, 1) \in K$ if and only if $(\bx, 1) \in K_1$
   as well as $(\bx, 1) \in K_2$.
1. Thus, $C = C_1 \cap C_2$.


[Intersection in $\VV$, addition in $\RR$]

1. $(\bx, 1) \in K$ if and only if $(\bx, t_1) \in K_1$
   and $(\bx, t_2) \in K_2$ for some $t_1, t_2 \geq 0$
   with $t_1 + t_2 = 1$.
1. In this case, we can write $C$ as:

   $$
   C &= \bigcup \{ t_1 C_1 \cap t_2 C_2 \ST t_1, t_2 \geq 0, t_1 + t_2 =1 \}\\
   &= \bigcup \{ (1 - t) C_1 \cap t C_2 \ST t \in [0, 1]\}. 
   $$

[TODO] Clarify this further. It is not obvious.


## Positive Semidefinite Cone

````{prf:theorem} The convex cone of positive semidefinite matrices
:label: res-cvx-psd-cone

The set of positive semidefinite matrices $\SS_+^n$ is a convex cone.
````

````{prf:proof}
Let $\bA, \bB \in \SS_+^n$ and $\theta_1, \theta_2 \geq 0$. We have to show that
$\theta_1 \bA + \theta_2 \bB \in \SS_+^n$.

$$
\bA \in \SS_+^n \implies \bv^T \bA \bv \geq 0 \Forall \bv \in \RR^n.
$$

$$
\bB \in \SS_+^n \implies \bv^T \bB \bv \geq 0 \Forall \bv \in \RR^n.
$$

Now

$$
\bv^T (\theta_1 \bA + \theta_2 \bB) \bv 
= \theta_1 \bv^T \bA \bv + \theta_2 \bv^T \bB \bv \geq 0 
\Forall \bv \in \RR^n.
$$

Hence $\theta_1 \bA + \theta_2 \bB \in \SS_+^n$.
````

## Linear System with Nonnegativity Constraints

Consider the system

$$
P = \{ \bx \in \RR^n \ST \bA \bx = \bb, \bx \succeq \bzero \}
$$
where $\bA \in \RR^{m \times n}$ and $\bb \in \RR^m$.
Without loss of generality, we shall assume that the rows
of $\bA$ are linearly independent.
This is a linear system $\bA \bx = \bb$ with the nonnegativity
constraint $\bx \succeq \bzero$.
If we write $\bA$ in the form of column vectors as 

$$
\bA = \begin{bmatrix}
\ba_1 & \dots & \ba_n
\end{bmatrix}
$$
Then, the set $Q = \{ \bA \bx \ST \bx \in \RR^n_+ \}$
can be written as

$$
Q = \cone \{\ba_1, \dots \ba_n\}.
$$
In other words, $Q$ is the conic hull of the column vectors
of $\bA$. We can think of $\bA$ as a linear mapping of the
nonnegative orthant (a convex cone) $\RR^n_+$ from $\RR^n$
to another convex cone in $\RR^n$ given as a conic hull
of the columns of $\bA$.

We can now see that $P$ is nonempty if $\bb \in Q$. 

```{index} Basic feasible solution
```
```{prf:definition} Basic feasible solution
:label: def-cvx-basic-feasible-solution

Let $P = \{ \bx \in \RR^n \ST \bA \bx = \bb, \bx \succeq \bzero \}$
where $\bA \in \RR^{m \times n}$ and $\bb \in \RR^m$. 
Assume that the rows of $\bA$ are linearly independent. 
Then, $\bv \in \RR^n$ is a *basic feasible solution* (in short "bfs")
of $P$ if the columns of $\bA$ corresponding to the positive
entries of $\bv$ are linearly independent.

Consequently, $\bv$ has at most $m$ has positive entries.
All other entries of $\bv$ are $0$.
```

```{prf:theorem} Existence of basic feasible solution
:label: res-cvx-cone-bfs-existence

Let $P = \{ \bx \in \RR^n \ST \bA \bx = \bb, \bx \succeq \bzero \}$
where $\bA \in \RR^{m \times n}$ and $\bb \in \RR^m$. 
Assume that the rows of $A$ are linearly independent. 

If $P$ is nonempty; i.e. $P \neq \EmptySet$, then 
it contains at least one basic feasible solution.
```

```{prf:proof}
Recall that

$$
Q = \{ \bA \bx \ST \bx \in \RR^n_+ \} = \cone \{\ba_1, \dots \ba_n\}
$$
where $\ba_1, \dots, \ba_n$ are columns of the matrix $\bA$.

1. If $P \neq \EmptySet$, then $\bb \in Q$.
1. In other words, $\bb$ is a conic combination of columns of $\bA$.
1. By the {prf:ref}`conic representation theorem <res-cvx-conic-rep-unique>`,
   there exists a subset of $k$ linearly independent vectors among
   $\{\ba_1, \dots, \ba_n \}$ such that $\bb$ is their conic 
   combination.
1. In other words, there exist $k$ indices $1 \leq i_1 < \dots < i_k \leq n$
   and $k$ numbers $v_{i_1}, \dots, v_{i_k} > 0$ such that

   $$
   \bb = \sum_{j=1}^k v_{i_j} \ba_{i_j}
   $$
   and $\{\ba_{i_1}, \dots, \ba_{i_k}\}$ are linearly independent.
1. Consequently $k \leq m$ since columns of $\bA$ belong to $\RR^m$.
1. Let 
   
   $$
   \bv = \sum_{j=1}^k v_{i_j} \be_{i_j}
   $$
   where $\be_{i_j}$ are unit vectors of $\RR^n$.
1. Clearly, $\bv \succeq \bzero$ and $\bA \bv = \bb$.
1. Therefore, $\bv \in P$ and $\bv$ is a basic feasible solution.
```

The basic feasible solutions of $P$ are the
{prf:ref}`extreme points <def-cvx-extreme-point>` 
of $P$. Recall that a point is an extreme point
if it cannot be expressed as a nontrivial convex
combination of two distinct points of a set.

```{prf:theorem} Equivalence between basic feasible solutions and extreme points
:label: res-cvx-cone-bfs-extreme

Let $P = \{ \bx \in \RR^n \ST \bA \bx = \bb, \bx \succeq \bzero \}$
where $\bA \in \RR^{m \times n}$ and $\bb \in \RR^m$. 
Assume that the rows of $A$ are linearly independent. 

Then $\bv$ is a basic feasible solution of $P$ if and only if 
$\bv$ is an extreme point of $P$.
```

```{prf:proof}

Let $\bv$ be a basic feasible solution of $P$.

1. Then $\bb = \bA \bv$ and $\bv$ has $k$ positive entries
   with $k \leq m$.
1. Without loss of generality, assume that first $k$ entries
   of $\bv$ are positive. This can be easily achieved by 
   shuffling the columns of $\bA$ in the linear system $\bA \bx = \bb$.
1. Therefore, $v_1, \dots, v_k > 0$ and $v_{k+1}, \dots, v_n = 0$.
1. Also, the first $k$ columns $\ba_1, \dots, \ba_k$ of the matrix
   $\bA$ are linearly independent since $\bv$ is a basic feasible solution.
1. For contradiction, assume that $\bv$ is not an extreme point of $P$;
   i.e.,  $\bv \notin \extreme P$.
1. Then, there exist $\by, \bz \in P$ with $\by \neq \bz$ 
   and $t \in (0,1)$ such that
   $\bv = t \by + (1-t)\bz$.
1. Since $\by, \bz \in P$, hence $\by \succeq \bzero$ and $\bz \succeq \bzero$.
1. Since the last $n-k$ entries of $\bv$ are zero, hence
   the last $n-k$ entries of $\by$ and $\bz$ also must be zero
   as they have to be nonnegative.
1. Since $\by, \bz \in P$, hence $\bA \by = \bb$ and $\bA \bz = \bb$.
1. Therefore, 

   $$
   \bb = \sum_{i=1}^k y_i \ba_i = \sum_{i=1}^k z_i \ba_i. 
   $$
1. This implies that

   $$
   \sum_{i=1}^k (y_i -z_i) \ba_i = \bzero.
   $$
1. But, $\ba_1, \dots, \ba_k$ are linearly independent by hypothesis.
1. Thus, $y_i = z_i$ for $i=1,\dots,k$ must hold.
1. Then, $\by = \bz$.
1. We arrive at a contradiction.
1. Thus, $\bv$ must be an extreme point of $P$.

For the converse, assume that $\bv$ is an extreme point of $P$.

1. Again, by contradiction, assume that $\bv$ is not a basic 
   feasible solution. 
1. Thus, the columns of $\bA$ corresponding to the positive
   entries of $\bv$ are linearly dependent.
1. Assume that there are $k$ positive entries in $\bv$
   and WLOG, assume that they correspond to first $k$ 
   columns of $\bA$.
1. Then, since the corresponding columns are linearly 
   dependent, hence there exists a nonzero vector $\bt \in \RR^k$
   such that

   $$
   \sum_{i=1}^k t_i \ba_i = \bzero.
   $$
1. We can extend $\bt$ to $\RR^n$ by appending $n-k$ zeros such that
   $\bA \bt = \bzero$.
1. Since the first $k$ entries of $\bv$ are positive, we can
   choose a sufficiently small $r > 0$ such that
   $\by = \bv - r \bt \succeq \bzero$
   and $\bz = \bv + r \bt \succeq \bzero$.
1. Note that $\bA \by = \bA \bz = \bb$.
1. Therefore, $\by, \bz \in P$.
1. At the same time, it is easy to see that

   $$
   \bv = \frac{1}{2} \by + \frac{1}{2} \bz.
   $$
1. Thus, $\bv$ is a convex combination of two distinct points of $P$.
1. This contradicts our hypothesis that $\bv$ is an extreme point of $P$.
1. Thus, $\bv$ must be a basic feasible solution.
```


