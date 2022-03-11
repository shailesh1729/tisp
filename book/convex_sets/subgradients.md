(sec:cvxf:subgradients)=
# Subgradients
Primary references for this section are {cite}`beck2017first`.

Throughout this section, we assume that $\VV, \WW$ are 
real vector spaces. Wherever necessary, 
they are equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \|$
or an {prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle$. 
They are also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$
as needed.


## Subgradients

````{prf:definition} Subgradient
:label: def-cvxf-subgradient

Let $f : \VV \to \RERL$ be a 
{prf:ref}`proper function <def-cvxf-proper-function>`. 
Let $\bx \in \dom f$. 
A vector $\bg \in \VV^*$ is called a *subgradient* of $f$ at $\bx$ 
if
```{math}
:label: eq-cvxf-subgradient-inequality
f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle \Forall \by \in \VV.
```
This inequality is known as the *subgradient inequality*.
````
```{div}
Here, we assume that $f$ is an extended value extension whenever
required; i.e., $f(\bx) = \infty$ for all $\bx \notin \dom f$.

As discussed in {prf:ref}`res-la-ip-dual-space-isomorphism`,
the vector spaces $\VV$ and $\VV^*$ are isomorphic.
Therefore, we follow the convention that both 
$\VV$ and $\VV^*$ have exactly the same elements.
The primary difference between $\VV$ and $\VV^*$ comes from the
computation of norm. If $\VV$ is endowed with a norm $\| \cdot \|$
then $\VV^*$ is endowed with a {prf:ref}`dual norm <def-la-dual-norm>`
$\| \cdot \|_*$.

In the arguments below $B[\ba, r]$ or $B_{\| \cdot \|}[\ba, r]$ denotes the
closed ball of radius $r$ in the normed space $(\VV, \| \cdot \|)$.
The closed ball of radius $r$ in the dual space $(\VV, \| \cdot \|_*)$
shall be denoted by $B_*[\ba, r]$ or $B_{\| \cdot \|_*}[\ba, r]$.
Open balls shall be denoted similarly.
```


```{prf:observation} Global affine underestimator
:label: res-cvxf-subgradient-affine-under-estimator

If $\bg$ is a subgradient of $f$ at some $\bx \in \dom f$, then
the affine function $a : \VV \to \RR$ given by: 

$$
a(\by) = f(\bx) + \langle \by - \bx, \bg \rangle 
= \langle \by, \bg \rangle + f(\bx) - \langle \bx, \bg \rangle \Forall \by \in \VV
$$
is a global affine underestimator for $f$.
Note that the term $f(\bx) - \langle \bx, \bg \rangle$ is a constant
since $\bx \in \VV$ and $\bg \in \VV^*$ are fixed.
This comes from the subgradient inequality:

$$
f(\by) \geq a(\by) \Forall \by \in \VV.
$$
```

````{prf:observation} Subgradient inequality alternative form
:label: res-cvxf-subgradient-inequality-alternative-form

For $\by \notin \dom f$, $f(\by) = \infty$. Thus, the subgradient
inequality is trivially satisfied for all $\by \notin \dom f$.
An alternate form of the inequality is:

```{math}
:label: eq-cvxf-subgradient-inequality-2
f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle \Forall \by \in \dom f.
```
````

## Subdifferential

At a point $\bx \in \dom f$, it is possible that there are
more than one subgradients. It is thus natural to introduce
the notion of the set of all subgradients of $f$ at a specific
point $\bx \in \dom f$.

```{prf:definition} Subdifferential set
:label: def-cvxf-subdifferential
Let $f : \VV \to \RERL$ be a proper function.
The set of all subgradients of $f$ at a point $\bx \in \dom f$
is called the *subdifferential* of $f$ at $\bx$ and is denoted by
$\partial f(\bx)$.

$$
\partial f(\bx) \triangleq 
\{ \bg \in \VV^* \ST f (\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle 
  \Forall \by \in \VV \}.
$$

For all $\bx \notin \dom f$, we define $\partial f(\bx) = \EmptySet$.
```

```{prf:theorem} Subdifferential of norm at $\bx = \bzero$
Let $f : \VV \to \RR$ by given by:

$$
f(\bx) = \| \bx \|
$$
where $\| \cdot \|$ is the norm endowed on $\VV$. Then, 
the subdifferential of $f$ at $\bx = \bzero$ is given by the
dual norm unit ball:

$$
\partial f (\bzero) = B_{\| \cdot \|_*}[\bzero, 1] 
= \{ \bg \in \VV^*  \ST \| \bg \|_* \leq 1 \}.
$$
```

```{prf:proof}
$\bg \in \partial f (\bzero)$ if and only if 

$$
f(\by) \geq f(\bzero) + \langle \by - \bzero, g \rangle \Forall \by \in \VV.
$$
This reduces to:

$$
\| \by \| \geq \langle \by, \bg \rangle \Forall \by \in \VV.
$$

Maximizing both sides of this inequality over the set $\{ \by \ST \| \by \| \leq 1 \}$,
we obtain:

$$
\| \bg \|_* = \underset{\| \by \| \leq 1}{\sup} \{\langle \by, \bg \rangle \}
\leq \underset{\| \by \| \leq 1}{\sup} \| \by \| = 1. 
$$
Thus, $\| \bg \|_* \leq 1$ is a necessary condition.

We now show that $\| \bg \|_* \leq 1$ is sufficient too.
By {prf:ref}`Generalized Cauchy Schwartz inequality <res-la-ip-gen-cs-ineq>`:
   
$$
\langle \by , \bg \rangle \leq \| \by \| \| \bg \|_* \leq \| \by \| \Forall \by \in \VV.
$$
Thus, if $\| \bg \|_* \leq 1$, then $\bg$ is a subgradient.

Thus, the vectors that satisfy the subgradient inequality are exactly the
same as those in $ B_{\| \cdot \|_*}[\bzero, 1]$.
```

The subdifferential of a function $f$ may be empty at specific points
$\bx \in \VV$.

```{prf:definition} Subdifferentiability
:label: def-cvxf-subdifferentiable

A proper function $f : \VV \to \RERL$ is called *subdifferentiable* 
at some $\bx \in \dom f$ if $\partial f(\bx) \neq \EmptySet$. 
```

```{prf:definition} Domain of subdifferentiability
:label: def-cvxf-domain-subdifferentiable

The set of points at which a proper function $f : \VV \to \RERL$ is
subdifferentiable, denoted by $\dom (\partial f)$, is defined as:

$$
\dom (\partial f) \triangleq \{\bx \in \VV \ST \partial f(\bx) \neq \EmptySet \}.
$$
```

### Properties of Subdifferential Set

```{prf:theorem} Closedness and convexity of the subdifferential set
:label: res-cvxf-subdifferential-closed-convex

Let $f: \VV \to \RERL$ be a proper function. Then the set $\partial f(\bx)$
is closed and convex for any $\bx \in \VV$.
```

```{prf:proof}
Let $\bx \in \VV$ be fixed. For any $\by \in \VV$, define the set

$$
H_{\by} = \{ \bg \in \VV^* \ST \langle \by - \bx, \bg \rangle \leq f(\by) - f(\bx) \}.
$$

Note that $H_{\by}$ is a closed {prf:ref}`half space <def-halfspace>` in $\VV^*$.

It is easy to see that 

$$
\partial f(\bx) = \bigcap_{\by \in \VV} H_{\by}.
$$

$$
& \bg \in \partial f(\bx) \\
&\iff f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle \Forall \by \in \VV\\
&\iff f(\by) - f(\bx) \geq \langle \by - \bx, \bg \rangle \Forall \by \in \VV\\
&\iff  \langle \by - \bx, \bg \rangle \leq f(\by) - f(\bx) \Forall \by \in \VV\\
&\iff \bg \in H_{\by} \Forall \by \in \VV\\
&\iff \bg \in \bigcap_{\by \in \VV} H_{\by}.
$$

Thus,  $\partial f(\bx)$ is an infinite intersection of closed and convex sets.
Hence $\partial f(\bx)$ is closed and convex.
```

```{prf:theorem} Subdifferentiability + Convex domain $\implies$ Convexity
:label: res-cvxf-subdiff-cvx-dom-cvx

Let $f: \VV \to \RERL$ be a proper function.
Assume that $\dom f$ is convex.
If $f$ is subdifferentiable at every $\bx \in \dom f$, then $f$ is convex.

In other words:

$$
\Forall \bx \in \dom f, \partial f(\bx) \neq \EmptySet \implies f \text{ is convex}.
$$
```

```{prf:proof}
Let $\bx, \by \in \dom f$. Let $t \in [0,1]$.
Let $\bz = (1- t) \bx + t \by$.

1. Since $\dom f$ is convex, hence $\bz \in \dom f$.
1. By hypothesis, $f$ is subdifferentiable at $\bz$.
1. Thus, there exists $\bg \in \partial f(\bz)$.
1. By subgradient inequality {eq}`eq-cvxf-subgradient-inequality-2`

   $$
   f(\by) \geq f(\bz) + \langle \by - \bz, \bg \rangle = f(\bz) + (1-t) \langle \by - \bx, \bg \rangle\\
   f(\bx) \geq f(\bz) + \langle \bx - \bz, \bg \rangle = f(\bz) - t \langle \by - \bx, \bg \rangle.
   $$
1. Multiplying the first inequality by $t$, second by $(1-t)$ and adding, we get:

   $$
   t f(\by) + (1-t) f(\bx) \geq f(\bz).
   $$

1. Thus, 

   $$
   f((1-t)\bx + t \by) = f(\bz) \leq t f(\by) + (1-t) f(\bx)
   $$
   holds true for any $\bx, \by \in \dom f$ and any $t \in [0,1]$.
1. Thus, $f$ is convex.
```

A convex function need not be subdifferentiable at every point in its domain.
The problem usually occurs at the boundary points of the domain if the domain
is not open.



```{prf:theorem} Multiplication by a positive scalar
:label: res-cvxf-subdiff-scaling

Let $f: \VV \to \RERL$ be a proper function.
Let $\bx \in \dom f$.
For any $\alpha > 0$, 

$$
\partial (\alpha f)(\bx) = \alpha \partial f(\bx).
$$
```

```{prf:proof}
Let $\bg \in \partial f(\bx)$.

1. By subgradient inequality {eq}`eq-cvxf-subgradient-inequality-2`
   
   $$
   f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle \Forall \by \in \dom f.
   $$
1. Multiplying by $\alpha$, we get:

   $$
   (\alpha f)(\by) \geq (\alpha f)(\bx) + 
   \langle \by - \bx, \alpha \bg \rangle \Forall \by \in \dom (\alpha f).
   $$
1. Thus, $\alpha \bg \in \partial (\alpha f)(\bx)$.
1. Thus, $\alpha \partial f(\bx) \subseteq \partial (\alpha f)(\bx)$.
1. It is easy to see the same argument backwards to show that

   $$
   \partial (\alpha f)(\bx) = \alpha \partial f(\bx).
   $$
```

### Proper Convex Functions

In this section, we discuss the properties of the
subdifferential sets for convex functions.


```{prf:theorem} Nonemptiness and boundedness of the subdifferential at interior points
:label: res-cvxf-subdiff-scaling-nonempty-bounded

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $\ba \in \interior S$.
Then, $\partial f (\ba)$ is nonempty and bounded. 

In other words, for a proper convex function, the subdifferential
at the interior points of its domain is nonempty and bounded.
```

```{prf:proof}

Outline of the proof

1. Identify a supporting hyperplane for the epigraph of $f$ at $(\ba, f(\ba)$.
1. Make use of the local Lipschitz continuity of the convex function at its interior points.
1. Show that the normal to the supporting hyperplane leads to a subgradient at $\ba$.
1. Show that the subgradients are bounded by using the
   local Lipschitz continuity inequality and the subgradient inequality.

Consider the {prf:ref}`direct sum <def-cvx-real-vector-space-r-prod>`
vector space $\VV \oplus \RR$.

1. $\epi f \subseteq \VV \oplus \RR$. 
1. Since $f$ is convex, hence $\epi f$ is convex.
1. For some $\ba \in \interior S$, consider the point
   $(\ba, f(\ba)) \in \VV \oplus \RR$.
1. Since $f$ is convex, hence $(\ba, f(\ba)) \in \boundary \epi f$.
1. By {prf:ref}`supporting hyperplane theorem <res-cvx-supporting-hyperplane-theorem>`,
   there exists a vector $(\bp, -\alpha) \in \VV^* \oplus \RR$ such that

   $$
   \langle \bx, \bp \rangle - t \alpha 
   \leq \langle \ba, \bp \rangle - f(\ba) \alpha
   \Forall (\bx, t) \in \epi f.
   $$
1. We shall show that $\alpha > 0$ must hold true and $\bg = \frac{\bp}{\alpha}$
   is indeed a subgradient at $\ba$.
1. We note that, $(\ba, f(\ba) + 1) \in \epi f$. Putting it in,

   $$
   & \langle \ba, \bp \rangle -  (f(\ba) + 1) \alpha  
   \leq \langle \ba, \bp \rangle - \alpha f(\ba)\\
   &\iff -\alpha \leq 0 \\
   &\iff \alpha \geq 0.
   $$
   Thus, $\alpha \geq 0$.
1. Recall from {prf:ref}`res-cvxf-convex-local-lipschitz-continuous` that
   $f$ is locally Lipschitz continuous at $\ba \in \interior \dom f$.
1. Thus, there exists $r > 0$ and $L > 0$ such that
   $B[\ba, r] \subseteq S$ and 

   $$
   |f(\bx) - f(\ba)| \leq L \| \bx - \ba \| \Forall \bx \in B[\ba, r].
   $$
1. Since $B[\ba, r] \subseteq S$, hence $(\bx, f(\bx)) \in \epi f$
   for every $\bx \in B[\ba, r]$.
1. Plugging $t = f(\bx)$ in the supporting hyperplane inequality, 
   we get

   $$
   \langle \bx, \bp \rangle - f(\bx) \alpha 
   \leq \langle \ba, \bp \rangle - f(\ba) \alpha
   \Forall \bx \in B[\ba, r].
   $$
1. Rearranging the terms, 

   $$
   \langle \bx - \ba, \bp \rangle \leq \alpha (f(\bx) - f(\ba))
   \Forall \bx \in B[\ba, r].
   $$
1. Using the local Lipschitz property,

   $$
   \langle \bx - \ba, \bp \rangle \leq  \alpha L \| \bx - \ba \| 
   \Forall \bx \in B[\ba, r]. 
   $$
1. Recall that the {prf:ref}`dual norm <res-la-ip-dual-norm>` 
   for $\bp \in \VV^*$ is given by

   $$
   \| \bp \|_* = \sup \{ |\langle \bx, \bp \rangle | \ST \bx \in \VV, \bx \| \leq 1 \}.
   $$
1. Let $\bp^{\dag} \in \VV$ with $\| \bp^{\dag} \| = 1$ be the vector at which
   the supremum is attained.
1. Then, $\| \bp \|_* = \langle \bp^{\dag}, \bp \rangle$ (since $\VV$ is real).
1. Since $\bp^{\dag}$ is a unit vector, hence $\ba + r \bp^{\dag} \in B[\ba, r]$.
1. Plugging $\bx = \ba + r \bp^{\dag}$ in the inequality above, we get

   $$
   r \langle \bp^{\dag}, \bp \rangle \leq  \alpha L \|  r \bp^{\dag} \| 
   \Forall \bx \in B[\ba, r]. 
   $$
1. Simplifying

   $$
   r \| \bp \|_* \leq \alpha L r \Forall \bx \in B[\ba, r].
   $$
1. This means that $\alpha > 0$ must be true.
   1. If $\alpha = 0$, then this inequality would require $\bp = \bzero$.
   1. But $(\bp, -\alpha)$ is a nonzero vector describing the supporting hyperplane.
1. Going back to the supporting hyperplane inequality and putting $t=f(\bx)$, 
   we have

   $$
   \langle \bx, \bp \rangle - f(\bx) \alpha 
   \leq \langle \ba, \bp \rangle - f(\ba) \alpha
   \Forall \bx \in S.
   $$
1. Rearranging the terms, we get

   $$
   \alpha (f(\bx) - f(\ba)) \geq \langle \bx - \ba, \bp \rangle \Forall \bx \in S.
   $$
1. Letting $\bg = \frac{1}{\alpha} \bp$ and dividing on both sides by 
   $\alpha$ (which is positive), we obtain

   $$
   f(\bx) - f(\ba) \geq \langle \bx - \ba, \bg \rangle \Forall \bx \in S.
   $$
1. Rearranging again

   $$
   f(\bx) \geq f(\ba) +  \langle \bx - \ba, \bg \rangle \Forall \bx \in S
   $$
   which is the subgradient inequality.
1. Thus, $\bg \in \partial f(\ba)$. 
1. Thus, $\partial f(\ba)$ is nonempty. 


We next show the boundedness of $\partial f(\ba)$.

1. Let $\bg \in \partial f(\ba)$.
1. Let $\bg^{\dag} \in \VV$ such that $\| \bg^{\dag} \| = 1$ and

   $$
   \| \bg \|_* = \langle \bg^{\dag}, \bg \rangle.
   $$
1. Let $\bx = \ba + r \bg^{\dag}$.
1. Applying the subgradient inequality on $\bx$, we get:

   $$
   f(\bx) \geq f(\ba) +  \langle r \bg^{\dag}, \bg \rangle
   = f(\ba) + r \| \bg \|_*.
   $$
1. Thus, 

   $$
   r \| \bg \|_* \leq f(\bx) - f(\ba) \leq L \| \bx - \ba \| = L \| r \bg^{\dag} \| = L r.
   $$
1. Thus, $\| \bg \|_* \leq L$ for every $\bg \in \partial f(\ba)$.
1. Thus, $\partial f(\ba)$ is bounded.
```


Let $f : \VV \to (-\infty, \infty]$ be a proper convex function.

* $f$ need not be subdifferentiable at every point in $\dom f$.
* For a point $\bx \in \interior \dom f$, $\partial f (x)$ is non-empty and bounded.
* $f$ is subdifferentiable at every point in the interior of its domain.
* In other words, the subdifferential set may be empty only on the boundary of 
  $\dom f$ for a proper convex function.
* If $X \subseteq \interior \dom f$ is nonempty and compact, then 
  $Y = \cup_{\bx \in X} \partial f (\bx)$ is nonempty and bounded. i.e., the
  subdifferentiables over a compact set in the domain are nonempty 
  and bounded.
* $f$ is subdifferentiable at a point in its relative interior.

  $$
  \relint \dom f \subseteq \dom \partial f.
  $$ 
* There exists $\bx \in \dom f$ where $\partial f(\bx)$ is nonempty. In other
  words, $\dom \partial f$ is not empty since $\relint \dom f$ is always
  nonempty.
* If $\Dim(\dom f) < \Dim(\VV)$ and $\partial f(\bx)$ is nonempty for some
  $\bx \in \dom f$, then $\partial f(\bx)$ is unbounded. 

### Convex Functions

Let $f : \VV \to \RR$ be convex. 

* $f$ is subdifferentiable over $\VV$.


## Directional Derivatives


```{div}
Let $f : \VV \to (-\infty, \infty]$ be a proper function.
Let $\bx \in \interior \dom f$. 
The *directional derivative* at $\bx$ in the direction $\bd \in \VV$ is defined by 

$$
f'(\bx;\bd) \triangleq \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha \bd) - f(\bx)}{\alpha}.
$$
```
The directional derivative is a scalar quantity ($\in \RR$).

### Proper Convex Functions

Let $f : \VV \to (-\infty, \infty]$ be a proper convex function.
Let $\bx \in \interior \dom f$. 

* For any $\bd \in \VV$, the directional derivative $f'(\bx; \bd)$ exists.
* $f(\by) \geq f(\bx) + f'(\bx; \by -\bx) \Forall \by \in \dom f$.
* Max formula: For any $\bd \in \VV$, 

  $$
  f'(\bx;\bd) = \max \{ \langle \bg, \bd \rangle \ST \bg \in \partial f(\bx) \}.
  $$

* Max formula alternative formulation using the support function notation:

  $$
  f'(\bx;\bd) = \sigma_{\partial f(\bx)}(\bd).
  $$

For a proper convex function, at a point $\bx \in \interior \dom f$, we define 
a mapping $g : \VV \to \RR$ given by $ g(\bd) \triangleq f'(\bx;\bd)$.
In other words, $g$ performs $\bd \mapsto f'(\bx;\bd)$ mapping at $\bx$.

* $g$ is convex.
* $g$ is homogeneous. i.e. $g(\lambda \bd) = \lambda g(\bd)$ for some $\lambda \geq 0$.



## Differentiability

```{div}
Let $f : \VV \to (-\infty, \infty]$ be a proper function.
Let $\bx \in \interior \dom f$. 
$f$ is said to be *differentiable* at $\bx \in \interior \dom f$
if there exists $\bg \in \VV^*$ such that:

$$
\underset{\bh \to 0}{\lim} 
\frac{f(\bx + \bh) - f(\bx) - \langle \bg, \bh \rangle}{\| \bh \|} = 0.
$$
The unique vector $\bg$ satisfying this condition is called
the *gradient* of $f$ at $\bx$ and is denoted by $\nabla f(\bx)$.
```


```{div}
Let $f : \VV \to (-\infty, \infty]$ be a proper function.
Let $\bx \in \interior \dom f$. Assume $f$ to be 
differentiable at $\bx$. 

* Directional derivative in terms of gradient: 

  $$
  f'(\bx; \bd) = \langle \nabla f(\bx) , \bd \rangle \Forall \bd \in \VV.
  $$

* The i-th component of the gradient:

  $$
  (\nabla f(\bx))_i = \langle \nabla f(\bx), \be_i \rangle = f'(\bx; \be_i).
  $$

  $$
  \frac{\partial f}{\partial \bx_i} (x) = (\nabla f(\bx))_i = f'(\bx; \be_i).
  $$

* The gradient in terms of partial derivatives:

  $$
  \nabla f(\bx) = D_f(\bx) \triangleq
    \begin{pmatrix}
    \frac{\partial f}{\partial x_1} (\bx)\\
    \frac{\partial f}{\partial x_2} (\bx)\\
    \vdots \\
    \frac{\partial f}{\partial x_n} (\bx)
    \end{pmatrix}
  $$
  This holds if $\VV$ is endowed with the standard dot product 
  as the inner product.
* Directional derivative in terms of partial derivatives:

  $$
  f'(\bx; \bd) = D_f(\bx)^T \bd = \sum_{i=1}^n \frac{\partial f}{\partial x_i} (\bx) d_i.
  $$

* For a general inner product $\langle \bx, \by \rangle_{\bH} = \bx^T \bH \by$
  where $\bH$ is is a positive definite matrix:

  $$
  \begin{aligned}
  (\nabla f(\bx))_i
  &= \nabla f(\bx)^T \be_i \\ 
  &= \langle \nabla f(\bx), \bH^{-1} \be_i \rangle_{\bH}\\ 
  &= f'(\bx; \bH^{-1} \be_i)\\
  &= D_f(\bx)^T \bH^{-1} \be_i.
  \end{aligned}
  $$

* The gradient in terms of partial derivatives for a 
  general inner product:

  $$
  \nabla f(\bx) = \bH^{-1} D_f(\bx).
  $$
```


```{div}
Let $f : \VV \to (-\infty, \infty]$ be a proper convex function.
Let $\bx \in \interior \dom f$. 
Assume $f$ to be differentiable at $\bx$. 

* The subdifferential set at $\bx$ is a singleton.

  $$
  \partial f(\bx) = \{\nabla f(\bx) \}.
  $$


Let $f : \VV \to (-\infty, \infty]$ be a proper convex function.
Let $x \in \interior \dom f$. 

* If $f$ has a unique subdifferential at $\bx$, then it is 
  differentiable at $\bx$ with:

  $$
  \partial f(\bx) = \{\nabla f(\bx) \}.
  $$
```


## Subdifferential Calculus

### Sums of Functions

Let $f_1, f_2 : \VV \to (-\infty, \infty]$ be proper convex functions.

Let $x \in \dom f_1 \cap \dom f_2$.
Let $y \in \interior \dom f_1 \cap \interior \dom f_2$.

* $\partial f_1(x) + \partial f_2(x) \subseteq \partial (f_1 + f_2)(x)$.
* $\partial(f_1 + f_2)(y) = \partial f_1 (y) + \partial f_2(y)$.


Let $f_1, f_2, \dots, f_m : \VV \to (-\infty, \infty]$ be proper convex functions.

Let $x \in \bigcap_{i=1}^m \dom f_i$.
Let $y \in \bigcap_{i=1}^m \interior \dom f_i$.

* Weak sum rule 

  $$
  \sum_{i=1}^m \partial f_i (x) \subseteq \partial \left ( \sum_{i=1}^m f_i \right )(x).
  $$

* Strong sum rule

  $$
  \sum_{i=1}^m \partial f_i (y) = \partial \left ( \sum_{i=1}^m f_i \right )(y).
  $$

If $f_i$ are real-valued then, the strong sum rule holds for the 
entire $\VV$.

If $\bigcap_{i=1}^m \relint \dom f_i \neq \EmptySet$, then for any $x \in \VV$,
the strong sum rule holds:

$$
\sum_{i=1}^m \partial f_i (x) = \partial \left ( \sum_{i=1}^m f_i \right )(x).
$$

### Affine Transformations

Let $f: \VV \to (-\infty, \infty]$ be a proper convex function.
Let $\AAA : \VV \to \VV$ be a linear transformation.
Let 

$$
h (x) = f (\AAA(x) + b)\; \text{ with } b \in \VV.
$$

Assume that $h$ is proper, i.e. $\dom h$ is not empty where: 

$$
\dom h = \{ x \in \VV \ST \AAA(x) + b \in \dom f\}.
$$

Weak affine transformation rule. For any $x \in \dom h$: 

$$
\AAA^T (\partial f (\AAA(x) + b)) \subseteq \partial h(x).
$$

Strong affine transformation rule. 
For any $x \in \interior \dom h$ such that $\AAA (x) + b \in \interior \dom f$:

$$
\AAA^T (\partial f (\AAA(x) + b)) = \partial h(x).
$$

If we know the subdifferential set of $f$, then we can compute
the subdifferential set of $h$.

### Composition

```{rubric} Chain rule
```

```{div} 
Let $f : \RR \to \RR$ be continuous on $[a,b]$ with $a < b$. Let 
$f'_+(a)$ exist. Let $g : \RR \to \RR$ be defined on an open interval 
$I$ such that $\range f \subseteq I$. Assume $g$ is differentiable
at $f(a)$. Then the composite function

$$
h(t) \triangleq g (f (t)) \quad (a \leq t \leq b)
$$ 
is right differentiable at $t=a$. In particular,

$$
h'_+(a) = g'(f(a)) f'_+(a).
$$
```

```{rubric} Subdifferential chain rule
```

```{div} 
Let $f : \VV \to \RR$ be convex and let $g : \RR \to \RR$ be a 
nondecreasing convex function. Let $x \in \VV$ and assume that
$g$ is differentiable at $f(x)$. Let $h = g \circ f$. Then

$$
\partial h (x) = g'(f(x)) \partial f(x).
$$
```

## Maximum over a Set of Functions

```{rubric} Proper functions
```

```{div}
Let $f_1, f_2, \dots, f_m : \VV \to (-\infty,\infty]$ be a set of
proper functions. Let

$$
f(x) = \max \{ f_1(x), f_2(x), \dots, f_m(x)\}.
$$

Let $x \in \bigcap_{i=1}^m \interior \dom f_i$ be a point common to the
domains of all the functions.
Let $d \in \VV$ be a direction. 

If $f'_i(x;d)$ exist for all $i$, we have,

$$
f'(x; d) = \underset{i \in I(x)}{\max} f'_i(x;d)
$$
where $I(x) = \{ i \ST f_i(x) = f(x)\}$.

In other words, we identify the functions $f_i$ which achieve the maximum
$f(x)$ at $x$, compute the directional derivatives of these functions at $x$
for the direction $d$ and then compute the maximum of the directional derivatives.
```

```{rubric} Proper convex functions
```

```{div}


Let $f_1, f_2, \dots, f_m : \VV \to (-\infty,\infty]$ be a set of
proper convex functions. Let

$$
f(x) = \max \{ f_1(x), f_2(x), \dots, f_m(x)\}.
$$

Let $x \in \bigcap_{i=1}^m \interior \dom f_i$ be a point common to the
domains of all the functions.
Let $d \in \VV$ be a direction. 
For proper convex functions $f_i$, the directional derivatives exist 
always. We have:

$$
f'(x; d) = \underset{i \in I(x)}{\max} f'_i(x;d)
$$
where $I(x) = \{ i \ST f_i(x) = f(x)\}$.

Subgradient set of $f$ from subgradients of $f_i$:

$$
\partial f(x) = \text{conv } \left ( \bigcup_{i\in I(x)} \partial f_i (x) \right ).
$$
```

```{rubric} Differentiable functions
```

```{div}
If $f_i$ are differentiable at $x$, then

$$
f'(x; d) = \underset{i \in I(x)}{\max} f'_i(x;d) 
= \underset{i \in I(x)}{\max} \langle \nabla f_i(x) , d \rangle.
$$
```

```{rubric} Infinite set of functions
```
We have a weak rule for the subdifferential of the supremum of 
an arbitrary set of functions.

```{div}
Let $I$ be an arbitrary index set indexing a set of proper 
convex functions $f_i : \VV \to (-\infty, \infty]$ where $i \in I$.

Then for any  $x \in \dom f$, 

$$
\text{conv } \left ( \bigcup_{i \in I(x)} \partial f_i(x)
  \right ) \subseteq \partial f(x)
$$

where $I (x) = \{i \in I \ST f(x) = f_i (x) \}$.
```

## Norm Functions

```{div}
Subdifferential of a norm $\| \cdot \|: \VV \to \RR$ at $x = \ZeroVec$:

$$
\partial f(\ZeroVec) = B_{\| \cdot \|_*} [\ZeroVec, 1] = \{ g \in \VV^* \ST \|g\|_* \leq 1 \}. 
$$
```

### $\ell_1$-Norm

```{div}
Let $f : \RR^n \to \RR$ be given by $f(x) = \| x \|_1$.

Subdifferential of $f$ at $x = \ZeroVec$:

$$
\partial f(\ZeroVec) = B_{\| \cdot \|_{\infty}} [\ZeroVec, 1] = [-1, 1]^n. 
$$
```

```{div}
Subdifferential of $g : \RR \to \RR$ with $g(x) = |x|$ at $x = 0$:

$$
\partial g (0) = [-1, 1].
$$
```

```{div}
We can write $f$ as a sum of $n$ functions

$$
f(x) = \| x \|_1 =  \sum_{i=1}^n |x_i| = \sum_{i=1}^n f_i(x)
$$

where 

$$
f_i (x) = | x_i |.
$$

The subdifferential set of $f_i$ is given by:

$$
\partial f_i (x) = \begin{cases} 
\{ \sgn (x_i) e_i \} & \text{for} & x_i \neq 0 \\
[-e_i, e_i] & \text{for} & x_i  = 0
\end{cases}.
$$

We define the index set:

$$
I_0(x) = \{ i \ST x_i = 0\}.
$$


Using the strong sum rule, we have:

$$
\partial f (x) = \sum_{i \in I_0(x)} [-e_i, e_i] + \sum_{i \notin I_0(x)} \sgn (x_i) e_i.
$$

We can rewrite this as:

$$
\partial f (x) = \{ z \in \RR^n \ST z_i = \sgn (x_i) 
  \text{ whenever } x_i \neq 0, |z_i | \leq 1, \text{ otherwise } \}.
$$

We also have a weak result from this:

$$
\sgn (x) \in \partial f (x) = \partial \| x \|_1.
$$

Now let $g(t) = [t]_+^2$. And consider the function $h = g \circ f$ given by

$$
h (x) = \| x \|_1^2.
$$

By subdifferential chain rule:

$$
\partial h (x) = 2 \| x \|_1 \partial f (x)
= 2 \| x \|_1 \{ z \in \RR^n \ST z_i = \sgn (x_i) 
  \text{ whenever } x_i \neq 0, |z_i | \leq 1, \text{ otherwise } \}.
$$
```



### $\ell_2$-Norm

```{div}
Let $f : \RR^n \to \RR$ be given by $f(x) = \| x \|_2$.

Subdifferential of $f$ at $x = \ZeroVec$:

$$
\partial f(\ZeroVec) = B_{\| \cdot \|_2} [\ZeroVec, 1] 
= \{ g \in \RR^n \ST \|g\|_2 \leq 1 \}. 
$$

At $x \neq \ZeroVec$, $f$ is differentiable with the gradient:

$$
\nabla f (x) = \frac{x}{ \| x \|_2}.
$$

Combining the two, we get:

$$
\partial f (x) = \begin{cases} 
\left \{ \frac{x}{ \| x \|_2} \right \} & \text{for} & x \neq \ZeroVec \\
B_{\| \cdot \|_2} [\ZeroVec, 1] & \text{for} & x  = \ZeroVec
\end{cases}.
$$
```

### $\ell_{\infty}$-Norm

```{div}
Let $f : \RR^n \to \RR$ be given by $f(x) = \| x \|_{\infty}$.
```

```{div}
Subdifferential of $f$ at $x = \ZeroVec$:

$$
\partial f(\ZeroVec) = B_{\| \cdot \|_1} [\ZeroVec, 1] 
= \{ x \in \RR^n \ST \|x\|_1 \leq 1 \}. 
$$

Subdifferential of $f$ at $x \neq \ZeroVec$.

We have:

$$
f(x) = \max \{f_1(x), f_2(x), \dots, f_n(x)\}
$$
where $f_i(x) = |x_i|$. We set:

$$
I(x) = \{i \ST |x_i | = f(x) = \| x \|_{\infty} \}.
$$

We have

$$
\partial f_i(x) = \{\sgn (x_i)  e_i \} \Forall i \in I(x).
$$

$$
\partial f(x) = \text{conv } \left (\bigcup_{i \in I(x)} \{\sgn (x_i)  e_i \} \right ).
$$

We can rewrite this as:

$$
\partial f(x) = \left \{\sum_{i \in I(x)} \lambda_i \sgn(x_i) e_i \ST 
 \sum_{i \in I(x)} \lambda_i = 1, \lambda_j \geq 0, j \in I(x) \right \}.
$$


Combining the two cases, we get:

$$
\partial f (x) = \begin{cases} 
\left \{\sum_{i \in I(x)} \lambda_i \sgn(x_i) e_i \ST 
 \sum_{i \in I(x)} \lambda_i = 1, \lambda_j \geq 0, j \in I(x) \right \},
& x \neq \ZeroVec \\
B_{\| \cdot \|_1} [\ZeroVec, 1], & x  = \ZeroVec
\end{cases}.
$$
```

### $\ell_1$ Norm over Affine Transformation  

```{div}
Let $A \in \RR^{m \times n}$. Let $b \in \RR^m$. 
Let $f : \RR^m \to \RR$ be given by $f(y) = \| y \|_1$.

Let $h : \RR^n \to \RR$ be the function 
$h(x) = \| A x + b \|_1 = f(A x + b)$.

By affine transformation rule, we have:

$$
\partial h (x) = A^T \partial f (A x + b) \Forall x \in \RR^n.
$$

Denoting $i$-th row of $A$ as $a_i^T$, we define the index set:

$$
I_0(x) = \{i : a_i^T x_i + b_i = 0 \}.
$$

we have:

$$
\partial h (x) = \sum_{i \in I_0(x)} [-a_i, a_i] + 
\sum_{i \notin I_0(x)} \sgn(a_i^T x + b_i) a_i.
$$


In particular, we have the weak result:

$$
A^T \sgn (A x + b) \in \partial h (x).
$$
```


### $\ell_2$ Norm over Affine Transformation  

```{div}
Let $A \in \RR^{m \times n}$. Let $b \in \RR^m$. 
Let $f : \RR^m \to \RR$ be given by $f(y) = \| y \|_2$.

Let $h : \RR^n \to \RR$ be the function 
$h(x) = \| A x + b \|_2 = f(A x + b)$.

We have:

$$
\partial f (Ax + b) = \begin{cases} 
\left \{ \frac{A x + b}{ \| A x + b \|_2} \right \} & \text{for} & Ax + b \neq \ZeroVec \\
B_{\| \cdot \|_2} [\ZeroVec, 1] & \text{for} & A x + b  = 0
\end{cases}.
$$

Applying the affine transformation rule, we get:


$$
\partial h (x) = A^T \partial f (Ax + b) 
= \begin{cases} 
\left \{ \frac{A^T (A x + b)}{ \| A x + b \|_2} \right \} & \text{for} & Ax + b \neq \ZeroVec \\
A^T B_{\| \cdot \|_2} [\ZeroVec, 1] & \text{for} & A x + b  = 0
\end{cases}.
$$

For $x \ST A x + b = 0$, we can write this as 

$$
\partial h (x) = A^T B_{\| \cdot \|_2} [\ZeroVec, 1] = \{A^T y \ST \| y \|_2 \leq 1 \}.
$$
```

### $\ell_{\infty}$ Norm over Affine Transformation  

```{div}
Let $A \in \RR^{m \times n}$. Let $b \in \RR^m$. 
Let $f : \RR^m \to \RR$ be given by $f(y) = \| y \|_{\infty}$.

Let $h : \RR^n \to \RR$ be the function 
$h(x) = \| A x + b \|_{\infty} = f(A x + b)$.

We use the affine transformation rule on the subdifferential of $f$ to obtain:

$$
\partial h (x) = \begin{cases} 
\left \{\sum_{i \in I(x)} \lambda_i \sgn(a_i^T x + b_i) a_i \ST 
 \sum_{i \in I(x)} \lambda_i = 1, \lambda_j \geq 0, j \in I(x) \right \},
& A x + b \neq \ZeroVec \\
A^T B_{\| \cdot \|_1} [\ZeroVec, 1], & A x + b = \ZeroVec
\end{cases}
$$
where $a_1^T, \dots, a_m^T$ are the rows of $A$ and 

$$
I(x) = \{i \ST: |A x + b |_i = \| A x + b \|_{\infty} \}.
$$
```
## Indicator Functions


```{prf:theorem} Subdifferential of indicator function
:label: res-cvxf-subdifferential-indicator 

The subdifferential of indicator function for a nonempty set $S \subset \VV$
at any point $\bx \in S$ is given by

$$
\partial \delta_S (\bx) = N_S (\bx).
$$

where $N_S (\bx)$ is the 
{prf:ref}`normal cone <def-cvx-normal-cone>` of $S$ at $\bx$.
```

```{prf:proof}
Let $\bx \in S$ and $\bg \in \partial I_S(\bx)$. 
The subgradient inequality {eq}`eq-cvxf-subgradient-inequality-2` gives us:

$$
& I_S(\bz) \geq I_S(\bx) + \langle \bz - \bx , \bg \rangle \Forall \bz \in S\\
& \iff 0 \geq 0 + \langle \bz - \bx , \bg \rangle \Forall \bz \in S\\
& \iff \langle \bz - \bx , \bg \rangle \leq 0 \Forall \bz \in S\\
& \iff \bg \in N_S (\bx).
$$
```

```{prf:example} Subdifferential of the indicator function of the unit ball 
The unit ball at origin is given by:

$$
S = B[\bzero, 1] = \{\bx \in \VV  \ST \| \bx \| \leq 1 \}.
$$

From {prf:ref}`res-cvxf-normal-cone-unit-ball`, the normal cone
of $S$ at $\bx \in S$ is given by:

$$
N_S(\bx) = \{ \by \in \VV^* \ST \| \by \|_* \leq \langle \bx, \by \rangle \}.
$$

For any $\bx \notin S$, $N_S(\bx) = \EmptySet$. Combining:


$$
\partial \delta_{B[\ZeroVec, 1]} (x) = \begin{cases} 
 \{ \by \in \VV^* \ST \| \by \|_* \leq \langle \bx, \by \rangle \} 
 & \text{for} & \| \bx \| \leq 1 \\
\EmptySet & \text{for} & \| \bx \| > 1.
\end{cases}
$$
```

## Minimization Problems

```{div}
Minimization problem:

$$
\min \{f(x) \ST g(x) \leq 0, x \in X \}.
$$

Dual function:

$$
q(\lambda) \min_{x \in X} \{L(x, \lambda) \triangleq f(x) + \lambda^T g(x)\}
$$

Assume that for $\lambda = \lambda_0$ the minimization in R.H.S. is obtained at $x = x_0$.

Subgradient of the (negative of the) dual function $-q$:

$$
- g (x_0) \in \partial (-q) (\lambda_0).
$$
```

## Maximum Eigen Value Function

```{div}
The maximum eigen value function for symmetric matrices,
denoted as $f : \SS^n \to \RR$, is given by:

$$
f(\bX) \triangleq \lambda_{\max} (\bX).
$$
```

```{prf:theorem} Subgradient for maximum eigen value function
:label: res-cvxf-sg-max-eig-val-func

Let $f : \SS^n \to \RR$ be the maximum eigen value function. 
Then

$$
\bv \bv^T \in \partial f (\bX)
$$
where $\bv$ is a normalized eigen-vector of $\bX \in \SS^n$ 
associated with its maximum eigen value.
```

```{prf:proof}
Let $\bX \in \SS^n$ be given. Let $\bv$ be a normalized eigen vector
associated with the largest eigen value of $\bX$. Then, $\| \bv \|_2  = 1$. 

For any $\bY \in \SS^n$, we have:

$$
f(\bY) &= \lambda_{\max} (\bY) \\
&= \underset{\| \bu \|_2 = 1}{\max} \{ \bu^T \bY \bu \}\\
&\geq \bv^T \bY \bv \\
&= \bv^T \bX \bv + \bv^T (\bY - \bX) \bv\\
&= \lambda_{\max} (\bX) \| \bv \|_2^2 + \Trace (\bv^T (\bY - \bX) \bv) \\
&= \lambda_{\max} (\bX) + \Trace ((\bY - \bX) \bv \bv^T ) \\
&= f (\bX) + \langle \bY - \bX,  \bv \bv^T \rangle.
$$

In this derivation, we have used the following results:

* The maximum eigen value can be obtained by maximizing $\bu^T \bY \bu$ over the unit sphere.
* For a scalar $x \in \RR$, $\bx = \Trace(x)$.
* $\Trace (AB) = \Trace (BA)$ if both $AB$ and $BA$ are well defined.
* $\langle A, B \rangle = \Trace(AB)$ for the space of symmetric matrices.

Thus, $\bv \bv^T \in \partial f(\bX)$.
```

We note here that this result only identifies one of the
subgradients of $f$ at $\bX$. It doesn't characterize
the entire subdifferential of $f$ at $\bX$. In this sense,
this result is a *weak result*. In contrast, a *strong result*
would characterize the entire subdifferential.

## The Max Function

```{div}
Let $f : \RR^n \to \RR$ be given by:

$$
f(x) = \max \{ x_1, x_2, \dots, x_n\}.
$$

Let $f_i(x) = x_i$. Then

$$
f_(x) = \max \{ f_1(x), f_2(x), \dots, f_n(x)\}.
$$

$$
\partial f_i(x) = \{ e_i\}.
$$

We denote:

$$
I (x) = \{ i \ST f(x) = x_i\}.
$$

Using the max rule for functions:

$$
\partial f (x) = \text{conv } \left ( \bigcup_{i \in I(x)} \partial f_i(x) \right )
  = \text{conv } \left ( \bigcup_{i \in I(x)} \{ e_i\} \right ).
$$
```

For the vector of all ones:

$$
\partial f (\alpha \OneVec) = \Delta_n \Forall \alpha \in \RR.
$$


## Distance from a Convex Set


Let $C \subseteq \VV$ be a nonempty closed and convex set.
The *orthogonal projection* mapping under a norm $\| \cdot \|$
is defined by:

$$
P_C(x) \triangleq \underset{y \in C}{\argmin} \| y - x \| \Forall x \in \VV. 
$$
The mapping $P_C$ is well defined (exists and unique) when
the underlying set $C$ is nonempty, closed and convex.


The distance of a point $x \in \VV$ to $C$ is defined as

$$
d_C(x) = \| x - P_C(x) \|.
$$


Let $\phi_C : \VV \to \RR$ be defined as:

$$
\phi_C(x) \triangleq \frac{1}{2} d_C^2(x) 
= \frac{1}{2}\| x - P_C(x) \|^2.
$$


The gradient of $\phi_C(x)$ is given by:

$$
\nabla \phi_C(x) = x - P_C(x)  \Forall x \in \VV.
$$

```{div}
We note that $\phi_C = g \circ d_C$ where 
$g(t) = \frac{1}{2}[t]_+^2$.

Applying chain rule:

$$
\partial \phi_C (x) = [d_C(x)]_+ \partial d_C(x) = d_C(x) \partial d_C(x).
$$

For any $x \notin C$, $d_C(x) \neq 0$, and we have:

$$
d_C(x) = \left \{ \frac{x - P_C(x)}{d_C(x)}\right \} \Forall x \notin C.
$$

$d_C$ is differentiable at $x \notin C$.


For $x \in C$:

$$
\partial d_C (x) = N_C(x) \cap B[\ZeroVec, 1].
$$

Combining cases:

$$
\partial d_C (x) = \begin{cases} 
 \left \{ \frac{x - P_C(x)}{d_C(x)}\right \}, & x \notin C\\
N_C(x) \cap B[\ZeroVec, 1], & x \in C
\end{cases}.
$$
```


## Space of Matrices

```{div}
Let $\VV = \RR^{m \times n}$. Let the standard
inner product for $x, y, \in \VV$ be 
$\langle x, y \rangle = \Trace(x^T y)$. 

Let $f : \VV \to (-\infty, \infty]$ be a proper function.
Let $x \in \interior \dom f$.

The gradient at $x$, if it exists, is given by:

$$
\nabla f(x) = D_f(x) \triangleq \left ( \frac{\partial f}{\partial x_{ij}} (x) \right)_{i,j}.
$$ 
```

Let $H$ be a positive definite matrix and define an inner 
product for $\VV$ as:

$$
\langle x, y \rangle_H \triangleq \Trace (x^T H y).
$$

Then

$$
\nabla f(x) = H^{-1} D_f(x).
$$


## Convex Piecewise Linear Function


```{div}
Let a convex piecewise linear function $f : \RR^n \to \RR$ be given by:

$$
f(x) = \underset{1 \leq i \leq m}{\max} \{a_i^T x + b_i \}.
$$

We define $f_i(x) = a_i^T x + b_i$. Then 

$$
f(x) = \underset{1 \leq i \leq m}{\max} \{ f_i(x)\}.
$$

We set:

$$
I(x) = \{i \ST f(x) = a_i^T x + b_i \}.
$$

Then we have:

$$
\partial f(x) = \left \{  \sum_{i \in I(x)} \lambda_i a_i \ST 
  \sum_{i \in I(x)} \lambda_i = 1, \lambda_j \geq 0 \Forall j \in I(x)
  \right \}
$$
```