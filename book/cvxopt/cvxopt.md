# Convex Optimization

Main references for this section are {cite}`beck2014introduction,boyd2004convex,bertsekas2003convex`.


## Convex Optimization Problems


```{prf:definition} Convex optimization problem general form
:label: def-opt-convex-opt-problem

Let $\VV$ be an $n$-dimensional real vector space.
Let $f : \VV \to \RR$ be a convex function
with $S = \dom f$.
Let $C \subseteq S \subseteq \VV$ be a convex set.

A mathematical optimization problem of the form

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C
$$
is known as a *convex optimization problem*.

In other words, a convex optimization problem minimizes
a convex function over a convex set.
We can write the optimal value of the minimization problem
as

$$
p^* = \inf \{ f(\bx) \ST \bx \in C \}.
$$

The set of optimal points for the minimization problem is

$$
X_{\text{opt}}  = \{ \bx \in C \ST f(\bx) = p^* \}.
$$
```

```{note}
1. $f$ is the objective function (or cost function) being minimized.
1. $\bx$ is the optimization variable.
1. $C$ is the feasible set. Any $\bx \in C$ is a feasible point.
1. The problem is feasible if $C \neq \EmptySet$.
1. If $C = \EmptySet$, then the problem is infeasible.
1. If the problem is infeasible then $p^* = \infty$.
1. If the problem is feasible then $p^* < \infty$.
1. If $p^* = -\infty$, then the problem is unbounded below.
1. We say that $\bx^*$ is an optimal point for the minimization problem if
   $f(\bx^*) = p^*$.
1. If $X_{\text{opt}}$ is nonempty, then we say that the optimal value
   $p^*$ is attained at some point.
1. It is possible that $p^*$ is finite and yet the optimal set is empty.
```

```{prf:remark} Closedness of the feasible set
:label: rem-cvx-cvxopt-general-closed-feasible

Some authors prefer to define convex optimization as
the minimization of a convex function over a *closed* and convex set.

1. We have not insisted that $C$ be a closed set in the 
   general definition of convex optimization problem.
1. The closedness of $C$ is an additional property 
   which can provide additional guarantees on the
   existence of an optimal point. We shall introduce it
   whenever needed in the discussion below.
1. Recall from {prf:ref}`res-cvx-closed-convex-halfspace-intersection`
   that a closed and convex set $C$ is an intersection of all the halfspaces 
   that contain it. Let $\{ A_i \}_{i \in I}$ be the set of halfspaces
   that contains $C$.
1. Then, each half space can be written as

   $$
   A_i = \{ \bx \in \VV \ST  \langle \bx, \ba_i \rangle \leq b_i \}.
   $$
1. Thus, $\bx \in C$ is equivalent to 
   $\langle \bx, \ba_i \rangle \leq b_i$ for every $i \in I$.
1. This gives us the motivation to consider the feasible set
   in the form of intersection of sublevel sets of convex functions.
```


Majority of convex optimization problems can be transformed into
a functional form where the constraints are expressed in the
form of sublevel sets of convex functions
and the level sets of affine functions. 

### Convex Optimization Standard Form


````{prf:definition} Convex optimization problem standard form
:label: def-cvx-opt-problem-standard-form

Let $\VV$ be an $n$-dimensional real vector space.
A mathematical optimization problem of the form

```{math}
:label: eq-cvx-opt-prob-standard-form
& \text{minimize }   & & f_0(\bx) \\
& \text{subject to } & & f_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
```
with optimization variable $\bx \in \VV$ is called
a *convex optimization problem in standard form* if

1. The objective function $f_0: \VV \to \RR$ is a convex function.
1. The inequality constraint functions $f_i: \VV \to \RR$ are convex functions for $i=1,\dots,m$.
1. The equality constraint functions $h_j: \VV \to \RR$ are affine functions for $j=1,\dots,p$.
````

```{prf:observation} Discussion on the convex optimization standard form
:label: rem-cvx-opt-standard-form-discussion

1. The domain of the problem is given by

   $$
   \DDD = \dom f_0 \cap \bigcap_{i=1}^m \dom f_i \cap \bigcap_{j=1}^p \dom h_j.
   $$
1. $\dom h_j = \VV$ for every $j=1,\dots,p$ since $h_j$ are affine functions.
1. Thus,
 
   $$
   \DDD = \dom f_0 \cap \bigcap_{i=1}^m \dom f_i.
   $$
1. By definition $\dom f_i$ are convex for $i=0,\dots,m$.
   Hence $\DDD$ is convex.
1. The feasible set $C$ is given by

   $$
   C = \dom f_0 \cap \bigcap_{i=1}^m f_i^{-1}(-\infty, 0] \cap \bigcap_{j=1}^p h_j^{-1}(0).
   $$
1. Then, $f_i^{-1}(-\infty, 0]$ are sublevel sets of convex functions hence they
   are also convex sets.
1. By {prf:ref}`res-la-aff-rv-level-set`, the level sets of affine functions are affine sets.
1. Thus, $h_j^{-1}(0)$ is an affine set. Hence, it is a convex set.
1. Thus, $C$ is an intersection of convex sets. 
1. Thus, $C$ is a convex set. 
1. We note that we can rewrite the standard form as

   $$
   & \text{minimize }  &  & f_0(\bx) \\
   & \text{subject to } & & \bx \in C
   $$
   to match with {prf:ref}`def-opt-convex-opt-problem`.
```

```{prf:remark} Adding closedness of objective and constraint functions
:label: rem-cvxopt-standard-closedness-constraints

Suppose we add an additional requirement that
the function $f_i$ for $i=0,\dots,m$ are {prf:ref}`closed <def-ms-closed-function>`.

1. Recall from {prf:ref}`def-ms-closed-function` that a function is closed
   if all its sublevel sets are closed.
1. In particular, this means that the domain of a closed function is also closed.
1. Thus, $\DDD$ is a closed set.
1. Then, $f_i^{-1}(-\infty, 0]$ are closed sets since $f_i$ are closed functions.
1. Since $\VV$ is finite dimensional, hence affine sets are closed.
   Hence $h_j^{-1}(0)$
   is closed for every $j=1,\dots,p$. 
1. Thus, $C$ is an intersection of closed and convex sets. 
1. Thus, $C$ is a closed and convex set.
1. Recall from {prf:ref}`res-ms-closed-func-closed-epi` that a function is 
   closed if and only if it has a closed epigraph.
1. Also, recall from {prf:ref}`res-ms-func-lsc-closed-func` that
   a function is closed if and only if it is l.s.c. (lower semicontinuous).
1. Further, recall from {prf:ref}`res-cvxf-convex-func-closure-convex` that
   every convex function has a closure which is l.s.c. (hence closed)
   given by its lower semicontinuous hull and the closure of a convex
   function is also convex.
1. Thus, if any of the $f_i$ for $i=0,\dots,m$ is convex but not a closed function,
   we can replace it by its lower semicontinuous hull to convert it
   to a closed convex function. This way, be can bring such problems
   to the standard form for convex optimization. 
```


```{prf:remark} Comparison of two forms
:label: rem-cvx-opt-std-form-vs-convex-set-form

We have seen two forms of describing convex optimization problems.

1. {prf:ref}`def-opt-convex-opt-problem` describes it as minimizing
   a convex function over a convex set.
1. {prf:ref}`def-cvx-opt-problem-standard-form` describes it in the
   form of minimizing a convex objective function with convex
   inequality constraints and affine equality constraints.
1. As seen in comments above, the second form can be converted
   into the first form.
1. The first form is more general. It is very useful in establishing
   the theoretical properties of convex optimization problems.
1. The second form is more useful from practical perspective. 
   Almost all real life convex optimization problems can be
   reduced to this form. It is easier to describe algorithms
   to solve convex optimization problems in terms of this form.

In the sequel, we will liberally use either form for proving
theoretical results and developing algorithms.
```


````{prf:definition} Concave function maximization problem
:label: def-cvx-opt-concave-maximization

Let $\VV$ be an $n$-dimensional real vector space.
A mathematical optimization problem of the form

```{math}
:label: eq-cvx-opt-concave-maximization
& \text{maximize }   & & f_0(\bx) \\
& \text{subject to } & & f_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
```
with optimization variable $\bx \in \VV$ is called
a *concave maximization problem* if

1. The objective function $f_0: \VV \to \RR$ is a concave function.
1. The inequality constraint functions $f_i: \VV \to \RR$ are convex functions for $i=1,\dots,m$.
1. The equality constraint functions $h_j: \VV \to \RR$ are affine functions for $j=1,\dots,p$.
````

```{prf:remark} Concave maximization as a convex optimization problem
:label: rem-concave-max-cvxopt-problem

We note that maximizing $f_0$ is same as minimizing $-f_0$.
Further, if $f_0$ is concave then $-f_0$ is convex.
Thus, {eq}`eq-cvx-opt-concave-maximization` is equivalent
to the problem

$$
& \text{minimize }   & & -f_0(\bx) \\
& \text{subject to } & & f_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
$$
which is a convex optimization problem in standard form.
With an abuse of notation, we shall call a concave function maximization
program also a convex optimization program.
```


### Proper Convex Functions

It is useful to extend these definitions to proper convex functions
as objective functions and/or inequality constraint functions.

```{prf:definition} Optimization problem general form for proper convex functions
:label: def-opt-proper-convex-opt-problem

Let $\VV$ be an $n$-dimensional real vector space.
Let $f : \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $X \subseteq \VV$ be a convex set.

A mathematical optimization problem of the form

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in X
$$
is known as a *convex optimization problem*
for proper convex functions.

In other words, this problem minimizes
a proper convex function over a convex set.
We can write the optimal value of the minimization problem
as

$$
p^* = \inf \{ f(\bx) \ST \bx \in X \}.
$$

The set of feasible points is given by $C = X \cap \dom f$
which is a convex set.

The set of optimal points for the minimization problem is

$$
X_{\text{opt}}  = \{ \bx \in C \ST f(\bx) = p^* \}.
$$
```

````{prf:definition} Convex optimization problem standard form for proper convex functions
:label: def-cvx-opt-proper-problem-standard-form

Let $\VV$ be an $n$-dimensional real vector space.
A mathematical optimization problem of the form

```{math}
:label: eq-cvx-opt-proper-prob-standard-form
& \text{minimize }   & & f_0(\bx) \\
& \text{subject to } & & f_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
```
with optimization variable $\bx \in \VV$ is called
a *convex optimization problem in standard form* for proper convex functions if

1. The objective function $f_0: \VV \to \RERL$ is a proper convex function.
1. The inequality constraint functions $f_i: \VV \to \RERL$ are 
   proper convex functions for $i=1,\dots,m$.
1. The equality constraint functions $h_j: \VV \to \RR$ are affine functions for $j=1,\dots,p$.
````

The reader can check that the definitions of
problem domain, feasible set, optimal value,
optimal solutions/points, etc. can be easily 
extended by using the effective domains of $f_0, \dots, f_m$.


### Local and Global Optima


```{prf:theorem} Local minimum is a global minimum in convex optimization
:label: res-cvxopt-local-global-minimum

Let $f : \VV \to \RR$ be a convex function. Let $C \subseteq \dom f$
be a convex set. 
Consider the problem of minimizing $f$ over $C$.
Let $\bx^*$ be locally optimal for $f$ over $C$.
Then, $\bx^*$ is globally optimal for $f$ over $C$.

In other words,

$$
f(\by) \geq f(\bx^*) \Forall \by \in C.
$$
```

```{prf:proof}
Since $\bx^*$ is a local minimum of $f$ over $C$, hence there exists $r > 0$
such that

$$
f(\bx^*) = \inf \{f(\bz) \ST \bz \in B[\bx, r] \cap C \}.
$$

In other words, $f(\bx) \geq f(\bx^*)$ for every $\bx \in B[\bx, r] \cap C$.

1. Let $\by \in C$ be any point such that $\by \neq \bx^*$.
1. We need to show that $f(\by) \geq f(\bx^*)$.
1. Let $t \in (0,1]$ be such that $\bz = \bx^* + t(\by - \bx^*) \in B[\bx, r]$.
1. Since $C$ is convex, hence $\bz \in C$ as $\bx^*, \by \in C$ and $\bz$
   is their convex combination.
1. Thus, $\bz \in B[\bx, r] \cap C$.
1. By the local optimality condition

   $$
   f(\bx^*) &\leq f(\bz)  \\
   &= f(\bx^* + t(\by - \bx^*)) \\
   &= f( (1 - t) \bx^*  + t \by) \\
   &\leq (1 -t )f(\bx^*) + t f(\by).
   $$
   We used the fact that $f$ is convex.
1. Cancelling and rearranging the terms, we get $t f(\bx^*) \leq t f(\by)$.
1. Since $t > 0$, hence it reduces to $f(\bx^*) \leq f(\by)$.
1. Thus, $\bx^*$ is indeed globally optimal.
```

```{prf:corollary} Local minimum is a global minimum in for proper convex functions
:label: res-cvxopt-local-global-minimum-proper-convex

Let $f : \VV \to \RERL$ be a proper convex function. 
Let $X$ be a convex subset of $\VV$. 
Consider the problem of minimizing $f$ over $X$.
Let $\bx^*$ be locally optimal for $f$ over $X$.
Then, $\bx^*$ is globally optimal for $f$ over $X$.

In other words,

$$
f(\by) \geq f(\bx^*) \Forall \by \in X.
$$
```

```{prf:proof}
We note that the feasible set is $C = X \cap \dom f$.
Since both $X$ and $\dom f$ are convex, hence $C$ is convex.

1. If $C = \EmptySet$,
   then there are no feasible points. Hence, no local/global optima.
1. We now consider the case where $C \neq \EmptySet$.
1. Following the argument in {prf:ref}`res-cvxopt-local-global-minimum`,
   if $\bx^*$ is locally optimal for $f$ over $C$, then it is globally
   optimal for $f$ over $C$. 
1. Consequently, it is globally optimal for $f$ over $X$ 
   as $f(\bx) = \infty > f(\bx^*)$ for every $\bx \in X \setminus \dom f$.
```

The argument can be modified to show that if $f$ is strictly convex, 
then a locally optimal point for $f$ is strictly globally optimal point.



```{prf:theorem} Local minimum is strict global minimum for strictly convex functions
:label: res-cvxopt-strict-local-global-minimum

Let $f : \VV \to \RR$ be a strictly convex function. Let $C \subseteq \dom f$
be a convex set. Let $\bx^*$ be locally optimal for $f$ over $C$.
Then, $\bx^*$ is strictly globally optimal for $f$ over $C$.

In other words,

$$
f(\by) > f(\bx^*) \Forall \by \in C.
$$
```

```{prf:proof}


There exists $r > 0$ such that $f(\bx) \geq f(\bx^*)$ for every $\bx \in B[\bx, r] \cap C$.

1. Let $\by \in C$ be any point such that $\by \neq \bx^*$.
1. Let $t \in (0,1)$ be such that $\bz = \bx^* + t(\by - \bx^*) \in B[\bx, r]$.
1. Since $C$ is convex, hence $\bz \in C$ as $\bx^*, \by \in C$ and $\bz$
   is their convex combination.
1. Thus, $\bz \in B[\bx, r] \cap C$.
1. Note that $\bz = (1-t) \bx^* + t \by$. Thus, $\bz$ is distinct from
   $\bx^*$ and $\by$ and lies in the line segment between them.
1. By the local optimality condition

   $$
   f(\bx^*) &\leq f(\bz)  \\
   &= f( (1 - t) \bx^*  + t \by) \\
   &< (1 -t )f(\bx^*) + t f(\by).
   $$
   We used the fact that $f$ is strictly convex.
1. Cancelling and rearranging the terms, we get $t f(\bx^*) < t f(\by)$.
1. Since $t > 0$, hence it reduces to $f(\bx^*) < f(\by)$.
1. Thus, $\bx^*$ is indeed strictly globally optimal.
```

### Optimal Sets

The optimal sets of a convex optimization problem are also convex.


```{prf:theorem} Optimal set is convex for a convex optimization problem
:label: res-cvxopt-convex-optimal-set

Let $f : \VV \to \RR$ be a convex function. Let $C \subseteq \dom f$
be a convex set.
Let the optimal value for the minimization of $f$ over $C$ be given by

$$
p^* = \inf \{ f(\bx) \ST \bx \in C \}.
$$
Let the optimal set (the set of optimal points) be given by

$$
X_{\text{opt}}  = \{ \bx \in C \ST f(\bx) = p^* \}.
$$
Then, $X_{\text{opt}}$ is a convex set.
```

```{prf:proof}
If $X_{\text{opt}}$  is empty, then it is convex trivially.
Now consider the case where $X_{\text{opt}}$ is nonempty.

1. Let $\bx, \by \in X_{\text{opt}}$.
1. Then, $\bx, \by \in C$.
1. Let $t \in [0, 1]$.
1. Let $\bz = t \bx + (1- t) \by$.
1. Since $C$ is convex, hence $\bz \in C$. Thus, $\bz \in \dom f$.
1. Since $f$ is convex, hence

   $$
   f(\bz) \leq t f(\bx) + (1-t)f(\by) = t p^* + (1-t)p^* = p^*.
   $$
1. But $p^* = \inf \{ f(\bx) \ST \bx \in C \}$.
1. Thus, $f(\bz) \geq p^*$.
1. Combining, the two inequalities, we get $p^* = f(\bz)$.
1. Thus, $\bz \in  X_{\text{opt}}$.
1. Thus, for every $\bx, \by \in  X_{\text{opt}}$ and every $t \in [0,1]$,
   $\bz = t \bx + (1-t) \by \in  X_{\text{opt}}$.
1. Thus, $ X_{\text{opt}}$ is indeed convex.
```


```{prf:theorem} Optimal points for minimization of strictly convex functions
:label: res-cvxopt-strict-convex-singleton

Let $f : \VV \to \RR$ be a strictly convex function. Let $C \subseteq \dom f$
be a convex set. Then, the minimization problem

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C
$$
has at most one optimal point.
```


```{prf:proof}
Let the optimal value for the minimization of $f$ over $C$ be given by

$$
p^* = \inf \{ f(\bx) \ST \bx \in C \}.
$$
Let the optimal set (the set of optimal points) be given by

$$
X_{\text{opt}}  = \{ \bx \in C \ST f(\bx) = p^* \}.
$$

1. By {prf:ref}`res-cvxopt-local-global-minimum`,
   $X_{\text{opt}}$ is a convex set.
1. If $X_{\text{opt}}$ is empty or a singleton, there is nothing more to prove.
1. For contradiction, assume that there are two distinct points
   $\bx, \by \in X_{\text{opt}}$.
1. We have $p^* = f(\bx) = f(\by)$.
1. Let $\bz = \frac{1}{2} \bx + \frac{1}{2} \by$.
1. Thus, it is a convex combination of $\bx$ and $\by$.
1. By convexity of $X_{\text{opt}}$, $\bz \in X_{\text{opt}}$.
   Thus, $f(\bz) = p^*$.
1. By strict convexity of $f$

   $$
   f(\bz) < \frac{1}{2} f(\bx) + \frac{1}{2} f(\by) = p^*.
   $$
1. This contradicts the fact that $p^*$ is the optimal value for the
   minimization problem.
1. Thus, $X_{\text{opt}}$ must be either empty or a singleton.
1. Thus, the minimization problem has at most one optimal point.
```

## Differentiable Objective Functions

In this subsection, we focus on objective functions of type
$f : \RR^n \to \RR$ which are convex and differentiable.

````{prf:theorem} Optimality criterion for differentiable objective function
:label: res-cvxopt-diff-convex-optimal-criterion

Let $f : \RR^n \to \RR$ be a differentiable convex function. 
Let $C \subseteq \dom f$ be a convex set. 
Consider the minimization problem

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C.
$$
Then, $\bx \in C$ is an optimal point if and only if 

```{math}
:label: eq-cvx-opt-diff-opt-criterion
\nabla f(\bx)^T (\by - \bx) \geq 0 \Forall \by \in C.
```

````

```{prf:proof}
By {prf:ref}`res-cvxf-gradient-convexity-relation`

$$
f(\by) \geq f(\bx) + \nabla f(\bx)^T (\by - \bx)
$$
for every $\bx, \by \in \dom f$.

Assume that some $\bx \in C$ satisfies the optimality criterion
in {eq}`eq-cvx-opt-diff-opt-criterion`.

1. Let $\by \in C$.
1. Then, by differentiability

   $$
   f(\by) \geq f(\bx) + \nabla f(\bx)^T (\by - \bx).
   $$
1. By hypothesis $\nabla f(\bx)^T (\by - \bx) \geq 0$.
1. Thus, $f(\by) \geq f(\bx)$.
1. Since this is true for every $\by \in C$, hence
   $\bx$ is an optimal point for the minimization problem.

Now for the converse, assume that $\bx \in C$ is an optimal point.

1. For contradiction, assume that {eq}`eq-cvx-opt-diff-opt-criterion`
   doesn't hold.
1. Then, there exists $\by \in C$ such that

   $$
   \nabla f(\bx)^T (\by - \bx) < 0.
   $$
1. Let $t \in [0, 1]$ be a parameter.
1. Let $\bz(t) = t \by + (1-t) \bx$.
1. Since $C$ is convex, hence $\bz(t) \in C$.
1. Differentiating $f(\bz(t))$ w.r.t. $t$ at $t=0$, we obtain

   $$
   \left . \frac{d}{d t} f(\bz(t)) \right |_{t=0} = \nabla f(\bx)^T (\by - \bx) < 0.
   $$
1. Thus, for small enough $t$, $f(\bz(t)) < f(\bx)$. 
1. Thus, $\bx$ cannot be an optimal point for the minimization problem.
1. This contradicts our hypothesis that $\bx$ is an optimal point.
1. Hence, {eq}`eq-cvx-opt-diff-opt-criterion` must hold for every $\by \in C$.
```


````{prf:theorem} Optimality criterion for unconstrained problem with differentiable objective function
:label: res-cvxopt-diff-convex-optimal-unconstrained

Let $f : \RR^n \to \RR$ be a differentiable convex function. 
Consider the unconstrained minimization problem

$$
\text{minimize } f(\bx)
$$
Then, $\bx \in \RR^n$ is an optimal point if and only if 
$\nabla f(\bx) = \bzero$.
````

```{prf:proof}
In this case, the set of feasible points is $C = \dom f$.

1. Since $f$ is differentiable, hence $C$ is an open set.
1. By {prf:ref}`res-cvxopt-diff-convex-optimal-criterion`,
   $\bx$ is an optimal point if and only if

   $$
   \nabla f(\bx)^T (\by - \bx) \geq 0 \Forall \by \in C.
   $$
1. If $\nabla f(\bx) = \bzero$, then this inequality is satisfied.
   Hence, $\bx$ must be an optimal point.
1. Now, assume that $\bx$ is an optimal point.
1. Since $\bx \in C$ and $C$ is open, hence there exists
   a closed ball $B[\bx, r] \subseteq C$.
1. Let $\by = \bx - t \nabla f(\bx)$.
1. For sufficiently small $t > 0$, $\by \in B[\bx, r] \subseteq C$.
1. Then, 

   $$
   \nabla f(\bx)^T (\by - \bx)  = \nabla f(\bx)^T (-t  \nabla f(\bx))
   = -t \|  \nabla f(\bx) \|_2^2 \geq 0
   $$
   must hold true for $t > 0$.
1. This means that $\|  \nabla f(\bx) \|_2 \leq 0$ must be true.
1. Thus $\nabla f(\bx) = \bzero$ must be true.
```


```{prf:theorem} Differentiable objective minimization with equality constraints
:label: res-cvxopt-diff-obj-linear-constraints

Let $f : \RR^n \to \RR$ be a differentiable convex function
with $\dom f = \RR^n$.
Consider the minimization problem: 

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bA \bx = \bb
$$
where $\bA \in \RR^{p \times n}$ and $\bb \in \RR^p$ represent
$p$ linear equality constraints.
Assume that the problem is feasible.

Then, $\bx$ is an optimal point for the minimization problem
if and only if there exists a vector $\bv \in \RR^p$ such that

$$
\nabla f (\bx) + \bA^T \bv = \bzero.
$$
```

```{prf:proof}
The feasible set is given by $C = \{ \bx \ST \bA \bx = \bb \}$.
We recall from {prf:ref}`res-cvxopt-diff-convex-optimal-criterion`, that
$\bx$ is an optimal point if and only if
$\nabla f(\bx)^T (\by - \bx) \geq 0 \Forall \by \in C$.

1. Thus, $\bx$ is feasible if and only if
   $\nabla f(\bx)^T (\by - \bx) \geq 0$ for every $\by$ satisfying
   $\bA \by = \bb$.
1. Since both $\bx$ and $\by$ are feasible, hence $\bA (\by - \bx) = \bzero$.
1. Thus, $\bz = \by - \bx \in \NullSpace(\bA)$.
1. In fact, $\by \in C$ if and only if $\by = \bx + \bz$ for some
   $\bz \in \NullSpace(\bA)$. 
1. Thus, the optimality criteria reduces to
   $\nabla f(\bx)^T \bz \geq 0$ for every $\bz \in \NullSpace(\bA)$.
1. Note that $\nabla f(\bx)^T \bz$ is a linear function of $\bz$
   as $\nabla f(\bx)$ is a fixed vector.
1. If a linear function is nonnegative on a subspace, then it must
   be identically zero on the subspace.
1. Thus, $\nabla f(\bx)^T \bz = 0$ for every $\bz \in \NullSpace(\bA)$. 
1. In other words, $\bx$ is optimal if and only if
   $\nabla f(\bx) \perp \NullSpace(\bA)$.
1. Recall that $\NullSpace(\bA)^{\perp} = \ColSpace(\bA^T)$;
   i.e., the null space of $\bA$ is orthogonal complement of the
   column space (range) of $\bA^T$.
1. Thus, $\bx$ is optimal if and only if 
   $\nabla f(\bx) \in \ColSpace(\bA^T)$.
1. In other words, $\bx$ is optimal if and only if there exists
   a vector $\bv \in \RR^p$ such that

   $$
   \nabla f (\bx) + \bA^T \bv = \bzero.
   $$
```

This result is a Lagrange multiplier optimality condition to be
discussed in more detail in later sections.


```{prf:remark} Differentiable objective minimization over nonnegative orthant
:label: rem-cvxopt-diff-obj-nng-orthant


Let $f : \RR^n \to \RR$ be a differentiable convex function
with $\dom f = \RR^n$.
Consider the minimization problem: 

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \succeq \bzero.
$$

1. The feasible set is the nonnegative orthant $\RR^n_+$.
1. $\bx$ is optimal if and only if
   $\bx \succeq \bzero$ and
   $\nabla f (\bx)^T (\by - \bx) \geq 0$ for every $\by \succeq \bzero$.
1. The term $\nabla f (\bx)^T \by$ is unbounded below on $\by \in \RR^n_+$
   unless $\nabla f (\bx) \in \RR^n_+$.
1. Thus, $\nabla f (\bx)$ must be nonnegative. 
1. Then, the minimum value for $\nabla f (\bx)^T \by$ is 0.
1. Consequently, the optimality condition reduces to
   $-\nabla f (\bx)^T \bx \geq 0$
   or $\nabla f (\bx)^T \bx \leq 0$.
1. But $\bx \succeq \bzero$ and $\nabla f (\bx) \succeq \bzero$.
1. Thus, we must have $\nabla f (\bx)^T \bx = 0$.`
1. We note that 

   $$
   \nabla f (\bx)^T \bx = \sum_{i=1}^n (\nabla f (\bx))_i x_i.
   $$
1. Thus, it is a sum of products of nonnegative numbers.
1. So each term in the sum must be 0.
1. Thus, $(\nabla f (\bx))_i x_i = 0$ must hold true for every
   $i=1,\dots,n$.
1. Thus, the optimality condition can be rephrased as

   $$
   \bx \succeq \bzero
   \text{ and }
   \nabla f (\bx) \succeq \bzero
   \text{ and }
   (\nabla f (\bx))_i x_i = 0 \Forall i=1,\dots,n.
   $$

The condition $(\nabla f (\bx))_i x_i = 0$ for every $i$ is known
as *complementarity*. It means that for every $i$ either
$x_i$ or $(\nabla f (\bx))_i$ or both must be 0.
In other words, both $x_i$ and $(\nabla f (\bx))_i$ cannot be
nonzero at the same time.

Thus, the sparsity patterns of $\bx$ and $\nabla f (\bx)$ are
*complementary*. In other words,

$$
\supp (\bx) \cap \supp (\nabla f (\bx)) = \EmptySet
$$
where $\supp (\bx)$ denotes the index set of nonzero entries of $\bx$.
```




## Concave Objective Functions


```{prf:theorem} Minimization of concave function and relative interior
:label: res-cvxopt-concave-min-relint-const

Let $\VV$ be an $n$-dimensional real normed linear space.
Let $f : \VV \to \RR$ be a concave function with $S = \dom f$.
Let $C \subseteq S$ be a convex set.
Consider the problem of minimizing $f$ over $C$.
Let the optimal value be given by

$$
p^* = \inf \{ f(\bx) \ST \bx \in C \}.
$$
Let the set of optimal points for the minimization problem be given by

$$
X_{\text{opt}}  = \{ \bx \in C \ST f(\bx) = p^* \}.
$$
If $X_{\text{opt}}$ contains a
{prf:ref}`relative interior point <def-cvx-relative-interior-point>` of $C$,
then $f$ must be constant over $C$; i.e.,

$$
X_{\text{opt}} = C.
$$
```

```{prf:proof}
Assume that $\bx \in \relint C \cap X_{\text{opt}}$.

1. Let $\by \in C$ be any vector distinct from $\bx$.
1. Since $\bx \in \relint C$, hence
   due to {prf:ref}`res-cvx-relint-line-segment-characterization`,
   there exists $s > 1$ such that
   $\bz = \bx + (s -1) (\bx - \by) \in C$.
   $\bz$ is a point behind $\bx$ on the line from $\by$ to $\bx$ 
   which belongs to $C$.
1. Letting $t = \frac{1}{s}$ we can rewrite it as 

   $$
   \bx =  t \bz + (1-t) \by.
   $$
1. Thus, $\bx$ is a convex combination of $\bz$ and $\by$.
1. By concavity of $f$, we have

   $$
   f(\bx) \geq t f(\bz) + (1-t) f(\by).
   $$
1. Since $\bx$ is an optimal point over $C$ and $\bz, \by \in C$, hence
   $f(\bx) \leq f(\bz)$ and $f(\bx) \leq f(\by)$.
1. Thus,

   $$
   f(\bx) \geq t f(\bz) + (1-t) f(\by)
   \geq t f(\bx) + (1-t) f(\bx) = f(\bx).
   $$
1. This can be true only if $f(\bx) = t f(\bz) + (1-t) f(\by)$
   which in turn implies that $f(\bx) = f(\bz) = f(\by)$.
1. Thus, $f$ must be constant over $C$.
```


```{prf:corollary} Linear functions attain minimum only at boundary points
:label: res-cvxopt-linear-min-relbd

Let $\VV$ be an $n$-dimensional real normed linear space.
Let $f : \VV \to \RR$ be a nonzero linear functional.
Let $C \subseteq \VV$ be a convex set.
Then, $f$ cannot attain a minimum at any relative interior point of $C$.

In other words, $f$ can attain a minimum only at the relative boundary
of $C$ (if it does attain a minimum over $C$).
```

```{prf:proof}
We note that every linear functional is also concave.

1. Let $\bx \in \relint C$.
1. Then, there exists $r > 0$ such that $B(\bx, r) \cap \affine C \subseteq C$.
1. Since $f$ is linear, hence $f$ cannot be constant over $B(\bx, r) \cap \affine C$.
1. Thus, by {prf:ref}`res-cvxopt-concave-min-relint-const`, it cannot
   attain a minimum at $\bx$.
```
