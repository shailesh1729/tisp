# Cones

Throughout this section, $\VV$ is a real vector space. 
Some material is specific to $\RR^n$. Rest of the
material is applicable for any real vector space.

````{prf:definition} Cone
:label: def-cone

A set $C$ is called a *cone* or *nonnegative homogeneous*, 
if for every $\bx \in C$
and $t \geq 0$, we have $t \bx \in C$.
````

* By definition we have $\bzero \in C$.
* Some authors prefer to restrict the definition to $t > 0$
  thus the origin is not included in the cone by default.
* In our definition, a cone always includes the origin.


## Convex cones

````{prf:definition} Convex cone
:label: def-convex-cone

A set $C$ is called a *convex cone* if it is convex and a cone.
In other words, for every $\bx_1, \bx_2 \in C$ and $t_1, t_2 \geq 0$,
we have

$$
    t_1 \bx_1 + t_2 \bx_2 \in C
$$
````


## Conic Combinations

````{prf:definition} Conic combination
:label: def-conic-combination

A point of the form $t_1 \bx_1 + \dots + t_k \bx_k $ with
$t_1 , \dots, t_k \geq 0$ is called a *conic combination*
(or a *non-negative linear combination*) of $\bx_1,\dots, \bx_k$.
````

* A convex cone is closed under non-negative linear/conic combinations.
* One way to prove that a set is a convex cone is to show that it
  contains all its conic combinations.


````{prf:theorem} Convex cone contains all conic combinations
:label: res-cvx-convex-cone-conic-combs

Let $C$ be a convex cone. Then for every $\bx_1, \dots, \bx_k \in C$,
every conic combination $t_1 \bx_1 + \dots + t_k \bx_k $ with
$t_i \geq 0$ belongs to $C$.

Conversely, if a set $C$ contains all conic combinations of its
points, then it is a convex cone.
````

The idea of conic combinations can be generalized to infinite sums
and integrals.

````{prf:example} Convex cones
:label: ex-cvx-convex-cone-examples

*  A ray with its base at origin is a convex cone.
*  A line passing through origin is a convex cone.
*  A plane passing through origin is a convex cone.
*  Any subspace is a convex cone.
````

```{prf:theorem} 
:label: res-cvx-subspace-convex-cone

A subspace is a convex cone.
```

```{prf:proof}
Short proof:

Every subspace contains the $\bzero$ vector. 
Every conic combination is also a linear combination
and a subspace is closed under linear combinations.
Hence, it is also closed under conic combinations.

Detailed proof:

Let $V \subseteq \VV$ be a subspace. We show that it is also 
a convex cone.

Let $\bv_1, \bv_2 \in V$ and $t_1, t_2 \geq 0$, then

$$
\bv = t_1 \bv_1 + t_2 \bv_2
$$
is a linear combination of $\bv_1$ and $\bv_2$. Hence $\bv \in V$. 
Thus, $V$ is a convex cone.
```

## Pointed Cones

```{prf:definition} Pointed cone
:label: def-pointed-cone

A cone $C \subset \VV$ is called pointed if 
$\bx \in C$ and $-\bx \in C$ implies $\bx = \bzero$. 
```
In other words, a pointed cone, doesn't contain a line.

```{prf:example} The nonnegative orthant is a pointed convex cone.
Recall from {prf:ref}`def-convex-nonnegative-orthant`
that the nonnegative orthant is defined as:

$$
\RR_+^n = \{ \bx \in \RR^n \ST x_i \geq 0, \Forall 1 \leq i \leq n \}.
$$
In other words, for $\bx \in \RR^n_+$, every component is non-negative.

Let $\bx, \by \in \RR^n_+$. Let $\alpha, \beta \geq 0$ and consider their 
conic combination

$$
\bz = \alpha \bx + \beta \by.
$$

It is obvious that all components of $\bz$ are also nonnegative. Hence
$\bz \in \RR^n_+$. Thus, $\RR^n_+$ is closed under conic combinations.
Hence, $\RR^n_+$ is a convex cone.

Finally, $\RR^n_+$ is pointed as 
$\bx \in \RR^n_+$ and $-\bx \in \RR^n_+$ both hold true
only if $\bx = \bzero$.
```

## Conic Hulls

````{prf:definition} Conic hull
:label: def-conic-hull

The *conic hull* of a set $S$ is the set of all conic combinations
of points in $S$. i.e.

$$
    \{t_1 \bx_1 + \dots t_k \bx_k \ST \bx_i \in S, t_i \geq 0, i = 1, \dots, k \}.
$$
````

````{prf:theorem}
:label: res-cvx-conic-hull-smallest

Conic hull of a set is the smallest convex cone that contains the set.
````


## Proper Cones

````{prf:definition} Proper cone
:label: def-proper-cone

A cone $K \in \VV$ is called a *proper cone* if it satisfies the following:

*  $K$ is *convex*.
*  $K$ is *closed*.
*  $K$ is *solid*; i.e., it has a nonempty interior.
*  $K$ is *pointed*.
````

```{prf:example} Non-empty interior

Consider the following sets in $\RR^2$:

$$
C_1 = \{ (x_1, x_2) \ST x_1 \geq 0, x_2 = 0\}
$$

$$
C_2 = \{ (x_1, x_2) \ST x_1, x_2 \geq 0\}
$$

Both are closed convex cones. 
$C_1$ doesn't have an interior. All points in $C_1$ are on the 
boundary of $C_1$. 

$C_2$ has a non-empty interior; e.g., the point 
$(1,1) \in C_2$ is not on the boundary.
```


## Norm Cones

````{prf:definition} Norm cone
:label: def-cvx-norm-cone

Let $\|  \cdot \| : \VV \to \RR$ be any norm on $\VV$.
The *norm cone* associated with the norm $\| \cdot \|$ is given by the set

$$
C \triangleq \{ (\bx,t) \ST \| \bx \| \leq t \}
$$
$C$ lies in the product space $\VV \times \RR$.
````

If $\VV = \RR^n$, then a norm cone belongs to $\RR^{n+1}$.

 ````{prf:theorem}
 :label: res-cvx-norm-cone-is-convex

A norm cone is convex. Moreover, it is a convex cone.
````


````{prf:example} Second order cone
:label: ex-cvx-second-order-cone

The second order cone is the norm cone for the Euclidean norm
in the Euclidean space $\RR^n$, i.e.

$$
C  = \{(\bx,t) \ST \| \bx \|_2 \leq t \}.
$$
From definition, $C  \subseteq \RR^{n+1}$.

This can be rewritten as

$$
C = \left \{
\begin{bmatrix}
\bx \\ t
\end{bmatrix}
\middle |
\begin{bmatrix}
\bx \\ t
\end{bmatrix}^T
\begin{bmatrix}
I & 0 \\
0 & -1
\end{bmatrix}
\begin{bmatrix}
\bx \\ t
\end{bmatrix}
\leq 0 , t \geq 0
\right \}
$$
````

## Dual Cones

```{div}
Dual cones are defined for finite dimensional inner product spaces.
Dual cones technically belong to the dual space $\VV^*$.

Recall that the 
{prf:ref}`dual space <def-la-dual-space>`
$\VV^*$ of a vector space $\VV$ is the set
of all linear functionals on $\VV$.
For finite dimensional spaces, $\VV$ and 
its dual $\VV^*$ are isomorphic.
For an inner product space $\VV$ 
every linear functional in $\VV^*$ 
can be identified with a vector $\bv \in \VV$
by the functional $\langle \cdot, \bv \rangle$
({prf:ref}`res-la-ip-dual-space-isomorphism`).
```

```{prf:definition} Dual cone
:label: def-dual-cone
Let $\VV$ be a finite dimensional inner product space and $\VV^*$
be its dual space.

Let $C \subset \VV$. The set 

$$
C^* \triangleq \{ \by \in \VV^* \ST \langle \bx, \by \rangle \geq 0 
    \Forall \bx \in C \}
$$
is called the *dual cone* of $C$ in $\VV^*$. 
```

```{div}
In the Euclidean space $\RR^n$, the dual cone can be written as:

$$
C^* \triangleq \{ \by \in \RR^n \ST \langle \bx, \by \rangle \geq 0 
    \Forall \bx \in C \}.
$$
```


```{rubric} Geometric interpretation
```

* For a vector $\by$, the set 
  $H_{\by, +} \{ \bx \ST \langle \bx, \by \rangle \geq 0\}$ is 
  a {prf:ref}`halfspace <def-halfspace>` passing through origin.
* $\by$ is the normal vector of the halfspace along 
  (in the direction of) the halfspace.
* If $\by$ belongs to the dual cone of $C$, then for every $\bx \in C$, we have
  $ \langle \bx, \by \rangle \geq 0$. 
* Thus, the set $C$ is contained in the halfspace $H_{\by, +}$.
* In particular, if $C$ is a cone, then it will also touch the boundary of 
  the half space $H_{\by, +}$ as $C$ contains the origin.

### Properties

```{prf:property}
:label: res-cvx-dual-cone-is-cone

Dual cone is a cone.
```

```{prf:proof}

Let $\by \in C^*$. Then, by definition, 

$$
\langle \bx, \by \rangle \geq 0 \Forall \bx \in C.
$$

Thus, for some $\alpha \geq 0$, 

$$
\langle \bx, \alpha \by \rangle 
= \alpha \langle \bx, \by \rangle \geq 0 \Forall \bx \in C.
$$

Thus, for every $\by \in C^*$, $\alpha \by \in C^*$ for all $\alpha \geq 0$.
Thus, $C^*$ is a cone.
```

```{prf:property}
:label: res-cvx-dual-cone-is-convex

Dual cone is convex.
```

```{prf:proof}

Let $\by_1, \by_2 \in C^*$. Let $t \in [0, 1]$ and

$$
\by = t \by_1 + (1 - t) \by_2.
$$

Then for an arbitrary $\bx \in C$,

$$
\langle \bx, \by \rangle 
= \langle \bx, t \by_1 + (1-t) \by_2 \rangle
= t \langle \bx, \by_1 \rangle + (1-t) \langle \bx, \by_2\rangle \geq 0.
$$

Thus, $\by \in C^*$.
Thus, $C^*$ is convex. 
```

We note that dual cone is a convex cone even if the original set $C$
is neither convex nor a cone.

```{prf:property} Containment reversal in dual cone
:label: res-cvx-dual-cone-containment

Let $C_1$ and $C_2$ be two subsets of $\VV$ and let 
$C_1^*$ and $C_2^*$ be their corresponding dual cones.
Then,

$$
C_1 \subseteq C_2 \implies C_2^* \subseteq C_1^*.
$$
```
The dual cone of the subset contains the dual cone of the superset. 

```{prf:proof}
Let $\by \in C_2^*$. Then 

$$

\langle \bx , \by \rangle \Forall \bx \in C_2 \implies 
\langle \bx , \by \rangle \Forall \bx \in C_1 \implies
\by \in C_1^*.
$$ 

Thus, $C_2^* \subseteq C_1^*$.
```

```{prf:property} Interior of dual cone
:label: res-cvx-dual-cone-interior

The interior of the dual cone $C^*$ is given by

$$
\interior C^* = \{ \by \in \VV^* \ST \langle \bx , \by \rangle > 0 
    \Forall \bx \in C \}.
$$
```

```{prf:proof}
Let 

$$
A = \{ \by \ST \langle \bx , \by \rangle > 0 \Forall \bx \in C \}.
$$

Let $\by \in A$. By definition $\by \in C^*$. i.e., $A \subseteq C^*$.

Since $\langle \bx , \by \rangle > 0$ for every $\bx \in C$, 
hence $\langle \bx, \by +\bu  \rangle > 0$ for every $\bx \in C$ 
and every sufficiently small $\bu$. Hence, $\by \in \interior C^*$.
We have shown that $A \subseteq \interior C^*$.

Now, let $\by \notin A$ but $\by \in C^*$.
Then, $\langle \bx, \by \rangle = 0$ for some $\bx \in C$. But then

$$
\langle \bx, \by - t\bx \rangle 
= \langle \bx, \by \rangle - t \langle \bx, \bx \rangle < 0
$$
for all $t < 0$. Thus, $\by \notin \interior C^*$. 

Hence, $A = \interior C^*$.
```

```{prf:property} Non-empty interior implies pointed dual cone
:label: res-cvx-nonempty-pointed-dual-cone

If $C$ has a non-empty interior, then its dual cone $C^*$ is pointed.
```

```{prf:proof}
Let $C$ have a non-empty interior and assume that its dual cone $C^*$ 
is not pointed. Then, there exists a non-zero $\by \in C^*$ such that
$-\by \in C^*$ holds too.

Thus, $\langle \bx, \by \rangle \geq 0$ as well as 
$\langle \bx, -\by \rangle \geq 0$ for every $\bx \in C$,
i.e, $\langle \bx, \by \rangle = 0$ for every $\bx \in C$.
But this means that $C$ lies in a hyperplane $H_{\by, 0}$
and hence has an empty interior. 
A contradiction. 
```


```{prf:theorem} Dual cone of a subspace
:label: res-cvx-subspace-dual-cone

The dual cone of a subspace $V \subseteq \VV$ is its
{prf:ref}`orthogonal complement <def-la-orthogonal-complement>` 
$V^{\perp}$ defined as:

$$
V^{\perp} = \{ \by \ST \langle \bv, \by \rangle = 0 \Forall \bv \in V \}.
$$

More precisely, $V^*$ is isomorphic to $V^{\perp}$ as
the dual cone is a subset of $\VV^*$. 
```

```{prf:proof}
Let $V^*$ be the dual cone of $V$. If $\bv \in V^{\perp}$, then
by definition, $\bv \in V^*$. Thus, $V^{\perp} \subseteq V^*$.

Let us now assume that there is a vector 
$\by \in V^*$ s.t. $\by \notin V^{\perp}$.

Then, there exists $\bv \in V$ such that  $\langle \bv, \by \rangle > 0$.
Since $V$ is a subspace, it follows that $-\bv \in V$. 
But then  

$$
\langle -\bv, \by \rangle = - \langle \bv, \by \rangle < 0.
$$

Thus, $\by$ cannot belong to $V^*$. A contradiction.

Thus, $V^* = V^{\perp}$.
```

### Self Dual Cones

```{prf:definition} Self dual cone
:label: def-self-dual-cone

A cone $C$ is called self dual if $C^* = C$, i.e., it is its own dual cone.

By equality, we mean that the dual cone $C^*$ is isomorphic to $C$
since technically $C^* \subseteq \VV^*$.
```

```{prf:example} Nonnegative orthant
:label: ex-nonnegative-orthant-self-dual

The non-negative orthant $\RR^n_+$ is self dual.

Let $C = \RR^n_+$. For some $\bu, \bv \in C$,  $\langle \bu, \bv \rangle \geq 0$. 
Thus, $\RR^n_+ \subseteq C^*$.

Now, for some $\bv \notin \RR^n_+$, there is at least one component which is negative.
Without loss of generality, assume that the first component $v_1 < 0$. 

Now consider the vector $\bu = [1, 0, \dots, 0] \in \RR^n_+$. 
$\langle \bv, \bu \rangle < 0$. Thus, $\bv \notin C^*$. 

Thus, $C^* = \RR^n_+$. It is self dual.
```


```{prf:example} Positive semidefinite cone
:label: ex-psd-cone-self-dual

The positive semi-definite cone $\SS^n_+$ is self dual.

Let $C = \SS^n_+$ and $\bY \in C$. We first show that $\bY \in C^*$.

Choose an arbitrary $\bX \in C$.  
Express $\bX$ in terms of its eigenvalue 
decomposition as 

$$
\bX = \sum \lambda_i \bq_i \bq_i^T.
$$  

Since $\bX$ is PSD, hence, $ \lambda_i \geq 0$. 

Then, 

$$
\begin{aligned}
\langle \bY, \bX \rangle 
&= \Trace (\bX \bY) = \Trace (\bY \bX) \\
&= \Trace \left ( \bY \sum \lambda_i \bq_i \bq_i^T \right )\\
&= \sum \lambda_i \Trace \left (\bY \bq_i \bq_i^T \right) \\
&= \sum \lambda_i \Trace \left(\bq_i^T \bY \bq_i \right)\\
&= \sum \lambda_i (\bq_i^T \bY \bq_i).
\end{aligned}
$$

But since $\bY$ is PSD, 
hence $\bq_i^T \bY \bq_i \geq 0$. 
Hence $\langle \bY, \bX \rangle \geq 0$.
Thus, $\bY \in C^*$.

Now, suppose $\bY \notin \SS^n_+$. 
Then there exists a vector $\bv \in \RR^n$
such that $\bv^T \bY \bv < 0$. 
Consider the PSD matrix $\bV = \bv \bv^T$. 

$$
\langle \bY, \bV \rangle 
= \Trace(\bV\bY) = \Trace (\bv \bv^T \bY) 
= \Trace (\bv^T \bY \bv) < 0.
$$

Thus, $\bY \notin C^*$.

This completes the proof that $C^* = C = \SS^n_+$,
i.e., the positive semi-definite cone is self dual.
```


