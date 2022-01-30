# Differentiation

We consider functions from $\RR^n$ to $\RR^m$.


## Differentiability and Jacobian

````{prf:definition} Differentiability at a point
:label: def-mvc-point-differentiability

Let $f : \RR^n \to \RR^m$. Let $\bx \in \interior \dom f$.
The function $f$ is differentiable at $\bx$ if
there exists a matrix $Df(\bx) \in \RR^{m \times n}$
that satisfies

```{math}
:label: eq-mvc-f-m-n-jacobian-limit
\underset{\bz \in \dom f, \bz \neq \bx, \bz \to \bz}{\lim}
\frac{\| f(\bz) - f(\bx) - Df(\bx) (\bz - \bx) \|_2}{\| \bz - \bx \|_2} = 0.
``` 
Such a matrix $Df(\bx)$ is called the *derivative* (or *Jacobian*) of $f$
at $\bx$.
````


There can be at most one $Df(\bx)$ satisfying the limit in
{eq}`eq-mvc-f-m-n-jacobian-limit`.

```{div}
The matrix $Df(\bx)$ can be obtained from the partial
derivatives:

$$
Df(\bx)_{ij} = \frac{\partial f_i(\bx)}{\partial \bx_j}, \quad
i=1,\dots,m, \quad j=1,\dots,n.
$$

$$
Df(\bx) = \begin{bmatrix}
 \frac{\partial f_1(\bx)}{\partial \bx_1} 
 &  \frac{\partial f_1(\bx)}{\partial \bx_2} 
 & \dots 
 &  \frac{\partial f_1(\bx)}{\partial \bx_n}\\
 \frac{\partial f_2(\bx)}{\partial \bx_1} 
 &  \frac{\partial f_2(\bx)}{\partial \bx_2} 
 & \dots 
 &  \frac{\partial f_2(\bx)}{\partial \bx_n}\\
 \vdots & \vdots & \ddots & \vdots \\
 \frac{\partial f_m(\bx)}{\partial \bx_1} 
 &  \frac{\partial f_m(\bx)}{\partial \bx_2} 
 & \dots 
 &  \frac{\partial f_m(\bx)}{\partial \bx_n}
\end{bmatrix}.
$$

1. Partial derivatives of each component of $f$ (i.e., $f_i$) 
   line up on the $i$-th row.
1. Partial derivatives for one coordinate $x_j$ line up 
   on the $j$-th column.
1. If $f$ is single valued, then the Jacobian $Df(\bx)$ is a row vector. 
```

````{prf:definition} Differentiable function
:label: def-mvc-differentiable-function

A function $f$ is called differentiable if its domain $\dom f$
is open and it is differentiable at every point of $\dom f$.
````


````{prf:definition} First order approximation
:label: def-mvc-first-order-approx

The affine function given by:

```{math}
:label: eq-mvc-first-order-approx
\hat{f} (\bx) = f(\ba) + Df(\ba)(\bx - \ba)
```
is called the *first order approximation* of $f$ 
at $\bx=\ba \in \interior \dom f$.
````


## Gradient


```{prf:definition} Gradient
:label: def-mvc-gradient

When $f : \RR^n \to \RR$ is a real valued function, then
the derivative $Df(\bx)$ is a $1 \times n$ matrix. 
The *gradient* of a real valued function is 
defined as:

$$
\nabla f(\bx) = Df (\bx)^T 
$$
at $\bx \in \interior \dom f$ if $f$ is differentiable
at $\bx$.
```
For real valued functions, the derivative is a row vector
but the gradient is a column vector.

```{div}
The components of the gradient are given by the 
partial derivatives as:

$$
\nabla f(\bx)_i = \frac{\partial f(\bx)}{\partial x_i}, \quad
i=1,\dots,n.
$$ 
```

````{prf:definition} First order approximation of real valued functions
:label: def-mvc-first-order-approx-real

The affine function given by:

```{math}
:label: eq-mvc-first-order-approx-real
\hat{f} (\bx) = f(\ba) + \nabla f(\ba)^T(\bx - \ba)
```
is the *first order approximation* of 
a real valued function $f$ at $\bx=\ba \in \interior \dom f$.
````


```{prf:example} Quadratic functional

Let $\bP \in \SS^n$ be a symmetric matrix. 
Let $\bq \in \RR^n$ and $r \in \RR$. 
Consider the quadratic functional $f: \RR^n \to \RR$ given as:

$$
f(\bx) = \frac{1}{2} \bx^T \bP \bx + \bq^T \bx + r.
$$

The derivative of $f$ is given by:

$$
Df (\bx) = \bx^T \bP + \bq^T.
$$

The gradient is given by:

$$
\nabla f(\bx) = \bP \bx + \bq.
$$
```

```{prf:definition} Gradient mapping
If a real valued function $f: \RR^n \to \RR$ 
is differentiable, the *gradient mapping* 
of $f$ is the function $\nabla f : \RR^n \to \RR^n$
with $\dom \nabla f = \dom f$, with the value $\nabla f(\bx)$
at every $\bx \in \dom f$. 
```

## Chain Rule

```{prf:theorem} Chain rule
:label: res-mvc-chain-rule

Suppose $f : \RR^n \to \RR^m$ is differentiable
at $\bx \in \interior \dom f$ and $g : \RR^m \to \RR^p$
is differentiable at $f(\bx) \in \interior \dom g$.
Define the composition $h: \RR^n \to \RR^p$ as:

$$
h(\bx) = g(f(\bx)).
$$

Then, $h$ is differentiable at $\bx$ with the derivative
given by:

$$
Dh(\bx) = Dg(f(\bx)) Df(\bx).
$$
```
Notice how the derivative lines up as a simple 
matrix multiplication.


```{prf:corollary} Chain rule for real valued functions
:label: res-mvc-chain-rule

Suppose $f : \RR^n \to \RR$ is differentiable
at $\bx \in \interior \dom f$ and $g : \RR \to \RR$
is differentiable at $f(\bx) \in \interior \dom g$.
Define the composition $h: \RR^n \to \RR$ as:

$$
h(\bx) = g(f(\bx)).
$$

Then, $h$ is differentiable at $\bx$ with the gradient
given by:

$$
\nabla h(\bx) = g'(f(\bx)) \nabla f(\bx).
$$
```

```{prf:corollary} Chain rule for composition with affine function
:label: res-mvc-chain-rule

Suppose $f : \RR^n \to \RR^m$ is differentiable.
Let $\bA \in \RR^{n \times p}$ and $\bb \in \RR^n$.
Define $g : \RR^p \to \RR^m$ as:

$$
g(\bx) = f(\bA \bx + \bb)
$$ 
with $\dom g = \{ \bx \ST \bA \bx + \bb \in \dom f \}$.

The derivative of $g$ at $\bx \in \interior \dom g$ is given by:

$$
Dg(\bx) = Df(\bA \bx + \bb) A.
$$

If $f$ is real valued (i.e. $m=1$), then 
the gradient of a composition of a function
with an affine function is given by:

$$
\nabla g(\bx) = \bA^T \nabla f(\bA \bx + \bb).
$$
```


## Hessian

In this section, we review the second derivative
of a real valued function $f: \RR^n \to \RR$.

````{prf:definition} Hessian
:label: def-mvp-hessian

The *second derivative* or *Hessian matrix* 
of $f$ at $\bx \in \interior \dom f$, denoted by
$\nabla^2 f$, is given by:

```{math}
\nabla^2 f(\bx)_{i j} = \frac{\partial^2 f(\bx)}{\partial x_i \partial x_j}, i=1,\dots,n \quad j=1,\dots,n
```
provided $f$ is twice differentiable at $\bx$.
````


````{prf:definition} Second order approximation
:label: def-mvp-snd-ord-approx

The *second order approximation* of $f$ at or near $\bx=\ba$ 
is the quadratic function defined by:

```{math}
\hat{f} (\bx) = f(\ba) + \nabla f(\ba)^T (\bx - \ba)
+ \frac{1}{2} (\bx - \ba)^T \nabla^2 f(\ba) (\bx - \ba).
```

````

