# Random Vectors

We will continue to use the notation of capital letters to denote a random vector. We will specify the
space over which the random vector is generated to clarify the dimensionality.

A real random vector $X$ takes values in the vector space $\RR^n$.
A complex random vector $Z$ takes values in the vector space $\CC^n$.
We write

$$
X = 
\begin{bmatrix}
X_1 \\ \vdots \\ X_n
\end{bmatrix}.
$$

The expected value or mean of a random vector is $\EE(X)$. 

$$
\EE(X) = 
\begin{bmatrix}
\EE(X_1) \\ \vdots \\ \EE(X_n)
\end{bmatrix}.
$$

Covariance-matrix of a random vector:

$$
\Cov (X)  = \EE [(X - \EE(X)) (X - \EE(X))^T] = \EE [X X^T] - \EE[X] \EE[X]^T.
$$
We will use the symbols $\mu$ and $\Sigma$ for the mean vector and covariance 
matrix of a random vector $X$. Clearly

$$
\EE [X X^T]  = \Sigma + \mu \mu^T.
$$


Cross-covariance matrix of two random vectors:

$$
\Cov (X, Y)  = \EE [(X - \EE(X)) (Y - \EE(Y))^T]
= \EE [X Y^T] - \EE[X] \EE[Y]^T.
$$
Note that

$$
\Cov (X, Y)  =\Cov (Y, X)^T. 
$$

The characteristic function is defined as

$$
\Psi_X(j\omega) = \EE \left ( \exp (j \omega^T X) \right ), \quad \omega \in \RR^n.
$$
The MGF is defined as

$$
M_X(t) = \EE \left ( \exp (t^T X) \right ), \quad t \in \CC^n.
$$

````{prf:theorem}
:label: res-prob-r-vec-independence

The components $X_1, \dots, X_n$ of a random vector $X$ are independent if and only if

$$
\Psi_X(j\omega) = \prod_{i=1}^n \Psi_{X_i}(j\omega_i), \quad \forall  \omega \in \RR^n.
$$
````
