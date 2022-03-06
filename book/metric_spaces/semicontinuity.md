# Semicontinuity
The concept of semicontinuity is useful for the study of 
extreme values of some discontinuous functions.

We start with the notion of limit superior and limit
inferior at a point for functions.
We then proceed to define the notion of semicontinuity.

It is conventional to abbreviate "lower semicontinuous" as "l.s.c."
and "upper semicontinuous" as "u.s.c.". We will use these
abbreviations liberally.



We shall assume $(X,d)$ to be a metric space throughout this section.

## Limit Superiors and Inferiors

```{prf:definition} Limit superior and limit inferior for functions
:label: def-ms-limsup-liminf-func

Let $f : X \to \RR$ with $S = \dom f$.
Let $a$ be an accumulation point of $S$. 

For some $\delta > 0$, let

$$
u_{\delta} = \sup_{x \in B_d(a,r) \cap S} f(x).
$$
Then, the *limit superior of the function* $f$ at $a$ is defined by

$$
\limsup_{x \to a } f(x) \triangleq \inf_{\delta > 0} u_{\delta}
= \inf_{\delta > 0} \sup_{x \in B_d(a,r) \cap S} f(x).
$$


Similarly, let

$$
l_{\delta} = \inf_{x \in B_d(a,r) \cap S} f(x).
$$
Then, the *limit inferior of the function* $f$ at $a$ is defined by

$$
\liminf_{x \to a } f(x) \triangleq \sup_{\delta > 0} l_{\delta}
= \sup_{\delta > 0} \inf_{x \in B_d(a,r) \cap S} f(x).
$$
```
We note that limit superior and inferior is also defined
for points which are not necessarily in $S$ but are on the
boundary of $S$ as some accumulation points of $S$ may be
on its boundary outside $S$. 
E.g., $\tan(x)$ is not defined at $x = \frac{\pi}{2}$ but
$\frac{\pi}{2}$ is an accumulation point for $\dom \tan$.
Hence, $\limsup$ and $\liminf$ can be computed there.

```{div}
$B_d(a,r) \cap S$ is simply the part of deleted neighborhood
at $a$ of radius $r$ which intersects with the domain of $f$.
Since $a$ is an accumulation point of $S$, hence
$B_d(a,r) \cap S$ is not empty. 
Thus, we are evaluating $f$ only at points at which it is defined.

$u_{\delta}$ is the supremum value of $f$ in the deleted neighborhood
$B_d(a, \delta) \cap S$. 

It is clear that as $\delta$ increases, $u_{\delta}$ also increases.

If we define a function $g : (0, \infty) \to \RERL$ as

$$
g(\delta) = u_{\delta} = \sup_{x \in B_d(a,\delta) \cap S} f(x),
$$
then $g$ is a nondecreasing function. Then,

$$
\limsup_{x \to a } f(x) = \inf_{\delta > 0} g(\delta).
$$
```

```{prf:definition} Locally bounded function
:label: def-ms-locally-bounded-func

Let $f : X \to \RR$ with $S = \dom f$.
Let $a$ be an accumulation point of $S$. 

We say that $f$ is *locally bounded above* around $a$ if there
exists $r > 0$ and $M \in \RR$ such that

$$
f(x) \leq M \Forall x \in B(x, r) \cap S.
$$

We say that $f$ is *locally bounded below* around $a$ if there
exists $r > 0$ and $m \in \RR$ such that

$$
f(x) \geq m \Forall x \in B(x, r) \cap S.
$$
```

```{prf:remark} Locally bounded functions and limit superior and inferior
:label: res-ms-local-bound-func-liminf-limsup

Let $f : X \to \RR$ with $S = \dom f$.
Let $a \in S$. 

If $f$ is locally bounded above at $a$, then $\limsup_{x \to a} f(x)$
is finite. Otherwise, $\limsup_{x \to a} f(x) = \infty$.


Similarly, if $f$ is locally bounded below at $a$, then $\liminf_{x \to a} f(x)$
is finite. Otherwise, $\liminf_{x \to a} f(x) = -\infty$.
```

### Limit Superior

```{prf:theorem} Characterization of function limit superior
:label: res-ms-func-limsup-charac

Let $f : X \to \RR$ with $S = \dom f$.
Let $a$ be an accumulation point of $S$.
Then, $u = \limsup_{x \to a} f(x)$ if and only if the following two
conditions hold:

1. For every $\epsilon > 0$, there exists $\delta > 0$ such that

   $$
   f(x) < u + \epsilon \Forall x \in B_d(a, \delta) \cap S.
   $$
1. For every $\epsilon > 0$ and for every $\delta > 0$, there
   exists $x_{\delta} \in B_d(a, \delta) \cap S$ such that

   $$
   u - \epsilon < f(x_{\delta}).
   $$
```

```{prf:proof}
Let  $g : (0, \infty) \to \RERL$ be defined as

$$
g(\delta) = \sup_{x \in B_d(a,\delta) \cap S} f(x).
$$


Suppose that $u = \limsup_{x \to a} f(x)$.

1. Then, $u = \inf_{\delta > 0} g(\delta)$.
1. Then, for ever $\epsilon > 0$, there exists $\delta > 0$ such that

   $$
   u \leq g(\delta) < u + \epsilon.
   $$
   Otherwise, $u$ won't be the infimum of $g(\delta)$.
1. Thus, for ever $\epsilon > 0$, there exists $\delta > 0$ such that

   $$
   f(x) < u + \epsilon \Forall x \in B_d(a,\delta) \cap S
   $$
   which proves condition (1).
1. Now, for every $\epsilon > 0$ and every $\delta > 0$, we have

   $$
   u - \epsilon < u \leq g(\delta) = \sup_{x \in B_d(a,\delta) \cap S} f(x).
   $$
1. By definition of the supremum, there exists $x \in B_d(a,\delta) \cap S$
   such that

   $$
   u - \epsilon < f(x_{\delta}).
   $$
   Otherwise, $g(\delta)$ would be smaller than $u$. This proves condition (2).


For the converse, we assume that conditions (1) and (2) are satisfied.

1. Let $\epsilon > 0$. Choose $\delta > 0$ that satisfies condition (1).
1. Then, we get

   $$
   g(\delta) = \sup_{x \in B_d(a,\delta) \cap S} f(x) \leq u + \epsilon.
   $$
1. Consequently, 

   $$
   \limsup_{x \to a} f(x) = \inf_{\delta > 0} g(\delta) \leq u + \epsilon.
   $$
1. Since $\epsilon > 0$ can be arbitrarily small, hence

   $$
   \limsup_{x \to a} f(x) \leq u.
   $$
1. Again, fix any $\epsilon > 0$ and pick any $\delta > 0$. 
   From condition (2),
   there exists $x_{\delta} \in B_d(a,\delta) \cap S$ such that

   $$
   u - \epsilon < f(x_{\delta}).
   $$
1. But, 

   $$
   f(x_{\delta}) \leq \sup_{x \in B_d(a,\delta) \cap S} f(x) = g(\delta).
   $$
1. Thus, $u - \epsilon < g(\delta)$.
1. Taking infimum on the R.H.S., over all $\delta > 0$,

   $$
   u - \epsilon \leq \inf_{\delta > 0} g(\delta) =  \limsup_{x \to a} f(x).
   $$
1. Since $\epsilon > 0$ can be arbitrarily small, hence 
   
   $$
   u \leq  \limsup_{x \to a} f(x).
   $$

Combining, these inequalities, we get $u = \limsup_{x \to a} f(x)$.
```

```{prf:theorem} Existence of convergent sequence to the limit superior of a function
:label: res-ms-func-limsup-seq-converge

Let $f : X \to \RR$ with $S = \dom f$.
Let $a$ be an accumulation point of $S$.
If $u = \limsup_{x \to a} f(x)$,
then there exists a sequence $\{ x_n \}$ of $S$ converging to $a$
with $x_n \neq a$ for every $n$
such that

$$
\lim_{n \to \infty} f(x_n) = u.
$$

Moreover, if $\{ y_n \}$ is any sequence of $S$ converging to $a$
with $y_n \neq a$ for every $n$, and the sequence $\{ f(y_n ) \}$ 
converges, then

$$
\lim_{n \to \infty} f(y_n) = u' \leq u.
$$

In other words, for any sequence $\{ x_n \}$ of $S \setminus \{ a \}$ converging to $a$,
$u$ is the least upper bound on $\lim_{n \to \infty} f(y_n)$ 
if $\{ f(y_n) \}$ converges.
```


```{prf:proof}

$u$ as the least upper bound.

1. Let $\{ y_n \}$ be a sequence of $S \setminus \{a\}$ such that
   $\lim_{n \to \infty} y_n = a$ and $\{ f(y_n) \}$  converges.
1. Let $\epsilon > 0$.
1. Then, due to {prf:ref}`res-ms-func-limsup-charac`,
   there exists $\delta > 0$ such that

   $$
   f(x) < u + \epsilon \Forall x \in B_d(a, \delta) \cap S.
   $$
1. Since $\{ y_n \}$ is convergent, hence there exists
   $n_0 \in \Nat$ such that for every $n > n_0$,
   $d(a, y_n) < \delta$.
1. Thus, for every $n > n_0$, $y_n \in B_d(a, \delta) \cap S$.
1. Thus, for every $n > n_0$, $f(y_n) < u + \epsilon$.
1. Thus,

    $$
    \lim_{n \to \infty} f(y_n) \leq u + \epsilon.
    $$
1. Since this is true for any $\epsilon > 0$ and $\epsilon$ can
   be made arbitrarily small, hence

   $$
   \lim_{n \to \infty} f(y_n) \leq u = \limsup_{ x \to a} f(x).
   $$


Construction of $\{ x_n \}$ such that $\lim_{n \to \infty} f(x_n) = u$.

1. Let $\epsilon_n = \frac{1}{n}$.
1. Then, due to {prf:ref}`res-ms-func-limsup-charac` (1),
   there exists $\delta_n > 0$ such that

   $$
   f(x) < u + \epsilon_n \Forall x \in B_d(a, \delta_n) \cap S.
   $$
1. Now, let $\delta'_n = \min\{\delta_n, \frac{1}{n} \}$.
   Clearly, $\delta'_n > 0$.
1. Due to {prf:ref}`res-ms-func-limsup-charac` (2), 
   there exists $x_n \in B_d(a, \delta'_n) \cap S$ such that

   $$
   u - \epsilon_n < f(x_n).
   $$
1. Consider the sequence so constructed $\{ x_n \}$.
1. Since $\delta'_n \leq \frac{1}{n}$, hence

   $$
   \lim_{n \to \infty} x_n = a.
   $$
1. For every $n$, $u - \epsilon_n < f(x_n) < u + \epsilon_n$.
1. $\lim_{n \to \infty} \epsilon_n = 0$.
1. Thus, by {prf:ref}`squeeze theorem <res-bra-sequence-squeeze>`,
   
   $$
   \lim_{n \to \infty} f(x_n) = u.
   $$
```


```{prf:theorem} Divergence of limit superior of a function
:label: res-ms-limsup-divergence-seq

Let $f : X \to \RR$ with $S = \dom f$.
Let $a$ be an accumulation point of $S$.
Then,

$$
\limsup_{x \to a} f(x) = \infty
$$
if and only if there exists a sequence $\{x_n \}$ of $S \setminus \{ a \}$
such that $\lim x_n = a$ and $\lim f(x_n) = \infty$.
```

```{prf:proof}
Let  $g : (0, \infty) \to \RERL$ be defined as

$$
g(\delta) = \sup_{x \in B_d(a,\delta) \cap S} f(x).
$$

Assume that $\limsup_{x \to a} f(x) = \infty$.

1. Then, $\inf_{\delta > 0} g(\delta) = \infty$.
1. Thus, $g(\delta) = \infty$ for every $\delta > 0$.
1. For each $n \in \Nat$, let $\delta_n = \frac{1}{n}$.
1. We have

   $$
   g(\delta_n) =  \sup_{x \in B_d(a,\delta_n) \cap S} f(x) = \infty.
   $$
1. Thus, there exists $x_n \in B_d(a,\delta_n) \cap S$
   such that $f(x_n) > n$.
1. We note that $\{ x_n \}$ converges to $a$ since
   $d(x_n, a) < \frac{1}{n}$. 
1. At the same time $\lim f(x_n) = \infty$ as $\{f(x_n) \}$ is
   unbounded.


For the converse, assume that
there exists a sequence $\{x_n \}$ of $S \setminus \{ a \}$
such that $\lim x_n = a$ and $\lim f(x_n) = \infty$.

1. Let $\delta > 0$.
1. Since $\{ x_n \}$ is convergent, hence
   there exists $m \in \Nat$ such that
   for all $n \geq m$, we have
   $x_n \in B_d(a,\delta) \cap S$.
1. Since $\lim f(x_n) = \infty$, hence 
   for every $M > 0$, there exists $k \in \Nat$ such that
   $f(x_n) \geq M$ for all $n \geq k$.
1. Let $p = \max(k, m)$.
1. Then, for all $n \geq p$, $x_n \in B_d(a,\delta) \cap S$
   and  $f(x_n) \geq M$.
1. Thus,

   $$
   g(\delta) = \sup_{x \in B_d(a,\delta) \cap S} f(x) \geq M.
   $$
1. Since $M$ can be made arbitrarily large, hence
   $g(\delta) = \infty$.
1. Since $g(\delta) = \infty$ for every $\delta > 0$, hence

   $$
   \limsup_{x \to a} f(x) = \inf_{\delta > 0} g(\delta) = \infty.
   $$
```

### Limit Inferior


```{prf:theorem} Characterization of function limit inferior
:label: res-ms-func-liminf-charac

Let $f : X \to \RR$ with $S = \dom f$.
Let $a$ be an accumulation point of $S$.
Then, $l = \liminf_{x \to a} f(x)$ if and only if the following two
conditions hold:

1. For every $\epsilon > 0$, there exists $\delta > 0$ such that

   $$
   l - \epsilon < f(x) \Forall x \in B_d(a, \delta) \cap S.
   $$
1. For every $\epsilon > 0$ and for every $\delta > 0$, there
   exists $x_{\delta} \in B_d(a, \delta) \cap S$ such that

   $$
   f(x_{\delta}) < l + \epsilon.
   $$
```

```{prf:theorem} Existence of convergent sequence to the limit inferior of a function
:label: res-ms-func-liminf-seq-converge

Let $f : X \to \RR$ with $S = \dom f$.
Let $a$ be an accumulation point of $S$.
If $l = \liminf_{x \to a} f(x)$,
then there exists a sequence $\{ x_n \}$ of $S$ converging to $a$
with $x_n \neq a$ for every $n$
such that

$$
\lim_{n \to \infty} f(x_n) = l.
$$

Moreover, if $\{ y_n \}$ is any sequence of $S$ converging to $a$
with $y_n \neq a$ for every $n$, and the sequence $\{ f(y_n ) \}$ 
converges, then

$$
\lim_{n \to \infty} f(y_n) = l' \geq l.
$$

In other words, for any sequence $\{ x_n \}$ of $S \setminus \{ a \}$ converging to $a$,
$l$ is the greatest lower bound on $\lim_{n \to \infty} f(y_n)$ 
if $\{ f(y_n) \}$ converges.
```

```{prf:theorem} Divergence of limit inferior of a function
:label: res-ms-liminf-divergence-seq

Let $f : X \to \RR$ with $S = \dom f$.
Let $a$ be an accumulation point of $S$.
Then,

$$
\liminf_{x \to a} f(x) = -\infty
$$
if and only if there exists a sequence $\{x_n \}$ of $S \setminus \{ a \}$
such that $\lim x_n = a$ and $\lim f(x_n) = -\infty$.
```

### Existence of Function Limit


```{prf:theorem} Function limit = limit superior = limit inferior
:label: res-ms-func-liminf-limsup-eq-lim

Let $f : X \to \RR$ with $S = \dom f$.
Let $a$ be an accumulation point of $S$.

Then, 

$$
\lim_{x \to a} f(x) = l
$$
if and only if 

$$
\limsup_{x \to a} f(x) = \liminf_{x \to a} f(x) = l.
$$
```

```{prf:proof}

Suppose $\lim_{x \to a} f(x) = l$.

1. For every $\epsilon > 0$, there exists $r > 0$ such that

   $$
   l - \epsilon < f(x) < l + \epsilon \Forall x \in B_d(a, r) \cap S.
   $$
1. Note that this holds true for every $\delta \in (0, r]$.
1. Thus, for every $\delta \in (0, r]$
   
   $$
   l - \epsilon < g(\delta) = \sup_{x \in B_d(a,\delta) \cap S} f(x) \leq l + \epsilon.
   $$
1. Recall that $g(\delta)$ is a nondecreasing function.
1. Thus, taking infimum over $\delta > 0$ 
    
   $$
   l - \epsilon \leq \inf_{\delta > 0}g(\delta) \leq l + \epsilon.
   $$
1. Since, $\epsilon$ can be made arbitrarily small, hence
   
   $$
   \limsup_{x \to a} f(x) = \inf_{\delta > 0}g(\delta) = l.
   $$
1. An identical reasoning shows that $\liminf_{x \to a} f(x) = l$.


For the converse, assume that
$\limsup_{x \to a} f(x) = \liminf_{x \to a} f(x) = l$.

1. Let $\epsilon > 0$.
1. From {prf:ref}`res-ms-func-limsup-charac`, there exists $\delta_1 > 0$
   such that

   $$
   f(x) < l + \epsilon \Forall x \in B_d(a, \delta_1) \cap S.
   $$
1. From {prf:ref}`res-ms-func-liminf-charac`, there exists $\delta_2 > 0$
   such that 

   $$
   l - \epsilon < f(x) \Forall x \in B_d(a, \delta_2) \cap S.
   $$
1. Let $\delta = \min\{\delta_1, \delta_2 \}$. Then,

   $$
   l - \epsilon < f(x) < l + \epsilon \Forall x \in B_d(a, \delta) \cap S.
   $$
1. Thus, for every $\epsilon > 0$, there exists $\delta > 0$ such that

   $$
   |f(x) - l | < \epsilon \Forall x \in B_d(a, \delta) \cap S.
   $$
1. Thus, $\lim_{x \to a} f(x) = l$.
```

## Lower and Upper Semicontinuity

```{prf:definition} Lower and upper semicontinuity
:label: def-ms-lower-semicontinuity

A (partial) function $f : X \to \RR$ with $S = \dom f \subseteq X$
is said to be *lower-semicontinuous* 
at $a \in S$ if for every $\epsilon > 0$, there exists $\delta > 0$
such that

$$
f(a) - \epsilon < f(x) \text{ for every } x \in B(a, \delta) \cap S.
$$

Similarly, $f$ is said to be *upper-semicontinuous* at $a \in S$
if for every $\epsilon > 0$, there exists $\delta > 0$
such that

$$
f(x) < f(a) + \epsilon \text{ for every } x \in B(a, \delta) \cap S.
$$
```

```{prf:example} Semicontinuous functions

Consider the function $f : \RR \to \RR$ defined as

$$
f(x) = \begin{cases}
0, & x < 0\\
1, & x \geq 0.
\end{cases}
$$

$f$ is upper semicontinuous at $x=0$.

1. We have $f(0)= 1$. 
1. Let $\epsilon > 0$.
1. For any $\delta > 0$
   1. $f(\delta) = 1 < 1 + \epsilon$.
   1. $f(-\delta) = 0 < 1 + \epsilon$.
1. Thus, we can pick any $\delta > 0$ and for any
   $x \in (-\delta, \delta)$, 
   $f(x) < f(0) + \epsilon$.
1. Thus, $f$ is upper semicontinuous at $x=0$.

We can easily show that $f$ is not lower semicontinuous at $x=0$. 

1. Let $\epsilon = \frac{1}{2}$. 
1. $f(0)-\epsilon = \frac{1}{2}$.
1. For any $\delta > 0$, $f(0 - \delta) = 0 \not> \frac{1}{2} = f(0) - \epsilon$.
1. thus, for this choice of $\epsilon$, there is no $\delta > 0$ satisfying
   the lower semicontinuity inequality.

Consider the function $g : \RR \to \RR$ defined as

$$
g(x) = \begin{cases}
0, & x \leq 0\\
1, & x > 0.
\end{cases}
$$

$g$ is lower semicontinuous at $x=0$.

The ceiling function $f(x) = \lceil x \rceil$ is lower semicontinuous.

The floor function $f(x) = \lfloor x \rfloor$ is upper semicontinuous.
```


```{prf:theorem} Lower + upper semicontinuity = Continuity
:label: res-ms-lsc-usc-continuous

A (partial) function $f : X \to \RR$ with $S = \dom f \subseteq X$
is continuous at $a \in S$ if and only if 
$f$ is both lower semicontinuous and upper semicontinuous at $a$.
```

```{prf:proof}
Assume that $f$ is continuous at $a \in S$.

1. Let $\epsilon >0$.
1. There exists $\delta > 0$ such that for every
   $x \in B(a, \delta) \cap S$,
   $|f(x) - f(a)| < \epsilon$.
1. Consequently, $f(x) - f(a) < \epsilon$
   means that $f(x) < f(a) + \epsilon$
   for every $x \in B(a, \delta) \cap S$.
1. Thus, $f$ is upper semicontinuous at $a$.
1. Similarly, $f(a) - f(x) < \epsilon$
   means that $f(a) - \epsilon < f(x)$ for every
   $x \in B(a, \delta) \cap S$.
1. Thus, $f$ is lower semicontinuous at $a$.

Assume $f$ is lower and upper semicontinuous at $a \in S$.

1. Let $\epsilon > 0$.
1. There exists $\delta_1 > 0$ such that
   $f(a) - \epsilon < f(x)$ for every
   $x \in B(a, \delta_1) \cap S$.
1. There exists $\delta_2 > 0$ such that
   $f(x) < f(a) + \epsilon$ for every
   $x \in B(a, \delta_2) \cap S$.
1. Let $\delta = \min(\delta_1, \delta_2)$.
1. Then, for every $x \in B(a, \delta) \cap S$,
   $f(a) - f(x) < \epsilon$ as well as
   $f(x) - f(a) < \epsilon$.
1. Thus, for every $x \in B(a, \delta) \cap S$,
   $|f(x) - f(a)| < \epsilon$.
1. Thus, $f$ is continuous at $a$.
```

```{prf:theorem} Semicontinuity and function limits
:label: res-ms-semicont-func-limit

Let $f : X \to \RR$ with $S = \dom f$.
Let $a \in S$ be an accumulation point of $S$.
Then, $f$ is lower semicontinuous at $a$
if and only if 

$$
\liminf_{x \to a} f(x) \geq f(a).
$$

Similarly, $f$ is upper semicontinuous at $a$
if and only if

$$
\limsup_{x \to a}f(x) \leq f(a).
$$
```
For a function $f$ and at an accumulation point $a \in \dom f$,
we define a function $g : (0, \infty) \to \RERL$ as

$$
g(\delta) = \sup_{x \in B_d(a,\delta) \cap S} f(x).
$$
$g$ is a nondecreasing function of $\delta$.

Similarly, we define a function $h : (0, \infty) \to \LERL$ as

$$
h(\delta) = \inf_{x \in B_d(a,\delta) \cap S} f(x).
$$

$h$ is a nonincreasing function of $\delta$.

We note that

$$
\limsup_{x \to a} f(x) = \inf_{\delta > 0} g(\delta)
\text{ and }
\liminf_{x \to a} f(x) = \sup_{\delta > 0} h(\delta).
$$

```{prf:proof}

Let $f$ be lower semicontinuous at $a$.

1. Let $\epsilon > 0$.
1. Since $f$ is l.s.c. at $a$, hence there exists $\delta_0 > 0$
   such that

   $$
   f(a) - \epsilon < f(x) \Forall x \in B(a, \delta_0) \cap S.
   $$
1. Taking infimum in the R.H.S. over the set $B_d(a, \delta_0) \cap S$,

   $$
   f(a) - \epsilon \leq h(\delta_0).
   $$
1. Thus,

   $$
   \liminf_{x \to a} f(x) = \sup_{\delta > 0} h(\delta) 
   \geq h(\delta_0) \geq f(a) - \epsilon.
   $$
1. Since $\epsilon$ is arbitrary, hence

   $$
   \liminf_{x \to a} f(x) \geq f(a).
   $$

For the converse, assume that $\liminf_{x \to a} f(x) \geq f(a)$.

1. We can write this as

   $$
   \liminf_{x \to a} f(x) = \sup_{\delta > 0} h(\delta) \geq f(a).
   $$
1. Let $\epsilon > 0$.
1. Then, 

   $$
   \sup_{\delta > 0} h(\delta) > f(a) - \epsilon.
   $$
1. Thus, there exists $\delta > 0$ such that  $h(\delta) > f(a) - \epsilon$.
1. Thus,

   $$
   f(x) > f(a) - \epsilon \Forall x \in B_d(a, \delta) \cap S.
   $$
1. Also, $f(a) > f(a) - \epsilon$ trivially.
1. Thus, for every $\epsilon > 0$, there exists $\delta > 0$ such that

   $$
   f(x) > f(a) - \epsilon \Forall x \in B(a, \delta) \cap S.
   $$
1. Thus, $f$ is l.s.c. at $a$.

The proof for  upper semicontinuity is analogous.
```