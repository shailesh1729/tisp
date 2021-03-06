(sec:cvx:func:convexity:preserving)=
# Function Operations

In this section we discuss various operations
which generate new functions from a given
function, a pair of functions or a family
of functions. We discuss if the properties
like convexity and closedness are preserved
under these function operations.
Such operations include, scaling, sum,
composition, pointwise supremum, partial minimization,
etc..


Main references for this section are
{cite}`boyd2004convex,bertsekas2003convex`.

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
:label: res-cvxf-conic-comb-funcs

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



## Pointwise Supremum

### Two Functions

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

### Multiple Functions


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

### Family of Functions

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

Consequently, if $f_i$ are closed and convex for every $i \in I$,
then $f$ is closed and convex.
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

Closedness

1. If $f_i$ are closed for every $i \in I$, then $\epi f_i$ is closed for every $i \in I$.
1. Consequently, $\epi f$ is closed, since its an intersection of closed sets.
1. Hence $f$ is a closed function.
```

### Largest Entry

```{prf:example} Convexity of the largest entry in a vector
:label: ex-cvxf-largest-entry-convex

Let $h : \RR^n \to \RR$ be defined as

$$
h (\bx) = \max \{ x_1, \dots, x_n \}.
$$

If we introduce coordinate functions $f_i : \RR^n \to \RR$ as 

$$
f_i(\bx) =  x_i
$$

then, we can write $h$ as

$$
h(\bx) = \max \{ f_1(\bx), \dots, f_n(\bx) \}.
$$

Each of the coordinate functions is linear hence convex.
Thus, $h$ is a maximum of convex functions. Hence $h$ is convex.

```


### Sum of $k$ Largest Entries


```{prf:example} Sum of $k$ largest entries in a vector
:label: ex-cvxf-sum-k-largest-entries


Consider a vector $\bx \in \RR^n$ with $\bx = (x_1, \dots, x_n)$.

1. Let $x_{[i]}$ denote the $i$-th largest entry of $\bx$.
1. In particular, $x_{[1]} = \max \{ x_1, \dots, x_n \}$ is the largest entry of $\bx$.
1. Then, 

   $$
   x_{[2]} = \max \left (\{ x_1, \dots, x_n \} \setminus \{ x_{[1]}\} \right )
   $$
   is the second largest entry of $\bx$.
1. Similarly, 

   $$
   x_{[k]} = \max \left (\{ 
      x_1, \dots, x_n \} \setminus \{ x_{[1]}, \dots, x_{[k-1]}\} \right )
   $$
   is the $k$-th largest entry of $\bx$.
1. In other words, if we sort the entries of $\bx$ in descending order, we can
   pick the largest entries one by one.

We can introduce functions $g_i : \RR^n \to \RR$ as

$$
g_i (\bx) = x_{[i]}.
$$ 
As shown in {prf:ref}`ex-cvxf-largest-entry-convex`, $g_1$ is convex.
However, $g_2,\dots, g_n$ are not convex.

We now introduce a function which computes the sum of $k$ largest entries.
Let $h_k : \RR^n \to \RR$ be given by

$$
h_k (\bx) = \sum_{i=1}^k x_{[i]}.
$$
Then, $h$ is convex. To see this, we proceed as follows:

1. There are $N = {n \choose k}$ ways of choose $k$ indices from the set $1,\dots,n$.
1. Let $I_l = \{i_1^l, \dots, i_k^l \}$ be one of the $N$ ways to choose $k$ indices
   for $l=1,\dots,N$.
1. Let $F_l : \RR^n \to \RR$ be given by

   $$
   F_l (\bx) = x_{i_1^l} + \dots + x_{i_k^l}
   $$
   for $l=1,\dots,N$.
1. Then, $F_l$ is a linear (hence convex) function for every $l=1,\dots,N$.
1. We can now see that

   $$
   h_k(\bx) = \max \{ F_1(\bx), \dots, F_N(\bx) \}.
   $$
1. Thus, $h_k$ is a maximum of $N$ convex functions.
1. Hence $h$ is convex.
```

### Piecewise Linear Function

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

## Projection

```{prf:theorem} Projection for extended valued functions
:label: res-cvxf-projection-ev

Let $\VV$ and $\WW$ be finite dimensional real normed linear spaces.
Let $f : \VV \oplus \WW \to \ERL$ be a convex function.
Let $g_{\bx} : \WW \to \ERL$ be defined by

$$
g_{\bx}(\by)  = f(\bx, \by)
$$

1. If $f$ is convex, then $g_{\bx}$ is convex.
1. If $f$ is proper and $f(\bx, \by) < \infty$ for some $\by$,
   then $g_{\bx}$ is proper.
1. If $f$ is closed, then $g_{\bx}$ is closed.
```

```{prf:proof}

Convexity

1. Let $\by_1, \by_2 \in \WW$ and $t \in [0,1]$.
1. Then

   $$
   g_{\bx}(t \by_1 + (1-t) \by_2)
   &= f(\bx, t \by_1 + (1-t) \by_2) \\
   &= f(t\bx + (1-t) \bx, t \by_1 + (1-t) \by_2) \\
   &= f(t (\bx, \by_1) + (1-t)(\bx, \by_2)) \\
   &\leq t f(\bx, \by_1) + (1-t) f(\bx, \by_2) \\
   &= t g_{\bx}(\by_1) + (1-t) g(\by_2).
   $$
1. Hence $g$ is convex.


Properness

1. Since $f$ is proper, hence $g_{\bx} > -\infty$ for every $\by$.
1. Since $f(\bx, \by) < \infty$ for some $\by$, hence
   $g_{\bx}(\by) < \infty$ for the same $\by$.
1. Hence $g_{\bx}$ is proper.


Closedness

1. Let $G_t = \sublevel(g_{\bx}, t)$ for any $t \in \RR$.
1. Let $F_t = \sublevel(f, t)$ for any $t \in \RR$.
1. By hypothesis, $F_t$ is closed for every $t$.
1. Consider a converging sequence $\{ \by_k \}$ of $G_t$ with $\lim \by_k = \by$.
1. Then $g_{\bx} (\by_k ) \leq t$ for every $k$.
1. Thus $f(\bx, \by_k) \leq t$ for every $k$.
1. Hence $\{ (\bx, \by_k) \}$ is a converging sequence of $F_t$.
1. Since $F_t$ is closed, hence $\{ (\bx, \by_k) \}$ converges in $F_t$.
1. Hence $(\bx, \by) \in F_t$.
1. Hence $f(\bx, \by) \leq t$.
1. Hence $g_{\bx}(\by) \leq t$.
1. Hence $\by \in G_t$.
1. Hence $G_t$ is closed.
1. Hence all sublevel sets of $g_{\bx}$ are closed.
1. Hence $g_{\bx}$ is a closed function.
```


## Partial Minimization

### Real Valued Convex Functions

```{prf:theorem} Partial minimization
:label: res-cvxf-partial-minimization

Let $\VV$ and $\WW$ be real vector spaces.
Let $f : \VV \oplus \WW \to \RR$ be a convex function
with $C \oplus D = \dom f$.
Define a function $g : \VV \to \RR$ as

$$
g(\bx) \triangleq \underset{\by \in D}{\inf} f(\bx, \by), \Forall \bx \in C.
$$
Assume that the infimum is finite for every $\bx \in C$.
Then, $g$ is convex with $C = \dom g$.
```

Note that it is possible that $g(\bx)$ is finite for some
$\bx \in C$ and yet there is no $\by \in D$ such that $(\bx, \by) \in C \oplus D$.
In other words, we only assume that the infimum is finite at every $\bx \in C$.
We don't require that the infimum is attained at some point $(\bx, \by) \in C \oplus D$.

```{prf:proof}
Since $f$ is convex, hence $\dom f$ is convex. 
Thus, $C \oplus D$ is convex. 
By {prf:ref}`res-cvx-convex-set-direct-sum-projection`, $C$ and $D$ are convex.

1. Since the infimum is finite for every $\bx \in C$, hence $\dom g = C$.
1. Thus, $\dom g$ is a convex subset of $\VV$.
1. Let $\bx_1, \bx_2 \in C$ and $t \in (0, 1)$.
1. Take any $r > 0$. 
1. By definition of the infimum, there exist some $\by_1, \by_2 \in D$ such that

   $$
   & f(\bx_1, \by_1) \leq g(\bx_1) + r, \\
   & f(\bx_2, \by_2) \leq g(\bx_2) + r.
   $$
1. Let $(\bx, \by) = t (\bx_1, \by_1) + (1-t) (\bx_2, \by_2)$.
1. Since $f$ is convex, hence 

   $$
   f(\bx, \by) 
   &\leq t f(\bx_1, \by_1) + (1-t) f(\bx_2, \by_2) \\
   &\leq t (g(\bx_1) + r) + (1- t) (g (\bx_2) + r) \\
   = t g(\bx_1) + (1-t) g(\bx_2) + r.
   $$
1. By definition of $g$ 

   $$
   g(\bx) \leq f(\bx, \by) \leq t g(\bx_1) + (1-t) g(\bx_2) + r.
   $$
1. Since this inequality is valid for every $r > 0$, hence

   $$
   g(\bx) \leq t g(\bx_1) + (1-t) g(\bx_2)
   $$
   holds true for every $\bx_1,\bx_2 \in C$ and $t \in (0,1)$.
1. Thus, $g$ is convex.
```


```{prf:example} Convexity of the distance from a convex set function
:label: res-cvxf-set-distance-convex-min

Let $C \subseteq \VV$ be a convex set. The set distance function
$d_C : \VV \to \RR$ is defined by

$$
d_C(\bx) = \inf \{ \| \bx - \by \| \ST \by \in C \}.
$$


We define a function $f : \VV \oplus \VV \to \RR$ as

$$
f(\bx, \by) =  \| \bx - \by \|.
$$
Since the norm is convex, hence $f$ is convex over $\VV \oplus \VV$.
In particular $f$ is convex over the subset $\VV \oplus C$.

Then, by {prf:ref}`res-cvxf-partial-minimization`, $d_C$ is convex.
```

### Proper Convex Functions

```{prf:theorem} Partial minimization for proper convex functions
:label: res-cvxf-partial-minimization-proper

Let $\VV$ and $\WW$ be real vector spaces.
Let $f : \VV \oplus \WW \to \RERL$ be a proper convex function
satisfying the following property:

For every $\bx \in \VV$, there exists $\by \in \WW$ for which
$f(\bx, \by) < \infty$.


Let $g : \VV \to \LERL$ be defined by

$$
g(\bx) \triangleq \inf_{\by \in \WW} f(\bx, \by).
$$
Then $g$ is convex.
```

```{prf:proof}
We first mention that since for every $\bx \in \VV$,
there exists at least one $\by$ such that $f(\bx, \by) < \infty$,
hence $g(\bx) < \infty$ for every $\bx$.
This is why, the range of $g$ is $\LERL$.
Although it still leaves open the possibility that
$g(\bx) = -\infty$ for some $\bx \in \VV$.

We now show that $g$ satisfies the convexity inequality.

1. Let $\bx_1, \bx_2 \in \VV$ and $t \in (0,1)$.
1. We consider the two cases
   1. Both $g(\bx_1), g(\bx_2) > -\infty$.
   1. At least one of them equals $-\infty$. 
      Without loss of generality, assume that $g(\bx_1) = -\infty$.


Case 1: $g(\bx_1), g(\bx_2) > -\infty$

1. Choose some $\epsilon > 0$.
1. By the infimum property, there exist $\by_1, \by_2 \in \WW$
   such that

   $$
   & f(\bx_1, \by_1) \leq g(\bx_1) + \epsilon; \\
   & f(\bx_2, \by_2) \leq g(\bx_2) + \epsilon.
   $$
1. Since $f$ is convex, hence

   $$
   & f(t \bx_1 + (1-t) \bx_2, t \by_1 + (1-t) \by_2) \\
   & \leq t f(\bx_1, \by_1) + (1-t) f(\bx_2, \by_2) \\
   & \leq t (g(\bx_1) + \epsilon) + (1-t) (g(\bx_2) + \epsilon)\\
   & = t g(\bx_1) + (1-t) g(\bx_2) + \epsilon.
   $$
1. By the definition of $g$, we have

   $$
   g(t \bx_1 + (1-t) \bx_2) \leq f(t \bx_1 + (1-t) \bx_2, t \by_1 + (1-t) \by_2).
   $$
1. Thus we have

   $$
   g(t \bx_1 + (1-t) \bx_2) \leq t g(\bx_1) + (1-t) g(\bx_2) + \epsilon.
   $$
1. Since this inequality is valid for every $\epsilon > 0$, hence
 
   $$
   g(t \bx_1 + (1-t) \bx_2) \leq t g(\bx_1) + (1-t) g(\bx_2).
   $$
1. Thus $g$ is convex for this case.


Case 2: $g(\bx_1) = -\infty$.

1. To show that $g$ is convex, we need to show that
   $g(t \bx_1 +(1-t) \bx_2) = -\infty$.
1. Choose any $M \in \RR$.
1. Since $g(\bx_1) = -\infty$, there exists $\by_1 \in \WW$ such that

   $$
   f(\bx_1, \by_1) \leq M.
   $$
1. By hypothesis in the theorem, there exists $\by_2 \in \WW$ such that

   $$
   f(\bx_2, \by_2) < \infty.
   $$
   In other words, $f(\bx_2, \by_2)$ is finite.
1. Using the convexity of $f$, we have

   $$
   & f(t \bx_1 + (1-t) \bx_2, t \by_1 + (1-t) \by_2) \\
   & \leq t f(\bx_1, \by_1) + (1-t) f(\bx_2, \by_2) \\
   & \leq t M  + (1-t) f(\bx_2, \by_2).
   $$
1. By definition of $g$, we have

   $$
   g(t \bx_1 + (1-t) \bx_2) \leq  t M  + (1-t) f(\bx_2, \by_2).
   $$
1. Since the inequality holds for any $M \in \RR$ and the quantity
   $f(\bx_2, \by_2)$ is finite, hence taking the limit $M \to -\infty$
   on the R.H.S., we get

   $$
   g(t \bx_1 + (1-t) \bx_2) = -\infty.
   $$
1. Thus $g$ is convex for this case too.

Combining the two cases, $g$ is convex.
```


### Extended Valued Convex Functions

```{prf:theorem} Partial minimization for extended valued convex functions
:label: res-cvxf-partial-minimization-ev

Let $\VV$ and $\WW$ be real vector spaces.
Let $f : \VV \oplus \WW \to \ERL$ be a convex function.
Let $g : \VV \to \ERL$ be defined by

$$
g(\bx) \triangleq \inf_{\by \in \WW} f(\bx, \by).
$$
Then $g$ is convex.
```

```{prf:proof}

We proceed as follows.

1. If $g(\bx)$ is $\infty$ everywhere then $\epi g$ is empty,
   and $g$ is convex.
1. Hence assume that $\epi g \neq \EmptySet$.
1. If $\dom g$ is singleton, then also $g$ is convex and we are done.
1. Hence assume the case where $\dom g$ is not a singleton.
1. Let $(\bx_a, r_a)$ and $(\bx_b, r_b)$ belong to $\epi g$.
1. Hence $g(\bx_a) \leq r_a$ and $g(\bx_b) \leq r_b$.
1. By definition of $g$, we must have sequences
   $\{ \bu_k \}$ and $\{ \bv_k \}$ of $\WW$ so that

   $$
   f(\bx_a, \bu_k) \to g(\bx_a)
   \text{ and }
   f(\bx_b, \bv_k) \to g(\bx_b).
   $$
1. Pick some $t \in [0,1]$.
1. By definition of $g$

   $$
   g(t \bx_a + (1-t) \bx_b) \leq f(t \bx_a + (1-t) \bx_b, t \bu_k + (1-t) \bv_k) \Forall k.
   $$
1. By convexity of $f$

   $$
   f(t \bx_a + (1-t) \bx_b, t \bu_k + (1-t) \bv_k)
   \leq t f(\bx_a, \bu_k) + (1-t) f(\bx_b, \bv_k) \Forall k.
   $$
1. Hence we have
 
   $$
   g(t \bx_a + (1-t) \bx_b) \leq t f(\bx_a, \bu_k) + (1-t) f(\bx_b, \bv_k) \Forall k.
   $$
1. Taking limit $k \to \infty$ on the R.H.S., we obtain

   $$
   g(t \bx_a + (1-t) \bx_b) \leq t g(\bx_a) + (1-t) g(\bx_b)
   \leq t r_a + (1-t) r_b. 
   $$
1. Hence the point $(t \bx_a + (1-t) \bx_b, t r_a + (1-t) r_b) \in \epi g$.
1. Hence $\epi g$ is convex.
1. Hence $g$ is convex.
```


(sec:cvx:func:partial:min:closedness)=
## Partial Minimization and Closedness

The closedness of a function doesn't imply the closedness
of its partial minimization. The problem is that the
projection operation of a closed set to a subspace
doesn't always preserve the closedness. In this subsection,
we review specific conditions under which the closedness
of a function is guaranteed after partial minimization.

The results in this section draw heavily on
{ref}`sec:cvx:recession`. The reader is
encouraged to familiarize themselves with the
concepts of recession cones and lineality spaces
of convex sets.


We first establish the relationship between the sublevel sets
of the original function and the sublevel sets of its partial
minimization.

### Sublevel Sets

```{prf:lemma} Partial minimization and sublevel-sets
:label: res-cvxf-part-min-sublevel-sets

Let $\VV$ and $\WW$ be Euclidean spaces.
Let $f : \VV \oplus \WW \to \ERL$ be a convex function.
Let $g : \VV \to \ERL$ be defined by

$$
g(\bx) \triangleq \inf_{\bz \in \WW} f(\bx, \bz).
$$

Let $G_t$ denote the set $\sublevel(g, t) = \{ \bx \in \VV \ST g(\bx) \leq t \}$.
Then

$$
G_t = \bigcap_{k=1}^{\infty} \{ \bx \in \VV \ST \text{ there exists }  (\bx, \bz) \in \VV \oplus \WW 
\text{ with } f(\bx, \bz) \leq t_k \} 
$$
where $\{ t_k \}$ is any nonincreasing sequence with $t_k \downarrow t$.

We further note that the set on the R.H.S. is the
projection on $\VV$ of the set $\sublevel(f, t_k)$ where
the projection is given by $(\bx, \bz) \mapsto \bx$.
```

```{prf:proof}
$t_k \downarrow t$ means that
1. $t_k > t$ for every $k$.
1. $t_{k+1} \leq t_k$ for every $k$.
1. For every $\epsilon > 0$, there exists a $k$ such that $t_k \leq t + \epsilon$.

Let $X_t$ denote the set

$$
X_t = \{ \bx \in \VV \ST \text{ there exists }  (\bx, \bz) \in \VV \oplus \WW 
\text{ with } f(\bx, \bz) \leq t \}. 
$$

We first show that $G_t \subseteq \bigcap_{k=1}^{\infty} X_{t_k}$.

1. Let $\bx \in G_t$.
1. Then $g(\bx) \leq t$.
1. Thus $\inf_{\bz \in \WW} f(\bx, \bz) \leq t$.
1. Hence for every $\epsilon > 0$, there exists $\bz$ such that
   $f(\bx, \bz) \leq t + \epsilon$.
1. Since $t_k > t$ for every $k$,
   hence for every $k$, there exists $\bz$ such that $f(\bx, \bz) \leq t_k$.
1. Hence $\bx \in X_{t_k}$ for every $k$.
1. Hence $\bx \in \bigcap_{k=1}^{\infty} X_{t_k}$.
1. Hence $G_t \subseteq \bigcap_{k=1}^{\infty} X_{t_k}$.

Now for the converse,

1. Let $\bx \in \bigcap_{k=1}^{\infty} X_{t_k}$.
1. Then for every $k$, $\bx \in X_{t_k}$.
1. Hence for every $k$, there exists $\bz_k$ such that $f(\bx, \bz_k) \leq t_k$.
1. Also, $g(\bx) \leq f(\bx, \bz_k) \leq t_k$ for every $k$.
1. Taking the infimum on the R.H.S., we get $g(\bx) \leq t$.
1. Hence $\bx \in G_t$.
1. Hence $\bigcap_{k=1}^{\infty} X_{t_k} \subseteq G_t$.

Combining, we get

$$
G_t = \bigcap_{k=1}^{\infty} X_{t_k}.
$$
```

We see that the sublevel set of $g$ is an infinite
intersection of projections of a nested sequence
of sublevel sets of $f$. If the projections are
closed, then the sublevel set of $g$ is also closed.
Thus, to show that $g$ is closed, it is sufficient
to show that the projections of the sublevel sets
of $f$ on $\VV$ are closed.


### Closedness Conditions I

```{prf:theorem} Partial minimization and closedness I
:label: res-cvxf-partial-minimization-closedness-1

Let $\VV$ and $\WW$ be Euclidean spaces.
Let $f : \VV \oplus \WW \to \RERL$ be a proper, closed and convex function.

Let $g : \VV \to \ERL$ be defined by

$$
g(\bx) \triangleq \inf_{\bz \in \WW} f(\bx, \bz).
$$

Assume that there exists a vector $\tilde{\bx} \in \VV$ and a scalar $\gamma$
such that the set

$$
\{ \bz \ST f(\tilde{\bx}, \bz) \leq \gamma \}
$$
is nonempty and compact.
Then $g$ is proper, closed and convex.
Furthermore, for each $\bx \in \dom g$,
the set of points that attain the
infimum of $f(\bx, \cdot)$ over $\WW$
is nonempty and compact. 
```

```{prf:proof}
Due to {prf:ref}`res-cvxf-partial-minimization-ev`,
$g$ is convex. However, this result alone doesn't
guarantee that $g$ is proper or closed.

We shall denote the sublevel sets of $f$ as

$$
V_t = \sublevel(f, t) = \{ (\bx, \bz) \ST f(\bx, \bz) \leq t \}.
$$
We first establish that for any nonempty sublevel set $V_t$, there is no nonzero
direction of recession of the form $(\bzero, \by)$.

1. By hypothesis $\VV_{\gamma}$ is nonempty since there exists
   a $\bz$ such that $f(\tilde{\bx}, \bz) \leq \gamma$.
1. By {prf:ref}`def-cvx-func-recession-cone`, all nonempty sublevel sets
   of $f$ have the same
   recession cone given by $R_f$.
1. Let $(\bzero, \by) \in R_f$ be a direction of recession of $f$.
1. Then $(\bzero, \by)$ is also a direction of recession of $V_{\gamma}$.
1. For any $(\tilde{\bx}, \bz) \in V_{\gamma}$,
   such a direction of recession will satisfy

   $$
   f(\tilde{\bx}, \bz + \alpha \by) \leq \gamma \Forall \alpha \geq 0.
   $$
1. Since, by hypothesis, the set $\{ \bz \ST f(\tilde{\bx}, \bz) \leq \gamma \}$
   is compact, hence the previous statement can be true only if
   $\by = \bzero$.
1. Thus there is no nonzero direction of recession of $V_{\gamma}$ of the
   form $(\bzero, \by)$.
1. Since all sublevel sets share the same recession cone, hence
   for any nonempty sublevel set $V_t$, there is no nonzero direction of recession
   of the form $(\bzero, \by)$.

We now show that $g$ is a closed function. For this,
we shall show that the projection of every
sublevel set of $f$ to $\VV$ is closed.

1. If $V_t$ is an empty sublevel set of $f$ then its projection
   to $\VV$ is also an empty set which is a closed set. 
1. Now let $V_t$ be any nonempty sublevel set of $f$.
1. Let $p : \VV \oplus \WW \to \VV$ denote the projection operator
   given by

   $$
   p(\bx, \by) = \bx.
   $$
1. Note that $p$ is a linear operator.
1. The nullspace of this projection operator is the set of vectors of the
   form $(\bzero, \by)$.
1. Hence the nullspace of $p$ doesn't contain any nonzero direction of
   recession of $V_t$. 
1. Also, $R_{V_t} \cap (\nullspace p) = \{ (\bzero, \bzero) \} \subseteq L_{V_t}$
   since $(\bzero, \bzero)$ always belongs to the lineality space of $V_t$.
1. Hence, due to {prf:ref}`res-cvx-closed-im-lin-op-closed`, the projection
   of $V_t$ to $\VV$ under $p$ is closed.
1. By {prf:ref}`res-cvxf-part-min-sublevel-sets`,
   a sublevel set of $g$ is an infinite intersection of projections
   of a nested sequence of sublevel sets of $f$.
1. Since projection of every nonempty sublevel set of $f$ is closed,
   hence an intersection of any sequence of such projections is closed.
1. Thus every sublevel set of $g$ is closed.
1. Hence $g$ is closed.


We introduce a function $h_{\bx} : \WW \to \RERL$ as

$$
h_{\bx} (\bz) = f(\bx, \bz) \Forall \bz \in \WW.
$$

1. For every $\bx \in \dom g$, there exists $\bz \in \WW$
   such that $f(\bx, \bz) < \infty$.
1. Hence for every $\bx \in \dom g$, the function
   $h_{\bx}$ is proper, closed and convex
   due to {prf:ref}`res-cvxf-projection-ev`.
1. We can see that 

   $$
   g(\bx) = \inf_{\bz \in \WW} h_{\bx}(\bz).
   $$
1. By our previous argument, the function $h_{\bx}$
   has no nonzero direction of recession.
1. Hence the recession cone of every nonempty sublevel
   set of $h_{\bx}$ is $\{ \bzero \}$.
1. Then due to {prf:ref}`res-cvx-recession-dir-nz-unbounded`, every nonempty
   sublevel set is closed and bounded, hence compact.
1. Then due to Weierstrass theorem ({prf:ref}`res-opt-weierstrass-theorem`),
   the set of minimizers of $h_{\bx}$ is nonempty and compact
   (since one of the sublevel sets is nonempty and bounded).


We now show that $g$ is proper.

1. $g(\tilde{\bx}) = \inf_{\bz \in \WW} f(\tilde{\bx}, \bz)$.
1. By hypothesis, there exist $\bz \in \WW$ such that $f(\tilde{\bx}, \bz) \leq \gamma$.
1. Hence $g(\tilde{\bx}) \leq \gamma < \infty$.
1. Let $\bx \in \dom g$.
1. We have shown that the set of minimizers of $h_{\bx}$
   is nonempty and compact.
1. Hence $g(\bx) > -\infty$ for every $\bx \in \dom g$.
1. Hence $g$ is proper.
```



### Closedness Conditions II

```{prf:theorem} Partial minimization and closedness II
:label: res-cvxf-partial-minimization-closedness-2

Let $\VV$ and $\WW$ be Euclidean spaces.
Let $f : \VV \oplus \WW \to \RERL$ be a proper, closed and convex function.

Let $g : \VV \to \ERL$ be defined by

$$
g(\bx) \triangleq \inf_{\bz \in \WW} f(\bx, \bz).
$$

Assume that there exists a vector $\tilde{\bx} \in \VV$ and a scalar $\gamma$
such that the set

$$
K = \{ \bz \ST f(\tilde{\bx}, \bz) \leq \gamma \}
$$
is nonempty and its recession cone is equal to its lineality space.
Then $g$ is proper, closed and convex.
Furthermore, for each $\bx \in \dom g$,
the set of points that attain the
infimum of $f(\bx, \cdot)$ over $\WW$
is nonempty. 
```

```{prf:proof}
The proof is along similar lines.
Due to {prf:ref}`res-cvxf-partial-minimization-ev`,
$g$ is convex.

We shall denote the sublevel sets of $f$ as

$$
V_t = \sublevel(f, t) = \{ (\bx, \bz) \ST f(\bx, \bz) \leq t \}.
$$

1. By hypothesis $\VV_{\gamma}$ is nonempty since there exists
   a $\bz$ such that $f(\tilde{\bx}, \bz) \leq \gamma$.
1. Let $(\bzero, \by) \in R_f$ be a direction of recession of $f$.
1. Then $(\bzero, \by)$ is also a direction of recession of $V_{\gamma}$.
1. For any $(\tilde{\bx}, \bz) \in V_{\gamma}$,
   such a direction of recession will satisfy

   $$
   f(\tilde{\bx}, \bz + \alpha \by) \leq \gamma \Forall \alpha \geq 0.
   $$
1. Thus for every $\bz \in K$ and $\alpha \geq 0$, we have
   $\bz + \alpha \by \in K$.
1. Then $\by$ is a direction of recession of $K$.
1. By hypothesis $R_K = L_K$.
1. Hence $-\by$ is also a direction of recession of $K$.
1. Thus For any $(\tilde{\bx}, \bz) \in V_{\gamma}$,

   $$
   f(\tilde{\bx}, \bz - \alpha \by) \leq \gamma \Forall \alpha \geq 0.
   $$
1. Thus, $(\bzero, -\by)$ is also a direction of recession for $V_{\gamma}$
   due to {prf:ref}`res-cvx-recession-dir-charac`.
1. Hence $(\bzero, -\by) \in R_f$.
1. Since both $(\bzero, \by) \in R_f$ and $(\bzero, -\by) \in R_f$,
   hence $(\bzero, \by) \in L_f$. 
1. Hence $(\bzero, \by)$ is a direction along with $f(\tilde{\bx}, \cdot)$
   is constant.
1. Hence for any nonempty sublevel set $V_t$ of $f$,
   a direction of recession of the form $(\bzero, \by)$ is
   also in the lineality space of $V_t$.


We now show that $g$ is closed.

1. Let $V_t$ be any nonempty sublevel set of $f$.
1. Let $p$ be the projection operator as defined in the proof of
   {prf:ref}`res-cvxf-partial-minimization-ev`.
1. Then $\nullspace p = \{ (\bzero, \by) \ST \by \in \WW \}$.
1. If $(\bzero, \by) \in R_{V_t}$ then $(\bzero, \by) \in L_{V_t}$
   by the previous argument.
1. Hence $R_{V_t} \cap \nullspace p \subseteq  L_{V_t}$.
1. Hence, due to {prf:ref}`res-cvx-closed-im-lin-op-closed`,
   the projection of $V_t$ to $\VV$ under $p$ is closed.
1. Hence $g$ is closed.


As before, we define $h_{\bx} : \WW \to \RERL$
as a projection of $f$ by fixing $\bx$.

1. For every $\bx \in \dom g$, $h_{\bx}$ is proper,
   closed and convex.
1. By the previous argument $R_{h_{\bx}} = L_{h_{\bx}}$.
1. Following the arguments of {prf:ref}`res-opt-const-min-nonempty-minimizers`,
   the set of minimizers of $h_{\bx}$ is nonempty.
1. Hence $g(\bx)$ is finite for every $\bx \in \dom g$.
1. In particular $g(\tilde{\bx}) < \infty$ since $K$ is nonempty.
1. Hence $g$ is proper.
```
