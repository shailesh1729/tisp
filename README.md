# Optimization for Signal Processing Note Book

This is a collection of notes describing all the
necessary mathematics needed for building 
numerical optimization based algorithms for signal
processing.

The book is hosted at [convex.indigits.com](https://convex.indigits.com).

The topics covered include:

* Basic set theory
  * Sets, Relations, Functions
  * Sequences
  * Cartesian product, axiom of choice
* Elementary real analysis
  * Topology of the real line
  * Sequences and series
  * Extended real line
  * Real functions
  * Differentiable functions
  * Inequalities
* Metric spaces
  * Metric topology
  * Sequences
  * Functions and continuity
  * Completeness
  * Compactness
  * Subspaces
  * Real valued functions (closed functions, semicontinuity)
* Linear algebra
  * Vector spaces
  * Linear transformations
  * Inner product spaces
  * Dual spaces
  * Normed linear spaces
  * Euclidean space
  * Sequence spaces
  * Banach spaces
  * Hilbert spaces
  * Affine sets and transformations
* Multivariable calculus
  * Differentiation in n-dim spaces
  * Differentiation in Banach spaces
* Convex analysis and optimization
  * Convex sets and functions
  * Topology of convex sets
  * Separation theorems
  * Continuity of convex functions
  * Subgradients
  * Conjugate functions
  * Smoothness of convex functions
* Convex optimization
  * General concepts of mathematical optimization
  * Convex optimization formulations
  * Projection on convex sets
  * Duality
  * Linear programming
  * Quadratic programming
  * Optimization over differentiable objective functions
* Proximal operators


## Building from source

The book has been written using [jupyter-book](https://jupyterbook.org/).
You can build the book yourself from the source.

Make sure that you have Python 3.8 or later installed.

Clone the repository
```
git clone https://github.com/shailesh1729/cvx-opt-book.git
cd cvx-opt-book
```

Install the dependencies
```
pip install -r requirements.txt
```


Build the book
```
jupyter-book build book
```

Jupyter book will write the book's `HTML` content to `book/_build/html/`
directory, so you can open `index.html` from there to view the local build.

