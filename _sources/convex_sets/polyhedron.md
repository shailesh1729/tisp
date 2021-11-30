# Polyhedra

(def:polyhedron)=
````{prf:definition}
A **polyhedron** is defined as the solution set of a finite number of linear inequalities.

$$
    P = \{ x | a_j^T x \leq b_j, j = 1, \dots, M, c_k^T x = d_k, k = 1, \dots, P\}
$$

````

A polyhedron thus is the intersection of a finite number of halfspaces ($M$)
and hyperplanes ($P$).

````{prf:example} Polyhedra

*  Affine sets ( subspaces, hyperplanes, lines)
*  Rays
*  Line segments
*  Halfspaces

````

````{prf:remark}
A polyhedron is a convex set.
````

(def:polytope)=
````{prf:definition}
A bounded polyhedron is known as a **polytope**.

````


We can combine the set of inequalities and equalities in the form of
linear matrix inequalities and equalities.

$$
    P = \{ x | A x \preceq b,  C x = d\}
$$


where

$$
    &A = \begin{bmatrix}
    a_1^T \\
    \vdots \\
    a_M^T
    \end{bmatrix}
    ,
    b = \begin{bmatrix}
    b_1 \\
    \vdots \\
    b_M
    \end{bmatrix}\\
    &C = \begin{bmatrix}
    c_1^T \\
    \vdots\\
    c_P^T
    \end{bmatrix}
    ,
    d = \begin{bmatrix}
    d_1 \\
    \vdots \\
    d_P
    \end{bmatrix}
$$


and the symbol $\preceq$ means **vector inequality** or 
**component wise inequality** in $\RR^M$ i.e. $u \preceq v$
means $u_i \leq v_i$ for $i = 1, \dots, M$.

Note that $b \in \RR^M$, $A \in \RR^{M \times N}$, $A x \in \RR^M$, 
$d \in \RR^P$, $C \in \RR^{P \times N}$ and $C x \in \RR^P$.

````{prf:example} Set of nonnegative numbers
Let $\RR_+  = \{ x \in \RR | x \geq 0\}$. $\RR_+$ is a polyhedron
(a solution set of a single linear inequality). 
Hence, it is a convex set.
Moreover, it is a ray and a convex cone.
````

(def:nonnegative_orthant)=
````{prf:example} Non-negative orthant
We can generalize $\RR_+$ as follows.  Define

$$
    \RR_+^N = \{ x \in \RR^N | x_i \geq 0 , i = 1, \dots , N\}  = \{x \in \RR^N | x \succeq 0 \}.
$$

$\RR_+^N$ is called **nonnegative orthant**. 
It is a polyhedron (solution set of
$N$ linear inequalities). It is also a convex cone.

````

(def:simplex)=
````{prf:definition}
Let $K+1$ points $v_0, \dots, v_K \in \RR^N$ be affine independent
(see {ref}`here <def:affine_independence>`).

The **simplex** determined by them is given by

$$
    C = \ConvexHull \{ v_0, \dots, v_K\}
    = \{ \theta_0 v_0 + \dots + \theta_K v_K | \theta \succeq 0, 1^T \theta = 1\}
$$

where $\theta = [\theta_1, \dots, \theta_K]^T$ and
$1$ denotes a vector of appropriate size $(K)$ with all entries one.

In other words, $C$ is the convex hull of the set $\{v_0, \dots, v_K\}$.

````



