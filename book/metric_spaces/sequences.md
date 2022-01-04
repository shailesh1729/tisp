# Sequences

Let $(X, d)$ be a metric space.


## Accumulation Points


```{prf:definition} Accumulation point
:label: def-ms-accumulation-point

A point $x \in X$ is called an *accumulation point* of a set $A \subseteq X$,
if every open ball $B(x,r)$ contains a point in $A$ distinct from $A$.

$$
B(x, r) \cap A \setminus \{ x \} \neq \EmptySet \Forall r > 0.
$$
```

Note that an accumulation point need not belong to the set $A$.

```{prf:remark} 
Every accumulation point is a closure point.
```


Although, every closure point need not be an accumulation point.

```{prf:definition} Derived set
:label: def-ms-derived-set

The set of accumulation points of a set $A$ is called its *derived set* 
and is denoted by $A'$.
```

```{prf:definition} Isolated point
:label: def-ms-isolated-point

A point $x \in A$ is called isolated if there is an open ball
$B(x, r)$ which doesn't contain any other point of $A$.

In other words, there exists an $r > 0$ such that:

$$
B(x, r) \cap A \setminus \{ x \} = \EmptySet.
$$
```

```{prf:proposition} 
A closure point is either an accumulation point or an isolated point.
```

```{prf:proof}
Let $x \in \closure A$. Assume that $x$ is not an accumulation point.

We need to show that $x \in A$ and $x$ is isolated.

1. Since $x$ is not an accumulation point, there exists $r > 0$ such that 
   $B(x, r) \cap A \setminus \{ x \} = \EmptySet$.
1. Since $x$ is a closure point, hence 
   $B(x,r) \cap A$ is not empty.
1. Then, $B(x, r) \cap A$ must be $\{ x \}$. 
1. Thus, $x \in A$.
1. Finally, since $B(x, r) \cap A \setminus \{ x \} = \EmptySet$, 
   $x$ is an isolated point of $A$.
```


```{prf:proposition} 
$$
\closure A = A \cup A'.
$$
```
This is a restatement of the previous result.

```{prf:proposition} 
A set is closed if and only if it contains all its accumulation points.
```

```{prf:proof}
$A' \subseteq A \implies A \cup A' = A$. But $A \cup A' = \closure A$.
Thus, $A' \subseteq A \implies A = \closure A$.

$A = \closure A \implies  A =  A \cup A' \implies A' \subseteq A$.
```

## Sequences

````{prf:definition}
:label: def-ms-sequence

A {prf:ref}`sequence <def-st-sequence>` in a metric space $(X,d)$ is a 
function $f : \Nat \to X$.
````
A sequence can be thought of as an ordered (countable) list of 
points in $X$.


## Convergence


````{prf:definition} Convergence
:label: def-ms-convergence

A sequence $\{ x_n \}$ in a metric space $(X,d)$ 
is said to *converge* to $x \in X$ 
if for every $\epsilon > 0$,
there exists a natural number $n_0$ (depending upon $\epsilon$) 
such that

$$
    d (x_n,x) < \epsilon \Forall n > n_0.
$$

The point $x$ is called the *limit* of the sequence $\{ x_n \}$, 
and we write $x_n \to x$ or $x = \lim x_n$.
````

````{prf:remark}
The sequence $\{x_n\}$ gives a sequence of real numbers
$\{ y_n \}$ where $y_n = d(x_n, x)$. 

Thus, $\{ x_n \}$ converges if $\lim d(x_n, x) = 0$.
````


````{prf:theorem} Sequence Limit Uniqueness
:label: res-ms-sequence-limit-uniqueness

A sequence of points can have utmost one limit.
````

````{prf:proof}
If a sequence doesn't converge, then there is nothing to prove. 
Otherwise, suppose a sequence $\{ x_n \}$ converges to 
two limits $x$ and $y$. 
Thus, for every $\epsilon > 0$, there
exist $n_1, n_2 \in \Nat$ such that 
$d(x_n,x) < \epsilon \Forall n > n_1$  and
$d(x_n, y) < \epsilon \Forall n > n_2$. 
Now, choose $n_0 = \max (n_1, n_2)$.
Then, by triangle inequality, for every $n > n_0$

$$
    0 \leq d(x, y) \leq d(x, x_n) + d(x_n, y)  < \epsilon + \epsilon = 2\epsilon.
$$

Since this is true for all $\epsilon > 0$, hence $d(x,y)=0$.
This means that $x = y$ (Identity of indiscernibles).
````
