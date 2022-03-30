(sec:ms:real-valued-functions)=
Real Valued Functions
=============================

In this section, we discuss results related
to real valued functions on metric spaces.
It is suggested to review the material from
{ref}`sec:bra:real-valued-functions` on arbitrary sets.
We assume $(X,d)$ to be an arbitrary metric space in this section.
Unless otherwise specified, $f : X \to \RR$ is a partial real
valued function from $X$ to $\RR$
with $\dom f \subseteq X$.

We shall be discussing closedness of the sublevel sets
and epigraphs of a function. The closedness is with
respect to the subspace topology of $(S, d)$ 
where $S = \dom f$.

Recall from {ref}`sec:ms:subspaces` that
for a metric space $(S, d)$

1. $S$ is open as well as closed in the subspace topology
   $(S, d)$.
1. A set $A$ is open in $(S, d)$ if and only if
   $A = S \cap B$ for some set $B$ which is open
   in $(X, d)$.
1. A set $A$ is closed in $(S, d)$ if and only if
   $A = S \cap B$ for some set $B$ which is closed
   in $(X, d)$.
1. If a sequence $\{x_n \}$ of $S$ is convergent
   w.r.t. the subspace topology $(S,d)$,
   then its limit $x = \lim x_n \in S$.


## Extreme Values


```{prf:definition} Local extreme value
We say that $f(a)$ is a *local extreme value* of $f$ at $a \in \dom f$ 
if there exists
$\delta > 0$ such that $f(x) - f(a)$ doesn't change sign on
$B(a, \delta) \cap \dom f$.

More specifically,

1. $f(a)$ is a *local maximum value* of $f$ if for some $\delta > 0$:

   $$
   f(x) \leq f(a) \Forall x \in B(a, \delta) \cap \dom f.
   $$ 
1. $f(a)$ is a *local minimum value* of $f$ if for some $\delta > 0$:

   $$
   f(x) \geq f(a) \Forall x \in B(a, \delta) \cap \dom f.
   $$ 

The point $x=a$ is called a *local extreme point* of $f$ or more 
specifically, a *local maximum* or a *local minimum* point of $f$.
```

```{prf:definition} Global maximum
We say that $f : X \to \RR$ attains a *global maximum*
at some $a \in \dom f$, if:

$$
f(x) \leq f(a) \Forall x \in \dom f.
$$
```

```{prf:definition} Global minimum
We say that $f : X \to \RR$ attains a *global minimum*
at some $a \in \dom f$, if:

$$
f(x) \geq f(a) \Forall x \in \dom f.
$$
```

```{prf:theorem} Extreme value theorem
Let $f : X \to \RR$ be continuous. 
Let $K$ be a nonempty compact subset of $\dom f$. 
Then, the set $f(K)$ is closed and bounded.
Also, there exists $a$ and $b$ in $K$ such that

$$
f(a) = \inf f(K) \text{ and } f(b) = \sup f(K);
$$
i.e., $f$ attains its supremum and infimum over the values in $f(K)$.
```

```{prf:proof}
Recall from {prf:ref}`res-ms-compact-continuous-map`
that continuous image of a compact set is compact. 
Hence, $f(A)$ is compact. 

But the compact subsets of $\RR$ are closed and bounded.
Hence, $f(A)$ is closed and bounded. 

Since $f(A)$ is closed and bounded, hence it contains
a supremum and an infimum.

Let $y = \inf f(A)$. Since $y \in f(A)$, hence
there exists $a \in \dom f$ such that $f(a) = y$.

Let $z = \sup f(A)$. Since $z \in f(A)$, hence
there exists $b \in \dom f$ such that $f(b) = z$.
```

Extreme value theorem is useful in optimization
problems. If it is possible to identify the
feasible set of input values as a closed and
bounded set, then it is possible to indicate
if the optimization problem has a solution 
or not. Although, the theorem doesn't help
in identifying the solution as such.

```{prf:example}
:label: ex-ms-max-vol-whd-constraint

Consider the optimization problem of maximizing
the volume of a box with the constraints:

$$
w + h + d \leq 6
$$
where $w$ indicates the width, $h$ indicates the
height and $d$ indicates the depth of the box.

We can define volume as a function $v : \RR^3 \to \RR$ as 

$$
v = w h d
$$
where each input vector $\bx \in \RR^3$ is 
a triplet $(w, h, d)$.

Now, note the implicit assumption that width,
height and depth cannot be negative.

Thus, we have the following constraints:

$$
w \geq 0, h \geq 0, d \geq 0, w + h + d \leq 6.
$$

These constraints define a simplex in $\RR^3$ which
is a closed and bounded set (thus compact). Hence,
the range of function values is also closed and
bounded. Hence, it is possible to choose
a configuration which maximizes the volume. 
```

## Closed Functions

```{prf:definition} Closed function
:label: def-ms-closed-function

A real valued function $f : X \to \RR$ with $S = \dom f$ 
is *closed* if for each $\alpha \in \RR$,
the corresponding sublevel set is closed
with respect to the subspace topology $(S,d)$. 

In other words, the sublevel set
$\{ x \in S \ST f(x) \leq \alpha \}$
is closed for every $\alpha \in \RR$
in the subspace topology $(S,d)$.
```

```{prf:theorem} Closed function = closed epigraph
:label: res-ms-closed-func-closed-epi

The {prf:ref}`epigraph <def-bra-epigraph>` of a function
$f : X \to \RR$ with $S = \dom f$ is closed
if and only if $f$ is closed.
```

```{prf:proof}
Let $f : X \to \RR$ with $S = \dom f$.
The epigraph of $f$ is given by

$$
\epi f = \{ (x, r) \in X \times \RR \ST x \in S, f(x) \leq r \}.
$$
By $T_{\alpha}$, we shall denote the sublevel set given as

$$
T_{\alpha} = \{ x \in S \ST f(x) \leq \alpha \}.
$$

Assume that $\epi f$ is closed.

1. Pick any $\alpha \in \RR$.
1. Let $T_{\alpha} = \{ x \in S \ST f(x) \leq \alpha \}$
   be the corresponding sublevel set.
1. Let $\{ x_n \}$ be a convergent sequence of $T_{\alpha}$.
1. Let $x = \lim_{n \to \infty} x_n$.
   We need to show that $x \in T_{\alpha}$.
1. By definition of $T_{\alpha}$,
   for every $x_n$, we have $f(x_n) \leq \alpha$.
1. Thus, $p_n = (x_n, \alpha) \in \epi f$.
1. Now, we see that the sequence $\{ p_n \}$ of $\epi f$
   is convergent and
   
   $$
   p = \lim p_n = \lim (x_n, \alpha) 
   = (\lim x_n, \alpha) = (x, \alpha).
   $$
1. Since $\epi f$ is closed, hence $(x, \alpha) \in \epi f$.
1. Thus, $x \in S$.
1. Also, by definition, $(x, f(x)) \in \epi f$
   and $f(x) \leq \alpha$.
1. Thus, $x \in S$ and $f(x) \leq \alpha$.
1. Thus, $x \in T_{\alpha}$.
1. This, every convergent sequence of $T_{\alpha}$ converges in $T_{\alpha}$.
1. Thus, $T_{\alpha}$ is closed.
1. Since $\alpha$ was arbitrary, hence
   every sublevel set of $f$ is closed.
1. Thus, $f$ is a closed function.


Assume that $f$ is closed.

1. Thus, every sublevel set of $f$ is closed.
1. Let $\{p_n\}$ be a convergent sequence of $\epi f$. 
1. Let $p_n = (x_n, r_n)$.
1. Then, $f(x_n) \leq r_n$ for all $n \in \Nat$. 
1. Let $p = \lim p_n$. Let $p = (x, r)$.
1. Then, $\lim x_n = x$ and $\lim r_n = r$.
1. We need to show that $p \in \epi f$.
1. Recall from {prf:ref}`res-bra-convergent-bounded` 
   that every convergent sequence of real numbers is bounded.
1. Since $\{ r_n \}$ is convergent, hence it is bounded.
1. Let $M \in \RR$ such that $r_n \leq M$ for all $n \in \Nat$.
1. Then, $f(x_n) \leq r_n \leq M$ for all $n \in \Nat$.
1. Consider the sublevel set $T_M = \{ x \in S \ST f(x) \leq M \}$.
1. Then, $x_n \in T_M$ for all $n \in \Nat$.
1. Then $\{x_n \}$ is a convergent sequence of $T_M$.
1. But every sublevel set of $f$ is closed. Hence $T_M$ is closed.
1. Every convergent sequence of a closed set converges in the set.
   Hence, $x = \lim x_n \in T_M$.
1. Thus, $(x, f(x)) \in \epi f$.
1. To show that $p = (x, r) \in \epi f$,
   we need to show that $f(x) \leq r$.
1. Let $\limsup_{n \to \infty} f(x_n) = u$.
1. Then, by {prf:ref}`res-bra-lim-sup-charac`,
   for any $\epsilon > 0$, there exists $n_0 \in \Nat$ such that
   
   $$
   f(x_n) < u + \epsilon \Forall n \geq n_0.
   $$
1. Thus, $x_n \in T_{u + \epsilon}$ for every $n \geq n_0$
   where $T_{u + \epsilon}$ is the sublevel set for $u + \epsilon$.
1. Since $\{x_n \}$ (after dropping the finite $n_0$ terms)
   is a convergent sequence of $T_{u + \epsilon}$ and
   $T_{u + \epsilon}$ is closed,
   hence $x \in T_{u + \epsilon}$.
1. Thus, $f(x) \leq u + \epsilon$.
1. Since, this is true for every $\epsilon > 0$, hence
   $f(x) \leq u = \limsup_{n \to \infty} f(x_n)$.
1. Recall that $f(x_n) \leq r_n$ for all $n \in \Nat$.
1. Then, by {prf:ref}`res-bra-order-limsup-liminf`,
   
   $$
   f(x) \leq \limsup f(x_n) \leq \limsup r_n = r.
   $$ 
1. Thus, $f(x) \leq r$.
1. Thus, $p = (x, r) \in \epi f$.
1. Thus, $\{p_n\}$ converges in $\epi f$.
1. Since $\{p_n\}$ was an arbitrary convergent sequence,
   hence every convergent sequence of $\epi f$ converges
   in $\epi f$.
1. Thus, $\epi f$ is closed.
```


```{prf:proposition}
If $f: X \to \RR$ is continuous and $\dom f$ is closed, then 
$f$ is closed.
```

```{prf:proposition}
If $f: X \to \RR$ is continuous and $\dom f$ is open, then
$f$ is closed if and only if $f$ converges to $\infty$ along
every sequence converging to a boundary point of $\dom f$. 
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

## Semicontinuity

The concept of semicontinuity is useful for the study of 
extreme values of some discontinuous functions.

We start with the notion of limit superior and limit
inferior at a point for functions.
We then proceed to define the notion of semicontinuity.

It is conventional to abbreviate "lower semicontinuous" as "l.s.c."
and "upper semicontinuous" as "u.s.c.". We will use these
abbreviations liberally.



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

We say that $f$ is lower semicontinuous (l.s.c.) if $f$ 
is l.s.c. at every point of $S$.


Similarly, we say that $f$ is upper semicontinuous (u.s.c.) if $f$ 
is u.s.c. at every point of $S$.
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

```{prf:theorem} Semicontinuity at isolated points
:label: res-ms-sc-isolated

Let $f : X \to \RR$ with $S = \dom f \subseteq X$.

Let $a \in S$ be an isolated point of $S$. Then, $f$ is
lower semicontinuous as well as upper semicontinuous at
$a$.
```

```{prf:proof}
Recall from {prf:ref}`def-ms-isolated-point` that
$a$ is isolated if there exists $\delta > 0$ such that 
$B(a, r) \cap S = \{ a \}$.

1. We are given that $a$ is isolated.
1. Let $\epsilon > 0$.
1. Choose $\delta > 0$ such that $B(a, r) \cap S = \{ a \}$
1. Since $\epsilon > 0$, hence
   $f(a) - \epsilon < f(a)$ and $f(a) < f(a) + \epsilon$.
1. Thus, $f$ is l.s.c. as well as u.s.c. at $a$.
```

### Continuity


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

### Limit Superior and Inferior

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

### Converging Sequences

Recall from {prf:ref}`def-bra-lim-sup-inf` that
the limit superior and limit inferior of a sequence
of real numbers is defined as 

$$
\limsup_{n \to \infty} x_n = \lim_{n \to \infty} \sup \{ x_k \ST k \geq n\}
$$
and

$$
\liminf_{n \to \infty} x_n  = \lim_{n \to \infty} \inf \{ x_k \ST k \geq n\}.
$$


```{prf:theorem} Semicontinuity and converging sequences
:label: res-ms-semicont-seq-converge

Let $f : X \to \RR$ with $S = \dom f$.
Let $a \in S$.
Then, $f$ is l.s.c. at $a$
if and only if for every sequence $\{x_n \}$ of $S$
that converges to $a$,

$$
\liminf_{n \to \infty} f(x_n) \geq f(a).
$$

Similarly, $f$ is upper semicontinuous at $a$
if and only if every sequence $\{x_k \}$ of $S$
that converges to $a$,

$$
\limsup_{n \to \infty}f(x_n) \leq f(a).
$$
```

```{prf:proof}
If $a \in S$ is an isolated point of $S$, then the only sequence
that converges to $a$ is $\{ x_n \}$ where $x_n = a$ for all terms after
a finitely many terms. For such sequences,

$$
\liminf_{n \to \infty} f(x_n) = \limsup_{n \to \infty} f(x_n) = f(a).
$$
Also, due to {prf:ref}`res-ms-sc-isolated`, $f$ is l.s.c. as well as
u.s.c. at isolated points.
Thus, this result holds trivially at isolated points. 

We are now left with the case
where $a \in S$ is an accumulation point of $S$.

Let $f$ be lower semicontinuous at $a$.

1. Let $\epsilon > 0$.
1. Since $f$ is l.s.c. at $a$, hence there exists $\delta > 0$
   such that

   $$
   f(a) - \epsilon < f(x) \Forall x \in B(a, \delta) \cap S.
   $$
1. Let $\{x_n \}$ be a sequence of $S$ that converges to $a$.
1. Then, there exists $n_0 \in \Nat$ such that for all $n > n_0$,
   $x_n \in B(a, \delta) \cap S$.
1. Thus, for all $n > n_0$, 
   $f(a) - \epsilon < f(x_n)$.
1. It follows that $f(a) - \epsilon \leq \liminf_{n \to \infty} f(x_n)$.
1. Since $\epsilon$ can be arbitrarily small, hence
   $f(a) \leq \liminf_{n \to \infty} f(x_n)$.

For the converse, we assume that
if $\lim x_n = a$, then $\liminf_{n \to \infty} f(x_n) \geq f(a)$.

1. By way of contradiction, assume that $f$ is not l.s.c. at $a$.
1. Then, there exists $\epsilon > 0$ such that
   for every $\delta > 0$, there exists
   $x_{\delta} \in B(a, \delta) \cap S$ such that

   $$
   f(a) - \epsilon \geq f(x_{\delta}).
   $$
1. Let $\delta_n = \frac{1}{n}$.
1. We can construct a sequence $\{ x_n \}$ such that
   for every $n$, $x_n \in B(a, \frac{1}{n}) \cap S$ such that
   
   $$
   f(a) - \epsilon \geq f(x_n).
   $$
1. This implies that 

   $$
   f(a) - \epsilon \geq \liminf_{n \to \infty} f(x_n).
   $$
1. This is a contradiction.

A similar argument can be used for limit superior.
```

##  Lower Semicontinuity

The topological properties of convex sets can be studied
in terms of *lower semicontinuity*. In this subsection,
we study the implications of lower semicontinuity under
the subspace topology.

```{prf:theorem} Lower semicontinuity and convergent dominating sequence

Let $f : X \to \RR$ with $S = \dom f$.
Let $a \in S$. Let $\{ a_n \}$ be a sequence of $S$.
Let $ \{ \mu_n \}$ be a sequence of real numbers such that $\mu_n \geq f(a_n)$.

Then, $f$ is l.s.c. at $a$ if and only if 
$\mu \geq f(a)$ whenever $\mu = \lim \mu_n$ and $a = \lim a_n$.
```

```{prf:proof}

Assume that $f$ is l.s.c. and   $\mu = \lim \mu_n$ and $a = \lim a_n$.

1. Then, due to {prf:ref}`res-ms-semicont-seq-converge`,

   $$
   \liminf_{n \to \infty} f(a_n) \geq f(a).
   $$
1. We are given that $\mu_n \geq f(a_n)$ for every $n$.
1. By {prf:ref}`res-bra-order-limsup-liminf`,
   
   $$
   \liminf_{n \to \infty} \mu_n \geq \liminf_{n \to \infty} f(a_n).
   $$
1. Since $\mu_n$ is convergent, hence

   $$
   \lim_{n \to \infty} \mu_n 
   = \liminf_{n \to \infty} \mu_n 
   \geq \liminf_{n \to \infty} f(a_n) \geq f(a).
   $$


For the converse, we are given that 
for any sequence $\{ x_n \}$ converging to $a$,
and any sequence $\{ \mu_n \}$ with $\mu_n \geq f(x_n)$
converging to $\mu$, we have $\mu \geq f(a)$.

1. Let $a \in S$.
1. Pick a sequence $\{ a_n \}$ such that $\lim a_n = a$.
1. Pick a convergent sequence $ \{ s_n \}$ such that $s_n \geq f(a_n)$.
1. By hypothesis $s = \lim s_n \geq f(a)$.
1. By way of contradiction, assume that $f$ is not l.s.c. at $a$.
1. Thus, $\liminf_{n \to \infty} f(a_n) < f(a)$.
1. Let $\liminf_{n \to \infty} f(a_n) = f(a) - r$ for some $r > 0$.
1. Since $\{ s_n \}$ is convergent, hence it is bounded
   (see {prf:ref}`res-bra-convergent-bounded`).
1. Since $s_n \geq f(a_n)$, hence $\{ f(a_n) \}$ is bounded from above.
1. $\{ f(a_n) \}$ cannot be unbounded from below.
   1. For contradiction, assume $\{ f(a_n) \}$ is unbounded below.
   1. We can choose a subsequence $\{ f(a_{k_n}) \}$ such that
      $\lim_{n \to \infty} f(a_{k_n}) = -\infty$.
   1. Let $b_n = a_{k_n}$ and $t_n = f(b_n)$.
   1. Then, $\lim b_n = a$ and $\lim t_n = -\infty$ even though $t_n \geq f(b_n)$.
   1. This contradicts the assumption that $\lim t_n \geq f(a)$.
   1. Thus, $\{ f(a_n)\}$ must be bounded from below.
1. Since $\{ f(a_n)\}$ is bounded, hence there is a subsequence
   that converges to the limit inferior $f(a) -r$.
   (see {prf:ref}`res-bra-set-subseq-limits-limsup-liminf`). 
1. Let $\{f (a_{k_n}) \}$ be a subsequence of $\{ f(a_n) \}$
   such that $\lim f (a_{k_n}) = f(a) - r$.
1. Let $b_n = a_{k_n}$.
1. Then, $\{b_n \}$ is a subsequence of $\{ a_n \}$.
1. Since $\{a_n \}$ converges to $a$, hence $\{b_n \}$ converges to $a$.
1. Now, choose $t_n = f(b_n)$. This is by definition a convergent sequence
   satisfying $t_n \geq f(b_n)$.
1. But then, $t = \lim t_n = f(b) - r < f(b)$.
1. This contradicts the hypothesis that $t \geq f(a)$.
1. Thus, $f$ must be l.s.c. at $a$.
1. Since $a$ was arbitrary, hence $f$ is l.s.c. at every $a \in S$.
```


### Epigraphs

```{prf:theorem} Lower semicontinuity = closed epigraph
:label: res-ms-func-lsc-closed-epi

Let $f : X \to \RR$ with $S = \dom f$.
$f$ is lower semicontinuous if and only if $\epi f$ is closed.
```

```{prf:proof}
Recall that $\epi f$ is a subset of $X \times \RR$ given by

$$
\epi f = \{(x, y) \ST f(x) \leq y \}.
$$

Suppose that $\epi f$ is closed.

1. Let $a \in S$ and let $\epsilon > 0$. 
1. Let $b = f(a) - \epsilon$. 
1. Then, $(a, b) \notin \epi f$.
1. Since $\epi f$ is closed, hence, there is an open ball $B(a, \delta)$
   around $a$ and an $r > 0$ such that

   $$
   B(a, \delta) \times (b - r, b + r) \cap \epi f = \EmptySet.
   $$
1. By structure of epigraph, $(a, c) \notin \epi f$ for any $c \leq b$.
   Thus,

   $$
   B(a, \delta) \times (-\infty, b + r) \cap \epi f = \EmptySet.
   $$
1. Thus, $f(x) \geq b + r$ for all $x \in B(a, \delta) \cap S$.
1. Thus, $f(x) > b = f(a) - \epsilon$ for all $x \in B(a, \delta) \cap S$.
1. Thus, for every $\epsilon > 0$, there exists $\delta > 0$ such that
   for every $x \in B(a, \delta) \cap S$, $f(x) > f(a) - \epsilon$.
1. Thus, $f$ is l.s.c. at $a$.
1. Since $a$ was arbitrary, hence $f$ is l.s.c.


For the converse, assume that $f$ is l.s.c.

1. Let $\{p_n \}$ be a convergent sequence of $\epi f$.
1. Let $p_n = (a_n, b_n)$.
1. Let $\lim p_n = p = (a, b)$.
1. Then, $\lim a_n = a$ and $\lim b_n = b$.
1. Also, $f(a_n) \leq b_n$.
1. Since $f$ is l.s.c. at $a$, hence
   by {prf:ref}`res-ms-semicont-seq-converge`
   
   $$
   \liminf_{n \to \infty} f(a_n) \geq f(a).
   $$
1. But then, $b_n \geq f(a_n)$ implies that

   $$
   b = \lim b_n \geq \liminf_{n \to \infty} f(a_n) \geq f(a).
   $$
1. But then, $f(a) \leq b$ implies that $(a, b) \in \epi f$.
1. Thus, every convergent sequence of $\epi f$ converges in $\epi f$.
1. Thus, by {prf:ref}`res-ms-closure-convergence`, $\epi f$ is closed.
```

### Closed Functions


```{prf:theorem} Lower semicontinuity = closed function
:label: res-ms-func-lsc-closed-func

Let $f : X \to \RR$ with $S = \dom f$.
$f$ is lower semicontinuous if and only if $f$ is 
{prf:ref}`closed <def-ms-closed-function>`.
```

```{prf:proof}
We shall denote the sublevel sets for $\alpha \in \RR$ by

$$
T_{\alpha} = \{ x \in S \ST f(x) \leq \alpha \}.
$$

Also, define

$$
U_{\alpha} = \{ x \in S \ST f(x) > \alpha \}.
$$

Note that $U_{\alpha} = S \setminus T_{\alpha}$.
Thus, $T_{\alpha}$ is closed if and only if $U_{\alpha}$ is open
with respect to the subspace topology $(S, d)$.

Assume that $f$ is closed. 

1. Let $a \in S$ and $\epsilon > 0$.
1. Let $r = f(a) - \epsilon$.
1. Consider the set $U_r = \{ x \in S \ST f(x) > r \}$.
1. Since sublevel sets of $f$ are closed, hence $U_r$ is open.
1. We note that $f(a) = r + \epsilon > r$.
1. Thus, $a \in U_r$.
1. Since $U_r$ is open, hence $a$ is an interior point of $U_r$.
1. Thus, there exists an open ball $B(a, \delta) \cap S \subseteq U_r$
   around $a$. 
1. Thus, for every $x \in B(a, \delta) \cap S$, 
   $f(x) > r = f(a) - \epsilon$.
1. Thus, for every $\epsilon > 0$, there exists $\delta > 0$
   such that $f(x) > f(a) - \epsilon$ for every 
   $x \in  B(a, \delta) \cap S$.
1. Thus, $f$ is l.s.c. at $a$.
1. Since $a \in S$ was arbitrary, hence $f$ is l.s.c. 



For the converse, assume that $f$ is l.s.c. 

1. Let $r \in \RR$.
1. Let $T_r = \{ x \in S \ST f(x) \leq r \}$
   be the corresponding sublevel set.
1. Let $\{x_n \}$ be a convergent sequence of $T_r$.
1. Let $x = \lim x_n$ with $x \in S$ (subspace topology).
1. Then, $f(x_n) \leq r$ for every $n$.
1. We need to show that $f(x) \leq r$.
1. Since $f$ is l.s.c. at $x$, hence
   
   $$
   f(x) \leq \liminf_{n \to \infty} f(x_n).
   $$
1. But $f(x_n) \leq r$.
1. Hence, $\liminf_{n \to \infty} f(x_n) \leq r$.
1. Thus, $f(x) \leq r$.
1. Thus, $x \in T_r$.
1. Since the sequence $\{x_n \}$ was arbitrary, hence $T_r$ is closed.
```

### Lower Semicontinuous Hull

```{prf:definition} Lower semicontinuous hull of a function
:label: def-lsc-hull-func

Let $f : X \to \RR$ with $S = \dom f$ be a function. 
There exists a greatest l.s.c. function $g$, majorized by $f$,
namely the function whose epigraph is the closure of
the epigraph of $f$. This function is known as the
*lower semicontinuous hull*  of $f$.

$$
\epi g = \closure \epi f.
$$
```

## Compact Subsets



```{prf:theorem} Upper semicontinuity and absolute maximum on a compact set
:label: res-ms-func-usc-max-compact

Let $f : X \to \RR$ with $S = \dom f$.
Assume that $f$ is upper semicontinuous on $S$.
Let $A$ be a compact subset of $S$.
Then $f$ attains a maximum on $A$;
i.e., there exists $a \in A$ such that 

$$
f(x) \leq f(a) \Forall x \in A.
$$
```

```{prf:proof}
We are given that $A$ is a compact subset of $S = \dom f$.
Recall from {prf:ref}`res-ms-compact-is-closed-bounded`
that compact sets are closed and bounded.

We first establish that $f(A)$ is bounded above.

1. For contradiction, assume that $f(A)$ is not bounded above.
1. Thus, $\sup_{x \in A} f(x) = \infty$.
1. Then, for every $n \in \Nat$, there exists
   $x_n \in A$ such that $f(x_n) \geq n$.
1. Consider the sequence $\{x_n \}$. 
   We have $\lim_{n \to \infty} f(x_n) = \infty$.
1. Since $A$ is compact,
   hence due to {prf:ref}`def-ms-compact-characterization`,
   $\{x_n \}$ has a convergent subsequence $\{ y_n \}$.
1. Since $A$ is closed, hence $y = \lim y_n \in A$.
1. Since $f$ is u.s.c. at $y$, hence
   
   $$
   \limsup_{n \to \infty} f(y_n) \leq f(y).
   $$
1. Since $f$ is real valued, hence $f(y)$ is finite.
1. But then, 

   $$
   \infty = \lim_{n \to \infty} f(x_n) 
   \leq \limsup_{n \to \infty} f(y_n)
   \leq f(y).
   $$
   A contradiction.
1. Thus, $f(A)$ must be bounded from above.


We now show that $f$ attains a maximum at some point in $A$.

1. Suppose that $\sup_{x \in A} f(x) = M$.
1. Then, for each $n$, there exists $x_n \in A$ such that
   
   $$
   M - \frac{1}{n} \leq f(x_n) \leq M.
   $$
1. Thus, we obtain a sequence $\{ x_n \}$ such that
   $\lim_{n \to \infty} f(x_n) = M$.
1. Since $A$ is bounded, hence $\{ x_n \}$ contains
   a convergent subsequence $\{ y_n \}$.
1. Since $A$ is closed, hence $y = \lim y_n \in A$.
1. Also $\lim f(y_n) = M$.
1. Thus, $f(y) = M$.
1. Thus, $f$ attains a maximum value of $M$ at $y \in A$. 
```

```{prf:theorem} Lower semicontinuity and absolute minimum on a compact set
:label: res-ms-func-lsc-min-compact

Let $f : X \to \RR$ with $S = \dom f$.
Assume that $f$ is lower semicontinuous on $S$.
Let $A$ be a compact subset of $S$.
Then $f$ attains a minimum on $A$;
i.e., there exists $a \in A$ such that 

$$
f(x) \geq f(a) \Forall x \in A.
$$
```


## Extended Real Valued Functions


Often, it is easier to work with extended real valued
functions $f : X \to \ERL$. In this case, $f$ is
defined at every $x \in X$ with $f$ taking the
value of $\infty$ or $-\infty$ outside its effective
domain. 

$$
\dom f = \{x \in X \ST f(x) \in \RR \}.
$$

We don't have to think in terms of subspace topology 
w.r.t. $(S, d)$ where $S$ is the effective domain.
All the definitions and results can be presented
w.r.t. the topology of $(X, d)$ itself.

### Proper Functions

```{prf:definition} Proper function
:label: def-ms-proper-function

Let $(X, d)$ be a metric space.
An extended real-valued function 
$f : X \to \ERL$ is called *proper*
if its domain is nonempty, it never
takes the value $-\infty$ and is
not identically equal to $\infty$.

$$
\exists x \in X \text{ such that } f(x) < \infty
\text{ and }
f(x) > -\infty \Forall x \in X.
$$
``` 
Putting another way, a proper function
is obtained by taking a real valued function $f$
defined on a nonempty set $C \subseteq X$
and then extending it to all of $X$ by 
setting $f(x) = +\infty$ for all $x \notin C$.

It is easy to see that the codomain for a proper
function can be changed from $\ERL$
to $\RERL$ to clarify that it never takes
the value $-\infty$.

```{prf:definition} Improper function
:label: def-ms-improper-function

Let $(X, d)$ be a metric space.
An extended real-valued function 
$f : X \to \ERL$ is called *improper*
if it is not proper.
```

For an improper function $f$:

* $\dom f$ may be empty. 
* $f$ might take a value of $-\infty$ at some $x \in X$.


```{prf:definition} Indicator function
:label: def-ms-indicator-function

Let $(X, d)$ be a metric space.
Let $C \subseteq X$. Then, its 
*indicator function* is given by
$I_C(x) = 0 \Forall x \in C$. 
Here, $\dom I_C = C$.

The extended value extension of an indicator
function is given by:

$$
\tilde{I_C}(x) \triangleq \begin{cases} 
0 & \text{for} & x \in C \\
\infty & \text{for} & x \notin C.
\end{cases}
$$
```



### Extreme Values

1. $f(a)$ is a *local maximum value* of $f$ if for some $\delta > 0$:

   $$
   f(x) \leq f(a) \Forall x \in B(a, \delta).
   $$ 
1. $f(a)$ is a *local minimum value* of $f$ if for some $\delta > 0$:

   $$
   f(x) \geq f(a) \Forall x \in B(a, \delta).
   $$ 
1. We say that $f : X \to \ERL$ attains a *global maximum*
   at some $a \in X$, if:

   $$
   f(x) \leq f(a) \Forall x \in X.
   $$
1. We say that $f : X \to \ERL$ attains a *global minimum*
   at some $a \in X$, if:

   $$
   f(x) \geq f(a) \Forall x \in X.
   $$

Evidently, a point outside $\dom f$ is either a 
global maximum or a global minimum.

If $f$ is proper, then $f$ never takes the value of $-\infty$.
In that case, if a global minimum is attained, then the
attained value is a finite real value.


Let $f : X \to \ERL$ be continuous. 
Let $K$ be a nonempty compact subset of $X$. 
Then, the set $f(K)$ is closed and bounded.
Also, there exists $a$ and $b$ in $K$ such that

$$
f(a) = \inf f(K) \text{ and } f(b) = \sup f(K);
$$
i.e., $f$ attains its supremum and infimum over the values in $f(K)$.

### Closed Functions

```{prf:definition} Closed Extended Real Valued Functions
:label: def-ms-evf-closed-func

$f : X \to \ERL$ is closed if for each $\alpha \in \ERL$, the
sublevel set
$T_{\alpha} = \{ x \in X \ST f(x) \leq \alpha \}$
is closed. 
```
We note that $T_{\infty} = X$ is closed.


### Limits


```{prf:definition} Limit superior and limit inferior
:label: def-ms-limsup-liminf-evf

Let $f : X \to \ERL$.
Let $a$ be an accumulation point of $X$. 

For some $\delta > 0$, let

$$
u_{\delta} = \sup_{x \in B_d(a,r)} f(x).
$$
Then, the *limit superior of the function* $f$ at $a$ is defined by

$$
\limsup_{x \to a } f(x) = \inf_{\delta > 0} u_{\delta}
= \inf_{\delta > 0} \sup_{x \in B_d(a,r)} f(x).
$$


Similarly, let

$$
l_{\delta} = \inf_{x \in B_d(a,r)} f(x).
$$
Then, the *limit inferior of the function* $f$ at $a$ is defined by

$$
\liminf_{x \to a } f(x) \triangleq \sup_{\delta > 0} l_{\delta}
= \sup_{\delta > 0} \inf_{x \in B_d(a,r)} f(x).
$$
```


* Even if $a \notin \dom f$, the $\limsup_{x \to a} f(x)$
  and $\liminf_{x \to a} f(x)$ may still be finite
  as long as there is a deleted neighborhood of $a$ which
  is entirely contained in $\dom f$.
* If there is a deleted neighborhood at $a$ such that
  $B_d(a, \delta) \cap \dom f = \EmptySet$, then 
  both limits will diverge.

```{prf:theorem} Characterization of function limit superior
:label: res-ms-evf-limsup-charac

Let $f : X \to \ERL$.
Let $a$ be an accumulation point of $X$.
Then, $u = \limsup_{x \to a} f(x)$ if and only if the following two
conditions hold:

1. For every $\epsilon > 0$, there exists $\delta > 0$ such that

   $$
   f(x) < u + \epsilon \Forall x \in B_d(a, \delta).
   $$
1. For every $\epsilon > 0$ and for every $\delta > 0$, there
   exists $x_{\delta} \in B_d(a, \delta)$ such that

   $$
   u - \epsilon < f(x_{\delta}).
   $$
```

```{prf:theorem} Characterization of function limit inferior
:label: res-ms-evf-liminf-charac

Let $f : X \to \ERL$.
Let $a$ be an accumulation point of $X$.
Then, $l = \liminf_{x \to a} f(x)$ if and only if the following two
conditions hold:

1. For every $\epsilon > 0$, there exists $\delta > 0$ such that

   $$
   l - \epsilon < f(x) \Forall x \in B_d(a, \delta).
   $$
1. For every $\epsilon > 0$ and for every $\delta > 0$, there
   exists $x_{\delta} \in B_d(a, \delta)$ such that

   $$
   f(x_{\delta}) < l + \epsilon.
   $$
```

### Semicontinuity

```{prf:definition} Lower and upper semicontinuity
:label: def-ms-evf-lower-semicontinuity

A function $f : X \to \ERL$
is said to be *lower-semicontinuous* 
at $a \in X$ if for every $\epsilon > 0$, there exists $\delta > 0$
such that

$$
f(a) - \epsilon < f(x) \text{ for every } x \in B(a, \delta).
$$

Similarly, $f$ is said to be *upper-semicontinuous* at $a \in X$
if for every $\epsilon > 0$, there exists $\delta > 0$
such that

$$
f(x) < f(a) + \epsilon \text{ for every } x \in B(a, \delta).
$$

We say that $f$ is lower semicontinuous (l.s.c.) if $f$ 
is l.s.c. at every point of $X$.

Similarly, we say that $f$ is upper semicontinuous (u.s.c.) if $f$ 
is u.s.c. at every point of $X$.
```


```{prf:theorem} Semicontinuity and function limits
:label: res-ms-evf-sc-limit

Let $f : X \to \ERL$.
Let $a \in X$ be an accumulation point of $X$.
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

```{prf:theorem} Semicontinuity and converging sequences
:label: res-ms-evf-sc-seq-converge

Let $f : X \to \ERL$.
Let $a \in X$.
Then, $f$ is l.s.c. at $a$
if and only if for every sequence $\{x_n \}$
that converges to $a$,

$$
\liminf_{n \to \infty} f(x_n) \geq f(a).
$$

Similarly, $f$ is upper semicontinuous at $a$
if and only if every sequence $\{x_k \}$
that converges to $a$,

$$
\limsup_{n \to \infty}f(x_n) \leq f(a).
$$
```
