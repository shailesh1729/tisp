# Infimal Convolution


```{note}
Several results in this section appear without complete proof at the moment.
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
This is consistent with the convention that $\inf \EmptySet = \infty$.

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


```{prf:theorem} Connection with epigraph
:label: res-cvx-infimal-epi-con

$$
(f \infimal g) (\bx) = \inf \{ r \in \RR \ST (\bx, r) \in \epi f + \epi g \}.
$$
```

```{prf:proof}

1. Let $(\bx, r) \in \epi f + \epi g$.
1. Then, there exist $(\by, s) \in \epi f$ and $(\bz, t) \in \epi g$
   such that $(\bx, r) = (\by + \bz, s + t)$.
1. $(f \infimal g) (\bx) \leq f(\by) + g(\bz)$.
```

### Epigraph

```{prf:property} Epigraph of infimal convolution
:label: res-cvx-infimal-epi

Let $f, g : \VV \to \ERL$ be given functions. 

1. $\dom f \infimal g = \dom f + \dom g$.
1. $\epi_s f \infimal g = \epi_s f + \epi_s g$.
1. $\epi f + \epi g \subseteq \epi f \infimal g$
   and the equality holds if and only if the
   infimal convolution is exact at each $\bx \in \VV$
   where $(f \infimal g) (\bx) \in \RR$.
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



```{div}
For two proper functions 
$h_1, h_2: \VV \to \RERL$, it holds that:

$$
(h_1 \infimal h_2)^*  = h_1^*  + h_2^*.
$$

Let $h_1 : \VV \to \RERL$ be a proper convex
function and $h_2 : \VV \to \RR$ be a real valued
convex function. Then

$$
(h_1 + h_2)^* = h_1^* \infimal h_2^*.
$$

Let $h_1 : \VV \to \RERL$ be a proper closed convex
function and $h_2 : \VV \to \RR$ be a real valued
convex function. Then

$$
h_1 + h_2 = (h_1^* \infimal h_2^*)^*.
$$

Let $h_1 : \VV \to \RERL$ be a proper convex
function and $h_2 : \VV \to \RR$ be a real valued
convex function. Suppose $h_1 \infimal h_2$ is 
a real valued function. Then


$$
h_1 \infimal h_2 = (h_1^* + h_2^*)^*.
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
