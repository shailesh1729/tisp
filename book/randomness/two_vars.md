# Two Variables

Let $X$ and $Y$ be two random variables and
let $F_(X, Y)(x, y)$ be their joint CDF.

$$
\lim_{\substack{x \to -\infty\\ y \to -\infty}} F_{X, Y} (x, y)  = 0.
$$

$$
\lim_{\substack{x \to \infty\\ y \to \infty}} F_{X, Y} (x, y)  = 1.
$$

Right continuity:

$$
\lim_{x \to x_0^+} F_{X, Y} (x, y)  = F_{X, Y} (x_0, y).
$$

$$
\lim_{y \to y_0^+} F_{X, Y} (x, y)  = F_{X, Y} (x, y_0).
$$

The joint probability density function is given by $f_{X, Y} (x, y)$. It satisfies $f_{X, Y} (x, y) \geq 0$ and

$$
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X, Y} (x, y) d y d x = 1.
$$

The joint CDF and joint PDF  are related by

$$
F_{X, Y} (x, y) = \PP (X \leq x, Y \leq y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f_{X, Y} (u , v) d v d u.
$$
Further

$$
\PP (a \leq X \leq b, c \leq Y \leq d) = \int_{a}^{b} \int_{c}^{d} f_{X, Y} (u , v) d v d u.
$$
The marginal probability is

$$
\PP (a \leq X \leq b) = \PP (a \leq X \leq b, -\infty \leq Y \leq \infty) = \int_{a}^{b} \int_{-\infty}^{\infty} f_{X, Y} (u , v) d v d u.
$$
We define the marginal density functions as

$$
f_X(x) = \int_{-\infty}^{\infty} f_{X, Y} (x, y) d y
$$
and

$$
f_Y(y) = \int_{-\infty}^{\infty} f_{X, Y} (x, y) d x.
$$
We can now write

$$
\PP (a \leq X \leq b) =  \int_{a}^{b} f_X(x) d x.
$$
Similarly

$$
\PP (c \leq Y \leq d) =  \int_{c}^{d} f_Y(y) d y.
$$


## Conditional Density

We define

$$
\PP (a \leq x \leq b | y = c) = \int_{a}^{b} f_{X | Y}(x | y = c) d x.
$$
We have

$$
f_{X | Y}(x | y = c) = \frac{f_{X, Y} (x, c)}{f_{Y} (c)}.
$$
In other words

$$
f_{X | Y}(x | y = c) f_{Y} (c) = f_{X, Y} (x, c).
$$
In general we write

$$
f_{X | Y}(x | y) f_Y(y) = f_{X, Y} (x, y).
$$
Or even more loosely as

$$
f(x | y) f(y) = f(x, y).
$$
More identities

$$
f(x | y \leq d) = \frac{ \int_{-\infty}^d  f(x, y)  d y} {\PP (y \leq d)}.
$$


## Independent Variables

If $X$ and $Y$ are independent then

$$
f_{X, Y}(x, y)  = f_X(x) f_Y(y).
$$

$$
f(x | y)  = \frac{f(x, y)}{f(y)} = \frac{f(x) f(y)}{f(y)} = f(x).
$$
Similarly

$$
f(y | x) = f(y).
$$

The CDF also is separable

$$
F_{X, Y}(x, y)  = F_X(x) F_Y(y).
$$









