(sec:cvx:cone:2)=
# Cones II

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

```{index} Dual cone
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

\langle \bx , \by \rangle \geq 0 \Forall \bx \in C_2 \implies 
\langle \bx , \by \rangle \geq 0 \Forall \bx \in C_1 \implies
\by \in C_1^*.
$$ 

Thus, $C_2^* \subseteq C_1^*$.
```

```{prf:property} Closedness
:label: res-cvx-dual-cone-closed

A dual cone is a closed set.
```

```{prf:proof}
The dual cone of a set $C$ is given by

$$
C^* = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \geq 0 
    \Forall \bx \in C \}
$$

Fix a $\bx \in C$ and consider the set

$$
H_{\bx} = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \geq 0 \}.
$$

The set $H_{\bx}$ is a closed half space.

We can now see that

$$
C^* =  \bigcap_{\bx \in C} H_{\bx}.
$$
Thus, $C^*$ is an intersection of closed half spaces.
An arbitrary intersection of closed sets is closed.
Hence $C^*$ is closed.
```


```{prf:property} Interior of dual cone
:label: res-cvx-dual-cone-interior

The interior of the dual cone $C^*$ is given by

$$
\interior C^* = \{ \by \in \VV^* \ST \langle \bx , \by \rangle > 0 
    \Forall \bx \in C \setminus \{ \bzero \} \}.
$$
```

```{prf:proof}
Let 

$$
A = \{ \by \ST \langle \bx , \by \rangle > 0 \Forall \bx \in C \setminus \{ \bzero \} \}.
$$

Let $\by \in A$. By definition $\by \in C^*$;
i.e., $A \subseteq C^*$.

Since $\langle \bx , \by \rangle > 0$ for every nonzero $\bx \in C$, 
hence $\langle \bx, \by +\bu  \rangle > 0$ for every nonzero $\bx \in C$ 
and every sufficiently small $\bu$. Hence, $\by \in \interior C^*$.
We have shown that $A \subseteq \interior C^*$.

Now, let $\by \notin A$ but $\by \in C^*$.
Then, $\langle \bx, \by \rangle = 0$ for some nonzero $\bx \in C$. But then

$$
\langle \bx, \by - t\bx \rangle 
= \langle \bx, \by \rangle - t \langle \bx, \bx \rangle < 0
$$
for all $t > 0$. Thus, $\by \notin \interior C^*$. 

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

```{index} Self dual cone
```
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

## Polar Cones

```{index} Polar cone
```
```{prf:definition} Polar cone
:label: def-cvx-polar-cone

Let $\VV$ be a finite dimensional inner product space and $\VV^*$
be its dual space.

Let $C \subseteq \VV$.
Then, its polar cone $C^{\circ}$ is defined as

$$
C^{\circ} \triangleq \{ \by \in \VV^* \ST \langle \bx, \by \rangle \leq 0
\Forall \bx \in C \}.
$$
```

We note that polar cones are just the negative of dual cones.
Thus, they exhibit similar properties as dual cones.


```{prf:example} Polar cone of a ray
:label: ex-cvx-polar-cone-ray

Let $\bx$ be a given nonzero vector.
Let 

$$
C = \cone \{  \bx \}  = \{ t \bx \ST t \geq 0 \}.
$$

1. Let $\by \in C^{\circ}$.
1. Then for every $t \geq 0$, we have $\langle t \bx, \by \rangle \leq 0$.
1. Equivalently, $\langle \bx, \by \rangle \leq 0$ since $t \geq 0$.
1. Hence

   $$
   C^{\circ} = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \leq 0\}.
   $$
1. Also note that $C$ is closed and convex.
1. We shall show later in {prf:ref}`polar cone theorem <res-cvx-polar-cone-theorem>`
   that

   $$
   (C^{\circ})^{\circ} = C.
   $$
1. Hence the polar cone of the set 
   
   $$
   \{ \by \in \VV^* \ST \langle \bx, \by \rangle \leq 0\}
   $$
   is $\cone \{ \bx \}$.
```


### Properties

```{prf:property}
:label: res-cvx-polar-cone-is-cone

Polar cone is a cone.
```

```{prf:proof}

Let $\by \in C^{\circ}$. Then, by definition, 

$$
\langle \bx, \by \rangle \leq 0 \Forall \bx \in C.
$$

Thus, for some $\alpha \geq 0$, 

$$
\langle \bx, \alpha \by \rangle 
= \alpha \langle \bx, \by \rangle \leq 0 \Forall \bx \in C.
$$

Thus, for every $\by \in C^{\circ}$, 
$\alpha \by \in C^{\circ}$ for all $\alpha \geq 0$.
Thus, $C^{\circ}$ is a cone.
```

```{prf:property}
:label: res-cvx-polar-cone-is-convex

Polar cone is convex.
```

```{prf:proof}

Let $\by_1, \by_2 \in C^{\circ}$. Let $t \in [0, 1]$ and

$$
\by = t \by_1 + (1 - t) \by_2.
$$

Then for an arbitrary $\bx \in C$,

$$
\langle \bx, \by \rangle 
= \langle \bx, t \by_1 + (1-t) \by_2 \rangle
= t \langle \bx, \by_1 \rangle + (1-t) \langle \bx, \by_2\rangle \leq 0.
$$

Thus, $\by \in C^{\circ}$.
Thus, $C^{\circ}$ is convex. 
```

We note that polar cone is a convex cone even if the original set $C$
is neither convex nor a cone.


```{prf:property} Containment reversal in polar cone
:label: res-cvx-polar-cone-containment

Let $C_1$ and $C_2$ be two subsets of $\VV$ and let 
$C_1^{\circ}$ and $C_2^{\circ}$ be their corresponding polar cones.
Then,

$$
C_1 \subseteq C_2 \implies C_2^{\circ} \subseteq C_1^{\circ}.
$$
```
The polar cone of the subset contains the polar cone of the superset. 

```{prf:proof}
Let $\by \in C_2^{\circ}$. Then 

$$

\langle \bx , \by \rangle \leq 0 \Forall \bx \in C_2 \implies 
\langle \bx , \by \rangle \leq 0 \Forall \bx \in C_1 \implies
\by \in C_1^{\circ}.
$$ 

Thus, $C_2^{\circ} \subseteq C_1^{\circ}$.
```

```{prf:property} Closedness
:label: res-cvx-polar-cone-closed

A polar cone is a closed set.
```

```{prf:proof}
The polar cone of a set $C$ is given by

$$
C^{\circ} = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \leq 0 
    \Forall \bx \in C \}
$$

Fix a $\bx \in C$ and consider the set

$$
H_{\bx} = \{ \by \in \VV^* \ST \langle \bx, \by \rangle \leq 0 \}.
$$

The set $H_{\bx}$ is a closed half space.

We can now see that

$$
C^{\circ} =  \bigcap_{\bx \in C} H_{\bx}.
$$
Thus, $C^{\circ}$ is an intersection of closed half spaces.
An arbitrary intersection of closed sets is closed.
Hence $C^{\circ}$ is closed.
```


```{prf:property} Interior of polar cone
:label: res-cvx-polar-cone-interior

The interior of the polar cone $C^{\circ}$ is given by

$$
\interior C^{\circ} = \{ \by \in \VV^* \ST \langle \bx , \by \rangle < 0 
    \Forall \bx \in C \setminus \{ \bzero \} \}.
$$
```

```{prf:proof}
Let 

$$
A = \{ \by \ST \langle \bx , \by \rangle < 0 
   \Forall \bx \in C \setminus \{ \bzero \} \}.
$$

Let $\by \in A$. By definition $\by \in C^{\circ}$;
i.e., $A \subseteq C^{\circ}$.

Since $\langle \bx , \by \rangle < 0$ for every nonzero $\bx \in C$, 
hence $\langle \bx, \by +\bu  \rangle < 0$ for every $\bx \in C$ 
and every sufficiently small $\bu$. Hence, $\by \in \interior C^{\circ}$.
We have shown that $A \subseteq \interior C^{\circ}$.

Now, let $\by \notin A$ but $\by \in C^{\circ}$.
Then, $\langle \bx, \by \rangle = 0$ for some nonzero $\bx \in C$. But then

$$
\langle \bx, \by - t\bx \rangle 
= \langle \bx, \by \rangle - t \langle \bx, \bx \rangle > 0
$$
for all $t < 0$. Thus, $\by \notin \interior C^{\circ}$. 

Hence, $A = \interior C^{\circ}$.
```

```{prf:property} Non-empty interior implies pointed polar cone
:label: res-cvx-nonempty-pointed-polar-cone

If $C$ has a non-empty interior, then its polar cone $C^{\circ}$ is pointed.
```

```{prf:proof}
Let $C$ have a non-empty interior and assume that its polar cone $C^{\circ}$ 
is not pointed. Then, there exists a non-zero $\by \in C^{\circ}$ such that
$-\by \in C^{\circ}$ holds too.

Thus, $\langle \bx, \by \rangle \leq 0$ as well as 
$\langle \bx, -\by \rangle \leq 0$ for every $\bx \in C$,
i.e, $\langle \bx, \by \rangle = 0$ for every $\bx \in C$.
But this means that $C$ lies in a hyperplane $H_{\by, 0}$
and hence has an empty interior. 
A contradiction. 
```

```{prf:theorem} Polar cone of a subspace
:label: res-cvx-subspace-polar-cone

The polar cone of a subspace $V \subseteq \VV$ is its
{prf:ref}`orthogonal complement <def-la-orthogonal-complement>` 
$V^{\perp}$ defined as:

$$
V^{\perp} = \{ \by \ST \langle \bv, \by \rangle = 0 \Forall \bv \in V \}.
$$

More precisely, $V^{\circ}$ is isomorphic to $V^{\perp}$ as
the polar cone is a subset of $\VV^*$. 
```

```{prf:proof}
Let $V^{\circ}$ be the polar cone of $V$. If $\bv \in V^{\perp}$, then
by definition, $\bv \in V^{\circ}$. Thus, $V^{\perp} \subseteq V^{\circ}$.

Let us now assume that there is a vector 
$\by \in V^{\circ}$ s.t. $\by \notin V^{\perp}$.

Then, there exists $\bv \in V$ such that  $\langle \bv, \by \rangle < 0$.
Since $V$ is a subspace, it follows that $-\bv \in V$. 
But then  

$$
\langle -\bv, \by \rangle = - \langle \bv, \by \rangle > 0.
$$

Thus, $\by$ cannot belong to $V^{\circ}$. A contradiction.

Thus, $V^{\circ} = V^{\perp}$.
```

```{prf:example} Polar cone of a null space
:label: ex-cvx-polar-cone-nullspace

Let $\bA \in \RR^{m \times n}$ and 
$C = \nullspace \bA$.

1. Recall from linear algebra that

   $$
   (\nullspace \bA)^{\perp} = \range \bA^T.
   $$
1. Hence by {prf:ref}`res-cvx-subspace-polar-cone`,

   $$
   C^{\circ} = C^{\perp} = \range \bA^T.
   $$

We can verify this result easily.

1. Let $\bv \in \range \bA^T$.
1. Then there exists $\bu \in \RR^m$ such that
   $\bv = \bA^T \bu$.
1. For every $\bx \in \nullspace \bA$, we have $\bA \bx = \bzero$.
1. Hence

   $$
   \langle \bx, \bv \rangle
   = \langle \bx, \bA^T \bu \rangle
   = \langle \bA \bx, \bu \rangle
   = \bzero.
   $$
1. Hence $\bv \in (\nullspace \bA)^{\circ}$.
```



```{prf:property} Polar cone and closure
:label: res-cvx-polar-cone-closure

For any nonempty set $C$, we have

$$
C^{\circ} = (\closure C)^{\circ}.
$$
```

```{prf:proof}
We first show that $(\closure C)^{\circ} \subseteq C^{\circ}$.

1. We have $C \subseteq \closure C$.
1. Hence by {prf:ref}`res-cvx-polar-cone-containment`,
   
   $$
   (\closure C)^{\circ} \subseteq C^{\circ}.
   $$

We now show that $C^{\circ} \subseteq (\closure C)^{\circ}$.

1. Let $\by \in C^{\circ}$.
1. Then for every $\bx \in C$, we have $\langle \bx, \by \rangle \leq 0$.
1. Let $\bx \in \closure C$.
1. There exists a sequence $\{ \bx_k \}$ of $C$ such that $\lim \bx_k = \bx$.
1. But $\langle \bx_k, \by \rangle \leq 0$ for every $k$.
1. Hence, taking the limit, we have
   $\langle \bx, \by \rangle \leq 0$.
1. Hence for every $\bx \in \closure C$, we have $\langle \bx, \by \rangle \leq 0$.
1. Hence $\by \in  (\closure C)^{\circ}$.
1. Hence $C^{\circ} \subseteq (\closure C)^{\circ}$.
```

```{prf:property} Polar cone and convex hull
:label: res-cvx-polar-cone-convex-hull

For any nonempty set $C$, we have

$$
C^{\circ} = (\convex C)^{\circ}.
$$
```

```{prf:proof}
We first show that $(\convex C)^{\circ} \subseteq C^{\circ}$.

1. We have $C \subseteq \convex C$.
1. Hence by {prf:ref}`res-cvx-polar-cone-containment`,
   
   $$
   (\convex C)^{\circ} \subseteq C^{\circ}.
   $$

We now show that $C^{\circ} \subseteq (\convex C)^{\circ}$.

1. Let $\by \in C^{\circ}$.
1. Then for every $\bx \in C$, we have $\langle \bx, \by \rangle \leq 0$.
1. Let $\bx \in \convex C$.
1. Then there exist $\bx_1, \dots, \bx_k \in C$ and $t_1, \dots t_k \geq 0$
   with $t_1 + \dots + t_k = 1$ such that

   $$
   \bx = \sum_{i=1}^k t_i \bx_i.
   $$
1. Then 

   $$
   \langle \bx, \by \rangle = \sum_{i=1}^k t_i \langle \bx_i, \by \rangle.
   $$
1. But $\langle \bx_i, \by \rangle \leq 0$ since $\bx_i \in C$ for every $i$.
1. Hence  $\langle \bx, \by \rangle \leq 0$.
1. Hence for every $\bx \in \convex C$, we have $\langle \bx, \by \rangle \leq 0$.
1. Hence $\by \in (\convex C)^{\circ}$.
1. Hence $C^{\circ} \subseteq (\convex C)^{\circ}$.
```

```{prf:property} Polar cone and conic hull
:label: res-cvx-polar-cone-conic-hull

For any nonempty set $C$, we have

$$
C^{\circ} = (\cone C)^{\circ}.
$$
```

```{prf:proof}
We first show that $(\cone C)^{\circ} \subseteq C^{\circ}$.

1. We have $C \subseteq \cone C$.
1. Hence by {prf:ref}`res-cvx-polar-cone-containment`,
   
   $$
   (\cone C)^{\circ} \subseteq C^{\circ}.
   $$

We now show that $C^{\circ} \subseteq (\cone C)^{\circ}$.

1. Let $\by \in C^{\circ}$.
1. Then for every $\bx \in C$, we have $\langle \bx, \by \rangle \leq 0$.
1. Let $\bx \in \cone C$.
1. Then there exist $\bx_1, \dots, \bx_k \in C$ and $t_1, \dots t_k \geq 0$
   such that

   $$
   \bx = \sum_{i=1}^k t_i \bx_i.
   $$
1. Then 

   $$
   \langle \bx, \by \rangle = \sum_{i=1}^k t_i \langle \bx_i, \by \rangle.
   $$
1. But $\langle \bx_i, \by \rangle \leq 0$ since $\bx_i \in C$ for every $i$.
1. Hence  $\langle \bx, \by \rangle \leq 0$.
1. Hence for every $\bx \in \cone C$, we have $\langle \bx, \by \rangle \leq 0$.
1. Hence $\by \in (\cone C)^{\circ}$.
1. Hence $C^{\circ} \subseteq (\cone C)^{\circ}$.
```


```{prf:theorem} Polar cone theorem
:label: res-cvx-polar-cone-theorem

For any nonempty cone $C$, we have

$$
(C^{\circ})^{\circ} = \closure \convex C.
$$

In particular, if $C$ is closed and convex, we have

$$
(C^{\circ})^{\circ} = C.
$$
```

```{prf:proof}
First we assume that $C$ is nonempty, closed and convex
and show that $(C^{\circ})^{\circ} = C$.

1. Pick any $\bx \in C$.
1. By definition, we have
   $\langle \bx, \by \rangle \leq 0$ for every $\by \in C^{\circ}$.
1. Hence $\bx \in (C^{\circ})^{\circ}$.
1. Hence $C \subseteq (C^{\circ})^{\circ}$.
1. Now choose any $\bz \in (C^{\circ})^{\circ}$.
1. Since $C$ is nonempty, closed and convex, hence
   by projection theorem ({prf:ref}`res-cvx-projection-characterization`),
   there exists a unique projection of $\bz$ on $C$,
   denoted by $\widehat{\bz}$ that satisfies

   $$
   \langle \bx - \widehat{\bz}, \bz - \widehat{\bz} \rangle \leq 0 \Forall \bx \in C.
   $$
1. Since $C$ is a cone, hence $\bzero \in C$.
1. Since $C$ is a cone and $\widehat{\bz} \in C$, hence $2 \widehat{\bz} \in C$.
1. By putting $\bx = \bzero$, we get

   $$
   \langle \widehat{\bz}, \bz - \widehat{\bz} \rangle \geq 0.
   $$
1. By putting $\bx =2 \widehat{\bz}$, we get

   $$
   \langle \widehat{\bz}, \bz - \widehat{\bz} \rangle \leq 0.
   $$
1. Together, we have

   $$
   \langle \widehat{\bz}, \bz - \widehat{\bz} \rangle = 0.
   $$
1. Putting this back into the projection inequality, we get

   $$
   \langle \bx, \bz - \widehat{\bz} \rangle \leq 0 \Forall \bx \in C.
   $$
1. Hence $\bz - \widehat{\bz} \in C^{\circ}$.
1. Since $\bz \in (C^{\circ})^{\circ}$, hence
   $\langle \bz, \bz - \widehat{\bz} \langle \leq 0$.
1. We also have $-\langle \widehat{\bz}, \bz - \widehat{\bz} \rangle = 0$.
1. Adding these two, we get

   $$
   \langle \bz - \widehat{\bz}, \bz - \widehat{\bz} \rangle \leq 0.
   $$
1. This means that

   $$
   \| \bz - \widehat{\bz} \|_2^2 \leq 0.
   $$
1. It follows that $\bz  = \widehat{\bz}$.
1. Hence $\bz \in C$.
1. Hence $(C^{\circ})^{\circ} \subseteq C$.

We have so far shown that if $C$ is a nonempty, closed and convex cone then

$$
C = (C^{\circ})^{\circ}.
$$

Now consider the case where $C$ is just an arbitrary nonempty cone.

1. Then $\closure \convex C$ is a closed convex cone.
1. By previous argument

   $$
   \closure \convex C = (\closure \convex C)^{\circ})^{\circ}.
   $$
1. But

   $$
   (\closure \convex C)^{\circ} = (\convex C)^{\circ} = C^{\circ}.
   $$
1. Hence

   $$
   \closure \convex C = (C^{\circ})^{\circ}.
   $$
```


## Normal Cones

```{index} Normal cone; normal vector
```
```{prf:definition} Normal vector
:label: def-cvx-convex-set-normal-vector

Let $S$ be an arbitrary subset of $\VV$.
A vector $\bv \in \VV^*$ is said to be *normal*
to $S$ at a point $\ba \in S$
if $\bv$ does not make an acute angle with
any line segment starting from $\ba$ and ending at some $\bx \in S$;
i.e., if

$$
\langle \bx - \ba, \bv \rangle \leq 0 \Forall \bx \in S.
$$ 
```

```{prf:example} Normal vector
:label: ex-cone-normal-vec-1

Let $C$ be a half space given by:

$$
C  = \{ \bx \ST \langle \bx, \bb \rangle \leq s\}.
$$

Let $\ba$ be any point on the boundary hyperplane of $C$
given by $\langle \ba, \bb \rangle = s$.

Then, $\bb$ is normal to $C$ at $\ba$ since for any $\bx \in C$

$$
\langle \bx - \ba , \bb \rangle 
= \langle \bx, \bb \rangle - \langle \ba, \bb \rangle
\leq s - s = 0.
$$
Note that $\bb$ points opposite to the direction of the
halfspace.
```

```{index} Normal cone
```
```{prf:definition} Normal cone
:label: def-cvx-normal-cone

The set of all vectors normal to a set $S$ at 
a point $\ba \in S$, denoted by $N_S(\ba)$, is called the
*normal cone* to $S$ at $\ba$. 

$$
N_S(\ba) \triangleq \{ \bv \in \VV^* \ST 
   \langle \bx - \ba , \bv \rangle \leq 0 
   \Forall \bx \in S \}.
$$

We customarily define $N_S(\ba) = \EmptySet$ for any $\ba \notin S$.
```


```{prf:property}
:label: res-cvx-normal-cone-convex

A normal cone is always a convex cone.
```

```{prf:proof}
Let $S$ be a subset of $\VV$ and let $\ba \in S$.
Let $N$ denote the set of normal vectors to $S$ at $\ba$.
We have to show that $N$ is a convex cone;
i.e., we have to show that $N$ contains all its conic combinations.

For any $\bx \in S$:

$$
\langle \bx - \ba , \bzero \rangle = 0.
$$

Thus, $\bzero \in N$.

Assume $\bu \in N$. 
Then, 

$$
\langle \bx - \ba, \bu \rangle \leq 0 \Forall \bx \in S.
$$

But then for any $t \geq 0$,

$$
\langle \bx - \ba, t\bu \rangle 
= t \langle \bx - \ba, \bu \rangle
\leq 0 \Forall \bx \in S.
$$
Thus, $t \bu \in N$. Thus, $N$ is closed under
nonnegative scalar multiplication.

Now, let $\bu, \bv \in N$. 
Then,

$$
\langle \bx - \ba, \bu + \bv \rangle 
=  \langle \bx - \ba, \bu \rangle
   + \langle \bx - \ba, \bv \rangle
\leq 0 \Forall \bx \in S.
$$
since sum of two nonpositive quantities is nonpositive. 

Thus, $\bu + \bv \in N$.
Thus, $N$ is closed under vector addition.

Combining these two observations, $N$ is closed
under conic combinations. Hence, $N$ is a convex cone.
```

```{prf:property}
:label: res-cvx-normal-cone-closed

A normal cone is closed.


Specifically, if $N_S(\ba)$ is the normal cone 
to a set $S$ at a point $\ba \in S$,
then:

$$
N_S(\ba) 
= \bigcap_{\bx \in S} 
\{ \bv \in \VV^* \ST \langle \bx - \ba , \bv \rangle \leq 0 \}.
$$
```

```{prf:proof}
For some fixed $\ba \in S$ and any fixed $\bx \in \VV$, define:

$$
H_{-}(\bx - \ba) = \{ \bv \in \VV^* \ST \langle \bx - \ba , \bv \rangle \leq 0 \}.
$$
Note that $H_{-}(\bx - \ba)$ is a closed {prf:ref}`half-space <def-halfspace>`
passing through origin of $\VV^*$ extending opposite to the direction $\bx - \ba$.

Let $\bv \in N_S(\ba)$ be a normal vector to $S$ at $\ba$.

1. Then, for every $\bx \in S$, $\langle \bx - \ba, \bv \rangle \leq 0$.
1. Thus,  for every $\bx \in S$, $\bv \in H_{-}(\bx - \ba)$.
1. Thus, $\bv \in \bigcap_{\bx \in S} H_{-}(\bx - \ba)$.
1. Thus, $N_S(\ba) \subseteq \bigcap_{\bx \in S} H_{-}(\bx - \ba)$.

Going in the opposite direction:

1. Let $\bv \in \bigcap_{\bx \in S} H_{-}(\bx - \ba)$.
1. Then, for every $\bx \in S$, $\bv \in H_{-}(\bx - \ba)$.
1. Thus, for every $\bx \in S$, $\langle \bx - \ba , \bv \rangle \leq 0$.
1. Thus, $\bv$ is a normal vector to $S$ at $\ba$.
1. Thus, $\bv \in N_S(\ba)$.
1. Thus, $\bigcap_{\bx \in S} H_{-}(\bx - \ba) \subseteq N_S(\ba)$.

Combining, we get:

$$
N_S(\ba) = \bigcap_{\bx \in S} H_{-}(\bx - \ba).
$$

Now, since $N_S(\ba)$ is an arbitrary intersection of closed
half spaces which are individually closed sets, hence
$N_S(\ba)$ is closed.

Since each half space is convex and intersection of 
convex sets is convex, hence, as a bonus, this proof also
shows that $N_S(\ba)$ is convex.
```

```{prf:theorem} Normal cone of entire space
:label: res-cvx-normal-cone-vec-space

Let $C = \VV$. We wish to compute the
normal cone $N_C(\bx)$ at every $\bx \in C$.

1. Let $\bv \in N_C(\bx)$.
1. Then we must have

   $$
   \langle \by - \bx, \bv \rangle \leq 0 \Forall \by \in \VV. 
   $$
1. This is equivalent to
   
   $$
   \langle \bz, \bv \rangle \leq 0 \Forall \bz \in \VV.
   $$
1. The only vector that satisfies this inequality is $\bv = \bzero$.
1. Hence $N_C(\bx) = \{ \bzero \}$.
```


```{prf:theorem} Normal cone of unit ball
:label: res-cvxf-normal-cone-unit-ball

$$
N_{B[\bzero, 1]} (\bx) = \{ \by \in \VV^* \ST \| \by \|_* \leq \langle \bx, \by \rangle \}.
$$
```

```{prf:proof}
The unit ball at origin is given by:

$$
S = B[\bzero, 1] = \{\bx \in \VV  \ST \| \bx \| \leq 1 \}.
$$

Consider $\bx \in S$.
Then, $\by \in N_S(\bx)$ if and only if

$$
& \langle \bz - \bx , \by \rangle \leq 0 \Forall \bz \in S\\
& \iff \langle \bz , \by \rangle \leq \langle \bx, \by \rangle \Forall \bz \in S\\
& \iff \underset{\| \bz \|  \leq 1}{\sup} \langle \bz , \by \rangle
\leq \langle \bx, \by \rangle \\
& \iff \| \by \|_* \leq \langle \bx, \by \rangle.
$$

Therefore, for any $\bx \in S$:

$$
N_S(\bx) = \{ \by \in \VV^* \ST \| \by \|_* \leq \langle \bx, \by \rangle \}.
$$
```
