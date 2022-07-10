# Expectation

This section contains several results on expectation operator.

Any function $g(x)$ defines a new random variable $g(X)$. If $g(X)$ has a finite expectation, then

$$
\EE [g(X)] = \int_{-\infty}^{\infty} g(x) f_X(x) d x. 
$$

If several random variables $X_1, \dots, X_n$ are defined on the same sample space, then
their sum $X_1 + \dots + X_n$ is a new random variable. If all of them have
finite expectations, then the expectation of their sum exists and is given by

$$
\EE [X_1 + \dots + X_n] = \EE [X_1] + \dots + \EE [X_n].
$$


If $X$ and $Y$ are mutually independent random variables with finite expectations, then their product is a random variable with finite expectation
and

$$
\EE (X Y) = \EE (X) \EE (Y).
$$
By induction, if $X_1, \dots, X_n$ are mutually independent random variables with finite expectations, then

$$
\EE \left [ \prod_{i=1}^n X_i \right ] = \prod_{i=1}^n \EE \left [  X_i \right ].
$$


Let $X$ and $Y$ be two random variables with the joint density function $f_{X, Y} (x, y)$. 
Let the marginal density function of  $Y$ given $X$ be $f(y | x)$. Then
the conditional expectation is defined as follows:

$$
    \EE [Y | X] = \int_{-\infty}^{\infty} y f(y | x)  d y.
$$
$\EE [Y | X ]$ is a new random variable. 

$$
\EE \left [ \EE [Y | X ] \right ] &= \int_{-\infty}^{\infty} \EE [Y | X] f (x) d x\\
&= \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} y f(y | x) f (x)  d y  d x\\
&= \int_{-\infty}^{\infty}y \left ( \int_{-\infty}^{\infty}  f(x, y) d x \right ) d y  \\
&= \int_{-\infty}^{\infty} y f(y) d y = \EE [Y].
$$

In short, we have

$$
\EE \left [ \EE [Y | X ] \right ] = \EE [Y].
$$

The covariance of $X$ and $Y$ is defined as

$$
\Cov (X, Y) = \EE \left [ (X - \EE[X]) ( Y - \EE[Y]) \right ].
$$
It is easy to see that

$$
\Cov (X, Y) = \EE [X Y] - \EE [X] \EE [ Y].
$$

The *correlation coefficient* is defined as

$$
\rho  \triangleq \frac{\Cov (X, Y)}{\sqrt{Var (X) Var (Y)}}.
$$

## Independent Variables


If $X$ and $Y$ are independent, then

$$
\EE [ g_1(x) g_2 (y)] = \EE [g_1(x)] \EE [g_2 (y)].
$$
If $X$ and $Y$ are independent, then $\Cov (X, Y)  = 0$.

## Uncorrelated Variables

The two variables $X$ and $Y$ are called uncorrelated if $\Cov (X, Y)  = 0$.
Covariance doesn't imply independence.
