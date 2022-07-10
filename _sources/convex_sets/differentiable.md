(sec:cvx:func:differentiability)=
# Differentiability and Convex Functions

## First Order Conditions

Let us look at the special case of 
real valued functions over $\RR^n$ 
which are differentiable.

````{prf:theorem} First order characterization of convexity
:label: res-cvxf-gradient-convexity-relation

Let $f : \RR^n \to \RR$ be a real valued function
which is {prf:ref}`differentiable <def-mvc-differentiable-function>`
at each point in $\dom f$ which is open.

Then $f$ is convex if and only if $\dom f$ is convex
and 

```{math}
:label: eq-cvxf-first-order-convexity-condition
f(\by) \geq f(\bx) + \nabla f(\bx)^T (\by - \bx)
```
holds true for all $\bx, \by \in \dom f$.
````


```{prf:proof}
To prove {eq}`eq-cvxf-first-order-convexity-condition`,
we first show that a differentiable real function $f: \RR \to \RR$
is convex if and only if  

$$
f(y) \geq f(x) + f'(x)(y - x)
$$
holds true for all $x, y \in \dom f$.


Assume that $f$ is convex. Hence, $\dom f$ is convex too.

1. Let $x,y \in \dom f$.
1. Since $\dom f$ is convex, hence 
   $ (1-t) x + t y = x + t(y-x) \in \dom f$ for all $t \in [0, 1]$.
1. By convexity of $f$, we have:

   $$
   f(x + t(y-x)) \leq (1-t) f(x) + t f(y).
   $$
1. If we divide by $t$ on both sides, we obtain:

   $$
   f(y) \geq f(x) + \frac{f(x + t(y-x)) - f(x)}{t}.
   $$
1. Taking the limit as $t \to 0^+$, we obtain:

   $$
   f(y) \geq f(x) + f'(x)(y-x).
   $$

For the converse, assume that $\dom f$ is convex and

$$
f(y) \geq f(x) + f'(x)(y - x)
$$
holds true for all $x, y \in \dom f$.

1. Recall that in $\RR$ the only convex sets are 
   intervals. Thus, $\dom f$ is an open interval.
1. Choose any $x, y \in \dom f$ such that $x \neq y$.
1. Choose $t \in [0,1]$.
1. Let $z = t x + (1-t)y$.
1. By hypothesis, we have:
   
   $$
   f(x) \geq f(z) + f'(z) (x - z)
   $$
   and

   $$
   f(y) \geq f(z) + f'(z) (y - z).
   $$
1. Multiplying the first inequality with $t$ and second
   with $(1-t)$ and adding them yields:
   
   $$
   t f(x) + (1-t) f(y) \geq f(z) = f(tx + (1-t)y).
   $$
1. Thus, $f$ is convex.


We now prove for the general case with $f : \RR^n \to \RR$.
Recall from {prf:ref}`res-cvxf-convx-on-lines`
that for any $\bx, \by \in \dom f$ 
the restriction of $f$ on the line passing through $\bx$ and $\by$
is given by:

$$
g(t) = f(t\by + (1-t) \bx) = f(\bx + t(\by - \bx)).
$$

Note that, by chain rule ({prf:ref}`ex-f-rest-line-chain-rule`):

$$
g'(t) = \nabla f(t\by + (1-t) \bx)^T (\by - \bx)
$$

Assume $f$ is convex.
1. Let $\bx, \by \in \dom f$ such that $\bx \neq \by$.
1. Let $g$ be the restriction of $f$ on the line passing through
   $\bx, \by$ as described above.
1. Due to {prf:ref}`res-cvxf-convx-on-lines`, $g$ is convex.
1. By the argument for real functions above:

   $$
   g(t') \geq g(t) + g'(t)(t' - t)
   $$
   holds true for all $t, t' \in \dom g$.
1. In particular, with $t'=1$ and $t=0$, we have:

   $$
   g(1) \geq g(0) + g'(0).
   $$
1. But $g'(0) = \nabla f(\bx)^T (\by - \bx)$.
1. Also, $g(1) = f(\by)$ and $g(0) = f(\bx)$.
1. Thus, we get:

   $$
   f(\by) \geq f(\bx) + \nabla f(\bx)^T (\by - \bx)
   $$
   as desired.


For the converse, assume that this inequality holds
for all $\bx, \by \in \dom f$ and $\dom f$ is convex.

1. Pick some $\bx, \by \in \dom f$ with $\bx \neq \by$.
1. Let $g$ be the restriction of $f$ on the line passing through
   $\bx, \by$ as described above.
1. Pick $t_1, t_2 \in \dom g$.
1. Then, $\bz_1 = t_1\by + (1-t_1) \bx$ and 
   $\bz_2 = t_2\by + (1-t_2) \bx$
   are in $\dom f$.
1. Consider $g(t_1) = f(t_1\by + (1-t_1) \bx) = f(\bz_1)$
   and $g(t_2) = f(t_2\by + (1-2_1) \bx) = f(\bz_2)$.
1. Note that $g'(t_2) =  \nabla f(t_2\by + (1-t_2) \bx)^T (\by - \bx) = \nabla f(\bz_2)^T (\by - \bx)$.
1. By hypothesis, we have:

   $$
   f(\bz_1) \geq f(\bz_2) + \nabla f(\bz_2)^T (\bz_1 - \bz_2).
   $$
1. But $\bz_1  - \bz_2 = (t_1 - t_2) (\by - \bx)$.
1. Thus, we get:

   $$
   g'(t_1) \geq g'(t_2) + g'(t_2)(t_1 - t_2).
   $$
1. This holds for every $t_1, t_2 \in \dom g$.
1. But then, $g$ is convex by previous argument for
   real functions.
1. Since this is valid for every restriction of $f$ 
   to a line passing through its domain, hence
   by {prf:ref}`res-cvxf-convx-on-lines` $f$ is convex.
```


## Second Order Conditions

For functions which are twice differentiable,
convexity can be expressed in terms of the positive-semidefiniteness of
their Hessian matrices.

We start with a result on convexity of real functions on open intervals.

```{prf:theorem} Convexity characterization for twice differentiable real functions on open intervals
:label: res-cvxf-2nd-derivative-convexity-interval

Let $f : \RR \to \RR$ be twice continuously differentiable on an open interval
$(\alpha, \beta)$;
i.e., second derivative $f''$ exists and is continuous
at every point the open interval $(\alpha, \beta)$.

Then, $f$ is convex if and only if
its second derivative $f''$ is non-negative
for every $x \in (\alpha, \beta)$:

$$
f''(x) \geq 0 \quad \Forall x \in (\alpha, \beta).
$$ 
```

```{prf:proof}
Assume that $f''$ is nonnegative on $(\alpha, \beta)$.

1. Then, $f'$ is nondecreasing on $(\alpha, \beta)$.
1. For any $x, y \in (\alpha, \beta)$ with $x < y$ 
   and $r \in (0,1)$,
   let $z = (1-r)x  + r y$.
1. We have $z \in (x,y)$; i.e. $x < z < y$. Consequently,

   $$
   & f(z) - f(x) = \int_x^z f'(t) dt \leq f'(z) (z - x);\\
   &f(y) - f(z) = \int_z^y f'(t) dt \geq f'(z) (y - z).
   $$
1. Since $z-x = r(y - x)$ and $y -z = (1-r)(y - x)$, we have

   $$
   f(z) \leq f(x) + r f'(z) (y -x);\\
   f(z) \leq f(y) - (1-r) f'(z) (y -x ).
   $$
   We wish to eliminate $f'(z)$ from these inequalities.
1. Multiplying the two inequalities by $(1-r)$ and $r$ respectively,
   and adding them together, we obtain:

   $$
   (1-r)f(z) + r f(z) \leq (1-r)f(x) + r f(y).
   $$
1. But $(1-r)f(z) + r f(z) = f(z) = f((1-r)x + r y)$.
1. Thus, $f((1-r)x + r y) \leq (1-r)f(x) + r f(y)$.
1. This inequality is valid for the case where $x > y$ also.
1. Thus, $f$ is convex over $(\alpha, \beta)$.


For the converse, assume that $f''$ is not non-negative on $(\alpha, \beta)$.
1. Then, since $f''$ is continuous in $(\alpha, \beta)$, 
   hence $f''$ is negative in some subinterval
   $(\alpha', \beta')$.
1. Choose $x, y$ such that $\alpha' < x < y < \beta'$. Choose some $r \in (0,1)$.
1. Following an argument parallel to above, we have

   $$
   f((1-r)x  + r y) > (1-r) f(x) + r f(y).
   $$
1. Thus, there exist $x, y \in (\alpha, \beta)$ where the inequality 
   {eq}`eq-convexity-inequality` is not valid.
1. Consequently, $f$ is non-convex.
```

We continue further with 
real valued functions over $\RR^n$ 
which are twice differentiable.


```{prf:theorem} Second order characterization of convexity in Euclidean spaces
:label: res-cvxf-hessian-convexity-relation

Let $f : \RR^n \to \RR$ be twice continuously differentiable;
i.e., its {prf:ref}`Hessian <def-mvp-hessian>`
or second derivative $\nabla^2 f$ exists 
at every point in $\dom f$ which is open.

Then, $f$ is convex if and only if
$\dom f$ is convex and its Hessian is positive semidefinite
for every $\bx \in \dom f$:

$$
\nabla^2 f(\bx) \succeq \ZERO \quad \Forall \bx \in \dom f.
$$ 
```

```{prf:proof}
The convexity of $f$ on its domain $C = \dom f$ is equivalent
to the convexity of the restriction of $f$ to each line segment
in $C$ due to {prf:ref}`res-cvxf-convx-on-lines`.

We first note that if $f$ is convex then $C$ is convex
and if $C$ is not convex, then $f$ is not convex. So, 
for the rest of the argument, we shall assume that $C$ is convex.

Consequently, for any $\by \in C$ and a nonzero $\bz \in \RR^n$
the intersection of the line $\{ \bx = \by + t \bz \ST t \in \RR\}$
and $C$ is an open line segment as $C$ is open and convex.

1. Let $\by \in C$.
1. Let $\bz \in \RR^n$ be an arbitrary (nonzero) direction.
1. Let $L = \{ \bx = \by + t \bz \ST t \in \RR\}$ be a line passing
   through $\by$ in the direction $\bz$. 
1. Consider the open real interval $S = \{t \ST \by + t \bz \in C\}$.
   Since $L \cap C$ is an open line segment in $\RR^n$, hence
   $S$ is indeed an open interval in $\RR$.
1. Consider the parameterized restriction of $f$ on the open interval $S$ as:

   $$
   g(t) = f(\by + t \bz), \Forall t \in S.
   $$
1. A simple calculation shows that

   $$
   g''(t) = \langle \bz, \nabla^2 f(\bx) \bz \rangle
   $$
   where $\bx = \by + t \bz$.
1. By {prf:ref}`res-cvxf-2nd-derivative-convexity-interval`,
   $g$ is convex for each $\by \in C$ and nonzero $\bz \in \RR^n$ if and only if
   $\langle \bz, \nabla^2 f(\bx) \bz \rangle \geq 0$ for every $\bz \in \RR^n$
   and $\bx \in C$.
1. Thus, $f$ is convex if and only if 
   $\nabla^2 f(\bx) \succeq \ZERO \quad \Forall \bx \in C$.
```

For real functions, the Hessian is simply the
second derivative $f''$.




```{prf:corollary} Second order characterization of concavity
:label: res-cvxf-hessian-concavity-relation

Let $f : \RR^n \to \RR$ be twice continuously differentiable;
i.e., its Hessian
or second derivative $\nabla^2 f$ exists 
at every point in $\dom f$ which is open.

Then, $f$ is concave if and only if
$\dom f$ is convex and its Hessian is negative semidefinite
for every $\bx \in \dom f$:

$$
\nabla^2 f(\bx) \preceq \ZERO \quad \Forall \bx \in \dom f.
$$ 
```


```{prf:example} Convexity of a quadratic function
:label: ex-cvxf-quadratic-func-convexity

Let $\bP \in \SS^n$ be a symmetric matrix. 
Let $\bq \in \RR^n$ and $r \in \RR$. 
Consider the quadratic functional $f: \RR^n \to \RR$ given as:

$$
f(\bx) = \frac{1}{2} \bx^T \bP \bx + \bq^T \bx + r.
$$

As shown in {prf:ref}`ex-mvc-hessian-quadratic-form`, 
the Hessian of $f$ is:

$$
\nabla^2 f (\bx) = \bP \quad \Forall \bx \in \RR^n.
$$
Thus, $f$ is convex if and only if $\bP \succeq \ZERO$ 
(i.e., it is positive semidefinite).

In fact $f$ is strictly convex if and only if $P \succ \ZERO$.
```

```{prf:example} Identity is convex and concave
:label: ex-cvxf-real-identity

Let $f : \RR \to \RR$ be:

$$
f(x) = x.
$$

We have $f'(x) = 1$ and $f''(x) = 0$.

$f$ is both convex and concave. 
```

```{prf:example} Exponential is convex
:label: ex-cvxf-real-exponential

Let $f : \RR \to \RR$ be:

$$
f(x) = e^{ax}
$$
with $\dom f = \RR$.

We have $f'(x) = a e^{ax}$ and $f''(x) = a^2 e^{ax}$. 

For any $a,x \in \RR$, $a^2 e^{ax} > 0$. 
Thus, $f$ is strictly convex.
```



```{prf:example} Powers
:label: ex-cvxf-real-power-x-a


Let $f : \RR \to \RR$ be:

$$
f(x) = x^a
$$
with $\dom f = \RR_{++}$.

Now, $f'(x) = a x^{a-1}$ and $f''(x) = a (a - 1) x^{a-2}$.

1. We have $x > 0$.
1. For $a \geq 1$, $f''(x) \geq 0$. 
   $f$ is convex for $a \geq 1$.
1. For $a \leq 0$, $a (a -1) \geq 0$. 
   Thus, $f''(x) \geq 0$. $f$ is convex for $a \leq 0$.
1. For $0 \leq a \leq 1$, $a (a-1) \leq 0$. Thus, $f''(x) \leq 0$. 
   $f$ is concave on $0 \leq a \leq 1$.
```




```{prf:example} Reciprocal powers
:label: ex-cvxf-real-reciprocal-power-x-r

Let $f : \RR \to \RR$ be:

$$
f(x) = \frac{1}{x^r} = x^{-r}.
$$
with $\dom f = \RR_{++}$.

Now, $f'(x) = (-r) x^{-r-1}$ and $f''(x) = (-r)(-r - 1) x^{-r-2} = r(r+1) x^{-(r+2)}$.

1. We have $x > 0$.
1. For $r \geq 0$, $f''(x) \geq 0$. 
   $f$ is convex for $r \geq 0$.
```


```{prf:example} Logarithm is concave
:label: ex-cvxf-real-logarithm

Let $f : \RR \to \RR$ be:

$$
f(x) = \ln x.
$$
with $\dom f = \RR_{++}$.

Now, $f'(x) = \frac{1}{x}$ and $f''(x) = \frac{-1}{x^2}$.

1. $f''(x) < 0$ for all $x > 0$.
1. Thus, $f$ is concave for all $x > 0$.
```


```{prf:example} Negative entropy is convex
:label: ex-cvxf-real-negative-entropy

Let $f : \RR \to \RR$ be:

$$
f(x) = x \ln x.
$$
with $\dom f = \RR_{++}$.

Now, $f'(x) = \ln x + 1$ and $f''(x) = \frac{1}{x}$.

1. $f''(x) > 0$ for all $x > 0$.
1. Thus, $f$ is convex for all $x > 0$.
```

```{prf:example} Quadratic over linear form is convex
:label: ex-cvxf-r-r-quad-lin

Let $f : \RR \times \RR \to \RR$ be given by:

$$
f(x, y) = \frac{x^2}{y}
$$
with $\dom f = \{ (x, y) \ST y > 0\}$.

From {prf:ref}`ex-mvc-derivatives-quad-lin-func`, 
the Hessian is:


$$
\nabla^2 f(x, y) = 
\frac{2}{y^3} \begin{bmatrix}
y^2 & - x y\\
- x y & x^2
\end{bmatrix}
= \frac{2}{y^3} 
\begin{bmatrix} y\\ - x \end{bmatrix}
\begin{bmatrix} y\\ - x \end{bmatrix}^T .
$$

Recall that for any $\bx \in \RR^n$, the matrix $\bx \bx^T$
is positive semi-definite. 
Hence,

$$
\begin{bmatrix} y\\ - x \end{bmatrix}
\begin{bmatrix} y\\ - x \end{bmatrix}^T
$$
is positive semi-definite.

For $y > 0$, $\frac{2}{y^3} > 0$. Combining:

$$
\nabla^2 f(x, y) \succeq \ZERO.
$$

Thus, $f$ is convex.
```


```{prf:example} Log sum exponential is convex
:label: ex-cvxf-log-sum-exp

Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) = \ln \left ( \sum_{i=1}^n e^{x_i} \right )
$$
with $\dom f = \RR^n$.

From {prf:ref}`ex-mvc-hessian-log-sum-exp`, we have

$$
\nabla^2 f(\bx) = \frac{1}{(\bone^T \bz)^2} \left ((\bone^T \bz) \Diag (\bz) - \bz \bz^T \right )
$$

where 

$$
\bz = \begin{bmatrix}
e^{x_1} \\ 
\vdots \\
e^{x_n}
\end{bmatrix}.
$$

To show that $\nabla^2 f(\bx)$ is p.s.d., it suffices to
show that $(\bone^T \bz) \Diag (\bz) - \bz \bz^T$ is p.s.d..

Now for any $\bv \in \RR^n$. 

$$
&\bv^T \left ( (\bone^T \bz) \Diag (\bz) - \bz \bz^T \right ) \bv\\
&= (\bone^T \bz) (\bv^T \Diag (\bz) \bv) - \bv^T  \bz \bz^T \bv \\
&= (\bone^T \bz) (\bv^T \Diag (\bz) \bv) - (\bv^T  \bz)^2 \\
&= \left (\sum_{i=1}^n z_i \right ) 
\left (\sum_{i=1}^n v_i^2 z_i \right)
- \left (\sum_{i=1}^n v_i z_i \right )^2.
$$

If we define vectors $\ba$ and $\bb$ with
$a_i  = v_i \sqrt{z_i}$ and $b_i = \sqrt{z_i}$,
then by 
{prf:ref}`Cauchy-Schwartz inequality <res-la-ip-cauchy-chwartz-inequality>`
, we have:

$$
(\ba^T \ba)(\bb^T \bb) \geq (\ba^T \bb)^2
\iff (\ba^T \ba)(\bb^T \bb) - (\ba^T \bb)^2 \geq 0.
$$

But this is exactly the expression above.
Thus, $\nabla^2 f(\bx) \succeq \ZERO$.

Hence, $f$ is convex.
```


```{prf:example} Log determinant function is concave
:label: ex-cvxf-log-det

Let $f : \SS^n \to \RR$ be:

$$
f(\bX) = \log \det X.
$$
with $\dom f = \SS^n_{++}$ (the set of symmetric positive definite matrices).

Let any line in $\SS^n$ be given by:

$$
\bX = \bZ + t \bV 
$$
where $\bZ, \bV \in \SS^n$.

Consider the restriction of $f$ on a line:

$$
g(t) = \log \det (\bZ + t \bV) 
$$
to the interval of values where $\bZ + t \bV \succ \ZERO$ 
(since $\dom f = \SS^n_{++}$ ).
In other words, 

$$
\dom g = \{t \in \RR \ST \bZ + t \bV \succ \ZERO \}.
$$

Without any loss of generality, we can assume that $t=0 \in \dom g$;
i.e. $\bZ \succ \ZERO$.

Recall that:
1. $\det (AB) = \det(A) \det(B)$ for square matrices.
1. $ \det (A) = \prod_{i=1}^n \lambda_i $ for symmetric matrices with $\lambda_i$ 
   being their eigen values.
1. If $\lambda_i$ are eigen values of $A$, then the eigen values of $I + t A$ are
   $1 + t \lambda_i$.


Now

$$
g(t) &= \log \det (\bZ + t \bV) \\
&= \log \det (\bZ^{\frac{1}{2}} (\bZ^{\frac{1}{2}} + t \bZ^{-\frac{1}{2}} \bV) )\\
&= \log \det (\bZ^{\frac{1}{2}} (I + t \bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}) \bZ^{\frac{1}{2}})\\
&= \log \det(\bZ^{\frac{1}{2}}) + \log \det (I + t \bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}})
  + \log \det(\bZ^{\frac{1}{2}})\\
&= \log \det(\bZ) + \log \det (I + t \bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}).
$$

1. Let $\lambda_i$ be the eigen values of $\bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}$. 
1. Then, $1 + t \lambda_i$ are eigen values of $I + t\bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}$.
1. Thus, $\log \det (I + t\bZ^{-\frac{1}{2}} \bV \bZ^{-\frac{1}{2}}) = \sum_{i=1}^n \log \det (1 + t\lambda_i)$.


Thus,

$$
g(t) = \sum_{i=1}^n \log \det (1 + t\lambda_i) + \log \det(\bZ).
$$
Note that $\log \det(\bZ)$ doesn't depend on $t$.
Similarly, $\lambda_i$ only depend on $\bZ$ and $\bV$, hence they don't depend on $t$.

Differentiating $g$ w.r.t. $t$, we get:

$$
g'(t) = \sum_{i=1}^n \frac{\lambda_i}{1 + t \lambda_i}.
$$

Differentiating again, we get:

$$
g''(t) = -\sum_{i=1}^n \frac{\lambda_i^2}{(1 + t \lambda_i)^2}.
$$

Since $g''(t) \leq 0$, hence $f$ is concave.
```
