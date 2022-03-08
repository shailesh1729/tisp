# Semicontinuity

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