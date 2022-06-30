# Univariate Distributions

## Gaussian Distribution

### Standard Normal Distribution


This distribution has a mean of 0 and a variance of 1.
It is denoted by

$$
X \sim \NNN(0, 1).
$$

The PDF is given by

$$
f_X(x) = \frac{1}{\sqrt{2\pi}} \exp \left ( - \frac{x^2}{2} \right ).
$$
The CDF is given by

$$
F_X(x) = \int_{-\infty}^x f_X(t) d t
= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} \exp \left ( - \frac{t^2}{2} \right ) d t.
$$
Symmetry

$$
f(-x) = f(x). \quad F(-x) + F(x)  = 1.
$$
Some specific values

$$
F_X(-\infty) = 0, \quad  F_X(0) = \frac{1}{2}, 
\quad F_X(\infty) = 1.
$$

The Q-function is given as

$$
Q(x) = \int_{x}^{\infty} f_X(t) d t 
= \frac{1}{\sqrt{2\pi}} \int_{x}^{\infty} \exp \left ( - \frac{t^2}{2} \right ) d t.
$$

We have

$$
F_X(x) + Q(x) = 1. 
$$
Alternatively

$$
F_X(x) = 1 - Q(x).
$$
Further

$$
Q(x) + Q(-x) = 1.
$$
This is due to the symmetry of normal distribution.
Alternatively

$$
Q(x)  = 1 - Q(-x).
$$
Probability of $X$ falling in a range $[a,b]$

$$
\PP (a \leq X \leq b) =  Q(a) - Q(b) = F(b) - F(a).
$$
The characteristic function is

$$
\Psi_X(j\omega) = \exp\left ( - \frac{\omega^2}{2}\right ).
$$
Mean:

$$
\mu = \EE (X) = 0.
$$
Mean square value

$$
\EE (X^2) = 1.
$$
Variance:

$$
\sigma^2 = \EE (X^2) - \EE(X)^2 = 1.
$$
Standard deviation

$$
\sigma = 1.
$$

An upper bound on Q-function

$$
Q(x) \leq \frac{1}{2} \exp \left ( - \frac{x^2}{2} \right ).
$$
The moment generating function is

$$
M_X(t) = \exp\left ( \frac{t^2}{2}\right ).
$$

### Error Function

The *error function* is defined as

$$
\erf(x) \triangleq  \frac{2}{\sqrt{\pi}} \int_0^x \exp\left ( - t^2 \right) d t.
$$
The *complementary error function* is defined as

$$
\erfc(x) = 1 - \erf(x) = \frac{2}{\sqrt{\pi}} \int_x^{\infty} \exp\left ( - t^2 \right) d t.
$$
Error function is an odd function.

$$
\erf(-x) = - \erf(x).
$$
Some specific values of error function.

$$
\erf(0) = 0, \quad \erf(-\infty) = -1 , \quad \erf (\infty) = 1.
$$
The relationship with normal CDF.

$$
F_X(x) = \frac{1}{2} + \frac{1}{2}  \erf \left ( \frac{x}{\sqrt{2}}\right)
= \frac{1}{2} \erfc \left (- \frac{x}{\sqrt{2}}\right).
$$
Relationship with Q function.

$$
Q(x) = \frac{1}{2} \erfc\left (\frac{x}{\sqrt{2}} \right)
= \frac{1}{2} - \frac{1}{2}  \erf \left ( \frac{x}{\sqrt{2}} \right ).
$$

$$
\erfc(x) = 2 Q(\sqrt{2} x).
$$
We also have some useful results:

$$
\int_0^{\infty} \exp\left ( - \frac{t^2}{2}\right ) d t 
= \sqrt{\frac{\pi}{2}}.
$$

### General Normal Distribution

The general Gaussian (or normal) random variable
is denoted as

$$
X \sim \NNN (\mu, \sigma^2).
$$
Its PDF is

$$
f_X( x) = \frac{1}{\sqrt{2 \pi} \sigma} \exp \left ( 
\frac{1}{2} \frac{(x -\mu)^2}{\sigma^2}.
\right)
$$
A simple transformation 

$$
Y  = \frac{X - \mu}{\sigma}
$$
converts it into standard normal random variable.

The mean:

$$
\EE (X) = \mu.
$$
The mean square value:

$$
\EE (X^2) = \sigma^2 + \mu^2.
$$
The variance:

$$
\EE (X^2) - \EE (X)^2 = \sigma^2.
$$
The CDF:

$$
F_X(x) = \frac{1}{2} + \frac{1}{2}  \erf \left ( \frac{x - \mu}{\sigma\sqrt{2}}\right).
$$
Notice the transformation from $x$ to $(x - \mu) / \sigma$.

The characteristic function:

$$
\Psi_X(j\omega) = \exp\left (j \omega \mu - \frac{\omega^2 \sigma^2}{2}\right ).
$$
Naturally putting $\mu = 0$ and $\sigma = 1$, it reduces
to the CF of the standard normal r.v.

Th MGF:

$$
M_X(t) = \exp\left (\mu t  + \frac{\sigma^2 t^2}{2}\right ).
$$

Skewness is zero and Kurtosis is zero.
