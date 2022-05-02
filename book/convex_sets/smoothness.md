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

```{prf:definition} Strong convexity
:label: def-cvxf-strong-convexity

A function $f : \VV \to \RERL$ is called 
$\sigma$-*strongly convex* for $\sigma > 0$ if 
$\dom f$ is convex and the following holds for any 
$\bx, \by \in \dom f$ and $t \in [0,1]$:

$$
f(t \bx + (1 - t)\by) \leq t f(\bx) 
+ (1-t)f(\by) 
- \frac{\sigma}{2} t (1 - t) \| \bx - \by \|^2. 
$$
```

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
and $\sigma \leq t_{\min}(\bA)$.
```

### Properties

```{div}
Let $f$ be strongly convex and $g$ be convex. Then 
$f+g$ is strongly convex.
```

