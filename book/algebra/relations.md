# Relations

Relations {cite}`wiki:relation` between two sets $X$ and $Y$ are subsets of 
the Cartesian product of two sets $X \times Y$. 

Relations on a set $X$ are subsets of the Cartesian
product $X \times X$. We recall:

$$
X \times X = \{ (a, b) \ST a \in X \text{ and } b \in X \}.
$$
In other words, $X \times X$ is the collection of all possible 
ordered pairs of elements of $X$.

```{index} Relation; binary
```
````{prf:definition} Binary relation
:label: def-st-binary-relation

Given sets $X$ and $Y$, a *binary relation* over sets $X$ and $Y$
is defined as a subset $\RRR$ of the Cartesian product $X \times Y$.

If $(x,y) \in \RRR$ then $x$ is said to be in relation $\RRR$
with $y$. This is denoted by $x \RRR y$.

$X$ is called the *domain* or set of departure of $\RRR$ and 
$Y$ is called the *codomain* or set of destination of $\RRR$.

A *binary relation* on a set $X$ is defined as a subset of
$X \times X$. It is also known as a *homogeneous relation*.

When $X \neq Y$, then the relation is called a *heterogeneous relation*.
````

## Types of relations

```{index} Relation; injective
```
```{prf:definition} Injective relation
:label: def-st-injective-relation

A relation $\RRR : X \to Y$ is called *injective* if $x \RRR y$ 
and $z \RRR y$ implies $x = z$. In other words, for each
$y \in Y$, there is at-most one $x \in X$ such that $x \RRR y$. 
```

If $X$ is the set of men, $Y$ is the set of women
and $\RRR$ is the relation of marriage, then 
we are saying that each woman can have at most one husband.

A man may have multiple wives. 
Some men or women may be unmarried too.

```{index} Relation; functional
```
```{prf:definition} Functional relation
:label: def-st-functional-relation

A relation $\RRR : X \to Y$ is called *functional* if $x \RRR y$ 
and $x \RRR z$ implies $y = z$. In other words, for each
$x \in X$, there is at-most one $y \in Y$ such that $x \RRR y$. 
Such binary relations are also called *partial functions*.
```

We are saying that each man can have at most one wife.

A woman may have multiple husbands. 
Some men or women may be unmarried too.

```{index} Relation; one-to-one
```
```{prf:definition} One-to-one relation
:label: def-st-one-one-relation

A relation is called *one-to-one* if it is injective and functional.
```

We are saying that each woman can have at most one husband
and each man can have at most one wife.

Some men or women may still be unmarried.

```{index} Relation; one-to-many
```
```{prf:definition} One-to-many relation
:label: def-st-one-many-relation

A relation is called *one-to-many* if it is injective but not functional.
```

While each woman has at most one husband, there are some men who 
have multiple wives. 

Some men or women may still be unmarried.

```{index} Relation; many-to-one
```
```{prf:definition} Many-to-one relation
:label: def-st-many-one-relation

A relation is called *many-to-one* if it is functional but not injective.
```

While each man can have at most one wife, there are women 
who have multiple husbands.

Some men or women may still be unmarried.

```{index} Relation; many-to-many
```
```{prf:definition} Many-to-many relation
:label: def-st-many-many-relation

A relation is called *many-to-many* if it is neither injective nor functional.
```

No spouse, one spouse, multiple spouses, all are permitted.

```{index} Relation; serial
```
```{prf:definition} Serial relation
:label: def-st-serial-relation

A relation  $\RRR : X \to Y$ is called *serial* if for every
$x \in X$ there exists at least one $y\in Y$ such that $x \RRR y$.
```

Every man has at least one wife.

Some women may still be unmarried. 

```{index} Relation; surjective
```
```{prf:definition} Surjective relation
:label: def-st-surjective-relation

A relation  $\RRR : X \to Y$ is called *surjective* if for every
$y \in Y$ there exists at least one $x\in X$ such that $x \RRR y$.
```

Every woman has at least one husband.

Some men may still be unmarried.

## Operations on Relations

Let $R$ and $S$ be relations over sets $X$ and $Y$.

```{index} Relation; union
```
```{prf:definition} Union of relations
:label: def-st-relation-union

$$
R \cup S = \{(x, y) \ST x R y \text{ or } x S y\}.
$$
```

```{index} Relation; intersection
```
```{prf:definition} Intersection of relations
:label: def-st-relation-intersection

$$
R \cap S = \{(x, y) \ST x R y \text{ and } x S y\}.
$$
```

```{index} Relation; composition
```
```{prf:definition} Composition of relations
:label: def-st-relation-composition

Let $R : X \to Y$ and $S : Y \to Z$ be two relations. Then,
there composition is defined as:

$$
S \circ R \triangleq \{ (x,z) \in X \times Z \ST \text{ there exists } y \in Y 
\text{ such that } x R y \text{ and } y R z \}.
$$
```

##  Equivalence Relations

An interesting type of relations are equivalence relations over a set $X$.

```{index} Equivalence relation
```
````{prf:definition}  Equivalence relation
:label: def-st-equivalence-relation

A relation $\mathcal{R}$ on a set $X$ is said to be an
*equivalence relation* if it satisfies the following properties:

*  $x \mathcal{R} x$ for each $x \in X$ (*reflexivity*).
*  If $x \mathcal{R} y$ then $y \mathcal{R} x$ (*symmetry*).
*  If $x \mathcal{R} y$ and $y \mathcal{R} z$ then $x \mathcal{R} z$ (*transitivity*).
````

We can now introduce equivalence classes on a set.

```{index} Equivalence class
```
````{prf:definition}  Equivalence class
:label: def-st-equivalence-class

Let $\mathcal{R}$ be an equivalence relation on a set $X$. Then the
*equivalence class* determined by the element $x \in X$ is
denoted by $[x]$ and is defined as

$$
    [x]  = \{ y \in X \ST x \mathcal{R} y\}
$$

i.e. all elements in $X$ which are related to $x$.
````

We can now look at some properties of equivalence classes and relations.

````{prf:proposition}
:label: res-st-eq-class-identical-disjoint

Any two equivalence classes are either disjoint or else they coincide.
````

````{prf:example} Equivalent classes
:label: ex-st-eq-class-1

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
:label: res-st-family-eq-classes-union-set

Let $\mathcal{R}$ be an equivalence relation on a set $X$.
Since $x \in [x]$ for each $x \in X$, there exists a family
$\{A_i\}_{i \in I}$ of pairwise disjoint sets (a family of
equivalence classes) such that $X = \cup_{i \in I} A_i$.
````

```{index} Set partition
```
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
:label: res-st-partition-induces-eq-class-relation

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

Another important type of relation is an order relation over a set $X$.

```{index} Partial order
```
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

```{index} Partially ordered set
```
````{prf:definition} Partially ordered set
:label: def-st-partially-ordered-set

A set equipped with a partial order is known as a *partially ordered set*
(a.k.a *poset*).
````

````{prf:example} Partially ordered set
:label: ex-st-poset-1

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

```{index} Chain
```
````{prf:definition} Chain
:label: def-st-chain

A subset $Y$ of a partially ordered set $X$
is called a *chain* if for every $x, y \in Y$
either $x \leq y$ or $y \leq x$ holds.

A chain is also known as *totally ordered*.
````

*  In a partially ordered set $X$, we don't require that 
for every $x,y \in X$, either $x \leq y$ or $ y \leq x$ should
hold. Thus there could be elements which are not connected by
the order relation.
*  In a totally ordered set $Y$, for every $x,y \in Y$ we
require that either $x \leq y$ or $y \leq x$ holds.
*  If a set is totally ordered, then it is partially ordered also.

````{prf:example} Chain
:label: ex-st-poset-chain

Continuing from previous example consider a subset $Y$ of $X$ defined by

$$
    Y = \{\EmptySet, \{1\}, \{1,2\}, \{1,2,3\} \}.
$$

Clearly, for every $x, y \in Y$, either $x \subseteq y$ or $y \subseteq x$ holds.

Hence $Y$ is a chain or a totally ordered set within $X$.
````


```{index} Total order
```
```{prf:definition} Total order
:label: def-st-total-order

A relation, denoted by $\leq$, on a set $X$ is said to be a
*total order* for $X$ (or that $X$ is totally ordered by $\leq$)
if it satisfies the following properties:

*  $x \leq x$ holds for every $x \in X$ (reflexivity).
*  If $x \leq y$ and $y \leq x$, then $x = y$ (antisymmetry).
*  If $x \leq y$ and $y \leq z$, then $x \leq z$ (transitivity).
*  $x \leq y$ or $y \leq x$ holds for every $x, y \in X$ (strongly connected).
```

```{index} Totally ordered set
```
```{prf:definition} Totally ordered set
:label: def-st-totally-ordered-set

A set equipped with a total order is known as a *totally ordered set*.
```


````{prf:example} More ordered sets
:label: ex-st-ordered-sets-2

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

```{index} Partial order; upper bound
```
````{prf:definition} Upper bound
:label: def-st-upper-bound

If $Y$ is a subset of a partially ordered set $X$ such that
$y \leq u$ holds for all $y \in Y$ and for some $u \in X$, then
$u$ is called an *upper bound* of $Y$.
````

Note that there can be more than one upper bounds of $Y$. Upper bound
is not required to be unique.

```{index} Partial order; maximal element
```
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
:label: ex-st-maximal-elements-1

Consider the following set

$$
    Z = \{\EmptySet, \{1\}, \{2\}, \{3\}, \{1,2\} , \{2,3\} , \{1,3\} \}.
$$

The set is partially ordered w.r.t. the relation $\subseteq$.

There are three maximal elements in this set namely $\{1,2\} , \{2,3\} , \{1,3\}$.
````


````{prf:example} Ordered sets without a maximal element
:label: ex-st-ordered-set-no-max-element

*  The set of natural numbers $\Nat$ has no maximal element.

````


What are the conditions under which a maximal element is guaranteed
in a partially ordered set $X$? 


Following statement known as 
Zorn's lemma guarantees the existence of maximal elements in
certain partially ordered sets.

````{prf:proposition}
:label: res-st-chain-upper-bound-implies-max-element

If a {prf:ref}`chain <def-st-chain>` in a partially
ordered set $X$ has an upper bound in $X$, then $X$
has a maximal element.
````

### Lower Bounds

Following is corresponding notion of lower bounds.

```{index} Partial order; lower bound
```
````{prf:definition} Lower bound
:label: def-st-lower-bound

If $Y$ is a subset of a partially ordered set $X$ such that
$u \leq y$ holds for all $y \in Y$ and for some $u \in X$, then
$u$ is called an *lower bound* of $Y$.
````


```{index} Partial order; minimal element
```
````{prf:definition} Minimal element
:label: def-st-minimal-element

An element $m \in X$ is called a *minimal element* whenever
the relation $x \leq m$ implies $x = m$.
````

As before there can be more than one minimal elements in a set.

