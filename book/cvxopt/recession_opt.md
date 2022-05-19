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


