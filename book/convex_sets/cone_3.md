(sec:cvx:cone:3)=
# Cones III

## Polyhedral Cones

```{index} Polyhedral cone
```
```{prf:definition} Polyhedral cone
:label: def-cvx-polyhedral-cone

The conic hull of a finite set of points is known as
a *polyhedral cone*.

In other words, let $\{ \bx_1, \bx_2, \dots, \bx_m \}$
be a finite set of points. Then

$$
C = \cone \{ \bx_1, \bx_2, \dots, \bx_m \} 
$$ 
is known as a polyhedral cone.
```

```{prf:theorem}
:label: res-cvx-polyhedral-cone-closed-convex

A polyhedral cone is nonempty, closed and convex.
```

```{prf:proof}
Since it is the conic hull of a nonempty set, hence 
it is nonempty and convex.

{prf:ref}`res-cvx-closed-conic-hull` shows that
the conic hulls of a finite set of points are
closed.
```

```{prf:remark} Polyhedral cone alternative formulations
:label: res-cvx-polyhedral-cone-definitions

Following are some alternative definitions of a polyhedral cone.

1. A cone is polyhedral if it is the intersection of a finite
   number of half spaces which have $\bzero$ on their boundary.
1. A cone $C$ is polyhedral if there is some matrix
   $\bA$ such that $C = \{ \bx \in \RR^n \ST \bA \bx \succeq \bzero  \}$.
1. A cone is polyhedral if it is the solution set of a system of 
   homogeneous linear inequalities.
```

### Polar Cones

```{prf:theorem} Polar cone of a polyhedral cone
:label: res-cvx-polar-polyhedral-cone

Let the ambient space by $\RR^n$. Let $\bA \in \RR^{m \times n}$.
Let 

$$
C = \{\bx \in \RR^n \ST \bA \bx \preceq \bzero \}.
$$

Then

$$
C^{\circ}  = \{ \bA^T \bt \ST \bt \in \RR^m_+ \}.
$$
```

We note that the set $C$ is a convex cone. It is known
as the convex polyhedral cone.

```{prf:proof}
We note that $\by \in C^{\circ}$ if and only if 
$\bx^T \by \leq 0$ for every $\bx$ satisfying $\bA \bx \preceq \bzero$.

1. Thus, for every $\bx \in \RR^n$, the statement
   $\bA \bx \preceq \bzero \implies \bx^T \by \leq 0$ is true.
1. By Farkas' lemma ({prf:ref}`res-cvx-farkas-lemma-v3`),
   it is equivalent to the statement that
   there exists $\bt \succeq \bzero$ such that $\bA^T \bt = \by$.
1. Thus, 

   $$
   C^{\circ}  = \{ \bA^T \bt \ST \bt \in \RR^m_+ \}.
   $$
```