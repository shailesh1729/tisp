# Sets

In this section we will review basic concepts of set theory. 

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


````{prf:definition} Singleton set
:label: def-singleton-set

A set with only one element is known as a *singleton* set.
````


````{prf:definition} Set equality
:label: def-equal-sets

Two sets $A$ and $B$ are said to be equal ($A=B$) if they have precisely the same elements. i.e.
if $x \in A$ then $x \in B$ and vice versa. Otherwise, they are not equal ($A \neq B$).
````

````{prf:definition} Subset
:label: def-subset

A set $A$ is called a *subset* of another set $B$ if every element of $A$ belongs to $B$.
This is denoted as $A \subseteq B$. Formally $A \subseteq B \iff (x \in A \implies x \in B)$.
````

````{prf:remark}
:label: rem-set-subset-equal

$A = B \iff (A \subseteq B \text{ and } B \subseteq A)$.
````

````{prf:definition} Proper subset
:label: def-proper-subset

If $A \subseteq B$ and $A \neq B$ then $A$ is called a *proper subset* of $B$ denoted by $A \subset B$.
````

````{prf:definition} Empty set
:label: def-empty-set

A set without any elements is called the *empty* or *void* set. It is denoted by $\EmptySet$.
````

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

````{prf:definition} Disjoint sets
:label: def-disjoint-sets

$A$ and $B$ are called *disjoint* if $A \cap B = \EmptySet$.
````


Some useful identities


*  $(A \cup B) \cap C = (A \cup C) \cap (B \cup C)$.
*  $(A \cap B) \cup C = (A \cap C) \cup (B \cap C)$.
*  $(A \cup B) \setminus C = (A \setminus C) \cap (B \setminus C)$.
*  $(A \cap B) \setminus C = (A \setminus C) \cap (B \setminus C)$.


````{prf:definition} Symmetric difference
:label: def-symmetric-difference

*Symmetric difference* between sets $A$ and $B$ is defined as

$$
        A \Delta B = ( A \setminus B) \cup (B \setminus A)
$$

i.e. the elements which are in $A$ but not in $B$ and the elements which are in $B$ but not in $A$.
````


## Family of sets

````{prf:definition} Family of sets
:label: def-set-family

A *Family of sets* is a nonempty set $\mathcal{F}$ whose members are sets by themselves.
````

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
If $\mathcal{F}$ is a family of sets, 
then by letting $I=\mathcal{F}$ and 
$A_i = i \quad \forall i \in I$,
we can express $\mathcal{F}$ in the form of 
$\{ A_i\}_{i \in I}$.

In other words, a family of sets can index itself. 
````

````{prf:definition} Union of families of sets
:label: def-union-family-of-sets

Let $\{ A_i\}_{i \in I}$ be a family of sets. The *union* of the family is defined to be

$$
\bigcup_{i\in I} A_i = \{ x \ST \exists i \in I \text{ such that } x \in A_i\}.
$$

In words, every element of the union exists in one of the members of the family.
````

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
$$
        &\left ( \bigcup_{i\in I} A_i \right ) \cap B = \bigcup_{i\in I}  \left ( A_i \cap B \right )\\
        &\left ( \bigcap_{i\in I} A_i \right ) \cup B = \bigcap_{i\in I}  \left ( A_i \cup B \right )
$$
````


````{prf:definition} Family of pairwise disjoint sets
:label: def-pairwise-disjoint-sets

A family of sets $\{ A_i\}_{i \in I}$ is called *pairwise disjoint* 
if for each pair $i, j \in I$
the sets $A_i$ and $A_j$  are disjoint i.e. $A_i \cap A_j = \EmptySet$.
````

````{prf:definition} Power set
:label: def-power-set

The set of all subsets of a set $A$ is called its *power set* and is denoted by
$\Power (A)$.
````

In the following $X$ is a big fixed set (sort of a frame of reference) and 
we will be considering different subsets of it.

````{prf:remark}
Let $X$ be a fixed set. If $P(x)$ is a property well defined for all $x \in X$, then
the set of all $x$ for which $P(x)$ is true is denoted by $\{x \in X \ST P(x)\}$.
````

````{prf:definition} Complement of a set
:label: def-complement-set

Let $A$ be a set. Its *complement* w.r.t. a fixed set $X$ is the set  $A^c = X \setminus A$.
````

```{prf:proposition}
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
