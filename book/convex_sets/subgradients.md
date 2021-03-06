(sec:cvxf:subgradients)=
# Subgradients
Primary references for this section are
{cite}`bertsekas2003convex,beck2017first`.

Throughout this section, we assume that $\VV, \WW$ are 
finite dimensional real vector spaces. Wherever necessary, 
they are equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \|$
or an {prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle$. 
They are also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$
as needed.


## Subgradients

```{index} Subgradient
```
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

### Geometric Interpretation

```{prf:observation} Subgradient and supporting hyperplane
:label: res-cvxf-subgradient-supporting-hyperplane

Let $f: \VV \to \RERL$ be a proper function.
Then $\bg$ be a subgradient of $f$ at $\bx$
if and only if $\epi f$ has a supporting
hyperplane at $(\bx, f(\bx))$ with
a normal $(-\bg, 1)$. 

Let $H$ be a supporting hyperplane of $\epi f$ at $(\bx, f(\bx))$
with the normal $(-\bg, 1)$. 

1. Then

   $$
   H = \{ (\by, t) \ST \langle \by, -\bg \rangle  + t 
      =  \langle \bx, -\bg \rangle + f(\bx) \}.
   $$
1. For any $(\by, f(\by)) \in \epi f$, we must have

   $$
   & \langle \by, -\bg \rangle  + f(\by) 
      \geq  \langle \bx, -\bg \rangle + f(\bx) \\
   \iff & f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle.
   $$
1. Then $\bg$ is a subgradient of $f$ at $\bx$.

Now let $\bg$ be a subgradient of $f$ at $\bx$.

1. Let $(\by, t) \in \epi f$.
1. Then we have

   $$
   t \geq f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle.
   $$
1. Rearranging the terms, we have

   $$
   \langle \by, -\bg \rangle + t
   \geq \langle \bx, -\bg \rangle + f(\bx) 
   $$
   for every $(\by, t) \in \epi f$.
1. Then the hyperplane

   $$
   H = \{ (\by, t) \ST \langle \by, -\bg \rangle  + t 
      =  \langle \bx, -\bg \rangle + f(\bx) \}
   $$
   is indeed a supporting hyperplane for $\epi f$.
1. The normal vector for this hyperplane is $(-\bg, 1)$
   and it passes through the point $(\bx, f(\bx))$.
```

## Subdifferential

At a point $\bx \in \dom f$, it is possible that there are
more than one subgradients. It is thus natural to introduce
the notion of the set of all subgradients of $f$ at a specific
point $\bx \in \dom f$.

```{index} Subdifferential
```
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

```{prf:theorem} Subdifferential of norm at origin
:label: res-cvxf-subdiff-norm-origin

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

```{index} Subdifferentiability
```
```{prf:definition} Subdifferentiability
:label: def-cvxf-subdifferentiable

A proper function $f : \VV \to \RERL$ is called *subdifferentiable* 
at some $\bx \in \dom f$ if $\partial f(\bx) \neq \EmptySet$. 
```

```{index} Subdifferentiability; domain
```
```{prf:definition} Domain of subdifferentiability
:label: def-cvxf-domain-subdifferentiable

The set of points at which a proper function $f : \VV \to \RERL$ is
subdifferentiable, denoted by $\dom (\partial f)$, is defined as:

$$
\dom (\partial f) \triangleq \{\bx \in \VV \ST \partial f(\bx) \neq \EmptySet \}.
$$
```

### Closedness and Convexity

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

### Subdifferentiability and Convex Domain

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

### Positive Scaling

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

## Proper Convex Functions

In this subsection, we discuss the properties of the
subdifferential sets for proper convex functions.

A proper convex function may not be subdifferentiable
at every point in its domain. 
However, it is indeed subdifferentiable at 
the interior points and relative interior points
of its domain.

### Nonemptiness and Boundedness at Interior Points

```{prf:theorem} Nonemptiness and boundedness of the subdifferential at interior points
:label: res-cvxf-proper-interior-subdiff-nonempty-bounded

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $\ba \in \interior S$.
Then, $\partial f (\ba)$ is nonempty and bounded. 

In other words, for a proper convex function, the subdifferential
at the interior points of its domain is nonempty and bounded.
We have

$$
\interior \dom f \subseteq \dom (\partial f).
$$
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

If $f$ is a  proper convex function, then the only points
at which $f$ may not be subdifferentiable (i.e. the
subdifferential set is empty) are the points at the
frontier of $\dom f$ (i.e., $\dom f \setminus \interior \dom f$).
$f$ may be subdifferentiable on the frontier points too.


```{prf:corollary} Subdifferentiability of real valued convex functions
:label: res-cvxf-convex-subdiff-everywhere

Let $f: \VV \to \RR$ be a convex function. Then, $f$ is subdifferentiable 
over $\VV$.

$$
\dom (\partial f) = \VV.
$$
```

```{prf:proof}
We have $\dom f = \VV$.

1. Let $\bx \in \VV$.
1. $\VV$ is open in $(\VV, \| \cdot \|)$.
1. Thus, $\bx \in \interior \VV = \dom f$.
1. By {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`, 
   $\partial f(\bx)$ is nonempty and bounded as $\bx \in \interior \dom f$.
1. Hence, $f$ is subdifferentiable at $\bx$.
1. Since this is valid for every $\bx \in \VV$, hence $\dom (\partial f) = \VV$.
```

### Nonempty, Convex and Compact Subdifferentials

```{prf:theorem} Nonempty, convex and compact subdifferentials for proper convex functions
:label: res-cvxf-subdiff-proper-convex-interior

Let $f : \VV \to \RERL$ be a proper and convex function.
Let $\bx \in \interior S$. Then
$\partial f(\bx)$ is nonempty, convex and compact.
```

```{prf:proof}
Let $\bx \in \interior S$.

1. By {prf:ref}`res-cvxf-subdifferential-closed-convex`,
   $\partial f(\bx)$ is closed and convex.
1. By {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`,
   $\partial f(\bx)$ is nonempty and bounded.
1. Since $\partial f(\bx)$ is closed and bounded, hence
   it must be compact since $\VV$ is a finite dimensional normed linear space.
```

We present an alternative proof based on the min common/max crossing
framework developed in {ref}`sec:opt:duality:common:crossing`.
This proof can be skipped in first reading.

```{prf:proof}
This proof is based on 
the second min common/max crossing theorem
{prf:ref}`res-opt-min-max-strong-duality-2`.

We fix some $\bx \in \interior S$.
We construct the set $M$ as

$$
M = \{ (\bu, t) \ST \bu \in \VV, f(\bx + \bu) \leq t \}. 
$$

We first consider the min common problem.

1. Note that $(\bzero, f(\bx)) \in M$
   since $f(\bx + \bzero) \leq f(\bx)$.
1. Further see that the min common value

   $$
   p^* = \inf_{(\bzero, p) \in M} p = f(\bx).
   $$
1. Hence $p^*$ is finite.
1. Note that $\overline{M} = M$ where

   $$
   \overline{M} = \{ (\bx, t) \in \VV \oplus \RR \ST \text{ there exists } 
   \bar{t} \in \RR \text{ with } 
   \bar{t} \leq t \text{ and } (\bx, \bar{t}) \in M \}.
   $$
1. $M$ is convex.
   1. Let $(\bu_1, t_1), (\bu_2, t_2) \in M$ and let $r \in (0, 1)$.
   1. Let $(\bu, t) = r (\bu_1, t_1) + (1-r) (\bu_2, t_2)$.
   1. We have $f(\bx + \bu_1) \leq t_1$
      and $f(\bx + \bu_2) \leq t_2$.
   1. Now

      $$
      f(\bx + \bu)
      &= f(\bx + r \bu_1 + (1-r) \bu_2) \\
      &= f(r (\bx + \bu_1) + (1-r)(\bx + \bu_2)) \\
      &\leq r f(\bx + \bu_1) + (1-r) f(\bx + \bu_2) \\
      &\leq r t_1 + (1-r) t_2 = t.
      $$
   1. Hence $(\bu, t) \in M$.
   1. Hence $M$ is convex.

Next consider the max crossing problem and strong duality.
1. We have 
   
   $$
   q^* = \sup_{\ba \in \VV} q(\ba)
   $$
   where

   $$
   q(\ba) = \inf_{(\bu, t) \in M} \{ \langle \bu, \ba \rangle + t \}.
   $$
1. The set of optimal solutions of the max crossing problem
   is given by

   $$
   Q^* = \{ \ba \in \VV \ST q(\ba) = q^* \}
   $$
1. For some $\ba \in Q^*$, we can attain strong duality with

   $$
   p^* = q^* = q(\ba)
   $$
   if and only if

   $$
   f(\bx) = \inf_{(\bu, t) \in M} \{ \langle \bu, \ba \rangle + t \}.
   $$
1. Equivalently

   $$
   f(\bx) \leq f(\bx + \bu) + \langle \bu, \ba \rangle \Forall \bu \in \VV.
   $$
1. Equivalently

   $$
   f(\bx + \bu) \geq f(\bx) + \langle \bu, -\ba \rangle \Forall \bu \in \VV.
   $$
1. But this is nothing but the subgradient inequality with $-\ba$
   as the subgradient at $\bx$.
1. In other words, strong duality is attained at $\ba$ as a solution
   of the max crossing problem if and only if
   $-\ba$ is a subgradient of $f$.
1. Hence $Q^*$ with strong duality
   is given by $-\partial f(\bx)$.

We next establish the conditions for the
second min common/max crossing theorem
{prf:ref}`res-opt-min-max-strong-duality-2`

1. Consider the set

   $$
   D = \{ \bu \in \VV \ST \text{ there exists } 
   t \in \RR \text{ with }  (\bu, t) \in M \}.
   $$
1. It is easy to see that $D = S - \bx$.
   1. Consider the set $T = S - \bx$.
   1. Let $\bu \in T$.
   1. Then $\bx + \bu \in S$.
   1. Hence $f(\bx + \bu) \leq f(\bx + \bu)$.
   1. Hence $(\bu, f(\bx + \bu)) \in M$.
   1. Hence $\bu \in D$.
   1. Hence $T = S - \bx \subseteq D$.
   1. Let $\bu \notin T$.
   1. Then $\bu + \bx \notin S$.
   1. Hence $f(\bu + \bx) = \infty$.
   1. Hence for every $t \in \RR$, $f(\bu + \bx) > t$.
   1. Hence $(\bu, t) \notin M$ for every $t \in \RR$.
   1. Hence $\bu \notin D$.
   1. Hence $D = T = S - \bx$. 
1. Since $\bx \in \interior S$, hence $\bzero \in \interior D$.
1. We see that all the conditions of the second min common/max crossing
   theorem are satisfied.
   1. $p^*$ is finite.
   1. $\overline{M} = M$ is convex.
   1. The set $D$ contains $\bzero$ in its interior.
1. Hence $-\partial f(\bx)$ is nonempty, convex and compact.
1. Hence $\partial f(\bx)$ is also nonempty, convex and compact.
```

### Subgradients over a Compact Set

```{prf:theorem} Subgradients over a compact set are nonempty and bounded
:label: res-cvxf-subg-compact-nonempty-bounded

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $A \subseteq \interior S$ be a nonempty and compact
subset of the interior of the domain of $f$. Then, the 
set of subgradients over $A$ given by

$$
Y = \bigcup_{\bx \in A} \partial f(\bx)
$$
is nonempty and bounded.
```

```{prf:proof}
We are given that $A$ is nonempty and compact subset of interior of domain of $f$.

1. For any $\bx \in A$, 
   by {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`,
   $\partial f(\bx)$ is nonempty and bounded.
1. Thus, $Y$ is nonempty.

We next prove that $Y$ must be bounded also.

1. Let $T = \VV \setminus (\interior S)$.
1. $T$ is closed and $A$ is closed. $A \subseteq \interior S$. 
   Hence, $A \cap T = \EmptySet$.
1. Since $A$ is compact and $T$ is closed and $A \cap T = \EmptySet$, 
   hence distance between $A$ and $T$ is nonzero
   due to {prf:ref}`res-ms-dist-disjoint-compact-closed`.

   $$
   r = d(A, T) > 0. 
   $$
1. Thus, 

   $$
   \| \bx - \by \| \geq r \Forall \bx \in A, \by \notin \interior S.
   $$
1. Let $s = \frac{r}{2}$.
1. Let $D = B[\bzero, s]$. $D$ is a closed and bounded
   set. Hence, it is compact 
   due to {prf:ref}`res-la-ndim-compact-closed-bounded`.
1. Let $E = A + D$. Then $E \subseteq \interior S$.
   1. Let $\by \in E$.
   1. Then, there is $\bx \in A$ and $\bv \in D$ such that
      $\by = \bx + \bv$.
   1. Thus, $\by - \bx = \bv$. 
   1. Hence $\| \by - \bx \| \leq s < r$.
1. Since both $A$ and $D$ are compact, hence $E$ is compact
   due to {prf:ref}`res-la-ndim-sum-compact`.
1. By {prf:ref}`res-cvxf-convex-local-lipschitz-continuous`, $f$
   is local Lipschitz continuous at every $\bx \in E$
   since $\bx \in E \subseteq \interior S$.
1. Then, by {prf:ref}`res-ms-compact-llc-lipschitz`,
   $f$ is Lipschitz continuous on $E$.
1. Thus, there exists $L > 0$ such that 

   $$
   |f(\bx) - f(\by)| \leq L \| \bx - \by \| \Forall \bx, \by \in E.
   $$
1. Let $\bg \in Y$. Then, there is $\bx \in A$ such that
   $\bg \in \partial f(\bx)$.
1. we can choose $\bg^{\perp} \in \VV$ such that

   $$
   \| \bg \|_* = \langle \bg^{\perp}, \bg \rangle
   \text{ and }
   \| \bg^{\perp} \| = 1.
   $$
1. Now, let $\by = \bx + s \bg^{\perp}$. Then, $\by \in E$.
   1. $ \| \by - \bx \| = \| s \bg^{\perp}\| = s$.
   1. Thus, $s \bg^{\perp} \in D$.
   1. Thus, $\by \in E$ since $\bx \in A$.
1. Also, $\bx \in E$ since $\bx = \bx + \bzero$ and $\bzero \in D$.
1. Consequently, by Lipschitz continuity

   $$
   |f(\by) - f(\bx)| \leq L \| \by - \bx \| = L s.
   $$
1. By subgradient inequality at $\bx$
 
   $$
   f(\by) - f(\bx) \geq \langle \by - \bx, \bg \rangle
   = s \langle \bg^{\perp}, \bg \rangle
   = s \| \bg \|_*.
   $$
1. Using the Lipschitz bound above, we get

   $$
   s \| \bg \|_* \leq L s.
   $$
1. Thus, $\| \bg \|_* \leq L$.
1. Since $\bg$ was chosen arbitrarily, hence $Y$ is bounded.
```

We recall from {prf:ref}`def-cvx-relative-interior`
that the relative interior of a convex set is given by

$$
\relint C = \{\bx \in C \ST \exists r > 0, 
B(\bx, r) \cap \affine C \subseteq C \}.
$$
It is interior of the convex set w.r.t. the 
subspace topology of its affine hull.

### Nonempty Subdifferential at Relative Interior Points

```{prf:theorem} Nonemptiness of the subdifferential at relative interior points
:label: res-cvxf-relint-subdiff-nonempty

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $\bx \in \relint S$.
Then, $\partial f (\bx)$ is nonempty and has the form

$$
\partial f(\bx) = L^{\perp} + G
$$
where $L$ is the subspace that is parallel to $\affine S$
and $G$ is a nonempty and compact set.

In other words, for a proper convex function, the subdifferential
at the relative interior points of its domain is nonempty.
We have

$$
\relint \dom f \subseteq \dom (\partial f).
$$
```
The proof is based on the min common/max crossing
framework developed in {ref}`sec:opt:duality:common:crossing`.
It can be skipped in first reading.
It follows the proof of {prf:ref}`res-cvxf-subdiff-proper-convex-interior`.

```{prf:proof}
This proof is based on 
the second min common/max crossing theorem
{prf:ref}`res-opt-min-max-strong-duality-2`.

We fix some $\bx \in \relint S$.
We construct the set $M$ as

$$
M = \{ (\bu, t) \ST \bu \in \VV, f(\bx + \bu) \leq t \}. 
$$
We have already established the following in the proof of
{prf:ref}`res-cvxf-subdiff-proper-convex-interior`:
1. $M$ is convex.
1. $\overline{M} = M$.
1. $p^* = f(\bx)$.
1. $p^*$ is finite.
1. $q^* = \sup_{\ba \in \VV} q(\ba)$
   where

   $$
   q(\ba) = \inf_{(\bu, t) \in M} \{ \langle \bu, \ba \rangle + t \}.
   $$
1. $Q^* = \{ \ba \in \VV \ST q(\ba) = q^* \}$.
1. When the strong duality holds, then

   $$
   Q^* = -\partial f(\bx).
   $$
1. The set

   $$
   D = \{ \bu \in \VV \ST \text{ there exists } 
   t \in \RR \text{ with }  (\bu, t) \in M \}
   = S - \bx.
   $$

Continuing further

1. Since $\bx \in \relint S$, hence $\bzero \in \relint D$.
1. Hence $\affine D = \affine S - \bx = L$.
1. Hence by the second min common/max crossing theorem

   $$
   -\partial f(\bx) = Q^* = L^{\perp} + \tilde{Q}
   $$
   where $\tilde{Q}$ is a nonempty, convex and compact set.
1. Negating on both sides, we obtain

   $$
   \partial f(\bx) = L^{\perp} + G
   $$
   where $G$ is a nonempty, convex and compact set.
```


```{prf:corollary} Existence of points with nonempty subdifferential
:label: res-cvxf-subdiff-exist-relint

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Then, there exists $\bx \in S$ such that $\partial f(\bx)$
is nonempty.
```

```{prf:proof}
The effective domain of a proper convex function
is convex and nonempty.

1. By {prf:ref}`res-cvx-nonempty-relint`, the relative
   interior of $S = \dom f$ is nonempty.
1. Thus, there exists $\bx \in S$.
1. By {prf:ref}`res-cvxf-relint-subdiff-nonempty`, 
   $\partial f(\bx)$ is nonempty.
```

### Unbounded Subdifferential

```{prf:theorem} Unboundedness condition for subdifferential
:label: res-cvxf-subdiff-relint-unbounded

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.

Assume that $\dim S < \dim \VV$.
Let $\bx \in S$. 
If $\partial f(\bx) \neq \EmptySet$, then 
$\partial f(\bx)$ is unbounded.
```

```{prf:proof}

We proceed as follows.

1. Let $n = \dim \VV$.
1. Let $A = \affine S$. $A$ is an affine set.
1. We have $\bx \in S \subseteq A$.
1. Then, $\WW = A - \bx$ is the subspace parallel to $A$.
1. Accordingly, $m = \dim \WW < \dim \VV = n$.
1. Then, the orthogonal complement of $\WW$ is a nontrivial subspace with dimension $n -m$.
1. Let $\bv \in \WW^{\perp}$ be a nonzero vector.
1. Then, $\langle \bw, \bv \rangle = 0$ for every $\bw \in \WW$.
1. Now let $\bg \in \partial f(\bx)$ be an arbitrary subgradient at $\bx$.
1. By subgradient inequality

   $$
   f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle  \Forall \by \in S.
   $$
1. Note that both $\bx \in S$ and $\by \in S$. 
1. Hence, $\by - \bx \in \WW$.
1. Thus, $\langle \by - \bx, \bv \rangle = 0$.
1. But then, for any $\alpha \in \RR$,

   $$
   \langle \by - \bx, (\bg + \alpha \bv) \rangle
   &= \langle \by - \bx, \bg \rangle + \alpha \langle \by - \bx, \bv \rangle\\
   &= \langle \by - \bx, \bg \rangle.
   $$
1. Thus, if $\bg \in \partial f(\bx)$, then $\bg + \alpha \bv \in \partial f(\bx)$
   for every $\alpha \in \RR$.
1. Thus, $\partial f(\bx)$ is unbounded.
```


## Directional Derivatives

The directional derivative of a proper convex function
is closely linked with its subdifferential.
To see this, let $\bx \in \interior \dom f$,
let $\bd \in \VV$ be a nonzero direction
and $t > 0$.
Let $\bg \in \partial f(\bx)$
and consider the subgradient inequality

$$
f(\bx + t \bd) \geq f(\bx) + \langle t \bd, \bg \rangle.
$$
Hence

$$
\frac{f(\bx + t \bd) - f(\bx)}{t} \geq \langle \bd, \bg \rangle
$$
We saw in {prf:ref}`res-cvxf-dir-der-infimum` that
$\frac{f(\bx + t \bd) - f(\bx)}{t}$ is a nondecreasing
quantity and

$$
f'(\bx; \bd) = \inf_{t > 0} \frac{f(\bx + t \bd) - f(\bx)}{t}.
$$
This establishes the basic relation

```{math}
:label: eq-cvxf-subg-dir-der-inequality
f'(\bx; \bd) \geq  \langle \bd, \bg \rangle
```
for every $\bg \in \partial f(\bx)$.
In fact a stronger result is available in the form of
max formula.

### Max Formula

The max formula is one of the key results in this section.
It connects subgradients with directional derivatives.

```{prf:theorem} Max formula
:label: res-cvxf-subg-dir-der-max-formula

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Then for any $\bx \in \interior S$ and $\bd \in \VV$,

$$
f'(\bx;\bd) = \sup \{ \langle \bd, \bg \rangle \ST \bg \in \partial f(\bx) \}.
$$
In words, the directional derivative is the supremum of the
inner product of the subgradients with the direction.
```

```{prf:proof}

Let $\bx \in \interior S$ and $\bd \in \VV$.

1. Let $t > 0$. Then, by subgradient inequality

   $$
   f(\bx + t \bd) - f(\bx) \geq \langle t \bd , \bg \rangle 
   \Forall \bg \in \partial f(\bx).
   $$
1. Thus,

   $$
   \frac{f(\bx + t \bd) - f(\bx)}{t} \geq \langle \bd , \bg \rangle 
   \Forall \bg \in \partial f(\bx).
   $$
1. Taking the limit 

   $$
   f'(\bx; \bd) = \lim_{t \to 0^+} \frac{f(\bx + t \bd) - f(\bx)}{t} 
   \geq \lim_{t \to 0^+} \langle \bd , \bg \rangle 
   = \langle \bd , \bg \rangle  
   $$
   for every $\bg \in \partial f(\bx)$.
1. Taking the supremum over $\partial f(\bx)$ on the R.H.S., we obtain

   $$
   f'(\bx;\bd) \geq\sup \{ \langle \bd, \bg \rangle \ST \bg \in \partial f(\bx) \}.
   $$

We now show that the inequality is indeed an equality.

1. Let $h : \VV \to \RR$ be given by

   $$
   h(\bv) = f'(\bx; \bv).
   $$
1. By {prf:ref}`res-cvxf-dir-der-convex-homo`, $h$ is a real valued convex
   function and nonnegative homogeneous.
1. By {prf:ref}`res-cvxf-convex-subdiff-everywhere`, $h$ is 
   subdifferentiable everywhere in $\VV$.
1. In particular, $h$ is subdifferentiable at $\bd$.
1. Let $\bg \in \partial h(\bd)$.
1. For any $\bv \in \VV$ and $t \geq 0$, 

   $$
   t f'(\bx; \bv) = t h(\bv) = h (t \bv)
   $$
   since $h$ is nonnegative homogeneous.
1. By subdifferential inequality
   
   $$
   t f'(\bx; \bv) &= h(t \bv)\\ 
   &\geq h(\bd) + \langle t \bv - \bd , \bg \rangle\\
   &=f'(\bx; \bd) + \langle t \bv - \bd , \bg \rangle.
   $$
1. Rearranging the terms,

   $$
   t (f'(\bx; \bv) - \langle \bv, \bg \rangle) \geq
   f'(\bx; \bd) - \langle \bd, \bg \rangle.
   $$
1. Since this inequality is valid for every $t \geq 0$, 
   hence the term $f'(\bx; \bv) - \langle \bv, \bg \rangle$ 
   must be nonnegative. 
   Otherwise, the inequality will be invalided for large enough $t$.
   Thus,

   $$
   f'(\bx; \bv) \geq \langle \bv, \bg \rangle.
   $$
1. By {prf:ref}`res-cvxf-dir-der-underestimator`, for any $\by \in S$,

   $$
   f(\by) \geq f(\bx) + f'(\bx; \by - \bx).
   $$
1. From previous inequality, 

   $$
   f'(\bx; \by - \bx) \geq \langle \by - \bx, \bg \rangle.
   $$
1. Thus, for any $\by \in S$,

   $$
    f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle.
   $$
1. But this is a subgradient inequality. 
   Hence, $\bg \in \partial f(\bx)$.
1. Taking $t=0$, in the subgradient inequality for $h$, 

   $$
   0 \geq f'(\bx; \bd) - \langle \bd, \bg \rangle. 
   $$
1. Thus, there exists $\bg \in \partial f(\bx)$ such that

   $$
   f'(\bx; \bd) \leq \langle \bd, \bg \rangle.
   $$
1. Consequently,

   $$
   f'(\bx;\bd) \leq\sup \{ \langle \bd, \bg \rangle \ST \bg \in \partial f(\bx) \}.
   $$

Combining the two inequalities, we obtain the max formula:

 $$
 f'(\bx;\bd) = \sup \{ \langle \bd, \bg \rangle \ST \bg \in \partial f(\bx) \}.
 $$
```

Recall from {prf:ref}`def-cvxf-support-function` that 
support function for a set $C$ is given by

$$
\sigma_C (\bx) =  \sup \{\langle \bx, \by \rangle \ST \by \in C \}.
$$


```{prf:corollary} Max formula as a support function
:label: res-cvxf-dir-der-subg-support

The max formula can be written as

$$
f'(\bx;\bd) =  \sigma_{\partial f(\bx)} (\bd).
$$
```

## Differentiability


### Subdifferential and gradient

```{prf:theorem} Subdifferential at points of differentiability
:label: res-cvxf-subdiff-grad

Let $f : \VV \to \RERL$ be a proper convex function with $S = \dom f$.
Let $\bx \in \interior S$. 

Then $f$ is differentiable at $\bx$ if and only if

$$
\partial f(\bx) = \{ \nabla f (\bx) \}.
$$

In other words, if $f$ is differentiable at $\bx$ then
its subdifferential is a singleton set consisting of the
gradient and if the subdifferential at $\bx$ is a singleton, then
$f$ is differentiable at $\bx$.
```

```{prf:proof}

Assume that $f$ is differentiable at $\bx$.

1. Let $\bd \in \VV$ be some direction.
1. By {prf:ref}`res-cvxf-grad-dir-der`, 
   
   $$
   f'(\bx; \bd) = \langle \bd, \nabla f(\bx) \rangle.
   $$
1. By {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`,
   $f$ is subdifferentiable at $\bx$ since $f$ is convex
   and $\bx \in \interior S$.
1. Let $\bg \in \partial f(\bx)$.
1. By the max formula ({prf:ref}`res-cvxf-subg-dir-der-max-formula`):

   $$
   f'(\bx;\bd) \geq \langle \bd, \bg \rangle
   $$
   as the directional derivative is the supremum of the
   inner product of the subgradients with the direction.
1. Thus, 

   $$
   \langle \bd, \nabla f(\bx) \rangle \geq \langle \bd, \bg \rangle.
   $$
1. In turn,

   $$
   \langle \bd, \bg - \nabla f(\bx) \rangle \leq 0.
   $$
   This holds for every $\bd \in \VV$.
1. By the definition of {prf:ref}`dual norm  <res-la-rip-dual-norm>`

   $$
   \| \bg - \nabla f(\bx) \|_* = \underset{\| \bd \| \leq 1}{\sup} 
    \{ \langle \bd, \bg - \nabla f(\bx) \rangle \}.
   $$
1. Using the previous inequality

   $$
   \| \bg - \nabla f(\bx) \|_* \leq 0.
   $$
1. Since, dual norm is a norm, hence it cannot be negative. Thus,

   $$
   \| \bg - \nabla f(\bx) \|_* = 0
   $$
1. Moreover, due to positive definiteness of a norm

   $$
   \bg - \nabla f(\bx) = \bzero
   $$
   must hold true.
1. Thus, $\bg = \nabla f(\bx)$.
1. In other words, if $\bg$ is a subgradient to $f$ at $\bx$,
   then it must equal $\nabla f(\bx)$.
1. Thus, the only subgradient for $f$ at $\bx$ is $\nabla f(\bx)$.
1. Thus,

   $$
   \partial f(\bx) = \{ \nabla f(\bx) \}.
   $$

For the converse, assume that $f$ is subdifferentiable at $\bx$
with $\partial f(\bx) = \{ \bg \}$.

1. By the subgradient inequality

   $$
   f(\bx + \bu) \geq f(\bx) + \langle \bu, \bg \rangle \Forall \bu \in \VV.
   $$
1. Thus,

   $$
   f(\bx + \bu) - f(\bx) - \langle \bu, \bg \rangle \geq 0 \Forall \bu \in \VV.
   $$   
1. Define a function $h : \VV \to \RERL$ as 

   $$
   h(\bu) \triangleq f(\bx + \bu) - f(\bx) - \langle \bu, \bg \rangle.
   $$
1. We list some properties of $h$.
   1. By definition $h(\bu) \geq 0$ for every $\bu \in \VV$.
   1. $h$ is a convex function since $f(\bx + \bu)$ is convex, 
      $\langle \bu, \bg \rangle$ is linear and
      $f(\bx)$ is a constant (w.r.t. the variable $\bu$).
   1. $\dom h = \dom f - \bx = S - \bx$.
   1. Thus, since $\bx \in \interior S$,
      hence $\bzero = \bx - \bx \in \interior \dom h$.
   1. $h(\bzero) = f(\bx) - f(\bx) - \langle \bzero, \bg \rangle = 0$.
1. If we are able to show that

   $$
   \lim_{\bu \to \bzero}\frac{h(\bu)}{\| \bu \|} = 0
   $$
   then, by the definition of gradient
   ({prf:ref}`def-cvxf-differentiability-proper`),

   $$
   \bg = \nabla f(\bx).
   $$
1. We can easily show that $\partial h(\bzero) = \{ \bzero \}$.
   1. If $\tilde{\bg}$ is a subgradient of $h$ at $\bzero$, 
      then by subgradient inequality

      $$
      h(\bu) \geq h(\bzero) + \langle \bu, \tilde{\bg} \rangle
      = \langle \bu, \tilde{\bg} \rangle
      \Forall \bu \in \VV.
      $$
   1. Then, $\tilde{\bg} = \bzero$ satisfies this inequality
      since $h(\bu) \geq 0$ by definition.
   1. For contradiction, assume a nonzero $\tilde{\bg}$ can satisfy this inequality.
   1. Then,

      $$
       & h(\bu) \geq  \langle \bu, \tilde{\bg} \rangle \\
       & \iff f(\bx + \bu) - f(\bx) - \langle \bu, \bg \rangle \geq \langle \bu, \tilde{\bg} \rangle \\
       & \iff f(\bx + \bu) \geq f(\bx) + \langle \bu, \tilde{\bg} + \bg \rangle \\
       & \iff \tilde{\bg} + \bg \in \partial f(\bx).
      $$
   1. This contradicts the hypothesis that the subgradient of $f$ at $\bx$ is $\{ \bg \}$.
   1. Thus, $\partial h(\bzero) = \{ \bzero \}$.
1. Then, max formula ({prf:ref}`res-cvxf-subg-dir-der-max-formula`):

   $$
   h'(\bzero; \bd) = \sigma_{\partial h (\bzero)} (\bd)
   = \langle \bd, \bzero \rangle = 0.
   $$
1. Thus, from the definition of
   {prf:ref}`directional derivatives <def-cvxf-directional-derivative>`

   $$
   0 = h'(\bzero; \bd) 
   = \lim_{\alpha \to 0^+} \frac{h(\alpha \bd) - h(\bzero)}{\alpha}
   = \lim_{\alpha \to 0^+} \frac{h(\alpha \bd)}{\alpha}.
   $$
1. Let us now introduce an orthonormal basis for $\VV$ as
   $\{\be_1, \dots, \be_n \}$.
1. Assume that $\VV$ has been equipped with various
   $\ell_p$ norms as described in {prf:ref}`rem-cvx-nd-space-norms`.
1. Since $\bzero \in \interior \dom h$, there exists
   $r \in (0, 1)$ such that

   $$
   B_1[\bzero, r] \subseteq \dom h.
   $$
1. It is a cross polytope of radius $r$ with $2n$ vertices given by
   $\{\pm r \be_i \}_{i=1}^n$.

   $$
   B_1[\bzero, r] = \convex \{\pm r \be_i \}_{i=1}^n.
   $$
1. Let us denote these $2n$ vectors as 
   $\bw_1, \dots, \bw_{2n}$.
1. By {prf:ref}`rem-cvx-nd-space-norms`

   $$
   B[\bzero, s] = B_2[\bzero, s] \subseteq B_1[\bzero, r]
   $$
   where $s = \frac{r}{\sqrt{n}}$.
1. Let $\bu \in B[\bzero, s^2]$ be a nonzero vector.
1. Since $r < 1$, hence $s < 1$, hence $s^2 < s$.
1. Let $\bv = s \frac{\bu}{\| \bu \|}$.
1. Then, $\bv \in B[\bzero, s] \subseteq B_1[\bzero, r]$.
1. Thus, $\bv \in \convex \{\bw_i \}_{i=1}^n$. 
1. Thus, there exists $\bt \in \Delta_{2 n}$ such that

   $$
   s \frac{\bu}{\| \bu \|} = \bv  = \sum_{i=1}^{2n} t_i \bw_i.
   $$
1. Then,

   $$
   \frac{h(\bu)}{\| \bu \|}
   &= \frac{h\left ( \frac{\| \bu \|}{s}  s \frac{\bu}{\| \bu \|} \right ) }{\| \bu \|} & \\
   &= \frac{h \left ( \sum_{i=1}^{2n} t_i \frac{\| \bu \|}{s} \bw_i  \right ) }{\| \bu \|} &  \text{convex combination} \\
   &\leq \sum_{i=1}^{2n} t_i \frac{h \left ( \| \bu \| \frac{\bw_i}{s}   \right ) }{\| \bu \|} & h \text{ is convex and } \bt \in \Delta_{2 n}\\
   &\leq \underset{i=1,\dots, 2n}{\max} \left \{
    \frac{h \left ( \| \bu \| \frac{\bw_i}{s}   \right ) }{\| \bu \|}
  \right \} & \text{since } \sum t_i = 1.
   $$
   Note that $\| \bu \| \frac{\bw_i}{s} \in B[\bzero, s] \subseteq B_1[\bzero, r] \subseteq \dom h$.
1. Now,

   $$
   \lim_{\bu \to \bzero} \frac{h \left ( \| \bu \| \frac{\bw_i}{s}   \right ) }{\| \bu \|}
   = \lim_{ \| \bu \| \to 0} \frac{h \left ( \| \bu \| \frac{\bw_i}{s}   \right ) }{\| \bu \|}
   =  \lim_{ \alpha \to 0^+} \frac{h \left ( \alpha \frac{\bw_i}{s}   \right ) }{\alpha}
   = 0.  
   $$
1. Thus, 
   
   $$
   \lim_{\bu \to \bzero} \frac{h(\bu)}{\| \bu \|} = 0.
   $$
1. Thus, $\bg = \nabla f(\bx)$ as desired.

```


## Subdifferential Calculus

### Function Sums

```{prf:theorem} Subdifferential subadditivity with sum of functions
:label: res-cvxf-subdiff-function-sum

Let $f_1, f_2 : \VV \to \RERL$ be proper functions
with $S_1 = \dom f_1$ and $S_2 = \dom f_2$.
For any $\bx \in S_1 \cap S_2$

$$
\partial f_1(\bx) + \partial f_2(\bx) \subseteq \partial (f_1 + f_2)(\bx).
$$
```

```{prf:proof}
Let $f = f_1 + f_2$.
We note that $\dom f = \dom (f_1 + f_2) = \dom f_1 \cap \dom f_2 = S_1 \cap S_2$.

1. Let $\bx \in S_1 \cap S_2$.
1. Let $\bg \in \partial f_1(\bx) + \partial f_2(\bx)$.
1. Then, there exist $\bg_1 \in \partial f_1(\bx)$ and $\bg_2 \in \partial f_2(\bx)$ 
   such that $\bg = \bg_1 + \bg_2$.
1. Then, by subgradient inequality, for any $\by \in S_1 \cap S_2$

   $$
   &f_1(\by) \geq f_1(\bx) + \langle \by - \bx , \bg_1 \rangle, \\
   &f_2(\by) \geq f_2(\bx) + \langle \by - \bx , \bg_2 \rangle.
   $$
1. Summing the two inequalities, we get 

   $$
   f_1(\by) + f_2(\by) \geq f_1(\bx) + f_2(\bx) + \langle \by - \bx , \bg_1 + \bg_2 \rangle.
   $$
1. Rewriting, for every $\by \in \dom f$

   $$
   (f_1 + f_2)(\by) \geq (f_1 + f_2)(\bx) + \langle \by - \bx , \bg \rangle.
   $$
1. Thus, $\bg = \bg_1 + \bg_2 \in \partial (f_1 + f_2)(\bx)$ = \partial f (\bx).
1. Thus, $\partial f_1(\bx) + \partial f_2(\bx) \subseteq \partial f(\bx)$.
```

We can generalize this result for a finite sum of functions
using simple mathematical induction.

```{prf:corollary} Weak sum rule of subdifferential calculus
:label: res-cvxf-subdiff-weak-sum-rule

Let $f_1, \dots, f_m : \VV \to \RERL$ be proper functions.
For any $\bx \in \cap_{i=1}^m \dom f_i$

$$
\sum_{i=1}^m \partial f_i(\bx) \subseteq 
\partial \left ( \sum_{i=1}^m f_i \right )(\bx).
$$
```


```{prf:theorem} Subdifferential additivity with sum of convex functions
:label: res-cvxf-subdiff-function-sum-convex

Let $f_1, f_2 : \VV \to \RERL$ be proper convex functions
with $S_1 = \dom f_1$ and $S_2 = \dom f_2$.
For any $\bx \in \interior S_1 \cap \interior S_2$

$$
\partial (f_1 + f_2) (\bx) = \partial f_1(\bx) + \partial f_2(\bx).
$$
```

```{prf:proof}
With $f = f_1 + f_2$,
by {prf:ref}`res-ms-int-intersect-int`, 

$$
\interior \dom f = \interior (S_1 \cap S_2) = \interior S_1 \cap \interior S_2.
$$

1. Let $\bx \in \interior S_1 \cap \interior S_2$. 
1. Thus, $\bx \in \interior \dom f$.
1. By {prf:ref}`max formula <res-cvxf-subg-dir-der-max-formula>`,
   for any $\bd \in \VV$,

   $$
   f'(\bx;\bd) = \sup \{ \langle \bd, \bg \rangle \ST \bg \in \partial f(\bx) \}
   = \sigma_{\partial f(\bx)}(\bd).
   $$
1. Since directional derivative is additive, hence

   $$
   f'(\bx;\bd) = f'_1(\bx;\bd) + f'_2(\bx;\bd).
   $$
1. Expanding on this

   $$
   \sigma_{\partial f(\bx)} (\bd) &= f'(\bx;\bd)\\
   &= f'_1(\bx;\bd) + f'_2(\bx;\bd)\\
   &= \sup \{ \langle \bd, \bg_1 \rangle \ST \bg_1 \in \partial f_1(\bx) \}
   + \sup \{ \langle \bd, \bg_1 \rangle \ST \bg_2 \in \partial f_2(\bx) \}\\
   &= \sup \{ \langle \bd, \bg_1 + \bg_2 \rangle \ST \bg_1 \in \partial f_1(\bx) 
      , \bg_2 \in \partial f_2(\bx) \}\\
   &= \sup \{ \langle \bd, \bg \rangle \ST \bg \in \partial f_1(\bx) 
      + \partial f_2(\bx) \}\\
   &= \sigma_{\partial f_1(\bx) + \partial f_2(\bx)} (\bd).
   $$
1. In summary, for every $\bd \in \VV$, 

   $$
   \sigma_{\partial f(\bx)} (\bd) = 
   \sigma_{\partial f_1(\bx) + \partial f_2(\bx)} (\bd).
   $$

1. By {prf:ref}`res-cvxf-subdifferential-closed-convex`,
   $\partial f(\bx)$, $\partial f_1(\bx)$ and $\partial f_2(\bx)$
   are closed and convex.
1. By {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`,
   $\partial f(\bx)$, $\partial f_1(\bx)$ and $\partial f_2(\bx)$
   are nonempty and bounded.
1. Since $\partial f_1(\bx)$ and $\partial f_2(\bx)$ are
   closed and bounded, hence they are compact ($\VV$ is finite dimensional).
1. Thus, $\partial f_1(\bx) + \partial f_2(\bx)$ is also
   closed, bounded, convex and nonempty.
1. Thus, both $\partial f(\bx)$ and $\partial f_1(\bx) + \partial f_2(\bx)$
   are nonempty, convex and closed.
1. Then, due to {prf:ref}`res-cvxf-support-func-equality-convex`,

   $$
   \partial f(\bx) = \partial f_1(\bx) + \partial f_2(\bx).
   $$
```


We can generalize this result for a finite sum of proper convex functions
using simple mathematical induction.

```{prf:corollary} Sum rule of subdifferential calculus for proper convex functions at interior points
:label: res-cvxf-subdiff-sum-rule-proper-convex

Let $f_1, \dots, f_m : \VV \to \RERL$ be proper convex functions.
For any $\bx \in \cap_{i=1}^m \interior \dom f_i$

$$
\sum_{i=1}^m \partial f_i(\bx) = 
\partial \left ( \sum_{i=1}^m f_i \right )(\bx).
$$
```

For real valued convex functions, the domain is the entire $\VV$
and interior of $\VV$ is $\VV$ itself.

```{prf:corollary} Sum rule of subdifferential calculus for real valued convex functions
:label: res-cvxf-subdiff-sum-rule-rv-convex

Let $f_1, \dots, f_m : \VV \to \RR$ be real valued convex functions.
For any $\bx \in \VV$

$$
\sum_{i=1}^m \partial f_i(\bx) = 
\partial \left ( \sum_{i=1}^m f_i \right )(\bx).
$$
```

A more powerful result with less restrictive assumptions than
{prf:ref}`res-cvxf-subdiff-sum-rule-proper-convex` is possible
if the intersection of the relative interiors of the domains
of the individual functions is nonempty.


```{prf:theorem} Sum rule of subdifferential calculus for proper convex functions
:label: res-cvxf-subdiff-sum-rule-relint

Let $f_1, \dots, f_m : \VV \to \RERL$ be proper convex functions.
Assume that $\bigcap_{i=1}^m \relint \dom f_i \neq \EmptySet$.
Then for any $\bx \in \VV$

$$
\sum_{i=1}^m \partial f_i(\bx) = 
\partial \left ( \sum_{i=1}^m f_i \right )(\bx).
$$
```


###  Linear Transformations

```{div}
Our interest here is in compositions of the
form $h = f \circ \bAAA$ where $\bAAA$ is a linear transformation.
In other words $h (\bx) = f (\bAAA(\bx))$.

If $\bAAA : \VV \to \WW$ is a linear transformation
then $\bAAA^T : \WW^* \to \VV^*$ is a mapping from 
$\WW^*$ to $\VV^*$ and satisfies the relationship:

$$
\langle \bAAA (\bx), \by \rangle = \langle \bx, \bAAA^T (\by) \rangle.
$$

From the definition of directional derivative, we have

$$
h'(\bx; \bd) 
&= \lim_{t \downarrow 0} \frac{h(\bx + t \bd) - h(\bx)}{t} \\
&= \lim_{t \downarrow 0} \frac{f(\bAAA(\bx + t \bd)) - f(\bAAA(\bx))}{t}\\
&= \lim_{t \downarrow 0} \frac{f(\bAAA(\bx) + t \bAAA(\bd)) - f(\bAAA(\bx))}{t}\\
&= f'(\bAAA(\bx); \bAAA(\bd)).
$$
```

```{prf:theorem} Weak linear transformation rule of subdifferential calculus
:label: res-cvxf-subdiff-weak-rule-linear


Let $f: \WW \to \RERL$ be a proper function.
Let $\bAAA : \VV \to \WW$ be a linear transformation.
Define $h : \VV \to \RERL$ as 

$$
h (\bx) = f (\bAAA(\bx)).
$$

Assume that $h$ is proper, i.e. $\dom h$ is not empty: 

$$
\dom h = \{ \bx \in \VV \ST \bAAA(\bx) \in \dom f\} \neq \EmptySet.
$$

Then, for any $\bx \in \dom h$

$$
\bAAA^T (\partial f (\bAAA(\bx))) \subseteq \partial h(\bx).
$$
```

```{prf:proof}
We proceed as follows.

1. Let $\bx \in \dom h$. 
1. Let $\bg \in \partial f(\bAAA(\bx))$.
1. By {prf:ref}`res-cvxf-subg-dir-der-max-formula`,
   
   $$
   \langle \bz, \bg \rangle \leq f'(\bAAA(\bx); \bz)
   \Forall \bz \in \WW.
   $$
1. Choosing $\bz = \bAAA(\bd)$, we have

   $$
   \langle \bAAA(\bd), \bg \rangle \leq f'(\bAAA(\bx); \bAAA(\bd))
   \Forall \bd \in \VV.
   $$
1. Equivalently

   $$
   \langle \bd, \bAAA^T(\bg) \rangle \leq h'(\bx; \bd)
   \Forall \bd \in \VV.
   $$
1. Hence $\bAAA^T(\bg) \in \partial h(\bx)$
   due to {eq}`eq-cvxf-subg-dir-der-inequality`.
1. Hence $\bAAA^T (\partial f(\bAAA(\bx)) ) \subseteq \partial h(\bx)$.
```


```{prf:theorem} Strong linear transformation rule for subdifferential calculus
:label: res-cvxf-subdiff-rule-linear

Let $f: \WW \to \RERL$ be a proper convex function.
Let $\bAAA : \VV \to \WW$ be a linear transformation.
Define $h : \VV \to \RERL$ as 

$$
h (\bx) = f (\bAAA(\bx)).
$$

Assume that $h$ is proper, i.e. $\dom h$ is not empty: 

$$
\dom h = \{ \bx \in \VV \ST \bAAA(\bx) \in \dom f\} \neq \EmptySet.
$$

Then, for any $\bx \in \interior \dom h$ such that
$\bAAA(\bx) \in \interior \dom f$, we have:

$$
\bAAA^T (\partial f (\bAAA(\bx))) = \partial h(\bx).
$$
```

```{prf:proof}
We showed $\bAAA^T (\partial f (\bAAA(\bx))) \subseteq \partial h(\bx)$
in {prf:ref}`res-cvxf-subdiff-weak-rule-linear`.
We show the reverse inclusion by contradiction.

1. Let $\bx \in \interior \dom h$ such that
   $\bAAA(\bx) \in \interior \dom f$.
1. Assume that there exists $\bd \in \partial h(\bx)$
   such that $\bd \notin \bAAA^T (\partial f(\bAAA(\bx)) )$.
1. By {prf:ref}`res-cvxf-subdiff-proper-convex-interior`,
   the set $\partial f(\bAAA(\bx))$ is nonempty, convex and compact.
1. Hence $\bAAA^T (\partial f(\bAAA(\bx)))$ is also
   nonempty, convex and compact.
1. By strict separation theorem
   ({prf:ref}`res-cvxf-cl-convex-set-strict-separation`),
   there exists a vector $\bp$ and a scalar $c$ such that

   $$
   \langle \bAAA^T(\bg), \bp \rangle
   < c < \langle \bd, \bp \rangle \Forall \bg \in \partial f(\bAAA(\bx)).
   $$
1. Equivalently


   $$
   \langle \bg, \bAAA(\bp) \rangle
   < c < \langle \bd, \bp \rangle \Forall \bg \in \partial f(\bAAA(\bx)).
   $$
1. Taking the supremum over $ \partial f(\bAAA(\bx))$ on the
   L.H.S., we obtain

   $$
   \sup_{\bg \in  \partial f(\bAAA(\bx))}
   \langle \bg, \bAAA(\bp) \rangle
   < \langle \bd, \bp \rangle.
   $$
1. By the max formula

   $$
   f'(\bAAA(\bx); \bAAA(\bp)) < \langle \bd, \bp \rangle.
   $$
1. But this means that

   $$
   h'(\bx; \bp) < \langle \bd, \bp \rangle.
   $$
1. This contradicts the assumption that $\bd \in \partial h(\bx)$.
1. Hence we must have

   $$
   \bAAA^T (\partial f(\bAAA(\bx)) ) = \partial h(\bx).
   $$
```


### Affine Transformations


```{prf:theorem} Weak affine transformation rule of subdifferential calculus
:label: res-cvxf-subdiff-weak-rule-affine


Let $f: \WW \to \RERL$ be a proper function.
Let $\bAAA : \VV \to \WW$ be a linear transformation.
Let $\bb \in \WW$.
Define $h : \VV \to \RERL$ as 

$$
h (\bx) = f (\bAAA(\bx) + \bb).
$$

Assume that $h$ is proper, i.e. $\dom h$ is not empty: 

$$
\dom h = \{ \bx \in \VV \ST \bAAA(\bx) + \bb \in \dom f\} \neq \EmptySet.
$$

Then, for any $\bx \in \dom h$

$$
\bAAA^T (\partial f (\bAAA(\bx) + \bb)) \subseteq \partial h(\bx).
$$
```


```{prf:proof}
We proceed as follows.

1. Let $\bx \in \dom h$. 
1. Then, $\bx' = \bAAA(\bx) + \bb \in \dom f$ such that $h(\bx) = f(\bx')$.
1. Let $\bg \in \bAAA^T (\partial f (\bx'))$.
1. Then, there is $\bd \in \WW^*$ such that $\bg = \bAAA^T (\bd)$ with
   $\bd \in \partial f(\bx')$.
1. Let $\by \in \dom h$.
1. Then, $\by' = \bAAA(\by) + \bb \in \dom f$ such that $h(\by)= f(\by')$.
1. Applying subgradient inequality for $f$ at $\bx'$ 
   with the subgradient being $\bd$, we get

   $$
   f(\by') \geq
   f(\bx') + \langle \by' - \bx', \bd \rangle.
   $$
1. We have $h(\by) = f(\by')$, $h(\bx) = f(\bx')$ and 
   $\by' - \bx' = \bAAA(\by - \bx)$.
1. Thus, the subgradient inequality simplifies to 

   $$
   h(\by) \geq h(\bx) + \langle \bAAA(\by - \bx), \bd \rangle.
   $$
1. We note that 

   $$
   \langle \bAAA(\by - \bx), \bd \rangle 
   = \langle \by - \bx, \bAAA^T(\bd) \rangle.
   $$
1. Thus, for any $\by \in \dom h$, we have

   $$
   h(\by) \geq h(\bx) + \langle \by - \bx, \bAAA^T(\bd) \rangle.
   $$
1. Thus, $\bg = \bAAA^T(\bd) \in \partial h (\bx)$.

Since this is valid for any $\bx \in \dom h$ and for every
$\bg \in \bAAA^T (\partial f (\bAAA(\bx) + \bb))$, hence

$$
\bAAA^T (\partial f (\bAAA(\bx) + \bb)) \subseteq h(\bx).
$$ 
```


```{prf:theorem} Affine transformation rule of subdifferential calculus
:label: res-cvxf-subdiff-strong-rule-affine


Let $f: \WW \to \RERL$ be a proper convex function.
Let $\bAAA : \VV \to \WW$ be a linear transformation.
Let $\bb \in \WW$.
Define $h : \VV \to \RERL$ as 

$$
h (\bx) = f (\bAAA(\bx) + \bb).
$$

Assume that $h$ is proper, i.e. $\dom h$ is not empty: 

$$
\dom h = \{ \bx \in \VV \ST \bAAA(\bx) + \bb \in \dom f\} \neq \EmptySet.
$$

Then, for any $\bx \in \interior \dom h$ such that
$\bAAA(\bx) + \bb \in \interior \dom f$, we have:

$$
\bAAA^T (\partial f (\bAAA(\bx) + \bb)) = \partial h(\bx).
$$
```

```{prf:proof}
We note that $h$ is a proper convex function since it is a composition
of an affine transformation with a proper convex function.


1. Let $\bx \in \interior \dom h$ such that $\bx' = \bAAA(\bx) + \bb \in \interior \dom f$.
1. Then, for any direction $\bd \in \VV$, by the 
   {prf:ref}`max formula <res-cvxf-dir-der-subg-support>`, 

   $$
   h'(\bx; \bd) = \sigma_{\partial h(\bx)} (\bd).
   $$
1. By the definition of the directional derivative, we have

   $$
   h'(\bx; \bd) &= \lim_{\alpha \to 0^+} \frac{h(\bx + \alpha \bd ) - h(\bx)}{\alpha}\\
   &= \lim_{\alpha \to 0^+} \frac{f(\bAAA(\bx) + \bb + \alpha \bAAA(\bd) ) 
      - f(\bAAA(\bx) + \bb}{\alpha}\\
   &= f'(\bAAA(\bx) + \bb; \bAAA(\bd)).
   $$
1. Thus,

   $$
   \sigma_{\partial h(\bx)} (\bd) = f'(\bAAA(\bx) + \bb; \bAAA(\bd)).
   $$
1. Using the max formula on the R.H.S., we get

   $$
   \sigma_{\partial h(\bx)} (\bd) &= f'(\bAAA(\bx) + \bb; \bAAA(\bd))\\
   &= \sup_{\bg \in \partial f(\bAAA(\bx) + \bb)} \langle \bAAA(\bd), \bg \rangle \\
   &= \sup_{\bg \in \partial f(\bAAA(\bx) + \bb)} \langle \bd, \bAAA^T (\bg) \rangle \\
   &= \sup_{\bg' \in \bAAA^T(\partial f(\bAAA(\bx) + \bb))} \langle \bd, \bg' \rangle \\
   &= \sigma_{\bAAA^T(\partial f(\bAAA(\bx) + \bb))}(\bd).
   $$
1. Since $\bx \in \interior \dom h$, hence
   by {prf:ref}`res-cvxf-subdifferential-closed-convex` and
   {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`
   $\partial h(\bx)$ is nonempty, closed and convex.
1. Since $\bAAA(\bx) + \bb \in \interior \dom f$, hence
   by {prf:ref}`res-cvxf-subdifferential-closed-convex` and
   {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`
   $\partial f(\bAAA(\bx) + \bb)$ is nonempty, closed and convex.
1. It follows that
   $\bAAA^T(\partial f(\bAAA(\bx) + \bb))$ is nonempty, closed and convex
   since $\bAAA^T$ is a linear operator and both $\VV$ and $\WW$ are 
   finite dimensional.
1. Then, due to {prf:ref}`res-cvxf-support-func-equality-convex`,

   $$
   \bAAA^T (\partial f (\bAAA(\bx) + \bb)) = \partial h(\bx).
   $$
```

### Composition

Chain rule is a key principle in computing derivatives of composition of functions.
A chain rule is available for subgradient calculus also.

We first recall a result on the derivative of composition of real functions.

```{prf:theorem} Chain rule for real functions
:label: res-cvxf-subdiff-chain-rule-rf

Let $f : \RR \to \RR$ be a real function which is
continuous on $[a,b]$ with $a < b$. 
Assume that $f'_+(a)$ exists.
Let $g : \RR \to \RR$ be another real function defined on an open interval 
$I$ such that $\range f \subseteq I$.
Assume $g$ is differentiable at $f(a)$.
Then the composite real function $h : \RR \to \RR$
given by

$$
h(t) \triangleq g (f (t)) \quad (a \leq t \leq b)
$$ 
is right differentiable at $t=a$. In particular,

$$
h'_+(a) = g'(f(a)) f'_+(a).
$$
```

```{prf:proof}
We show this by working with the definition of right hand derivative as a limit

$$
h'_+(a) &= \lim_{t \to a^+} \frac{h(t) - h(a)}{t - a} \\
&= \lim_{t \to a^+} \frac{g(f(t)) - g(f(a))}{t - a} \\
&= \lim_{t \to a^+} \frac{g(f(t)) - g(f(a))}{f(t) - f(a)} \frac{f(t) - f(a)}{t - a} \\
&= \lim_{z \to f(a)} \frac{g(z) - g(f(a))}{z - f(a)} \lim_{t \to a^+} \frac{f(t) - f(a)}{t - a} \\
&= g'(f(a)) f'_+(a).
$$
```


We can now develop a chain rule for subdifferentials
of multidimensional functions with the help of max formula. 

```{prf:theorem} Subdifferential chain rule
:label: res-cvxf-subdiff-chain-rule

Let $f : \VV \to \RR$ be convex and let $g : \RR \to \RR$ be a 
nondecreasing convex function.
Let $\bx \in \VV$.
Assume that $g$ is differentiable at $f(\bx)$.
Let $h = g \circ f$. Then

$$
\partial h (\bx) = g'(f(\bx)) \partial f(\bx).
$$
```

```{prf:proof}
We are given $\bx \in \VV$ at which $g$ is differentiable and $f$ is convex.

1. Since $f$ is convex and $g$ is nondecreasing convex function, hence $h$ is also convex.
1. We now introduce two real functions parametrized on $\bx$ and
   an arbitrary direction $\bd \in \VV$
   
   $$
   & f_{\bx, \bd} (t) = f(\bx + t \bd), t \in \RR \\
   & h_{\bx, \bd} (t) = h(\bx + t \bd), t \in \RR
   $$
1. It is now easy to see that

   $$
   h_{\bx, \bd} (t) = h(\bx + t \bd) = g ( f (\bx + t\bd))  = g (f_{\bx, \bd} (t)).
   $$
1. Thus, $h_{\bx, \bd} = g \circ f_{\bx, \bd}$.
1. Since $f_{\bx, \bd}$ and $ h_{\bx, \bd}$ are restrictions of $f$ and $h$
   along a line, they are also convex.
1. Due to {prf:ref}`res-cvxf-dir-der-exist-convex`, the directional derivatives of $f$
   and $h$ exist in every direction.
1. By the definition of directional derivative {prf:ref}`def-cvxf-directional-derivative`,
   
   $$
   & (f_{\bx, \bd})'_+ (0) = f'(\bx; \bd), \\
   & (h_{\bx, \bd})'_+ (0) = h'(\bx; \bd).
   $$
1. Also note that $f_{\bx, \bd} (0) = f(\bx)$ and $h_{\bx, \bd} (0) = h(\bx)$.
1. $f_{\bx, \bd}$ is right differentiable at $t=0$, 
   and $g$ is differentiable at $f(\bx)$.
1. Hence, by the chain rule in {prf:ref}`res-cvxf-subdiff-chain-rule-rf`, 
   
   $$
   h'(\bx; \bd) = g'(f(\bx)) f'(\bx; \bd).
   $$
1. By the max formula in {prf:ref}`res-cvxf-dir-der-subg-support`, 
 
   $$
   & h'(\bx; \bd) = \sigma_{\partial h (\bx)} (\bd) \\
   & f'(\bx; \bd) = \sigma_{\partial f (\bx)} (\bd).   
   $$
1. Thus,

   $$
   \sigma_{\partial h (\bx)} (\bd) &= h'(\bx; \bd) \\
   &= g'(f(\bx)) f'(\bx; \bd) \\
   &= g'(f(\bx)) \sigma_{\partial f (\bx)} (\bd) \\
   &= \sigma_{g'(f(\bx)) \partial f (\bx)} (\bd).
   $$
   The last step is due to {prf:ref}`res-cvxf-support-func-Homogeneity`.
   Since $g$ is nondecreasing, hence $g'(f(\bx)) \geq 0$.
1. By {prf:ref}`res-cvxf-subdifferential-closed-convex` and
   {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`, 
   the sets $\partial f(\bx)$ and $\partial h(\bx)$ are nonempty,
   closed and convex.
1. Then, the set $g'(f(\bx)) \partial f (\bx)$ is also nonempty,
   closed and convex.
1. Thus, by {prf:ref}`res-cvxf-support-func-equality-convex`,
    
   $$
   \partial h (\bx) = g'(f(\bx)) \partial f (\bx).
   $$

````

Applications of this rule are presented later
in {prf:ref}`ex-cvxf-subdiff-l1-norm-squared`.


### Max Rule

```{prf:theorem} Max rule of subdifferential calculus
:label: res-cvxf-subdiff-calculus-max-rule


Let $f_1, f_2, \dots, f_m : \VV \to \RERL$ be a set of
proper convex functions. Let $f : \VV \to \RERL$ be given by:

$$
f(\bx) = \max \{ f_1(\bx), f_2(\bx), \dots, f_m(\bx)\}.
$$

Let $\bx \in \bigcap_{i=1}^m \interior \dom f_i$ be a point common to the
interiors of domains of all the functions.

The subdifferential set of $f$ at $\bx$ can be obtained from
the subdifferentials of $f_i$ as follows:

$$
\partial f(\bx) = \convex \left ( \bigcup_{i\in I(\bx)} \partial f_i (\bx) \right )
$$
where $I(\bx) = \{ i \ST f_i(\bx) = f(\bx)\}$.
```
```{prf:proof}
Since $f_i$ are proper convex, hence their pointwise maximum $f$ is proper convex.

1. Let $I(\bx) = \{ i \in 1,\dots,m \ST f_i(\bx) = f(\bx)\}$.
1. For any (nonzero) direction, $\bd \in \VV$,
   by {prf:ref}`res-cvxf-dir-der-max-convex-funcs`:

   $$
   f'(\bx; \bd) = \underset{i \in I(\bx)}{\max} f'_i(\bx;\bd).
   $$
1. Without loss of generality, let us assume that $I(\bx) = 1,\dots,k$ 
   for some $k \in 1,\dots,m$. This can be achieved by reordering $f_i$.
1. By max formula ({prf:ref}`res-cvxf-subg-dir-der-max-formula`), 
   
   $$
   f_i'(\bx;\bd) = \sup \{ \langle \bd, \bg \rangle \ST \bg \in \partial f_i(\bx) \}.
   $$
1. Thus,

   $$
   f'(\bx; \bd) = \underset{i \in 1,\dots,k}{\max} 
   \underset{\bg_i \in \partial f_i(\bx)}{\sup} \langle \bd, \bg_i \rangle.
   $$
1. Recall that for any $a_1, \dots, a_k \in \RR$, the identity below holds:

   $$
   \max \{ a_1, \dots, a_k \} = \underset{\bt \in \Delta_k }{\sup} \sum_{i=1}^k t_i a_i.
   $$
1. Thus, we can expand $f'(\bx; \bd)$ as:

   $$
   f'(\bx; \bd)
   &= \underset{i \in 1,\dots,k}{\max} 
   \underset{\bg_i \in \partial f_i(\bx)}{\sup} \langle \bd, \bg_i \rangle\\
   &= \underset{\bt \in \Delta_k }{\sup} \left \{ \sum_{i=1}^k t_i 
   \underset{\bg_i \in \partial f_i(\bx)}{\sup} \langle \bd, \bg_i \rangle
   \right \} \\
   &= \underset{\bt \in \Delta_k }{\sup} \left \{
   \sum_{i=1}^k  
   \sup 
   \left \langle \bd, t_i \bg_i \right \rangle
   \ST \bg_i \in \partial f_i(\bx) \right \} \\
   &= \sup \left \{ 
   \left \langle \bd, \sum_{i=1}^k t_i \bg_i \right \rangle
   \ST \bg_i \in \partial f_i(\bx), \bt \in \Delta_k \right \} \\
   &= \sup \left \{ 
   \left \langle \bd, \bg \right \rangle
   \ST \bg \in \convex \left (\bigcup_{i=1}^k \partial f_i(\bx) \right) \right \} \\
   &= \sigma_A (\bd)
   $$
   where $A = \convex \left (\bigcup_{i=1}^k \partial f_i(\bx) \right )$
   and $\sigma$ denotes the support function.
1. Since $\bx \in \interior \dom f$, hence, by the
   max formula ({prf:ref}`res-cvxf-dir-der-subg-support`)

   $$
   f'(\bx;\bd) =  \sigma_{\partial f(\bx)} (\bd).
   $$
1. Thus, we have

   $$
   \sigma_{\partial f(\bx)} (\bd) = \sigma_A {\bd}.
   $$
1. By {prf:ref}`res-cvxf-subdifferential-closed-convex`, $\partial f(\bx)$
   is closed and convex.
1. By {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`,
   $\partial f(\bx)$ is nonempty and bounded.
1. Thus, $\partial f(\bx)$ is nonempty, closed and convex.
1. Similarly, $\partial f_i(\bx)$ are nonempty, closed, convex and
   bounded.
1. Thus, $\bigcup_{i=1}^k \partial f_i(\bx)$
   is a finite union of nonempty, closed, convex and bounded sets.
1. Thus, $\bigcup_{i=1}^k \partial f_i(\bx)$ 
   is also nonempty and compact.
   1. A finite union of nonempty sets is nonempty.
   1. A finite union of bounded sets is bounded.
   1. A finite union of closed sets is closed.
   1. Thus, $\bigcup_{i=1}^k \partial f_i(\bx)$ is closed and bounded.
   1. Since $\VV$ is finite dimensional, hence closed and bounded
      sets are compact.
1. Since $A$ is a convex hull of $\bigcup_{i=1}^k \partial f_i(\bx)$,
   hence $A$ is nonempty, closed and convex.
   1. Recall from {prf:ref}`res-cvxf-convex-hull-compact` that
   convex hull of a compact set is compact.
   1. Also, recall that compact sets are closed and bounded.
1. Since $\sigma_{\partial f(\bx)} (\bd) = \sigma_A (\bd)$
   is true for any $\bd \in \VV$,
   the support functions for the underlying nonempty, closed and convex
   set are equal.
   Hence by {prf:ref}`res-cvxf-support-func-equality-convex`,

   $$
   \partial f(\bx) = A = \convex \left ( \bigcup_{i=1}^k \partial f_i(\bx) \right ).
   $$
```

Some applications of this rule are presented later in
{prf:ref}`ex-cvxf-subdiff-linf-norm`,
{prf:ref}`ex-cvxf-subdiff-ax-b-inf-norm`,
{prf:ref}`ex-cvxf-subdiff-max-func`,
{prf:ref}`ex-cvxf-subdiff-piecewise-linear-function`.


We now present a weaker version of the max rule which is applicable
for pointwise supremum over an arbitrary set of functions.

```{prf:theorem} Weak max rule of subdifferential calculus
:label: res-cvxf-subdiff-calculus-weak-max-rule

Let $I$ be an arbitrary index set and suppose that
for every $i \in I$, there exists a proper convex
function $f_i : \VV \to \RERL$.
Let $f : \VV \to \RERL$ be given by:

$$
f(\bx) = \sup_{i \in I} \{ f_i(\bx)\}.
$$

Then for any $\bx \in \dom f$,

$$
\convex \left ( \bigcup_{i\in I(\bx)} \partial f_i (\bx) \right ) 
\subseteq \partial f(\bx)
$$
where $I(\bx) = \{ i \in I \ST f_i(\bx) = f(\bx)\}$.

In words, if $f_i(\bx) = f(\bx)$, then a subgradient of $f_i$
at $\bx$ is also a subgradient of $f$ at $\bx$.
Also, for all $i \in I$ such that $f_i(\bx) = f(\bx)$,
any convex combination of their subgradients at $\bx$ is also a subgradient
of $f$ at $\bx$.
```

```{prf:proof}
Pick some $\bx \in \dom f$.

1. Let $\bz \in \dom f$ be arbitrary.
1. Let $I(\bx) =  \{ i \in I \ST f_i(\bx) = f(\bx)\}$.
1. Let $i \in I(\bx)$ be arbitrary.
1. Let $\bg \in \partial f_i(\bx)$ be a subgradient of $f_i$ at $\bx$.
1. Then, by definition of $f$ and subgradient inequality:

   $$
   f(\bz) \geq f_i(\bz) \geq f_i(\bx) + \langle \bz - \bx, \bg \rangle
   = f(\bx) + \langle \bz - \bx, \bg \rangle. 
   $$
   We used the fact that $f_i(\bx) = f(\bx)$ for $i \in I(\bx)$.
1. Thus, $\bg \in \partial f(\bx)$. $\bg$ is a subgradient of $f$
   at $\bx$.
1. Since this is valid for every subgradient of $f_i$ at $\bx$, 
   hence $\partial f_i(\bx) \subseteq \partial f(\bx)$.
1. Since this is valid for every $i \in I(\bx)$, hence

   $$
    \bigcup_{i\in I(\bx)} \partial f_i (\bx) \subseteq \partial f(\bx).
   $$

1. Recall from {prf:ref}`res-cvxf-subdifferential-closed-convex`
   that $\partial f(\bx)$ is convex.
1. Thus, it contains the convex hull of any of its subsets.
   Hence,
   
   $$
   \convex \left ( \bigcup_{i\in I(\bx)} \partial f_i (\bx) \right ) 
   \subseteq \partial f(\bx).
   $$
```

Next is an example application of the weak max rule.

```{prf:example} Subgradient of $\lambda_{\max}(\bA_0 + \sum_{i=1}^m x_i \bA_i$
:label: ex-cvxf-subdiff-max-eigen-val-m-sym-mat-sum


Let $\bA_0, \bA_1, \dots, \bA_m \in \SS^n$ be $m+1$ given symmetric
matrices. Define an affine transformation $\bAAA : \RR^m \to \SS^n$
as

$$
\bAAA(\bx) \triangleq \bA_0 + \sum_{i=1}^m x_i \bA_i.
$$
For every vector $\bx \in \RR^m$, this mapping
defines a symmetric matrix $\bAAA(\bx)$.
We can compute the largest eigen value of $\bAAA(\bx)$.
We introduce a function $f: \RR^m \to \RR$ as

$$
f(\bx) \triangleq \lambda_{\max} (\bAAA(\bx)) 
=  \lambda_{\max} (\bA_0 + \sum_{i=1}^m x_i \bA_i). 
$$
Our task is to find a subgradient of $f$ at $\bx$.

1. Recall from the definition of largest eigen values,

   $$
   f(\bx) = \underset{\by \in \RR^n;  \| \by \|_2 = 1 }{\sup} \by^T \bAAA(\bx) \by.
   $$

1. For every $\by \in \RR^n$ such that $\| \by \|_2 = 1$,
   we can define a function:

   $$
   f_{\by}(\bx) \triangleq \by^T \bAAA(\bx) \by.
   $$

1. Then,

   $$
   f(\bx) = \underset{\by \in \RR^n;  \| \by \|_2 = 1 }{\sup} f_{\by}(\bx).
   $$
1. The function $f_{\by}(\bx)$ is affine (in $\bx$) for every $\by$.
1. Thus, $f_{\by}$ is convex for every $\by$.
1. Thus, $f$ is a pointwise supremum of a family of 
   functions $f_{\by}$.
1. Thus, $f$ is also convex (see {prf:ref}`res-cvx-ptws-supremum`).
1. Consequently, we can use the weak max rule
   {prf:ref}`res-cvxf-subdiff-calculus-weak-max-rule`
   to identify a subgradient of $f$ at $\bx$.
1. Let $\tilde{\by}$ be a normalized eigenvector of $\bAAA(\bx)$
   corresponding to its largest eigenvalue. Then

   $$
   f(\bx) = \tilde{\by}^T \bAAA(\bx) \tilde{\by}.
   $$
1. This means that $f(\bx) = f_{\tilde{\by}}(\bx)$.
1. By the weak max rule, a subgradient of $f_{\tilde{\by}}$ at $\bx$
   is also a subgradient of $f$ at $\bx$.
1. Expanding $f_{\tilde{\by}}(\bx)$:

   $$
   f_{\tilde{\by}}(\bx) = \tilde{\by}^T \bAAA(\bx) \tilde{\by}
   = \tilde{\by}^T \bA_0\tilde{\by} 
   + \sum_{i=1}^m \tilde{\by}^T \bA_i \tilde{\by} x_i.
   $$
1. Then, the gradient of $f_{\tilde{\by}}$ at $\bx$
   (computed by taking partial derivatives w.r.t. $x_i$) is

   $$
   \nabla f_{\tilde{\by}}(\bx) = 
   (\tilde{\by}^T \bA_1 \tilde{\by}, \dots, \tilde{\by}^T \bA_m \tilde{\by}). 
   $$
1. Since $f_{\by}$ is affine (thus convex), hence its gradient
   is also a subgradient.
1. Thus, 

   $$
   (\tilde{\by}^T \bA_1 \tilde{\by}, \dots, \tilde{\by}^T \bA_m \tilde{\by})
   \in \partial f(\bx).
   $$
```

## Lipschitz Continuity

```{prf:theorem} Lipschitz continuity and boundedness of the subdifferential sets
:label: res-cvxf-subdiff-bounded-lipschitz-continuous

Let $f : \VV \to \RERL$ be a proper convex function.
Suppose that $X \subseteq \interior \dom f$.
Consider the following two claims:

1. $| f(\bx) - f(\by) | \leq L \| \bx - \by \|$ for any $\bx, \by \in X$.
1. $ \| \bg \|_* \leq L$ for any $\bg \in \partial f(\bx)$ where $\bx \in X$.

Then,

* (2) implies (1). In other words, if subgradients are bounded
  then, the function is Lipschitz continuous.
* If $X$ is open, then (1) holds if and only if (2) holds. 

In other words, if the subgradients over a set $X$
are bounded then $f$ is Lipschitz continuous over $X$.
If $X$ is open then $f$ is Lipschitz continuous over $X$
if and only if the subgradients over $X$ are bounded.
```

```{prf:proof}
(a) We first show that $(2) \implies (1)$.

1. Assume that (2) is satisfied.
1. Pick any $\bx, \by \in X$.
1. Since $f$ is proper and convex and $\bx, \by \in \interior \dom f$,
   hence due to {prf:ref}`res-cvxf-proper-interior-subdiff-nonempty-bounded`,
   $\partial f(\bx)$ and $\partial f(\by)$ are nonempty.
1. Let $\bg_x \in \partial f(\bx)$
   and $\bg_y \in \partial f(\by)$.
1. By subgradient inequality
   
   $$
   & f(\by) \geq f(\bx) + \langle \by - \bx, \bg_x \rangle; \\
   & f(\bx) \geq f(\by) + \langle \bx - \by, \bg_y \rangle.
   $$
1. We can rewrite this as

   $$
   & f(\bx) - f(\by) \leq \langle \bx - \by , \bg_x \rangle; \\
   & f(\by) - f(\bx) \leq \langle \by - \bx , \bg_y \rangle.
   $$
1. By generalized Cauchy Schwartz inequality ({prf:ref}`res-la-ip-gen-cs-ineq`),
   
   $$
   \langle \bx - \by , \bg_x \rangle \leq \| \bx - \by \| \| \bg_x \|_*
   \leq L \| \bx - \by \|; \\
   \langle \by - \bx , \bg_y \rangle \leq \| \by - \bx \| \| \bg_y \|_*
   \leq L \| \bx - \by \|.
   $$
1. Combining the two inequalities, we get

   $$
   | f(\bx) - f(\by) | \leq L \| \bx - \by \|.
   $$
1. Thus, $(2) \implies (1)$.


(b) If $X$ is open, then we need to show that $(1) \iff (2)$.

1. We have already shown that $(2) \implies (1)$.
1. Assume that $X$ is open and $(1)$ holds.
1. Let $\bx \in X$. 
1. Since $\bx$ is an interior point of $\dom f$, hence
   the subdifferential is nonempty.
1. Pick any $\bg \in \partial f(\bx)$.
1. Let $\bg^{\dag} \in \VV$ be a vector with $\| \bg^{\dag} \|=1$
   and $\langle \bg^{\dag}, \bg \rangle = \| \bg \|_*$.
   Such a vector exists by definition of the dual norm.
1. Since $X$ is open, we can choose $\epsilon > 0$ small enough
   such that $\bx + \epsilon \bg^{\dag} \in X$.
1. By the subgradient inequality, we have:

   $$
   f(\bx + \epsilon \bg^{\dag}) \geq f(\bx) + \langle \epsilon \bg^{\dag}, \bg \rangle.
   $$
1. Thus,

   $$
   \epsilon \| \bg \|_* 
   &= \langle \epsilon \bg^{\dag}, \bg \rangle \\
   &\leq f(\bx + \epsilon \bg^{\dag}) - f(\bx) \\
   &\leq L \| (\bx + \epsilon \bg^{\dag} - \bx \|  & \text{ by hypothesis in (1)} \\
   &= L \epsilon \| \bg^{\dag} \| = L \epsilon.
   $$
1. Canceling $\epsilon$, we get:

   $$
   \| \bg \|_*  \leq L
   $$
   holds true for every $\bg \in \partial f(\bx)$ where $\bx \in X$ as desired.
```


```{prf:corollary} Lipschitz continuity of convex functions over compact domains
:label: res-cvxf-convex-func-compact-dom-lipschitz-cont

Let $f: \VV \to \RERL$ be a proper and convex function. Suppose that
$X \subseteq \interior \dom f$ is compact. 
Then, there exists $L > 0$ such that

$$
| f(\bx) -f(\by) | \leq L \| \bx - \by \| \quad \Forall \bx, \by \in X.
$$  
```

```{prf:proof}
Recall from {prf:ref}`res-cvxf-subg-compact-nonempty-bounded`
that the subgradients of a proper convex function over
a compact set are nonempty and bounded.

1. In other words, the set

   $$
   Y = \bigcup_{\bx \in X} \partial f(\bx)
   $$
   is nonempty and bounded.
1. Thus, for every $\bg \in Y$, there exists $L > 0$
   such that $\| \bg \|_* \leq L$.
1. Then by {prf:ref}`res-cvxf-subdiff-bounded-lipschitz-continuous`,
   
   $$
   | f(\bx) - f(\bx)| \leq L \| \bx - \by \| \Forall \bx, \by \in X.
   $$
1. Thus, $f$ is indeed Lipschitz continuous over $X$.
```


## $\epsilon$-Subgradients

```{index} Approximate subgradient
```
````{prf:definition} $\epsilon$-Subgradient
:label: def-cvxf-e-subgradient

Let $f : \VV \to \RERL$ be a proper function. 
Let $\bx \in \dom f$. 
A vector $\bg \in \VV^*$ is called an $\epsilon$-*subgradient*
of $f$ at $\bx$ 
if
```{math}
:label: eq-cvxf-e-subgradient-inequality
f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle - \epsilon \Forall \by \in \VV.
```
````

### Geometric Interpretation

```{prf:observation} $\epsilon$-subgradient and supporting hyperplane
:label: res-cvxf-e-subgradient-supporting-hyperplane

Let $f: \VV \to \RERL$ be a proper function.
Then $\bg$ be an $\epsilon$-subgradient of $f$ at $\bx$
if and only if $\epi f$ is contained in the positive
halfspace of the
hyperplane with a normal $(-\bg, 1)$
passing through $(\bx, f(\bx) - \epsilon)$. 
```

```{prf:proof}
Let $H$ denote the hyperplane

$$
H = \{
(\by, t) \ST \langle \by, -\bg \rangle  + t 
      =  \langle \bx, -\bg \rangle + f(\bx) - \epsilon \}.
$$
The positive halfspace of $H$ is given by

$$
H_+ = \{
(\by, t) \ST \langle \by, -\bg \rangle  + t 
      \geq  \langle \bx, -\bg \rangle + f(\bx) - \epsilon \}.
$$


Assume that $\bg$ is an $\epsilon$-subgradient of $f$ at $\bx$.
1. For any $(\by, t) \in \epi f$, we have

   $$
   t \geq f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle - \epsilon.
   $$
1. This is equivalent to

   $$
   \langle \by, -\bg \rangle + t  \geq
   \langle \bx, -\bg \rangle + f(\bx) - \epsilon
   $$
   for all $(\by, t) \in \epi f$.
1. Hence $\epi f \subseteq H_+$.


Now assume that $\epi f \subseteq H_+$.

1. Let $(\by, f(\by)) \in \epi f$.
1. Then we have

   $$
   \langle \by, -\bg \rangle  + f(\by)  \geq  \langle \bx, -\bg \rangle + f(\bx) - \epsilon.
   $$

1. Rearranging the terms, we have

   $$
   f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle - \epsilon \Forall \by \in \VV. 
   $$
1. But this means that $\bg$ is an $\epsilon$-subgradient of $f$ at $\bx$.
```


### $\epsilon$-Subdifferential


```{index} Approximate Subdifferential
```
```{prf:definition} $\epsilon$-subdifferential
:label: def-cvxf-e-subdifferential

Let $f : \VV \to \RERL$ be a proper function.
The set of all $\epsilon$-subgradients of $f$ at a point $\bx \in \dom f$
is called the $\epsilon$-*subdifferential* of $f$ at $\bx$ and is denoted by
$\partial_{\epsilon} f(\bx)$.

$$
\partial_{\epsilon} f(\bx) \triangleq 
\{ \bg \in \VV^* \ST f (\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle
- \epsilon 
  \Forall \by \in \VV \}.
$$

For all $\bx \notin \dom f$, we define $\partial_{\epsilon} f(\bx) = \EmptySet$.
```
It is easy to see that 

$$
\partial f(\bx) \subseteq \partial_{\epsilon} f(\bx).
$$
Also, if $\epsilon_2 \geq \epsilon_1 > 0$, then

$$
\partial_{\epsilon_1} f(\bx) \subseteq \partial_{\epsilon_2} f(\bx).
$$ 

## Optimality Conditions

A well known result for differentiable functions is that
at the point of optimality $\nabla f(\bx) = \bzero$
(see {prf:ref}`res-opt-first-order-optimality-local`).
Subdifferentials are useful in characterizing the
minima of a function. The idea of vanishing gradients
can be generalized for subgradients also.

```{prf:theorem} Fermat's optimality condition
:label: res-cvxf-subdiff-fermat-optimality

Let $f : \VV \to \RERL$ be a proper convex function.
Then 

$$
\ba \in \argmin \{ f(\bx) \ST \bx \in \VV \}
$$
if and only if $\bzero \in \partial f(\ba)$.

In other words, $\ba$ is a minimizer of $f$ if and only if
$\bzero$ is a subgradient of $f$ at $\ba$.
```

```{prf:proof}
Assume that $\bzero \in \partial f(\ba)$ where $\ba \in \dom f$.

1. By subgradient inequality

   $$
   f(\bx) \geq f(\ba) + \langle \bx - \ba, \bzero \rangle \Forall \bx \in \VV.
   $$
1. This simplifies to
   
   $$
   f(\bx) \geq f(\ba) \Forall \bx \in \VV.
   $$
1. Thus, $\ba \in \argmin \{ f(\bx) \ST \bx \in \VV \}$.


For the converse, assume that $\ba \in \argmin \{ f(\bx) \ST \bx \in \VV \}$.

1. Then, 
   
   $$
   f(\bx) \geq f(\ba) \Forall \bx \in \VV.
   $$
1. But then

   $$
   & f(\bx) \geq f(\ba) \\
   & \iff f(\bx) \geq f(\ba) + 0 \\
   & \iff f(\bx) \geq f(\ba) + \langle \bx - \ba, \bzero \rangle
   $$
   holds true for every $\bx \in \VV$.
1. This implies that $\bzero \in \partial f(\ba)$.
```

## Mean Value Theorem

The following result is from {cite}`hiriart2013convex`.

```{prf:theorem} A subgradients based mean value theorem for 1D functions
:label: res-cvxf-convex-subdiff-mvt

Let $f : \RR \to \RERL$ be a proper closed convex function.
Let $[a,b] \subseteq \dom f$ with $a < b$. Then,

$$
f(b) - f(a) = \int_a^b h(t) d t
$$
where $h : (a, b) \to \RR$ satisfies $h(t) \in \partial f(t)$
for every $t \in (a, b)$.
```







In the reminder of this section, we compute the subgradients
and subdifferential sets for a variety of standard functions.

## Norm Functions

```{div}
We recall from {prf:ref}`res-cvxf-subdiff-norm-origin` that
the subdifferential of a norm $\| \cdot \|: \VV \to \RR$ at $x = \bzero$
is given by:

$$
\partial f(\bzero) 
= B_{\| \cdot \|_*} [\bzero, 1] 
= \{ g \in \VV^* \ST \|g\|_* \leq 1 \}. 
$$
```

### $\ell_1$-Norm

```{prf:example} Subdifferential of $\ell_1$ norm at origin
:label: ex-cvxf-subdiff-l1-norm-origin

Let $f : \RR^n \to \RR$ be given by $f(\bx) = \| \bx \|_1$.
We recall that the dual norm of $\ell_1$ is $\ell_{\infty}$.
The unit ball of $\ell_{\infty}$-norm at origin is given by

$$
B_{\| \cdot \|_{\infty}} [\bzero, 1] = [-1, 1]^n.
$$

Following {prf:ref}`res-cvxf-subdiff-norm-origin`,
the subdifferential of $f$ at $\bx = \bzero$ is given by:

$$
\partial f(\bzero) = B_{\| \cdot \|_{\infty}} [\bzero, 1] = [-1, 1]^n. 
$$
```

```{prf:example} Subdifferential of absolute value function at origin
:label: ex-cvxf-subdiff-abs-func-origin

Let $g : \RR \to \RR$ be the absolute value function given by

$$
g(x) = | x |.
$$
This is a special case of $\ell_1$ norm for $\RR^1$.
Thus, following {prf:ref}`ex-cvxf-subdiff-l1-norm-origin`,
the subdifferential of $g$ at $x = 0$ is given by:

$$
\partial g (0) = [-1, 1].
$$
For a complete specification of the subdifferential of $g$,
see {prf:ref}`ex-cvxf-subdiff-abs-func-l2` below.
```


```{prf:example} Subdifferential of $\ell_1$ norm 
:label: ex-cvxf-subdiff-l1-norm

Let $f : \RR^n \to \RR$ be given by $f(\bx) = \| \bx \|_1$.
We can write $f$ as a sum of $n$ functions

$$
f(\bx) = \| \bx \|_1 =  \sum_{i=1}^n |x_i| = \sum_{i=1}^n f_i(\bx)
$$

where 

$$
f_i (\bx) = | x_i |.
$$


Let $g (x) = | x |$. Then 

$$
f_i (\bx) = | x_i | = | \be_i^T  \bx | = g(\be_i^T  \bx).
$$

Due to affine transformation rule ({prf:ref}`res-cvxf-subdiff-strong-rule-affine`),

$$
\partial f_i (\bx) = (\partial g(\be_i^T  \bx)) \be_i 
= (\partial g(x_i)) \be_i.
$$
The subdifferential of the absolute value function $g$
is described in {prf:ref}`ex-cvxf-subdiff-abs-func-l2` below.


Thus, the subdifferential set of $f_i$ is given by:

$$
\partial f_i (\bx) = \begin{cases} 
\{ \sgn (x_i) \be_i \} & \text{for} & x_i \neq 0 \\
[-\be_i, \be_i] & \text{for} & x_i  = 0
\end{cases}.
$$


Using the sum rule {prf:ref}`res-cvxf-subdiff-sum-rule-rv-convex`, we have:

$$
\sum_{i=1}^n \partial f_i(\bx) = 
\partial \left ( \sum_{i=1}^n f_i \right )(\bx).
$$
We define the index set:

$$
I_0(\bx) = \{ i \ST x_i = 0\}.
$$


Expanding the sum of subdifferentials,

$$
\partial f (\bx) = \sum_{i \in I_0(\bx)} [-\be_i, \be_i] 
+ \sum_{i \notin I_0(\bx)} \sgn (x_i) \be_i.
$$

We can rewrite this as:

$$
\partial f (\bx) = \{ \bz \in \RR^n \ST z_i = \sgn (x_i) 
  \text{ whenever } x_i \neq 0, |z_i | \leq 1, \text{ otherwise } \}.
$$

We also have a weak result from this:

$$
\sgn (\bx) \in \partial f (\bx) = \partial \| \bx \|_1.
$$
```

```{prf:example} Subdifferential of $\ell_1$ norm squared
:label: ex-cvxf-subdiff-l1-norm-squared

Let $f : \RR^n \to \RR$ be given by $f(\bx) = \| \bx \|_1$.

Now let $g(t) = [t]_+^2$. And consider the function $h = g \circ f$ given by

$$
h (\bx) = \| \bx \|_1^2.
$$

By subdifferential chain rule ({prf:ref}`res-cvxf-subdiff-chain-rule`):

$$
\partial h (\bx) &= 2 \| \bx \|_1 \partial f (\bx) \\
&= 2 \| \bx \|_1 \{ \bz \in \RR^n \ST z_i = \sgn (x_i) 
  \text{ whenever } x_i \neq 0, |z_i | \leq 1, \text{ otherwise } \}.
$$

We have used the subdifferential of $f$ from {prf:ref}`ex-cvxf-subdiff-l1-norm`.
```



### $\ell_2$-Norm


```{prf:example} Subdifferential of $\ell_2$ norm at origin
:label: ex-cvxf-subdiff-l2-norm-origin

Let $f : \RR^n \to \RR$ be given by $f(\bx) = \| \bx \|_2$.
We recall that the dual norm of $\ell_1$ is also $\ell_2$
as this norm is self dual.

Following {prf:ref}`res-cvxf-subdiff-norm-origin`,
the subdifferential of $f$ at $\bx = \bzero$ is given by:

$$
\partial f(\bzero) = B_{\| \cdot \|_2} [\bzero, 1]
= \{ \bg \in \RR^n \ST \| \bg \|_2 \leq 1 \}.
$$
```

```{prf:example} Subdifferential of $\ell_2$ norm
:label: ex-cvxf-subdiff-l2-norm

Let $f : \RR^n \to \RR$ be given by $f(\bx) = \| \bx \|_2$.
At $\bx \neq \bzero$, $f$ is differentiable with the gradient
(see {prf:ref}`ex-mvc-gradient-l2-norm`):

$$
\nabla f (\bx) = \frac{\bx}{ \| \bx \|_2}.
$$

Since $f$ is convex and differentiable at $\bx \neq \bzero$,
hence due to {prf:ref}`res-cvxf-subdiff-grad`,

$$
\partial f(\bx) = \{ \nabla f (\bx) \} =
\left \{ \frac{\bx}{ \| \bx \|_2} \right \}.
$$



Combining this with the subdifferential of $f$
at origin from {prf:ref}`ex-cvxf-subdiff-l2-norm-origin`,
we obtain:

$$
\partial f (\bx) = \begin{cases} 
\left \{ \frac{\bx}{ \| \bx \|_2} \right \} & \text{for} & \bx \neq \bzero \\
B_{\| \cdot \|_2} [\bzero, 1] & \text{for} & \bx  = \bzero .
\end{cases}
$$
```

```{prf:example} Subdifferential of absolute value function
:label: ex-cvxf-subdiff-abs-func-l2

Let $g : \RR \to \RR$ be the absolute value function given by

$$
g(x) = | x |.
$$
This is a special case of $\ell_2$ norm for $\RR^1$.
Following {prf:ref}`ex-cvxf-subdiff-l2-norm`,


$$
\partial g(x) = \begin{cases} 
\left \{ \sgn (x) \right \} & \text{for} & x \neq 0 \\
[-1,1] & \text{for} & x  = 0 .
\end{cases}
$$
c.f. {prf:ref}`ex-cvxf-subdiff-abs-func-origin`.
```




### $\ell_{\infty}$-Norm

```{prf:example} Subdifferential of $\ell_{\infty}$ norm at origin
:label: ex-cvxf-subdiff-linf-norm-origin

Let $f : \RR^n \to \RR$ be given by $f(\bx) = \| \bx \|_{\infty}$.
We recall that the dual norm of $\ell_{\infty}$ is $\ell_{1}$.
The unit ball of $\ell_{1}$-norm at origin is given by

$$
B_{\| \cdot \|_1} [\bzero, 1] = \{ \bx \in \RR^n \ST \| \bx \|_1 \leq 1\}.
$$

Following {prf:ref}`res-cvxf-subdiff-norm-origin`,
the subdifferential of $f$ at $\bx = \bzero$ is given by:

$$
\partial f(\bzero) = B_{\| \cdot \|_1 [\bzero, 1]}
= \{ \bx \in \RR^n \ST \| \bx \|_1 \leq 1\}. 
$$
```

```{prf:example} Subdifferential of $\ell_{\infty}$ norm
:label: ex-cvxf-subdiff-linf-norm

Let $f : \RR^n \to \RR$ be given by $f(\bx) = \| \bx \|_{\infty}$.
Let us compute the subdifferential of $f$ at $\bx \neq \bzero$.

We have:

$$
f(\bx) = \max \{f_1(\bx), f_2(\bx), \dots, f_n(\bx)\}
$$
where $f_i(\bx) = |x_i|$. 
We define:

$$
I(\bx) = \{i  \in [1,\dots,n] \ST |x_i | = f(\bx) = \| \bx \|_{\infty} \}.
$$

Then, following {prf:ref}`ex-cvxf-subdiff-l1-norm`

$$
\partial f_i(\bx) = \{\sgn (x_i)  \be_i \} \Forall i \in I(\bx).
$$
This is valid since $\bx \neq \bzero$ implies that $f(\bx) \neq 0$
which in turn implies that $x_i \neq 0$ for every $i \in I(\bx)$.

Then, using the max rule for proper convex functions
({prf:ref}`res-cvxf-subdiff-calculus-max-rule`):

$$
\partial f(\bx) = 
\convex \left (\bigcup_{i \in I(\bx)} \{\sgn (x_i)  \be_i \} \right ).
$$

We can rewrite this as:

$$
\partial f(\bx) = \left \{\sum_{i \in I(\bx)} \lambda_i \sgn(x_i) \be_i \ST 
 \sum_{i \in I(\bx)} \lambda_i = 1, \lambda_j \geq 0, j \in I(\bx) \right \}.
$$


Combining this with the subdifferential of $f$
at origin from {prf:ref}`ex-cvxf-subdiff-linf-norm-origin`,
we obtain:

$$
\partial f (\bx) = \begin{cases} 
\left \{\sum_{i \in I(\bx)} \lambda_i \sgn(x_i) \be_i \ST 
 \sum_{i \in I(\bx)} \lambda_i = 1, \lambda_j \geq 0, j \in I(\bx) \right \},
& \bx \neq \bzero \\
B_{\| \cdot \|_1} [\bzero, 1], & \bx  = \bzero .
\end{cases}
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
\left \{ \frac{A x + b}{ \| A x + b \|_2} \right \} & \text{for} & Ax + b \neq \bzero \\
B_{\| \cdot \|_2} [\bzero, 1] & \text{for} & A x + b  = 0
\end{cases}.
$$

Applying the affine transformation rule, we get:


$$
\partial h (x) = A^T \partial f (Ax + b) 
= \begin{cases} 
\left \{ \frac{A^T (A x + b)}{ \| A x + b \|_2} \right \} & \text{for} & Ax + b \neq \bzero \\
A^T B_{\| \cdot \|_2} [\bzero, 1] & \text{for} & A x + b  = 0
\end{cases}.
$$

For $x \ST A x + b = 0$, we can write this as 

$$
\partial h (x) = A^T B_{\| \cdot \|_2} [\bzero, 1] = \{A^T y \ST \| y \|_2 \leq 1 \}.
$$
```

### $\ell_{\infty}$ Norm over Affine Transformation  

```{prf:example} Subdifferential of $\|\bA \bx + \bb \|_{\infty}$
:label: ex-cvxf-subdiff-ax-b-inf-norm

Let $\bA \in \RR^{m \times n}$. Let $\bb \in \RR^m$. 
Let $f : \RR^m \to \RR$ be given by 

$$
f(\by) = \| \by \|_{\infty}.
$$

Let $h : \RR^n \to \RR$ be the function 

$$
h(\bx) = \| \bA \bx + \bb \|_{\infty} = f(\bA \bx + \bb).
$$

With $\by = \bA \bx + \bb$, we have $y_i = \ba_i^T \bx + b_i$
where $\ba_i^T$ is the $i$-th row vector of $\bA$.

Following {prf:ref}`ex-cvxf-subdiff-linf-norm`

$$
\partial f (\by) = \begin{cases} 
\left \{\sum_{i \in I(\by)} \lambda_i \sgn(y_i) \be_i \ST 
 \sum_{i \in I(\by)} \lambda_i = 1, \lambda_j \geq 0, j \in I(\by) \right \},
& \by \neq \bzero \\
B_{\| \cdot \|_1} [\bzero, 1], & \by  = \bzero
\end{cases}
$$
where $I(\by) = \{i  \in [1,\dots,n] \ST |y_i | = f(\by) = \| \by \|_{\infty} \}$.



Due to affine transformation rule ({prf:ref}`res-cvxf-subdiff-strong-rule-affine`),

$$
\partial h(\bx) = \bA^T \partial f (\bA \bx + \bb).
$$

We have the following cases.

(a) $\by = \bzero$.

1. In terms of $\bx$, the condition $\by = \bzero$ is equivalent to
   $\bA \bx + \bb = \bzero$.
1. Then, 

   $$
   \partial f (\bA \bx + \bb) = \partial f(\bzero)
   = B_{\| \cdot \|_1} [\bzero, 1].
   $$
1. Thus,

   $$
   \partial h(\bx) = \bA^T B_{\| \cdot \|_1} [\bzero, 1].
   $$

(b)  $\by \neq \bzero$.

1. In terms of $\bx$, the condition $\by \neq \bzero$ is equivalent to
   $\bA \bx + \bb \neq \bzero$.
1. Then,

   $$
   \partial f(\bA \bx + \bb)
   &= \left \{\sum_{i \in I(\by)} \lambda_i \sgn(y_i) \be_i 
   \ST \sum_{i \in I(\by)} \lambda_i = 1, \lambda_j \geq 0, j \in I(\by) \right \} \\
   &= \left \{\sum_{i \in I_x} \lambda_i \sgn(\ba_i^T \bx + b_i) \be_i 
   \ST \sum_{i \in I_x} \lambda_i = 1, \lambda_j \geq 0, j \in I_x \right \}
   $$
   where 

   $$
   I_x = I(\by) = I(\bA \bx + \bb).
   $$
1. Note that $\bA^T \be_i = \ba_i$.
1. Then,

   $$
   \partial h(\bx) &= \bA^T \partial f (\bA \bx + \bb) \\
   &= \left \{\sum_{i \in I_x} \lambda_i \sgn(\ba_i^T \bx + b_i) \ba_i \ST 
 \sum_{i \in I_x} \lambda_i = 1, \lambda_j \geq 0, j \in I_x \right \}.
   $$

Combining the two cases, we get:

$$
\partial h (\bx) = \begin{cases} 
\left \{\sum_{i \in I_x} \lambda_i \sgn(\ba_i^T \bx + b_i) \ba_i \ST 
 \sum_{i \in I_x} \lambda_i = 1, \lambda_j \geq 0, j \in I_x \right \},
& \bA \bx + \bb \neq \bzero \\
\bA^T B_{\| \cdot \|_1} [\bzero, 1], & \bA \bx + \bb = \bzero
\end{cases}
$$
```

## Indicator Functions


```{prf:theorem} Subdifferential of indicator function
:label: res-cvxf-subdifferential-indicator 

The subdifferential of indicator function for a nonempty set $S \subset \VV$
at any point $\bx \in S$ is given by

$$
\partial I_S (\bx) = N_S (\bx).
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
:label: ex-cvxf-subg-ind-unit-ball

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
\partial \delta_{B[\bzero, 1]} (x) = \begin{cases} 
 \{ \by \in \VV^* \ST \| \by \|_* \leq \langle \bx, \by \rangle \} 
 & \text{for} & \| \bx \| \leq 1 \\
\EmptySet & \text{for} & \| \bx \| > 1.
\end{cases}
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

```{prf:example} Subdifferential of the max function
:label: ex-cvxf-subdiff-max-func

Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) = \max \{ x_1, x_2, \dots, x_n\}.
$$

Let $f_i(\bx) = x_i = \be_i^T \bx$. Then

$$
f_(\bx) = \max \{ f_1(\bx), f_2(\bx), \dots, f_n(\bx)\}.
$$

We note that $f_i$ are differentiable and their
gradient is given by
(see {prf:ref}`ex-mvc-gradient-linear-functional`):

$$
\nabla f_i(\bx) = \be_i.
$$
Also, $f_i$ are linear, hence convex.
Thus, due to {prf:ref}`res-cvxf-subdiff-grad`:

$$
\partial f_i(\bx) = \{ \be_i\}.
$$

We denote the index set of functions which
equal the value of $f(\bx$ at $\bx$ by:

$$
I (\bx) = \{ i \ST f(\bx) = x_i\}.
$$

Then, using the max rule for proper convex functions
({prf:ref}`res-cvxf-subdiff-calculus-max-rule`):

$$
\partial f (\bx) = \convex \left ( 
   \bigcup_{i \in I(\bx)} \partial f_i(\bx) \right )
  = \convex \left ( \bigcup_{i \in I(\bx)} \{ \be_i\} \right ).
$$

As and example, consider the case where $\bx = \alpha \bone$
for some $\alpha \in \RR$.

1. In other words, $\bx = (\alpha, \dots, \alpha)$.
1. Then, $f(\bx) = \alpha$.
1. $f_i(\bx) = \alpha = f(\bx)$ for ever $i \in [1,\dots, n]$.
1. $I(\bx) =  \{1, \dots, n \}$.
1. $\nabla f_i(\bx) = \be_i$.
1. $\convex ( \bigcup_{i \in I(\bx)} \{ \be_i\} ) = \convex \{ \be_1, \dots, \be_n \}$.
1. But $\convex \{ \be_1, \dots, \be_n \} = \Delta_n$.
1. Thus,

   $$
   \partial f (\alpha \bone) = \Delta_n \Forall \alpha \in \RR.
   $$
```




## Space of Matrices

```{div}
Let $\VV = \RR^{m \times n}$. Let the standard
inner product for $x, y, \in \VV$ be 
$\langle x, y \rangle = \Trace(x^T y)$. 

Let $f : \VV \to \RERL$ be a proper function.
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


## Convex Piecewise Linear Functions


```{prf:example} Subdifferential of convex piecewise linear functions
:label: ex-cvxf-subdiff-piecewise-linear-function


Let a convex piecewise linear function $f : \RR^n \to \RR$ be given by:

$$
f(\bx) = \underset{1 \leq i \leq m}{\max} \{\ba_i^T \bx + b_i \}
$$
where $\ba_i \in \RR^n, b_i \in \RR$ for $i=1,\dots,m$.

We define a set of functions $f_i : \RR^n \to \RR$
for $i=1,\dots,m$ as 

$$
f_i(\bx) = \ba_i^T \bx + b_i
$$  

We can see that $f$ is a pointwise maximum of these functions.

$$
f(\bx) = \underset{1 \leq i \leq m}{\max} \{ f_i(\bx)\}.
$$

Clearly,

$$
\partial f_i(\bx) = \{ \nabla f_i(\bx) \}
= \{ \ba_i \}.
$$

We define:

$$
I(\bx) = \{i \in [1,\dots,m] \ST f(\bx) = f_i(\bx) = \ba_i^T \bx + b_i \}.
$$

Then, using the max rule for proper convex functions
({prf:ref}`res-cvxf-subdiff-calculus-max-rule`):

$$
\partial f(\bx) 
&= \convex \left ( \bigcup_{i\in I(\bx)} \partial f_i (\bx) \right ) \\
&= \left \{  \sum_{i \in I(\bx)} \lambda_i \ba_i \ST 
  \sum_{i \in I(\bx)} \lambda_i = 1, \lambda_j \geq 0 \Forall j \in I(\bx)
  \right \}.
$$

By Fermat's optimality condition
({prf:ref}`res-cvxf-subdiff-fermat-optimality`),
$\bx^*$ is a minimizer of $f$ if and only if $\bzero \in f(\bx^*)$.

Thus, $\bx^*$ is a minimizer if and only if
there exists $\blambda \in \Delta_m$ such that

$$
\bzero = \sum_{i=1}^m \lambda_i \ba_i,\quad \lambda_j = 0 \Forall j \notin I(\bx^*).
$$

Note that at any $\bx$, for every $j \notin I(\bx)$, we have

$$
\ba_j^T \bx + b_j - f(\bx) < 0.
$$

Thus, the complimentary condition

$$
\lambda_j (\ba_j^T \bx + b_j - f(\bx)) = 0, j=1,\dots,m
$$
denotes the fact that whenever
$\ba_j^T \bx + b_j - f(\bx) < 0$, then $\lambda_j$ must be zero
and whenever $\ba_j^T \bx + b_j - f(\bx) = 0$ then $\lambda_j \geq 0$
is allowed (since $\blambda \in \Delta_m$).

If we put together a matrix $\bA \in \RR^{m \times n}$
whose rows are $\ba_1^T, \dots, \ba_m^T$, then
the optimality condition can be succinctly stated as

$$
\exists \blambda \in \Delta_m \text{ s.t. }
\bA^T \blambda = \bzero \text{ and }
\lambda_j (\ba_j^T \bx + b_j - f(\bx^*)) = 0, j=1,\dots,m.
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


