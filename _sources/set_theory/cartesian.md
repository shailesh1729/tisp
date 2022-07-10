# General Cartesian Product

In this section, we extend the definition of
Cartesian product to an arbitrary number of sets.


```{index} Cartesian product
```
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

```{index} Choice function
```
```{prf:definition} Choice function
:label: def-st-choice-function

A member function $f$ of the Cartesian product $\prod A_i$
is called a *choice function* and
often denoted by $(x_i)_{i \in I}$ or simply by $(x_i)$.
```

```{prf:remark}
:label: rem-st-empty-input-empty-product

For a family $\{A_i\}_{i \in I}$,  if any of the $A_i$ is empty, then
the Cartesian product $\prod A_i$ is empty.
```
This follows from the definition of the Cartesian product
as a choice function $f$ must choose an element from each $A_i$.
If an $A_i$ is empty, a choice function cannot choose any element
from it, hence the choice function cannot exist.

```{prf:remark}
:label: rem-st-cart-prod-same-input-notation

If the family of sets $\{A_i\}_{i \in I}$ satisfies $A_i = A \Forall i \in I$,
then $\prod_{i \in I} A_i$ is written as $A^I$.

$$
    A^I = \{ f | f : I \to A\}.
$$

i.e. $A^I$ is the set of all functions from $I$ to $A$.
```

## Examples

```{prf:example} Binary functions on the real line
:label: ex-st-cart-prod-binary-function-r

Let $A = \{0, 1\}$. $A^{\RR}$ is a set of all functions on $\RR$
which can take only one of the two values $0$ or $1$.
```

```{prf:example} Binary sequences
:label: ex-st-binary-seq-as-cart-prod

Let $A = \{0, 1\}$. $A^{\Nat}$ is a set of all sequences of $0$s and $1$s.
```

```{prf:example} Real sequences
:label: ex-st-real-seq-as-cart-prod

$\RR^{\Nat}$ is a set of all real sequences. 
It is also denoted as $\RR^{\infty}$.
```

```{prf:example} Real valued functions on the real line 
:label: ex-st-real-func-as-cart-prod

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
