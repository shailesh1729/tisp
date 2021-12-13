# Dual Cones


```{prf:definition} Dual cone
:label: def-dual-cone

Let $C \subset \RR^n$. The set 

$$
C^* \triangleq \{ y \,|\, \langle y, x \rangle \geq 0 \Forall x \in C \}
$$

is called the *dual cone* of $C$. 
```

## Properties

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


```{rubric} Geometric interpretation
```

* For a vector $y$, the set $H_{y, +} \{ x \ST \langle y, x \rangle \geq 0\}$ is 
  a halfspace passing through origin.
* If $y$ belongs to the dual cone of $C$, then for every $x \in C$, we have
  $ \langle y, x \rangle \geq 0$. 
* Thus, the set $C$ is contained in the halfspace $H_{y, +}$.
* In particular, if $C$ is a cone, then it must be supported by the half space $H_{y, +}$ as $C$ contains the $0$ vector.


## Self dual cones

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


