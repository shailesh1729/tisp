(sec:subgradients:summary)=
# Chapter Summary

## Subgradients

```{div}

Let $\EE$ be a vector space equipped with the standard inner product.

Let $f : \EE \to (-\infty, \infty]$ be a proper function.
Let $\bx \in \dom f$. Let $\by \in \EE$. Let $\bg \in \EE^*$
be a subgradient of $f$ at $x$. 

Subgradient inequality:

$$
f(\by) \geq f(\bx) + \langle \bg, \by - \bx \rangle \Forall \by \in \EE.
$$
```

```{div}
Alternative form:

$$
f(\by) \geq f(\bx) + \langle \bg, \by - \bx \rangle \Forall \by \in \dom f.
$$
```

```{div}
Subdifferential set:

$$
\partial f(\bx) \triangleq 
\{ \bg \in \EE^* \ST f (\by) \geq f(\bx) + \langle \bg, \by - \bx \rangle 
  \Forall \by \in \EE \}.
$$
```

* The subdifferential set $\partial f (\bx)$ is closed and convex for any $\bx \in \EE$.
* $\partial f (\bx)$ may be empty at some $\bx \in \EE$.
* $f$ is called subdifferentiable at $\bx \in \EE$
  if $\partial f (\bx) \neq \EmptySet$.
* The set of points at which $f$ is subdifferentiable is denoted by

  $$
  \dom \partial f = \{ \bx  \in \EE \ST \partial f (\bx) \neq \EmptySet \}.
  $$
* If $\dom f$ is convex and $\partial f(\bx)$ is nonempty at every 
  $\bx \in \dom f$, then $f$ is convex.

Multiplication by a positive scalar: Let $\bx \in \dom f$.
For any $\alpha > 0$, 

$$
\partial (\alpha f)(\bx) = \alpha \partial f(\bx).
$$


### Proper Convex Functions

Let $f : \EE \to (-\infty, \infty]$ be a proper convex function.

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
* If $\Dim(\dom f) < \Dim(\EE)$ and $\partial f(\bx)$ is nonempty for some
  $\bx \in \dom f$, then $\partial f(\bx)$ is unbounded. 

### Convex Functions

Let $f : \EE \to \RR$ be convex. 

* $f$ is subdifferentiable over $\EE$.


## Directional Derivatives


```{div}
Let $f : \EE \to (-\infty, \infty]$ be a proper function.
Let $\bx \in \interior \dom f$. 
The *directional derivative* at $\bx$ in the direction $\bd \in \EE$ is defined by 

$$
f'(\bx;\bd) \triangleq \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha \bd) - f(\bx)}{\alpha}.
$$
```
The directional derivative is a scalar quantity ($\in \RR$).

### Proper Convex Functions

Let $f : \EE \to (-\infty, \infty]$ be a proper convex function.
Let $\bx \in \interior \dom f$. 

* For any $\bd \in \EE$, the directional derivative $f'(\bx; \bd)$ exists.
* $f(\by) \geq f(\bx) + f'(\bx; \by -\bx) \Forall \by \in \dom f$.
* Max formula: For any $\bd \in \EE$, 

  $$
  f'(\bx;\bd) = \max \{ \langle \bg, \bd \rangle \ST \bg \in \partial f(\bx) \}.
  $$

* Max formula alternative formulation using the support function notation:

  $$
  f'(\bx;\bd) = \sigma_{\partial f(\bx)}(\bd).
  $$

For a proper convex function, at a point $\bx \in \interior \dom f$, we define 
a mapping $g : \EE \to \RR$ given by $ g(\bd) \triangleq f'(\bx;\bd)$.
In other words, $g$ performs $\bd \mapsto f'(\bx;\bd)$ mapping at $\bx$.

* $g$ is convex.
* $g$ is homogeneous. i.e. $g(\lambda \bd) = \lambda g(\bd)$ for some $\lambda \geq 0$.



## Differentiability

```{div}
Let $f : \EE \to (-\infty, \infty]$ be a proper function.
Let $\bx \in \interior \dom f$. 
$f$ is said to be *differentiable* at $\bx \in \interior \dom f$
if there exists $\bg \in \EE^*$ such that:

$$
\underset{\bh \to 0}{\lim} 
\frac{f(\bx + \bh) - f(\bx) - \langle \bg, \bh \rangle}{\| \bh \|} = 0.
$$
The unique vector $\bg$ satisfying this condition is called
the *gradient* of $f$ at $\bx$ and is denoted by $\nabla f(\bx)$.
```


```{div}
Let $f : \EE \to (-\infty, \infty]$ be a proper function.
Let $\bx \in \interior \dom f$. Assume $f$ to be 
differentiable at $\bx$. 

* Directional derivative in terms of gradient: 

  $$
  f'(\bx; \bd) = \langle \nabla f(\bx) , \bd \rangle \Forall \bd \in \EE.
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
  This holds if $\EE$ is endowed with the standard dot product 
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
Let $f : \EE \to (-\infty, \infty]$ be a proper convex function.
Let $\bx \in \interior \dom f$. 
Assume $f$ to be differentiable at $\bx$. 

* The subdifferential set at $\bx$ is a singleton.

  $$
  \partial f(\bx) = \{\nabla f(\bx) \}.
  $$


Let $f : \EE \to (-\infty, \infty]$ be a proper convex function.
Let $x \in \interior \dom f$. 

* If $f$ has a unique subdifferential at $\bx$, then it is 
  differentiable at $\bx$ with:

  $$
  \partial f(\bx) = \{\nabla f(\bx) \}.
  $$
```


## Subdifferential Calculus

### Sums of Functions

Let $f_1, f_2 : \EE \to (-\infty, \infty]$ be proper convex functions.

Let $x \in \dom f_1 \cap \dom f_2$.
Let $y \in \interior \dom f_1 \cap \interior \dom f_2$.

* $\partial f_1(x) + \partial f_2(x) \subseteq \partial (f_1 + f_2)(x)$.
* $\partial(f_1 + f_2)(y) = \partial f_1 (y) + \partial f_2(y)$.


Let $f_1, f_2, \dots, f_m : \EE \to (-\infty, \infty]$ be proper convex functions.

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
entire $\EE$.

If $\bigcap_{i=1}^m \relint \dom f_i \neq \EmptySet$, then for any $x \in \EE$,
the strong sum rule holds:

$$
\sum_{i=1}^m \partial f_i (x) = \partial \left ( \sum_{i=1}^m f_i \right )(x).
$$

### Affine Transformations

Let $f: \EE \to (-\infty, \infty]$ be a proper convex function.
Let $\AAA : \VV \to \EE$ be a linear transformation.
Let 

$$
h (x) = f (\AAA(x) + b)\; \text{ with } b \in \EE.
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
Let $f : \EE \to \RR$ be convex and let $g : \RR \to \RR$ be a 
nondecreasing convex function. Let $x \in \EE$ and assume that
$g$ is differentiable at $f(x)$. Let $h = g \circ f$. Then

$$
\partial h (x) = g'(f(x)) \partial f(x).
$$
```

## Maximum over a Set of Functions

```{rubric} Proper functions
```

```{div}
Let $f_1, f_2, \dots, f_m : \EE \to (-\infty,\infty]$ be a set of
proper functions. Let

$$
f(x) = \max \{ f_1(x), f_2(x), \dots, f_m(x)\}.
$$

Let $x \in \bigcap_{i=1}^m \interior \dom f_i$ be a point common to the
domains of all the functions.
Let $d \in \EE$ be a direction. 

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


Let $f_1, f_2, \dots, f_m : \EE \to (-\infty,\infty]$ be a set of
proper convex functions. Let

$$
f(x) = \max \{ f_1(x), f_2(x), \dots, f_m(x)\}.
$$

Let $x \in \bigcap_{i=1}^m \interior \dom f_i$ be a point common to the
domains of all the functions.
Let $d \in \EE$ be a direction. 
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
convex functions $f_i : \EE \to (-\infty, \infty]$ where $i \in I$.

Then for any  $x \in \dom f$, 

$$
\text{conv } \left ( \bigcup_{i \in I(x)} \partial f_i(x)
  \right ) \subseteq \partial f(x)
$$

where $I (x) = \{i \in I \ST f(x) = f_i (x) \}$.
```

## Norm Functions

```{div}
Subdifferential of a norm $\| \cdot \|: \EE \to \RR$ at $x = \ZeroVec$:

$$
\partial f(\ZeroVec) = B_{\| \cdot \|_*} [\ZeroVec, 1] = \{ g \in \EE^* \ST \|g\|_* \leq 1 \}. 
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

```{div}
Normal cone of a set $S \subset \EE$ at a point $x \in S$:

$$
N_s(x) \triangleq \{ y \in \EE^* \ST \langle y, z - x \rangle \leq 0 \Forall z \in S\}.
$$
```

```{div}
Subdifferential of indicator function for a nonempty set $S \subset \EE$  at a point $x \in S$:

$$
\partial \delta_S (x) = N_S (x) \Forall x \in S.
$$
```

```{div}
Subdifferential of the indicator function of the unit ball 
(with center at origin) $B[\ZeroVec, 1]$:

$$
S = B[\ZeroVec] = \{ x \in \EE \ST \| x \|  \leq 1\}.
$$

$$
\partial \delta_{B[\ZeroVec, 1]} (x) = \begin{cases} 
 \{ y \in \EE^* \ST \| y \|_* \leq \langle y, x \rangle \} & \text{for} & \| x \| \leq 1 \\
\EmptySet & \text{for} & \| x \| > 1
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
Maximum eigen value function $f : \SS^n \to \RR$:

$$
f(X) \triangleq \lambda_{\max} (X).
$$

$$
v v^T \in \partial f (X)
$$
where $v$ is a normalized eigen-vector of $X$ associated with its maximum eigen value.
```



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


Let $C \subseteq \EE$ be a nonempty closed and convex set.
The *orthogonal projection* mapping under a norm $\| \cdot \|$
is defined by:

$$
P_C(x) \triangleq \underset{y \in C}{\argmin} \| y - x \| \Forall x \in \EE. 
$$
The mapping $P_C$ is well defined (exists and unique) when
the underlying set $C$ is nonempty, closed and convex.


The distance of a point $x \in \EE$ to $C$ is defined as

$$
d_C(x) = \| x - P_C(x) \|.
$$


Let $\phi_C : \EE \to \RR$ be defined as:

$$
\phi_C(x) \triangleq \frac{1}{2} d_C^2(x) 
= \frac{1}{2}\| x - P_C(x) \|^2.
$$


The gradient of $\phi_C(x)$ is given by:

$$
\nabla \phi_C(x) = x - P_C(x)  \Forall x \in \EE.
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
Let $\EE = \RR^{m \times n}$. Let the standard
inner product for $x, y, \in \EE$ be 
$\langle x, y \rangle = \Trace(x^T y)$. 

Let $f : \EE \to (-\infty, \infty]$ be a proper function.
Let $x \in \interior \dom f$.

The gradient at $x$, if it exists, is given by:

$$
\nabla f(x) = D_f(x) \triangleq \left ( \frac{\partial f}{\partial x_{ij}} (x) \right)_{i,j}.
$$ 
```

Let $H$ be a positive definite matrix and define an inner 
product for $\EE$ as:

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