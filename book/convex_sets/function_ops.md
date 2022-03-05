# Convexity Preserving Function Operations

## Scaling and Addition of Convex Functions

Here we show some basic results about operations
that preserve convexity

```{prf:theorem} Nonnegative multiplication
:label: res-cvxf-nonnegative-mult-cvx

If $f$ is convex, then so is $\alpha f$ for all $\alpha \geq 0$.
```
```{prf:proof}

Assume $f$ is convex.
Note that $\dom f = \dom \alpha f$. 
Thus, $\dom \alpha f$ is convex since $\dom f$ is convex.

Now, let $\bx, \by \in \dom f$ and $t \in [0,1]$. Then

$$
& f(t\bx + (1-t) \by) \leq t f(\bx) + (1-t)f(\by)\\
& \implies  \alpha f(t\bx + (1-t) \by) \leq \alpha (t f(\bx) + (1-t)f(\by)) \Forall \alpha \geq 0\\
& \implies (\alpha f)(t\bx + (1-t) \by) \leq  t (\alpha f)(\bx) + (1-t) (\alpha f)(\by) \Forall \alpha \geq 0.
$$
Thus, $\alpha f$ is convex for every $\alpha \geq 0$.
```


```{prf:theorem} Convex function sum
:label: res-cvxf-func-sum

If $f$ and $g$ are convex, then so is $f + g$
with $\dom (f + g) = \dom f \cap \dom g$.
```
```{prf:proof}
We discussed earlier that $\dom (f + g) = \dom f \cap \dom g$
as $f + g$ is defined only for the points where both $f$ and $g$
are defined.

Recall from {prf:ref}`res-cvx-intersection`
that intersection of convex sets is convex.
Thus, $\dom (f + g)$ is convex since $\dom f$ and $\dom g$
are both convex.

Now let $\bx, \by \in \dom (f + g)$ and $t \in [0, 1]$.

1. Since $f$ is convex, hence
   
   $$
   f(t\bx + (1-t) \by) \leq t f(\bx) + (1-t) f(\by).
   $$
1. Since $g$ is convex, hence
   
   $$
   g(t\bx + (1-t) \by) \leq t g(\bx) + (1-t) g(\by).
   $$
1. Adding the two inequalities, we get:

   $$
   & f(t\bx + (1-t) \by) + g(t\bx + (1-t) \by) \leq 
   t f(\bx) + (1-t) f(\by) + t g(\bx) + (1-t) g(\by)\\
   & \implies 
   (f + g)(t\bx + (1-t) \by) \leq t (f + g)(\bx) + (1-t) (f + g)(\by).
   $$
1. Thus, $f+g$ is convex.
```

```{prf:theorem} Conic combinations of convex functions
:label: res-cvxf-func-conic-combs

If $f_1, \dots, f_n$ are convex, then for any
$t_1, \dots, t_n \geq 0$, the 
{prf:ref}`conic combination <def-conic-combination>`
of functions given by:

$$
f = t_1 f_1 + \dots + t_n f_n
$$
is also convex.
```

The conic combinations are also called nonnegative weighted
sums.

```{prf:proof}
Due to {prf:ref}`res-cvxf-nonnegative-mult-cvx`,
$t_i f_i$ are convex since $f_i$ are convex and $t_i \geq 0$.

Due to {prf:ref}`res-cvxf-func-sum`, sum
of two convex functions is convex.

It can be easily shown by mathematical induction
that sum of $n$ convex functions is convex too.

Thus, $f$ is convex.
```

```{prf:theorem}
:label: res-cvxf-total-funcs-cvx-cone

The set of convex functions 
in the {prf:ref}`vector space of real valued functions <def-la-is-real-valued-functions-space>`
form a convex cone.
```

Note that the set of real valued functions forms a vector
space over $\RR$ with the standard definitions of
function scalar multiplication and function addition.
We are examining the convexity of the set of functions
under this vector space.


```{prf:proof}
Since every conic combination of convex functions
is convex, hence the set of convex functions is
a convex cone.
```

```{prf:theorem} Concave function sum
:label: res-cvxf-concave-func-sum

If $f$ and $g$ are concave, then so is $f + g$
with $\dom (f + g) = \dom f \cap \dom g$.
```
```{prf:proof}
We proceed as follows:

1. Let $f$ and $g$ be concave.
1. $-f$ and $-g$ are convex.
1. By {prf:ref}`res-cvxf-func-sum`, $(-f) + (-g) = -(f + g)$
   is convex.
1. Thus, $f+g$ is concave.
```

```{prf:theorem} Conic combinations of cave functions
:label: res-cvxf-concave-func-conic-combs

If $f_1, \dots, f_n$ are concave, then for any
$t_1, \dots, t_n \geq 0$, the 
{prf:ref}`conic combination <def-conic-combination>`
of functions given by:

$$
f = t_1 f_1 + \dots + t_n f_n
$$
is also concave.
```

```{prf:proof}
We proceed as follows:

1. If $f_1, \dots, f_n$ are concave then $-f_1, \dots, -f_n$ are convex.
1. By {prf:ref}`res-cvxf-func-conic-combs`, 
   $(-t_1 f_1) + \dots + (-t_n f_n)$ is convex.
1. Thus, $-(t_1 f_1 + \dots + t_n f_n)$ is convex.
1. Thus, $t_1 f_1 + \dots + t_n f_n$ is concave. 
```

## Composition with Nondecreasing Functions

```{prf:theorem} Composition with a convex nondecreasing function preserves convexity
:label: res-cvx-convex-nondec-composition

Let $\VV$ be a real vector space. 
Let $f : \VV \to \RERL$ be a proper convex function. 
Let $g : \RR \to \RERL$ be a convex function which is nondecreasing. 

Then, their composition $h = g \circ f$ given by:

$$
h (\bx) = g ( f (\bx)) \Forall \bx \in \VV
$$
with $g(\infty) = \infty$, is convex on $\VV$. 
```

```{prf:proof}
We note that $\dom h = \dom f \cap \dom g$.
Since both $f$ and $g$ are convex, hence
$\dom f$ and $\dom g$ are convex and hence
$\dom h$ is convex.

Choose any $\bx, \by \in \VV$ and $t \in (0, 1)$.

1. We need to show that 
   
   $$
   h((1-t) \bx + t \by) \leq (1-t) h(\bx) + t h(\by).
   $$
1. If $\bx \notin \dom f$, then $h(\bx) = g(f(\bx)) = \infty$.
   Similarly, if $\by \notin \dom f$, then $h(\by) = g(f(\by)) = \infty$.
1. In either case, the convexity inequality will be satisfied trivially.
1. Let us now consider the case where $\bx, \by \in \dom f$.
1. By convexity of $f$, we have:

   $$
   f((1-t) \bx + t \by) \leq (1-t) f(\bx) + t f(\by).
   $$
1. Note that $(1-t) f(\bx) + t f(\by)$ is a convex combination of $f(\bx)$ and $f(\by)$.
1. Since $g$ is nondecreasing, hence if $r \leq s$ then $g(r) \leq g(s)$.
1. By applying $g$ on both sides of the previous inequality, we obtain

   $$
   h ((1-t) \bx + t \by) 
   &= g (f ((1-t) \bx + t \by)) \\ 
   &\leq g((1-t) f(\bx) + t f(\by)) \\
   &\leq (1-t) g(f(\bx)) + t g(f(\by)) \\
   &= (1-t) h(\bx) + t h(\by).
   $$
1. Thus, $h$ is convex.
```

```{prf:example} Exponential of a convex function
:label: ex-cvxf-exp-cvx-func

Recall from {prf:ref}`ex-cvxf-real-exponential` that the exponential function $e^x$
is convex. 

Then, for any convex $f$,  $h(x) = e^{f(x)}$ is convex
due to {prf:ref}`res-cvx-convex-nondec-composition`.
```

```{prf:example} Power of a nonnegative convex function
:label: ex-cvxf-pow-cvx-func-non-neg

Let $f: \VV \to \RR$ be a proper convex and nonnegative function.

Then, $f(x) = | f(x) |$. 

Let $p \geq 1$ and consider the function $g(x) = |x|^p$.
By {prf:ref}`ex-cvxf-real-power-absolute-x-p`, $g$ is convex.

Then, $ h = g \circ f$ given by

$$
h(\bx) = g(f(\bx)) = | f(\bx) |^p  = f(\bx)^p
$$
is also convex.
```

```{prf:example} Power of a norm
:label: ex-cvxf-pow-norm

Let $\| \cdot \| : \VV \to \RR$ be a norm on the
real vector space $\VV$. Let $p \geq 1$.

Then, the $p$-th power of the norm given by

$$
h(\bx) = \| \bx \|^p \Forall \bx \in \VV 
$$
is convex.

1. The norm is a convex and nonnegative function.
1. $g(x) = |x|^p$ is convex.
1. By {prf:ref}`res-cvx-convex-nondec-composition`,
   $\| \cdot \|^p$ is convex.
```

```{prf:example} Reciprocal of a concave function
:label: ex-cvxf-concave-reciprocal-convex

Let $g$ be a concave function. 
Then, $h(\bx) = \frac{1}{g(\bx)}$ is convex
on the set $C = \{\bx \ST g(\bx) > 0 \}$.

1. Since $g$ is concave, hence $f = -g$ is convex.
1. For all $\bx \in C$, $f(\bx) < 0$.
1. Consider the function

   $$
   \phi(x) = \begin{cases} 
   \frac{1}{x} & \text{ if } & x < 0\\
   \infty & \text{ if } & x \geq 0.
   \end{cases}
   $$
1. It is easy to see that $\phi$ is convex with
   the domain $\RR_{++}$
   ({prf:ref}`ex-cvxf-real-reciprocal-power-x-r`).
1. We can see that, $h = \phi \circ f$.
1. Since $f$ is convex and negative, 
   $h$ is also convex with $\dom h = C \cap \RR_{++}$.
```

```{prf:example} Scaling and translation of a convex function
:label: ex-cvxf-convex-func-scale-translate

Let $f : \VV \to \RR$ be a proper convex function.
Let $m \geq 0$ and $c \in \RR$.  
Let $g : \RR \to \RR$ be given by

$$
g(x) = m x + c.
$$
Then, $g$ is convex (in fact affine) and nondecreasing.

Thus, $h = g \circ f = m f + c$ is also a
proper convex function due to
{prf:ref}`res-cvx-convex-nondec-composition`.
```



## Composition with Affine Mapping


```{prf:theorem} Affine transformations preserve convexity
:label: res-cvx-affine-composition

Let $\VV$ and $\WW$ be real vector spaces.
Let $T : \VV \to \WW$ be a linear transformation.
Let $\bb \in \WW$.
Let $f : \WW \to \RR$ be a function.
Define $g : \VV \to \RR$ as:

$$
g(\bx) = f(T(\bx) + \bb)
$$
with $\dom g = \{\bx \in \VV \ST T(\bx) + \bb \in \dom f \}$.

If $f$ is convex, then so is $g$.
If $f$ is concave, then so is $g$.
```


```{prf:proof}

Assume $f$ is convex.

1. If we define $A : \VV \to \WW$ as $A(\bx) = T(\bx) + \bb $
   then $\dom g = A^{-1}(\dom f)$.
1. $A$, so defined, is an affine transformation.
1. By {prf:ref}`res-cvx-convex-set-inverse-affine-image`,
   $\dom g$ is convex since $\dom f$ is convex. 
1. Let $\bx, \by \in \dom g$.
1. $g(\bx) = f(T(\bx) + \bb)$. Define $\bu = T(\bx) + \bb$.
1. $g(\by) = f(T(\by) + \bb)$. Define $\bv = T(\by) + \bb$.
1. By definition, $\bu, \bv \in \dom f$.
1. Let $t \in [0,1]$.
1. Since $f$ is convex, hence

   $$
   f(t\bu + (1-t) \bv) \leq t f(\bu) + (1-t)f(\bv).
   $$
1. Now 

   $$
   g(t\bx + (1-t) \by)
   &= f(T(t\bx + (1-t) \by) + \bb)\\
   &= f(tT(\bx) + (1-t) T(\by) + (t + (1-t))\bb)\\
   &= f(t(T(\bx) + \bb) + (1-t) (T(\by) + \bb))\\
   &= f(t\bu + (1-t) \bv )\\
   &\leq t f(\bu) + (1-t) f(\bv)\\
   &= t g(\bx) + (1-t) g(\by).
   $$
1. Thus, $g$ satisfies the 
   convexity defining inequality {eq}`eq-convexity-inequality`.
1. Thus, $g$ is convex.

A similar argument shows that if $f$ is concave
then so is $g$.
```

## Sum of Functions

```{prf:theorem} Sum of convex functions
:label: res-cvx-function-sum-convex

Let $\VV$ be a real vector space.
Let $f_1 : \VV \to \RERL$ and $f_2 : \VV \to \RERL$
be proper convex functions. Then, the function
$f = f_1 + f_2$ is a proper convex function.
```

We note that since both $f_1$ and $f_2$ are proper,
hence neither attains a value of $-\infty$, thus
undesired sums like $\infty - \infty$ are avoided.

```{prf:proof}

Convexity of the domain

1. Since $f_1$ is convex, hence $\dom f_1$ is a convex set.
1. Since $f_2$ is convex, hence $\dom f_2$ is a convex set.
1. By definition of function sum $\dom f = \dom f_1 \cap \dom f_2$.
1. Intersection of convex sets is convex.
1. Hence, $\dom f$ is convex.

We note that $f(\bx) < \infty$ if and only if $f_1(\bx) < \infty$
and $f_1(\bx) < \infty$.

If $\dom f = \EmptySet$, then 
by {prf:ref}`res-cvxf-empty-func-convex`, $f$ is convex.
We are left with the case where $\dom f$ is not empty.


Convexity inequality

1. Let $\bx, \by \in \dom f$. Let $t \in (0, 1)$.
1. Then, $\bx, \by \in \dom f_1$
   as well as $\bx, \by \in \dom f_2$.
1. By convexity of $f_1$

   $$
   f_1(t \bx + (1-t) \by) \leq t f_1(\bx) + (1-t)f_1(\by).
   $$
1. By convexity of $f_2$

   $$
   f_2(t \bx + (1-t) \by) \leq t f_2(\bx) + (1-t)f_2(\by).
   $$
1. Summing these inequalities, we get:

   $$
   f(t \bx + (1-t) \by) \leq t f(\bx) + (1-t)f(\by).
   $$
```


```{prf:corollary} Sum of multiple convex functions
:label: res-cvx-function-sum-convex-n

Let $\VV$ be a real vector space.
Let $f_1, \dots, f_k : \VV \to \RERL$
be proper convex functions. Then, the function
$f = f_1 + \dots + f_k$ is a proper convex function.
```

```{prf:proof}
We note that $\dom f = \bigcap_{i=1}^k \dom f_k$.
$\dom f$ is convex since it is an intersection of
convex sets.
The proof of convexity is a simple application of
mathematical induction.

1. Let $g_r = f_1 + \dots + f_r$ for $r \in 2,\dots, k$.
1. By {prf:ref}`res-cvx-function-sum-convex`, $g_2 = f_1 + f_2$
   is a proper convex function.
1. Assume that $g_r$ is a  proper convex function for some $r$.
1. Then, $g_{r+1} = g_r + f_{r+1}$.
1. Since both $g_r$ and $f_{r+1}$ are proper convex, hence
   $g_{r+1}$ is also a proper convex function.
```

```{prf:theorem} Conic combination of convex functions

Let $\VV$ be a real vector space.
Let $f_1, \dots, f_k : \VV \to \RERL$
be proper convex functions. 
Let $r_1, \dots, r_k \geq 0$.

Then, the function
$f = r_1 f_1 + \dots + r_k f_k$ is a proper convex function.
$f$ is a conic combination of $f_1, \dots, f_k$.
```

```{prf:proof}
By {prf:ref}`ex-cvxf-convex-func-scale-translate`,
$r_i f_i$ are proper convex functions.

By {prf:ref}`res-cvx-function-sum-convex-n`, 
their sum is a proper convex function.
```

```{prf:example} Restricting the domain of a convex function
:label: ex-cvxf-restrict-domain-ind-sum


Let $f : \VV \to \RR$ be a convex function with
$\dom f = \VV$.

Let $C \subseteq \VV$ be a convex set.
Let $I_C$ be the indicator function for the set $C$ given by

$$
I_C(\bx) =  \begin{cases}
0 & \text{ if } & \bx \in C\\
\infty & \text{ if } & \bx \notin C.
\end{cases}
$$


Consider the proper function $h = f + I_C$ given by


$$
h(\bx) = f(\bx) + I_C(\bx) =  \begin{cases}
f(\bx) & \text{ if } & \bx \in C\\
\infty & \text{ if } & \bx \notin C.
\end{cases}
$$

By {prf:ref}`res-cvx-function-sum-convex`,
$h$ is a proper convex function.
$\dom h = \dom f \cap \dom I_C = \VV \cap C = C$.

Thus, $h$ restricts the effective domain of $f$ to $C$.
```

## Construction from $\VV \oplus \RR$

One way to construct convex functions on $\VV$ 
is from convex sets in $\VV \oplus \RR$.

```{prf:theorem} Construction from convex sets of $\VV \oplus \RR$
:label: res-cvxf-construct-convex-sets-dirsum


Let $\VV$ be a real vector space.
Let $F \subseteq \VV \oplus \RR$ be a convex
subset of $\VV \oplus \RR$. 
Let $f : \VV \to \RERL$ be defined as

$$
f(\bx) \triangleq \inf \{t \in \RR \ST (\bx, t) \in F \}.
$$

Then, $f$ is a proper convex function on $\VV$.
```

We note that $f(\bx) = \infty$ if there is
no $t \in \RR$ such that $(\bx, t) \in F$.
This is consistent since $\inf \EmptySet = \infty$.


```{prf:proof}

Convexity of domain of $f$

1. We note that for some $\bv \in \VV$, if there
   is no $t \in \RR$ such that $(\bv, t) \in F$,
   then $f(\bv) = \infty$ and $\bv \notin \dom f$.
1. Thus, if $\bv \in \dom f$, then there exists
   $t \in \RR$ such that $(\bv, t) \in F$.
1. Let $\bx, \by \in \dom f$ and $t \in (0, 1)$.
1. Then, there exists $(\bx, p) \in F$ 
   and $(\by, q) \in F$ for some $p,q \in \RR$.
1. Since $F$ is convex, hence
   
   $$
   t(\bx, p) + (1-t)(\by, q) 
   = (t \bx + (1-t) \by, t p + (1-t)q ) \in F.
   $$
1. But then, $f(t \bx + (1-t) \by) \leq  t p + (1-t)q \in \RR$.
1. Thus,  $t \bx + (1-t) \by \in \dom f$.
1. Thus, $\dom f$ is convex.


Convexity inequality in the domain

1. Let $\bx, \by \in \dom f$ and $t \in (0, 1)$.
1. Let $X = \{v \in \RR \ST (\bx, v) \in F \}$.
1. Let $Y = \{v \in \RR \ST (\by, v) \in F \}$.
1. By definition of $f$, $f(\bx) = \inf X$ and $f(\by) = \inf Y$.
1. Let $\bz = t \bx + (1-t) \by$.
1. Let $Z = \{v \in \RR \ST (\bz, v) \in F \}$. 
1. We have $f(\bz) = \inf Z$.
1. Since $F$ is convex, hence 
   for every $p \in X$ and every $q \in Y$,
   the point $(t\bx + (1-t)\by, t p + (1-t) q) = (\bz, t p + (1-t) q) \in F$.
1. Thus, for every $p \in X$ and every $q \in Y$,
   $t p + (1-t) q \in Z$.
1. But then, $\inf Z \leq t p + (1-t) q$ for every $p \in X$ 
   and every $q \in Y$.
1. Thus, taking infimum on the R.H.S. over $X$ and $Y$, 
   
   $$
   \inf Z \leq \inf_{p \in X} \inf_{q \in Y} (t p + (1-t) q ) 
   = t \inf X + (1-t) \inf Y.
   $$
1. In other words

   $$
   f(t \bx + (1-t) \by) = f(\bz) \leq t f(\bx) + (1-t) f(\by).
   $$
1. Thus, $f$ is convex.
```

We note that $F \neq \epi f$. Although, $F \subseteq \epi f$ 
and can be easily
extended to become $\epi f$.


## Infimal Convolution

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

## Pointwise Supremum

```{prf:theorem} Pointwise maximum of two convex functions
:label: res-cvx-ptws-max-2

Let $f_1$ and $f_2$ be convex functions. Define
their pointwise maximum as

$$
f(\bx) = \max \{f_1(\bx), f_2(\bx) \}
$$
with $\dom f = \dom f_1 \cap \dom f_2$.
Then, $f$ is convex.
```

```{prf:proof}
$\dom f$ is an intersection of convex sets. Hence, it is convex.

Let $\bx, \by \in \dom f$ and $t \in [0,1]$.

$$
f(t \bx + (1-t) \by)
&= \max \{f_1(t \bx + (1-t) \by), f_2(t \bx + (1-t) \by) \}\\
&\leq \max \{t f_1(\bx) + (1-t) f_1(\by), t f_2(\bx) + (1-t) f_2(\by) \}\\
&\leq t \max \{f_1(\bx), f_2(\bx) \} + (1-t)\max \{f_1(\by), f_2(\by) \}\\
&= t f(\bx) + (1-t) f(\by).
$$
Thus, $f$ is convex.
```


```{prf:theorem} Pointwise maximum of multiple convex functions
:label: res-cvx-ptws-max-n

Let $f_1, f_2, \dots, f_n$ be convex functions. Define
their pointwise maximum as

$$
f(\bx) = \max \{f_1(\bx), \dots, f_n(\bx) \}
$$
with $\dom f = \dom f_1 \cap \dots \cap \dom f_n$.
Then, $f$ is convex.
```

```{prf:proof}
The result has been proved for the base case of 2 functions
in {prf:ref}`res-cvx-ptws-max-2`.

Assume that it is true for $n$ functions. We
can easily show it true for $n+1$ functions since

$$
\max \{f_1(\bx), \dots, f_{n+1}(\bx) \}
= \max \{\max \{f_1(\bx), \dots, f_n(\bx) \}, f_{n+1}(\bx) \}.
$$

Thus, by principle of mathematical induction, the result
is true for all $n$.
```

```{prf:theorem} Pointwise supremum of a family of convex functions
:label: res-cvx-ptws-supremum

Let $I$ be an index set.
Let $\{ f_i : \VV \to \RR \}_{i \in I}$ be a family of convex functions. 
Define their pointwise supremum as

$$
f(\bx) = \sup \{f_i(\bx)\}_{i \in I}
$$
with 

$$
\dom f = \bigcap_{i \in I} \dom f_i.
$$
Then, $f$ is convex.
Moreover,

$$
\epi f = \bigcap_{i \in I} \epi f_i.
$$
```

```{prf:proof}
We  shall first verify the epigraph equality.

1. Let $(\bx, t) \in \epi f$.
1. Then, $f(\bx) \leq t$.
1. Thus, $f_i(\bx) \leq t$ for all $i \in I$ 
   since $f(\bx) = \sup \{f_i(\bx)\}_{i \in I}$.
1. Thus, $(\bx, t) \in \epi f_i$ for all $i \in I$.
1. Thus, $\epi f \subseteq \bigcap_{i \in I} \epi f_i$.


Now, for the converse:

1. Let $(\bx, t) \in \bigcap_{i \in I} \epi f_i$.
1. Thus, $(\bx, t) \in \epi f_i$ for all $i \in I$.
1. Thus, $f_i(\bx) \leq t$ for all $i \in I$.
1. Taking the supremum over $i \in I$ on the L.H.S., we obtain:

   $$
   \sup \{f_i(\bx)\}_{i \in I} = f(\bx) \leq t.
   $$
1. Thus, $(\bx, t) \in \epi f$.
1. Thus, $\bigcap_{i \in I} \epi f_i \subseteq \epi f$.

Combining the two, we get:

$$
\epi f = \bigcap_{i \in I} \epi f_i.
$$

1. Since $f_i$ are convex functions, hence $\epi f_i$ are convex sets
   due to {prf:ref}`res-cvxf-convexity-epigraph`.
1. Thus, $\epi f$ is a convex set due to {prf:ref}`res-cvx-arbitrary-intersection`.
1. But then, $f$ is convex
   again due to {prf:ref}`res-cvxf-convexity-epigraph`.
```


```{prf:definition} Piecewise linear function
:label: def-cvxf-piecewise-linear-func

Let $\ba_1, \dots, \ba_n \in \VV$.
Let $b_1, \dots, b_n \in \RR$.

A function $f: \VV \to \RR$ given by:

$$
f(\bx) = \max \{\langle \bx, \ba_i \rangle + b_i  \}_{i \in 1, \dots, n}
$$
is called a *piecewise linear* or *piecewise affine* function.
```


```{prf:theorem}
:label: res-cvxf-piecewise-linear-convex

Piecewise linear functions are convex.
```

```{prf:proof}
Each of the functions $f_i (\bx) = \langle \bx, \ba_i \rangle + b_i$
is affine functionals. 
Thus, $f_i$ are convex ({prf:ref}`res-cvxf-affine-functional-convex`).
$f$ is a pointwise maximum of $n$ convex functions.
Hence, $f$ is convex ({prf:ref}`res-cvx-ptws-max-n`).
```

