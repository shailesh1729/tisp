# Functions

````{prf:definition} Function
:label: def-st-function

A *partial function* (or simply *function*) 
from a set $A$ to a set $B$, in symbols $f : A \to B$ (or $A \xrightarrow{f} B$
or $x \mapsto f(x)$) is a specific *rule* that assigns 
a *unique* element $y \in B$
to an element $x \in A$.

The rule need not be defined for every element in $A$.
````

```{note}
Following {cite}`boyd2004convex`,
our definition of functions is somewhat different from the 
traditional definition. In particular, we don't require that
$f$ maps *each* element of $A$ to an element of $B$. It may 
map only some elements of $A$ to $B$. 

See also : {prf:ref}`total function <def-st-total-function>` below. 
```


````{prf:definition} Function value or image
:label: def-st-function-image

If $f$ maps an element $x \in A$ to an element $y \in B$, 
We say that the element $y$ is the *value* of the function $f$ 
at $x$ (or the *image* of $x$ under $f$) 
and denote as $f(x)$, that is, $y = f(x)$.

We also sometimes say that $y$ is the *output* of $f$ when the *input* is $x$.
````

```{prf:definition} Domain of a function
:label: def-st-function-domain

For a function $f: A \to B$ the *domain* of the
function is the subset of $A$ for which the function
is defined. It is denoted by $\dom f$.

$$
\dom f \triangleq \{x \in A \ST \exists \; y \in B \text{ such that } y = f(x) \}.
$$ 
```

```{prf:definition} Total function
:label: def-st-total-function

A function $f : A \to B$ is called a *total function* if $\dom f = A$.
```

The normal set-theoretic definition of a function coincides with the
definition of *total function* above.

```{prf:definition} Range of a function
:label: def-st-function-range

The set $\{y \in B \ST \exists \; x \in A \text{ such that } y = f(x)\}$ 
is called the *range* of $f$ denoted by $\range f$.
```

The domain is a subset of $A$ and the range is a subset of $B$.

````{prf:example} Dirichlet's unruly indicator function for rational numbers
:label: ex-st-dirichlet-unruly-indicator-function

$$
    g(x) =
     \left\{
            \begin{array}{ll}
                1 & \mbox{if $x \in \QQ$};\\
                0 & \mbox{if $x \notin \QQ$}.
            \end{array}
          \right.
$$

This function is not continuous anywhere on the real line.
````

````{prf:example} Absolute value function
:label: ex-st-absolute-value-function

$$
    | x | =
     \left\{
            \begin{array}{ll}
                x & \mbox{if $x \geq 0$};\\
                -x & \mbox{if $x < 0$}.
            \end{array}
          \right.
$$

This function is continuous but not differentiable at $x=0$.
````


````{prf:definition} Equality of functions
:label: def-st-function-equal

Two functions $f : A \to B$ and $g : A \to B$ are said to be *equal*,
in symbols $f = g$ if $\dom f = \dom g$ and
$f(x) = g(x) \quad \forall x \in \dom f$.

In words, they map the same elements of $A$ to same elements of $B$.
````

````{prf:definition} Surjective function
:label: def-st-surjective-function

A function $f : A \to B$ is called *onto* or *surjective* if $\range f$ is
all of $B$. i.e. for every $y \in B$, there exists (at least one) $x \in A$ such that
$ y = f(x)$.
````

````{prf:definition} Injective function
:label: def-st-injective-function

A function $f : A \to B$ is called *one-one* or *injective* if $x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$.
````

````{prf:definition} Bijective function
:label: def-st-bijective-function

A *total* function $f : A \to B$ is called *one-one onto* or *bijective* 
if it is injective as well as surjective.
````

For a bijective function $\dom f = A$, $\range f = B$, the elements
of $A$ and $B$ are in one-to-one mapping, hence they have same cardinality.


````{prf:definition} Image of a set under a function
:label: def-set-set-image-under-function

Let $f : X \to Y$ be  a function. 
If $A \subseteq X$, then *image* of $A$ under $f$
denoted as $f(A)$ (a subset of $Y$) is defined by

$$
f(A) = \{  y \in Y \ST \exists \; x \in A \text{ such that } y = f(x)\}.
$$
````
Note that the definition is valid even if some elements of the subset $A$
may not belong to $\dom f$.


````{prf:definition} Inverse image 
:label: def-set-set-inverse-image-under-function

If $B$ is a subset of $Y$ then the *inverse image* $f^{-1}(B)$ of $B$ under $f$
is the subset of $X$ defined by

$$
f^{-1} (B) = \{ x \in X \ST f(x) \in B\}.
$$
````

````{prf:proposition} 
Let $f : X \to Y$.
Let $\{A_i\}_{i \in I}$  be a family of subsets of $X$.
Let $\{B_i\}_{i \in I}$ be a family of subsets of $Y$.

Then the following results hold:

Image of the union of $A_i$ is the union of the images of $A_i$.

$$
    f ( \cup_{i \in I} A_i) = \cup_{i \in I} f(A_i).
$$

Image of the intersection of $A_i$ is a subset of the intersection of the images of $A_i$.

$$
    f (\cap_{i \in I} A_i) \subseteq \cap_{i \in I} f(A_i).
$$

Inverse image of the union of $B_i$ is the union of the inverse images of $B_i$.

$$
    f^{-1} (\cup_{i \in I} B_i) = \cup_{i \in I}f^{-1} (B_i).
$$

Inverse image of the intersection of $B_i$ is the intersection of the inverse images of $B_i$.

$$
    f^{-1} (\cap_{i \in I} B_i) = \cap_{i \in I}f^{-1} (B_i).
$$

Let $B \subseteq Y$. Inverse image of complement of $B$ (w.r.t. $Y$) 
is the complement of the inverse image of $B$ w.r.t. the domain of $f$.

$$
    f^{-1}(Y \setminus B) = \dom f \setminus f^{-1}(B) 
    \subseteq X \setminus f^{-1}(B).
$$
````

## Function Composition

````{prf:definition} Composition
:label: def-st-function-composition

Given two functions $f : X \to Y$ and $g : Y \to Z$, their *composition*
$g \circ f$ is the function $g \circ f : X \to Z$ defined by

$$
(g \circ f)(x) = 
g(f(x)) \quad \forall x \in \dom f \text{ such that } f(x) \in \dom g.
$$
````

```{prf:remark}

$$
\dom g \circ f \subseteq \dom f \subseteq X.
$$
```
The domain of the composition may be smaller than the domain of $f$
as $g$ may not be defined for every $y$ in $\range f$.


````{prf:theorem}
:label: res-st-composition-of-one-one-functions

Given two one-one functions $f : X \to Y$ and $g : Y \to Z$, their composition
$g \circ f$ is one-one.
````
````{prf:proof}
Let $x_1, x_2 \in \dom g \circ f$. 
We need to show that $g(f(x_1)) = g(f(x_2)) \implies x_1 = x_2$.
Since $g$ is one-one, hence 

$$ 
g(f(x_1)) = g(f(x_2)) \implies f(x_1) = f(x_2).
$$

Further, since $f$ is one-one, hence 

$$
f(x_1) = f(x_2) \implies x_1 = x_2.
$$
````

````{prf:theorem}
:label: res-st-composition-of-onto-functions

Given two onto functions $f : X \to Y$ and $g : Y \to Z$, their composition
$g \circ f$ is onto.
````

````{prf:proof}
Let $z \in Z$. We need to show that there exists $x \in X$ such that
$g(f(x)) = z$.
Since $g$ is on-to, hence for every $z \in Z$, there exists $y \in Y$
such that $z = g(y)$. Further, since $f$ is onto, for every $y \in Y$, there exists $x \in X$
such that $y = f(x)$. Combining the two, for every $z \in Z$, there exists $x \in X$ such
that $z = g(f(x))$.
````

````{prf:theorem}
:label: res-st-composition-of-one-one-onto-functions

Given two one-one onto functions $f : X \to Y$ 
and $g : Y \to Z$, their composition
$g \circ f$ is one-one onto.
````
````{prf:proof}
This is a direct result of combining 
{prf:ref}`res-st-composition-of-one-one-functions`
and {prf:ref}`res-st-composition-of-onto-functions`.
````

## Inverse Function

````{prf:definition} Inverse function
:label: def-st-inverse-function

If a function $f : X \to Y$ is one-one, then for every $y$ in $\range f$,
there exists a unique $x \in X$ such that $ y = f(x)$.  
This unique element
is denoted by $f^{-1}(y)$. 
Thus, a function $f^{-1} : Y \to X$ can be defined
by

$$
    f^{-1}(y) = x \text{ whenever } f(x) = y.
$$

The function $f^{-1}$ is called the *inverse* of $f$.
````
Note that we don't require $f$ to be *onto* since our 
definition of a function allows $\dom f^{-1}$ to be a 
subset of $Y$ (which happens to be $\range f$).

````{prf:remark}
We can see that $(f \circ f^{-1})(y) = y$ for all $ y \in \range f$.
Also $ (f^{-1} \circ f) (x) = x$ for all $ x \in \dom f$.

$$
\dom f^{-1} = \range f.
$$

$$
\dom f = \range f^{-1}.
$$
````

````{prf:definition} Inverse of a total function
:label: def-st-inverse-total-function

If a total function $f : X \to Y$ is bijective, 
then for every $y$ in $Y$,
there exists a unique $x \in X$ such that $y = f(x)$.  
This unique element
is denoted by $f^{-1}(y)$. 
Thus, a total function $f^{-1} : Y \to X$ can be defined
by

$$
    f^{-1}(y) = x \text{ whenever } f(x) = y.
$$

The total function $f^{-1}$ is called the *inverse* of $f$.
````

## Identity Function

````{prf:definition} Identity function
:label: def-st-identity-function

We define an *identity* function on a set $X$ denoted by
$I_X : X \to X$ as:

$$
I_X(x) = x \Forall x \in X
$$
````

````{prf:remark}
Identify function is one-one and onto. It is a total function
and is bijective.
````

Thus we have:

$$
        & f \circ f^{-1} = I_Y.\\
        & f^{-1} \circ f = I_X.
$$


## Schröder-Bernstein Theorem

````{prf:theorem} Schröder-Bernstein Theorem
:label: res-st-schroder-bernstein-theorem

Given two one-one {prf:ref}`total functions <def-st-total-function>` 
$f : X \to Y$ and $g : Y \to X$, there exists
a bijective total function $h : X \to Y$.
````

````{prf:proof}
Clearly, we can define a one-one onto function $f^{-1} : f(X) \to X$ and
another one-one onto function $g^{-1} : g(Y) \to Y$.
Let the two-sided sequence $C_x$ be defined as

$$
    \dots, f^{-1} (g^{-1}(x)), g^{-1}(x), x , f(x), g(f(x)), f(g(f(x))), \dots.
$$

Note that the elements in the sequence alternate between $X$ and $Y$. On
the left side, the sequence stops whenever $f^{-1}(y)$ or $g^{-1}(x)$ is not
defined. On the right side the sequence goes on infinitely.

We call the sequence as $X$ stopper if it stops at an element of $X$ or
as $Y$ stopper if it stops at an element of $Y$. If any element in the left
side repeats, then the sequence on the left will keep on repeating. We call
the sequence doubly infinite if all the elements (on the left) are distinct, or cyclic
if the elements repeat. Define $Z = X \cup Y$ If an element $z \in Z$ occurs
in two sequences, then the two sequences must be identical by definition.
Otherwise, the two sequences must be disjoint.  Thus the sequences
form a partition on $Z$. All elements within one equivalence class of $Z$
are reachable from each other through one such sequence. The elements
from different sequences are not reachable from each other at all. Thus,
we need to define bijections between elements of $X$ and $Y$ which belong
to same sequence separately.

For an $X$-stopper sequence $C$, every element $y \in C \cap Y$ is reachable from
$f$. Hence $f$ serves as the bijection between elements of $X$ and $Y$.
For an $Y$-stopper sequence $C$, every element $x \in C \cap X$ is reachable from
$g$. Hence $g$ serves as the bijection between elements of $X$ and $Y$.
For a cyclic or doubly infinite sequence $C$,
every element $y \in C \cap Y$ is reachable from $f$
and every element $x \in C \cap X$ is reachable from $g$. Thus either of $f$
and $g$ can serve as a bijection.

````






