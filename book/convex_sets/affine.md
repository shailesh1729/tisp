# Affine Sets

In this section $\VV$ denotes a real vector space.

## Lines

```{prf:definition}
:label: def-aff-line

Let $x_1$ and $x_2$ be two points in $\VV$. Points of the form

$$
y = \theta x_1 + (1 - \theta) x_2 \text{ where } \theta \in \RR
$$ 
form a *line* passing through $x_1$ and $x_2$.
```

* at $\theta=0$ we have $y=x_2$.
* at $\theta=1$ we have $y=x_1$.




We can also rewrite $y$ as 

$$
y = x_2 + \theta (x_1 - x_2) \Forall \theta \in \RR.
$$
In this definition:

* $x_2$ is called the *base point* for this line.
* $x_1 - x_2$ defines the *direction* of the line.
* $y$ is the sum of the base point and the direction scaled by the parameter $\theta$.
* As $\theta$ increases from $0$ to $1$, $y$ moves from $x_2$ to $x_1$.

```{prf:remark}
An alternative notation for the line as a set is $x_2 + \RR (x_1 - x_2)$
following the notation in {prf:ref}`def-vs-set-arithmetic`.
```

## Line Segments

```{prf:definition}
:label: def-aff-line-segment

Let $x_1$ and $x_2$ be two points in $\VV$. Points of the form

$$
y = (1 - \theta) x_1 + \theta x_2 \text{ where } 0 \leq \theta \leq 1
$$ 
form a (closed) *line-segment* between $x_1$ and $x_2$. 
The closed line segment is denoted by $[x_1, x_2]$.

$$
[x_1, x_2] \triangleq \{ (1 - \theta) x_1 + \theta x_2 \ST 0 \leq \theta \leq 1 \}.
$$ 

Similarly, we define an *open line segment* as:

$$
(x_1, x_2) \triangleq \{ (1 - \theta) x_1 + \theta x_2 \ST 0 < \theta < 1 \}.
$$ 

The half-open segment $(x_1, x_2]$ is defined as:

$$
(x_1, x_2] \triangleq \{ (1 - \theta) x_1 + \theta x_2 \ST 0 < \theta \leq 1 \}.
$$ 

The half-open segment $[x_1, x_2)$ is defined as:

$$
[x_1, x_2) \triangleq \{ (1 - \theta) x_1 + \theta x_2 \ST 0 \leq \theta < 1 \}.
$$ 
```

## Affine Sets

```{prf:definition}
:label: def-affine-set

A set $C \subseteq \VV$ is *affine* if the line through
any two distinct points in $C$ lies in $C$.

In other words, for any $x_1, x_2 \in C$, we have $\theta x_1 + (1 - \theta) x_2 \in C$ 
for all $\theta \in \RR$.

Another way to write this is:

$$
\Forall \theta \in \RR, \quad C = \theta C + (1 - \theta) C.
$$
```

```{prf:example}
The empty set $\EmptySet$ is affine vacuously as it contains
no points. Hence, every line passing through the points in $\EmptySet$ 
is inside it vacuously.
```

```{prf:example}
For any $x \in \VV$, the singleton set $\{ x \}$ is affine vacuously.
It contains only one point. 
Hence, every line passing through two distinct points in $\{ x \}$
is inside it vacuously.

In fact:

$$
\theta x  + (1 - \theta) x = x \Forall \theta \in \RR.
$$
```

```{prf:example}
Any line in $\VV$ is an affine set.
```

## Affine Combinations

If we denote $\alpha = \theta$ and $\beta = (1 - \theta)$ we see that 
$\alpha x_1 + \beta x_2$ represents a linear combination of points in $C$
such that $\alpha + \beta = 1$.
The idea can be generalized in following way.

```{prf:definition}
:label: def-affine-combination

A point of the form $x = \theta_1 x_1 + \dots + \theta_k x_k$ where 
$\theta_1 + \dots + \theta_k = 1$ with $\theta_i \in \RR$ and $x_i \in \VV$, 
is called an *affine combination* of the points $x_1,\dots,x_k$.
```
Note that the definition only considers finite number of terms in the
affine combination.

It can be shown easily that an affine set $C$ 
contains all affine combinations of its points.

```{prf:proposition}
:label: res-aff-set-contains-aff-combs

If $C$ is an affine set,
$x_1, \dots, x_k \in C$,
and $\theta_1 + \dots + \theta_k = 1$, then
the point $x = \theta_1 x_1 + \dots + \theta_k x_k$ 
also belongs to $C$. 
```

```{prf:proof}

We shall call $\theta_1 x_1 + \dots + \theta_k x_k = \sum_{i=1}^k \theta_i x_i$
with $\sum_{i=1}^k \theta_i = 1$ as $k$ term affine combinations.

Our proof strategy is as follows:

1. We show that an affine set contains all its 2 term affine combinations.
1. We then show that if an affine set contains all its $k-1$ term affine combinations
   then it must contain all its $k$ term affine combinations.
1. Thus, by principle of mathematical induction, it contains all its
   affine combinations.

An affine combination of two points is of the form $\theta_1 x_1 + \theta_2 x_2$
where $\theta_1 + \theta_2 = 1$.
By {prf:ref}`definition <def-affine-set>` an affine set contains
all its 2 term affine combinations.

Now, assume that $C$ contains all its $k-1$ term affine combinations.

1. Consider points $x_1, \dots, x_{k-1}, x_k \in C$.
1. Let $\theta_1, \dots, \theta_{k-1}, \theta_k \in \RR$ 
   such that $\theta_1 + \dots + \theta_{k-1} + \theta_k = 1$.
1. Without loss of generality, assume that $\theta_k \neq 1$. Thus, $1 - \theta_k \neq 0$.
1. Note that $\theta_1 + \dots + \theta_{k-1} = 1 - \theta_k$.
1. Thus, $\frac{\theta_1}{1 - \theta_k} + \dots + \frac{\theta_{k-1}}{1- \theta_k} = 1$.
1. We can then write:

   $$
   \begin{aligned}
   x &= \sum_{i=1}^k \theta_i x_i =  \sum_{i=1}^{k-1} \theta_i x_i + \theta_k x_k \\
   &= (1 - \theta_k) \sum_{i=1}^{k-1} \frac{\theta_i}{1 - \theta_k} x_i + \theta_k x_k.
   \end{aligned}
   $$
1. Note that the term $y = \sum_{i=1}^{k-1} \frac{\theta_i}{1 - \theta_k} x_i$ is
   an affine combination of $k-1$ terms. 
1. Thus, by inductive hypothesis, $y \in C$.
1. We are left with 

   $$
   x = (1 - \theta_k) y + \theta_k x_k.
   $$
1. This is a two term affine combination. Since $y, x_k \in C$, hence $x \in C$.
1. Thus, we established that if $C$ contains its $k-1$ term affine combinations,
   it contains its $k$ term affine combinations too.
```

```{prf:proposition}
:label: res-aff-comb-aff-comb-aff-comb

An affine combination of affine combinations is an affine combination.
```

```{prf:proof}
Let $u = \sum_{i=1}^k \theta_i x_i$ and $v = \sum_{j=1}^l \lambda_j y_j$
where $x_i , y_j \in \VV$ and $\sum \theta_i = 1$ and $\sum \lambda_j = 1$.

We claim that $w = \gamma u + ( 1 - \gamma) v$ is also an affine combination.

$$
\begin{aligned}
w &= \gamma u + ( 1 - \gamma) v \\
&= \gamma \sum_{i=1}^k \theta_i x_i + ( 1 - \gamma) \sum_{j=1}^l \lambda_j y_j\\
&= \sum_{i=1}^k \gamma \theta_i x_i + \sum_{j=1}^l ( 1 - \gamma)  \lambda_j y_j.
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

Thus, $w$ is an affine combination of the points $x_i$ and $y_j$.

We can use the mathematical induction to show that arbitrary
affine combinations of affine combinations are affine combinations.
```

## Connection with Linear Subspaces

```{prf:proposition}
:label: res-aff-offset-plus-linear-subspace

Let $C$ be a nonempty affine set and $x_0$ be any element in $C$. Then the set

$$
    V = C  - x_0 = \{ x  - x_0 | x \in C\}
$$

is a linear subspace of $\VV$.
```
To show that $V$ is indeed a linear subspace, we can show that
every linear combination of two arbitrary elements in $V$
belongs to $V$.

```{prf:proof}
Let $v_1$ and $v_2$ be two elements in $V$. 
Then by definition, there exist $x_1$ and $x_2$ in $C$ such that

$$
    v_1 = x_1 - x_0 \text{ and } v_2 = x_2 - x_0.
$$

Thus 

$$
    a v_1 + v_2 = a (x_1 - x_0) + x_2 - x_0 
    = (a x_1 + x_2  - a x_0 )  - x_0 \Forall a \in \RR.
$$

But since $a + 1 - a = 1$, 
hence $x_3 = (a x_1 + x_2  - a x_0 ) \in C$ (an affine combination). 

Hence $a v_1 + v_2 = x_3 - x_0 \in V$ [by definition of $V$].

Thus, any linear combination of elements in $V$ belongs to $V$. 
Hence, $V$ is a linear subspace of $\VV$.
```

```{prf:observation}
With the previous result, we can use the following notation:

$$
    C = V + x_0 = \{ v + x_0 | v \in V\}
$$
where $V$ is a linear subspace of $\VV$ and $x_0 \in \VV$.
In other words, a nonempty affine set is a linear subspace with an offset.
```
We need to justify this notation by establishing that there
is one and only linear subspace associated with an affine set.
This is done in the next result.

```{prf:proposition}
Let $C$ be a nonempty affine set and
let $x_1$ and $x_2$ be two distinct elements in $C$.
Let $V_1 = C - x_1$ and $V_2 = C - x_2$, then the 
linear subspaces $V_1$ and $V_2$ are identical.
```
```{prf:proof}

We show that $V_1 \subseteq V_2$ and $V_2 \subseteq V_1$.

1. Let $v \in V_1$. 
1. There exists $x \in C$ such that $v = x - x_1$.
1. Then, $v = x - x_1 + x_2 - x_2$.
1. Let $y = x - x_1 + x_2$. Note that $x, x_1, x_2 \in C$ and
   $y$ is an affine combination of $x, x_1, x_2$.
1. Thus, $y \in C$.
1. We can now write $v = y - x_2$.
1. Thus, $v \in V_2$ as $V_2 = C - x_2$. 
1. Thus, $V_1 \subseteq V_2$.
1. An identical reasoning starting with some $v \in V_2$ gives us $V_2 \subseteq V_1$.
1. Thus, $V_1 = V_2$.
```

Thus the subspace $V$ associated with a nonempty affine set $C$ doesn't depend upon
the choice of offset $x_0$ in $C$.

## Affine Subspaces and Dimension

```{prf:definition} Affine subspace
:label: def-affine-subspace

A nonempty affine set is called an *affine subspace*.
An affine subspace is a linear subspace with an offset.

Another way to express this is as follows. $C$ is an 
affine subspace of $\VV$ if:

$$
C \neq \EmptySet \text{ and } \Forall \theta \in \RR, \quad C = \theta C + (1 - \theta) C.
$$
```


```{prf:definition}
:label: def-affine-dimension

We define the *affine dimension* of an affine subspace $C$ as the dimension
of the associated linear subspace $V = C - x_0$ for some $x_0 \in C$. 
```
The definition is consistent since $V$ is independent of the choice of
$x_0 \in C$.


```{prf:example}
For any $x \in \VV$, the singleton set $\{ x\}$ can be expressed as

$$
\{ x\} = x + \{ 0 \}.
$$
Its corresponding linear subspace is $\{0 \}$ of zero dimension.

Thus, the singleton set has an affine dimension of 0.
```

```{prf:example} Solution set of linear equations
We show that the solution set of linear equations forms an affine set.

Let $C = \{ x | A x = b\}$ where $A \in \RR^{M \times N}$ and $b \in \RR^M$.

Let $C$ be the set of all vectors $x \in \RR^N$ which satisfy the system of linear
equations given by $A x = b$. 
Then $C$ is an affine set.

Let $x_1$ and $x_2$ belong to $C$.  Then we have

$$
    A x_1 = b
$$ 

and 

$$
    A x_2 = b
$$

Thus 

$$
    &\theta A x_1 + ( 1 - \theta ) A x_2 = \theta b + (1 - \theta ) b\\
    &\implies A (\theta x_1 + (1  - \theta) x_2) = b\\
    &\implies (\theta x_1 + (1  - \theta) x_2) \in C
$$

Thus, $C$ is an affine set.

The subspace associated with $C$ is nothing but the
null space of $A$ denoted as $\NullSpace(A)$.
```

```{prf:remark}
Every affine set of $\RR^n$ can be expressed as the solution set of a 
system of linear equations.
If the system of equations is infeasible, then its solution set is
$\EmptySet$. Otherwise, its solution set is an affine subspace.
If the system of equations has a unique solution, then the solution
set is a singleton set which is an affine subspace of dimension 0.
```


```{prf:example} More affine sets
* The whole euclidean space $\RR^N$ is affine.
* Any line is affine. The associated subspace is a line 
  parallel to it which passes through origin.
* Any plane is affine. If it passes through origin, it's a
  subspace. The associated subspace is the plane parallel to it
  which passes through origin.
```

```{prf:proposition}
:label: res-aff-space-closed-aff-comb

An affine subspace is closed under affine combinations.
```
```{prf:proof}
This is from the definition of affine sets
and {prf:ref}`res-aff-set-contains-aff-combs`.
```

```{prf:observation}
Let $C$ be an affine subspace. 
Let $V$ be the linear subspace associated with $C$ given by $V = C - x$.
Then every vector $v \in V$ can be written as $v = y - x$ where $y \in C$.
Since $V$ doesn't depend on the choice of $x$, hence 
$V$ is the set of all vectors of the form $y - x$ where $y, x \in C$.

Thus, following the notation in 
{prf:ref}`def-vs-set-arithmetic`,
we can write $V$ as:

$$
V = C - C.
$$
```

## Affine Hull 

```{prf:definition}
:label: def-affine-hull

The set of all affine combinations of points in some arbitrary nonempty set 
$S \subseteq \VV$ 
is called the *affine hull* of $S$ and denoted as $\affine S$:

$$
    \affine S = \{\theta_1 x_1 + \dots + \theta_k x_k | x_1, \dots, x_k \in S \text{ and } \theta_1 + \dots + \theta_k = 1\}.
$$
```
```{prf:proposition}
:label: res-aff-hull-subspace

An affine hull is an affine subspace.
```
```{prf:proof}
Let $S \subset \VV$ be nonempty. Let $T = \affine S$. 
Let $u, v \in T$. Then

$$
u = \sum_{i=1}^{k} \theta_i x_i \text {and } v = \sum_{j=1}^{l} \lambda_j y_j
$$ 
where $x_i, y_j \in S$, $\sum \theta_i  = 1$ and $\sum \lambda_j = 1$.

Then, as shown in {prf:ref}`res-aff-comb-aff-comb-aff-comb`,

$$
w = \gamma u + (1 - \gamma) v
$$
is an affine combination of points $x_i, y_j \in S$.

Thus, $w \in T$. 
Hence, $T$ is an affine set. 
Since $T$ is nonempty, hence $T$ is an affine subspace.
```


```{prf:proposition}
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


```{prf:definition}
:label: def-affine-independence

A set of vectors $v_0, v_1, \dots, v_K \in \VV$ is called *affine independent*,
if the vectors $v_1 - v_0, \dots, v_K - v_0$ are linearly independent.

In other words, the difference vectors $v_k - v_0$ 
belong to the associated linear subspace. 
```
If the associated subspace has dimension $L$ then a maximum of $L$ vectors can 
be linearly independent in it. Hence a maximum of $L+1$ vectors can be affine
independent for the affine set.

