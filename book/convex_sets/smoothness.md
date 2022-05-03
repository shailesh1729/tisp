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


### Descent Lemma

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


### Characterization of $L$-Smooth Functions


```{prf:theorem} Characterization of $L$-smooth functions
:label: res-cvxf-smoothness-charac

Let $f : \VV \to \RR$ be convex and differentiable over $\VV$.
Let $L > 0$. The following claims are equivalent:

1. $f$ is $L$-smooth.
1. $f(\by) \leq f(\bx) + \langle \by - \bx, \nabla f(\bx) \rangle + \frac{L}{2} \| \bx - \by \|^2 \Forall \bx, \by \in \VV$. 
1. $f(\by) \geq f(\bx) + \langle \by - \bx, \nabla f(\bx) \rangle + \frac{1}{2L} \| \nabla f (\bx) - \nabla f(\by) \|_*^2 \Forall \bx, \by \in \VV$.
1. $\langle \bx - \by, \nabla f (\bx) - \nabla f(\by) \rangle  \geq \frac{1}{L} \| \nabla f (\bx) - \nabla f(\by) \|_*^2 \Forall \bx, \by \in \VV$.
1. $f(t \bx + (1-t) \by) \geq t f(\bx) + (1-t) f(\by) - \frac{L}{2} t (1 - t) \| \bx - \by \|^2  \Forall \bx, \by \in \VV, t \in [0, 1]$.
```

```{prf:proof}
(1) $\implies$ (2). This is a direct implication of the descent lemma
({prf:ref}`res-cvxf-smooth-descent-lemma`).


(2) $\implies$ (3)

1. We are given that (2) is satisfied.
1. If $\nabla f(\bx) = \nabla f(\by)$, then the inequality is trivial
   due to the convexity of $f$.
   Hence, we consider the case where $\nabla f(\bx) \neq \nabla f(\by)$.
1. Fix a $\bx \in \VV$.
1. Consider a function $g_{\bx} : \VV \to \RR$ given by

   $$
   g_{\bx}(\by) = f(\by) - f(\bx)  - \langle \by - \bx, \nabla f(\bx) \rangle.
   $$
1. Then,

   $$
   \nabla g_{\bx}(\by)  = \nabla f(\by) - \nabla f(\bx).
   $$
1. By hypothesis in property (2), for any $\bz \in \VV$

   $$
   f(\bz) \leq f(\by) + \langle \bz - \by, \nabla f(\by) \rangle + \frac{L}{2} \| \bz - \by \|^2.
   $$
1. Now,

   $$
   & g_{\bx}(\bz) \\
   &= f(\bz) - f(\bx)  - \langle \bz - \bx, \nabla f(\bx) \rangle \\
   &\leq f(\by) + \langle \bz - \by, \nabla f(\by) \rangle + \frac{L}{2} \| \bz - \by \|^2
   - f(\bx)  - \langle \bz - \bx, \nabla f(\bx) \rangle\\
   &= f(\by) - f(\bx)  - \langle \bz - \bx, \nabla f(\bx) \rangle
   + \langle \bz - \by, \nabla f(\bx) \rangle - \langle \bz - \by, \nabla f(\bx) \rangle\\
   &+ \langle \bz - \by, \nabla f(\by) \rangle + \frac{L}{2} \| \bz - \by \|^2\\
   &= f(\by) - f(\bx)  - \langle \by - \bx, \nabla f(\bx) \rangle
   + \langle \bz - \by, \nabla f(\by) - \nabla f(\bx) \rangle + \frac{L}{2} \| \bz - \by \|^2\\
   &= g_{\bx}(\by) + \langle \bz - \by, \nabla g_{\bx}(\by) \rangle + \frac{L}{2} \| \bz - \by \|^2.
   $$
1. Thus, $g_{\bx}$ also satisfies the inequality in property (2).
1. We note in particular that $\nabla g_{\bx} (\bx) = \nabla f(\bx) - \nabla f(\bx) = \bzero$.
1. Since $g_{\bx}$ is convex, hence $\bx$ is the global minimizer of $g_{\bx}$.
1. In other words,

   $$
   g_{\bx}(\bx) \leq g_{\bx}(\bz) \Forall \bz \in \VV.
   $$
1. We can also see that $g_{\bx}(\bx) = f(\bx) - f(\bx)  - \langle \bx - \bx, \nabla f(\bx) \rangle = 0$.
1. Let $\by \in \VV$
1. Let $\bv \in \VV$ be the unit norm vector satisfying 
   $\| \nabla g_{\bx}(\by) \|_* = \langle \bv , \nabla g_{\bx}(\by) \rangle$.
1. Choose

   $$
   \bz = \by - \frac{\| \nabla g_{\bx}(\by) \|_*}{L} \bv.
   $$
1. Then,

   $$
   0 = g_{\bx}(\bx) \leq g_{\bx}(\bz) = g_{\bx}\left (\by - \frac{\| \nabla g_{\bx}(\by) \|_*}{L} \bv \right ).
   $$
1. Using property (2) on $g_{\bx}(\bz)$, we get

   $$
   0 &\leq g_{\bx}(\bz) \\
   &\leq g_{\bx}(\by) + \langle \bz - \by, \nabla g_{\bx}(\by) \rangle + \frac{L}{2} \| \bz - \by \|^2 \\
   &= g_{\bx}(\by) - \frac{\| \nabla g_{\bx}(\by) \|_*}{L} \langle \bv, \nabla g_{\bx}(\by) \rangle 
   + \frac{L}{2} \left \| \frac{\| \nabla g_{\bx}(\by) \|_*}{L} \bv \right \|^2 \\
   &= g_{\bx}(\by) - \frac{\| \nabla g_{\bx}(\by) \|_*}{L} \| \nabla g_{\bx}(\by) \|_* 
   + \frac{1}{2 L}  \| \nabla g_{\bx}(\by) \|_*^2 \\
   &= g_{\bx}(\by)
   - \frac{1}{2 L}  \| \nabla g_{\bx}(\by) \|_*^2 \\
   &= f(\by) - f(\bx)  - \langle \by - \bx, \nabla f(\bx) \rangle
   - \frac{1}{2 L}  \| \nabla f(\by) - \nabla f(\bx) \|_*^2.
   $$
1. Simplifying this, we get

   $$
   f(\by) \geq f(\bx) + \langle \by - \bx, \nabla f(\bx) \rangle + \frac{1}{2 L}  \| \nabla f(\by) - \nabla f(\bx) \|_*^2
   $$
   as desired.

(3) $\implies$ (4) 

1. For $\bx, \by$, the property (3) gives us:
 
   $$
   f(\by) \geq f(\bx) + \langle \by - \bx, \nabla f(\bx) \rangle + \frac{1}{2 L}  \| \nabla f(\by) - \nabla f(\bx) \|_*^2.
   $$
1. For $\by, \bx$, the property (3) gives us:
 
   $$
   f(\bx) \geq f(\by) + \langle \bx - \by, \nabla f(\by) \rangle + \frac{1}{2 L}  \| \nabla f(\bx) - \nabla f(\by) \|_*^2.
   $$
1. Adding the two inequalities and canceling the term $f(\bx) + f(\by)$ gives us

   $$
   0 \geq \langle \bx - \by, \nabla f(\by) - f(\bx) \rangle + \frac{1}{L}  \| \nabla f(\bx) - \nabla f(\by) \|_*^2.
   $$
1. Rearranging, we get

   $$
   \langle \bx - \by, \nabla f(\bx) - f(\by) \rangle \geq \frac{1}{L}  \| \nabla f(\bx) - \nabla f(\by) \|_*^2
   $$
   as desired.


(4) $\implies$ (1)

1. When $\nabla f(\bx) = \nabla f(\by)$, then the Lipschitz condition in (1) is trivial.
   Hence, we consider the case where $\nabla f(\bx) \neq \nabla f(\by)$.
1. By generalized Cauchy Schwartz inequality ({prf:ref}`res-la-ip-gen-cs-ineq`)

   $$
   \langle \bx - \by, \nabla f(\bx) - f(\by) \rangle \leq \| \bx - \by \| \| f(\bx) - f(\by) \|_*.
   $$
1. Thus, combining with hypothesis (4), we obtain

   $$
   \frac{1}{L}  \| \nabla f(\bx) - \nabla f(\by) \|_*^2 \leq \| \bx - \by \| \| f(\bx) - f(\by) \|_*.
   $$
1. Since $\nabla f(\bx) \neq \nabla f(\by)$, hence $\| f(\bx) - f(\by) \|_* > 0$.
1. Canceling it from both sides, we get

   $$
   \| \nabla f(\bx) - \nabla f(\by) \|_* \leq L \| \bx - \by \|
   $$
   as desired.

We have shown so far that (1), (2), (3) and (4) are equivalent statements.
We are left with showing that (5) is equivalent to the other statements.

(2) $\implies$ (5)

1. Pick $\bx, \by \in \VV$ and $t \in [0,1]$.
1. Let $\bz = t \bx + (1-t) \by$.
1. By hypothesis (2),

   $$
   & f(\bx) \leq f(\bz) + \langle \bx - \bz, \nabla f(\bz) \rangle + \frac{L}{2} \| \bx - \bz \|^2;\\
   & f(\by) \leq f(\bz) + \langle \by - \bz, \nabla f(\bz) \rangle + \frac{L}{2} \| \by - \bz \|^2.
   $$
1. Note that $\bx - \bz = (1-t) (\bx - \by)$ and $\by - \bz = t (\by - \bx)$.
1. Thus, the previous two inequalities are same as

   $$
   & f(\bx) \leq f(\bz) + (1-t)\langle \bx - \by, \nabla f(\bz) \rangle + \frac{L (1-t)^2}{2} \| \bx - \by \|^2;\\
   & f(\by) \leq f(\bz) + t\langle \by - \bx, \nabla f(\bz) \rangle + \frac{L t^2}{2} \| \bx - \by \|^2.
   $$
1. Multiplying the first inequality by $t$, the second by $(1-t)$ and adding, we get

   $$
   t f(\bx) + (1-t) f(\by) \leq f(\bz) + \frac{L t(1-t)}{2} \| \bx - \by \|^2.
   $$
1. Rearranging, we get

   $$
   f(t \bx + (1-t) \by) = f(\bz) \geq t f(\bx) + (1-t) f(\by)  -  \frac{L }{2} t(1-t) \| \bx - \by \|^2.
   $$

(5) $\implies$ (2)

1. Pick $\bx, \by \in \VV$ and $t \in (0,1)$.
1. By hypothesis in inequality (5)

   $$
   f(t \bx + (1-t) \by) \geq t f(\bx) + (1-t) f(\by)  -  \frac{L }{2} t(1-t) \| \bx - \by \|^2.
   $$
1. Rearranging the terms, we obtain

   $$
   & (1-t) f(\by) \leq f(t \bx + (1-t) \by) - t f(\bx) + \frac{L }{2} t(1-t) \| \bx - \by \|^2 \\
   &\iff (1-t) f(\by) \leq f(t \bx + (1-t) \by) - f(\bx) + (1 - t) f(\bx) + \frac{L }{2} t(1-t) \| \bx - \by \|^2 \\
   &\iff f(\by) \leq f(\bx) + \frac{f(t \bx + (1-t) \by) - f(\bx)}{1-t} + \frac{L }{2} t \| \bx - \by \|^2.
   $$
   Division by $(1-t)$ is fine since $(1-t) \in (0, 1)$.
1. Recalling the definition of directional derivative ({prf:ref}`def-cvxf-directional-derivative`):

   $$
   &\lim_{t \to 1^-}  \frac{f(t \bx + (1-t) \by) - f(\bx)}{1-t} \\
   &= \lim_{s \to 0^+} \frac{f( (1-s) \bx + s \by) - f(\bx)}{s} \\
   &= \lim_{s \to 0^+} \frac{f( \bx + s (\by - \bx) ) - f(\bx)}{s}\\
   &= f'(\bx; \by - \bx).
   $$
1. Since the previous inequality is valid for every $t \in (0,1)$, 
   taking the limit to $t \to 1^-$ on the R.H.S., we obtain

   $$
   f(\by) \leq f(\bx) + f'(\bx; \by - \bx) +  \frac{L }{2} \| \bx - \by \|^2.
   $$

1. Recall from {prf:ref}`res-cvxf-grad-dir-der` that 
   $f'(\bx; \by - \bx) = \langle \by - \bx, \nabla f(\bx) \rangle$.
1. Thus, we get:

   $$
   f(\by) \leq f(\bx) + \langle \by - \bx, \nabla f(\bx) \rangle +  \frac{L }{2} \| \bx - \by \|^2.
   $$
   as desired.
```

### Second Order Characterization

We now restrict our attention to the vector space $\RR^n$ equipped with
an $\ell_p$ norm with $p \geq 1$.

```{prf:theorem} $L$-smoothness and the boundedness of the Hessian
:label: res-cvxf-smoothness-twice-diff

Let $f : \RR^n \to \RR$ be a twice continuously differentiable function over $\RR^n$. 
Then, for any $L \geq 0$, the following claims are equivalent:

1. $f$ is $L$-smooth w.r.t. the $\ell_p$-norm ($p \in [1, \infty]$).
1. $\| \nabla^2 f(\bx)\|_{p, q} \leq L$ for any $\bx \in \RR^n$ where $q \geq 1$ satisfies
   $\frac{1}{p} + \frac{1}{q} = 1$.
```

```{prf:proof}
(2) $\implies$ (1)

1. We are given that $\| \nabla^2 f(\bx)\|_{p, q} \leq L$ for any $\bx \in \RR^n$.
1. By the fundamental theorem of calculus

   $$
   \nabla f(\by) - \nabla f(\bx) &= \int_0^1 \nabla^2 f(\bx + t(\by - \bx)) (\by - \bx) dt \\
   &=  \left (\int_0^1 \nabla^2 f(\bx + t(\by - \bx)) dt \right )  (\by - \bx).
   $$
1. Taking the (dual)-norm on both sides

   $$
   \| \nabla f(\by) - \nabla f(\bx)  \|_q
   &= \left \| \left (
      \int_0^1 \nabla^2 f(\bx + t(\by - \bx)) dt \right )  (\by - \bx) 
      \right \|_q \\
    &\leq \left \| \int_0^1 \nabla^2 f(\bx + t(\by - \bx)) dt \right \|_{p, q}
    \| \by - \bx \|_p \\
    &\leq \left ( \int_0^1  \|  \nabla^2 f(\bx + t(\by - \bx)) \|_{p, q} dt \right ) 
    \| \by - \bx \|_p \\
    &\leq \left ( \int_0^1 L dt \right ) \| \by - \bx \|_p \\
    &= L \| \by - \bx \|_p.
   $$
1. Thus, $\| \nabla f(\by) - \nabla f(\bx)  \|_q  \leq L \| \by - \bx \|_p$ as desired.


(1) $\implies$ (2)

1. We are given that $f$ is $L$ smooth with $\ell_p$ norm.
1. By fundamental theorem of calculus, for any $\bd \in \RR^n$ and $s > 0$,

   $$
   \nabla f(\bx + s \bd) - \nabla f(\bx) = \int_0^s \nabla^2 f(\bx + t \bd) \bd dt.
   $$
1. Taking $q$ norm on both sides

   $$
   \left \| \left ( \int_0^s \nabla^2 f(\bx + t \bd)  dt \right ) \bd \right \|_q 
   = \| \nabla f(\bx + s \bd) - \nabla f(\bx) \|_q
   \leq L \|\bx + s \bd - \bx \|_p = s L \| \bd \|_p.
   $$
1. Dividing by $s$ on both sides and taking the limit $s \to 0^+$, we get

   $$
   \| \nabla^2 f(\bx) \bd \|_q \leq L \| \bd \|_p. 
   $$
1. Since this is valid for every $\bd \in \RR^n$, hence

   $$
   \| \nabla^2 f(\bx) \|_{p,q} \leq L.
   $$
```

```{prf:corollary} $L$-smoothness and largest eigenvalue of Hessian
:label: res-cvxf-l-smoothness-twice-diff-max-eigen-hessian

Let $f : \RR^n \to \RR$ be a twice continuously differentiable convex function over $\RR^n$. 
Then $f$ is $L$-smooth w.r.t. $\ell_2$-norm if and only if 

$$
\lambda_{\max}( \nabla^2 f(\bx)) \leq L \Forall \bx \in \RR^n.
$$
```

```{prf:proof}
Since $f$ is convex, hence it follows that $\nabla^2 f(\bx) \succeq \ZERO$ for every $\bx$.
Thus,

$$
\|\nabla^2 f(\bx) \|_{2,2} =    \sqrt{\lambda_{\max}( \nabla^2 f(\bx)^2 )}  = \lambda_{\max}( \nabla^2 f(\bx)).
$$

From {prf:ref}`res-cvxf-smoothness-twice-diff`, $f$ is $L$-smooth
is equivalent to the condition that 

$$
\lambda_{\max}( \nabla^2 f(\bx)) = \|\nabla^2 f(\bx) \|_{2,2} \leq L.
$$
```

## Strong Convexity

````{prf:definition} Strong convexity
:label: def-cvxf-strong-convexity

A function $f : \VV \to \RERL$ is called 
$\sigma$-*strongly convex* for $\sigma > 0$ if 
$\dom f$ is convex and the following holds for any 
$\bx, \by \in \dom f$ and $t \in [0,1]$:

```{math}
:label: eq-cvxf-strong-convexity-cond
f(t \bx + (1 - t)\by) \leq t f(\bx) 
+ (1-t)f(\by) 
- \frac{\sigma}{2} t (1 - t) \| \bx - \by \|^2. 
```
````

Strongly convex functions are convex. In fact,
we have a stronger result available.

```{prf:theorem} Strong convexity and convexity
:label: res-cvx-strong-convexity-convexity

Assume that the ambient space $\VV$ is
{prf:ref}`Euclidean <def-la-gen-euclidean-space>`.

A function $f : \VV \to \RERL$ is $\sigma$-strongly convex
if and only if the function $f(\cdot) - \frac{\sigma}{2} \| \cdot \|^2$
is convex.
```

```{prf:proof}
Let us define a function $g : \VV \to \RERL$ as 

$$
g(\bx) = f(\bx) = \frac{\sigma}{2} \| \bx \|^2.
$$
We need to show that $f$ is $\sigma$-strongly convex
if and only if $g$ is convex.

1. We first note that $\dom g = \dom f$. 
1. Thus, $\dom g$ is convex if and only if $\dom f$ is convex.
1. Now, $g$ is convex if and only if $\dom g = \dom f$ is convex 
   and for any $\bx, \by \in \dom f$ and $t \in (0, 1)$

   $$
   g(t \bx + (1-t) \by) \leq t g(\bx) + (1-t) g(\by).
   $$
1. Now,

   $$
   & g(t \bx + (1-t) \by) \leq t g(\bx) + (1-t) g(\by) \\
   \iff & f(t \bx + (1-t) \by) -  \frac{\sigma}{2} \| t \bx + (1-t) \by \|^2 \\ 
   & \leq t f(\bx) + (1-t) f(\by) -  \frac{\sigma}{2} [t \| \bx \|^2 + (1-t) \| \by \|^2] \\
   \iff & f(t \bx + (1-t) \by) \leq t f(\bx) + (1-t) f(\by) \\
   & + \frac{\sigma}{2} [  \| t \bx + (1-t) \by \|^2  - t \| \bx \|^2 - (1-t) \| \by \|^2].
   $$
1. Since the norm is Euclidean, hence

   $$
   & \| t \bx + (1-t) \by \|^2  - t \| \bx \|^2 - (1-t) \| \by \|^2  \\
   &=  \langle t \bx + (1-t) \by, t \bx + (1-t) \by \rangle 
   - t \| \bx \|^2 - (1-t) \| \by \|^2 \\
   &= t^2 \| \bx \|^2 + (1-t)^2 \| \by \|^2 + 2 t (1-t)\langle \bx, \by \rangle
   - t \| \bx \|^2 - (1-t) \| \by \|^2  \\
   &= - t(1-t) \| \bx \|^2 - t(1-t) \| \by \|^2 + 2 t (1-t)\langle \bx, \by \rangle \\
   &= - t(1-t) \left ( \| \bx \|^2 +  \| \by \|^2 - 2 \langle \bx, \by \rangle \right ) \\
   &= - t(1-t) \| \bx - \by \|^2.
   $$
1. Thus, the convexity inequality for $g$ is equivalent to

   $$
   f(t \bx + (1-t) \by) \leq t f(\bx) + (1-t) f(\by) - \frac{\sigma}{2}t(1-t) \| \bx - \by \|^2
   $$
   which is nothing but the $\sigma$-strong convexity condition of $f$.
```


```{prf:theorem} Strong convexity of quadratic functions
:label: res-cvxf-quadratic-strong-convex

Let $\bA \in \SS^n$, $\bb \in \RR^n$ and $c \in \RR$.
Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) = \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c.
$$

Then $f$ is $\sigma$-strongly convex if and only if $\bA$ is positive definite
and $\sigma \leq \lambda_{\min}(\bA)$.
```

```{prf:proof}

Due to {prf:ref}`res-cvx-strong-convexity-convexity`,
$f$ is strongly convex with $\sigma > 0$ 
if and only if 
$g(\bx) = f(\bx) - \frac{\sigma}{2} \| \bx \|^2$
is convex.

1. We note that

   $$
   g(\bx) &= \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c - \frac{\sigma}{2} \| \bx \|^2\\
   &= \frac{1}{2} \bx^T (\bA - \sigma \bI) \bx + \bb^T \bx + c.
   $$
1. As shown in {prf:ref}`ex-cvxf-quadratic-func-convexity`,
   $g$ is convex if and only if $\bA - \sigma \bI \succeq \ZERO$.
1. This is equivalent to $\sigma \leq \lambda_{\min}(\bA)$.
```


### Sum Rule

```{prf:theorem} Sum of strongly convex and convex functions
:label: res-cvxf-sum-strong-convex-convex

Let $f$ be $\sigma$-strongly convex and $g$ be convex. Then 
$f+g$ is strongly convex.
```

```{prf:proof}
Since both $f$ and $g$ are convex, hence their domains are convex.
Hence, $\dom (f + g) = \dom f \cap \dom g$ is also convex.

We further need to show that $f+g$ satisfies {eq}`eq-cvxf-strong-convexity-cond`.

1. Let $\bx, \by \in \VV$ and $t \in (0,1)$.
1. Since $f$ is $\sigma$-strongly convex, hence

   $$
   f(t \bx + (1 - t)\by) \leq t f(\bx)  + (1-t)f(\by) 
   - \frac{\sigma}{2} t (1 - t) \| \bx - \by \|^2.
   $$
1. Since $g$ is convex, hence

   $$
   g(t \bx + (1 - t)\by) \leq t g(\bx)  + (1-t)g(\by).
   $$
1. Then, 

   $$
   & (f + g)(t \bx + (1 - t)\by) \\
   &= f(t \bx + (1 - t)\by) + g((t \bx + (1 - t)\by)) \\
   &\leq f(t \bx + (1 - t)\by) \leq t f(\bx)  + (1-t)f(\by) 
   - \frac{\sigma}{2} t (1 - t) \| \bx - \by \|^2 
   + t g(\bx)  + (1-t)g(\by)\\
   &= t (f + g) (\bx) + (1-t) (f + g)(\by) - \frac{\sigma}{2} t (1 - t) \| \bx - \by \|^2.
   $$
1. Thus, $f+g$ is also $\sigma$-strongly convex.
```


```{prf:example} Strong convexity of $\frac{1}{2}\| \cdot \|^2 + I_C$
:label: ex-cvxf-strong-convex-norm-sqr-indicator

Let $\VV$ be a {prf:ref}`Euclidean <def-la-gen-euclidean-space>` space.

1. The function $\frac{1}{2}\| \bx \|^2$ is 1-strongly convex
   due to {prf:ref}`res-cvxf-quadratic-strong-convex`.
1. Let $C$ be a convex set.
1. Then, the indicator function $I_C$ is convex.
1. Due to {prf:ref}`res-cvxf-sum-strong-convex-convex`, the function 

   $$
   g(\bx) = \frac{1}{2}\| \bx \|^2 + I_C(\bx)
   $$
   is also 1-strongly convex.
```


### First Order Characterization

Recall that $\dom (\partial f)$ denotes the set of points at which
$f$ is subdifferentiable.


```{prf:theorem} First order characterization of strong convexity
:label: res-cvxf-strong-convexity-charac-first-order

Let $f: \VV \to \RERL$ be a proper closed and convex function.
For a given $\sigma > 0$, the following statements are equivalent.


1. $f$ is $\sigma$-strongly convex.
1. For every $\bx \in \dom (\partial f)$, $\by \in \dom f$ and $\bg \in \partial f(\bx)$,
   the following holds true

   $$
   f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle 
   + \frac{\sigma}{2} \| \by - \bx \|^2.
   $$
1. For any $\bx, \by \in \dom (\partial f)$ and $\bg_{\bx} \in \partial f(\bx)$,
   $\bg_{\by} \in \partial f(\bx)$, the following holds true:

   $$
   \langle \bx - \by, \bg_{\bx}  - \bg_{\by} \rangle \geq \sigma \| \bx - \by \|^2.
   $$
```


```{prf:proof}
We shall prove the equivalence of these statements in the following order.
$(2) \implies (1)$, $(1) \implies (3)$, $(3) \implies (2)$.

(2) $\implies$ (1)

1. We assume that (2) is true.
1. Let $\bx, \by \in \dom f$ and $t \in (0,1)$. 
1. We need to show that {eq}`eq-cvxf-strong-convexity-cond` holds for $f$.
1. Since $\dom f$ is convex, its relative interior is not empty
   (see {prf:ref}`res-cvx-nonempty-relint`).
1. Let $\bz \in \relint \dom f$.
1. Choose some $\alpha \in (0, 1]$.
1. Let $\tilde{\bx} = (1-\alpha) \bx + \alpha \bz$.
1. By the line segment property ({prf:ref}`res-cvx-convex-relint-segment`),
   $\tilde{\bx} \in \relint \dom f$.
1. Let $\bx_t = t \tilde{\bx} + (1-t)\by$.
1. Again, by the line segment property,
   $\bx_t \in \relint \dom f$.
1. Since $f$ is a proper convex function, hence the subdifferential
   of $f$ at relative interior points is nonempty
   ({prf:ref}`res-cvxf-relint-subdiff-nonempty`).
1. Thus, $\partial f(\bx_t) \neq \EmptySet$
   and $\bx_t \in \dom (\partial f)$.
1. Take some $\bg \in \partial f(\bx_t)$.
1. By hypothesis (2)

   $$
   f(\tilde{\bx}) \geq f(\bx_t) + \langle \tilde{\bx} - \bx_t, \bg \rangle 
   + \frac{\sigma}{2} \| \tilde{\bx} - \bx_t \|^2.
   $$
1. Substituting $\bx_t  = t \tilde{\bx} + (1-t)\by$, we have
   $\tilde{\bx} - \bx_t = (1-t) (\tilde{\bx} - \by)$. Thus,

   $$
   f(\tilde{\bx}) \geq f(\bx_t) + (1-t)\langle \tilde{\bx} - \by, \bg \rangle 
   + \frac{\sigma (1-t)^2}{2} \| \tilde{\bx} - \by \|^2.
   $$
1. Similarly, by hypothesis (2)

   $$
   f(\by) \geq f(\bx_t) + \langle \by - \bx_t, \bg \rangle 
   + \frac{\sigma}{2} \| \by - \bx_t \|^2.
   $$
1. $\by - \bx_t = \by - t \tilde{\bx} - (1-t)\by = t (\by - \tilde{\bx})$.
1. This gives us,

   $$
   f(\by) \geq f(\bx_t) + t \langle \by - \tilde{\bx}, \bg \rangle 
   + \frac{\sigma t^2}{2} \| \by - \tilde{\bx} \|^2.
   $$
1. Multiplying the first inequality by $t$ and the second one by $(1-t)$
   and adding them together, we get

   $$
   t f(\tilde{\bx}) + (1-t)f(\by) \geq
   f(\bx_t) + \frac{\sigma t(1-t)}{2} \| \tilde{\bx} - \by \|^2.
   $$
1. Thus,

   $$
   f(t \tilde{\bx} + (1-t)\by) = f(\bx_t)
   \leq t f(\tilde{\bx}) + (1-t)f(\by) - \frac{\sigma t(1-t)}{2} \|\tilde{\bx} - \by \|^2.
   $$
1. Expanding $\tilde{\bx}$,

   $$
   t \tilde{\bx} + (1-t)\by 
   &= t ((1-\alpha) \bx + \alpha \bz) + (1-t)\by\\
   &= t(1-\alpha) \bx + (1-t) \by + t \alpha \bz.
   $$
1. Define $g_1(\alpha) = f(t \tilde{\bx} + (1-t)\by) = f(t(1-\alpha) \bx + (1-t) \by + t \alpha \bz)$.
1. Define $g_2(\alpha) = f(\tilde{\bx}) = f((1-\alpha) \bx + \alpha \bz)$.
1. Substituting these into the previous inequality, we obtain

   $$
   g_1(\alpha) \leq t g_2(\alpha)+ (1-t)f(\by) 
   - \frac{\sigma t(1-t)}{2} \|(1-\alpha) \bx + \alpha \bz - \by \|^2.
   $$
1. The functions $g_1$ and $g_2$ are one dimensional, proper, closed and convex
   functions.
1. By {prf:ref}`res-cvxf-convex-closed-univariate`, both $g_1$ and $g_2$
   are continuous on their domain.
1. Therefore, taking the limit $\alpha \to 0^+$, it follows that

   $$
   g_1(0) \leq t g_2(0) + (1-t)f(\by) 
   - \frac{\sigma t(1-t)}{2} \|\bx - \by \|^2.
   $$
1. Now $g_1(0) = f(t\bx + (1-t) \by)$
   and $g_2(0) = f(\bx)$.
1. Thus, 

   $$
   f(t\bx + (1-t) \by) \leq t f(\bx) + (1-t)f(\by) 
   - \frac{\sigma t(1-t)}{2} \|\bx - \by \|^2.
   $$
1. This establishes that $f$ is indeed $\sigma$-strongly convex.


(1) $\implies$ (3)

1. We are given that $f$ is $\sigma$-strongly convex.
1. Let $\bx, \by \in \dom (\partial f)$. 
1. Pick any $\bg_{\bx} \in \partial f(\bx)$ 
   and $\bg_{\by} \in \partial f(\by)$.
1. Let $t \in [0, 1)$ and
   denote $\bx_t = t \bx + (1-t) \by$.
1. By the hypothesis

   $$
   f(\bx_t) \leq t f(\bx) + (1-t) f(\by) - \frac{\sigma t (1-t) }{2} \| \bx - \by \|^2.
   $$
1. This is same as

   $$
   f(\bx_t) - f(\bx) \leq (1-t) [f(\by) - f(\bx)] 
   - \frac{\sigma t (1-t) }{2} \| \bx - \by \|^2.
   $$

1. We can see that $(1-t) \in (0, 1]$. 
1. Dividing both sides of inequality by $(1-t)$, we obtain

   $$
   \frac{f(\bx_t) - f(\bx)}{1-t} \leq f(\by) - f(\bx) 
   - \frac{\sigma t }{2} \| \bx - \by \|^2.
   $$
1. Since $\bg_{\bx} \in \partial f(\bx)$, hence by subgradient inequality

   $$
   f(\bx_t) \geq f(\bx) + \langle \bx_t - \bx, \bg_{\bx} \rangle.
   $$
1. We can rewrite this as

   $$
   \frac{f(\bx_t) - f(\bx)}{1-t} \geq \frac{\langle \bx_t - \bx, \bg_{\bx} \rangle}{1-t}.
   $$
1. Note that $\bx_t - \bx = (1-t)(\by - \bx)$.
1. Thus,

   $$
   \frac{f(\bx_t) - f(\bx)}{1-t} \geq  \langle \by - \bx, \bg_{\bx} \rangle.
   $$
1. Thus, 

   $$
   \langle \by - \bx, \bg_{\bx} \rangle \leq f(\by) - f(\bx) 
   - \frac{\sigma t }{2} \| \bx - \by \|^2.
   $$
1. This inequality holds for every $t \in [0, 1)$.
1. Taking the limit $t \to 1^-$, we obtain

   $$
   \langle \by - \bx, \bg_{\bx} \rangle \leq f(\by) - f(\bx) 
   - \frac{\sigma}{2} \| \bx - \by \|^2.
   $$
1. An identical reasoning by switching the roles of $\bx$ and $\by$, gives us

   $$
   \langle \bx - \by, \bg_{\by} \rangle \leq f(\bx) - f(\by) 
   - \frac{\sigma}{2} \| \by - \bx \|^2.
   $$
1. Adding these two inequalities gives us

   $$
   \langle \bx - \by, \bg_{\by} - \bg_{\bx} \rangle \leq
    - \sigma \| \bx - \by \|^2.
   $$
1. Multiplying both sides by $-1$ (and switching the inequality accordingly), we get

   $$
   \langle \bx - \by, \bg_{\bx} - \bg_{\by} \rangle \geq
   \sigma \| \bx - \by \|^2
   $$
   as desired.

(3) $\implies$ (2)

1. We are given that (3) is satisfied.
1. Let $\bx \in \dom (\partial f)$, $\by \in \dom f$ and $\bg \in \partial f(\bx)$.
1. Pick any $\bz \in \relint \dom f$.
1. Pick some $\alpha \in (0, 1)$.
1. Define $\tilde{\by} = (1 - \alpha) \by + \alpha \bz$.
1. By line segment property $\tilde{\by} \in \relint \dom f$.
1. Define $\bx_t = (1-t) \bx + t \tilde{\by}$.
1. Consider the 1D function
   
   $$
   \varphi(t) = f(\bx_t), \Forall t \in [0, 1]. 
   $$
1. Pick any $t \in (0, 1)$.
1. Then, by line segment principle $\bx_t \in \relint \dom f$.
1. Due to ({prf:ref}`res-cvxf-relint-subdiff-nonempty`),
   $\partial f(\bx_t) \neq \EmptySet$
   and $\bx_t \in \dom (\partial f)$.
1. Take some $\bg_t \in \partial f(\bx_t)$.
1. By subgradient inequality

   $$
   f(\bz) \geq f(\bx_t) + \langle \bz - \bx_t, \bg_t \rangle \Forall \bz \in \VV.
   $$
1. In particular, for $\bx_s = (1-s) \bx + s \tilde{\by}$, we have

   $$
   & f(\bx_s) \geq f(\bx_t) + 
   \langle (1-s) \bx + s \tilde{\by} - (1-t) \bx - t \tilde{\by}, \bg_t \rangle \\
   & \implies \varphi(s) \geq \varphi(t) + \langle (s-t) (\tilde{\by} - \bx), \bg_t \rangle \\
   &\implies \varphi(s) \geq \varphi(t) + (s-t) \langle \tilde{\by} - \bx, \bg_t \rangle.
   $$
1. Since this is valid for every $s$,
   hence $\langle \tilde{\by} - \bx, \bg_t \rangle \in \partial \varphi(t)$.
1. Applying the mean value theorem ({prf:ref}`res-cvxf-convex-subdiff-mvt`)

   $$
   f(\tilde{\by}) - f(\bx) = \varphi(1) - \varphi(0) 
   = \int_0^1 \langle \tilde{\by} - \bx, \bg_t \rangle dt.
   $$
1. Since $\bg \in \partial f(\bx)$ and $\bg_t \in \partial f(\bx_t)$,
   hence applying the hypothesis (3), we get

   $$
   \langle \bx_t - \bx, \bg_t - \bg \rangle \geq
   \sigma \| \bx_t - \bx \|^2.
   $$
1. But $\bx_t - \bx = t (\tilde{\by} - \bx)$.
1. Hence

   $$
   t \langle \tilde{\by} - \bx, \bg_t - \bg \rangle \geq
   \sigma t^2 \| \tilde{\by} - \bx \|^2.
   $$
1. This simplifies to

   $$
   \langle \tilde{\by} - \bx, \bg_t \rangle \geq
   \langle \tilde{\by} - \bx, \bg \rangle
   + \sigma t \| \tilde{\by} - \bx \|^2.
   $$
   Canceling $t$ on both sides doesn't change the sign of inequality since $t > 0$.
1. Applying the inequality to the integral above

   $$
   f(\tilde{\by}) - f(\bx) \geq \int_0^1
   \left [ \langle \tilde{\by} - \bx, \bg \rangle
   + \sigma t \| \tilde{\by} - \bx \|^2 \right ] d t.
   $$
1. Integrating, we get

   $$
   f(\tilde{\by}) - f(\bx) \geq  \langle \tilde{\by} - \bx, \bg \rangle
   + \frac{\sigma}{2}\| \tilde{\by} - \bx \|^2.
   $$
1. Expanding for $\tilde{\by}$ for any $\alpha \in (0,1)$, we have

   $$
   f((1 - \alpha) \by + \alpha \bz) \geq f(\bx) +  
   \langle (1 - \alpha) \by + \alpha \bz - \bx, \bg \rangle
   + \frac{\sigma}{2}\| (1 - \alpha) \by + \alpha \bz - \bx \|^2.
   $$
1. The 1D function $g(\alpha) = f((1 - \alpha) \by + \alpha \bz)$ is
   continuous again due to {prf:ref}`res-cvxf-convex-closed-univariate`.
1. Taking the limit $\alpha \to 0^+$ on both sides, we obtain

   $$
   f(\by) \geq f(\bx) +  
   \langle \by - \bx, \bg \rangle
   + \frac{\sigma}{2}\| \by - \bx \|^2
   $$
   which is the desired result.
```

### Minimization

```{prf:theorem} Existence and uniqueness of a a minimizer of closed strongly convex function
:label: res-cvxf-strong-convex-minimizer

Let $f: \VV \to \RERL$ be a proper, closed and $\sigma$-strongly convex
function with $\sigma > 0$. Then,

1. $f$ has a unique minimizer $\ba \in \dom f$ such that
   $f(\bx) > f(\ba)$ for every $\bx \in \dom f$ and $\bx \neq \ba$.
1. The increase in the value of $f$ w.r.t. its minimum satisfies

   $$
   f(\bx) - f(\ba) \geq \frac{\sigma}{2} \| \bx - \ba \|^2
   $$
   where $\ba \in \dom f$ is the unique minimizer of $f$.
```


```{prf:proof}

(1) Existence of the minimizer

1. Since $f$ is proper and convex, hence $\dom f$ is nonempty and convex.
1. Since $\dom f$ is nonempty and convex, hence its relative interior
   is nonempty ({prf:ref}`res-cvx-nonempty-relint`).
1. Pick $\by \in \relint \dom f$.
1. By {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`, $\partial f(\by)$
   is nonempty.
1. Pick some $\bg \in \partial f(\by)$.
1. Then, by property 2 of {prf:ref}`res-cvxf-strong-convexity-charac-first-order`,
   
   $$
   f(\bx) \geq f(\by) + \langle \bx - \by, \bg \rangle + \frac{\sigma}{2} \| \bx - \by \|^2
   $$
   holds true for every $\bx \in \VV$.
1. Let $\| \cdot \|_2 \triangleq \sqrt{\langle \cdot, \cdot \rangle}$
   denote the Euclidean norm associated with the inner product of the
   space $\VV$. This might be different from the endowed norm $\| \cdot \|$.
1. Since all norms in a finite dimensional space are equivalent, 
   hence, there exists a constant $C > 0$ such that 

   $$
   \| \bz \| \geq \sqrt{C} \| \bz \|_2
   $$
   for every $\bz \in \VV$.
1. Therefore,

   $$
   f(\bx) \geq f(\by) + \langle \bx - \by, \bg \rangle + \frac{\sigma C}{2} \| \bx - \by \|_2^2
   \Forall \bx \in \VV.
   $$
1. This in turn is same as

   $$
   f(\bx) \geq f(\by) - \frac{1}{2 C \sigma} \| \bg \|_2^2 
   + \frac{C \sigma}{2} 
   \left \| \bx - \left (\by - \frac{1}{C \sigma} \bg \right )
   \right \|_2^2
   \Forall \bx \in \VV.
   $$
1. Let $S_t$ denote the sublevel set $\{ \bx \ST f(\bx) \leq t \}$.
1. Consider the sublevel set $S_{f(\by)}$.
1. Let $\bx \in S_{f(\by)}$. 
1. Then, $f(\bx) = f(\by) - r$ for some $r \geq 0$.
1. But then

   $$
   f(\by) - r \geq f(\by) - \frac{1}{2 C \sigma} \| \bg \|_2^2 
   + \frac{C \sigma}{2} 
   \left \| \bx - \left (\by - \frac{1}{C \sigma} \bg \right )
   \right \|_2^2.
   $$
1. This simplifies to

   $$
   r \leq \frac{1}{2 C \sigma} \| \bg \|_2^2 
   - \frac{C \sigma}{2} 
   \left \| \bx - \left (\by - \frac{1}{C \sigma} \bg \right )
   \right \|_2^2.
   $$
1. Since $r$ must be nonnegative, hence the R.H.S. must be nonnegative
   also. 
1. Thus, we require that

   $$
   \frac{1}{2 C \sigma} \| \bg \|_2^2 
   \geq \frac{C \sigma}{2} 
   \left \| \bx - \left (\by - \frac{1}{C \sigma} \bg \right )
   \right \|_2^2.
   $$
1. This simplifies to

   $$
   \left \| \bx - \left (\by - \frac{1}{C \sigma} \bg \right )
   \right \|_2 \leq \frac{1}{C \sigma} \| \bg \|_2.
   $$
1. In other words, $\bx$ must belong to an $\ell_2$ closed ball given by

   $$
   B_{\| \cdot \|_2}\left [ \by - \frac{1}{C \sigma} \bg, 
      \frac{1}{C \sigma} \| \bg \|_2 \right ].
   $$
1. Since this is valid for every $\bx \in S_{f(\by)}$, hence

   $$
   S_{f(\by)} \subseteq B_{\| \cdot \|_2}\left [ \by - \frac{1}{C \sigma} \bg, 
      \frac{1}{C \sigma} \| \bg \|_2 \right ].
   $$
1. Since $f$ is closed, hence all its sublevel sets are closed.
1. since $S_{f(\by)}$ is contained in a ball, hence $S_{f(\by)}$ is bounded.
1. Thus, $S_{f(\by)}$ is closed and bounded. 
1. Since $\VV$ is finite dimensional, hence $S_{f(\by)}$ is compact.
1. $S_{f(\by)}$ is also nonempty since $\by \in S_{f(\by)}$.
1. Thus, the problem of minimizing $f$ over $\dom f$ reduces
   to the problem of minimizing $f$ over the nonempty compact set $S_{f(\by)}$.
1. Since $f$ is closed, it is also lower semicontinuous.
1. By {prf:ref}`res-ms-func-lsc-min-compact`, $f$ attains a minimum
   on $S_{f(\by)}$ at some point $\ba \in S_{f(\by)}$.
1. Thus, we have established the existence of a minimizer of $f$
   at some $\ba \in S_{f(\by)} \subseteq \dom f$.

(1) Uniqueness of the minimizer

1. To show the uniqueness, for contradiction, assume that
   $\bu$ and $\bv$ are two different minimizers of $f$
   with $f(\bu) = f(\bv) = p^*$, the optimal value.
1. Let $\bw = \frac{1}{2} \bu + \frac{1}{2} \bv$.
1. We must have $f(\bw) \geq p^*$.
1. By strong convexity of $f$,

   $$
   f(\bw) \leq \frac{1}{2} f(\bu) + \frac{1}{2} f(\bv) - 
   \frac{\sigma}{2}\frac{1}{2}\frac{1}{2} \| \bu - \bv \|^2
   = p^* - \frac{\sigma}{8}\| \bu - \bv \|^2.
   $$
1. If $\bu \neq \bv$, then $f(\bw) < p^*$; a contradiction.
1. Hence, the minimizer must be unique.


(2) Increase in value of $f$

1. Let $\ba$ be the unique minimizer of $f$.
1. By Fermat's optimality condition $\bzero \in \partial f(\ba)$.
1. Since $f$ is $\sigma$-strongly convex,
   hence by property (2) in the {prf:ref}`res-cvxf-strong-convexity-charac-first-order`,

   $$
   f(\bx) - f(\ba) \geq \langle \bx - \ba, \bzero \rangle 
   + \frac{\sigma}{2} \| \bx - \ba \|^2
   = \frac{\sigma}{2} \| \bx - \ba \|^2
   $$
   holds true for any $\bx \in \dom f$.
```



