# Convex Sets and Functions

We will primarily be considered with functions 
of type $\EE \to \VV$ where $\EE$ and $\VV$ are
finite dimensional real inner product spaces.

Examples of inner product spaces:

- Euclidean space $\RR^n$
- Space of matrices $\RR^{m \times n}$
- Space of symmetric matrices $\SS^n$.


In particular, we will concern ourselves with 
real valued functions with signatures $f: \VV \to \RR$ from an 
inner product space $\VV$ to real line. 
Often, interesting functions are not defined over
the entirety of $\VV$. Their domain is a proper subset
of $\VV$. In such cases, it is very useful to extend
such functions by assigning an infinity value to them
at points outside their domain.
Their extended value extensions $\tilde{f} : \VV \to [-\infty, \infty]$
will play a crucial role in simplifying analysis.
Real-valued functions are equipped with a total order in the codomain
$\RR$. Thus, it is possible to compare $f(\bx)$ with $f(\by)$
for some $\bx, \by \in \VV$ to establish whether 
$f(\bx) < f(\by)$ or $f(\bx) = f(\by)$ or $f(\bx) > f(\by)$.
Real valued functions are naturally used to represent
the cost functions in optimization problems where the
goal is to minimize the cost. Or they can be value
functions if the goal is to maximize some kind of value.
A special class of these real valued functions are
the convex functions. The epigraph of convex
functions is a convex set. Their domain is also
a convex set. Convex functions support
a wonderful feature that any local minimizer 
is also a global minimizer. 


Chapter objectives

* Convex set definitions
* Different types of convex sets
* Properties of convex sets
* Convexity preserving operations
* Generalized inequalities on convex cones
* Convex functions and their properties
* Extended valued functions
* Subgradients
* Conjugate functions
* Norms and dual norms
* Strong convexity
* Convexity preserving operations
* Smoothness
* Quasiconvex functions
* Proximal mappings


* Subgradient
  * Subgradient inequality
  * Subdifferential set
  * Subdifferential of indicator functions
  * Subgradient of the dual function
  * Subgradient of maximum eigen value function
  * Weak vs strong results
  * Subdifferentiability
* Properties of subdifferential set 
  * closedness
  * convexity
  * nonemptiness of subdifferential sets implies convexity
  * convex functions may not be subdifferentiable at the boundary points
  * nonemptiness and boundedness of the subdifferentiable set at the 
    interior points of the domain of a convex function
  * Subdifferentiability of real-valued convex functions
  * Boundedness of subgradients over compact sets
  * Nonemptiness of the subdifferential set at relative interior points
  * Unboundedness condition for subdifferential sets
* Directional derivatives
  * Existence in the interior
  * Direction to directional derivative map
    * Convexity
    * Homogeneity
  * Connection between directional derivative and convex function value
  * Directional derivative of a maximum of functions
  * Directional derivative of a maximum of functions - convex case
  * Max formula connecting subgradients and directional derivatives
  * Max formula as support function
* Differentiability
  * Differentiable functions
  * Gradient
  * Uniqueness of the gradient
  * Directional derivatives at the point of differentiability
  * Directional derivative of maximum of differentiable functions
  * Gradient of the squared Euclidean distance to a convex set function



Related concepts

* Normal cone
* Supporting hyperplane theorem
* Local Lipschitz continuity property
* Relative interior
* Nonemptiness of the relative interior
* Orthogonal projection mapping (POCS)

