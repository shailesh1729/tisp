# Cartesian product

## General definition

```{prf:definition} Cartesian product
:label: def-st-cartesian-product

Let $\{ A_i \}_{i \in I}$ be a family of sets. Then the
*Cartesian product* $\prod_{i \in I} A_i$ or $\prod A_i$
is defined to be the set consisting of all functions
$f : I \to \cup_{i \in I}A_i$ such that $x_i = f(i) \in A_i$
for each $i \in I$.

In other words, the function $f$ chooses an element $x_i$
from the set $A_i$ for each index $i \in I$.
```
The general definition of the Cartesian product allows the
index set to be finite, countably infinite as well as 
uncountably infinite.

Note that we didn't require $A_i$ to be non-empty. This 
is discussed below.

```{prf:definition} Choice function
:label: def-st-choice-function

A member function $f$ of the Cartesian product $\prod A_i$
is called a *choice function* and
often denoted by $(x_i)_{i \in I}$ or simply by $(x_i)$.
```

```{prf:remark}
For a family $\{A_i\}_{i \in I}$,  if any of the $A_i$ is empty, then
the Cartesian product $\prod A_i$ is empty.
```
This follows from the definition of the Cartesian product
as a choice function $f$ must choose an element from each $A_i$.
If an $A_i$ is empty, a choice function cannot choose any element
from it, hence the choice function cannot exist.

```{prf:remark}
If the family of sets $\{A_i\}_{i \in I}$ satisfies $A_i = A \Forall i \in I$,
then $\prod_{i \in I} A_i$ is written as $A^I$.

$$
    A^I = \{ f | f : I \to A\}.
$$

i.e. $A^I$ is the set of all functions from $I$ to $A$.
```


## Finite cases

```{prf:definition} Binary Cartesian product
:label: def-st-binary-cartesian-product

If a family consists of two sets, say $A$ and $B$, then
the *Cartesian product* of the sets $A$ and $B$ is denoted
by $A \times B$.  The members of $A \times B$ are denoted
as *ordered pairs*:

$$
    A \times B  = \{ (a, b) \ST a \in A \text{  and  } b \in B \}.
$$
```

```{prf:definition} Finite Cartesian product
:label: def-st-finite-cartesian-product

Similarly, the Cartesian product of a finite family of
sets $\{ A_1, \dots, A_n\}$ is written as
$A_1 \times \dots \times A_n$ and its members are
denoted as $n$-tuples, i.e.:

$$
    A_1 \times \dots \times  A_n = \{(a_1, \dots, a_n) \ST a_i \in A_i \Forall
    i = 1,\dots,n\}.
$$
```

Note that $(a_1,\dots, a_n) = (b_1,\dots,b_n)$ if and only if
$a_i = b_i \Forall i = 1,\dots,n$.

```{prf:remark}
If $A_1 = A_2 = \dots = A_n = A$, then it is standard to write
$A_1 \times \dots \times A_n$ as $A^n$.
```

## Examples

```{prf:example} $A^n$

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


```{prf:example} Binary functions on the real line

Let $A = \{0, 1\}$. $A^{\RR}$ is a set of all functions on $\RR$
which can take only one of the two values $0$ or $1$.
```

```{prf:example} Binary sequences
Let $A = \{0, 1\}$. $A^{\Nat}$ is a set of all sequences of $0$s and $1$s.
```

```{prf:example} Real valued functions on the real line 

$\RR^\RR$ is a set of all functions from $\RR$ to $\RR$.
```


## Axiom of choice

If a Cartesian product is non-empty, then each $A_i$ must be non-empty. 
We can therefore ask: If each $A_i$ is non-empty, is then the 
Cartesian product $\prod A_i$ nonempty?
An affirmative answer cannot be proven within the usual axioms of set
theory.
This requires us to introduce the *axiom of choice*.

```{prf:axiom} Axiom of choice
:label: ax-st-axiom-of-choice

If $\{A_i\}_{i \in I}$ is a
nonempty family of sets such that $A_i$ is nonempty for each $i \in I$,
then the Cartesian product $\prod A_i$ is nonempty.
```
This means that if every member of a family of sets is 
non empty, then it is possible to pick one element from each 
of the members.

Another way to state the axiom of choice is:

```{prf:axiom} Axiom of choice (disjoint sets formulation)
:label: ax-st-axiom-of-choice-disjoint-sets

If $\{A_i\}_{i \in I}$ is a 
nonempty family of pairwise disjoint sets such that 
$A_i \neq \EmptySet $ for each $i \in I$, then 
there exists a set $E \subseteq \cup_{i \in I} A_i$ such that
$E \cap A_i$ consists of precisely one element for each
$i \in I$.
```




