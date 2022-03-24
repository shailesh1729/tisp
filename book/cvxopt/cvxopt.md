# Convex Optimization

## Convex Optimization Problems


```{prf:definition} Convex optimization problem
:label: def-opt-convex-opt-problem

Let $\VV$ be an $n$-dimensional real vector space.
Let $f : \VV \to \RR$ be a convex function
with $S = \dom f$.
Let $C \subseteq S \subseteq \VV$ be a closed and convex set.

A mathematical optimization problem of the form

$$
& \text{minimize }  &  & f(\bx) \\
& \text{subject to } & & \bx \in C
$$
is known as a *convex optimization problem*.
```

```{div}
Recall from {prf:ref}`res-cvx-closed-convex-halfspace-intersection`
that a closed and convex set $C$ is an intersection of all the halfspaces 
that contain it. Let $\{ A_i \}_{i \in I}$ be the set of halfspaces
that contains $C$.
Then, each half space can be written as

$$
A_i = \{ \bx \in \VV \ST  \langle \bx, \ba_i \rangle \leq b_i \}.
$$
Thus, $\bx \in C$ is equivalent to 
$\langle \bx, \ba_i \rangle \leq b_i$ for every $i \in I$.
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
1. The equality constraint functions $h_j: \VV \to \RR$ are affine functions for $j=1,\dots,m$.
1. The function $f_i$ for $i=0,\dots,m$ are {prf:ref}`closed <def-ms-closed-function>`.
````

```{div}

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
1. Recall from {prf:ref}`def-ms-closed-function` that a function is closed
   if all its sublevel sets are closed.
1. In particular, this means that the domain of a closed function is also closed.
1. Thus, $\DDD$ is a closed set.
1. The feasible set $C$ is given by

   $$
   C = \dom f_0 \cap \bigcap_{i=1}^m f_i^{-1}(-\infty, 0] \cap \bigcap_{j=1}^p h_j^{-1}(0).
   $$
1. Then, $f_i^{-1}(-\infty, 0]$ are closed sets since $f_i$ are closed functions.
1. Then, $f_i^{-1}(-\infty, 0]$ are sublevel sets of convex functions hence they
   are also convex sets.
1. By {prf:ref}`res-la-aff-rv-level-set`, the level sets of affine functions are affine sets.
1. Thus, $h_j^{-1}(0)$ is an affine set. Hence, it is a convex set.
1. Since $\VV$ is finite dimensional, hence affine sets are closed.
   Hence $h_j^{-1}(0)$
   is closed for every $j=1,\dots,p$. 
1. Thus, $C$ is an intersection of closed and convex sets. 
1. Thus, $C$ is a closed and convex set. 
1. We note that we can rewrite the standard form as

   $$
   & \text{minimize }  &  & f(\bx) \\
   & \text{subject to } & & \bx \in C
   $$
   to match with {prf:ref}`def-opt-convex-opt-problem`.
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