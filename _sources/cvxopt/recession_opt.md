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

### Constrained Minimization: Compact Solution Set


```{prf:theorem} Constrained minimization: nonempty and compact minimizer set
:label: res-opt-const-min-compact-minimizers

Let $f : \VV \to \RERL$ be a proper, closed and convex function.
Let $X$ be a nonempty, closed and convex subset of $\VV$.
Assume that $C = X \cap \dom f \neq \EmptySet$.
Consider the optimization problem:

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in X.
$$
Then the set of minimizers of $f$ over $X$ is nonempty and compact
if and only if $X$ and $f$ have no common nonzero direction of recession;
i.e.,

$$
R_f \cap R_X = \{ \bzero \}.
$$
```

```{prf:proof}
Let $X^*$ denote the set of minimizers for this optimization problem.
Let $p^*$ be the optimal value of the optimization problem.

We first consider the case of unconstrained minimization where
$X = \VV$. Hence $C = \dom f$. 

1. In this case $R_X = \VV$.
1. Hence $R_f \cap R_X = \{ \bzero \}$ if and only if $R_f = \{ \bzero \}$.
1. Assume that $X^*$ is nonempty and compact.
1. We have $X^* = \{\bx \in \VV \ST f(\bx) \leq p^* \}$.
1. $X^*$ is a nonempty sublevel set. 
1. Since $X^*$ is a sublevel set and $f$ is closed and convex, hence $X^*$ is also
   closed and convex.
1. Since $X^*$ is compact, it is closed and bounded.
1. Hence, as per {prf:ref}`res-cvx-recession-dir-nz-unbounded`,
   its recession cone is $\{ \bzero \}$.
1. Then due to {prf:ref}`def-cvx-func-recession-cone`, the recession cone of $f$,
   $R_f =  \{ \bzero \}$.
1. Conversely if $R_f \cap R_X = \{ \bzero \}$, then $R_f = \{ \bzero \}$.
1. Then the recession cone of every nonempty sublevel set is $\{ \bzero \}$.
1. Then due to {prf:ref}`res-cvx-recession-dir-nz-unbounded`, every nonempty
   sublevel set is closed and bounded, hence compact.
1. Then due to Weierstrass theorem ({prf:ref}`res-opt-weierstrass-theorem`),
   $X^*$ is nonempty and compact (since one of the sublevel sets is nonempty
   and bounded).

We now consider the more general case where $X \neq \VV$.


1. Introduce a new function $\tilde{f} : \VV \to \RERL$ given by

   $$
   \tilde{f}(\bx) = \begin{cases}
   f(\bx) & \text{ if } \bx \in X;\\
   \infty & \text{ otherwise }.
   \end{cases}
   $$
1. We can see that $\dom \tilde{f} = X \cap \dom f = C$ which is nonempty
   by hypothesis.
1. Hence $\tilde{f}$ is proper.
1. Since $f$ is convex, hence $\tilde{f}$ (a restriction of $f$ on $X$)
   is also convex.
1. Note that for any $t \in \RR$
   
   $$
   \sublevel (\tilde{f}, t) = \sublevel(f, t) \cap X.
   $$
1. Since both $\sublevel(f, t)$ and $X$ are closed and convex sets, 
   hence $\sublevel (\tilde{f}, t)$ is also closed and convex for every $t \in \RR$.
1. Since all sublevel sets of $\tilde{f}$ are closed, hence $f$ is a closed function.
1. Thus, $\tilde{f}$ is a proper, closed and convex function.
1. Furthermore, the set of minimizers for the unconstrained minimization
   of $\tilde{f}$ is nothing but $X^*$.
1. Thus, the original constrained minimization program of minimizing
   $f$ over $X$ is equivalent to the unconstrained minimization
   of $\tilde{f}$.
1. By the previous argument, $X^*$ is nonempty and compact
   if and only if $\tilde{f}$ has no nonzero direction of recession.
1. The recession cones of $f$ and $\tilde{f}$ are related by
  
   $$
   R_{\tilde{f}} = R_f \cap R_X.
   $$
   1. Let $t \in \RR$ be such that $\sublevel (\tilde{f}, t)$ is nonempty.
   1. Then $R_{\tilde{f}} = R_{\sublevel (\tilde{f}, t)}$.
   1. But $\sublevel (\tilde{f}, t) = \sublevel(f, t) \cap X$.
   1. Since both $\sublevel(f, t)$ and $X$ are nonempty, closed and
      convex and their intersection is nonempty, hence
      due to {prf:ref}`res-cvx-recession-cone-intersect`,

      $$
      R_{\sublevel (\tilde{f}, t)} = R_{\sublevel(f, t)} \cap R_X
      = R_f \cap R_X.
      $$
1. Hence $X^*$ is nonempty and compact if and only if
   $R_f \cap R_X = \{ \bzero \}$. 
```

### Constrained Minimization: Existence of Solutions

```{div}
The {prf:ref}`res-opt-const-min-compact-minimizers`
provides guarantees under which the problem of
minimization of a proper, closed and convex function $f$
over a nonempty, closed and convex set $X$ has nonempty
as well as compact solution set $X^*$.
In this subsection, we concern ourselves with the
more general case where the solution set may be
unbounded.
In other words, we are only concerned with the
conditions under which $X^*$ is nonempty.
```

```{prf:lemma} Constrained minimization: nested sublevel sets
:label: res-opt-const-min-nested-sublevel-sets

Let $f : \VV \to \RERL$ be a proper, closed and convex function.
Let $X$ be a nonempty, closed and convex subset of $\VV$.
Assume that $X \cap \dom f \neq \EmptySet$.
Consider the optimization problem:

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in X.
$$
Let $p^* = \inf_{\bx \in X} f(\bx)$.
Let $\{ t_k \}$ be a nonincreasing sequence of real numbers
such that $t_k \downarrow p^*$; i.e., 
the sequence reaches the limit $p^*$ from above.
Consider the sublevel sets $V_k = \sublevel(f, t_k)$.

1. The sublevel sets $V_k$ are nonempty for every $k$.
1. The sequence $\{ V_k \}$ is a sequence of nested sets.
1. The set $X \cap V_k$ is nonempty for every $k$.
1. The set $X \cap V_K$ is closed and convex for every $k$.
1. The sequence $\{ X \cap V_k \}$ is a sequence of nested sets.
1. The set of minimizers $X^*$ for the optimization problem
   is given by

   $$
   X^* = \bigcap_{k=1}^{\infty} (X \cap V_k).
   $$
```

```{prf:proof}
$t_k \downarrow p^*$ means that
1. $t_k > p^*$ for every $k$.
1. $t_{k+1} \leq t_k$ for every $k$.
1. For every $\epsilon > 0$, there exists a $k$ such that $t_k \leq p^* + \epsilon$.

We are given that $p^*$ is the optimum value.
Hence for every $\epsilon > 0$, there exists a $\bx \in X \cap \dom f$ such that
$f(\bx) \leq p^* + \epsilon$.

(1) $V_k$ is nonempty.
1. Since $t_k > p^*$, hence $\epsilon = t_k - p^* > 0$.
1. Then there exists $\bx \in X \cap \dom f$ such that
   $f(\bx) \leq p^* + \epsilon = t_k$.
1. Hence $V_k = \sublevel(f, t_k) \neq \EmptySet$.

(2) Nested sublevel sets
1. $V_{k+1} \subseteq V_k$ for every $k$ since $t_{k+1} \leq t_k$ for every $k$.
1. Hence $\{ V_k \}$ is a sequence of nested sets.

(3) $X \cap V_k$ is nonempty.
1. We established that there exists $\bx \in X \cap \dom f$ such that
   $f(\bx) \leq t_k$.
1. Hence $\bx \in X$ and $\bx \in V_k$.
1. Hence $X \cap V_k$ is nonempty.

(4) $X \cap V_k$ is closed and convex.
1. $X$ is closed by hypothesis.
1. Since $f$ is closed, hence $V_k$ is closed.
1. Since $X$ and $V_k$ are both closed, hence $X \cap V_k$ is closed.
1. $X$ is convex by hypothesis.
1. Since $f$ is convex, hence $V_k$ is convex.
1. Since $X$ and $V_k$ are both convex, hence $X \cap V_k$ is convex.

(5) $\{ X \cap V_k \}$ is nested.
1. Since $V_{k+1} \subseteq V_k$,
   hence $X \cap V_{k+1} \subseteq X \cap V_k$ for every $k$.
1. Hence $\{ X \cap V_k \}$ is a sequence of nested sets.

(6) Minimizers
1. Let $\bx \in X^*$.
1. Then $f(\bx) = p^*$ and $\bx \in X$.
1. Hence $\bx \in \sublevel(f, t)$ for every $t \geq p^*$ and $\bx \in X$.
1. Hence $\bx \in X \cap V_k$ for every $k$.
1. Hence $X^* \subseteq X \cap V_k$ for every $k$.
1. Hence $X^* \subseteq \bigcap_{k=1}^{\infty} (X \cap V_k)$.
1. For the converse, let $\bx \in \bigcap_{k=1}^{\infty} (X \cap V_k)$.
1. Then $\bx \in X$ and $\bx \in V_k$ for every $k$.
1. Hence $\bx \in X$ and $f(\bx) \leq t_k$ for every $k$.
1. Then $f(\bx) \leq \lim_{k \to \infty} t_k$.
1. Hence $f(\bx) \leq p^*$.
1. But since $p^*$ is the optimal value, hence $f(\bx) = p^*$.
1. Thus, $\bx \in X$ and $f(\bx) = p^*$.
1. Hence $\bx \in X^*$.
1. Hence $\bigcap_{k=1}^{\infty} (X \cap V_k) \subseteq X^*$.
1. Together $X^* = \bigcap_{k=1}^{\infty} (X \cap V_k)$.
```

```{prf:theorem} Constrained minimization: existence of solutions
:label: res-opt-const-min-nonempty-minimizers

Let $f : \VV \to \RERL$ be a proper, closed and convex function.
Let $X$ be a nonempty, closed and convex subset of $\VV$.
Assume that $C = X \cap \dom f \neq \EmptySet$.
Consider the optimization problem:

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in X.
$$
Then the set of minimizers of $f$ over $X$ is nonempty
if

$$
R_X \cap R_f = L_X \cap L_f.
$$

In particular, the set of minimizers is of the form

$$
(L_X \cap L_f) + \tilde{X}
$$
where $\tilde{X}$ is some nonempty and compact set.
```

```{prf:proof}
.

1. Let $p^* = \inf_{\bx \in X} f(\bx)$.
1. Let $\{ t_k \}$ be a nonincreasing sequence of real numbers
   such that $t_k \downarrow p^*$; i.e., 
   the sequence reaches the limit $p^*$ from above.
1. Consider the sublevel sets 

   $$
   V_k = \sublevel(f, t_k) = \{ \bx \in \VV \ST f(\bx) \leq t_k \}.
   $$
1. Then the set of minimizers is given by
   $X^* = \bigcap_{k=1}^{\infty} (X \cap V_k)$.
1. The sets $X \cap V_k$ are nonempty, closed, convex and nested
   due to {prf:ref}`res-opt-const-min-nested-sublevel-sets`.
1. For every $k$, the recession cone of $X \cap V_k$ is $R = R_X \cap R_f$
   due to {prf:ref}`res-cvx-recession-cone-intersect`
   and {prf:ref}`def-cvx-func-recession-cone`.
1. For every $k$, the lineality space of $X \cap V_k$ is $L = L_X \cap L_f$
   due to {prf:ref}`res-cvx-lineality-space-intersect`
   and {prf:ref}`res-cvx-sublevel-sets-lineality-space`.
1. Thus, every $X \cap V_k$ has the same recession cone and lineality space
   satisfying $R=L$ by hypothesis.
1. Then due to {prf:ref}`res-cvx-recession-nested-nonempty-intersect-gen-cond`,
   the nested sequence of nonempty, closed and convex sets
   $\{ X \cap V_k \}$ has a nonempty intersection and
   has the form

   $$
   \bigcap_{k=1}^{\infty} (X \cap V_k) = (L_X \cap L_f) + \tilde{X}
   $$
   where $\tilde{X}$ is a nonempty and compact set.
1. By {prf:ref}`res-opt-const-min-nested-sublevel-sets`,
   $X^* = \bigcap_{k=1}^{\infty} (X \cap V_k)$.
1. We are done.
```

### Minimization with Linear Constraints: Existence of Solutions

```{prf:theorem} Minimization with linear inequality constraints: existence of solutions
:label: res-opt-min-lin-const-nonempty-minimizers

Let $f : \VV \to \RERL$ be a proper, closed and convex function.
Let $X$ be a nonempty, closed and convex subset of $\VV$
specified as a 
set of linear inequality constraints; i.e.,

$$
X = \{ \bx \in \VV \ST \langle \bx, \ba_i \rangle \leq b_i, i=1,\dots,r \}
$$
where $\ba_i \in \VV$ and $b_i \in \RR$.

Assume that $C = X \cap \dom f \neq \EmptySet$.
Consider the optimization problem:

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in X.
$$
Then the set of minimizers of $f$ over $X$ is nonempty
if

$$
R_X \cap R_f \subseteq L_f,
$$
``` 

```{prf:proof}
Following the proof of {prf:ref}`res-opt-const-min-nonempty-minimizers`,
we choose $\{ t_k \}$ such that $t_k \downarrow p^*$.

1. $X$ is an intersection of closed half-spaces.
1. Hence $X$ is nonempty, closed and convex.
1. $\{ V_k \}$ is a nested
   sequences of nonempty, closed and convex sets.
1. $X \cap V_k$ is nonempty for all $k$.
1. Since $V_k$ are nonempty, hence they have the same
   recession cone $R_f$ and same lineality space $L_f$.
1. $R_X \cap R_f \subseteq L_f$ by hypothesis.
1. Hence due to {prf:ref}`res-cvx-rec-nested-seq-closed-inequality-constraints`,

   $$
   X^* = \bigcap_{k=1}^{\infty} (X \cap V_k)
   = X \cap \left (\bigcap_{k=1}^{\infty} V_k \right )
   $$
   is nonempty.
```

### Quadratically Constrained Quadratic Minimization

```{prf:theorem} Quadratically constrained quadratic minimization: existence of solutions
:label: res-opt-qcqp-nonempty-minimizers

Let $f : \RR^n \to \RERL$ be a proper, closed and convex function
given by

$$
f(\bx) = \bx^T \bQ \bx + \ba^T \bx
$$
where $\bQ \in \SS^n_+$ is a symmetric positive semidefinite
matrix, $\ba \in \RR^n$ is a vector.

Let $X$ be a nonempty, closed and convex subset of $\RR^n$ given by

$$
X = \{ \bx \in \RR^n \ST 
\bx^T \bQ_j \bx + \ba^T_j \bx + b_j \leq 0, j=1,\dots, r \}
$$
where $\bQ_j \in \SS^n_+$, $\ba_j \in \RR^n$ 
and $b_j \in \RR$.
Assume that $C = X \cap \dom f \neq \EmptySet$.
Consider the optimization problem:

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in X.
$$

Assume that the optimal value for this optimization problem
$p^* > -\infty$.
Then the set of minimizers of $f$ over $X$ is nonempty.
```

```{prf:proof}
Following the proof of {prf:ref}`res-opt-const-min-nonempty-minimizers`,
we choose $\{ t_k \}$ such that $t_k \downarrow p^*$.

1. The sets $V_k$ have the form

   $$
   V_k = \{ \bx \in \RR^n \ST \bx^T \bQ \bx + \ba^T \bx \leq t_k \}
   $$
   where $\{ t_k \}$ is a nonincreasing sequence converging to $p^*$
   which is finite.
1. $X$ is specified via a set of quadratic inequalities.
1. $X \cap V_k$ is nonempty for all $k$.
1. By {prf:ref}`res-cvx-recession-quad-func-quad-constraints`, the set

   $$
   X^* = \bigcap_{k=1}^{\infty} (X \cap V_k)
   = X \cap \left (\bigcap_{k=1}^{\infty} V_k \right )
   $$
   is nonempty.
```


### Quadratic Programs

```{prf:theorem} Quadratic minimization with linear inequalities: existence of solutions
:label: res-opt-qp-lin-ineq-nonempty-minimizers

Let $f : \RR^n \to \RERL$ be a proper, closed and convex function
given by

$$
f(\bx) = \bx^T \bQ \bx + \bc^T \bx
$$
where $\bQ \in \SS^n_+$ is a symmetric positive semidefinite
matrix, $\bc \in \RR^n$ is a vector.

Let $X$ be a nonempty set of the form

$$
X = \{ \bx \in \RR^n \ST \bA \bx \preceq \bb \}
$$
where $\bA \in \RR^{m \times n}$ and $\bb \in \RR^n$. 
The following are equivalent.

1. $f$ attains a minimum over $X$.
1. The optimum value $p^* > -\infty$.
1. For all $\by$ such that $\bA \by \preceq \bzero$
   and $\by \in \nullspace \bQ$, we have
   $\bc^T \by \geq 0$.
```

The recession cone of $X$ is given by $\{ \by \ST \bA \by \preceq \bzero \}$.

Recall from {prf:ref}`ex-cvx-recession-cone-quadratic-functional` that

$$
R_f = \{\by \ST \bQ \by = \bzero,  \bc^T \by \leq 0 \}
\text{ and }
L_f = \{\by \ST \bQ \by = \bzero,  \bc^T \by = 0 \}.
$$
```{prf:proof}

(1) $\implies$ (2) is obvious.

(2) $\implies$ (3)

1. For all $\bx \in X$, $\by \in \nullspace \bQ$ with
   $\bA \by \preceq \bzero$ and $\alpha \geq 0$, we have
   1. $\by \in R_X$ since $\bA \by \preceq \bzero$.
   1. Hence $\bx + \alpha \by \in X$.
   1. Also

      $$
      f(\bx + \alpha \by)
      &= (\bx + \alpha \by)^T \bQ (\bx + \alpha \by)
      + \bc^T (\bx + \alpha \by) \\
      &= \bx^T \bQ \bx + \bc^T \bx + \alpha \bc^T \by \\
      &= f(\bx) + \alpha \bc^T \by.
      $$
      We used the hypothesis that $\bQ \by = \by^T \bQ = \bzero$.
1. If $\bc^T \by < 0$, then $\lim_{\alpha \to \infty} f(\bx + \alpha \by) = -\infty$.
1. Hence $p^* = -\infty$.
1. This contradicts the hypothesis that $p^* > -\infty$.
1. Hence $\bc^T \by \geq 0$ must hold
   for every $\by \in \nullspace \bQ$ with $\bA \by \preceq \bzero$.

(3) $\implies$ (1)

1. $\by \in R_X$ since $\bA \by \preceq \bzero$.
1. $R_f = (\nullspace \bQ) \cap \{ \by \ST \bc^T \by \leq 0 \}$.
1. Hence

   $$
   R_X \cap R_f = \{ \by \ST \bA \by \preceq \bzero \}
   \cap (\nullspace \bQ) \cap \{ \by \ST \bc^T \by \leq 0 \}.
   $$
1. Then for every $\by \in R_X \cap R_f$, then we  must have $\bc^T \by = 0$.
   1. Since $\by \in  R_X \cap R_f$, hence $\bA \by \preceq \bzero$
      and $\by \in \nullspace \bQ$.
   1. By hypothesis (3), we must have $\bc^T \by \geq 0$.
   1. But since $\by \in  R_X \cap R_f$, hence we also have $\bc^T \by \leq 0$.
   1. Together, we must have $\bc^T \by = 0$.
1. Hence $R_X \cap R_f$ reduces to

   $$
   R_X \cap R_f = \{ \by \ST \bA \by \preceq \bzero \}
   \cap (\nullspace \bQ) \cap \{ \by \ST \bc^T \by = 0 \}.
   $$
1. Recall that $L_f = \{\by \ST \bQ \by = \bzero,  \bc^T \by = 0 \}$.
1. Hence $R_X \cap R_f \subseteq L_f$.
1. We satisfy all the requirements of
   {prf:ref}`res-opt-min-lin-const-nonempty-minimizers`,
1. Hence the set of minimizers is nonempty.
1. $f$ indeed attains a minimum over $X$.
```
