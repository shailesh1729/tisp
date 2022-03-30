# Linear Programming


## Linear Optimization Problem

### General Form

````{prf:definition} Linear optimization problem
:label: def-opt-linear-optimization

A convex optimization problem where the objective and
constraint functions are all affine is known as 
a *linear optimization problem* or a *linear program*.

A general linear program has the following form:

```{math}
:label: eq-opt-linear-program-general-form
& \text{minimize }   & & \bc^T \bx + d \\
& \text{subject to } & & \bG \bx \preceq \bh \\
&                    & & \bA \bx = \bb
```
where
1. $\bx \in \RR^n$ is the optimization variable.
1. $f(\bx) = \bc^T \bx + d$ is an affine objective function.
1. $\bG \in \RR^{m \times n}$ and $\bh \in \RR^m$
  describe the $m$ affine inequality constraints.
1. $\bA \in \RR^{p \times n}$ and $\bb \in \RR^p$
   describe the $p$ affine equality constraints.
````

```{note}

1. Minimizing $\bc^T \bx + d$ is same as minimizing $\bc^T \bx$ 
   with the scalar $d$ only being an offset for the optimal value.
   Thus, the affine objective can be replaced as a linear objective.
1. The problem of maximizing $\bc^T \bx + d$ is same as
   the problem of minimizing $-\bc^T \bx - d$ which is also an
   affine functional.
   Thus, an affine maximization problem with affine constraints is
   also a linear program.
1. The feasible set of a linear program is a polyhedron.
   Recall from {prf:ref}`def-convex-polyhedron` that a polyhedron
   is the solution set of a finite number of linear inequalities
   and linear equations. In this case, we have $m$ linear inequalities
   and $p$ linear equations.
```

### Standard Form

````{prf:definition} Linear programming standard form
:label: def-opt-lp-standard-form

The standard form for linear programming is given by

```{math}
:label: eq-opt-lp-standard-form
& \text{minimize }   & & \bc^T \bx \\
& \text{subject to } & & \bA \bx = \bb \\
&                    & & \bx \succeq \bzero.
```
````

```{note}
This form has

1. A linear objective function.
1. A system of linear equations as equality constraints.
1. Component wise nonnegativity constraints on the optimization variable $\bx$.
```



```{prf:observation} Converting general form into standard form
:label: res-lp-general-to-standard

We show how the general form {eq}`eq-opt-linear-program-general-form`
can be converted to an equivalent standard form {eq}`eq-opt-lp-standard-form`
linear programming problem.

1. We first introduce slack variables to the linear inequalities $\bs \in \RR^m$.
   We get the form

   $$
   & \text{minimize }   & & \bc^T \bx + d \\
   & \text{subject to } & & \bG \bx + \bs = \bh \\
   &                    & & \bA \bx = \bb \\
   &                    & & \bs \succeq \bzero.
   $$

1. We next split the optimization variable $\bx \in \RR^n$ as the
   difference between two nonnegative variables $\bx^+$ and $\bx^-$.
   $\bx = \bx^+ - \bx^-$ where both $\bx^+, \bx^- \in \RR^n_+$.
   The optimization problem becomes:

   $$
   & \text{minimize }   & & \bc^T \bx^+ - \bc^T \bx^- + d \\
   & \text{subject to } & & \bG \bx^+ - \bG \bx^- + \bs = \bh \\
   &                    & & \bA \bx^+ - \bA \bx^- = \bb \\
   &                    & & \bx^+ \succeq \bzero, \bx^- \succeq \bzero, \bs \succeq \bzero.
   $$
1. This is an LP in standard form with the optimization variables being
   $\bx^+$, $\bx^-$, and $\bs$. 
   1. We can drop the scalar $d$ to get a linear objective function. 
   1. We can introduce an optimization variable $\by \in \RR^{2n + m}$ as the concatenation
      of $\bx^+$, $\bx^-$, and $\bs$ and require that $\by \succeq \bzero$
      be the unified inequality constraint.
   1. We can then write $\bG \bx^+ - \bG \bx^- + \bs = \bh$ as

      $$
      \begin{bmatrix} \bG & - \bG & \bI_m \end{bmatrix} \by = \bh.
      $$
   1. Similarly, the objective function can be written as

      $$
      \begin{bmatrix} \bc \\ - \bc \\ \bzero_m \end{bmatrix}^T \by.
      $$ 
```

### Inequality Form

````{prf:definition} Linear programming inequality form
:label: def-opt-lp-inequality-form

The standard form for linear programming is given by

```{math}
:label: eq-opt-lp-inequality-form
& \text{minimize }   & & \bc^T \bx \\
& \text{subject to } & & \bA \bx \preceq \bb.
```
````

```{note}
This form has

1. A linear objective function.
1. A system of linear inequalities as inequality constraints.
1. No equality constraints.
```


