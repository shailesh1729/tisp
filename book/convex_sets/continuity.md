# Continuity

This section focuses on closure and semicontinuity of convex functions
in normed linear spaces.

Throughout this section, we assume that $\VV$ is a 
finite dimensional real normed linear space equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \| : \VV \to \RR$.
It is also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$.
Wherever necessary,
it is also equppied with an 
{prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle : \VV \times \VV \to \RR$. 


We recall that a function $f : \VV \to \RR$ is
$L$-Lipschitz if 

$$
| f(\bx) - f(\by) | \leq L \| \bx - \by \| \Forall \bx, \by \in \VV.
$$


The concept of semicontinuity, inferior and superior limits
and closedness of real valued functions in metric spaces
is discussed in detail in {ref}`sec:ms:real-valued-functions`.

We recall some results.


Let $f : \VV \to \RR$ with $S = \dom f$ be a function.

Let $\ba$ be an accumulation point of $S$. 
The limit superior of $f$ at $\ba$ is defined by

$$
\limsup_{\bx \to \ba } f(\bx)
= \inf_{\delta > 0} \sup_{\bx \in B_d(\ba,r) \cap S} f(\bx).
$$
The limit inferior of $f$ at $\ba$ is defined by

$$
\liminf_{\bx \to \ba } f(\bx)
= \sup_{\delta > 0} \inf_{\bx \in B_d(\ba,r) \cap S} f(\bx).
$$


$f$ is lower-semicontinuous 
at $\ba \in S$ if for every $\epsilon > 0$, there exists $\delta > 0$
such that

$$
f(\ba) - \epsilon < f(\bx) 
\text{ for every } \bx \in B(\ba, \delta) \cap S.
$$

$f$ is upper-semicontinuous 
at $\ba \in S$ if for every $\epsilon > 0$, there exists $\delta > 0$
such that

$$
f(\bx)  < f(\ba) + \epsilon 
\text{ for every } \bx \in B(\ba, \delta) \cap S.
$$

We say that $f$ is lower semicontinuous (l.s.c.) if $f$ 
is l.s.c. at every point of $S$.
Similarly, we say that $f$ is upper semicontinuous (u.s.c.) if $f$ 
is u.s.c. at every point of $S$.


$f$ is continuous at $\ba \in S$ if and only if 
$f$ is l.s.c. as well as u.s.c. at $\ba$.


Let $\ba \in S$ be an accumulation point of $S$.
Then, $f$ is lower semicontinuous at $\ba$
if and only if 

$$
\liminf_{\bx \to \ba} f(\bx) \geq f(\ba).
$$
Similarly, $f$ is upper semicontinuous at $\ba$
if and only if

$$
\limsup_{\bx \to \ba}f(\bx) \leq f(\ba).
$$
Let $\ba \in S$.
Then, $f$ is l.s.c. at $\ba$
if and only if for every sequence $\{\bx_n \}$ of $S$
that converges to $\ba$,

$$
\liminf_{n \to \infty} f(\bx_n) \geq f(\ba).
$$

Similarly, $f$ is upper semicontinuous at $\ba$
if and only if every sequence $\{\bx_k \}$ of $S$
that converges to $\ba$,

$$
\limsup_{n \to \infty}f(\bx_n) \leq f(\ba).
$$


The following conditions are equivalent.

1. $f$ is l.s.c. 
1. $f$ is closed; i.e., every sublevel set of $f$ is closed
   with respect to the subspace topology $(S, \| \cdot \|)$.
1. $\epi f$ is closed in  $\VV \oplus \RR$.


## Closure

```{prf:definition} Closure of a convex function
:label: def-cvxf-convex-func-closure

Let $f : \VV \to \RR$ be a convex function.
Then, its *closure* is defined to be the
{prf:ref}`lower semicontinuous hull <def-lsc-hull-func>`  of $f$.

If $g$ is the closure of $f$, then

$$
\epi g = \closure \epi f.
$$

If $f: \VV \to \RERL$ is a proper convex function, 
then also, its closure is defined to be the
lower semicontinuous hull.

If $f: \VV \to \ERL$ is an improper convex function
which attains a value $f(\bx) = -\infty$ at some
$\bx \in \VV$, then its closure is defined to be 
the constant function $g(\bx) = -\infty$ for all $\bx \in \VV$.

The closure of a convex function is denoted by $\closure f$.
```


```{prf:theorem} Closure of a convex function is convex
:label: res-cvxf-convex-func-closure-convex

The closure of a convex function is convex.
```

```{prf:proof}
Let $f$ be a convex function. Then, $\epi f$ is convex.
Let $g$ be its closure.

1. If $f$ is improper, then $g$ is a constant function, hence convex.
1. Otherwise, $\epi g = \closure \epi f$.
1. Since $f$ is convex, hence $\epi f$ is convex.
1. Due to {prf:ref}`res-cvx-closure-convex-set-convex`,
   the closure of a convex set is convex.
1. Hence, $\epi g$ is convex.
1. Hence, $g$ is convex.
```


```{prf:definition} Closed convex function
:label: def-cvx-closed-convex-func

A convex function $f: \VV \to \ERL$ is called
*closed* if 

$$
\closure f = f.
$$
```

For a proper convex function, closedness
is same as lower semicontinuity.

The only closed improper convex functions are

1. $f(\bx) = \infty \Forall \bx \in \VV$. Here $\epi f = \EmptySet$.
1. $f(\bx) = -\infty \Forall \bx \in \VV$. Here $\epi f = \VV \times \RR$.


```{prf:example} Closed convex function with open domain
:label: ex-cvxf-closed-convex-function-open-domain

Let $f: \RR \to \RERL$ be given as

$$
f(x) = \begin{cases}
\frac{1}{x}, & x > 0\\
\infty, & x \leq 0.
\end{cases} 
$$
Then, $\dom f = (0, \infty)$. 

1. $\dom f$ is an open interval in $\RR$.
1. $f$ is continuous at every $x > 0$.
1. Thus, $f$ is l.s.c. at every $x > 0$.
1. Thus, $f$ is l.s.c.
1. Let the sublevel set for $r \in \RR$ 
   be given by 

   $$
   T_r = \{ x \in (0, \infty) \ST f(x) \leq r \}.
   $$
1. We can see that $T_r = \EmptySet$ for $r \leq 0$.
1. For $r > 0$,  

   $$
   f(x) = \frac{1}{x} \leq r \iff x \geq \frac{1}{r}.
   $$
1. Thus, $T_r = [\frac{1}{r}, \infty)$.
1. $T_r$ is indeed closed in the topology $(\dom f, | \cdot |)$.
1. Since $f$ is l.s.c., hence $\epi f$ is closed.
1. Thus, $\closure f = f$.
1. Thus, $f$ is a closed convex function.
```

```{prf:remark} Closure of proper convex functions and epigraph
:label: rem-cvxf-epi-cl-cl-epi

Let $f: \VV \to \RERL$ be a proper convex function. Then, 

$$
\epi \closure f = \closure \epi f.
$$

This follows from the definition, since $g = \closure f$ is
defined by the fact that

$$
\epi g = \closure \epi f.
$$
```