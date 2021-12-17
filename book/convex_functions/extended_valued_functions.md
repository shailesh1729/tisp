# Extended Real Valued Functions

```{prf:definition} Extended real-valued function
:label: def-extended-real-valued-function

A function is called an *extended real-valued function* if it
can take any real value as well as the infinite values
$-\infty$ and $\infty$. 

In other words, its codomain is $\RR \cup \{ -\infty, \infty \}$.
We also write the codomain as $[-\infty, \infty]$.
```

Some notation:

- $\RR = (-\infty, \infty)$
- $\RR \cup \{ \infty\} = (-\infty, \infty]$
- $\RR \cup \{ -\infty\} = [-\infty, \infty)$
- $\RR \cup \{ -\infty, \infty\} = [-\infty, \infty]$


```{prf:definition} Extended valued comparison rules

We define the following rules of comparison between real numbers
and infinities:

- $ a < \infty \Forall a \in \RR$
- $ a > -\infty \Forall a \in \RR$
- $ -\infty < \infty $

In other words $ -\infty < a < \infty \Forall a \in \RR$.
```

```{prf:definition} Extended valued arithmetic

The arithmetic between real numbers and the infinite values
is defined as below:

$$
a + \infty = \infty + a = \infty \;\; (-\infty < a < \infty)
$$


$$
a - \infty = -\infty + a = -\infty \;\; (-\infty < a < \infty)
$$

$$ 
a \times \infty = \infty \times a  = \infty \;\; (0 < a < \infty)
$$ 


$$ 
a \times (-\infty) = (-\infty) \times a  = -\infty \;\; (0 < a < \infty)
$$ 

$$ 
a \times \infty = \infty \times a  = -\infty \;\; (-\infty < a < 0)
$$ 


$$ 
a \times (-\infty) = (-\infty) \times a  = \infty \;\; (-\infty < a < 0)
$$ 

$$
0 \times \infty = \infty \times 0 = 0 \times (-\infty) = (-\infty) \times 0 = 0.
$$
```

## Extensions for Convex Functions



```{prf:definition} Extended-value extension
:label: def-extended-value-extension

If $f$ is convex, we define its *extended-value extension*
$\tilde{f} : \RR^n \to (0, \infty]$ by

$$
    \tilde{f}(x) = \begin{cases} 
     f(x) & \text{for} & x \in \dom f \\
    \infty & \text{for} & x \notin \dom f
    \end{cases}
$$
```

## Indicator Functions

