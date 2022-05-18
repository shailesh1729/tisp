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


```{prf:theorem} Recession cone theorem
:label: res-cvx-recession-cone-theorem

Let $C$ be a nonempty, closed and convex set.


1. The recession cone $R_C$ is a closed and convex cone.
1. A vector $\by$ belongs to $R_C$ if and only if there exists
   a vector $\bx \in C$ such that $\bx + \alpha \by \in C$ for all $\alpha \geq 0$.
1. $R_C$ contains a nonzero direction if and only if $C$ is unbounded.
1. The recession cones of $C$ and $\relint C$ are equal.
1. If $D$ is another closed convex set such that $C \cap D \neq \EmptySet$, we have

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
(1)

1. We established in {prf:ref}`res-cvx-recession-dir-set-cone` that $R_C$
   is a convex cone.
```