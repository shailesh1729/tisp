# Integers

We provide an axiomatic description of integers and natural numbers.
We introduce the set of integers denoted by $\ZZ$ as a set which
is equipped with two functions

* addition ($+ : \ZZ \times \ZZ \to \ZZ$)
* multiplication ($- : \ZZ \times \ZZ \to \ZZ$)

which satisfy the axioms described below.

## Arithmetic Axioms

### Closure

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

### Commutativity

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

###  Associativity

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

### Distributive Law

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

### Identity

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

### Inverse

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

We can now see that

$$
(- a) \cdot b 
&= ((-1) \cdot a) \cdot b = (-1) \cdot (a \cdot b)\\
&= - (a \cdot b). 
$$

Similarly

$$
a \cdot (-b) 
&= a \cdot ((-1) \cdot b) =  a \cdot (b \cdot (-1))\\
&= (a \cdot b) \cdot (-1) = (-1) \cdot (a \cdot b)\\
&= - (a \cdot b). 
$$

Hence

$$
(- a) \cdot b = - (a \cdot b) = a \cdot (-b).
$$


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

We can now see that

$$
(-a) \cdot (- b)
&= (-1) \cdot (a \cdot (-b))
= (-1) \cdot ( (-1) \cdot (a \cdot b) ) \\
&= ((-1) \cdot (-1)) \cdot (a \cdot b)
= 1 \cdot (a \cdot b)\\
= a \cdot b.
$$

### Subtraction

```{prf:definition} Subtraction
:label: def-integer-subtraction

For any $a, b \in \ZZ$, a binary operation $- : \ZZ \times \ZZ \to \ZZ$
is defined as 

$$
a - b = a + (-b).
$$
```
We can see that

$$
& a - b = 0\\
& \iff a + (-b) = 0 \\
& \iff (a + (-b)) + b = 0 + b \\
& \iff a + ((-b) + b) = b \\
& \iff a + 0 = b \\
& \iff a = b.
$$
In short $a - b = 0 \iff a = b$.

Similarly we can see that

$$
a \cdot c - b \cdot c
&= a \cdot c + (- (b \cdot c)) \\
&= a \cdot c + ((- b) \cdot c) \\
&= (a + (- b)) \cdot c \\
&= (a - b) \cdot c.
$$
In short $a \cdot c - b \cdot c = (a - b) \cdot c$.
Similarly, $a \cdot b - a \cdot c = a \cdot (b - c)$.


## Natural Numbers

We introduce the natural numbers,
denoted as $\Nat$ as a subset of integers
that satisfy the following two axioms.

### Closure

```{prf:axiom} Closure axiom of natural numbers
:label: ax-integer-closure-nat

If $a, b \in \Nat$, then $a + b \in \Nat$
and $a \cdot b \in \Nat$.
```

### Trichotomy

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
The law of trichotomy states that $0$ is
not a natural number.

The law of trichotomy also implies that for every
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
```{prf:theorem}
:label: res-integer-nat-gt-zero

Let $a \in \Nat$. Then $a > 0$.
```

```{prf:proof}
Since $a \in \Nat$ hence

$$
a - 0  = a + (-0) = a + 0  = a \in \Nat.
$$
Hence $a > 0$.
```

```{prf:theorem}
:label: res-integer-nat-sum-gt-parts

Let $a, b \in \Nat$. Let $c = a + b$.
Then $c > a$ and $c > b$.
```

```{prf:proof}
We have

$$
c - a =  (a + b) - a = (b + a) + (-a) = b + (a + (-a)) = b + 0 = b. 
$$
Hence $c - a = b \in \Nat$. Hence $c > a$.
Similarly $c > b$.
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
```

## Zero Divisor

```{index} Zero divisor
```
```{prf:definition} Zero divisor
:label: def-integer-zero-divisor

We say that an integer $a$ is a *zero divisor*
or *divisor of zero* if and only if $a \neq 0$
and there exists an integer $b \neq 0$ such
that $a \cdot b = 0$.
```

We now show that $\ZZ$ doesn't contain any zero divisors.

```{prf:theorem} No zero divisors
:label: res-integer-no-zero-divisors

If $a, b \in \ZZ$ and $a \cdot b = 0$ then either
$a = 0$ or $b = 0$ or both.

In other words, the set of integers contains no zero divisors.
```

```{prf:proof}
Suppose that $a, b \in \ZZ$ and $a \cdot b = 0$.
For contradiction assume that $a \neq 0$ and $b \neq 0$.

1. By law of trichotomy either $a \in \Nat$ or $-a \in \Nat$.
1. Similarly either $b \in \Nat$ or $-b \in \Nat$.
1. Thus, we have 4 possible cases.

We recall that

$$
a \cdot b = (-a) \cdot (-b)
\text{ and}
- (a \cdot b) = (-a) \cdot b = a \cdot (-b).
$$
We shall consider the four possible cases and
arrive at contradiction for each case.

1. $a, b \in \Nat$. Then by closure $0 = a \cdot b \in \Nat$.
   A contradiction.
1. $a \in \Nat$ and $-b \in \Nat$.
   Then $a \cdot (-b) = - (a \cdot b) = - 0 = 0 \in \Nat$.
   A contradiction.
1. $-a \in \Nat$ and $b \in \Nat$
   Then $(-a) \cdot b = - (a \cdot b) = -0 = 0 \in \Nat$.
   A contradiction.
1. $-a \in \Nat$ and $-b \in \Nat$.
   Then $(-a) \cdot (-b) = - (a \cdot b) = - 0 = 0 \in \Nat$.
   A contradiction.

Therefore we must have either $a = 0$ or $b = 0$
whenever $a \cdot b = 0$.
```


```{note}
The idea of zero divisors becomes important
in the theory of rings. While the set
of integers doesn't contain any zero divisors
other rings do contain zero divisors.
```

### Cancellation Law

```{prf:theorem} Cancellation law
:label: res-integer-cancellation-law

Let $a, b, c \in \ZZ$ such that $c \neq 0$.
If $a \cdot c  = b \cdot c$ then $a = b$.
```

```{prf:proof}
We note that

$$
& a \cdot c  = b \cdot c \\
\iff & a \cdot c + (- b \cdot c) = b \cdot c + (- b \cdot c) = 0\\
\iff & a \cdot c + ((- b) \cdot c) = 0 \\
\iff & (a + (- b)) \cdot c = 0 \\
\iff & (a - b) \cdot c = 0.
$$
Since $c \neq 0$ hence by cancellation law $a - b = 0$.
Which means that $a = b$.
```

## Partial Order

Recall from {prf:ref}`def-st-partial-order`
that a relation, denoted by $\leq$, on a set $X$ is said to be a
*partial order* for $X$ (or that $X$ is partially ordered by $\leq$)
if it satisfies the following properties:

*  $x \leq x$ holds for every $x \in X$ (reflexivity).
*  If $x \leq y$ and $y \leq x$, then $x = y$ (antisymmetry).
*  If $x \leq y$ and $y \leq z$, then $x \leq z$ (transitivity).

```{prf:definition} Partial order on the set of integers
:label: def-integer-partial-order

For any $a, b \in \ZZ$, we say that $a \leq b$
if and only if $a  < b$ or $a = b$.

This relation is a *partial order* on the set of integers.
```

```{prf:proof}
Since $a = a$ for every $a \in \ZZ$, hence reflexivity holds.


Antisymmetry

1. Let $a \leq b$ and $b \leq a$.
1. Assume that $a \neq b$.
1. Then, $a < b$ and $b < a$.
1. This means $b -a \in \Nat$ and $a - b \in \Nat$.
1. But $- (b - a) = a - b$.
1. Hence, they both cannot be in $\Nat$.
1. Hence we must have $a = b$.

Transitivity

1. Let $a \leq b$ and $b \leq c$.
1. Then $b -a = 0$ or $b - a \in \Nat$.
1. Similarly, $c - b = 0$ or $c - b \in \Nat$.
1. We have $c -a  = (c - b) + (b - a)$.
1. If $c -b = 0$ and $b - a = 0$ then $c - a = 0$.
1. In all other cases, we have $c -a \in \Nat$.
1. Hence $c-a =0$ or $c - a \in \Nat$.
1. Hence $c = a$ or $a < c$.
1. Hence $a \leq c$.
```


```{prf:theorem} Total order
:label: res-integer-total-order

The relation $\leq$ defines a total order on $\ZZ$.
In other words, for every $a, b \in \ZZ$, we must have
either $a \leq b$ or $b \leq a$.
```

```{prf:proof}
Let $a, b \in \ZZ$. 

1. If $a \leq b$ then there is nothing more to say.
1. Suppose that $a \not\leq b$.
1. Then neither $a = b$ nor $a < b$.
1. Hence $b - a \notin \Nat$ and $b - a \neq 0$.
1. Hence $-(b -a) = a - b \in \Nat$.
1. Hence $b < a$.
1. Hence $b \leq a$.
1. Hence $\leq$ is a total order.
```

```{prf:theorem} Implications of order relation
:label: res-integer-order-implications

Let $a,b,c,d \in \ZZ$. Then

1. If $a < b$, then $a \pm c \leq b \pm c$.
1. If $a < b$ and $c > 0$ then $a \cdot c < b \cdot c$.
1. If $a < b$ and $c < 0$ then $a \cdot c > b \cdot c$.
1. If $0 < a < b$ and $0 < c < d$ then $a \cdot c  < b \cdot d$.
1. If $a \in \ZZ$ and $a \neq 0$ then $a^2 > 0$.
```

## Well Ordering Principle

There are some issues still left with the construction of
integers. We don't know if there is any integer
between $0$ and $1$. The nonexistence of any
integer between $0$ and $1$ cannot be established
based on the arithmetic and natural number axioms
established so far. Readers can check that the
set of rational numbers also satisfy all the
axioms stated so far. 

This requires another axiom known as the
*well ordering principle*.

```{prf:axiom} Well ordering principle
:label: ax-integer-well-ordering-principle

If $B$ is a nonempty subset of $\ZZ$ which is bounded below;
i.e., there exists an $n \in \ZZ$ such that 
$n \leq b$ for every $b \in B$, then $B$ has a smallest
element; i.e., there exists $b_0 \in B$ such that
$b_0 < b$ for every $b \in B, b \neq b_0$. 
```

As a consequence every nonempty subset of integers
that is bounded above has a largest element.

```{prf:theorem} Well ordering principle for natural numbers
:label: res-integer-nat-well-ordering-principle

Every nonempty set of natural numbers has a least element.
```
```{prf:proof}
Let $A \subseteq \Nat$.
1. Since for every $a \in A$, we have $0 < a$, hence
   $A$ is bounded below by $0$.
1. Hence by well ordering principle, it has a least element. 
```

```{prf:theorem}
:label: res-integer-0-1-gap

There is no integer $n$ satisfying $0 < n < 1$.
```

```{prf:proof}
Let 

$$
B = \{ n \ST n \in \ZZ, \text{ and } 0 < n < 1 \}.
$$

1. Assume for contradiction that $B$ is not empty.
1. $B$ is bounded below by $0$.
1. By well ordering principle, $B$ has a least element.
1. Let $m$ be the least element of $B$.
1. Then we have $0 < m < 1$.
1. Since $m$ is an integer hence $m^2 = m \cdot m$ is also an integer.
1. Since $m < 1$, hence $m^2 < m$.
1. Since $0 < m$, hence $0 < m^2$.
1. We have $0 < m^2 < m < 1$.
1. Hence $m^2 \in B$.
1. But this contradicts the fact that $m$ is the smallest
   element in $B$.
1. A contradiction. Hence, $B$ must be empty.
```


### Odd and Even Numbers

```{prf:definition} Odd and even numbers
:label: def-integer-odd-even

If $n \in \ZZ$, then we say that $n$ is *even*
if and only if there exists an integer $k \in \ZZ$
such that $n = 2 k$.

We say that $n$ is *odd* if and only if there
exists $k \in \ZZ$ such that $n = 2 k + 1$.
```


```{prf:theorem}
:label: res-integer-odd-even

Every integer is either even or odd.
```
```{prf:proof}
For contradiction, assume that there is an integer $m$
that is neither even nor odd.

1. Define the set
   
   $$
   B = \{n \in \ZZ \ST n \text{ is even or odd and } n \leq m \}.
   $$
1. Then $B \neq \EmptySet$ and $B$ is bounded above by $m$.
1. Hence $B$ by well ordering principle, $B$ has a largest element.
1. Let $p \in B$ be the largest element of $B$.
1. Since $p$ is either even or odd and $p \leq m$ hence $p < m$.
1. If $p$ is even then $p+1$ is odd. Since $p$ is the largest
   element of $B$, we must have $p < m < p + 1$.
1. If $p$ is odd then $p+1$ is even. Since $p$ is the largest
   element of $B$, we must have $p < m < p + 1$.
1. Thus, in both cases, we have

   $$
   p < m < p + 1.
   $$
1. Subtracting $p$ from this inequality, we get
   
   $$
   0 < m - p < 1.
   $$
1. Since $m$ and $p$ are both integers. Hence $m - p$ must be
   an integer too.
1. But due to {prf:ref}`res-integer-0-1-gap` there is no
   integer between $0$ and $1$. A contradiction.
1. Therefore every integer must be either odd or even.
```

```{prf:theorem} Distinctness of odd and even integers
:label: res-integer-odd-even-distinct

There is no integer which is even or odd.
```

```{prf:proof}
Let $a \in \ZZ$ be an integer which is both even and odd.

1. Then there exist $k, l \in \ZZ$ such that
   $a = 2 k$ and $a = 2 l + 1$.
1. Therefore $2 k = 2 l + 1$.
1. Hence $2 (k - l) = 1$.
1. Since $1 > 0$ hence by law of trichotomy, $k -1 > 0$.
1. Since $2 = 1 + 1 > 1 + 0 = 1$, hence

   $$
   1 = 2 ( k - l) > 1 (k - l ) = k - l.
   $$
1. Therefore, we have $0 < k - l < 1$.
1. But due to {prf:ref}`res-integer-0-1-gap` there is no
   integer between $0$ and $1$. A contradiction.
1. Hence $a$ cannot be odd and even simultaneously.
```

(sec:int:math:induction)=
### Principle of Mathematical Induction

Well ordering principle is equivalent to the principle of 
mathematical induction. 

````{prf:theorem} Principle of mathematical induction
:label: res-st-principle-mathematical-induction

If a subset $S$ of $\Nat$ satisfies the following properties:

*  $1 \in S$ and
*  $n \in S \implies n + 1 \in S$,

then $S = \Nat$.
````

```{prf:proof}
We prove this by contradiction.

1. Assume that $S \neq \Nat$.
1. Consider the set $T = \Nat \setminus S$.
1. Since $S \neq \Nat$, hence $T$ is nonempty.
1. By definition $T$ is a subset of natural numbers.
1. By the well ordering principle
   {prf:ref}`res-integer-nat-well-ordering-principle`,
   $T$ has a smallest number.
   Let it be $t$.
1. A lower bound on $\Nat$ is $1$.
1. Hence $1$ is also a lower bound of $T$.
1. By hypothesis, $1 \in S$.
1. Hence $1 \notin T$.
1. Hence $t$ is of the form $k+1$ where
   $k \in \Nat$.
1. Since $t$ is the smallest element of $T$,
   hence $k \notin T$.
1. Hence $k \in S$ as by definition $\Nat = S \cup T$
   (a disjoint union).
1. But by hypothesis $k \in S$ implies $t = k+1 \in S$.
1. We arrive at a contradiction that $t$ belongs to
   both $T$ and $S$ but the two sets are disjoint.
```

The principle of mathematical induction is applied as follows.
1. We consider a set
   
   $$
   S \triangleq \{ n \in \Nat \ST n \text{ satisfies } P \}
   $$
   where $P$ is some property that the members of this set satisfy. 
1. We then show that $1$ satisfies the property $P$.
1. Further, we show that if $n$ satisfies property $P$,
   then $n + 1$ also has to satisfy $P$. 
1. Then, applying the principle of mathematical induction, 
   we claim that $S = \Nat$.
1. In other words, every number $n \in \Nat$ satisfies the property $P$.


The following is a different version of the principle
of mathematical induction.

```{prf:theorem} Principle of mathematical induction
:label: res-int-math-ind-v2

Let $P(n)$ be an assertion about the integer $n$.
Assume the following:

1. The assertion $P(n_0)$ is true for some
   integer $n_0$.
1. For any integer $k \geq n_0$, if $P(k)$ is true
   then $P(k+1)$ must also be true.

Then $P(n)$ is true for every integer $n \geq n_0$.
```

```{prf:proof}
Consider the set $S$ defined as follows.

$$
S = \{n \in \Nat \ST P(n + n_0 -1) \text{ is true } \}.
$$

1. By hypothesis, $P(n_0)$ is true.
1. $P(n_0) = P(1 + n_0 - 1)$.
1. Hence $1 \in S$.
1. Assume that $n \in S$.
1. Then $P(n + n_0 -1)$ is true.
1. Since $n \in \Nat$, hence $k = n + n_0 -1 \geq n_0$.
1. By hypothesis $P(k + 1) = P(n + n_0)$ is also true.
1. Hence $n + 1 \in S$ also holds.
1. Hence by {prf:ref}`res-st-principle-mathematical-induction`,
   $S = \Nat$.
1. Now, let $n$ be some integer with $n \geq n_0$.
1. Then $n - n_0 \geq 0$.
1. Hence $n - n_0 + 1 \geq 1$.
1. Hence $n - n_0 + 1 \in S = \Nat$.
1. Hence $P((n - n_0 + 1) + n_0 - 1) = P(n)$ is true.

We are done.
```

```{index} Induction; base case, Induction; inductive step
```
```{index} Induction; inductive hypothesis
```
```{prf:definition} Proof by mathematical induction
:label: def-int-math-ind-terms

Let $P$ be some assertion which is defined for every integer
and is either false or true for each integer.

In a proof by mathematical induction:

1. Some particular integer $n_0$ for which 
   the assertion $P(n_0)$ is true is known
   as the *base case*.
1. Proving the statement that $P(n) \implies P(n + 1)$
   for every $n \geq n_0$ is called the *inductive step*.
1. The assumption in the inductive step that $P(n)$
   is true for some arbitrary $k \geq n_0$ is called
   the *inductive hypothesis*.
```

See {ref}`sec:alg:combinatorics` for a number of
applications of the principle of mathematical induction.

Sometimes we need a stronger form of mathematical induction.


````{prf:theorem} Strong mathematical induction
:label: res-int-strong-induction

Let $P(n)$ be an assertion about the integer $n$.
Assume the following:

1. The assertion $P(n_0)$ is true for some
   integer $n_0$.
1. For any integer $k \geq n_0$, if $P(i)$ is true
   for every $i \in \{n_0, \dots, k \}$;
   then $P(k+1)$ must also be true.

Then $P(n)$ is true for every integer $n \geq n_0$.
````

We can call the induction described in {prf:ref}`res-int-math-ind-v2`
as the weak form of mathematical induction.

```{prf:proof}
We shall prove this result by forming an equivalent
problem for which weak induction applies.

1. Let $Q(n)$ be the assertion that
   for every $i$ with $n_0 \leq i \leq n$, $P(n)$ is true.
1. By hypothesis, $Q(n_0)$ is true since $P(n_0)$ is true.
1. Assume that for some $k \geq n_0$, $Q(k)$ is true.
1. Then by definition of $Q$, $P(i)$ is true
   for every $i$ with $n_0 \leq i \leq k$.
1. Then by hypothesis $P(k+1)$ is also true.
1. But $Q(k+1)$ is true if $P(i)$ is true
   for every $i$ with $n_0 \leq i \leq k+1$.
1. Hence $Q(k+1)$ is also true.
1. Thus, for every $k \geq n_0$, $Q(k) \implies Q(k+1)$. 
1. Then by principle of induction ({prf:ref}`res-int-math-ind-v2`),
   $Q(n)$ is true for every $n \geq n_0$.
1. Since $Q(n)$ is true for every $n \geq n_0$, hence
   $P(n)$ is also true for every $n \geq n_0$.
```

## Informal Definitions

We end this section with the casual descriptions
of the set of integers and natural numbers
with which we are normally familiar.

```{index} Integer
```
```{prf:definition} Integers
:label: def-alg-integer

The *set of all integers* is the set

$$
\ZZ = \{\dots, -3,-2,-1,0,1,2,3, \dots \}.
$$
```

```{index} Natural number
```
```{prf:definition} Natural numbers
:label: def-alg-natural-number

The *set of all natural numbers* is the set

$$
\Nat = \{1,2,3, \dots \}.
$$
```


