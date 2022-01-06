# Real Valued Functions and Extensions


## Real Valued Functions


```{prf:definition} Real valued function
:label: def-bra-real-valued-function

A (partial) *real valued function* is a function whose values are real numbers.
Let $X$ be a set. Then $f : X \to \RR$ is a real valued function
from $X$ to $\RR$.

The set $\FFF (X, \RR)$ denotes the set of all real valued functions
from $X$ to $\RR$.
```


```{prf:definition} The vector space of real valued functions
:label: def-bra-real-valued-function-vector-space

The set $\FFF (X, \RR)$ can be turned into a vector space
over the field $\RR$ with the following operations.

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
f g: x \mapsto f(x) g(x) \text{ with } \dom f g = \dom f \cap \dom g
$$


For *total functions*:

$$
\dom f + g = \dom \bzero = \dom cf = \dom f g = \dom f = \dom g  = X.
$$
```

```{prf:definition} Partial order on real valued functions
Since $\RR$ is ordered, hence a partial order can be defined
on $\FFF (X, \RR)$.

We say that 

$$
f \preceq g \iff f(x) \leq g(x) \Forall x \in \dom f \cap \dom g.
$$

For total functions:

$$
f \preceq g \iff f(x) \leq g(x) \Forall x \in X.
$$
```

```{prf:definition} Bounded function
:label: def-bra-bounded-function

A real valued function $f:X \to \RR$ is called *bounded*
if there exists a number $M \geq 0$ (depending on $f$) 
such that 

$$
| f(x)| \leq M \Forall x \in \dom f.
$$

A function which is not bounded is called *unbounded*.

$f$ is called *bounded from above* by $a \in \RR$ if:

$$
f(x) \leq a \Forall x \in \dom f.
$$

$f$ is called *bounded from below* by $b \in \RR$ if:

$$
b \leq f(x) \Forall x \in \dom f.
$$
```

```{prf:proposition}
A real valued function is bounded if and only if
it is bounded from above as well as below.
```

## See also

1. The set of bounded (total) functions can be turned into
   a metric space. 
   See {prf:ref}`ex-ms-bounded-functions-metric-space`. 