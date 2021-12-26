The Extended Real Line
=========================

```{prf:definition} Extended real line

The *extended real number system* or *extended real line* 
is obtained from the real number system $\RR$ by adding 
two infinity elements $+\infty$ and $-\infty$, where the
infinities are treated as actual numbers. 

It is denoted as $\ERL$ or $\RR \cup \{-\infty, +\infty\}$.

The symbol $+\infty$ is often written simply as $\infty$.
```

In order to make $\ERL$ a useful number system, we need
to define the comparison and arithmetic rules of the new
infinity symbols w.r.t. existing elements in $\RR$ and between
themselves.


```{prf:definition} Extended valued comparison rules

We define the following rules of comparison between real numbers
and infinities:

- $ a < \infty \Forall a \in \RR$
- $ a > -\infty \Forall a \in \RR$
- $ -\infty < \infty $

In other words $ -\infty < a < \infty \Forall a \in \RR$.
```

Following notations are useful:

- $\RR = (-\infty, \infty)$
- $\RR \cup \{ \infty\} = (-\infty, \infty]$
- $\RR \cup \{ -\infty\} = [-\infty, \infty)$
- $\RR \cup \{ -\infty, \infty\} = [-\infty, \infty]$


```{prf:definition} Extended valued arithmetic

The arithmetic between real numbers and the infinite values
is defined as below:

$$
\begin{aligned}
& a + \infty = \infty + a = \infty \quad (-\infty < a < \infty)\\
& a - \infty = -\infty + a = -\infty \quad (-\infty < a < \infty)\\
& a \times \infty = \infty \times a  = \infty \quad (0 < a < \infty)\\
& a \times (-\infty) = (-\infty) \times a  = -\infty \quad (0 < a < \infty)\\
& a \times \infty = \infty \times a  = -\infty \quad (-\infty < a < 0)\\
& a \times (-\infty) = (-\infty) \times a  = \infty \quad (-\infty < a < 0)\\
& \frac{a}{\pm \infty} = 0\quad (-\infty < a < \infty)
\end{aligned}
$$

The arithmetic between infinities is defined as follows:

$$
\begin{aligned}
&\infty + \infty = \infty\\
&(-\infty) + (-\infty) = -\infty\\
&\infty \times \infty = \infty\\
&(-\infty) \times (-\infty) = \infty\\
&(-\infty) \times \infty = -\infty\\
&\infty \times (-\infty) = -\infty
\end{aligned}
$$

Usually, multiplication of infinities with zero is left undefined.
But for the purposes of optimization literature, it is useful to 
define as follows: 

$$
0 \times \infty = \infty \times 0 = 0 \times (-\infty) = (-\infty) \times 0 = 0.
$$
```
