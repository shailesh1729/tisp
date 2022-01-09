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
* The derivative is not defined for the boundary points
  of $\dom f$. Only one sided limits may be computed
  at the boundary points on the difference quotient.
