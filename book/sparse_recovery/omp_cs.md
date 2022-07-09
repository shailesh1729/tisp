# Orthogonal Matching Pursuit

In this section, we consider the application of Orthogonal Matching Pursuit (OMP)
for the problem of recovering a signal from its compressive measurements. 
This section is largely based on {cite}`tropp2007signal`.

Please review the notation of compressing
sensing process from {prf:ref}`def:ssm:compressed_sensing`. 

We will restrict our attention to the $N$ dimensional Euclidean space
as our signal space for the moment.

1. $\bx \in \RR^N$ is a signal vector. 
1. $\Phi \in \RR^{M \times N}$ is the real sensing matrix with $M \ll N$.
1. The measurement vector $\by \in \RR^M $ is given by
   
   $$
    \by = \Phi \bx
   $$
   where $\RR^M$ is our measurement space.
1. $\by$ is known, $\Phi$ is known while $\bx$ is unknown
   to the recovery algorithm.
1. $\bx$ is assumed to be either $K$-sparse or $K$-compressible.

The sparse recovery problem can be written as

```{math}
:label: eq:greedy:omp_sparse_recovery_problem

& \underset{x}{\text{minimize }} 
& &  \| \by - \Phi \bx \|_2 \\
& \text{subject to}
& &  \| \bx \|_0 \leq K.
```

Though the problem looks similar to $(\mathcal{D}, K)$-SPARSE approximation problem,
but there are  differences since $\Phi$ is not a dictionary
(see {ref}`sec:cs:sensing:matrices`).
In particular, we don't require each column to be unit norm.


We will adapt OMP algorithm studied in
{ref}`sec:sa:omp` for the problem of 
sparse recovery in compressed sensing framework.
In the analysis of OMP for CS We will address following questions:

*  How many measurements are required to recover $\bx$ from $\by$ exactly
   if $\bx$ is $K$-sparse? 
*  What kind of sensing matrices are admissible for OMP to work in CS framework?
*  If $\bx$ is not $K$-sparse, then how much maximum error is incurred? 

## The Algorithm


OMP algorithm adapted to CS is presented in {prf:ref}`alg:greedy:omp_cs`.


```{prf:algorithm} Orthogonal matching pursuit for sparse recovery from compressive measurements
:label: alg:greedy:omp_cs


Inputs:
* Sensing matrix $\Phi \in \RR^{M \times N}$
* Measurement vector $\by \in \RR^M$
* Desired sparsity level $K$


Outputs:
* A $K$-sparse estimate $\widehat{\bx} \in \Sigma_{K} \subseteq \RR^N$
  for the ideal signal $\bx$
* An index set $\Lambda^K \subset \{1,\dots, N\}$
  identifying the support of $\widehat{\bx}$
* An approximation $\by^K \in \RR^M$ of $\by$
* A  residual $\br^K = \by  - \by^K \in \RR^M$

Initialization:

1. $k \leftarrow 0$ # Iteration counter
1. $\bx^0 \leftarrow \bzero$ # Initial Estimate of $\bx \in \RR^N$
1. $\by^0 \leftarrow \Phi \bx^0 = \bzero$ # Approximation of $\by$
1. $\br^0 \leftarrow \by - \by^0 =\by$ # Residual $\br \in \RR^M$
1. $\Lambda^0 \leftarrow \EmptySet$ # Solution support $\Lambda = \supp(\widehat{\bx})$

Algorithm:

1. If $k == K$ or $\br^k == \bzero$: break.
1. Increase the iteration count

   $$
   k \leftarrow k + 1.
   $$ 
1. Sweep (find column with largest inner product)

   $$
   \lambda_k  = \text{arg} \; \underset{1 \leq j \leq N}{\max}
   |\langle \br^{k-1}, \phi_j \rangle|.
   $$
1. Update support
   
   $$
   \Lambda^{k} \leftarrow \Lambda^{k - 1} \cup \{ \lambda_k\}.
   $$
1. Update provisional solution
   
   $$
   \bx^k \leftarrow \underset{\bx}{\argmin}\, 
   \| \Phi \bx - \by \|^2_2
   $$
   subject to $\supp(\bx) = \Lambda^{k}$.
1. Update residual
   
   $$
   & \by^k \leftarrow \Phi \bx^k; \\
   & \br^k \leftarrow \by - \by^k.
   $$
1. Go to step 1.

Finalization:

* $\widehat{\bx} \leftarrow \bx^k$.
```


Some remarks are in order

1. The algorithm returns a $K$-term approximation of $\bx$ given by $\widehat{\bx}$.
1. Each step of algorithm is identified by the iteration counter $k$ which runs from 0 to $K$.
1. At each step $\bx^k$, $\by^k$ and $\br^k$ are computed
   where $\bx^k$ is the $k$-term estimate of $\bx$, 
   $\by^k$ is corresponding measurement vector and $\br^k$
   is the residual between actual measurement
   vector $\by$ and the estimated measurement vector $\by^k$. 
1. The support for $\widehat{\bx}$ is maintained in an index set $\Lambda$. 
1. At each iteration we add one more new index $\lambda_k$ to $\Lambda^{k-1}$ giving us $\Lambda^k$.
1. We will use $\Phi_{\Lambda^k} \in \RR^{M \times k}$ to denote the submatrix constructed
   from the columns indexed by $\Lambda^k$.
   In other words, if $\Lambda^k = \{ \lambda_1, \dots, \lambda_k\}$, then
   
   $$
    \Phi_{\Lambda^k} = \begin{bmatrix}
    \phi_{\lambda_1} & \dots & \phi_{\lambda_k}
    \end{bmatrix}.
   $$ 
1. Similarly we will denote a vector $\bx^k _{\Lambda^k} \in \RR^k$
   to denote a vector consisting of only
   $k$ non-zero entries in $\bx$.
1. We note that $\br^k$ is orthogonal to $\Phi_{\Lambda^k}$.
   This is true due to $\bx^k$ being the least squares
   solution in the update provisional solution step.
1. This also ensures that in each iteration a new column from $\Phi$
   indexed by $\lambda_k$ will be chosen. 
   OMP will never choose the same column again.
1. In case $\bx$ has a sparsity level less than $K$ then $\br^k$
   will become zero in the middle.
   At that point we halt. There is no point going forward.
1. An equivalent formulation of the least squares step is
   
   $$
   \bz \leftarrow \text{arg } \underset{\bv \in \RR^k}{\min}\, \| \Phi_{\Lambda^k}  \bv - \by \|^2_2
   $$
   followed by 
   
   $$
   \bx^k_{\Lambda^k}  \leftarrow \bz.
   $$
1. We solve the least squares problem for columns of $\Phi$ indexed by $\Lambda^k$
   and then assign the $k$ entries in the resultant $\bz$ to the entries in $\bx^k$
   indexed by $\Lambda^k$ while keeping other entries as 0.
1. Least squares can be accelerated by using $\bx^{k-1}$ as the starting estimate of
   $\bx^k$ and carrying out a descent like Richardson's iteration from there.

## Exact Recovery using OMP with Random Sensing Matrices

The objective of this subsection is to prove theoretically that OMP can recover
sparse signals from a small set of random linear measurements. In this
subsection we discuss the conditions on the random sensing matrix $\Phi$ 
under which they are suitable for signal recovery through OMP.

````{prf:definition} Admissible sensing matrix
:label: def:greedy:omp:admissible_sensing_matrix

An *admissible sensing matrix* for $K$-sparse signals in $\RR^M$ is an $M \times N$
random matrix $\Phi$ with following properties.

* [M0] *Independence*: The columns of $\Phi$ are stochastically independent.
* [M1] *Normalization*: $\EE(\| \phi_j \|_2^2) = 1$ for $j = 1, \dots, N$.
* [M2] *Joint correlation*: 
  * Let $\{\bu_k \}$ be a sequence of $K$ vectors
    whose $\ell_2$ norms do not exceed one.
  * Let $\phi$ be a column of $\Phi$ that is independent from this sequence.
  * Then
  
      $$
        \PP(\max_{k} | \langle \phi,  \bu_k \rangle | \leq \epsilon) \geq 
        1  - 2 K \exp (- c \epsilon^2 M).
      $$ 
* [M3] *Smallest singular value*: Given any 
  $M \times K$ ($K < M$) submatrix $\bZ$ from $\Phi$,
  the smallest ($K$-th largest) singular value
  $\sigma_{\min}(\bZ)$ satisfies 
  
  $$
    \PP (\sigma_{\min}(\bZ) \geq 0.5) \geq 1 - \exp(-c M).
  $$
$c > 0$ is some positive constant.
````

It can be shown Rademacher sensing matrices ({ref}`sec:sm:rademacher_sensing_matrix`)
and Gaussian sensing matrices ({ref}`sec:sm:gaussian_sensing_matrix`)
satisfy all the requirements of admissible sensing matrices
for sparse recovery using OMP. 
Some of the proofs are included in the book.
You may want to review corresponding sections.

Some remarks are in order to further explain the definition
of admissible sensing matrices.

```{div}
1. Typically all the columns of a sensing matrix are drawn from the same distribution.
   But (M0) doesn't require so.
   It allows different columns of $\Phi$ to be drawn from different distributions.
1. The joint correlation property (M2) depends on the decay of random variables
   $\| \phi_j \|_2$. i.e. it needs the tails of  $\| \phi_j \|_2$ to be small.
1. A bound on the smallest (non-zero) singular value of $M \times K$-sub-matrices (M3) controls 
   how much the sensing matrix can shrink $K$-sparse vectors.
1. I guess that the idea of admissible matrices came as follows.
   First OMP signal recovery guarantees were developed for Gaussian and Rademacher sensing matrices.
   Then the proofs were analyzed to identify the minimum requirements
   they imposed on the structure of random sensing matrices.
   This was extracted in the form of notion of admissible matrices.
   Finally the proof was reorganized to work for all random matrices which satisfy the
   admissibility criteria.
   It is important to understand this process of abstraction otherwise
   we just get surprised as to how the ideas like admissible matrices came out of the blue.
```

## Signal Recovery Guarantees with OMP


We now show that OMP can be used to recover the original signal with high probability if the random measurements are taken using an
admissible sensing matrix as described above.

Here we consider the case where $\bx$ is known to be $K$-sparse.

````{prf:theorem}
:label: thm:greedy:omp:cs_recovery_guarantee

Fix some $\delta \in (0,1)$, and choose
$M \geq C K \ln \left(\frac{N}{\delta} \right)$
where $C$ is an absolute constant.
Suppose that $\bx$ is an arbitrary $K$-sparse signal in $\RR^N$ 
and draw an $M \times N$ admissible sensing matrix $\Phi$
independent from $\bx$. 

Given the measurement vector $\by = \Phi \bx \in \RR^M$,
Orthogonal Matching Pursuit can reconstruct
the signal with probability exceeding $1 - \delta$.
````

Some remarks are in order.
Specifically we compare OMP here with basis pursuit (BP).

1. The theorem provides probabilistic guarantees.
1. The theorem actually requires more measurements than the results for BP.
1. The biggest advantage is that OMP is a much simpler algorithm
   than BP and works very fast.
1. Results for BP show that a single random sensing matrix 
   can be used for recovering all sparse signals.
1. This theorem says that any sparse signal independent from the sensing matrix
   can be recovered.
1. Thus this theorem is weaker than the results for BP.
   It can be argued that for practical situations,
   this limitation doesn't matter much.


````{prf:proof}
The main challenge here is to handle the issues that arise
due to random nature of $\Phi$. 
We start with setting up some notation for this proof. 

1. We note that the columns that OMP chooses do not depend on the order
   in which they are stacked in $\Phi$.
1. Thus without loss of generality we can assume that the first
   $K$ entries of $\bx$ are non-zero and rest are zero. 
1. If OMP picks up the first $K$ columns,
   then OMP has succeeded otherwise it has failed.
1. With this, support of $\bx$ given by $\Lambda_{\opt} = \{ 1, \dots, K\}$.

We now partition the sensing matrix $\Phi$ as

$$
\Phi = \begin{bmatrix}
\Phi_{\opt} & | & \Psi 
\end{bmatrix}
$$
where $\Phi_{\opt}$ consists of first $K$ columns of $\Phi$ which 
correspond to $\Lambda_{\opt}$.
$\Psi$ consists of remaining $(N - K)$ 
columns of $\Phi$.

We recall from the proof of {prf:ref}`thm:greedy:omp_exact_recovery_sufficient_condition`
that in order for OMP to make absolute progress at step $k+1$ we require 
the *greedy selection ratio* $\rho(\br^k) < 1$ where

$$
\rho(\br^k) = \frac{\| \Psi^H \br^k \|_{\infty}}{\| \Phi_{\opt}^H \br^k \|_{\infty}} 
= \frac{\underset{\psi \in \Psi}{\max} | \langle \psi, \br^k \rangle |}{\| \Phi_{\opt}^H \br^k \|_{\infty}}.
$$

The proof is organized as follows:

1. We first construct a thought experiment in which $\Psi$
   is not present and OMP is run
   only with $\by$ and $\Phi_{\opt}$.
1. We then run OMP with $\Psi$ present under the condition $\rho(\br^k) <1$.
1. We show that the sequence of columns chosen and residual obtained
   in both cases is exactly the same.
1. We show that the residuals obtained in the thought experiment
   are stochastically independent from the columns of $\Psi$. 
1. We then describe the success of OMP as an event in terms of these residuals.
1. We compute a lower bound on the probability of the event of OMP success. 


For a moment suppose that there was no $\Psi$ and OMP is run with $\by$
and $\Phi_{\opt}$ as input for $K$ iterations.
Naturally OMP will choose $K$ columns in $\Phi_{\opt}$ one by one.

1. Let the columns it picks up in each step be indexed by
   $\omega_1, \omega_2, \dots, \omega_K$. 
1. Let the residuals before each step be
   $\bq^0, \bq^1, \bq^2, \dots, \bq^{K-1}$.
1. Since $\bx \in \ColSpace(\Phi_{\opt})$,
   hence the residual after $K$ iterations $\bq^K = \bzero$.  
1. Since OMP is a deterministic algorithm, hence the two sequences
   are simply functions of $\bx$ and $\Phi_{\opt}$.
1. Clearly, we can say that the residual $\bq^k$ are stochastically independent
   of the columns in $\Psi$
   (since columns of $\Psi$ are independent of the columns of $\Phi_{\opt}$).
1. We also know that $\bq^k \in \ColSpace(\Phi_{\opt})$.

In this thought experiment we made no assumptions about
$\rho(\bq^k)$ since $\Psi$ is not present.
We now consider the full matrix $\Phi$ and execute OMP with $\by$. 

1. The actual sequence of residuals before each step is
   $\br^0, \br^1, \dots, \br^{K-1}$.
1. The actual sequence of column indices is $\lambda_1, \dots, \lambda_K$.
1. OMP succeeds in recovering $\bx$ in $K$ steps
   if and only if it selects the first $K$ columns of $\Phi$ 
   in some order.
1. This can happen if and only if $\rho(\br^k) < 1$ holds.
1. We are going to show inductively that this can happen
   if and only if $\lambda_k = \omega_k$ and 
   $\bq^k = \br^k$. 
1. At the beginning of step 1,
   we have $\br^0 = \bq^0 = \by$.
1. Now OMP selects one column from $\Phi_{\opt}$ if and only if
   $\rho(\br^0) <1$ which is identical to $\rho(\bq^0) <1$.
1. So it remains to show at step 1 that $\lambda_1 = \omega_1$. 
1. Because $\rho(\br^0) < 1$, the algorithm selects the index $\lambda_1$
   of the column from $\Phi_{\opt}$ whose inner product with $\br^0$ is the
   largest (in absolute value). 
1. Also since $\rho(\bq^0) < 1$ with $\br^0 = \bq^0$, $\omega_1$ is the index
   of column in $\Phi_{\opt}$ whose inner product with $\bq^0$ is largest.
1. Thus $\omega_1 = \lambda_1$. 
1. We now assume that for the first $k$ iterations, real OMP chooses
   the same columns as our imaginary thought experiment.
1. Thus we have
   
   $$
    \lambda_j = \omega_j \Forall 1 \leq j \leq k
   $$
   and 
   
   $$
    \br^j = \bq^j \Forall 0 \leq j \leq k.
   $$
   This is valid since the residuals at each step depend solely on the set
   of columns chosen so far and input $\by$ which are same for both cases.
1. OMP chooses a column in $\Phi_{\opt}$ at $(k+1)$-th step
   if and only if $\rho(\br^k) < 1$ which is same as $\rho(\bq^k) < 1$.
1. Moreover since $\br^k = \bq^k$ hence the column chosen by maximizing
   the inner product is same for both situations.
1. Thus
   
   $$
    \lambda_{k + 1} = \omega_{k + 1}.
   $$
1. Therefore the criteria for success of OMP can be stated as 
   $\rho(\bq^k) < 1$ for all $0 \leq k \leq K-1$. 

We now recall that $\bq^k$ is actually a random variable (depending upon the
random vectors which comprise the columns of $\Phi_{\opt}$).

1. Thus the event on which the algorithm succeeds in sparse recovery of $\bx$
   from $\by$ is given by
   
   $$
    E_{\succ} \triangleq 
    \left \{ \underset{0 \leq k < K}{\max} \rho(\bq^k)  < 1 \right \}.
   $$
1. In a particular instance of OMP execution if the event $E_{\succ}$ happens,
   then OMP successfully recovers $\bx$ from $\by$. 
1. Otherwise OMP fails.
1. Hence the probability of success of OMP is same as the
   probability of event $E_{\succ}$.
1. We will be looking for some sort of a lower bound on $\PP(E_{\succ})$.
1. We note that we have $\{ \bq^k \}$ as a sequence of random vectors in the
   column span of $\Phi_{\opt}$ and
   they are stochastically independent from columns of $\Psi$.
1. It is difficult to compute $\PP(E_{\succ})$ directly.
1. We consider another event
   
   $$
   \Gamma = \{ \sigma_{\min} (\Phi_{\opt}) \geq 0.5 \}.
   $$
1. Clearly
   
   $$
    \PP(E_{\succ}) 
    \geq \PP \left (  \underset{0 \leq k < K}{\max} \rho(\bq^k)  < 1
    \; \text{ and } \;
    \Gamma
    \right ).
   $$
1. Using conditional probability we can rewrite
   
   $$
    \PP(E_{\succ}) \geq 
    \PP \left (  \underset{0 \leq k < K}{\max} \rho(\bq^k)  < 1 | \Gamma \right ) \PP (\Gamma).
   $$
1. Since $\Phi$ is an admissible matrix hence it satisfies (M3)
   which gives us

    $$
     \PP (\Gamma) \geq 1 - \exp(-c M).
    $$
1. We just need a lower bound on the conditional probability.
1. We assume that $\Gamma$ occurs.
1. For each step index $k = 0, 1, \dots, K-1$, we have
   
   $$
    \rho(\bq^k) 
    = \frac{ \max_{\psi} | \langle \psi, \bq^k \rangle |}{\| \Phi_{\opt}^H \bq^k \|_{\infty}}.
   $$
1. Since $ \Phi_{\opt}^H \bq^k \in \RR^K$, we have
   
   $$
    \sqrt{K} \| \Phi_{\opt}^H \bq^k \|_{\infty} \geq  \| \Phi_{\opt}^H \bq^k \|_2.
   $$
1. This gives us

    $$
    \rho(\bq^k) \leq 
    \frac{ \sqrt{K} \max_{\psi } | \langle \psi, \bq^k \rangle | }{ \| \Phi_{\opt}^H \bq^k \|_2 }.
    $$
1. To simplify this expression, we define a vector

    $$
    \bu^k \triangleq \frac{0.5 \bq^k} {\| \Phi_{\opt}^H \bq^k \|_2}.
    $$
1. This lets us write

    $$
    \rho(\bq^k) \leq 2 \sqrt{K} \max_{\psi } | \langle \psi, \bu^k \rangle |.
    $$
1. Thus

    $$
    \PP(\rho(\bq^k) < 1 | \Gamma) \geq \PP (2 \sqrt{K} \max_{\psi } | \langle \psi, \bu^k \rangle | < 1 | \Gamma) 
    = \PP \left (\max_{\psi } | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}}  | \Gamma \right ).
    $$
1. From the basic properties of singular values we recall that
    
    $$
    \frac{\| \Phi_{\opt}^H \bq \|_2}{ \|\bq \|_2} 
    \geq \sigma_{\min} (\Phi_{\opt}) \geq 0.5
    $$
    for all vectors $\bq$ in the range of $\Phi_{\opt}$.
1. This gives us

    $$
    \frac{ 0.5 \|\bq \|_2}  {\| \Phi_{\opt}^H \bq \|_2} \leq 1.
    $$
1. Since $\bq^k$ is in the column space of $\Phi_{\opt}$,
   for $\bu^k$ defined above we have

    $$
    \| \bu^k \|_2 \leq 1.
    $$
    This is valid under the assumption that the event $\Gamma$ has happened.
1. From the above we get

    $$
    \PP\left (\max_k \rho(\bq^k) < 1  | \Gamma \right) \geq 
    \PP \left ( \max_k \max_{\psi } | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}}  | \Gamma \right )
    $$
1. In the R.H.S. we can exchange the order of two maxima. This gives us
    
    $$
    \PP \left ( \max_k \max_{\psi } | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}}  | \Gamma \right ) 
    =  \PP \left ( \max_{\psi } \max_k | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}}  | \Gamma \right ).
    $$
1. We also note that columns of $\Psi$ are independent.
1. Thus in above we require that for each column of $\Psi$ 
   $\max_k | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}}$
   should hold independently.
1. Hence we can say
    
    $$
    \PP \left ( \max_{\psi } \max_k | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}}  | \Gamma \right )
    = \prod_{\psi}\PP \left ( \max_k | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}}  | \Gamma \right ).
    $$
1. We recall that event $\Gamma$ depends only on columns of $\Phi_{\opt}$.
1. Hence columns of $\Psi$ are independent of $\Gamma$.
1. Thus

    $$
    \prod_{\psi}\PP \left ( \max_k | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}}  | \Gamma \right )
    = \prod_{\psi}\PP \left ( \max_k | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}} \right ).
    $$
1. Since the sequence $\{\bu^k \}$ depends only on columns of $\Phi_{\opt}$,
   hence columns of $\Psi$ are independent of $\{\bu^k \}$.
1. Thus we can take help of (M2) to get

    $$
    \prod_{\psi}\PP \left ( \max_k | \langle \psi, \bu^k \rangle | < \frac{1}{2 \sqrt{K}} \right )
    \geq  \left (1 - 2 K \exp\left(- \frac{c M}{4 K} \right) \right )^{N - K}.
    $$
1. This gives us the lower bound

    $$
    \PP\left (\max_k \rho(\bq^k) < 1  | \Gamma \right) \geq 
    \left (1 - 2 K \exp\left(- \frac{c M}{4 K} \right) \right )^{N - K}.
    $$
1. Finally plugging in the lower bound for $\PP(\Gamma)$ we get

    ```{math}
    :label: eq:7237821a-ba2a-4820-ad4c-74433f7efa5f
    \PP(E_{\succ}) \geq \left (1 - 2 K \exp\left(- \frac{c M}{4 K} \right) \right )^{N - K} (1 - \exp(-c M)).
    ```
    All that is remaining now is to simplify this expression. 
1. We recall that we assumed in the theorem statement

    $$
    & M \geq C K \ln \left(\frac{N}{\delta} \right)\\
    \implies & \frac{M}{C K} \geq  \ln \left(\frac{N}{\delta} \right)\\
    \implies & \exp \left  ( \frac{M}{C K} \right ) \geq \frac{N}{\delta} \\
    \implies & \frac{\delta}{N} \geq \exp \left  ( - \frac{M}{C K} \right ) \\
    \implies & \delta \geq N \exp \left  ( - \frac{M}{C K} \right ).
    $$
1. But we assumed that $0 < \delta < 1$.
1. Thus

    $$
    N \exp \left  ( - \frac{M}{C K} \right ) < 1.
    $$
1. If we choose $C  \geq \frac{4}{c}$ then

    ```{math}
    :label: eq:cfc76c94-6c53-429b-91be-020e5258cc2a

    & - \frac{1}{C} \geq - \frac{c}{4}\\
    \implies & - \frac{M}{CK} \geq - \frac{cM}{4K}\\
    \implies & \exp\left ( - \frac{M}{CK} \right) \geq \exp \left( - \frac{cM}{4K} \right ) \\
    \implies & N \exp\left ( - \frac{M}{CK} \right) \geq 2K \exp \left( - \frac{cM}{4K} \right ) \\
    \implies & 1 > \delta \geq 2K \exp \left( - \frac{cM}{4K} \right ) \\
    ```
    where we assumed that $N \gg 2 K$.
1. We recall that

    $$
    (1 - x)^k \geq 1 - k x \text{ if } k \geq 1 \text{ and } x \leq 1.
    $$
1. Applying on {eq}`eq:7237821a-ba2a-4820-ad4c-74433f7efa5f` we get

    ```{math}
    :label: eq:09bfc9be-b2cb-419d-a0ba-1dffb2ba12f6

    \PP(E_{\succ}) \geq 1 - 2 K (N - K) \exp\left(- \frac{c M}{4 K} \right) - \exp(-c M).
    ```
    We ignored the 4-th term in this expansion.
1. Now we can safely assume that $K(N -K) \geq \frac{N^2}{4}$ giving us

    $$
    \PP(E_{\succ}) \geq 1 - \frac{N^2}{2} \exp\left(- \frac{c M}{4 K} \right) - \exp(-c M).
    $$
1. If we choose $C  \geq \frac{8}{c}$ then following
   {eq}`eq:cfc76c94-6c53-429b-91be-020e5258cc2a`
   we can get

    $$
    & N \exp\left ( - \frac{M}{CK} \right) \geq N \exp \left( - \frac{cM}{8K} \right )\\
    \implies & \delta \geq N \exp \left( - \frac{cM}{8K} \right )\\
    \implies & \delta^2 \geq N^2 \exp \left( - \frac{cM}{4K} \right )\\
    \implies & 1 - \frac{\delta^2}{2} \leq 1  - \frac{N^2}{2} \exp\left(- \frac{c M}{4 K} \right).
    $$
1. Thus

    $$
    \PP(E_{\succ}) \geq 1 - \frac{\delta^2}{2} - \exp(-c M).
    $$
1. Some further simplification can give us

    $$
    \PP(E_{\succ}) \geq 1 - \delta.
    $$
1. Thus with a suitable choice of the constant $C$, a choice of 
   $M \geq C K \ln \left(\frac{N}{\delta} \right)$ with $\delta \in (0,1)$
   is sufficient to reduce the failure probability below $\delta$. 
````

(sec:greedy:omp_rip_analysis)=
## Analysis of OMP using Restricted Isometry Property

In this subsection we present an alternative analysis of 
OMP algorithm using the Restricted Isometry Property of
the matrix $\Phi$ {cite}`davenport2010analysis`.  


### A re-look at the OMP Algorithm


Before we get into the RIP based analysis of OMP, it would be
useful to get some new insights into the behavior of OMP algorithm.
These insights will help us a lot in performing the analysis later.

1. We will assume throughout that whenever $| \Lambda | \leq K$, 
   then $\Phi_{\Lambda}$ is full rank.
1. The pseudo-inverse is given by

   $$
    \Phi_{\Lambda}^{\dag}
    = \left (\Phi_{\Lambda}^H \Phi_{\Lambda} \right )^{-1} \Phi_{\Lambda}^H.
   $$
1. The orthogonal projection operator to the column space for
   $\Phi_{\Lambda}$ is given by
   
   $$
    \bP_{\Lambda}  = \Phi_{\Lambda}\Phi_{\Lambda}^{\dag}.
   $$
1. The orthogonal projection operator onto the orthogonal complement of
   $\ColSpace(\Phi_{\Lambda})$ (column space of $\Phi_{\Lambda}$)
   is given by
   
   $$
    \bP_{\Lambda}^{\perp} = \bI - \bP_{\Lambda}.
   $$
1. Both $\bP_{\Lambda}$ and $\bP_{\Lambda}^{\perp}$
   satisfy the standard properties like
   $\bP = \bP^H$ and $\bP^2 = \bP$.
1. We further define
   
   $$
    \Psi_{\Lambda} = \bP_{\Lambda}^{\perp} \Phi.
   $$
1. We are orthogonalizing the atoms in $\Phi$ against
   $\ColSpace(\Phi_{\Lambda})$,
   i.e. taking the component of the atom which is  orthogonal
   to the column space of $\Phi_{\Lambda}$.
1. The atoms in $\Psi_{\Lambda}$ corresponding
   to the index set $\Lambda$ would be $\bzero$.
1. We will make some further observations on the behavior of 
   OMP algorithm {cite}`davenport2010analysis`.
1. Recall that the approximation after the $k$-th iteration is given by
   
   $$
    \bx^k_{\Lambda^k}  = \Phi_{\Lambda^k}^{\dag} \by \quad \text{ and } 
    \quad \bx^k_{{\Lambda^k}^c} = \bzero.
   $$
1. The residual after $k$-th iteration is given by
   
    $$
    \br^k  = \by - \Phi \bx^k
    $$
    and by construction $\br^k$ is orthogonal to $\Phi_{\Lambda^k}$.
1. We can write
   
   $$
    \Phi \bx^k  = \Phi_{\Lambda}\bx^k_{\Lambda^k} + 
    \Phi_{{\Lambda^k}^c} \bx^k_{\Lambda^c} 
    = \Phi_{\Lambda^k}\bx^k_{\Lambda^k}.
   $$
1. Thus,

    ````{math}
    \br^k  &=  \by - \Phi_{\Lambda^k}\bx^k_{\Lambda^k} \\
    &= \by - \Phi_{\Lambda^k}\Phi_{\Lambda^k}^{\dag} \by \\
    &= ( \bI - \bP_{\Lambda^k}) \by = \bP_{\Lambda^k}^{\perp} \by.
    ````
1. In summary
   
   $$
    \br^k  = \bP_{\Lambda^k}^{\perp} \by.
   $$
1. This shows that it is not actually necessary to compute $\bx^k$
   in order to find $\br^k$.
   An equivalent way of writing OMP algorithm could be
   as in {prf:ref}`alg:omp_rip_variant_a`.

````{prf:algorithm} Sketch of OMP without intermediate $\bx^k$ computation
:label: alg:omp_rip_variant_a

Algorithm:

1. If halting criteria is satisfied, then break.
1. $\bh^{k + 1} \leftarrow \Phi^H \br^{k}$ # Match
1. $\lambda^{k + 1} \leftarrow \underset{j \notin \Lambda^{k}}{\text{arg} \max} | \bh^{k + 1}_j |$ # Identify
1. $\Lambda^{k + 1} \leftarrow \Lambda^{k} \cup \{ \lambda^{k + 1} \}$ # Update support
1. $\br^{k + 1} \leftarrow \bP_{\Lambda^{k + 1}}^{\perp} \by$ # Update residual
1. $k \leftarrow k + 1$.
1. Go back to step 1.

Finalization:
1. $\widehat{\bx}_{\Lambda^k}  \leftarrow \Phi_{\Lambda^k}^{\dag} \by$.
1. $\widehat{\bx}_{{\Lambda^k}^c}  \leftarrow \bzero$.
````

1. In the matching step, we are correlating $\br^k$ with columns of $\Phi$.
1. Since $\br^k$ is orthogonal to column space of $\Phi_{\Lambda^k}$, hence
   this correlation is identical to correlating $\br^k$ with $\Psi_{\Lambda^k}$.
1. To see this, observe that
   
   $$
    \br^k = \bP_{\Lambda^k}^{\perp} \by 
    = \bP_{\Lambda^k}^{\perp} \bP_{\Lambda^k}^{\perp} \by
    = (\bP_{\Lambda^k}^{\perp})^H \bP_{\Lambda^k}^{\perp} \by.
   $$
1. Thus,
   
   $$
    \bh^{k + 1 } 
    &= \Phi^H \br^k \\
    &=  \Phi^H ( \bP_{\Lambda^k}^{\perp})^H \bP_{\Lambda^k}^{\perp} \by\\
    &= \left (\bP_{\Lambda^k}^{\perp} \Phi \right )^H  
    \bP_{\Lambda^k}^{\perp} \by \\
    &= \left ( \Psi_{\Lambda^k} \right ) ^H \br^k.
   $$
1. On similar lines, we can also see that
   
   $$
    \bh^{k + 1} 
    =  \Phi^H  \br^k 
    = \Phi^H \bP_{\Lambda^k}^{\perp} \by 
    = \Phi^H \left ( \bP_{\Lambda^k}^{\perp} \right)^H \by 
    = \left ( \Psi_{\Lambda^k}\right )^H \by.
   $$
1. In other words, we have

    ```{math}
    :label: eq:greedy:cda31681-9bbd-4406-94da-15cb0f116122

    \bh^{k + 1 } = \left ( \Psi_{\Lambda^k} \right)^H \br^k 
    = \left ( \Psi_{\Lambda^k} \right )^H \by.
    ```
1. Thus, we can observe that OMP can be further simplified and
   we don't even need to compute $\br^k$ in order to compute $\bh^{k + 1}$. 
1. There is one catch though.
   If the halting criterion depends on the need to compute the residual energy,
   then we certainly need to compute $\br^k$. If the halting criteria is simply
   the number of $K$ iterations, then we don't need to compute $\br^k$.
1. The revised OMP algorithm sketch is presented in
   {prf:ref}`alg:omp_rip_variant_b`.

````{prf:algorithm} Sketch of OMP without intermediate $\bx^k$ computation
:label: alg:omp_rip_variant_b

Algorithm:

1. If halting criteria is satisfied, then break.
1. $\bh^{k + 1} \leftarrow \left ( \Psi_{\Lambda^{k}} \right)^H \by$ # Match
1. $\lambda^{k + 1} \leftarrow \underset{i \notin \Lambda^{k}}{\text{arg} \max} | \bh^{k + 1}_i |$ # Identify
1. $\Lambda^{k + 1} \leftarrow \Lambda^{k} \cup \{ \lambda^{k + 1} \}$ # Update support
1. $k \leftarrow k + 1$
1. Go back to step 1.


Finalization:
1. $\widehat{\bx}_{\Lambda^k}  \leftarrow \Phi_{\Lambda^k}^{\dag} \by $.
1. $\widehat{\bx}_{{\Lambda^k}^c}  \leftarrow \bzero$.
````
With this the OMP algorithm is considerably simplified from the
perspective of analyzing its recovery guarantees.

````{div}
1. Coming back to $\bh^{k + 1}$, note that the columns of $\Psi_{\Lambda^k}$
   indexed by $\Lambda^k$ are all $\bzero$s.
1. Thus
   
   $$
    h^{k + 1}_j = \bzero \quad \Forall j \in \Lambda^k.
   $$
1. This makes it obvious that $\lambda^{k + 1} \notin \Lambda$ and 
   consequently $|\Lambda^k | = k$ (inductively).
1. Lastly for the case of noise free model $\by = \Phi \bx$, we may write
   
   $$
    \br^k = \bP_{\Lambda^k}^{\perp} \by 
    = \bP_{\Lambda^k}^{\perp} \Phi \bx 
    = \Psi_{\Lambda^k} \bx.
   $$
1. Since columns of $\Psi_{\Lambda^k}$ indexed by $\Lambda^k$ are $\bzero$,
   hence when $\supp(\bx) \subseteq \Lambda^k$, then $\br^k = \bzero$. 
1. In this case $\bx^k = \bx$ exactly since it is a least squares estimate
   over $\Phi_{\Lambda^k}$.
1. For the same reason, if we construct a vector $\widetilde{\bx}^k$
   by zeroing out the entries indexed by $\Lambda^k$ i.e.

    ```{math}
    :label: eq:omp:widetilde_alpha_definition

    \widetilde{\bx}^k_{\Lambda^k} = 0  \quad 
    \text{ and } \quad \widetilde{\bx}_{{\Lambda^k}^c} = \bx_{{\Lambda^k}^c}
    ```
    then
    ```{math}
    :label: eq:omp:3715a448-7956-43a0-91d5-43447bbdfa7b

    \br^k = \Psi_{\Lambda^k} \widetilde{\bx}^k.
    ```
1. If $\| \bx \|_0 = K$, then $\| \widetilde{\bx}^k \|_0 = K - k$.
1. Lastly putting $\br^k$ back in 
   {eq}`eq:greedy:cda31681-9bbd-4406-94da-15cb0f116122`, we obtain

    ```{math}
    :label: eq:omp:3dfc00cb-f266-4876-b7d9-14daeca3056a

    \bh^{k + 1 } = \left ( \Psi_{\Lambda^k} \right)^H \Psi_{\Lambda^k} \widetilde{\bx}^k.
    ```
1. In this version, we see that $\bh^{k + 1}$ is computed by applying the
   matrix $\left ( \Psi_{\Lambda^k} \right)^H \Psi_{\Lambda^k}$ to the
   $(K - k)$ sparse vector $\widetilde{\bx}^k$.
1. We are now ready to carry out RIP based analysis of OMP.
````

### RIP based Analysis of OMP

Our analysis here will focus on the case for
real signals and real matrices i.e. $\Phi \in \RR^{M \times N}$
and $\bx \in \RR^N$. We will attack the noise free case. 

Some results for matrices that satisfy RIP will be useful
in the upcoming analysis.
Please refer to {ref}`sec:ssm:rip` for an extensive
treatment of RIP based results.


`````{div}
{prf:ref}`lem:rip:inner_product_upper_bound_2`
applies to approximate preservation of the inner
product of sparse signals  $\bu, \bv \in \RR^N$.

Let $\bu, \bv \in \RR^N$ and $K \geq \max( \| \bu + \bv \|_0 , \| \bu - \bv \|_0)$.
Then 

```{math}
:label: eq:greedy:ef6701cc-26cb-4293-9f6f-828ce08658c7

| \langle \Phi \bu, \Phi \bv \rangle - \langle \bu, \bv \rangle | 
\leq \delta_{K} \| \bu \|_2 \| \bv \|_2.
```
{prf:ref}`res:proj:rip_orthogonal_projection`
shows that the matrix  $\Psi_{\Lambda}$ also satisfies 
a modified version of RIP.
Let $|\Lambda | < K$. Then

```{math}
:label: eq:greedy:5774ac7f-1f4b-464f-882b-9795c5996278

\left ( 1 - \frac{\delta_K}{1 - \delta_K} \right )
\| \by \|_2^2 
\leq \| \Psi_{\Lambda} \by \|_2^2
\leq (1 + \delta_K) \| \by \|_2^2
```
whenever $\|\by \|_0 \leq K - | \Lambda|$ and 
$\supp(\by) \cap \Lambda = \EmptySet$.

If $\Phi$ satisfies RIP of order $K$, then $\Psi_{\Lambda}$
acts as an approximate isometry on every $(K - |\Lambda|)$-sparse vector
supported on $\Lambda^c$.

From {eq}`eq:omp:3715a448-7956-43a0-91d5-43447bbdfa7b` recall that
the residual vector $\br^k$ is formed by applying $\Psi_{\Lambda^k}$ 
to $\widetilde{\bx}^k$ which is a $K - k$ sparse vector supported
on ${\Lambda^k}^c$.

Our interest is in combining above two results and get some
bound on the inner products $\bh^{k + 1}_j$. Exactly what kind of bound? 
When $\Lambda^k$ has been identified, our interest is in ensuring
that the next index is chosen from the set $\supp(\bx) \setminus \Lambda^k$.
A useful way to ensure this would be to verify if the entries in $\bh^{k + 1}$
are close to $\widetilde{\bx}^k$. If they are, then they would be 0 over $\Lambda^k$
, they would be pretty high over $\supp(\bx) \setminus \Lambda^k$  and lastly,
very small over $\supp(\bx)^c$ which is what we want. 

The next result 
develops these bounds around {eq}`eq:omp:3dfc00cb-f266-4876-b7d9-14daeca3056a`.
`````

````{prf:lemma}
:label: res:omp:rip:inner_product_upper_bound

Let $\Lambda \subset \{1, \dots, N \}$ and suppose
$\widetilde{\bx} \in \RR^N$ with
$\supp(\widetilde{\bx}) \cap \Lambda = \EmptySet$.
Define 

```{math}
:label: eq:omp:ec749572-224c-4fe1-8796-a35ef1284d4c

\bh = \Psi_{\Lambda}^T \Psi_{\Lambda} \widetilde{\bx}.
```
Then if $\Phi$ satisfies the RIP of order
$K \geq \| \widetilde{\bx} \|_0 + |\Lambda | + 1$
with isometry constant $\delta_K$, we have

```{math}
:label: eq:omp:3dc0c334-dedf-4c86-8c3d-d72d78951ac0

| h_j - \widetilde{x}_j | 
\leq \frac{\delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2 
\Forall j \notin \Lambda.
```
````
Note that $|\Lambda |$ is the number of entries in the the discovered part
of the support at any iteration in OMP and $\| \widetilde{\bx} \|_0$ 
is the number of entries in not yet discovered part of the support.

````{prf:proof}
.

1. We have $|\Lambda | < K$ and $\| \widetilde{\bx} \|_0 < K - |\Lambda |$.
1. Thus, from {eq}`eq:greedy:5774ac7f-1f4b-464f-882b-9795c5996278`, we obtain

    $$
    \left ( 1 - \frac{\delta_K}{1 - \delta_K} \right )
    \| \widetilde{\bx} \|_2^2 
    \leq \| \Psi_{\Lambda} \widetilde{\bx} \|_2^2
    \leq (1 + \delta_K) \| \widetilde{\bx} \|_2^2.
    $$
1. We can make a statement saying $\Psi_{\Lambda}$ satisfies a RIP of order
   
   $$
   ( \| \widetilde{\bx} \|_0 + |\Lambda | + 1) -  |\Lambda | 
   =  \| \widetilde{\bx} \|_0  + 1
   $$
   with a RIP constant $\frac{\delta_K}{1 - \delta_K}$.
1. By the definition of $\bh$, we have

   $$
    h_j = \langle\Psi_{\Lambda} \widetilde{\bx},  \Psi_{\Lambda} \be_j \rangle
   $$
   where $h_j$ is the $j$-th entry in $\bh$ and
   $\be_j$ denotes the $j$-th vector from the identity basis. 
1. We already know that $h_j = 0$ for all $j \in \Lambda$. 
1. Consider $j \notin \Lambda$ and take the two vectors $\widetilde{\bx}$
   and $\be_j$.
1. We can see that
   
   $$
    \|\widetilde{\bx} \pm \be_j \|_0  \leq \|\widetilde{\bx} \|_0 + 1
   $$
   and
   
   $$
    \supp (\widetilde{\bx} \pm \be_j ) \cap \Lambda = \EmptySet.
   $$
1. Applying {eq}`eq:greedy:ef6701cc-26cb-4293-9f6f-828ce08658c7`
   on the two vectors with $\Psi_{\Lambda}$ as our RIP matrix,
   we see that

   $$
    | \langle \Psi_{\Lambda} \widetilde{\bx}, 
    \Psi_{\Lambda} \be_j \rangle - \langle \widetilde{\bx}, \be_j \rangle | 
    \leq \frac{\delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2 \| \be_j \|_2.
   $$
1. But 
   
   $$
    | \langle \Psi_{\Lambda} \widetilde{\bx}, 
    \Psi_{\Lambda} \be_j \rangle - \langle \widetilde{\bx}, \be_j \rangle | 
    = | h_j - \widetilde{x}_j |.
   $$
1. Noting that $\| \be_j \|_2 = 1$, we get our desired result.
````

With this bound in place, we can develop a sufficient condition under which
the identification step of OMP (which identifies the new index $\lambda^{k + 1}$) 
will succeed.

The following corollary establishes a lower bound on the largest entry
in $\widetilde{\bx}$ which will ensure that OMP indeed chooses
the next index $\lambda^k$ from the support of $\widetilde{\bx}$.

````{prf:corollary}
:label: res:omp:rip:alpha_lower_bound

Suppose that $\Lambda$, $\Phi$, $\widetilde{\bx}$ meet the assumptions
in {prf:ref}`res:omp:rip:inner_product_upper_bound`, and let $\bh$ be as
defined in {eq}`eq:omp:ec749572-224c-4fe1-8796-a35ef1284d4c`.
If 

```{math}
:label: eq:omp:47b4e318-f7c1-4f83-be43-dcb2d2011fa2

\| \widetilde{\bx} \|_{\infty} 
> \frac{2 \delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2,
```
we are guaranteed that

$$
\underset{j \notin \Lambda}{\text{arg} \, \max}|h_j| 
\in \supp(\widetilde{\bx}).
$$
````
````{prf:proof}
.

1. If {eq}`eq:omp:3dc0c334-dedf-4c86-8c3d-d72d78951ac0` is satisfied, then
   for indices $j \notin \supp(\widetilde{\bx})$, we will have
   
   $$
    | h_j | \leq \frac{\delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2.
   $$
1. We already know that $h_j = 0$ for all $j \in \Lambda$.
1. If {eq}`eq:omp:47b4e318-f7c1-4f83-be43-dcb2d2011fa2` is satisfied, then
   there exists $j \in \supp(\widetilde{\bx})$ with
   
   $$
    | \widetilde{\bx}_j | 
    > \frac{2 \delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2.
   $$
1. For this particular $j$,
   applying triangular inequality on
   {eq}`eq:omp:3dc0c334-dedf-4c86-8c3d-d72d78951ac0`
   
   $$
    \frac{\delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2  \geq | h_j - \widetilde{x}_j | 
    \geq | \widetilde{x}_j | - | h_j |.
   $$
1. Thus
    
    $$
    | h_j |  &\geq | \widetilde{x}_j | - \frac{\delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2\\
    &> \frac{2 \delta_K}{1 - \delta_K} \| 
    \widetilde{\bx} \|_2 - \frac{\delta_K}{1 - \delta_K} 
    \| \widetilde{\bx} \|_2\\
    = \frac{\delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2.
   $$
1. We have established that there exists some 
   $j \in \supp(\widetilde{\bx})$ for which
   
   $$
    | h_j | > \frac{\delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2
   $$
   and for every $j \notin \supp(\widetilde{\bx})$
   
   $$
    | h_j | \leq \frac{\delta_K}{1 - \delta_K} \| \widetilde{\bx} \|_2.
   $$
1. Together, they establish that OMP will indeed choose an index
   from the correct set.
````

All we need to do now is to make sure that {eq}`eq:omp:47b4e318-f7c1-4f83-be43-dcb2d2011fa2`
is satisfied by choosing $\delta_K$ small enough.
The following result from {cite}`davenport2010analysis`
guarantees that.

````{prf:theorem}
:label: res:greedy:omp_rip_bound

Suppose that $\Phi$ satisfies the RIP of order $K + 1$ with
isometry constant $\delta < \frac{1}{2 \sqrt{K} + 1}$. 
Then for any $\bx \in \RR^N$ with $\| \bx\|_0 \leq K$,
OMP will recover $\bx$ exactly from $\by = \Phi \bx$ in 
$K$ iterations.
````
The upper bound on $\delta$ can be simplified  can be
simplified as $\delta < \frac{1}{3 \sqrt{K}}$. 

````{prf:proof}
The proof works by induction.
We show that under the stated conditions, 
$\lambda^1 \in \supp(\bx)$.
Then we show that whenever $\lambda^k \in \supp(\bx)$
then $\lambda^{k + 1}$ also $\in \supp(\bx)$.

1. For the first iteration, we have
   
   $$
    \bh^1 = \Phi^T \Phi \by.
   $$
1. Note that $\Phi = \Psi_{\EmptySet}$.
1. It is given that $\| \bx \|_0 \leq K$.
1. Thus due to {prf:ref}`lem:u_sigma_k_norms`:

   $$
    \| \bx \|_{\infty} \geq \frac{\| \bx \|_2}  {\sqrt{K}} .
   $$
1. Now $\delta < \frac{1}{3 \sqrt{K}}$
   or $\delta < \frac{1}{2 \sqrt{K} + 1}$ implies that

    ```{math}
    :label: eq:omp:2fb934e3-6998-4216-8459-31685c4dd941

    \frac{2 \delta}{1 - \delta} < \frac{1}{\sqrt{K}}.
    ```
1. This can be seen as follows. Assuming $K \geq 1$, we have:
    
    $$
    &3 \sqrt{K } \geq 2 \sqrt{K} + 1 \\
    \implies &\frac{1}{3 \sqrt{K}} \leq \frac{1}{2 \sqrt{K} + 1}\\
    \implies &\delta < \frac{1}{2 \sqrt{K} + 1}\\
    \implies &2 \delta \sqrt{K} + \delta < 1 \\
    \implies &2 \delta \sqrt{K} < 1 - \delta \\
    \implies &\frac{2 \delta}{1 - \delta} <  \frac{1}{\sqrt{K}}.
    $$
1. Therefore
    
    $$
    \| \bx \|_{\infty} > \frac{2 \delta}{1 - \delta} \| \bx \|_2
    $$
    and {eq}`eq:omp:47b4e318-f7c1-4f83-be43-dcb2d2011fa2` is satisfied
    and $\lambda^1$ will indeed be chosen from $\supp(\bx)$ 
    due to {prf:ref}`res:omp:rip:alpha_lower_bound`.
1. We now assume that OMP has correctly discovered indices
   up to $\lambda^1, \dots, \lambda^k$. i.e.
   
   $$
    \Lambda^k \subset \supp(\bx).
   $$
1. We have to show that it will also correctly discover $\lambda^{k + 1}$.
1. From the definition of $\widetilde{\bx}$ in
   {eq}`eq:omp:widetilde_alpha_definition`,
   we know that $\supp\left (\widetilde{\bx}^k\right ) \cap \Lambda^k = \EmptySet$.
1. Thus

    $$
    \| \widetilde{\bx}^k \|_0 \leq K - k. 
    $$
1. We also know that $|\Lambda^k | = k$. By assumption $\Phi$
   satisfies RIP of order $K + 1 = (K - k) + k + 1 $.
1. Thus
   
   $$
    K + 1 \geq \| \widetilde{\bx}^k \|_0 + |\Lambda^k | + 1. 
   $$

1. Also due to {prf:ref}`lem:u_sigma_k_norms`:
   
   $$
    \| \widetilde{\bx}^k \|_{\infty} \geq 
    \frac{\| \widetilde{\bx}^k \|_2}{\sqrt{K - k}} \geq
    \frac{\| \widetilde{\bx}^k \|_2}{\sqrt{K}}.
   $$
1. Using {eq}`eq:omp:2fb934e3-6998-4216-8459-31685c4dd941`, we get
   
   $$
    \| \widetilde{\bx}^k \|_{\infty} 
    > \frac{2 \delta}{1 - \delta}\| \widetilde{\bx}^k \|_2.
   $$
1. This is the sufficient condition for {prf:ref}`res:omp:rip:alpha_lower_bound`
   in {eq}`eq:omp:47b4e318-f7c1-4f83-be43-dcb2d2011fa2` giving us

    $$
    \lambda^{k + 1} = 
    \underset{j \notin \Lambda^k}{\text{arg} \, \max}| \bh^{k + 1}_j |  
    \in \supp(\widetilde{\bx}^k).
    $$
1. Hence $\Lambda^{ k + 1} \subseteq \supp(\bx)$.
````



