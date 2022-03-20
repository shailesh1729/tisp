# Strong Convexity

```{div}
A function $f : \EE \to \RERL$ is called 
$\sigma$-*strongly convex* for $\sigma > 0$ if 
$\dom f$ is convex and the following holds for any 
$\bx, \by \in \dom f$ and $\lambda \in [0,1]$:

$$
f(\lambda \bx + (1 - \lambda)\by) \leq \lambda f(\bx) 
+ (1-\lambda)f(\by) 
- \frac{\sigma}{2} \lambda (1 - \lambda) \| \bx - \by \|^2. 
$$

Strongly convex functions are convex.

If $\EE$ is Euclidean then $f$ is $\sigma$-strongly convex
if and only if the function $f(\cdot) - \frac{\sigma}{2} \| \cdot \|^2$
is convex.
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

Then $f$ is strongly convex if and only if $\bA$ is positive definite
and $\sigma \leq \lambda_{\min}(\bA)$.
```

## Useful Results

```{div}
Let $f$ be strongly convex and $g$ be convex. Then 
$f+g$ is strongly convex.
```
