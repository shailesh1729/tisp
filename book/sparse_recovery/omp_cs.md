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

