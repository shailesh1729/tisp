(sec:conjugate-functions)=
# Conjugate Functions

```{div}

Throughout this section, we assume that $\VV, \WW$ are 
real vector spaces. Wherever necessary, 
they are equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \|$
or an {prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle$. 
They are also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$
as needed.
$\VV^*$ denotes the dual vector space (to $\VV$).
```

## Definition and Properties

```{prf:definition} Conjugate function
:label: def-cvxf-conjugate-function

Let $f : \VV \to \ERL$ be an extended real valued function. 
Its *conjugate function* $f^*: \VV^* \to \ERL$ is given by

$$
f^*(\by) = \underset{\bx \in \VV}{\sup} \{ \langle \bx, \by \rangle - f(\bx)\}
\Forall \by \in \VV^*.
$$ 
```

Note that the conjugate function is a mapping from the *dual* vector space
to extended real line.

Recall from {prf:ref}`def-cvxf-support-function` that
the support function of a set $C$ is given by

$$
\sigma_C (\bx) =  \sup_{\bz \in C} \langle \bz, \bx \rangle.
$$

```{prf:theorem} Conjugate of an indicator function
:label: res-cvxf-conjugate-indicator-func

Let $C \subseteq \VV$ be a nonempty set. 
Let $\delta_C : \VV \to \RERL$ be the indicator function for the set $C$.
Then,

$$
\delta_C^*(\by) = \sigma_C (\by) = \underset{\bx \in C}{\sup} \langle \bx, \by \rangle. 
$$

In other words, the conjugate of the indicator function of a set
is the support function of the same set.
```

```{prf:proof}

Let $\by \in \VV*$ be arbitrary.

1. At any $\bx \in C$, we have
   
   $$
   \langle \bx, \by \rangle - \delta_C(\bx) = \langle \bx, \by \rangle. 
   $$
1. At any $\bx \notin C$, we have

   $$
   \langle \bx, \by \rangle - \delta_C(\bx) = -\infty. 
   $$
1. Since $C$ is nonempty, hence

   $$
   \underset{\bx \in \VV}{\sup} \{ \langle \bx, \by \rangle - f(\bx)\}
   = \underset{\bx \in C}{\sup} \langle \bx, \by \rangle.
   $$
   The result follows.
```



```{prf:theorem} Convexity and closedness
:label: res-cvxf-conjugate-convex-closed

Let $f : \VV \to \RERL$ be an extended real valued function. 
Then, the conjugate function $f^*$ is closed and convex.    
```

```{prf:proof}
We note that for a fixed $\bx$, the function

$$
g_x(\by) =  \langle \bx, \by \rangle - f(\bx)
$$
is an affine function. 

1. Due to {prf:ref}`res-la-affine-finite-closed-func`,
   affine functions are closed.
1. Due to {prf:ref}`res-cvxf-affine-functional-convex`,
   affine functions are convex.
1. Thus, $g_x$ is indeed convex and closed for every $\bx$.
1. Thus, $f$ is a pointwise supremum of convex and closed functions.
1. By {prf:ref}`res-ms-ptws-sup-closed-functions-closed`, $f$ is closed.
1. By {prf:ref}`res-cvx-ptws-supremum`, $f$ is convex.
1. Thus, $f$ is closed and convex.
```

The beauty of this result is the fact that
The conjugate function is always closed and
convex even if the original function is not
convex or not closed.


```{rubric} Proper functions
```
```{div}
Let $f : \VV \to \RERL$ be a proper function. 

Fenchel's inequality holds for any $\bx \in \VV$ and $\by \in \VV^*$:

$$
f(x) + f^*(y) \geq \langle y, x \rangle.
$$
```

```{rubric} Proper convex functions
```
```{div}
Let $f : \VV \to \RERL$ be a proper convex function. 
Then, the conjugate function $f^*$ is proper.    
```


## Biconjugate

The conjugate of the conjugate is called the *biconjugate*. 

```{div}
Let $f : \VV \to \ERL$ be an extended real valued function. 
Its *biconjugate function* $f^{**}: \VV \to \ERL$ is given by

$$
f^{**} (\bx) = \underset{\by \in \VV^*}{\sup} 
\{ \langle \bx, \by \rangle - f^*(\by)  \}, \quad \bx \in \VV.
$$

The biconjugate is an underestimator of the original function.

$$
f(\bx) \geq f^{**} (\bx) \Forall x \in \VV. 
$$

Let $f : \VV \to \ERL$ be a proper, closed and convex function. 
Then,

$$
f(\bx) = f^{**} (\bx) \Forall x \in \VV. 
$$
```

```{rubric} Indicator and support functions
```

```{div}
For a nonempty, closed and convex set $C \subseteq \VV$, 

$$
\sigma^*_C = \delta_C.
$$

For an arbitrary nonempty set $C \subseteq \VV$, 

$$
\sigma^*_C = \delta_{\closure \ConvexHull C}.
$$
```

```{rubric} Max function
```
```{div}
Let $f : \RR^n \to \RR$ be given by

$$
f(\bx) \triangleq \max \{x_1, x_2, \dots, x_n \}.
$$

We can rewrite it as

$$
f(\bx) = \underset{\by \in \Delta_n}{\sup} \langle \by, \bx \rangle
= \sigma_{\Delta_n} (x)
$$
where $\Delta_n$ is the unit simplex in $\RR^n$.

The conjugate of max function $f$ is 

$$
f^* = \delta_{\Delta_n}.
$$
```

## Conjugate Calculus


```{rubric} Separable functions
```
```{div}
Let $g: \VV_1 \times \VV_2 \times \dots \times \VV_p \to \RERL$ be given by 

$$
g(\bx_1, \bx_2, \dots, \bx_p) = \sum_{i=1}^p f_i (\bx_i)
$$
where $f_i : \VV_i \to \RERL$ are proper functions.
Then: 

$$
g^*(\by_1, \by_2, \dots, \by_p) = 
\sum_{i=1}^p f_i^*(\by_i) \Forall \by_i \in \VV_i^*, 1 \leq i \leq p.
$$
```

```{rubric} Invertible affine transformation
```
```{div}
Let $f : \VV \to \RERL$ be an extended real valued function.
Let $\bAAA : \VV \to \VV$ be an invertible linear transformation.
Let $\ba \in \VV$, $\bb \in \VV^*$ and $c \in \RR$. 
Consider the function $g: \VV \to  \RERL$ given by:

$$
g(\bx) \triangleq f\left (\bAAA (\bx - \ba) \right ) + \langle \bb, \bx \rangle + c
\Forall \bx \in \VV.
$$

Then the convex conjugate of $g$ is given by:

$$
g^*(\by) = f^*\left ((\bAAA^T)^{-1} (\by - \bb) \right ) 
+ \langle \ba, \by \rangle 
- c - \langle \ba, \bb \rangle
\Forall \by \in \VV^*.
$$
```

```{rubric} Scaling
```
```{div}
Let $f : \VV \to \RERL$ be an extended real valued function.
Let $\alpha > 0$.

For $g(\bx) = \alpha f(\bx)$:

$$
g^*(\by) = \alpha f^*\left (\frac{\by}{\alpha} \right ) \Forall \by \in \VV^*.
$$

For $h(\bx) = \alpha f(\frac{\bx}{\alpha})$:

$$
h^*(\by) = \alpha f^*(\by) \Forall \by \in \VV^*.
$$ 
```

## Useful Results

```{rubric} Fenchel's duality theorem
```

```{div}
Let $f,g : \VV \to \RERL$ be proper convex function.
If $\relint \dom f \cap \relint \dom g \neq \EmptySet$, then 

$$
\underset{\bx \in \VV}{\sup} \{f(\bx) + g(\bx) \}
= \underset{\by \in \VV^*}{\sup} \{ - f^*(\by) - g^*(-\by) \}.
$$
The supremum of R.H.S. is attained whenever it is finite.
```

```{rubric} Infimal Convolution
```

```{div}
Recall that the *infimal convolution* of two functions
$f,g : \VV \to \ERL$ is defined as:

$$
(f \square g)(\bx) \triangleq 
\underset{\by \in \VV}{\inf} (f(\bx - \by) + g(\by)). 
$$

For two proper functions 
$h_1, h_2: \VV \to \RERL$, it holds that:

$$
(h_1 \square h_2)^*  = h_1^*  + h_2^*.
$$

Let $h_1 : \VV \to \RERL$ be a proper convex
function and $h_2 : \VV \to \RR$ be a real valued
convex function. Then

$$
(h_1 + h_2)^* = h_1^* \square h_2^*.
$$

Let $h_1 : \VV \to \RERL$ be a proper closed convex
function and $h_2 : \VV \to \RR$ be a real valued
convex function. Then

$$
h_1 + h_2 = (h_1^* \square h_2^*)^*.
$$

Let $h_1 : \VV \to \RERL$ be a proper convex
function and $h_2 : \VV \to \RR$ be a real valued
convex function. Suppose $h_1 \square h_2$ is 
a real valued function. Then


$$
h_1 \square h_2 = (h_1^* + h_2^*)^*.
$$
```

```{rubric} Conjugate subgradient theorem
```

```{div}
Let $f : \VV \to \RERL$ be proper and convex. 
The following claims are equivalent for any $\bx \in \VV$
and $\by \in \VV^*$:

1. $\langle \by, \bx \rangle = f(\bx) + f^*(\by)$.
2. $\by \in \partial f(\bx)$.

If $f$ is closed, then 1 and 2 are equivalent to:

3. $\bx \in \partial f^*(\by)$.
```



## 1-dim Functions


```{rubric} Exponent
```

```{div}
$ f : \RR \to \RR$, $f(x) = e^x$.

$$
f^*(x) = \begin{cases}
y \log y - y & y \geq 0 \\
\infty & \text{ otherwise }
\end{cases}
$$
```

```{rubric} Negative log
```

```{div}
$ f : \RR \to (-\infty,\infty]$ be given by: 

$$
f(x) = \begin{cases}
- \log(x) & x > 0 \\
\infty &  x \leq 0
\end{cases}.
$$

Then, the conjugate is:

$$
f^*(y) = \begin{cases}
-1 - \log (-y) & y < 0 \\
\infty & y \geq 0
\end{cases}.
$$
```

```{rubric} Hinge loss
```

```{div}

Let $f : \RR \to \RR$ be given by:

$$
f(x) = \max \{1 - x, 0 \}
$$

Then, the conjugate is:

$$
f^*(y) = y + \delta_{[-1,0]} (y) \Forall y \in \RR.
$$
```

```{rubric} Power by p
```

```{div}

Let for some $p > 1$, $f : \RR \to \RR$ be given by:

$$
f(x) = \frac{1}{p} | x |^p
$$

Then, the conjugate is:

$$
f^*(y) = \frac{1}{q} | y |^q \Forall y \in \RR
$$

where $q > 1$ satisfying: 

$$
\frac{1}{p} + \frac{1}{q} = 1.
$$
```


```{div}

Let for some $0 < p < 1$, $f : \RR \to \RR$ be given by:

$$
f(x) = \begin{cases}
- \frac{1}{p} x^p &  x \geq 0 \\
\infty & x < 0
\end{cases}.
$$

Then, the conjugate is:

$$
f^*(y) = \begin{cases}
- \frac{(-y)^q}{q}  &  y < 0 \\
\infty & \text{ otherwise }
\end{cases}
$$

where $q < 0$ satisfying: 

$$
\frac{1}{p} + \frac{1}{q} = 1.
$$
```

## n-dim functions



```{rubric} Strictly convex quadratic
```

```{div}
Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) \triangleq \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c 
$$

where $A \in \SS^n_{++}$, $\bb \in \RR^n$ and $c \in \RR$. 

Then, the conjugate is:

$$
f^*(\by) = \frac{1}{2}(\by - \bb)^T \bA^{-1}(\by -\bb) - c.
$$
```


```{rubric} Convex quadratic
```

```{div}
Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) \triangleq \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c 
$$

where $A \in \SS^n_{+}$, $\bb \in \RR^n$ and $c \in \RR$. 

Then, the conjugate is:

$$
f^*(\by) = \begin{cases}
\frac{1}{2}(\by - \bb)^T \bA^{\dag}(\by -\bb) - c & \by \in \bb + \range (\bA)\\
\infty & \text{ otherwise }
\end{cases}.
$$
```

```{rubric} Negative entropy
```

```{div}
Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) \triangleq \begin{cases}
\sum_{i=1}^n x_i \log (x_i) & \bx \succeq \bzero\\
\infty & \text{ otherwise }
\end{cases}.
$$

Then, the conjugate is:

$$
f^*(\by) = \sum_{i=1}^n e^{y_i - 1}.
$$
```

```{rubric} Negative sum of logs
```

```{div}
Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) \triangleq \begin{cases}
- \sum_{i=1}^n \log (x_i) & \bx \succ \bzero\\
\infty & \text{ otherwise }
\end{cases}.
$$

Then, the conjugate is:

$$
f^*(\by) =  \begin{cases}
- n - \sum_{i=1}^n \log(-y_i) & \by \prec \bzero \\
\infty & \text{ otherwise}
\end{cases}.
$$
```


```{rubric} Negative entropy over unit simplex
```

```{div}
Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) \triangleq \begin{cases}
\sum_{i=1}^n x_i \log (x_i) & \bx \in \Delta_n\\
\infty & \text{ otherwise }
\end{cases}.
$$


The conjugate is:

$$
f^*(\by) =  \log \left ( \sum_{j=1}^n e^{y_j}
    \right )
$$
```

```{rubric} Log sum exp
```

```{div}
Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) \triangleq \log \left ( \sum_{j=1}^n e^{x_j}
    \right ).
$$

The conjugate is:

$$
f^*(\by) =  \begin{cases}
\sum_{i=1}^n y_i \log (y_i) & \by \in \Delta_n\\
\infty & \text{ otherwise }
\end{cases}.
$$
```

Log-sum-exp and negative entropy over simplex and conjugate
of each other.



```{rubric} Norm
```

```{div}
Let $f : \VV \to \RR$ be given by

$$
f(\bx) = \| \bx \|
$$

Then, the conjugate $f^* : \VV^* \to \ERL$ for any $\by \in \VV^*$
is given by:

$$
f^*(\by) = \begin{cases}
0 & \| \by \|_* \leq 1 \\
\infty & \text{ otherwise }
\end{cases}
$$

In other words, it is the indicator function for the unit ball
w.r.t. the dual norm $\| \cdot \|_*$.
```

```{rubric} Ball-Pen
```

```{div}
Let $f : \VV \to \RERL$ be given by

$$
f(\bx) \triangleq \begin{cases}
- \sqrt{1 - \| x \|^2} & \| x \| \leq 1\\
\infty & \text{ otherwise }
\end{cases}.
$$

Then, the conjugate $f^* : \VV^* \to \ERL$ for any $\by \in \VV^*$
is given by:

$$
f^*(\by) = \sqrt{\| y \|_*^2 + 1}.
$$

Let $f_{\alpha}$ for some $\alpha > 0$ be defined as

$$
f_{\alpha}(\bx) \triangleq \begin{cases}
- \sqrt{\alpha^2 - \| x \|^2} & \| x \| \leq \alpha\\
\infty & \text{ otherwise }
\end{cases}.
$$

The conjugate:

$$
f_{\alpha}^*(\by) = \alpha \sqrt{\| y \|_*^2 + 1}.
$$


In the reverse direction, let $g_{\alpha} : \VV \to \RR$ 
for some $\alpha > 0$ be given by:

$$
g_{\alpha} (\bx) = \sqrt{\alpha^2 + \| x \|^2}.
$$

Then the conjugate is:

$$
g_{\alpha}^*(\by) = \begin{cases}
-\alpha \sqrt{1 - \| y \|_*^2} & \| y \|_* \leq 1\\
\infty & \text{ otherwise }
\end{cases}.
$$
```


```{rubric} Squared Norm
```

```{div}
Let $f : \VV \to \RR$ be given by

$$
f(\bx) = \frac{1}{2}\| \bx \|^2
$$

Then, the conjugate $f^* : \VV^* \to \ERL$ for any $\by \in \VV^*$
is given by:

$$
f^*(\by) = \frac{1}{2} \| \by \|_*^2.
$$
```
