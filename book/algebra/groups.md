(sec:alg:group:theory)=
# Groups

We introduce the notion of groups in this section.

```{note}
All functions in this section are total functions.
```

## Definition

A group is a set with a single binary operation. It is one of the simplest
algebraic structures.

````{prf:definition} Group
:label: def-alg-group

Let $G$ be a set. 
Let $\cdot : G \times G \to G$ be a binary operation 
defined on $G$ mapping $(g_1, g_2) \to \cdot (g_1, g_2)$ and denoted as

$$
\cdot (g_1, g_2)\triangleq g_1 \cdot g_2.
$$
If the binary operation $\cdot$ satisfies the following properties:

1. [Closure] The set $G$ is closed under the binary operation $\cdot$. i.e.

   $$
   \forall g_1, g_2 \in G, g_1 \cdot g_2 \in G.
   $$
1. [Associativity] For every $g_1, g_2, g_3 \in G$

   $$
   g_1 \cdot (g_2 \cdot g_3) = (g_1 \cdot g_2) \cdot g_3
   $$
1. [Identity element] There exists an element $e \in G$ such that

   $$
   g \cdot e = e \cdot g = g \quad \forall g \in G
   $$
1. [Inverse element] For every $g \in G$ there exists an 
   element $g^{-1} \in G$ such that

   $$
   g \cdot g^{-1} = g^{-1} \cdot g = e
   $$

then the set $G$ together with the operator $\cdot$ denoted 
as $(G, \cdot)$ is known as a *group*.
````

Above properties are known as *group axioms*.
Note that commutativity is not a requirement of a group.

```{prf:remark}
:label: rem-alg-group-operation-add-mult

Frequently, the group operation is the regular mathematical
addition. In those cases, we write $g_1 \cdot g_2$ as $g_1 + g_2$. 
Otherwise, we will write $g_1 \cdot g_2$ as $g_1 g_2$. 

Often, we may simply write a group $(G, \cdot)$ as $G$ 
when the underlying operation $\cdot$ is
clear from the context.
```

### Commutative groups

A commutative group is a richer structure than a group. Its
elements also satisfy the commutativity property.

````{prf:definition} Commutative group
:label: def-alg-commutative-group

Let $(G, \cdot)$ be a group such that its binary operation $\cdot$ 
satisfies an additional property:

1. [Commutativity] For every $g_1, g_2 \in G$

   $$
   g_1 g_2 = g_2 g_1 
   $$

Then $(G,\cdot)$ is known as a *commutative group* 
or an *Abelian group*.
````


## Permutation Groups

```{prf:definition} Permutation
:label: def-alg-permutation

Let $X$ be a nonempty set.
A bijective function $\pi : X \to X$ is called a *permutation* of $X$.

The set of all permutations of a set $X$ is denoted by
$\Sym(X)$.
```


```{prf:theorem} Permutation group
:label: res-alg-permutation-group

Let $X$ be a nonempty set. The set of all permutations of $X$,
namely $\Sym(X)$, is a group under the operation of
function composition.

It is known as the permutation group of $X$
and denoted as $(\Sym(X), \circ)$.
```

```{prf:proof}
Since every permutation $\pi: X \to X$ is a bijection,
hence it has a unique inverse function $\pi^{-1}: X \to X$
which is also a permutation (as it is also a bijection).

Closure

1. Let $\pi$ and $\sigma$ be permutations.
1. Then they are both bijections.
1. Hence Their composition $\pi \circ \sigma$ is also a bijection.
1. Hence $\pi \circ \sigma$ is also a permutation.
1. Hence $\Sym(X)$ is closed under function composition.

Associativity
1. Function composition is by definition associative.

Identity element
1. Consider the identity function  $\id_X : X \to X$ defined as

   $$
   \id_X(x) = x \Forall x \in X.
   $$
1. $\id_X$ is a bijection. Hence $\id_X \in\Sym(X)$.
1. For any $\pi \in \Sym(X)$, we can see that
   $\pi \circ \id_X = \pi$.
1. Similarly, $\id_X \circ \pi = \pi$.
1. Hence $\id_X$ serves as an identity permutation.

Inverse
1. Since bijections are invertible, hence
   for every permutation, there exists an inverse permutation.

Hence $(\Sym(X), \circ)$ is a group.
```

### Permutations on Finite Sets


````{div}

Let $X$ be a finite set written as $X = \{ x_1, \dots, x_n \}$.
A convenient way of writing a permutation of a finite set is


```{math}
:label: eq-alg-permutation-finite-1

\pi = \begin{pmatrix}
x_1 & x_2 & \dots & x_n \\
\pi(x_1) & \pi(x_2)& \dots & \pi (x_n)
\end{pmatrix}
```
1. We can see that the two rows are two different (ordered) arrangements
   of the elements of $X$.
1. One can think of a permutation as a rearrangement of the elements
   of the set $X$.
1. Recall from {prf:ref}`def-finite-set` that for a finite set,
   there exists a bijection from the set $\{1, \dots, n \}$
   to the set $X$ given by  $i \mapsto x_i$.
1. Hence, for every permutation of a finite $X$, there exists
   a corresponding permutation of the set $\{1, \dots, n \}$.
````

### Symmetric Groups

```{prf:definition} Symmetric group of degree $n$
:label: def-alg-sym-group-n

Consider the set $X = \{1, \dots, n \}$. The set of
all permutations of $X$ under the operation of
function composition is known as the
*symmetric group*  of degree $n$
and is denoted by $S_n$.
```

```{prf:example} Symmetric group $S_4$
:label: ex-alg-sym-group-4-1

1. Let $X = \{ 1, 2, 3, 4 \}$.
1. Let $\pi$ and $\sigma$ be two permutations given by

   $$
   \pi = \begin{pmatrix}
   1 & 2 & 3 & 4 \\
   4 & 1 & 3 & 2
   \end{pmatrix}
   \text{ and }
   \sigma = \begin{pmatrix}
   1 & 2 & 3 & 4 \\
   3 & 2 & 4 & 1
   \end{pmatrix}.
   $$
1. $\pi^{-1}$ is given by

   $$
   \pi^{-1} = \begin{pmatrix}
   1 & 2 & 3 & 4 \\
   2 & 4 & 3 & 1
   \end{pmatrix}.
   $$
1. $\sigma^{-1}$ is given by

   $$
   \sigma^{-1} = \begin{pmatrix}
   1 & 2 & 3 & 4 \\
   4 & 2 & 1 & 3
   \end{pmatrix}.
   $$
1. Then $\pi \sigma$ is given by

   $$
   \pi \sigma = \begin{pmatrix}
   1 & 2 & 3 & 4 \\
   3 & 1 & 2 & 4
   \end{pmatrix}.
   $$
   We have $(\pi \sigma) (i) = \pi (\sigma (i))$.
   E.g. $(\pi \sigma) (3) = \pi (4) = 2$.
1. Then $\sigma \pi$ is given by

   $$
   \pi \sigma = \begin{pmatrix}
   1 & 2 & 3 & 4 \\
   1 & 3 & 4 & 2
   \end{pmatrix}.
   $$
1. We can see that $\pi \sigma \neq \sigma \pi$.
   Hence the permutation group is not commutative.
```

```{prf:theorem} Cardinality of symmetric group
:label: res-alg-sym-group-card

Let $X$ be a finite set with $n$ elements.
Then $|\Sym(X)| = n!$.
```

```{prf:proof}
We can write a permutation as

$$
\pi = \begin{pmatrix}
x_1 & x_2 & \dots & x_n \\
y_1 & y_2 & \dots & y_n
\end{pmatrix}
$$
1. We need to count the number of ways of constructing
   the second row.
1. There are $n$ ways of choosing $y_1$.
1. Once $y_1$ has been chosen, there are $n-1$ ways
   of choosing $y_2$ since $y_1$ cannot be
   chosen again as $\pi$ is injective.
1. Similarly, there are $n-2$ ways of choosing $y_3$
   since $y_1$ and $y_2$ have already been chosen
   and cannot be chosen again.
1. We continue in this manner.
1. Finally, there is just one way of choosing $y_n$.
1. Each choice of $y_i$ can occur with each choice of $y_j$.
1. Hence total number of permutations is given by

   $$
   n (n - 1) (n -2) \dots 1 = n!.
   $$ 
```