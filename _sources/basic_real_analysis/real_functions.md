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
:label: res-bra-rf-monotonic-func-limits

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
This theorem is a restatement of continuity definition 
in the form of $\epsilon-\delta$ rules.

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


```{prf:proposition} Continuity on a closed interval $[a,b]$
:label: res-bra-rf-continuity-closed-interval-cover

Let $f$ be continuous on $[a,b]$. Then, for every $t \in [a,b]$,
and for every $\epsilon > 0$, 
there exists an open interval $I_t = (c,d)$ containing $t$ such that

$$
|f(x) - f(t)| < \epsilon \text{ whenever } x \in I_t \cap [a,b].
$$ 
```

```{prf:proof}

Assume $a < t < b$.  Then, there exists $\delta > 0$, such that:

$$
|f(x) - f(t)| < \epsilon \text{ whenever }  t - \delta < x < t + \delta.
$$ 

Choose $I_t = (t-\delta, t+\delta)$.

Now, assume $t=a$. $f$ must be continuous from the right at $t=a$. 
There exists $\delta > 0$ such that:

$$
|f(x) - f(t)| < \epsilon \text{ whenever } t \leq x < t  + \delta.
$$

Choose $I_t = (t - \delta, t+\delta)$. 
Then $I_t \cap (a,b) = [t, t+\delta)$.

Finally, assume $t=b$. $f$ must be continuous from the left at $t=b$. 
There exists $\delta > 0$ such that:

$$
|f(x) - f(t)| < \epsilon \text{ whenever } t - \delta < x \leq t.
$$

Choose $I_t = (t - \delta, t+\delta)$. 
Then $I_t \cap (a,b) = (t-\delta, t]$.  
```

The set $\OOO \triangleq \{I_t \Forall t \in [a,b] \}$ forms an
*open cover* of $[a,b]$.

```{prf:proposition}
:label: res-bra-rf-continuous-gap-neighborhood

Let $f$ be continuous at $x=a$ 

1. If $f(a) > \mu$, then $f(x) > \mu$ in some neighborhood of $a$.
1. If $f(a) < \mu$, then $f(x) < \mu$ in some neighborhood of $a$.
```

```{prf:proof}
(1) Let $\epsilon = f(a) - \mu$. $\epsilon > 0$ as $f(a) > \mu$.
There exists $\delta > 0$ such that

$$
|f(x) - f(a)| < \epsilon \text{ whenever } | x - a | < \delta. 
$$

Thus, in the neighborhood $x \in (a-\delta, a+\delta)$:

$$
f(a) - \epsilon < f(x) < f(a) + \epsilon \implies \mu < f(x) < 2 f(a) - \mu.
$$

(2) Let $\epsilon = \mu - f(a)$. $\epsilon > 0$ as $f(a) < \mu$.
There exists $\delta > 0$ such that

$$
|f(x) - f(a)| < \epsilon \text{ whenever } | x - a | < \delta. 
$$

Thus, in the neighborhood $x \in (a-\delta, a+\delta)$:

$$
f(a) - \epsilon < f(x) < f(a) + \epsilon \implies \mu - 2 f(a) < f(x) < \mu.
$$
```

```{prf:theorem} Continuity and arithmetic
If $f$ and $g$ are continuous on a set $S$, then so are
$f+g$, $f-g$, and $f g$. 
$\frac{f}{g}$ is continuous at each $x \in S$ such that 
$g(x) \neq 0$. 
```


## Discontinuities

A function $f$ is discontinuous at some $x=c$ in its domain $\dom f$ if 
either $\lim_{x\to c} f(x)$ doesn't exist or $\lim_{x\to c} f(x) \neq f(c)$.

```{prf:definition} Jump discontinuity
:label: def-bra-rf-jump-discontinuity

Let $f : \RR \to \RR$ be a real function and let $[a,b] \subseteq \dom f$.

1. $f$ has a *jump discontinuity* at a point $c \in (a,b)$ if both 
   the left hand limit $f(c^-)$ and the right hand limit $f(c^+)$ exist
   but $f(c^-) \neq f(c^+)$. In this case, $\lim_{x \to c} f(x)$ doesn't
   exist and $f$ is not continuous at $x=c$.
1. $f$ has a *jump discontinuity* at $x=a$ if the right hand limit 
   $f(a^+)$ exists but $f(a) \neq f(a^+)$. In this case, $f$ is not
   continuous from the right at $x=a$. 
1. $f$ has a *jump discontinuity* at $x=b$ if the left hand limit 
   $f(b^-)$ exists but $f(b) \neq f(b^-)$. In this case, $f$ is not
   continuous from the left at $x=b$. 
```

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

```{prf:definition} Essential discontinuity
:label: def-bra-rf-essential-discontinuity

Let $x$ be an interior point of $\dom f$. If either of 
the one sided limits $f(x^+)$, or $f(x^-)$ don't exist, then
$f$ has an *essential discontinuity* at $x$.

If $x \in \dom f$ is a boundary point, then only
a one sided limit is possible (left or right hand limit).
If such a limit doesn't exist, then $f$ has an *essential
discontinuity* at the boundary point $x$.
```

## Continuity with Function Composition

Next, we look at continuity w.r.t. 
{prf:ref}`function composition <def-st-function-composition>`.


```{prf:theorem}
Suppose $f$ is continuous at $x=a$; $f(a)$ is an
{prf:ref}`interior point <def-rl-interior-point>` 
of $\dom g$ and $g$ is continuous
at $f(a)$. Then $g \circ f$ is continuous at $x=a$. 
```

```{prf:proof}

We proceed as follows:

1. Let $\epsilon > 0$ be arbitrary.
1. Since $g$ is continuous at $f(a)$, there is $\delta_1 > 0$
   such that 

   $$
   |g(t) - g(f(a))| < \epsilon \text{ whenever } | t - f(a)| < \delta_1.
   $$
1. Since $f$ is continuous at $a$, hence, there exists $\delta > 0$
   such that

   $$
   |f(x) - f(a)| < \delta_1 \text{ whenever } | x - a | < \delta.
   $$
1. Together, they imply that

   $$
   |g(f(x)) - g(f(a)) | < \epsilon \text{ whenever } | x - a | < \delta.
   $$
1. Therefore, $g \circ f$ is continuous at $x=a$.
```

## Boundedness

```{prf:definition} Bounded function
:label: def-bra-rf-bounded-function

A real function $f$ is *bounded below* on a set 
$S \subseteq \dom f$ if 
there is a real number $m$ such that

$$
f(x) \geq m \Forall x \in S.
$$

Then, the set  

$$
V  = \{f(x) \ST x \in S \}
$$

has a infimum (due to {prf:ref}`res-rl-completeness-lower`),
and we write:

$$
\alpha = \underset{x \in S}{\inf} f(x).
$$ 

If there is a point $c \in S$ such that $\alpha = f(c)$,
we say that $\alpha$ is the *minimum* of $f$ on $S$
and $f$ *attains* the minimum at $x=c$. 


A real function $f$ is *bounded above* on a set 
$S \subseteq \dom f$ if 
there is a real number $M$ such that

$$
f(x) \leq M \Forall x \in S.
$$

Then, the set $V$
has a supremum (due to {prf:ref}`axm-rl-completeness-axiom`),
and we write:

$$
\beta = \underset{x \in S}{\sup} f(x).
$$ 

If there is a point $d \in S$ such that $\beta = f(d)$,
we say that $\beta$ is the *maximum* of $f$ on $S$
and $f$ *attains* the maximum at $x=d$. 

If $f$ is bounded above and below on a set $S$, we 
say that $f$ is *bounded* on $S$.
```

```{prf:theorem}
:label: res-bra-rf-continuous-interval-bounded

If $f$ is continuous on a finite closed interval $[a,b]$, then
$f$ is bounded on $[a,b]$.
```

```{prf:proof}
Let $f$ be continuous on $[a,b]$. Let $t \in [a,b]$.
Choose $\epsilon = 1$. Then,
due to {prf:ref}`res-bra-rf-continuity-closed-interval-cover`,
there exists an interval $I_t$ such that

$$
|f(x) - f(t) | < 1 \text{ whenever } x \in I_t \cap [a,b].
$$

The set $\OOO \triangleq \{I_t \Forall t \in [a,b] \}$ forms an
*open cover* of $[a,b]$.

Due to {prf:ref}`Heine-Borel theorem <res-rl-heine-borel>`,
$[a,b]$ has a finite subcover contained in $\OOO$.

Let $t_1 < t_2 < \dots < t_n$ index the finite open subcover.
We have:

$$
[a,b] \subset \bigcup_{i=1}^n \left ( I_{t_i} \cap [a,b] \right ).
$$

Then, for each $t_i$:

$$
|f(x) - f(t_i) | < 1 \text{ whenever } x \in I_{t_i} \cap [a,b].
$$

Therefore, 

$$
|f(x)| = |f(x) - f(t_i) + f(t_i)| \leq |f(x) - f(t_i)| + |f(t_i)|
\leq 1 + |f(t_i)| \text{ whenever } x \in I_{t_i} \cap [a,b].
$$

Thus, for every $x \in [a,b]$, there exists a $t_i \in [a,b]$ such that,

$$
|f(x) | \leq 1 + |f(t_i)|.
$$

Taking the maximum on the R.H.S. over all the inequalities, we get:

$$
|f(x) \leq 1 + \underset{1 \leq i \leq n}{\max} |f(t_i)|.
$$

Thus, $f$ is bounded with a bound:

$$
M = 1 + \underset{1 \leq i \leq n}{\max} |f(t_i)|.
$$
```

```{prf:corollary}
If $f$ is continuous on a finite closed interval $[a,b]$, then
$f$ has an infimum and a supremum.
```

```{prf:proof}
By {prf:ref}`res-bra-rf-continuous-interval-bounded`, $f$ 
is bounded. Let

$$
V  = \{f(x) \ST x \in [a,b] \}.
$$

Since $f$ is bounded, hence $V$ is bounded, hence
$V$ has an infimum as well as a supremum. 
```

```{prf:theorem}
Let $f$ be continuous on a finite closed interval $[a,b]$.
Let

$$
\alpha = \underset{a \leq x \leq b}{\inf}f(x) \text{ and }
\beta = \underset{a \leq x \leq b}{\sup}f(x).
$$

Then, $\alpha$ and $\beta$ are respectively, the 
minimum and maximum values of $f$ on $[a,b]$ and $f$
attains these values at some points in $[a,b]$.

I.e., there exists $x_1, x_2 \in [a,b]$ such that:

$$
f(x_1) = \alpha \text{ and } f(x_2) = \beta.
$$
```

```{prf:proof}
Assume that $\alpha$ is the infimum of $f$ over $[a,b]$
and there is no $x_1 \in [a,b]$ such that $f(x_1) = \alpha$.
Then $f(x) > \alpha$ for all $x\in [a,b]$.

Let $t \in [a,b]$. Then, $f(t)> \alpha$. 
Thus, 

$$
f(t) > \frac{f(t) + \alpha}{2} > \alpha.
$$

By {prf:ref}`res-bra-rf-continuity-closed-interval-cover` 
and {prf:ref}`res-bra-rf-continuous-gap-neighborhood`, 
there is a open interval $I_t$ at $t$ such that

$$
f(x) > \frac{f(t) + \alpha}{2}  \text{ whenever } x \in I_t \cap [a,b]. 
$$

The set $\OOO = \{ I_t \ST a \leq t \leq b \}$ is an open cover
of $[a,b]$.


Due to {prf:ref}`Heine-Borel theorem <res-rl-heine-borel>`,
$[a,b]$ has a finite subcover contained in $\OOO$.
Thus, there are finitely many points $t_1, t_2, \dots, t_n$
such that:

$$
[a,b] \subset \bigcup_{i=1}^n \left ( I_{t_i} \cap [a,b] \right ).
$$

Define:

$$
\alpha_1 = \underset{1 \leq i \leq n}{\min}\frac{f(t_i) + \alpha}{2}.
$$
Due to the finite cover; for every $x \in [a,b]$, there exists $t_i$ 
such that $x \in I_{t_i} \cap [a,b]$ and thus, 
$f(x) > \frac{f(t_i) + \alpha}{2} \geq \alpha_1$. 
Thus,

$$
f(x) > \alpha_1 \Forall x \in [a,b].
$$
But $\alpha_1 > \alpha$. Thus, $\alpha$ cannot be the infimum of 
$f$ over $[a,b]$. We arrive at the contradiction.

Thus, there exists some $x=x_1$ such that $f(x_1) = \alpha$.

A similar argument shows that $f$ attains $\beta$ at some $x_2 \in [a,b]$.
```


```{prf:theorem} Intermediate value theorem
:label: res-bra-rf-intermediate-value

Let $f$ be continuous on a finite closed interval $[a,b]$. 
Assume that $f(a) \neq f(b)$.
Let $\mu$ be in between $f(a)$ and $f(b)$.
Then $f$ attains the value of $\mu$ at some $x=c \in (a,b)$. 

In other words, there exists $c \in (a,b)$ such that $f(c)=\mu$. 
```

```{prf:proof}
Let us assume that $f(a) < \mu < f(b)$.

Define the set:

$$
A = \{x \in [a,b] \ST f(x) \leq \mu \}.
$$

1. The set is bounded since $a \leq x \leq b$.
1. The set is nonempty since $f(a) < \mu$. 
   And since $f$ is continuous from the right at $a$, 
   hence there exists an interval $[a, a+\delta)$ such that $f(x) < \mu$ 
   in this interval.
1. Thus, $A$ has an infimum(obviously $a$) and a supremum. 
1. Let $c = \sup A$. 
1. We will claim that $f(c) = \mu$.

If $f(c) > \mu$, then:

1. $c > a$.
1. $f$ is continuous at $x=c$. 
1. Thus, there exists an $\epsilon > 0$ such that 
   $f(x) > \mu$ whenever $c - \epsilon < x \leq c$.
1. Therefore, the interval $(c - \epsilon, c]$ is not included in $A$.
1. Therefore, $c-\epsilon$ is an upper bound for $A$.
1. This contradicts the assumption that $c = \sup A$.


If $f(c) < \mu$, then:

1. $c < b$. 
1. $f$ is continuous at $x=c$. 
1. Thus, there exists an $\epsilon > 0$ such that 
   $f(x) < \mu$ whenever $c \leq x < c + \epsilon$.
1. Therefore, the interval $[c, c + \epsilon)$ is included in $A$.
1. Therefore, $c$ is not an upper bound for $A$.
1. This also contradicts the assumption that $c = \sup A$.

Therefore $f(c) = \mu$ must be true.

A similar argument can be pursued when $f(b) < \mu < f(a)$.
```

Note that the proof picks up just one possible value of $x$ 
such that $f(x) = \mu$. It is quite possible that $f$ attains
$\mu$ more than one times in the interval $[a,b]$. The proof
doesn't claim to find all such values of $x$.

In this sense, this theorem is a weak result as it claims
the existence of just one point at which $f(x) = \mu$. 
It doesn't claim to characterize the set of points at which $f(x) = \mu$.

## Uniform Continuity

```{prf:definition} Continuity over a set
:label: def-bra-rf-continuity-over-set

Let $A \subseteq \dom f$. We say that $f$ is *continuous* 
over the set $A$ if for each $\epsilon > 0$ and each
$x_0 \in A$, there exists $\delta > 0$ 
(depending on $x_0$ and $\epsilon$) such that

$$
|f(x) - f(x_0)| < \epsilon \text{ whenever } |x - x_0| < \delta 
\text{ and } x \in \dom f.
$$
```

The clause $x \in \dom f$ in the definition is important.

1. If $x_0$ is an interior point of $\dom f$, we can pick
   an interval $(x_0 - \delta, x_0 + \delta)$.
1. If $x_0$ is a non-interior point of $\dom f$, we can pick up
   a half-open interval $(x_0 - \delta, x_0]$ or $[x_0, x_0 + \delta)$
   whichever is applicable.
1. If $x_0$ is an isolated point, we pick the degenerate interval
   $[x_0, x_0]$ with suitable choice of $\delta$.
1. Thus, on the non-interior points, $f$ is either continuous from
   the left or right while on the interior points, $f$ is continuous.

The key issue here is that the size of the interval 
(decided by $\delta$) may depend on both $\epsilon$ 
as well as the point $x_0$. This is not always desirable. 
Uniform continuity addresses this concern.

```{prf:definition} Uniform continuity
:label: def-bra-rf-uniform-continuity

Let $f: \RR \to \RR$ be a real function. 
Let $A \subseteq \dom f$. 
We say that $f$ is *uniformly continuous*
over the set $A$ if for every $\epsilon > 0$, 
there exists $\delta > 0$ (depending on $\epsilon$) such that

$$
|f(x) - f(y)| < \epsilon \text{ whenever } |x - y| < \delta 
\text{ and } x, y \in A.
$$
```

Few observations on this definition:

1. $\delta$ depends on $\epsilon$. 
1. $\delta$ is independent of the choice of $x$ and $y$.
1. $\delta$ might depend on the set $A$. E.g., if 
   $A$ is a bounded set, it may depend on its size.
1. The definition is restricted to points in $A$.
   It doesn't consider points in $\dom f \setminus A$.


```{prf:remark}
If $f$ is not uniformly continuous on a set $A$, then
there is an $\epsilon_0 > 0$ such that for any $\delta > 0$,
there are points $x,y$ in $A$ such that:

$$
|x - y | < \delta \text{ but } |f(x) - f(y)| \geq \epsilon_0.
$$
```

While a continuous function may not be uniformly continuous
in general, it is so on a compact subset.

```{prf:theorem}
If $f$ is continuous on a closed and bounded (compact)
interval $[a,b]$, then $f$ is uniformly continuous on $[a,b]$.
```

```{prf:proof}
Let $\epsilon > 0$ be arbitrary. Since $f$ is continuous 
on $[a,b]$, for every $t \in [a,b]$, there exists $\delta_t > 0$
such that

$$
| f(x) - f(t) | < \frac{\epsilon}{2} \text{ whenever } | x - t | < 2 \delta_t
\text{ and } x \in [a,b].
$$

Choose an open interval $I_t = (t - \delta_t, t + \delta_t)$ for 
every $t \in [a,b]$. 

The collection $\OOO = \{ I_t \ST t \in [a,b] \}$ is an open cover
for $[a,b]$. Since $[a,b]$ is closed and bounded (compact), hence
due to {prf:ref}`Heine-Borel theorem <res-rl-heine-borel>`, 
there are finitely many points $t_1, t_2, \dots, t_n$ in $[a,b]$
such that $\PPP = \{ I_{t_1}, I_{t_2}, \dots, I_{t_n} \}$ form a finite 
open cover of $[a,b]$.

Define:

$$
\delta = \min \{\delta_{t_1}, \delta_{t_2}, \dots, \delta_{t_n}\}.
$$

Assume that $|x - y| < \delta$ and $x,y \in [a,b]$. 
Assume that $x \in I_{t_r}$ for some $r$. 
This is true since $\PPP$ is a cover for $[a,b]$.

Now, from triangle inequality:

$$
| f(x) - f(y) | = | f(x) - f(t_r) + f(t_r)  - f(y)| \leq | f(x) - f(t_r) | + | f(t_r) - f(y)|.
$$ 

Since $x \in I_{t_r}$, hence $|x - t_r | < \delta_{t_r}$, hence:

$$
| f(x) - f(t_r) | < \frac{\epsilon}{2}.
$$

On the other hand:

$$
|y - t_r |  \leq |y - x | + | x - t_r | < \delta + \delta_{t_r} \leq 2 \delta_{t_r}.
$$

Thus,

$$
| f(t_r) - f(y)| < \frac{\epsilon}{2}.
$$

Together, we have:

$$
| f(x) - f(y) | < \epsilon.
$$

We have shown that for any $\epsilon > 0$, a $\delta > 0$ can be chosen 
such that, $|x - y | < \delta$ with $x,y \in [a,b]$ implies
$|f(x) - f(y)| < \epsilon$.
Thus, $f$ is uniformly continuous over $[a,b]$.
```

```{prf:corollary}
If $f$ is continuous on a set $A$, then $f$ is uniformly continuous
on any finite closed interval contained in $A$.
```

## Continuity and Monotonic Functions

```{prf:proposition}
If $f$ is monotonic on an interval $I$, then $f$ is either 
continuous or has a jump discontinuity at each $x \in I$. 
```

```{prf:proof}
Let $I$ be an open interval $(a,b)$. 
Then, due to {prf:ref}`res-bra-rf-monotonic-func-limits`, 
both left hand and right hand limits exist at each point in $(a,b)$.

Consider some $c \in (a,b)$.

1. If $f(c^-) = f(c^+)$, then by monotonicity, $f(c^-) = f(c) = f(c^+)$,
   thus $f$ is continuous at $c$.
1. If $f(c^-) \neq f(c^+)$, then we have a jump discontinuity.

Next, the boundary points. Consider $x=a$. 

1. The right hand limit $f(a^+)$ exists 
   due to {prf:ref}`monotonicity <res-bra-rf-monotonic-func-limits>`. 
1. If $f(a) = f(a^+)$, then $f$ is continuous from the right at $x=a$.
1. Otherwise, we have a jump discontinuity at $x=a$.

Similarly, for $x=b$:

1. The left hand limit $f(b^-)$ exists 
   due to {prf:ref}`monotonicity <res-bra-rf-monotonic-func-limits>`. 
1. If $f(b) = f(b^-)$, then $f$ is continuous from the left at $x=b$.
1. Otherwise, we have a jump discontinuity at $x=b$.


```

```{prf:theorem}
:label: res-bra-rf-monotonic-continuous-closed-range

If $f$ is monotonic on $[a,b]$, then $f$ is continuous
on $[a,b]$ if and only if its range 
$R_f = f([a,b]) = \{f(x) \ST a \leq x \leq b \}$ is
a closed interval with endpoints $f(a)$ and $f(b)$.

In other words, $f$ is continuous on $[a,b]$ if and only if:

$$
f([a,b]) = [f(a), f(b)] \text{ if } f(a) \leq f(b) \text { else } [f(b), f(a)].
$$
```

```{prf:proof}
If $f$ is constant over $[a,b]$, there is nothing to prove.
Hence, we shall restrict our attention to the case where $f$ is non-constant.
Then $f(a) \neq f(b)$ since $f$ is monotonic.
Without loss of generality, assume that $f(a) < f(b)$ ($f$ is increasing). 
If $f(a) > f(b)$, we can replace $f$ by $-f$ and proceed.

Consider the set 

$$
S_f = \{ f((a,b)) \} = \{f(x) \ST a < x < b \}.
$$
Due to {prf:ref}`res-bra-rf-monotonic-func-limits`:

$$
S_f \subseteq [f(a^+), f(b^-)].
$$

Thus, 

$$
R_f = \{ f(a) \} \cup S_f \cup \{ f(b) \} \subseteq \{ f(a) \} \cup [f(a^+), f(b^-)] \cup \{ f(b) \}. 
$$

If $f$ is continuous on $[a,b]$, then $f(a) = f(a^+)$
and $f(b) = f(b^-)$. Thus, we have:
$R_f \subseteq [f(a), f(b)]$.

Further, due to {prf:ref}`intermediate value theorem <res-bra-rf-intermediate-value>`,
for every $f(a) < \mu < f(b)$, there exists $x \in (a,b)$, such that
$\mu = f(x)$. Thus, 
$R_f = [f(a), f(b)]$.


We now assume that $R_f = [f(a), f(b)]$ and show that $f$ must be continuous.

1. Since $f$ is increasing, hence $f(a) \leq f(a^+)$ and $f(b^+) \leq f(b)$. 
1. We also have: $[f(a), f(b)] \subseteq \{ f(a) \} \cup [f(a^+), f(b^-)] \cup \{ f(b)$.
1. If $f(a) < f(a^+)$ were true, then the subset relationship above will be invalid. 
   Similar case with $f(b^-) < f(b)$.
1. Thus, we both $f(a) = f(a+)$ and $f(b) = f(b^-)$ must be true.
1. $f$ is continuous from the right at $a$ and from the left at $b$.
1. Also, since $f$ is increasing, hence for any $c \in (a,b)$, we have
   $f(c^-) \leq f(c) \leq f(c^+)$.
1. If $f(c^-) < f(c)$, then $(f(c^-), f(c))$ cannot be part of $R_f$.
   Thus, $f(c^-) = f(c)$ 
```

For strictly monotonic functions which are continuous on an
interval $[a,b]$, it is possible to find an inverse function
on the same interval.

```{prf:theorem}
Let $f$ be a strictly increasing and continuous function on 
an interval $[a,b]$.
Let $f(a) = c$ and $f(b) = d$. Then, there is a unique 
function $g$ defined on $[c,d]$ such that:

$$
g (f(x)) = x \Forall a \leq x \leq b
$$ 
and 

$$
f(g(y)) = y \Forall c \leq y \leq d.
$$

Moreover, $g$ is continuous and strictly increasing on $[c,d]$.
```

```{prf:proof}

We first show that such a function $g$ can be defined:

1. Since $f$ is (strictly) monotone, hence 
   due to {prf:ref}`res-bra-rf-monotonic-continuous-closed-range`,
   $f([a,b]) = [c,d]$. 
1. In other words, $f$ restricted to $[a,b]$ as $f : [a,b] \to [c,d]$ 
   is {prf:ref}`total <def-st-total-function>`
   and {prf:ref}`surjective <def-st-surjective-function>`.
1. Thus, for each $y \in [c,d]$, there exists $x \in [a,b]$ 
   such that $y = f(x)$.
1. Since $f$ is strictly increasing, hence $f(x_1) \neq f(x_2)$
   for any $x_1, x_2 \in [a,b]$.
1. Hence, $f : [a,b] \to [c,d]$ is 
   {prf:ref}`injective <def-st-injective-function>`.
1. Thus, $f : [a,b] \to [c,d]$ is 
   {prf:ref}`bijective <def-st-bijective-function>`.
1. Thus, we can introduce an 
   {prf:ref}`inverse function <def-st-inverse-total-function>`
   $g : [c,d] \to [a,b]$ with the rule $g(y) = x$ whenever $f(x) = y$.  

Next, we show that $g$ is strictly increasing.

1. Let $y_1, y_2 \in [c,d]$ such that $y_1 < y_2$. 
1. Let $x_1, x_2 \in [a,b]$ such that $y_1 = f(x_1)$ and $y_2 = f(x_2)$.
1. Thus, $x_1 = g(y_1)$ and $x_2 = g(y_2)$.
1. Since $f$ is strictly increasing, hence $f(x_1) < f(x_2)$ implies $x_1 < x_2$.
1. Thus, $y_1 < y_2$ implies $g(y_1) = x_1 < g(y_2) = x_2$. 
1. Thus, $g$ is strictly increasing.


Finally, notice that $g$ is monotonic and
the range $g([c,d]) = [a,b]$ is a closed interval with the
end points $a = g(c)$ and $b=g(d)$.
Thus, due to {prf:ref}`res-bra-rf-monotonic-continuous-closed-range`,
$g$ is continuous.
```