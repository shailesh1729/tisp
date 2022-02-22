# Relative Interiors
This section focuses on some topological properties
of convex sets.
Throughout this section, we assume that $\VV$ is a 
finite dimensional real normed linear space equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \| : \VV \to \RR$.
It is also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$.
Wherever necessary,
it is also equppied with an 
{prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle : \VV \times \VV \to \RR$. 

In a finite dimensional real normed linear space:

- Linear subspaces are closed.
- Hyperplanes are closed.
- Affine subspaces are closed.
- Interiors of proper linear/affine subspaces are empty.
- Linear/affine transformations are continuous.
- Bijective linear/affine transformations are homeomorphisms.
- Bijective linear/affine transformations preserve interiors and closures.


Following the discussion in {ref}`sec:la:normed-spaces`,
$B$ shall denote the open unit ball $B(\bzero, 1)$.
$\bar{B}$ shall denote the closed unit ball $B[\bzero, 1]$.
The open ball $B(\bx, r)$ (for some $r > 0$) can be written as
$\bx + r B$. 
Similarly, the closed ball $B[\bx, r]$ can be written as
$\bx + r \bar{B}$.


We shall use several set and vector arithmetic identities
and inequalities in the discussion below. We list them here 
for quick reference. See {ref}`sec:la:set-arithmetic`
for detailed discussion.

Let $C,D,E$ be subsets of $\VV$.
Let $\bx, \bv, \bz \in \VV$ be arbitrary vectors.

From {prf:ref}`res-vs-set-vec-arithmetic`

$$
C = (C + \bz) - \bz.
$$


$$
C \subseteq D \iff C + \bz \subseteq D + \bz.
$$


From {prf:ref}`res-vs-set-intersect-sum-dist`,

$$
(C \cap D) + E \subseteq (C + E) \cap (D + E).
$$

For any set $A \subseteq \VV$, the set of points $\bx$
whose distance from $A$ is less than $r$ for some $r > 0$
is given by:

$$
A + r B = \bigcup_{\ba \in A} \ba + r B 
= \{\bx \ST \exists \ba \in A, d(\ba, \bx) < r \}.
$$

Recall from {prf:ref}`res-la-closure-point-ball` that
$\bx \in \closure A$ if and only if

$$
\bx \in A + r B \Forall r > 0.
$$ 
Similarly, recall from {prf:ref}`res-la-interior-point-ball` 
that $\bx \in \interior A$ if and only if 

$$
\exists r > 0 \text{ such that } \bx + r B \subseteq A.
$$


## Relative Interior

```{prf:definition} Relative interior point
:label: def-cvx-relative-interior-point
Let $\VV$ be a normed linear space.
Let $C \subseteq \VV$. We say that $\bx \in C$ 
is a *relative interior point* of $C$ if
there exists an open ball $B(\bx, r)$ for some $r > 0$
such that 

$$
B(\bx, r) \cap \affine C \subseteq C.
$$
```

Note that, the open ball $B(\bx, r)$ itself need not be
contained inside $C$.

```{prf:definition} Relative interior
:label: def-cvx-relative-interior

The *relative interior* of a set $C$, denoted by $\relint C$
is the set of 
all its relative interior points.

$$
\relint C \triangleq \{\bx \in C \ST \exists r > 0, 
B(\bx, r) \cap \affine C \subseteq C \}.
$$
```

$C$ may have an empty interior
and yet may have a nonempty relative interior.
Often, a convex set lies in a low dimensional
(affine or linear) subspace of the ambient vector space.
Thus, the interior of the convex set is empty.
At the same time, the relative interior of the set
(w.r.t. its affine hull) need not be empty.
It plays a similar topological role as the interior of a set.
We develop some fundamental results on the relative
interior of a convex set.


```{prf:theorem} Relative interiors are subset
:label: res-cvx-relint-subset

For any set $C$

$$
\relint C \subseteq C.
$$
```

```{prf:proof}
This follows directly from the definition of
relative interior.
```

```{prf:theorem} Relative interior and interior
:label: res-cvx-relint-interior


For any set $C$

$$
\interior C \subseteq \relint C.
$$
```

```{prf:proof}
Let $\bx \in \interior C$.

1. Then, there exists $r > 0$ such that $B(\bx, r) \subseteq C$.
1. But $B(\bx, r) \subseteq C$ implies that 
   $B(\bx, r) \cap \affine C \subseteq C$.
1. Thus, $\bx \in \relint C$ also holds.

Thus, $\interior C \subseteq \relint C$.
```

### Containment Relationship

In general $A \subseteq B$ implies that
$\interior A \subseteq \interior B$ and 
$\closure A \subseteq \closure B$. 
However, this is not the case with relative interiors.

```{prf:remark}
:label: res-cvx-relint-non-inclusive

An inclusion $A \subseteq B$ does not imply 
$\relint A \subseteq \relint B$.

Consider $C$ to be a cube in $\RR^3$ and
$A$ to be one of its faces.
The relative interiors of both $A$ and $C$ are nonempty
but disjoint.
```

However, if the affine hulls of $A$ and $B$ are same,
then $A \subseteq B$ does imply that $\relint A \subseteq \relint B$.

```{prf:theorem} Relative interior and containment
:label: res-cvx-relint-subset-rel


Let $A, B \subseteq \VV$.
If $A \subseteq B \subseteq \affine A$, 
then $\relint A \subseteq \relint B$.
```

```{prf:proof}
By {prf:ref}`res-affine-hull-tight-containment`,
$\affine A = \affine B$.

Now, let us focus on the relative interiors.

1. Let $\bx \in \relint A$.
1. Then, there exists $r > 0$ such that

   $$
   B(\bx, r) \cap \affine A \subseteq A.
   $$
1. Replace $\affine A$ by $\affine B$ and use the fact that $A \subseteq B$.
   Thus,

   $$
   B(\bx, r) \cap \affine B \subseteq B.
   $$
1. Thus, $\bx \in \relint B$.

Thus, $\relint A \subseteq \relint B$.
```


```{prf:theorem} Relative interior of closure
:label: res-cvx-closure-relint

Let $\VV$ be a real finite dimensional normed linear space.
For any set $C \subseteq \VV$ 

$$
\relint C \subseteq \relint \closure C.
$$
```

```{prf:proof}
The statement is trivial for $C = \EmptySet$. We shall
assume that $C$ is nonempty.

1. $C \subseteq \closure C$
1. Since $\VV$ is finite dimensional, 
   hence by {prf:ref}`res-la-affine-hull-closure`, 
   $\affine (\closure C) = \affine C$.
1. Thus, $C \subseteq \closure C \subseteq \affine C$.
1. Thus, by {prf:ref}`res-cvx-relint-subset-rel`,
   we have $\relint C \subseteq \relint \closure C$.
```

### Relatively Open Sets

```{prf:definition} Relatively open set
:label: def-cvx-relatively-open

We say that a set $C$ is *relatively open* if $C$
is open relative to its affine hull $\affine C$.
In other words, $C$ is *relatively open* if

$$
\relint C = C.
$$
```

### Affine Sets

```{prf:theorem} Affine sets are relatively open
:label: res-cvx-affine-relative-open

An affine set is relatively open.
```

```{prf:proof}
Let $A$ be an affine set. Then, $\affine A = A$.
Thus, for any $\bx \in A$

$$
B(\bx, r) \cap \affine A = B(\bx, r) \cap A \subseteq A.
$$
Thus, every $\bx \in A$ is a relative interior point of $A$.
Thus,

$$
\relint A = A.
$$ 
```

```{prf:corollary} Hyperplanes are relatively open
:label: res-cvx-hyperplane-relative-open

The relative interior of a hyperplane is the hyperplane itself. 
A hyperplane is relatively open.
```
This is a consequence of the fact that every hyperplane
is affine.


An affine set in a finite dimensional vector space 
is also closed since it is an
intersection of hyperplanes and every hyperplane
is a closed set. See {prf:ref}`res-la-affine-closed`

### Relative Interior of Relative Interior

```{prf:theorem} Relative interior is relatively open
:label: res-cvx-relint-relint

For any set $C$, 

$$
\relint (\relint C) = \relint C.
$$
Thus, $\relint C$ is relatively open.
```
TODO this proof is not solid.

```{prf:proof}
By definition $\relint (\relint C) \subseteq \relint C$.

Thus, we need to show that $\relint C \subseteq \relint (\relint C)$.

1. Let $\bx \in \relint C$.
1. Then, there exists $r > 0$ such that 
   
   $$
   (\bx + r B) \cap \affine C \subseteq C.
   $$
1. We can write $\bx + rB$ as 

   $$
   \bx + r B = \left (\bx + \frac{r}{2} B \right ) + \frac{r}{2} B.
   $$
1. Thus, the previous inclusion can be written as 
   
   $$
   \left ( \left (\bx + \frac{r}{2} B \right ) + \frac{r}{2} B \right ) 
   \cap \affine C \subseteq C.
   $$
1. Let $U = \left (\bx + \frac{r}{2} B \right ) \cap C$.
1. Let $\by \in U$.
1. Then, $\by \in C$ and $\by \in \left (\bx + \frac{r}{2} B \right )$.
1. From previous inclusion, we can say that for every $\by \in U$

   $$
   \left (\by + \frac{r}{2} B \right ) \cap \affine C \subseteq C.
   $$
1. Thus, $\by \in \relint C$ for every $\by \in U$.
1. Thus, $U \subseteq \relint C$.
1. Thus, 

   $$
   \left (\bx + \frac{r}{2} B \right ) \cap C \subseteq \relint C.
   $$
1. By definition of relative interior, $\bx \in \relint (\relint C)$.
```

### Relative Boundary

```{prf:definition} Relative boundary
:label: def-cvx-relative-boundary

The *relative boundary* of a set $C$, denoted by $\relbd C$
is given by

$$
\relbd C \triangleq \closure C \setminus \relint C.
$$
```

## Translations

```{prf:theorem} Translations preserve relative interiors
:label: res-cvx-relint-translation-pres

Let $\VV$ be a normed linear space.
Let $\ba \in \VV$ be some fixed vector.
Let a translation map $g_a : \VV \to \VV$ be defined as

$$
g_a = \bx + \ba \Forall \bx \in \VV.
$$

Then, for any set $A \subseteq \VV$,

$$
g_a (\relint A) = \relint (g_a (A)).
$$

In other words,

$$
\relint (A + \ba) = (\relint A)  + \ba.
$$
```



```{prf:proof}

Let $\bx \in \relint (A + \ba)$.

1. Then, there exists $r > 0$ such that

   $$
   (\bx + r B ) \cap \affine (A + \ba) \subseteq A + \ba.
   $$
1. Let $\by = \bx - \ba$. 
1. Since $\bx \in A + \ba$ hence $\by \in A$.
1. Consider the set:

   $$
   R = (\by + r B) \cap \affine A.
   $$
1. We have

   $$
   R + \ba &= ((\by + r B) \cap \affine A) + \ba\\
   &\subseteq ((\by + r B) + \ba) \cap ((\affine A) + \ba)\\
   &= (\bx + r B) \cap (\affine (A + \ba))\\
   &\subseteq A + \ba.
   $$
   1. Recall that $(C \cap D) + E \subseteq (C + E) \cap (D + E)$.
   1. $(\affine A) + \ba = \affine (A + \ba)$ since
      translation which is an affine transformation
      preserves affine hulls ({prf:ref}`res-la-aff-func-aff-hull`).
1. Thus, $R + \ba \subseteq A + \ba$.
1. Thus, $R \subseteq A$.
1. Thus, $\by \in \relint A$.
1. Thus, $\bx - \ba \in \relint A$.
1. Thus, $\bx \in \relint A + \ba$.

Thus, $\relint (A + \ba) \subseteq \relint A + \ba$.

For the converse, assume that
$\bx \in \relint A + \ba$.

1. Then, $\bx - \ba \in \relint A$.
1. Let $\by = \bx - \ba$.
1. Then, there exists $r > 0$ such that

   $$
   (\by + r B ) \cap \affine A \subseteq A.
   $$
1. Consider the set

   $$
   R = (\bx + r B) \cap \affine (A + \ba).
   $$

1. We have

   $$
   R - \ba &= ((\bx + r B) \cap \affine (A + \ba)) - \ba\\
   &\subseteq ((\bx + r B) - \ba) \cap ((\affine (A + \ba)) - \ba)\\
   &= (\by + r B) \cap (\affine (A + \ba) - \ba)\\
   &= (\by + r B) \cap \affine A\\
   &\subseteq A.
   $$
1. Thus, $R - \ba \subseteq A$.
1. Thus, $R \subseteq A + \ba$.
1. Thus, $\bx \in \relint (A + \ba)$.

Thus, $\relint A + \ba \subseteq \relint (A + \ba)$.

Together, we have

$$
\relint A + \ba = \relint (A + \ba)
$$
```

## Convex Sets

Relative interiors play the role of interiors for convex sets.
Much of the following discussion is focused on the relative
interiors of convex sets (in finite dimensional real normed linear spaces).


### Nonempty Relative Interiors

```{prf:theorem} Nonempty relative interiors
:label: res-cvx-nonempty-relint

If $C$ is a nonempty convex set, then its relative interior
is nonempty.
```

```{prf:proof}

Let $A = \affine C$ and let $\dim A = k$.

1. Choose $k+1$ affine independent points of $C$:
   $\bv_0, \dots, \bv_k$.
1. Let $H = \ConvexHull \{\bv_0, \dots, \bv_k \}$ be their convex hull.
1. Since $C$ is convex, it contains the convex hull $H$;
   i.e., $H \subseteq C$.
1. $H$ contains all convex combinations of  $\{\bv_0, \dots, \bv_k \}$.
1. In particular, it contains the point:

   $$
   \bv = \frac{1}{k+1} (\bv_0 + \dots + \bv_k).
   $$
1. Note that $\bv \in H \subseteq C$.
1. Note that $A = \affine C = \affine \{\bv_0, \dots, \bv_k \} = \affine H$.
1. Thus, we can select a sufficiently small $r > 0$ 
   such that all points in $B(\bv, r) \cap A$ are contained in $H$.
1. But then, $B(\bv, r) \subseteq H \subseteq C$.
1. Thus, $\bv \in C$ and $B(\bv, r) \cap A \subseteq C$. 
1. Thus, $\bv \in \relint C$.
1. Thus, the relative interior of $C$ is nonempty.
```


### Line Segment Property

```{prf:theorem} Line segment property of relative interior
:label: res-cvx-convex-relint-segment

Let $\VV$ be a finite dimensional normed linear space.

Let $C$ be a nonempty convex subset of $\VV$. 
Let $\bx \in \relint C$
and $\by \in \closure C$. Then, 

$$
(1-t) \bx + t \by \in \relint C \Forall t \in [0,1).
$$
```

```{prf:proof}
Let $C$ be a convex set. Fix some $t \in [0,1)$.
For simplicity, we shall assume that $\relint C = \interior C$.
Let $B$ denote the unit open ball $B(\bzero, 1)$.

1. Let $\bz = (1-t) \bx + t \by$. 
   It suffices to show that there is an open ball
   $B(\bz, r) \subseteq C$.
1. Since $\by \in \closure C$, hence for every $r > 0$, 
   we have $\by \in C + r B$.
1. Then,

   $$
   \bz + r B &= (1-t)\bx + t \by + r B \\
   &\subseteq (1-t)\bx + t (C + r B) + r B \\
   &= (1-t)\bx + (1 + t) rB + t C\\
   & = (1 -t)(\bx + r (1+t)(1-t)^{-1} B) + t C.
   $$
1. Since $\bx \in \interior C$, hence we can take $r$ to be so small 
   such that

   $$
   \bx + r (1+t)(1-t)^{-1} B \subseteq C.
   $$
1. But then

   $$
   (1 -t)(\bx + r (1+t)(1-t)^{-1} B) + t C 
   &\subseteq (1 -t) C + t C\\ 
   &\subseteq C
   $$
   since $C$ is convex and $t \in [0,1)$.
1. Thus, we established that there exists an $r > 0$ 
   such that $\bz + r B \subseteq C$.
1. Hence, $\bz \in \interior C = \relint C$.

This argument can be extended for the case where
$\relint C \neq \interior C$.
```
One way to interpret this result is as follows.
If we draw a line segment between a point
in the relative interior of a convex set $C$
and a point on the boundary of $C$, then 
every point on the segment (except the boundary point)
lies inside the relative interior of $C$.

Several topological properties follow.


### Closure of Relative Interior

```{prf:theorem} Closure of relative interior
:label: res-cvx-relint-closure

For any convex set $C$, 

$$
\closure \relint C = \closure C.
$$
```

```{prf:proof}
Since $\relint C \subseteq C$, hence
$\closure \relint C \subseteq \closure C$.


For the other direction, we proceed as follows:

1. Let $\by \in \closure C$.
1. Choose some $\bx \in \relint C$.
1. By {prf:ref}`res-cvx-convex-relint-segment`, 
   the line segment between $\bx$ and $\by$
   (excluding $\by$) lies in $\relint C$.
1. Hence, $\by$ is a limit point of $\relint C$.
1. Thus, $\by \in \closure \relint C$.
1. Thus, $\closure C \subseteq \closure \relint C$.

Combining the two inclusions, we get:

$$
\closure \relint C = \closure C.
$$ 
```

### Relative Interior of Closure

```{prf:theorem} Relative interior of closure
:label: res-cvx-convex-closure-relint

For any convex set $C$, 

$$
\relint \closure C = \relint C.
$$
```

```{prf:proof}
The statement is trivial for $C = \EmptySet$. We shall
assume that $C$ is nonempty.

By {prf:ref}`res-cvx-closure-relint`
$\relint C \subseteq \relint \closure C$
holds true for any set $C$.


For the converse, assume that $\bx \in \relint \closure C$.
Our goal is to show that $\bx \in \relint C$. 
Towards this, we have to find points $\by \in \relint C$
and $\bz \in \closure C$ such that $\bx$ lies
on the line segment between $\by$ and $\bz$. 
Since, $C$ is nonempty and convex, it is easy
to pick a point $\by \in \relint C$. Then,
on the path from $\by$ to $\bx$, the point
$\bz$ must be behind $\bx$ and yet not too far 
behind $\bx$ so that we can ensure that $\bz$
is indeed in $\closure C$. That is where
we use the fact that there is a ball 
around $\bx$ whose intersection with $\affine C$
is totally inside $\closure C$.

1. We have, $\bx \in \closure C$ and there exists $r > 0$ such that

   $$
   (\bx + r B) \cap \affine (\closure C) \subseteq \closure C.
   $$
1. Recall from {prf:ref}`res-la-affine-hull-closure` that 
   $\affine (\closure C) = \affine C$.
1. Thus, there exists $r > 0$ such that

   $$
   (\bx + r B) \cap \affine C \subseteq \closure C.
   $$
1. By {prf:ref}`res-cvx-nonempty-relint`, the relative
   interior of $C$ is nonempty.
1. Choose a point $\by \in \relint C$.
1. Let $t = \frac{r}{2\| \bx - \by \|}$.
1. Define
   
   $$
   \bz = (1 + t) \bx - t \by.
   $$
1. $\bz$ is an affine combination of $\bx$ and $\by$.
   Since $\bx \in \closure C$ and $\by \in \relint C \subseteq \closure C$,
   hence $\bz \in \affine (\closure C) = \affine C$.
1. Also note that

   $$
   d(\bz, \bx) &= \| \bz - \bx \|\\
   &= \|(1 + t) \bx - t \by - \bx \|\\
   &= t \| \bx - \by \| = \frac{r}{2}.
   $$
1. Hence, $\bz \in B(x, r)$.
1. Thus, $\bz \in B(x, r) \cap \affine C \subseteq \closure C$.
1. Thus, $\bz \in \closure C$.
1. We have found the points $\by \in \relint C$ and $\bz \in \closure C$.
1. Now note that, 

   $$
   \bx = \frac{t}{1+t} \by + \frac{1}{1+t} \bz.
   $$
1. Thus, $\bx$ is a convex combination of $\by$ and $\bz$.
1. Since $t > 0$,  hence $\bx$ lies in the line segment 
   between $\bz$ and $\by$.
1. By the 
   {prf:ref}`line segment property <res-cvx-convex-relint-segment>`, 
   the line segment between $\bz$ and $\by$
   (excluding $\bz$) lies in $\relint C$.
1. Hence, $\bx \in \relint C$.

Thus, we have shown that $\relint \closure C \subseteq \relint C$
as desired.
```

## Affine Transformations

```{prf:theorem}
:label: res-cvx-relint-aff-map-pres

Let $\VV$ be a finite dimensional normed linear space.
A bijective affine transformation $T : \VV \to \VV$ 
preserves relative interiors.

$$
T (\relint A) = \relint (T (A)).
$$
```

