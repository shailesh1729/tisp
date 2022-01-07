# Topology of Real Line

Topology of metric spaces is fully developed in
{ref}`ch:metric-spaces`. In this section, we quickly 
describe the topology of the real line $\RR$ as it 
will be needed for the development of the material
related to {pref:ref}`real functions <def-bra-real-function>`. 
We state a number of results without proving. All of these
results can be proven in the more general context of
metric spaces. Please see {ref}`sec:ms:metric-topology`
for detailed proofs.

## Distance

```{prf:definition} Distance function
:label: def-bra-rl-distance
The *distance function* between two real numbers is defined as 

$$
d(x, y) = | x - y | \Forall x, y \in \RR.
$$
```

```{prf:remark} 
The distance function satisfies following properties:

1. $d(x,y) \geq 0$.
1. $d(x,y) = 0 \iff x = y$.
1. $d(x,y) = d(y,x)$.
1. $d(x,y) \leq d(x,z) + d(z,x)$ 
   due to {prf:ref}`res-rl-distance-triangle-inequality`.

It is a {prf:ref}`metric <def-ms-distance-function>`.
```

## Neighborhoods or Balls

````{prf:definition} Neighborhood
:label: def-bra-neighborhood

Given a real number $x \in \RR$ and $\epsilon > 0$, the set

$$
    V_{\epsilon}(x)  = \{y \in \RR \ST | y - x | < \epsilon\}
$$

is called the $\epsilon$-neighborhood of $x$. 
It is also called an *open ball*.
````

In other words, $V_{\epsilon}(x) = (x - \epsilon, x + \epsilon)$.
A neighborhood is an open interval.


````{prf:definition} Closed Neighborhood
:label: def-bra-closed-neighborhood

Given a real number $x \in \RR$ and $\epsilon > 0$, the set

$$
    C_{\epsilon}(x)  = \{y \in \RR : | y - x | \leq \epsilon\}
$$

is called the $\epsilon$-closed-neighborhood of $x$. 
It is also called a *closed ball*.
````

In other words, $C_{\epsilon}(x) = [x - \epsilon, x + \epsilon]$.
A closed neighborhood/ball is a closed interval.

````{prf:definition} Deleted neighborhood
:label: def-bra-deleted-neighborhood

Given a real number $x \in \RR$ and $\epsilon > 0$, the set
$(x-\epsilon, x) \cup (x, x+\epsilon)$
is called a *deleted-neighborhood* of $x$. 
````
The deleted neighborhood doesn't include $x$.


## Open Sets

```{prf:definition} Open sets
:label: def-rl-open-set

A subset $S$ of $\RR$ is said to be *open* in $\RR$ 
if for every $x \in S$ there exists an "open ball" entirely
within $S$. 

In other words, there exists an $r > 0$ such that
$(x-r, x+r) \subseteq S$. 
```

We claim without proving:

1. Every open ball/neighborhood is an open set.
1. Arbitrary unions of open sets are open sets.
1. Finite intersections of open sets are open sets.
1. Every open interval is an open set.


## Closed Sets

```{prf:definition} Closed sets
:label: def-rl-closed-set

A subset $S$ of $\RR$ is said to be *closed* in $\RR$ 
if $\RR \setminus S$ is open in $\RR$.
```

We claim without proving:

1. $\EmptySet$ and $\RR$ are both open and closed subsets of $\RR$.
1. Every singleton (or a degenerate interval) is a closed set.
1. A closed neighborhood/ball is a closed set.
1. Every closed interval is a closed set.
1. Half open intervals are neither open nor closed.
1. Arbitrary intersections of closed sets are closed sets.
1. Finite unions of closed sets are closed sets.


## Interior

```{prf:definition} Interior point
:label: def-rl-interior-point

A point $x$ is called an interior point of a set $A \subseteq \RR$ if there
exists an open interval $(x-r, x+r)$ such that $(x-r, x+r) \subseteq A$. 
```

By definition an interior point of a set belongs to the set too.
$x \in (x-r, x+r) \subseteq A$. 

```{prf:definition} Interior
:label: def-rl-interior

Let $A \subseteq \RR$. The largest open set in $\RR$ that is contained
in $A$ is called the *interior* of $A$
and is denoted by $\interior A$.
```
Note that $\interior A \subseteq A$.

We claim without proving.

1. Let $O \subseteq A$ be an open set. Then $O \subseteq \interior A$. 
1. The interior of a set $A$ is the collection of 
   all the interior points of $A$.
1. $A$ is open if and only if $A = \interior A$. 


## Closure

```{prf:definition} Closure point
:label: def-rl-closure-point

A point $x \in \RR$ is called a *closure point* of a subset $A$ of $\RR$ 
if every open ball at $x$ contains (at least) one point in $A$.

In other words:

$$
(x-r, x+r) \cap A \neq \EmptySet \Forall r > 0.
$$
```

```{prf:definition} Closure
:label: def-rl-closure

Let $A \subseteq \RR$. The smallest closed set in $\RR$ that contains
$A$ is called the *closure* of $A$
and is denoted by $\closure A$.
```


We claim without proving:

1. Every point in $A$ is a closure point of $A$.
1. Let $C$ be a closed subset of $\RR$ such that $A \subseteq C$.
   Then $\closure A \subseteq C$.
1. The closure of a set $A$ is the collection of 
   all the closure points of $A$.
1. $A$ is closed if and only if $A = \closure A$. 
1. Let $A \subseteq \RR$. Then

   $$
   \RR \setminus (\interior A) = \closure (\RR \setminus A).
   $$

## Boundary

```{prf:definition} Boundary point
:label: def-rl-boundary-point

A point $x \in \RR$ is called a *boundary point* of $A$ if
every open ball $(x-r, x+r)$ at $x$ contains points from 
$A$ as well as $\RR \setminus A$. 
```

```{prf:definition} Boundary
:label: def-rl-boundary

The *boundary* of a set $A \subseteq \RR$, 
denoted by $\boundary A$ is defined as
the set of all boundary points of $A$.
```

We claim without proving:

1. $\boundary A = \closure A \setminus \interior A$.
1. For intervals $(a,b)$, $(a,b]$, $[a, b)$ 
   and $[a,b]$, the boundary points are $a$ and $b$.

## Accumulation


```{prf:definition} Accumulation point
:label: def-rl-accumulation-point

A point $x \in \RR$ is called an *accumulation point* of a set $A \subseteq \RR$,
if every open ball $(x-r,x+r)$ contains a point in $A$ distinct from $x$.

$$
(x-r, x+r) \cap A \setminus \{ x \} \neq \EmptySet \Forall r > 0.
$$
```

```{prf:definition} Derived set
:label: def-rl-derived-set

The set of accumulation points of a set $A$ is called its *derived set* 
and is denoted by $A'$.
```

```{prf:definition} Isolated point
:label: def-rl-isolated-point

A point $x \in A$ is called isolated if there is an open ball
$(x-r, x+r)$ which doesn't contain any other point of $A$.
```

We claim without proving:

1. Every accumulation point is a closure point.
1. A closure point is either an accumulation point or an isolated point.
1. $\closure A = A \cup A'$.
1. A set is closed if and only if it contains all its accumulation points.
