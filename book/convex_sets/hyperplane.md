(sec:convex:hyperplane)=
# Hyperplanes and Half spaces

## hyperplanes

In this section $\VV$ is a real inner product space.

````{prf:definition} Hyperplane
:label: def-hyperplane

A *hyperplane*  is a set of the form

$$
       H_{\ba, b} =  \{ x : \langle \ba, \bx \rangle = b \}
$$
where $\ba \in \VV, \ba \neq \bzero$ and $b \in \RR$.
The vector $\ba$ is called the *normal vector* to the hyperplane.
````


*  Algebraically, it is a solution set of a 
   nontrivial linear equation. 
   Thus, it is an affine set.
*  Geometrically, it is a set of points with a 
   constant inner product to a given vector $\ba$.

```{prf:theorem} Hyperplane second form
Let $\bx_0$ be an arbitrary element in $H_{\ba, b}$. Then

$$
H_{\ba, b} = \{ \bx \ST \langle a, \bx-\bx_0 \rangle = 0\}.
$$ 
```

```{prf:proof}
Given $\bx_0 \in H$,

$$
             &\langle \ba, \bx_0 \rangle = b\\
    \implies &\langle \ba, \bx \rangle = \langle \ba, \bx_0 \rangle \Forall \bx \in H\\
    \implies &\langle \ba, \bx - \bx_0 \rangle = 0 \Forall \bx \in H\\
    \implies &H = \{ \bx \ST \langle a, \bx-\bx_0 \rangle = 0\}.
$$
```

Recall that 
{prf:ref}`orthogonal complement <def-la-orthogonal-complement-vector>`
of $\ba$ is defined as

$$
a^{\perp} = \{ \bv \in \VV \ST  \ba \perp \bv \};
$$
i.e., the set of all vectors that are orthogonal to $\ba$.

```{prf:theorem} Hyperplane third form
Let $\bx_0$ be an arbitrary element in $H_{\ba, b}$. Then

$$
H_{\ba, b} = \bx_0 + \ba^{\perp}.
$$
```

```{prf:proof}
Consider the set

$$
S = \bx_0 + \ba^{\perp}. 
$$

Every element  $\bx \in S$
can be written as $\bx = \bx_0 + \bv$ 
such that $\langle \bv, \ba \rangle = 0$.
Thus,

$$
\langle \bx , \ba \rangle = \langle \bx_0 , \ba \rangle = b. 
$$

Thus, $S \subseteq H$.

For any $\bx \in H$:

$$
\langle \ba, \bx - \bx_0 \rangle = b - b = 0. 
$$
Thus, $\bx - \bx_0 \in \ba^{\perp}$. 
Thus, $\bx \in \bx_0 + \ba^{\perp} = S$.
Thus, $H \subseteq S$.

Combining:

$$
H = S = \bx_0 + \ba^{\perp}. 
$$
```
Thus, the hyperplane consists of an offset $\bx_0$ plus 
all vectors orthogonal to the (normal) vector $\ba$.

```{prf:observation}
A hyperplane is an {prf:ref}`affine subspace <def-affine-subspace>`
since $\ba^{\perp}$ is a linear subspace and 
$H$ is the linear subspace plus an offset $\bx_0$.
```

## Half spaces

````{prf:definition} halfspace
:label: def-halfspace

A hyperplane divides $\VV$ into two *halfspaces*.
The two (closed) halfspaces are given by

$$
    H_+ = \{ \bx : \langle \ba, \bx \rangle \geq b \}
$$

and

$$
    H_- = \{ \bx : \langle \ba, \bx \rangle \leq b \}
$$

The halfspace $H_+$ extends in the direction of $\ba$ while
$H_-$ extends in the direction of $-\ba$.
````


*  A halfspace is the solution set of one (nontrivial) linear inequality.
*  The halfspace can be written alternatively as 

$$
    H_+  = \{ \bx \ST \langle \ba, \bx - \bx_0 \rangle \geq 0\}\\
    H_-  = \{ \bx \ST \langle \ba, \bx - \bx_0 \rangle \leq 0\}
$$


where $\bx_0$ is any point in the associated hyperplane $H$.
*  Geometrically, points in $H_+$ make an acute angle with $\ba$ 
   while points in $H_-$ make an obtuse angle with $\ba$.


````{prf:definition} Open halfspace
:label: def-open-halfspace
The sets given by

$$
    \Interior{H_+} = \{ \bx | \langle \ba, \bx \rangle > b\}\\
    \Interior{H_-} = \{ \bx | \langle \ba, \bx \rangle < b\}
$$

are called *open halfspaces*. They are the interior
of corresponding closed halfspaces.
````
