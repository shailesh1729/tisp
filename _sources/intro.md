# Welcome


## What is New

* {ref}`sec:ms:metric-topology`
* Linear Algebra and Analysis
  * {ref}`sec:la:normed-spaces`
  * {ref}`sec:la:affine_sets`
* Convex Sets and Functions
  * {ref}`sec:cvxf:convex-functions`
  * {ref}`sec:cvx:relint`


## Mathematical Optimization Problems

A mathematical optimization problem consists of maximizing
or minimizing a real valued function under a set of constraints.


Formally, we express a mathematical optimization problem as:

$$
\begin{aligned}
  & \text{minimize}  & &  f_0(x) & & \\
  & \text{subject to} & & f_i(x) \leq b_i, & & i = 1, \dots, m.
\end{aligned}
$$

* $x \in \RR^n$ is the *optimization variable* of the problem.
* $f_0 : \RR^n \to \RR$ is the *objective function*.
* The functions $f_i : \RR^n \to \RR, \; i=1,\dots, m$ are the
  (inequality) *constraint functions*.
* The constants $b_1, \dots, b_m$ are the limits for the 
  inequality constraints.
* A vector $x \in \RR^n$ is called *feasible* if it belongs to
  the domains of $f_0, f_1, \dots, f_m$ and satisfies all the
  constraints. 
* A vector$x^{\dag}$ is called *optimal* if is feasible and has
  the smallest objective value; i.e. for any feasible $z$, 
  we have $f_0(z)\geq f_0(x^{\dag})$. 
* An optimal vector is also called a *solution* to the 
  optimization problem.
* An optimization problem is called *infeasible* if there
  is no feasible vector. i.e. there is no vector $x \in \RR^n$
  which satisfies the inequality constraints.
* An infeasible problem doesn't have a solution.
* A feasible problem may not have a solution if the objective
  function is *unbounded below*. i.e. for every feasible $x$, 
  there exists another feasible $z$ such that $f_0(z) < f_0(x)$.
* If a feasible problem is not unbounded below, then it may have
  one or more solutions.

Convex Optimization focuses on a special class of mathematical 
optimization problems where:

* The real valued function being optimized (maximized or minimized)
  is convex.
* The feasible set of values for the function is a convex set.

In the sequel, we will elaborate on these requirements.


```{figure} images/convex_function.png
---
name: convex_function
---
For a convex function, the line segment between any two
points on the graph of the function does not lie below
the graph between the two points. Its epigraph is a 
convex set. A local minimum of a convex function 
is also a global minimum.
``` 

## Convex Optimization Problems

Convex optimization problems are usually further classified into

* Least squares
* Linear programming
* Quadratic minimization with linear constraints
* Quadratic minimization with convex quadratic constraints
* Conic optimization
* Geometric programming
* Second order cone programming 
* Semidefinite programming 

There are specialized algorithms available for each of these
classes.

## Applications

Some of the applications of convex optimization include:

* Portfolio optimization
* Worst case risk analysis
* Compressive sensing
* Statistical regression
* Model fitting
* Combinatorial Optimization



## References

This listing is by no means exhaustive. 

* General introduction to optimization can be found in
  {cite}`nocedal2006numerical`.
* Main references for convex analysis are 
  {cite}`bertsekas2003convex,rockafellar2015convex`.
* {cite}`boyd2004convex` is a standard textbook for 
  convex optimization theory, applications and algorithms.
* {cite}`luenberger1984linear` is a good reference for linear
  programming.
* {cite}`boyd2011distributed` covers alternating direction 
  method of multipliers (ADMM) algorithms.
* {cite}`parikh2014proximal` provides good coverage on 
  proximal algorithms.


The content in the sequel is derived extensively from 
these sources.

