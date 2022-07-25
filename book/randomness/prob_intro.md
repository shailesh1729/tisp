(sec:prob:intro)=
# Introduction

Our notes will be based on the axiomatic treatment of probability.

```{index} Random experiment
```
```{prf:definition} Random experiment
:label: def-prob-random-experiment

A *random experiment* is an experiment in which the
outcomes are nondeterministic.
In other words, different outcomes can occur each time
the experiment is run.
```

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

```{index} Event
```
```{prf:definition} Event
:label: def-prob-event

An *event* is a subset of the sample space of
a random experiment that satisfies some given
constraints.
```

Events are the meaningful subsets of the
sample space to which probabilities can
be assigned. We will develop the notion
of events further in the following.

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



## Sigma Fields


```{prf:definition} Field
:label: def-prob-field

Consider the sample space $\Omega$
and a certain collection of subsets of $\Omega$ denoted by $\MMM$.
Let $E$ and $F$ be arbitrary members of $\MMM$.

We say that $\MMM$ forms a *field* if meets the following
constraints:

1. $\EmptySet \in \MMM$.
1. $\Omega \in \MMM$.
1. If $E, F \in \MMM$ then $E \cup F \in \MMM$ and $E \cap F \in \MMM$.
1. If $E \in \MMM$ then $\Omega \setminus E = E^c \in \MMM$.

In other words,
$\MMM$ contains the null and certain events,
$\MMM$ is closed under finite union and intersection,
and $\MMM$ is closed under complement.
```

```{note}
The notion of field here is different from the notion
of algebraic fields (e.g. $\RR$ and $\CC$).
```

```{index} $\sigma$ field, $\sigma$ algebra
```
```{prf:definition} $\sigma$ field
:label: def-prob-sigma-field

Consider an infinite sample space $\Omega$
and a certain collection of subsets of $\Omega$ denoted by $\FFF$.
We say that $\FFF$ is a $\sigma$-*field* if
it is a field and it is closed
under countable unions, intersections and complements.
This is also known as a *\sigma$-algebra.
```


```{prf:definition} Borel field
:label: def-prob-borel-field


```