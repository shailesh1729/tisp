# Sets

In this section we will review basic concepts of set theory. 

```{index} Set
```
````{prf:definition} Set
:label: def-set

A *set* is a collection of objects viewed as a single entity.
````

It is just a working definition which we will use in this book.



*  Sets are denoted by capital letters. 
*  Objects in a set are called *members*, *elements* or *points*. 
*  $x \in A$ means that element $x$ belongs to set $A$.
*  $x \notin A$ means that $x$ doesn't belong to set $A$.
*  $\{ a,b,c\}$ denotes a set with elements $a$, $b$, and $c$. Their order 
    is not relevant.
* $\{ x \ST  \text{property}(x) \}$ is a set of elements which satisfy a given property
  (a predicate or a condition or a rule).


```{index} Set; singleton
```
````{prf:definition} Singleton set
:label: def-singleton-set

A set with only one element is known as a *singleton* set.
````


```{index} Set; equality
```
````{prf:definition} Set equality
:label: def-equal-sets

Two sets $A$ and $B$ are said to be equal ($A=B$) if they have precisely the same elements. i.e.
if $x \in A$ then $x \in B$ and vice versa. Otherwise, they are not equal ($A \neq B$).
````

```{index} Subset
```
````{prf:definition} Subset
:label: def-subset

A set $A$ is called a *subset* of another set $B$ if every element of $A$ belongs to $B$.
This is denoted as $A \subseteq B$. Formally $A \subseteq B \iff (x \in A \implies x \in B)$.
````

````{prf:remark}
:label: rem-set-subset-equal

$A = B \iff (A \subseteq B \text{ and } B \subseteq A)$.
````

```{index} Subset; proper
```
````{prf:definition} Proper subset
:label: def-proper-subset

If $A \subseteq B$ and $A \neq B$ then $A$ is called a *proper subset* of $B$ denoted by $A \subset B$.
````

```{index} Set; empty
```
````{prf:definition} Empty set
:label: def-empty-set

A set without any elements is called the *empty* or *void* set. It is denoted by $\EmptySet$.
````

```{index} Set; operations
```
````{prf:definition} Set operations
:label: def-set-operations

We define fundamental set operations below

*  The *union* $A \cup B$ of $A$ and $B$ is defined as

$$
            A \cup B  = \{ x \ST x \in A \text{ or } x \in B\}.
$$

*  The *intersection* $A \cap B$ of $A$ and $B$ is defined as

$$
            A \cap B  = \{ x \ST x \in A \text{ and } x \in B\}.
$$

*  The *difference* $A \setminus B$ of $A$ and $B$ is defined as

$$
            A \setminus B  = \{ x \ST x \in A \text{ and } x \notin B\}.
$$
````

```{index} Set; disjoint
```
````{prf:definition} Disjoint sets
:label: def-disjoint-sets

$A$ and $B$ are called *disjoint* if $A \cap B = \EmptySet$.
````


Some useful identities


*  $(A \cup B) \cap C = (A \cup C) \cap (B \cup C)$.
*  $(A \cap B) \cup C = (A \cap C) \cup (B \cap C)$.
*  $(A \cup B) \setminus C = (A \setminus C) \cap (B \setminus C)$.
*  $(A \cap B) \setminus C = (A \setminus C) \cap (B \setminus C)$.


```{index} Set; symmetric difference
```
````{prf:definition} Symmetric difference
:label: def-symmetric-difference

*Symmetric difference* between sets $A$ and $B$ is defined as

$$
        A \Delta B = ( A \setminus B) \cup (B \setminus A)
$$

i.e. the elements which are in $A$ but not in $B$ and the elements which are in $B$ but not in $A$.
````


## Family of sets

```{index} Family of sets
```
````{prf:definition} Family of sets
:label: def-set-family

A *Family of sets* is a nonempty set $\mathcal{F}$ whose members are sets by themselves.
````

```{index} Family of sets; index set
```
````{prf:definition} Families indexed by an index set
:label: def-index-set

If for each element $i$ of a non-empty set $I$, 
a subset $A_i$ of a fixed set $X$ is assigned,
then $\{ A_i\}_{i \in I}$ ( or $\{ A_i \ST i \in I\}$ or simply $\{A_i\}$
denotes the family whose members are the sets
$A_i$. 
The set $I$ is called the *index set* of the family and 
its members are known as *indices*.
````


````{prf:example} Index sets
:label: ex-index-sets

Following are some examples of index sets

*  $\{1,2,3,4\}$: the family consists of only 4 sets.
*  $\{0,1,2,3\}$: the family consists again of only 4 sets but indices are different.
*  $\Nat$: The sets in family are indexed by natural numbers. They are
countably infinite.
*  $\ZZ$: The sets in family are indexed by integers. They are countably
infinite.
*  $\QQ$: The sets in family are indexed by rational numbers. They are
countably infinite.
*  $\RR$: There are uncountably infinite sets in the family.
````

````{prf:remark}
:label: rem-st-indexing-family-self

If $\mathcal{F}$ is a family of sets, 
then by letting $I=\mathcal{F}$ and 
$A_i = i \quad \forall i \in I$,
we can express $\mathcal{F}$ in the form of 
$\{ A_i\}_{i \in I}$.

In other words, a family of sets can index itself. 
````

```{index} Family of sets; union
```
````{prf:definition} Union of families of sets
:label: def-union-family-of-sets

Let $\{ A_i\}_{i \in I}$ be a family of sets. The *union* of the family is defined to be

$$
\bigcup_{i\in I} A_i = \{ x \ST \exists i \in I \text{ such that } x \in A_i\}.
$$

In words, every element of the union exists in one of the members of the family.
````

```{index} Family of sets; intersection
```
````{prf:definition} Intersection of families of sets
:label: def-intersection-family-of-sets

Let $\{ A_i\}_{i \in I}$ be a family of sets. The *intersection* of the family is defined to be

$$
\bigcap_{i \in I} A_i  = \{ x \ST x \in A_i \quad \forall i \in I\}.
$$

In words, every element of the union exists in every member of the family.
````

We will also use simpler notation $\bigcup A_i$, $\bigcap A_i$ 
for denoting the union and intersection of family.

If $I =\Nat = \{1,2,3,\dots\}$ (the set of natural numbers), 
then we will denote
union and intersection by $\bigcup_{i=1}^{\infty}A_i$ and $\bigcap_{i=1}^{\infty}A_i$.


````{prf:proposition} Generalized distributive laws
:label: res-st-generalized-distributive-laws

$$
        &\left ( \bigcup_{i\in I} A_i \right ) \cap B = \bigcup_{i\in I}  \left ( A_i \cap B \right )\\
        &\left ( \bigcap_{i\in I} A_i \right ) \cup B = \bigcap_{i\in I}  \left ( A_i \cup B \right )
$$
````


```{index} Family of sets; pairwise disjoint
```
````{prf:definition} Family of pairwise disjoint sets
:label: def-pairwise-disjoint-sets

A family of sets $\{ A_i\}_{i \in I}$ is called *pairwise disjoint* 
if for each pair $i, j \in I$
the sets $A_i$ and $A_j$  are disjoint i.e. $A_i \cap A_j = \EmptySet$.
````

```{index} Power set
```
````{prf:definition} Power set
:label: def-power-set

The set of all subsets of a set $A$ is called its *power set* and is denoted by
$\Power (A)$.
````

In the following $X$ is a big fixed set (sort of a frame of reference) and 
we will be considering different subsets of it.

````{prf:remark} The subset satisfying a property
:label: res-st-property-predicate

Let $X$ be a fixed set. If $P(x)$ is a property well defined for all $x \in X$, then
the set of all $x$ for which $P(x)$ is true is denoted by $\{x \in X \ST P(x)\}$.
````

```{index} Set; complement
```
````{prf:definition} Complement of a set
:label: def-complement-set

Let $A$ be a set. Its *complement* w.r.t. a fixed set $X$ is the set  $A^c = X \setminus A$.
````

```{prf:proposition}
:label: res-st-complement-properties

Let $X$ be a fixed set, $A, B$ be subsets of $X$ and $A^c$ denote the
complement of some subset $A$ of $X$ w.r.t. $X$.

We have the following results:

*  $(A^c)^c = A$.
*  $A \cap A^c = \EmptySet$.
*  $A \cup A^c = X$.
*  $A\setminus B = A \cap B^c$.
*  $A \subseteq B \iff B^c \subseteq A^c$.
*  $(A \cup B)^c = A^c \cap B^c$.
*  $(A \cap B)^c = A^c \cup B^c$.
```

## Ordered Pairs and n-Tuples

We will introduce the notion of *ordered pairs* informally 
following {cite}`wiki:ordered-pair`.

```{index} Ordered pair
```
```{prf:definition} Ordered pair
:label: def-st-ordered-pair

For any two objects a and b, the *ordered pair* (a, b) is a 
notation specifying the two objects a and b, in that order.
```

```{prf:property} Equality of ordered pairs
:label: res-st-ordered-pair-equality

$$
(a_1, a_2) = (b_1, b_2) \iff a_1 = b_1 \text{ and } a_2 = b_2.
$$
```

A tuple {cite}`wiki:tuple` is a finite ordered list of elements.
An n-tuple is a sequence (ordered list) of $n$ elements where 
$n$ is a non-negative integer.

* A tuple may contain multiple instances of the same element.
* Tuple elements are ordered.
* A tuple has a finite number of elements.

Following is an informal definition

```{prf:definition} n-tuple
:label: def-st-n-tuple

For any $n$ objects $a_1, a_2, \dots, a_n$ where $n \in \Nat$, the
*n-tuple* $(a_1, a_2, \dots, a_n)$ is a notation specifying the
$n$ objects in that order.

The 0-tuple $()$ is an tuple containing $0$ elements.  
```

```{prf:property} Equality of n-tuples
:label: res-st-n-tuple-equality

$$
(a_1, a_2, \dots, a_n) = (b_1, b_2, \dots, b_n) \iff a_1 = b_1, a_2 = b_2, \dots, \text{ and } a_n = b_n.
$$
```
In other words, $(a_1,\dots, a_n) = (b_1,\dots,b_n)$ if and only if
$a_i = b_i \Forall i = 1,\dots,n$.


## Cartesian Products

In this section, we restrict our
attention to finite Cartesian products.
Cartesian product over infinite sets is 
discussed later.


```{prf:definition} Binary Cartesian product
:label: def-st-binary-cartesian-product

The *Cartesian product* of the two sets $A$ and $B$ denoted
by $A \times B$ is the set of all possible ordered pairs
of elements where the first element is from $A$ and the second
is from $B$:

$$
    A \times B  \triangleq \{ (a, b) \ST a \in A \text{  and  } b \in B \}.
$$
```

```{prf:definition} Finite Cartesian product
:label: def-st-finite-cartesian-product

Similarly, the Cartesian product of a finite family of
sets $(A_1, \dots, A_n)$ is written as
$A_1 \times \dots \times A_n$ and its members are
denoted as $n$-tuples, i.e.:

$$
    A_1 \times \dots \times  A_n = \{(a_1, \dots, a_n) \ST a_i \in A_i \Forall
    i = 1,\dots,n\}.
$$

The sets $A_i$ may be same of different.
```

```{prf:remark}
:label: res-st-n-th-power-of-set

If $A_1 = A_2 = \dots = A_n = A$, then it is standard to write
$A_1 \times \dots \times A_n$ as $A^n$.
```

```{prf:example} $A^n$
:label: ex-st-a-n-1


Let $A = \{ 0, +1, -1\}$.

Then $A^2$  is

$$
    \{\\
    &(0,0), (0,+1), (0,-1),\\
    &(+1,0), (+1,+1), (+1,-1),\\
    &(-1,0), (-1,+1), (-1,-1)\\
    \}.
$$

And $A^3$ is given by

$$
     \{\\
    &(0,0,0), (0,0,+1), (0,0,-1),\\
    &(0,+1,0), (0,+1,+1), (0,+1,-1),\\
    &(0,-1,0), (0,-1,+1), (0,-1,-1),\\
    &(+1,0,0), (+1,0,+1), (+1,0,-1),\\
    &(+1,+1,0), (+1,+1,+1), (+1,+1,-1),\\
    &(+1,-1,0), (+1,-1,+1), (+1,-1,-1),\\
    &(-1,0,0), (-1,0,+1), (-1,0,-1),\\
    &(-1,+1,0), (-1,+1,+1), (-1,+1,-1),\\
    &(-1,-1,0), (-1,-1,+1), (-1,-1,-1)\\
    &\}.
$$
```

## Covers

```{prf:definition} Cover
:label: def-st-cover

A family $\{ A_i \}_{i \in I}$ of subsets of $X$ is said to *cover* a set
$A$ if

$$
A \subseteq \bigcup_{i \in I} A_i.
$$
Here $I$ is an index set indexing the sets in the family. $I$ 
could be finite, countable or uncountable.
```

```{prf:example}
:label: ex-st-cover-1

1. The family $\{[n, n+1]\}_{n \in \ZZ}$ covers $\RR$.
1. The family $\{[n-1, n]\}_{n \in \Nat}$ covers $\RR_{+}$.
1. The family $\{(n-1, n+1)\}_{n \in \Nat}$ covers $\RR_{++}$.
```

```{prf:definition} Subcover
:label: def-st-subcover

If a subfamily of a cover $\{ A_i \}_{i \in I}$  of $A$ also covers
$A$, then the subfamily is called a *subcover*.
```

* Covers play an important role in the theory of
  metric spaces. See {prf:ref}` open covers <def-ms-open-cover>`.