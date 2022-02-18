(sec:la:affine_sets)=
# Affine Sets and Transformations

In this section $\VV$ denotes a vector space on some field $\FF$
which can be either $\RR$ (real numbers) or $\CC$ (complex numbers).
Much of the section will not require any other structure on 
the vector space. 

Some results in this section are applicable for
normed linear spaces or inner product spaces.
We shall assume that $\VV$ is endowed with
an appropriate norm $\| \cdot \| : \VV \to \RR$ 
or an inner product $\langle \cdot, \cdot \rangle : \VV \times \VV \to \FF$
wherever applicable.

```{note}
The notion of lines in a complex vector space may sound 
very confusing as a complex line is topologically 
equivalent to a real plane, not a real line. 
If you are getting lost while reading this section, 
just think of $\FF$ as $\RR$ and visualize everything
in a real vector space. The algebraic presentation
of affine sets and spaces is equally valid for
complex vector spaces.

A key property of $\RR$ is that $\RR$ is totally
ordered. 
Hence, the scalars from $\RR$ can be compared.
There is no natural order in $\CC$, the field
of complex numbers.
As you study this section, you will notice that 
scalar comparison is never needed in the treatment
of affine sets, subspaces and transformations in this
section.
```

## Lines

```{prf:definition} Line
:label: def-aff-line

Let $\bx_1$ and $\bx_2$ be two points in $\VV$. Points of the form

$$
\by = \theta \bx_1 + (1 - \theta) \bx_2 \text{ where } \theta \in \FF
$$ 
form a *line* passing through $\bx_1$ and $\bx_2$.
```

* at $\theta=0$ we have $\by=\bx_2$.
* at $\theta=1$ we have $\by=\bx_1$.




We can also rewrite $\by$ as 

$$
\by = \bx_2 + \theta (\bx_1 - \bx_2) \Forall \theta \in \FF.
$$
In this definition:

* $\bx_2$ is called the *base point* for this line.
* $\bx_1 - \bx_2$ defines the *direction* of the line.
* $\by$ is the sum of the base point and the direction scaled by the parameter $\theta$.
* As $\theta$ goes from $0$ to $1$, $\by$ moves from $\bx_2$ to $\bx_1$.

```{prf:remark}
An alternative notation for the line as a set is $\bx_2 + \FF (\bx_1 - \bx_2)$
following the notation in {prf:ref}`def-vs-set-arithmetic`.
```

## Affine Sets

```{prf:definition} Affine set
:label: def-affine-set

A set $C \subseteq \VV$ is *affine* if the line through
any two distinct points in $C$ lies in $C$.

In other words, for any $\bx_1, \bx_2 \in C$, 
we have $\theta \bx_1 + (1 - \theta) \bx_2 \in C$ 
for all $\theta \in \FF$.

Another way to write this is:

$$
\Forall \theta \in \FF, \quad C = \theta C + (1 - \theta) C.
$$
```
Different authors use other names for affine sets
like "affine manifold", "affine variety", "linear variety"
or "flat".


```{prf:example}
:label: ex-affine-empty-set

The empty set $\EmptySet$ is affine vacuously as it contains
no points. Hence, every line passing through the points in $\EmptySet$ 
is inside it vacuously.
```

```{prf:example}
:label: ex-affine-singleton-set

For any $\bx \in \VV$, the singleton set $\{ \bx \}$ is affine vacuously.
It contains only one point. 
Hence, every line passing through two distinct points in $\{ \bx \}$
is inside it vacuously.

In fact:

$$
\theta \bx  + (1 - \theta) \bx = \bx \Forall \theta \in \FF.
$$
```

```{prf:example}
:label: ex-aff-line-is-affine

Any line in $\VV$ is an affine set.
```

```{prf:example}
:label: ex-aff-vector-space-affine

Any vector space $\VV$ is affine. It is so since a vector space
is closed under vector addition and scalar multiplication. 
Hence, for any two points in the vector space, the line passing
through it is contained inside the space.
```

```{prf:theorem} Linear subspaces are affine
The linear subspaces of a vector space $\VV$ 
are affine sets containing the zero vector.
```

```{prf:proof}
Let $\WW$ be a linear subspace of $\VV$.

1. Then $\WW$ contains $\bzero$.
1. Let $\bx, \by \in \WW$. 
1. Then, by linearity, any
   $\alpha \bx + \beta \by \in \WW$. 
1. In particular, for some $\theta \in \FF$,
   $\theta \bx  + (1 - \theta)\bw \in \WW$ holds too.
1. Thus, $\WW$ is affine.

For the converse, let $A$ be an affine set containing
$\bzero$.

1. For any $\bx \in A$ and $t \in \FF$,

   $$
   t \bx = (1 - t) \bzero + t \bx \in A
   $$
   since $A$ is affine. Thus, $A$ is closed under scalar multiplication.
1. Let $\bx, \by \in A$. Since $A$ is affine, hence
   
   $$
   \frac{1}{2} (\bx + \by) = \frac{1}{2} \bx + \left (1 - \frac{1}{2} \right) \by \in A.
   $$
1. But then, $\bx + \by \in A$ holds too since $A$ is closed under scalar 
   multiplication.
1. Thus, $A$ is closed under vector addition.
1. Since $A$ is closed under scalar multiplication and vector addition,
   hence $A$ must be a subspace. 
```




## Affine Combinations

If we denote $\alpha = \theta$ and $\beta = (1 - \theta)$ we see that 
$\alpha \bx_1 + \beta \bx_2$ represents a linear combination of points in $C$
such that $\alpha + \beta = 1$.
The idea can be generalized in following way.

```{prf:definition} Affine combination
:label: def-affine-combination

A point of the form $\bx = \theta_1 \bx_1 + \dots + \theta_k \bx_k$ where 
$\theta_1 + \dots + \theta_k = 1$ with $\theta_i \in \FF$ and $\bx_i \in \VV$, 
is called an *affine combination* of the points $\bx_1,\dots,\bx_k$.
```
Note that the definition only considers finite number of terms in the
affine combination.

It can be shown easily that an affine set $C$ 
contains all affine combinations of its points.

```{prf:theorem} Affine set contains affine combinations
:label: res-aff-set-contains-aff-combs

If $C$ is an affine set,
$\bx_1, \dots, \bx_k \in C$,
and $\theta_1 + \dots + \theta_k = 1$, then
the point $\bx = \theta_1 \bx_1 + \dots + \theta_k \bx_k$ 
also belongs to $C$. 
```

```{prf:proof}

We shall call $\theta_1 \bx_1 + \dots + \theta_k \bx_k = \sum_{i=1}^k \theta_i \bx_i$
with $\sum_{i=1}^k \theta_i = 1$ as $k$ term affine combinations.

Our proof strategy is as follows:

1. We show that an affine set contains all its 2 term affine combinations.
1. We then show that if an affine set contains all its $k-1$ term affine combinations
   then it must contain all its $k$ term affine combinations.
1. Thus, by principle of mathematical induction, it contains all its
   affine combinations.

An affine combination of two points is of the form $\theta_1 \bx_1 + \theta_2 \bx_2$
where $\theta_1 + \theta_2 = 1$.
By {prf:ref}`definition <def-affine-set>` an affine set contains
all its 2 term affine combinations.

Now, assume that $C$ contains all its $k-1$ term affine combinations.

1. Consider points $\bx_1, \dots, \bx_{k-1}, \bx_k \in C$.
1. Let $\theta_1, \dots, \theta_{k-1}, \theta_k \in \FF$ 
   such that $\theta_1 + \dots + \theta_{k-1} + \theta_k = 1$.
1. Without loss of generality, assume that $\theta_k \neq 1$. Thus, $1 - \theta_k \neq 0$.
1. Note that $\theta_1 + \dots + \theta_{k-1} = 1 - \theta_k$.
1. Thus, $\frac{\theta_1}{1 - \theta_k} + \dots + \frac{\theta_{k-1}}{1- \theta_k} = 1$.
1. We can then write:

   $$
   \begin{aligned}
   \bx &= \sum_{i=1}^k \theta_i \bx_i =  \sum_{i=1}^{k-1} \theta_i \bx_i + \theta_k \bx_k \\
   &= (1 - \theta_k) \sum_{i=1}^{k-1} \frac{\theta_i}{1 - \theta_k} \bx_i + \theta_k \bx_k.
   \end{aligned}
   $$
1. Note that the term $\by = \sum_{i=1}^{k-1} \frac{\theta_i}{1 - \theta_k} \bx_i$ is
   an affine combination of $k-1$ terms. 
1. Thus, by inductive hypothesis, $\by \in C$.
1. We are left with 

   $$
   \bx = (1 - \theta_k) \by + \theta_k \bx_k.
   $$
1. This is a two term affine combination. Since $\by, \bx_k \in C$, hence $\bx \in C$.
1. Thus, we established that if $C$ contains its $k-1$ term affine combinations,
   it contains its $k$ term affine combinations too.
```

```{prf:theorem}
:label: res-aff-comb-aff-comb-aff-comb

An affine combination of affine combinations is an affine combination.
```

```{prf:proof}
Let $\bu = \sum_{i=1}^k \theta_i \bx_i$ and $\bv = \sum_{j=1}^l \lambda_j \by_j$
where $\bx_i , \by_j \in \VV$ and $\sum \theta_i = 1$ and $\sum \lambda_j = 1$.

We claim that $\bw = \gamma \bu + ( 1 - \gamma) \bv$ is also an affine combination.

$$
\begin{aligned}
\bw &= \gamma \bu + ( 1 - \gamma) \bv \\
&= \gamma \sum_{i=1}^k \theta_i \bx_i + ( 1 - \gamma) \sum_{j=1}^l \lambda_j \by_j\\
&= \sum_{i=1}^k \gamma \theta_i \bx_i + \sum_{j=1}^l ( 1 - \gamma)  \lambda_j \by_j.
\end{aligned}
$$ 

Notice that:

$$
\begin{aligned}
& \sum_{i=1}^k \gamma \theta_i +  \sum_{j=1}^l ( 1 - \gamma)  \lambda_j\\
&= \gamma \sum_{i=1}^k \theta_i +  ( 1 - \gamma)  \sum_{j=1}^l \lambda_j\\
&= \gamma 1 + (1 - \gamma)1 = 1.
\end{aligned}
$$

Thus, $\bw$ is an affine combination of the points $\bx_i$ and $\by_j$.

We can use the mathematical induction to show that arbitrary
affine combinations of affine combinations are affine combinations.
```

## Connection with Linear Subspaces

```{prf:theorem} affine - point = linear
:label: res-aff-offset-plus-linear-subspace

Let $C$ be a nonempty affine set and $\bx_0$ be any element in $C$. Then the set

$$
    V = C  - \bx_0 = \{ \bx  - \bx_0 | \bx \in C\}
$$

is a linear subspace of $\VV$.
```
To show that $V$ is indeed a linear subspace, we can show that
every linear combination of two arbitrary elements in $V$
belongs to $V$.

```{prf:proof}
Let $\bv_1$ and $\bv_2$ be two elements in $V$. 
Then by definition, there exist $\bx_1$ and $\bx_2$ in $C$ such that

$$
    \bv_1 = \bx_1 - \bx_0 \text{ and } \bv_2 = \bx_2 - \bx_0.
$$

Thus 

$$
    a \bv_1 + \bv_2 = a (\bx_1 - \bx_0) + \bx_2 - \bx_0 
    = (a \bx_1 + \bx_2  - a \bx_0 )  - \bx_0 \Forall a \in \FF.
$$

But since $a + 1 - a = 1$, 
hence $\bx_3 = (a \bx_1 + \bx_2  - a \bx_0 ) \in C$ (an affine combination). 

Hence $a \bv_1 + \bv_2 = \bx_3 - \bx_0 \in V$ [by definition of $V$].

Thus, any linear combination of elements in $V$ belongs to $V$. 
Hence, $V$ is a linear subspace of $\VV$.
```

```{prf:observation}
:label: res-aff-subspace-lin-space-offset

With the previous result, we can use the following notation:

$$
    C = V + \bx_0 = \{ \bv + \bx_0 | \bv \in V\}
$$
where $V$ is a linear subspace of $\VV$ and $\bx_0 \in \VV$.
In other words, a nonempty affine set is a linear subspace with an offset.
```
We need to justify this notation by establishing that there
is one and only linear subspace associated with an affine set.
This is done in the next result.

```{prf:theorem} Uniqueness of associated subspace
:label: res-aff-unique-lin-sub

Let $C$ be a nonempty affine set and
let $\bx_1$ and $\bx_2$ be two distinct elements in $C$.
Let $V_1 = C - \bx_1$ and $V_2 = C - \bx_2$, then the 
linear subspaces $V_1$ and $V_2$ are identical.
```

```{prf:proof}

We show that $V_1 \subseteq V_2$ and $V_2 \subseteq V_1$.

1. Let $\bv \in V_1$. 
1. There exists $\bx \in C$ such that $\bv = \bx - \bx_1$.
1. Then, $\bv = \bx - \bx_1 + \bx_2 - \bx_2$.
1. Let $\by = \bx - \bx_1 + \bx_2$. Note that $\bx, \bx_1, \bx_2 \in C$ and
   $\by$ is an affine combination of $\bx, \bx_1, \bx_2$.
1. Thus, $\by \in C$.
1. We can now write $\bv = \by - \bx_2$.
1. Thus, $\bv \in V_2$ as $V_2 = C - \bx_2$. 
1. Thus, $V_1 \subseteq V_2$.
1. An identical reasoning starting with some $\bv \in V_2$ gives us $V_2 \subseteq V_1$.
1. Thus, $V_1 = V_2$.
```

Thus the subspace $V$ associated with a nonempty affine set $C$ doesn't depend upon
the choice of offset $\bx_0$ in $C$.


```{prf:corollary}
:label: res-aff-with-zero-is-linear

If an affine set contains $\bzero$ then it is a linear subspace.
```

```{prf:proof}
The linear subspace associated with an affine set $C$ is given by
$V = C - \bx_0$ for any $\bx_0 \in \VV$.

In particular, if $C$ contains $\bzero$, then

$$
V = C - \bzero = C.
$$
Thus, $C$ is a linear subspace.
```

## Affine Subspaces and Dimension

```{prf:definition} Affine subspace
:label: def-affine-subspace

A nonempty affine set is called an *affine subspace*.
An affine subspace is a linear subspace with an offset.

Another way to express this is as follows. $C$ is an 
affine subspace of $\VV$ if:

$$
C \neq \EmptySet \text{ and } \Forall \theta \in \FF, \quad C = \theta C + (1 - \theta) C.
$$
```

```{prf:definition} Affine proper subspace
:label: def-affine-proper-subspace

An affine subspace $A$ in a vector space $\VV$
is called a proper subspace 
if the linear subspace associated with $A$ 
is a {prf:ref}`proper subspace <def-la-proper-subspace>` of $\VV$.
```


```{prf:definition} Affine dimension
:label: def-affine-dimension

We define the *affine dimension* of an affine subspace $C$ as the dimension
of the associated linear subspace $V = C - \bx_0$ for some $\bx_0 \in C$
if the subspace $V$ is finite dimensional. 

The dimension of $\EmptySet$ (empty affine set) is $-1$ by convention.
```
The definition is consistent since $V$ is independent of the choice of
$\bx_0 \in C$.


```{prf:example} Singletons as affine subspaces
:label: ex-aff-singleton-subspace

For any $\bx \in \VV$, the singleton set $\{ \bx\}$ can be expressed as

$$
\{ \bx\} = \bx + \{ \bzero \}.
$$
Its corresponding linear subspace is $\{ \bzero \}$ of zero dimension.

Thus, the singleton set has an affine dimension of 0.
```

```{prf:remark} Points, lines, planes, flats
:label: res-aff-simple-geom-examples

The affine sets of dimension 0, 1 and 2 are called
points, lines and planes respectively.

An affine set of dimension $k$ is often called a
$k$-*flat*.
```

```{prf:example} More affine sets
:label: ex-aff-more-affine-examples

* The euclidean space $\RR^n$ is affine.
* Any line is affine. The associated linear subspace is a line 
  parallel to it which passes through origin.
* Any plane is affine. If it passes through origin, it is a
  linear subspace. 
  The associated linear subspace is the plane parallel to it
  which passes through origin.
```

```{prf:theorem}
:label: res-aff-space-closed-aff-comb

An affine subspace is closed under affine combinations.
```
```{prf:proof}
This is from the definition of affine sets
and {prf:ref}`res-aff-set-contains-aff-combs`.
```

```{prf:observation} Affine - affine = Linear
:label: res-aff-affine-minus-affine

Let $C$ be an affine subspace. 
Let $V$ be the linear subspace associated with $C$ given by $V = C - \bx$.
Then every vector $\bv \in V$ can be written as $\bv = \by - \bx$ where $\by \in C$.
Since $V$ doesn't depend on the choice of $\bx$, hence 
$V$ is the set of all vectors of the form $\by - \bx$ where $\by, \bx \in C$.

Thus, following the notation in 
{prf:ref}`def-vs-set-arithmetic`,
we can write $V$ as:

$$
V = C - C.
$$
```
One way to think of affine sets as collections of points
in an arbitrary space and the associated linear subspace as
the collection of difference vectors between points. 

$$
\text{vector ab} = \text{point b} - \text{point a}.
$$

## Affine Hull 

```{prf:definition} Affine hull
:label: def-affine-hull

The set of all affine combinations of points in some arbitrary nonempty set 
$S \subseteq \VV$ 
is called the *affine hull* of $S$ and denoted as $\affine S$:

$$
\affine S = \{\theta_1 \bx_1 + \dots + \theta_k \bx_k \ST 
    \bx_1, \dots, \bx_k \in S \text{ and } \theta_1 + \dots + \theta_k = 1\}.
$$
```
```{prf:theorem}
:label: res-aff-hull-subspace

An affine hull is an affine subspace.
```
```{prf:proof}
Let $S \subset \VV$ be nonempty. Let $T = \affine S$. 
Let $\bu, \bv \in T$. Then

$$
\bu = \sum_{i=1}^{k} \theta_i \bx_i \text {and } v = \sum_{j=1}^{l} \lambda_j \by_j
$$ 
where $\bx_i, \by_j \in S$, $\sum \theta_i  = 1$ and $\sum \lambda_j = 1$.

Then, as shown in {prf:ref}`res-aff-comb-aff-comb-aff-comb`,

$$
\bw = \gamma \bu + (1 - \gamma) \bv
$$
is an affine combination of points $\bx_i, \by_j \in S$.

Thus, $\bw \in T$. 
Hence, $T$ is an affine set. 
Since $T$ is nonempty, hence $T$ is an affine subspace.
```


```{prf:theorem} Smallest containing affine subspace
:label: res-aff-affine-hull-smallest

The affine hull of a nonempty set $S$ is the smallest affine subspace containing $S$. 
More specifically, let $C$ be any affine subspace
with $S \subseteq C$. Then $\affine S \subseteq C$.
```

```{prf:proof}
Let $C$ be an arbitrary affine subspace such that $S \subseteq C$.

1. From {prf:ref}`res-aff-space-closed-aff-comb`, $C$ is closed under
   affine combinations. 
1. Thus, $C$ contains all affine combinations of 
   points of $S$. 
1. Thus, $\affine S \subseteq C$.
1. We established in {prf:ref}`res-aff-hull-subspace` that 
   $\affine S$ is an affine subspace. 
1. Thus, it is the smallest affine subspace containing $S$.
```

```{prf:corollary} Affine hull as intersection
:label: res-aff-affine-hull-intersection-all

The affine hull of a set is the intersection of all affine subspaces containing it.
```

```{prf:theorem} Affine hull of a finite set
:label: res-aff-finite-set-hull-ass-space

Let $S = \{ \bv_0, \bv_1, \dots, \bv_k \}$
be a finite set of vectors from a vector space $\VV$.
Let $A = \affine S$ be their affine hull.
Then, the linear subspace associated with $A$ is given by

$$
L = \span \{\bv_1 - \bv_0, \dots, \bv_k - \bv_0\}.
$$

Consequently, the dimension of $\affine S$ is at most $k$.
```

```{prf:proof}
Since $L = A - \bv_0$, hence 
$\bv_1 - \bv_0, \dots, \bv_k - \bv_0 \in L$. 
Thus, $\span \{ \bv_1 - \bv_0, \dots, \bv_k - \bv_0\} \subseteq L$.

Now, let $\bv \in L$. Then, there exist $t_0, \dots, t_k$ 
with $t_0 + \dots + t_k =1$ such that

$$
\bv = t_0 \bv_0 + \dots + t_k \bv_k - \bv_0.
$$

But then

$$
\bv &= (1 - t_1 - \dots - t_k) \bv_0 + t_1 \bv_1 + \dots + t_k \bv_k - \bv_0\\
&= t_1 (\bv_1 - \bv_0) + \dots + t_k (\bv_k - \bv_0).
$$

Thus, $\bv \in \span \{\bv_1 - \bv_0, \dots, \bv_k - \bv_0\}$.
Thus, $L \subseteq \span \{\bv_1 - \bv_0, \dots, \bv_k - \bv_0\}$.

Combining:

$$
L = \span \{\bv_1 - \bv_0, \dots, \bv_k - \bv_0\}.
$$

Since $L$ is a span of $k$ vectors, hence
$\dim L \leq k$. Thus, $\dim A \leq k$.
```

## Affine Independence

```{prf:definition} Affine independence
:label: def-affine-independence

A set of vectors $\bv_0, \bv_1, \dots, \bv_k \in \VV$ is called *affine independent*,
if the vectors $\bv_1 - \bv_0, \dots, \bv_k - \bv_0$ are linearly independent.
```
If the associated subspace has dimension $l$ then a maximum of $l$ vectors can 
be linearly independent in it. Hence a maximum of $l+1$ vectors can be affine
independent for the affine set.

```{prf:theorem} Affine independence and dimension
:label: res-aff-independence-hull-dim

A set of vectors $\bv_0, \bv_1, \dots, \bv_k \in \VV$ is 
affine independent if and only if their affine hull
$\affine \{\bv_0, \bv_1, \dots, \bv_k\}$ is $k$ dimensional.
```

```{prf:proof}
Assume $\bv_0, \bv_1, \dots, \bv_k$ to be affine independent.

1. Then,  by {prf:ref}`def-affine-independence`,
   $\bv_1 - \bv_0, \dots, \bv_k - \bv_0$ are linearly independent.
1. Let $L = \span \{ \bv_1 - \bv_0, \dots, \bv_k - \bv_0 \}$.
1. By {prf:ref}`res-aff-finite-set-hull-ass-space` 
   
   $$
   \dim \affine \{\bv_0, \bv_1, \dots, \bv_k\} = \dim L = k
   $$
   since $L$ is a span of $k$ linearly independent vectors.

Now, assume $A = \affine \{\bv_0, \bv_1, \dots, \bv_k\}$ is $k$ dimensional.

1. By {prf:ref}`res-aff-finite-set-hull-ass-space`, the linear subspace
   associated with $A$ is given by 
   $L = \span \{ \bv_1 - \bv_0, \dots, \bv_k - \bv_0 \}$.
1. Thus, $L$ is $k$ dimensional since $\dim L = \dim A = k$.
1. But, $L$ is a span of $k$ vectors. 
1. Hence, the $k$ vectors 
   $\bv_1 - \bv_0, \dots, \bv_k - \bv_0$
   must be linearly independent.
```


## Translations

```{prf:definition} Translation operator
:label: def-la-translation-operator

Let $\VV$ be a vector space.
An operator
$T_{\ba} : \VV \to \VV$ 
is called a *translation operator* if 

$$
T_{\ba}(\bx) = \bx + \ba \Forall \bx \in \XX
$$
where $\ba \in \XX$ is a fixed (translation) vector.
```

It can be easily seen that $T_{\ba}(C) = \ba + C = C + \ba$. 

```{prf:definition} Translate
:label: def-la-translate

Let $C \subseteq \VV$. The *translate* of $C$ by
some $\ba \in \VV$ is defined to be the set $C + \ba$.
```
```{prf:observation} Translating the vector space
:label: res-aff-space-translate

$$
\VV + \ba = \VV \Forall \ba \in \VV.
$$
Translating the whole vector space doesn't change it.

$$
\EmptySet + \ba = \EmptySet.
$$
This follows from the definition of the set vector addition.

$$
\{ \bzero \} + \ba = \{ \ba \}.
$$
The translate of the trivial subspace is a singleton set.
```

```{prf:theorem} Affine translate
:label: res-aff-affine-translate

A translate of an affine set is affine.
```


```{prf:proof}
Let $C$ be affine and $\ba \in \VV$.

1. Let $\bx, \by \in C + \ba$. 
1. Then, $\bx = \bu + \ba$ and $\by  = \bv + \ba$ for some $\bu, \bv \in C$.
1. Then for some $t \in \FF$, 
   
   $$
   t \bx + (1-t) \by
   &= t (\bu + \ba) + (1-t) (\bv + \ba)\\
   &= t \bu + (1-t)\bv + t \ba + (1-t)\ba\\
   &= t \bu + (1-t)\bv + \ba.
   $$
1. But $\bw = t \bu + (1-t)\bv \in C$ since $C$ is affine. 
1. Hence, $t \bx + (1-t) \by = \bw + \ba \in C + \ba$.
1. Thus, $C + \ba$ is affine. 
```

```{prf:definition} Parallel affine sets
:label: def-la-affine-parallel-set

Two affine sets $C$ and $D$ are called *parallel* to each other if

$$
D = C + \ba
$$
for some $\ba \in \VV$.
We denote this by $C \parallel D$.
```
Clearly, every affine set is parallel to its associated linear subspace.

This definition of parallelism is more restrictive 
as it allows comparing only those affine sets
which have the same dimension. 
Thus, we cannot compare a line with a plane. 

Every point is parallel to every other point.

```{prf:theorem} Parallelism equivalence relation
:label: res-la-affine-parallel-equivalence-relation

Consider the class of all affine subsets of a vector space $\VV$. 
The relation $C \parallel D$ is an equivalence relation.
```

```{prf:proof}
[Reflexivity]

1. $C = C + \bzero$. 
1. Hence $C \parallel C$.

[Symmetry]

1. Let $C \parallel D$. 
1. Then, there exists $\ba \in \VV$ such that
   $D = C + \ba$.
1. But then, $C = D + (-\ba)$.
1. Thus, $D \parallel C$.

[Transitivity]
1. Let $C \parallel D$ and $D \parallel E$.
1. Then, $D = C + \ba$ and $E = D + \bb$ for some $\ba, \bb \in \VV$.
1. But then, $E = C + (\ba + \bb)$. 
1. Thus, $C \parallel E$.
```


```{prf:theorem} Existence and uniqueness of a parallel linear subspace
:label: res-aff-subspace-parallel-linear

Every affine subspace (nonempty affine set) $A$ is parallel
to a unique subspace. The subspace is given by:

$$
W = A - A.
$$
```
This result is a restatement of {prf:ref}`res-aff-affine-minus-affine`.

```{prf:proof}
From {prf:ref}`res-aff-unique-lin-sub`, there
is a unique linear subspace $L$ associated with 
$A$ given by  $L = A - \ba$ for some $\ba \in A$.

Since $A = L + \ba$ hence, $A$ and $L$ are parallel
to each other.

Two linear subspaces are parallel to each other
only if they are identical. Thus, $L$ is the
unique linear subspace parallel to $A$.

Now, notice that:

$$
W = A - A = \bigcup_{\ba \in A} A - \ba.
$$
But $L = A - \ba$ for any $\ba \in A$ as $L$
is independent of the choice of $\ba \in A$.

Thus, 

$$
W = \bigcup_{\ba \in A} A - \ba = \bigcup_{\ba \in A} L = L.
$$

Thus, the unique linear subspace parallel to $A$ is given by
$W = A - A$.
```

## Affinity Preserving Operations

We discuss some operations which preserve the affine character
of its inputs


### Intersection

````{prf:theorem} Intersection of affine sets
:label: res-aff-intersection

If $S_1$ and $S_2$ are affine sets then $S_1 \cap S_2$ is affine.
````

````{prf:proof}
Let $\bx_1, \bx_2 \in S_1 \cap S_2$. We have to show that

$$
t \bx_1 + (1 - t) \bx_2 \in S_1 \cap S_2, \Forall t \in \FF.
$$

Since $S_1$ is affine and $\bx_1, \bx_2 \in S_1$, hence

$$
t \bx_1 + (1 - t) \bx_2 \in S_1, \Forall t \in \FF.
$$

Similarly

$$
t \bx_1 + (1 - t) \bx_2 \in S_2, \Forall t \in \FF.
$$

Thus

$$
t \bx_1 + (1 - t) \bx_2 \in S_1 \cap S_2, \Forall t \in \FF.
$$

Thus, $S_1 \cap S_2$ is affine.
````

We can generalize it further.

````{prf:theorem} Intersection of arbitrary collection of affine sets
:label: res-aff-arbitrary-intersection

Let $\{ A_i\}_{i \in I}$ be a family of sets such that $A_i$ is affine
for all $i \in I$.  Then $\cap_{i \in I} A_i$ is affine.
````

````{prf:proof}
Let $\bx_1, \bx_2$ be any two arbitrary elements in $\cap_{i \in I} A_i$.

$$
&\bx_1, \bx_2 \in \cap_{i \in I} A_i\\
\implies & \bx_1, \bx_2 \in A_i \Forall i \in I\\
\implies &t \bx_1 + (1 - t) \bx_2 \in A_i \Forall t \in \FF \Forall i \in I
\text{ since $A_i$ is affine }\\
\implies &t \bx_1 + (1 - t) \bx_2 \in \cap_{i \in I} A_i.
$$

Hence $\cap_{i \in I} A_i$ is affine.
````



## Hyper Planes

Recall from {prf:ref}`def-la-hyperplane-functional` that
a set of the form:

$$
H_{\bf, a} \triangleq \{ \bx \in \VV \ST \bf(\bx) = a \}
$$
where $\bf$ is a nonzero {prf:ref}`linear functional <def-la-linear-functional>`
on $\VV$ and $a \in \FF$ 
is called a hyperplane.

```{prf:theorem}
:label: res-la-aff-hyperplane-affine

Every hyperplane is affine.
```

```{prf:proof}
We proceed as follows:

1. Let $\bx, \by \in H_{\bf, a}$.
1. Then, $\bf(\bx) = a$ and $\bf(\by) = a$.
1. Consider any $t \in \FF$ and let $\bz = t \bx + (1-t) \by$.
1. Then, due to linearity of $\bf$,

   $$
   \bf(\bz)
   &= \bf(t \bx + (1-t) \by)\\
   &= t \bf(\bx) + (1-t) \bf(\by)\\
   &= t a + (1-t) a = a.
   $$
1. Thus, $\bz \in H_{\bf, a}$.
1. Thus, $H_{\bf, a}$ is an affine set.
```


```{prf:theorem} Linear subspace parallel to a hyperplane
:label: res-aff-hyperplane-parallel-space

Let $H$ be a hyperplane given by

$$
H = \{ \bx \in \VV \ST \bf(\bx) = a \}
$$
where $\bf$ is a nonzero {prf:ref}`linear functional <def-la-linear-functional>`
on $\VV$ and $a \in \FF$.

Then, the linear subspace parallel to $H$ is given by the
{prf:ref}`kernel <res-la-linear-functional-kernel>`
of the linear functional $\bf$:

$$
L = \bf^{-1}(0) = \{ \bx \in \VV \ST \bf(\bx) = 0 \}.
$$ 
```

```{prf:proof}
Let $V$ be the linear subspace parallel to $H$.

1. Then, any $\bv \in V$ can be written as 
   $\bv = \bx - \by$ for some $\bx, \by \in H$.
1. But then,

   $$
   \bf(\bv) = \bf (\bx - \by) = \bf (\bx) - \bf(\by) = a - a = 0.
   $$
1. Thus, $\bv \in L$ and hence $V \subseteq L$.

For the converse, we proceed as follows.

1. Let $\bv \in L$ and $\bx \in H$.
1. Let $\by = \bx - \bv$.
1. Then, $\bf(\by) = \bf (\bx) - \bf (\bv) = a - 0 = a$.
1. Thus, $\by \in H$.
1. Thus, $\bv = \bx - \by$ where $\bx, \by \in H$.
1. Thus, $\bv \in H - H = V$.
1. Thus, $L \subseteq V$.

Combining, $L = H$.
```

```{prf:theorem} Dimension of a hyperplane
:label: res-aff-dim-hyperplane

Let $H$ be a hyperplane given by

$$
H = \{ \bx \in \VV \ST \bf(\bx) = a \}
$$
where $\bf$ is a nonzero {prf:ref}`linear functional <def-la-linear-functional>`
on $\VV$ and $a \in \FF$.

If $\VV$ is finite dimensional, then 

$$
\dim H = \dim \VV - 1.
$$
```

```{prf:proof}
From {prf:ref}`res-aff-hyperplane-parallel-space`,
the linear subspace parallel to $H$ is given by


$$
L = \bf^{-1}(0) = \{ \bx \in \VV \ST \bf(\bx) = 0 \}.
$$

From {prf:ref}`res-la-linear-functional-kernel-dim`,
the dimension of the kernel of a linear functional
in a finite dimensional vector space is given by:

$$
\dim L = \dim \VV - 1.
$$

From {prf:ref}`def-affine-dimension`,

$$
\dim H = \dim L = \dim \VV - 1.
$$ 
```


```{prf:theorem} Hyperplanes in inner product spaces
:label: res-aff-ip-hyperplane

If $\VV$ is an inner product space over $\FF$, then
a set of the form

$$
H = \{\bx \ST \langle \bx, \ba \rangle = b \}
$$
where $\ba \in \VV$ is a nonzero vector 
and $b \in \FF$; is a hyperplane.

Moreover, every hyperplane of $\VV$ can be represented
in this form, with $\ba$ and $b$ unique up to a
common non-zero multiple.
```

```{prf:proof}
By {prf:ref}`res-la-inner-product-linear-functional`,
the mapping  $T_{\ba} : \VV \to \FF$ defined by:

$$
T_{\ba} (\bx) \triangleq \langle \bx , \ba \rangle  \Forall \bx \in \VV
$$
is a linear functional.
Thus, $H$ is a {prf:ref}`hyperplane <def-la-hyperplane-functional>`.

By {prf:ref}`res-la-linear-functional-inner-product`,
every linear functional can be identified as an
inner product with a vector $\ba \in \VV$. 
Thus, every hyperplane can be written as 

$$
H = \{\bx \ST \langle \bx, \ba \rangle = b \}.
$$

This representation is not unique since the set

$$
\{\bx \ST \langle \bx, \overline{t} \ba \rangle = t b \}
$$
is identical to $H$ for any $t \in \FF$ such that $t \neq 0$.
```


```{prf:theorem} Affine = Intersection of hyperplanes
:label: res-aff-proper-sub-hyper-intersect

Let $\VV$ be a finite dimensional vector space.
Then, every proper affine subset of $\VV$
is a finite intersection of hyperplanes.
```


```{prf:proof}
If $C = \EmptySet$, we can choose any
two non-intersecting parallel hyperplanes and $C$ is
their intersection.

Let $C$ be a proper affine subspace of $\VV$
such that $1 \leq \dim C < \dim \VV$.

1. Let $L$ be the linear subspace parallel to $C$.
1. Then $C = L + \ba$ for some fixed $\ba \in C$.
1. Let $n = \dim \VV$ and $m = \dim L$.
1. Since $L$ is a proper subspace of $\VV$ hence $m < n$.
1. Let $\{\bx_1, \dots, \bx_m \}$ be a basis for $L$.
1. Then, every $\bv \in C$ can be written as:

   $$
   \bv = \sum_{i=1}^m t_i \bx_i + \ba.
   $$
1. We can extend this basis to construct a basis
   $\{\bx_1, \dots, \bx_n \}$ for $\VV$.
1. We can construct a {prf:ref}`dual basis <res-la-finite-dual-space-basis>`
   for the dual space $\VV^*$.
   For each $i=1,\dots,n$, define a linear functional
   $\bf_i : \VV \to \FF$ by setting:

   $$
   \bf_i(\bx_j) = \begin{cases}
   1 && \text{ if } && i = j\\
   0 && \text{ if } && i \neq j
   \end{cases}.
   $$
1. Let $a_i = \bf_i (\ba)$. 
1. Consider a family of hyperplanes defined as:

   $$
   H_i = \{ \bx \in \VV \ST \bf_i(\bx) = a_i \}
   $$
   where $i=m+1, \dots, n$.
1. Consider their intersection

   $$
   H = \bigcap_{i=m+1}^n H_i = \{ \bx \in \VV \ST \bf_i(\bx) = a_i, i=m+1,\dots, n \}.
   $$
1. We claim that $C = H$.


We shall first show that $C \subseteq H$.

1. Let $\bv \in C$.
1. Then, $\bv = \sum_{j=1}^m t_j \bx_j + \ba$.
1. Then, $\bf_i (\bv) = \sum_{j=1}^m t_j \bf_i(\bx_j) + \bf_i(\ba) = a_i$ for $i=m+1, \dots, n$.
1. Thus, $\bv \in H_i$ for every $i=m+1, \dots, n$.
1. Thus, $\bv \in H$.
1. Thus, $C \subseteq H$.


We now show that $H \subseteq C$. Note that this is same as
showing $H - \ba \subseteq L = C - \ba$.

1. Let $\bv \in H - \ba$.
1. Hence, $\bv = \bx - \ba$ such that $\bx \in H$.
1. We can write $\bv$ in terms of the 
   basis $\{\bx_1, \dots, \bx_n\}$ as
   
   $$
   \bv = \sum_{j=1}^n t_j \bx_j.
   $$
1. Then $\bf_i(\bv) = t_i$ (by definition of $\bf_i$).
1. But, for any $i \in [m+1, \dots, n]$

   $$
   \bf_i(\bv) = \bf_i(\bx - \ba) = \bf_i (\bx) - \bf_i(\ba) = a_i - a_i = 0
   $$
   since $\bx \in H \subseteq H_i$.
1. Thus, $t_i = 0$ for every $i=m+1, \dots, n$.
1. Thus, 

   $$
   \bv = \sum_{j=1}^m t_j \bx_j.
   $$
1. Thus, $\bv \in L$ since $\{\bx_1, \dots, \bx_m\}$ is a basis for $L$. 
1. Thus, $H - \ba \subseteq L$.
1. Thus, $H \subseteq L + \ba = C$.

Combining these observations, we have $H = C$.

We are now left with the case of singleton sets 
$C = \{ \ba \}$ where $\dim C = 0$ since the
associated linear subspace is $\{ \bzero \}$.

1. Choose any basis $\BBB = \{\bx_1, \dots, \bx_n\}$ for $\VV$.
1. Construct a 
   {prf:ref}`dual basis <res-la-finite-dual-space-basis>`
   $\FFF = \{\bf_1, \dots, \bf_n \}$ for $\VV^*$ as before.
1. Let $a_i = \bf_i(\ba)$ for $i=1,\dots, n$.
1. Consider a family of hyperplanes defined as:

   $$
   H_i = \{ \bx \in \VV \ST \bf_i(\bx) = a_i \}
   $$
   where $i=1, \dots, n$.
1. Consider their intersection

   $$
   H = \bigcap_{i=1}^n H_i = \{ \bx \in \VV \ST \bf_i(\bx) = a_i, i=1,\dots, n \}.
   $$
1. Now, it is straightforward to show that
   $H = \{\ba \}  = C$.
```

```{prf:corollary} Affine sets in inner product space
:label: res-aff-finite-ip-proper-sub-hyper-intersect

Let $\VV$ be a finite dimensional inner product space over field $\FF$.
Let $A$ be a proper affine subset of $\VV$. 

Then, there exist $r$ (where $r < \dim \VV$) nonzero vectors
$\ba_i \in \VV$ and scalars $b_i \in \FF$ such
that $A$ is the intersection of the
hyperplanes given by

$$
H_i = \{\bx \in \VV \ST \langle \bx, \ba_i \rangle = b_i \}.
$$

Specifically,

$$
A = \bigcap_{i=1}^m H_i = \{\bx \in \VV \ST 
   \langle \bx, \ba_i \rangle = b_i, i=1,\dots,m \}.
$$
```

```{prf:proof}
It follows from {prf:ref}`res-aff-proper-sub-hyper-intersect`
that $A$ is a finite intersection of hyperplanes
with $r < n$ where $n = \dim \VV$.

Since $\VV$ is an inner product space, hence,
due to {prf:ref}`res-aff-ip-hyperplane`,
each hyperplane can be represented as

$$
H_i = \{\bx \in \VV \ST \langle \bx, \ba_i \rangle = b_i \}
$$
where $\ba_i \in \VV$ and $b_i \in \FF$.
```

Procedure to select the hyperplane parameters.

1. Pick a vector $\ba \in A$.
1. Identify the linear subspace $L = A - \ba$.
1. Pick an orthonormal basis for $L$: $\{\bv_1, \dots, \bv_m \}$.
1. Extend the orthonormal basis to $\VV$.
1. Pick the basis vectors for $L^{\perp}$: $\{\ba_1, \dots, \ba_r \}$
   with $m + r = n$.
1. Compute $b_i = \langle \ba, \ba_i \rangle$.

## Linear Equations

```{prf:example} Solution set of linear equations
We show that the solution set of linear equations forms an affine set.

Let $C = \{ \bx \ST \bA \bx = \bb\}$ where $\bA \in \FF^{m \times n}$ and $\bb \in \FF^m$.

Let $C$ be the set of all vectors $\bx \in \FF^n$ which satisfy the system of linear
equations given by $\bA \bx = \bb$. 
Then $C$ is an affine set.

Let $\bx_1$ and $\bx_2$ belong to $C$.  Then we have

$$
\bA \bx_1 = \bb
\text{ and }
\bA \bx_2 = \bb
$$

Thus 

$$
&\theta \bA \bx_1 + ( 1 - \theta ) \bA \bx_2 = \theta \bb + (1 - \theta ) \bb\\
&\implies \bA (\theta \bx_1 + (1  - \theta) \bx_2) = \bb\\
&\implies (\theta \bx_1 + (1  - \theta) \bx_2) \in C
$$

Thus, $C$ is an affine set.

The subspace associated with $C$ is nothing but the
null space of $\bA$ denoted as $\NullSpace(\bA)$.
```

Every affine set of $\FF^n$ can be expressed as the solution set of a 
system of linear equations.
If the system of equations is infeasible, then its solution set is
$\EmptySet$. Otherwise, its solution set is an affine subspace.
If the system of equations has a unique solution, then the solution
set is a singleton set which is an affine subspace of dimension 0.

```{prf:theorem} Affine set = system of linear equations in $\FF^n$
:label: res-aff-sol-lin-eq

Let $\bb \in \FF^m$. Let $\bA$ be an $m \times n$ 
matrix in $\FF^{m \times n}$. Consider the solution set
of the system of linear equations $\bA \bx = \bb$:

$$
C = \{\bx \in \FF^n \ST \bA \bx = \bb \}.
$$
Then, $C$ is an affine set.

Moreover, every affine set in $\FF^n$ can be represented 
as a system of linear equations.
```

```{prf:proof}
If $C = \EmptySet$ (i.e., the system of equations is infeasible),
then $C$ is affine (since empty sets are affine by definition).

If the system of equations has a unique solution, then
$C = \{ \bv \}$ where $\bv$ is the unique solution of
the system of equations, 
then $C$ is affine since singleton sets are affine.

We now consider the case that the system of equations
has more than one solutions.

Let $\bx_1, \bx_2 \in C$ be distinct solutions of the
system of linear equations
and let $t \in \FF$.
Then,

$$
\bA \bx_1 = \bb
\text{ and }
\bA \bx_2 = \bb
$$

Consider $\bx = t \bx_1 + (1-t) \bx_2$. 
Then,

$$
\bA \bx &= \bA (t \bx_1 + (1-t) \bx_2) \\
&= t \bA \bx_1 + (1-t) \bA \bx_2 \\
&= t \bb + (1-t) \bb = \bb.
$$
This means that $\bx \in C$.
Thus, $C$ contains all its affine combinations.
Hence, $C$ is affine.

We next show that every affine set of $\FF^n$ can be represented
as a system of linear equations. 
Note that $\FF^n$ is an inner product space with the
standard inner product given by $\langle \bx, \by \rangle = \overline{\by} \bx$.

Let $C$ be an arbitrary affine set in $\FF^n$. 

1. If $C = \EmptySet$, we can pick any
   infeasible system of linear equations as a representation of $C$.
1. If $C = \{ \bv \}$ is a singleton, we can pick the system
   $\bI \bx = \bv$ where $I$ is an identity matrix in $\FF^{n \times n}$.
1. If $C = \FF^n$, we can choose $\bA$ to be any $m \times n$
   zero matrix and $\bb = \bzero \in \FF^m$.
   Then, the solution set of $\ZERO \bx = \bzero$ is all of $\FF^n$.
1. We shall now consider the case of affine $C$ with more than
   one elements and $C \subset \FF^n$ (proper subset). 
1. Let $L$ be the subspace parallel to $C$ ({prf:ref}`res-aff-subspace-parallel-linear`).
1. Let $L^{\perp}$ be the 
   {prf:ref}`orthogonal complement <def-la-orthogonal-complement>` of $L$.
1. Let $\BBB = \{\bv_1, \dots, \bv_m \}$ be a
   basis for $L^{\perp}$ (where $m < n$).
1. Since $\FF^n$ is finite dimensional, hence
   $L = \left (L^{\perp} \right )^{\perp}$ ({prf:ref}`res-la-orth-comp-orth-comp`).
1. Thus, due to {prf:ref}`res-la-ip-orth-comp-perp-basis`, 

   $$
   L = \{ \bx \ST \bx \perp \bv_1, \dots, \bx \perp \bv_m \}.
   $$
1. Thus,

   $$
   L = \{\bx \ST \langle \bx, \bv_i \rangle = 0, i=1,\dots, m \}
   = \{ \bx \ST \bA \bx = \bzero \}
   $$
   where $\bA$ is the $m \times n$ matrix whose rows are
   $\bv_1, \dots, \bv_m$. 
1. Since $C$ is parallel to $L$, there exists an $\ba \in \FF^n$
   such that

   $$
   C = L + \ba 
   =  \{ \bx \ST \bA (\bx - \ba) = \bzero \}
   =  \{ \bx \ST \bA \bx = \bb \}
   $$ 
   where $\bb = \bA \ba$.
```

## Affine Transformations



```{prf:definition} Affine transformation
:label: def-la-affine-operator

Let $\XX$ and $\YY$ be vector spaces. 
A (total) function $T : \XX \to \YY$ (on some field $\FF$)
is called an *affine transformation* if
for every $\bx,\by \in \XX$ and for every $t \in \FF$

$$
T (t \bx + (1 - t) \by) = t T(\bx) + (1 - t) T(\by).
$$

An affine transformation is also known as an *affine function*
or an *affine operator*.
```


```{prf:theorem} Affine = Linear + Translation
:label: res-la-op-affine-linear-p-offset

$T$ is affine if and only if the mapping $\bx \mapsto T(\bx) - T(\bzero)$
is linear.

In other words, an affine transformation can be written as a linear
transformation followed by a translation.
```

```{prf:proof}
Let $T : \XX \to \YY$ be some mapping. Define:

$$
L (\bx) = T (\bx)  - T(\bzero).
$$

Assume $T$ to be affine. We shall show that $L$ is linear.

Let $\bx, \by \in \XX$ and $t \in \FF$. Then

$$
L(t\bx) &= T (t\bx) - T(\bzero)\\
&= T(t\bx + (1-t) \bzero) - T(\bzero)\\
&= t T(\bx) + (1-t)T(\bzero) - T(\bzero)\\
&= t (T(\bx) - T(\bzero)) = t L(\bx).
$$

$$
L (\bx + \by) &= T (\bx + \by)  - T(\bzero)\\
&= T(\frac{1}{2} 2 \bx + \frac{1}{2} 2 \by) - T(\bzero)\\
&= \frac{1}{2} T (2 \bx) + \frac{1}{2} T(2 \by) - T(\bzero)\\
&= \frac{1}{2} (T (2\bx) - T(\bzero)) + \frac{1}{2}( T(2\by) - T(\bzero))\\
&= \frac{1}{2} (L (2\bx)  + L (2\by))\\
&= \frac{1}{2} (2 L (\bx)  + 2 L (\by))\\
&= L(\bx) + L (\by).
$$
Thus, $L$ is linear.
Here, we used the fact that $L(2\bx) = T(2\bx) - T(\bzero)$
and $L$ was already shown to be homogeneous above giving 
$L(2\bx) = 2 L(\bx)$.


Now, assume $L$ to be linear. We shall show that $T$ is affine.


Let $\bx, \by \in \XX$ and $t \in \FF$. Then

$$
T (t \bx + (1 - t) \by) 
&= L (t \bx + (1 - t) \by) + T(\bzero)  \\
&= t L(\bx) + (1 -t) L (\by) + T(\bzero) \\
&= t L(\bx) + t T(\bzero) + (1 -t) L (\by) + (1-t)T(\bzero) \\
&= t (L (\bx) + T(\bzero)) + (1 -t) (L (\by) + T(\bzero))\\
&= tT (\bx) + (1- t) T(\by).
$$
Thus, $T$ is affine.
```

We show that affine functions distribute over
arbitrary affine combinations.

```{prf:theorem} Affine functions on affine combinations
:label: res-la-aff-func-aff-comb

Let $\XX$ and $\YY$ be vector spaces on a field $\FF$.
Let $T : \XX \to \YY$ be affine. 

Let $\bx_0, \bx_1, \dots, \bx_k \in \XX$ and 
$t_0, t_1, \dots, t_k \in \FF$ such that
$\sum_{i=0}^k t_i = 1$.
Then,

$$
T \left ( \sum_{i=0}^k t_i \bx_i \right ) = \sum_{i=0}^k t_i T(\bx_i).
$$
```

```{prf:proof}

Define:

$$
L(\bx) = T(\bx)  - T(\bzero).
$$

We know that $L$ is linear. We have $T(\bx) = L(\bx) + T(\bzero)$.

Now,

$$
T \left ( \sum_{i=0}^k t_i \bx_i \right ) 
&= L \left ( \sum_{i=0}^k t_i \bx_i \right )  + T(\bzero)\\
&= \sum_{i=0}^k t_i L( \bx_i)  + T(\bzero)\\
&= \sum_{i=0}^k t_i L( \bx_i)  + (\sum_{i=0}^k t_i) T(\bzero)\\
&= \sum_{i=0}^k t_i \left (L( \bx_i)  + T(\bzero) \right )\\
&= \sum_{i=0}^k t_i T( \bx_i).
$$
```


## Topology in Normed Spaces

We next consider the special case of a vector space $\VV$
endowed with a 
{prf:ref}`norm <def-la-norm>` $\| \cdot \| : \VV \to \RR$, 
which induces a {prf:ref}`metric <def-ms-distance-function>` 
$d: \VV \times \VV \to \RR$ given by:

$$
d (x, y) = \| x - y \|.
$$
$\VV$ equipped with this metric becomes a 
{prf:ref}`metric space <def-ms-metric-space>`
and is endowed with a metric topology.
Useful topological properties of affine sets 
are discussed below.

```{prf:theorem}
:label: res-la-affine-closed

Every affine subset of a normed linear space $\VV$ is a closed set.
```

```{prf:theorem}
:label: res-la-affine-subspace-empty-interior

Every proper affine subspace of a normed linear space $\VV$
has an empty interior.
```
