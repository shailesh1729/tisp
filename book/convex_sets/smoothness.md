# Smoothness


Primary references for this section are
{cite}`beck2017first`.


## L-Smooth Functions 

```{prf:definition} L-smooth functions
:label: def-cvxf-l-smooth-func

For some $L \geq 0$, a function 
$f : \VV \to \RERL$ is called $L$-*smooth* over a set
$D \subseteq \VV$ if it is differentiable over $D$ 
and satisfies

$$
\| \nabla f(\bx) - \nabla f(\by)\|_* \leq L \| \bx - \by \| \Forall
\bx, \by \in D.
$$
The constant $L$ is called the *smoothness parameter*.
```

```{div}
* Since $f$ is differentiable over $D$, hence $D \subseteq \interior \dom f$.
* If $f$ is $L$-smooth over the entire $\VV$, we simply say that $f$ is $L$-smooth.
* $L$-smooth functions are also known as *functions with Lipschitz gradient with constant* $L$.
* The class of functions which are $L$-smooth over a set $D$ is denoted by $C_L^{1,1}(D)$.
* When $D = \VV$, then the class is simply denoted as $C_L^{1,1}$.
* The class of functions which are $L$-smooth for some $L \geq 0$ (but $L$ may not be known),
  is denoted by $C^{1,1}$.
* By definition, if a function is $L_1$-smooth, then it is $L_2$-smooth for
  every $L_2 \geq L_1$.
* Thus, it is often useful to identify the smallest possible value of $L$
  for which a function is $L$-smooth.
```


```{prf:example} Zero smoothness of affine functions
:label: ex-cvxf-affine-func-zero-smooth

Let $\bb \in \VV^*$ and $c \in \RR$.
Let $f : \VV \to \RR$ be given by:

$$
f(\bx) = \langle \bx, \bb \rangle + c.
$$

Then, $f$ is $0$-smooth.

To see this, we note that $\nabla f(\bx) = \bb$.
Consequently,

$$
\| \nabla f(\bx) - \nabla f(\by) \|_*  = \| \bb - \bb \|_* = \| \bzero \|_* = 0
\leq 0 \| \bx - \by \|.
$$
```


```{prf:theorem} Smoothness of quadratic functions
:label: res-cvxf-quadratic-smoothness

Let $\bA \in \SS^n$, $\bb \in \RR^n$ and $c \in \RR$.
Assume that $\RR^n$ is endowed with $\ell_p$-norm
for some $1 \leq p \leq \infty$.
Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) = \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c.
$$

Then, $f$ is $L$-smooth with $L = \| \bA \|_{p, q}$
where $q \in [1,\infty]$ is the {prf:ref}`conjugate exponent <def-bra-conjugate-exponent>`
satisfying

$$
\frac{1}{p} + \frac{1}{q} = 1
$$
and $\| \bA \|_{p, q}$ is the induced norm given by

$$
\| \bA \|_{p, q} = \sup \{ \| \bA \bx \|_q \ST \| \bx \|_p \leq 1 \}.
$$
```

```{prf:proof}
We note that the dual norm of $\ell_p$ norm is the $\ell_q$ norm.
Now,

$$
& \| \nabla f(\bx) - \nabla f(\by)\|_* \\
&= \| \nabla f(\bx) - \nabla f(\by)\|_q \\
&= \| \bA \bx + \bb - \bA \by - \bb \|_q \\
&= \| \bA \bx - \bA \by \|_q \\
&\leq  \| \bA \|_{p, q} \| \bx - \by \|_p.
$$

Thus, $f$ is  $\| \bA \|_{p, q}$ smooth.

We next show that $\| \bA \|_{p, q}$ is the smallest smoothness
parameter for $f$.

1. Assume that $f$ is $L$ smooth for some $L$.
1. By definition of $\| \bA \|_{p, q}$, there exists a vector
   $\tilde{\bx}$ such that $\| \tilde{\bx} \|_p = 1$ and 

   $$
   \| \bA \tilde{\bx} \|_q = \| \bA \|_{p, q} \| \tilde{\bx} \|_p
   = \| \bA \|_{p, q}.
   $$
1. Then,

   $$
   \| \bA \|_{p, q} &= \| \bA \tilde{\bx} \|_q\\
   &=  \| \bA \tilde{\bx} + \bb - \bA \bzero - \bb \|_q\\
   &= \| \nabla f(\tilde{\bx}) - \nabla f(\bzero) \|_q \\
   &\leq L \| \tilde{\bx} - \bzero \|_p = L.
   $$
1. Thus, $\| \bA \|_{p, q} \leq L$.

Thus, $\| \bA \|_{p, q}$ is indeed the smallest smoothness parameter for $L$.
```


## Descent Lemma

```{prf:theorem} Descent lemma
:label: res-cvxf-smooth-descent-lemma

Let $f : \VV \to \RERL$ be $L$-smooth for some $L \geq 0$ over 
some convex set $D$. Then for any $\bx, \by \in D$, 

$$
f(\by) \leq f(\bx) + \langle \by - \bx, \nabla f(\bx) \rangle + \frac{L}{2} \| \bx - \by \|^2. 
$$ 
```

```{prf:proof}

we proceed as follows:

1. By the fundamental theorem of calculus

   $$
   f(\by) - f(\bx) = \int_0^1 \langle \by - \bx, \nabla f(\bx + t(\by - \bx)) \rangle dt.
   $$
1. By adding and subtracting $\langle \by - \bx, \nabla f(\bx) \rangle$, we get:

   $$
   f(\by) - f(\bx) = \langle \by - \bx, \nabla f(\bx) \rangle + 
    \int_0^1 \langle \by - \bx, \nabla f(\bx + t(\by - \bx))  - \nabla f(\bx) \rangle dt.
   $$
1. This gives us

   $$
   & | f(\by) - f(\bx) -  \langle \by - \bx, \nabla f(\bx) \rangle | \\
   &= \left | 
   \int_0^1 \langle \by - \bx, \nabla f(\bx + t(\by - \bx))  - \nabla f(\bx) \rangle dt 
   \right | \\
   &\leq  \int_0^1 | \langle \by - \bx, \nabla f(\bx + t(\by - \bx))  - \nabla f(\bx) \rangle | dt \\
   &\leq \int_0^1 \| \by - \bx \|  \| \nabla f(\bx + t(\by - \bx))  - \nabla f(\bx) \|_* dt
   & \text{ (a) } \\
   &\leq \int_0^1 \| \by - \bx \|  tL \| \by - \bx \| dt 
   & \text { (b) } \\
   &= \int_0^1 tL  \| \by - \bx \|^2  dt \\
   &= L  \| \by - \bx \|^2 \int_0^1  t dt \\
   &= \frac{L}{2} \| \by - \bx \|^2.
   $$
   * (a) is an application of Generalized Cauchy Schwartz inequality ({prf:ref}`res-la-ip-gen-cs-ineq`}).
   * (b) is the application of $L$-smoothness of $f$ ({prf:ref}`def-cvxf-l-smooth-func`).
1. Thus,

   $$
   & | f(\by) - f(\bx) -  \langle \by - \bx, \nabla f(\bx) \rangle |  
   \leq \frac{L}{2} \| \by - \bx \|^2 \\
   & \implies f(\by) - f(\bx) -  \langle \by - \bx, \nabla f(\bx) \rangle  
   \leq \frac{L}{2} \| \by - \bx \|^2 \\
   & \implies f(\by) \leq f(\bx) + \langle \by - \bx, \nabla f(\bx) \rangle 
   + \frac{L}{2} \| \by - \bx \|^2.
   $$
```


## Characterization of $L$-smooth functions


```{div}
Let $f : \VV \to \RR$ be convex and differentiable over $\VV$.
Let $L > 0$. The following claims are equivalent:

1. $f$ is $L$-smooth.
1. $f(\by) \leq f(\bx) + \langle \nabla f(\bx), \by - \bx \rangle + \frac{L}{2} \| \bx - \by \|^2 \Forall \bx, \by \in \VV$. 
1. $f(\by) \geq f(\bx) + \langle \nabla f(\bx), \by - \bx \rangle + \frac{1}{2L} \| \nabla f (\bx) - \nabla f(\by) \|_*^2 \Forall \bx, \by \in \VV$.
1. $\langle \nabla f (\bx) - \nabla f(\by), \bx - \by \rangle  \geq \frac{1}{L} \| \nabla f (\bx) - \nabla f(\by) \|_*^2 \Forall \bx, \by \in \VV$.
1. $f(\lambda \bx + (1-\lambda) \by) \geq \lambda f(\bx) + (1-\lambda) f(\by) - \frac{L}{2} \lambda (1 - \lambda) \| \bx - \by \|^2  \Forall \bx, \by \in \VV, \lambda \in [0, 1]$.

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
