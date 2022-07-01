# Multivariate Gaussian Distribution



````{prf:definition}
:label: def:prob:gaussian_random_vector

A random vector $X = [X_1, \dots, X_n]^T$ is called *Gaussian random vector* if 

$$
\langle t , X \rangle = X^T t = \sum_{i = 1}^n t_i X_i  = t_1 X_1 + \dots + t_n X_n
$$
follows a normal distribution for all $t = [t_1, \dots, t_n ]^T \in \RR^n$. 
The components $X_1, \dots, X_n$ are called *jointly Gaussian*. It is denoted
by $X \sim \NNN_n (\mu, \Sigma)$ where $\mu$ is its mean vector and $\Sigma$ 
is its covariance matrix. 
````


Let $X \sim \NNN_n (\mu, \Sigma)$ be a Gaussian random vector. 
The subscript $n$ denotes that it takes values over the space $\RR^n$.
We assume that  $\Sigma$ is invertible. 
Its PDF is given by

$$
    f_X (x) = \frac{1}{(2\pi)^{n / 2} \det (\Sigma)^{1/2} } \exp \left \{- \frac{1}{2} (x - \mu)^T \Sigma^{-1}  (x - \mu) \right\}.
$$

Moments:

$$
    \EE [X] = \mu \in \RR^n.
$$

$$
    \EE[XX^T] = \Sigma + \mu \mu^T.
$$

$$
    \Cov[X] = \EE[XX^T] - \EE[X]\EE[X]^T = \Sigma.
$$


Let $Y = A X + b$ where $A \in \RR^{n \times n}$ is an invertible matrix and $b \in \RR^n$. Then

$$
    Y \sim \NNN_n (A \mu + b  , A \Sigma A^T). 
$$

$Y$ is also a Gaussian random vector with the mean vector being $A \mu + b$ and the covariance 
matrix being $A \Sigma A^T$. This essentially is a change in basis in $\RR^n$.

The CF is given by

$$
    \Psi_X(j \omega) \exp \left ( j \omega^T x - \frac{1}{2} \omega^T \Sigma \omega \right ), \quad \omega \in \RR^n.
$$



## Whitening


Usually we are interested in making the components of $X$ uncorrelated. This process is
known as whitening. We are looking for a linear transformation $Y = A X + b$ such that
the components of $Y$ are uncorrelated. i.e. we start with

$$
    X \sim \NNN_n (\mu, \Sigma)
$$
and transform $Y = A X + b$ such that

$$
    Y \sim \NNN_n (0, I_n)
$$
where $I_n$ is the $n$-dimensional identity matrix.

### Whitening by Eigen Value Decomposition
Let

$$
\Sigma = E \Lambda E^T
$$
be the eigen value decomposition of $\Sigma$ with $\Lambda$ being a diagonal matrix and $E$ 
being an orthonormal basis.

Let 

$$
\Lambda^{\frac{1}{2}} = \Diag (\lambda_1^{\frac{1}{2}}, \dots, \lambda_n^{\frac{1}{2}}).
$$

Choose $B = E \Lambda^{\frac{1}{2}}$ and $A = B^{-1} = \Lambda^{-\frac{1}{2}} E^T$.  
Then 

$$
\Cov (B^{-1} X) = \Cov (A X) =  \Lambda^{-\frac{1}{2}} E^T \Sigma E \Lambda^{-\frac{1}{2}} = I. 
$$

$$
\EE [B^{-1} X] = B^{-1} \mu \iff \EE [B^{-1} (X - \mu)]  = 0.
$$
Thus the random vector $Y = [B^{-1} (X - \mu)$ is a whitened vector of uncorrelated components.

 
### Causal Whitening


We want that the transformation be causal, i.e. $A$ should be a lower triangular matrix. We start with

$$
\Sigma = L D L^T = (L D^{\frac{1}{2}} ) (D^{\frac{1}{2}} L^T).
$$
Choose $B = L D^{\frac{1}{2}} $ and $A = B^{-1} = D^{-\frac{1}{2}} L^{-1}$. Clearly, $A$
is lower triangular.

The transformation is $Y = [B^{-1} (X - \mu)$. 



