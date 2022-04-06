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
