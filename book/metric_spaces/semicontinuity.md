# Semicontinuity
The concept of semicontinuity is useful for the study of 
extreme values of some discontinuous functions.

Let $(X,d)$ be a metric space.

## Deleted Neighborhood


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
$B_d(a, r) \cap S$. 

It is clear that as $\delta$ increases, $u_{\delta}$ also increases.

If we define a function $g : (0, \infty) \to \RERL$ as

$$
g(\delta) = u_{\delta} = \sup_{x \in B_d(a,r) \cap S} f(x),
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

```{prf:theorem} Semicontinuity and function limits
:label: res-ms-semicont-func-limit

Let $f : X \to \RR$ with $S = \dom f$.
Let $a \in S$ be a limit point of $S$.
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

