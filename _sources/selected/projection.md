# Projection onto Convex Set

```{div}
We will assume $\EE$ to be Euclidean space with
an inner product $\langle \cdot, \cdot \rangle$ 
, an induced norm $\| \cdot \|$ and corresponding
dual norm $\| \cdot \|_*$ for the dual space $\EE^*$.
```

## Orthogonal Projection

Let $C \subseteq \EE$ be a nonempty closed and convex set.
The *orthogonal projection* mapping is defined by:

$$
P_C(\bx) \triangleq \underset{\by \in C}{\argmin} \| \by - \bx \| 
\Forall \bx \in \EE. 
$$
The mapping $P_C$ is well defined (exists and unique) when
the underlying set $C$ is nonempty, closed and convex.

## Distance Function

The distance of a point $\bx \in \EE$ from the set $C$ is defined as

$$
d_C(\bx) \triangleq \underset{\by \in C}{\min} \| \bx - \by \|
= \| \bx - P_C(\bx) \|.
$$


## Squared Distance Function

Let $\varphi_C : \EE \to \RR$ be defined as:

$$
\varphi_C(\bx) \triangleq \frac{1}{2} d_C^2(\bx) 
= \frac{1}{2}\| \bx - P_C(\bx) \|^2.
$$

We also define $\psi_C : \EE  \to \RR$ as:

$$
\psi_C(\bx) \triangleq \frac{1}{2} \left (\| \bx \|^2 - d_C^2(\bx) \right) 
= \underset{\by \in C}{\max}\left [ \langle y, x \rangle - \frac{1}{2} \| y \|^2 \right ]. 
$$

$\psi_C$ is convex as long as $C$ is nonempty (
regardless whether $C$ is convex or not).

## Nonexpansiveness 

```{rubric} Firm nonexpansiveness property
```

```{div}
For any $\bv, \bw \in \EE$, the following holds:

$$
\langle P_C(\bv) - P_C(\bw), \bv - \bw \rangle \geq 
\| P_C(\bv) - P_C (\bw) \|^2.
$$
```

```{rubric} Nonexpansiveness property
```

```{div}
For any $\bv, \bw \in \EE$, the following holds:

$$
\| P_C(\bv) - P_C (\bw) \| \leq \| \bv - \bw \|.
$$
```

In words, the distance between projection cannot be longer
than the distance between original points. Orthogonal
projection is a non-expansive map.


## Gradients and Subgradients

The gradient of $\varphi_C$ is given by:

$$
\nabla \varphi_C(\bx) = \bx - P_C(\bx)  \Forall \bx \in \EE.
$$

The gradient of $\psi_C$ is given by:

$$
\nabla \psi_C(\bx) = P_C(\bx).
$$


```{div}
We note that $\varphi_C = g \circ d_C$ where 
$g(t) = \frac{1}{2}[t]_+^2$.

We can get the subdifferentials for $d_C$ by applying the chain rule.

$d_C$ is differentiable at $\bx \notin C$.

$$
\partial d_C (\bx) = \begin{cases} 
 \left \{ \frac{\bx - P_C(\bx)}{d_C(\bx)}\right \}, & \bx \notin C\\
N_C(\bx) \cap B[\bzero, 1], & \bx \in C
\end{cases}.
$$
```

## Conjugates

```{div}

Let $f : \EE \to \RERL$ be:

$$
f(\bx) = \frac{1}{2} \| \bx \|^2 + \delta_C(\bx).
$$

Then, its conjugate is:

$$
f^*(\by) = \frac{1}{2}\| \by \|^2 - \frac{1}{2} d_C^2 (\by) = \psi_C(\by).
$$
```

## Smoothness 

The function $\varphi_C = \frac{1}{2} d_C^2$ is 1-smooth.

The function $\psi_C$ is also 1-smooth.