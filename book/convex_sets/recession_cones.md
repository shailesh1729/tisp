# Recession Cones


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

### Recession Cones for Closed and Convex Sets

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
