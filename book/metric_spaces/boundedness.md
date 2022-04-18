(sec:ms:boundedness)=
# Boundedness

Let $(X, d)$ be a metric space.


```{prf:definition} Boundedness of a set
:label: def-ms-boundedness-set

A subset $A \subseteq X$ is called *bounded* if there exists
a number $M > 0$ such that 

$$
d(x, y) \leq M \Forall x, y \in A.
$$
```


```{prf:definition} Boundedness of the metric space
:label: def-ms-boundedness-space

A metric space $(X,d)$ is called *bounded* if there exists
a number $M > 0$ such that 

$$
d(x, y) \leq M \Forall x, y \in X.
$$
```
Even if a metric space $(X,d)$ is unbounded, 
it is possible to introduce a metric $\rho$ for it
which makes the metric space $(X, \rho)$ bounded.
See {prf:ref}`res-ms-bounded-metric` for details.

## Diameter

```{prf:definition} Diameter
:label: def-ms-diameter

The *diameter* of a nonempty subset $A$ of $(X, d)$ is defined as:

$$
\diam A \triangleq \sup \{ d(x,y) \ST x, y \in A \}.
$$

$A$ is bounded if its diameter is finite
(i.e. the supremum on the R.H.S. exists). 
Otherwise, it is *unbounded*.
```

```{prf:remark}
:label: rem-ms-bounded-diam-finite

$(X, d)$ is bounded if and only if $\diam X$ is finite. 
```


```{prf:proposition}
:label: res-ms-diam-open-ball-bound

The diameter of an open ball $B(x, r)$ is bounded by $2 r$.
```

```{prf:proof}
Let $y,z \in B(x,r)$. Then by triangle inequality:

$$
d(y,z) \leq d(x,y) + d(x,z) < r + r = 2 r.
$$
Taking supremum on the L.H.S., we get:

$$
\diam B(x,r) = \sup d(y, z) \leq 2 r.
$$
```

For an example where $B(x,r ) < 2 r$, see
{prf:ref}`def-ms-ds-ball-diam`.


```{prf:proposition}
:label: res-ms-zero-diam-singleton

$\diam A = 0$ if and only if $A$ is a singleton set.
```

```{prf:proof}
Let $A$ be singleton. Then, $A = \{ x \}$. 
Then $\diam A = d(x, x ) = 0$. 

For the converse, we proceed as follows:

1. Let $\diam A = 0$. 
1. Assume $A$ is not a singleton.
1. Then there exist distinct $x, y \in A$. 
1. Since $x \neq y$, hence $d(x, y) > 0$. 
1. But then, $\diam A  \geq d(x,y) > 0$. 
1. A contradiction.
1. Hence, $A$ must be a singleton.
```

```{prf:proposition}
:label: res-ms-subset-sub-diam

If $A \subseteq B$, then $\diam A \leq \diam B$.
```

```{prf:proof}

We proceed as follows:

1. Let $x, y \in A$.
1. Then $x, y \in B$.
1. Thus, $d(x,y) \leq \diam B$ (by definition).
1. Taking supremum over all pairs of $x, y \in A$ in the L.H.S., we get:
   $\diam A \leq \diam B$.
```

```{prf:proposition}
:label: res-ms-point-dist-leq-union-diam

Let $x \in A$ and $y \in B$. Then $d(x,y) \leq \diam (A \cup B)$.
```
```{prf:proof}
Since $x$ and $y$ both belong to $A \cup B$, hence, 
by {prf:ref}`definition <def-ms-diameter>`:

$$
d(x,y) \leq \diam (A \cup B).
$$
```

```{prf:proposition}
:label: res-ms-diam-union-leq-sum-diam

If $A \cap B \neq \EmptySet$, then

$$
\diam (A \cup B) \leq \diam A + \diam B.
$$ 
```

```{prf:proof}
Let $x, y \in A\cup B$.

1. If both $x,y \in A$, then $d(x,y) \leq \diam A$.
1. If both $x,y \in B$, then $d(x,y) \leq \diam B$.
1. Now, consider the case when $x \in A$ and $y \in B$.
1. Since $A \cap B \neq \EmptySet$, we can pick $z \in A \cap B$.
1. Then, by triangle inequality:

   $$
   d(x, y) \leq d(x, z) + d(y, z).
   $$
1. Since $x, z \in A$, hence $d(x, z) \leq \diam A$.
1. Since $y, z \in B$, hence $d(y, z) \leq \diam B$.
1. Combining $d(x, y) \leq \diam A + \diam B$.
1. Taking the supremum over all pairs $x, y \in A \cup B$, 
   

   $$
   \diam (A \cup B) \leq \diam A + \diam B.
   $$
```

## Characterization of Boundedness

```{prf:theorem}
:label: def-ms-bounded-set-in-open-ball

A set $A \subseteq X$ is bounded if and only if
there exists $a \in X$  and $r > 0$ such that

$$
A \subseteq B(a, r).
$$

In other words, $A$ is bounded if and only if
$A$ is contained in an open ball.
```

```{prf:proof}

Assume $A$ is bounded.

1. Let $r = \diam A$.
1. Fix some $a \in A$.
1. Consider an open ball $B(a, r + 1)$.
1. Consider any $x \in A$. 
1. Since $r$ is diameter of $A$ and $a, x \in A$, hence
   $d(a,x) \leq r$.
1. Thus, $d (x, a) \leq r < r + 1$.
1. Thus, $x \in B(a, r+1)$.
1. Since $x$ was arbitrary, hence $A \subseteq B(a, r+1)$.

Now assume that there is some $a \in X$ and $r > 0$ such
that $A \subseteq B(a, r)$.

1. Let $x,y \in A$. Then, $x,y \in B(a, r)$.
1. By triangle inequality 
   
   $$
   d(x, y) \leq d(a, x) + d(a, y) < r + r = 2 r.
   $$
1. Taking supremum on the L.H.S. over all $x,y \in A$, we get
   $\diam A \leq 2 r$.
1. Thus, $A$ is bounded.
```