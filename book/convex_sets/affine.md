# Affine Sets

(def:line)=
```{prf:definition}
Let $x_1$ and $x_2$ be two points in $\RR^N$. Points of the form

$$
y = \theta x_1 + (1 - \theta) x_2 \text{ where } \theta \in \RR
$$ 
form a *line* passing through $x_1$ and $x_2$.
```

* at $\theta=0$ we have $y=x_2$.
* at $\theta=1$ we have $y=x_1$.
* $\theta \in [0,1]$ corresponds to the points belonging 
  to the \[closed\] *line segment* between $x_1$ and $x_2$.

We can also rewrite $y$ as 
$$
y = x_2 + \theta (x_1 - x_2)
$$
In this definition:

* $x_2$ is called the *base point* for this line.
* $x_1 - x_2$ defines the *direction* of the line.
* $y$ is the sum of the base point and the direction scaled by the parameter $\theta$.
* As $\theta$ increases from $0$ to $1$, $y$ moves from $x_2$ to $x_1$.

(def:affine_set)=
```{prf:definition}
A set $C \subseteq \RR^N$ is **affine** if the line through
any two distinct points in $C$ lies in $C$.

In other words, for any $x_1, x_2 \in C$, we have $\theta x_1 + (1 - \theta) x_2 \in C$ 
for all $\theta \in \RR$.
```

If we denote $\alpha = \theta$ and $\beta = (1 - \theta)$ we see that 
$\alpha x_1 + \beta x_2$ represents a linear combination of points in $C$
such that $\alpha + \beta = 1$.

The idea can be generalized in following way.

(def:affine_combination)=
```{prf:definition}
A point of the form $\theta_1 x_1 + \dots + \theta_k x_k$ where 
$\theta_1 + \dots + \theta_k = 1$ with $\theta_i \in \RR$ and $x_i \in \RR^N$, is called
an **affine combination** of the points $x_1,\dots,x_k$.
```

It can be shown easily that an affine set $C$ contains all affine combinations of its points.
```{prf:remark}
If $C$ is an affine set, $x_1, \dots, x_k \in C$, and $\theta_1 + \dots + \theta_k = 1$, then
the point $y = \theta_1 x_1 + \dots + \theta_k x_k$ also belongs to $C$. 
```

```{prf:lemma}
Let $C$ be an affine set and $x_0$ be any element in $C$. Then the set

$$
    V = C  - x_0 = \{ x  - x_0 | x \in C\}
$$

is a subspace of $\RR^N$.
```
To show that $V$ is indeed a vector space, we can show that
every linear combination of two arbitrary elements in $V$
belongs to $V$.

```{prf:proof}
Let $v_1$ and $v_2$ be two elements in $V$. Then by definition, there exist $x_1$ and $x_2$ in $C$ such that

$$
    v_1 = x_1 - x_0
$$

and 

$$
    v_2 = x_2 - x_0
$$

Thus 

$$
    a v_1 + v_2 = a (x_1 - x_0) + x_2 - x_0 = (a x_1 + x_2  - a x_0 )  - x_0 \Forall a \in \RR.
$$

But since $a + 1 - a = 1$, hence $x_3 = (a x_1 + x_2  - a x_0 ) \in C$ (an affine combination). 

Hence $a v_1 + v_2 = x_3 - x_0 \in V$ [by definition of $V$].

Thus any linear combination of elements in $V$ belongs to $V$. Hence $V$ is a subspace of $\RR^N$.
```

With this, we can use the following notation:

$$
    C = V + x_0 = \{ v + x_0 | v \in V\}
$$

i.e. an affine set is a subspace with an offset.
```{prf:remark}
Let $C$ be an affine set and let $x_1$ and $x_2$ be two distinct elements.
Let $V_1 = C - x_1$ and $V_2 = C - x_2$, then the subspaces $V_1$ and $V_2$ 
are identical.
```
Thus the subspace $V$ associated with an affine set $C$ doesn't depend upon
the choice of offset $x_0$ in $C$.

(def:affine_dimension)=
```{prf:definition}
We define the **affine dimension** of an affine set $C$ as the dimension
of the associated subspace $V = C - x_0$ for some $x_0 \in C$. 
```

```{prf:example} Solution set of linear equations
We show that the solution set of linear equations forms an affine set.

Let $C = \{ x | A x = b\}$ where $A \in \RR^{M \times N}$ and $b \in \RR^M$.

Let $C$ be the set of all vectors $x \in \RR^N$ which satisfy the system of linear
equations given by $A x = b$. 
Then $C$ is an affine set.

Let $x_1$ and $x_2$ belong to $C$.  Then we have

$$
    A x_1 = b
$$ 

and 

$$
    A x_2 = b
$$

Thus 

$$
    &\theta A x_1 + ( 1 - \theta ) A x_2 = \theta b + (1 - \theta ) b\\
    &\implies A (\theta x_1 + (1  - \theta) x_2) = b\\
    &\implies (\theta x_1 + (1  - \theta) x_2) \in C
$$

Thus $C$ is an affine set.

The subspace associated with $C$ is nothing but the
null space of $A$ denoted as $\NullSpace(A)$.
```

```{prf:remark}
Every affine set can be expressed as the solution set of a 
system of linear equations.
```


```{prf:example} More affine sets
*  The empty set $\EmptySet$ is affine.
*  A singleton set containing a single point $x_0$ is affine.
Its corresponding subspace is $\{0 \}$ of zero dimension.
*  The whole euclidean space $\RR^N$ is affine.
*  Any line is affine. The associated subspace is a line parallel to it
which passes through origin.
*  Any plane is affine. If it passes through origin, it's a
subspace. The associated subspace is the plane parallel to it
which passes through origin.
```

(def:affine_hull)=
```{prf:definition}
The set of all affine combinations of points in some arbitrary set 
$S \subseteq \RR^N$ 
is called the **affine hull** of $S$ and denoted as $\AffineHull(S)$:

$$
    \AffineHull(S) = \{\theta_1 x_1 + \dots + \theta_k x_k | x_1, \dots, x_k \in S \text{ and } \theta_1 + \dots + \theta_k = 1\}.
$$
```

```{prf:remark}
The affine hull is the smallest affine set containing $S$. In other words, let $C$ be any affine set
with $S \subseteq C$. Then $\AffineHull(S) \subseteq C$.
```

(def:affine_independence)=
```{prf:definition}
A set of vectors $v_0, v_1, \dots, v_K \in \RR^N$ is called **affine independent**,
if the vectors $v_1 - v_0, \dots, v_K - v_0$ are linearly independent.
```

In other words, the difference vectors $v_k - v_0$ 
belong to the associated subspace. 

If the associated subspace has dimension $L$ then a maximum of $L$ vectors can 
be linearly independent in it. Hence a maximum of $L+1$ vectors can be affine
independent for the affine set.
