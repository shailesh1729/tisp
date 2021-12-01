# Introduction


A mathematical optimization problem consists of maximizing
or minimizing a real valued function under a set of constraints.


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

