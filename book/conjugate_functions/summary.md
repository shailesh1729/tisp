(sec:conjugate-functions:summary)=
# Chapter Summary

## Conjugate Function

```{div}
Let $f : \EE \to \ERL$ be an extended real valued function. 
Its *conjugate function* $f^*: \EE^* \to \ERL$ is given by

$$
f^*(\by) = \underset{\bx \in \EE}{\sup} \{ \langle \by, \bx \rangle - f(\bx)\}, 
\quad \by \in \EE^*.
$$ 

Note that the conjugate function is a mapping from the *dual* vector space
to extended real line.
```

```{rubric} Indicator functions
```
The conjugate of the indicator function is the support function of the same set.

```{div}
Let $C \subseteq \EE$. Let $\delta_C$ be the indicator function for $C$.

$$
f^*(\by) = \sigma_C (\by) = \underset{\bx \in C}{\sup} \langle \by, \bx \rangle. 
$$

$$
\delta^*_C  = \sigma_C.
$$
```

```{rubric} Extended real valued functions
```
```{div}
Let $f : \EE \to (-\infty, \infty]$ be an extended real valued function. 
Then, the conjugate function $f^*$ is closed and convex.    
```


```{rubric} Proper functions
```
```{div}
Let $f : \EE \to (-\infty, \infty]$ be a proper function. 

Fenchel's inequality holds for any $\bx \in \EE$ and $\by \in \EE^*$:

$$
f(x) + f^*(y) \geq \langle y, x \rangle.
$$
```

```{rubric} Proper convex functions
```
```{div}
Let $f : \EE \to (-\infty, \infty]$ be a proper convex function. 
Then, the conjugate function $f^*$ is proper.    
```


## Biconjugate

The conjugate of the conjugate is called the *biconjugate*. 

```{div}
Let $f : \EE \to [-\infty, \infty]$ be an extended real valued function. 
Its *biconjugate function* $f^{**}: \EE \to [-\infty, \infty]$ is given by

$$
f^{**} (\bx) = \underset{\by \in \EE^*}{\sup} 
\{ \langle \bx, \by \rangle - f^*(\by)  \}, \quad \bx \in \EE.
$$

The biconjugate is an underestimator of the original function.

$$
f(\bx) \geq f^{**} (\bx) \Forall x \in \EE. 
$$

Let $f : \EE \to [-\infty, \infty]$ be a proper, closed and convex function. 
Then,

$$
f(\bx) = f^{**} (\bx) \Forall x \in \EE. 
$$
```

```{rubric} Indicator and support functions
```

```{div}
For a nonempty, closed and convex set $C \subseteq \EE$, 

$$
\sigma^*_C = \delta_C.
$$

For an arbitrary nonempty set $C \subseteq \EE$, 

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
Let $g: \EE_1 \times \EE_2 \times \dots \times \EE_p \to (-\infty, \infty]$ be given by 

$$
g(\bx_1, \bx_2, \dots, \bx_p) = \sum_{i=1}^p f_i (\bx_i)
$$
where $f_i : \EE_i \to (-\infty, \infty]$ are proper functions.
Then: 

$$
g^*(\by_1, \by_2, \dots, \by_p) = 
\sum_{i=1}^p f_i^*(\by_i) \Forall \by_i \in \EE_i^*, 1 \leq i \leq p.
$$
```

```{rubric} Invertible affine transformation
```
```{div}
Let $f : \EE \to (-\infty, \infty]$ be an extended real valued function.
Let $\bAAA : \VV \to \EE$ be an invertible linear transformation.
Let $\ba \in \VV$, $\bb \in \VV^*$ and $c \in \RR$. 
Consider the function $g: \VV \to  (-\infty, \infty]$ given by:

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
Let $f : \EE \to (-\infty, \infty]$ be an extended real valued function.
Let $\alpha > 0$.

For $g(\bx) = \alpha f(\bx)$:

$$
g^*(\by) = \alpha f^*\left (\frac{\by}{\alpha} \right ) \Forall \by \in \EE^*.
$$

For $h(\bx) = \alpha f(\frac{\bx}{\alpha})$:

$$
h^*(\by) = \alpha f^*(\by) \Forall \by \in \EE^*.
$$ 
```

## Useful Results

```{rubric} Fenchel's duality theorem
```

```{div}
Let $f,g : \EE \to (-\infty, \infty]$ be proper convex function.
If $\relint \dom f \cap \relint \dom g \neq \EmptySet$, then 

$$
\underset{\bx \in \EE}{\sup} \{f(\bx) + g(\bx) \}
= \underset{\by \in \EE^*}{\sup} \{ - f^*(\by) - g^*(-\by) \}.
$$
The supremum of R.H.S. is attained whenever it is finite.
```

```{rubric} Infimal Convolution
```

```{div}
Recall that the *infimal convolution* of two functions
$f,g : \EE \to \ERL$ is defined as:

$$
(f \square g)(\bx) \triangleq 
\underset{\by \in \EE}{\inf} (f(\bx - \by) + g(\by)). 
$$

For two proper functions 
$h_1, h_2: \EE \to \RERL$, it holds that:

$$
(h_1 \square h_2)^*  = h_1^*  + h_2^*.
$$

Let $h_1 : \EE \to \RERL$ be a proper convex
function and $h_2 : \EE \to \RR$ be a real valued
convex function. Then

$$
(h_1 + h_2)^* = h_1^* \square h_2^*.
$$

Let $h_1 : \EE \to \RERL$ be a proper closed convex
function and $h_2 : \EE \to \RR$ be a real valued
convex function. Then

$$
h_1 + h_2 = (h_1^* \square h_2^*)^*.
$$

Let $h_1 : \EE \to \RERL$ be a proper convex
function and $h_2 : \EE \to \RR$ be a real valued
convex function. Suppose $h_1 \square h_2$ is 
a real valued function. Then


$$
h_1 \square h_2 = (h_1^* + h_2^*)^*.
$$
```

```{rubric} Conjugate subgradient theorem
```

```{div}
Let $f : \EE \to \RERL$ be proper and convex. 
The following claims are equivalent for any $\bx \in \EE$
and $\by \in \EE^*$:

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
Let $f : \EE \to \RR$ be given by

$$
f(\bx) = \| \bx \|
$$

Then, the conjugate $f^* : \EE^* \to \ERL$ for any $\by \in \EE^*$
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
Let $f : \EE \to (-\infty, \infty]$ be given by

$$
f(\bx) \triangleq \begin{cases}
- \sqrt{1 - \| x \|^2} & \| x \| \leq 1\\
\infty & \text{ otherwise }
\end{cases}.
$$

Then, the conjugate $f^* : \EE^* \to \ERL$ for any $\by \in \EE^*$
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


In the reverse direction, let $g_{\alpha} : \EE \to \RR$ 
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
Let $f : \EE \to \RR$ be given by

$$
f(\bx) = \frac{1}{2}\| \bx \|^2
$$

Then, the conjugate $f^* : \EE^* \to \ERL$ for any $\by \in \EE^*$
is given by:

$$
f^*(\by) = \frac{1}{2} \| \by \|_*^2.
$$
```
