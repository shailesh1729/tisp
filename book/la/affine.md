(sec:la:affine_sets)=
# Affine Sets and Transformations

In this section $\VV$ denotes a vector space on some field $\FF$
which can be either $\FF$ or $\CC$.


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

```{prf:example}
The empty set $\EmptySet$ is affine vacuously as it contains
no points. Hence, every line passing through the points in $\EmptySet$ 
is inside it vacuously.
```

```{prf:example}
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
Any line in $\VV$ is an affine set.
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

```{prf:theorem} Linear subspaces are affine
A linear subspace $\WW$ of $\VV$ is affine.
```

```{prf:proof}
Let $\bx, \by \in \WW$. Then, by linearity, any
$\alpha \bx + \beta \by \in \WW$. In particular,
for some $\theta \in \FF$,
$\theta \bx  + (1 - \theta)\bw \in \WW$ holds too.
Thus, $\WW$ is affine.
```

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

```{prf:theorem}
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


```{prf:definition} Affine dimension
:label: def-affine-dimension

We define the *affine dimension* of an affine subspace $C$ as the dimension
of the associated linear subspace $V = C - \bx_0$ for some $\bx_0 \in C$. 

The dimension of $\EmptySet$ (empty affine set) is $-1$ by convention.
```
The definition is consistent since $V$ is independent of the choice of
$\bx_0 \in C$.


```{prf:example}
For any $\bx \in \VV$, the singleton set $\{ \bx\}$ can be expressed as

$$
\{ \bx\} = \bx + \{ \bzero \}.
$$
Its corresponding linear subspace is $\{ \bzero \}$ of zero dimension.

Thus, the singleton set has an affine dimension of 0.
```

```{prf:remark}
The affine sets of dimension 0, 1 and 2 are called
points, lines and planes respectively.

An affine set of dimension $k$ is often called a
$k$-*flat*.
```

### Hyper Planes

Recall from {prf:ref}`def-la-hyperplane-functional` that
a set of the form:

$$
H_{\bf, a} \triangleq \{ \bx \in \VV \ST \bf(\bx) = a \}
$$
where $\bf$ is a {prf:ref}`linear functional <def-la-linear-functional>`
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


### Linear Equations

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

```{prf:remark}
Every affine set of $\FF^n$ can be expressed as the solution set of a 
system of linear equations.
If the system of equations is infeasible, then its solution set is
$\EmptySet$. Otherwise, its solution set is an affine subspace.
If the system of equations has a unique solution, then the solution
set is a singleton set which is an affine subspace of dimension 0.
```


```{prf:example} More affine sets
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

```{prf:observation}
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


```{prf:theorem}
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

```{prf:corollary}
The affine hull of a set is the intersection of all affine subspaces containing it.
```


```{prf:definition} Affine independence
:label: def-affine-independence

A set of vectors $\bv_0, \bv_1, \dots, \bv_k \in \VV$ is called *affine independent*,
if the vectors $\bv_1 - \bv_0, \dots, \bv_k - \bv_0$ are linearly independent.

In other words, the difference vectors $\bv_k - \bv_0$ 
belong to the associated linear subspace. 
```
If the associated subspace has dimension $l$ then a maximum of $l$ vectors can 
be linearly independent in it. Hence a maximum of $l+1$ vectors can be affine
independent for the affine set.


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
```{prf:observation}
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
