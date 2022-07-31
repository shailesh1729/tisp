(sec:prob:intro)=
# Probability Spaces

Probability measures the amount of uncertainty in an event.
Typically, the probability of an event is expressed
as a nonnegative real number ranging between $0$ and $1$.

1. When an event has a probability $1$, we are certain that
   the event will occur.
1. When an event has a probability $0$, we are certain that
   the event will not occur.
1. When we toss a coin, we are not certain whether it will
   turn heads (H) or tails (T). We normally assign
   a probability of $0.5$ to both H and T outcomes as
   we believe that both outcomes are equally likely.
1. When we throw a die, then the possible outcomes are
   $\{ 1, 2, 3, 4, 5, 6 \}$. If we believe that each
   outcome is equally likely, then we can assign
   a probability of $\frac{1}{6}$ to each outcome.
1. If we have a fairly reliable digital communication
   channel, then the probability of error may be
   as low as $1e-6$. In other words, there is a
   one in a million chance of a transmitted bit
   flipping during the transmission.

Given a sample space of outcomes, there are two main
activities involved:

1. Assigning a probability to different outcomes or
   events in a manner that the probabilities
   are sensible.
1. Use the laws of probability theory to infer
   the probabilities of other outcomes or events.

Our notes will be based on the axiomatic treatment of probability.
We describe the rules for assigning sensible probabilities
to different events. We then develop the theory for computing with
the probabilities. We leave out the task of estimating the
probabilities of individual events which is covered extensively
in statistics.
The foundations of modern probability theory are rooted in
the measure theory which is a study of measures.
A measure is a generalization of geometric notions like
length, area and volume. The probability of a set is
also a measure.
Although we don't provide extensive coverage of
measure theory in these notes,
we cover some fundamental concepts like $\sigma$-algebra
in our introduction to probability theory.
For a comprehensive measure theoretic treatment,
see {cite}`billingsley2012probability`.


```{index} Random experiment
```
```{prf:definition} Random experiment
:label: def-prob-random-experiment

A *random experiment* is an experiment in which the
outcomes are nondeterministic.
In other words, different outcomes can occur each time
the experiment is run.
```

## Sample Space

```{index} Sample space
```
```{prf:definition} Sample space
:label: def-prob-sample-space

The *sample space* associated with a random experiment
is the set of all possible outcomes of the experiment.
```

We shall often denote the sample space by the symbol
$\Omega$. Individual outcomes shall often be denoted
by $\zeta$.

## Sigma Algebras and Fields

```{index} Field; probability, Algebra; probability
```
```{prf:definition} Field, Algebra
:label: def-prob-field

Consider a sample space $\Omega$
and a certain collection of subsets of $\Omega$ denoted by $\FFF$.
We say that $\FFF$ forms an *algebra* (in the set theoretic sense)
over $\Omega$ if meets the following rules:

1. $\EmptySet \in \FFF$.
1. If $A, B \in \FFF$ then $A \cup B \in \FFF$ and $A \cap B \in \FFF$.
1. If $E \in \FFF$ then $\Omega \setminus E = E^c \in \FFF$.

In other words,
$\FFF$ contains the empty set,
$\FFF$ is closed under union, intersection, complement operations.
The pair $(\Omega, \FFF)$ is known as a *field*.
```

```{note}
The term *algebra* is used here in the sense of Boolean
algebra from set theory whose operations include
union, intersection and complement.
The notion of *field* here is different from the notion
of fields (e.g. $\RR$ and $\CC$)
in ring theory.
Similarly the term algebra over $\Omega$ should not
be confused with algebras over fields or rings in ring theory.
```


```{prf:example} trivial algebra
:label: ex-prob-algebra-1

Let $\Omega$ be an arbitrary sample space.
Then, $\{ \EmptySet, \Omega \}$ is a trivial algebra over $\Omega$.
```

```{prf:example} algebras over a set of 4 elements
:label: ex-prob-algebra-4

Let $\Omega = \{ 1, 2, 3, 4 \}$.

1. $\{\EmptySet,  \{ 1, 2, 3, 4 \} \}$ is an algebra.
1. $\{\EmptySet, \{ 1, 2\}, \{3, 4 \}, \{ 1, 2, 3, 4 \} \}$ is an algebra.
1. $\{\EmptySet, \{ 1\}, \{2, 3, 4 \}, \{ 1, 2, 3, 4 \} \}$ is an algebra.
1. The power set consisting of all subsets of $\Omega$ is an algebra.
```


```{prf:theorem} Properties of an algebra
:label: res-prob-algebra-props

Let $\FFF$ be an algebra over $\Omega$. Then

1. $\Omega \in \FFF$.
1. If $A_1, \dots, A_n \in \FFF$, then $A_1 \cup \dots \cup A_n \in \FFF$.
1. If $A_1, \dots, A_n \in \FFF$, then $A_1 \cap \dots \cap A_n \in \FFF$.
1. If $A, B \in \FFF$ then $A \setminus B \in \FFF$.
```

$\FFF$ includes the sample space.
$\FFF$ is closed under finite unions and finite intersections.
$\FFF$ is closed under set difference.

```{prf:proof}
(1) Sample space
1. $\EmptySet \in \FFF$.
1. $\Omega = \EmptySet^c$.
1. Hence $\Omega \in \FFF$.

(2) Closure under finite union by mathematical induction

1. Base case: for $n=2$ is trivial.
1. Assume that the statement is true for some $n \geq 2$.
1. Let $A_1, \dots, A_n, A_{n+1} \in \FFF$.
1. By inductive hypothesis $A = A_1 \cup \dots \cup A_n \in \FFF$.
1. Then
   
   $$
   A_1 \cup \dots \cup A_n \cup A_{n + 1}
   = (A_1 \cup \dots \cup A_n) \cup A_{n + 1}
   = A \cup A_{n + 1}.
   $$
1. Since both $A, A_{n + 1} \in \FFF$, hence there union
   is also in $\FFF$.
1. Hence by mathematical induction, $\FFF$ is closed under
   all finite unions.

(3) Closure under finite intersection

1. We note that

   $$
   A_1 \cap \dots \cap A_n = (A_1^c \cup \dots \cup A_n^c)^c.
   $$
1. Since $A_i \in \FFF$, hence $A_i^c \in \FFF$ for $i=1,\dots,n$.
1. Then $A = A_1^c \cup \dots \cup A_n^c \in \FFF$ due to (2).
1. Then $A_1 \cap \dots \cap A_n = A^c \in \FFF$.

(4) Set difference

1. We note that $A \setminus B = A \cap B^c$.
1. Since $B \in \FFF$, hence $B^c \in \FFF$.
1. Since $A, B^c \in \FFF$, hence $A \cap B^c \in \FFF$.
```

```{prf:example} Algebra from a partition
:label: ex-prob-algebra-from-partition

Let $\Omega$ be a sample space. Let
$A = \{ A_1, \dots, A_n \}$ be a (finite) partition of $\Omega$.
In other words, $A_i$ are pairwise disjoint and their
union is $\Omega$. Then the collection $\FFF$
consisting of all unions of the sets $A_i$
(including the empty set which is the union of zero sets)
forms an algebra.

1. Since there are $n$ sets in the partition $A$, hence
   number of elements of $\FFF$ is $2^n$.
1. By definition $\EmptySet$ and $\Omega$ are in $\FFF$.
1. Let $X, Y \in \FFF$. Then both $X$ and $Y$ are unions
   of some members of $A$.
1. Hence $X \cup Y$ is also a union of some members of $A$.
1. Hence $\FFF$ is closed under union.
1. If $X$ and $Y$ are disjoint then $X \cap Y \in \FFF$.
1. Otherwise, $X \cap Y$ is the union of some members of $A$
   which are common in both $X$ and $Y$.
   Hence $X \cap Y \in \FFF$.
1. Hence $\FFF$ is closed under intersection.
1. Let $X \in \FFF$. Then $X$ is union of some members of $A$.
1. Then $\Omega \setminus X$ is the union of remaining members of $A$.
1. Hence $\Omega \setminus X \in \FFF$.
1. Hence $\FFF$ is closed under complement.
1. Hence $\FFF$ is an algebra.
```

Often, the sample space $\Omega$ is an infinite set (e.g., $\RR$)
and the field of subsets of $\Omega$ is also infinite.
For example, the Borel field defined over $\RR$ contains
all the open and closed intervals in $\RR$.
We have to deal with situations which
involve countable unions and intersections of sets in the field.
Mathematical induction shows that a field is
closed under finite unions and intersections
but it is not enough to prove that it is also
closed under countable unions.
To handle such cases, we need to extend the
definition of a field.

```{index} $\sigma$ field, $\sigma$ algebra
```
```{prf:definition} $\sigma$-field, $\sigma$-algebra
:label: def-prob-sigma-field

Consider an infinite sample space $\Omega$
and a certain collection of subsets of $\Omega$ denoted by $\FFF$.
We say that $\FFF$ is a $\sigma$-*algebra* over $\Omega$ if
it is an algebra over $\Omega$ and it is closed
under countable unions.
In other words, if $A_1, A_2, \dots$ is a countable
collection of sets in $\FFF$, then, their union

$$
\bigcup_{i=1}^{\infty} A_i \in \FFF.
$$
The pair $(\Omega, \FFF)$ is known as a $\sigma$-*field*.
```

When the sample space is obvious from the context, we will
often call $\FFF$ also as a field or a $\sigma$-field
as appropriate.

```{prf:example} Power set
:label: ex-prob-power-set-field

Let $\Omega$ be an arbitrary sample space.
Then its power set $\PPP(\Omega)$ is a $\sigma$-algebra.
```


```{prf:theorem} Countable intersection
:label: res-prob-sigma-algebra-countable-intersection

Let $\FFF$ be a $\sigma$-algebra over $\Omega$.
Then $\FFF$ is closed under countable intersection.
In other words, if $A_1, A_2, \dots$ is a countable
collection of sets in $\FFF$, then, their intersection

$$
\bigcap_{i=1}^{\infty} A_i \in \FFF.
$$
```
```{prf:proof}
We use the complement property.

1. Let  $A_1, A_2, \dots$ be subsets in $\FFF$.
1. Then $A_1^c, A_2^c, \dots$ are also in $\FFF$.
1. Then their countable union:

   $$
   \bigcup_{i=1}^{\infty} A_i^c \in \FFF.
   $$
1. Taking complement, we get

   $$
   \bigcap_{i=1}^{\infty} A_i \in \FFF
   $$
   as desired.
```


```{prf:remark}
:label: rem-prob-sigma-field-bounds

Any $\sigma$-algebra $\FFF$ of subsets of a sample space $\Omega$
likes between the two extremes:

$$
\{ \EmptySet, \Omega \} \subseteq \FFF \subseteq \PPP(\Omega).
$$
```




### Generated $\sigma$ Algebra

```{index} Atom; $\sigma$-algebra
```
```{prf:definition} atom
:label: def-prob-atom

An *atom* of $\FFF$ is a set $A \in \FFF$ such that
the only subsets of $A$ which are also in $\FFF$
are the empty set $\EmptySet$ and $A$ itself.
```

```{prf:theorem} Intersection of $\sigma$-algebras
:label: res-prob-intersection-sigma-algebras

Let $\GGG = \{ \GGG_i \}_{i \in I}$
be a nonempty collection of $\sigma$-algebras over $\Omega$
where $I$ is some index set.
Then their intersection $\bigcap_{i \in I} \GGG_i$ is
also a $\sigma$-algebra.
```

```{prf:proof}
Denote $\FFF = \bigcap_{i \in I} \GGG_i$. We shall
verify all the properties of a $\sigma$-algebra.

Empty Set

1. Since $\EmptySet \in \GGG_i$ for every $i$, hence
   $\EmptySet \in \FFF$.

Union

1. Let $A, B \in \FFF$.
1. Then $A, B \in \GGG_i$ for every $i$.
1. Hence $A \cup B \in \GGG_i$ for every $i$.
1. Hence $A \cup B \in \FFF$.

Intersection

1. Let $A, B \in \FFF$.
1. Then $A, B \in \GGG_i$ for every $i$.
1. Hence $A \cap B \in \GGG_i$ for every $i$.
1. Hence $A \cap B \in \FFF$.

Countable union
1. Let $A_1, A_2, \dots$ be a countable collection of subsets
   in $\FFF$.
1. Then $A_1, A_2, \dots \in \GGG_i$ for every $i$.
1. Since each $\GGG_i$ is a $\sigma$-algebra, hence
   $\bigcup_{j=1}^{\infty} A_j \in \GGG_i$ for every $i$.
1. Hence $\bigcup_{j=1}^{\infty} A_j \in \FFF$.
```

```{index} Generated sigma algebra
```
```{prf:definition} $\sigma$-algebra generated by a collection of sets
:label: res-prob-generated-field

Let $\AAA = \{ A_i \}_{i \in I}$ be a collection of subsets of $\Omega$
where $I$ is an index set.
Let $\FFF$ be the smallest $\sigma$-algebra such that
$A_i \in \FFF$ for every $i \in I$.
Then $\FFF$ is called the $\sigma$-*algebra generated by* $\AAA$
and is denoted by $\sigma(\AAA)$.
```

1. Here by smallest, we mean that if there is any other $\sigma$-algebra
   $\GGG$ such that $A_i \in \GGG$ for every $i \in I$, then
   $\FFF \subseteq \GGG$.
1. Since the power set $\PPP(\Omega)$ is a $\sigma$ algebra
   and it contains all subsets of $\Omega$ (including $\AAA$)
   hence there is always a $\sigma$-algebra containing a given
   collection of sets.
1. It may not be possible to visualize every member of $\FFF$ easily
   from the descriptions of $A_i$. 

We next show that a smallest $\sigma$-algebra exists
for every collection $\AAA$.

```{prf:theorem} Existence of the generated $\sigma$-algebra
:label: res-prob-existence-generated-algebra

Let $\AAA$ be a collection of subsets of $\FFF$. Then
there exists a smallest $\sigma$-algebra containing $\AAA$.
In other words, there is a $\sigma$-algebra generated by $\AAA$.
```

```{prf:proof}
The main issue is to verify that if there is any other
$\sigma$-algebra, it contains the smallest one.
We provide a constructive proof.

1. Let $\GGG = \{ \GGG_j \}_{j \in J}$
   be the collection of all $\sigma$-algebras
   containing all sets of $\AAA$.
1. We can see that $\GGG$ is nonempty since $\PPP(\Omega) \in \GGG$.
1. By {prf:ref}`res-prob-intersection-sigma-algebras`,
   $\FFF = \bigcap_{j \in J} \GGG_j$ is a $\sigma$-algebra.
1. We claim that $\sigma (\AAA) = \FFF$.
1. Since $\AAA \subseteq \GGG_j$ for every $j \in J$, hence
   $\AAA \subseteq \FFF$.
1. By construction $\FFF \subseteq \GGG_j$ for every $j \in J$.
   In other words, $\FFF$ is contained in every $\sigma$-algebra
   containing $\AAA$.
1. Hence $\FFF$ is indeed the $\sigma$-algebra generated by $\AAA$.

We note that if $\AAA$ itself is a $\sigma$-algebra, then
of course $\sigma(\AAA) = \AAA$.
```

```{prf:example} Algebra generated by 2 sets
:label: ex-prob-gen-algebra-2-sets

Let $\Omega$ be an arbitrary sample space. Let $A$ and $B$
be two subsets of $\Omega$ which are not necessarily disjoint.
We shall construct the algebra $\FFF$ generated by $A$ and $B$.

1. Since $A \in \FFF$, hence $A^c \in \FFF$.
1. Similarly, $B^c \in \FFF$.
1. Since $A$ and $B$ and their complements are in $\FFF$,
   hence $AB, AB^c, A^c B, A^c B^c \in \FFF$
   as $\FFF$ is closed under intersection.
1. Let us name them $E = AB$, $F = AB^c$, $G = A^c B$ and $H = A^c B^c$.
1. We can see that these four sets $E, F, G, H$
   are disjoint and

   $$
   \Omega = E \cup F \cup G \cup H.
   $$
1. We now have a partition of $\Omega$ into $4$ disjoint sets.
   We can follow the lead from {prf:ref}`ex-prob-algebra-from-partition`
   to construct an algebra
   by constructing all the unions of $0$ or more sets from the
   collection $\{ E, F, G, H \}$.
1. The empty set $\EmptySet$ doesn't contain any of these sets ${4 \choose 0}$.
1. There are ${4 \choose 1} = 4$ of these disjoint subsets. 
1. There are ${4 \choose 2} = 6$ pair-wise unions of these $4$ sets.
1. There are ${4 \choose 3} = 4$ unions of $3$ of these $4$ subsets.
1. There is ${4 \choose 4} = 1$ union of all the $4$ subsets which is $\Omega$.
1. A total of $1 + 4 + 6 + 4 + 1 = 16 = 2^4$ possible subsets are formed.
1. In particular, note that $A = E \cup F$, $B = E \cup G$,
   $A^c = G \cup H$ and $B^c  = F \cup H$.
1. We can see that this collection of $16$ subsets of $\Omega$ is
   an algebra following {prf:ref}`ex-prob-algebra-from-partition`.
1. This is indeed the smallest algebra containing
   $A$ and $B$ as any other algebra must contain $\FFF$.
1. Hence it is the algebra generated by $A$ and $B$.
1. We can see that $E, F, G, H$ are the atoms of the algebra $\FFF$.
```

### Dynkin $\pi-\lambda$ theorem

When constructing probability measures
(see {ref}`sec:prob:probability:measure`),
it is generally impossible to assign
a probability to each subset in a $\sigma$-algebra.
The Carathéodory extension theorem allows
us to define a measure explicitly for only a small
collection of simple sets, which may or may not
form a $\sigma$-algebra (e.g. the atoms inside
a $\sigma$-algebra) and automatically extend
the measure to all other sets in the algebra.
The uniqueness claim in the extension theorem
makes use of Dynkin $\pi-\lambda$ theorem
(below). Readers may skip this subsection
in the first reading.

```{index} Pi system
```
```{prf:definition} $\pi$ system
:label: def-prob-pi-system

Let $\Omega$ be a sample space. A collection $P$
of subsets of $\Omega$ is a $\pi$-*system* if
$P$ is closed under finite intersections.
In other words, if $A, B \in P$, then $A \cap B \in P$.
```

```{index} Lambda system
```
```{prf:definition} $\lambda$ system
:label: def-prob-lambda-system

Let $\Omega$ be a sample space. A collection $L$
of subsets of $\Omega$ is a $\lambda$-*system* if
1. $L$ contains the empty set $\EmptySet$
1. $L$ is closed under complements:
   if $A \in L$ then $A^c \in L$
1. $L$ is closed under countable *disjoint* union:
   if $A_1, A_2, \dots \in L$ and $A_i \cap A_j = \EmptySet$
   for every $i \neq j$, then $\bigcup_{i=1}^{\infty} A_i \in L$.
```

```{prf:theorem} Dynkin $\pi-\lambda$ theorem
:label: res-prob-dynkin-pi-lambda

If $P$ is a $\pi$ system and $L$ a $\lambda$-system
of subsets of $\Omega$ with $P \subseteq L$ then

$$
\sigma(P) \subseteq L.
$$
In other words, the $\sigma$-algebra generated by $P$
is contained in $L$.
```

The proof of this result is involved.
The overall strategy works as follows:

1. We shall construct a $\sigma$-algebra
   that lies between $P$ and $L$.
1. In particular, we shall construct the
   set $l(P)$ which is the intersection
   of all $\lambda$-systems containing $P$.
1. We then show that $l(P)$ is a $\lambda$-system. 
1. We then show that $l(P)$ is also a $\pi$-system.
1. We show that a collection which is both a $\lambda$-system
   and a $\pi$-system is also a $\sigma$-algebra.
1. Thus, we claim that $l(P)$ is a $\sigma$-algebra.
1. We finally show that $\sigma(P) \subseteq l(P) \subseteq L$.

In order to prove this result, we first prove
some of the intermediate steps individually.


```{prf:lemma} Closedness under proper differences
:label: res-prob-lambda-sys-proper-diff

A $\lambda$-system is closed under proper differences.
In other words, if $A, B \in L$ where $L$ is a
$\lambda$-system and $A \subseteq B$ then the difference
$B \setminus A$ is also in $L$.
```

```{prf:proof}
We note that $B \setminus A = B \cap A^c$. We shall show
this as a complement of the disjoint union of sets.

1. Since $B \in L$, hence $B^c \in L$.
1. Since $A \subseteq B$, hence $A$ and $B^c$ are disjoint.
1. Hence $D = A \cup B^c \in L$ since it is a disjoint union.
1. Hence $D^c = A^c \cap B$ in $L$.
1. But $B \setminus A = B \cap A^c = D^c$.
1. Hence $B \setminus A \in L$. 
```

```{prf:lemma} $\pi + \lambda \implies \sigma$
:label: res-prob-pi-lambda-sigma

A family of subsets of $\Omega$ which is both a $\pi$-system
and a $\lambda$-system is a $\sigma$-algebra.
```

```{prf:proof}
Let $S$ be a family of subsets of $\Omega$ which is
both a $\pi$-system and a $\lambda$-system.

1. $\EmptySet \in S$ since it is a $\lambda$-system.
1. $S$ is closed under finite intersections since it is a
   $\pi$-system.

We just need to show that it is closed under countable
unions of (not necessarily disjoint) sets.

1. Let $A_1, A_2, \dots \in S$.
1. We shall write $\bigcup_{i=1}^{\infty} A_i$ as a
   countable union of disjoint sets.
1. Let $B_1 = A_1$.
1. For $n \geq 2$, let

   $$
   B_n = A_n \setminus (A_1 \cup A_2 \cup \dots \cup A_{n-1})
   = A_n \cap A_1^c \cap A_2^c \cap \dots \cap A_{n-1}^c.
   $$
   In other words, $B_n$ consists of all elements of $A_n$
   which don't appear in any of the sets $A_1, \dots, A_{n-1}$.
1. Then $B_1, B_2, \dots$ is a sequence of disjoint sets.
1. We can also see that $A_1 \cup \dots \cup A_n = B_1 \cup \dots \cup B_n$
   for every $n$.
1. Hence $\bigcup_{i=1}^{\infty} A_i = \bigcup_{i=1}^{\infty} B_i$.
1. Since $S$ is a $\lambda$-system, hence $A_i^c \in S$ for every $i$.
1. Since $S$ is a $\pi$-system, hence $B_i \in S$ for every $i$.
1. Hence  $\bigcup_{i=1}^{\infty} B_i \in S$ as it is a countable
   union of disjoint sets.
```

```{prf:lemma} $\lambda$-co-systems
:label: res-prob-dynkin-lem-3

Suppose $L'$ is a $\lambda$-system of subsets of $\Omega$.
For any set $A \in L'$, let $S_A$ be the set of all
$B \in \Omega$ for which $A \cap B \in L'$.
Then $S_A$ is a $\lambda$-system.
```

```{prf:proof}
Empty set

1. Since $\EmptySet = A \cap \EmptySet \in L'$, hence
   $\EmptySet \in S_A$.

Countable union of disjoint sets
1. Let $B_1, B_2, \dots \in S_A$ be a sequence of
   disjoint subsets in $S_A$.
1. Then $A \cap B_i \in L'$ for every $i$.
1. Then $\bigcup (A \cap B_i) \in L'$
   since $A \cap B_i$ are also disjoint.
1. Also $\bigcup (A \cap B_i) = A \cap (\bigcup B_i)$.
1. Since $A \cap (\bigcup B_i) \in L'$, hence
   $\bigcup B_i \in S_A$.
1. Hence $S_A$ is closed under countable union of disjoint sets.

Complements

1. Let $B \in S_A$. Then $A \cap B \in L'$.
1. Now $A \cap B^c = A \setminus B = A \setminus (A \cap B)$.
1. Since $A \in L'$ and $A \cap B \in L'$
   and $A \cap B \subseteq A$, hence
   due to {prf:ref}`res-prob-lambda-sys-proper-diff`,
   $A \setminus (A \cap B) \in L'$.
1. Since $A \cap B^c \in L'$ hence $B^c \in S_A$.
1. Hence $S_A$ is closed under complements.

Thus, $S_A$ is indeed a $\lambda$-system.
```

```{prf:lemma}
:label: res-prob-dynkin-lem-4

Let $l(P)$ be the intersection of all $\lambda$-systems
containing $P$. Then $l(P)$ is a $\lambda$-system.
```
```{prf:proof}
We can easily verify that $l(P)$ satisfies all the properties
of a $\lambda$-system.

1. Let $\LLL = \{L_i \}$ be the collection of all $\lambda$-systems
   containing $P$.
1. Then $l(P) = \bigcap L_i$.
1. Since $\EmptySet \in L_i$ for every $i$, hence
   $\EmptySet \in l(P)$.
1. Let $A \in l(P)$.
1. Then $A \in L_i$ for every $i$.
1. Hence $A^c \in L_i$ for every $i$.
1. Hence $A^c \in l(P)$.
1. Let $A_1,A_2, \dots \in l(P)$ be a collection
   of pairwise disjoint sets.
1. Then $A_1,A_2,\dots \in L_i$ for every $i$.
1. Hence $\bigcup A_i \in L_i$ for every $i$.
1. Hence $\bigcup A_i \in l(P)$.
```

```{prf:lemma}
:label: res-prob-dynkin-lem-5

Let $l(P)$ be the intersection of all $\lambda$-systems
containing $P$. Then $l(P)$ is a $\pi$-system.
```
```{prf:proof}
The proof uses a *bootstrap* argument often used in
measure theory.

We first show that for any $A \in P$ and $B \in l(P)$,
$A \cap B \in l(P)$.

1. Let $A \in P$.
1. Then $A \in l(P)$.
1. Let $S_A$ be the set of all sets $B \subseteq \Omega$
   such that $A \cap B \in l(P)$.
1. By {prf:ref}`res-prob-dynkin-lem-3`, $S_A$
   is a $\lambda$-system.
1. Let $B \in P$. Then $A \cap B \in P$ since $P$ is a $\pi$-system.
1. But $P \subseteq l(P)$.
1. Hence $A \cap B \in l(P)$.
1. Hence $B \in S_A$.
1. Hence $P \subseteq S_A$.
1. Thus, $S_A$ is a $\lambda$-system containing $P$.
1. Hence $l(P) \subseteq S_A$ as $l(P)$ is the intersection
   of all $\lambda$-systems containing $P$.
1. Thus, for any $A \in P$ and for any $B \in l(P)$, 
   the intersection $A \cap B \in l(P)$.
   1. $B \in l(P) \implies B \in S_A$.
   1. $B \in S_A \implies A \cap B \in l(P)$.

We now show that for any $A, B \in l(P)$,
$A \cap B \in l(P)$.

1. Consider any $B \in l(P)$.
1. Let $S_B$ be the set of all sets $C \subseteq \Omega$
   such that $B \cap C \in l(P)$.
1. By preceding argument $P \subseteq S_B$.
   1. Let $A \in P$.
   1. Since $A \in P$ and $B \in l(P)$
      hence $A \cap B \in l(P)$.
   1. Hence $A \in S_B$.
   1. Hence $P \subseteq S_B$.
1. By {prf:ref}`res-prob-dynkin-lem-3`, $S_B$
   is a $\lambda$-system.
1. Therefore $l(P) \subseteq S_B$.
1. This means that for any $A \in l(P)$, the intersection
   $A \cap B \in l(P)$.
   1. $A \in l(P) \implies A \in S_B$.
   1. $A \in S_B \implies B \cap A \in l(P)$.

Thus, $l(P)$ is closed under intersections and
is indeed a $\pi$-system.
```

We are now ready to prove the Dynkin $\pi-\lambda$ theorem
({prf:ref}`res-prob-dynkin-pi-lambda`).

```{prf:proof}
Let $l(P)$ be the intersection of all $\lambda$-systems
containing $P$.

1. By hypothesis $L$ is a $\lambda$-system
   containing $P$.
1. By definition $l(P) \subseteq L$.
1. By {prf:ref}`res-prob-dynkin-lem-4`,
   $l(P)$ is a $\lambda$-system.
1. By {prf:ref}`res-prob-dynkin-lem-5`,
   $l(P)$ is a $\pi$-system.
1. By {prf:ref}`res-prob-pi-lambda-sigma`,
   $l(P)$ is a $\sigma$-algebra.
1. By definition $\sigma(P)$ is the smallest
   $\sigma$-algebra containing $P$.
1. Hence $P \subseteq \sigma(P) \subseteq l(P) \subseteq L$.
```

### Borel $\sigma$-Algebra

Recall the notions of topology (open sets, closed sets, etc.)
on the real line from {ref}`sec:bra:real-line-topology`.
If we consider the collection of open sets 
of $\RR$, denoted by $\OOO$, then it is
clear that it is not a $\sigma$-algebra
as it is not closed under complements.
We are interested in the $\sigma$-algebra
generated by $\OOO$.
By {prf:ref}`res-prob-existence-generated-algebra`
we know that such a $\sigma$-algebra exists.

```{index} Borel field, Borel algebra
```
```{prf:definition} Borel $\sigma$-algebra
:label: def-prob-borel-field

The $\sigma$-algebra generated by the open sets of the
real line $\RR$ is known as the
*Borel* $\sigma$-*algebra* of $\RR$
and is denoted by $\BBB$.
In other words, if $\OOO$ is the collection
of all open subsets of $\RR$, then

$$
\BBB = \sigma(\OOO).
$$
The pair $(\RR, \BBB)$ is known as the
*Borel field*.
The members of the Borel $\sigma$-algebra
are known as *Borel sets*.
```
Since $\BBB$ is a $\sigma$-algebra, it contains
all open sets, all closed sets,
all countable unions of closed sets,
all countable intersections of open sets.
There are other subsets of real line which are not
included in the Borel $\sigma$-algebra. However, they don't 
happen to be of much engineering and scientific
interest. 

```{prf:example} Examples of Borel sets
:label: ex-prob-borel-sets-1

Following are some examples of Borel sets:

1. $\{ x \}$ for any $x \in \RR$.
1. The set of rational numbers.
1. Any countable subset of $\RR$.
1. The intervals $(0,1)$, $[0,1]$, $(0, 1]$, $[1,0)$.
1. $[1,2] \cup [4,5]$.

```



```{prf:definition}  $G_{\delta}$-set
:label: def-prob-g-delta

A countable intersection of open sets is known as
a $G_{\delta}$-set.
```

```{prf:definition}  $F_{\sigma}$-set
:label: def-prob-f-sigma

A countable union of closed sets is known as
a $F_{\sigma}$-set.
```

We recall that a countable intersection of open
sets need not be open and a countable union
of closed sets need not be closed.
However $\BBB$ contains all the $G_{\delta}$
and $F_{\sigma}$ sets since it is a $\sigma$-algebra.

We haven't yet shown that $\BBB \neq 2^{\RR}$.
In other words, there exist non-Borel subsets of
$\RR$. There are other characterizations of the
Borel $\sigma$-algebra which provide us with 
a better understanding of its structure.

```{prf:theorem} Generation from one-sided closed intervals
:label: res-prob-borel-gen-intervals

The Borel $\sigma$-algebra $\BBB$ is generated
by intervals of the form $(-\infty, a]$, where
$a \in \QQ$ is a rational number.
```

```{prf:proof}
.

1. Let $\OOO_0$ denote the collection of all open intervals.
1. By {prf:ref}`res-rl-open-set-countable-union`, every
   open set in $\RR$ is an at most countable union
   of open intervals.
1. Hence $\sigma(\OOO_0) = \BBB$.
1. Let $\DDD$ denote the collection of all intervals
   of the form $(-\infty, a], a \in \QQ$.
1. Let $(a,b) \in \OOO_0$ for some $a < b$.
1. Let $a_n$ be a rational number in $(a, a + \frac{1}{n})$. 
   We can see that $a_n \downarrow a$ as $n \to \infty$.
1. Let $b_n$ be a rational number in $(b - \frac{1}{n}, b)$. 
   We can see that $b_n \uparrow b$ as $n \to \infty$.
1. Thus,

   $$
   (a, b) = \bigcup_{n=1}^{\infty}(a_n, b_n]
   = \bigcup_{n=1}^{\infty}
   \{ (-\infty, b_n] \cap (-\infty, a_n]^c \}.
   $$
1. Hence $(a, b) \in \sigma(\DDD)$.
1. Hence $\OOO_0 \subseteq \sigma(\DDD)$.
1. Hence $\sigma(\OOO_0) \subseteq \sigma(\DDD)$.
1. However, every element of $\DDD$ is a closed set.
1. Hence $\sigma(\DDD) \subseteq \BBB$.
1. We have

   $$
   \BBB \subseteq \sigma(\OOO_0) \subseteq \sigma(\DDD)
   \subseteq \BBB.
   $$
1. Hence $\BBB = \sigma(\DDD)$.
```

## Events

```{index} Event; probability
```
```{prf:definition} Event
:label: def-prob-event
An *event* is a subset of the sample space of
a random experiment that belongs to some
$\sigma$-algebra defined on it.
Let $\Omega$ be the sample space of a random experiment.
Let $\FFF$ be a $\sigma$-algebra of subsets of $\Omega$.
Then every member of $\FFF$ is an event.
```

```{note}
Events are the subsets of the
sample space to which probabilities can
be assigned. 
For finite sample spaces, any subset can
be an event. For infinite sample spaces,
it may not be possible to meaningfully
assign probabilities to every possible
subset. We need the notion of a $\sigma$-algebra
which is a collection of subsets of the
sample space satisfying closure under countable unions,
intersections and complements.
The subsets belonging to a $\sigma$-algebra
can be assigned probabilities and are
events.
```

We can translate the set-theoretic language
to the language of events as follows.
Let $A, B$ be two different events.

1. $A$ doesn't occur is denoted by $A^c$.
1. Either $A$ or $B$ occur is denoted by $A \cup B$.
1. Both $A$ and $B$ occur is denoted by $A B$.
1. $A$ occurs and $B$ doesn't occur is denoted by $A \setminus B$.
   This can also be denoted as $A B^c$.
1. The events $A$ and $B$ are *exhaustive* if
   $\Omega = A \cup B$.
   In particular $A \cup A^c = \Omega$.
1. $A$ and $B$ events are exclusive if $A B = \EmptySet$.



```{index} Singleton event, Elementary event
```
```{prf:definition} Elementary event
:label: def-prob-elementary-event

An event consisting of only one outcome
is called a *singleton event* or an *elementary event*.
```

```{index} Certain event
```
```{prf:definition} Certain event
:label: def-prob-certain-event

The sample space $\Omega$ is known as the *certain event*.
```
Since $\Omega$ contains all possible outcomes of an
experiment, hence this event always occurs whenever
the experiment is run.

```{index} Null event
```
```{prf:definition} Null event
:label: def-prob-null-event

The empty set $\EmptySet$ is known as the *null event*.
```

The null event never occurs.

```{index} Mutually exclusive events
```
```{prf:definition}  Mutually exclusive events
:label: def-prob-mutually-exclusive-events

Let $E$ and $F$ be two events. If $E$ and $F$ are disjoint sets
then we say that the two events are mutually exclusive.
```


(sec:prob:probability:measure)=
## Probability Measure and Space

We next provide an axiomatic definition of a probability measure.
Note that we will often write a joint event (intersection of two
events)
as $A B$ rather than $A \cap B$.

```{index} Probability measure
```
```{prf:definition} Probability measure
:label: def-prob-probability-measure


Let $\Omega$ be a sample space and
let $\FFF$ be a $\sigma$ algebra of subsets of $\Omega$.
A *probability measure* is a set function $\PP : \FFF \to \RR$
that assigns to every event $E \in \FFF$ a real number
$\PP(E)$ called the probability of the event $E$ satisfying
the following rules:

1. Nonnegativity: $\PP(E) \geq 0$.
1. Unit measure or normalization: $\PP(\Omega) = 1$.
1. Additivity: $\PP(E \cup F) = \PP(E) + \PP(F)$ if $E F = \EmptySet$.
```

We can write it in the form of axioms
(first introduced by Andrey Kolmogorov).

```{prf:axiom} First axiom: nonnegativity
:label: ax-prob-nonnegativity

The probability of an event is a nonnegative real number.

$$
\PP(E) \in \RR, \PP(E) \geq 0 \quad \Forall E \in \FFF.
$$
```
This axiom implies that the probability is always finite.

```{prf:axiom} Second axiom: unit measure
:label: ax-prob-unit-measure

$$
\PP(\Omega) = 1.
$$
```

```{prf:axiom} Third axiom: additivity
:label: ax-prob-additivity

Let $E, F \in \FFF$ be two disjoint sets. Then

$$
\PP(E \cup F) = \PP(E) + \PP(F).
$$
```

### Probability Space

```{index} Probability space
```
```{prf:definition} Probability space
:label: def-prob-probability-space

A sample space endowed with a $\sigma$-algebra and
a probability measure is known as a *probability space*.
In other words,
let $\Omega$ be the sample space of a random experiment,
let $\FFF$ be a $\sigma$ algebra of subsets of $\Omega$
and let $\PP$ be a probability measure defined on $\FFF$.
Then the triplet $(\Omega, \FFF, \PP)$ is known as
a probability space.
```


We next establish some basic facts about a probability measure.



### Basic Properties

```{prf:theorem} Properties of a probability measure
:label: res-prob-prob-measure-props

Let $(\Omega, \FFF, \PP)$ be a probability space.
Then for the events contained in $\FFF$ satisfy
the following properties. 

1. Probability of null event: $\PP(\EmptySet) = 0$.
1. $\PP(E F^c) = \PP(E) - \PP(EF)$.
1. Complement rule: $\PP(E) = 1 - \PP(E^c)$.
1. Sum rule: $\PP(E \cup F) = \PP(E) + \PP(F) - \PP(EF)$.
1. Monotonicity: If $E \subseteq F$, then 

   $$
   \PP (E)\leq \PP(F).
   $$
1. Numeric bound: 

   $$
   0 \leq \PP(E) \leq 1.
   $$
1. Finite additivity: For any positive integer $n$, we have

   $$
   \PP\left ( \bigcup_{i=1}^n E_i \right) = \sum_{i=1}^n \PP(E_i)
   $$
   if $E_1, E_2, \dots, E_n$ are pairwise disjoint events.
```

```{prf:proof}
(1)

1. $\EmptySet$ and $\Omega$ are disjoint.
1. Hence 

   $$
   \PP(\EmptySet \cup \Omega) = \PP(\EmptySet) + \PP(\Omega).
   $$
1. This simplifies to

   $$
   1 = \PP(\EmptySet) + 1.
   $$
1. Hence $\PP(\EmptySet) = 0$.

(2) 

1. Recall that $E F^c$ and $EF$ are disjoint sets
   with $E F^c \cup EF = E$.
1. Hence

   $$
   \PP(E) = \PP(E F^c) + \PP(E F).
   $$
1. Hence

   $$
   \PP(E F^c) = \PP(E) - \PP(EF).
   $$

(3)
1. $E$ and $E^c$ are disjoint with $E \cup E^c = \Omega$.
1. Hence

   $$
   1 = \PP(\Omega) = \PP(E \cup E^c) = \PP(E) + \PP(E^c).
   $$
1. Hence $\PP(E) = 1 - \PP(E^c)$.

(4)

1. Recall that we can split $E \cup F$ into disjoint sets

   $$
   E \cup F = EF^c \cup EF \cup E^c F.
   $$
1. By additivity, we have

   $$
   \PP(E \cup F) &= \PP(EF^c \cup (EF \cup E^c F))\\
   &= \PP(EF^c) + \PP(EF \cup E^c F)\\
   &= \PP(EF^c) + \PP(EF) + \PP(E^c F)\\
   &= \PP(E) - \PP(EF) + \PP(EF) + \PP(F) - \PP(EF)\\
   &= \PP(E) + \PP(F) - \PP(EF).
   $$

(5)
1. We have $F = F E \cup F E^c = E \cup F E^c$.
1. $E$ and $FE^c$ are disjoint.
1. Then
   
   $$
   \PP (F) = \PP(E \cup F E^c) = \PP(E) + \PP(F E^c). 
   $$
1. By nonnegativity, $\PP(F E^c) \geq 0$.
1. Hence $\PP(E) \leq \PP(F)$.

(6)

1. We have $\PP(E) = 1 - \PP(E^c)$.
1. But $\PP(E^c) \geq 0$.
1. Hence $\PP(E) \leq 1$.

(7)

1. The statement is trivially true for $n=1$.
1. The statement is true for $n=2$ by the additivity rule.
1. Assume that the statement is true for some $k \geq 2$.
1. In other words, for every collection of events
   $E_1, \dots, E_k$, such that the events are pairwise
   disjoint, we have

   $$
   \PP\left ( \bigcup_{i=1}^k E_i \right) = \sum_{i=1}^k \PP(E_i).
   $$
1. Let $E_1, E_2, \dots, E_k, E_{k+1}$ be a collection of $k+1$
   pairwise disjoint events. Define $E= \bigcup_{i=1}^k E_i$.
1. We have $E \cap E_{k+1} = \EmptySet$. 
1. Then

   $$
   \PP\left ( \bigcup_{i=1}^{k+1} E_i \right)
   &= \PP ( E \cup E_{k + 1}) \\
   &= \PP (E) + \PP(E_{k + 1})\\
   &= \PP\left ( \bigcup_{i=1}^k E_i \right) + \PP(E_{k + 1})\\
   &= \sum_{i=1}^k \PP(E_i) + \PP(E_{k + 1})\\
   &= \sum_{i=1}^{k+1} \PP(E_i).
   $$
1. By principle of mathematical induction, the statement is true
   for every $n$.
```


```{note}
We assign probabilities to events and not to individual outcomes
of a random experiment.
If the sample space is finite or countable, often it is convenient
to assign probabilities to individual outcomes. One should treat
this as assignment of probability
to the event consisting of a single outcome;
a singleton event.
```

In the following, we shall assume that a
probability space $(\Omega, \FFF, \PP)$ has
been given and all events are contained in $\FFF$.


```{prf:theorem} Union of three events
:label: res-prob-union-3-events

Let $A, B, C$ be three events. Then

$$
\PP(A \cup B \cup C) = \PP(A) + \PP(B) + \PP(C) - \PP(AB) - \PP(BC) - \PP(AC) + \PP(ABC).
$$
```
```{prf:proof}
Define $D = B \cup C$.

1. Then 

   $$
   \PP(A \cup B \cup C) = \PP(A \cup D) = \PP(A) + \PP(D) - \PP(AD).
   $$
1. Further

   $$
   \PP(D) = \PP(B \cup C) = \PP(B) + \PP(C) - \PP(BC).
   $$
1. Note that $AD = AB \cup AC$.
1. Also $AB \cap AC = ABC$.
1. Hence

   $$
   \PP(AD) = \PP(AB \cup AC) = \PP(AB) + \PP(AC) - \PP(ABC).
   $$
1. Putting these back, we get

   $$
   \PP(A \cup B \cup C) 
   &= \PP(A) + (\PP(B) + \PP(C) - \PP(BC)) - (\PP(AB) + \PP(AC) - \PP(ABC)) \\
   &= \PP(A) + \PP(B) + \PP(C) - \PP(AB) - \PP(BC) - \PP(AC) + \PP(ABC).
   $$
```

### Inclusion-Exclusion Principle

{prf:ref}`res-prob-union-3-events` can be extended
to the union of $n$ events. This is known
as the inclusion-exclusion principle.

```{index} Inclusion-exclusion principle
```
```{prf:theorem} Inclusion-exclusion principle
:label: res-prob-inc-ex

Let $A_1, A_2, \dots, A_n$ be $n$ events
in a probability space $(\Omega, \FFF, \PP)$.
Then

$$
\PP \left( \bigcup_{i=1}^n A_i \right )
&= S_1 - S_2 + S_3 - \dots + (-1)^{n + 1} S_n\\
&= \sum_{k=1}^n (-1)^{k+1}S_k
$$
where $S_k$ is the sum of the probability of all $k$-cardinality
intersections among the sets $A_1, \dots, A_n$.
In particular,

$$
& S_1 = \sum_{i=1}^n \PP(A_i) \\
& S_2 = \sum_{1 \leq i < j \leq n} \PP(A_i A_j) \\
& S_3 = \sum_{1 \leq i < j < k \leq n} \PP(A_i A_j A_k)\\
& \vdots\\
& S_n = \PP(A_1 A_2 \dots A_n).
$$
In general for every $k \in 1,\dots,n$, we can write:

$$
S_k = \sum_{1 \leq i_1 < i_2 <  \dots < i_k \leq n} \PP(A_{i_1} A_{i_2} \dots  A_{i_k}).
$$
```
It is known as inclusion-exclusion principle since $S_1$ is
included then $S_2$ is excluded, then $S_3$ is included and
so on.

```{prf:proof}
The proof is based on mathematical induction.
```


### Boole's Inequality

```{index} Boole's inequality, Union bound
```
````{prf:theorem} Boole's inequality
:label: res-prob-boole-inequality

Let  $A_1, A_2, \dots, A_n$ be a finite collection of events.
Then we have

$$
\PP \left ( \bigcup_{i=1}^n  A_i \right) \leq \sum_{i=1}^n \PP \left ( A_i \right).
$$
````
````{prf:proof}
We prove it using induction.

1. For $n=1$, obviously

    $$
    \PP (A_1) \leq \PP (A_1).
    $$
1. Assume the inequality is true for the set of $n$ events for some $n \geq 1$.
   In other words,

    $$
    \PP \left ( \bigcup_{i=1}^n  A_i \right) \leq \sum_{i=1}^n \PP \left ( A_i \right).
    $$
1. Since 

    $$
    \PP (A \cup B ) = \PP (A) + \PP(B) - \PP (A \cap B),
    $$
    hence

    $$
    \PP \left ( \bigcup_{i=1}^{n + 1}  A_i \right)  
    = \PP \left ( \bigcup_{i=1}^n  A_i \right) 
    + \PP (A_{n + 1}) - \PP \left ( \bigcup_{i=1}^n  A_i \bigcap A_{n +1} \right  ). 
    $$
1. Since

    $$
    \PP \left ( \bigcup_{i=1}^n  A_i \bigcap A_{n +1} \right  ) \geq 0,
    $$
    hence

    $$
    \PP \left ( \bigcup_{i=1}^{n + 1}  A_i \right) 
    \leq  \PP \left ( \bigcup_{i=1}^n  A_i \right) + \PP (A_{n + 1}) 
    \leq \sum_{i=1}^{n + 1} \PP \left ( A_i \right).
    $$
````

### Countable Additivity

Often, we need to work with problems where we need to estimate
the probability of a countable union of events. The basic
axioms of a probability measure are unable to handle
this. We need one more axiom that a probability measure
must satisfy.


```{prf:axiom} Fourth axiom: countable additivity
:label: ax-prob-countable-additivity

Let $E_1, E_2, \dots$ be a (countable) sequence of mutually exclusive
events (disjoint sets). Then

$$
\PP\left ( \bigcup_{i=1}^{\infty} E_i \right) = \sum_{i=1}^{\infty} \PP(E_i).
$$
```

## Joint and Conditional Probability

### Joint Probability

```{index} Joint probability
```
```{prf:definition} Joint probability
:label: def-prob-joint-probability

Let $A$ and $B$ be two different events. Then
the *joint probability* of the events $A$
and $B$ is the probability that the two events
occur together and is given by $\PP(A B)$.

Similarly, let $\{A_i \}_{i \in I}$ be a collection
of events indexed by the set $I$. Then their *joint probability*
is given by

$$
\PP \left (\bigcap_{i \in I} A_i \right ).
$$
In other words, it is the probability of every event
happening together.
```


### Conditional Probability

```{index} Conditional probability
```
```{prf:definition} Conditional probability
:label: def-prob-conditional-probability

Let $A$ and $B$ be two events.
Assume that $\PP(A) > 0$.
The *conditional probability* of the event $B$
given that the event $A$ has happened is denoted by
$\PP(B | A)$. It is defined as

$$
\PP(B | A) \triangleq \frac{\PP(AB)}{\PP(A)}.
$$
```
Note that the conditional probability is not
defined if $\PP(A) = 0$.

By definition, we can see that

$$
\PP(A B) = \PP(B | A) \PP(A) = \PP(A | B) \PP(B).
$$

```{prf:example}
:label: ex-prob-cond-prob-1-toss

Consider an experiment of tossing a coin 3 times.

1. The sample space is

   $$
   \Omega = 
   \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}.
   $$
1. Assume that all the outcomes are equally likely.
   Each each outcome has the probability $\frac{1}{8}$.
1. Let $A$ denote the event that the first toss is
   a head. We have

   $$
   A = \{ HHH, HHT, HTH, HTT \}.
   $$
1. We can see that $\PP(A) = \frac{1}{2}$.
1. Let $B$ be the event that more heads than tails
   come up in the three tosses. We have

   $$
   B = \{HHH, HHT, HTH, THH \}.
   $$
1. We can see that $\PP(B) = \frac{1}{2}$.
1. If the first outcome is a head, then the probability
   that more heads than tails come will increase.
1. Let us first check the event $A \cap B$. We have

   $$
   A \cap B = \{ HHH, HHT, HTH \}.
   $$
1. Hence $\PP(A B) = \frac{3}{8}$.
1. Then the probability that more heads than tails
   come up given that first toss is a head is
   given by

   $$
   \PP(B | A) = \frac{3 / 8}{ 1/2} = \frac{3}{4}.
   $$
1. We can also compute the probability that the
   first toss is a head given that more heads
   than tails come up as

   $$
   \PP(A | B) = \frac{3 / 8}{ 1/2} = \frac{3}{4}.
   $$   
```

We should verify that the conditional probability
as defined above satisfies the axioms of probability.

```{prf:theorem}
:label: res-prob-cond-prob-measure

The conditional probability is a probability measure.
```
```{prf:proof}

(Nonnegativity)
By definition, it is a ratio of nonnegative quantities.
Hence, it is nonnegative.


(Normalization)
We can see that

$$
\PP(\Omega | A) = \frac{\PP(A \Omega)}{\PP(A)}
= \frac{\PP(A)}{\PP(A)} = 1.
$$

(Additivity)

1. Let $B_1$ and $B_2$ be disjoint events.
1. Then $A B_1$ and $A B_2$ are also disjoint events.
1. Hence

   $$
   \PP(B_1 \cup B_2 | A) &= \frac{\PP(A (B_1 \cup B_2 ))}{\PP(A)}\\
   &= \frac{\PP(A B_1 \cup A B_2 ))}{\PP(A)}\\
   &= \frac{\PP(A B_1) + \PP(A B_2 ))}{\PP(A)}\\
   &= \frac{\PP(A B_1))}{\PP(A)} + \frac{\PP(A B_2 ))}{\PP(A)}\\
   &= \PP(B_1 | A) + \PP(B_2 | A).
   $$

The argument for countable additivity is similar.
```
We note that

$$
\PP(A | A)  = \frac{\PP(AA)}{\PP(A)}
= \frac{\PP(A)}{\PP(A)} = 1.
$$

Since $\PP(B | A)$ is a valid probability measure,
all the properties of a probability measure are
applicable for the conditional probability also.

```{prf:theorem} Properties of a conditional probability measure
:label: res-prob-cond-prob-measure-props

Let $(\Omega, \FFF, \PP)$ be a probability space.
Let all probabilities be conditioned on an event $A$.
Then the following properties hold:

1. $\PP(\EmptySet | A) = 0$.
1. $\PP(A | A) = 1$.
1. $\PP(E F^c | A) = \PP(E | A) - \PP(EF | A)$.
1. $\PP(E | A) = 1 - \PP(E^c | A)$.
1. $\PP(E \cup F | A) = \PP(E | A) + \PP(F | A) - \PP(EF | A)$.
1. If $E \subseteq F$, then 

   $$
   \PP (E | A)\leq \PP(F | A).
   $$
1. For any positive integer $n$, we have

   $$
   \PP\left ( \bigcup_{i=1}^n E_i | A \right) = \sum_{i=1}^n \PP(E_i | A)
   $$
   if $E_1, E_2, \dots, E_n$ are pairwise disjoint events.
1. Union of three events

   $$ 
   \PP(B \cup C \cup D | A ) 
   &= \PP(B | A) + \PP(C | A) + \PP(D | A) \\
   &- \PP(BC | A) - \PP(CD | A) - \PP(BD | A)  + \PP(BCD | A).
   $$
1. Let  $B_1, B_2, \dots, B_n$ be a finite collection of events.
   Then we have

   $$
   \PP \left ( \bigcup_{i=1}^n  B_i  | A \right) 
   \leq \sum_{i=1}^n \PP \left ( B_i | A \right).
   $$
```
The proofs are similar to {prf:ref}`res-prob-prob-measure-props`
and other results in the following.

```{note}
Since $\PP(A | A) = 1$, one can see that all
of the conditional probability is concentrated
on the outcomes in $A$. Thus, we might as well
discard the outcomes in $A^c$ and treat the
conditional probabilities as a probability
measure on the new sample space $A$.
```


```{index} Marginal probability
```
```{prf:definition} Marginal probability
:label: def-prob-marginal-probability

Let $A$ and $B$ be two events.
The *marginal probability* of the event $A$
is the probability $\PP(A)$ which is not
conditioned on the event $B$.
```

### Independence

```{index} Independence
```
```{prf:definition} Independence of two events
:label: def-prob-independence-2

Let $A$ and $B$ be two events
with $\PP(A) > 0$ and $\PP(B) > 0$.
We say that $A$ and $B$ are *independent* if and only if

$$
\PP(A B) = \PP(A) \PP(B).
$$
```

It follows that for independent events

$$
\PP(B | A) = \PP(B)
\text{ and }
\PP(A | B) = \PP(A).
$$

```{prf:definition} Independence of three events
:label: def-prob-independence-3

Let $A, B$ and $C$ be three events
with nonzero probabilities.
We say that $A, B$ and $C$ are *jointly independent* if and only if

$$
& \PP(A B C) = \PP(A) \PP(B) \PP(C)\\
& \PP(A B) = \PP(A) \PP(B)\\
& \PP(B C) = \PP(B) \PP(C)\\
& \PP(A C) = \PP(A) \PP(C).
$$
```


```{prf:definition} Independence of $n$ events
:label: def-prob-independence-n

Let $A_1, A_2, \dots, A_n$ be $n$ events contained in $\FFF$.
We say that $A_1, A_2, \dots, A_n$ are *jointly independent*
if and only if

$$
& \PP(A_{i_1} A_{i_2}) = \PP(A_{i_1}) \PP(A_{i_2})\\ 
& \PP(A_{i_1} A_{i_2} A_{i_3}) = \PP(A_{i_1}) \PP(A_{i_2}) \PP(A_{i_3})\\ 
& \vdots\\
& \PP(A_{i_1} A_{i_2} A_{i_3} \dots A_{i_k}) 
= \PP(A_{i_1}) \PP(A_{i_2}) \PP(A_{i_3}) \dots \PP(A_{i_k})\\ 
& \vdots\\
& \PP(A_1 A_2 \dots A_n) = \PP(A_1) \PP(A_2) \dots \PP(A_n)
$$
for all combinations of indices such that $1 \leq i_1 < i_2 < \dots < i_k \leq n$.
```

(sec:prob:compound:experiment)=
## Compound Experiments

Often we need to examine the outcomes of different experiments together.
Here are some examples:

- Tossing a coin and throwing a dice
- Tossing a coin twice in succession (first and second tosses are separate experiments)

Two or more experiments together form a compound experiment.
Repeated trials are an example of a compound experiment.

```{index} Compound experiment, Compound sample space
```
```{prf:definition} Compound experiment
:label: def-prob-compound-experiment

Let $A$ and $B$ be two different experiments.
Let $\Omega_1$ be the sample space of $A$
and $\Omega_2$ be the sample space of $B$.
Then the sample space of the *compound experiment*
is given by the Cartesian product $\Omega = \Omega_1 \times \Omega_2$.
```

### Product $\sigma$-Algebra

If $\FFF_1$ and $\FFF_2$ are $\sigma$-algebras over $\Omega_1$
and $\Omega_2$ respectively, it is natural to
ask how can we construct a $\sigma$-algebra
for the compound sample space.

Let $E_1$ be an event associated with experiment $A$
and $E_2$ be an event associated with experiment $B$.
Then $E = E_1 \times E_2$ is a *product event* associated with
the compound experiment. We have

$$
E_1 \times E_2 = \{\zeta = (\zeta_1, \zeta_2) \ST \zeta_1 \in E_1, \zeta_2 \in E_2 \}.
$$
However, we can see that the set

$$
\{ E_1 \times E_2 \ST E_1 \in \FFF_1, E_2 \in \FFF_2 \}
$$
is not a $\sigma$-algebra. Naturally, the
closest $\sigma$-algebra is the $\sigma$-algebra
generated by this set.

```{prf:definition} Product $\sigma$ algebra
:label: def-prob-prod-sigma-algebra

Let $(\Omega_1, \FFF_1)$ and $(\Omega_2, \FFF_2)$ be
two different $\sigma$-fields. Then the
*product* $\sigma$-*algebra* $\FFF_1 \otimes \FFF_2$
is the $\sigma$-algebra on $\Omega_1 \times \Omega_2$
generated by the collection of all product events:

$$
\FFF_1 \otimes \FFF_2 \triangleq
= \sigma(\{ E_1 \times E_2 \ST E_1 \in \FFF_1, E_2 \in \FFF_2 \}).
$$
The members of a product $\sigma$-algebra are known
as *compound events*.
```

### Compound Events

A *compound event* can be written
as a finite (or countable) disjoint union of product events
from the two experiments. A finite union looks like

$$
E = \bigcup_{i=1}^k E_{1, i} \times E_{2, i}
$$
where $E_{1,i}$ and $E_{2, i}$ are events in
$\FFF_1$ and $\FFF_2$ respectively.


```{prf:example} Compound events as union of product events
:label: ex-prob-compound-exp-union-products

1. Consider two experiments each of which consists
   of throwing a die.
1. The sample space for both experiments is
   
   $$
   \Omega_1 = \Omega_2 = \{ 1,2,3,4,5,6 \}.
   $$
1. There are $36$ possible outcomes in the compound experiment.
1. The compound sample space is given by

   $$
   \Omega = \Omega_1 \times \Omega_2 = \{
   (1,1), (1,2), \dots, (1,6),
   (2,1), \dots, (2,6),
   \dots,
   (6,1), \dots, (6,6) 
   \}.
   $$
```

### Independent Experiments

```{index} Independent experiments
```
```{prf:definition} Independent experiments
:label: def-prob-independent-experiment

Two experiments are called *independent*
if the outcome of one experiment doesn't
depend on the (past, present or future) outcomes
of the other experiment.
In that case, for every product event $E = E_1 \times E_2$, 
we can write

$$
\PP(E) = \PP(E_1) \PP(E_2).
$$
```

```{prf:example} Repeated coin tosses
:label: ex-prob-repeated-coin-tosses

Consider tossing a coin $n$ times.
1. Assume that the each toss is an independent random experiment.
1. The outcomes of each experiment are $H$ (head) and $T$ (tail).
1. Let $\PP(H) = p$ and $\PP(T) = q = 1 - p$.
1. The outcome of $n$ tosses can be described as a string
   of $n$ letters each of which is $H$ or $T$.
1. There are $2^n$ possible strings. They form the sample space
   of the compound experiment.
1. Let a particular string have $k$ heads and $n-k$ tails. 
1. Then the probability of this string is given by

    $$
    \PP(\zeta_1, \dots, \zeta_n) = \prod_{i=1}^n \PP(\{ \zeta_i \})
    = p^k q^{n - k}.
    $$
1. There are $n \choose k$ strings which consist of $k$ heads and
   $n-k$ tails.
1. Each of these strings (singleton events) are mutually exclusive
   of each other.
1. Hence, by the additivity axiom, the probability of having $k$
   heads and $n-k$ tails in $n$ trials is given by

   $$
   {n \choose k} p^k q^{n - k}.
   $$
```

Let $E$ be a compound event of two independent
experiments given as a disjoint union of product events.
Then the probability measure for the compound event
is given by

```{math}
:label: eq-prob-compound-event-prob-measure-1
\PP(E) = \sum_{i=1}^k \PP(E_{1, i}) \PP(E_{2, i}).
```


