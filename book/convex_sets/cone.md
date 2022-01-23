# Cones

````{prf:definition} Cone
:label: def-cone

A set $C$ is called a *cone* or *nonnegative homogeneous*, if for every $x \in C$
and $\theta \geq 0$, we have $\theta x \in C$.

````

By definition we have $0 \in C$.


## Convex cones

````{prf:definition} Convex cone
:label: def-convex-cone

A set $C$ is called a *convex cone* if it is convex and a cone.
In other words, for every $x_1, x_2 \in C$ and $\theta_1, \theta_2 \geq 0$,
we have

$$
    \theta_1 x_1 + \theta_2 x_2 \in C
$$
````


````{prf:definition} Conic combination
:label: def-conic-combination

A point of the form $\theta_1 x_1 + \dots + \theta_k x_k $ with
$\theta_1 , \dots, \theta_k \geq 0$ is called a *conic combination*
(or a *non-negative linear combination*) of $x_1,\dots, x_k$.

````

````{prf:remark}
Let $C$ be a convex cone. Then for every $x_1, \dots, x_k \in C$,
a conic combination $\theta_1 x_1 + \dots + \theta_k x_k $ with
$\theta_i \geq 0$ belongs to $C$.

Conversely if a set $C$ contains all conic combinations of its
points, then it is a convex cone.
````

The idea of conic combinations can be generalized to infinite sums
and integrals.

````{prf:example} Convex cones

*  A ray with its base at origin is a convex cone.
*  A line passing through zero is a convex cone.
*  A plane passing through zero is a convex cone.
*  Any subspace is a convex cone.

````

```{prf:example} A subspace is a convex cone

Let $V \subseteq \RR^n$ be a subspace. We show that it is also 
a convex cone.

Let $v_1, v_2 \in V$ and $\theta_1, \theta_2 \geq 0$, then

$$
v = \theta_1 v_1 + \theta_2 v_2
$$

is a linear combination of $v_1$ and $v_2$. Hence $v \in V$. 
Thus, $V$ is a convex cone.
```

## Pointed cones

```{prf:definition} Pointed cone
:label: def-pointed-cone

A cone $C \subset \RR^n$ is called pointed if $x \in C$ and $-x \in C$ implies $x = 0$. 
```
In other words, a pointed cone, doesn't contain a line.

```{prf:definition} Nonnegative orthant
:label: def-nonnegative-orthant

The nonnegative orthant is defined as:

$$
\RR^n_+ \triangleq \{ x \in \RR^n \ST x_i \geq 0, \Forall 1 \leq i \leq n \}.
$$
In other words, for $x \in \RR^n_+$, every component is non-negative.
```

```{prf:example} The nonnegative orthant is a pointed convex cone.

Let $x, y \in \RR^n_+$. Let $\alpha, \beta \geq 0$ and consider their 
conic combination

$$
z = \alpha x + \beta y.
$$

It is obvious that all components of $z$ are also nonnegative. Hence
$z \in \RR^n_+$. Thus, $\RR^n_+$ is closed under conic combinations.
Hence, $\RR^n_+$ is a convex cone.

Finally, $\RR^n_+$ is pointed as for any $x \in \RR^n_+$, $-x \in \RR^n_+$
only if $x = 0$.
```

## Conic hulls

````{prf:definition} Conic hull
:label: def-conic-hull

The *conic hull* of a set $S$ is the set of all conic combinations
of points in $S$. i.e.

$$
    \{\theta_1 x_1 + \dots \theta_k x_k | x_i \in S, \theta_i \geq 0, i = 1, \dots, k \}
$$

````

````{prf:remark}
Conic hull of a set is the smallest convex cone that contains the set.
````


## Proper cones

````{prf:definition} Proper cone
:label: def-proper-cone

A cone $K \in \RR^N$ is called a *proper cone* if it satisfies the following:

*  $K$ is *convex*.
*  $K$ is *closed*.
*  $k$ is *solid* i.e. it has a nonempty interior.
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

$C_2$ has a non-empty interior. e.g., the point 
$(1,1) \in C_2$ is not on the boundary.
```


## Norm Cones

(def:norm_cone)=
````{prf:definition}
Let $\|  \cdot \| : \RR^N \to R$ be any norm on $\RR$.
The **norm cone** associated with the norm $\| \cdot \|$ is given by the set

$$
    C = \{ (x,t) \;|\; \| x \| \leq t \} \subseteq \RR^{N+1}
$$

````

 ````{prf:remark}
 A norm cone is convex. Moreover it is a convex cone.
````


(ex:second_order_cone)=
````{prf:example} Second order cone
The second order cone is the norm cone for the Euclidean norm, i.e.

$$
    C  = \{(x,t) \;|\; \| x \|_2 \leq t \} \subseteq \RR^{N+1}
$$

This can be rewritten as

$$
    C = \left \{
    \begin{bmatrix}
    x \\ t
    \end{bmatrix}
    \middle |
    \begin{bmatrix}
    x \\ t
    \end{bmatrix}^T
    \begin{bmatrix}
    I & 0 \\
    0 & -1
    \end{bmatrix}
    \begin{bmatrix}
    x \\ t
    \end{bmatrix}
    \leq 0 , t \geq 0
    \right \}
$$
````

## Dual Cones


```{prf:definition} Dual cone
:label: def-dual-cone

Let $C \subset \RR^n$. The set 

$$
C^* \triangleq \{ y \,|\, \langle y, x \rangle \geq 0 \Forall x \in C \}
$$

is called the *dual cone* of $C$. 
```

```{rubric} Geometric interpretation
```

* For a vector $y$, the set $H_{y, +} \{ x \ST \langle y, x \rangle \geq 0\}$ is 
  a {prf:ref}`halfspace <def-halfspace>` passing through origin.
* $y$ is the normal vector of the halfspace along (in the direction of) the halfspace.
* If $y$ belongs to the dual cone of $C$, then for every $x \in C$, we have
  $ \langle y, x \rangle \geq 0$. 
* Thus, the set $C$ is contained in the halfspace $H_{y, +}$.
* In particular, if $C$ is a cone, then it will also touch the boundary of 
  the half space $H_{y, +}$ as $C$ contains the zero vector.



### Properties

```{prf:property}
Dual cone is a cone.
```

```{prf:proof}

Let $y \in C^*$. Then, by definition, 

$$
\langle y, x \rangle \geq 0 \Forall x \in C.
$$

Thus, for some $\alpha \geq 0$, 

$$
\langle \alpha y, x \rangle = \alpha \langle y, x \rangle \geq 0 \Forall x \in C.
$$

Thus, for every $y \in C^*$, $\alpha y \in C^*$ for all $\alpha \geq 0$.
Thus, $C^*$ is a cone.
```

```{prf:property}
Dual cone is convex.
```

```{prf:proof}

Let $y_1, y_2 \in C^*$. Let $\theta \in [0, 1]$ and

$$
y = \theta y_1 + (1 - \theta) y_2.
$$

Then for an arbitrary $x \in C$,

$$
\langle y, x \rangle = \langle \theta y_1 + (1-\theta) y_2, x \rangle
= \theta \langle y_1, x \rangle + (1-\theta) \langle y_2, x \rangle \geq 0.
$$

Thus, $y \in C^*$. 
```

We note that dual cone is a convex cone even if the original set $C$
is neither convex nor a cone.

```{prf:property}
Let $C_1$ and $C_2$ be two subsets of $\RR^n$ and let 
$C_1^*$ and $C_2^*$ be their corresponding dual cones.
Then,

$$
C_1 \subseteq C_2 \implies C_2^* \subseteq C_1^*.
$$
```
The dual cone of the subset contains the dual cone of the superset. 

```{prf:proof}
Let $y \in C_2^*$. Then 

$$

\langle y , x \rangle \Forall x \in C_2 \implies 
\langle y , x \rangle \Forall x \in C_1 \implies
y \in C_1^*.
$$ 

Thus, $C_2^* \subseteq C_1^*$.
```

```{prf:property}
The interior of the dual cone $C^*$ is given by

$$
\interior C^* = \{ y \ST \langle y , x \rangle > 0 \Forall x \in C \}.
$$
```

```{prf:proof}
Let 

$$
A = \{ y \ST \langle y , x \rangle > 0 \Forall x \in C \}
$$

Let $y \in A$. By definition $y \in C^*$. i.e., $A \subseteq C^*$.

Since $\langle y , x \rangle > 0$ for every $x \in C$, 
hence $\langle y +u , x \rangle > 0$ for every $x \in C$ 
and every sufficiently small $u$. Hence, $y \in \interior C^*$.
We have shown that $A \subseteq \interior C^*$.

Now, let $y \notin A$ but $y \in C^*$.
Then, $\langle y, x \rangle = 0$ for some $x \in C$. But then
$\langle y - tx, x \rangle = \langle y, x \rangle - t \langle x, x \rangle < 0$
for all $t < 0$. Thus, $y \notin \interior C^*$. 

Hence, $A = \interior C^*$.
```

```{prf:property}
If $C$ has a non-empty interior, then its dual cone $C^*$ is pointed.
```

```{prf:proof}
Let $C$ have a non-empty interior and assume that its dual cone $C^*$ 
is not pointed. Then, there exists a non-zero $y \in C^*$ such that
$-y \in C^*$ holds too.

Thus, $\langle y, x \rangle \geq 0$ as well as 
$\langle -y, x \rangle \geq 0$ for every $x \in C$,
i.e, $\langle y, x \rangle = 0$ for every $x \in C$.
But this means that $C$ lies in a hyperplane and hence has an empty interior. 
A contradiction. 
```


```{prf:proposition} Dual cone of a subspace
The dual cone of a subspace $V \subseteq \RR^n$ is its orthogonal
complete $V^{\perp}$ defined as:

$$
V^{\perp} = \{ y \ST \langle y, v \rangle = 0 \Forall v \in V \}.
$$
```

```{prf:proof}
Let $V^*$ be the dual cone of $V$. If $v \in V^{\perp}$, then
by definition, $v \in V^*$. Thus, $V^{\perp} \subseteq V^*$.

Let us now assume that there is a vector $y \in V^*$ s.t. $y \notin V^{\perp}$.

Then, there exists $v \in V$ such that  $\langle y, v \rangle > 0$.
Since $V$ is a subspace, it follows that $-v \in V$. 
But then  

$$
    \langle y, -v \rangle < 0 = - \langle y, v \rangle < 0
$$

Thus, $y$ cannot belong to $V^*$. A contradiction.

Thus, $V^* = V^{\perp}$.
```



### Self Dual Cones

```{prf:definition} Self dual cone
:label: def-self-dual-cone

A cone $C$ is called self dual if $C^* = C$, i.e., it is its own dual cone.
```

```{prf:example}

The non-negative orthant $\RR^n_+$ is self dual.

Let $C = \RR^n_+$. For some $u, v \in C$,  $\langle u, v \rangle \geq 0$. 
Thus, $\RR^n_+ \subseteq C^*$.

Now, for some $v \notin \RR^n_+$, there is at least one component which is negative.
Without loss of generality, assume that the first component $v_1 < 0$. 

Now consider the vector $u = [1, 0, \dots, 0] \in \RR^n_+$. 
$\langle v, u \rangle < 0$. Thus, $v \notin C^*$. 

Thus, $C^* = \RR^n_+$. It is self dual.
```


```{prf:example}
The positive semi-definite cone $\SS^n_+$ is self dual.

Let $C = \SS^n_+$ and $Y \in C$. We first show that $Y \in C^*$.

Choose an arbitrary $X \in C$.  Express $X$ in terms of its eigenvalue 
decomposition as 

$$
X = \sum \lambda_i q_i q_i^T.
$$  

Since $X$ is PSD, hence, $ \lambda_i \geq 0$. 

Then, 

$$
\begin{aligned}
\langle Y, X \rangle 
&= \Trace (X Y) = \Trace (Y X) \\
&= \Trace \left ( Y \sum \lambda_i q_i q_i^T \right )\\
&= \sum \lambda_i \Trace \left (Y q_i q_i^T \right) \\
&= \sum \lambda_i \Trace \left(q_i^T Y q_i \right)\\
&= \sum \lambda_i (q_i^T Y q_i).
\end{aligned}
$$

But since $Y$ is PSD, hence $q_i^T Y q_i \geq 0$. Hence $\langle Y, X \rangle \geq 0$.
Thus, $Y \in C^*$.

Now, suppose $Y \notin \SS^n_+$. Then there exists a vector $v \in \RR^n$
such that $v^T Y v < 0$. Consider the PSD matrix $V = v v^T$. 

$$
\langle Y, V \rangle = \Trace(VY) = \Trace (v v^T Y) = \Trace (v^T Y v) < 0.
$$

Thus, $Y \notin C^*$.

This completes the proof that $C^* = C = \SS^n_+$,
i.e., the positive semi-definite cone is self dual.
```


