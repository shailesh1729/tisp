# Directional Derivatives

This section deals with the subject of directional derivatives
for convex functions.

## Convex Real Functions

For real functions $f : \RR \to \RR$, several useful
results are available.

```{prf:remark} Domain of a convex real function
:label: rem-cvxf-rf-domain

The domain of a convex real function is an interval.

Let $f: \RR \to \RR$ be convex. Then $\dom f$ is
convex. But every convex subset of real line
is an interval.

1. Now let $I = \dom f$ be an interval.
1. We say $a  = \inf I$ as the left end point of $I$.
1. We say $b  = \sup I$ as the right end point of $I$.
1. $a$ and $b$ may or may not belong to $I$.
1. If both $a$ and $b$ belong to $I$, then $I$ is a closed interval.
1. If neither $a$ nor $b$ belongs to $I$, then $I$ is an open interval.
```



### Characterization

```{prf:theorem} Characterization of real convex functions
:label: res-cvxf-rf-convex-charac

Let $f: \RR \to \RR$ be a real function with $\dom f = I$
which is an interval (closed or open or semi-open).
Let $a$ and $b$ be the left and right endpoints of the interval $I$.

The following are equivalent.

1. $f$ is convex over $I$.
1. For every $x_1, x_2, x_3 \in I$ with $x_1 < x_2 < x_3$,

   $$
   \frac{f(x_2) - f(x_1)}{x_2 - x_1} \leq \frac{f(x_3) - f(x_1)}{x_3 - x_1}.
   $$
1. For every $x_1, x_2, x_3 \in I$ with $x_1 < x_2 < x_3$,

   $$
   \frac{f(x_2) - f(x_1)}{x_2 - x_1} \leq \frac{f(x_3) - f(x_2)}{x_3 - x_2}.
   $$
1. For every $x_1, x_2, x_3 \in I$ with $x_1 < x_2 < x_3$,

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

1. Let $x_1, x_3 \in I$ and $t \in (0, 1)$.
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

1. Pick any $x_1, x_2, x_3 \in I$ with $x_1 < x_2 < x_3$.
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

1. Pick any $x_1, x_2, x_3 \in I$ with $x_1 < x_2 < x_3$.
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

### One Sided Derivatives

Recall from {prf:ref}`def-bra-df-one-sided-derivative` that
if $f$ is defined over $[a,b)$, then the
*right hand derivative* is defined as:

$$
f'_+(a) = \lim_{x \to a^+} \frac{f(x) - f(a)}{x - a}
= \lim_{h \downarrow 0} \frac{f(a + h) - f(a)}{h}
$$
if the limit exists.
Similarly, if $f$ is defined over $(c,a]$, then the
*left hand derivative* is defined as:

$$
f'_-(a) = \lim_{x \to a^-} \frac{f(x) - f(a)}{x - a}
= \lim_{h \uparrow 0} \frac{f(a + h) - f(a)}{h}
= \lim_{r \downarrow 0} \frac{f(a) - f(a - r)}{r}
$$
if the limit exists.


We introduce two helper functions

$$
s_+(x, h) = \frac{f(x + h) - f(x)}{h}
$$
and

$$
s_-(x, h) = \frac{f(x) - f(x-h)}{h}
$$
where $h > 0$.

Then

$$
f'_+(x) = \lim_{h \downarrow 0} s_+(x, h)
$$
and

$$
f'_-(x) = \lim_{h \downarrow 0} s_-(x, h).
$$

An interesting property of convex functions is that
the one sided derivatives always exist.
On the real line, there are only two directions
to move; left and right. The one sided derivatives
play the role of directional derivatives on the
real line.

```{prf:lemma} Monotonicity of $s_+$ and $s_-$ for convex functions
:label: res-cvxf-rf-s-monotonic

Let $f: \RR \to \RR$ with $\dom f = I$ be convex.
Let $a$ and $b$ be the
left and right endpoints of the interval $I$.
Then $s_+$ and $s_-$ as functions of $h$ are monotonic.

1. $s_+(x, h)$ is a nondecreasing function of $h$.
1. $s_-(x, h)$ is a nonincreasing function of $h$.
```

```{prf:proof}
Monotonicity of $s_+$.

1. Let $x \in I$ such that $x \neq b$.
1. Let $h_1, h_2 > 0$ such that $h_1 < h_2$ and $x + h_2 \in I$.
1. Consider the three points $x < x + h_1 < x + h_2$.
1. Then 

   $$
   \frac{f(x+h_1) - f(x)}{h_1} \leq \frac{f(x+h_2) - f(x)}{h_2}.
   $$
1. Hence $s_+(x, h_1) \leq s_+(x, h_2)$.
1. Hence $s_+$ is a nondecreasing function of $h$.

The argument for monotonicity of $s_-$ is similar.
```

```{prf:observation} One sided derivatives as infimum/supremum
:label: res-cvxf-rf-one-sided-derivative-inf-sup

Due to the monotonicity of $s_+$ over $h$, we have

$$
f'_+(x) = \lim_{h \downarrow 0} s_+(x, h)
= \inf_{h > 0}s_+(x, h).
$$

Similarly, due to the monotonicity of $s_+$ over $h$, we have

$$
f'_-(x) = \lim_{h \downarrow 0} s_-(x, h)
= \sup_{h > 0}s_-(x, h).
$$
```

```{prf:theorem} Real convex functions and one sided derivatives
:label: res-cvxf-rf-convex-osd

Let $f: \RR \to \RR$ with $\dom f = I$ be convex.
Let $a$ and $b$ be the
left and right endpoints of the interval $I$.
Then, for every $x \in \interior I = (a,b)$, the left hand derivative
$f'_-(x)$ and the right hand derivative $f'_+(x)$ exist.

If $a \in I$, then the right hand derivative
$f'_+(a)$ exists.
If $b \in I$, then the left hand derivative
$f'_-(b)$ exists.

If $a \in I$, we define $f'_-(a) = -\infty$.
If $b \in I$, we define $f'_+(b) = \infty$.
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
1. Since $f$ is convex, hence by {prf:ref}`res-cvxf-rf-convex-charac`

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
1. Then, $f'_+(x) = \lim_{h \downarrow 0} F(h)$ exists.

A similar argument shows that $f'_-(x)$ also exists.
Similar arguments apply for the one sided derivatives
at the end points.
```

### Continuity

```{prf:theorem} Convex real function is continuous
:label: res-cvxf-rf-open-domain-continuous


Let $f: \RR \to \RR$ be a real convex function
with $\dom f = I$. Let $a$ and $b$ be the
left and right endpoints of the interval $I$.
Then,
1. $f$ is continuous at every $x \in (a,b)$.
1. If $a \in I$, then $f$ is continuous from the right at $a$.
1. If $b \in I$, then $f$ is continuous from the left at $b$.

In other words, $f$ is continuous on $I$.
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
   \lim_{h \downarrow 0} (f(x + h) - f(x)) 
   = \left ( \lim_{h \downarrow 0} \frac{f(x + h) - f(x)}{h} \right )
   \left ( \lim_{h \downarrow 0} h \right) = 0.
   $$
1. Thus, 

   $$
   \lim_{h \to 0^-} (f(x + h) - f(x)) 
   = \lim_{h \downarrow 0} (f(x + h) - f(x)) = 0.
   $$
1. Thus, $f$ is continuous at $x$.
1. Since $x$ was arbitrary, hence $f$ is continuous on $(a,b)$.

Now consider the case where $a \in I$.

1. By {prf:ref}`res-cvxf-rf-convex-osd`, 
   the one sided derivative $f'_+(a)$ exists.
1. Then, by limit arithmetic

   $$
   \lim_{h \to 0^-} (f(a + h) - f(a)) 
   = \left ( \lim_{h \to 0^-} \frac{f(a + h) - f(a)}{h} \right )
   \left ( \lim_{h \to 0^-} h \right) = 0.
   $$
1. Hence $f$ is continuous from the right at $a$.

A similar argument holds for continuity from the left at $b$.
```


### Properties of One Sides Derivatives

```{prf:theorem} Properties of one-sided derivatives
:label: res-cvxf-rf-one-sided-der-props

Let $f: \RR \to \RR$ be a real convex function
with $\dom f = I$. Let $a$ and $b$ be the
left and right endpoints of the interval $I$.

1. We have $f'_-(x) \leq f'_+(x)$ for every $x \in I$.
1. If $x \in \interior I$ then both
   $f'_-(x)$ and $f'_+(x)$ are finite.
1. If $x, z \in I$ and $x < z$, then $f'_+(x) \leq f'_-(z)$.
1. The functions $f'_-, f'_+ : \RR \to \ERL$ are nondecreasing over $I$.
1. The function $f'_+$ is right-continuous at every interior point of $I$.
   If $a \in I$ then $f'_+$ is right-continuous at $a$.
1. The function $f'_-$ is left-continuous at every interior point of $I$.
   If $b \in I$ then $f'_-$ is left-continuous at $b$.
1. The function $f'_+$ is upper-semicontinuous at every $x \in I$.
1. The function $f'_-$ is lower-semicontinuous at every $x \in I$.
```

```{prf:proof}
(1)

1. If $a \in I$, then by convention $f'_-(a) = -\infty$. Hence $f'_-(a) \leq f'_+(a)$.
1. If $b \in I$, then by convention $f'_+(b) = \infty$. Hence $f'_-(b) \leq f'_+(b)$.
1. Now let $x \in \interior I$.
1. Then there is $r > 0$ such that $(x-r, x+r) \in I$.
1. Pick any $h > 0$ such that $h < r$.
1. Then, using the three points $x - h, x, x + h$, we have

   $$
   \frac{f(x) - f(x - h)}{h} \leq \frac{f(x + h) - f(x)}{h}
   $$
   due to {prf:ref}`res-cvxf-rf-convex-charac`.
1. Taking the limit $h \downarrow 0$, we see that

   $$
   f'_-(x) \leq f'_+(x)
   $$
   holds true for every $x \in \interior I$.

(2)
1. Let $x \in \interior I$.
1. Let $h > 0$ such that $(x - h, x + h) \subseteq I$.
1. Then we have

   $$
   f'_+(x) \leq \frac{f(x+h) - f(x)}{h} < \infty.
   $$
1. Similarly, we have

   $$
   - \infty < \frac{f(x) - f(x -h)}{h} \leq f'_-(x).
   $$
1. By (1), we have

   $$
   -\infty < f'_-(x) \leq f'_+(x) < \infty.
   $$
1. Hence both are finite at interior points of $I$.

(3)
1. Let $y = \frac{x + z}{2}$.
1. Due to {prf:ref}`res-cvxf-rf-convex-charac`, we have

   $$
   \frac{f(y) - f(x)}{y - x} \leq \frac{f(z) - f(y)}{z - y}.
   $$
1. We also have

   $$
   f'_+(x) \leq \frac{f(y) - f(x)}{y - x}
   \text{ and }
   \frac{f(z) - f(y)}{z - y} \leq f'_-(z).
   $$
1. Combining, we get $f'_+(x)  \leq f'_-(z)$.

(4)
1. Let $x, z \in I$ such that $x < z$.
1. From (3), we have $f'_+(x)  \leq f'_-(z)$.
1. From (1), we have $f'_-(z) \leq f'_+(z)$.
1. Combining, we have $f'_+(x) \leq f'_+(z)$.
1. Hence $f'_+$ is nondecreasing.
1. Similarly, $f'_-(x) \leq f'_+(x) \leq f'_-(z)$.
1. Hence $f'_-$ is nondecreasing.

(5)

1. Pick any $x \in I$ such that $x \neq b$ (if $b \in I$).
1. Then $x < b$.
1. We can pick $h > 0$ and $r > 0$ such that
   $x + h + r < b$.
1. Then $f'_+(x + h) \leq \frac{f(x + h + r) - f(x + h)}{r}$.
1. We established in {prf:ref}`res-cvxf-rf-open-domain-continuous`
   that $f$ is continuous.
1. Taking the limit $h \downarrow 0$, we obtain

   $$
   \lim_{h \downarrow 0} f'_+(x + h) \leq \frac{f(x + r) - f(x)}{r}.
   $$
   This is valid since $f$ is continuous.
1. Now taking the limit $r \downarrow 0$ on the R.H.S., we obtain

   $$
   \lim_{h \downarrow 0} f'_+(x + h) \leq f'_+(x).
   $$
1. Since $f'_+$ is nondecreasing by claim (4), hence

   $$
   f'_+(x) \leq \lim_{h \downarrow 0} f'_+(x + h).
   $$
1. Together, we must have

   $$
   f'_+(x) = \lim_{h \downarrow 0} f'_+(x + h).
   $$
1. Hence $f'_+$ is right continuous at $x$.

(6)
1. An argument similar to (5) shows that $f'_-$ is 
   left continuous at every $x \in I$ except for $x=a$
   (if $a \in I$).


(7) Upper semicontinuity of $f'_+$

1. We need to show that for every $\epsilon > 0$
   there exists $r > 0$ such that

    $$
    f'_+(y) < f'_+(x) + \epsilon \text{ for every } y \in (x-r, x+r) \cap I.
    $$
1. Pick some $\epsilon > 0$.
1. Consider any $x \in \interior I$.
1. By (6) $f'_+$ is right continuous at $x$.
1. Hence there exists $r_1 > 0$ such that for every $y \in [x, x+r_1)$,
   we have
   
   $$
   |f'_+(y) - f'_+(x)| < \epsilon.
   $$
1. By (4), $f'_+$ is nondecreasing.
   Hence for every $y \in [x, x+r_1)$

   $$
   |f'_+(y) - f'_+(x)| = f'_+(y) -  f'_+(x).
   $$
1. Hence for every $y \in [x, x+r_1)$, we have
   
   $$
   f'_+(y) -  f'_+(x) < \epsilon
   \iff f'_+(y) < f'_+(x) + \epsilon.
   $$
1. Now, let $r = \min(x - a, r_1)$.
1. By monotonicity of $f'_+$, for every $y \in (x - r, x)$

   $$
   f'_+(y) \leq f'_+(x).
   $$
1. Hence for every $y \in (x, -r, x)$

   $$
   f'_+(y) < f'_+(x) + \epsilon.
   $$
1. Combining the two, for every $y \in (x - r, x + r)$, we have

   $$
   f'_+(y) < f'_+(x) + \epsilon.
   $$
1. Hence $f'_+$ is u.s.c. at $x$.
1. Now, if $a \in I$ then let $x = a$.
1. By right continuity of $f'_+$ at $a$, 
   there exists $r > 0$ such that
   for every $y \in [a, a + r)$, we have

   $$
   f'_+(y) < f'_+(a) + \epsilon.
   $$
1. Also $(a - r, a + r) \cap I = [a, a + r)$.
1. Hence $f'_+$ is u.s.c. at $a$.
1. If $b \in I$, then by convention $f'_+(b) = \infty$.
1. Hence $f'_+$ is u.s.c. at $b$.

(8) Lower semicontinuity of $f'_-$

1. The argument is similar to (7).
```

## Directional Derivatives of Proper Functions

```{index} Directional derivative
```
```{prf:definition} Directional derivative
:label: def-cvxf-directional-derivative

Let $f : \VV \to \RERL$ be a proper function
with $S = \dom f$.
Let $\bx \in \interior S$. 
The *directional derivative* at $\bx$ in the direction $\bd \in \VV$ is defined by 

$$
f'(\bx;\bd) \triangleq \lim_{\alpha \downarrow 0} \frac{f(\bx + \alpha \bd) - f(\bx)}{\alpha}
$$
provided the limit exists.

We say that $f$ is *directionally differentiable* at $\bx$
if it is directionally differentiable in every direction
at $\bx$.
```

```{div}
The directional derivative is a scalar quantity ($\in \RR$)
if it is defined (i.e., the limit exists).
When we say that 

$$
f'(\bx;\bd) = \lim_{t \downarrow 0} \frac{f(\bx + t \bd) - f(\bx)}{t},
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
f'(\bx;\bzero) = \lim_{\alpha \downarrow 0} \frac{f(\bx + \alpha \bzero) - f(\bx)}{\alpha} = 0.
$$
```

A useful result is for computing the directional derivative of a function
which is the pointwise maximum of a finite number of proper functions.

We recall from {prf:ref}`res-ms-int-intersect-int` that
the interior of a finite intersection of sets is the 
intersection of their interiors. This is useful in
identifying the interior of the domain for a pointwise
maximum of a finite set of functions. 


## Differentiability

### Differentiability of Proper Functions

```{index} Differentiability; proper function
```
````{prf:definition} Differentiability of proper functions
:label: def-cvxf-differentiability-proper

Let $f : \VV \to \RERL$ be a proper function with $S = \dom f$.
Let $\bx \in \interior S$. 
$f$ is said to be *differentiable* at $\bx$
if there exists $\bg \in \VV^*$ such that:

```{math}
:label: eq-cvxf-differentiability
\underset{\bh \to \bzero}{\lim}
\frac{f(\bx + \bh) - f(\bx) - \langle \bh, \bg \rangle}{\| \bh \|} = 0.
```
The unique vector $\bg$ satisfying this condition is called
the *gradient* of $f$ at $\bx$ and is denoted by $\nabla f(\bx)$.
````


If $f$ is differentiable at some $\bx \in \interior S$,
then there is a simple formula to connect the gradient
and the directional derivatives.

### Gradient and Directional Derivatives

```{prf:theorem} Gradient and directional derivatives
:label: res-cvxf-grad-dir-der

Let $f : \VV \to \RERL$ be a proper function with $S = \dom f$.
Let $\bx \in \interior S$. 
Assume that $f$ is differentiable at $\bx$.
Then, for any $\bd \in \VV$,

$$
f'(\bx; \bd) = \langle \bd, \nabla f(\bx) \rangle.
$$
In other words, the directional derivative is the projection
of the gradient in the specified direction.
```

```{prf:proof}
For $\bd = \bzero$, the equality is obvious. 
We shall consider the case where $\bd \neq \bzero$.

1. Since $f$ is differentiable at $\bx$, hence

  $$
  \underset{\bh \to \bzero}{\lim}
  \frac{f(\bx + \bh) - f(\bx) - \langle \bh, \nabla f(\bx) \rangle}{\| \bh \|} = 0.
  $$
1. In particular, if we take the limit of $\bh$ along the
   direction of $\bd$ as $t \bd$ where $t > 0$ and $t \to 0^+$, 
   then

   $$
   \underset{t \to 0^+}{\lim}
   \frac{f(\bx + t \bd) - f(\bx) - \langle t \bd, \nabla f(\bx) \rangle}{\| t \bd \|} = 0.
   $$
1. Splitting the terms, we get

   $$
   \underset{t \to 0^+}{\lim}
   \frac{f(\bx + t \bd) - f(\bx)}{\| t \bd \|} -
   \underset{t \to 0^+}{\lim}
   \frac{\langle \bd, \nabla f(\bx) \rangle}{\| \bd \|}
   = 0.
   $$
1. Multiplying with $\| \bd \|$ and simplifying, we get:

   $$
   \underset{t \to 0^+}{\lim}
   \frac{f(\bx + t \bd) - f(\bx)}{t} -
   \underset{t \to 0^+}{\lim} \langle \bd, \nabla f(\bx) \rangle
   = 0.
   $$
1. Thus,

   $$
   f'(\bx; \bd ) =  \underset{t \to 0^+}{\lim}
   \frac{f(\bx + t \bd) - f(\bx)}{t} 
   = \langle \bd, \nabla f(\bx) \rangle.
   $$
```

### Gradient in $\RR^n$

```{prf:remark} Gradient in $\RR^n$
:label: res-cvxf-gradient-r-n

It is imperative to compare the definition of gradients in this section
with {prf:ref}`def-mvc-point-differentiability`
(differentiability of functions from $\RR^n$ to $\RR^m$)
and the notion of the gradient as defined in
{prf:ref}`def-mvc-gradient`. 


To better develop our understanding of gradients, let us
examine the gradient in the Euclidean space $\RR^n$.
The standard basis is given by $\BBB = \{\be_1, \dots, \be_n \}$
which are the coordinate unit vectors.
The standard inner product is given by the dot product

$$
\langle \bx, \by \rangle = \by^T \bx  = \bx^T \by.
$$
A vector $\bx \in \RR^n$ is written as

$$
\bx  = \sum_{i=1}^n x_i \be_i.
$$
The individual coordinates are obtained via 

$$
x_i = \langle \be_i, \bx \rangle 
= \langle \bx, \be_i \rangle 
= \bx^T \be_i \Forall i \in [1,\dots, n].
$$

Let $f: \RR^n \to \RERL$ be a proper function. 
Let $S = \dom f$.
Let $\bx \in \interior S$. 
Assume that $f$ is differentiable at $\bx$.
Let $\bg = \nabla f (\bx)$.
Let 

$$
\bg = \sum_i^n g_i \be_i.
$$

Following the notation in {prf:ref}`res-mvc-f-m-n-jacobian-limit-alt`,
the derivative of $f$ at $\bx$, denoted by $Df(\bx)$
is given by

$$
\underset{\bh \to \bzero}{\lim}
\frac{\| f(\bx + \bh) - f(\bx) - Df(\bx) \bh \|_2}{\| \bh \|_2} = 0.
$$
We don't have to check for $\bx + \bh \in \dom f$ 
as $f$ is a proper function with a value of $\infty$ at
points outside its effective domain.

Compare this with {eq}`eq-cvxf-differentiability`.
For $f : \RR^n \to \RR$, $Df(\bx)$ is a row vector.
If we let $\tilde{\bg} = Df(\bx)^T$, then

$$
Df(\bx) \bh = \tilde{\bg}^T \bh = \langle \bh, \tilde{\bg} \rangle.
$$
Then, the definition of $\tilde{\bg}$ in the limit above
is exactly the same as $\bg$ in {eq}`eq-cvxf-differentiability`.
Thus, $\tilde{\bg} = \bg$.
We can see that our definition of gradient
coincides with the definition in
{prf:ref}`def-mvc-gradient` for $\RR^n$
with the dot product as standard inner product.


Now consider the components of $\bg$.

$$
g_i = \langle \be_i, \bg \rangle = \langle \be_i, \nabla f (\bx) \rangle.
$$

By {prf:ref}`res-cvxf-grad-dir-der`, the directional
derivative in the direction $\be_i$ is given by

$$
f'(\bx; \be_i) = \langle \be_i, \nabla f(\bx) \rangle
= \langle \be_i, \bg \rangle = g_i.
$$

Thus, 

$$
\frac{\partial f(\bx)}{\partial x_i} = \langle \be_i, \nabla f(\bx) \rangle.
$$
The partial derivatives of $f$ at $\bx$ along the
standard basis vectors are identical to the
directional derivatives of $f$.

$$
\nabla f(\bx) = \begin{bmatrix}
\frac{\partial f(\bx)}{\partial x_1}\\
\vdots\\
\frac{\partial f(\bx)}{\partial x_n}
\end{bmatrix}
= \begin{bmatrix}
\langle \be_1, \nabla f(\bx) \rangle\\
\vdots\\
\langle \be_n, \nabla f(\bx) \rangle
\end{bmatrix}.
$$

Then, for an arbitrary direction 
$\bd = \sum_{i=1}^n \be_i$, the directional derivative 
becomes

$$
f'(\bx; \bd) = \langle \bd, \nabla f(\bx) \rangle
= \nabla f(\bx)^T \bd
= \sum_{i=1}^n \frac{\partial f(\bx)}{\partial x_i} d_i.
$$

Recall from {prf:ref}`def-cvxf-directional-derivative`,
that the directional derivative is independent 
on the choice of the inner product. This
is also clear from the expression
$\sum_{i=1}^n \frac{\partial f(\bx)}{\partial x_i} d_i$
as the partial derivatives are independent of the
choice of the inner product.

However, this means that the gradient itself must
depend on the choice of inner product. 
If $\langle \cdot, \cdot \rangle_a$ 
and $\langle \cdot, \cdot \rangle_b$
are two different inner products defined on $\RR^n$,
then the gradients of $f$ at $\bx$ w.r.t. the
two inner products, denoted by $\nabla_a f(\bx)$
and $\nabla_b f(\bx)$ must satisfy the relationship

$$
f'(\bx; \bd) = \langle \bd, \nabla_a f(\bx) \rangle_a
= \langle \bd, \nabla_b f(\bx) \rangle_b
\Forall \bd \in \VV.
$$
In the following, we shall assume that
$\nabla f(\bx)$ denotes the gradient
w.r.t. the dot product.

Consider the inner product given by

$$
\langle \bx, \by \rangle_H = \bx^T \bH \by
$$
where $\bH \in \RR^{n \times n}$ is a symmetric
positive definite matrix.

Then,

$$
(\nabla_H f(\bx))_i &= \nabla_H f(\bx)^T \be_i 
& \text{coordinate in standard basis}\\
&= \nabla_H f(\bx)^T (\bH \bH^{-1}) \be_i & \text{$\bH$ is invertible}\\
&= \nabla_H f(\bx)^T \bH (\bH^{-1}\be_i) & \\
&= \langle \bH^{-1}\be_i, \nabla_H f(\bx) \rangle_H  
& \text{by definition of this inner product} \\
&= f'(\bx; \bH^{-1}\be_i)
& \text{directional derivative w.r.t. this inner product} \\
&= \nabla f(\bx)^T \bH^{-1}\be_i 
& \text{directional derivative w.r.t. dot product}\\
&= (\bH^{-1} \nabla f(\bx))^T \be_i
& \text{$\bH$ is symmetric}.
$$
Thus,

$$
\nabla_H f(\bx) = \bH^{-1} \nabla f(\bx).
$$


Thus, the gradient w.r.t. the inner product
$\langle \cdot, \cdot \rangle_H$ is the
scaled version of the standard gradient
where the scaling factor is $\bH^{-1}$.
```

###  Gradient in $\RR^{m \times n}$

```{prf:remark} Gradient in $\RR^{m \times n}$
:label: res-cvxf-gradient-r-m-n

We next look at the vector space of real matrices.
The standard basis is a family of unit matrices
$\{ \bE_{i j} \}_{1 \leq i \leq m, 1 \leq j \leq n}$
where $\bE_{i j}$ has the $(i,j)$-th entry as 1 and other
entries as 0.

The standard inner product is given by

$$
\langle \bX , \bY \rangle =  \Trace(\bY^T \bX )
\Forall \bX, \bY \in \RR^{m \times n}.
$$

Let $f : \RR^{m \times n} \to \RR$ be a proper function.
Let $S = \dom f$.
Let $\bX \in \interior S$.
Assume that $f$ is differentiable at $\bX$.

The gradient is given by

$$
\partial f(\bX) = \left ( 
  \frac{\partial f(\bX)}{\partial x_{i j}} \right )_{i j }.
$$

The directional derivative for some direction $\bD \in \RR^{m \times n}$
is given by

$$
f(\bX ; \bD) = \langle \bD, \partial f(\bX) \rangle
= \Trace(\partial f(\bX)^T \bD).
$$


Consider the inner product given by

$$
\langle \bX, \bY \rangle_H = \Trace(\bX^T \bH \bY)
$$
where $\bH \in \RR^{m \times m}$ is a symmetric
positive definite matrix.

Then,

$$
(\nabla_H f(\bX))_{i j} &= \Trace(\nabla_H f(\bX)^T \bE_{i j}) 
& \text{coordinate in standard basis}\\
&= \Trace(\nabla_H f(\bX)^T (\bH \bH^{-1}) \bE_{i j}) & \text{$\bH$ is invertible}\\
&= \Trace(\nabla_H f(\bX)^T \bH (\bH^{-1}\bE_{i j}) ) & \\
&= \langle \bH^{-1}\bE_{i j}, \nabla_H f(\bX) \rangle_H  
& \text{by definition of this inner product} \\
&= f'(\bX; \bH^{-1}\bE_{i j})
& \text{directional derivative w.r.t. this inner product} \\
&= \Trace(\nabla f(\bX)^T \bH^{-1}\bE_{i j}) 
& \text{directional derivative w.r.t. standard inner product}\\
&= (\bH^{-1} \nabla f(\bX))^T \bE_{i j}
& \text{$\bH$ is symmetric}.
$$
Thus,

$$
\nabla_H f(\bX) = \bH^{-1} \nabla f(\bX).
$$
```


## Proper Convex Functions

### Existence of Directional Derivatives

An important property of directional derivatives
is that if $f$ is a proper convex function then
$f$ is directionally differentiable at every
$\bx \in \interior \dom f$.

```{prf:theorem} Existence of directional derivatives for convex functions.
:label: res-cvxf-dir-der-exist-convex

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $\bx \in \interior S$. 
Then, for any $\bd \in \VV$, 
the directional derivative $f'(\bx; \bd)$ exists.
```

```{prf:proof}
This is a consequence of the directional differentiability
of the scalar convex functions.

1. Define the convex function $F : \RR \to \RR$ as

   $$
   F(t) = f(\bx + t \bd).
   $$
1. Let $I = \dom F$.
1. Then $I$ is an interval of values for which
   $\bx + t \by \in S$.
1. Since $\bx \in \interior S$, hence
   $t=0 \in \interior I$.
1. We now note that

   $$
   f'(\bx; \bd) 
   = \lim_{t \downarrow 0} \frac{f(\bx + t \bd) - f(\bx)}{t}
   = \lim_{t \downarrow 0} \frac{F(t) - F(0)}{t}
   = F'_+ (0).
   $$
   It is the right hand derivative of $F$ at $t=0$.
1. By {prf:ref}`res-cvxf-rf-convex-osd`, $F'_+(0)$
   exists.
1. Hence $f'(\bx; \bd)$ exists for every $\bx \in \interior S$
   and every $\bd \in \VV$.
```

```{prf:observation} Relation between the directional derivatives in opposite directions
:label: res-cvxf-dir-der-opposite

We can see that

$$
f'(\bx; -\bd) 
= \lim_{t \downarrow 0} \frac{f(\bx - t \bd) - f(\bx)}{t}
= \lim_{t \downarrow 0} \frac{F(-t) - F(0)}{t}
= - \lim_{r \uparrow 0} \frac{F(r) - F(0)}{r}
= - F'_- (0).
$$
Hence

$$
F'_- (0) = - f'(\bx; -\bd).
$$

By {prf:ref}`res-cvxf-rf-one-sided-der-props`

$$
F'_- (0) \leq F'_+(0).
$$

Hence

$$
- f'(\bx; -\bd) \leq f'(\bx; \bd) \Forall \bd \in \VV.
$$
```

```{prf:observation} Directional derivative as infimum
:label: res-cvxf-dir-der-infimum

Let $f: \VV \to \RERL$ be a proper convex function
with $S = \dom f$.
Let $\bx \in \interior S$. 
Then, for any $\bd \in \VV$, 

$$
f'(\bx; \bd) = \inf_{t > 0} \frac{f(\bx + t \bd) - f(\bx)}{t}.
$$

This follows from the fact that
$F(t) = f(\bx + t \bd)$ is convex
and due to {prf:ref}`res-cvxf-rf-one-sided-derivative-inf-sup`,

$$
f'(\bx; \bd) = F'_+(0)
= \inf_{t > 0} \frac{F(t) - F(0)}{t}
= \inf_{t > 0} \frac{f(\bx + t \bd) - f(\bx)}{t}.
$$
```

### Upper Semicontinuity

The next result generalizes the upper semicontinuity
property of the right hand derivatives of real convex
functions.

```{prf:theorem}
Let $f: \VV \to \RERL$ be a proper convex function
with $\dom f = S$.
Assume that $S$ is an open subset of $\VV$.
Let $\{ f_k \}$ be a sequence of
proper convex functions $f_k : \VV \to \RERL$
with $\dom f_k = S$ with the property that

$$
\lim_{k \to \infty} f_k(\bx_k) = f(\bx)
$$
holds true for every $\bx \in S$
and every sequence $\{ \bx_k \}$ of $S$ that converges to $\bx$.
Then for any $\bx \in S$ and any direction $\bd \in \VV$
and any sequences $\{ \bx_k \}$ of $S$
and $\{ \bd_k \}$ of $\VV$ converging to $\bx$ and $\bd$
respectively, we have

$$
\limsup_{k \to \infty} f'_k (\bx_k; \bd_k ) \leq f'(\bx; \bd).
$$
Furthermore if $f$ is differentiable over $S$,
then $f$ is also continuously differentiable over $S$.
```

```{prf:proof}
Limit superior

1. Choose any $\epsilon > 0$.
1. By definition of the directional derivative, there exists a $t > 0$
   such that

   $$
   \frac{f(\bx + t \bd) - f(\bx)}{t} < f'(\bx; \bd) + \epsilon.
   $$
1. Due to {prf:ref}`res-cvxf-dir-der-infimum`, for every $k$
   and every $t > 0$, we have

   $$
   f'_k(\bx_k; \bd_k) \leq \frac{f_k(\bx_k + t \bd_k) - f(\bx_k)}{t}.
   $$
1. Now

   $$
   \lim_{k \to \infty} \frac{f_k(\bx_k + t \bd_k) - f(\bx_k)}{t}
   = \frac{f(\bx + t \bd) - f(\bx)}{t}.
   $$
1. Hence for sufficiently large $k$, we have

   $$
   f'_k(\bx_k; \bd_k) \leq \frac{f_k(\bx_k + t \bd_k) - f(\bx_k)}{t}
   < f'(\bx; \bd) + \epsilon.
   $$
1. By taking the limit superior on the L.H.S. as $k \to \infty$, we have

   $$
   \limsup_{k \to \infty} f'_k (\bx_k; \bd_k ) \leq f'(\bx; \bd) + \epsilon.
   $$
1. Since this is valid for every $\epsilon > 0$, hence we must have

   $$
   \limsup_{k \to \infty} f'_k (\bx_k; \bd_k ) \leq f'(\bx; \bd)
   $$
   as desired.


Continuous differentiability

1. We are given that $f$ is differentiable over $S$.
1. Then $f$ is also continuous over $S$.
1. Let $\bx \in S$.
1. Let $\{ \bx_k \}$ be a sequence of $S$ converging to $\bx$.
1. Let $\bd \in \VV$ be any nonzero direction.
1. Due to {prf:ref}`res-cvxf-grad-dir-der`, for every $k$,

   $$
    f'(\bx_k; \bd) = \langle \bd, \nabla f(\bx_k) \rangle.
   $$
1. Hence

   $$
   \limsup_{k \to \infty} \langle \bd, \nabla f(\bx_k) \rangle
   &= \limsup_{k \to \infty} f'(\bx_k; \bd)\\
   &\leq f'(\bx; \bd) \\
   &= \langle \bd, \nabla f(\bx) \rangle.
   $$
1. By replacing $\bd$ with $-\bd$ in the previous argument,
   we have

   $$
   - \liminf_{k \to \infty} \langle \bd, \nabla f(\bx_k) \rangle
   &= \limsup_{k \to \infty} \langle -\bd, \nabla f(\bx_k) \rangle\\
   &= \limsup_{k \to \infty} f'(\bx_k; -\bd)\\
   &\leq f'(\bx; -\bd)\\
   &= -\langle \bd, \nabla f(\bx) \rangle.
   $$
1. Hence

   $$
   \liminf_{k \to \infty} \langle \bd, \nabla f(\bx_k) \rangle
   \geq \langle \bd, \nabla f(\bx) \rangle.
   $$
1. Thus we have

   $$
   \limsup_{k \to \infty} \langle \bd, \nabla f(\bx_k) \rangle
   \leq
   \liminf_{k \to \infty} \langle \bd, \nabla f(\bx_k) \rangle.
   $$
1. But then this must be an equality. Hence

   $$
   \lim_{k \to \infty} \langle \bd, \nabla f(\bx_k) \rangle
   = \langle \bd, \nabla f(\bx) \rangle.
   $$
1. Since this is valid for every nonzero direction $\bd \in \VV$,
   hence we must have

   $$
   \lim_{k \to \infty} \nabla f(\bx_k)  = \nabla f(\bx).
   $$
1. Hence $\nabla f$ is continuous at every $\bx \in S$.
1. Hence $f$ is continuously differentiable at every $\bx \in S$.
```

### Directional Derivatives Map

The existence of directional derivatives in all directions
allows us to consider a mapping from a direction $\bd \in \VV$
to the directional derivative of $f$ in this direction at $\bx$.
We can define a directional derivative map
parameterized by $\bx \in S$ as:

$$
\bg_x(\bd) \triangleq f'(\bx; \bd) = 
\lim_{\alpha \downarrow 0} \frac{f(\bx + \alpha \bd) - f(\bx)}{\alpha}.
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
   &= \lim_{\alpha \downarrow 0} \frac{f(\bx + \alpha [t \bd_1 + (1-t) \bd_2]) - f(\bx)}{\alpha}\\
   &= \lim_{\alpha \downarrow 0} 
   \frac{f(t \bx + \alpha t \bd_1 + (1-t) \bx + \alpha (1-t) \bd_2) - f(\bx)}{\alpha}\\
   &= \lim_{\alpha \downarrow 0} 
   \frac{f(t (\bx + \alpha \bd_1) + (1-t) (\bx + \alpha \bd_2)) - f(\bx)}{\alpha}\\
   &\leq \lim_{\alpha \downarrow 0} 
   \frac{t f(\bx + \alpha \bd_1) + (1-t) f(\bx + \alpha \bd_2) - t f(\bx) - (1-t)f(\bx)}{\alpha}\\
   &= t \lim_{\alpha \downarrow 0} \frac{f(\bx + \alpha \bd_1) - f(\bx)}{\alpha} +
   (1-t) \lim_{\alpha \downarrow 0} \frac{f(\bx + \alpha \bd_2) - f(\bx)}{\alpha}\\
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
   f'(\bx; t \bd) &= \lim_{\alpha \downarrow 0} \frac{f(\bx + \alpha t \bd) - f(\bx)}{\alpha}\\
   &= t \lim_{\alpha \downarrow 0} \frac{f(\bx + \alpha t \bd) - f(\bx)}{\alpha t}\\
   &= t f'(\bx; \bd).
   $$
1. Thus, $f'(\bx; \bd)$ is nonnegative homogeneous.
```

### As Linear Underestimator

Directional derivatives are a linear underestimator for convex functions.

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
&= \lim_{\alpha \downarrow 0} \frac{f(\bx + \alpha (\by - \bx)) - f(\bx)}{\alpha}\\
&= \lim_{\alpha \downarrow 0} \frac{f((1-\alpha) \bx + \alpha \by) - f(\bx)}{\alpha}\\
&\leq \lim_{\alpha \downarrow 0} \frac{(1-\alpha)f(\bx) + \alpha f(\by) - f(\bx)}{\alpha}\\
&= \lim_{\alpha \downarrow 0} \frac{\alpha (f(\by) - f(\bx))}{\alpha}\\
&= \lim_{\alpha \downarrow 0}(f(\by) - f(\bx)) = f(\by) - f(\bx).
$$

Thus,

$$
f(\by) \geq f(\bx) + f'(\bx; \by - \bx).
$$
```


## Pointwise Maximum of Finite Set of Functions

### Directional Derivative

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
1. Taking the limit $t \downarrow 0$,

   $$
   f'(\bx; \bd) 
   &= \lim_{t \downarrow 0} \frac{f(\bx + t \bd) - f(\bx)}{t}\\
   &= \lim_{t \downarrow 0} \underset{i \in I(\bx)}{\max} \frac{f_i(\bx + t \bd) - f_i(\bx)}{t}\\
   &= \underset{i \in I(\bx)}{\max} \lim_{t \downarrow 0} \frac{f_i(\bx + t \bd) - f_i(\bx)}{t}\\
   &= \underset{i \in I(\bx)}{\max} f'_i(\bx; \bd).
   $$
```

### Finite Set of Convex Functions Case

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
