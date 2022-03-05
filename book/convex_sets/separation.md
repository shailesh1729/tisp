# Separation Theorems

Separation theorems provide us ways to find a separating hyperplane
between two disjoint convex sets. Hyperplanes
require the notion of an inner product. 
This subsection focuses on vector spaces
which are real, finite dimensional and equipped
with a real inner product $\langle \cdot, \cdot \rangle \to \RR$.


## Types of Separating Hyperplanes

```{prf:definition} Separating hyperplane
:label: def-cvx-separating-hyperplane

Let $\VV$ be a real $n$-dimensional inner product space.
For any two convex subsets $C$ and $D$ of $\VV$, a hyperplane
$H$ is said to *separate* $C$ and $D$ if
$C$ is contained in one of the closed halfspaces
corresponding to $H$ and $D$ is contained in the other 
closed halfspace.
```
This definition allows for some degenerate possibilities where
both $C \subseteq H$ and $D \subseteq H$ since the closed
halfspaces contain $H$ (as their boundary).

```{prf:definition} Proper separation
:label: def-cvx-proper-separation

Let $\VV$ be a real $n$-dimensional inner product space.
For any two convex subsets $C$ and $D$ of $\VV$, a hyperplane
$H$ is said to *properly separate* $C$ and $D$ if
$H$ separates them and both are not entirely contained
in $H$; i.e., either $C \not\subseteq H$ or $D \not\subseteq H$
or both.
```
Proper separation still allows for the possibility that
parts of $C$ or $D$ lies inside $H$. But it ensures that
$C \triangle D \neq \EmptySet$.
$C \cap D \subseteq H$ is the common part.

```{prf:definition} Strong separation
:label: def-cvx-strong-separation

Let $\VV$ be a real $n$-dimensional inner product space.
For any two convex subsets $C$ and $D$ of $\VV$, a hyperplane
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

Let $\VV$ be a real $n$-dimensional inner product space.
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

Let $\VV$ be an $n$-dimensional real inner product space.
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

## Separating Hyperplane Theorems

```{prf:theorem} Separating hyperplane theorem I
:label: res-cvx-sep-plan-1


Let $\VV$ be an $n$-dimensional real inner product space.
Let $S$ and $T$ be nonempty convex subsets of $\VV$. There exists
a hyperplane $H$ that separates $S$ and $T$ *properly*
if and only if $\relint S \cap \relint T = \EmptySet$.
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

Let $\VV$ be an $n$-dimensional real inner product space.
Let $S$ and $T$ be nonempty disjoint convex subsets of $\VV$;
i.e., $S \cap T = \EmptySet$.

Then, there exists a hyperplane that properly separates them.
```

```{prf:proof}
Since $S \cap T = \EmptySet$, hence $\relint S \cap \relint T = \EmptySet$.
Then, applying {prf:ref}`res-cvx-sep-plan-1`, there exists
a hyperplane that properly separates $S$ and $T$.
```

Disjointness of convex sets is not enough for
strong separation as their closures might meet.



## Strong Separation Characterization

```{prf:theorem} Characterization of strong separation
:label: res-cvx-strong-sep-charac

Let $\VV$ be an $n$-dimensional real inner product space.
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



## Closed Convex Sets

```{prf:theorem} Closed Convex = Intersection of Halfspaces
:label: res-cvx-closed-convex-halfspace-intersection

Let $\VV$ be a real $n$-dimensional inner product space.
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

## Supporting Hyperplanes


```{prf:definition} Supporting hyperplane and halfspaces
:label: def-cvx-supporting-hyperplane

Let $\VV$ be a real $n$-dimensional inner product space.
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

Let $\VV$ be a real $n$-dimensional inner product space.
Let $C$ be a nonempty convex subset of $\VV$. 
Let $\bx \in \boundary C$ be any point in the boundary of $C$.
Then, there exists a supporting hyperplane to $C$ at $\bx$.
```


```{prf:proof}

Consider the case where $\interior C = \EmptySet$.

1. Then, due to {prf:ref}`res-cvx-convex-set-empty-interior`,
   $\dim \affine C < n$.
1. Thus, there exists a hyperplane $H$ such that $\affine C \subseteq H$.
1. This $H$ trivially separates $\{ \bx \}$ and $C$ as both are 
   contained in $H$.

Now, assume that $\interior C \neq \EmptySet$.

1. $\dim \affine C = n$.
1. $\relint C = \interior C$.
1. Since $\bx \in \boundary C$, hence the sets
   $\{ \bx \}$ and $\interior C$ are disjoint.
1. $\relint \{ \bx \} = \{ \bx \}$.
1. We have $\relint \{ \bx \} \cap \relint C = \EmptySet$.
1. By {prf:ref}`res-cvx-sep-plan-1`, there exists
   a hyperplane $H$ that separates $\{\bx \}$ and $C$ properly.
1. Consequently $H$ lies entirely in one of the closed halfspaces
   of $H$.
```

```{prf:corollary}
:label: res-cvx-closed-convex-intersect-supporting

Let $\VV$ be a real $n$-dimensional inner product space.
A closed convex set $C$ of $\VV$ is the intersection of
all the supporting halfspaces that contain it.
```
