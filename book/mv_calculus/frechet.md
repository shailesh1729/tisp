(sec:mvc:banach:diff)=
# Differentiation in Banach Spaces

We introduce the concept of differentiation in Banach spaces.
Recall that {prf:ref}`Banach spaces <def-la-banach-space>` 
are normed linear spaces that are complete.

## Gateaux Differential

```{prf:definition} Directional derivative
:label: def-mvcb-directional-derivative

Let $X$ and $Y$ be Banach spaces.
Let $f: X \to Y$ be a function
with $S = \dom f$.
The directional derivative of $f$ at $\bx \in \interior S$
in the direction $\bh \in X$ where $\bh \neq \bzero$,
denoted by $f'(\bx; \bh)$ is 
given by

$$
f'(\bx; \bh) \triangleq \lim_{t \to 0^+} \frac{f (\bx + t \bh) - f(\bx)}{t}
$$
whenever the limit exists.
This is also known as the *Gateaux differential*.
By convention, $f'(\bx; \bzero_X) = \bzero_Y$. This is consistent
with the definition above.
```

```{div}
* There is no single directional derivative at a point $\bx$.
* The directional derivative depends on the direction $\bh$.
* In one dimension, there are two directional derivatives at each $\bx$.
* In two or more dimensions, there are infinitely many directional derivatives.
* The directional derivative is a one dimensional calculation along the
  direction $\bh$.
* It is usually easy to compute the directional derivative even when
  the space $X$ is infinite dimensional.
```




```{prf:definition} Gateaux differentiability
:label: def-mvcb-gateaux-differentiability

Let $X$ and $Y$ be Banach spaces.
Let $f: X \to Y$ be a function
with $S = \dom f$.
Let $U \subseteq S$ be an open set.
We say that $f$ is *Gateaux differentiable*
at $\bx \in U$ 
if the Gateaux differential $f'(\bx; \bh)$
exists for every direction $\bh \in X$.

Accordingly, we can define a bounded operator $T_x : X \to Y$ given by

$$
T_x(\bh) \triangleq \lim_{t \to 0^+} \frac{f (\bx + t \bh) - f(\bx)}{t} \Forall \bh \in X.
$$
The operator $T$ is called the *Gateaux derivative* of $f$ at $\bx$.
```

```{prf:example} Gateaux differential of exponential function
:label: def-mcvb-exponential-gateaux

Let $f(x) = e^x$. Then,

$$
f'(x; h) &= \lim_{t \to 0^+}\frac{e^{x + th} - e^x}{ t} \\
&= e^x \lim_{t \to 0^+} \frac{e^{t h} - 1}{t} \\
&= e^x \lim_{t \to 0^+} \frac{t h }{t} = h e^x.
$$

We note that the Gateaux derivative depends linearly on $h$.
```


```{prf:theorem} Gateaux differential nonnegative homogeneity
:label: res-mvcb-gateaux-homogeneity

The Gateaux differential of a function $f : X \to Y$
is nonnegative homogeneous in the sense that

$$
f'(\bx; \alpha \bh) = \alpha f'(\bx; \bh)
$$
for every $\alpha \in \RR_+$ and every $\bh \in X$.
```

However, the Gateaux differential may not be additive.
Thus, the Gateaux differential may fail to be linear.


```{prf:example} Gateaux differential of absolute value function
:label: ex-mvcb-abs-val-func-gateaux

Let $f(x) = |x|$. Then, the Gateaux differentials are given by

$$
f'(x; h) = \begin{cases}
h \frac{x}{|x|} & x \neq 0;\\
|h | & x = 0.
\end{cases}
$$
We note that the Gateaux differential of $f$ exists 
everywhere.
However the Gateaux differential depends on $h$
in a nonlinear way at $x=0$. 
At $x \neq 0$, the Gateaux differential depends
linearly on $h$.
```

```{prf:example} Gateaux differential of square function
:label: ex-mvcb-square-func-gateaux

Let $f(x) = x^2$. Then, the Gateaux differential is given by

$$
f'(x; h) &= \lim_{t \to 0^+} \frac{f(x + t h) - f(x)}{t}  \\
&= \lim_{t \to 0^+} \frac{x^2 + t^2 h^2 + 2 x t h - x^2 }{t}  \\
&= 2 x h.
$$
We note that the Gateaux differential is linear w.r.t. $h$.
```

```{prf:example} Gateaux differential of linear functional
:label: ex-mvcb-linear-functional-gateaux

Let $f(\bx) = \ba^T \bx$ where $\ba \in \RR^n$ is a given fixed vector.

$$
f'(\bx; \bh) = \lim_{t \to 0^+}\frac{\ba^T \bx + t \ba^T \bh - \ba^T \bx}{t} 
= \ba^T \bh.
$$
We note that the Gateaux differential is linear w.r.t. $\bh$.
```

```{prf:example} Gateaux differential of simple quadratic
:label: ex-mvcb-simple-quadratic-gateaux

Let $f(\bx) = \bx^T \bA \bx$ where $\bA \in \SS^n$ is a given symmetric matrix.

$$
f'(\bx; \bh) &= \lim_{t \to 0^+}\frac{(\bx + t \bh) ^T \bA (\bx + t \bh)  - \bx^T \bA \bx}{t} \\
&= \lim_{t \to 0^+}\frac{t^2 \bh ^T \bA \bh + 2 t \bh^T \bA \bx}{t} \\
&= 2 \bh^T \bA \bx = 2 \bx^T \bA \bh.
$$
We note that the Gateaux differential is linear w.r.t. $\bh$.

In particular, if $f(\bx) = \bx^T \bx$, then $f'(\bx; \bh) = 2 \bh^T \bx = 2 \bx^T \bh$.
```


```{prf:theorem} Gateaux differential of a constant function
:label: res-mvcb-const-func-gateaux

The Gateaux differential of a constant function is zero.
```

```{prf:theorem} Gateaux differential sum rule
:label: res-mvcb-gateaux-sum-rule

Gateaux differential distributes over sum.

Let $f, g: X \to Y$ both have Gateaux derivatives at $\bx$
in the direction $\bh$.
Then,

$$
(f + g)'(\bx; \bh) = f'(\bx; \bh) + g'(\bx; \bh).
$$
Also,

$$
(f - g)'(\bx; \bh) = f'(\bx; \bh) - g'(\bx; \bh).
$$
```

```{prf:theorem} Gateaux differential product rule
:label: res-mvcb-gateaux-product-rule

Let $f, g: X \to Y$ both be Gateaux differentiable at $\bx \in \interior \dom f \cap \dom g$.
Let $h$ be their (pointwise) product function given by

$$
h(\bx) = f(\bx) g(\bx)
$$
with $\dom h = \dom f \cap \dom g$.
Then,

$$
h'(\bx; \bh) = = (fg)'(\bx; \bh)  = f'(\bx; \bh) g(\bx)  + g'(\bx; \bh) f(\bx).
$$
```

```{prf:theorem} Gateaux differential chain rule
:label: res-mvcb-gateaux-chain-rule

Let $f : X \to Y$ and $g : Y \to Z$ be functions.
Let $h : X \to Z$ be the composition of $f$ and $g$
given by $h = g \circ f$.
Let $U \subseteq \dom h$ be an open set.
Let $\bx \in U$.
Assume that $f$ is Gateaux differentiable at $\bx$
and $g$ is Gateaux differentiable at $f(\bx)$.
Then,

$$
h'(\bx; \bh) = g'(f(\bx); f'(\bx; \bh)) \Forall \bh \in X.
$$
```

We recall the little-$o$ notation. We say that a quantity $q$
is $o(t)$ if 

$$
\lim_{t \to 0^+} \frac{q}{t} = 0.
$$

For vector valued functions, a quantity $\bq$ is $o(t)$
if

$$
\lim_{t \to 0^+} \frac{ \| \bq \| }{t} = 0.
$$
or 

$$
\lim_{t \to 0^+} \frac{ \bq }{t} = \bzero.
$$

```{prf:proof}
If $f$ is Gateaux differentiable at $\bx$, then

$$
f'(\bx; \bh) = \lim_{t \to 0^+} \frac{f (\bx + t \bh) - f(\bx)}{t} \Forall \bh \in X.
$$

In terms of little-o notation,

$$
f(\bx + t \bh) = f(\bx) + t f'(\bx; \bh) + o(t). 
$$

Similarly, if $g$ is Gateaux differentiable at $\by$, then

$$
g(\by + s \bu) = g (\by) + s g'(\by; \bu) + o(s).
$$

Now,

$$
h'(\bx; \bh) = (g \circ f)' (\bx; \bh)
&= \lim_{t \to 0^+}\frac{g(f(\bx + t \bh)) - g(f(\bx)) }{t} \\
&=  \lim_{t \to 0^+}\frac{g(f(\bx) + t f'(\bx; \bh) + o(t) ) - g(f(\bx)) }{t} \\
&=  \lim_{t \to 0^+}\frac{g(f(\bx) + t (f'(\bx; \bh) + t^{-1}o(t)) ) - g(f(\bx)) }{t} \\
&=  \lim_{t \to 0^+}\frac{g(f(\bx)) + t g'(f(\bx); f'(\bx; \bh) + t^{-1}o(t)) + o(t) - g(f(\bx))}{t} \\
&=  \lim_{t \to 0^+}\frac{t g'(f(\bx); f'(\bx; \bh) + t^{-1}o(t) ) + o(t) } {t} \\
&=  \lim_{t \to 0^+} [g'(f(\bx); f'(\bx; \bh) ) + t^{-1}o(t)) + t^{-1} o(t) ] \\
&= g'(f(\bx); f'(\bx; \bh) ).
$$
```


```{prf:example} Chain rule for square of inner product
:label: ex-mvcb-gateaux-chain-rule-1

Consider the function $h(\bx) = (\bx^T \bx)^2$. 

1. Define $g(t) = t^2$
1. Define $f(\bx) = \bx^T \bx$.
1. Then $h = g \circ f$.
1. We have $f'(\bx; \bh) = 2 \bh^T \bx$.
1. We have $g'(y; u) = 2 y u$.
1. Thus, 
   
   $$
   g'(f(\bx); f'(\bx; \bh) ) 
   &= 2 f(\bx) f'(\bx; \bh) \\
   &= 2 (\bx^T \bx) (2 \bh^T \bx) \\
   &= 4 (\bh^T \bx) (\bx^T \bx).
   $$

We can compute the same thing using the product rule.

1. We note that $h (\bx) = f(\bx) f(\bx)$.
1. Applying the product rule:

   $$
   h'(\bx; \bh) &= f'(\bx; \bh) f(\bx)  + f'(\bx; \bh) f(\bx)\\
   &=  2 f'(\bx; \bh) f(\bx) \\
   &= 2 (2 \bh^T \bx) (\bx^T \bx) \\
   &= 4 (\bh^T \bx) (\bx^T \bx).
   $$
```

## Fréchet Derivative

```{prf:definition} Fréchet differentiability
:label: def-mvcb-frechet-differentiability

Let $X$ and $Y$ be Banach spaces.
Let $f: X \to Y$ be a function
with $S = \dom f$.
Let $U \subseteq S$ be an open set.
We say that $f$ is *Fréchet differentiable*
at $\bx \in U$ if there is a bounded and linear
operator $T_x : X \to Y$ given by

$$
T_x(\bh) = \lim_{t \to 0^+} \frac{f (\bx + t \bh) - f(\bx)}{t} \Forall \bh \in X.
$$
The operator $T_x$ is called the *Fréchet derivative*
of $f$ at $\bx$.
```

We note that $T_x$ depends on $\bx$.

```{prf:remark} Fréchet differentiability alternate forms
:label: rem-mvcb-frechet-differentiability-2

By definition, if $f$ is Fréchet differentiable at $\bx$, then it is
Gateaux differentiable at $\bx$. Since $T_x$ is linear, we can write
it as

$$
T_x(\bh) = \bA \bh
$$
emphasizing the fact that the essential part of $T_x$ doesn't depend
on $\bh$. $\bA$ may still depend on $\bx$.


Using the little-$o$ notation, we can write

$$
f(\bx + t \bh) = f(\bx) + t T_x(\bh) + o(t)
= f(\bx) + t \bA \bh + o(t). 
$$

If we set $t\bh = \by$, then $t \to 0$ if and only if $\by \to \bzero$.
In particular, $\| \by \|_X = t \| \bh \|_X = o (t)$.
Now,

$$
& f(\bx + \by) = f(\bx) + \bA \by + o(t) \\
&\iff f(\bx + \by) - f(\bx) - \bA \by = o (t) = o( \| \by \|_X) \\
&\iff \lim_{\| \by \|_X \to 0 } \frac{ \| f(\bx + \by) - f(\bx) - \bA \by \|_Y}{\| \by \|_X} = 0 \\
&\iff \lim_{ \by \to \bzero } \frac{\| f(\bx + \by) - f(\bx) - \bA \by \|_Y}{\| \by \|_X} = 0 \\
&\iff \lim_{ \by \to \bzero } \frac{\| f(\bx + \by) - f(\bx) - T_x (\by) \|_Y }{\| \by \|_X} = 0.
$$

Therefore $f : X \to Y$ is Fréchet differentiable at $\bx \in U$ 
if and only if 

$$
\lim_{\by \to \bzero} \frac{f(\bx + \by) - f(\bx) - T_x(\by)}{\| \by \|_X} = \bzero
$$
for every $\by \in X$.

It is worthwhile to compare this definition to
the definition of differentiability of $ f: \RR^n \to \RR^m$
in {prf:ref}`def-mvc-point-differentiability`. If we put $\bz = \bx + \by$,
we can rewrite the condition as

$$
\lim_{\bz \to \bx} \frac{ \| f(\bz) - f(\bx) - T_x(\bz - \bx) \|_Y}{\| \bz - \bx \|_X} = 0.
$$
Thus, $T_x$ plays the same role as the Jacobian matrix $Df(\bx)$
in {eq}`eq-mvc-f-m-n-jacobian-limit`.
```

```{prf:theorem} Existence of Fréchet derivative
:label: res-mvcb-frechet-existence

The Fréchet derivative of a function $f$ exists at a point $\bx = \ba$
if and only if all Gateaux differentials of $f$ at $\bx$ are continuous functions
of $\bx$ at $\bx=\ba$.
```

```{prf:theorem} Uniqueness of Fréchet derivative
:label: res-mvcb-frechet-uniqueness

If the Fréchet derivative of a function $f$ exists at a point $\bx = \ba$
then it is unique.
```


## Gradient

```{prf:definition} Gradient
:label: def-mvcb-gradient
Let $\VV$ be a Hilbert space.
Let $f : \VV \to \RR$ is a real valued function.
Let $S = \dom f$ and $U \subseteq S$ be an open set.
Assume that $f$ is Fréchet differentiable at $\bx \in U$.
Then, the Fréchet derivative $T_x : \VV \to \RR$ is a
bounded linear functional.

The *gradient* of a real valued function is denoted
by $\nabla f(\bx)$ and $\nabla f(\bx) \in \VV^*$
satisfying

$$
\langle \bh, \nabla f(\bx) \rangle = T_x(\bh).
$$
```

