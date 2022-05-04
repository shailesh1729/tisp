(sec:opt:quadratic-programming)=
# Quadratic Programming

## Quadratic Functions

```{prf:definition} Quadratic function
:label: def-opt-quadratic-function

A function $f : \RR^n \to \RR$ of the form

$$
f(\bx) = \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c
$$
where $\bA \in \SS^n$, $\bb \in \RR^n$ and $c \in \RR$,
is known as a *quadratic function*.

The matrix $\bA$ is known as the *matrix associated with the quadratic function*.
```

```{prf:remark} Gradient and Hessian of a quadratic function
:label: res-opt-quadratic-gradient-hessian


Let 

$$
f(\bx) = \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c
$$
be a quadratic function. 
Then, the gradient is given by:

$$
\nabla f(\bx)  = \bA \bx + \bb.
$$

And, the Hessian is given by:

$$
\nabla^2 f(\bx) = \bA.
$$
```
See  {prf:ref}`ex-mvc-gradient-quadratic-functional`
and  {prf:ref}`ex-mvc-hessian-quadratic-form` for reference.

### Stationary Points

```{prf:theorem} Stationary points of quadratic functions
:label: res-opt-quadratic-func-stationary

Let a quadratic function $f : \RR^n \to \RR$ be given by

$$
f(\bx) = \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c
$$
where $\bA \in \SS^n$, $\bb \in \RR^n$ and $c \in \RR$.

1. $\bx \in \RR^n$ is a stationary point if and only if $\bA \bx = - \bb$.
1. If $\bA \succeq \ZERO$, then $\bx$ is a global minimum point of $f$ if and only if
   $\bA \bx = -\bb$.
1. If $\bA \succ \ZERO$, then $\bx = - \bA^{-1} \bb$
   is a strict global minimum point of $f$.
1. If $\bA \succ \ZERO$, then the minimum value of $f$ is
   $c - \frac{1}{2} \bb^T \bA^{-1} \bb$.
```


```{prf:proof}
(1) is a direct implication of the fact that $\nabla f(\bx) = \bzero$
if and only if $\bA \bx + \bb = \bzero$.

(2) We are given that $\nabla^2 f(\bx) = \bA \succeq \ZERO$.

1. Thus, $\nabla^2 f(\bx) \succeq \ZERO$ for every $\bx \in \RR^n$.
1. By {prf:ref}`res-opt-hessian-global-minimum-suf`, if $\bx$ is a
   stationary point of $f$, then it is a global minimum point.
1. By first part, $\bx$ is a stationary point if and only if $\bA \bx = - \bb$.

(3) We are given that $\bA \succ \ZERO$.

1. Then, $\bA$ is invertible.
1. Hence, $\bx = - \bA^{-1} \bb$ is the unique solution to the equation
   $\bA \bx = - \bb$.
1. By parts (1) and (2), it is the unique (hence strict) global minimizer of $f$.

(4) We know that strict global minimum point of $f$ is given by $\ba = - \bA^{-1} \bb$
with $\bA \ba = - \bb$.
Therefore,

$$
f(\ba) &=  \frac{1}{2} \ba^T \bA \ba + \bb^T \ba + c \\
&= - \frac{1}{2} \ba^T \bb + \bb^T \ba + c \\
&= c + \frac{1}{2} \bb^T \ba  \\
&= c - \frac{1}{2} \bb^T \bA^{-1} \bb.
$$
```

### Coerciveness

```{prf:theorem} Coerciveness of quadratic functions
:label: res-opt-quadratic-func-coercive

Let a quadratic function $f : \RR^n \to \RR$ be given by

$$
f(\bx) = \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c
$$
where $\bA \in \SS^n$, $\bb \in \RR^n$ and $c \in \RR$.

$f$ is coercive if and only if $\bA \succ \ZERO$; i.e.,
$\bA$ is positive definite.
```

```{prf:proof}

Assume that $\bA$ is positive definite. 

1. Then, all eigenvalues of $\bA$ are positive.
1. Let $\lambda$ be the smallest eigenvalue of $\bA$.
1. Then, $\bx^T \bA \bx \geq \lambda \| \bx \|^2$ for every $\bx \in \RR^n$.
1. Thus,

   $$
   f(\bx) &\geq \frac{ \lambda}{2}  \| \bx \|^2 + \bb^T \bx + c \\
   &\geq \frac{ \lambda}{2}  \| \bx \|^2 - \|\bb \| \| \bx \| + c 
   & \text{ Cauchy Schwartz inequality }\\
   &= \frac{ \lambda}{2} \| \bx \| \left (\| \bx \| - \frac{2}{\lambda} \| \bb \| \right ) + c.
   $$
1. We can see that $f(\bx) \to \infty$ as $\| \bx \| \to \infty$.
1. Thus, $f$ is coercive.

Now, assume that $f$ is coercive.

1. We need to show that $\bA$ must be positive definite.
1. Thus, all eigenvalues of $\bA$ must be positive.
1. For contradiction, assume that an eigenvalue of $\bA$ is negative.
1. Let $\lambda < 0$ be such an eigenvalue with the corresponding
   normalized eigenvector $\bv$ such that $\bA \bv = \lambda \bv$.
1. Then, for any $t \in \RR$,

   $$
   f(t \bv) &= \frac{t^2}{2} \bv^T \bA \bv + t \bb^T \bv + c \\
   &= \frac{\lambda t^2}{2} + t \bb^T \bv + c.
   $$
1. Clearly, $f(t \bv) \to -\infty$ as $t \to \infty$ since $\lambda$ is negative.
1. Thus, it contradicts the hypothesis that $f$ is coercive.
1. We now consider the possibility where there is a 0 eigenvalue.
1. Then, there exists a normalized eigenvector $\bv$ such that $\bA \bv = \bzero$.
1. Then, for any $t \in \RR$,

   $$
   f(t \bv) = t \bb^T \bv + c.
   $$
1. If $\bb^T \bv = 0$, then $f(t\bv) = c$ for every $t \in \RR$.
1. If $\bb^T \bv > 0$, then $f(t \bv) \to -\infty$ as $t \to -\infty$.
1. If $\bb^T \bv < 0$, then $f(t \bv) \to -\infty$ as $t \to \infty$.
1. In all the three cases, $f(t \bv)$ does not go to $\infty$ as $\| t \bv \| \to \infty$.
1. Thus, $f$ is not coercive. A contradiction to the hypothesis.
1. Hence, the eigenvalues of $\bA$ must be positive.
1. Hence, $\bA$ must be positive definite.
```

### Nonnegative Quadratics

It is useful to work with quadratic functions which are nonnegative
on the entire $\RR^n$.

The basic quadratic form $f(\bx) = \frac{1}{2} \bx^T \bA \bx$
is nonnegative on entire $\RR^n$ if $\bA$ is positive semidefinite.

For the general quadratic function, we need to incorporate the
contribution from $\bb$ and $c$ terms also.

```{prf:theorem} Nonnegativity of quadratic function
:label: res-opt-quadratic-func-nng

Let a quadratic function $f : \RR^n \to \RR$ be given by

$$
f(\bx) = \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c
$$
where $\bA \in \SS^n$, $\bb \in \RR^n$ and $c \in \RR$.

The following statements are equivalent.

1. $f(\bx) \geq 0$ for every $\bx \in \RR^n$.
1. $\begin{bmatrix} \bA & \bb \\ \bb^T & 2 c \end{bmatrix} \succeq \ZERO$;
   i.e., this $n+1 \times n+1$ symmetric matrix is positive semidefinite.
```

```{prf:proof}

Assume that (2) is true.

1. Then, for every $\bx \in \RR^n$

   $$
   \begin{bmatrix} \bx \\ 1 \end{bmatrix}^T
   \begin{bmatrix} \bA & \bb \\ \bb^T & 2 c \end{bmatrix}
   \begin{bmatrix} \bx \\ 1 \end{bmatrix}
   \geq 0
   $$
   due to positive semidefiniteness.
1. But 

   $$
   \begin{bmatrix} \bx \\ 1 \end{bmatrix}^T
   \begin{bmatrix} \bA & \bb \\ \bb^T & 2 c \end{bmatrix}
   \begin{bmatrix} \bx \\ 1 \end{bmatrix}
   &= \begin{bmatrix} \bx^T & 1 \end{bmatrix}
   \begin{bmatrix} \bA \bx + \bb \\ \bb^T \bx + 2c \end{bmatrix} \\
   & = \bx^T \bA \bx + 2 \bx^T \bb + 2 c \\
   &= 2 \left ( \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c \right ) \\
   = 2 f(\bx).
   $$
1. Thus, $f(\bx) \geq 0$ for every $\bx \in \RR^n$.

For the converse, assume (1) is true.

1. We need to show that $\begin{bmatrix} \bA & \bb \\ \bb^T & 2 c \end{bmatrix}$
   is positive semidefinite.
1. We shall first show that $\bA$ is positive semidefinite.
1. For contradiction, assume that $\bA$ is not positive semidefinite.
1. Then, there exists a negative eigenvalue $\lambda < 0$ and corresponding
   normalized eigenvector $\bv$ for $\bA$
   such that $\bA \bv = \lambda \bv$.
1. Then, for any $t \in \RR$
   
   $$
   f(t \bv) = \frac{\lambda t^2}{2} + t \bb^T \bv + c. 
   $$
1. Then, $f(t \bv) \to -\infty$ as $t \to -\infty$.
1. This contradicts the hypothesis that $f$ is nonnegative everywhere.
1. Thus, $\bA$ must be positive semidefinite.
1. We now need to show that for any $\by \in \RR^n$ and any $t \in \RR$,
   
   $$
   \begin{bmatrix} \by \\ t \end{bmatrix}^T
   \begin{bmatrix} \bA & \bb \\ \bb^T & 2 c \end{bmatrix}
   \begin{bmatrix} \by \\ t \end{bmatrix} \geq 0.
   $$
1. This condition is equivalent to

   $$
   \frac{1}{2} \by^T \bA \by + t \bb^T \by + c t^2 \geq 0
   $$
   for every $\by \in \RR^n$ and $t \in \RR$.
1. If $t = 0$, then this condition reduces to 

   $$
   \by^T \bA \by \geq 0 \Forall \by \in \RR^n.
   $$
1. This is valid for every $\by \in \RR^n$ since $\bA$ is p.s.d..
   as established earlier.
1. For $t \neq 0$, we have

   $$
   t^2 f \left ( \frac{\by}{ t} \right ) 
   = t^2 \left ( \frac{1}{2 t^2} \by^T \bA \by + \frac{1}{t} \bb^T \by + c \right )
   = \frac{1}{2 } \by^T \bA \by + t \bb^T \by + c t^2.
   $$
1. By hypothesis, $t^2 f \left ( \frac{\by}{ t} \right ) \geq 0$ 
   for every $\by \in \RR^n$ and $t \neq 0$.
1. Thus, $\frac{1}{2 } \by^T \bA \by + t \bb^T \by + c t^2 \geq 0$ for every $\by \in \RR^n$
   and $t \in \RR$.
1. Thus, $\begin{bmatrix} \bA & \bb \\ \bb^T & 2 c \end{bmatrix}$ is indeed p.s.d..
```






## Quadratic Optimization Problems

We consider the following possibilities:

1. The objective function is a quadratic function.
1. Both the objective function as well as the inequality constraints function
   are quadratic.

### Quadratic Program

````{prf:definition} Quadratic program
:label: def-opt-quadratic-program

A convex optimization problem is known as 
a *quadratic program* (QP) if the objective function
is a (convex) quadratic and the constraint functions are affine.

A general quadratic program has the following form:

```{math}
:label: eq-opt-quadratic-program-general-form
& \text{minimize }   & & \frac{1}{2} \bx^T \bP \bx + \bq^T \bx + r \\
& \text{subject to } & & \bG \bx \preceq \bh \\
&                    & & \bA \bx = \bb
```
where
1. $\bx \in \RR^n$ is the optimization variable.
1. $\bP \in \SS^n_+$ is a symmetric positive semidefinite matrix.
1. $\bq \in \RR^n$ and $r \in \RR$.
1. $f(\bx) = \frac{1}{2} \bx^T \bP \bx + \bq^T \bx + r$ is a
   (convex) quadratic objective function.
1. $\bG \in \RR^{m \times n}$ and $\bh \in \RR^m$
   describe the $m$ affine inequality constraints.
1. $\bA \in \RR^{p \times n}$ and $\bb \in \RR^p$
   describe the $p$ affine equality constraints.
````


### Quadratically Constrained Quadratic Program

````{prf:definition} Quadratically constrained quadratic program
:label: def-opt-qcqp

A convex optimization problem is known as 
a *quadratically constrained quadratic program* (QCQP) if the objective function
and the inequality constraint functions are (convex) quadratic 
while the equality constraint functions are affine.

A general quadratic program has the following form:

```{math}
:label: eq-opt-qcqp-general-form
& \text{minimize }   & & \frac{1}{2} \bx^T \bP_0 \bx + \bq_0^T \bx + r_0 \\
& \text{subject to } & &  \frac{1}{2} \bx^T \bP_i \bx + \bq_i^T \bx + r_i \leq 0 & 
  \quad i=1,\dots, m\\
&                    & & \bA \bx = \bb
```
where
1. $\bx \in \RR^n$ is the optimization variable.
1. $\bP_i \in \SS^n_+$ are symmetric positive semidefinite matrices for $i=0,\dots,m$.
1. $\bq_i \in \RR^n$ and $r_i \in \RR$ for $i=0,\dots,m$.
1. $f_0(\bx) = \frac{1}{2} \bx^T \bP_0 \bx + \bq_0^T \bx + r_0$ is a
   (convex) quadratic objective function.
1. $f_i(\bx) = \frac{1}{2} \bx^T \bP_i \bx + \bq_i^T \bx + r_i$ are
   (convex) quadratic inequality constraint functions for $i=1,\dots,m$.
1. $\bA \in \RR^{p \times n}$ and $\bb \in \RR^p$
   describe the $p$ affine equality constraints.
````
