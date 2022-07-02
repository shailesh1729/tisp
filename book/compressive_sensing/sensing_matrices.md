# Sensing Matrices

## Matrices Satisfying RIP

This section provides basic results about construction of matrices which can satisfy
restricted isometry property.

The goal of designing an $M \times N$ sensing matrix involves:

* Stable embedding for signals with has high sparsity as possible (high $K$)
* As few measurements as possible (low $M$)

There are two different approaches

*  Deterministic approach
*  Randomized approach


Known deterministic approaches so far tend to require $M$ to be very large($O(K^2 \ln N)$
or $O(KN^{\alpha}$). 
We can overcome this limitation by randomizing matrix construction.

Construction process:

*  Input $M$ and $N$.
*  Generate $\Phi$ by choosing $\Phi_{i j}$ as independent realizations
   from some probability distribution.

Suppose that $\Phi$ is drawn from normal distribution.

It can be shown that the rank of $\Phi$ is $M$ with probability $1$. 

````{prf:example} Random matrices are full rank.
:label: ex-cs-sm-random-mat-full-rank
We can verify this fact by doing a small computer simulation.

```matlab
M = 6;
N = 20;
trials = 10000;
numFullRankMatrices = 0;
for i=1:trials
    % Create a random matrix of size M x N
    A = rand(M,N);
    % Obtain its rank
    R = rank(A);
    % Check whether the rank equals M or not
    if R == M
        numFullRankMatrices = numFullRankMatrices + 1;
    end
end
fprintf('Number of trials: %d\n',trials);
fprintf('Number of full rank matrices: %d\n',numFullRankMatrices);
percentage = numFullRankMatrices*100/trials;
fprintf('Percentage of full rank matrices: %.2f %%\n', percentage);
```
This program generates a number of random matrices and measures 
their ranks. It verifies whether they are full rank or not.

Here is a sample output:

```matlab
>> demoRandomMatrixRank
Number of trials: 10000
Number of full rank matrices: 10000
Percentage of full rank matrices: 100.00 
```
````
Thus if we choose $M=2K$,
any subset of $2K$ columns will be linearly independent.
Thus the matrix with satisfy RIP with some $\delta_{2K} > 0$.
But this construction doesn't tell us exact value of $\delta_{2K}$.
In order to find out $\delta_{2K}$, we must consider all possible $K$-dimensional
subspaces of $\RR^N$. 
This is computationally impossible for reasonably large $N$ and $K$.
What is the alternative?

We can start with a chosen value of $\delta_{2K}$ and
try to construct a matrix which matches it.

Before we proceed further, we should take a 
detour and review sub-Gaussian distributions in 
{ref}`sec:randomness:subgaussian`.


We now state the main theorem of this section.

````{prf:theorem} Norm bounds on subgaussian vectors
:label: res-cs-subgaussian-norm-bounds

Suppose that $X = [X_1, X_2, \dots, X_M]$ where each $X_i$ is i.i.d. with $X_i \sim \Sub (c^2)$ and
$\EE (X_i^2) = \sigma^2$. Then

$$
\EE (\| X\|_2^2) = M \sigma^2 
$$
Moreover, for any $\alpha \in (0,1)$ and for any
$\beta \in [c^2/\sigma^2, \beta_{\text{max}}$, there exists
a constant $\kappa^* \geq 4$ depending only on  $\beta_{\text{max}}$ and the ratio $\sigma^2/c^2$ such that

$$
\PP(\| X\|_2^2 \leq \alpha M \sigma^2) \leq \exp \left  ( -\frac{M(1-\alpha)^2}{\kappa^*} \right ) 
$$
and   

$$
\PP(\| X\|_2^2 \geq \beta M \sigma^2) \leq \exp \left  ( -\frac{M(\beta-1)^2}{\kappa^*} \right ) 
$$ 
````
## Conditions on Random Distribution for RIP
Let us get back to our business of constructing a matrix $\Phi$
using random distributions which satisfies RIP with a given $\delta$.
We will impose some conditions on the random distribution.

*  We require that the distribution will yield a matrix that is norm-preserving.
   This requires that
    
    ```{math}
    :label: eq:rip_subgaussian_variance

    \EE (\Phi_{ij}^2) = \frac{1}{M}
    ```
   Hence variance of distribution should be $\frac{1}{M}$.
*  We require that distribution is a sub-Gaussian distribution;
   i.e., there exists a constant $c > 0$ 
   such that
   ```{math}
   :label: eq:rip_subgaussian_mgf
    \EE(\exp(\Phi_{ij} t)) \leq \exp \left (\frac{c^2 t^2}{2} \right )
    ```
  This says that the moment generating function of the distribution
  is dominated by a Gaussian distribution.  
  In other words, tails of the distribution decay at least as fast as the tails of a Gaussian distribution.
* We will further assume that entries of $\Phi$ are strictly sub-Gaussian.
  i.e., they must satisfy
  {eq}`eq:rip_subgaussian_mgf` with
  
  $$
  c^2 = \EE (\Phi_{ij}^2) = \frac{1}{M}.
  $$

Under these conditions we have the following result.

````{prf:corollary} Norm bounds on subgaussian matrix vector product
:label: res-cs-subgaussian-rip-2

Suppose that $\Phi$ is an $M\times N$ matrix whose entries $\Phi_{ij}$ are i.i.d. with
$\Phi_{ij}$ drawn according to a strictly sub-Gaussian distribution with $c^2 = \frac{1}{M^2}$.

Let $Y = \Phi x$ for $x \in \RR^N$. Then for any $\epsilon > 0$ and any $x \in \RR^N$,

$$
\EE ( \| Y \|_2^2) = \| x \|_2^2
$$
and

$$
\PP ( \| Y \|^2_2 - \| x \|_2^2 \geq \epsilon \| x \|_2^2 ) 
\leq 2 \exp \left ( - \frac{M \epsilon^2}{\kappa^*} \right) 
$$
where $\kappa^* = \frac{2}{1 - \ln(2)} \approx 6.5178$.
````
This means that the norm of a sub-Gaussian random vector strongly concentrates about its mean.


## Sub Gaussian Matrices satisfy the RIP
Using this result we now state that sub-Gaussian matrices satisfy the RIP.

````{prf:theorem} Lower bound on required number of measurements
:label: res-cs-subgaussian-rip-3

Fix $\delta \in (0,1)$.
Let $\Phi$ be an $M\times N$ random matrix whose entries
$\Phi_{ij}$ are i.i.d. with
$\Phi_{ij}$ drawn according to a
strictly sub-Gaussian distribution with $c^2 = \frac{1}{M}$.
If

$$
M \geq \kappa_1 K \ln \left ( \frac{N}{K} \right ),
$$

then $\Phi$ satisfies the RIP of order $K$ with the prescribed $\delta$
with probability exceeding  $1 - 2e^{-\kappa_2 M}$, where $\kappa_1$ is arbitrary and

$$
\kappa_2 = \frac{\delta^2 }{2 \kappa^*} 
- \frac{1}{\kappa_1} \ln \left ( \frac{42 e}{\delta} \right ) 
$$
````
We note that this theorem achieves $M$ of the same order as the lower bound
obtained in  {prf:ref}`thm:rip_measurement_bound` up to a constant. 

This is much better than deterministic approaches.

## Advantages of Random Construction
There are a number of advantages of the random sensing matrix construction approach:

* One can show that for random construction, the measurements are *democratic*.
  This means that all measurements are equal in importance and it is possible to recover the
  signal from any sufficiently large subset of the measurements.
 
  Thus by using random $\Phi$ one can be robust to the loss of loss or corruption of a small fraction
  of measurements.
* In general we are more interested in $x$ which is sparse in some basis $\Psi$. In this setting,
  we require that $\Phi \Psi$ satisfy the RIP.
  
  Deterministic construction would explicitly require taking $\Psi$ into account.
  
  But if $\Phi$ is random, we can avoid this issue.
  
  If $\Phi$ is Gaussian and $\Psi$ is an orthonormal basis, then one can easily show that $\Phi \Psi$ will also
  have a Gaussian distribution.
  
  Thus if $M$ is high, $\Phi \Psi$ will also satisfy RIP with very high probability.
  
  Similar results hold for other sub-Gaussian distributions as well.