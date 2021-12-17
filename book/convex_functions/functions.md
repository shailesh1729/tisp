# Functions

We quickly recall some important definitions which will 
be useful later on.

```{prf:definition} Domain of a function
:label: def-function-domain

For a function $f: A \to B$ the *domain* of the
function is the subset of $A$ for which the function
is defined. It is denoted by $\dom f$. 
```
The notation $f : \RR^n \to \RR^m$ means that f maps
(some) n-vectors into m-vectors. $f$ need not be defined
for all of $\RR^n$.

```{prf:example} 
The set of $n \times n$ real symmetric matrices is denoted by $\SS^n$. 
The set of positive semidefinite symmetric matrices is denoted by $\SS^n_+$. 
The set of positive definite symmetric matrices is denoted by $\SS^n_{++}$.

Consider the function $f : \SS^n \to \RR$ given by

$$
f (X) = \log \det (X).
$$

The domain of the function is $\dom f = \SS^n_{++}$. The function
is not defined for matrices which are not positive definite.
```

By $\interior \dom f$, we shall mean the interior of the domain of $f$.

```{prf:definition} Graph of a function
:label: def-function-graph

Given a function $f : X \to Y$, 
the set of ordered pairs $(x, y)$ where
$x \in \dom f$ and $y = f(x)$,
is known as the *graph* of a function.

$$
G(f) \triangleq \{ (x, f(x)) : x \in X \}
$$

The graph of a function is the subset of the
Cartesian product  $X \times Y$. 
```

Real valued functions: 

* For a function $f : \RR^n \to \RR$,
  its graph is a subset of $\RR^{n+1}$.
* We say that a point $(x, f(x))$ in the graph of $f$
  is above (resp. below) of another point $(y, f(y))$
  if $f(x) \geq f(y)$ (resp. $f(x) \leq f(y)$).
* A line segment connecting the two points 
  $(x_1, f(x_1))$ and $(x_2, f(x_2))$ is called a
  *chord* of the graph of the function.

```{prf:definition} Epigraph
:label: def-epigraph

The *epigraph* of a real valued function $f: \EE \to \RR$ is
defined as:

$$
\epi f \triangleq \{ (x,t) \in \EE \times \RR \, | \, x \in \dom f, f(x) \leq t \}.
$$ 
```
The epigraph lies above (and includes) the graph of a function.

```{prf:definition} Sub-level set
:label: def-epigraph

For a real valued function $f: \EE \to \RR$, the sublevel set
for some $\alpha \in \RR$ is defined as 

$$
\{ x \in \dom f \,|\, f(x) \leq \alpha \}.
$$
```


## Continuity

```{prf:definition} Continuous function
:label: def-continuous-function

A function $f : \EE \to \VV$ is *continuous* at a 
point $x \in \dom f$ if for every $\epsilon > 0$ there exists
$\delta > 0$ such that 
for every $y \in \dom f$,

$$ 
\| y - x \|_2 \leq \delta \implies \| f(y)  - f(x) \|_2 \leq \epsilon .
$$

A function is *continuous* if it is continuous at every point
in its domain.
```


## Closed Functions

```{prf:definition} Closed function
:label: def-closed-function

A real valued function $f : \EE \to \RR$ is *closed* 
if for each $\alpha \in \RR$,
the corresponding sublevel set is closed. 

In other words, the set:

$$
\{ x \in \dom f \,|\, f(x) \leq \alpha \}
$$

is closed for every $\alpha \in \RR$.
```
```{prf:lemma}
The epigraph of a closed function is closed.
```

```{prf:lemma}
If $f: \EE \to \RR$ is continuous and $\dom f$ is closed, then 
$f$ is closed.
```

```{prf:lemma}
If $f: \EE \to \RR$ is continuous and $\dom f$ is open, then
$f$ is closed if and only if $f$ converges to $\infty$ along
every sequence converging to a boundary point of $\dom f$. 
```
