# Continuity

This section focuses on topological properties of 
convex functions in normed linear spaces.
In particular, we discuss 
closure of convex functions,
continuity of convex functions at interior points.

Main references for this section are 
{cite}`beck2014introduction,boyd2004convex,rockafellar2015convex`. 

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


## Continuity

Convex functions are not necessarily continuous on non-open sets.

```{prf:example} A convex function which is not continuous
:label: ex-cvxf-convex-non-continuous

Let $f : \RR \to \RR$ be given by

$$
f(x) = \begin{cases}
1, & x = 0,\\
x^2 & 0 < x \leq 1.
\end{cases}
$$
We can see that $\dom f = [0, 1]$. $f$ is continuous on $(0,1)$
but $f$ is not continuous (from the right) at $x=0$. It is
continuous (from the left) at $x=1$.
```

Convex functions are continuous at points in the
interior of their domain.


```{prf:theorem} Local Lipschitz continuity of convex functions
:label: res-cvxf-convex-local-lipschitz-continuous

Let $\VV$ be an $n$-dimensional real normed linear space.
Let $f: \VV \to \RR$ be a convex function with $S = \dom f$.
Let $\ba \in \interior S$. Then, there exists $r > 0$ 
and $L > 0$ such that $B(\ba, r) \subseteq S$ and

$$
|f (\bx) - f(\ba)| \leq L \| \bx - \ba \|
$$
for every $\bx \in B[\ba, r]$.
```

We recall from {prf:ref}`res-cvx-convex-set-empty-interior`
that if $\dim \affine S < n$ then $S$ has an empty interior.
Thus, if $\interior S$ is nonempty, then, $\affine S = \VV$.

```{prf:proof}

We shall structure the proof as follows. For any $\ba \in \interior S$:

1. We show that $f$ is bounded on a closed ball $B[\ba, r] \subseteq S$.
1. Then, we show that $f$ satisfies the Lipschitz inequality
   $|f (\bx) - f(\ba)| \leq L \| \bx - \ba \|$ on the 
   closed ball $B[\ba, r]$
   for a specific choice of $L$ depending on $\ba$ and $r$.

We first introduce $\| \cdot \|_{\infty}$
norm on $\VV$ and describe its implications.

1. Choose a basis $\BBB = \{\be_1, \dots, \be_n \}$ for $\VV$.
1. For every $\bx \in \VV$, we have a unique representation
   
   $$
   \bx = \sum_{i=1}^n x_i \be_i.
   $$
1. Let $T : \VV \to \RR^n$ be a coordinate mapping 
   which maps every vector $\bx \in \VV$ to its
   coordinate vector $(x_1, \dots, x_n) \in \RR^n$.
1. $T$ is an isomorphism.
1. Define $\| \cdot \|_{\infty} : \VV \to \RR$ as

   $$
   \| \bx \|_{\infty} = \| T(\bx) \|_{\infty} = \max_{i=1,\dots,n}|x_i|.
   $$
1. It is easy to show that $\| \cdot \|_{\infty}$ is a norm on $\VV$.
1. By {prf:ref}`res-la-ns-finite-all-norms-eq`, 
   all norms are equivalent.
1. Thus, $\| \cdot \|$ and $\| \cdot \|_{\infty}$ are
   equivalent norms for $\VV$.
1. By {prf:ref}`def-la-ns-finite-norm-topology`, 
   the norm topology is identical for all norms
   in a finite dimensional space.
1. Thus, a point is an interior point of $S$ 
   irrespective of the norm chosen.
1. We introduce the closed and open balls in 
   $(\VV, \| \cdot \|_{\infty})$
   as

   $$
   B_{\infty}[\ba, \delta] = \{\bx \in \VV  \ST 
      \| \bx - \ba \|_{\infty} \leq \delta \}
   \text{ and }
   B_{\infty}(\ba, \delta) = \{\bx \in \VV  \ST 
      \| \bx - \ba \|_{\infty} < \delta \}.
   $$
1. Let $\ba \in \interior S$.
1. Then, there exists $r_1 > 0$ such that
   $B_{\infty}[\ba, r_1] \subseteq S$.
   due to {prf:ref}`res-ms-interior-point-closed`.
1. Then, $B_{\infty}(\ba, r_1) \subseteq B_{\infty}[\ba, r_1]$.
1. By {prf:ref}`res-ms-eq-metric-ball-in-ball`, there
   is an $r_2 > 0$ such that
   $B(\ba, r_2) \subseteq  B_{\infty}(\ba, r_1)$.
1. By {prf:ref}`res-open-closed-ball-contain`, 
   we can pick an $0 < r < r_2$ such that

   $$
   B[\ba, r] \subseteq B(\ba, r_2)
   \subseteq  B_{\infty}(\ba, r_1)
   \subseteq B_{\infty}[\ba, r_1]
   \subseteq S.
   $$

We now show that $f$ is bounded on $B[\ba, r]$.

1. $B_{\infty}[\ba, r_1]$ is closed and bounded.
1. Hence $B_{\infty}[\ba, r_1]$ is compact
   due to {prf:ref}`res-la-ndim-compact-closed-bounded`.
1. By {prf:ref}`Krein Milman theorem <res-cvx-krein-milman>`,
   a compact convex set is convex hull of its extreme points.
   Thus,

   $$
   B_{\infty}[\ba, r_1] = \convex \extreme B_{\infty}[\ba, r_1].
   $$
1. Let $\bv_1, \dots, \bv_N$ be the $N=2^n$ 
   extreme points of $B_{\infty}[\ba, r_1]$.
   1. These extreme points are given by
    
      $$
      \bv_i = \ba + r_1 \bw_i
      $$
      where $\bw_i$ are the vectors with coordinates
      $\{-1, 1\}^n$.
   1. In other words,

      $$
      \bw_i = \sum_{j=1}^n w^i_j \be_j
      $$
      where $w^i_j \in \{ -1, 1 \}$.
   1. Note that

      $$
      \| \bv_i - \ba \| = r \| \bw_i \| 
      = r_1 \max \{ |w^i_j| \} = r_1.
      $$
   1. Thus, $\bv_i \in \boundary B_{\infty}[\ba, r_1]$.
   1. Readers can verify that these are indeed the
      extreme points of $B_{\infty}[\ba, r_1]$ and 
      there are no other extreme points.
1. Then, by Krein Milman theorem,
 
   $$
   B_{\infty}[\ba, r_1] = \convex \{\bv_1, \dots, \bv_N \}.
   $$
1. Thus, every $\bx \in B_{\infty}[\ba, r_1]$ is a convex
   combination of the extreme points. Specially, 
   there exists $t \in \Delta_N$ (unit simplex of $\RR^N$) such that

   $$
   \bx = \sum_{i=1}^N t_i \bv_i.
   $$
1. Now, by {prf:ref}`Jensen's inequality <res-cvxf-jensen-inequality>`,

   $$
   f(\bx) \leq \sum_{i=1}^N t_i f(\bv_i).
   $$
1. Let $M = \max \{f(\bv_1), \dots, f(\bv_N) \}$.
1. Then,

   $$
   f(\bx) \leq \sum_{i=1}^N t_i f(\bv_i)
   \leq \sum_{i=1}^N t_i  M = M \sum_{i=1}^N t_i = M.
   $$
1. Since $B[\ba, r] \subseteq B_{\infty}[\ba, r_1]$, 
   hence $f(\bx) \leq M$ for every $\bx \in B[\ba, r]$.

We have shown that $f(\bx) \leq M$ for every $\bx \in B[\ba, r]$.
We next find an $L$ such that

$$
f (\bx) - f(\ba) \leq L \| \bx - \ba \|
$$
for every $\bx \in B[\ba, r]$.


1. Let $\bx \in B_d[\ba, r]$ (the deleted neighborhood).
1. Then, $\| \bx - \ba \| \leq r$ and $f(\bx) \leq M$. 
1. Let $\alpha = \frac{1}{r} \| \bx - \ba \|$. 
   Note that by definition $\alpha \leq 1$.
1. Define
   
   $$
   \by = \ba + \frac{1}{\alpha}(\bx - \ba).
   $$
1. Note that

   $$
   \| \by - \ba \| = r \frac{\| \bx - \ba \| }{\| \bx - \ba \|} = r.
   $$
1. Thus, $\by \in B[\ba, r]$. 
1. Hence $f(\by)\leq M$.
1. We can rewrite the above equation (defining $\by$) as

   $$
   \bx = \alpha \by + (1- \alpha) \ba.
   $$
1. Thus, $\bx$ is a convex combination of $\by, \ba$.
1. Then, by convexity,

   $$
   f(\bx) &\leq \alpha f(\by) + (1- \alpha) f(\ba)\\
   &= f(\ba) + \alpha (f(\bx) - f(\ba))\\
   &\leq  f(\ba) + \alpha (M - f(\ba))\\
   &= f(\ba) + \frac{1}{r} \| \bx - \ba \| (M - f(\ba)).
   $$
1. Consequently, 

   $$
   f(\bx) - f(\ba) \leq \frac{M - f(\ba)}{r} \| \bx - \ba \|.
   $$
1. Let $L = \frac{M - f(\ba)}{r}$.
1. Then, for every $\bx \in B[\ba, r]$, we have

   $$
   f(\bx) - f(\ba) \leq L \| \bx - \ba \|.
   $$


We next show that for this choice of $L$

$$
f (\ba) - f(\bx) \leq L \| \bx - \ba \|
$$
for every $\bx \in B[\ba, r]$.

1. Define

   $$
   \bz = \ba + \frac{1}{\alpha} (\ba - \bx).
   $$
1. It is easy to see that $\| \ba - \bz \| = r$.
1. Hence, $\bz \in B[\ba, r]$ and $f(\bz) \leq M$.
1. Rearranging, we have

   $$
   \bx = \ba + \alpha (\ba - \bz).
   $$
1. Now, note that:

   $$
   \ba = \frac{1}{1 + \alpha}(\ba + \alpha(\ba - \bz))
   + \frac{\alpha}{1 + \alpha} \bz.
   $$
1. Thus, $\ba$ is a convex combination of 
   $\bx = \ba + \alpha (\ba - \bz)$
   and $\bz$.
1. Also, both $\bx, \bz \in B[\ba, r]$.
1. Applying convexity,

   $$
   f(\ba) \leq \frac{1}{1 + \alpha} f(\bx) 
   + \frac{\alpha}{1 + \alpha} f(\bz).
   $$
1. Thus,

   $$
   (1 + \alpha)f(\ba) \leq f(\bx) + \alpha f(\bz).
   $$
1. Thus, 

   $$
   f(\bx) \geq (1 + \alpha)f(\ba) - \alpha f(\bz)
   = f(\ba) + \alpha (f(\ba) - f(\bz)).
   $$
1. Continuing from here

   $$
   f(\bx) &\geq f(\ba) + \alpha (f(\ba) - f(\bz))\\
   &\geq f(\ba) - \alpha (M - f(\ba))\\
   &= f(\ba) - \frac{M - f(\ba)}{r} \| \bx - \ba \|\\
   =  f(\ba) - L \| \bx - \ba \|.
   $$
1. Thus, $f(\ba) - f(\bx) \leq L \| \bx - \ba \|$.


Combining, we see that with $L = \frac{M - f(\ba)}{r}$,

$$
|f (\bx) - f(\ba)| \leq L \| \bx - \ba \|
$$
for every $\bx \in B[\ba, r]$.

Thus, $f$ is locally Lipschitz at every interior
point of $S = \dom f$.
```


### Continuity of Univariate Closed Convex Functions


```{prf:theorem} Continuity of closed convex univariate functions
:label: res-cvxf-convex-closed-univariate

Let $f: \RR \to \RERL$ be a proper closed and convex function.
Then, $f$ is continuous over $\dom f$.
```

```{prf:proof}
Since $f$ is convex, hence its domain is convex. Hence
$\dom f$ must be an interval $I$. 

1. If $\interior I = \EmptySet$, then $I$ must be a singleton.
1. In that case $f$ is continuous obviously.
1. Now consider the case where $\interior I \neq \EmptySet$.
1. Then, due to {prf:ref}`res-cvxf-convex-local-lipschitz-continuous`,
   $f$ is continuous at every $x \in \interior I$.
1. If $I$ is open (i.e., it has no endpoints), then there is
   nothing more to prove.
1. We are left with showing the (one sided) continuity of $f$
   at one of the endpoints of $I$ if it has any.
1. Since, the argument will be identical for either of the
   endpoints, without loss of generality, let us assume
   that $I$ has a left endpoint $a$ and we show the continuity
   from the right at $a$; i.e. $\lim_{x \to a^+} f(x) = f(a)$.
1. Pick any $c \in I$ such that $c > a$.
1. Define a function

   $$
   g(t) = \frac{f(c -t) - f(c)}{t}.
   $$
1. Clearly, $g$ is defined over $(0, c-a]$.
1. We shall show that $g$ is nondecreasing and upper bounded
   over $(0, c-a]$.
1. Pick any $t,s$ satisfying $0 < t \leq s \leq c-a$.
1. Then,

   $$
   c - t = \left (1 - \frac{t}{s} \right ) c + \frac{t}{s} (c - s).
   $$
1. $\frac{t}{s}$ is well defined and $\frac{t}{s} \in (0, 1]$.
1. Thus, $c-t$ is a convex combination of $c$ and $c-s$.
1. Since $f$ is convex, hence

   $$
   & f(c - t) \leq \left (1 - \frac{t}{s} \right ) f(c) + \frac{t}{s} f(c - s)\\
   & \iff f(c - t) - f(c) \leq \frac{t}{s} (f(c -s) - f(c)) \\
   &\iff \frac{f(c - t) - f(c)}{t} \leq \frac{f(c -s) - f(c)}{s}.
   $$
1. Thus,
   
   $$
   g(t) \leq g(s) \Forall 0 < t \leq s \leq c-a.
   $$
1. Thus, $g$ is nondecreasing over $(0, c-a]$.
1. Finally $g(c-a) = \frac{f(a) - f(c)}{c - a}$ is finite since both $c,a \in \dom f$.
1. Since $g$ is nondecreasing, hence

   $$
   g(t) \leq g(c -a) \Forall t \in (0, c-a].
   $$
1. Thus, $g$ is upper bounded.
1. Since $g$ is nondecreasing and upper bounded,
   hence due to {prf:ref}`res-bra-rf-monotonic-func-limits`,
   the left hand limit of $g(t)$ at $c-a$ exists and 
   is equal to some real number, say, 

   $$
   \lim_{t \to (c-a)^-} g(t) = \ell.
   $$
   Note that we haven't said that $g$ is continuous from the left at $c-a$.
1. Recall from the definition of $g$ that
   
   $$
   f(c-t) = f(c) + t g(t).
   $$
1. Hence

   $$
   \lim_{t \to (c-a)^-} f(c -t) = f(c) + (c-a) \ell.
   $$
1. Replacing $c-t$ by $r$, we get

   $$
   \lim_{r \to a^+} f(r) = f(c) + (c - a) \ell.
   $$
1. We have shown so far that the limit from the right at $a$ exists
   for $f$ and is equal to $f(c) + (c - a) \ell$.
1. Using the upper bound on $g$, we can say that
   
   $$
   f(c -t) 
   &= f(c) + t g(t) \\
   &\leq f(c) + (c-a) g(c-a) \\
   &= f(c) + f(a) - f(c) = f(a)
   $$
   holds true for every $t \in (0, c-a]$.
1. Thus,

   $$
   \lim_{r \to a^+} f(r) = \lim_{t \to (c-a)^-} f(c -t)  \leq f(a).
   $$
1. On the other hand, since $f$ is closed, hence it is also
   lower semicontinuous. This means that

   $$
   \lim_{r \to a^+} f(r)  \geq f(a).
   $$
1. Combining these two inequalities, we get

   $$
   \lim_{r \to a^+} f(r)  = f(a).
   $$
1. Thus, $f$ is indeed continuous from the right at $a$.
1. Similarly, if $I$ has a right endpoint $b$,
   then $f$ is continuous from the left at $b$.
1. Thus, $f$ is continuous at every point in its domain.
```


