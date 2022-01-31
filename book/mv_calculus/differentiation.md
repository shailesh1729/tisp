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


```{prf:observation}
:label: res-mvc-f-m-n-jacobian-limit-alt

If we write $\bz = \bx + \bh$ then an alternative form for 
{eq}`eq-mvc-f-m-n-jacobian-limit` is given by:

$$
\underset{\bx + \bh \in \dom f, \bh \neq \bzero, \bh \to \bzero}{\lim}
\frac{\| f(\bx + \bh) - f(\bx) - Df(\bx) \bh \|_2}{\| \bh \|_2} = 0.
$$
```

```{div}
The matrix $Df(\bx)$ can be obtained from the partial
derivatives:

$$
Df(\bx)_{ij} = \frac{\partial f_i(\bx)}{\partial x_j}, \quad
i=1,\dots,m, \quad j=1,\dots,n.
$$

$$
Df(\bx) = \begin{bmatrix}
 \frac{\partial f_1(\bx)}{\partial x_1} 
 &  \frac{\partial f_1(\bx)}{\partial x_2} 
 & \dots 
 &  \frac{\partial f_1(\bx)}{\partial x_n}\\
 \frac{\partial f_2(\bx)}{\partial x_1} 
 &  \frac{\partial f_2(\bx)}{\partial x_2} 
 & \dots 
 &  \frac{\partial f_2(\bx)}{\partial x_n}\\
 \vdots & \vdots & \ddots & \vdots \\
 \frac{\partial f_m(\bx)}{\partial x_1} 
 &  \frac{\partial f_m(\bx)}{\partial x_2} 
 & \dots 
 &  \frac{\partial f_m(\bx)}{\partial x_n}
\end{bmatrix}.
$$

1. The Jacobian $Df(\bx)$ is an $m \times n$ real matrix.
1. Partial derivatives of each component of $f$ (i.e., $f_i$) 
   line up on the $i$-th row.
1. Partial derivatives for one coordinate $x_j$ line up 
   on the $j$-th column.
1. If $f$ is single valued, then the Jacobian $Df(\bx)$ is a row vector. 
```

```{prf:example} Jacobian of identity function
:label: ex-mvc-derivative-identity-map

Let $f: \RR^n \to \RR^n$ be defined as: 

$$
f(\bx) = \bx.
$$

Then,  $f_i(\bx) = x_i$. Hence,

$$
\frac{\partial f_i(\bx)}{\partial x_j} = \delta(i, j).
$$

Thus 

$$
D f(\bx) = \bI_n
$$
the $n\times n$ identity matrix.
```

```{prf:example} Jacobian of linear transformation
:label: ex-mvc-derivative-linear-map

Let $f: \RR^n \to \RR^m$ be defined as: 

$$
f(\bx) = \bA \bx
$$
where $\bA = (a_{i j})$ is an $m \times n$ real matrix.

Then,  $f_i(\bx) = \sum_{j=1}^n a_{i j} x_j$. Hence,

$$
\frac{\partial f_i(\bx)}{\partial x_j} = a_{i j}.
$$

Thus 

$$
D f(\bx) = \bA.
$$
```



```{prf:example} Jacobian of affine transformation
:label: ex-mvc-derivative-affine-map

Let $f: \RR^n \to \RR^m$ be defined as: 

$$
f(\bx) = \bA \bx + \bb
$$
where $\bA = (a_{i j}) \in \RR^{m \times n}$
and $\bb \in \RR^m$.

Then,  $f_i(\bx) = \sum_{j=1}^n a_{i j} x_j + b_i$. Hence,

$$
\frac{\partial f_i(\bx)}{\partial x_j} = a_{i j}.
$$

Thus 

$$
D f(\bx) = \bA.
$$

The vector $\bb$ is a constant offset. It has no impact
on the derivative.
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

```{prf:example} Gradient of linear functional
:label: ex-mvc-gradient-linear-functional

Let $f : \RR^n \to \RR$ be a linear functional given by:

$$
f(\bx) = \langle \bx, \ba \rangle = \ba^T \bx.
$$

We can expand it as:

$$
f(\bx) = \sum_{j=1}^n a_j x_j.
$$

Computing partial derivative with respect to $x_i$, we get:

$$
\frac{\partial f(\bx)}{\partial x_i} 
= \frac{\partial }{\partial x_i}\left (\sum_{j=1}^n a_j x_j \right )
= a_i.
$$

Putting the partial derivatives together, we get:

$$
\nabla f(\bx) = \ba.
$$
```

```{prf:example} Gradient of affine functional
:label: ex-mvc-gradient-affine-functional

Let $f : \RR^n \to \RR$ be a affine functional given by:

$$
f(\bx) = \ba^T \bx + b
$$
where $\ba \in \RR^n$ and $b \in \RR$.

We can expand it as:

$$
f(\bx) = \sum_{j=1}^n a_j x_j + b.
$$

Computing partial derivative with respect to $x_i$, we get:

$$
\frac{\partial f(\bx)}{\partial x_i} 
= \frac{\partial }{\partial x_i}\left (\sum_{j=1}^n a_j x_j  + b \right)
= a_i.
$$

Putting the partial derivatives together, we get:

$$
\nabla f(\bx) = \ba.
$$
The intercept $b$ is a constant term which doesn't affect the 
gradient.
```


```{prf:example} Gradient of quadratic form
:label: ex-mvc-gradient-quadratic-form

Let $f : \RR^n \to \RR$ be a quadratic form given by:

$$
f(\bx) = \bx^T \bA \bx
$$
where $\bA \in \RR^{n \times n}$.

We can expand it as:

$$
f(\bx) = \sum_{i=1}^n \sum_{j=1}^n x_i a_{i j} x_j.
$$
Note that the diagonal elements $a_{ii}$ give us terms of the 
form $a_{i i} x_i^2$. Let us split the expression into
diagonal and non-diagonal terms:

$$
f(\bx) = \sum_{i=1}^n a_{i i }x_i^2 + \sum_{\substack{i, j\\i \neq j}} x_i a_{i j} x_j.
$$
There are $n$ terms in the first sum (the diagonal entries of $\bA$)
and $n^2 - n$ terms in the second sum (the non-diagonal entries of $\bA$).

Taking partial derivative w.r.t. $x_k$, we obtain:

$$
\frac{\partial f(\bx)}{\partial x_k}
= 2 a_{k k} x_k 
+ \sum_{\substack{i\\i \neq k}} x_i a_{ i k} 
+ \sum_{\substack{j\\j \neq k}} a_{k j} x_j.
$$
* The first term comes from $a_{k k}$ term that is quadratic in $x_k$.
* The first sum comes from linear terms where $k=j$ and $i=1,\dots,n$ except $i\neq k$.
* The second sum comes from linear terms where $k=i$ and $j=1,\dots,n$ except $j\neq k$.
* There are $2n -2$ terms in the sums and $2$ $a_{k k} x_k$ terms.
* We can move one $a_{k k }x_k$ into each sum to simplify the partial derivative
  as:

$$
\frac{\partial f(\bx)}{\partial x_k}
= \sum_{i=1}^n x_i a_{i k}  + \sum_{j = 1}^n a_{k j} x_j. 
$$

Note that the $k$-th component of the vector $\bu = \bA \bx$ is
$\sum_{j=1}^n a_{k j} x_j$.

Similarly, the $k$-th component of the vector $\bv = \bA^T \bx$ is
$\sum_{i=1}^n a_{i k} x_i$.


Thus, 

$$
\frac{\partial f(\bx)}{\partial x_k} = v_k + u_k.
$$

Putting together the partial derivatives, we obtain:

$$
\nabla f(\bx) = \bv + \bu = \bA^T \bx + \bA \bx 
= (\bA^T  + \bA) \bx
= (\bA  + \bA^T) \bx.
$$

If $\bA$ is symmetric then,

$$
\nabla f(\bx) =  2 \bA \bx.
$$
```

```{prf:example} Gradient of quadratic functional
:label: ex-mvc-gradient-quadratic-functional

Let $\bP \in \SS^n$ be a symmetric matrix. 
Let $\bq \in \RR^n$ and $r \in \RR$. 
Consider the quadratic functional $f: \RR^n \to \RR$ given as:

$$
f(\bx) = \frac{1}{2} \bx^T \bP \bx + \bq^T \bx + r.
$$

We can compute the gradient as follows:

$$
\nabla f(\bx) 
&= \nabla \left( \frac{1}{2} \bx^T \bP \bx + \bq^T \bx + r \right )\\
&= \frac{1}{2} \nabla (\bx^T \bP \bx) + \nabla (\bq^T \bx)  + \nabla r \\
&= \frac{1}{2} (\bP + \bP^T) \bx + \bq \\
&= \frac{1}{2} (\bP + \bP) \bx + \bq\\
&= \bP \bx + \bq.
$$
* We took advantage of the fact that gradient operation commutes with
  scalar multiplication and distributes on vector addition.
* Since $r$ is a constant, it has no contribution to the derivative.
* We reused results from previous examples.
* We utilized the fact that $\bP = \bP^T$ since $\bP$ is symmetric.

In summary:

$$
\nabla f(\bx) 
= \bP \bx + \bq.
$$

The derivative of $f$ is then obtained by taking the transpose of the gradient:

$$
Df (\bx) = \bx^T \bP + \bq^T.
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
:label: res-mvc-chain-rule-real

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

```{prf:example} Gradient of log-sum-exp
:label: ex-mvc-gradient-log-sum-exp

Let $h : \RR^n \to \RR$ be given by:

$$
h(\bx) = \ln \left ( \sum_{i=1}^n \exp x_i \right )
$$
with $\dom h = \RR^n$.

Let $g(y) = \ln y$ and 

$$
f(\bx) = \sum_{i=1}^n \exp x_i
$$

Then, we can see that $h(\bx) = g (f (\bx))$.
Now $g'(y) = \frac{1}{y}$ and

$$
\nabla f(\bx) = \begin{bmatrix}
\exp x_1 \\ 
\vdots \\
\exp x_n
\end{bmatrix}.
$$

Thus,

$$
\nabla h(\bx) = \frac{1}{\sum_{i=1}^n \exp x_i} 
\begin{bmatrix}
\exp x_1 \\ 
\vdots \\
\exp x_n
\end{bmatrix}.
$$

Now, if we define 

$$
\bz = \begin{bmatrix}
\exp x_1 \\ 
\vdots \\
\exp x_n
\end{bmatrix}
$$
then, we see that:

$$
\bone^T \bz = \sum_{i=1}^n \exp x_i.
$$
Using this notation:

$$
\nabla h(\bx) = \frac{1}{\bone^T \bz} \bz.
$$
```

```{prf:corollary} Chain rule for composition with affine function
:label: res-mvc-chain-rule-affine-composition

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


```{prf:example} Chain rule for restriction on a line
:label: ex-f-rest-line-chain-rule

Let $f : \RR^n \to \RR$ be a real valued differentiable
function. Consider the restriction of $f$ on a line
in its domain

$$
g(t) = f(\bx + t \bv)
$$
where $\bx \in \dom f$ and $\bv \in \RR^n$ 
with the domain

$$
\dom g = \{t \ST \bx + t \bv \in \dom f\}.
$$ 

If we define $h : \RR \to \RR^n$ as:

$$
h(t) = \bx + t \bv;
$$
we can see that:

$$
g(t) = f(h(t))
$$

By chain rule:

$$
g'(t) = Df(h(t)) Dh(t) = \nabla f(h(t))^T \bv 
= \nabla f(\bx + t \bv)^T \bv.
$$

In particular, if $\bv = \by - \bx$, with $\by \in \dom f$,

$$
g'(t) = \nabla f(\bx + t (\by -\bx) )^T (\by - \bx)
= \nabla f(t \by + (1-t) \bx)^T (\by - \bx).
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

```{prf:example} Hessian of linear functional
:label: ex-mvc-hessian-linear-functional

Let $f : \RR^n \to \RR$ be a linear functional given by:

$$
f(\bx) = \langle \bx, \ba \rangle = \ba^T \bx.
$$

We can expand it as:

$$
f(\bx) = \sum_{j=1}^n a_j x_j.
$$

Computing partial derivative with respect to $x_i$, we get:

$$
\frac{\partial f(\bx)}{\partial x_i} 
= \frac{\partial }{\partial x_i}\left (\sum_{j=1}^n a_j x_j \right )
= a_i.
$$

If we further compute the partial derivative w.r.t. $x_j$, we get:

$$
\frac{\partial^2 f(\bx)}{\partial x_i \partial x_j} 
= \frac{\partial a_i}{\partial x_j}
= 0.
$$

Thus, the Hessian is an $n \times n$ 0 matrix:

$$
\nabla^2 f(\bx) = \ZERO_n.
$$
```

```{prf:theorem} 
:label: res-mvc-hessian-derivative-gradient

Hessian is the derivative of the gradient mapping.

$$
D \nabla f(\bx) = \nabla^2 f(\bx).
$$
```

```{prf:example} Hessian of quadratic form
:label: ex-mvc-hessian-quadratic-form

Let $f : \RR^n \to \RR$ be a quadratic form given by:

$$
f(\bx) = \bx^T \bA \bx
$$
where $\bA \in \RR^{n \times n}$.

Recall from {prf:ref}`ex-mvc-gradient-quadratic-form`
that:

$$
\nabla f(\bx)  = (\bA^T  + \bA) \bx.
$$

Also recall from {prf:ref}`ex-mvc-derivative-linear-map`
that 

$$
D (\bC \bx) = \bC 
$$
for all $\bC \in \RR^{m \times n}$.

Thus, using {prf:ref}`res-mvc-hessian-derivative-gradient`

$$
\nabla^2 f(\bx)  
= D \nabla f(\bx) 
= D ((\bA^T  + \bA) \bx)
= \bA^T  + \bA.
$$

If $\bA$ is symmetric then


$$
\nabla^2 f(\bx) = 2 \bA.
$$
```



```{prf:example} Hessian of log-sum-exp
:label: ex-mvc-hessian-log-sum-exp

Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) = \ln \left ( \sum_{i=1}^n e^{x_i} \right )
$$
with $\dom f = \RR^n$.

Define 

$$
\bz = \begin{bmatrix}
e^{x_1} \\ 
\vdots \\
e^{x_n}
\end{bmatrix}
$$
then, we see that:

$$
\bone^T \bz = \sum_{i=1}^n e^{x_i}.
$$
Using this notation:

$$
f(\bx) = \ln \left (\bone^T \bz \right).
$$

We have:

$$
\frac{\partial z_i}{\partial x_i} 
= \frac{\partial}{\partial x_i} e^{x_i}
= e^{x_i} = z_i.
$$
$\frac{\partial z_j}{\partial x_i} = 0$ for $i \neq j$. 
Now,

$$
\frac{\partial }{\partial x_i} f(\bx)
&= \frac{\partial}{\partial z_i} \ln \left (\bone^T \bz \right) \cdot \frac{\partial z_i}{\partial x_i} \\
&= \frac{1}{\bone^T \bz}\frac{\partial}{\partial z_i} \bone^T \bz \cdot z_i \\
&= \frac{1}{\bone^T \bz} z_i.
$$

Proceeding to compute the second derivatives:

$$
\frac{\partial^2 }{\partial x_i \partial x_j} f(\bx)
&= \frac{\partial }{\partial x_i} \left (\frac{1}{\bone^T \bz} z_j \right )\\
&= \frac{\partial }{\partial z_i} \left (\frac{1}{\bone^T \bz} z_j \right ) \cdot \frac{\partial z_i}{\partial x_i} \\
&= \frac{\bone^T \bz \delta_{i j} - z_j}{(\bone^T \bz)^2} \cdot z_i\\
&= \frac{\bone^T \bz \delta_{i j} z_i - z_i z_j}{(\bone^T \bz)^2}\\
&=\frac{\delta_{i j} z_i}{\bone^T \bz} - \frac{z_i z_j}{(\bone^T \bz)^2}.
$$

Now, note that $(\bz \bz^T)_{i j} = z_i z_j$.
And, $(\Diag (\bz))_{i j} = \delta_{ i j} z_i $. 

Thus,

$$
\nabla^2 f(\bx) = \frac{1}{\bone^T \bz} \Diag (\bz) - \frac{1}{(\bone^T \bz)^2} \bz \bz^T.
$$

Alternatively,

$$
\nabla^2 f(\bx) = \frac{1}{(\bone^T \bz)^2} \left ((\bone^T \bz) \Diag (\bz) - \bz \bz^T \right ).
$$

```


```{prf:example} Derivatives for least squares cost function
:label: ex-mvc-derivatives-ls-cost-func

Let $\bA \in \RR^{m \times n}$. Let $\bb \in \RR^n$.
Consider the least squares cost function:

$$
f(\bx) = \frac{1}{2} \| \bA \bx - \bb \|_2^2.  
$$

Expanding it, we get:

$$
f(\bx) = \frac{1}{2} \bx^T \bA^T \bA \bx - \bb^T \bA \bx + \frac{1}{2} \bb^T \bb. 
$$

Note that $\bA^T \bA$ is symmetric. Using previous results,
we obtain the gradient:

$$
\nabla f(\bx) = \bA^T \bA \bx - \bA^T \bb.
$$

And the Hessian is:

$$
\nabla^2 f(\bx) = D \nabla f (\bx) = \bA^T \bA.
$$
```

```{prf:example} Derivatives for quadratic over linear function
:label: ex-mvc-derivatives-quad-lin-func

Let $f : \RR \times \RR \to \RR$ be given by:

$$
f(x, y) = \frac{x^2}{y}
$$
with $\dom f = \{ (x, y) \ST y > 0\}$.

The gradient is obtained by computing the partial derivatives
w.r.t. $x$ and $y$:

$$
\nabla f(x,y) = \begin{bmatrix}
\frac{2x}{y}\\
\frac{-x^2}{y^2}
\end{bmatrix}.
$$

The Hessian is obtained by computing second order partial
derivatives:

$$
\nabla^2 f(x, y) = \begin{bmatrix}
\frac{2}{y} & \frac{-2 x}{y^2}\\
\frac{-2 x}{y^2} & \frac{2 x^2}{y^3} 
\end{bmatrix}
= \frac{2}{y^3} \begin{bmatrix}
y^2 & - x y\\
- x y & x^2
\end{bmatrix}.
$$
```



````{prf:definition} Second order approximation
:label: def-mvp-snd-ord-approx

The *second order approximation* of $f$ at or near $\bx=\ba$ 
is the quadratic function defined by:

```{math}
\hat{f} (\bx) = f(\ba) + \nabla f(\ba)^T (\bx - \ba)
+ \frac{1}{2} (\bx - \ba)^T \nabla^2 f(\ba) (\bx - \ba).
```

````

