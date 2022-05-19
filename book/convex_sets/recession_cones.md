# Recession Cones

Main references for this section are {cite}`bertsekas2003convex`.


```{prf:definition} Direction of recession
:label: def-cvx-recession-direction

Given a nonempty convex set $C$, we say that a vector $\by$ is
in the *direction of recession* of $C$ if $\bx + \alpha \by \in C$
for all $\bx \in C$ and $\alpha \geq 0$.

In words, starting from any point $\bx \in C$ and going
indefinitely along the direction $\by$, we always stay inside $C$.
We never cross the relative boundary of $C$ to a point outside $C$.
```

## Recession Cone


```{prf:theorem} Recession cone
:label: res-cvx-recession-dir-set-cone

Let $C$ be a nonempty convex set.
The set of all directions of recession for $C$ is a convex cone.
```

```{prf:proof}
Let $R$ be the set of recession directions of $C$.

1. Note that $\bx + \alpha \bzero = \bx \in C$ for every $\bx \in C$ and every $\alpha \geq 0$.
1. Hence $\bzero \in R$.
1. Now assume $\bu \in R$.
1. Let $\bx \in C$.
1. Let $t > 0$.
1. Let $\bv = t \bu$.
1. Let $\alpha \geq 0$.
1. Then $\bx + \alpha \bv = \bx + (\alpha t) \bu \in C$
   since $\alpha t \geq 0$ and $\bu$ is a recession direction.
1. Hence $\bv$ is also a recession direction.
1. Thus $R$ is a cone.

We now show that $R$ is in fact a convex cone.

1. Let $t_1, t_2 \geq 0$ such that $t_1 + t_2 = 1$ and let $\bu, \bv \in R$.
1. Let $\bw = t_1 \bu + t_2 \bv$ be a convex combination of $\bu$ and $\bv$.
1. Let $\bx \in C$ and $\alpha \geq 0$.
1. Then

   $$
   \bx + \alpha \bw &= (t_1 + t_2) \bx + \alpha (t_1 \bu + t_2 \bv) \\
   &= t_1(\bx + \alpha \bu) + t_2(\bx + \alpha \bv).
   $$
1. Since $\bu, \bv \in R$, hence $\by = \bx + \alpha \bu, \bz = \bx + \alpha \bv \in C$.
1. But then $t_1 \by + t_2 \bz$ is a convex combination of $\by, \bz$.
1. Hence $t_1 \by + t_2 \bz \in C$.
1. Hence $\bx + \alpha \bw \in C$ for every $\alpha \geq 0$ and every $\bx \in C$.
1. Hence $\bw \in R$.
1. Hence $R$ is convex.
1. Since $R$ is also a cone, hence $R$ is a convex cone.
```


```{prf:definition} Recession cone
:label: def-cvx-recession-cone

Let $C$ be a nonempty convex set.
The set of all directions of recession for $C$ is called its *recession cone*
and is denoted by $R_C$.
```

```{prf:theorem} Recession cone of a linear subspace
:label: res-cvx-subspace-recession-cone

Let $\VV$ be a real vector space.
Let $S$ be a linear subspace of $\VV$.
Then $R_S = S$.
```

```{prf:proof}
We first show that $S \subseteq R_S$.

1. Pick some $\by \in S$.
1. Pick any $\bx \in S$.
1. Then for all $\alpha \geq 0$, $\bx + \alpha \by \in S$ 
   since $S$ is a subspace and is closed under
   scalar multiplication and vector addition.
1. Hence $\by \in R_S$.
1. Thus $S \subseteq R_S$.

We now show that $R_S \subseteq S$.

1. Pick some $\by \in R_S$.
1. Pick some fixed $\bx \in S$.
1. Since $\by$ is a recession direction, hence for every $\alpha > 0$,
   $\bx + \alpha \by \in S$.
1. Let $\bz = \bx + \alpha \by$.
1. Then $\by = \frac{1}{\alpha}(\bz - \bx)$.
1. But that means $\by \in S$. 
1. Hence $R_S \subseteq S$.
```

```{prf:theorem} Recession cone of an affine subspace
:label: res-cvx-affine-recession-cone

Let $\VV$ be a real vector space.
Let $A$ be an affine subspace of $\VV$.
Let $S$ be the linear subspace parallel to $A$.
Then $R_A = S$.
```

```{prf:proof}
Let $\ba \in A$ be some fixed point.
Then $S = A - \ba$.
We first show that $S \subseteq R_A$.

1. Pick any $\by \in S$.
1. Then $\by = \bu - \ba$ for some $\bu \in A$.
1. Pick some $\bx \in A$ and let $\alpha \geq 0$.
1. Then

   $$
   \bx + \alpha \by = \bx + \alpha (\bu - \ba)
   = 1 \cdot \bx + \alpha \cdot \bu + (- \alpha) \cdot \ba.
   $$
1. Hence $\bx + \alpha \by$ is an affine combination of
   $\bx, \bu, \ba \in A$.
1. Hence $\bx + \alpha \by \in A$.
1. Hence $\by \in R_A$.
1. Hence $S \subseteq R_A$.

We now show that $R_A \subseteq S$.

1. Pick some $\by \in R_A$.
1. Pick some fixed $\bx \in A$.
1. Since $\by$ is a recession direction, hence for every $\alpha > 0$,
   $\bx + \alpha \by \in A$.
1. Let $\bz = \bx + \alpha \by - \ba$.
1. Then $\bz \in S$. And $\bu = \bx - \ba \in S$.
1. Hence $\bz = \bu + \alpha \by$.
1. Hence $\by = \frac{1}{\alpha} (\bz - \bu)$.
1. But that means $\by \in S$. 
1. Hence $R_A \subseteq S$.
```


The following results describe the properties of
recession cones for nonempty, closed and convex sets.

### Closedness

```{prf:property} Closedness of recession cone
:label: res-cvx-recession-cone-closedness

Let $C$ be a nonempty, closed and convex set.
Then the recession cone $R_C$ is a closed and convex cone.
```

```{prf:proof}
We established in {prf:ref}`res-cvx-recession-dir-set-cone` that $R_C$
is a convex cone. We next prove the closedness.

1. Let $\{ \by_k \}$ be a convergent sequence of $R_C$.
1. Let $\by = \lim_{k \to \infty} \by_k$.
1. For any $\bx \in C$ and $\alpha \geq 0$, we have
   $\bz_k = \bx + \alpha \by_k \in C$ since $\by_k$ is a recession direction.
1. Now let $\bz = \lim \bz_k = \bx + \alpha \by$.
1. Since $C$ is closed, hence $\bz \in C$.
1. Thus, for any $\bx \in C$ and $\alpha \geq 0$,
   $\bx + \alpha \by \in C$.
1. Hence $\by$ is a recession direction of $C$ and $\by \in R_C$.
1. Thus every convergent sequence of $R_C$ converges in $R_C$.
1. Hence $R_C$ is closed.
```

### Recession Directions for Closed and Convex Sets

```{prf:theorem} Characterization of recession directions
:label: res-cvx-recession-dir-charac

Let $C$ be a nonempty, closed and convex set.
A vector $\by$ belongs to $R_C$ if and only if there exists
a vector $\bx \in C$ such that $\bx + \alpha \by \in C$ for all $\alpha \geq 0$.
```

```{prf:proof}
Suppose $\by \in R_C$.
Then by definition, for every $\bx \in C$ and $\alpha \geq 0$,
$\bx + \alpha \by \in C$.

Now, for the converse, let $\by \in \VV$ and
assume that there exists a vector $\bx \in C$ such that
for every $\alpha \geq 0$, $\bx + \alpha \by \in C$.
If $\by = \bzero$, then there is nothing to prove as $\bzero \in R_C$
always. Hence, assume that $\by \neq \bzero$.
Let $\widehat{\bx} \in C$ be arbitrary.
We shall first show that $\widehat{\bx} + \by \in C$.
We shall do this by building a converging sequence $\{ \by_k \}$
that converges to $\by$ and showing that for sufficiently
large $k$, $\widehat{\bx} + \by_k \in C$, hence
$\{ \widehat{\bx} + \by_k \}$ is a converging sequence of $C$
converging in $C$ due to closedness of $C$.

1. By hypothesis, $\bz_k = \bx + k \by \in C$, where $k \in \Nat$.
1. If $\widehat{x} = \bz_k$ for some $k$, then
   $\widehat{\bx} + \by = \bx + (k+1) \by \in C$ and we are done.
1. Let us then consider the case where $\widehat{\bx} \neq \bz_k$
   for every $k$.
1. Define

   $$
   \by_k = \frac{\bz_k - \widehat{\bx}}{\| \bz_k - \widehat{\bx} \|} \| \by \|.
   $$
1. Then

   $$
   \widehat{\bx} + \by_k
   = \frac{\| \by \|}{\| \bz_k - \widehat{\bx} \|} \bz_k
   + \frac{\| \bz_k - \widehat{\bx} \| - \| \by \|}{\| \bz_k - \widehat{\bx} \|} \widehat{\bx}.
   $$
1. We can see that $\widehat{\bx} + \by_k$ lies on a line that starts
   at $\widehat{\bx}$ and passes through $\bz_k$
   since $\widehat{\bx} + \by_k$ is an affine combination of
   $\widehat{\bx}$ and $\bz_k$.
1. Also, note that $\widehat{\bx} + \by_k$ lies between
   $\widehat{\bx}$ and $\bz_k$ for all $k$ for which
   $\| \bz_k - \widehat{\bx} \| > \| \by \|$.
1. Hence, there exists $k_0 \in \Nat$ such that for all $k > k_0$,
   $\widehat{\bx} + \by_k \in C$ due to convexity of $C$.
1. We have

   $$
   \frac{\by_k}{\| \by \|} 
   &= \frac{\bz_k - \widehat{\bx}}{\| \bz_k - \widehat{\bx} \|}\\
   &= \frac{\bz_k - \bx}{\| \bz_k - \widehat{\bx} \|}
   + \frac{\bx - \widehat{\bx}}{\| \bz_k - \widehat{\bx} \|}\\
   &=  \frac{\| \bz_k - \bx \|}{\| \bz_k - \widehat{\bx} \|}
   \frac{\bz_k - \bx}{\| \bz_k - \bx \|}
   + \frac{\bx - \widehat{\bx}}{\| \bz_k - \widehat{\bx} \|}\\
   &=  \frac{\| \bz_k - \bx \|}{\| \bz_k - \widehat{\bx} \|}
   \frac{\by}{\| \by \|}
   + \frac{\bx - \widehat{\bx}}{\| \bz_k - \widehat{\bx} \|}\\
   $$
1. Note that $\{ \bz_k \}$ is an unbounded sequence.
1. Hence $\| \bz_k - \widehat{\bx} \| \to \infty$ and

   $$
   \frac{\| \bz_k - \bx \|}{\| \bz_k - \widehat{\bx} \|} \to 1,
   \quad
   \frac{\bx - \widehat{\bx}}{\| \bz_k - \widehat{\bx} \|} \to \bzero
   $$
   as $k \to \infty$.
1. Hence $\by_k \to \by$ as $k \to \infty$.
1. After dropping the first $k_0$ terms, the sequence
   $\{\widehat{\bx} + \by_k \}$ is a sequence of $C$.
1. Since $\widehat{\bx} + \by_k \to \widehat{\bx} + \by$ as
   $k \to \infty$, hence $\{\widehat{\bx} + \by_k \}$
   is a converging sequence of $C$ (after the first $k_0$ terms).
1. Since $C$ is closed, hence $ \widehat{\bx} + \by \in C$.

We have established that 
for every $\widehat{\bx} \in C$, $\widehat{\bx} + \by \in C$.
We now need to show that $\widehat{\bx} + \beta \by \in C$
for every $\beta \geq 0$.

1. If $\beta = 0$ then $\widehat{\bx} \in C$.
   Hence assume that $\beta > 0$.
1. Consider the vector $\beta \by$.
1. For ever $\alpha \geq 0$,
   
   $$
   \bx + \alpha (\beta \by) = \bx + (\alpha \beta) \by \in C.
   $$
1. Hence due to previous argument, $\widehat{\bx} + \beta \by \in C$.
1. This proves that $\by$ is indeed a recession direction of $C$.
```

### Unboundedness

```{prf:theorem} Unboundedness = Nonzero recession directions
:label: res-cvx-recession-dir-nz-unbounded

Let $C$ be a nonempty, closed and convex set.
Its recession cone $R_C$ contains a nonzero direction if and only if $C$ is unbounded.
```

```{prf:proof}

It is easy to show that $C$ must be unbounded to have
a nonzero recession direction.
We now show that if $C$ is unbounded, then $R_C$
does contain a nonzero recession direction.

1. Assume that $C$ is unbounded.
1. Pick some $\bx \in C$.
1. Let $\{ \bz_k \}$ be an unbounded sequence of $C$.
1. Consider the sequence $\{ \by_k \}$ where

   $$
   \by_k = \frac{\bz_k - \bx}{\| \bz_k - \bx \|}.
   $$
1. Note that $\{ \by_k \}$ is a bounded sequence since $\| \by_k \| = 1$.
1. Let $\by$ be a limit point of $\{ \by_k \}$.
1. Note that $\by$ must be a nonzero vector since it is a limit point of
   $\{ \by_k \}$.
1. Let $\alpha \geq 0$ and consider the vector $\bx + \alpha \by_k$.

   $$
   \bx + \alpha \by_k &= \bx + \alpha  \frac{\bz_k - \bx}{\| \bz_k - \bx \|} \\
   &=  \frac{\alpha}{\| \bz_k - \bx \|}\bz_k 
   + \frac{\| \bz_k - \bx \| - \alpha}{\| \bz_k - \bx \|} \bx.
   $$
1. $\bx + \alpha \by_k$ is an affine combination of $\bx$ and $\bz_k$.
   Hence it lies on the line starting from $\bx$ passing through $\bz_k$.
1. Also since $\{ \bz_k \}$ is unbounded, hence there exists
   $k_0 \in \Nat$ such that for all $k > k_0$,
   the inequality $\| \bz_k - \bx \| > \alpha$ holds true.
1. Hence for all $k > k_0$,  the point $\bx + \alpha \by_k$
   lies on the line segment between $\bx$ and $\bz_k$.
1. Due to convexity of $C$, for all $k > k_0$,
   we have $\bx + \alpha \by_k \in C$.
1. Since $\bx + \alpha \by$ is a limit point of $\{ \bx + \alpha \by_k \}$
   and $C$ is closed, hence $\bx + \alpha \by \in C$.
1. Thus for a given $\bx \in C$
   there exists a nonzero $\by$ such that for all $\alpha \geq 0$, 
   we have $\bx + \alpha \by \in C$.
1. By {prf:ref}`res-cvx-recession-dir-charac`, $\by$ must be
   a (nonzero) recession direction of $C$.
```

```{prf:corollary} Boundedness and recession cone
:label: res-cvx-recession-cone-bounded

A nonempty, closed and convex set $C$ is bounded if and only if $R_C = \{  \bzero \}$.

Recall that in a finite dimensional ambient vector space,
closed and bounded sets are compact.
Hence a nonempty, compact and convex set has a zero recession cone.
```


### Relative Interior

```{prf:theorem} Recession cone of relative interior
:label: res-cvx-recession-cone-relint

Let $C$ be a nonempty, closed and convex set.
The recession cones of $C$ and $\relint C$ are equal.
```

```{prf:proof}
We need to show that $R_C = R_{\relint C}$.
We first show that $R_{\relint C} \subseteq R_C$.

1. Recall that since $C$ is nonempty and convex, 
   hence $\relint C$ is nonempty and convex ({prf:ref}`res-cvx-nonempty-relint`).
1. Let $\by \in R_{\relint C}$.
1. Pick some $\bx \in \relint C \subseteq C$.
1. Then for all $\alpha \geq 0$, 
   we have $\bx + \alpha \by \in \relint C \subseteq C$.
1. By {prf:ref}`res-cvx-recession-dir-charac`, $\by$ is also
   a recession direction for $C$.
1. Since this applies for every $\by \in R_{\relint C}$,
   hence $R_{\relint C} \subseteq R_C$.

For the converse, we proceed as follows.

1. Let $\by \in R_C$.
1. Pick some $\bx \in \relint C$.
1. Then for any $\alpha \geq 0$, we have $\bx + \alpha \by \in C$.
1. Hence by line segment principle ({prf:ref}`res-cvx-convex-relint-segment`),
   $\bx + \alpha \by \in \relint C$ for all $\alpha \geq 0$.
   1. We have $\bx \in \relint C$.
   1. Pick any $\beta > \alpha$.
   1. We also have $\bx + \beta \by \in C = \closure C$.
   1. Then $\bx + \alpha \by$ lies on the line segment between $\bx$ and $\bx + \beta \by$.
   1. Hence $\bx + \alpha \by \in \relint C$.
1. We have established that for any fixed $\bx \in \relint C$ and all $\alpha \geq 0$,
   $\bx + \alpha \by \in \relint C$.
1. Hence $\by \in R_{\relint C}$.
1. Thus $R_C \subseteq R_{\relint C}$.

Together we have $R_C = R_{\relint C}$.
```

### Intersection

```{prf:theorem} Intersection and recession cones
:label: res-cvx-recession-cone-intersect

Let $C$ and $D$ be nonempty, closed and convex sets
such that $C \cap D \neq \EmptySet$, we have

$$
R_{C \cap D} = R_C \cap R_D.
$$
More generally, for any collection of closed convex sets $\{ C_i \}_{i \in I}$,
where $I$ is an arbitrary index set and $\bigcap_{i \in I} C_i \neq \EmptySet$,
we have

$$
R_{\bigcap_{i \in I} C_i} = \bigcap_{i \in I}R_{C_i}.
$$
```

```{prf:proof}
We first show it for two nonempty, closed and convex sets $C$ and $D$
with nonempty intersection.

1. We can see that $C \cap D$ is also a nonempty, closed and convex set.
1. Let $\by \in R_{C \cap D}$.
1. Then for every $\bx \in C \cap D$ and all $\alpha \geq 0$, we have
   $\bx + \alpha \by \in C \cap D$.
1. Hence, by {prf:ref}`res-cvx-recession-dir-charac`, $\by \in R_C$
   and $\by \in R_D$.
1. Hence $\by \in R_C \cap R_D$.
1. Hence $R_{C \cap D} \subseteq R_C \cap R_D$.
1. Conversely, let $\by \in R_C \cap R_D$.
1. Pick any $\bx \in C \cap D$.
1. By definition, $\bx + \alpha \by \in C \cap D$ for all $\alpha \geq 0$.
1. Hence $\by \in R_{C \cap D}$.
1. Hence $R_C \cap R_D \subseteq R_{C \cap D}$.
1. Together we have $R_{C \cap D} = R_C \cap R_D$.


It is straightforward to generalize this argument for an arbitrary family of
nonempty closed and convex sets with a nonempty intersection.
```


```{prf:corollary} Recession cones and containment
:label: res-cvx-recession-cone-contain

Let $C$ and $D$ be nonempty, closed and convex sets
such that $C \subseteq D$.
Then $R_C \subseteq R_D$.
```

```{prf:proof}
We note that $C = C \cap D$.
Due to {prf:ref}`res-cvx-recession-cone-intersect`,

$$
R_C = R_{C \cap D} = R_C \cap R_D.
$$
Hence $R_C \subseteq R_D$.
```


### Linear Transformations

```{prf:theorem} Recession cone of inverse image under linear transformation
:label: res-cvx-recession-cone-lin-op-inverse-image

Let $\VV$ and $\WW$ be real, finite dimensional, normed linear spaces.
Let $\bAAA : \VV \to \WW$ be a linear operator.
Let $C \subseteq \VV$ be a nonempty, closed and convex subset of $\VV$.
Let $D \subseteq \WW$ be a nonempty, compact and convex subset of $\WW$.
Consider the set

$$
E = \{ \bx \in C \ST \bAAA(\bx)  \in D \}.
$$
Assume that $E$ is nonempty.
Then, $E$ is closed and convex and its recession cone is given by

$$
R_E = R_C \cap (\nullspace \bAAA)
$$
where $\nullspace \bAAA$ denotes the null space of the linear operator $\bAAA$.
Furthermore, $E$ is compact if and only if $R_E = \{ \bzero \}$.
```

```{prf:proof}
Consider the set $F = \{ \bx \in \VV \ST \bAAA(\bx)  \in D \}$.

1. $\bAAA$ is a continuous (linear) transformation since both $\VV$ and $\WW$
   are finite dimensional.
1. $F$ is the inverse image of a closed and convex set $D$ under $\bAAA$.
1. Hence $F$ is closed and convex.
1. We further note that $E = C \cap F$.
1. Since $E$ is nonempty by hypothesis, hence $F$ is also nonempty.
1. We can easily show that the recession cone of $F$, is $R_F = \nullspace \bAAA$.
   1. Let $\by \in \nullspace \bAAA$.
   1. Pick any fixed $\bx \in F$ and $\alpha \geq 0$.
   1. Then $\bAAA(\bx + \alpha \by) = \bAAA(\bx) \in D$.
   1. Hence $\bx + \alpha \by \in F$.
   1. Hence $\by \in R_F$.
   1. Hence $\nullspace \bAAA \subseteq R_F$.
   1. Conversely, for contradiction assume that there exists
      $\by \in R_F$ such that $\by \notin \nullspace \bAAA$.
   1. Then $\bz = \bAAA(\by) \neq \bzero$.
   1. We require that for every $\bx \in F$ and for every $\alpha > 0$,
      we must have

      $$
      \bAAA(\bx + \alpha \by)
      = \bAAA(\bx) + \alpha \bz \in D.
      $$
   1. However, this can only happen if $D$ is unbounded.
   1. Since $D$ is compact, it is bounded, hence we arrive at a contradiction.
   1. This establishes that $R_F = \nullspace \bAAA$.
1. Due to {prf:ref}`res-cvx-recession-cone-intersect`,
   since $E = C \cap F$ and both $C$ and $F$ are nonempty, closed and convex,
   hence

   $$
   R_E = R_C \cap R_F = R_C \cap (\nullspace \bAAA).
   $$

Finally, due to {prf:ref}`res-cvx-recession-cone-bounded`,
$E$ is compact if and only if $R_C \cap (\nullspace \bAAA) = \{ \bzero \}$.
```


## Lineality Space

```{prf:definition} Lineality space
:label: def-cvx-lineality-space

Let $C$ be a nonempty and convex set. The *lineality space*
of $C$, denoted by $L_C$, is the set of directions of recession
$\by$ whose opposite, $-\by$, is also a direction of recession.

In other words,

$$
L_C = R_C \cap (- R_C).
$$
```

As a consequence of this definition, if $\by \in L_C$, then
$\bx + \alpha \by \in C$ for every $\alpha \in \RR$.
In other words, the whole line in the direction of $\by$
with $\bx$ as one of its points belongs to $C$.

### As a Subspace

For nonempty, closed and convex sets, their lineality space
is a subspace of the ambient vector space.

```{prf:theorem} Lineality space as a subspace
:label: res-cvx-lineality-subspace-closed-convex

Let $\VV$ be an $n$-dim real normed linear space.
Let $C \subseteq \VV$ be a nonempty, closed and convex subset of $\VV$.
Then the lineality space of $C$ is a subspace of $\VV$.
```

```{prf:proof}
Let $\by_1, \by_2 \in L_C$ and $\alpha_1, \alpha_2 \in \RR$ be nonzero scalars.

1. Then

   $$
   \alpha_1 \by_1 + \alpha_2 \by_2
   = |\alpha_1 | (\sgn(\alpha_1)) \by_1 + |\alpha_2 |  (\sgn(\alpha_2)) \by_2.
   $$
1. Let $c = |\alpha_1 | + |\alpha_2 |$ and 
   define $t = \frac{ |\alpha_1 |}{|\alpha_1 | + |\alpha_2 |} = \frac{|\alpha_1 |}{c}$.
1. We note that $\frac{|\alpha_2 |}{c} = 1 - t$.
1. Also define $\bz_1 = (\sgn(\alpha_1)) \by_1$ and $\bz_2 = (\sgn(\alpha_2)) \by_2$.
1. Then

   $$
   \alpha_1 \by_1 + \alpha_2 \by_2
   &= |\alpha_1 | (\sgn(\alpha_1)) \by_1 + |\alpha_2 |  (\sgn(\alpha_2)) \by_2 \\
   &= |\alpha_1 | \bz_1 + |\alpha_2 |  \bz_2 \\ 
   &=  (|\alpha_1 | + |\alpha_2 |) (t \bz_1 + (1-t) \bz_2) \\ 
   &= c ( t \bz_1 + (1- t) \bz_2).
   $$
1. Since $R_C$ is a convex cone, hence $L_C$ is also a convex cone.
1. We can see that $\bz_1$ and $\bz_2$ in $L_C$ because
   $\bz_i$ is either equal to $\by_i$ or equal to $-\by_i$.
1. By convexity of $L_C$, $\bz = t \bz_1 + (1- t) \bz_2 \in L_C$.
1. Since $L_C$ is a cone, hence $c \bz \in L_C$.
1. Hence $\alpha_1 \by_1 + \alpha_2 \by_2  \in L_C$.
1. Hence $L_C$ is closed under linear combinations.
1. Hence $L_C$ is indeed a linear subspace of $\VV$.
```

### Relative Interior

```{prf:theorem} Lineality space of relative interior
:label: res-cvx-lineality-space-relint

Let $C$ be a nonempty, closed and convex set.
The lineality spaces of $C$ and $\relint C$ are equal.
```

```{prf:proof}
We have

$$
L_{\relint C} = R_{\relint C} \cap (- R_{\relint C}) 
= R_C \cap (- R_C) = L_C.
$$
We used {prf:ref}`res-cvx-recession-cone-relint`.
```

### Intersection

```{prf:theorem} Intersection and lineality spaces
:label: res-cvx-lineality-space-intersect

Let $C$ and $D$ be nonempty, closed and convex sets
such that $C \cap D \neq \EmptySet$, we have

$$
L_{C \cap D} = L_C \cap L_D.
$$
More generally, for any collection of closed convex sets $\{ C_i \}_{i \in I}$,
where $I$ is an arbitrary index set and $\bigcap_{i \in I} C_i \neq \EmptySet$,
we have

$$
L_{\bigcap_{i \in I} C_i} = \bigcap_{i \in I}L_{C_i}.
$$
```

```{prf:proof}
We have

$$
L_{\bigcap_{i \in I} C_i} 
&= R_{\bigcap_{i \in I} C_i} \bigcap (- R_{\bigcap_{i \in I} C_i}) \\
&= (\bigcap_{i \in I}R_{C_i}) \bigcap (- \bigcap_{i \in I}R_{C_i}) \\
&= \bigcap_{i \in I} (R_{C_i} \cap (-R_{C_i})) \\
&= \bigcap_{i \in I} L_{C_i}.
$$
We made use of {prf:ref}`res-cvx-recession-cone-intersect`.
```

```{prf:corollary} Lineality spaces and containment
:label: res-cvx-lineality-space-contain

Let $C$ and $D$ be nonempty, closed and convex sets
such that $C \subseteq D$.
Then $L_C \subseteq L_D$.
```

```{prf:proof}
We note that $C = C \cap D$.
Due to {prf:ref}`res-cvx-lineality-space-intersect`,

$$
L_C = L_{C \cap D} = L_C \cap L_D.
$$
Hence $L_C \subseteq L_D$.
```


### Linear Transformations

```{prf:theorem}
:label: res-cvx-lineality-space-lin-op-inverse-image

Let $\VV$ and $\WW$ be real, finite dimensional, normed linear spaces.
Let $\bAAA : \VV \to \WW$ be a linear operator.
Let $C \subseteq \VV$ be a nonempty, closed and convex subset of $\VV$.
Let $D \subseteq \WW$ be a nonempty, compact and convex subset of $\WW$.
Consider the set

$$
E = \{ \bx \in C \ST \bAAA(\bx)  \in D \}.
$$
Assume that $E$ is nonempty.
Then, $E$ is closed and convex and its lineality space is given by

$$
L_E = L_C \cap (\nullspace \bAAA)
$$
where $\nullspace \bAAA$ denotes the null space of the linear operator $\bAAA$.
Furthermore, $E$ is compact if and only if $R_E = \{ \bzero \}$.
```


```{prf:proof}
We have

$$
L_E 
&= R_E \cap (-R_E) \\
&= (R_C \cap (\nullspace \bAAA)) \cap (- (R_C \cap (\nullspace \bAAA))) \\
&= (R_C \cap (\nullspace \bAAA)) \cap ((- R_C) \cap (\nullspace \bAAA))) \\
&= (R_C \cap (- R_C)) \cap (\nullspace \bAAA)\\
&= L_C \cap (\nullspace \bAAA).
$$
We used {prf:ref}`res-cvx-recession-cone-lin-op-inverse-image`.
```

### Decomposition along Lineality Spaces


```{prf:theorem} Decomposition of a convex set along subspaces of its lineality space
:label: res-cvx-lineality-decomposition-subspace

Let $\VV$ be an $n$-dim real inner product space.
Let $C$ be a nonempty convex subset of $\VV$.
Let $L_C$ be its lineality space.
Then for every linear subspace $S \subseteq L_C$,
we have

$$
C = S + (C \cap S^{\perp}).
$$
```

Note that since $C$ is not required to be closed, hence
$L_C$ itself may not be a linear subspace.

```{prf:proof}
Since $\VV$ is finite dimensional, hence it supports
an orthogonal decomposition ({prf:ref}`res-la-vs-direct-sum-orth-comp`)

$$
\VV = S + S^{\perp}.
$$

We first show that $C \subseteq S + C \cap S^{\perp}$.

1. Let $\bx \in C$.
1. Then $\bx = \by + \bz$ where $\by \in S$ and $\bz \in S^{\perp}$.
1. Since $\by \in S \subseteq L_C$, hence $\by$ is 
   a recession direction of $C$ and so is $-\by$.
1. Hence $\bz = \bx - \by \in C$.
1. Hence $\bz \in C \cap S^{\perp}$.
1. Thus for every $\bx \in C$, we have $\bx = \by + \bz$
   such that $\by \in S$ and $\bz \in C \cap S^{\perp}$.
1. Hence $C \subseteq S + C \cap S^{\perp}$.

We now show the converse $S + C \cap S^{\perp} \subseteq C$.

1. Let $\bx \in S + C \cap S^{\perp}$.
1. Then $\bx  = \by + \bz$ such that $\by \in S$
   and $\bz \in C \cap S^{\perp}$.
1. Thus $\bz \in C$.
1. Since $S \subseteq L_C$, hence $\by$ is a recession direction
   for $C$.
1. Hence $\bz + \by = \bx \in C$.
1. Hence $S + C \cap S^{\perp} \subseteq C$.
```

## Nested Sequences of Closed and Convex Sets

Recall that the intersection of a nested sequence
of compact sets is nonempty and compact.

In this subsection, we consider a nested sequence
$\{ C_k \}$ of nonempty, closed and convex sets.
We derive a number of conditions under which
their intersection $\bigcap_{k=1}^{\infty}C_k$
is nonempty.

A very good example of a nested sequence of
closed and convex sets is a sequence of
sublevel sets of a closed and convex function.


```{prf:theorem} General condition for nonempty intersection
:label: res-cvx-recession-nested-nonempty-intersect-gen-cond

Let $\VV$ be an $n$-dim real inner product space.
Let $\{ C_k \}$ be a sequence of nonempty, closed and convex subsets
of $\VV$
such that $C_{k + 1} \subseteq C_k$ for all $k \in \Nat$.
Let $R_k$ and $L_k$ be the recession cone
and lineality space of $C_k$ respectively for every $k \in \Nat$.
Further, let

$$
R = \bigcap_{k=1}^{\infty} R_k
\text{ and }
L = \bigcap_{k=1}^{\infty} L_k.
$$
Assume that $R = L$.
Then the intersection $C = \bigcap_{k=1}^{\infty} C_k$
is nonempty and has the form

$$
C = \bigcap_{k=1}^{\infty} C_k = L + \tilde{C}
$$
where $\tilde{C}$ is some nonempty and compact set.
```

```{prf:proof}
We note some properties of the sequences $\{ R_k \}$
and $\{ L_k \}$.

1. Since $C_k$ are nested, hence the recession cones
   $R_k$ are also nested ({prf:ref}`res-cvx-recession-cone-contain`).
1. Since $C_k$ are nested, hence the lineality spaces
   $L_k$ are also nested ({prf:ref}`res-cvx-lineality-space-contain`).
1. Since $C_k$ are nonempty closed and convex, hence
   $L_k$ are linear subspaces
   due to {prf:ref}`res-cvx-lineality-subspace-closed-convex`.

We first show that $L$ is a linear subspace and
for all sufficiently large $k$, $L_k = L$.

1. Since $L_k$ are nested subspaces,
   hence $\dim L_{k+1} \leq \dim L_k$ for every $k$.
1. $L \neq \EmptySet$ since $\bzero \in L_k$ for every $k$.
   Hence $\bzero \in L$.
1. We can also see that $L$ must be a linear subspace of $\VV$
   since it is an (infinite) intersection of linear subspaces.
1. Since $\VV$ is finite dimensional, it follows that
   for all $k$ sufficiently large, we have $L_k = L$.
   In other words, there exists $k_0 \in \Nat$ such that
   for all $k > k_0$, $L_k = L$. 
1. Without loss of generality, assume that 

   $$
   L_k = L, \Forall k.
   $$
   We can achieve this by dropping the first $k_0$ terms
   from the sequence $\{ C_k \}$ for which 
   $L$ is a proper subset of $L_k$.

We next show that for all sufficiently large $k$,
we have $R_k \cap L^{\perp} = \{ \bzero \}$.

1. Since $\bzero \in R_k$ for every $R_k$ and
   $L$ is a linear subspace, hence
   $\bzero \in R_k \cap L^{\perp}$ for every $k$.
1. For contradiction, assume that it is not true
   that there exists $k_0 \in \Nat$ such that
   for every $k > k_0$,
   $R_k \cap L^{\perp} = \{ \bzero \}$.
1. Then, since $R_k$ are nested,
   hence for each $k$ there exists $\by_k \in R_k \cap L^{\perp}$
   with $\| \by_k \| = 1$.
   1. Consider some $k \in \Nat$.
   1. There exists some $l > k$ such that
      $R_l \cap L^{\perp} \neq \{ \bzero \}$.
   1. Then $R_l \cap L^{\perp}$ contains a nonzero vector $\bu$.
   1. Since $R_l$ is a cone, hence $\bu$ can be scaled
      to some $\bv$ so that $\| \bv \| = 1$.
   1. Since $L^{\perp}$ is a linear subspace, hence $\bv \in L^{\perp}$
      also.
   1. Hence $\bv \in R_l \cap L^{\perp}$.
   1. But since $R_l \subseteq R_k$, hence
      $\bv \in R_k \cap L^{\perp}$.
1. Now consider the set $D = \{\by \ST \| \by \| = 1 \}$.
1. Let $E_k = D \cap R_k \cap L^{\perp}$ for every $k$.
1. Then $E_k$ is nonempty for every $k$.
1. We note that $E_k$ is also compact.  
   1. The set $D$ is closed and bounded.
   1. $R_k$ is closed for every $k$
      ({prf:ref}`res-cvx-recession-cone-closedness`).
   1. $L^{\perp}$ is a subspace of a finite dimensional space,
      hence it is closed.
   1. $E_k$ is an intersection of
      closed sets, hence it is closed.
   1. Since $D$ is bounded, hence $E_k \subseteq D$
      is also bounded.
   1. Since $E_k$ is closed and bounded,
      hence it is compact as $\VV$ is finite dimensional.
1. Then $\{ E_k \}$ is a sequence of nested compact sets
   since $E_{k + 1} \subseteq E_k$ for every $k$.
1. Hence $E = \bigcap_{k=1}^{\infty} E_k$ is nonempty.
   TBD link result.
1. But expanding $E$ we see that

   $$
   E &= \bigcap_{k=1}^{\infty} E_k \\
   &= \bigcap_{k=1}^{\infty} (D \cap R_k \cap L^{\perp}) \\
   &= D \cap L^{\perp} \cap \left (\bigcap_{k=1}^{\infty} R_k \right ) \\
   &= D \cap L^{\perp} \cap R \\
   &= D \cap L^{\perp} \cap L \\
   &= D \cap \{ \bzero \} \\
   &= \EmptySet.
   $$
   We used the facts that
   1. $R = \bigcap_{k=1}^{\infty} R_k$.
   1. $L = R$ by hypothesis.
   1. $L^{\perp} \cap L = \{ \bzero \}$ since they are orthogonal
      complements.
   1. All members of $D$ are nonzero since they are unit norm.
1. We have arrived at a contradiction that $E$ must be an empty set.
1. Hence, we conclude that  $R_k \cap L^{\perp} = \{ \bzero \}$
   holds true for all sufficiently large $k$.
1. Again without loss of generality, we shall assume that

   $$
   R_k \cap L^{\perp} = \{ \bzero \}, \quad \Forall k \in \Nat.
   $$

We have established so far that
$L$ is a linear subspace,
$L_k = L$ and $R_k \cap L^{\perp} = \{ \bzero \}$
for all $k$ without loss of generality.
We shall now show that $C =\bigcap_{k=1}^{\infty} C_k$ is nonempty.

1. Note that $C_k \cap L^{\perp}$ is not empty.
   1. We have $\VV = L \oplus L^{\perp}$.
   1. Let $\bx \in C_k$.
   1. Then $\bx = \by + \bz$ where $\by \in L$ and $\bz \in L^{\perp}$.
   1. But then $\by \in L_k$ since $L \subseteq L_k$.
   1. Then $\by$ and $-\by$ are recession directions of $C_k$.
   1. Hence $\bz = \bx - \by \in C_k$.
   1. Hence $\bz \in C_k \cap L^{\perp}$.
1. By {prf:ref}`res-cvx-recession-cone-intersect`, the recession cone
   of $C_k \cap L^{\perp}$ is given by

   $$
   R_{C_k \cap L^{\perp}} = R_k \cap R_{L^{\perp}}.
   $$
1. Since $L^{\perp}$ is a linear subspace of $\VV$, hence
   due to {prf:ref}`res-cvx-subspace-recession-cone`,
   $R_{L^{\perp}} = L^{\perp}$.
1. Hence

   $$
    R_{C_k \cap L^{\perp}} = R_k \cap L^{\perp} = \{ \bzero \}.
   $$
1. Then due to {prf:ref}`res-cvx-recession-dir-nz-unbounded`,
   $C_k \cap L^{\perp}$ is bounded for ever $k$.
1. Since $C_k$ is closed and $L^{\perp}$ is closed, hence
   $C_k \cap L^{\perp}$ is also closed for every $k$.
1. Hence $C_k \cap L^{\perp}$ is a compact set for every $k$.
1. Since $\{ C_k \}$ are nested, hence
   $\{ C_k \cap L^{\perp} \}$ are also a nested sequence
   of compact sets.
1. Then their intersection is nonempty and compact. In other words,
   the set

   $$
   \tilde{C} = \bigcap_{k=1}^{\infty}
   \left (C_k \cap L^{\perp} \right )
   = \left ( \bigcap_{k=1}^{\infty} C_k \right ) \cap L^{\perp}
   = C \cap L^{\perp}
   $$
   is nonempty and compact.
1. Hence $C$ is also nonempty.
1. Hence, due to {prf:ref}`res-cvx-lineality-space-intersect`,
   the lineality space of $C = \bigcap_{k=1}^{\infty} C_k$
   is given by $L = \bigcap_{k=1}^{\infty} L_k$.
1. By {prf:ref}`res-cvx-lineality-decomposition-subspace`,

   $$
   C = L + (C \cap L^{\perp})
   = L + \tilde{C}.
   $$
```

```{prf:corollary} Compactness of the nested intersection
:label: res-cvx-rec-nested-compact-intersect

Under the assumptions of
{prf:ref}`res-cvx-recession-nested-nonempty-intersect-gen-cond`,
if $R = \bigcap_{k=1}^{\infty} R_k = \{ \bzero \}$,
then the intersection
$C = \bigcap_{k=1}^{\infty} C_k$ is nonempty and compact.
```

```{prf:proof}
Since $L = R = \{ \bzero \}$, hence
$C = L + \tilde{C} = \tilde{C}$.
We have already established that $\tilde{C}$
is both nonempty and compact. 
```


### Nested Sequence with Linear Inequality Constraints

Consider the problem of minimizing a closed and convex
function under linear inequality constraints.

1. The sublevel sets form a nested sequence of
   closed and convex sets.
1. The solution set of a set of linear inequality
   constraints is another convex set
   (an intersection of closed half spaces).


```{prf:theorem} Nested sequence with inequality constraints
:label: res-cvx-rec-nested-seq-closed-inequality-constraints

Let $\VV$ be a Euclidean space.
Let $\{ C_k \}$ be a sequence of nonempty, closed and convex
subsets of $\VV$.
Let $R_k$ and $L_k$ be the recession cone
and lineality space of $C_k$ respectively for every $k \in \Nat$.
Further, let

$$
R = \bigcap_{k=1}^{\infty} R_k
\text{ and }
L = \bigcap_{k=1}^{\infty} L_k
\text{ and }
C = \bigcap_{k=1}^{\infty} C_k
$$
Let $X$ be a subset of $\VV$ specified by
linear inequality constraints; i.e.,

$$
X = \{ \bx \in \VV \ST \langle \bx, \ba_i \rangle \leq b_i, i=1,\dots,r \}
$$
where $\ba_i \in \VV$ and $b_i \in \RR$.
Further assume that

1. $C_{k+1} \subseteq C_k$ for all $k$.
1. The intersection $X \cap C_k$ is nonempty for all $k$.
1. We have $R_X \cap R \subseteq L$
   where $R_X$ is the recession cone of $X$.

Then the intersection $X \cap C$ is nonempty. 
```

### Quadratic Function with Quadratic Constraints

```{prf:theorem} Quadratic function with quadratic constraints
:label: res-cvx-recession-quad-func-quad-constraints

Let $\{ C_k \}$ be a sequence of subsets of $\RR^n$
given by

$$
C_k = \{ \bx \ST \bx^T \bQ \bx + \ba^T \bx + b \leq w_k \}
$$
where $\bQ \in \SS^n_+$ is a symmetric positive semidefinite
matrix, $\ba \in \RR^n$ is a vector, $b  \in \RR$ is a scalar,
and $\{ w_k \}$ is a nonincreasing sequence of scalars
that converges to $0$.

Also, let $X$ be a subset of $\RR^n$ of the form

$$
X = \{ \bx \in \RR^n \ST 
\bx^T \bQ_j \bx + \ba^T_j \bx + b_j \leq 0, j=1,\dots, r \}
$$
where $\bQ_j \in \SS^n_+$, $\ba_j \in \RR^n$ 
and $b_j \in \RR$.

Assume further that $X \cap C_k \neq \EmptySet$ for all $k$.
Then, the intersection
$X \cap (\bigcap_{k=1}^{\infty} C_k)$ is nonempty.
```

Note that $\bx^T \bQ \bx + \ba^T \bx + b$
is a quadratic function and $C_k$ are its sublevel sets.



## Closedness Under Linear Transformations

We address the question of guarantees under which
the image of a closed and convex set under a linear
transformation is also closed from the perspective
of recession cones.

If a set $C$ is closed and bounded, then it is
compact in a finite dimensional space, the
linear operator is continuous in a finite
dimensional space, hence the image of $C$
is also compact.
The results in this section are relevant for
closed and convex sets which are not bounded.


```{prf:theorem} Closedness of image under linear transformation
:label: res-cvx-closed-im-lin-op-closed

Let $\VV$ and $\WW$ be real, finite dimensional, normed linear spaces.
Let $\bAAA : \VV \to \WW$ be a linear operator.
Let $C \subseteq \VV$ be a nonempty, closed and convex subset of $\VV$.
Let the nullspace of $\bAAA$ be denoted by $\nullspace \bAAA$.

If $R_C \cap \nullspace \bAAA \subseteq L_C$, then
the set $\bAAA(C)$ is closed.
```

```{prf:proof}
We shall show that every converging sequence of $D = \bAAA(C)$
converges in $D$.

1. Let $\{ \by_k \}$ be a sequence of points in $D$
   converging to some point $\by \in \WW$.
1. We introduce the sets

   $$
   W_k = \{ \bz \in \WW \ST \| \bz - \by \| \leq \| \by_k - \by \| \}.
   $$
1. Note that $W_k$ are closed balls centered at
   $\by$ and with radii $\| \by_k - \by \|$.
1. Hence $W_k$ are nonempty, closed and convex.
1. By taking appropriate subsequence of $\{ W_k \}$ if necessary,
   we can ensure that it is a nested sequence of closed balls.
1. Further define

   $$
   C_k = \{ \bx \in C \ST \bAAA(\bx) \in W_k \}.
   $$
1. Since $\by_k \in W_k$, hence $C_k$ is nonempty.
1. Then due to {prf:ref}`res-cvx-recession-cone-lin-op-inverse-image`,
   $C_k$ is closed and convex.
1. Since  $\{ W_k \}$ is nested, hence  $\{ C_k \}$ is also
   a nested sequence of nonempty, closed and convex sets.
1. We note that every $C_k$ has the same recession cone
   given by $R = R_C \cap (\nullspace \bAAA)$
   due to {prf:ref}`res-cvx-recession-cone-lin-op-inverse-image`.
1. Similarly, every $C_k$ has the same lineality space
   given by $L = L_C \cap (\nullspace \bAAA)$
   due to {prf:ref}`res-cvx-lineality-space-lin-op-inverse-image`. 
1. By hypothesis, $R_C \cap \nullspace \bAAA \subseteq L_C$.
1. Hence $R_C \cap \nullspace \bAAA \subseteq L_C \cap \nullspace \bAAA$.
1. In other words, $R \subseteq L$.
1. By definition $L \subseteq R$.
1. Hence $R = L$.
1. Consequently, due to
   {prf:ref}`res-cvx-recession-nested-nonempty-intersect-gen-cond`,
   the set $\bigcap_{k=1}^{\infty} C_k$ is nonempty.
1. Now pick some $\bx \in \bigcap_{k=1}^{\infty} C_k$.
1. Then $\bx \in C$ since $C_k \subseteq C$ for ever $k$.
1. Since $\bx \in C_k$ for every $k$, hence $\bAAA(\bx) \in W_k$
   for every $k$.
1. Hence, $\bAAA(\bx) \in \bigcap_{k=1}^{\infty} W_k$.
1. But $\bigcap_{k=1}^{\infty} W_k = \{ \by \}$.
1. Hence $\bAAA(\bx) = \by$.
1. Since $\bx \in C$, hence $\by = \bAAA(\bx) \in D = \bAAA(C)$.
1. Hence the sequence $\{ \by_k \}$ converges in $D$.
1. Since the sequence was chosen arbitrarily,
   hence every convergent sequence of $D$ converges in $D$.
1. Hence $D$ is closed.
```

In the special case where
the closed and convex set $C$ is bounded, then
$R_C = L_C = \{ \bzero \}$ and 
$R_C \cap \nullspace \bAAA = L_C$. Hence
$\bAAA(C)$ is also closed.

### Linear Inequality Constraints

```{prf:theorem} Closedness of image of a closed and convex set with linear inequality constraints under linear transformation
:label: res-cvx-closed-im-lin-op-closed-lin-constraints

Let $\VV$ and $\WW$ be real, finite dimensional, normed linear spaces.
Let $\bAAA : \VV \to \WW$ be a linear operator.
Let $C \subseteq \VV$ be a nonempty, closed and convex subset of $\VV$.
Let the nullspace of $\bAAA$ be denoted by $\nullspace \bAAA$.

Let $X$ be a subset of $\VV$ specified by
linear inequality constraints; i.e.,

$$
X = \{ \bx \in \VV \ST \langle \bx, \ba_i \rangle \leq b_i, i=1,\dots,r \}
$$
where $\ba_i \in \VV$ and $b_i \in \RR$.

If $R_X \cap R_C \cap \nullspace \bAAA \subseteq L_C$,
then the set $\bAAA(X \cap C)$ is closed.
```

```{prf:proof}

The argument is similar to {prf:ref}`res-cvx-closed-im-lin-op-closed`
and uses {prf:ref}`res-cvx-rec-nested-seq-closed-inequality-constraints`
to establish the nonemptiness of the intersection of the
nested sequence of closed and convex sets.

Let $D = \bAAA(X \cap C)$.
We shall show that every converging sequence of $D = \bAAA(C)$
converges in $D$.

1. Let $\{ \by_k \}$ be a sequence of points in $D$
   converging to some point $\by \in \WW$.
1. Let $W_k$ and $C_k$ be defined as in
   {prf:ref}`res-cvx-closed-im-lin-op-closed`.
1. By choosing a suitable subsequence, we are guaranteed
   that $C_k$ are nested.
1. We have $\by_k \in W_k$. Hence $C_k \subseteq C$ is nonempty.
1. Also $\by_k \in D = \bAAA(X \cap C)$.
1. Let $\bu \in C_k$ such that $\bAAA(\bu) = \by_k$.
1. Then $\bu \in X \cap C$ holds true also.
1. Hence $(X \cap C) \cap C_k = X \cap C_k$ is not empty for every $k$.
1. By hypothesis, $R_X \cap R_C \cap \nullspace \bAAA \subseteq L_C$.
1. Hence $R_X \cap R_C \cap \nullspace \bAAA \subseteq L_C \cap \nullspace \bAAA$.
1. Following the definition of $R$ and $C$ from the proof
   of {prf:ref}`res-cvx-closed-im-lin-op-closed`,
   we have $R_X \cap R \subseteq L$.
1. Thus, all assumptions of
   {prf:ref}`res-cvx-rec-nested-seq-closed-inequality-constraints`
   are satisfied.
1. Hence the set $X \cap (\bigcap_{k=1}^{\infty} C_k)$ is nonempty.
1. Pick any point $\bx \in X \cap (\bigcap_{k=1}^{\infty} C_k)$.
1. Then $\bx \in X$ and $\bx \in C$ with 
   $\bAAA(\bx) = \by$.
1. Hence $\by \in \bAAA(X \cap C)$.
1. Hence the sequence $\{ \by_k \}$ converges in $D$.
1. Since the sequence was chosen arbitrarily,
   hence every convergent sequence of $D$ converges in $D$.
1. Hence $D$ is closed.
```