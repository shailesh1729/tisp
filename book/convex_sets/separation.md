(sec:cvx:separation:theorems)=
# Separation Theorems

```{div}
Separation theorems provide us ways to find a separating hyperplane
between two disjoint convex sets. Hyperplanes
require the notion of an inner product. 

Throughout this section, we assume that $\VV$ is a finite dimensional
real vector space
endowed with
{prf:ref}`norm <def-la-norm>` $\| \cdot \| : \VV \to \RR$
and a {prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle : \VV \times \VV \to \RR$. 
The norm in general is not necessarily induced by the inner product.
The Euclidean norm is denoted by $\| \cdot \|_2$.
```

## Types of Separating Hyperplanes

```{prf:definition} Separating hyperplane
:label: def-cvx-separating-hyperplane

Let $\VV$ be a real $n$-dimensional vector space.
For any two subsets $C$ and $D$ of $\VV$, a hyperplane
$H$ is said to *separate* $C$ and $D$ if
$C$ is contained in one of the closed halfspaces
corresponding to $H$ and $D$ is contained in the other 
closed halfspace.
```

```{div}
Let $H$ be given by

$$
H =  \{ \bx \in \VV \ST \langle \bx, \ba \rangle = b \}
$$
where $\ba \in \VV^*$ and $b \in \RR$.

If $C$ and $D$ are separated by $H$, then either

$$
\langle \bx_1, \ba \rangle \leq b \leq \langle \bx_2, \ba \rangle
\Forall \bx_1 \in C, \bx_2 \in D
$$
or

$$
\langle \bx_2, \ba \rangle \leq b \leq \langle \bx_1, \ba \rangle
\Forall \bx_1 \in C, \bx_2 \in D
$$
holds true.

We can also say that the two sets $C$ and $D$ can
be separated by a hyperplane or there exists
a hyperplane separating $C$ and $D$ if there
exists a nonzero vector $\ba \in \VV^*$ such that

$$
\sup_{\bx \in C} \langle \bx, \ba \rangle \leq
\inf_{\bx \in D} \langle \bx, \ba \rangle.
$$
Any choice of $b \in [l,u]$ where $l = \sup_{\bx \in C} \langle \bx, \ba \rangle$
and $u = \inf_{\bx \in D} \langle \bx, \ba \rangle$
describes a separating hyperplane.
```

This definition allows for some degenerate possibilities where
both $C \subseteq H$ and $D \subseteq H$ since the closed
halfspaces contain $H$ (as their boundary).

```{prf:definition} Proper separation
:label: def-cvx-proper-separation

Let $\VV$ be a real $n$-dimensional vector space.
For any two subsets $C$ and $D$ of $\VV$, a hyperplane
$H$ is said to *properly separate* $C$ and $D$ if
$H$ separates them and both are not entirely contained
in $H$; i.e., either $C \not\subseteq H$ or $D \not\subseteq H$
or both.
```
Proper separation still allows for the possibility that
parts of $C$ or $D$ lies inside $H$. But it ensures that
$C \triangle D \neq \EmptySet$.
$C \cap D \subseteq H$ is the common part.

```{div}
If $C$ and $D$ are properly separated by $H$, then
they are also separated by $H$. Hence

$$
\langle \bx_1, \ba \rangle \leq b \leq \langle \bx_2, \ba \rangle
\Forall \bx_1 \in C, \bx_2 \in D
$$
or

$$
\langle \bx_2, \ba \rangle \leq b \leq \langle \bx_1, \ba \rangle
\Forall \bx_1 \in C, \bx_2 \in D
$$
holds true. 
Also, there exists at least one $\bx_1 \in C$
and $\bx_2 \in D$ such that at least one of these inequalities
is a strict inequality thus ensuring that either $C$
or $D$ or both are not contained entirely in $H$.


We can also say that the two sets $C$ and $D$ can
be properly separated by a hyperplane or there exists
a hyperplane properly separating $C$ and $D$ if there
exists a nonzero vector $\ba \in \VV^*$ such that

$$
\sup_{\bx \in C} \langle \bx, \ba \rangle \leq
\inf_{\bx \in D} \langle \bx, \ba \rangle.
$$
and

$$
\inf_{\bx \in C} \langle \bx, \ba \rangle <
\sup_{\bx \in D} \langle \bx, \ba \rangle.
$$
Any choice of $b \in [l,u]$ where $l = \sup_{\bx \in C} \langle \bx, \ba \rangle$
and $u = \inf_{\bx \in D} \langle \bx, \ba \rangle$
describes a properly separating hyperplane.
This characterization is proved in
{prf:ref}`res-cvx-proper-sep-charac` below.
```

If a convex set has a nonempty interior,
then it cannot be contained in a hyperplane.
Two disjoint sets one of which has a
nonempty interior can indeed be properly
separated.

```{prf:definition} Strong separation
:label: def-cvx-strong-separation

Let $\VV$ be a real $n$-dimensional vector space.
For any two subsets $C$ and $D$ of $\VV$, a hyperplane
$H$ is said to *strongly separate* $C$ and $D$ if
there exists an $r > 0$ such that 
$C + r B$ is contained in one of the open halfspaces
corresponding to $H$ and $D + rB$ is contained in the other 
open halfspace.
```
```{div}
Under these assumptions, one set lies in the interior of $H_{++}$
and the other set lies in the interior of $H_{--}$.
Under strong separation, $C \cap D = \EmptySet$ is guaranteed
since $H_{++} \cap H_{--} = \EmptySet$.

We can also say that the two sets $C$ and $D$ can
be strongly separated by a hyperplane or there exists
a hyperplane strongly separating $C$ and $D$ if there
exists a nonzero vector $\ba \in \VV^*$ such that

$$
\sup_{\bx \in C} \langle \bx, \ba \rangle <
\inf_{\bx \in D} \langle \bx, \ba \rangle.
$$
Any choice of $b \in (l,u)$ where $l = \sup_{\bx \in C} \langle \bx, \ba \rangle$
and $u = \inf_{\bx \in D} \langle \bx, \ba \rangle$
describes a strongly separating hyperplane.

Strong separation is called as strict separation
in {cite}`bertsekas2003convex`.
```


```{prf:remark}
:label: rem-cvx-separation-translation-invariance

Separation is translation invariant.
For any $\ba \in \VV$ and convex sets $C, D \subseteq \VV$,

$C$ and $D$ are separated by a hyperplane $H$ if and 
only if $C - \ba$, $D -\ba$ are separated by the hyperplane $H - \ba$.
```

## Disjoint Affine and Convex Sets

Separation between sets can be discussed at several levels.
We start with a simple case where an affine set
and a relatively open convex set are disjoint.

```{prf:theorem} Disjoint affine and relatively open convex sets
:label: res-cvx-sep-affine-rel-open-convex

Let $\VV$ be a real $n$-dimensional vector space.
Let $C$ be a nonempty relatively open convex set of $\VV$.
Let $M \subseteq \VV$ be an affine subspace such that
$M \cap C = \EmptySet$. 
Then, there exists a hyperplane $H$ such that $M \subseteq H$
and one of the two open halfspaces associated with $H$ contains
$C$. 
```

```{prf:proof}

Consider the case where $M$ is a hyperplane. Then, $H = M$ 
and the result is immediate.

1. If for contradiction, $C$ is not contained in one of the
   open halfspaces of $M$.
1. Then, $C \cap H \neq \EmptySet$  since $H$ is the 
   boundary of the halfspaces.
1. It will contradict 
   our hypothesis that $C \cap M = \EmptySet$.
1. Thus, $C$ must be in one of the open halfspaces of $H$.


Now, assume that $M$ is not a hyperplane. 

Without loss of generality, assume that $\bzero \in M$.
We can do this by picking any element $\bm$ of $M$ 
and replacing $M$ by $M - \bm$ and $C$ by $C - \bm$.
Thus, $M$ is a subspace.

The proof is constructive. We iteratively construct
subspaces of increasing dimension which contain $M$
but don't contain $C$ till we reach a hyperplane.

1. Let $\dim M = d$ where $d  < n$. 
1. Let $S = M$ be the initial subspace.
1. Let $r=n-1-d$ be the number of iterations
   (if $M$ is a hyperplane, no iterations are needed).
1. For $i=1,\dots,r$:
   1. Replace $S$ by a subspace $S'$ such that $\dim S' = \dim S + 1$ 
      and $S' \cap C = \EmptySet$.
   1. Let $S = S'$
1. We have arrived with a hyperplane $S$ such that $S \cap C = \EmptySet$.

 
Towards this, let us look at the procedure to
construct $S'$ from $S$ such that $\dim S' = \dim S + 1$
and $S \cap C = \EmptySet$. Here is the outline

1. Let $S^{\perp}$ be the orthogonal complement of $S$.
1. Pick any 2D subspace $P$ of $S^{\perp}$.
1. Pick a line $L$ in $P$ which passes through origin 
   but doesn't intersect with $C$; i.e. $L \cap C = \EmptySet$.
1. Construct the subspace $S' = S \oplus L$. 
   The direct sum is valid since $S \cap L = \{ \bzero \}$.
1. Note that $\dim S' = \dim S + 1$ and $S' \cap C = \EmptySet$
   since $S \cap C = \EmptySet$ as well as $L \cap C = \EmptySet$.

We now elaborate the procedure for finding the line $L$:

1. We have $S$ as a linear subspace with $\dim S < n -1$
   and $S \cap C = \EmptySet$.
1. $\dim S^{\perp} = n  - \dim S > n - (n - 1) = 1$.
1. Since $\dim S^{\perp} > 1$, it contains a two dimensional subspace $P$.
1. Consider the set $C' = P \cap (C - S)$.
1. The set $C-S$ has some properties.
   1. $C-S$ is convex since it is the sum of two convex sets.
   1. Since $\bzero \in S$, hence $C = C - \bzero \subseteq C - S$.
   1. Since $C \cap S = \EmptySet$, hence $\bzero \notin C - S$.
   1. Note that due to {prf:ref}`res-cvx-convex-sum-relint`:

      $$
      \relint (C - S) = \relint C - \relint S = C - S
      $$
      since $C$ is relatively open and $S$ is affine, hence relatively open.
   1. Thus, $C - S$ is relatively open.
1. Consequently, the set $C'$ also has some properties.
   1. $C'$ is convex since it is the intersection of two convex sets.
   1. Since  $\bzero \notin C - S$, 
      hence, $\bzero \not\in C' = P \cap (C - S)$.
   1. $C'$ is relatively open.
      1. If $C'$ is empty, then $C'$ is relatively open vacuously.
      1. Otherwise, by
      {prf:ref}`res-cvx-convex-affine-intersect-pres-relint-cl`:

      $$
      \relint C' = \relint (P \cap (C - S)) = P \cap \relint (C - S) = P \cap (C- S).
      $$
      Thus, $\relint C' = C'$ implies that $C'$ is relatively open.
1. We now seek a line $L \subseteq P$ passing through the origin $\bzero$ 
   that doesn't intersect $C'$.
1. We note that $L \cap C' = \EmptySet \implies L \cap C = \EmptySet$.
   1. Suppose for contradiction that
      $L \cap C' = \EmptySet$ but $L \cap C \neq \EmptySet$.
   1. Let $\bx \in L \cap C$.
   1. Then, $\bx \in L \subseteq P$.
   1. Also, $\bx \in C \subseteq C - S$.
   1. Thus, $\bx \in C' = P \cap (C - S)$.
   1. This means that $\bx \in L \cap C'$.
   1. In other words, $L \cap C' \neq \EmptySet$ which
      contradicts our assumption.
1. How to choose $L$? There are three possibilities:

   1. $C'$ is empty.
   1. $C'$ is contained in a line; i.e., $\dim \affine C' = 1$.
   1. $\affine C' = P$ and $\dim \affine C' = 2$.

   $\affine C'$ cannot be larger than $P$ since $C' \subseteq P$
   and $P$ is affine.
1. If $C'$ is empty, then any line in $P$ passing through origin will do.
1. If $\affine C$ is a line.
   1. If $\affine C'$ passes through the origin, we can take a line
      perpendicular to $\affine C'$ passing through origin.
      In this case, $L \cap \affine C' = \{\bzero \}$.
      Since $\bzero \notin C'$, hence $L \cap C' = \EmptySet$. 
   1. If $\affine C'$ is a line that doesn't pass through $\bzero$, we
      can simply take a line that is parallel to $\affine C'$ and passes
      through $\bzero$. In this case $L \cap \affine C' = \EmptySet$.
      Consequently, $L \cap C' = \EmptySet$.
1. If $\affine C'$ is the entire 2D subspace $P$.
   1. Consider the set $K = \bigcup \{t C' \ST t > 0 \}$.
   1. $C' \subseteq K$ (specifically, for $t = 0$).
   1. $K$ is a convex cone containing $C'$ but not containing $\bzero$. 
   1. $K$ is relatively open since $C'$ is relatively open.
   1. A boundary ray of $K$ doesn't intersect with $C'$ since
      $K$ is relatively open. 
   1. Take $L$ to be any of the two boundary rays of $K$ and extend
      it to a line passing through $\bzero$.
```


## Proper Separation Characterization


```{prf:theorem} Characterization of proper separation
:label: res-cvx-proper-sep-charac

Let $\VV$ be an $n$-dimensional real vector space.
Let $S$ and $T$ be nonempty subsets of $\VV$. There exists
a hyperplane $H$ that separates $S$ and $T$ *properly*
if and only if there exists a vector $\ba \in \VV$
such that

$$
\inf \{ \langle \bx, \ba \rangle \ST \bx \in S \} 
\geq \sup \{ \langle \bx, \ba \rangle \ST \bx \in T \}
$$
and

$$
\sup \{ \langle \bx, \ba \rangle \ST \bx \in S \} 
>  \inf \{ \langle \bx, \ba \rangle \ST \bx \in T \}.
$$
```

```{prf:proof}
Assume that there is some vector $\ba \in \VV$
satisfying the conditions above.

1. Since $\ba$ satisfies the second strict inequality,
   hence $\ba \neq \bzero$. Otherwise, the second
   inequality cannot hold.
1. Choose any $b \in \RR$ such that

   $$
   \underset{\bx \in S}{\inf}\{ \langle \bx, \ba \rangle \}
   \geq b \geq 
   \underset{\bx \in S}{\sup}\{ \langle \bx, \ba \rangle \}.
   $$
1. Then, the set $H = \{ \bx \ST \langle \bx, \ba \rangle = b \}$
   is a hyperplane.
1. Let $H_+ = \{ \bx \ST \langle \bx, \ba \rangle \geq b \}$
   and $H_- = \{ \bx \ST \langle \bx, \ba \rangle \leq b \}$.
1. Clearly, $S \subseteq H_+$ and $T \subseteq H_-$.
1. The second strict inequality ensures that both $S$ and $T$ cannot
   be contained in $H$. 
   1. For contradiction, assume $S \subseteq H$ and $T \subseteq H$ 
   1. Then $\sup \{ \langle \bx, \ba \rangle \ST \bx \in S \} = b$
      and $\inf \{ \langle \bx, \ba \rangle \ST \bx \in T \} = b$.
   1. Thus, the second inequality will not hold.
1. Thus, $S$ and $T$ are properly separated.

Now, assume that $S$ and $T$ are properly separated by 
some hyperplane $H$.

1. Let $H = \{ \bx \ST \langle \bx, \ba \rangle = b \}$ be
   the specification of the said hyperplane.
1. Let $H_+ = \{ \bx \ST \langle \bx, \ba \rangle \geq b \}$
   and $H_- = \{ \bx \ST \langle \bx, \ba \rangle \leq b \}$.
1. Without loss of generality, assume that $S \subseteq H_+$
   and $T \subseteq H_+$.
1. Then, $\langle \bx, \ba \rangle \geq b$ for every $\bx \in S$.
1. Thus, $\inf \{ \langle \bx, \ba \rangle \ST \bx \in S \} \geq b$.
1. Similarly, $\langle \bx, \ba \rangle \leq b$ for every $\bx \in T$.
1. Thus, $\sup \{ \langle \bx, \ba \rangle \ST \bx \in T \} \leq b$.
1. Thus, the first inequality is satisfied.
1. Since $H$ properly separates $S$ and $T$, hence
   either $S \not\subseteq H$ or $T \not\subseteq H$. 
1. If $S \not\subseteq H$, 
   then there exists $\bx \in S$ such that $\langle \bx, \ba \rangle > b$.
1. Consequently, $\sup \{ \langle \bx, \ba \rangle \ST \bx \in S \} > b$.
1. If $T \not\subseteq H$,
   then there exists $\bx \in T$ such that 
   $\langle \bx, \ba \rangle < b$.
1. Consequently, $\inf \{ \langle \bx, \ba \rangle \ST \bx \in T \} < b$.
1. Combining, 
   
   $$
   \sup \{ \langle \bx, \ba \rangle \ST \bx \in S \} 
   >  \inf \{ \langle \bx, \ba \rangle \ST \bx \in T \}
   $$
   must be true.
```

### Proper Separation : Set and Point

```{prf:remark} Proper separation between a set and a point
:label: res-cvx-proper-sep-set-point-def

Let $\VV$ be an $n$-dimensional real vector space.
We consider the case of proper separation between
a set $S$ and a point $\bp$.
We can form a set $T = \{ \bp \}$.
Then the proper separation between $S$ and $\bp$ can be described
in terms of proper separation between $S$ and $T$.

Then

$$
\sup \{ \langle \bx, \ba \rangle \ST \bx \in T \}
= \inf \{ \langle \bx, \ba \rangle \ST \bx \in T \} 
= \langle \bp, \ba \rangle.
$$

Hence, $S$ and $\bp$ are properly separated
if and only if there exists a vector $\ba \in \VV$
such that

$$
\inf \{ \langle \bx, \ba \rangle \ST \bx \in S \} 
\geq \langle \bp, \ba \rangle
\text{ and }
\sup \{ \langle \bx, \ba \rangle \ST \bx \in S \} 
>  \langle \bp, \ba \rangle.
$$


We now consider a hyperplane

$$
H  = \{ \bx \in \VV \ST  \langle \bx, \ba \rangle =  \langle \bp, \ba \rangle \}.
$$

And let $H_+$ denote one of its closed half-spaces

$$
H_+  = \{ \bx \in \VV \ST  \langle \bx, \ba \rangle  \geq  \langle \bp, \ba \rangle \}.
$$
We can clearly see that

1. $\ba \in H$.
1. $S \subseteq H_+$. $S$ is contained entirely in the closed half-space $H_+$.
1. $S \not\subseteq H$. $S$ is not contained entirely in $H$.

Thus, if a set and a point are properly separated, then there
exists a hyperplane that passes through the point, 
contains the set in one of its half-spaces but does not
fully contain the set itself.
```


## Separating Hyperplane Theorems

```{prf:theorem} Separating hyperplane theorem I
:label: res-cvx-sep-plan-1


Let $\VV$ be an $n$-dimensional real vector space.
Let $S$ and $T$ be nonempty convex subsets of $\VV$. There exists
a hyperplane $H$ that separates $S$ and $T$ *properly*
if and only if $\relint S \cap \relint T = \EmptySet$.

In other words, two sets are properly separated
if and only if their relative interiors are disjoint.
```

```{prf:proof}

Let $C = S - T$.

1. By {prf:ref}`res-cvx-nonempty-relint`, 
   $\relint S$ and $\relint T$ are nonempty
   since $S$ and $T$ are nonempty convex sets.
1. By {prf:ref}`res-cvx-convex-sum-relint`,
   $\relint C = \relint S - \relint T$
   and it is nonempty.
1. Note that, $\bzero \notin \relint C$ if and only if 
   $\relint S \cap \relint T = \EmptySet$.
   1. If $\bzero \in \relint C$ then there exists
      $\bx \in \relint S \cap \relint T$ such that
      $\bx - \bx = \bzero$.


Now assume that $\relint S \cap \relint T = \EmptySet$.

1. Thus, $\bzero \notin \relint C$.
1. Consider the affine set $M = \{ \bzero \}$.
1. Clearly, $M \cap \relint C = \EmptySet$ and $\relint C$ 
   is relatively open.
1. By {prf:ref}`res-cvx-sep-affine-rel-open-convex`, 
   there exists a hyperplane containing $M$ such that
   $\relint C$ is a subset of one of its associated open halfspaces.
1. Let $H$ be this hyperplane given by 
   $H = \{\bx \ST \langle \bx, \ba \rangle = 0\}$. 
   Since the hyperplane contains $M$, hence it is a subspace. 
1. By {prf:ref}`res-cvx-convex-relint-closure`,
   $ C \subseteq \closure C \subseteq \closure \relint C$.
1. Thus, $C$ is contained in the corresponding closed halfspace.
1. Without loss of generality, assume that $C$ is contained
   in the nonnegative halfspace $H_+$.
1. Thus, $\inf \{ \langle \bx, \ba \rangle  \ST \bx \in C\} \geq 0$.
1. This means that 
    
   $$
   \inf \{ \langle \bx, \ba \rangle  \ST \bx \in C\}
   = \inf \{ \langle \bx, \ba \rangle  \ST \bx \in S\}
     - \sup \{ \langle \bx, \ba \rangle  \ST \bx \in T\} \geq 0.
   $$
1. Thus, 

   $$
   \inf \{ \langle \bx, \ba \rangle  \ST \bx \in S\} \geq
   \sup \{ \langle \bx, \ba \rangle  \ST \bx \in T\}.
   $$
1. Since $\relint C \in H_{++}$, there exists $\bx \in C$,
   such that $\langle \bx, \ba \rangle > 0$.
1. Thus, $\sup \{ \langle \bx, \ba \rangle  \ST \bx \in C\} > 0$.
1. But then,

   $$
   \sup \{ \langle \bx, \ba \rangle  \ST \bx \in C\} 
   = \sup \{ \langle \bx, \ba \rangle  \ST \bx \in S\}
   - \inf \{ \langle \bx, \ba \rangle  \ST \bx \in T\} > 0. 
   $$
1. Thus, 

   $$
   \sup \{ \langle \bx, \ba \rangle  \ST \bx \in S\} > 
   \inf \{ \langle \bx, \ba \rangle  \ST \bx \in T\}.
   $$
1. Then, by {prf:ref}`res-cvx-proper-sep-charac`, 
   $S$ and $T$ are properly separated.


Now, for the converse, assume that $S$ and $T$ are
properly separated. Thus,
there exists a vector $\ba \in \VV$
such that

$$
\inf \{ \langle \bx, \ba \rangle \ST \bx \in S \} 
\geq \sup \{ \langle \bx, \ba \rangle \ST \bx \in T \}
$$
and

$$
\sup \{ \langle \bx, \ba \rangle \ST \bx \in S \} 
>  \inf \{ \langle \bx, \ba \rangle \ST \bx \in T \}.
$$

1. From the first inequality, we get that 
   $\inf \{ \langle \bx, \ba \rangle  \ST \bx \in C\} \geq 0$.
1. From the second inequality, we get that
   $\sup \{ \langle \bx, \ba \rangle  \ST \bx \in C\} > 0$.
1. Thus, there exists a hyperplane $H$ given by
   $H = \{\bx \ST \langle \bx, \ba \rangle = 0\}$
   such that the corresponding nonnegative closed halfspace
   $H_+ =  \{\bx \ST \langle \bx, \ba \rangle \geq 0\}$
   contains $C$.
1. Note that 
   
   $$
   \interior H_+ = \relint H_+ = 
   H_{++} = \{\bx \ST \langle \bx, \ba \rangle > 0\}.
   $$
1. Since $\sup \{ \langle \bx, \ba \rangle  \ST \bx \in C\} > 0$,
   hence $H_{++} \cap C \neq \EmptySet$.
1. $C \subseteq \closure H_{++} = H_+$ 
   but $C \not\subseteq \closure H_{++} \setminus \relint H_{++}
   = H_+ \setminus H_{++} = H$.
1. Thus, by {prf:ref}`res-cvx-nonbd-cl-subset-interior`,
   $\relint C \subseteq \relint H_{++} = H_{++}$.
1. Thus, $\bzero \notin \relint C$.
1. Thus, $\relint S \cap \relint T = \EmptySet$.

We are done.
```



```{prf:corollary} Separating hyperplane theorem II
:label: res-cvx-separating-hyperplane

Let $\VV$ be an $n$-dimensional real vector space.
Let $S$ and $T$ be nonempty disjoint convex subsets of $\VV$;
i.e., $S \cap T = \EmptySet$.

Then, there exists a hyperplane that properly separates them.
```

```{prf:proof}
Since $S \cap T = \EmptySet$, hence $\relint S \cap \relint T = \EmptySet$.
Then, applying {prf:ref}`res-cvx-sep-plan-1`, there exists
a hyperplane that properly separates $S$ and $T$.
```

This result is stronger than proposition
2.4.2 in {cite}`bertsekas2003convex`.

Disjointness of convex sets is not enough for
strong separation as their closures might meet.


```{prf:theorem} Separating hyperplane theorem III
:label: res-cvx-proper-sep-set-point


Let $\VV$ be an $n$-dimensional real vector space.
Let $S$ be a nonempty convex subset of $\VV$.
Let $\ba \in \VV$ be a vector.
There exists
a hyperplane $H$ that separates $S$ and $\ba$ *properly*
if and only if $\ba \notin \relint S$.

In other words, a point can be properly separated
from a convex set if and only if it doesn't belong
to its relative interior.
```

```{prf:proof}
.

1. We form a set $T = \{ \ba \}$.
1. Then $\relint T = \{ \ba \}$ ({prf:ref}`res-cvx-relint-singleton`).
1. By {prf:ref}`res-cvx-sep-plan-1`, $S$ and $T$ are properly
   separated if and only if

   $$
   \relint S \cap \relint T = \EmptySet.
   $$
1. In other words,

   $$
   \relint S \cap \{ \ba \} = \EmptySet.
   $$
1. In other words, $\ba \notin \relint S$.
```



## Strong Separation Characterization

```{prf:theorem} Characterization of strong separation
:label: res-cvx-strong-sep-charac

Let $\VV$ be an $n$-dimensional real vector space.
Let $S$ and $T$ be nonempty convex subsets of $\VV$. There exists
a hyperplane $H$ that separates $S$ and $T$ *strongly*
if and only if 

$$
\inf \{ \| \bx - \by \| \ST \bx \in S, \by \in T \} > 0.
$$
In other words, $H$ strongly separates $S$ and $T$
if and only if $\bzero \notin \closure (S - T)$.
```

```{prf:proof}
Let $C = S-T$.
Then 

$$
\inf \{ \| \bx - \by \| \ST \bx \in S, \by \in T \}
= \inf \{ \| \bv \| \ST \bv \in C \}.
$$
By {prf:ref}`res-la-set-zero-infimum`, 
$\inf \{ \| \bv \| \ST \bv \in C \} = 0$
if and only if $\bzero \in \closure C$.

Thus, $\inf \{ \| \bv \| \ST \bv \in C \} > 0$
if and only if $\bzero \notin \closure C$.


Assume that $S$ and $T$ are strongly separated.
Let $H$ be the hyperplane that separates $S$ and $T$.
Let $H_{++}$ be the positive open halfspace.
Let $H_{--}$ be the negative open halfspace.

1. Then, there exists an $r > 0$ such that 
   $S + r B \subseteq H_{++}$ 
   and $T + rB \subseteq H_{--}$.
1. Since $H_{++} \cap H_{--} = \EmptySet$, 
   hence $(S + r B) \cap (T + r B) = \EmptySet$.
1. Then, for any $\bx \in S$ and $\by \in T$ and  every $\bu, \bv \in B$,
   
   $$
   \| \bx + r \bu - (\by + r\bv ) \| > 0
   $$
   as $\bx + r \bu = \by + r \bv$ would mean that
   $(S + r B) \cap (T + r B) \neq \EmptySet$
1. Note that,
   $\| \bx + r \bu - (\by + r\bv ) \| = \| (\bx - \by) - r (\bv - \bu) \|$.
1. Then, $\| \bx - \by \| \geq 2 r$ must be true for every $\bx \in S$ and $\by \in T$.
   1. For contradiction, assume that $\| \bx - \by \| < 2 r$
      for some $\bx \in S$ and $\by \in T$.
   1. Let $\bu = \frac{1}{2r} (\by - \bx)$.
   1. Let $\bv = \frac{1}{2r} (\bx - \by)$.
   1. Note that $\| \bu \| < 1$ and $\| \bv \| < 1$.
   1. Thus, $\bu, \bv \in B$.
   1. Then, $r (\bv - \bu) = \bx - \by$.
   1. Then, $\| (\bx - \by) - r (\bv - \bu) \| = \| \bzero \| = 0$.
   1. This contradicts the condition that 
      $\| \bx + r \bu - (\by + r\bv ) \| > 0$
      for every $\bx \in S$, $\by \in T$ and $\bu, \bv \in B$.
1. Thus, $\inf \{ \| \bx - \by \| \ST \bx \in S, \by \in T \} > 0$.

Conversely, assume that
$\inf \{ \| \bx - \by \| \ST \bx \in S, \by \in T \} > 0$.

1. Let $\inf \{ \| \bx - \by \| \ST \bx \in S, \by \in T \} = 2 r$ where $r > 0$.
1. Then, $\| \bx - \by \| \geq 2 r \Forall \bx \in S, \by \in T$.
1. Then, $(S + rB) \cap (T + rB) = \EmptySet$. 

   1. For contradiction, assume that $(S + rB) \cap (T + rB) \neq \EmptySet$.
   1. Let $\ba \in (S + rB) \cap (T + rB)$.
   1. Then, there exists $\bx \in S$ and $\bu \in B$ such that $\ba = \bx + r \bu$.
   1. And, there exists $\by \in T$ and $\bv \in B$ such that $\ba = \by + r \bv$.
   1. Then, $\bx + r \bu = \by + r \bv$.
   1. Thus, $\bx - \by = r (\bv - \bu)$.
   1. Thus, 

      $$
      \| \bx - \by \| = r \| \bv - \bu \|
      \leq r (\| \bv \| + \| \bu \|) < r (1 + 1) = 2 r.
      $$
   1. This contradictions our hypothesis that 
      $\| \bx - \by \| \geq 2 r \Forall \bx \in S, \by \in T$.
1. Note that $S +rB$ and $T + rB$ are convex and disjoint.
1. Then, due to {prf:ref}`res-cvx-separating-hyperplane`, 
   there exists a hyperplane $H$ which separates $S + rB$ and $T + rB$ 
   properly.
1. We can choose $H$ so that $S + rB \subseteq H_+$ and 
   $T + rB \subseteq H_-$.
1. But then, $S + \frac{r}{2} B \in H_{++}$ and 
   $T + \frac{r}{2} B \in H_{--}$ lie in
   the opposite open halfspaces.
1. Thus, $S$ and $T$ are strongly separated.
```


## Strong Separation Conditions

We describe several conditions which are sufficient to
achieve strong separation between two sets.
See also strict separation theorem (proposition 2.4.3) of {cite}`bertsekas2003convex`.


```{prf:theorem} Strong separation: closed subtraction
:label: res-cvx-strong-sep-1

Let $\VV$ be an $n$-dimensional real vector space.
Let $S$ and $T$ be two disjoint nonempty convex subsets of $\VV$.
There exists a hyperplane $H$ that separates $S$ and $T$ *strongly*
if $S - T$ is closed.
```

```{prf:proof}
We proceed as follows.

1. Since $S$ and $T$ are disjoint hence $\bzero \notin S-T$.
1. Since $S-T$ is closed, hence $\bzero \notin \closure (S - T) = S - T$.
1. By {prf:ref}`res-cvx-strong-sep-charac`, $S$ and $T$ are
   strongly separated.
```

```{prf:theorem} Strong separation: closed and compact sets
:label: res-cvx-strong-sep-2

Let $\VV$ be an $n$-dimensional real vector space.
Let $S$ and $T$ be two disjoint nonempty convex subsets of $\VV$.
There exists a hyperplane $H$ that separates $S$ and $T$ *strongly*
if $S$ is closed and $T$ is compact.
```

```{prf:proof}
We proceed as follows.

1. Since $S$ and $T$ are disjoint hence $\bzero \notin S-T$.
1. Since $S-T$ is closed, hence $\bzero \notin \closure (S - T) = S - T$.
1. By {prf:ref}`res-cvx-strong-sep-charac`, $S$ and $T$ are
   strongly separated.
```


### Recession Cones

The conditions below are based on the theory
of recession cones and lineality spaces of convex sets.
See {ref}`sec:cvx:recession` for a background.


```{prf:theorem} Strong separation: recession cones
:label: res-cvx-strong-sep-rec-cone

Let $\VV$ be an $n$-dimensional real vector space.
Let $S$ and $T$ be two disjoint nonempty closed and convex subsets of $\VV$.
There exists a hyperplane $H$ that separates $S$ and $T$ *strongly*
if

$$
R_S \cap R_T  = L_S \cap L_T
$$
where $R_X$ denotes the recession cone
and $L_X$ denotes the lineality space of a set $X$.
```

```{prf:proof}
Due to {prf:ref}`res-cvx-set-sub-closed-recession-lineality`,
$S - T$ is closed.
Then due to {prf:ref}`res-cvx-strong-sep-1`, $S$ and $T$
are strongly separated.
```

### Strongly Separating Hyperplane

Recall that the (orthogonal) projection of a vector $\bv$ on a convex set $C$
is the vector $\bx \in C$ which is nearest to $\bv$ under the
(Euclidean) norm. In particular, if $\bv \in C$ then $\bv$
is its own projection on $C$. The projection of the
vector $\bzero$ on a convex set $C$ is this the vector
of $C$ with the minimum norm.
See {ref}`sec:opt:pocs` for details.

```{prf:theorem} Strongly separating hyperplane
:label: res-cvx-strong-sep-hyperplane

Let $\VV$ be an $n$-dimensional real vector space.
Let $S$ and $T$ be two disjoint nonempty and convex subsets of $\VV$.
Assume that $S - T$ is closed.

Consider the vector of minimum norm (projection of the origin)
in $S - T$ given by $\bv = \bs - \bt$ where $\bs \in S$ and $\bt \in T$.

1. Let $\ba = \frac{1}{2} \bv = \frac{1}{2} (\bs - \bt)$.
1. Let $\bb = \frac{1}{2} (\bs + \bt)$.
1. Let $c = \langle \bb, \ba \rangle$.

Then the hyperplane $H$ given by

$$
H = \{ \bx \in \VV \ST \langle \bx, \ba \rangle = c \}
$$
strongly separates $S$ and $T$.
In other words,

$$
\langle \bx_1, \ba \rangle > c >  
\langle \bx_2, \ba \rangle \quad \Forall \bx_1 \in S, \bx_2 \in T.
$$
```

```{prf:proof}
.

1. Since $S$ and $T$ are disjoint hence $\bs - \bt \neq \bzero$.
1. Hence $\ba \neq \bzero$.
1. $\bs$ is the nearest point in $\closure S$ from $\closure T$.
1. $\bt$ is the nearest point in $\closure T$ from $\closure S$.
1. The line segment $[\bs, \bt]$ connects these nearest points.
1. $\bb$ lies on this line segment.
1. Accordingly, $\bs$ is projection of $\bb$ in $\closure S$.
1. Similarly $\bt$ is projection of $\bb$ in $\closure T$.
1. Then, due to {prf:ref}`res-cvx-projection-characterization`
   (orthogonal projection characterization),
   for every $\bx \in S$
    
   $$
   \langle \bx - \bs, \bb - \bs \rangle \leq 0.
   $$
1. But
   
   $$
   \bb - \bs 
   = \frac{1}{2} (\bs + \bt) - \bs 
   = \frac{1}{2} (\bt - \bs) = -\ba.
   $$
1. Hence $\langle \bx - \bs, \ba \rangle \geq 0$.
1. Hence $\langle \bx, \ba \rangle \geq \langle \bs, \ba \rangle$.
1. Further

   $$
   \langle \bs, \ba \rangle
   &= \langle \bs - \bb + \bb, \ba \rangle \\
   &= \langle \ba + \bb, \ba \rangle \\
   &= \| \ba \|_2^2 + \langle \bb, \ba \rangle \\
   &= \| \ba \|_2^2 + c
   > c.
   $$
   since $\ba \neq \bzero$.
1. Hence for every $\bx \in S$, we have
   $\langle \bx, \ba \rangle > c$.
1. A similar argument shows that for every $\bx \in T$, we have
   $\langle \bx, \ba \rangle < c$.
```






## Closed Convex Sets

```{prf:theorem} Strict separation theorem
:label: res-cvxf-cl-convex-set-strict-separation

Let $\VV$ be a real $n$-dimensional vector space.
Let $C \subseteq \VV$ be a nonempty closed convex set.
Let $\by \notin C$. Then, there exists $\bp \in \VV^*$ 
and $\alpha \in \RR$ such that 

$$
\langle \by , \bp \rangle > \alpha
\text{ and }
\langle \bx, \bp \rangle \leq \alpha \Forall \bx \in C.
$$
In other words, there exists a separating hyperplane
such that $C$ is contained in one of its (closed) halfspaces
and $\by$ is not in that halfspace (i.e., it is in the opposite open halfspace). 

By choosing any $\beta \in (\alpha, \langle \by , \bp \rangle)$,
we also have


$$
\langle \by , \bp \rangle > \beta
\text{ and }
\langle \bx, \bp \rangle < \beta \Forall \bx \in C.
$$
```

```{prf:proof}
This is an application of strong separation.

1. Define a set $D = \{ \by \}$.
1. Since $C$ is closed and $\by \notin C$, hence
   $\by$ is not a closure point of $C$.
1. Thus, there exists $r > 0$ such that 
   $B(\by, r) \cap C = \EmptySet$.
1. Thus, $d(C, D) \geq r$.
1. Then, by {prf:ref}`res-cvx-strong-sep-charac`, 
   $C$ and $D$ are strongly separated.
1. Let $H$ be a hyperplane which strongly separates them.
1. Then one of the closed halfspaces of $H$ contains $C$ 
   but not $\by$.
1. Let $H$ be described by 

   $$
   H = \{ \bx \in \VV \ST \langle \bx, \bp \rangle = \alpha \}.
   $$
1. We can negate $\bp, \alpha$ if necessary so that

   $$
   C \subseteq H_- = \{ \bx \in \VV \ST \langle \bx, \bp \rangle \leq \alpha \}.
   $$
1. Accordingly, $\langle \by, \bp \rangle > \alpha$.
```


```{prf:theorem} Closed Convex = Intersection of Halfspaces
:label: res-cvx-closed-convex-halfspace-intersection

Let $\VV$ be a real $n$-dimensional vector space.
A closed convex set $C$ of $\VV$ is the intersection of
all the closed halfspaces that contain it.
```

```{prf:proof}

The set $\VV$ is closed and convex but no halfspace contains
it. So the statement is vacuously true.

The empty set is closed and convex and every halfspace
contains it. The intersection of all halfspaces  
is the empty set. Thus, the statement is vacuously true.

Let us assume that $C$ is nonempty and not equal to $\VV$.

1. Let $\ba \in \VV$ such that $\ba \notin C$.
1. Since $C$ is closed, hence $\ba$ is not a closure point of $C$.
1. Thus, there exists $r > 0$ such that $B(\ba, r) \cap C = \EmptySet$.
1. Thus, $\| \ba - \bx \| > 0 \Forall \bx \in C$.
   Specifically, $\inf \{ \| \ba - \bx \|  \ST \bx \in C \} \geq r$.
1. Thus, by {prf:ref}`res-cvx-strong-sep-charac`, $\{ \ba \}$
   and $C$ are strongly separated by some hyperplane $H$. 
1. Thus, one of the corresponding closed halfspaces contains $C$ but not $\ba$.
1. In other words, for every $\ba \notin C$, there exists a 
   closed halfspace that doesn't contain $\ba$ but contains $C$.
1. Thus, the intersection of all halfspaces containing $C$ cannot 
   contain any element from $\VV \setminus C$.
   1. If the intersection contained an element $\ba \notin C$, 
      then there would be a closed halfspace containing $C$ but not $\ba$
      which would mean that the intersection of all halfspaces
      containing $C$ cannot contain $\ba$.
1. Hence, the intersection of all closed halfspaces containing $C$
   is exactly equal to $C$.
```

We now have two different characterizations of closed convex sets.

1. From {prf:ref}`res-cvx-closed-closure-line-segments`,
   a closed and convex set is the closure of the union of
   all the line segments connecting the points of the set.
1. From {prf:ref}`res-cvx-closed-convex-halfspace-intersection`,
   a closed and convex set is the intersection of all the
   closed half-spaces containing it.

## Supporting Hyperplanes


```{prf:definition} Supporting hyperplane and halfspaces
:label: def-cvx-supporting-hyperplane

Let $\VV$ be a real $n$-dimensional vector space.
Let $S \subseteq \VV$. Let $\bx_0 \in \boundary S$ be a point
on its boundary.

If there exists a nonzero vector $\ba \in \VV$ such that
$\langle \bx, \ba \rangle \leq \langle \bx_0, \ba \rangle$
for every $\bx \in S$,
then the hyperplane $H$ given by

$$
H = \{ \bx \ST \langle \bx, \ba \rangle = \langle \bx_0, \ba \rangle \}
$$
is called a *supporting hyperplane* of $S$ at $\bx_0$.

$H$ separates $\{ \bx_0 \}$ and $S$ and $H$ contains $\bx_0$.
The halfspace
$ \{ \bx \ST \langle (\bx - \bx_0), \ba \rangle \leq 0 \}$
corresponding to $H$ is called a *supporting halfspace*
of $S$ at $\bx_0$.
```

Convex sets have this beautiful property that there exists
a supporting hyperplane at every point in the boundary of the
set.

```{prf:theorem} Supporting hyperplane theorem
:label: res-cvx-supporting-hyperplane-theorem

Let $\VV$ be a real $n$-dimensional vector space.
Let $C$ be a nonempty convex subset of $\VV$. 
Let $\bx \in \boundary C$ be any point in the boundary of $C$.
Then, there exists a supporting hyperplane to $C$ at $\bx$.
```


```{prf:proof}

Consider the case where $\interior C = \EmptySet$.

1. Then, due to {prf:ref}`res-cvx-convex-set-empty-interior`,
   $\dim \affine C < n$.
1. Thus, there exists a hyperplane $H$ such that $\affine C \subseteq H$.
1. Since $\VV$ is finite dimensional, hence $H$ is closed
   ({prf:ref}`res-la-affine-closed`).
1. Thus, $\closure C \subseteq H$.
1. Thus, $\bx \in H$. 
1. This $H$ trivially separates $\{ \bx \}$ and $C$ as both are 
   contained in $H$.

Now, assume that $\interior C \neq \EmptySet$.

1. $\dim \affine C = n$.
1. $\relint C = \interior C$.
1. Since $\bx \in \boundary C$, hence the sets
   $\{ \bx \}$ and $\interior C$ are disjoint.
1. $\relint \{ \bx \} = \{ \bx \}$ ({prf:ref}`res-cvx-relint-singleton`).
1. We have $\relint \{ \bx \} \cap \relint C = \EmptySet$.
1. By {prf:ref}`res-cvx-sep-plan-1`, there exists
   a hyperplane $H$ that separates $\{\bx \}$ and $C$ properly.
1. Consequently $C$ lies entirely in one of the closed halfspaces
   of $H$.
```

```{prf:corollary}
:label: res-cvx-closed-convex-intersect-supporting

Let $\VV$ be a real $n$-dimensional vector space.
A closed convex set $C$ of $\VV$ is the intersection of
all the supporting halfspaces that contain it.
```


## Farkas' Lemma

```{prf:theorem} Farkas' lemma
:label: res-cvx-farkas-lemma

Let $\bA \in \RR^{m \times n}$ and $\bb \in \RR^m$. 
Then, exactly one of the following two statements is true.

1. There exists $\bx \in \RR^n$ such that
   $\bA \bx = \bb, \bx \succeq \bzero$.
1. There exists $\by \in \RR^m$ such that
   $\bA^T \by \succeq \bzero, \by^T \bb < 0$.
```

(1) and (2) are called *strong alternatives* 
as exactly one of them must be true.
In contrast *weak alternatives* are
statements in which at most one of them can be true.

```{prf:proof}

We first show that both (1) and (2) cannot be true
simultaneously.

1. Assume that both (1) and (2) are true.
1. Note that 
   
   $$
   \by^T \bA \bx = \by^T (\bA \bx) = \by^T \bb < 0
   $$
   since $\bA \bx = \bb$ by (1) and $\by^T \bb < 0$ by (2).
1. At the same time

   $$
   \by^T \bA \bx = (\by^T \bA) \bx
   = (\bA^T \by)^T \bx \geq 0
   $$
   since by (2) $\bA^T \by \succeq \bzero$
   and by (1) $\bx \succeq \bzero$.
1. Thus, we have a contradiction.
1. Hence (1) and (2) cannot be true simultaneously.

We now show that if (1) doesn't hold then (2) must be true.
In other words, not (1) $\implies$ (2).

1. Let $\ba_1, \dots, \ba_n$ be the columns of $\bA$.
1. Note that the columns of $\bA \in \RR^m$.
1. Then, (1) can be interpreted as saying that
   $\bb$ is a conic combination of columns of $\bA$.
1. Let $Q$ denote the cone generated by the columns of $\bA$

   $$
   Q = \cone \{\ba_1, \dots, \ba_n \}.
   $$
1. $Q$ is nonempty, closed and convex cone.
   The closedness of $Q$ is due to {prf:ref}`res-cvx-closed-conic-hull`
   since $Q$ is a conic hull of a finite set of points.
1. Since (1) doesn't hold true, hence $\bb \notin Q$.
1. By the strict separation theorem 
   {prf:ref}`res-cvxf-cl-convex-set-strict-separation`,
   the set $Q$ and the point $\bb$ can be strictly separated
   by a hyperplane.
1. Specifically, there exists $\bp \in \RR^m$ and $\beta \in \RR$ such that 

   $$
   \bp^T \bb > \beta
   \text{ and }
   \bp^T \bx \leq \beta \Forall \bx \in Q.
   $$
1. Since $\bzero \in Q$, hence $\beta \geq 0$.
1. Pick any $i \in \{1,\dots, n\}$.
1. Then, $t \ba_i \in Q$ for all $t > 0$ since $Q$ is a cone containing $\ba_i$.
1. Thus, $\bp^T t \ba_i \leq \beta$ for all $t > 0$.
1. Thus, $\bp^T \ba_i \leq \frac{\beta}{t}$ for all $t > 0$.
1. Since $\beta \geq 0$, hence taking the limit $t \to \infty$, we get
   $\bp^T \ba_i \leq 0$.
1. This holds true for every $i=1,\dots,n$. 
1. Choose $\by = -\bp$.
1. Then, $\by^T \bb = - (\bp^T \bb) < -\beta \leq 0$.
1. Thus, $\by^T \bb < 0$.
1. Also, $\by^T \ba_i \geq 0$ for all $i=1,\dots,n$.
1. Thus, $\by^T \bA \succeq \bzero$ and $\by^T \bb < 0$ as desired in (2).

Showing that if (2) doesn't hold true,
then (1) must be true is straightforward.

1. Assume that (2) is false.
1. For contradiction, assume that (1) is false.
1. Then (2) must be true by the previous argument.
1. We have a contradiction.
1. Hence, (1) must be true.
```


```{prf:theorem} Farkas' lemma version 2
:label: res-cvx-farkas-lemma-v2

Let $\bA \in \RR^{m \times n}$ and $\bb \in \RR^m$. 
Then, exactly one of the following two statements is true.


1. There exists $\bx \in \RR^n$ such that $\bA \bx \preceq \bb$.
1. There exists $\by \in \RR^n$ such that $\bA^T \by = \bzero, \by^T \bb < 0, \by \succeq \bzero$.

(2) is also equivalent to the following statement:

3 There exists $\by \in \RR^m$ such that $\bA^T \by = \bzero, \by^T \bb = -1, \by \succeq \bzero$.
```

```{prf:proof}

We first show that (2) and (3) are equivalent.

1. Clearly (3) $\implies$ (2).
1. Assume (2) is true.
1. Let $\by^T \bb = s$. Let $r = \frac{-1}{s}$. Then, $r > 0$.
1. Let $\tilde{\by} = \frac{\by}{r}$.
1. Then, $\tilde{\by} \succeq \bzero$ since $\by \succeq \bzero$ and $r > 0$.
1. Also $\tilde{\by}^ \bb = r \by^T \bb = \frac{-1}{s} s = -1$.
1. Finally $\bA^T \tilde{\by} = r \bA^T \by = \bzero$.
1. Thus, $\tilde{\by}$ satisfies (3).


Next, we show that (1) and (2) cannot be both true simultaneously.

1. For contradiction, assume that both (1) and (2) are true.
1. Then 

   $$
   \by^T \bA \bx = \by^T (\bA \bx) \leq \by^T \bb < 0
   $$
   since $\bA \bx \preceq \bb$ from (1), $\by \succeq \bzero$ from (2)
   and $\by^T \bb < 0$ from (2).
1. Also

   $$
   \by^T \bA \bx  = (\by^T \bA) \bx = (\bA^T \by)^T \bx = \bzero^T \bx = 0 
   $$
   since  $\bA^T \by= \bzero$ from (2).
1. We have a contradiction.
1. Thus, both (1) and (2) cannot be true simultaneously.


We next prove that if (2) is false then (1) must be true.

1. Since (2) and (3) are equivalent hence (3) is false too.
1. Combine the system of equations $\bA^T \by  = \bzero$ and $\by^T \bb = -1$ as
   $\tilde{\bA} \by  = \tilde{\bb}$ where

   $$
   \tilde{\bA} = \begin{bmatrix}
   \bA^T \\
   \bb^T
   \end{bmatrix}
   \text{ and }
   \tilde{\bb} = \begin{bmatrix}
   0\\
   \vdots\\
   0\\
   -1
   \end{bmatrix}.
   $$
1. Since (3) if false, hence there doesn't exist $\by \in \RR^m$ such that
   $\tilde{\bA} \by  = \tilde{\bb}$.
1. This is identical to statement (1) of the original Farkas' lemma
   in {prf:ref}`res-cvx-farkas-lemma`.
1. Hence statement (2) of {prf:ref}`res-cvx-farkas-lemma` must hold true.
1. Thus, there exists $\bv \in \RR^{n + 1}$ such that
   $\tilde{\bA}^T \bv \succeq \bzero$ and $\tilde{\bb}^T \bv < 0$. 
1. Set 

   $$
   \bv = \begin{bmatrix} \bx  \\ t \end{bmatrix}
   $$
   where $\bx \in \RR^n$ and $t \in \RR$.
1. Then $\tilde{\bb}^T \bv < 0$ implies that $t > 0$.
1. $\tilde{\bA}^T \bv \succeq \bzero$ simplifies to

   $$
   \bA \bx + t \bb \succeq \bzero.
   $$
1. This further simplifies to

   $$
   & \bA \bx + t \bb \succeq \bzero\\
   \iff & \bA \bx \succeq -t \bb \\
   \iff & \bA \left ( \frac{-1}{t} \bx \right ) \preceq \bb.
   $$
   The inequality sign changes since $t > 0$.
1. Clearly, $\frac{-1}{t} \bx$ satisfies (1) as desired.
   Thus, (1) is indeed true.
```

```{prf:theorem} Farkas' lemma version 3
:label: res-cvx-farkas-lemma-v3

Let $\bA \in \RR^{m \times n}$ and $\bc \in \RR^n$.

Then the following statements are equivalent.

1. The implication $\bA \bx \preceq \bzero \implies \bc^T \bx \leq 0$ holds true.
1. There exists $\by \succeq \bzero$ such that $\bA^T \by = \bc$.  

```

```{prf:proof}
(2) $\implies$ (1)

1. (2) is same as statement (1) of {prf:ref}`res-cvx-farkas-lemma`.
1. Thus, by {prf:ref}`res-cvx-farkas-lemma`,
   there is no $\bx \in \RR^n$ such that
   $\bA \bx \succeq \bzero$ and $\bx^T \bc < 0$.
1. Hence for every $\bx \in \RR^n$,  
   $\bA \bx \succeq \bzero \implies \bx^T \bc \geq 0$.
1. Replacing $\bx$ by $-\bx$, we see that
   for every $\bx \in \RR^n$,  
   $\bA \bx \preceq \bzero \implies \bx^T \bc \leq 0$.

(1) $\implies$ (2)

1. For every $\bx$, $\bA \bx \preceq \bzero \implies \bc^T \bx \leq 0$.
1. Thus, For every $\bx$, $\bA \bx \succeq \bzero \implies \bc^T \bx \geq 0$.
1. Thus, there doesn't exist any $\bx$ with $\bA \bx \succeq \bzero$
   and $\bc^T \bx < 0$.
1. Thus, by {prf:ref}`res-cvx-farkas-lemma`, 
   there exists $\by \succeq \bzero$ such that $\bA^T \by = \bc$. 
```

