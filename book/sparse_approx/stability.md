# Stability of the Sparsest Solution

We discuss various results related to the stability
of the sparsest solution for the sparse approximation problem.

````{div}
For convenience, we restate the problem.
We represent the signal $\bx \in \CC^N$ as
$\bx = \bDDD \ba + \be$ where
$\ba$ is a sparse approximation of $\bx$ in $\bDDD$.

```{math}
:label: eq-sa-sparse-approx-error-bound
\widehat{\ba} = \text{arg } \underset{\ba \in \CC^D}{\min} \| \ba \|_0 \text{ subject to }  \| \bx - \bDDD \ba \|_2 \leq \epsilon.    
```

Since we only know $\bx$ and $\bDDD$
(both $\ba$ and $\be$ are unknown to us),
hence in general it is not possible to 
reconstruct $\ba$ exactly.
The term $\bd = \ba - \widehat{\ba}$
will represent the reconstruction error (note that
it is different from the approximation error $\be$).
It is important for us to ensure that the solution of 
the approximation problem is stable; i.e.,
in the presence of small approximation error $\| \be \|_2$,
the reconstruction error $\| \bd \|_2$ should also be small.
For the sparse approximation problem {eq}`eq-sa-sparse-approx-error-bound`,
we cannot provide a uniqueness guarantee as such.
Still, we can identify criteria which ensure
that the solution remains stable when the approximation error is bounded.  
Our analysis in this section will focus on identifying criteria
which ensures this.

We start with generalizing the notion of spark for the noisy case.
1. Suppose $\ba$ and $\bb$ are two solutions of
   {eq}`eq-sa-sparse-approx-error-bound`.
1. Then $\|\bDDD \ba - \bx \|_2 \leq \epsilon$
   as well as  $\| \bDDD \bb - \bx \|_2 \leq \epsilon$.
1. Thus, both $\bDDD \ba$ and $\bDDD \bb$ lie in a ball of radius $\epsilon$
   around $\bx$.
1. Thus, the maximum distance between $\bDDD \ba$ and $\bDDD \bb$
   can be $2 \epsilon$. 
1. Alternatively, using triangle inequality we have
   
   $$
    \| \bDDD (\ba - \bb) \|_2 
    &= \| \bDDD \ba -  \bx + \bx - \bDDD \bb) \|_2 \\
    & \leq \| \bDDD \ba -  \bx \|_2 + \| \bx - \bDDD \bb) \|_2 \leq 2 \epsilon.
   $$
1. If we define $\bd = \ba - \bb$, then
   
   $$
    \| \bDDD \bd  \|_2 \leq 2 \epsilon.
   $$
````

## Spark $\eta$



````{prf:definition}
:label: def:ssm:spark_eta

Let $\bA \in \CC^{N \times D}$ be some matrix.
Consider all possible sub-sets of $K$ columns. 
Let each such set form sub-matrix $\bA_{\Lambda} \in \CC^{N \times K}$
where $\Lambda$ denotes
the index set of $K$ indices chosen.
We define $\spark_{\eta}(\bA)$ as the
smallest possible $K$ (number of columns) that guarantees

$$
\underset{\Lambda}{\min}\sigma_K (\bA_{\Lambda}) \leq \eta
$$
where $\sigma_K$ denotes the smallest singular value (i.e. $K$-th singular value) of the sub-matrix $\bA_{\Lambda}$.
Note that we are minimizing over all possible index sets
$\Lambda$ with $| \Lambda | = K$.
````
In words, this is the smallest number of columns (indexed by $\Lambda$)
that can be gathered from $\bA$ such 
that the smallest singular value of $\bA_{\Lambda}$
is no larger than $\eta$; i.e., there exists
a sub-matrix of $\bA$ consisting of $\spark_{\eta}(\bA)$ columns
whose smallest singular value is 
$\eta$ or less.
At the same time, all submatrices of $\bA$ with number of columns
less than $\spark_{\eta}(\bA)$
have the smallest singular value larger than $\eta$.

````{div}

Relationship with $\spark$:

1. When the smallest singular value is $0$,
   then the columns are linearly dependent.
1. Thus, by choosing $\eta = 0$, we get the smallest number of columns
   $K$ which are linearly dependent.
1. This matches with the definition of spark.
1. Thus,
   
   $$
    {\spark}_0 (\bA)  = \spark (\bA).
   $$
1. Since singular values are always non-negative, hence $\eta \geq 0$.

Matrix with unit norm columns:

1. When columns of $\bA$ are unit-norm (the case of dictionaries), then
   any single column sub-matrix has a singular value of $1$. Hence,
   
   $$
    {\spark}_1(\bA) = 1.
   $$
1. Choosing a value of $\eta > 1$ doesn't make any difference since
   with a single column sub-matrix, we can show that
   
   $$
    {\spark}_{\eta}(\bA) = 1 \Forall \eta \geq 1.
   $$

Monotonicity:

1. Let $\eta_1 > \eta_2$. Let 
   
   $$
    K_2 = {\spark}_{\eta_2} (\bA).
   $$
1. Then there exists a sub-matrix consisting of $K_2$ columns of $\bA$
   whose smallest singular value is upper bounded by $\eta_2$.
1. Since $\eta_1 > \eta_2$, $\eta_1$  also serves as an upper bound
   for the smallest singular value for this sub-matrix.
1. Clearly then $K_1 = \spark_{\eta_1}(\bA) \leq K_2$.
1. Thus, we note that ${\spark}_{\eta}$ is a monotone decreasing function
   of $\eta$. i.e.
   
   $$
    {\spark}_{\eta_1} (\bA) \leq {\spark}_{\eta_2} (\bA),
    \text{ whenever } \eta_1 > \eta_2.
   $$

Maximum value:

1. We recall that the spark of $\bA$ is upper bounded by its rank plus one.
1. Assuming $\bA$ to be  a full rank matrix, we get following inequality:
   
   $$
    1 \leq {\spark}_{\eta} (\bA) 
    \leq {\spark}_0(\bA) 
    = \spark(\bA) \leq N + 1 
    \Forall  0 \leq \eta \leq 1.
   $$

We recall that if $\bA \bv = \bzero$ then
$\| \bv \|_0 \geq \spark(\bA)$. A similar property can be
developed for $\spark_{\eta}(\bA)$ also.
````

````{prf:theorem}
:label: res:ssm:spark_eta_null_vec_length

If $\| \bA \bv \|_2 \leq \eta$ and $\| \bv \|_2 = 1$,
then $ \| \bv \|_0 \geq \spark_{\eta} (\bA)$.
````
````{prf:proof}
For contradiction, let us assume that $ K = \| \bv \|_0 < {\spark}_{\eta}(\bA)$.
1. Let $\Lambda = \supp (\bv)$.
1. Then $\bA \bv = \bA_{\Lambda} \bv_{\Lambda}$.
1. Also $\| \bv_{\Lambda} \|_2 = \| \bv \|_2 = 1$.
1. We recall that the smallest singular value of $\bA_{\Lambda}$ is given by
   
   $$
    \sigma_{\text{min}} (\bA_{\Lambda})
    = \underset{\| \bx \|_2 = 1}{\inf} \| \bA_{\Lambda} \bx \|_2.
   $$
1. Thus,
   
   $$
    \| \bA_{\Lambda} \bx \|_2 \geq \sigma_{\text{min}} (\bA_{\Lambda})
    \text{ whenever } \| \bx \|_2  = 1.
   $$
1. Thus, in our particular case
   
   $$
    \| \bA_{\Lambda} \bv_{\Lambda} \|_2 \geq \sigma_{\text{min}}(\bA_{\Lambda}).
   $$
   $\bA_{\Lambda}$ has $K$ columns with $K < \spark_{\eta} (\bA)$.
1. Thus, from the definition of $\spark_{\eta} (\bA)$
   
   $$
    \sigma_{\text{min}} (\bA_{\Lambda}) > \eta.
   $$
1. This gives us
   
   $$
    \| \bA \bv \|_2  = \| \bA_{\Lambda} \bv_{\Lambda} \|_2  > \eta
   $$
   which contradicts with the assumption that $\| \bA \bv \|_2 \leq \eta$. 
````
### Coherence

In the following, we will focus on the $\spark_{\eta}$ of
a full rank dictionary $\bDDD$.
We now establish a connection between $\spark_{\eta}$
and coherence of a dictionary.


````{prf:theorem}
:label: res:ssm:spark_eta_coherence_bound

Let $\bDDD$ be a full rank dictionary with coherence $\mu$. Then

```{math}
:label: eq:ssm:spark_eta_coherence_bound
{\spark}_{\eta} (\bDDD) \geq \frac{1 - \eta^2}{ \mu} + 1.
```
````

````{prf:proof}
.

1. We recall from Gershgorin's theorem that for any square matrix
   $\bA \in \CC^{K \times K}$, 
   every eigen value $\lambda$ of $\bA$ satisfies 
   
   $$
    | \lambda  - a_{i i} | 
    \leq \sum_{j, j \neq i} |a_{i j}| 
    \text{ for some } i \in \{ 1, \dots, K\}.
   $$
1. Now consider a matrix $\bA$ with diagonal elements equal to 1 and
   off diagonal elements bounded by a value $\mu$.
1. Then
   
   $$
    | \lambda  - 1 | \leq \sum_{j, j \neq i} |a_{i j}|
    \leq \sum_{j \neq i} \mu = (K - 1) \mu.
   $$
1. Thus,
   
   $$
    & - (K - 1) \mu  
    \leq \lambda  - 1 
    \leq (K - 1) \mu \\ 
    \iff &  1 - (K - 1)   \mu  \leq \lambda \leq 1 + (K - 1)   \mu.
   $$
1. This gives us a lower bound on the smallest eigen value.
   
   $$
    \lambda_{\min} (\bA) \geq 1 - (K - 1) \mu.
   $$
1. Now consider any index set $\Lambda \subseteq \{ 1, \dots, D \}$
   and consider the submatrix $\bDDD_{\Lambda}$
   with $|\Lambda | = {\spark}_{\eta}(\bDDD) = K$.
1. Define $\bG = \bDDD_{\Lambda}^H \bDDD_{\Lambda}$.
1. The diagonal  elements of $\bG$ are one,
   while off-diagonal elements are bounded by $\mu$.
1. Thus,
   
   $$
    & \lambda_{\min} (\bG) \geq 1 - (K - 1) \mu \\
    \iff & (K - 1) \mu \geq 1 - \lambda_{\min} (\bG)\\
    \iff & K - 1 \geq \frac{1 - \lambda_{\min} (\bG)}{\mu}\\
    \iff & K \geq \frac{1 - \lambda_{\min} (\bG)}{\mu} + 1.
   $$
1. Since this applies to every sub-matrix $\bDDD_{\Lambda}$,
   this in particular applies to the sub-matrix
   for which $\sigma_{\min}(\bDDD_{\Lambda}) \leq \eta$ holds.
1. For this sub-matrix
   
   $$
    \lambda_{\min}(\bDDD_{\Lambda}^H \bDDD_{\Lambda})
    = \sigma_{\min}^2(\bDDD_{\Lambda}) \leq \eta^2.
   $$
1. Thus
   
   $$
    K = {\spark}_{\eta} (\bDDD) 
    \geq \frac{1 - \lambda_{\min} (\bG)}{\mu} + 1 
    \geq \frac{1 - \eta^2}{\mu} + 1.
   $$
````


## Uncertainty with Spark $\eta$


We now present an uncertainly result for the noisy case.
````{prf:theorem}
:label: res:ssm:spark_eta_uncertainty

If $\ba_1$ and $\ba_2$ satisfy $\| \bx - \bDDD \ba_i \|_2 \leq \epsilon, i = 1,2$,
then

```{math}
:label: eq:ssm:spark_eta_uncertainty

\| \ba_1 \|_0  + \| \ba_2 \|_0 
\geq {\spark}_{\eta}(\bDDD), \text{ where } \eta = \frac{2 \epsilon}{\| \ba_1  - \ba_2 \|_2}.
```
````
````{prf:proof}
.

1. From triangle inequality we have
   
   $$
    \| \bDDD (\ba_1 - \ba_2) \|_2 \leq 2 \epsilon.
   $$
1. We define $\bb = \ba_1 - \ba_2$.
1. Then $ \| \bDDD \bb \|_2 \leq 2 \epsilon$.
1. Further define $\bv = \bb / \| \bb \|_2$ as the normalized vector. 
1. Then
   
   $$
    \| \bDDD \bv \|_2 
    = \frac{\| \bDDD \bb \|_2}{\| \bb \|_2} 
    \leq \frac{2 \epsilon}{\| \bb \|_2}.
   $$
1. Now define 
   
   $$
    \eta = \frac{2 \epsilon}{\| \bb \|_2} 
    = \frac{2 \epsilon}{\| \ba_1 - \ba_2 \|_2}.
   $$
1. Then from {prf:ref}`res:ssm:spark_eta_null_vec_length`
   if $\| \bDDD \bv \|_2 \leq \eta$ with $\| \bv \|_2 = 1$,
   then $\| \bv \|_0 \geq {\spark}_{\eta}(\bDDD)$.
1. Finally,
   
   $$
    \| \ba_1 \|_0  + \| \ba_2 \|_0 
    \geq \| \ba_1 - \ba_2 \|_0 
    = \| \bb \|_0 
    = \| \bv \|_0 \geq {\spark}_{\eta}(\bDDD).
   $$
1. This concludes the proof.
````
This result gives us a lower bound on the sum of sparsity levels of
two different sparse representations of same vector $\bx$
under the given bound approximation error.

## Localization

We can now develop a localization result
for the sparse approximation up to a Euclidean ball. This is analogous to the
uniqueness result in noiseless case.

````{prf:theorem}
:label: res:ssm:spark_eta_uniqueness

Given a distance $\delta \geq 0$
(bound on distance between two sparse representations) 
and $\epsilon$ (bound on norm of approximation error),
set $\eta = 2 \epsilon / \delta$. 
Suppose there are two approximate representations $\ba_i, i = 1,2$ both obeying

$$
\| \bx - \bDDD \ba_i \|_2 \leq \epsilon 
\, \text{ and }\, 
\| \ba_i \|_0 \leq \frac{1}{2} {\spark}_{\eta} (\bDDD).
$$
Then $\| \ba_1 - \ba_2 \|_2 \leq \delta$.
````
````{prf:proof}
.

1. Since $\| \ba_i \|_0 \leq \frac{1}{2} {\spark}_{\eta} (\bDDD)$, hence
   
   $$
    \| \ba_1 \|_0  + \| \ba_2 \|_0  \leq {\spark}_{\eta} (\bDDD).
   $$
1. From {prf:ref}`res:ssm:spark_eta_uncertainty`, if we define
   
   $$
    \nu  = \frac{2 \epsilon}{ \| \ba_1 - \ba_2\|_2},
   $$
   then
   
   $$
    \| \ba_1 \|_0  + \| \ba_2 \|_0 \geq {\spark}_{\nu}(\bDDD).
   $$
1. Combining the two, we get
   
   $$
    {\spark}_{\eta} (\bDDD) 
    \geq \| \ba_1 \|_0  + \| \ba_2 \|_0 
    \geq {\spark}_{\nu}(\bDDD).
   $$
1. Because of the monotonicity of ${\spark}_{\eta} (\bDDD)$, we have
   
   $$
    {\spark}_{\eta} (\bDDD) 
    \geq {\spark}_{\nu}(\bDDD)
    &\implies \eta \leq \nu \\
    &\implies \frac{2\epsilon}{\delta} \leq \frac{2 \epsilon}{ \| \ba_1 - \ba_2\|_2}\\
    &\implies \delta \geq \| \ba_1 - \ba_2\|_2
   $$
   which completes our proof.
````
This theorem says that if $\bx$ has two different sufficiently sparse 
representations $\ba_i$ with small approximation errors,
they fall within a small distance.


## Stability using Coherence

We can now develop a stability result
for the {eq}`eq-sa-sparse-approx-error-bound` problem
in terms of coherence of the dictionary.

````{prf:theorem}
:label: res:ssm:stability_p_0_eps_coherence

Consider an instance of the {eq}`eq-sa-sparse-approx-error-bound` problem
defined by the triplet $(\bDDD, \bx, \epsilon)$.
Suppose that a sparse vector $\ba \in \CC^D$ satisfies the sparsity constraint

$$
\| \ba \|_0  < \frac{1}{2} \left (1  + \frac{1}{\mu} \right) 
$$
and gives a representation of $\bx$ to within error tolerance $\epsilon$
(i.e. $\| \bx - \bDDD \ba\|_2 \leq \epsilon$).
Every solution $\widehat{\ba}$ of {eq}`eq-sa-sparse-approx-error-bound` must obey

$$
\|\widehat{\ba} - \ba \|_2^2 
\leq \frac{4 \epsilon^2}{ 1 - \mu ( 2 \| \ba \|_0 - 1)}.
$$

````
````{prf:proof}
.

1. Note that $\ba$ need not be sparsest possible representation of $\bx$
   within the approximation error $\epsilon$. 
1. But $\ba$ is a feasible point of {eq}`eq-sa-sparse-approx-error-bound`.
1. Now since $\widehat{\ba}$ is an optimal solution of
  {eq}`eq-sa-sparse-approx-error-bound` (thus sparsest possible), 
   hence it is at least as sparse as
   $\ba$; i.e.,
   
   $$
    \| \widehat{\ba} \|_0 \leq \| \ba \|_0.
   $$
1. Due to {prf:ref}`lem:ssm:spark_lower_bound_coherence`, 
   
   $$
    \frac{1}{2} \spark(\bDDD) 
    \geq \frac{1}{2} \left (1  + \frac{1}{\mu} \right) > \| \ba \|_0.
   $$
1. Thus, there exists a value $\eta \geq 0$ such that
   
   $$
    \frac{1}{2} \spark(\bDDD) 
    \geq \frac{1}{2} {\spark}_{\eta} (\bDDD) 
    \geq \| \ba \|_0 \geq \| \widehat{\ba} \|_0.
   $$
1. From {prf:ref}`res:ssm:spark_eta_coherence_bound` we recall that
   
   $$
    {\spark}_{\eta} (\bDDD) \geq \frac{1 - \eta^2}{ \mu} + 1.
   $$
1. Thus, we can find a suitable value of $\eta \geq 0$
   such that we can enforce a stricter requirement:
   
   $$
    \| \ba \|_0 \leq \frac{1}{2} \left ( \frac{1 - \eta^2}{ \mu} + 1 \right )
    \leq \frac{1}{2}{\spark}_{\eta} (\bDDD).
   $$
1. From this we can develop an upper bound on $\eta$ being
   
   $$
    \| \ba \|_0 \leq \frac{1}{2} \left ( \frac{1 - \eta^2}{ \mu} + 1 \right ) 
    &\iff 2 \| \ba \|_0 \mu \leq 1 - \eta^2 + \mu \\
    &\iff \eta^2 \leq 1 - \mu (2 \| \ba \|_0 - 1). 
   $$
1. If we choose $\eta^2 = 1 - \mu (2 \| \ba \|_0 - 1)$, then
   
   $$
    \| \ba \|_0 = \frac{1}{2} \left ( \frac{1 - \eta^2}{ \mu} + 1 \right ) 
    & \implies \| \ba \|_0 \leq \frac{1}{2} {\spark}_{\eta} (\bDDD)\\ 
    & \implies \| \widehat{\ba} \|_0 
    \leq \| \ba \|_0 \leq \frac{1}{2} {\spark}_{\eta} (\bDDD) 
   $$
   continues to hold.
1. We have two solutions $\ba$ and $\widehat{\ba}$ both of which satisfy
   
   $$
    \| \ba \|_0, \| \widehat{\ba} \|_0 \leq \frac{1}{2} {\spark}_{\eta} (\bDDD)
   $$
   and 
   
   $$
    \| \bx  - \bDDD \ba \|_2, \| \bx  - \bDDD \widehat{\ba} \|_2 \leq \epsilon. 
   $$
1. If we choose a $\delta = \frac{2 \epsilon}{\eta}$, then 
   applying {prf:ref}`res:ssm:spark_eta_uniqueness`, we will get
   
   $$
    \| \ba - \widehat{\ba} \|_2^2 
    \leq \delta^2 = \frac{4 \epsilon^2}{\eta^2} 
    = \frac{4 \epsilon^2}{1 - \mu (2 \| \ba \|_0 - 1)}.
   $$
````

