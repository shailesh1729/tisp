# Stability of the Sparsest Solution

We discuss various results related to the stability
of the sparsest solution for the sparse recovery problem.

```{div}
For convenience, we restate the problem.
We measure the sparse signal $\bx \in \CC^N$
via a sensing matrix $\Phi$ as
$\by = \Phi \bx + \be$ where
$\be$ is the measurement error and $\by$ is the
measurement vector.
The sparse recovery problem in the presence of noise is:

```{math}
:label: eq-sr-sparse-rec-error-bound
\widehat{\bx} = \text{arg } \underset{\bx \in \CC^N}{\min} 
\| \bx \|_0 \text{ subject to }  \| \by - \Phi \bx \|_2 \leq \epsilon.    
```



## Stability of sparsest solution  using RIP



````{prf:theorem}
:label: res:ssm:stability_p_0_eps_RIP
Consider an instance of the {eq}`eq-sr-sparse-rec-error-bound` problem
defined by the triplet $(\Phi, \by, \epsilon)$.
Let $\Phi$ satisfy RIP of order 2K.
Suppose that a sparse vector $\bx \in \CC^N$ with $\| \bx \|_0 = K$
is a feasible solution of {eq}`eq-sr-sparse-rec-error-bound`.
Then, every solution $\widehat{\bx}$ of {eq}`eq-sr-sparse-rec-error-bound`  must obey

$$
\| \widehat{\bx} - \bx \|_2^2 \leq \frac{4 \epsilon^2}{1 - \delta_{2K}}.
$$
Further, if 

$$
\| \bx \|_0  < \frac{1}{2} \left (1  + \frac{1}{\mu} \right) 
$$
then the following also holds:

$$
\|\widehat{\bx} - \bx \|_2^2 \leq \frac{4 \epsilon^2}{ 1 - \mu ( 2 \| \bx \|_0 - 1)}.
$$
````
````{prf:proof}
.

1. Let $\widehat{\bx}$ be an alternative solution to {eq}`eq-sr-sparse-rec-error-bound`.
1. Defining $\bz = \widehat{\bx} - \bx$,
   
   $$
    \| \Phi \bz \|_2 \leq 2 \epsilon.
   $$
1. Further 
   
   $$
    \| \bz \|_0 
    = \| \bx - \widehat{\bx} \|_0 
    \leq \| \bx \|_0  + \| \widehat{\bx} \|_0 \leq 2 K
   $$
   since $ \| \widehat{\bx} \|_0 \leq \| \bx \|_0  = K$.
1. Since $\Phi$ satisfies RIP of order 2K, hence
   
   $$
    (1 - \delta_{2K}) \| \bz \|_2^2 
    \leq \| \Phi \bz \|_2^2 \leq (1 + \delta_{2K}) \| \bz \|_2^2.
   $$
1. This gives us
   
   $$
    (1 - \delta_{2K}) \| \bz \|_2^2  \leq 4 \epsilon^2.
   $$
1. Rewriting we get
   
   $$
    \| \bz \|_2^2 \leq \frac{4 \epsilon^2}{1 - \delta_{2K}}
   $$
   which is the desired result.

Coherence:

1. We recall from {prf:ref}`res:proj:rip_coherence_bound` that
   
   $$
    \delta_{2K} \leq (2K - 1) \mu.
   $$
1. Thus,
   
   $$
    1 - \delta_{2K} \geq 1 - (2K - 1) \mu 
    \implies \frac{4 \epsilon^2}{1 - \delta_{2K}} 
    \leq \frac{4 \epsilon^2}{1 - (2K - 1) \mu }.
   $$
1. This is useful only if the denominator is positive, i.e.
   
   $$
    1 - (2K - 1) \mu > 0 \implies \frac{1}{\mu} > 2K - 1 
    \implies K < \frac{1}{2} \left (1 +  \frac{1}{\mu}\right).
   $$
1. Under this condition, we get the result
   
   $$
    \| \bz \|_2^2 \leq \frac{4 \epsilon^2}{1 - (2K - 1) \mu }.
   $$
````




