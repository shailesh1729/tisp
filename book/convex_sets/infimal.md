(sec:cvx:infimal)=
# Infimal Convolution


```{note}
Some results in this section appear without complete proof at the moment.
They have been collected from various
sources. The proofs will be added later.
```

## Definition

````{prf:definition} Infimal convolution
:label: def-cvx-infimal-convolution

Let $\VV$ be a real vector space.
Let $f, g : \VV \to \ERL$ be extended real-valued functions.
Their *infimal convolution*,
denoted by $f \infimal g : \VV \to \ERL$, is defined
as

```{math}
:label: eq-cvx-infimal-convolution
(f \infimal g)(\bx) \triangleq 
\inf \{ f(\by) + g(\bz) \ST \by, \bz \in \VV, \by + \bz = \bx \}. 
```

The infimal convolution of $f$ with $g$ is called
*exact* at $\bx$ if the infimum in {eq}`eq-cvx-infimal-convolution` is attained
at some $\by, \bz \in \VV$ such that $\by + \bz = \bx$.

The infimal convolution is called *exact* if it is attained at
every $\bx \in X$.
````

```{prf:remark} Alternative definitions
:label: rem-cvx-infimal-convolution-2

It is easy to see that

$$
(f \infimal g)(\bx) = 
\inf \{ f(\by) + g(\bz) \ST \by, \bz \in \VV, \by + \bz = \bx, 
    f(\by) < \infty, g(\bz) < \infty \}. 
$$

Another formulation is

$$
(f \infimal g)(\bx) =  \inf \{ f(\by) + g(\bx - \by) \ST \by \in \VV \}.
$$
This definition is reminiscent of the convolution operation in
signal processing. The word *infimal* reminds of the infimum
appearing in the definition. This is the motivation for the
name *infimal convolution*.

Infimal convolution is also known as *epigraphical addition*
because performing an infimal convolution of $f$ and $g$
amounts to the adding of the strict epigraphs of $f$ and $g$.
Recall from {prf:ref}`def-bra-strict-epigraph` that
the strict epigraph of a function $f : \VV \to \ERL$ is given by

$$
\epi_s f \triangleq \{ (\bx,t) \in \VV \oplus \RR \ST  f(\bx) < t \}.
$$
We show in {prf:ref}`res-cvx-infimal-strict-epi` that
$\epi_s f \infimal g = \epi_s f + \epi_s g$. 

From the definition, it is clear that
$f \infimal g$ is the largest of all the functions
$h: \VV \to \ERL$ satisfying

$$
h(\by + \bz) \leq f(\by) + g(\bz) \Forall \by, \bz \in X.
$$
```

```{prf:example} Cost minimization
:label: ex-cvx-infimal-cost-min

Consider a situation where a person sources a certain product
from two different manufactures.

1. The person needs to acquire $x$ total quantity.
1. The total supply is given by the equation $x = y + z$
   where $y$ is the quantity sourced from manufacturer A
   and $z$ is the quantity sourced from manufacture B.
1. Suppose the total cost of acquisition from manufacture
   A is given by a function $f(y)$. It may not be linear
   as the manufacturer may have different levels of discounts
   as $y$ increases.
1. Similarly, the cost of acquisition from manufacture B
   is given by the function $g(z)$.
1. Then the total cost is given by $f(y) + g(z)$
   subject to the condition that $y + z = x$.
1. Then the cost minimization problem is given by
   
   $$
   h(x) = \inf \{ f(y) + g(z) \ST x = y + z \}
   = (f \infimal g) (x).
   $$
1. We will also be interested in the set of solutions
   to the infimal problem; i.e., 
   
   $$
   \{ (y,z ) \ST f(y) + g(z) = (f \infimal g) (x) \}.
   $$
```


## Basic Properties

### Domain 

```{prf:property} Domain of infimal convolution
:label: res-cvx-infimal-dom

Let $f, g : \VV \to \ERL$ be given extended valued functions. 
Then

$$
\dom f \infimal g = \dom f + \dom g.
$$
```

```{prf:proof}

Let $\bz \in \dom f + \dom g$.

1. Then there exist $\bx \in \dom f$ and $\by \in \dom g$
   such that $\bz = \bx + \by$.
1. Then $f(\bx) < \infty$ and $g(\by) < \infty$.
1. By definition of infimal convolution

   $$
   (f \infimal g)(\bz) \leq f(\bx) + g(\by) < \infty.
   $$
1. Hence $\bz \in \dom f \infimal g$.
1. Hence $\dom f + \dom g \subseteq \dom f \infimal g$.

For the converse, let $\bz \in \dom f \infimal g$.

1. Then $(f \infimal g)(\bz) < \infty$.
1. First consider the case where $(f \infimal g)(\bz) = t \in \RR$.
1. Then for any $\epsilon > 0$, there exist $\bx, \by$ with $\bx + \by = \bz$
   such that

   $$
   t \leq f(\bx) + g(\by) \leq t + \epsilon.
   $$
1. Since $f(\bx) + g(\by)$ is finite, hence $f(\bx) < \infty$
   and $g(\by) < \infty$.
1. Hence $\bx < \dom f$ and $\by \in \dom g$.
1. Thus $\bz = \bx + \by \in \dom f + \dom g$.
1. Now consider the case where $(f \infimal g)(\bz) = -\infty$.
1. Then for every $M \in \RR$, there exist $\bx, \by$ with $\bx + \by = \bz$
   such that

   $$
   f(\bx) + g(\by) \leq M.
   $$
1. Thus $f(\bx) < \infty$ and $g(\by) < \infty$ for such pairs of $\bx, \by$.
1. Consequently $\bz = \bx + \by \in \dom f + \dom g$.
1. Combining the two cases $\dom f \infimal g \subseteq  \dom f + \dom g$.

Finally

1. We have already shown that $\dom f + \dom g \subseteq \dom f \infimal g$.
1. Thus $\dom f + \dom g = \dom f \infimal g$.
```

### Epigraph

```{prf:property} Connection with epigraph
:label: res-cvx-infimal-epi-con

$$
(f \infimal g) (\bx) = \inf \{ r \in \RR \ST (\bx, r) \in \epi f + \epi g \}.
$$
```

```{prf:proof}

Let $t = (f \infimal g) (\bx)$.
Define $S = \{ r \in \RR \ST (\bx, r) \in \epi f + \epi g \}$.
We need to show that $t$ is the greatest lower bound of the set $S$.

1. Let $(\bx,r) \in  \epi f + \epi g$.
1. Then there exists $(\by, r_1) \in \epi f$ and $(\bz, r_2) \in \epi g$
   so that $\bx = \by + \bz$ and $r = r_1 + r_2$.
1. Thus $f(\by) + g(\bz) \leq r_1 + r_2 = r$ (by epigraphs).
1. By infimal convolution definition $t \leq f(\by) + g(\bz) \leq r$.
1. Thus we have shown that $t \leq r$ if $(\bx, r) \in \epi f + \epi g$.
1. Thus $t$ is a lower bound of the set $S$.
1. Now choose any $\epsilon > 0$.
1. Then there exists $\by \in \dom f$ and $\bz \in \dom g$
   with $\bx = \by + \bz$ 
   such that
   
   $$
   f(\by) + g(\bz) \leq t + \epsilon.
   $$
1. Note that $(\by, f(\by)) \in \epi f$ and $(\bz, g(\bz)) \in \epi g$.
1. Hence $(\by + \bz, f(\by) + f(\bz)) \in \epi f + \epi g$.
1. Consequently $(\by + \bz, t + \epsilon) \in \epi f + \epi g$.
1. Replacing $\bx = \by + \bz$, we have $(\bx, t + \epsilon) \in \epi f + \epi g$.
1. Thus, for every $\epsilon > 0$, $t + \epsilon \in S$.
1. Hence $t$ must be the greatest lower bound of the set $S$.
1. In other words, $t = \inf S$ as desired.
```

```{prf:property} Strict epigraph of infimal convolution
:label: res-cvx-infimal-strict-epi

Let $f, g : \VV \to \ERL$ be given extended valued functions. 
Then

$$
\epi_s f \infimal g = \epi_s f + \epi_s g.
$$
```

```{prf:proof}

We show the set inclusion from both sides.

1. Let $(\bx, r) \in \epi_s f \infimal g$.
1. Then  $(f \infimal g)(\bx) < r$.
1. Then there exist $\by \in \dom f$ and $\bz \in \dom g$
   with $\bx = \by + \bz$ such that

   $$
   f(\by) + g(\bz) < r.
   $$
   This is directly from the definition of infimal convolution.
1. Consequently, we can split $r$ as $r = r_1 + r_2$ such that
   $f(\by) < r_1$ and $g(\bz) < r_2$.
   1. Let $s = f(\by)$, $t = g(\bz)$.
   1. Let $d = r - (s + t) > 0$.
   1. Let $e = \frac{d}{2} > 0$.
   1. Let $r_1 = s + e$ and $r_2 = t + e$.
   1. Then $r_1 + r_2 = s + t + 2e = s + t + d = r$.
   1. Also $f(\by) = s < r_1$ and $g(\bz) = t < r_2$.
1. Then $(\by, r_1) \in \epi_s f$ and $(\bz, r_2) \in \epi_s g$
   by definition of strict epigraphs.
1. Hence $(\by + \bz, r_1 + r_2)  = (\bx, r) \in \epi_s f + \epi_s g$.
1. Thus $\epi_s f \infimal g \subseteq \epi_s f + \epi_s g$

For the converse

1. Let $(\bx, r) \in \epi_s f + \epi_s g$.
1. Then there is $(\by, r_1) \in \epi_s f$ and $(\bz, r_2) \in \epi_s g$
   so that 

   $$
   \bx = \by + \bz \text{ and } r = r_1 + r_2.
   $$
1. Thus $f(\by) < r_1$ and $g(\bz) < r_2$.
1. Thus $f(\by) + g(\bz) < r_1 + r_2 = r$.
1. Hence $(f \infimal g)(\bx) \leq f(\by) + g(\bz) < r$.
1. Hence $(\bx, r) \in \epi_s f \infimal g$.
1. Hence $\epi_s f + \epi_s g \subseteq \epi_s f \infimal g$.
```




```{prf:property} Epigraph of infimal convolution
:label: res-cvx-infimal-epi

Let $f, g : \VV \to \ERL$ be given functions.
Then

$$
\epi f + \epi g \subseteq \epi f \infimal g.
$$

The equality holds if and only if the
infimal convolution is exact at each $\bx \in \VV$
where $(f \infimal g) (\bx) \in \RR$.
```

```{prf:proof}
We first show the inclusion.

1. Let $(\bx, r) \in \epi f + \epi g$.
1. Then there is $(\by, r_1) \in \epi f$ and $(\bz, r_2) \in \epi g$
   so that 

   $$
   \bx = \by + \bz \text{ and } r = r_1 + r_2.
   $$
1. Thus $f(\by) \leq r_1$ and $g(\bz) \leq r_2$.
1. Thus $f(\by) + g(\bz) \leq r_1 + r_2 = r$.
1. Hence $(f \infimal g)(\bx) \leq f(\by) + g(\bz) \leq r$.
1. Hence $(\bx, r) \in \epi f \infimal g$.
1. Hence $\epi f + \epi g \subseteq \epi f \infimal g$.

Next we show that the reverse inclusion holds 
if infimal convolution is exact at each $\bx \in \VV$
where $(f \infimal g) (\bx) \in \RR$.

1. Let $(\bx, r) \in \epi f \infimal g$.
1. Then  $(f \infimal g)(\bx) \leq r$.
1. Consider first the case where $(f \infimal g)(\bx) = -\infty$.
1. Then for any $M \in \RR$, 
   there exist $\by \in \dom f$ and $\bz \in \dom g$ with $\bx = \by + \bz$
   such that $f(\by) + f(\bz) < M$.
1. In particular, there exist $\by, \bz$ so that $f(\by) + f(\bz) < r$.
1. Hence $(\bx, r) \in \epi f + \epi g$.
1. Now if $(f \infimal g)(\bx) \in \RR$ then the infimal convolution is exact.
1. Since the infimal convolution is exact,
   hence there exist $\by \in \dom f$ and $\bz \in \dom g$
   with $\bx = \by + \bz$ such that

   $$
   f(\by) + g(\bz) = (f \infimal g)(\bx) \leq r.
   $$
   This is directly from the definition of infimal convolution.
1. Consequently, we can split $r$ as $r = r_1 + r_2$ such that
   $f(\by) \leq r_1$ and $g(\bz) \leq r_2$.
1. Then $(\by, r_1) \in \epi f$ and $(\bz, r_2) \in \epi g$
   by definition of epigraphs.
1. Hence $(\by + \bz, r_1 + r_2)  = (\bx, r) \in \epi f + \epi g$.
1. Thus $\epi_s f \infimal g \subseteq \epi f + \epi g$.


Finally, to show that this condition is necessary, assume that
there exists a point $\bx \in \VV$ where $(f \infimal g) (\bx) \in \RR$
and the infimal convolution is not exact.

1. Let $t  = (f \infimal g) (\bx)$.
1. Then $(\bx, t) \in \epi f \infimal g$.
1. Since the infimal convolution is not exact, hence
   for any $\by \in \dom f$ and $\bz \in \dom g$ with $\bx = \by + \bz$

   $$
   t < f(\by) + g(\bz).
   $$
1. For contradiction, assume that $(\bx, t) \in \epi f + \epi g$.
1. Then there exist $(\by, t_1) \in \epi f$ and $(\bz, t_2) \in \epi g$
   so that $\bx = \by + \bz$ and $t = t_1 + t_2$.
1. Thus $f(\by) \leq t_1$ and $g(\bz) \leq t_2$.
1. Thus $f(\by) + g(\bz) \leq t_1 + t_2 = t$.
1. We have arrived at a contradiction.
1. Hence $(\bx, t) \notin \epi f + \epi g$.
```

### Convexity

```{prf:theorem} Infimal convolution of convex functions
:label: res-cvx-infimal-convex-proper

Let $f : \VV \to \RERL$ be a proper convex function
and $g : \VV \to \RR$ be a real valued convex function.
Then $f \infimal g$ is convex.
```

```{prf:proof}

Define $h(\bx, \by) = f(\by) + g(\bx - \by)$.

1. Since $f$ and $g$ are convex, hence $h$ is convex.
1. We can easily show that for any $\bx \in \VV$,
   there exists $\by \in \VV$ such that
   $h(\bx, \by) < \infty$.
   1. Pick any $\bx \in \VV$.
   1. Choose any $\by \in \dom f$.
   1. Then $f(\by) < \infty$.
   1. Since $g$ is real valued, hence $g(\bx - \by) < \infty$.
   1. Thus $h(\bx, \by) = f(\by) + g(\bx - \by) < \infty$.
1. Then due to {prf:ref}`res-cvxf-partial-minimization-proper`

   $$
   (f \infimal g) (\bx) = \inf_{\by \in \VV} h(\bx, \by) 
   = \inf_{\by \in \VV} [f(\by) + g(\bx - \by)]
   $$
   is convex as a partial minimization of the function $h(\bx, by)$
   w.r.t. $\by$.
```

It is still possible that $f \infimal g$ is not a proper function
and may be equal to $-\infty$ at some $\bx$.


```{prf:example} Set distance function as infimal convolution
:label: ex-cvx-set-dist-infimal

Let $C \subseteq \VV$ be a nonempty convex set.

1. The indicator function $I_C$ is a proper convex function.
1. The norm function $\| \cdot \|$ is a real valued convex function.
1. By {prf:ref}`res-cvx-infimal-convex-proper`, $I_C \infimal \| \cdot \|$
   is convex.
1. But then

   $$
   (I_C \infimal \| \cdot \|) (\bx) = \inf_{\by \in \VV} (I_C(\by) + \| \bx - \by \|)
   = \inf_{\by \in C} \| \bx - \by \|
   = d_C(\bx).
   $$
1. Thus $d_C$ (the distance function to a convex set) is convex.
```

## Conjugates

```{prf:theorem} Conjugate of infimal convolution of proper functions
:label: res-cvx-infimal-proper-conjugate

For two proper functions  $h_1, h_2: \VV \to \RERL$, it holds that:

$$
(h_1 \infimal h_2)^*  = h_1^*  + h_2^*.
$$
```

```{prf:proof}
Pick $\by \in \VV^*$. Then

$$
(h_1 \infimal h_2)^* (\by)
&= \sup_{\bx \in \VV} \{ \langle \bx, \by \rangle - (h_1 \infimal h_2)(\bx) \}\\
&= \sup_{\bx \in \VV} \{ \langle \bx, \by \rangle 
   - \inf_{\bu \in \VV}(h_1(\bu) + h_2(\bx - \bu) ) \}\\
&= \sup_{\bx \in \VV} \sup_{\bu \in \VV} \{ \langle \bx, \by \rangle 
   - h_1(\bu) - h_2(\bx - \bu) \}\\
&= \sup_{\bu \in \VV} \sup_{\bx \in \VV} \{ \langle \bx - \bu, \by \rangle + \langle \bu, \by \rangle 
   - h_1(\bu) - h_2(\bx - \bu) \}\\
&= \sup_{\bu \in \VV} \{ 
   \sup_{\bx \in \VV} \{ \langle \bx - \bu, \by \rangle - h_2(\bx - \bu) \}
   + \langle \bu, \by \rangle  - h_1(\bu)  \}\\
&= \sup_{\bu \in \VV} \{h_2^*(\by) + \langle \bu, \by \rangle  - h_1(\bu)  \}\\
&= h_2^*(\by) + \sup_{\bu \in \VV} \{\langle \bu, \by \rangle  - h_1(\bu)  \}\\
&= h_2^*(\by) + h_1^*(\by) \\
&= (h_1^*  + h_2^*) (\by).
$$
```


```{prf:theorem} Conjugate of sum of convex functions
:label: res-cvx-sum-proper-conjugate

Let $h_1 : \VV \to \RERL$ be a proper convex
function and $h_2 : \VV \to \RR$ be a real valued
convex function. Then

$$
(h_1 + h_2)^* = h_1^* \infimal h_2^*.
$$
```

```{prf:proof}
The proof is more complicated and requires the application
of Fenchel's duality theorem ({prf:ref}`res-opt-fenchel-duality-theorem`).

1. Pick any $\by \in \VV^*$.
1. Elaborating the conjugate function

   $$
   (h_1 + h_2)^* (\by)
   &= \sup_{\bx \in \VV} \{ \langle \bx, \by \rangle - (h_1 + h_2)(\bx) \}\\
   &= \sup_{\bx \in \VV} \{ \langle \bx, \by \rangle - h_1(\bx) - h_2(\bx) \}\\
   &= -\inf_{\bx \in \VV} \{ h_1(\bx) + h_2(\bx) - \langle \bx, \by \rangle  \}\\
   &= -\inf_{\bx \in \VV} \{ h_1(\bx) + g(\bx)  \}\\
   $$
   where $g(\bx) = h_2(\bx) - \langle \bx, \by \rangle$.
1. We note that since $h_2$ is a real valued convex function, hence $g$ is also
   a real valued convex function.
1. We note that

   $$
   (\relint \dom h_1) \cap (\relint \dom g) = (\relint \dom h_1) \cap \VV
   = \relint \dom h_1 \neq \EmptySet.
   $$
1. Applying the Fenchel's duality theorem ({prf:ref}`res-opt-fenchel-duality-theorem`),

   $$
   \inf_{\bx \in \VV} \{ h_1(\bx) + g(\bx)  \} = 
   \sup_{\bz \in \VV} \{ -h_1^*(\bz) - g^*(-\bz)  \}.
   $$
1. Further 

   $$
   g^*(-\bz) 
   &= \sup_{\bx \in \VV} \{ \langle \bx, - \bz \rangle - g(\bx) \}\\
   &= \sup_{\bx \in \VV} \{ \langle \bx, - \bz \rangle - h_2(\bx) + \langle \bx, \by \rangle \}\\
   &= \sup_{\bx \in \VV} \{ \langle \bx, \by - \bz \rangle - h_2(\bx) \}\\
   &= h_2^*(\by - \bz ).
   $$
1. Consequently

   $$
   (h_1 + h_2)^* (\by) 
   &=  -\inf_{\bx \in \VV} \{ h_1(\bx) + g(\bx)  \} \\
   &= - \sup_{\bz \in \VV} \{ -h_1^*(\bz) - g^*(-\bz)  \}\\
   &= \inf_{\bz \in \VV} \{h_1^*(\bz) + g^*(-\bz)  \}\\
   &= \inf_{\bz \in \VV} \{h_1^*(\bz) + h_2^*(\by - \bz )\} \\
   &= (h_1^* \infimal h_2^*) (\by).
   $$

This completes the proof.
```

```{prf:corollary} Function sum as conjugate of infimal convolution of conjugates
:label: res-cvx-conj-inf-conj-eq-sum

Let $h_1 : \VV \to \RERL$ be a proper closed convex
function and $h_2 : \VV \to \RR$ be a real valued
convex function. Then

$$
h_1 + h_2 = (h_1^* \infimal h_2^*)^*.
$$
```

```{prf:proof}

We proceed as follows.

1. Since $h_1$ is proper and $h_2$ is real valued,
   hence $h_1 + h_2$ is proper.
1. Since both $h_1$ and $h_2$ are closed functions,
   hence $h_1 + h_2$ is closed.
1. Since both $h_1$ and $h_2$ are convex functions,
   hence $h_1 + h_2$ is convex.
1. Thus $h_1 + h_2$ is a proper, closed convex function.
1. By {prf:ref}`res-cvxf-biconjugate-proper-closed-convex`,

   $$
   (h_1 + h_2)^{**} = h_1 + h_2.
   $$
1. By {prf:ref}`res-cvx-sum-proper-conjugate`,

   $$
   (h_1 + h_2)^* = h_1^* \infimal h_2^*.
   $$
1. Hence

   $$
   h_1 + h_2 = (h_1 + h_2)^{**} = [(h_1 + h_2)^*]^*
   = [h_1^* \infimal h_2^*]^*.
   $$
```

```{prf:theorem} Representation of the infimal convolution by conjugates
:label: res-cvx-infimal-conjugate-rep

Let $h_1 : \VV \to \RERL$ be a proper convex
function and $h_2 : \VV \to \RR$ be a real valued
convex function. 
Suppose $h_1 \infimal h_2$ is a real valued function.
Then

$$
h_1 \infimal h_2 = (h_1^* + h_2^*)^*.
$$
```

```{prf:proof}
We proceed as follows.

1. By {prf:ref}`res-cvx-infimal-proper-conjugate`

   $$
   (h_1 \infimal h_2)^*  = h_1^*  + h_2^*.
   $$
1. Since $h_1$ is proper and convex and $h_2$ is real valued and convex,
   hence by {prf:ref}`res-cvx-infimal-convex-proper`,
   $h_1 \infimal h_2$ is convex.
1. By hypothesis $h_1 \infimal h_2$  is also real valued.
1. Thus $h_1 \infimal h_2$  is proper and closed.
1. Since $h_1 \infimal h_2$ is proper, closed and convex; 
   hence by {prf:ref}`res-cvxf-biconjugate-proper-closed-convex`

   $$
   (h_1 \infimal h_2)^{**} = h_1 \infimal h_2.
   $$
1. Hence
 
   $$
    h_1 \infimal h_2 = [(h_1 \infimal h_2)^*]^*
    = [h_1^*  + h_2^*]^*.
   $$
```

## Convexity

An interesting application of constructing
a convex function from a convex set in $\VV \oplus \RR$
is the fact that addition of
epigraphs leads to another convex function. 
This is also known as infimal convolution.

```{prf:theorem} Infimal convolution
:label: res-cvx-infimal-convolution-is-convex

Let $f_1, \dots, f_m : \VV \to \RERL$ be proper convex functions.
Let $f : \VV \to \RERL$ be defined as

$$
f(\bx) = \inf \{f_1(\bx_1) + \dots + f_m(\bx_m) \ST \bx_i \in \VV,
   \bx_1 + \dots + \bx_m = \bx \}.
$$
Then, $f$ is a proper convex function.
```

```{prf:proof}
Let $F_i = \epi f_i$ and $F = F_1 + \dots + F_m$.

1. Since $f_i$ is convex, hence $F_i = \epi f_i$ are convex sets
   for $i=1,\dots,m$.
1. Sum of convex sets is convex. Hence, $F$ is a convex set.
1. By definition of $F$, 
   $(\bx, t) \in F$ if and only if
   there exists $\bx_i \in \VV$ and $t_i \in \RR$
   with $(\bx_i, t_i) \in F_i$ 
   such that $\bx = \bx_1 + \dots + \bx_m$
   and $t = t_1 + \dots + t_m$.
1. It follows that $f_i(\bx_i) \leq t_i$ for $i=1,\dots,m$.
1. Consequently, $f_1(\bx_1) + \dots + f_m(\bx_m) \leq t_1 + \dots + t_m$.
1. By {prf:ref}`res-cvxf-construct-convex-sets-dirsum`,
   a function $g: \VV \to \RERL$ defined as

   $$
   g(\bx) \triangleq \inf \{t \in \RR \ST (\bx, t) \in F \}
   $$
   is a proper convex function.
1. Let $T = \{t \in \RR \ST (\bx, t) \in F \}$. 
   Then $g(\bx) = \inf T$.
1. We note that

   $$
   T = \{t \ST (\bx_i, t_i) \in F_i, t = t_1 + \dots + t_m, 
      \bx = \bx_1 + \dots + \bx_m \}.
   $$
1. We claim that $g = f$.

To show that $g=f$, we need to do the following.

1. Show that $\dom f = \dom g$.
1. Then, show that for every $\bx \in \dom f$, $f(\bx) = g(\bx)$. 


Assume that $\bx \notin \dom g$.

1. Then, there is no $t \in \RR$ such that $(\bx, t) \in F$.
1. Thus, there is no $(\bx_i, t_i) \in F_i$ for $i=1,\dots,m$
   such that $\bx = \bx_1 + \dots + \bx_m$.
1. Thus, for every $\bx_i \in \VV$ such that $\bx = \bx_1 + \dots + \bx_m$
   there is at least one $i$ such that there is no $t_i \in \RR$
   such that $(\bx_i, t_i) \in F_i$.
1. Thus, for every $\bx_i \in \VV$ such that $\bx = \bx_1 + \dots + \bx_m$
   there is at least one $i$ such that $f_i(\bx_i) = \infty$.
1. Thus, for every $\bx_i \in \VV$ such that $\bx = \bx_1 + \dots + \bx_m$,
   $f_1(\bx_1) + \dots + f_m(\bx_m) = \infty$.
1. Thus, $f(\bx) = \infty$.
1. Thus, $\bx \notin \dom f$.


Assume that $\bx \notin \dom f$.

1. Then, $f(\bx) = \infty$.
1. Thus, for every $\bx_i \in \VV$ such that $\bx = \bx_1 + \dots + \bx_m$,
   $f_1(\bx_1) + \dots + f_m(\bx_m) = \infty$.
1. Thus, for every $\bx_i \in \VV$ such that $\bx = \bx_1 + \dots + \bx_m$,
   there exists at least one $i$ such that $f_i(\bx_i) = \infty$.
1. Thus, for every $\bx_i \in \VV$ such that $\bx = \bx_1 + \dots + \bx_m$,
   there exists at least one $i$ such that $\bx_i \notin \dom f_i$.
1. Thus, for every $\bx_i \in \VV$ such that $\bx = \bx_1 + \dots + \bx_m$,
   there exists at least one $i$ such that there is no $t_i \in \RR$
   with $(\bx_i, t_i) \in F_i$.
1. Thus, there is no $(\bx_i, t_i) \in F_i$ for $i=1,\dots,m$
   such that $\bx = \bx_1 + \dots + \bx_m$.
1. Thus, there is no $t \in \RR$ such that $(\bx, t) \in F$.
1. Thus, $\bx \notin \dom g$.


Thus, $\bx \notin \dom f \iff \bx \notin \dom g$.
Thus, $\dom f = \dom g$. 


Let us now consider some $\bx \in \dom f = \dom g$.
Then, both $f(\bx)$ and $g(\bx)$ are finite.
Our goal is to show that $f(\bx) = g(\bx)$.

We first show that $f(\bx) \leq g(\bx)$.

1. For every $\bx_i \in \VV$ with $\bx = \bx_1 + \dots + \bx_m$,
   and $f_i(\bx_i)$ finite, we have:
   
   $$
   f(\bx) \leq f_1(\bx_1) + \dots + f_m(\bx_m).
   $$
1. Thus, for every $(\bx_i, t_i) \in F_i$ with $\bx = \bx_1 + \dots + \bx_m$,
   we have

   $$
   f(\bx) \leq f_1(\bx_1) + \dots + f_m(\bx_m) \leq t_1 + \dots + t_m.
   $$
1. Thus, for every $(\bx, t) \in F$ with $(\bx_i, t_i) \in F_i$,
   $\bx = \bx_1 + \dots + \bx_m$, $t = t_1 + \dots + t_m$,
   we have 

   $$
   f(\bx) \leq t.
   $$
1. Taking the infimum on the R.H.S. over the set $T$, we get
   
   $$
   f(\bx) = f(\bx) \leq g(\bx) = z.
   $$

Now, for contradiction, assume that $f(\bx) < g(\bx)$.

1. For every $t \in \RR$ such that $(\bx, t) \in F$, we have
   $g(\bx) \leq t$.
1. Thus, for every $(\bx_i, t_i) \in F_i$ with $\bx = \bx_1 + \dots + \bx_m$,
   we have

   $$
   g(\bx) \leq t_1 + \dots + t_m.
   $$
1. Then, for every $(\bx_i, t_i) \in F_i$ with $\bx = \bx_1 + \dots + \bx_m$,
   we have

   $$
   f(\bx) < t_1 + \dots + t_m.
   $$
1. Thus, there exists $r > 0$ such that
   for every $(\bx_i, t_i) \in F_i$ with $\bx = \bx_1 + \dots + \bx_m$,
   we have

   $$
   f(\bx) + r \leq t_1 + \dots + t_m.
   $$

TO BE COMPLETED.
```


