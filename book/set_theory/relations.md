# Relations

Relations on a set $X$ are subsets of the Cartesian product
of $X$ with itself. General Cartesian products are 
formally defined {prf:ref}`later <def-st-cartesian-product>`.

For now, we will define the product $X \times X$ as follows:

$$
X \times X = \{ (a, b) \ST a \in X \text{ and } b \in X \}.
$$
In other words, $X \times X$ is the collection of all possible 
ordered pairs of elements of $X$.

````{prf:definition} Binary relation
:label: def-st-binary-relation

A *binary relation* on a set $X$ is defined as a subset $\mathcal{R}$ of
$X \times X$.

If $(x,y) \in \mathcal{R}$ then $x$ is said to be in relation $\mathcal{R}$
with $y$. This is denoted by $x \mathcal{R} y$.
````

##  Equivalence Relations

The most interesting relations are equivalence relations.

````{prf:definition}  Equivalence relation
:label: def-st-equivalence-relation

A relation $\mathcal{R}$ on a set $X$ is said to be an
*equivalence relation* if it satisfies the following properties:

*  $x \mathcal{R} x$ for each $x \in X$ (*reflexivity*).
*  If $x \mathcal{R} y$ then $y \mathcal{R} x$ (*symmetry*).
*  If $x \mathcal{R} y$ and $y \mathcal{R} z$ then $x \mathcal{R} z$ (*transitivity*).
````

We can now introduce equivalence classes on a set.

````{prf:definition}  Equivalence class
:label: def-st-equivalence-class

Let $\mathcal{R}$ be an equivalence relation on a set $X$. Then the
*equivalence class* determined by the element $x \in X$ is
denoted by $[x]$ and is defined as

$$
    [x]  = \{ y \in X : x \mathcal{R} y\}
$$

i.e. all elements in $X$ which are related to $x$.
````

We can now look at some properties of equivalence classes and relations.

````{prf:proposition}
Any two equivalence classes are either disjoint or else they coincide.
````

````{prf:example} Equivalent classes
Let $X$ bet the set of integers $\ZZ$. Let $\mathcal{R}$ be defined as

$$
    x \mathcal{R} y \iff 2 \mid (x-y)
$$

i.e. $x$ and $y$ are related if the difference of $x$ and $y$ given by
$x-y$ is divisible by $2$.

Clearly, the set of odd integers and the set of even integers forms two
disjoint equivalent classes.
````



````{prf:proposition}
Let $\mathcal{R}$ be an equivalence relation on a set $X$.
Since $x \in [x]$ for each $x \in X$, there exists a family
$\{A_i\}_{i \in I}$ of pairwise disjoint sets (a family of
equivalence classes) such that $X = \cup_{i \in I} A_i$.
````

````{prf:definition} Partition
:label: def-st-partition

If a set $X$ can be represented as a union of a family $\{A_i\}_{i \in I}$ of
pairwise disjoint sets i.e.

$$
    X  = \cup_{i \in I} A_i
$$

then we say that $\{A_i\}_{i \in I}$ is a *partition* of
$X$.

````

A partition over a set $X$ also defines an equivalence relation on it.



````{prf:proposition}
If there exists a family
$\{A_i\}_{i \in I}$ of pairwise disjoint sets which partitions
a set $X$, (i.e. $X = \cup_{i \in I} A_i $), then by letting

$$
    \mathcal{R} = \{(x,y) \in X \times X \ST \exists \; i \in I \text{ such that } x, y \in A_i\}
$$

an equivalence relation is defined on $X$ whose equivalence classes
are precisely the sets $A_i$.
````

In words, the relation $\mathcal{R}$ includes only those tuples $(x,y)$
from the Cartesian product $X\times X$ for which there exists one
set $A_i$ in the family of sets $\{A_i\}$ such that both $x$ and $y$ belong to $A_i$.


## Order

Another important type of relation is an order relation.

````{prf:definition} Partial order
:label: def-st-partial-order

A relation, denoted by $\leq$, on a set $X$ is said to be a
*partial order* for $X$ (or that $X$ is partially ordered by $\leq$)
if it satisfies the following properties:

*  $x \leq x$ holds for every $x \in X$ (reflexivity).
*  If $x \leq y$ and $y \leq x$, then $x = y$ (antisymmetry).
*  If $x \leq y$ and $y \leq z$, then $x \leq z$ (transitivity).
````

An alternative notation for $x \leq y$ is $y \geq x$.

````{prf:definition} Partially ordered set
:label: def-st-partially-ordered-set

A set equipped with a partial order is known as a *partially ordered set*
(a.k.a *poset*).
````

````{prf:example} Partially ordered set
Consider a set $A = \{1,2,3\}$.  Consider the power set of $A$ which is

$$
    X = \{\EmptySet, \{1\}, \{2\}, \{3\}, \{1,2\} , \{2,3\} , \{1,3\}, \{1,2,3\} \}.
$$

Define a relation $\mathcal{R}$ on $X$ such that $x \mathcal{R} y$ if
$x \subseteq y$.

Clearly

*  $x \subseteq x \quad \forall x \in X$.
*  If $x \subseteq y$ and $y \subseteq x$ then $x =y$.
*  If $x \subseteq y$ and $y \subseteq z$ then $x \subseteq y$.

Thus the relation $\mathcal{R}$ defines a partial order on the power set $X$.
````


We can look at how elements are ordered within a set a bit more closely.

````{prf:definition} Chain
:label: def-st-chain

A subset $Y$ of a partially ordered set $X$
is called a *chain* if for every $x, y \in Y$
either $x \leq y$ or $y \leq x$ holds.

A chain is also known as a *totally ordered set*.
````

*  In a partially ordered set $X$, we don't require that 
for every $x,y \in X$, either $x \leq y$ or $ y \leq x$ should
hold. Thus there could be elements which are not connected by
the order relation.
*  In a totally ordered set $Y$, for every $x,y \in Y$ we
require that either $x \leq y$ or $y \leq x$ holds.
*  If a set is totally ordered, then it is partially ordered also.

````{prf:example} Chain
Continuing from previous example consider a subset $Y$ of $X$ defined by

$$
    Y = \{\EmptySet, \{1\}, \{1,2\}, \{1,2,3\} \}.
$$

Clearly, for every $x, y \in Y$, either $x \subseteq y$ or $y \subseteq x$ holds.

Hence $Y$ is a chain or a totally ordered set within $X$.
````


````{prf:example} More ordered sets

*  The set of natural numbers $\Nat$ is totally ordered.
*  The set of integers $\ZZ$ is totally ordered.
*  The set of real numbers $\RR$ is totally ordered.
*  Suppose we define an order relation in the set of complex numbers
   as follows. Let $x+jy$ and $u+jv$  be two complex numbers. We say that

   $$
   x+jy \leq u+jv \iff  x \leq u  \text{ and } y \leq v.
   $$
   With this definition, the set of complex numbers $\CC$ is partially ordered.
*  $\RR$ is a totally ordered subset of $\CC$ since the imaginary component
is 0 for all real numbers in the complex plane.
*  In fact, any line or a ray or a line segment
in the complex plane represents a totally ordered
set in the complex plane.
````


### Upper Bounds

We can now define the notion of upper bounds in a partially ordered set.

````{prf:definition} Upper bound
:label: def-st-upper-bound

If $Y$ is a subset of a partially ordered set $X$ such that
$y \leq u$ holds for all $y \in Y$ and for some $u \in X$, then
$u$ is called an *upper bound* of $Y$.
````

Note that there can be more than one upper bounds of $Y$. Upper bound
is not required to be unique.

````{prf:definition} Maximal element
:label: def-st-maximal-element

An element $m \in X$ is called a *maximal element* whenever
the relation $m \leq x$ implies $x = m$.

````

This means that there is no other element in $X$ which is greater than
$m$. 

A maximal element need not be unique. A partially ordered set may 
contain more than one maximal element.


````{prf:example} Maximal elements
Consider the following set

$$
    Z = \{\EmptySet, \{1\}, \{2\}, \{3\}, \{1,2\} , \{2,3\} , \{1,3\} \}.
$$

The set is partially ordered w.r.t. the relation $\subseteq$.

There are three maximal elements in this set namely $\{1,2\} , \{2,3\} , \{1,3\}$.
````


````{prf:example} Ordered sets without a maximal element

*  The set of natural numbers $\Nat$ has no maximal element.

````


What are the conditions under which a maximal element is guaranteed
in a partially ordered set $X$? 


Following statement known as 
Zorn's lemma guarantees the existence of maximal elements in
certain partially ordered sets.

````{prf:proposition}
If a {prf:ref}`chain <def-st-chain>` in a partially
ordered set $X$ has an upper bound in $X$, then $X$
has a maximal element.
````

### Lower Bounds

Following is corresponding notion of lower bounds.

````{prf:definition} Lower bound
:label: def-st-lower-bound

If $Y$ is a subset of a partially ordered set $X$ such that
$u \leq y$ holds for all $y \in Y$ and for some $u \in X$, then
$u$ is called an *lower bound* of $Y$.
````


````{prf:definition} Minimal element
:label: def-st-minimal-element

An element $m \in X$ is called a *minimal element* whenever
the relation $x \leq m$ implies $x = m$.
````

As before there can be more than one minimal elements in a set.

