# Integers

We provide an axiomatic description of integers and natural numbers.
We introduce the set of integers denoted by $\ZZ$ as a set which
is equipped with two functions 

* addition ($+ : \ZZ \times \ZZ \to \ZZ$)
* multiplication ($- : \ZZ \times \ZZ \to \ZZ$)

which satisfy the axioms described below.

## Arithmetic Axioms

```{prf:axiom} Closure laws
:label: ax-integer-closure

If $a, b \in \ZZ$ then

$$
a + b \in \ZZ
$$
and

$$
a \cdot b \in \ZZ.
$$
```

```{prf:axiom} Commutative laws
:label: ax-integer-commutativity

If $a, b \in \ZZ$ then

$$
a + b = b + a
$$
and

$$
a \cdot b = b \cdot a.
$$
```

```{prf:axiom} Associative laws
:label: ax-integer-associativity

If $a, b, c \in \ZZ$ then

$$
(a + b) + c = a + (b + c)
$$
and

$$
(a \cdot b) \cdot c = a \cdot (b \cdot c).
$$
```

```{prf:axiom} Distributive law
:label: ax-integer-distributive

If $a, b, c \in \ZZ$ then

$$
a \cdot (b + c) = a \cdot b + a \cdot c
$$
and

$$
(a + b) \cdot c = a \cdot c + b \cdot c.
$$
```

```{prf:axiom} Additive identity
:label: ax-integer-additive-identity

There exists an element $0 \in \ZZ$ such that

$$
a + 0 = 0 + a = a
$$
for every $a \in \ZZ$.
```

```{prf:axiom} Multiplicative identity
:label: ax-integer-multiplicative-identity

There exists an element $1 \in \ZZ$ with $1 \neq 0$
such that

$$
a \cdot 1 = 1 \cdot a = a
$$
for every $a \in \ZZ$.
```

```{prf:axiom} Additive inverse
:label: ax-integer-additive-inverse

For every $a \in \ZZ$, there exists an element $x \in \ZZ$
such that

$$
a + x = x + a = 0.
$$
$x$ is called the *additive inverse* of $a$
or the negative of $a$
and is denoted by $-a$.
```


## Implications of Integer Axioms

```{prf:theorem}  Multiplication by zero
:label: res-integer-mult-zero

For any $a \in \ZZ$, we have $0 \cdot a = a \cdot 0 = 0$.
```
```{prf:proof}
Let $b = - (a \cdot 0)$. Then $ a \cdot 0 + b = 0$.
Now

$$
& 0 + 0 = 0 & \text{ additive identity} \\
\implies & a \cdot (0 + 0 ) = a \cdot 0 & \text{ multiplication by } a\\
\implies & a \cdot 0 + a \cdot 0 = a \cdot 0 & \text{ distributive law}\\
\implies & (a \cdot 0 + a \cdot 0) + b = a \cdot 0 + b = 0 
& \text{ additive inverse} \\
\implies & a \cdot 0 + (a \cdot 0 +  b) = 0 
& \text{ associative law} \\
\implies & a \cdot 0 + 0 = 0 
& \text{ additive inverse} \\
\implies & a \cdot 0 = 0 
& \text{ additive identity}.
$$

By commutativity, we have

$$
0 \cdot a = a \cdot 0 = 0.
$$
```
```{prf:theorem}  Multiplication by $-1$
:label: res-integer-mult-min-1

For any $a \in \ZZ$, we have $-a = (-1) \cdot a$.
```

```{prf:proof}
We start with

$$
0 &= 0 \cdot a & \text{ multiplication by zero}\\
& = [1 + (-1)] \cdot a & \text{ additive inverse}\\
& = 1 \cdot a  + (-1) \cdot a & \text{ distributive law}\\
& = a  + (-1) \cdot a & \text{ multiplicative identity}.
$$

Adding by $-a$ on both sides, we get:

$$
& -a = (-a) + 0 = (-a) + (a  + (-1) \cdot a) & \text{ additive identity}\\
\implies & -a = (-a + a) + (-1) \cdot a & \text{ associative law}\\
\implies & -a = 0 + (-1) \cdot a & \text{ additive inverse}\\
\implies & -a = (-1) \cdot a & \text{ additive identity}.
$$
```

```{prf:theorem}
:label: res-integer-mult-min-1-min-1

$$
(-1) \cdot (-1) = 1.
$$
```

```{prf:proof}
We have

$$
(-1) \cdot (-1)  + (-1)
&=  (-1) \cdot (-1)  + (-1) \cdot 1  & \text{ multiplicative identity}\\
&= (-1) \cdot[(-1) + 1] & \text{ distributive law}\\
&= (-1) \cdot 0 & \text{ additive inverse}\\
&= 0 & \text{ multiplication by zero}.
$$
Adding by $1$ on both sides, we get:

$$
& [(-1) \cdot (-1)  + (-1)] + 1 = 0 + 1 = 1 & \text{ additive identity} \\
\implies & (-1) \cdot (-1)  + [(-1) + 1] = 1 & \text{ associative law} \\
\implies & (-1) \cdot (-1)  + 0 = 1 & \text{ additive inverse} \\
\implies & (-1) \cdot (-1) = 1 & \text{ additive identity}.
$$
```

```{prf:definition} Subtraction
:label: def-integer-subtraction

For any $a, b \in \ZZ$, a binary operation $- : \ZZ \times \ZZ \to \ZZ$
is defined as 

$$
a - b = a + (-b).
$$
```

## Natural Numbers

We introduce the natural numbers,
denoted as $\Nat$ as a subset of integers
that satisfy the following two axioms.

```{prf:axiom} Closure axiom of natural numbers
:label: ax-integer-closure-nat

If $a, b \in \Nat$, then $a + b \in \Nat$
and $a \cdot b \in \Nat$.
```

```{prf:axiom} Law of trichotomy
:label: ax-integer-trichotomy

For every integer $a \in \ZZ$, exactly one of the following
is true.

$$
a \in \Nat
\text{ or } -a \in \Nat
\text{ or } a = 0.
$$
```
The law of trichotomy implies that for every
nonzero integer, its additive inverse is
distinct from it since either $a \in \Nat$
or $-a \in \Nat$ but not both.

Axiomatic description of natural numbers doesn't
say whether $1 \in \Nat$ or $1 \notin \Nat$.
We prove that $1 \in \Nat$ in the next result.

```{prf:theorem} One is a natural number
:label: res-integer-one-nat

$1 \in \Nat$.
```

```{prf:proof}
By {prf:ref}`ax-integer-trichotomy` either
$1 \in \Nat$ or $-1 \in \Nat$ or $1 = 0$.

1. Since $1 \neq 0$, hence either $1 \in \Nat$ or $-1 \in \Nat$.
1. For contradiction assume that $-1 \in \Nat$.
1. Since $-1 \in \Nat$, hence by {prf:ref}`ax-integer-closure-nat`,
   $(-1) \cdot (-1) \in \Nat$.
1. By {prf:ref}`res-integer-mult-min-1-min-1`, we have
   $(-1) \cdot (-1) = 1$.
1. Hence $1 \in \Nat$.
1. But since $-1 \in \Nat$, hence $1 \notin \Nat$ due to
   {prf:ref}`ax-integer-trichotomy`. A contradiction.
1. Hence $-1 \notin \Nat$.
1. Hence we must have $1 \in \Nat$.
1. We can see that this is consistent with
   {prf:ref}`ax-integer-closure-nat`
   since $1 \cdot 1 = 1 \in \Nat$.
```

## Order

```{prf:definition} Order on integers
:label: def-integer-order

If $a, b \in \ZZ$, then we define $a < b$ if and only if
$b - a \in \Nat$.

If $a < b$, then we also write $b > a$.
```

```{prf:theorem} One is greater than zero
:label: res-integer-one-gt-zero

$1 > 0$.
```

```{prf:proof}
We have

$$
1 - 0 = 1 + (-0) = 1 + 0 = 1 \in \Nat.
$$
Hence $1 > 0$.
```




## Construction of Integers

```{prf:observation} Construction of integers
:label: rem-integer-construction

We can see that the above axioms are sufficient
to construct the entire set of integers.
Let us start with assuming that we know 
nothing about the set of integers except
that they satisfy the axioms described above.
In particular, we don't know that $1 \in \Nat$
or the integers $2,3,4,\dots,$ exist.

1. {prf:ref}`ax-integer-additive-identity` says
   that there exists an element in $\ZZ$ denoted as $0$.
1. {prf:ref}`ax-integer-multiplicative-identity` says
   that there exists an element in $\ZZ$ denoted as $1$
   such that $1 \neq 0$.
1. Thus, at least two different elements exist in $\ZZ$
   namely $0$ and $1$.
1. {prf:ref}`ax-integer-additive-inverse` says that
   there exists an additive inverse $-1$ of $1$ such that
   $(-1) + 1 = 1 + (-1) = 0$.
1. We need to show that $-1 \notin \{ 0, 1 \}$.
1. We must have $0 \neq -1$.
   Otherwise, we would have

   $$
   1 = 1 + 0 = 1 + (-1) = 0
   $$
   a contradiction.
1. In {prf:ref}`res-integer-one-nat`, we showed that
   $1 \in \Nat$.
1. By {prf:ref}`ax-integer-trichotomy` $-1 \notin \Nat$.
1. Hence $-1 \neq 1$.
1. Hence $-1, 0, 1$ are three distinct numbers belonging to $\ZZ$. 
1. By {prf:ref}`ax-integer-closure` a number $b = 1 + 1$
   belongs to $\ZZ$.
1. We claim that $b \notin \{ -1, 0, 1\}$.
   1. By {prf:ref}`ax-integer-closure-nat`, $b = 1 + 1 \in \Nat$.
   1. Since $0$ and $-1$ are not in $\Nat$, hence $b$ cannot
      be either one of them.
   1. For contradiction assume that $b = 1$.
   1. Then

      $$
      0 = 1 + (-1) = b + (-1) = (1 + 1) + (-1) = 1 + (1 + (-1)) = 1 + 0 = 1.
      $$
   1. But $0 \neq 1$, a contradiction.
   1. Hence $b= 1 + 1 \notin \{ -1, 0, 1\}$.
1. We assign the label $2$ to the distinct integer $1+1$.
   Note that the existence of a number $2$ distinct from
   $-1,0,1$ has been deduced directly from the axioms.
   $2$ is just a label assigned to this number for convenience.
1. Then $-2 \in \ZZ$ and $-2 \notin \Nat, -2 \neq 0$ due to
   {prf:ref}`ax-integer-trichotomy`.
1. We can also show that $-2 \neq -1$.
1. Thus, we have five distinct integers $-2,-1,0,1,2 \in \ZZ$.
1. Continuing in this manner, for every $n \in \Nat$, the
   integer $n + 1 \in \Nat$ and $n+1$ must be distinct
   from the integers $1,2,\dots,n$.
1. In this sequence, every new integer is a successor
   of the previous integer.
   This construction is similar to Peano axioms.
1. {prf:ref}`ax-integer-additive-inverse` leads to
   the existence of the negative integers.


This construction shows that closure axiom of natural numbers
and law of trichotomy are essential for the construction
of integers. Without these laws, there are several other
sets which can satisfy the axioms {prf:ref}`ax-integer-closure`
through {prf:ref}`ax-integer-additive-inverse` with an
appropriate choice of addition and multiplication functions.
But only the set of integers can satisfy the additional
axioms of closure and trichotomy.
```

## Informal Definitions

We end this section with the casual descriptions
of the set of integers and natural numbers
with which we are normally familiar.

```{prf:definition} Integers
:label: def-alg-integer

The *set of all integers* is the set

$$
\ZZ = \{\dots, -3,-2,-1,0,1,2,3, \dots \}.
$$
```

```{prf:definition} Natural numbers
:label: def-alg-natural-number

The *set of all natural numbers* is the set

$$
\Nat = \{1,2,3, \dots \}.
$$
```

