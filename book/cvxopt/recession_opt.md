# Directions of Recession

In this section, we analyze the question of
existence of optimal solutions of a convex
optimization problem from the perspective
of the theory of recession cones developed
in {ref}`sec:cvx:recession`.

Main references for this section are {cite}`bertsekas2003convex`.


Recall from {prf:ref}`res-cvxf-convexity-epigraph` that
the epigraph of a convex function is convex.
Recall from {prf:ref}`res-ms-closed-func-closed-epi`
that the epigraph of a closed function is closed.
Also the epigraph of a proper function is nonempty.
Hence, the epigraph of a proper, closed and convex function
is nonempty, closed and convex.
Also, it is easy to see that the epigraph is also unbounded.

The key idea is that the recession cone of the epigraph
can be used to obtain the directions along which the
function decreases monotonically.

Throughout this section, we shall assume that $\VV$ is
a Euclidean space unless otherwise specified.

## Recession Cone of a Convex Function

### Recession Cones of Sublevel Sets

```{prf:theorem} Recession cones of sublevel sets
:label: res-opt-sublevel-recession-cones

Let $f: \VV \to \RERL$ be a proper, closed and convex function.
Consider the sublevel sets $S_t = \{ \bx \in \VV \ST f(\bx) \leq t \}$
where $t \in \RR$.
Then

1. All the nonempty sublevel sets $S_t$ have the same
   recession cone given by

   $$
   R_{S_t} = \{ \by \in \VV \ST (\by, 0) \in R_{\epi f} \}
   $$
   where $R_{\epi f}$ is the recession cone of the epigraph of $f$.
1. If one nonempty sublevel set $S_t$ is compact, then all of the
   sublevel sets $\sublevel(f, t)$ are compact.
```

We mention that $(\bzero, 0) \in R_{\epi f}$.
Consequently, $\bzero \in R_{S_t}$.

```{prf:proof}
(1) Recession cone for sublevel sets

1. Pick some $t \in \RR$ such that $S_t$ is nonempty.
   Since $f$ is proper, hence such $t$ exists.
1. Let $\by$ be a direction of recession of $S_t$.
1. Let $\bx \in S_t$.
1. Then $f(\bx) \leq t$. Hence $(\bx, t) \in \epi f$.
1. Since $\by$ is a recession direction,
   we have $f(\bx + \alpha \by) \leq t$
   for every $\alpha \geq 0$.
1. Hence $(\bx + \alpha \by, t) \in \epi f$ for all $\alpha \geq 0$.
1. Rewriting $(\bx, t) + \alpha (\by, 0) \in \epi f$ 
   for every $\alpha \geq 0$.
1. Since $\epi f$ is a nonempty, closed and convex set,
   and there exists one $(\bx, t) \in \epi f$ such that
   for every $\alpha \geq 0$, the point $(\bx, t) + \alpha (\by, 0) \in \epi f$,
   hence due to {prf:ref}`res-cvx-recession-dir-charac`,
   $(\by, 0) \in R_{\epi f}$.
1. Since $\by$ was arbitrary element of $R_{S_t}$, hence
   for every $\by \in R_{S_t}$, $(\by, 0) \in R_{\epi f}$.
1. Hence $R_{S_t} \subseteq \{ \by \in \VV \ST (\by, 0) \in R_{\epi f} \}$.

For the converse, we proceed as follows.
1. Let $(\by, 0) \in R_{\epi f}$.
1. Pick some vector $(\bx, t) \in \epi f$.
1. Then for every $\alpha \geq 0$, we have
   $(\bx + \alpha \by, t) \in \epi f$.
1. Hence $f(\bx + \alpha \by) \leq t$  for every $\alpha \geq 0$.
1. Hence $\bx + \alpha \by \in S_t$ for every $\alpha \geq 0$.
1. Since $f$ is closed, hence $S_t$ is closed.
1. Since $S_t$ is a nonempty, closed and convex set, $\bx \in S_t$
   and for every $\alpha \geq 0$, we have $\bx + \alpha \by \in S_t$,
   hence by {prf:ref}`res-cvx-recession-dir-charac`,
   $\by \in R_{S_t}$.
1. Hence $R_{S_t} \supseteq \{ \by \in \VV \ST (\by, 0) \in R_{\epi f} \}$.

(2) Compactness of sublevel sets.

1. We are given that for some $t$, the nonempty, closed and convex set
   $S_t$ is compact.
1. Then $S_t$ is bounded.
1. Then due to {prf:ref}`res-cvx-recession-dir-nz-unbounded`,
   $R_{S_t} = \{ \bzero \}$.
1. By previous argument, all nonempty sublevel sets have the
   same recession cone.
1. Hence $\{ \bzero \}$ is the recession cone of every nonempty sublevel set.
1. Hence by {prf:ref}`res-cvx-recession-dir-nz-unbounded`
   every nonempty sublevel set is bounded.
1. Since $f$ is closed, hence every nonempty sublevel set is closed.
1. Since every nonempty sublevel set is closed and bounded and
   $\VV$ is Euclidean (finite dimensional), hence
   every nonempty sublevel set is compact.
```

### Recession Cone of a Convex Function

```{prf:definition} Recession cone of a convex function
:label: def-opt-cvx-func-recession-cone

Let $f: \VV \to \RERL$ be a proper, closed and convex function.
The (common) recession cone of its nonempty sublevel sets
is called the *recession cone* of $f$ and is denoted by
$R_f$. 
Each $\by \in R_f$ is called a *direction of recession* 
of $f$. 
```

1. The requirement that $f$ be proper guarantees that
   $f(\bx) < \infty$ for at least one $\bx \in \VV$
   and hence there exist some nonempty sublevel sets.
1. Since $f$ is also closed and convex,
   hence {prf:ref}`res-opt-sublevel-recession-cones`
   guarantees that all the nonempty sublevel sets
   have an identical recession cone.


## Existence of Solutions of Convex Programs

The recession cone of a function provides
excellent candidates for descent directions
for a convex function.

If we start at some $\bx \in \dom f$ and move
indefinitely along a recession direction
$\by \in R_f$, then we are guaranteed that
we stay within the sublevel set $\sublevel(f, f(\bx))$;
i.e., $f(\bx + \alpha \by) \leq f(\bx)$ for every
$\alpha \geq 0$. 

```{prf:observation}
:label: res-opt-recession-dir-non-ascent-dir

A direction of recession of a proper convex function
$f$ is a direction of continuous non-ascent; i.e.,
the value of the function never increases in a
direction of recession.

Conversely, if we start at some $\bx \in \dom f$
and while moving along a direction $\by \in \VV$,
encounter a point $\bz = \bx + \alpha \by$
for some $\alpha > 0$ such that
$f(\bz) > f(\bx)$, then $\by$ cannot be
a direction of recession.

A direction that is not a direction of
recession of $f$ is a direction of
eventual continuous ascent of $f$.
```

```{prf:theorem} Continuous ascent on non-recession directions
:label: res-opt-non-recession-dir-continuous-ascent

Let $f: \VV \to \RERL$ be a proper, closed and convex function.
Let $\by \notin R_f$ where $R_f$ is the recession cone of $f$.
Let $\bx \in \dom f$. Then, along the ray starting from $\bx$
in the direction $\by$, eventually $f$ increases
monotonically to $\infty$; i.e., for some $t \geq 0$
and for all $s_1, s_2 \geq t$ with
$s_1 < s_2$, we have

$$
f(\bx + s_1 \by) < f(\bx + s_2 \by).
$$
```

```{prf:proof}
We recall that $R_f$ is the recession cone for all nonempty
sublevel sets of $f$.

1. Let $S_0$ denote the sublevel set $\{ \bz \in \VV \ST f(\bz) \leq f(\bx) \}$.
1. Then $\by$ is not a recession direction of $S_0$.
1. Then due to {prf:ref}`res-cvx-recession-dir-charac`,
   there exists some $t > 0$ such that
   $\bx + t \by \notin S_0$.
1. Hence $f(\bx + t \by) > f(\bx)$.
1. In other words, the point $\bx + t \by$ is outside
   the relative boundary of $S_0$.
1. Consider any $s > t$. 
1. Let $\bu = \bx + t \by$ and $\bv = \bx + s \by$.
1. Clearly $\bu$ lies on the line segment between $\bx$ and $\bv$.
1. Let $r = \frac{t}{s}$.
1. Then
   
   $$
   (1-r) \bx + r \bv = \frac{1}{s}((s -t ) \bx + t (\bx + s \by))
   = \bx + t \by = \bu.
   $$
1. By convexity of $f$

   $$
   f(\bu) \leq (1-r) f(\bx) + r f(\bv).
   $$
1. Hence 
   
   $$
   r f(\bv) \geq f(\bu) - (1-r) f(\bx) > f(\bu) - (1-r) f(\bu) = r f(\bu).
   $$
1. Thus $f(\bv) > f(\bu)$.
1. Thus for every $s > t$, we have

   $$
   f(\bx + s \by) > f(\bx + t \by).
   $$
1. Now pick any $s_1, s_2 \geq t$ with
   $s_1 < s_2$.
1. By the previous argument

   $$
   f(\bx + s_1 \by) \geq f(\bx + t \by).
   $$
1. Noting that $\bx + s_1 \by$ lies on the line segment
   between $\bx$ and $\bx + s_2 \by$, using the previous
   argument, it is clear that

   $$
   f(\bx + s_2 \by) > f(\bx + s_1 \by).
   $$
1. Since for all $s \geq t$, $f$ is strictly monotonically
   increasing, hence

   $$
   \lim_{s \to \infty} f(\bx + s \by) = \infty.
   $$ 
```
