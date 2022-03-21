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
form of sublevel and level sets of convex functions. 


