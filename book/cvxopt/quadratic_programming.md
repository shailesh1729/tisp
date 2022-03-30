# Quadratic Programming


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
