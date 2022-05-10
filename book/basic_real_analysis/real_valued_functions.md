(sec:bra:real-valued-functions)=
# Real Valued Functions


## Real Valued Functions


```{prf:definition} Real valued function
:label: def-bra-real-valued-function

A (partial) *real valued function* is a function whose values are real numbers.
Let $X$ be a set. Then $f : X \to \RR$ is a real valued function
from $X$ to $\RR$.
```


```{prf:definition} The set of real valued total functions
:label: def-bra-rvf-set

The set $\FFF (X, \RR)$ denotes the set of all real valued (total) functions
from $X$ to $\RR$.
```

```{prf:definition} The vector space of real valued functions
:label: def-bra-real-valued-function-vector-space

The set $\FFF (X, \RR)$ can be turned into a vector space
over the field $\RR$ with the following operations.

Let $f,g \in \FFF (X, \RR)$.

Vector addition:

$$
f + g : x \mapsto f(x) + g(x) \Forall x \in X.
$$

Additive identity:

$$
\bzero : x \mapsto 0 \text{ with } \Forall x \in X.
$$

Scalar multiplication:

$$
cf : x \mapsto c f(x) \Forall x \in X.
$$


pointwise multiplication:

$$
f g: x \mapsto f(x) g(x) \Forall x \in X.
$$
```

```{prf:definition} An algebra for partial functions
:label: def-bra-rvpf-algebra

An algebraic structure can be provided to partial functions too.

Let $f,g$ be (partial) real valued functions  from $X$ to $\RR$.

Vector addition:

$$
f + g : x \mapsto f(x) + g(x) \text{ with } \dom f + g = \dom f \cap \dom g.
$$

Additive identity:

$$
\bzero : x \mapsto 0 \text{ with } \dom \bzero = X.
$$

Scalar multiplication:

$$
cf : x \mapsto c f(x) \text{ with } \dom cf = \dom f.
$$


pointwise multiplication:

$$
f g: x \mapsto f(x) g(x) \text{ with } \dom f g = \dom f \cap \dom g.
$$
```
However, there are certain limitations/odd behaviors with the structure.

* If $f$ and $g$ are such that $\dom f \cap \dom g = \EmptySet$.
  Then $f + g$ is an empty function.
* The function $f + (-f)$ is 0 over $\dom f$ but not defined
  over $X \setminus \dom f$. 
  Thus, it is not equal to the $\bzero$ function.
  Thus, an additive inverse doesn't exist.
* Scalar multiplication with $0$ leads to a function which 
  is $0$ only over $\dom f$. It is not defined over $X \setminus \dom f$.




```{prf:definition} Partial order on real valued (total) functions
:label: def-bra-rv-func-partial-order

Since $\RR$ is ordered, hence a partial order can be defined
on $\FFF (X, \RR)$.

We say that 

$$
f \preceq g \iff f(x) \leq g(x) \Forall x \in X.
$$
```

Partial order cannot be easily defined for partial functions as it is unclear 
how to compare $f(x)$ and $g(x)$ at $x \in \dom f \triangle \dom g$. 

One possible way is:

$$
f \preceq g \iff \dom f = \dom g \text{ and } f(x) \leq g(x) \Forall x \in \dom f.
$$

```{prf:definition} Bounded function
:label: def-bra-bounded-function

A real valued (total) function $f:X \to \RR$ is called *bounded*
if there exists a number $M \geq 0$ (depending on $f$) 
such that 

$$
| f(x)| \leq M \Forall x \in X.
$$

A function which is not bounded is called *unbounded*.

$f$ is called *bounded from above* by $a \in \RR$ if:

$$
f(x) \leq a \Forall x \in X.
$$

$f$ is called *bounded from below* by $b \in \RR$ if:

$$
b \leq f(x) \Forall x \in X.
$$
```
Boundedness of partial real valued functions (with $\dom f \subset X$)
is not useful as partial functions are typically extended (see below)
with $f(x)$ assigned to $\infty$ at $x \notin \dom f$.
In other words, partial functions are treated as unbounded outside
their domain.

```{prf:proposition}
:label: res-bra-rv-func-bounded-charac

A real valued function is bounded if and only if
it is bounded from above as well as below.
```

```{rubric} See also
```

1. The set of bounded (total) functions can be turned into
   a metric space. 
   See {prf:ref}`ex-ms-bounded-functions-metric-space`. 

## Graph

* For a function $f : \RR^n \to \RR$,
  its graph is a subset of $\RR^{n+1}$.
* We say that a point $(x, f(x))$ in the graph of $f$
  is above (resp. below) of another point $(y, f(y))$
  if $f(x) \geq f(y)$ (resp. $f(x) \leq f(y)$).
* A line segment connecting the two points 
  $(x_1, f(x_1))$ and $(x_2, f(x_2))$ is called a
  *chord* of the graph of the function.


## Epigraph

```{prf:definition} Epigraph
:label: def-bra-epigraph

The *epigraph* of a real valued function $f: X \to \RR$ is
defined as:

$$
\epi f \triangleq \{ (x,t) \in X \times \RR \ST x \in \dom f, f(x) \leq t \}.
$$ 
```
The epigraph lies above (and includes) the graph of a function.

```{prf:definition} Strict epigraph
:label: def-bra-strict-epigraph

The *strict epigraph* of a real valued function $f: X \to \RR$ is
defined as:

$$
\epi_s f \triangleq \{ (x,t) \in X \times \RR \ST x \in \dom f, f(x) < t \}.
$$ 
```
The strict epigraph lies above the graph of a function.


```{prf:theorem} Epigraph of pointwise maximum of two functions
:label: res-bra-epigraph-intersection


Let $f, g : X \to \RR$ be two different real valued functions.
Let $h : X \to \RR$ with $\dom h = \dom f \cap \dom g$  be defined as

$$
h(x) = \max(f(x), g(x)) \Forall x \in \dom h
$$

Then

$$
\epi h = \epi f \cap \epi g.
$$
```

```{prf:proof}

We first show that $\epi h \subseteq \epi f \cap \epi g$.

1. Let $(x, t) \in \epi h$.
1. Then $x \in \dom h$ and $h(x) \leq t$.
1. Hence $x \in \dom f$, $x \in \dom g$, $f(x) \leq t$ and $g(x) \leq t$.
1. Hence $(x,t) \in \epi f$ and $(x, t) \in \epi g$.
1. Hence $(x, t) \in \epi f \cap \epi g$.


For the converse, we show that  $\epi f \cap \epi g \subseteq \epi h$.

1. Let $(x, t) \in \epi f \cap \epi g$.
1. Then $(x, t) \in \epi f$ and $(x, t) \in \epi g$.
1. Thus $x \in \dom f$, $f(x) \leq t$, $x \in \dom g$ and $g(x) \leq t$.
1. Thus $x \in \dom f \cap \dom g = \dom h$.
1. Also, $h(x) = \max(f(x), g(x)) \leq t$.
1. Hence $(x, t) \in \epi h$.
```

This result can be generalized for an arbitrary family of functions.

```{prf:theorem} Epigraph of pointwise maximum of a family of functions
:label: res-bra-epigraph-intersection-family


Let $\{ f_i : X \to \RR \}_{i \in I}$ be a family of real valued functions
indexed by $I$.
Let $h : X \to \RR$ with $\dom h = \bigcap_{i \in I} \dom f_i$  be defined as

$$
h(x) = \max \{f_i(x) \ST i \in I \} \Forall x \in \dom h
$$

Then

$$
\epi h = \bigcap_{i \in I}  \epi f_i.
$$
```

```{prf:proof}
We first show that $\epi h \subseteq \bigcap_{i \in I}  \epi f_i$.

1. Let $(x, t) \in \epi h$.
1. Then $x \in \dom h$ and $h(x) \leq t$.
1. Hence $x \in \dom f_i$  and $f_i(x) \leq t$ for every $i  \in I$.
1. Hence $(x,t) \in \epi f_i$ for every $i \in I$.
1. Hence $(x, t) \in  \bigcap_{i \in I}   \epi f_i$.

The argument for the converse is similar and left as an exercise.
```


## Sub-level Sets

```{prf:definition} Sub-level set
:label: def-bra-sub-level-set

For a real valued function $f: X \to \RR$, the sublevel set
for some $\alpha \in \RR$,
denoted by $\sublevel(f, \alpha)$,
is defined as 

$$
\sublevel(f, \alpha) \triangleq \{ x \in \dom f \,|\, f(x) \leq \alpha \}.
$$
```

## Contours or Level Sets

```{prf:definition} Contour
:label: def-bra-contour

For a real valued function $f: X \to \RR$, the contour
for some $\alpha \in \RR$,
denoted by $\contour(f, \alpha)$,
is defined as 

$$
\contour(f, \alpha) \triangleq \{ x \in \dom f \,|\, f(x) = \alpha \}.
$$
```

## Hypograph

```{prf:definition} Hypograph
:label: def-bra-hypograph

The *hypograph* of a real valued function $f: X \to \RR$ is
defined as:

$$
\hypo f \triangleq \{ (x,t) \in X \times \RR \ST x \in \dom f, t \leq f(x) \}.
$$ 
```
The epigraph lies above (and includes) the graph of a function.


## Super-level Sets

```{prf:definition} Super-level set
:label: def-bra-super-level-set

For a real valued function $f: X \to \RR$, the super-level set
for some $\alpha \in \RR$,
denoted by $\superlevel(f, \alpha)$,
is defined as 

$$
\superlevel(f, \alpha) \triangleq \{ x \in \dom f \,|\, f(x) \geq \alpha \}.
$$
```


## Extended Real Valued Functions

```{prf:definition} Extended real-valued function
:label: def-bra-extended-real-valued-function

A function over a set $X$ is called 
an *extended real-valued function* if it
can take any real value as well as the infinity values
$-\infty$ and $\infty$. 

The signature of such a function is $f : X \to \ERL$
where $\ERL = \RR \cup \{ -\infty, \infty \}$.
We also write the codomain as $\ERL = [-\infty, \infty]$.
```

```{prf:definition} Effective domain of an extended real valued function
:label: def-bra-extension-domain

For an extended valued function $\tilde{f} : X \to \ERL$, its 
*effective domain* is defined as:

$$
\dom \tilde{f} \triangleq \{ x \in X \ST \tilde{f}(x) < \infty \}.
$$
```

```{prf:definition} Graphs and level sets
:label: def-bra-extended-value-func-graphs

The epigraph, hypograph, 
sublevel, superlevel and contour sets of an extended valued
function are defined in an identical manner.
However, the graph is defined slightly differently.

$$
& \graph f \triangleq \{ (x,t) \in X \times \ERL \ST x \in \dom f, f(x) = t \};\\
& \epi f \triangleq \{ (x,t) \in X \times \RR \ST x \in \dom f, f(x) \leq t \};\\
& \epi_s f \triangleq \{ (x,t) \in X \times \RR \ST x \in \dom f, f(x) < t \};\\
& \sublevel(f, \alpha) \triangleq \{ x \in \dom f \,|\, f(x) \leq \alpha \}; \\
& \contour(f, \alpha) \triangleq \{ x \in \dom f \,|\, f(x) = \alpha \};\\
& \hypo f \triangleq \{ (x,t) \in X \times \RR \ST x \in \dom f, t \leq f(x) \};\\
& \superlevel(f, \alpha) \triangleq \{ x \in \dom f \,|\, f(x) \geq \alpha \}.
$$ 
```

```{div}
For an extended valued function, it is not necessary
that $\graph f \subseteq \epi f$.

1. If $f(x) = \infty$, then $(x, \infty) \in \graph f$.
   However, $(x, \infty) \notin \epi f$. 
   At the same time $(x, t) \notin \epi f$ for every $\RR$.
1. If $f(x) = -\infty$ then $(x, -\infty) \in \graph f$.
   However $(x, -\infty) \notin \epi f$.
   But $(x, t) \in \epi f$ for every $\RR$.
```




```{prf:definition} Extended-value extension
:label: def-bra-extended-value-extension

Let $f: X \to \RR$ be a real valued (partial) function.

We define its *extended-value extension*
$\tilde{f} : X \to \ERL$ as

$$
    \tilde{f}(x) \triangleq \begin{cases} 
     f(x) & \text{for} & x \in \dom f \\
    \infty & \text{for} & x \notin \dom f
    \end{cases}
$$
```

The extension is pretty useful in analysis and optimization
as it extends the domain to the whole of $X$.




```{prf:definition} Indicator functions
:label: def-bra-indicator-function

Let $C$ be a subset of $X$. We define the
*indicator function* for $C$ as:

$$
I_C(x) = 0 \Forall x \in C.
$$

By definition: $\dom I_C = C$.

We can create an extended value extension of $I_C$ as:

$$
\tilde{I}_C(x) \triangleq \begin{cases}
0 & x \in C \\
\infty & x \notin C.
\end{cases}
$$
```

