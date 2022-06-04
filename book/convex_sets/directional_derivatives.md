# Directional Derivatives

This section deals with the subject of directional derivatives
for convex functions.

## Convex Real Functions

For real functions $f : \RR \to \RR$, several useful
results are available.

```{prf:remark} Domain of a convex real function
:label: rem-cvxf-rf-domain

The domain of a convex real function is an interval.
```

```{prf:proof}
Let $f: \RR \to \RR$ be convex. Then $\dom f$ is
convex. But every convex subset of real line
is an interval.
```

### Characterization

```{prf:theorem} Characterization of real convex functions
:label: res-cvxf-rf-convex-charac

Let $f: \RR \to \RR$ be a real function with $\dom f = (a,b)$
which is an open interval.
The following are equivalent.

1. $f$ is convex.
1. For every $x_1, x_2, x_3 \in (a, b)$ with $x_1 < x_2 < x_3$,

   $$
   \frac{f(x_2) - f(x_1)}{x_2 - x_1} \leq \frac{f(x_3) - f(x_1)}{x_3 - x_1}.
   $$
1. For every $x_1, x_2, x_3 \in (a, b)$ with $x_1 < x_2 < x_3$,

   $$
   \frac{f(x_2) - f(x_1)}{x_2 - x_1} \leq \frac{f(x_3) - f(x_2)}{x_3 - x_2}.
   $$
1. For every $x_1, x_2, x_3 \in (a, b)$ with $x_1 < x_2 < x_3$,

   $$
   \frac{f(x_3) - f(x_1)}{x_3 - x_1} \leq \frac{f(x_3) - f(x_2)}{x_3 - x_2}.
   $$
```


```{prf:proof}

(1) $\implies$ (2) 
Assume that $f$ is convex.

1. Let 

   $$
   \alpha = \frac{x_3 - x_2}{x_3 - x_1}, 
   \beta = \frac{x_2 - x_1}{x_3 - x_1}.
   $$
1. Then, $\alpha + \beta = 1$ and $\alpha , \beta \in (0,1)$.
1. Also, verify that

   $$
   x_2 = \alpha x_1 + \beta x_3.
   $$
1. Thus,

   $$
   & f(x_2) \leq \alpha f(x_1) + \beta f(x_3) \\
   & \iff f(x_2) \leq \frac{x_3 - x_2}{x_3 - x_1} f(x_1)
   + \frac{x_2 - x_1}{x_3 - x_1} f(x_3)\\
   & \iff (x_3 - x_1) f(x_2) \leq (x_3 - x_2) f(x_1)
      + (x_2 - x_1) f(x_3)\\
   & \iff (x_3 - x_1) f(x_2) \leq ((x_3 - x_1) - (x_2 - x_1)) f(x_1)
      + (x_2 - x_1) f(x_3)\\
   & \iff (x_3 - x_1) (f(x_2) - f(x_1)) \leq
    (x_2 - x_1) (f(x_3) - f(x_1))\\
   & \iff \frac{f(x_2) - f(x_1)}{x_2 - x_1} \leq \frac{f(x_3) - f(x_1)}{x_3 - x_1}. 
   $$

(2) $\implies$ (1)

1. Let $x_1, x_3 \in (a, b)$ and $t \in (0, 1)$.
1. WLOG, assume that $x_1 < x_3$.
1. Let $\alpha = t$ and $\beta = (1-t)$.
1. Let $x_2 =  \alpha x_1 + \beta x_3$.
1. Then, $x_1 < x_2 < x_3$.
1. From the hypothesis, we have

   $$
   \frac{f(x_2) - f(x_1)}{x_2 - x_1} \leq \frac{f(x_3) - f(x_1)}{x_3 - x_1}.
   $$
1. Using the previous argument backwards, this implies

   $$
   f(x_2) \leq \alpha f(x_1) + \beta f(x_3) = t f(x_1) + (1-t) f(x_3).
   $$
1. Thus, $f$ is convex.


(2) $\iff$ (3)

1. Pick any $x_1, x_2, x_3 \in (a, b)$ with $x_1 < x_2 < x_3$.
1. By hypothesis (2)

   $$
   & \frac{f(x_2) - f(x_1)}{x_2 - x_1} \leq \frac{f(x_3) - f(x_1)}{x_3 - x_1} \\
   \iff & (x_3 - x_1) (f(x_2) - f(x_1)) \leq
    (x_2 - x_1) (f(x_3) - f(x_1))\\
   \iff & (x_3 - x_1) f(x_2) \leq ((x_3 - x_1) - (x_2 - x_1)) f(x_1)
      + (x_2 - x_1) f(x_3)\\
   \iff & ((x_3 - x_2) + (x_2 - x_1) ) f(x_2) \leq ((x_3 - x_2) f(x_1)
      + (x_2 - x_1) f(x_3)\\
   \iff & (x_3 - x_2) (f(x_2) - f(x_1)) \leq
      (x_2 - x_1) (f(x_3) - f(x_2))\\
   \iff & \frac{f(x_2) - f(x_1)}{x_2 - x_1 } \leq \frac{f(x_3) - f(x_2)}{x_3 - x_2}.
   $$

(2) $\iff$ (4)

1. Pick any $x_1, x_2, x_3 \in (a, b)$ with $x_1 < x_2 < x_3$.
1. By hypothesis (2)

   $$
   & \frac{f(x_2) - f(x_1)}{x_2 - x_1} \leq \frac{f(x_3) - f(x_1)}{x_3 - x_1} \\
   \iff & (x_3 - x_1) (f(x_2) - f(x_1)) \leq
    (x_2 - x_1) (f(x_3) - f(x_1))\\
   \iff & (x_3 - x_1) f(x_2) \leq (x_3 - x_2) f(x_1)
      + ((x_2 - x_3) + (x_3 - x_1)) f(x_3)\\
   \iff & (x_3 - x_1) (f(x_2) - f(x_3)) \leq (x_3 - x_2) (f(x_1) - f(x_3)) \\
   \iff & (x_3 - x_1) (f(x_3) - f(x_2)) \geq (x_3 - x_2) (f(x_3) - f(x_1)) \\
   \iff & (x_3 - x_2) (f(x_3) - f(x_1)) \leq  (x_3 - x_1) (f(x_3) - f(x_2))\\
   \iff & \frac{f(x_3) - f(x_1)}{x_3 - x_1} \leq \frac{f(x_3) - f(x_2)} {x_3 - x_2}.
   $$
```

The previous result is limited to real convex functions with
an open interval as domain. We can say something about
all real convex functions.

```{prf:theorem} Slopes of intercepts on a real convex function
:label: res-cvxf-rf-slope-intercept

Let $f: \RR \to \RR$ be a real convex function with $I = \dom f$.
Let $x, y, z \in I$ such that $x < y < z$.
Then

$$
\frac{f(y) - f(x)}{y - x} \leq \frac{f(z) - f(x)}{z - x} 
\leq \frac{f(z) - f(y)}{z - y}.
$$
```
```{prf:proof}
The proof is similar to the proof of {prf:ref}`res-cvxf-rf-convex-charac`.
```


### One Sided Derivatives

Recall from {prf:ref}`def-bra-df-one-sided-derivative` that
if $f$ is defined over $[a,b)$, then the
*right hand derivative* is defined as:

$$
f'_+(a) = \lim_{x \to a^+} \frac{f(x) - f(a)}{x - a}
$$
if the limit exists.
Similarly, if $f$ is defined over $(c,a]$, then the
*left hand derivative* is defined as:

$$
f'_-(a) = \lim_{x \to a^-} \frac{f(x) - f(a)}{x - a}
$$
if the limit exists.

An interesting property of convex functions is that
the one sided derivatives always exist.
On the real line, there are only two directions
to move; left and right. The one sided derivatives
play the role of directional derivatives on the
real line.

```{prf:theorem} Real convex functions and one sided derivatives
:label: res-cvxf-rf-convex-osd

Let $f: \RR \to \RR$ with $\dom f = I$ be convex.
Then, for every $x \in \interior I$, the left hand derivative
$f'_-(x)$ and the right hand derivative $f'_+(x)$ exist.

If $a = \inf I \in I$, then the right hand derivative
$f'_-(a)$ exists.
If $b = \sup I \in I$, then the left hand derivative
$f'_+(b)$ exists.
``` 


```{prf:proof}
We are given that $f$ is convex over $(a,b)$.

1. Let $x \in \interior I$.
1. Then there exists $r > 0$ such that $(x - r, x + r) \subseteq I$.
1. For $h > 0$, define

   $$
   F(h) = \frac{f(x + h) - f(x)}{h}.
   $$
1. Let $0 < h_1 < h_2$ such that $h_2 < r$.
1. Let $x_1 = x$, $x_2 = x + h_1$, $x_3 = x + h_2$.
1. Since $f$ is convex, hence by {prf:ref}`res-cvxf-rf-slope-intercept`

   $$
   \frac{f(x_2) - f(x_1)}{x_2 - x_1} \leq \frac{f(x_3) - f(x_1)}{x_3 - x_1}.
   $$
1. But that means 

  $$
  \frac{f(x + h_1) - f(x)}{h_1} \leq \frac{f(x + h_2) - f(x)}{h_2}.
  $$
1. Thus, whenever $h_1 < h_2$ (up to $h_2 < r$),
   $F(h_1) \leq F(h_2)$.
1. Thus, $F$ is a nondecreasing (monotone) function of $h$
   in some interval $(0, \delta)$ where $\delta < r$.
1. Then, $f'_+(x) = \lim_{h \to 0^+} F(h)$ exists.

A similar argument shows that $f'_-(x)$ also exists.
Similar arguments apply for the one sided derivatives
at the end points.
```

### Continuity

```{prf:theorem} Convex real function is continuous
:label: res-cvxf-rf-open-domain-continuous


Let $f: \RR \to \RR$ with $\dom f = (a,b)$ be convex.
Then, for every $x \in (a,b)$, 
Then, $f$ is continuous on $(a,b)$.
```

```{prf:proof}
We proceed as follows.

1. Let $x \in (a,b)$.
1. By {prf:ref}`res-cvxf-rf-convex-osd`, 
   the one sided derivatives $f'_+(x)$ and $f'_-(x)$ exist.
1. Then, by limit arithmetic

   $$
   \lim_{h \to 0^-} (f(x + h) - f(x)) 
   = \left ( \lim_{h \to 0^-} \frac{f(x + h) - f(x)}{h} \right )
   \left ( \lim_{h \to 0^-} h \right) = 0.
   $$
1. Similarly, 

   $$
   \lim_{h \to 0^+} (f(x + h) - f(x)) 
   = \left ( \lim_{h \to 0^+} \frac{f(x + h) - f(x)}{h} \right )
   \left ( \lim_{h \to 0^+} h \right) = 0.
   $$
1. Thus, 

   $$
   \lim_{h \to 0^-} (f(x + h) - f(x)) 
   = \lim_{h \to 0^+} (f(x + h) - f(x)) = 0.
   $$
1. Thus, $f$ is continuous at $x$.
1. Since $x$ was arbitrary, hence $f$ is continuous on $(a,b)$.
```

## Proper Functions

### Directional Derivative

```{prf:definition} Directional derivative
:label: def-cvxf-directional-derivative

Let $f : \VV \to \RERL$ be a proper function
with $S = \dom f$.
Let $\bx \in \interior S$. 
The *directional derivative* at $\bx$ in the direction $\bd \in \VV$ is defined by 

$$
f'(\bx;\bd) \triangleq \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha \bd) - f(\bx)}{\alpha}.
$$
```

```{div}
The directional derivative is a scalar quantity ($\in \RR$).
When we say that 

$$
f'(\bx;\bd) = \lim_{t \to 0^+} \frac{f(\bx + t \bd) - f(\bx)}{t},
$$

we mean that $f$ is defined over a set
$\{ \bv \ST \bv = \bx + t \bd, 0 < t < t_{\max} \}$
and for every $\epsilon > 0$, there exists
$\delta > 0$ such that

$$
\left | \frac{f(\bx + t \bd) - f(\bx)}{t} - f'(\bx;\bd) \right | < \epsilon
\text{ whenever }
0 < t < \delta.
$$

Since $\bx \in \interior S$, hence there exists $r > 0$
such that $B(\bx, r) \subseteq S$.

With $\bv \in B(\bx, r)$, we need $\| t \bd \| < r$.
Thus, a $t_{\max} = \frac{r}{\| \bd \|}$ is a suitable
range of allowed values for $t$.
Accordingly, $0 < \delta < t_{\max}$ can be chosen.
```

```{prf:remark} Directional derivative for zero vector
:label: rem-cvxf-dir-der-zero

If $\bd = \bzero$ then, $f'(\bx; \bd) = 0$.

We can see this from the fact that

$$
f'(\bx;\bzero) = \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha \bzero) - f(\bx)}{\alpha} = 0.
$$
```

A useful result is for computing the directional derivative of a function
which is the pointwise maximum of a finite number of proper functions.

We recall from {prf:ref}`res-ms-int-intersect-int` that
the interior of a finite intersection of sets is the 
intersection of their interiors. This is useful in
identifying the interior of the domain for a pointwise
maximum of a finite set of functions. 


### Pointwise Maximum of Finite Set of Functions

```{prf:theorem} Directional derivative of a maximum of functions
:label: res-cvxf-dir-der-max-funcs

Let $f_1, f_2, \dots, f_m : \VV \to \RERL$ be proper functions.
Let $f : \VV \to \RERL$ be defined as

$$
f(\bx) = \max\{f_1(\bx), \dots, f_m(\bx) \}
$$
with $\dom f = \bigcap_{i=1}^m \dom f_i$.

Let $\bx \in \interior \dom f = \bigcap_{i=1}^m \interior \dom f_i$
and $\bd \in \VV$.
Assume that $f'(\bx; \bd)$ exists for every $i \in 1,\dots,m$.

Let $I(\bx) = \{i \in 1,\dots,m \ST f_i(\bx) = f(\bx) \}$ be the set
of indices of functions whose value at $\bx$ equals $f(\bx)$.
Then,

$$
f'(\bx; \bd) = \underset{i \in I(\bx)}{\max} f'(\bx; \bd).
$$

In other words, the directional derivative of a pointwise maximum
of functions equals the maximum of directional directives of functions
which attain the pointwise maximum at a specific point.
```

```{prf:proof}
The key idea here is that for computing the
directional derivative $f'(\bx; \bd)$, 
only those functions are relevant for which
$f_i(\bx) = f(\bx)$. We need to show this first.

1. Since $\bx \in \interior \dom f$, there
   exists $B(\bx, r)$ such that
   $f$ and $f_i$ are all defined over this open ball.
1. Let $s = \frac{r}{\| \bd \|}$.
1. For every $i \in 1,\dots,m$, 
   let $g_i : \RR \to \RR$ be defined as 

   $$
   g_i(t) = f_i(\bx + t \bd)
   $$
   with $\dom g_i = [0, s)$.
   $\| s \bd \| = r$. Thus, $\bx + t \bd \in B(\bx, r)$.
   Hence, $g_i$ are well defined.
1. Then,

   $$
   \lim_{t \to 0+} g_i(t) 
   &= \lim_{t \to 0+} f_i(\bx + t \bd) \\
   &= \lim_{t \to 0+} [(f_i(\bx + t \bd) - f_i(\bx)) + f_i(\bx)]\\
   &= \lim_{t \to 0+}\left [
   t \frac{f_i(\bx + t \bd) - f_i(\bx)}{t} + f_i(\bx) 
   \right] \\
   &= 0 \cdot f'_i(\bx; \bd) + f_i(\bx)\\
   &= f_i(\bx) = g_i(0).
   $$
   We used the fact that $f'_i(\bx; \bd)$ exists
   for every $f_i$.
1. Thus, $g_i$ is continuous from the right at $t=0$
   for every $i \in 1,\dots, m$.
1. Let $i \in I(\bx)$ and $j \notin I(\bx)$.
1. Then, $f_i(\bx) > f_j (\bx)$. Alternatively $g_i(0) > g_j(0)$.
1. Since $g_i, g_j$ are continuous from the right, hence
   there exists $\epsilon_{i j} > 0$ such that
   $g_i(t) > g_j(t)$ for every $t \in [0, \epsilon_{i j}]$.
1. Minimizing $\epsilon_{ij}$ over all pairs of 
   $i \in I(\bx)$ and $j \notin I(\bx)$,
   there exists $\epsilon > 0$ such that
   for any $i \in I(\bx)$ and $j \notin I(\bx)$,

   $$
   f_i(\bx + t \bd) = g_i(t) > g_j(t) = f_j(\bx + t \bd) 
   \Forall t \in [0, \epsilon].
   $$

We can now compute the directional derivative.

1. For every $t \in [0, \epsilon]$, 

   $$
   f(\bx + t \bd) = \underset{i=1,\dots,m}{\max} f_i(\bx + t \bd)
   = \underset{i \in I(\bx)}{\max} f_i(\bx + t \bd).
   $$
1. Consequently, for any $t \in (0, \epsilon]$

   $$
   \frac{f(\bx + t \bd) - f(\bx)}{t}
   &= \frac{\underset{i \in I(\bx)}{\max} f_i(\bx + t \bd) - f(\bx)}{t}\\
   &= \frac{\underset{i \in I(\bx)}{\max} (f_i(\bx + t \bd) - f_i(\bx))}{t}\\
   &= \underset{i \in I(\bx)}{\max} \frac{f_i(\bx + t \bd) - f_i(\bx)}{t}.
   $$
   We used the fact that $f_i(\bx) = f(\bx)$ for every $i \in I(\bx)$.
1. Taking the limit $t \to 0^+$,

   $$
   f'(\bx; \bd) 
   &= \lim_{t \to 0^+} \frac{f(\bx + t \bd) - f(\bx)}{t}\\
   &= \lim_{t \to 0^+} \underset{i \in I(\bx)}{\max} \frac{f_i(\bx + t \bd) - f_i(\bx)}{t}\\
   &= \underset{i \in I(\bx)}{\max} \lim_{t \to 0^+} \frac{f_i(\bx + t \bd) - f_i(\bx)}{t}\\
   &= \underset{i \in I(\bx)}{\max} f'_i(\bx; \bd).
   $$
```



## Proper Convex Functions

### Existence of Directional Derivatives

```{prf:theorem} Existence of directional derivatives for convex functions.
:label: res-cvxf-dir-der-exist-convex

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $\bx \in \interior S$. 
Then, for any $\bd \in \VV$, 
the directional derivative $f'(\bx; \bd)$ exists.
```

This allows us to consider a mapping from a direction $\bd \in \VV$
to the directional derivative of $f$ in this direction at $\bx$.
We can define a directional derivative map
parameterized by $\bx \in S$ as:

$$
\bg_x(\bd) \triangleq f'(\bx; \bd) = 
\lim_{\alpha \to 0^+} \frac{f(\bx + \alpha \bd) - f(\bx)}{\alpha}.
$$
We shall refer to such maps by $\bd \mapsto f'(\bx; \bd)$.

```{prf:theorem} Convexity and homogeneity of $\bd \mapsto f'(\bx; \bd)$
:label: res-cvxf-dir-der-convex-homo

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $\bx \in \interior S$.
Then, the function $\bd \mapsto f'(\bx; \bd)$ is convex and nonnegative
homogeneous. 

Nonnegative homogeneity: For any $t \geq 0$ and $\bd \in \VV$,

$$
f'(\bx; t \bd) = t f'(\bx; \bd).
$$
```

```{prf:proof}
Convexity

1. Let $\bd_1, \bd_2 \in \VV$ and $t \in (0, 1)$.
1. Let $\bd = t \bd_1 + (1-t) \bd_2$.
1. Then,
   
   $$
   f'(\bx; \bd) &= f'(\bx; t \bd_1 + (1-t) \bd_2)\\
   &= \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha [t \bd_1 + (1-t) \bd_2]) - f(\bx)}{\alpha}\\
   &= \lim_{\alpha \to 0^+} 
   \frac{f(t \bx + \alpha t \bd_1 + (1-t) \bx + \alpha (1-t) \bd_2) - f(\bx)}{\alpha}\\
   &= \lim_{\alpha \to 0^+} 
   \frac{f(t (\bx + \alpha \bd_1) + (1-t) (\bx + \alpha \bd_2)) - f(\bx)}{\alpha}\\
   &\leq \lim_{\alpha \to 0^+} 
   \frac{t f(\bx + \alpha \bd_1) + (1-t) f(\bx + \alpha \bd_2) - t f(\bx) - (1-t)f(\bx)}{\alpha}\\
   &= t \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha \bd_1) - f(\bx)}{\alpha} +
   (1-t) \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha \bd_2) - f(\bx)}{\alpha}\\
   &= t f'(\bx; \bd_1) + (1-t) f'(\bx; \bd_2).
   $$
   We used the convexity property of $f$ in this derivation.
1. Thus, $f'(\bx; \bd)$ is convex.

Nonnegative homogeneity

1. For $t=0$,

   $$
   f'(\bx, 0 \bd) = f'(\bx, \bzero) = 0 = 0 f'(\bx; \bd).
   $$
   Thus, the homogeneity property is trivial for $t=0$.
1. Now consider $t > 0$.
1. Then, 

   $$
   f'(\bx; t \bd) &= \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha t \bd) - f(\bx)}{\alpha}\\
   &= t \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha t \bd) - f(\bx)}{\alpha t}\\
   &= t f'(\bx; \bd).
   $$
1. Thus, $f'(\bx; \bd)$ is nonnegative homogeneous.
```

Directional derivatives are a linear underestimator for convex functions.

### As Linear Underestimator

```{prf:theorem} Directional derivative as linear underestimator
:label: res-cvxf-dir-der-underestimator

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $\bx \in \interior S$.
Then, for every $\by \in S$

$$
f(\by) \geq f(\bx) + f'(\bx; \by - \bx).
$$
```

```{prf:proof}
Note that

$$
f'(\bx; \by - \bx) 
&= \lim_{\alpha \to 0^+} \frac{f(\bx + \alpha (\by - \bx)) - f(\bx)}{\alpha}\\
&= \lim_{\alpha \to 0^+} \frac{f((1-\alpha) \bx + \alpha \by) - f(\bx)}{\alpha}\\
&\leq \lim_{\alpha \to 0^+} \frac{(1-\alpha)f(\bx) + \alpha f(\by) - f(\bx)}{\alpha}\\
&= \lim_{\alpha \to 0^+} \frac{\alpha (f(\by) - f(\bx))}{\alpha}\\
&= \lim_{\alpha \to 0^+}(f(\by) - f(\bx)) = f(\by) - f(\bx).
$$

Thus,

$$
f(\by) \geq f(\bx) + f'(\bx; \by - \bx).
$$
```

### Pointwise Maximum of Finite Set of Convex Functions

```{prf:theorem} Directional derivative of pointwise maximum of convex functions
:label: res-cvxf-dir-der-max-convex-funcs

Let $f_1, f_2, \dots, f_m : \VV \to \RERL$ be proper convex functions.
Let $f : \VV \to \RERL$ be defined as

$$
f(\bx) = \max\{f_1(\bx), \dots, f_m(\bx) \}
$$
with $\dom f = \bigcap_{i=1}^m \dom f_i$.

Let $\bx \in \interior \dom f$ and $\bd \in \VV$.
Then,

$$
f'(\bx; \bd) = \underset{i \in I(\bx)}{\max} f'(\bx; \bd).
$$
where $I(\bx) = \{i \in 1,\dots,m \ST f_i(\bx) = f(\bx) \}$.
```

```{prf:proof}
Since $f_i$ are proper convex, hence their pointwise maximum $f$ is proper convex.

By {prf:ref}`res-cvxf-dir-der-exist-convex`,
the directional derivatives $f'(\bx; \bd)$ and
$f'_i(\bx; \bd)$ for $i=1,\dots,m$ exist.

By {prf:ref}`res-cvxf-dir-der-max-funcs`,

$$
f'(\bx; \bd) = \underset{i \in I(\bx)}{\max} f'(\bx; \bd).
$$
where $I(\bx) = \{i \in 1,\dots,m \ST f_i(\bx) = f(\bx) \}$.
```
