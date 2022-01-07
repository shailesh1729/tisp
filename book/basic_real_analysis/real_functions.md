# Real Functions
In this section, we will deal with functions of type $f : \RR \to \RR$. 
Main references are 
{cite}`trench2003introduction,aliprantis1998principles`. 

Our goal is a cursory review of the relevant theory. We will
state the main definitions and results and provide a few
examples wherever needed. Detailed proofs will be skipped.
 
```{prf:definition} Real function
:label: def-bra-real-function

A (partial) function of type $f: \RR \to \RR$ mapping 
real values to real values is called a *real function*.
```

The domain and range of a real function are both subsets of $\RR$.

```{prf:definition} Arithmetic operators
:label: def-bra-real-function-arithmetic

Let $f,g$ be real functions with $\dom f \cap \dom g \neq \EmptySet$.

We define $f+g$ as:

$$
(f + g)(x) = f(x) + g(x) \Forall x \in \dom f \cap \dom g.
$$

We define $f-g$ as:

$$
(f - g)(x) = f(x) - g(x) \Forall x \in \dom f \cap \dom g.
$$


We define $f g$ as:

$$
(f g)(x) = f(x) g(x) \Forall x \in \dom f \cap \dom g.
$$


We define the quotient $f/g$ as:

$$
\left ( \frac{f}{g} \right )(x) = \frac{f(x)}{g(x)} 
\Forall x \in \dom f \cap \dom g \text{ such that } g(x) \neq 0.
$$

For some $c \in \RR$, we define $cf$ as:

$$
(cf)(x) = cf(x) \Forall x \in \dom f.
$$
```

```{prf:example}
Let $f_1, f_2, \dots, f_n$ be real functions.

Then, their sum is defined by:

$$
(f_1 + f_2 + \dots + f_n)(x) = f_1(x) + f_2(x) + \dots + f_n(x) 
\Forall x \in \bigcap_{i=1}^n \dom f_i
$$

and their product is defined by:

$$
(f_1 f_2 \dots f_n)(x) = f_1(x) f_2(x) \dots f_n(x) 
\Forall x \in \bigcap_{i=1}^n \dom f_i
$$

provided the domain $D = \bigcap_{i=1}^n \dom f_i$ is nonempty.

If $f = f_1 = f_2 = \dots = f_n$, then the n-th power of $f$ is defined as:

$$
(f^n)(x) = (f(x))^n \Forall x \in \dom f.
$$
```

## Limits


```{prf:definition} Limit
:label: def-bra-real-function-limit

We say that $f$ approaches the limit $a$ as $x$ approaches $x_0$
and write:

$$
\lim_{x \to x_0} f(x) = a
$$

if $f$ is defined on some 
{prf:ref}`deleted neighborhood <def-bra-deleted-neighborhood>` 
of $x_0$ and for every
$\epsilon > 0$, there is $\delta > 0$ such that:

$$
|f(x) - a | < \epsilon  \text{ whenever } 0 < | x - x_0 | < \delta.
$$
```

* $f$ may or may not be defined at $x=x_0$. But, it must be defined 
  in the neighborhood around $x_0$.
* If $f$ is defined at $x=x_0$, then $f(x_0)$ doesn't need to be equal to $a$.


```{prf:example}
Let 

$$
f(x) = x \sin \frac{1}{x}, \quad x \neq 0.
$$
We have $\dom f = \RR \setminus \{ 0 \} = (-\infty, 0) \cup (0, \infty)$.
We can compute the limit of $f$ at $x=0$. We will show that:

$$
\lim_{x \to 0} f(x) = 0.
$$

Assume, $\epsilon > 0$ and let $\delta  = \epsilon$.

Then, for any $x$ satisfying $0 < |x - 0| < \delta$, we have

$$
|f(x) - 0| = \left | x \sin \frac{1}{x} \right | 
= |x| \left |\sin \frac{1}{x} \right |
\leq | x | < \delta = \epsilon.
$$

Thus, for every $\epsilon > 0$, there exists $\delta > 0$,
given by $\delta = \epsilon$, such that:

$$
0 < |x - 0| < \delta \implies |f(x) - 0|  < \epsilon.
$$

Thus,

$$
\lim_{x \to 0} f(x) = 0.
$$
```


```{prf:theorem} Limit uniqueness
:label: def-bra-rf-limit-uniqueness

If $\lim_{x \to x_0} f(x)$ exists, then it is unique.
```

```{prf:proof}
Assume that the limit exists and assume that:

$$
\lim_{x \to x_0} f(x) = a_1 \text{ and } \lim_{x \to x_0} f(x) = a_2 
$$
hold true. We will show that $a_1=a_2$ must be true.

Let $\epsilon > 0$. Since, the limit exists, hence there are 
positive numbers $\delta_1$ and $\delta_2$ such that:

$$
|f(x) - a_i | < \epsilon \text{ whenever } 0 < | x - x_0 | < \delta_i, \quad i=1,2.
$$

Choose $\delta = \min(\delta_1, \delta_2)$.

Then:

$$
|a_1 - a_2 | \leq |f(x) - a_1 | + | f(x) - a_2 | \leq 2 \epsilon 
\text{ whenever } 0 < | x - x_0 | < \delta.
$$

Thus, $| a_1 - a_2 | < 2 \epsilon$. Since this is valid for
every $\epsilon > 0$, hence $a_1 = a_2$ must be true
({prf:ref}`ref-rl-real-equality`).
```

```{prf:theorem} Arithmetic of limits
:label: def-bra-rf-limit-arithmetic

Let $\lim_{x \to x_0}f(x) = a$ and $\lim_{x \to x_0} g(x) = b$. 

Then, we have the following rules.

Addition of limits:

$$
\lim_{x \to x_0} (f + g)(x) = a + b.
$$

Subtraction of limits:

$$
\lim_{x \to x_0} (f - g)(x) = a - b.
$$

Multiplication of limits:

$$
\lim_{x \to x_0} (f g)(x) = a b.
$$

Division of limits. If $b \neq 0$, then:

$$
\lim_{x \to x_0} \left (\frac{f}{g} \right )(x) = \frac{a}{b}.
$$
```

```{prf:definition} One sided limits
:label: def-bra-rf-one-sided-limit

We that that $f$ approaches the *left hand limit* $p$ as $x$ approaches $a$
from the left and write:

$$
\lim_{x \to a^-} f(x) = p
$$

if $f$ is defined on some open interval $(a - b, a)$ (with $b > 0$) 
and for each $\epsilon >0$,
there is a $\delta > 0$ such that

$$
|f(x) - p | < \epsilon \text{ whenever } a - \delta < x < a.
$$

We that that $f$ approaches the *right hand limit* $p$ as $x$ approaches $a$
from the right and write:

$$
\lim_{x \to a^+} f(x) = p
$$

if $f$ is defined on some open interval $(a, a+b)$ (with $b > 0$) 
and for each $\epsilon >0$,
there is a $\delta > 0$ such that

$$
|f(x) - p | < \epsilon \text{ whenever } a < x < a + \delta.
$$

The left and right hand limits are called *one sided limits*.

We often write simplify the notation as:

$$
\lim_{x \to a^-} f(x) =  f(a^-) \text{ and } \lim_{x \to a^+} f(x) = f(a^+).
$$
```


```{prf:theorem}
A function $f$ has a limit at $x=a$ if and only if it has left and
right hand limits at $x=a$ and they are equal.

$$
\lim_{x \to a} f(x) = p \iff f(a^-) = f(a^+) = p.
$$
```

```{prf:definition} Limits at infinities
:label: def-bra-rf-limit-at-infinity

We say that $f$ approaches the limit $p$ as $x$ approaches $\infty$ 
and write:

$$
\lim_{x \to \infty} f(x) = p
$$

if $f$ is defined on an interval $(a, \infty)$ and 
for each $\epsilon > 0$, there exists a number $b$ such that

$$
|f(x) - p | < \epsilon \text{ whenever } x > b.
$$

We say that $f$ approaches the limit $p$ as $x$ approaches $-\infty$ 
and write:

$$
\lim_{x \to -\infty} f(x) = p
$$

if $f$ is defined on an interval $(-\infty, a)$ and 
for each $\epsilon > 0$, there exists a number $b$ such that

$$
|f(x) - p | < \epsilon \text{ whenever } x < b.
$$

We sometimes write:

$$
\lim_{x \to \infty} f(x) = f(\infty) \text{ and } \lim_{x \to -\infty} f(x) = f(-\infty).
$$
```


```{prf:definition} Infinite limits
:label: def-bra-rf-infinite-limit

We say that $f$ approaches $\infty$ as $x$ approaches $a$ from the
left, and write:

$$
\lim_{x \to a^-} f(x) = \infty
$$

if $f$ is defined on an interval $(a-b, a)$ (with $b > 0$), and,
for each real number $M$, there exists $\delta > 0$ such that

$$
f(x) > M \text{ whenever } a - \delta < x < a.
$$


We say that $f$ approaches $\infty$ as $x$ approaches $a$ from the
right, and write:

$$
\lim_{x \to a^+} f(x) = \infty
$$

if $f$ is defined on an interval $(a, a+b)$ (with $b > 0$), and,
for each real number $M$, there exists $\delta > 0$ such that

$$
f(x) > M \text{ whenever } a < x < a + \delta.
$$


We say that $f$ approaches $-\infty$ as $x$ approaches $a$ from the
left, and write:

$$
\lim_{x \to a^-} f(x) = -\infty
$$

if $f$ is defined on an interval $(a-b, a)$ (with $b > 0$), and,
for each real number $M$, there exists $\delta > 0$ such that

$$
f(x) < M \text{ whenever } a - \delta < x < a.
$$


We say that $f$ approaches $-\infty$ as $x$ approaches $a$ from the
right, and write:

$$
\lim_{x \to a^+} f(x) = -\infty
$$

if $f$ is defined on an interval $(a, a+b)$ (with $b > 0$), and,
for each real number $M$, there exists $\delta > 0$ such that

$$
f(x) < M \text{ whenever } a < x < a + \delta.
$$

If left hand and right hand limits are equal, we say that
the limit at $x=a$ given by $\lim_{x \to a} f(a)$ exists and
is equal to $f(a^+)$ or $f(a^-)$.
```

```{prf:remark}

{prf:ref}`def-bra-rf-limit-uniqueness` can be extended for 
the following too:

* If a left hand limit exists, it is unique.
* If a right hand limit exists, it is unique.
* If a limit at infinity exists, it is unique.
* If the limit value is infinite, it is unique.

{prf:ref}`def-bra-rf-limit-arithmetic` remains valid for
the following too:

* Left hand limits
* Right hand limits
* Limits at infinity

Addition, subtraction and multiplication rules remain 
valid if either or both limits are infinite, 
provided that the R.H.S. is not indeterminate.
E.g., if $\lim f = \infty$ and $\lim g = \infty$, then
$\lim (f - g) = \lim f - \lim g$ 
doesn't make sense as $\infty - \infty$ is
indeterminate.

Division rule for limits remains valid if $\lim f / \lim g$ 
is not indeterminate and $\lim g \neq 0$.
```

## Monotonicity

```{prf:definition} Monotonic function
:label: def-rf-monotonic-function

A function $f$ is *increasing* on an interval $I$ if

$$
f(x_1) \leq f(x_2) \text{ whenever } x_1 < x_2 \Forall x_1, x_2 \in I.
$$

A function $f$ is *decreasing* on an interval $I$ if

$$
f(x_1) \geq f(x_2) \text{ whenever } x_1 < x_2 \Forall x_1, x_2 \in I.
$$

If $f$ is *increasing* or *decreasing* on $I$, then we say that
$f$ is *monotonic* on $I$.


A function $f$ is *strictly increasing* on an interval $I$ if

$$
f(x_1) < f(x_2) \text{ whenever } x_1 < x_2 \Forall x_1, x_2 \in I.
$$

A function $f$ is *strictly decreasing* on an interval $I$ if

$$
f(x_1) <  f(x_2) \text{ whenever } x_1 < x_2 \Forall x_1, x_2 \in I.
$$

If $f$ is *strictly increasing* or 
*strictly decreasing* on $I$, then we say that
$f$ is *strictly monotonic* on $I$.
```

```{prf:theorem}
Let $f$ be monotonic of an interval $(a, b)$. Let

$$
\alpha = \underset{a < x < b}{\inf} f(x) \text{ and }
\beta = \underset{a < x < b}{\sup} f(x).
$$

1. If $f$ is increasing, then $f(a^+) = \alpha$ and $f(b^-) = \beta$.
1. If $f$ is decreasing, then $f(a^+) = \beta$ and $f(b^-) = \alpha$.
1. If $a < c < b$, then $f(c^+)$ and $f(c^-)$ exist and are finite.
   Moreover, if $f$ is increasing, then:

   $$
   f(c^-) \leq f(c) \leq f(c^+)
   $$

   and, if $f$ is decreasing, then:


   $$
   f(c^-) \geq f(c) \geq f(c^+).
   $$
```


## Continuity

If the limit of a function at a point matches its value at that
point, then the function is continuous at that point. 

```{prf:definition} Continuity
:label: def-bra-rf-continuity

1. We say that $f$ is *continuous* at $x=c$ if $f$ is defined
   on an interval $(a,b)$ containing $c$ (i.e. $a < c < b$)
   and $\lim_{x \to c} f(x) = f(c)$.
1. We say that $f$ is *continuous from the left* at $x=c$ if $f$ is defined
   on an interval $(a,c]$ and $f(c^-) = f(c)$.
1. We say that $f$ is *continuous from the right* at $x=c$ if $f$ is defined
   on an interval $[c,b)$ and $f(c^+) = f(c)$.
```

```{prf:theorem} Characterization of continuity

A function $f$ is continuous at $x=c$ if and only if $f$ is defined
on an interval $(a,b)$ containing $c$ and for each $\epsilon > 0$,
there exists $\delta > 0$ such that:

$$
|f(x) - f(c)| < \epsilon \text{ whenever } |x -c | < \delta.
$$ 

A function $f$ is continuous from the left at $x=c$ 
if and only if $f$ is defined
on an interval $(a,c]$ and for each $\epsilon > 0$,
there exists $\delta > 0$ such that:

$$
|f(x) - f(c)| < \epsilon \text{ whenever } c - \delta < x \leq c.
$$

A function $f$ is continuous from the right at $x=c$ 
if and only if $f$ is defined
on an interval $[c,b)$ and for each $\epsilon > 0$,
there exists $\delta > 0$ such that:

$$
|f(x) - f(c)| < \epsilon \text{ whenever } c \leq x < c  + \delta.
$$

$f$ is continuous at $x=c$ if and only if

$$
f(c^-) = f(c) = f(c^+).
$$
```

```{prf:definition} Continuity on an interval
:label: def-bra-rf-continuity-interval

A function $f$ is *continuous* on an open interval $(a,b)$ 
if it is continuous at every point in $(a, b)$.

* If $f(b^-) = f(b)$ holds too (i.e. $f$ is continuous from the left at $b$),
  then $f$ is continuous on $(a,b]$.
* If $f(a^+) = f(a)$ holds too (i.e. $f$ is continuous from the right at $a$),
  then $f$ is continuous on $[a,b)$.
* If both $f(a^+) = f(a)$ and $f(b^-) = f(b)$ hold true, then 
  $f$ is continuous on the closed interval $[a,b]$.

If $S$ is a subset of $\dom f$ consisting of finitely or infinitely
many disjoint intervals, then $f$ is continuous on $S$ if 
$S$ is continuous on every interval in $S$.
```

When we say that $f$ is continuous on some set $S \subseteq \dom f$, 
we mean that $S$ is a union of finitely or infinitely many 
disjoint intervals.

```{prf:definition} Piecewise continuity
:label: def-bra-rf-piecewise-continuity

A function $f$ is *piecewise-continuous* on $[a,b]$ if

1. $f(x^+)$ exists for all $a \leq x < b$;
1. $f(x^-)$ exists for all $a < x \leq b$;
1. $f(x^+) = f(x^-) = f(x)$ for all but finitely many points in $(a,b)$.

Jump discontinuities:

* If (3) fails to hold at some $x=c$ in $(a,b)$, 
  $f$ has a *jump discontinuity* at $x=c$.
* $f$ has a jump discontinuity at $a$ if $f(a^+) \neq f(a)$.
* $f$ has a jump discontinuity at $b$ if $f(b^-) \neq f(b)$.
```

In other words:

* Left hand limits exist everywhere (except at $x=b$).
* Right hand limits exist everywhere (except at $x=a$).
* There are only a finite number of points where these two limits don't match.
* $f$ is not continuous at those finite number of points.
* $f$ is continuous everywhere else in the open interval $(a,b)$.
* $f$ may not be continuous at the boundaries $x=a$ and $x=b$.
* At a jump discontinuity, $f$ may be continuous from the right
  or continuous from the left or neither.



```{prf:theorem}
If $f$ and $g$ are continuous on a set $S$, then so are
$f+g$, $f-g$, and $f g$. 
$\frac{f}{g}$ is continuous at each $x \in S$ such that 
$g(x) \neq 0$. 
```


```{prf:definition} Removable discontinuity

Let $f$ be discontinuous at some $x=a$. If 
$\lim_{x \to a} f(x)$ exists, then we say that
the discontinuity at $x=a$ is a *removable discontinuity*.
Moreover, the function:

$$
g(x) \triangleq \begin{cases}
f(x) & x \in \dom f \setminus \{ a \} \\
\lim_{x \to a} f(x) & x = a
\end{cases}
$$
is continuous at $x=a$.
```

Next, we look at continuity w.r.t. 
{prf:ref}`function composition <def-st-function-composition>`.


