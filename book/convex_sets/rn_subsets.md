# Convex Subsets of $\RR^n$

This section focuses on important convex subsets of $\RR^n$.


```{prf:definition} Nonnegative orthant
:label: def-convex-nonnegative-orthant

The *nonnegative orthant* denoted by $\RR_+^n$ is defined as:

$$
\RR_+^N \triangleq \{ \bx \in \RR^n \ST x_i \geq 0 , i = 1, \dots , n\}  
= \{\bx \in \RR^n \| x \succeq \bzero \}.
$$
```

```{prf:definition} Positive orthant
:label: def-convex-positive-orthant

The *positive orthant* denoted by $\RR_{++}^n$ is defined as:

$$
\RR_{++}^N \triangleq \{ \bx \in \RR^n \ST x_i > 0 , i = 1, \dots , n\}  
= \{\bx \in \RR^n \| x \succ \bzero \}.
$$
```

## Simplex

````{prf:definition} $k$-simplex
:label: def-convex-simplex

Let $k+1$ points $\bv_0, \dots, \bv_k \in \RR^n$ be 
{prf:ref}`affine independent <def-affine-independence>`.

The *simplex* determined by them is given by

$$
C = \ConvexHull \{ \bv_0, \dots, \bv_k\}
= \{ t_0 \bv_0 + \dots + t_k \bv_k \ST 
    \bt \succeq 0, \bone^T \bt = 1\}
$$

where $\bt = [t_1, \dots, t_k]^T$ and
$\bone$ denotes a vector of appropriate size $(k)$ 
with all entries one.

In other words, $C$ is the convex hull of the set 
$\{\bv_0, \dots, \bv_k\}$.
````
A simplex is a convex set since it is a convex hull of its vertices.

```{prf:example}

* A 0-simplex is a point.
* A 1-simplex is a line segment.
* A 2-simplex is a triangle.
* A 3-simplex is a tetrahedron.
* A 4-simplex is a 5-cell.
```

```{prf:definition} Regular simplex
:label: def-convex-regular-simplex

A *regular simplex* is the set of nonnegative vectors with elements
summing up to $a$. 

$$
\Delta_a \triangleq \{\bx \in \RR^n \ST 
    \langle \bx, \bone \rangle = a, \bx \succeq \bzero \}.
$$
```

```{prf:definition} Unit simplex
:label: def-convex-unit-simplex

A *unit simplex* is the set of nonnegative vectors with elements
summing up to $1$. 

$$
\Delta \triangleq \{\bx \in \RR^n 
    \ST \langle \bx, \bone \rangle = 1, \bx \succeq \bzero \}.
$$
```


## Polyhedra

````{prf:definition} Polyhedron
:label: def-convex-polyhedron

A *polyhedron* is defined as the solution set of a finite number of linear inequalities.

$$
    P = \{ \bx | \langle \ba_j, \bx \rangle \leq b_j, j = 1, \dots, m,
     \langle \bc_k, \bx \rangle = d_k, k = 1, \dots, p\}
$$
````

A polyhedron thus is the intersection of a finite number of halfspaces ($m$)
and hyperplanes ($p$).

````{prf:example} Polyhedra

*  Affine sets ( subspaces, hyperplanes, lines)
*  Rays
*  Line segments
*  Halfspaces
````

````{prf:theorem}
A polyhedron is a convex set.
````
```{prf:proof}
Intersection of convex sets is convex.
```

````{prf:definition} Polytope
:label: def-convex-polytope

A bounded polyhedron is known as a *polytope*.
````


We can combine the set of inequalities and equalities in the form of
linear matrix inequalities and equalities.

$$
P = \{ \bx \ST \bA \bx \preceq \bb,  \bC \bx = \bd\}
$$


where

$$
&\bA = \begin{bmatrix}
\ba_1^T \\
\vdots \\
\ba_m^T
\end{bmatrix}
,
\bb = \begin{bmatrix}
b_1 \\
\vdots \\
b_m
\end{bmatrix}\\
&\bC = \begin{bmatrix}
\bc_1^T \\
\vdots\\
\bc_p^T
\end{bmatrix}
,
\bd = \begin{bmatrix}
d_1 \\
\vdots \\
d_p
\end{bmatrix}
$$


and the symbol $\preceq$ means *vector inequality* or 
*component wise inequality* in $\RR^m$ i.e. $\bu \preceq \bv$
means $u_i \leq v_i$ for $i = 1, \dots, m$.

Note that $\bb \in \RR^m$, $\bA \in \RR^{m \times n}$, $\bA \bx \in \RR^m$, 
$\bd \in \RR^p$, $\bC \in \RR^{p \times n}$ and $\bC \bx \in \RR^p$.

````{prf:example} Set of nonnegative numbers
Let $\RR_+  = \{ x \in \RR | x \geq 0\}$. $\RR_+$ is a polyhedron
(a solution set of a single linear inequality). 
Hence, it is a convex set.
Moreover, it is a ray and a convex cone.
````

````{prf:example} Nonnegative orthant
The nonnegative orthant $\RR_+^n$ 
is a polyhedron (solution set of
$n$ linear inequalities). 
It is also a convex cone.
````



## Euclidean Balls

````{prf:definition} Euclidean ball
:label: def-euclidean-ball

A *Euclidean closed ball* (or just ball) in $\RR^n$ has the form

$$
B[\bx_c, r] \triangleq \{ \bx \ST \|  \bx - \bx_c\|_2 \leq r \} 
= \{\bx \ST (\bx - \bx_c)^T (\bx  - \bx_c) \leq r^2 \}
$$
where $r > 0$ and $ \| \cdot \|_2$ denotes the Euclidean norm.
$\bx_c$ is the *center* of the ball.
$r$ is the *radius* of the ball.
````

```{div}
An equivalent expression is given by

$$
B = \{\bx_c +  r \bu \, | \, \| \bu \|_2 \leq 1  \}.
$$
```
A Euclidean ball is a convex set.

## Ellipsoids

````{prf:definition}
:label: def-convex-ellipsoid

An *ellipsoid* is a set of the form

$$
\xi = \{\bx \ST (\bx - \bx_c)^T \bP^{-1} (\bx - \bx_c) \leq 1\}
$$
where $\bP = \bP^T \succ 0$;
i.e., $\bP$ is symmetric and positive definite.

The vector $\bx_c \in \RR^n$ is the *centroid* of the ellipse.

Eigen values of the matrix $\bP$ (which are all positive) determine
how far the ellipsoid extends in every direction from $\bx_c$.

The lengths of semi-axes of $\xi$ are given by $\sqrt{\lambda_i}$
where $\lambda_i$ are the eigen values of $\bP$.
````

 ````{prf:remark}
 A Euclidean ball is an ellipsoid with $\bP = r^2 I$.
````

```{div}
An alternative representation of an ellipsoid is given by

$$
\xi = \{\bx_c + \bA \bu | \| \bu\|_2 \leq 1 \}
$$
where $\bA$ is a square and nonsingular matrix.

To show the equivalence of the two definitions, we proceed as follows.

Let $\bP = \bA \bA^T$. Let $\bx$ be any arbitrary element in $\xi$.

Then $\bx - \bx_c = \bA \bu$ for some $\bu$ such that $\| \bu \|_2 \leq 1$.

Thus

$$
&(\bx - \bx_c)^T \bP^{-1} (\bx - \bx_c) =  (\bA \bu)^T (\bA \bA^T)^{-1} (\bA \bu)\\ 
&= \bu^T \bA^T (\bA^T)^{-1} \bA^{-1} \bA \bu = \bu^T \bu\\
&= \| \bu \|_2^2 \leq 1.
$$
The two representations of an ellipsoid are therefore equivalent.

````{prf:remark}
An ellipsoid is a convex set.
````
