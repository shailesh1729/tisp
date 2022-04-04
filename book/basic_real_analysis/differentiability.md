(sec:bra:differentiable-functions)=
# Differentiable Functions

We continue our discussion on real functions and
focus on a special class of functions which are *differentiable*.

```{prf:definition} Differentiable function
:label: def-bra-rf-differentiable-function

A real function $f: \RR \to \RR$ is *differentiable* 
at an interior point $x=a$ of its domain $\dom f$ 
if the difference quotient

$$
\frac{f(x) - f(a)}{x - a}, \quad x \neq a
$$
approaches a {prf:ref}`limit <def-bra-real-function-limit>`
as $x$ approaches $a$. 

If $f$ is differentiable at $x=a$, the limit is called
the *derivative* of $f$ at $x=a$ and is denoted by 
$f'(a)$; thus,

$$
f'(a) = \lim_{x \to a}\frac{f(x) - f(a)}{x - a}.
$$
An alternative way is to write $x$ as $x = a + h$ and 
define $f'(a)$ as:

$$
f'(a) = \lim_{h \to 0}\frac{f(a + h) - f(a)}{h}.
$$
```

Notes 

* The difference quotient is not 
  defined at $x=a$. This is okay as 
  computing the limit $\lim_{x \to a} g(x)$ 
  doesn't require $g$ to be defined at $x=a$.
* The derivative is not defined for the non-interior points
  of $\dom f$. Only one sided limits may be computed
  at the non-interior points on the difference quotient.
* We can treat $f'$ as a function from $\RR$ to $\RR$ 
  where $f'$ is defined only on points at which 
  $f$ is differentiable.
* The type signature for $f'$ is $f' : \RR \to \RR$.
* The domain of $f'$ denoted by $\dom f'$ is the set
  of points at which $f$ is differentiable.


```{prf:remark} Domain of the derivative function
:label: rem-bra-rf-derivative-domain

The domain of the derivative of a function $f$;
i.e., the set of points at which the derivative exists
(or is defined) is a subset of the interior of the domain
of the function $f$ itself.

$$
\dom f' \subseteq \interior \dom f.
$$
```


```{prf:definition} Differentiable function
:label: def-bra-rf-differentiable-func

Let $f$ be defined on an open set $A$. 
We say that $f$ 
is *differentiable on $A$* if $f$ is differentiable 
at every point in $A$.
```

If $f$ is differentiable on (open) $A$, 
then $f'$ is defined on $A$. 
In other words: $\dom f' = A$.


```{prf:definition} Continuously differentiable function
:label: def-bra-rf-continuously-differentiable-func

We say that $f$ is *continuously differentiable* on an open set $A$
if $f$ is differentiable on $A$ and $f'$ is continuous on $A$.
```


```{prf:definition} Second and $n$-th derivatives
:label: def-bra-rf-nth-derivative

If $f$ is differentiable on a neighborhood of $x=a$ 
and $f'$ is differentiable at $x=a$, we denote the
derivative of $f'$ at $x=a$ by $f''(a)$ and 
call it the *second derivative* of $f$ at $x=a$.
Another notation for the second derivative is
$f^{(2)}(a)$.

Inductively, if $f^{(n-1)}$ is defined on a neighborhood
of $x=a$ and $f^{(n-1)}$ is differentiable at $x=a$, then
the n-th derivative of $f$ at $x=a$, denoted by
$f^{(n)}(a)$, is the derivative of $f^{(n-1)}$ at $x=a$.

The *zeroth derivative* of $f$ is defined to be $f$ itself.

$$
f^{(0)} = f.
$$ 
```

Another common notation is:

$$
\frac{d f}{d x} = f'
\text{ and } \frac{d^n f}{d x^n} = f^{(n)}.
$$


```{prf:definition} Tangent line
:label: def-bra-df-tangent

If $f$ is differentiable at $x=a$, then the tangent to $f$ 
at $x=a$ can be given by:

$$
T(x) = f(a) + f'(a)(x -a).
$$
```

It is useful to remove the contribution of the tangent in $f$
and study the remaining part of $f$.

````{prf:lemma} Removal of tangent line from function
:label: res-bra-df-f-t-e

If $f$ is differentiable at $x=a$, then we can write
$f$ as:

```{math}
:label: eq-bra-df-f-minus-tangent
f(x) = f(a) + [f'(a) + E(x)](x -a)
```
where $E$ is defined in the neighborhood of $x=a$ and

$$
\lim_{x \to a} E(x) = E(a) = 0.
$$

In other words, $E$ is continuous at $x=a$.
````

```{prf:proof}
We define $E$ as:

$$
E(x) = \begin{cases}
\frac{f(x) - f(a)}{x - a} - f'(a), & x \in \dom f \text{ and } x \neq a\\
0, & x = a
\end{cases}.
$$
This $E$ meets the requirements of {eq}`eq-bra-df-f-minus-tangent`.
Note that $E$ is continuous at $x=a$ as $\lim_{x \to a} E(x) = E(a)= 0$.

We note that:

$$
f(x) - T(x) = E(x) (x - a).
$$


Alternatively

$$
f(x) = T(x) + E(x) (x - a).
$$
```

```{prf:remark} Difference quotient and derivative
:label: rem-bra-df-tangent-form-2

At $x \neq a$, {eq}`eq-bra-df-f-minus-tangent` can also be written as:

$$
\frac{f(x) - f(a)}{x -a}  = f'(a) + E(x).
$$

In other words, the difference quotient $\frac{f(x) - f(a)}{x -a}$ 
is the sum of the
derivative $f'(a)$ and $E(x)$.
```

```{prf:theorem} Differentiability implies continuity
:label: res-bra-rf-diff-implies-cont

If $f$ is differentiable at $x=a$, then $f$ is continuous at $x=a$.
```

```{prf:proof}
Using {prf:ref}`def-bra-df-tangent` and {prf:ref}`res-bra-df-f-t-e`, we have:

$$
f(x) = T(x) + E(x) (x - a).
$$

It is easy to see that $E(x)$ and $T(x)$ are both continuous at $x=a$. 
Thus, $f$ is continuous at $x=a$.
```

Notes:

1. If $f$ is not continuous at $x=a$ then $f$ is not differentiable at $x=a$.
1. Continuity is a necessary condition but not sufficient condition for
   differentiability.

```{prf:remark} Derivative sign and monotonicity in the neighborhood
:label: res-bra-rf-derivative-sign-monotonicity

If $f$ is differentiable at $x=a$, and $f'(a) \neq 0$, 
then there is $\delta > 0$ such that if $f'(a) > 0$, then

$$
\sgn (f(x) - f(a)) = \sgn (x - a) \Forall |x - a| < \delta
$$
and if $f'(a) < 0$, then

$$
\sgn (f(x) - f(a)) = \sgn (a - x) \Forall |x - a| < \delta.
$$
```

```{prf:proof}

We have, from {prf:ref}`res-bra-df-f-t-e`, for $x \neq a$:

$$
\frac{f(x) - f(a)}{x -a}  = f'(a) + E(x).
$$

Assume $f'(a) \neq 0$. Then $|f'(a)| > 0$.
Since $E$ is continuous at $a$,
with $\epsilon =  |f'(a)| > 0$, there exists $\delta > 0$ such that

$$
|E(x) - E(a)| = |E(x)| < \epsilon = |f'(a)| \text{ whenever } |x - a| < \delta.
$$

Thus, 

$$
\sgn(f'(a) + E(x)) = \sgn (f'(a)) \Forall |x - a| < \delta.
$$

Thus,

$$
\sgn \left ( \frac{f(x) - f(a)}{x -a} \right ) = \sgn (f'(a)) \Forall |x - a| < \delta.
$$

Now, if $f'(a) > 0$, then

$$
\sgn (f(x) - f(a)) = \sgn (x - a) \Forall |x - a| < \delta.
$$

If $f'(a) < 0$, then

$$
\sgn (f(x) - f(a)) = - \sgn (x - a) = \sgn (a - x) \Forall |x - a| < \delta.
$$
```

## Arithmetic

```{prf:theorem} Differentiation and arithmetic 
:label: res-bra-rf-differentiation-arithmetic

If $f$ and $g$ are differentiable at $x=a$, then so are
$f+g$, $f-g$, $fg$.
$\frac{f}{g}$ is differentiable at $x=a$ if $g'(a) \neq 0$.
The derivatives are:

1. $(f + g)'(a) = f'(a) + g'(a)$.
1. $(f - g)'(a) = f'(a) - g'(a)$.
1. $(f g)'(a) = f'(a) g(a) + f(a) g'(a)$.
1. $\left(\frac{f}{g} \right)'(a) = \frac{f'(a) g(a) - f(a) g'(a)}{[g'(a)]^2}$
   provided $g'(a) \neq 0$.
```


## The Chain Rule

```{prf:theorem} The chain rule
:label: res-bra-rf-diff-chain-rule

Let $f$ be differentiable at $x=a$. Assume that $g$ is differentiable 
at $f(a)$. Then the composite function given by $h = g \circ f$ is
differentiable at $f(a)$ with

$$
h'(a) = g'(f(a))f'(a).
$$
```

```{prf:proof}
Let $b = f(a)$. Since $g$ is differentiable at $b$, we can
write $g$ as ({prf:ref}`res-bra-df-f-t-e`):

$$
g(t) = g(b) + [g'(b) + E(t)] (t - b)
$$ 
where $E$ is continuous in the neighborhood of $t=b$ 
and $\lim_{t \to b} E(t) = E(b) = 0$.
Thus,

$$
g(t) - g(b) = [g'(b) + E(t)] (t - b).
$$
Putting $t=f(x)$, we get:

$$
g(f(x)) - g(f(a)) = [g'(f(a)) + E(f(x))][f(x) - f(a)].
$$
Since $h(x) = g(f(x))$, we get:

$$
h(x) - h(a) = [g'(f(a)) + E(f(x))][f(x) - f(a)].
$$

Dividing both sides by $(x-a)$, we get:

$$
\frac{h(x) - h(a)}{x - a} = [g'(f(a)) + E(f(x))] \frac{f(x) - f(a)}{x-a}.
$$

Since $f$ is continuous at $x=a$, 
$E$ is continuous at $t=b=f(a)$,
and $b$ is an interior point of $\dom E$, 
hence $E\circ f$ is continuous at $x=a$ 
due to {prf:ref}`res-bra-rf-composition-continuity`. 
Thus, 

$$
\lim_{x \to a} E(f(x)) = E(f(a)) = E(b) = 0.
$$

Therefore,

$$
\begin{aligned}
h'(a) &= \lim_{x \to a} \frac{h(x) - h(a)}{x - a} \\
&= \lim_{x \to a} [g'(f(a)) + E(f(x))] 
\lim_{x \to a} \frac{f(x) - f(a)}{x-a}\\
&= [g'(f(a)) + \lim_{x \to a}E(f(x)) ] f'(a) =  g'(f(a)) f'(a).
\end{aligned}
$$

```

```{prf:example}
:label: ex-bra-rf-chain-rule-1
Let 

$$
f(x) = \frac{1}{x} \text{ and } g(x) = \sin x.
$$

Then, the composition $h = g \circ f$ is given by

$$
h(x) = (g \circ f)(x) = g (f (x)) =  \sin \frac{1}{x}.
$$

We have:

$$
f'(x) = -\frac{1}{x^2} \text{ and } g'(x) = \cos x.
$$

Thus, 

$$
h'(x) = g'(f(x))f'(x) = \left (\cos \frac{1}{x} \right )
\left (-\frac{1}{x^2} \right ).
$$
```

## One Sided Derivatives

```{prf:definition} One sided derivatives
:label: def-bra-df-one-sided-derivative

One sided limits of the difference quotient

$$
\frac{f(x) - f(a)}{x - a}, \quad x \neq a
$$
are called *one-sided derivatives* if they exist.

If $f$ is defined over $[a,b)$, then the
*right hand derivative* is defined as:

$$
f'_+(a) \triangleq \lim_{x \to a^+} \frac{f(x) - f(a)}{x - a}
$$
if the limit exists.


If $f$ is defined over $(c,a]$, then the
*left hand derivative* is defined as:

$$
f'_-(a) \triangleq \lim_{x \to a^-} \frac{f(x) - f(a)}{x - a}
$$
if the limit exists.
```

```{prf:remark} Differentiability and one-sided derivatives
:label: rem-bra-rf-diff-one-sided-derivatives

A function $f$ is differentiable at $x=a$ if and only if
its left and right hand derivatives exist and are equal.
In that case:

$$
f'_-(a) = f'(a) = f'_+(a).
$$
```

This is a direct implication of {prf:ref}`res-bra-rf-equal-one-sided-limits`.

```{prf:remark}
:label: rem-bra-rf-one-sided-derivative-limit-diff

One sided derivative is not the same thing as
one sided limit of a derivative.

1. $f'_+(a)$ need not be equal to $f'(a^+)$.
1. $f'_-(a)$ need not be equal to $f'(a^-)$.
```

## Closed Intervals

```{prf:definition} Differentiability on a closed interval
:label: def-bra-df-differentiability-closed-interval

We say that $f$ is *differentiable on the closed interval* $[a,b]$
if $f$ is differentiable on the open interval $(a,b)$ and the
one sided derivatives $f'_+(a)$ and $f'_-(b)$ both exist.

We assign $f'(a) = f'_+(a)$ and $f'(b) = f'_-(b)$ to complete
the definition of $f'$ over $[a,b]$.
```

```{note}
While it is possible to use the notion of one sided derivatives
to define $f'$ on a closed interval, this notion doesn't generalize
to multivariable calculus. The definition of derivative 
on an open interval (or an open subset of $\dom f$) can be easily
extended to multivariable calculus.
```


```{prf:definition} Continuous differentiability on a closed interval
:label: def-bra-df-continuous-differentiability-closed-interval

We say that $f$ is *continuously differentiable on the closed interval* $[a,b]$
if 

1. $f$ is differentiable on the closed interval $[a,b]$
1. $f'$ is continuous over the open interval $(a,b)$
1. $f'_+(a) = f'(a^+)$.
1. $f'_-(b) = f'(b^-)$.
```

## Extreme Values


```{prf:definition} Local extreme value
:label: res-bra-rf-local-extreme-value

We say that $f(a)$ is a *local extreme value* of $f$ if there exists
$\delta > 0$ such that $f(x) - f(a)$ doesn't change sign on

$$
(a - \delta, a + \delta) \cap \dom f.
$$

More specifically,

1. $f(a)$ is a *local maximum value* of $f$ if for some $\delta > 0$:

   $$
   f(x) \geq f(a) \Forall x \in (a - \delta, a + \delta) \cap \dom f.
   $$ 
1. $f(a)$ is a *local minimum value* of $f$ if for some $\delta > 0$:

   $$
   f(x) \geq f(a) \Forall x \in (a - \delta, a + \delta) \cap \dom f.
   $$ 

The point $x=a$ is called a *local extreme point* of $f$ or more 
specifically, a *local maximum* or a *local minimum* point of $f$.
```

```{prf:theorem}
:label: res-bra-df-extremum-zero-derivative

If $f$ is differentiable at a local extreme point $a \in \dom f$,
then $f'(a) = 0$. 

In other words, if the derivative exists at a local extreme point,
it vanishes there.
```


```{prf:proof}
We show that if $f'(a) \neq 0$ then $a$ is not a local extreme point.
Thus, if $a$ is a local extreme point then $f'(a)$ must be 0.

Assume $f'(a) \neq 0$.

From {prf:ref}`res-bra-df-f-t-e`, we have (at $x \neq a$):

$$
\frac{f(x) - f(a)}{x -a}  = f'(a) + E(x)
$$
where $\lim_{x \to a} E(x) = 0$ and $E$ is continuous at $x=a$.

Since $f'(a) \neq 0$, hence $|f'(a)| > 0$, hence 
there exists $\delta > 0$ such that

$$
|E(x) | < |f'(a)|  \text{ whenever } |x - a | < \delta.
$$

Thus, in the interval $|x - a | < \delta$, the term $f'(a) + E(x)$ has the
same sign as $f'(a)$.

Hence the term $\frac{f(x) - f(a)}{x -a}$ must not change sign 
in $|x - a | < \delta$. 

But the term $(x -a)$ changes sign in $|x - a | < \delta$. 
Hence, $f(x) - f(a)$ must also change sign.

Moreover, $(x -a)$ changes sign in every neighborhood $|x - a | < \delta_1$ 
with $\delta_1 > 0$. 
Hence $f(x) - f(a)$ must also change sign in every neighborhood.

Hence there is no neighborhood of $a$ in which $f(x) - f(a)$
doesn't change sign. Hence, $a$ is not a local extreme point of $f$.
```


```{prf:definition} Critical point
:label: def-bra-rf-critical-point

Let $f : \RR \to \RR$ be a real function. Let $a \in \interior \dom f$.
If $f$ is not differentiable at $a$ or
if $f$ is differentiable at $x=a$ and $f'(a) = 0$, then we say that
$a$ is a *critical point* of $f$.
```

```{prf:definition} Stationary point
:label: def-bra-rf-stationary-point

If $f$ is differentiable at $x=a$ and $f'(a) = 0$, then we say that
$a$ is a *stationary point* of $f$.
```

All stationary points are critical points while all critical points
need not be stationary points. If the derivative doesn't exist
at some point $a \in \interior \dom f$, it could indicate a
potential maximum or minimum.


```{prf:remark}
:label: rem-bra-rf-extreme-critical-points

All local extreme points are critical points.
```

```{prf:example} A non-extreme critical point
:label: ex-bra-rf-non-extreme-critical-point

A critical point need not be a local extreme point. 
For the function $f(x) = x^3$, $f'(0) = 0$. Thus, $x=0$ is a
critical point. But it is not a local extreme point since $f$ 
changes sign around $x=0$.
```

```{prf:theorem} Rolle's theorem
:label: res-bra-df-rolle

Let $f$ be continuous on the closed interval $[a,b]$. 
Assume $f$ to be differentiable on the open interval $(a,b)$.
Further assume that $f(a) = f(b)$.
Then, $f'(c) = 0$ for some $c \in (a,b)$.
```

```{prf:proof}
Recall that if $f$ is continuous on a closed interval, then 
$f$ attains its maximum and minimum value on points in the interval
({prf:ref}`res-bra-rf-continuous-closed-max-min`).

Assume 

$$
\alpha = \inf_{a \leq x \leq b} f(x) \text{ and }
\beta = \sup_{a \leq x \leq b} f(x).
$$ 

If $\alpha=\beta$, then $f$ is a constant function on $[a,b]$. 
In that case, $f'(c) = 0$ for all $c \in (a,b)$.

Consider the case where  $\alpha < \beta$. 
In that case, either the maximum or the minimum
is attained at some point $c \in (a,b)$ 
since $f(a) = f(b)$.

1. If $\alpha = f(a) = f(b)$, then $\beta$ must be attained at some point in $c \in (a,b)$.
1. If $\beta = f(a) = f(b)$, then $\alpha$ must be attained at some point in $c \in (a,b)$.
1. If neither of the above hold true, then both $\alpha$ and $\beta$ are attained
   at some point in $(a,b)$.

Since $f$ is differentiable at $c$ and $f(c)$ is 
either maximum or minimum (i.e. a local extremum), hence $f'(c) = 0$ 
due to {prf:ref}`res-bra-df-extremum-zero-derivative`.
```

## Intermediate Values

```{prf:theorem} Intermediate value theorem for derivatives
:label: res-bra-rf-iv-theorem-derivatives

Suppose that:

1. $f$ is differentiable on an open interval $I$. 
1. There is a closed interval $[a,b] \subset I$. 
1. $f'(a) \neq f'(b)$.
1. $\mu$ is in between $f'(a)$ and $f'(b)$.

Then $f'(c) = \mu$ for some $c \in (a,b)$
```

Note that this result doesn't require 
$f$ to be {prf:ref}`continuously differentiable <def-bra-df-differentiability-closed-interval>` 
(i.e. $f'$ to be continuous). 

```{prf:proof}
Since $f$ is differentiable on $I$,
hence $f$ is continuous on $I$.

Assume without loss of generality:

$$
f'(a) < \mu < f'(b).
$$

Define

$$
g(x) = f(x) - \mu x.
$$

Then,

$$
g'(x) = f'(x) - \mu, \Forall a \leq x \leq b.
$$

Since $f'(a) < \mu$ hence $g'(a) < 0$. Similarly, $g'(b) > 0$. 

Since $g$ is continuous on $[a,b]$, hence $g$ attains a minimum
at some point $c \in [a,b]$ ({prf:ref}`res-bra-rf-continuous-closed-max-min`).

Now, $g'(a) < 0$ implies that there exists $\delta > 0$ such that:

$$
g(x) < g(a) \Forall a < x < a + \delta.
$$

Similarly,

$$
g(x) < g(b) \Forall b - \delta < x < b.
$$

Thus, minimum of $g$ cannot be at $a$ or $b$. Hence, $c \in (a, b)$.
Since $c$ is a local extreme point, and $g$ is differentiable at $c$, 
Hence $g'(c) = 0$ due to {prf:ref}`res-bra-df-extremum-zero-derivative`.
This in turn implies that $f'(c) = \mu$.

The case of $f'(a) > \mu > f'(b)$ can be handled by applying the
same argument to $-f$.
```

## Mean Values


```{prf:theorem} Generalized mean value theorem
:label: res-bra-df-gmvt

If $f$ and $g$ are continuous on the closed interval $[a,b]$ and
differentiable on the open interval $(a,b)$, then

$$
[g(b) - g(a)] f'(c) = [f(b) - f(a)]g'(c)
$$

holds true for some $c \in (a,b)$.
```

```{prf:proof}

Define the function:

$$
h(x) = [g(b) - g(a)] f(x) - [f(b) - f(a)]g(x).
$$

1. Since $f$ and $g$ are continuous on $[a,b]$, so is $h$.
1. Since $f$ and $g$ are differentiable on $(a,b)$ so is $h$.
1. $h(a) = h(b) = g(b)f(a) - f(b)g(a)$.
1. Therefore, by {prf:ref}`Rolle's theorem <res-bra-df-rolle>`, 
   $h'(c) = 0$ for some $c \in (a,b)$.
1. But $h'(c) = [g(b) - g(a)] f'(c) - [f(b) - f(a)]g'(c)$.
1. Hence the result.
```

```{prf:theorem} Mean value theorem
:label: res-bra-df-smvt

If $f$ is continuous on the closed interval $[a,b]$ and 
differentiable on the open interval $(a,b)$, then

$$
f'(c) = \frac{f(b) - f(a)}{b -a}
$$
for some $c \in (a,b)$. 
```

```{prf:proof}
In {prf:ref}`res-bra-df-gmvt`, let $g(x) = x$. 

Then,

$$
(b - a) f'(c) = f(b) - f(a).
$$
```

````{prf:remark}
:label: res-bra-df-smvt-impl

Assume $f$ to be differentiable on some open interval $(a,b)$.
Assume $x_1, x_2 \in (a,b)$. We haven't specified whether $x_1 < x_2$ or $x_1 > x_2$.


1. $f$ is continuous on the closed interval with endpoints $x_1$ and $x_2$.
1. $f$ is differentiable on the interior of this closed interval.
1. By {prf:ref}`mean value theorem <res-bra-df-smvt>`:

   ```{math}
   :label: eq-bra-df-mvt
   f(x_2) - f(x_1)  = f'(c) (x_2 - x_1)
   ```
   for some $c$ in the open interval between $x_1$ and $x_2$.
````


```{prf:theorem}
:label: res-bra-rf-zero-der-interval-constant-val

If $f'(x)=0$ for all $x \in (a,b)$, then $f$ is constant on $(a,b)$. 
```

```{prf:proof}
For any $x_1, x_2 \in (a,b)$, using {eq}`eq-bra-df-mvt`, we get:

$$
f(x_2)  - f(x_1) = 0.
$$
```

```{prf:theorem} No change in derivative sign implies monotonicity
:label: res-bra-rf-derivative-sign-change-monotonicity

If $f'$ exists and does not change sign on $(a,b)$, then $f$ is monotonic
on $(a,b)$. In particular:

1. If $f'(x) > 0$, then $f$ is strictly increasing in $(a,b)$.
1. If $f'(x) \geq 0$, then $f$ is increasing in $(a,b)$.
1. If $f'(x) \leq 0$, then $f$ is decreasing in $(a,b)$.
1. If $f'(x) < 0$, then $f$ is strictly decreasing in $(a,b)$.
```

```{prf:proof}
Let $x_1, x_2 \in (a,b)$ be such that $x_1 < x_2$. By mean value theorem,
there exists $c \in (x_1,x_2)$ such that:

$$
f(x_2) - f(x_1)  = f'(c) (x_2 - x_1).
$$


Now, 

1. If $f'(x) > 0 \Forall x \in (a,b)$, then $f(x_2) - f(x_1) > 0$.
1. If $f'(x) \geq 0 \Forall x \in (a,b)$, then $f(x_2) - f(x_1) \geq 0$.
1. If $f'(x) \leq 0 \Forall x \in (a,b)$, then $f(x_2) - f(x_1) \leq 0$.
1. If $f'(x) < 0 \Forall x \in (a,b)$, then $f(x_2) - f(x_1) < 0$.
```

```{prf:theorem} Bounded derivative implies Lipschitz continuity
:label: res-bra-rf-bounded-derivative-bounded-range

If 

$$
|f'(x)| \leq M, \Forall a < x < b,
$$

then:

$$
|f(x) - f(x') | \leq M | x - x'|, \Forall x, x' \in (a,b).
$$
```

This is another direct implication of the mean value theorem.
