(sec:bra:sequences)=
# Sequences and Series

This section collects results on sequences and series of real numbers.

````{prf:definition}
:label: def-bra-sequence

A {prf:ref}`sequence <def-st-sequence>` of real numbers is a 
function $f : \Nat \to \RR$.
````
A sequence can be thought of as an ordered (countable) list of real numbers.

````{prf:definition} Convergence
:label: def-bra-convergence

A sequence $\{ x_n \}$ of real numbers is said to *converge* to $x \in \RR$ 
if for every $\epsilon > 0$,
there exists a natural number $n_0$ (depending upon $\epsilon$) such that

$$
    | x_n - x | < \epsilon \Forall n > n_0.
$$

The real number $x$ is called the *limit* of the sequence $\{ x_n \}$, 
and we write $x_n \to x$ or $x = \lim_{n \to \infty} x_n$.
````

In other words, a sequence of real numbers 
$\{ x_n \}$ converges to some real number $x$ 
if and only if for each $\epsilon > 0$, the terms $x_n$ are eventually $\epsilon$-close to $x$.

````{prf:example} Sequence convergence
:label: ex-bra-seq-converge-1

Consider the sequence $\{ x_n \}$, where $x_n = \frac{1}{\sqrt{n}}$.
For a given $\epsilon > 0$, choose $n_0 > \frac{1}{\epsilon^2}$. 
Then, for every $n > n_0$, we have 

$$
\left |\frac{1}{n^2} - 0 \right | = \frac{1}{n^2} < \epsilon.
$$

Thus, the sequence converges to 0.
````

````{prf:definition} Divergence
:label: def-bra-divergence

A sequence which doesn't converge, is said to *diverge*.
````

````{prf:theorem} Sequence Limit Uniqueness
:label: res-bra-sequence-limit-uniqueness

A sequence of real numbers can have utmost one limit.
````

````{prf:proof}
If a sequence diverges, then there is nothing to prove. 
Otherwise, suppose a sequence $\{ x_n \}$ converges to 
two limits $x$ and $y$. 
Thus, for every $\epsilon > 0$, there
exist $n_1, n_2 \in \Nat$ such that 
$|x_n - x | < \epsilon \Forall n > n_1$  and
$| x_n - y | < \epsilon \Forall n > n_2$. 
Now, choose $n_0 = \max (n_1, n_2)$.
Then, by triangle inequality, for every $n > n_0$

$$
    0 \leq | x  - y  | \leq | x - x_n | + | x_n - y |  < \epsilon + \epsilon = 2\epsilon.
$$

Since this is true for all $\epsilon > 0$, hence $x = y$.
Since $x,y$ are arbitrarily close, they must be equal.
````

Recall that the notion of $\sup$ and $\inf$ was
introduced in the {prf:ref}`def-rl-bounds`.
The same notation can be used for sequences also.

```{prf:definition} Upper and lower bounds 
:label: def-bra-sequence-bounds

Let $X = \{ x_n \}$ be a sequence of $\RR$. 

* An *upper bound* of $X$ is any
  $u \in \RR$ such that $ x_n \leq u \Forall n \in \Nat$.
* A *lower bound* of $X$ is any 
  $l \in \RR$ such that $ x_n \geq l \Forall n \in \Nat$.
* If $X$ has an upper bound it is said to be *bounded from above*.
* If $X$ has a lower bound it is said to be *bounded from below*.
* If $X$ is both bounded from above and below, then $X$ is said to 
  be *bounded*.
* A real number is called a *least upper bound* or *supremum* of $X$ 
  if it is an upper bound of $X$, and it is less than or equal to 
  every other upper bound of $X$.
* The least upper bound is denoted by $\sup(X)$.
* A real number is called a *greatest lower bound* or 
  *infimum* of $X$ if it is a lower bound of $X$, 
  and it is greater than or equal to every other 
  lower bound of $X$.
* The greatest lower bound is denoted by $\inf(X)$.
```

```{prf:remark}
:label: rem-bra-seq-ub-lub-gb-glb

Due to the {prf:ref}`completeness axiom <axm-rl-completeness-axiom>`,
if a sequence $\{x_n\}$ has an upper bound, it has a least upper bound
denoted by $\sup\{ x_n \}$ and if it has a lower bound, it has a 
greatest lower bound denoted by  $\inf\{ x_n \}$.
```

The notion of upper boundedness and lower boundedness can be
subsumed into a single definition.

````{prf:definition} Boundedness 
:label: def-bra-bounded-sequence

A sequence $\{ x_n \}$ is said to be *bounded* 
if there exists a number $M > 0$ such that
$| x_n | \leq M \Forall n \in \Nat$.
````

````{prf:theorem}
:label: res-bra-convergent-bounded

Every convergent sequence is bounded.
````
````{prf:proof}
Let $\{ x_n \}$ converge to $x$. 
Choosing a particular value of $\epsilon = 1$, there
exists $n_0 \in \Nat$ such that 
$| x_n - x | < 1 \Forall n > n_0$. 
Thus, $x_n \in (x - 1, x + 1)$.
This means that

$$
    | x_n | < | x | + 1 \Forall n > n_0.
$$

Now define $M = \max \{|x_1|, |x_2|, \dots, |x_{n_0}|,  | x | + 1 \}$.
It follows that $|x_n | \leq M \Forall n \in \Nat$ as desired.
````

```{prf:definition} Unbounded above 
:label: def-bra-unbounded-above-sequence

A sequence $\{ x_n \}$ is said to be *unbounded above* 
if there exists no $u \in \RR$ such that
$x_n \leq u \Forall n \in \Nat$.

In other words, for every $u \in \RR$, there exists an $x_n > u$.
```

```{prf:definition} Unbounded below 
:label: def-bra-unbounded-below-sequence

A sequence $\{ x_n \}$ is said to be *unbounded below* 
if there exists no $l \in \RR$ such that
$x_n \geq l \Forall n \in \Nat$.

In other words, for every $l \in \RR$, there exists an $x_n < l$.
```

## Monotone Sequences

````{prf:definition} Monotone sequences
:label: def-bra-monotone-sequence

* A sequence $\{ x_n \}$ is said to be *increasing* 
  if $x_n \leq x_{n + 1}$ for each $n$.
* A sequence $\{ x_n \}$ is said to be *decreasing* 
  if $x_n \geq x_{n + 1}$ for each $n$.
* A sequence $\{ x_n \}$ is said to be *monotone* if 
  it is either increasing or decreasing.
* The notation $x_n \uparrow x$ means $\{ x_n \}$ is increasing 
  and $x  = \sup \{ x_n \}$. It applies if $\{x_n \}$ is bounded from above.
* The notation $x_n \downarrow x$ means $\{ x_n \}$ is decreasing 
  and $x  = \inf \{ x_n \}$. It applies if $\{x_n \}$ is bounded from below.
* If a sequence $\{ x_n \}$ satisfies $x_n = c$ 
  for all $n$, then it is called a *constant* sequence.
````
An increasing sequence is bounded from below. Its greatest
lower bound is $x_1$. 

A decreasing sequence is bounded from above. Its least 
upper bound is $x_1$.

```{prf:remark} Unbounded increasing sequences
:label: rem-bra-seq-unbounded-increasing

Let $\{x_n\}$ be an increasing and unbounded sequence. 
Then for every $M > 0$, there exists $n_0 \in \Nat$ such that
for every $n > n_0$, $x_n > M$.
```

```{prf:remark} Unbounded decreasing sequences
:label: rem-bra-seq-unbounded-decreasing

Let $\{x_n\}$ be an decreasing and unbounded sequence. 
Then for every $M < 0$, there exists $n_0 \in \Nat$ such that
for every $n > n_0$, $x_n < M$.
```

````{prf:theorem} Convergence of bounded monotone sequences
:label: res-bra-sequence-monotone-bounded-convergence

Every monotone bounded sequence of real numbers is convergent.
````


````{prf:proof}
Let $\{ x_n \}$ be increasing and bounded sequence. From
{prf:ref}`completeness axiom <axm-rl-completeness-axiom>` 
it follows that there exists
$x = \sup \{ x_n \}$. 
We claim that $x$ itself is the limit of $\{ x_n \}$.
From
{prf:ref}`res-rl-supremum-epsilon` we recall that 
for every $\epsilon > 0$,
there exists a number $x_{n_0} \in \{ x_n \}$, such that

$$
    x - \epsilon < x_{n_0} \leq x.
$$

Since $\{ x_n \}$ is increasing, hence

$$
    x - \epsilon < x_{n} \leq x \quad \Forall n \geq n_0.
$$

This means that $| x - x_n | = x - x_n < \epsilon \Forall n \geq n_0$. Thus $x$ is
indeed the limit. We follow similar steps to prove for decreasing sequence.
````

````{prf:theorem} Convergence of constant sequences
:label: res-limit-constant-sequence

Let  $\{ x_n \}$ be a constant sequence with $x_n = c$. Then $\lim \{ x_n \} = c$.
````
````{prf:proof}
For all $\epsilon > 0$, $| x_n - c | = 0 < \epsilon$ for all $n \in \Nat$.
````


(sec:bra:sequences:calculus:limits)=
## The Calculus of Limits

Let $\{ x_n \}$ and $\{ y_n \}$ be convergent sequences of $\RR$.
Our concern here is to understand what happens to the limits if
the sequences are combined.

Let $\lim \{x_n\} = x$ and $\lim \{y_n\}  = y$. Then:

```{prf:theorem} Scaling a sequence
:label: res-bra-seq-calculus-scaling

$$
\lim \{\alpha x_n \} = \alpha x \Forall \alpha \in \RR.
$$
```

```{prf:proof}
If $\alpha = 0$, then we have a constant sequence and the result is trivial.
So assume that $\alpha \neq 0$. Then:

$$
    |\alpha x_n - \alpha x | = | \alpha |  | x_n - x |.
$$

Let $\epsilon > 0$ and choose $n_0 \in \Nat$ such that $| x - x_n | < \frac{\epsilon}{ | \alpha | }$
for all $n > n_0$. Then

$$
    |\alpha x_n - \alpha x | = | \alpha |  | x_n - x | < | \alpha | \frac{\epsilon}{ | \alpha | } = \epsilon \Forall n > n_0.
$$
```

```{prf:corollary} Negating a sequence
:label: res-bra-seq-calculus-negation

$$
\lim \{-x_n \} = -x.
$$
```

We get this result by choosing $\alpha = -1$.


```{prf:theorem} Addition of sequences
:label: res-bra-seq-calculus-addition

$$
\lim \{x_n  + y_n\} =  x + y.
$$
```
```{prf:proof}
From triangle inequality we get:

$$
    | x_n + y_n - (x + y) | \leq | x_n - x | + | y_n - y |.
$$

For any $\epsilon > 0$, choose $n_1$ such that $| x_n - x | < \frac{\epsilon}{2} \Forall n > n_1$.
Similarly, choose $n_2$ such that $| y_n - y | < \frac{\epsilon}{2} \Forall n > n_2$.
Now choose $n_0 = \max (n_1, n_2)$. Then:

$$
    | x_n + y_n - (x + y) |  \leq | x_n - x | + | y_n - y | < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
    \Forall n > n_0.
$$
```

```{prf:corollary} Subtraction of sequences
:label: res-bra-seq-calculus-subtraction

$$
\lim \{x_n  - y_n\} =  x - y.
$$
```
Negate $\{ y_n \}$ and add to $\{x_n \}$.


```{prf:theorem} Multiplication of sequences
:label: res-bra-seq-calculus-multiplication

$$
\lim \{x_n  y_n\} =  x y.
$$
```

```{prf:proof}
First let us assume that $x \neq 0$.
We note that:

$$
    | x_n y_n - x y | &= | x_n y_n - x y_n + x y_n - x y | \\
    &\leq | x_n y_n - x y_n | + | x y_n - x y |\\
    &= | y_n | |x_n - x |  + | x | | y_n - y |.
$$

Let $\epsilon > 0$ be arbitrary. Choose $n_1 > 0$ such that

$$
    n > n_1 \implies  |y_n - y | < \frac{1}{| x  |} \frac{\epsilon}{2}.
$$

Since {prf:ref}`every convergent sequence is bounded <res-bra-convergent-bounded>`,
let $M > 0$ be a bound of $\{y_n \}$ (i.e. $-M \leq y_n \leq M $). Choose $n_2 > 0$ such that

$$
    n > n_2 \implies  |x_n - x | < \frac{1}{M} \frac{\epsilon}{2}.
$$

Further choose $n_0 = \max(n_1, n_2)$. Then, we have

$$
    | x_n y_n - x y | \leq | y_n | |x_n - x |  + | x | | y_n - y |
    < | y_n | \frac{1}{M} \frac{\epsilon}{2}  + | x | \frac{1}{| x  |} \frac{\epsilon}{2}
    \leq \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.
$$

Since $\epsilon$ is arbitrary, hence we have shown that $\lim \{ x_n y_n \} = x y $.

Now consider the case where $x = 0$. We need to show that  $\lim \{ x_n y_n \} = 0 $.
Let $\epsilon > 0$ and choose $n_0$ such that $ |x_n - 0 | = | x_n | < \frac{\epsilon}{M}$ for all $n  > n_0$.
Then

$$
    | x_n y_n - 0 | \leq |x_n | | y_n| \leq |x_n | M <\frac{\epsilon}{M}  M  = \epsilon.
$$
```

```{prf:theorem} Division of sequences
:label: res-bra-seq-calculus-division

$$
\lim \{x_n / y_n\} =  x / y \text{ provided } y \neq 0.
$$
```

````{prf:proof}
If we can prove that $y_n \to y$ implies that $\frac{1}{y_n} \to \frac{1}{y}$
whenever $y \neq 0$, then the division of sequences
reduces to multiplication of sequences $\{ x_n \}$ and $\{ \frac{1}{y_n} \}$. 
But

$$
    \left | \frac{1}{y_n} - \frac{1}{y} \right | =  \frac{| y - y_n | }{ | y | |y_n |}.
$$

Choose $\epsilon_0 = | y | / 2$. Then there exists $n_1 \in \Nat$ such that
$| y - y_n | < \epsilon_0 = | y | / 2$ whenever $n > n_1$. This gives us,
$| y_n | > | y | / 2$ whenever $n > n_1$ (i.e. $y_n$ is so close to $y$ that
its magnitude is much larger than $| y | / 2$). Equivalently, we have

$$
    \frac{1}{ | y_n | } < \frac{2}{| y |} \quad \forall n > n_1.
$$

Next, for arbitrary $\epsilon > 0$, we choose $n_2$ such that for all $n > n_2$

$$
    | y_n - y | < \frac{\epsilon | y |^2}{2}.
$$

Finally, pick $n_0 = \max(n_1, n_2)$. Then $n > n_0$ implies

$$
    \left  | \frac{1}{y_n} - \frac{1}{y} \right |  = \frac{| y - y_n |}{ | y | |y_n |} <
    \frac{\epsilon | y |^2}{2} \frac{1}{| y |} \frac{2}{| y |} = \epsilon.
$$

Thus, $y_n \to y$ implies that $\frac{1}{y_n} \to \frac{1}{y}$
whenever $y \neq 0$. Now division reduces to multiplication and we are done.
````

Although some elements of $\{ y_n\}$ may be zero, but eventually
$y_n$ becomes arbitrarily close to $y$ and since $y \neq 0$, hence,

$$
0 < \frac{|y|}{2} < | y_n | < | y|  \Forall n > \text{ some } m.
$$

In other words, there comes a point $m$ in the sequence $Y$ so that all elements
in $Y$ after $y_m$ are non-zero with magnitude larger than $|y|/2$. 
We can practically throw away the first $m$ terms
from both the sequences $X$ and $Y$ and focus on the convergence of remaining
sequence. 


Next, we examine some of the order properties of the limits of sequences.

````{prf:theorem} Order limit theorem
:label: res-bra-order-limit


Assume $\lim x_n = x$ and $\lim y_n = y$.

1. If $x_n \geq 0$ for all $n \in \Nat$, then $x \geq 0$.
1. If $x_n \leq y_n$ for all $n \in \Nat$, then $x \leq y$.
1. If there exists $\alpha \in \RR$ for which 
   $\alpha \leq y_n$ for all $n \in \Nat$, then 
   $\alpha \leq y$. Similarly if $x_n \leq \alpha$ 
   for all $n \in \Nat$, then $x \leq \alpha$.
````
In words,

1. If a sequence is non-negative, then its limit is non-negative.
1. If one sequence is less than equal to another sequence for every term 
   in the sequence, then its limit is also less than equal to the other sequence.
1. A lower bound of a sequence is less than equal to its limit. 
   An upper bound of a sequence is greater than equal to its limit.

````{prf:proof}
(1) By contradiction, assume that $x < 0$.  Then $x + | x | = 0$.
Now consider $\epsilon = | x |$. Since $\{x_n \}$
is convergent, there exists $n_0 \in \Nat$ such that $ | x_n - x | < \epsilon = | x |$. Thus,

$$
    | x_n - x | < | x | \implies x - | x | < x_n < x + | x | \implies x_n < 0.
$$

This is a contradiction. Hence $x \geq 0$.

(2) By {prf:ref}`res-bra-seq-calculus-subtraction` we have,
$\lim (y_n - x_n) = y - x$. Since $y_n \geq x_n$, hence $y_n - x_n \geq 0$. From
(1), we get $y - x \geq 0$. This implies $y \geq x$.

(3) Take $x_n = \alpha$. Then $y_n \geq \alpha = x_n \implies y \geq \alpha$ (using (2)).
````

````{prf:corollary} Order limit theorem extension
:label: res-bra-order-limit-2


Assume $\lim x_n = x$ and $\lim y_n = y$.

1. If $x_n \geq 0$ for all $n > n_0$, then $x \geq 0$.
1. If $x_n \leq y_n$ for all $n > n_0$, then $x \leq y$.
1. If there exists $\alpha \in \RR$ for which 
   $\alpha \leq y_n$ for all $n > n_0$, then 
   $\alpha \leq y$. Similarly if $x_n \leq \alpha$ 
   for all $n > n_0$, then $x \leq \alpha$.
````

We throw away the first $n_0$ terms from each sequence and 
apply the theorem on the remaining part(s).

```{prf:example} Limits don't preserve strict inequality
:label: ex-bra-order-limit-strict-inequality

Consider $x_n = \frac{1}{n}$ and $y_n = \frac{1}{n+1}$. 
$\lim x_n = 0$. $\lim y_n = 0$. 

Thus, $x_n > y_n$ doesn't imply $\lim x_n > \lim y_n$.
We only have $x_n > y_n \implies x_n \geq y_n \implies \lim x_n \geq \lim y_n$.

Similarly,  $x_n > 0$ implies that $\lim x_n \geq 0$.
Or $x_n < r$ implies that $\lim x_n \leq r$.
```

````{prf:theorem} Squeeze theorem for sequences
:label: res-bra-sequence-squeeze

If $x_n \leq y_n \leq z_n$ for all $n \in \Nat$ and 
if $\lim x_n = \lim z_n = l$, then
$\lim y_n = l$.
````
````{prf:proof}
Let $\lim y_n = y$. Using {prf:ref}`order limit theorem <res-bra-order-limit>`,
$x_n \leq y_n$ gives us $l \leq y$ and $y_n \leq z_n$ gives us $y \leq l$. Thus,
$l \leq y \leq l \implies y = l$.
````

````{prf:corollary} Squeeze theorem for sequences extension
:label: res-bra-sequence-squeeze-2

Let $\lim x_n = \lim z_n = l$. If there exists $n_0 \in \Nat$ such that
for all $n > n_0$, $x_n \leq y_n \leq z_n$,
then $\lim y_n = l$.
````

Drop the first $n_0$ terms from all the three sequences and then apply the theorem
on remaining sequences.

````{prf:theorem} Convergence of absolute sequence
:label: res-bra-sequence-convergence-absolute

If $x_n \to x$, then $| x_n | \to x$. But the converse is not true.
````
````{prf:proof}
Since $x_n \to x$, for every $\epsilon > 0$, there exists $n_0 \in \Nat$ such that
$n > 0$ implies $ | x_n  - x | < \epsilon$. By triangle inequality

$$
    | | x_n | - | x | | \leq | x_n - x | < \epsilon.
$$

This completes the proof.

Now consider the sequence

$$
    \{ 1, -1, 1, -1, 1, -1, \dots \}.
$$

Although in absolute value it converges to $1$, the sequence itself doesn't converge. 
Thus, the converse is not true.
````



## Infinite Series



````{prf:definition}
:label: def-bra-infinite-series

Let $\{ x_n \}$ be a sequence. An *infinite series* is a formal expression of the form

$$
    \sum_{n  = 1}^{\infty} x_n = x_1 + x_2 + x_3 + x_4 + \dots.
$$

The corresponding *sequence of partial sums* $\{ s_m\}$ is defined as

$$
    s_m = x_1 + \dots + x_m.
$$

We say that the series $\sum_{n  = 1}^{\infty} x_n$ converges to some $s \in \RR$ 
if the sequence
$\{ s_m \}$ converges to $s$. In this case we write

$$
    \sum_{n  = 1}^{\infty} x_n = s.
$$
````

````{prf:example} Convergent series
:label: ex-bra-seq-convergent-series-1

Consider

$$
    \sum_{n  = 1}^{\infty} \frac{1}{n^2}.
$$

Looking at the partial sums, we observe:

$$
    s_m &= 1 + \frac{1}{4} + \frac{1}{9} \dots + \frac{1}{m^2}\\
    & < 1 + \frac{1}{2 \cdot 1} + \frac{1}{3 \cdot 2} + \dots \frac{1}{m \cdot (m - 1)}\\
    & =  1 + \left (1  - \frac{1}{2} \right) + \left (\frac{1}{2}  - \frac{1}{3} \right)
    + \dots + \left (\frac{1}{m - 1}  - \frac{1}{m} \right) \\
    & = 1 + 1  - \frac{1}{m} \\
    &< 2.
$$

 Thus, $2$ is an upper bound of the sequence of partial sums. Hence, by
 {prf:ref}`monotone convergence theorem <res-bra-sequence-monotone-bounded-convergence>`,
 the series converges to some (unknown) limit less than 2.
````

````{prf:example} Harmonic series
:label: ex-bra-seq-harmonic-series-1

Consider

$$
    \sum_{n  = 1}^{\infty} \frac{1}{n}.
$$

We note that

$$
    s_4 = 1 + \frac{1}{2} + \left (\frac{1}{3} + \frac{1}{4} \right )
    > 1 + \frac{1}{2}  + \left (\frac{1}{4} + \frac{1}{4} \right ) = 2.
$$

Similarly, we find that $s_8 > 2\frac{1}{2}$.
Further, we note that:

$$
    s_{2^k} &= 1 + \frac{1}{2} + \left (\frac{1}{3} + \frac{1}{4} \right )  +
    \left (\frac{1}{5} +  \dots + \frac{1}{8} \right ) + \dots +
    \left (\frac{1}{2^{k - 1} + 1} + \dots + \frac{1}{2^k} \right )  \\
    &> 1 + \frac{1}{2} + \left (\frac{1}{4} + \frac{1}{4} \right )  +
    \left (\frac{1}{8} +  \dots + \frac{1}{8} \right ) + \dots +
    \left (\frac{1}{2^k} + \dots + \frac{1}{2^k} \right )  \\
    &= 1 + \frac{1}{2} + 2 \frac{1}{4} + 4 \frac{1}{8} + \dots + 2^{k - 1} \frac{1}{2^k} \\
    &= 1 + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \dots + \frac{1}{2}\\
    &= 1 + k \frac{1}{2}.
$$

Thus, the harmonic series is unbounded.
````
````{prf:theorem} Cauchy condensation test
:label: res-bra-cauchy-condensation-test

Suppose $\{ x_n \}$ is decreasing and satisfies $x_n \geq 0$ for all $n \in \Nat$.
Then, the series $\sum_{n  = 1}^{\infty} x_n$ converges if and only if the
series

$$
    \sum_{n  = 0}^{\infty} 2^n x_{2^n} = x_1 + 2 x_2 + 4 x_4 + 8 x_8 + 16 x_{16} + \dots
$$
converges.
````
````{prf:proof}
Let $y_n = 2^{n-1} x_{2^{n-1}}$. Then, the second series is $\sum_{n  = 1}^{\infty} y_n$.
Let the partial sums of $\{ x_n \}$ be $s_m$ and the partial sums of $\{ y_n\}$ be
$t_k$.

First, assume that  $\sum_{n  = 1}^{\infty} y_n$ converges. Thus, the
sequence $\{ t_k \}$ converges.
Since {prf:ref}`every convergent sequence is bounded <res-bra-convergent-bounded>`,
the sequence $\{ t_k \}$ is bounded. Thus, there exists $M > 0$ such that
$t_k \leq M$ for all $k \in \Nat$. Since $x_n \geq 0$, the partial sums $s_m$
are increasing. Thus, if we show that $ \{ s_m \}$ is bounded, then by
{prf:ref}`monotone convergence theorem <res-bra-sequence-monotone-bounded-convergence>`,
we would have shown that $\{s_m\}$ converges, hence the series
$\sum_{n  = 1}^{\infty} x_n$ converges.

Let us fix $m$ and choose $k$ to be large enough so that $m \leq 2^{k + 1} - 1$.
Then $s_m \leq s_{2^{k + 1} - 1}$. Now,

$$
    s_{2^{k + 1} - 1} &= x_1 + (x_2 + x_3) + (x_4 + \dots x_7) + \dots
    + \dots + (x_{2^k} + \dots + x_{2^{k + 1} - 1})\\
    &\leq x_1 + (x_2 + x_2) + (x_4 + x_4 + x_4 + x_4) + \dots + (x_{2^k} + \dots + x_{2^k})\\
    &= x_1 + 2 x_2 + \dots + 2^k x_{2^k}\\
    &= y_1 + y_2 + \dots + y_k \\
    &= t_k.
$$

Thus, $s_m \leq t_k \leq M$. $\{s_m \}$ is bounded, hence convergent.

We now show that if $\sum_{n  = 1}^{\infty} y_n$ diverges, then
$\sum_{n  = 1}^{\infty} x_n$ diverges too.

Consider the sum

$$
    s_{2^k} &= x_1 + x_2 + (x_3 + x_4) + (x_5 + \dots + x_8) + \dots  +
    (x_{2^{k -1 } + 1} + \dots x^{2^k})\\
    &\geq x_1 + x_2 +  (x_4 + x_4) + (x_8 + \dots + x_8) + \dots  +
    (x_{2^k} + \dots x_{2^k})\\
    &= x_1 + x_2 + 2 x_4 + 4 x_8 + \dots 2^{k - 1} x_{2^k}\\
    &= \frac{1}{2} x_1 + \frac{1}{2} \left (x_1 + 2 x_2 + 4 x_4 + 8 x_8 + \dots + 2^k x^{2^k} \right )\\
    &= \frac{1}{2} x_1 + t_k \geq t_k.
$$

Now, since $\{ t_k \}$ diverges, hence $\{ s_{2^k} \}$ too diverges. Thus, the series diverges.
````

```{prf:definition} Absolutely summable
:label: def-bra-absolutely-summable-series

A series $\sum x_n$ is called *absolutely summable* if 
$\sum |x_n|$ converges. 

A sequence $\{x_n \}$ is called *absolutely summable* if
$\sum |x_n|$ converges.
```


## Subsequences




````{prf:theorem} Subsequence convergence
:label: res-subsequence-convergence

Subsequences of a convergent sequence converge to the same limit 
as the original sequence.
If $\lim_{n \to \infty} x_n = x$, then $\lim_{n \to \infty} y_n = x$ for every
{prf:ref}`subsequence <def-st-sub-sequence>` $\{ y_n \}$ of $\{ x_n \}$.

Conversely, if two different subsequences of $\{ x_n \}$ converge to different limits,
then the sequence  $\{ x_n \}$  does not converge.
````
````{prf:proof}
Since $\lim_{n \to \infty} x_n = x$, for every $\epsilon > 0$, there exists $n_0 \in \Nat$ such that
$| x - x_n | < \epsilon \Forall n > n_0$.
Now, if $\{ y_n \}$ is a subsequence, then there exists a strictly increasing sequence
$\{ k_n \}$ of natural numbers (i.e. $1 \leq k_1 < k_2  < k_3 < \ldots)$
such that $y_n = x_{k_n}$ holds for each $n$. Clearly, there exists a $k_0 > 0$ such that
$k_n \geq n_0 \Forall n > k_0$. Then,
$| x - y_n | < \epsilon \Forall n > k_0$.
Thus, $\{ y_n \}$ converges to $x$ too.
````

````{prf:theorem} Bolzano Weierstrass theorem
:label: res-bolzano-weierstrass-theorem

Every bounded sequence contains a convergent subsequence.
````
The proof of this theorem follows a constructive approach 
(i.e., we will construct a subsequence and show that it is convergent). 
We construct a sequence of nested closed intervals with increasingly
smaller lengths and pick a point in each such interval to form 
a subsequence.

````{prf:proof}
Let $\{ x_n \}$ be a bounded sequence. Thus, there exists $M > 0$ such that
$ | x_n | \leq M$ for all $n \in \Nat$. Divide the interval $[-M, M]$ into
two equal closed intervals $[-M, 0]$ and $[0, M]$. At least one of the two halves must have
an infinite number of points in $\{ x_n \}$
(since if both halves had finite number of points, then the total number of points
in the sequence would be finite which is a contradiction).
Choose a half for which this is true, and label this half as $I_1$.
Choose a point $x_{n_1} \in I_1$. Now divide $I_1$ into two equal closed intervals.
Again, since $I_1$ contains infinite number of points, hence at least one
of the halves must have infinite number of points. Pick a half which contains
infinite number of points and label it as $I_2$. Now, pick a point $x_{n_2}$ from
$I_2$ such that $n_2 > n_1$. In general, construct a closed interval $I_k$ from
a half of $I_{k-1}$ containing infinite number of points. Further, we choose
a point $x_{n_k}$ such that $n_k > n_{k-1} > \dots > n_2 > n_1$ and $x_{n_k} \in I_k$.
We claim that the subsequence $\{x_{n_k} \}$ is a convergent subsequence. For this, we need
a limit for the sequence. Since

$$
    I_1 \supseteq I_2 \supseteq \dots \supseteq I_k \supseteq \dots
$$

are a nested sequence of closed intervals, hence by
{prf:ref}`nested interval property <res-rl-nested-interval-property>`, their
intersection $I = \bigcap_{k=1}^{\infty} I_k$
is non-empty.
Actually, it's easy to show that this $I$ is a
singleton too. If there were two distinct points $x, y$ in $I$, then
considering $d = | x - y | > 0$, we could find an interval $I_j$ whose length
is smaller than $d$. Thus both $x, y$ could not fit in $I_j$. Hence $I$ contains
only one point. Let $I = \{ x \}$. We now
show that $x_{n_k} \to x$.

Let $\epsilon > 0$. By construction, the length of $I_k$ is $M\frac{1}{2^{k-1}}$. Since
it converges to 0, hence, we can choose $n_0 \in \Nat$ such that for every $k > n_0$,
the length of $I_k$ is less than $\epsilon$. Since $x$ and $x_{n_k}$ are both in $I_k$,
hence it follows that $| x_{n_k} - x| < \epsilon$.
````



## Cauchy Sequence



````{prf:definition} Cauchy sequence
:label: def-bra-cauchy-sequence

A sequence $\{ x_n \}$ in $\RR$ is called a *Cauchy sequence* if,
for every $\epsilon > 0$, there exists $n_0 \in \Nat$ (depending on $\epsilon$)
such that whenever $m, n > n_0$ it follows that $| x_m - x_n | < \epsilon$.
````
````{prf:remark}
:label: rem-bra-seq-cauchy-m-n

A little thought would show that  saying $m, n > n_0$ or $m, n \geq n_1$ doesn't make much difference
in the definition. The two thresholds can be related by : $n_1 = n_0 + 1$.
````

````{prf:theorem} Boundedness of Cauchy sequences
:label: res-bra-cauchy-sequence-bounded

A Cauchy sequence is bounded.
````
````{prf:proof}
Let $\{ x_n \}$. Choose $\epsilon = 1$. Then there exists
$n_0 \in \Nat$ such that $ | x_n - x_m | < 1$ whenever $m, n \geq n_0$.
In particular, the statement is valid when $m  = n_0$. i.e. $ | x_n - x_{n_0} | < 1$ .
But,

$$
    | x_n - x_{n_0} | < 1 \implies | | x_n | - | x_{n_0 } | | < 1 \implies |x_n | < 1  + | x_{n_0 } | \Forall n \geq n_0.
$$

Choosing $M = \max(|x_1|, \dots, |x_{n_0-1}|, |x_{n_0}| + 1)$, it is clear that $| x_n | \leq M$, hence $\{ x_n \}$ is bounded.
````

```{prf:theorem} Convergence of Cauchy sequences
:label: res-bra-cauchy-sequence-convergent

A Cauchy sequence is convergent.
```

```{prf:proof}
Let $\{ x_n \}$ be a Cauchy sequence. 
Hence it is {prf:ref}`bounded <res-bra-cauchy-sequence-bounded>`.
Hence, by {prf:ref}`Bolzano Weierstrass theorem <res-bolzano-weierstrass-theorem>`, 
it has a convergent subsequence. 

Let $\{ x_{n_k} \}$ be such a convergent subsequence with the limit $\lim x_{n_k} = x$.

Thus, for any $\epsilon > 0$, there exists $n_1 \in \Nat$ such that for all $k > n_1$, 

$$
| x_{n_k} - x | < \frac{\epsilon}{2}.
$$ 

Also, since $\{x_n \}$ is Cauchy, there exists $n_2 \in \Nat$ such that for all 
$n, m > n_2$, 

$$
|x_n - x_m | < \frac{\epsilon}{2}.
$$

Pick any $k > n_1$ such that $n_k > n_2$. Then, for all $n > n_2$, 

$$
|x_n - x | \leq |x_n - x_{n_k} | + |x_{n_k} - x | < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.
$$

Thus, $\lim x_n = x$. 
```

````{prf:theorem} Convergence and Cauchyness
:label: res-bra-cauchy-sequence-convergence

A sequence of real numbers converges if and only if it is a Cauchy sequence.
````

````{prf:proof}
Let a sequence $\{ x_n \}$ converge to $\epsilon$. Then for every $\epsilon > 0$, there exists
$n_0 \in \Nat$ such that $| x_n - x | < \epsilon / 2$ for all $n > n_0$. Clearly, if $m, n > n_0$, then

$$
    | x_m - x_n | \leq | x_m - x | + | x - x_n | < \frac{\epsilon}{2}  + \frac{\epsilon}{2}  = \epsilon.
$$

Thus, $\{ x_n \}$ is Cauchy.

For the converse, in the previous theorem, we proved that a Cauchy sequence is convergent.
````

```{prf:remark}
Let $\{ x_n \}$ be a Cauchy sequence with $\lim x_n = x$. 
Let $\epsilon > 0$. Choose $n_0$ such that $m, n > n_0$ implies
$|x_m - x_n| < \epsilon$.

Then

$$
|x_n - x | \leq \epsilon \Forall n > n_0.
$$
```

```{prf:proof}
We have, for all $m, n > n_0$

$$
|x_m - x_n | < \epsilon \iff x_m - \epsilon < x_n < x_m + \epsilon.
$$
We will fix $n$ and vary $n$ to compute the limit inequalities. 

1. Consider the strict inequality: $x_m - \epsilon < x_n$ for all $m > n_0$.
1. Taking the limit on the sequence $x_m$ (in L.H.S.), we get: $x - \epsilon \leq x_n$.
1. Consider the strict inequality: $x_n < x_m + \epsilon$ for all $m > n_0$.
1. Taking the limit on the sequence $x_m$ (in R.H.S.), we get: $x_n \leq x + \epsilon$.
1. Together, we get: $x - \epsilon \leq x_n \leq x + \epsilon$.
1. Combining, we get $|x_n -x| \leq \epsilon$ for all $n > n_0$.

See also {prf:ref}`ex-bra-order-limit-strict-inequality`.
```


## Limit Inferior and Limit Superior


```{prf:theorem} Sequences of partial suprema and infima
:label: res-bra-bounded-seq-sup-inf-subseq-converg

Let $\{ x_n \}$ be a sequence of $\RR$. 
Define

$$
s_n = \sup \{ x_k \ST k \geq n\}
$$
and

$$
t_n = \inf \{ x_k \ST k \geq n\}.
$$

If $\{ x_n \}$ is not bounded above, then

$$
\lim_{n \to \infty} s_n = \infty.
$$

If $\{ x_n \}$ is not bounded below, then

$$
\lim_{n \to \infty} t_n = -\infty.
$$

If $\{x_n\}$ is bounded from above, then
$\{ s_n \}$ is a nonincreasing sequence.

If $\{x_n\}$ is bounded from below, then
$\{ t_n \}$ is a nondecreasing sequence.

If $\{ x_n \}$ is bounded, then both the sequences
$\{ s_n \}$ and $\{ t_n \}$ are convergent.
```

```{prf:proof}

Let $\{x_n \}$ not be bounded from above. 

1. Then, for any $n \in \Nat$, the set $\{ x_k \ST k \geq n \}$ is also
   not bounded from above.
1. Thus, $s_n = \sup \{ x_k \ST k \geq n\} = \infty$ for all $n \in \Nat$.
1. Thus, $\lim_{n \to \infty} s_n = \infty$.


Let $\{x_n \}$ not be bounded from below. 

1. Then, for any $n \in \Nat$, the set $\{ x_k \ST k \geq n \}$ is also
   not bounded from below.
1. Thus, $t_n = \inf \{ x_k \ST k \geq n\} = -\infty$ for all $n \in \Nat$.
1. Thus, $\lim_{n \to \infty} t_n = -\infty$.


We note that for $m < n$,

$$
\{ x_k \ST k \geq n\} \subseteq \{ x_k \ST k \geq m\}.
$$


Now, assume that $\{x_n \}$ is bounded from above. 

1. Then, $\sup \{ x_k \ST k \geq n\} \leq \sup \{ x_k \ST k \geq m\}$.
1. Or $s_n \leq s_m$.
1. Thus, $m < n$ implies that $s_m \geq s_n$.
1. Thus, $\{ s_n \}$ is a nonincreasing sequence.

Now, assume that $\{x_n \}$ is bounded from below. 

1. Then, $\inf \{ x_k \ST k \geq n\} \geq \inf \{ x_k \ST k \geq m\}$.
1. Or $t_n \geq t_m$.
1. Thus, $m < n$ implies that $t_m \leq t_n$.
1. Thus, $\{ t_n \}$ is a nondecreasing sequence.

Now, assume that $\{x_n \}$ is bounded. 


1. From {prf:ref}`res-bra-sequence-monotone-bounded-convergence`,
   a monotone bounded sequence is convergent.
1. Since $\{ x_n \}$ is bounded, hence $\{ s_n \}$ is bounded too.
1. Since $\{ x_n \}$ is bounded, hence $\{ t_n \}$ is bounded too.
1. Thus, both $\{ s_n \}$ and $\{ t_n \}$ are bounded and monotone.
1. Thus, both of them are convergent sequences.
```

```{prf:definition} Limit superior and inferior
:label: def-bra-lim-sup-inf

Let $\{x_n \}$ be a sequence of $\RR$. 
The *limit superior* of the sequence is defined as:

$$
\limsup_{n \to \infty} x_n 
\triangleq \lim_{n \to \infty} \sup \{x_k \ST k \geq n \}.
$$

Similarly, the *limit inferior* of the sequence is defined as:

$$
\liminf_{n \to \infty} x_n 
\triangleq \lim_{n \to \infty} \inf \{x_k \ST k \geq n \}.
$$

If we define

$$
s_n = \sup \{ x_k \ST k \geq n\}
\text{ and }
t_n = \inf \{ x_k \ST k \geq n\}
$$
then,

$$
\limsup_{n \to \infty} x_n = \lim_{n \to \infty} s_n
$$
and

$$
\liminf_{n \to \infty} x_n  = \lim_{n \to \infty} t_n.
$$
```

It is imperative to establish that the definition of 
limit inferior and limit superior is justified. 

1. If $\{x_n \}$ is not bounded from above, then $s_n = \infty$.
1. If $\{x_n \}$ is bounded from above then $\{ s_n \}$ is nondecreasing.
1. In this case, if $\{x_n \}$ is bounded from below, then $\{ s_n \}$
   converges, otherwise it diverges to $-\infty$.

Similar justification applies for the limit inferior too. 

```{prf:remark} Limit superior and inferior for unbounded sequences
:label: ref-bra-lim-sup-inf-unbounded

Let $\{ x_n \}$ be a sequence of $\RR$.

If $\{ x_n \}$ is not bounded from above, then

$$
\limsup_{n \to \infty} x_n = \infty.
$$

If $\{ x_n \}$ is not bounded from below, then

$$
\liminf_{n \to \infty} x_n = -\infty.
$$
```

```{prf:theorem} Limit superior $\geq$ limit inferior
:label: res-bra-limsup-geq-liminf

Let $\{ x_n \}$ be a sequence of $\RR$.
Then,

$$
\liminf_{n \to \infty} x_n \leq
\limsup_{n \to \infty} x_n.
$$
```

```{prf:proof}

If we define

$$
s_n = \sup \{ x_k \ST k \geq n\}
\text{ and }
t_n = \inf \{ x_k \ST k \geq n\}
$$
then, $t_n \leq s_n$ for every $n$. 

Then, by {prf:ref}`res-bra-order-limit`,

$$
\lim_{n \to \infty} t_n \leq \lim_{n \to \infty} s_n.
$$

Thus,

$$
\liminf_{n \to \infty} x_n  = \lim_{n \to \infty} t_n
\leq \lim_{n \to \infty} s_n = \limsup_{n \to \infty} x_n.
$$
```


```{prf:theorem} Relationship between limit superior and inferior
:label: res-bra-limsup-liminf-rel

Let $\{ x_n \}$ be a sequence of $\RR$. Then,

$$
\limsup_{n \to \infty} (-x_n) = - \liminf_{n \to \infty} x_n. 
$$
```

```{prf:proof}
We recall that

$$
\inf(-1 \cdot A) = -1 \cdot \sup (A)
\text{ and }
\sup(-1 \cdot A) = -1 \cdot \inf \sup (A)
$$

Thus,

$$
\limsup_{n \to \infty} (-x_n)
&= \lim_{n \to \infty} \sup \{-x_k \ST k \geq n \}\\
&= \lim_{n \to \infty} -\inf \{x_k \ST k \geq n \}\\
&= - \lim_{n \to \infty} \inf \{x_k \ST k \geq n \}\\
&= - \liminf_{n \to \infty} x_n.
$$
```


```{prf:theorem} Characterization of limit superior
:label: res-bra-lim-sup-charac

Let $\{ x_n \}$ be a sequence of $\RR$. Let $u \in \RR$.
The following are equivalent.

1. $\limsup_{n \to \infty} x_n = u$.
1. For any $\epsilon > 0$, there exists $n_0 \in \Nat$ such that
   
   $$
   x_n < u + \epsilon \Forall n \geq n_0.
   $$
   and there exists a subsequence $\{x_{k_n} \}$ of $\{ x_n \}$
   such that $\lim_{n \to \infty} x_{k_n} = u$.
```


```{prf:proof}
TBD
```


```{prf:theorem} Characterization of limit inferior
:label: res-bra-lim-inf-charac

Let $\{ x_n \}$ be a sequence of $\RR$. Let $l \in \RR$.
The following are equivalent.

1. $\liminf_{n \to \infty} x_n = l$.
1. For any $\epsilon > 0$, there exists $n_0 \in \Nat$ such that
   
   $$
   x_n > l - \epsilon \Forall n \geq n_0.
   $$
   and there exists a subsequence $\{x_{k_n} \}$ of $\{ x_n \}$
   such that $\lim_{n \to \infty} x_{k_n} = l$.
```

```{prf:proof}
TBD
```

This leads us to the fact that the limit of a sequence
exists if and only if its limit inferior and limit superior
are identical.

### Existence of Limit

```{prf:theorem} Limit = limit superior = limit inferior
:label: res-bra-lim-eq-liminf-limsup

Let $\{ x_n \}$ be a sequence of $\RR$.
Then,

$$
\lim_{n \to \infty} x_n = l
\text{ if and only if }
\limsup_{n \to \infty} x_n = \liminf_{n \to \infty} x_n = l.
$$

In other words the limit of a sequence exists if and only
if both limit superior and limit inferior are equal and in 
this case, the limit of sequence equals the limit superior
and inferior.
```

```{prf:proof}
TBD
```

### Subsequences

```{prf:theorem} Convergent subsequences and limit superior/inferior
:label: res-bra-subseq-lim-liminf-limsup

Let $\{ x_n \}$ be a sequence of $\RR$.
Let $\{ x_{k_n} \}$ be an arbitrary subsequence of $\{ x_n \}$.

Suppose $\limsup x_n = u$.
If $\{ x_{k_n} \}$ converges then

$$
\lim_{n \to \infty} x_{k_n} \leq u.
$$


Suppose $\liminf x_n = l$.
If $\{ x_{k_n} \}$ converges then

$$
\lim_{n \to \infty} x_{k_n} \geq l.
$$
```

```{prf:proof}
Assume that $\limsup x_n = u$.

1. Let $\epsilon > 0$.
1. By {prf:ref}`res-bra-lim-sup-charac`, there exists $n_0$ 
   such that for all $n > n_0$

   $$
   x_n < u + \epsilon.
   $$
1. Let  $\lim_{n \to \infty} x_{k_n} = s$.
1. Then, there exists $n_1$ such that for all $k_n > n_1$

   $$
   s - \epsilon < x_{k_n} < s + \epsilon.
   $$
1. Let $n_2 = \max(n_0, n_1)$.
1. Then, for all $k_n > n_2$

   $$
   s - \epsilon < x_{k_n} < u + \epsilon.
   $$
1. Thus, $s < u + 2 \epsilon$ for every $\epsilon > 0$.
1. Thus, $s \leq u$.

The proof for limit inferior is similar.
```

```{prf:remark} The set of subsequential limits for bounded sequences
:label: res-bra-set-subseq-limits-limsup-liminf

Let $\{ x_n \}$ be a bounded sequence of $\RR$.
Define

$$
A = \{ x \in \RR \ST \text{ there exists a subsequence } 
\{ x_{k_n} \} \text{ with } 
\lim x_{k_n} = x \}.
$$
This is the set of limits of convergent subsequences of $\{ x_n \}$.
By {prf:ref}`res-bolzano-weierstrass-theorem`
$\{ x_n \}$ has a convergent subsequence since it is bounded.
Hence, $A$ is not empty.

Each element of $A$ is called a *subsequential limit* of $\{x_n \}$.
Due to {prf:ref}`res-bra-bounded-seq-sup-inf-subseq-converg`, 
both $\limsup x_n$ and $\liminf x_n$ are finite since $\{ x_n \}$
is bounded.

Let $a \in A$. Then, by {prf:ref}`res-bra-subseq-lim-liminf-limsup`:

$$
\liminf x_n \leq a \leq \limsup x_n.
$$

By {prf:ref}`res-bra-lim-sup-charac`, there exists $u \in A$
such that

$$
\limsup x_n = u.
$$

By {prf:ref}`res-bra-lim-inf-charac`, there exists $l \in A$
such that

$$
\liminf x_n = l.
$$

Thus,

$$
\limsup x_n = \max A
\text{ and }
\liminf x_n = \min A.
$$
```

### Arithmetic

```{prf:theorem} Arithmetic of limit superior and inferior
:label: res-bra-arithmetic-limsup-liminf

Let $\{ a_n \}$ and $\{ b_n \}$ be sequences of $\RR$.

The limit superior satisfies subadditivity.

$$
\limsup_{n \to \infty} (a_n + b_n) \leq 
\limsup_{n \to \infty} a_n + \limsup_{n \to \infty} b_n.
$$

The limit inferior satisfies superadditivity.

$$
\liminf_{n \to \infty} (a_n + b_n) \geq
\liminf_{n \to \infty} a_n + \liminf_{n \to \infty} b_n.
$$

If both $\{ a_n \}$ and $\{ b_n \}$ are nonnegative, 
then

$$
\limsup_{n \to \infty} (a_n b_n) \leq
\left (\limsup_{n \to \infty} a_n \right)
\left ( \limsup_{n \to \infty} b_n \right)
$$
and

$$
\liminf_{n \to \infty} (a_n b_n) \geq
\left (\liminf_{n \to \infty} a_n \right)
\left ( \liminf_{n \to \infty} b_n \right).
$$
```


### Order

```{prf:theorem} Order properties of limit superior and inferior
:label: res-bra-order-limsup-liminf

Let $\{ x_n \}$ and $\{ y_n \}$ be sequences of $\RR$.


1. If $x_n \geq 0$ for all $n \in \Nat$, 
   then $\liminf_{n \to \infty} x \geq 0$.   
1. If $x_n \leq 0$ for all $n \in \Nat$, 
   then $\limsup_{n \to \infty} x \leq 0$.
1. If $x_n \leq y_n$ for all $n \in \Nat$, 
   then $\limsup x_n \leq \limsup y_n$.
1. If $x_n \geq y_n$ for all $n \in \Nat$, 
   then $\liminf x_n \geq \liminf y_n$.
```

```{prf:proof}

Assume that $x_n \geq 0$.

1. Then, $\inf \{x_k \ST k \geq n \} \geq 0$.
1. Thus, 

   $$
    \liminf_{n \to \infty} x_n 
    = \lim_{n \to \infty} \inf \{x_k \ST k \geq n \}
    \geq \lim_{n \to \infty} 0 = 0.
   $$


Assume that $x_n \leq 0$.

1. Then, $\sup \{x_k \ST k \geq n \} \leq 0$.
1. Thus, 

   $$
    \limsup_{n \to \infty} x_n 
    = \lim_{n \to \infty} \sup \{x_k \ST k \geq n \}
    \leq \lim_{n \to \infty} 0 = 0.
   $$


Assume that $x_n \leq y_n$ for all $n \in \Nat$.

1. Choose any $k \in \Nat$.
1. Let $M_n = \sup \{y_k \ST k \geq n \}$.
1. Then, $y_k \leq M_n$ for every $k \geq n$.
1. Then, $x_k \leq y_k \leq M_n$ for every $k \geq n$.
1. Taking supremum over $k \geq n$, 
   $m_n = \sup \{x_k \ST k \geq n \} \leq M_n$.
1. Thus, $m_n \leq M_n$ for every $n$.
1. Thus, by {prf:ref}`res-bra-order-limit`,
   $\lim m_n \leq \lim M_n$.
1. Thus,  $\limsup x_n \leq \limsup y_n$.

A similar argument can be used for $x_n \geq y_n$ also.
```


### Damping and Growing Sequences

```{prf:theorem} Damping sequences
:label: res-bra-damping-sequence

Let $\{ x_n \}$ be a sequence of $\RR$ such that $x_n > 0$ for every $n$.

Assume that the following holds:

$$
\limsup_{n \to \infty} \frac{x_{n+1}}{x_n} = u < 1.
$$

Then, $\lim_{n \to \infty} x_n = 0$.
```

```{prf:proof}
We proceed as follows.

1. Since $\frac{x_{n+1}}{x_n} > 0$, hence $u \geq 0$.
1. Since $u < 1$, we can choose an $\epsilon > 0$ such that
   $u + \epsilon < 1$.
1. Let $q = u + \epsilon$. Then, $0 < q < 1$.
1. By {prf:ref}`res-bra-lim-sup-charac`, there exists $n_0 \in \Nat$
   such that for all $n \geq n_0$

   $$
   \frac{x_{n+1}}{x_n} < u + \epsilon = q.
   $$
1. Thus, $x_{n+1} < q x_n$ for every $n \geq n_0$.
1. Let $x = x_{n_0}$.
1. Then, we have $x_n < q^{n - n_0} x$ for every $n > n_0$.
1. Also, $\lim_{n \to \infty} q^{n - n_0} x = 0$ since $q < 1$.
1. We have $0 < x_n < q^{n - n_0} x$ for all $n > n_0$.
1. Hence, due to the
   {prf:ref}`squeeze theorem <res-bra-sequence-squeeze-2>`,
   $\lim_{n \to \infty} x_n = 0$. 
```


```{prf:theorem} Growing sequences
:label: res-bra-growing-sequence

Let $\{ x_n \}$ be a sequence of $\RR$ such that $x_n > 0$ for every $n$.

Assume that the following holds:

$$
\liminf_{n \to \infty} \frac{x_{n+1}}{x_n} = l > 1.
$$

Then, $\lim_{n \to \infty} x_n = \infty$.
```


```{prf:proof}
We proceed as follows.

1. Since $l > 1$, we can choose an $\epsilon > 0$ such that
   $l - \epsilon > 1$.
1. Let $q = l - \epsilon$. Then, $q > 1$.
1. By {prf:ref}`res-bra-lim-inf-charac`, there exists $n_0 \in \Nat$
   such that for all $n \geq n_0$

   $$
   \frac{x_{n+1}}{x_n} > l - \epsilon = q.
   $$
1. Thus, $x_{n+1} > q x_n$ for every $n \geq n_0$.
1. Let $x = x_{n_0}$.
1. Then, we have $x_n > q^{n - n_0} x$ for every $n > n_0$.
1. Also, $\lim_{n \to \infty} q^{n - n_0} x = \infty$ since $q > 1$.
1. We have $x_n > q^{n - n_0} x$ for all $n > n_0$.
1. Hence, $\lim x_n \geq \lim q^{n - n_0} x = \infty$.
1. Thus, $\lim x_n = \infty$.
```

