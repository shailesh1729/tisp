# Smoothness

## L-Smooth Functions

```{div}

For some $L \geq 0$, a function 
$f : \EE \to \RERL$ is called $L$-smooth over a set
$D \subseteq \EE$ if it is differentiable over $D$ 
and satisfies

$$
\| \nabla f(\bx) - \nabla f(\by)\|_* \leq L \| \bx - \by \| \Forall
\bx, \by \in D.
$$
```

```{rubric} Quadratic functions
```

```{div}
Let $\bA \in \SS^n$, $\bb \in \RR^n$ and $c \in \RR$.
Assume that $\RR^n$ is endowed with $p$-norm. Let
$f : \RR^n \to \RR$ be given by:

$$
f(\bx) = \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c.
$$

Then, $f$ is $L$-smooth with $L = \| A \|_{p, q}$.
```

```{rubric} Affine functions
```

```{div}
Let $\bb \in \EE^*$ and $c \in \RR$.
Let $f : \EE \to \RR$ be given by:

$$
f(\bx) = \langle \bb, \bx \rangle + c.
$$

Then, $f$ is $0$-smooth.
```

```{rubric} Descent lemma
```

```{div}
Let $f : \EE \to \RERL$ be $L$-smooth for some $L \geq 0$ over 
some convex set $D$. Then for any $\bx, \by \in D$, 

$$
f(\by) \leq f(\bx) + \langle \nabla f(\bx), \by - \bx \rangle + \frac{L}{2} \| \bx - \by \|^2. 
$$ 
```

## Characterization of $L$-smooth functions


```{div}
Let $f : \EE \to \RR$ be convex and differentiable over $\EE$.
Let $L > 0$. The following claims are equivalent:

1. $f$ is $L$-smooth.
1. $f(\by) \leq f(\bx) + \langle \nabla f(\bx), \by - \bx \rangle + \frac{L}{2} \| \bx - \by \|^2 \Forall \bx, \by \in \EE$. 
1. $f(\by) \geq f(\bx) + \langle \nabla f(\bx), \by - \bx \rangle + \frac{1}{2L} \| \nabla f (\bx) - \nabla f(\by) \|_*^2 \Forall \bx, \by \in \EE$.
1. $\langle \nabla f (\bx) - \nabla f(\by), \bx - \by \rangle  \geq \frac{1}{L} \| \nabla f (\bx) - \nabla f(\by) \|_*^2 \Forall \bx, \by \in \EE$.
1. $f(\lambda \bx + (1-\lambda) \by) \geq \lambda f(\bx) + (1-\lambda) f(\by) - \frac{L}{2} \lambda (1 - \lambda) \| \bx - \by \|^2  \Forall \bx, \by \in \EE, \lambda \in [0, 1]$.

Let $f : \RR^n \to \RR$ be a twice continuously differentiable function over $\RR^n$. 
Then, for any $L \geq 0$, the following claims are equivalent:

1. $f$ is $L$-smooth w.r.t. the $\ell_p$-norm ($p \in [1, \infty]$).
1. $\| \nabla^2 f(\bx)\|_{p, q} \leq L$ for any $\bx \in \RR^n$ where $q \geq 1$ satisfies
   $\frac{1}{p} + \frac{1}{q} = 1$.


Let $f : \RR^n \to \RR$ be a twice continuously differentiable convex function over $\RR^n$. 
Then $f$ is $L$-smooth w.r.t. $\ell_2$-norm if and only if 

$$
\lambda_{\max}( \nabla^2 f(\bx)) \leq L \Forall \bx \in \RR^n.
$$
```
