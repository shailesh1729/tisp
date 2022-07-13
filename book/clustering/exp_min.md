(sec:ml:cluster:em)=
# Expectation Maximization

Expectation-Maximization (EM)
{cite}`dempster1977maximum` method is a maximum
likelihood based estimation paradigm. It requires 
an explicit probabilistic model of the mixed data-set.
The algorithm estimates model parameters and the
segmentation of data in Maximum-Likelihood (ML) sense.

We assume that $\by_s$ are samples drawn from 
multiple "component" distributions and each 
component distribution is centered around a mean.
Let there be $K$ such component distributions.
We introduce a latent (hidden) discrete random
variable $z \in \{1, \dots, K\}$ associated with the
random variable  $\by$ such that $z_s = k$ if $\by_s$
is drawn from $k$-th component distribution. The
random vector $(\by, z) \in \RR^M \times \{1, \dots, K\}$ 
completely describes the event that a point $\by$
is drawn from a component indexed by the value of $z$.

We assume that $z$ is subject to a multinomial (marginal)
distribution. i.e.:

$$
p(z= k) = \pi_k \geq 0, \quad 
\pi_1 + \dots + \pi_K = 1.
$$
````{div}
Each component distribution can then be modeled as a
conditional (continuous) distribution $f(\by | z)$.
If each of the components is a multivariate normal distribution,
then we have $f(\by | z = k) \sim \NNN(\mu_k, \Sigma_k)$
where $\mu_k$ is the mean and $\Sigma_k$ is the covariance
matrix of the $k$-th component distribution.
The parameter set for this model is then 
$\theta = \{\pi_k, \mu_k, \Sigma_K \}_{k=1}^K$
which is unknown in general and needs to be estimated from
the dataset $\bY$. 

With $(\by, z)$ being the complete random 
vector, the marginal PDF of $\by$ given $\theta$ is given by

$$
f(\by | \theta) = \sum_{z = 1}^K f(\by | z, \theta) p (z | \theta)
= \sum_{z = 1}^K \pi_k f(\by | z=k, \theta).
$$
The log-likelihood function for the dataset 

$$
\bY = \{ \by_s\}_{s=1}^N
$$
is given by

$$
l (\bY; \theta) = \sum_{s=1}^S \ln f(\by_s | \theta).
$$
An ML estimate of the parameters, namely $\hat{\theta}_{\ML}$ 
is obtained by maximizing $l (\bY; \theta)$ over the
parameter space.
The statistic $l (Y; \theta)$ is called
*incomplete log-likelihood function*
since it is marginalized over $z$.
It is very difficult to compute and maximize directly.
The EM method provides an alternate
means of maximizing $l (\bY; \theta)$ by
utilizing the latent r.v. $z$.

We start with noting that

$$
f(\by | \theta) p ( z | \by , \theta) = f(\by, z | \theta), 
$$

$$
\sum_{k=1}^K p(z = k | \by , \theta) = 1.
$$
Thus, $l (\bY; \theta)$ can be rewritten as

$$
l (\bY; \theta) 
&= \sum_{s=1}^S \sum_{k=1}^K p(z_s = k | \by_s , \theta)
\ln \frac{f(\by_s, z_s =k | \theta)}{p(z_s=k | \by_s, \theta)}\\
&= \sum_{s, k}  p(z_s = k | \by_s , \theta) 
\ln f(\by_s, z_s =k | \theta) \\
&- \sum_{s, k}  p(z_s = k | \by_s , \theta) 
\ln p(z_s=k | \by_s, \theta) .
$$
The first term is 
*expected complete log-likelihood function*
and the second term is the 
*conditional entropy* of $z_s$ given $\by_s$ 
and $\theta$.

Let us introduce auxiliary variables
$w_{s k} (\theta) = p(z_s = k | \by_s , \theta)$.
$w_{s k}$ represents the expected membership
of $\by_s$ in the $k$-th cluster.
Put $w_{sk}$ in a matrix $\bW (\theta)$ and write:

$$
l'(\bY; \theta, \bW) = \sum_{s=1}^S \sum_{k=1}^K 
w_{s k} \ln f(\by_s, z_s =k | \theta).
$$

$$
h( z | \by;  \bW) = - \sum_{s=1}^S \sum_{k=1}^K 
w_{s k} \ln w_{sk}.
$$
Then, we have

$$
l(\bY; \theta, \bW) = l'(\bY; \theta, \bW)  + h( z | \by;  W)
$$
where, we have written $l$ as a function of
both $\theta$ and $W$.

An iterative maximization
approach can be introduced as follows:

1. Maximize $l(\bY; \theta, \bW)$ w.r.t. $\bW$ keeping 
   $\theta$ as constant.
1. Maximize $l(\bY; \theta, \bW)$ w.r.t. $\theta$ keeping
   $\bW$ as constant.
1. Repeat the previous two steps till convergence. 

This is essentially the EM algorithm. Step 1 is known
as *E-step* and step 2 is known as the *M-step*.
In the E-step, we are estimating the expected membership
of each sample being drawn from each component distribution.
In the M-step, we are maximizing the 
expected complete log-likelihood
function as the conditional entropy term 
doesn't depend on $\theta$.

Using Lagrange multiplier, we can show that the optimal
$\hat{w}_{s k}$ in the E-step is given by

$$
\hat{w}_{sk} = \frac{\pi_k f( \by_s | z_s = k, \theta )}
{\sum_{l=1}^K \pi_l f(\by_s | z_s = l, \theta )}.
$$

A closed form solution for the $M$-step depends on the
particular choice of the component distributions.
We provide a closed form solution for the special
case when each of the components is an
isotropic normal distribution ($\NNN(\mu_k, \sigma_k^2 I)$).

$$
&\hat{\mu_k} = \frac{\sum_{s=1}^S w_{sk} y_s}
{\sum_{s=1}^S w_{sk}},\\
&\hat{\sigma}_k^2 = \frac{\sum_{s=1}^S w_{sk} \| y_s - \mu_k \|_2^2}
{M \sum_{s=1}^S w_{sk}},\\
&\hat{\pi_k} = \frac{\sum_{k=1}^K w_{sk}}{K}.
$$

In $K$-means, each $\by_s$ gets hard assigned to
a specific cluster. In EM, we have a soft assignment
given by $w_{s k}$. 


EM-method is a good method for a hybrid dataset
consisting of mixture of component distributions. 
Yet, its applicability is limited. We need to have
a good idea of the number of components beforehand.
Further, for a Gaussian Mixture Model (GMM), 
it fails to work if the variance in 
some of the directions is arbitrarily small {cite}`vapnik2013nature`.
For example, a subspace like 
distribution is one where the data has large variance
within a subspace but almost zero variance orthogonal
to the subspace. The EM method tends to fail with 
subspace like distributions.
````



