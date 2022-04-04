(sec:bra:real-line)=
# Real Line

The set of real numbers is also known as *real line*.

## Prelude

We look at some justification for why real numbers are needed.

````{prf:proposition}
:label: res-rl-no-rational-sqrt-2

There is no rational number whose square root is 2.
````

````{prf:proof}
Let us assume that there indeed is a rational number whose square root is 2:

$$
    \left ( \frac{p}{q} \right )^2 = 2.
$$

We assume that $p$ and $q$ have no common factor. 
Then we have: $p^2 = 2 q^2$. 
This means that $p^2$ is even. 
Thus, $p$ is even. Let $p = 2r$. 
Then $4r^2  = 2q^2 \implies q^2 = 2r^2$.
This means that $q^2$ is even. 
Thus, $q$ is even. 
But this contradicts our assumption that $p$ and $q$ have no common factor.
````

This argument shows that the set of rational numbers is not complete
in the sense that we can posit the existence of numbers which are not rational.

We extend the set further to a larger number system known as real numbers. 
The {prf:ref}`completeness axiom <axm-rl-completeness-axiom>` 
    plays a major role in the
definition of real numbers.


## Real numbers

We present the axiomatic definition of real numbers.


````{prf:definition} Real Numbers
:label: def-real-numbers

The *real numbers* are the members of a nonempty set $\RR$ equipped with two operations
$+$ and $\cdot$ from $\RR \times \RR$ into $\RR$ called *addition* and *multiplication*,
that satisfy following axioms. We will denote arbitrary members of $\RR$ as $x, y$ and $z$.
We will also abbreviate multiplication $x \cdot y$  as $x y$.

1.  $x + y = y + x$ and $x y = y x$; *commutative laws*.
1.  $x + (y + z) = (x + y) + z$ and $x (y z) = (x y) z$; *associative laws*.
1.  $x(y + z)  = x y + x z$; *distributive law*.
1.  There exists an element $0 \in \RR$ such that $x + 0 = x \Forall x \in \RR$; *additive identity*.
1.  For each $x \in \RR$ there exists an element in $\RR$ denoted by $-x$ such that
$x + (-x) = 0$; *additive inverse*.
1.  There exists an element $1 \in \RR$ with $1 \neq 0$ satisfying
$1\cdot x = x \Forall x \in \RR$; *multiplicative identity*.
1.  For each $x \neq 0$ there exists an element in $\RR$ denoted by $x^{-1}$ satisfying
$x x^{-1} = 1$; *multiplicative inverse*.
1.  For any $x, y \in \RR$ either $ x \geq y$ or $y \geq x$ holds; *total order*.
1.  If $x \geq y$, then $ x + z \geq y + z$ holds for each $z \in \RR$.
1.  If $x \geq y$ and $z \geq 0$ then $x z \geq y z$.
1.  Every nonempty set of real numbers that is bounded from above has a least upper bound; *completeness axiom*.

````
Axioms (1-7) are *field* axioms. Axioms (8-10) establish that $\RR$ is an *ordered field*.
Axiom (11) is discussed further in {prf:ref}`axm-rl-completeness-axiom`.

It can be shown that if $\RR$ and $\SS$ are two different
sets satisfying these axioms then they are isomorphic and
for all practical purposes identical.


Several remarks immediately follow from the definition.

*  The zero element (additive identity) is unique.
*  The one element (multiplicative identity) is unique.
*  The additive inverse $-x$ is unique.
*  $-x= (-1)x$ holds.
*  The  multiplicative inverse $x^{-1}$ for $x \neq 0$ is unique.
*  $0 \cdot x = 0$.
*  $ - ( - x) = x$.
*  $(-x) (-y) = x y$.
*  $ x - y = x + (-y) = - (y - x)$.
*  $(x^{-1})^{-1} = x \Forall x \neq 0$. 


Remarks above are derived from field properties of real line. 

Further remarks on order property

*  An alternative notation for $x \geq y$ is $y \leq x$.
*  $x > y$ means that $x \geq y$ and $x \neq y$.
*  $x < y$ means that $x \leq y$ and $x \neq y$.
*  $ x < y \iff y > x \iff y - x > x - x  = 0$.

````{prf:definition} Positive and negative numbers
:label: def-rl-positive-number

* Any number $x \in \RR$ satisfying $ x > 0$ is called a *positive number*.
* Any number $x \in \RR$ satisfying $ x < 0$ is called a *negative number*.
* Any number $x \in \RR$ satisfying $ x \geq 0$ is called 
  a *non-negative number*.
* Any number $x \in \RR$ satisfying $ x \leq 0$ is 
  called a *non-positive number*.
````

````{prf:proposition}
:label: res-rl-epsilon-order

If $x + \epsilon \geq y$ for each $\epsilon > 0$, then $ x \geq y$ holds.
````

````{prf:proof}
If the result doesn't hold, then $x < y \implies y - x > 0$.
Let $ \epsilon = \frac{1}{2} (y - x)$. Then $ x + \epsilon = \frac{1}{2} (x + y) \geq y$.
This implies $ \frac{1}{2} ( y - x) \geq 0 \iff  y - x < 0$, which is a contradiction.
````

````{prf:definition} Absolute value
:label: def-rl-absolute-value

The *absolute value* $| a |$ of a real number  $a \in \RR$ is defined as follows.
if $a \geq 0$, then $| a | = a$ and if $a < 0$, then $| a |  = -a$.
$a \vee b$ denotes the larger of the two numbers. $a \wedge b$ denotes the smaller of
the two numbers.
````

````{prf:remark}
:label: rem-rl-absolute-value-max-val

Thus $| a | = a \vee (-a) \Forall a \in \RR$. Further $| a | = |-a |$.
````

````{prf:proposition}
:label: res-absolute-value-properties

The absolute value satisfies following properties:

1.  $| a | \geq 0$ for each $a \in \RR$, and $ | a | = 0 \iff a = 0$.
1.  $ | a b |  = | a | \cdot | b | \Forall a, b \in \RR$.
1.  $ | a + b | \leq  | a | + | b | \Forall a, b \in \RR$; the triangle inequality.

````

````{prf:proof}
If $a=0$ then by definition $| a | = 0$. Again from definition, for any non-zero value,
$| a |$ is not zero. Hence $ | a | = 0 \iff a = 0$.

Let $a$ and $b$ two non-negative numbers. Then $| a |  = a$ and $ | b | = b$. Thus,
$| a | | b | = a b = | a b | $. Further $| a | + | b |  = a + b = | a  +  b |$.

Now, let $a$ and $b$ two non-positive numbers. Then $| a |  = - a$ and $ | b | = - b$.
$a b$ is non-negative, hence $| a b | = a b$. $a + b$ is non-positive, hence $| a + b | = - (a + b)$.
Thus,
$| a | | b | = (- a) ( - b) = a b = | a b | $.
Further, $| a | + | b |  = (-a) + (-b) = -(a +  b) = | a + b |$.

Now lets consider when $a$ and $b$ are of opposite signs. WLOG (without loss of generality), let
us assume that $a$ is positive and $b$ is negative.
Further let us assume that $| a | \geq | b |$. Clearly, then $ | a + b | < | a | + | b |$.
Also $| a b | = - a b = | a | | b |$.
````

````{prf:corollary}
:label: res-rl-triangle-inequality-for-difference

For $a , b \in \RR$ the following hold:

$$
    | a - b | \leq | a | + | b |.
$$

$$
    | | a | - | b | | \leq | a - b |.
$$

````

````{prf:proof}
We know that

$$
    | a + b | \leq  | a | + | b |.
$$

Replacing $b$ with $-b$ we get:

$$
    | a - b | \leq | a | + | b |.
$$

Again, replacing $b$ with $b - a$, we get:

$$
    | a + b - a | \leq | a | + | b - a  | \implies  | b | - | a | \leq | a - b |.
$$

Further, replacing $a$ with $a - b$ in $|a + b | \leq |a | + |b|$, we get:

$$
    | a - b + b | \leq | a - b | + | b | \implies  
    | a |  - | b | \leq | a  - b |.
$$

Combining the two, we get our result.
````


````{prf:proposition} Distance triangle inequality
:label: res-rl-distance-triangle-inequality

Let $ a, b, c \in \RR$. Then:

$$
    | a - b | \leq | a - c | + | c - b |.
$$

````
This is straight-forward application of {prf:ref}`res-absolute-value-properties`.

$$
| a - c | + | c - b | \geq | (a - c) + (c - b) | = | a - b |.
$$


````{prf:proposition}
:label: ref-rl-real-equality

Two real numbers $a$ and $b$ are equal if and only if for every real number $\epsilon > 0$,
$| a - b | < \epsilon$ holds.
````

````{prf:proof}
If $a = b$, then $a - b = 0 \implies | a - b | = 0 < \epsilon$ for every $\epsilon > 0$.
Now for the converse, we are given that for every $\epsilon > 0$, $| a - b | < \epsilon$.
We have to show that $a = b$. Let as assume that $a \neq b$. Choose $\epsilon_0 = | a -  b |$.
Clearly, for $\epsilon_0 > 0$, $ | a - b | < \epsilon_0$ doesn't hold.
This contradicts our assumption that for every $\epsilon > 0$
$| a  - b | < \epsilon$. Hence $a  = b$.
````

## Intervals

```{prf:definition} Interval
:label: def-rl-interval

A subset $S$ of $\RR$ is called an *interval* if
for every $a,b \in S$ such that $a < b$, 
$S$ contains all the real numbers between $a$ and $b$.
In other words, if $a < x < b$, then $x \in S$.

* An *open interval* does not include its endpoints and is denoted
  as $(a,b) \triangleq \{ x \in \RR \ST a < x < b\}$.
* A *closed interval* does not include its endpoints and is denoted
  as $[a,b] \triangleq \{ x \in \RR \ST a \leq x \leq b\}$.
* A *half-open interval* includes one of its its endpoints
  : $[a,b) \triangleq \{ x \in \RR \ST a \leq x < b\}$;
  $(a,b] \triangleq \{ x \in \RR \ST a < x \leq b\}$.
* A *degenerate interval* is an interval of the form $[a,a]$
  which is a singleton containing $a \in \RR$.
```

## Completeness Axiom


````{prf:definition} Upper and lower bounds
:label: def-rl-bounds

Let $A$ be a nonempty subset of $\RR$.

*  An *upper bound* of $A$ is any
$u \in \RR$ such that $ x \leq u \Forall x \in A$.
*  A *lower bound* of $A$ is any $ l \in \RR$ such that $ x \geq l \Forall x \in A$.
*  If $A$ has an upper bound it is said to be *bounded from above*.
*  If $A$ has a lower bound it is said to be *bounded from below*.
*  If $A$ is both bounded from above and below, then $A$ is said to be *bounded*.
*  A real number is called a *least upper bound* or *supremum* of $A$ if it
is an upper bound of $A$, and it is less than or equal to every other upper bound of $A$.
The least upper bound is denoted by $\sup (A)$.
*  A real number is called a *greatest lower bound* or *infimum* of $A$ if it
is a lower bound of $A$, and it is greater than or equal to every other lower bound of $A$.
The greatest lower bound is denoted by $\inf(A)$.
````

````{prf:remark}
:label: rem-rl-lub-glb-at-most-one

A set $A$ can have at most one least upper bound and at most one greatest lower bound.
````

````{prf:remark}
:label: rem-rl-set-inf-sup-outside

The infimum or supremum of a set $A$ need not belong to the set itself.
````
The set $S = \{ x \ST 0 < x < 1\}$ has an infimum $0$ and a supremum $1$.
Neither belong to the set.

The completeness axiom asserts that every nonempty set bounded from above has a least
upper bound. We restate the axiom independently for emphasis.

````{prf:axiom} Completeness axiom
:label: axm-rl-completeness-axiom

Every nonempty set of real numbers that is bounded from above has a least upper bound.
````


````{prf:example} Least upper and greatest lower bounds
:label: ex-rl-lub-glb-1

Let

$$
    A = \left \{ \frac{1}{n} : n \in \Nat \right \}.
$$

The set is bounded from above with $\sup(A) = 1$. 
The set is bounded from below with $\inf(A) = 0$.

The open interval $(0, 2) = \{x \in \RR : 0 < x < 2 \}$
has lower and upper bounds as $0$ and $2$ respectively. So does
the closed interval $[0, 2] = \{x \in \RR : 0 \leq x \leq 2 \}$.
But $(0,2)$ has no maximum or minimum element. $[0,2]$ has both.
Further, $(0,2]$ has maximum element but not minimum, and $[0,2)$ has
minimum element but not maximum.
````

````{prf:example} Distinction with rational numbers
:label: ex-rl-lub-choice-vs-rational

The set $S = \{ x \in \QQ : x^2 \leq 2\}$ doesn't have a least upper bound
in the set of rational numbers.
For every $x \in S$, it is possible to find a $y \in \QQ$ such that
$ y > x$ and $y^2 < 2$.

The axiomatic definition of real numbers claims that since 
the set $S = \{ x \in \RR : x^2 \leq 2\}$ is bounded from above,
hence there exists a real number which is the least upper bound
of this set. We simply denote this number as:

$$
\sqrt{2} \triangleq \sup \{ x \in \RR : x^2 \leq 2\}.
$$
````


````{prf:corollary}
:label: res-rl-completeness-lower

Every nonempty set of real numbers that is bounded from below has a greatest lower bound.
````

````{prf:proof}
Let $A \subset \RR$ be a nonempty set bounded from below. Consider the set of lower bounds for $A$
defined as

$$
    B = \{b \in \RR : b \leq x  \Forall x \in A \}.
$$

Since $B$ is bounded from above by numbers in $A$, hence by completeness axiom, $B$ has
a least upper bound denoted by $\sup (B)$. This indeed is the greatest lower bound of $A$
as $\sup (B) = \inf(A)$.
````

This result demonstrates that we only need an axiom for the least upper bound. The
idea of existence of greatest lower bound immediately follows from it. We could
have easily started with the existence of greatest lower bound as an axiom and derived
the existence of least upper bound from it.

````{prf:remark}
:label: rem-rl-max-sup-min-inf

If a set $A$ has a maximum (resp. minimum) element, then $\max(A) = \sup (A)$
(resp. $\min(A) = \inf (A)$ ).

On the other hand, if the supremum of a set $A$ exists and $\sup (A) \in A$, then
$\sup(A)$ is the maximum element of $A$. Similarly if the infimum of a set $A$
exists and $\inf(A) \in A$, then $\inf(A)$ is the minimum element of $A$.
````

````{prf:proposition}
:label: res-rl-supremum-epsilon

Assume that the supremum of a subset $A$ of $\RR$ exists. Then for every $\epsilon > 0$,
there exists some $x \in A$ such that

$$
    \sup (A) - \epsilon < x \leq \sup (A).
$$

Conversely, let $a$ be an upper bound of $A \subseteq \RR$ such that for every $\epsilon > 0$,
there exists an $x \in A$ such that $ a - \epsilon < x$, then $a$ is the least upper bound of $A$.
````

````{prf:proof}
Clearly, if $x \in A$ then $ x \leq \sup (A)$. Now, if for every $x \in A$ we have $x \leq \sup (A)  - \epsilon$, then
$\sup (A) - \epsilon$ is an upper bound of $A$, which is less than the least upper bound. This is
a contradiction.  Thus, for every $\epsilon > 0$, there exists an $x \in A$ such that
$\sup (A) - \epsilon < x \leq \sup (A)$.

Conversely, no matter how small $\epsilon > 0$ is chosen, $a - \epsilon$ cannot be an upper bound of
$A$ since there exists some $x \in A$ such that $x > a - \epsilon$. Hence $a$ is indeed the least
upper bound of $A$.
````

````{prf:proposition}
:label: res-rl-subset-upper-bound

Let $A$ and $B$ be two subsets of $\RR$ bounded above with $B \subseteq A$. Then

$$
    \sup(B) \leq \sup(A).
$$
````


````{prf:proof}
Let $a$ be an upper bound of $A$. Then $a \geq x \Forall x \in A$. Since $B \subseteq A$,
hence $a \geq y \Forall y \in B$ too. Thus, every upper bound of $A$ is also an upper bound of $B$.
Thus, $\sup(A)$ is also an upper bound of $B$. Since $\sup(B)$ is least upper bound of $B$,
it is smaller than or equal to any other upper bound of $B$. Thus $\sup(B) \leq \sup(A)$.
````

````{prf:proposition}
:label: res-rl-nat-numbers-unbounded

The set of natural numbers $\Nat$ is unbounded.
````

````{prf:proof}
Assume by contradiction that $\Nat$ is bounded. Since $\Nat \subset \RR$, hence by completeness
axiom, there exists a least upper bound of $\Nat$. Let $s = \sup(\Nat)$. Then  $ n \leq s \Forall n \in \Nat$.
Then by {prf:ref}`res-rl-supremum-epsilon`, for $\epsilon = 1$ there exists  some $k \in \Nat$ such that
$ s - 1 < k$. This implies $ s < k+1$. Further since $s$ is the supremum, hence $ k + 1 \leq s$. Thus,
$ s < k+1 \leq s$, which is impossible.
````

````{prf:proposition} Nested interval property
:label: res-rl-nested-interval-property

For each $n \in \Nat$, assume that we are given a closed interval
$I_n = [a_n, b_n] = \{x \in \RR : a_n \leq x \leq b_n\}$. Assume
also that each $I_n$ contains $I_{n + 1}$. Then, the resulting nested sequence of
closed intervals

$$
    I_1 \supseteq I_2 \supseteq \dots \supseteq  I_n \supseteq  I_{n + 1} \supseteq  \dots
$$

has a nonempty intersection; i.e.

$$
    \bigcap_{n= 1}^{\infty} I_n \neq \EmptySet.
$$

````
````{prf:proof}
Consider the set of lower bounds

$$
    A = \{ a_n : n \in \Nat \}.
$$

Due to {prf:ref}`completeness axiom <axm-rl-completeness-axiom>`, the set has a least upper bound.
Let $x = \sup (A)$.  Further, due to nested structure, each $b_n$ is also an upper bound of $A$.
Since $x$ is the least upper bound, hence $x \leq b_n \Forall n \in \Nat$. Thus, we have $a_n \leq x \leq b_n$
$\Forall n \in \Nat$. Hence, $x \in I_n \Forall n \implies x \in \bigcap_{n= 1}^{\infty} I_n$ .
````

## Archimedian Property

````{prf:proposition} Archimedian property
:label: res-rl-archimedian

If $x$ and $y$ are two positive real numbers, then there exists some natural number $n$ such that
$n x > y$.
````
````{prf:proof}
For contradiction assume that $ n x \leq y$ holds for every $n \in \Nat$. Since, $x, y > 0$,
$ n \leq y x ^{-1} \Forall n \in \Nat$. This contradicts 
{prf:ref}`res-rl-nat-numbers-unbounded`.
````
This also tells us that for any real number $x > 0$, there exists an $n \in \Nat$ satisfying
$\frac{1}{n} < x$. By choosing $y = 1$ in above, we get $n x > 1 \implies x > \frac{1}{n}$.

````{prf:example}
:label: ex-rl-inf-outside-set-1

Let $A = \{\frac{1}{n} : n \in \Nat \}$. We show that $\inf (A)  = 0$. Clearly 0 is a lower bound.
Now if $x > 0$ then we can find $n_0 \in \Nat$ such that $1/n_0 < x$. Thus $x > 0$ cannot be a lower bound of
$A$. Hence $0$ is the greatest lower bound of $A$.
````

## Rational Numbers

````{prf:proposition} Density of $\QQ$ in $\RR$
:label: res-rl-rational-existence

Between any two distinct real numbers there exists a rational number.
````

````{prf:proof}
Let $a$ and $b$ be the two distinct real numbers.
If the two numbers are of opposite sign, then 0 is an obvious rational number between them.
If $a$ and $b$ are both non-positive, then the rational number can be chosen to be the negative of the rational number
between $-a$ and $-b$.
We now consider the case where both $a$ and $b$ are non-negative. Without loss of generality,
we assume that $0 \leq a < b$. Consider the set

$$
    A = \left \{n \in \Nat : n > \max\left \{\frac{1}{b - a}, \frac{1}{b} \right \} \right \}.
$$

Since $\Nat$ is not bounded from above, $A$ is nonempty. Fix an element $q \in A$.
Clearly,  $0 < \frac{1}{q} < b - a$ and $ 1 < b q$.
Now, let

$$
    B = \{n \in \Nat : n < b q \}.
$$

Since $1 \in B$,  B is nonempty.
Also, $B$ is a finite set. Let $p = \max (B)$. Clearly, $p \in B$ and $p + 1 \notin B$.

Finally, we will show that $ a < \frac{p}{q} < b$.
Since $p \in B$, $ p < b q \implies \frac{p}{q} < b$.
Further,

$$
    p + 1 \geq  b q  \implies  b \leq \frac{p}{q} + \frac{1}{q} < \frac{p}{q} + b - a \implies a < \frac{p}{q}.
$$
````

````{prf:proposition}
:label: res-rl-existence-of-square-root-2

There exists a real number $\alpha \in \RR$ satisfying $\alpha^2 = 2$.
````
````{prf:proof}
Consider the set

$$
    A = \{ x \in \RR : x^2 < 2 \}.
$$

Clearly, A is bounded above. Now, choose $\alpha = \sup(A)$. We show that $\alpha^2 = 2$
by ruling out $\alpha^2 < 2$ and $\alpha^2 > 2$.
Assume that $\alpha^2 < 2$. Consider for some $n \in \Nat$:

$$
    \left ( \alpha + \frac{1}{n}\right )^2 &= \alpha^2 + \frac{2 \alpha}{n} + \frac{1}{n^2}\\
    &< \alpha^2 + \frac{2 \alpha}{n}  + \frac{1}{n}\\
    & = \alpha^2 + \frac{2 \alpha + 1}{n}.
$$

Now choose $n_0 \in \Nat$ large enough so that

$$
    \frac{1}{n_0} < \frac{2 - \alpha^2}{ 2 \alpha + 1}.
$$

This implies $\frac{2 \alpha + 1}{n_0} < 2 - \alpha^2$. Thus,

$$
    \left ( \alpha + \frac{1}{n_0}\right )^2 < \alpha^2 + (2 - \alpha^2) = 2.
$$

Thus $\alpha + \frac{1}{n_0} \in A$ contradicting the assumption that $\alpha^2$ is an upper bound of $A$.
Hence $\alpha^2 < 2$ is not possible.

Now assuming $\alpha^2 > 2$, we show that it cannot be the least upper bound of $A$.
We start with

$$
    \left ( \alpha - \frac{1}{n}\right )^2 &= \alpha^2 - \frac{2 \alpha}{n} + \frac{1}{n^2}\\
    & > \alpha^2 - \frac{2 \alpha}{n}.
$$

Choosing $n_0 > 2 \alpha / (\alpha^2 - 2)$, we get $\frac{2 \alpha}{n_0} < \alpha^2 - 2$.
Thus

$$
    \left ( \alpha - \frac{1}{n_0}\right )^2 > \alpha^2 - (\alpha^2 - 2) = 2.
$$

Thus $\left ( \alpha - \frac{1}{n_0}\right )^2$ is also an upper bound of $A$.
But

$$
    \left ( \alpha - \frac{1}{n_0}\right )^2 < \alpha^2.
$$

Hence, $\alpha^2$ cannot be the least upper bound of $A$. Thus, $\alpha^2 > 2$ is not possible.
Since for every real number $\alpha^2$, exactly one of the possibilities $\alpha^2 < 2$, $\alpha^2 > 2$
or $\alpha^2 = 2$ has to be true, hence $\alpha^2 = 2$.
````

## Irrational Numbers

````{prf:definition} Irrational number
:label: def-rl-irrational-number

A real number which is not rational is known as *irrational number*. The
set of irrational numbers is denoted by $\II$.
````

Clearly, $\II = \RR \setminus \QQ$. Also, $\RR = \QQ \cup \II$.
Although $\QQ$ forms a field, but $\II$ does not. For example $\sqrt{2} \times \sqrt{2} = 2$
is rational. Thus $\II$ is not closed under multiplication. Further, $0$ and $1$ 
(the additive and multiplicative identities) don't belong to $\II$. 

````{prf:proposition}
:label: res-rl-rational-irrational-sum-product

The sum of a rational and an irrational number is irrational.
The product of a non-zero rational number and an irrational number is irrational.
````

````{prf:proof}
Let $q \in \QQ$ and $i \in \II$.  Let $r = q + i$. Then $i = r - q$. If $r$ were rational, then
$i$ would have to be rational (since $\QQ$ is closed under addition). But $i$ is irrational, hence
$r$ is irrational.

Now let $q \neq 0$. Let $r = q i$. Then $i = r / q$.  If $r$ were rational, then $i$ would have
to be rational since $\QQ$ is closed under multiplication.
````

````{prf:proposition} Density of $\II$ in $\RR$
:label: res-rl-irrational-existence

Between any two distinct real numbers there exists an irrational number.
````

````{prf:proof}
Let $a, b \in \RR$. Without loss of generality, assume $a < b$. Consider the numbers:
$a - \sqrt{2}, b - \sqrt{2}$.  Since $\QQ$ is dense in $\RR$ ({prf:ref}`res-rl-rational-existence`),
there exists a rational number $q$ such that

$$
    a - \sqrt{2} < q < b - \sqrt{2}.
$$

Clearly $a < q + \sqrt{2} < b$. But by {prf:ref}`res-rl-rational-irrational-sum-product`,
$q + \sqrt{2}$ is irrational. This completes the proof.
````


````{prf:proposition} Existence of roots
:label: res-rl-existence-of-roots

For a real number $a$ and any natural number $n \geq 2$, we have the following:

1.  If $a \geq 0$ and $n$ is even, there exists a unique $b \geq 0$ such that $ b^n = a$.
1.  If $a \in \RR$ and $n$ is odd, then there exists a unique $b \in \RR$ such that $b^n = a$.
````

## Uncountability

````{prf:proposition}
:label: res-rl-real-numbers-uncountable

The set $\RR$ is uncountable.
````

````{prf:proof}
Assume that $\RR$ is countable. Then it is possible to enumerate $\RR$ as
$\RR = \{ x_1, x_2, \dots \}$. Consider a closed interval $I_1$ which doesn't contain $x_1$.
Further, consider a second closed interval $I_2 \subseteq I_1$ 
which doesn't contain $x_2$. If $I_1 = [a, b]$, then by choosing
$c_1 = (a + b) / 3$, and $c_2 = 2 (a + b) / 3$, we get disjoint closed sub-intervals $[a, c_1]$ and
$[c_2, b]$. $x_2$  can lie in at most one of them, hence it is always possible to choose $I_2 \subseteq I_1$
as desired. Now given $I_n$ has been chosen, choose $I_{n + 1}$ such that:

1.  $I_{n + 1} \subseteq I_n$ and
1.  $x_{n + 1} \notin I_{n + 1}$.

Now, consider the countable intersection of nested closed sets

$$
    I = \bigcap_{n = 1}^{\infty} I_n.
$$

If $x_i \in \RR$ (as an element in the enumeration of $\RR$), then $x_i \notin I_i$. Thus
$x_i \notin I$. Thus, if $\RR$ is countable, then no real number lies in $I$. But by
{prf:ref}`nested interval property <res-rl-nested-interval-property>`, $I$ is not empty.
This contradicts our assumption that $\RR$ is countable.
````

````{prf:corollary}
:label: res-rl-irrationals-uncountable

The set of {prf:ref}`irrational numbers <def-rl-irrational-number>` is uncountable.
````

````{prf:proof}
If $\II$ were countable, then $\RR = \QQ \cup \II$ would also be countable. But
this is not true. Hence $\II$ is uncountable.
````

## Algebraic Numbers

````{prf:definition} Algebraic real number
:label: def-rl-algebraic-real-number

A real number is called *algebraic* if it is the root of a polynomial with integer coefficients.
i.e. $x \in \RR$ is algebraic if
there exist integers $a_0, a_1, \dots, a_n \in \ZZ$, not all zero, such that

$$
    a_n x^n + a_{n -1} x^{n - 1} + \dots + a_1 x + a_0  = 0.
$$
````

````{prf:example} Algebraic real numbers
:label: ex-rl-algebraic-numbers-1

*  $\sqrt{2}$ is algebraic since it is the root of the equation $x^2 - 2 = 0$.
*  $\sqrt[3]{2}$ is algebraic since it is the root of the equation $x^3 - 2 = 0$.
*  $\sqrt{2} + \sqrt{3}$ is algebraic since it is the root of the equation $x^4 - 10 x^2 + 1 = 0$.

````

````{prf:proposition}
:label: res-rl-algebraic-numbers-countable

The set of algebraic numbers is countable.
````

````{prf:proof}
Let $n \in \Nat$. Let $A_n$ be the algebraic numbers obtained as roots of polynomials
with integer coefficients that have degree $n$ given by

$$
    a_n x^n + a_{n -1} x^{n - 1} + \dots + a_1 x + a_0  = 0.
$$

Each polynomial can be represented by an $n+ 1$-tuple given by

$$
    (a_n, a_{n-1}, \dots, a_1, a_0).
$$

Thus, it has a one-one correspondence with the Cartesian product $\ZZ^{n+ 1}$.
Since finite Cartesian product of countable sets is countable, 
hence $\ZZ^{n + 1}$ is countable. This means that the number of polynomials of
order $n$ is countable. Since each polynomial of order $n$ can have at most $n$ roots,
hence $A_n$ is countable.

Now consider the union

$$
    A = \bigcup_{n= 1}^{\infty} A_n
$$

as the set of algebraic numbers. Since union of a countable family of countable sets 
is countable,
hence $A$ is countable.
````


## Transcendental Numbers


````{prf:definition} Transcendental numbers
:label: def-rl-transcendental-numbers

A real number is called *transcendental* if it is not algebraic.
````

````{prf:proposition} Existence of transcendental numbers
:label: res-rl-existence-transcendental-numbers

Transcendental numbers exist and they are uncountable.
````

````{prf:proof}
Let $A$ denote the set of algebraic numbers and $B$ denote the set of transcendental numbers.
Then $\RR = A \cup B$. Since $A$ is countable and $\RR$ is uncountable, hence $B$ is non-empty
and is uncountable.
````

## Intervals are Uncountable

````{prf:proposition}
:label: res-rl-unit-open-interval-uncountable

The open interval $(0, 1) = \{x \in \RR : 0 < x < 1 \}$ is uncountable.
````

````{prf:proof}
Assume that $(0, 1)$ is countable. Then, the numbers $x \in (0, 1)$ can be
enumerated. Let $f : \Nat \to (0, 1)$ be such an enumeration. Let $f(m)$ be
given by (in the decimal representation)

$$
    f(m) = .a_{m 1} a_{m 2} \dots.
$$

Define a real number $x \in (0, 1)$ with the decimal expansion

$$
    x = . b_1 b_2 \dots
$$

using the rule:

$$
    b_n =
     \left\{
            \begin{array}{ll}
                2 & \mbox{if $a_{n n} \neq 2$};\\
                3 & \mbox{if $a_{n n}  = 2$}.
            \end{array}
          \right.
$$

The number $x$ cannot be $f(1)$ since $b_1 \neq a_{11}$.
The number $x$ cannot be $f(n) \Forall n \in \Nat$ since $b_n \neq a_{n n}$.
Thus $x$ doesn't belong to the suggested enumeration of $(0, 1)$. Thus,
$(0, 1)$ is uncountable.
````

````{prf:proposition}
$(0, 1)$ is uncountable if and only if $\RR$ is uncountable.
````

````{prf:proof}
If $\RR$ were countable, then $(0, 1)$ would be countable since $(0, 1) \subset \RR$.
Thus, $(0, 1)$ can be uncountable only if $\RR$ is uncountable.

Now if $(0, 1)$ were countable then $\RR$ would be countable since
$\RR$ can be written as

$$
    \RR = \bigcup_{n = -\infty}^{\infty} (n, n + 1)  \cup \ZZ.
$$

Every open interval $(n, n + 1)$  has the same cardinality as $(0, 1)$ and $\ZZ$ is
countable.
Thus, $\RR$ is uncountable only if $(0, 1)$ is uncountable. In other words,
$(0, 1)$ is uncountable if $\RR$ is uncountable.
````
