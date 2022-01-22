Real Valued Functions
=============================

In this section, we discuss results related
to real valued functions on metric spaces.
It is suggested to review the material from
{ref}`sec:bra:real-valued-functions` on arbitrary sets.
We assume $(X,d)$ to be an arbitrary metric space in this section.
Unless otherwise specified, $f : X \to \RR$ is a partial real
valued function from $X$ to $\RR$
with $\dom f \subseteq X$.

## Extreme Values


```{prf:definition} Local extreme value
We say that $f(a)$ is a *local extreme value* of $f$ at $a \in \dom f$ 
if there exists
$\delta > 0$ such that $f(x) - f(a)$ doesn't change sign on
$B(a, \delta) \cap \dom f$.

More specifically,

1. $f(a)$ is a *local maximum value* of $f$ if for some $\delta > 0$:

   $$
   f(x) \geq f(a) \Forall x \in B(a, \delta) \cap \dom f.
   $$ 
1. $f(a)$ is a *local minimum value* of $f$ if for some $\delta > 0$:

   $$
   f(x) \geq f(a) \Forall x \in B(a, \delta) \cap \dom f.
   $$ 

The point $x=a$ is called a *local extreme point* of $f$ or more 
specifically, a *local maximum* or a *local minimum* point of $f$.
```

```{prf:definition} Global maximum
We say that $f : X \to \RR$ attains a *global maximum*
at some $a \in \dom f$, if:

$$
f(x) \leq f(a) \Forall x \in \dom f.
$$
```

```{prf:definition} Global minimum
We say that $f : X \to \RR$ attains a *global minimum*
at some $a \in \dom f$, if:

$$
f(x) \geq f(a) \Forall x \in \dom f.
$$
```

```{prf:theorem} Extreme value theorem
Let $f : X \to \RR$ be continuous. 
Let $K$ be a nonempty compact subset of $\dom f$. 
Then, the set $f(K)$ is closed and bounded.
Also, there exists $a$ and $b$ in $K$ such that

$$
f(a) = \inf f(K) \text{ and } f(b) = \sup f(K);
$$
i.e., $f$ attains its supremum and infimum over the values in $f(K)$.
```

```{prf:proof}
Recall from {prf:ref}`res-ms-compact-continuous-map`
that continuous image of a compact set is compact. 
Hence, $f(A)$ is compact. 

But the compact subsets of $\RR$ are closed and bounded.
Hence, $f(A)$ is closed and bounded. 

Since $f(A)$ is closed and bounded, hence it contains
a supremum and an infimum.

Let $y = \inf f(A)$. Since $y \in f(A)$, hence
there exists $a \in \dom f$ such that $f(a) = y$.

Let $z = \sup f(A)$. Since $z \in f(A)$, hence
there exists $b \in \dom f$ such that $f(b) = z$.
```

Extreme value theorem is useful in optimization
problems. If it is possible to identify the
feasible set of input values as a closed and
bounded set, then it is possible to indicate
if the optimization problem has a solution 
or not. Although, the theorem doesn't help
in identifying the solution as such.

```{prf:example}
Consider the optimization problem of maximizing
the volume of a box with the constraints:

$$
w + h + d \leq 6
$$
where $w$ indicates the width, $h$ indicates the
height and $d$ indicates the depth of the box.

We can define volume as a function $v : \RR^3 \to \RR$ as 

$$
v = w h d
$$
where each input vector $\bx \in \RR^3$ is 
a triplet $(w, h, d)$.

Now, note the implicit assumption that width,
height and depth cannot be negative.

Thus, we have the following constraints:

$$
w \geq 0, h \geq 0, d \geq 0, w + h + d \leq 6.
$$

These constraints define a simplex in $\RR^3$ which
is a closed and bounded set (thus compact). Hence,
the range of function values is also closed and
bounded. Hence, it is possible to choose
a configuration which maximizes the volume. 
```

## Closed Functions

```{prf:definition} Closed function
:label: def-ms-closed-function

A real valued function $f : X \to \RR$ is *closed* 
if for each $\alpha \in \RR$,
the corresponding sublevel set is closed. 

In other words, the set:

$$
\{ x \in \dom f \,|\, f(x) \leq \alpha \}
$$

is closed for every $\alpha \in \RR$.
```
```{prf:proposition}
The epigraph of a closed function is closed.
```

```{prf:proposition}
If $f: X \to \RR$ is continuous and $\dom f$ is closed, then 
$f$ is closed.
```

```{prf:proposition}
If $f: X \to \RR$ is continuous and $\dom f$ is open, then
$f$ is closed if and only if $f$ converges to $\infty$ along
every sequence converging to a boundary point of $\dom f$. 
```
