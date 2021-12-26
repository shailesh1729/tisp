# Extended Real Valued Functions

```{prf:definition} Extended real-valued function
:label: def-extended-real-valued-function

A function is called an *extended real-valued function* if it
can take any real value as well as the infinite values
$-\infty$ and $\infty$. 

In other words, its codomain is $\RR \cup \{ -\infty, \infty \}$.
We also write the codomain as $[-\infty, \infty]$.
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

