# Boundedness


```{prf:definition} Boundedness
:label: def-ms-boundedness

A metric space $(X,d)$ is called *bounded* if there exists
a number $M > 0$ such that 

$$
d(x, y) \leq M \Forall x, y \in X.
$$
```

```{prf:definition} Diameter
:label: def-ms-diameter

The *diameter* of a subset $A$ of $(X, d)$ is defined as:

$$
\diam A \triangleq \sup \{ d(x,y) \ST x, y \in A \}.
$$
```

```{prf:remark}
$(X, d)$ is bounded if and only if $\diam X$ is finite. 
```

```{prf:example}
If $d$ is a metric on a set $X$, then the function
$\rho$ given by

$$
\rho(x, y) = \frac{d(x,y)}{1 + d(x,y)}
$$

is also a metric on $X$. Besides, $(X, \rho)$ is bounded and 
$\rho$ is equivalent of $d$.
```

We structure the proof into three parts:

1. Show that $\rho$ is a metric.
1. Show that $(X, \rho)$ is bounded.
1. Show that $\rho$ and $d$ are equivalent.

```{prf:proof} 
$\rho$ is a  
{prf:ref}`metric <def-ms-distance-function>`.

(1) Non-negativity: Since $d(x,y) \geq 0$, hence $\rho(x, y) \geq 0$
as it is a ratio of a non-negative number with a positive number.

(2) Identity of indiscernibles:

1. Assume $\rho(x, y) = 0$. 
1. Then $d(x,y)=0$. 
1. Thus $x=y$ since $d$ is a metric.
1. Now, assume $x=y$. 
1. Then $d(x,y)=0$.
1. Thus, $\rho(x,y)=0$. 


(3) Symmetry:

$$
\rho(y, x) = \frac{d(y,x)}{1 + d(y,x)} = \frac{d(x,y)}{1 + d(x,y)} = \rho(x, y).
$$


(4) Triangle inequality. This will require some work.

Consider the function $f: \RR \to \RR$:

$$
f(t) = \frac{t}{1+t}
$$
with $\dom f = \RR_+$.


Its derivative is 

$$
f'(t) = \frac{1}{(1+t)^2}.
$$

$f'(t) \geq 0$ for $t \in \RR_+$. Thus, $f$ is an increasing function
on $t \geq 0$. In particular:

$$
d(x, y)\leq d(x, z) + d(z, y) \implies f(d(x,y)) \leq f(d(x, z) + d(z, y)).
$$

Now, we proceed as follows:

$$
\begin{aligned}
\rho(x, y) &= f(d(x,y)) \\
&\leq f(d(x, z) + d(z, y))\\
&= \frac{d(x, z) + d(z, y)}{1 + d(x, z) + d(z, y)}\\
&= \frac{d(x, z)}{1 + d(x, z) + d(z, y)} + \frac{d(z, y)}{1 + d(x, z) + d(z, y)}\\
&\leq \frac{d(x, z)}{1 + d(x, z)} + \frac{d(z, y)}{1 + d(z, y)}\\
&= \rho(x,z) + \rho(z,y).
\end{aligned}
$$
```

```{prf:proof} 
$\rho$ is a bounded

It is easy to see that

$$
\sup \rho(x, y) = 1.
$$

Thus, $(X, \rho)$ is bounded.
```

```{prf:proof} $\rho$ is equivalent to $d$

We first show that the identity mapping $I : (X, d) \to (X, \rho)$ is continuous.

Let $a \in X$ and choose $\epsilon > 0$. 
Recall that $\rho$ is bounded with $\rho(x,y) < 1$. 

Thus, if $\epsilon \geq 1$, we can choose any $\delta > 0$ leading 
to $\rho(x,y) < \epsilon$  whenever $d(x,y) < \delta$.

Now, consider the case $\epsilon < 1$.

$$
\begin{aligned}
&\rho(x, a) < \epsilon\\
&\iff \frac{d(x,a)}{1 + d(x,a)} < \epsilon\\
&\iff 1 - \frac{d(x,a)}{1 + d(x,a)} > 1 - \epsilon\\
&\iff \frac{1}{1 + d(x,a)} > 1 - \epsilon\\
&\iff 1 + d(x, a) < \frac{1}{1 - \epsilon}\\
&\iff  d(x,a) < \frac{\epsilon}{1 - \epsilon}. 
\end{aligned}
$$

Now, choosing $\delta = \frac{\epsilon}{1 - \epsilon}$, we note that
$\delta > 0$ for $0 < \epsilon < 1$.

Thus, for every $\epsilon > 0$, there exists $\delta > 0$ 
such that $\rho(x, a) < \epsilon$ whenever $d(x, a) < \delta$.

Hence, $I$ is continuous. A similar argument also shows that
$I^{-1}$ is continuous.

Thus, $I$ is homeomorphism and the metric spaces 
$(X, d)$ and $(X, \rho)$ are homeomorphic. 

Hence, due to {prf:ref}`res-ms-equivalent-metric-homeomorphic-identity`,
the two metrics are equivalent.
```


