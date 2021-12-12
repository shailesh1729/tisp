# Convex Functions


```{prf:definition} Convex function
:label: def-convex-function

A function $f: \RR^n \to \RR$ is *convex* if 
$\dom f$ is a convex set and for all $x_1,x_2 \in \dom f$, 
and $\theta \in [0, 1]$, we have:

$$
f(\theta x_1 + (1-\theta) x_2) \leq \theta f(x_1) + (1-\theta) f(x_2).
$$
```

```{figure} ../images/convex_function.png
---
name: convex_function
---
```