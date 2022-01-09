# Differentiable Functions

We continue our discussion on real functions and
focus on a special class of functions which are *differentiable*.

```{prf:definition} Differentiable function
:label: def-bra-rf-differentiable-function

A real function $f: \RR \to \RR$ is *differentiable* 
at an interior point $x=a$ of its domain $\dom f$ 
if the difference quotient

$$
\frac{f(x) - f(a)}{x - a}, \quad x \neq 0
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


```{prf:remark}
$$
\dom f' \subseteq \interior \dom f.
$$
```


```{prf:definition}
Let $f$ be defined on an open set $A$. 
We say that $f$ 
is *differentiable on $A$* if $f$ is differentiable 
at every point in $A$.
```

1. If $f$ is differentiable on (open) $A$, 
   then $f'$ is defined on $A$. 
   In other words: $\dom f' = A$.


```{prf:definition}
We say that $f$ is *continuously differentiable* on an open set $A$
if $f$ is differentiable on $A$ and $f'$ is continuous on $A$.
```


```{prf:definition}
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


```{prf:remark}
If $f$ is differentiable at $x=a$, then the tangent to $f$ 
at $x=a$ can be given by:

$$
T(x) = f(a) + f'(a)(x -a).
$$
```

It is sometimes useful to remove the contribution of the tangent in $f$
and study the remaining part of $f$.

````{prf:lemma}
If $f$ is differentiable at $x=a$, then

```{math}
:label: eq-bra-df-f-minus-tangent
f(x) = f(a) + [f'(a) + E(x)](x -a)
```
where $E$ is defined in the neighborhood of $x=a$ and

$$
\lim_{x \to a} E(x) = E(a) = 0.
$$
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
```
