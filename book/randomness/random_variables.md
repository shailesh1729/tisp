# Random Variables

For different random variables, we will
characterize their distributions by several
parameters. These are listed below


*  Probability density function (PDF)
*  Cumulative distribution function (CDF)
*  Probability mass function (PMF)
*  Mean  ($\mu$ or $\EE(X)$)
*  Variance ($\sigma^2$ or $\Var(X)$)
*  Skew
*  Kurtosis
*  Characteristic function (CF)
*  Moment generating function (MGF)
*  Second characteristic function 
*  Cumulant generating function (CGF)


## Cumulative Distribution Function

The CDF is defined as

$$
F_X (x)  = \PP ( X \leq x).
$$

Properties of CDF:

$$
F_X(x) \geq 0, \quad F_X(-\infty) = 0, \quad F_X(\infty) = 1.
$$
CDF is a monotonically non-decreasing function.

$$
x_1 < x_2 \implies F_X(x_1) \leq F_X(x_2).
$$

$F_X(-\infty)$ is defined as

$$
F_X(-\infty) = \lim_{x \to - \infty} F_X(x).
$$
Similarly:

$$
F_X(\infty) = \lim_{x \to \infty} F_X(x).
$$

$F_X(x)$ is right continuous. 

$$
\lim_{x \to t^+} F_X(x) = F_X(t).
$$

## Probability Density Function

Properties of PDF

$$
f_X(x) \geq 0.
$$

$$
\int_{-\infty}^{\infty} f_X(x) d x = 1.
$$

The CDF and PDF are related as

$$
F_X(x) = \int_{-\infty}^x f_X(t ) d t.
$$


## Expectation

Expectation of a discrete random variable:

$$
\EE (X) = \sum_{x} x p_X(x). 
$$

Expectation of a continuous random variable:

$$
\EE (X) = \int_{- \infty}^{\infty} t f_X(t) d t.
$$

Expectation of a function of a random variable:

$$
\EE [g(X)] = \int_{- \infty}^{\infty} g(t) f_X(t) d t.
$$

Mean square value:

$$
\EE [X^2] = \int_{- \infty}^{\infty} t^2 f_X(t) d t.
$$

Variance:

$$
\Var(X) = \EE [X^2] - \EE [X]^2.
$$

$n$-th moment:

$$
\EE [X^n] = \int_{- \infty}^{\infty} t^n f_X(t) d t.
$$

## Characteristic Function

The *characteristic function* is defined as

$$
\Psi_X(j \omega) \triangleq \EE \left [ \exp (j \omega X) \right ].
$$

PDF as Fourier transform of CF.

$$
\Psi_X(j\omega) = \int_{-\infty}^{\infty} e^{j \omega x} f_X(x) d x.
$$

$$
f_X(x) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{-j \omega x} \Psi_X(j\omega) d \omega
$$

$$
\Psi_X(j 0) = \EE (1)  = 1.
$$

```{div}
$$
\left. \frac{d}{ d \omega} \Psi_X(j\omega) \right |_{\omega = 0} = j \EE [X].
$$

$$
\left. \frac{d^2}{ d \omega^2} \Psi_X(j\omega) \right |_{\omega = 0} = j^2 \EE [X^2] = - \EE [X^2].
$$

$$
\EE [X^k] = \frac{1}{j^k}  \left. \frac{d^k}{ d \omega^k} \Psi_X(j\omega) \right |_{\omega = 0}.
$$

Let $Y_1, \dots, Y_k$ be independent. Then

$$
\Psi_{Y_1 + \dots + Y_k} (j \omega) = \prod_{Y_1, \dots, Y_K} \EE [ \exp (j \omega Y_i)].
$$
```




## Moment Generating Function

```{div}
The *moment generating function* is defined as

$$
M_X(t) \triangleq \EE \left [ \exp (t X) \right ].
$$
```