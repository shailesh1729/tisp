(sec:cosamp)=
# Compressive Sampling Matching Pursuit

In this section, we look at an algorithm named CoSaMP
(Compressive Sampling Matching Pursuit)
developed in {cite}`needell2009cosamp`.
This algorithm follows in the tradition of
orthogonal matching pursuit while bringing
in other ideas from many recent developments in the field leading to
an algorithm which is much more robust, fast and provides much stronger
guarantees.

This algorithm has many impressive features:

* It can work with a variety of sensing matrices. 
* It works with minimal number of measurements (c.f. basis pursuit).
* It is robust against presence of measurement noise
  (OMP does not have such a claim).
* It provides optimal error guarantees for every signal
  (sparse signals, compressible signals, completely arbitrary signals).
* The algorithm is quite efficient in terms of resource (memory, CPU)
  requirements.

As we move along in this section, we will understand the algorithm
and validate all of these claims.
Hopefully through this process we will have a very 
good understanding of how to evaluate the quality of signal recovery algorithm.

## Algorithm

The algorithm itself is presented in
{prf:ref}`alg:greedy:cosamp:core_algorithm`.

````{prf:algorithm} CoSaMP for iterative sparse signal recovery
:label: alg:greedy:cosamp:core_algorithm

Inputs:
* Sensing matrix $\Phi \in \CC^{M \times N}$
* Measurement vector: $\by \in \CC^M$ where $\by = \Phi \bx + \be$
* Sparsity level: $K$

Outputs:
* $\bz$: a $K$-sparse approximation of the signal:$\bx \in \CC^N$

Initialization:
1. $\bz^0 \leftarrow \bzero$ # Initial approximation
1. $\br^0 \leftarrow \by$ # Residual $\by - \Phi \bz$
1. $k \leftarrow 0$ # Iteration counter

Algorithm:

1. If halting criteria is satisfied: break.
1. $k \leftarrow k + 1$.
1. $\bp \leftarrow \Phi^H \br^{k-1}$ # Form signal proxy
1. $\Omega = \supp(\bp|_{2K})$ # Identify $2K$ large components
1. $T \leftarrow \Omega \cup \supp(\bz^{k-1})$ # Merge supports
1. $\bb_T \leftarrow \Phi_T^{\dag} \by$ # Estimation by least-squares
1. $\bb_{T^c} \leftarrow \bzero$
1. $\bz^k \leftarrow \bb|_K$  # Prune to obtain next approximation
1. $\br^k \leftarrow \by - \Phi \bz^k$ # Update residual
1. Go to step 1.
````

Let us set out the notation before proceeding further.
Most of the things are as usual, with few minor updates.

````{div}
* $\bx \in \CC^N$ represents the signal which is to be
  estimated through the algorithm.
  $\bx$ is unknown to us within the algorithm.
* $N$ is the dimension of ambient signal space, 
  $K \ll N$ is the sparsity level of of the approximation of
  $\bx$ that we are estimating
  and $M$ is the dimension of measurement space (number of measurements $K < M \ll N$).
* We note that $\bx$ itself may not be $K$-sparse.
* Our algorithm is designed to estimate a $K$-sparse approximation of $\bx$.
* $\Phi \in \CC^{M \times N}$ represents the sensing matrix. It is known to the algorithm.
* $\by = \Phi \bx + \be$ represents the measurement vector belonging to $\CC^M$.
  This is known to the algorithm.
* $\be \in \CC^M$ represents the measurement noise which is unknown to us
  within the algorithm.
* $k$ represents the iteration (or step) counter within the algorithm.
* $\bz \in \CC^N$ represents our estimate of $\bx$. $\bz$ is updated iteratively.
* $\bz^k$ represents the estimate of $\bx$ at the end of $k$-th iteration.
* We start with $\bz^0=\bzero$ and update it in each iteration.
* $\bp \in \CC^N$ represents a proxy for $\bx- \bz^{k-1}$.
  We will explain it shortly.
* $T$, $\Omega$ etc. represent index sets (subsets of $\{1,2,\dots, N\}$).
* For any $\bv \in \CC^N$ and any index set $T \subseteq \{1,2,\dots, N\}$,
  $\bv_T$ can mean either of the two things:
  * A vector in $\CC^{|T|}$ consisting of only those entries in $\bv$ which are
    indexed by $T$.
  * A vector in $\CC^N$ whose entries indexed by $T$ are same as that of $\bv$ while
    entries indexed by $\{1,2,\dots, N\} \setminus T$ are set all to zero.
    
    ```{math}
    :label: eq:96451a22-d91b-44ba-a209-34010fb150ab

    v_{T}(i) = \left\{
            \begin{array}{ll}
                v(i) & \mbox{if $i \in T$};\\
                0 & \mbox{otherwise}.
            \end{array}
          \right.
    ```
* For any $\bv \in \CC^N$ and any integer $1 \leq n \leq N$, $\bv|_n$ means
  a vector in $\CC^N$ which consists of the $n$ largest (in magnitude) entries
  of $\bv$ (at the corresponding indices) while rest of the entries in $\bv|_n$ are 0.
* With an index set $T$, $\Phi_T$ means an $M \times |T|$ matrix consisting of
  selected columns of $\Phi$ indexed by $T$.
* $\br \in \CC^M$ represents the difference between the actual measurement vector
  $\by$ and estimated measurement vector $\Phi \bz$.
* Ideal estimate of $\br$ would be $\be$ itself.
  But that won't be possible to achieve in general.
* $\bx|_K$ is the best $K$-sparse approximation of $\bx$ which can
  be estimated by our algorithm ({prf:ref}`def:ssm:largest_entries_signal`). 
````

````{prf:example} Clarifying the notation in CoSaMP
:label: res-sr-cosamp-ex-1

1. Let us consider

    $$
    \bx = (-1, 5, 8, 0, 0, -3, 0, 0, 0, 0)
    $$
1. Then

    $$
    \bx|_2 = (0, 5, 8, 0, 0, 0, 0, 0, 0, 0)
    $$
1. Also

    $$
    \bx|_4 = \bx
    $$
    since $\bx$ happens to be $4$-sparse.
1. For $\Lambda = \{1,2,3,4\}$, we have

    $$
    x_{\{1,2,3,4\}} = (-1, 5, 8, 0, 0, 0, 0, 0, 0, 0)
    $$
    or

    $$
    x_{\{1,2,3,4\}} = (-1, 5, 8, 0)
    $$
    in different contexts.
````

 
### The Signal Proxy

As we have learnt by now that the most challenging part in a signal recovery 
algorithm is to identify the support of the $K$-sparse approximation.
OMP identifies one index in the support at each iteration and hopes that it
never makes any mistakes.
It ends up taking $K$ iterations and solving $K$ least squares problems.
If there could be a simple way which could identify 
the support quickly (even if roughly), that can help in tremendously 
accelerating the algorithm.
The fundamental innovation in CoSaMP is to identify the support
through the signal proxy. 

1. If $\bx$ is $K$-sparse and $\Phi$ satisfies RIP
   (see {ref}`sec:ssm:rip`)
    of order $K$ with the restricted isometry constant $\delta_K \ll 1$
    then it can be argued that $\bp = \Phi^H \Phi \bx$
    can serve as a proxy for the signal $\bx$. 
1. In particular the largest $K$ entries of $\bp$ point towards the largest
   $K$ entries of $\bx$.
1. Although we don't know $\bx$ inside the algorithm,
   yet we have access to $\by = \Phi \bx$
   (assuming error to be $\bzero$),
   the proxy can be easily estimated by computing $\bp = \Phi^H \by$. 

This is the key idea in CoSaMP.
1. Rather than identifying just one new index in support of $\bx$,
   it tries to identify whole of support by picking up the largest $2K$
   entries of $\bp$.
1. It then solves a least squares problem around the columns of $\Phi$
   indexed by this support set.
1. It keeps only the $K$ largest entries from the least squares solution
   as an estimate of $\bx$.
1. Of course there is no guarantee that in a single attempt
   the support of $\bx$ will be  recovered completely.
1. Hence the residual between actual measurement vector $\by$
   and estimated measurement vector $\Phi \bz$ is computed
   and it is used to identify other indices of $\supp(\bx)$ iteratively.

### Core of Algorithm

There are two things which are estimated in each iteration of algorithm

1. $K$-sparse estimate of $\bx$ at $k$-th step: $\bz^k$. 
1. Residual at $k$-th step: $\br^k$.

Residual and proxy:

1. We start with a trivial estimate $\bz^0 = \bzero$
   and improve it in each iteration.
1. $\br^0$ is nothing but the measurement vector $\by$.
1. As explained before $\br^k$ is the difference between
   actual measurement vector $\by$ and the estimated
   measurement vector $\Phi \bz^k$.
1. This $\br^k$ is used for computing the signal proxy at $k$-th step.
1. Concretely assuming $\be=\bzero$
   
   $$
    \bp = \Phi^H \br^k 
    = \Phi^H (\by - \Phi \bz^k) 
    = \Phi^H \Phi (\bx - \bz^k).
   $$
1. Thus $\bp$ is the proxy of the difference between
   the original signal and the estimated signal.


During each iteration, the algorithm performs following tasks

1. [Identification] The algorithm forms a proxy of the residual
   $\br^{k-1}$ and locates the $2K$ largest entries of the proxy.
1. [Support merger] The set of newly identified indices is merged with 
   the set of indices that appear in the current approximation
   $\bz^{k-1}$ (i.e. $\supp(\bz^{k-1})$).
1. [Estimation] The algorithm solves a least squares problem
   to approximate the signal $\bx$ on the merged set of indices.
1. [Pruning] The algorithm produces a new approximation $\bz^k$
   by retaining only the largest $K$ entries in the least squares solution.
1. [Residual update] Finally the new residual $\br^k$ between original
   measurement vector $\by$ and estimated measurement vector
   $\Phi \bz^k$ is computed.

The steps are repeated until the halting criteria is reached.
We will discuss the halting criteria in detail later.
A possible halting criteria is when the norm of residual $\br^k$
reaches a very small value.

(sec:greedy:cosamp:sparse_case_analysis)=
## CoSaMP Analysis Sparse Case

In this subsection, we will carry out a detailed theoretical analysis of
CoSaMP algorithm for sparse signal recovery.

We will make following assumptions in the analysis:


*  The sparsity level $K$ is fixed and known in advance.
*  The signal $\bx$ is $K$-sparse (i.e. $\bx \in \Sigma_K \subseteq \CC^N$).
*  The sensing matrix $\Phi$ satisfies RIP of order $4K$ with $\delta_{4K} \leq 0.1$.
*  Measurement error $\be \in \CC^M$ is arbitrary.

````{div}
For each iteration, we need to define one more quantity: *recovery error*

$$
\bd^k = \bx - \bz^k.
$$
The quantity $\bd^k$ captures the difference between actual signal $\bx$
and estimated signal $\bz^k$ at the end of $k$-th iteration.

1. Under ideal recovery, $\bd^k$ should become $\bzero$ as $k$ increases.
1. Since we don't know $\bx$ within the algorithm,
   we cannot see $\bd^k$ directly.
1. We do have following equation

   $$
    \br^k &= \by - \Phi \bz^k\\
    &= \Phi \bx + \be - \Phi \bz^k \\ 
    &= \Phi (\bx - \bz^k)  + \be  \\
    &= \Phi \bd^k + \be.
   $$
1. We will show that in each iteration, CoSaMP reduces the recovery
   error by a constant factor while adding a small multiple of the
   measurement noise $\|\be\|_2$. 
1. As a result, when recovery error is large compared to measurement noise,
   the algorithm makes substantial progress in each step.
1. The algorithm stops making progress when recovery error
   is of the order of measurement noise.

We will consider some iteration $k \geq 1$ and
analyze the behavior of each of the steps:
identification, support merger, estimation, pruning and residual update one by one.

1. At the beginning of the iteration we have

    $$
    \br^{k-1} = \Phi (\bx - \bz^{k - 1}) + \be 
    = \Phi \bd^{k - 1} + \be.
    $$
1. The quantities of interest are 
   $\bz^{k-1}$, $\br^{k-1}$ and $\bd^{k-1}$
   out of which $\bd^{k-1}$ is unknowable.
1. In order to simplify the equations below we will write
   
   $$
    \br = \br^{k-1}, \; \bz = \bz^{k-1} \; \text{ and } \bd = \bd^{k-1}.
   $$
````

```{list-table} Terms used in analysis
:header-rows: 1

* - Term
  - Description
  - Details
* - $\bx$
  - $K$ sparse signal
  - 
* - $\Phi$
  - Sensing matrix
  -
* - $\be$
  - Measurement noise
  - 
* - $\by$
  - Measurement vector
  - $\by  = \Phi \bx + \be$
* - $\bz$
  - A $K$ sparse estimate of $\bx$ at the beginning of the iteration
  - $\bz = \bz^{k-1} = \bb|_K$, $\bb_T = \Phi_T^{\dag} \by$
* - $\br$
  - Residual at the beginning of the iteration
  - $\br = \br^{k -1} = \by - \Phi \bz^{k - 1}$
* - $\bd$
  - Recovery error at the beginning of the iteration
  - $\bd = \bd^{k-1} = \bx  - \bz^{k-1}$
* - $\bp$
  - The proxy for $\bd$
  - $\bp - \Phi^H \br = \Phi^H (\Phi \bd^{k-1} + \be)$
* - $\Omega$
  - The index set of largest $2K$ entries in $\bp$
  - 
```
 
### Identification

We start our analysis with the identification step in the main loop of CoSaMP
({prf:ref}`alg:greedy:cosamp:core_algorithm`).


````{div}

1. We compute $\bp = \Phi^H \br$ and consider
   $\Omega = \supp(\bp|_{2K})$ as the index
   set of largest $2K$ indices in $\bp$.
1. We will show that most of the energy in $\bd$ (the recovery error)
   is concentrated in the entries indexed by $\Omega$.
1. In other words, we will be looking for a bound of the form
   
   $$
    \| \bd_{\Omega^c} \|_{2} \ll \| \bd \|_2.
   $$
1. Since $\bx$ is $K$-sparse and $\bz$ is $K$-sparse hence $\bd$ is
   $2K$-sparse.
   1. In first iteration where $\bz^0 = \bzero$,
      support of $\bd^0$ is same as support of $\bx$.
   1. In later iterations it may include more indices.
1. Let

   $$
    \Gamma = \supp(\bd).
   $$
1. We remind that $\Omega$ is known to us while $\Gamma$ is unknown to us.
1. Ideal case would be when $\Gamma \subseteq \Omega$.
1. Then we would have recovered whole of support of $\bx$;
   recovering $\bx$ would therefore be easier.
1. Let us examine what are the differences between the two sets.
1. We have $|\Omega| \leq 2K$ and $|\Gamma| \leq 2K$.
1. Moreover, $\Omega$ indexes $2K$ largest entries in $\bp$.
1. Thus we have (due to {prf:ref}`lem:ssm:best_k_term_approximation`)
   
   ```{math}
    :label: eq:e8c6dc0f-4262-4911-a973-7c52b312762e
    \| \bp_{\Gamma} \|_2 \leq \| \bp_{\Omega} \|_2
    ```
    where $\bp_{\Gamma},  \bp_{\Omega} \in \CC^N$
    are obtained from $\bp$ as per {prf:ref}`def:ssm:signal_restriction`.
1. Squaring {eq}`eq:e8c6dc0f-4262-4911-a973-7c52b312762e`
   on both sides and expanding we get

    $$
    \sum_{\gamma \in \Gamma} |p_{\gamma}|^2  
    \leq \sum_{\omega \in \Omega} |p_{\omega}|^2.
    $$
1. Now we do hope that some of the entries are common in both sides. 
   Those entries are indexed by $\Gamma \cap \Omega$.
1. The remaining entries on L.H.S. are indexed by $\Gamma \setminus \Omega$
   and on the R.H.S. are indexed by $\Omega \setminus \Gamma$.
1. Hence we have

    ```{math}
    :label: eq:D10D1D93-E8FB-4092-909C-C623B19B7928

    \| \bp_{\Gamma \setminus \Omega} \|_2^2 
    \leq \| \bp_{\Omega \setminus \Gamma} \|_2^2
    \implies \| \bp_{\Gamma \setminus \Omega} \|_2 
    \leq \| \bp_{\Omega \setminus \Gamma} \|_2.
    ```
1. For both $\Gamma \setminus \Omega$ and $\Omega \setminus \Gamma$ we have

    $$
    | \Gamma \setminus \Omega | 
    \leq 2 K \; \text{ and } \; 
    |\Omega \setminus \Gamma| \leq 2 K.
    $$
1. The worst case happens when both sets are totally disjoint.
1. Let us first examine the R.H.S and find an upper bound for it.

    $$
     \| \bp_{\Omega \setminus \Gamma} \|_2 
     &= \| \Phi_{\Omega \setminus \Gamma}^H \br \|_2  \\
     &= \| \Phi_{\Omega \setminus \Gamma}^H (\Phi \bd + \be) \|_2\\
    & \leq \| \Phi_{\Omega \setminus \Gamma}^H \Phi \bd \|_2 
    + \| \Phi_{\Omega \setminus \Gamma}^H \be \|_2.
    $$
    At this juncture, its worthwhile to scan various results in
   {ref}`sec:ssm:rip` since we are going to need
   many of them in the following steps.
1. Let us look at the term $\| \Phi_{\Omega \setminus \Gamma}^H \Phi \bd \|_2$. 
1. We have $ |\Omega \setminus \Gamma| \leq 2K$.
1. Further $\bd$ is $2K$ sparse and sits over $\Gamma$ 
   which is disjoint with  $\Omega \setminus \Gamma$. 
1. Together $|\Gamma \cup \Omega| \leq 4K$.
1. A straightforward application of
   {prf:ref}`cor:approximate_orthogonality_submatrix_vector` gives us

   $$
    \| \Phi_{\Omega \setminus \Gamma}^H \Phi \bd \|_2 
    \leq \delta_{4K} \|  \bd  \|_2.
   $$
1. Similarly using
   {prf:ref}`lem:proj:rip:phi_phi_H_embedding_l2_norm_upper_bound`
   we get

    $$
    \| \Phi_{\Omega \setminus \Gamma}^H \be \|_2 
    \leq \sqrt{1 + \delta_{2K}} \| \be \|_2.
    $$
1. Combining the two we get

    ```{math}
    :label: eq:2D13B94B-2F02-4404-9808-E7484D697DAE
    \| \bp_{\Omega \setminus \Gamma} \|_2 
    \leq  \delta_{4K} \|  \bd  \|_2 + \sqrt{1 + \delta_{2K}} \| \be \|_2.
    ```
1. We now look at L.H.S. and find a lower bound for it. 

    $$
    \| \bp_{\Gamma \setminus \Omega} \|_2  
    &= \|  \Phi_{\Gamma \setminus \Omega}^H \br \|_2 \\
     &= \| \Phi_{\Gamma \setminus \Omega}^H (\Phi \bd + \be) \|_2.
    $$
1. We will split  $\bd$ as 
    
    $$
    \bd = \bd_{\Gamma \setminus \Omega} + \bd_{\Omega}.
    $$
1. Further we will use a form of triangular inequality as
    
    $$
    \| \ba + \bb \| \geq \|\ba \| - \| \bb \|.
    $$
1. We  expand L.H.S.
    
    $$
     \| \Phi_{\Gamma \setminus \Omega}^H (\Phi \bd + \be) \|_2 
    &=  \| \Phi_{\Gamma \setminus \Omega}^H \left (\Phi \left ( \bd_{\Gamma \setminus \Omega} + \bd_{\Omega} \right) + \be \right) \|_2\\
    &\geq  \| \Phi_{\Gamma \setminus \Omega}^H \Phi \bd_{\Gamma \setminus \Omega} \|_2
    - \| \Phi_{\Gamma \setminus \Omega}^H \Phi \bd_{\Omega} \|_2
    - \| \Phi_{\Gamma \setminus \Omega}^H \be \|_2.
    $$
1. As before 

    $$
    \| \Phi_{\Gamma \setminus \Omega}^H \Phi \bd_{\Gamma \setminus \Omega} \|_2 
    = \| \Phi_{\Gamma \setminus \Omega}^H \Phi_{\Gamma \setminus \Omega} \bd_{\Gamma \setminus \Omega} \|_2.
    $$
1. We can use the lower bound from
   {prf:ref}`lem:proj:rip:phi_J_gram_embedding_l2_norm_bounds_range`
   to give us
    
    $$
    \| \Phi_{\Gamma \setminus \Omega}^H \Phi_{\Gamma \setminus \Omega} \bd_{\Gamma \setminus \Omega} \|_2 
    \geq (1 - \delta_{2K}) \| \bd_{\Gamma \setminus \Omega} \|_2 
    $$
    since $|\Gamma \setminus \Omega| \leq 2K $.
1. For the other two terms we need to find their upper bounds
   since they appear in negative sign.
1. Applying {prf:ref}`cor:approximate_orthogonality_submatrix_vector` we get

    $$
    \| \Phi_{\Gamma \setminus \Omega}^H \Phi \bd_{\Omega} \|_2 
    \leq \delta_{2K} \|  \bd\|_2.
    $$
1. Again using {prf:ref}`lem:proj:rip:phi_phi_H_embedding_l2_norm_upper_bound`
   we get
    
    $$
    \| \Phi_{\Gamma \setminus \Omega}^H \be \|_2 
    \leq \sqrt{1 + \delta_{2K}} \| \be \|_2.
    $$
1. Putting the three bounds together, we get a lower bound for L.H.S.

    ```{math}
    :label: eq:A8AF1455-5B2B-4896-BFA5-B2861BFA28D0
    \| \bp_{\Gamma \setminus \Omega} \|_2 
    \geq (1 - \delta_{2K}) \| \bd_{\Gamma \setminus \Omega} \|_2
    -  \delta_{2K} \|  \bd\|_2 - \sqrt{1 + \delta_{2K}} \| \be \|_2.
    ```
1. Finally plugging the upper bound from
   {eq}`eq:2D13B94B-2F02-4404-9808-E7484D697DAE`
   and lower bound from {eq}`eq:A8AF1455-5B2B-4896-BFA5-B2861BFA28D0`
   into {eq}`eq:D10D1D93-E8FB-4092-909C-C623B19B7928` we get

    $$
    & (1 - \delta_{2K}) \| \bd_{\Gamma \setminus \Omega} \|_2
    -  \delta_{2K} \|  \bd\|_2 - \sqrt{1 + \delta_{2K}} \| \be \|_2 
    \; \leq \; \delta_{4K} \|  \bd  \|_2 + \sqrt{1 + \delta_{2K}} \| \be \|_2\\
    \implies &  (1 - \delta_{2K}) \| \bd_{\Gamma \setminus \Omega} \|_2
    \leq \left ( \delta_{2K} +   \delta_{4K} \right )\|  \bd  \|_2  
    + 2 \sqrt{1 + \delta_{2K}} \| \be \|_2\\
    \implies &  \| \bd_{\Gamma \setminus \Omega} \|_2 \leq 
    \frac{\left ( \delta_{2K} +   \delta_{4K} \right )\|  \bd  \|_2  
    + 2 \sqrt{1 + \delta_{2K}} \| \be \|_2}
    {1 - \delta_{2K}}.
    $$
1. This result is nice but there is a small problem.
   We would like to get rid of
   $\Gamma$ from L.H.S. and get $\bd_{\Omega^c}$ instead.
1. Recall that

    $$
    \Omega^c = (\Gamma \cap \Omega^c) \cup (\Gamma^c \cap \Omega^c)
    $$
    where $\Gamma \cap \Omega^c$ and $\Gamma^c \cap \Omega^c$ are disjoint.
1. Thus
   
    $$
    \bd_{\Omega^c} = \bd_{\Gamma \cap \Omega^c} + \bd_{\Gamma^c \cap \Omega^c}.
    $$
1. Since $\bd$ is $\bzero$ on $\Gamma^c$ (recall that $\Gamma = \supp(\bd)$), hence
   
   $$
    \bd_{\Gamma^c \cap \Omega^c} = \bzero.
    $$
1. As a result
    
    $$
    \bd_{\Omega^c} = \bd_{\Gamma \cap \Omega^c} = \bd_{\Gamma \setminus \Omega}.
    $$
1. This gives us

    ```{math}
    :label: eq:4ED9419B-2635-4F10-B3C0-7CBB69928420

    \| \bd_{\Omega^c} \|_2 
    \leq \frac{\left ( \delta_{2K} +   \delta_{4K} \right )\|  \bd  \|_2  
    + 2 \sqrt{1 + \delta_{2K}} \| \be \|_2}
    {1 - \delta_{2K}}.
    ```
1. Let us simplify this equation by using $\delta_{2K} \leq \delta_{4K} \leq 0.1$
   assumed at the beginning of the analysis.
1. This gives us
    
    $$
    1 - \delta_{2K} \geq 0.9,\; 
    \delta_{2K} + \delta_{4K} \leq 0.2, \; 
    2 \sqrt{1 + \delta_{2K}} \leq 2 \sqrt{1.1} = 2.098.
    $$
1. Thus we get

    $$
    \| \bd_{\Omega^c} \|_2 \leq \frac{ 0.2\|  \bd  \|_2  + 2.098 \| \be \|_2}{.9}.
    $$
1. Simplifying

    ```{math}
    :label: eq:greedy:cosamp:identification_analysis_recovery_error_bound

    \| \bd_{\Omega^c} \|_2 \leq  0.223 \|  \bd  \|_2  + 2.331 \| \be \|_2.
    ```
1. This result tells us that in the absence of measurement noise, at least 78%
   of energy in the recovery error is indeed concentrated in the entries
   indexed by $\Omega$. 
1. Moreover, if the measurement noise is small compared to
   the size of recovery error, then
   this concentration continues to hold.
1. Thus even if we don't know $\Gamma$ directly, 
   $\Omega$ is a close approximation for $\Gamma$. 
````
We summarize the analysis for the *identification* step in the following lemma.

````{prf:lemma}
:label: lem:greedy:cosamp:identification_proxy_support_energy_bound

Let $\Phi$ satisfy RIP of order $4K$ with $\delta_{4K} \leq 0.1$.
At every iteration $k$ in CoSaMP algorithm, let 
$\bd^{k - 1} = (\bx - \bz^{k - 1})$ be the recovery error and 
$\bp  = \Phi^H \br^{k - 1}$ be the signal proxy.
The set $\Omega =  \supp(\bp|_{2K})$  contains at most $2K$ indices and

```{math}
:label: eq:greedy:cosamp:identification_proxy_support_energy_bound

\| \bd^{k - 1}_{\Omega^c} \|_2 
\leq  0.223 \|  \bd^{k - 1}  \|_2  + 2.331 \| \be \|_2.
```
In other words, most of the energy in $\bd^{k - 1}$ is concentrated
in the entries indexed by $\Omega$
when measurement noise is small.
````

 
### Support Merger

The next step in a CoSaMP iteration is support merger. 
Recalling from {prf:ref}`alg:greedy:cosamp:core_algorithm`,
the step involves computing

$$
T = \Omega \cup \supp(\bz)
$$
i.e. we merge the support of current signal estimate $\bz$ with the
newly identified set of indices $\Omega$.

````{div}
In previous lemma we were able to show how well the recovery error
is concentrated over the index set $\Omega$. But we didn't establish
anything concrete about how $\bx$ is concentrated. In the support merger
step, we will be able to show that $\bx$ is highly concentrated over
the index set $T$. For this we will need to find an upper bound
on $\|\bx_{T^c}\|_2$ i.e. the energy of entries in $\bx$ which are
not covered by $T$.


1. We recall that $|\Omega| \leq 2K$ and since $\bz$ is a
   $K$-sparse estimate of $\bx$ hence
   $|\supp(\bz)| \leq K$.
1. Thus

    $$
    |T | \leq 3K.
    $$
1. Clearly

    $$
    T^c = \Omega^c \cap \supp(\bz)^c \subseteq \Omega^c.
    $$
1. Further since $\supp(\bz) \subseteq T$ hence $\bz_{T^c} = \bzero$.
1. Thus

    $$
    \bx_{T^c} =  (\bx - \bz)_{T^c} = \bd_{T^c}.
    $$
1. Since $T^c \subseteq \Omega^c$ hence

    $$
    \| \bd_{T^c} \|_2 \leq \| \bd_{\Omega^c} \|_2.
    $$
1. Combining these facts we can write

    $$
    \| \bx_{T^c} \|_2 = \| \bd_{T^c} \|_2 \leq \| \bd_{\Omega^c} \|_2.
    $$
1. We summarize this analysis in following lemma.

````{prf:lemma}
:label: lem:greedy:cosamp:support_merger_x_omega_c_energy_bound

Let $\Omega$ be a set of at most $2K$ entries.
The set $T = \Omega \cup \supp(\bz^{k-1})$ contains
at most $3K$ entries, and

```{math}
:label: eq:greedy:cosamp:support_merger_x_omega_c_energy_bound

\| \bx_{T^c} \|_2 \leq \| \bd_{\Omega^c} \|_2.
```
````

```{div}
Note that this inequality says nothing about how $\Omega$ is chosen.
But we can use an
upper bound on $\| \bd_{\Omega^c} \|_2$ 
from {prf:ref}`lem:greedy:cosamp:identification_proxy_support_energy_bound`
to get an upper bound on $\| \bx_{T^c} \|_2$.
```

 
### Estimation


The next step is a least square estimate of $\bx$ over the columns indexed by $T$. Recalling from {prf:ref}`alg:greedy:cosamp:core_algorithm`
we compute

$$
\bb_T = \Phi_T^{\dag} \by =  \Phi_T^{\dag} (\Phi \bx + \be). 
$$

````{div}
1. We also set $\bb_{T^c} = \bzero$.
1. We have

    $$
    \bb = \bb_T + \bb_{T^c} = \bb_T.
    $$
1. Since $|T| \leq 3K$, $\bb$ is a $3K$-sparse approximation of $\bx$.
1. What we need here is a bound over the approximation error $\| \bx - \bb \|_2$.
1. We have already obtained a bound on  $\| \bx_{T^c} \|_2$.
1. If an upper bound on $\| \bx - \bb \|_2$ depends on $\| \bx_{T^c} \|_2$
   and measurement noise $\|\be \|_2$ that would be quite reasonable.
1. We start with splitting $\bx$ over $T$ and $T^c$.

    $$
    \bx = \bx_T + \bx_{T^c}.
    $$
1. Since $\supp(\bb) \subseteq T$ hence

    $$
    \bx - \bb = \bx_T + \bx_{T^c} - \bb_T = (\bx_T - \bb_T) + \bx_{T^c}.
    $$
1. This gives us

    $$
    \| \bx - \bb \|_2 \leq \| \bx_T - \bb_T \|_2 + \| \bx_{T^c} \|_2.
    $$
1. We will now expand the term $\| \bx_T - \bb_T \|_2$.

    $$
    \| \bx_T - \bb_T \|_2 = \| \bx_T -  \Phi_T^{\dag} (\Phi \bx + \be) \|_2
    = \| \bx_T -  \Phi_T^{\dag} (\Phi \bx_T + \Phi \bx_{T^c} + \be) \|_2
    $$
1. Now since $\Phi_T$ is full column rank (since $\Phi$ satisfies RIP of order $3K$)
   hence $\Phi_T^{\dag} \Phi_T = \bI$.
1. Also $\Phi \bx_T = \Phi_T \bx_T$ (since column columns indexed by $T$ are involved).
1. This helps us cancel $\bx_T  - \Phi_T^{\dag} \Phi \bx_T$. 
1. Thus

    $$
    \| \bx_T - \bb_T \|_2 
    =   \| \Phi_T^{\dag} (\Phi \bx_{T^c} + \be) \|_2
    \leq \| (\Phi_T^H \Phi_T)^{-1} \Phi_T^H \Phi \bx_{T^c} \|_2 
    + \|  \Phi_T^{\dag} \be \|_2.
    $$
1. Let us look at the terms on R.H.S. one by one.
1. Let $\bv  = \Phi_T^H \Phi \bx_{T^c}$.
1. Then

    $$
    \| (\Phi_T^H \Phi_T)^{-1} \Phi_T^H \Phi \bx_{T^c} \|_2 
    = \| (\Phi_T^H \Phi_T)^{-1} \bv \|_2.
    $$
1. This perfectly fits
   {prf:ref}`lem:proj:rip:phi_J_gram_embedding_l2_norm_bounds_range`
   with $|T| \leq 3K$ giving us

    $$
    \| (\Phi_T^H \Phi_T)^{-1} \Phi_T \Phi \bx_{T^c} \|_2 
    \leq \frac{1}{1 - \delta_{3K}} \|  \Phi_T^H \Phi \bx_{T^c}\|_2.
    $$
1. Further, applying {prf:ref}`cor:approximate_orthogonality_submatrix_vector` we get

    $$
    \|  \Phi_T^H \Phi \bx_{T^c}\|_2 \leq \delta_{4K} \| \bx_{T^c}\|_2
    $$
    since $|T \cup \supp(\bx)| \leq 4K$.
1. For the measurement noise term, applying
   {prf:ref}`lem:proj:rip:phi_pseudo_inverse_embedding_l2_norm_upper_bound`
   we get

    $$
    \|  \Phi_T^{\dag} \be \|_2 \leq \frac{1}{\sqrt{1 - \delta_{3K}}} \|\be \|_2.
    $$
1. Combining the above inequalities we get

    $$
    \| \bx - \bb \|_2 
    \leq \left [1 +  \frac{\delta_{4K}}{1 - \delta_{3K}} \right ]  
    \| \bx_{T^c}\|_2 +  \frac{1}{\sqrt{1 - \delta_{3K}}} \|\be \|_2.
    $$
1. Recalling our assumption that $\delta_{3K} \leq \delta_{4K} \leq 0.1$
   we can simplify the constants to get

    $$
    \| \bx - \bb \|_2 \leq 1.112 \| \bx_{T^c}\|_2  + 1.0541 \| \be \|_2.
    $$
````
We summarize the analysis in this step in the following lemma.
````{prf:lemma}
:label: lem:greedy:cosamp:estimation_x_omega_c_energy_bound

Let $T$ be a set of at most $3K$ indices,
and define the least squares signal estimate $\bb$ by the formula

$$
    \bb_T = \Phi_T^{\dag} \by 
    =  \Phi_T^{\dag} (\Phi \bx + \be) \; \text{ and } 
    \bb_{T^c} = \bzero. 
$$
If $\Phi$ satisfies RIP of order $4K$ with $\delta_{4K} \leq 0.1$
then the following holds

$$
\| \bx - \bb \|_2 \leq 1.112 \| \bx_{T^c}\|_2  + 1.0541 \| \be \|_2.
$$
````
Note that the lemma doesn't make any assumptions about
how $T$ is arrived at except that $|T| \leq 3K$.
Also, this analysis assumes that the least squares solution
is of infinite precision given by $\Phi_T^{\dag} \by$.
The approximation error in an iterative least squares solution
needs to be separately analyzed to identify
the number of required steps so that the least squares error is negligible.

### Pruning

The last step in the main loop of CoSaMP
({prf:ref}`alg:greedy:cosamp:core_algorithm`) is pruning.

````{div}
We compute

$$
\bz^k = \bb|_K
$$
as the next estimate of $\bx$ by picking the $K$ largest entries in $\bb$.

1. We note that both $\bx$ and $\bb|_K$ can be
   regarded as $K$ term approximations of $\bb$.
1. As established in {prf:ref}`lem:ssm:best_k_term_approximation`,
   $\bb|_K$ is the best $K$-term approximation of $\bb$.
1. Thus

    $$
    \| \bb - \bb|_K \|_2 \leq \|\bb - \bx \|_2.
    $$
1. Now 

    $$
    \| \bx  - \bz^k \|_2 = \| \bx -\bb + \bb -  \bb|_K \|_2 
    \leq \| \bx - \bb \|_2 +   \| \bb - \bb|_K \|_2 \leq  2 \| \bx - \bb \|_2.
    $$
1. This helps us establish that although the $3K$-sparse approximation
   $\bb$ is closer to $\bx$ compared to
   $\bb|_K$, but $\bb|_K$ is also not too bad approximation of $\bx$
   while using only $K$ entries at most.
````

We summarize it in following lemma.
````{prf:lemma}
:label: lem:greedy:cosamp:pruning_bound

The pruned estimate $\bz^k = \bb|_K$ satisfies 

```{math}
:label: eq:greedy:cosamp:pruning_bound

\| \bx - \bz^k \|_2 = \| \bx - \bb|_K \|_2 \leq 2 \| \bx  - \bb \|_2.
```
````

 
### The CoSaMP Iteration Invariant

Having analyzed each of the steps in the main loop of CoSaMP algorithm,
it is time  for us to combine the analysis.
Concretely, we wish to establish how much 
progress CoSaMP makes in each iteration.
Following theorem provides an upper bound
on how the recovery error changes from one iteration to next iteration.
This  theorem is known as the iteration invariant for the sparse case. 

````{prf:theorem} CoSaMP iteration invariant for exact sparse recovery
:label: thm:greedy:cosamp:iteration_invariant_sparse_case

Assume that $\bx$ is $K$-sparse.
Assume that $\Phi$ satisfies RIP of order $4K$ with $\delta_{4K} \leq 0.1$.
For each iteration number $k \geq 1$, the signal estimate
$\bz^k$ is $K$-sparse and satisfies 

$$
\| \bx - \bz^{k} \|_2 \leq \frac{1}{2} \| \bx - \bz^{k-1} \|_2 + 7.5 \|\be \|_2.
$$
In particular

$$
\| \bx  - \bz^{k} \|_2 \leq 2^{-k} \| \bx \|_2 + 15 \| \be \|_2.
$$
````
This theorem helps us establish that if measurement noise is small,
then the algorithm makes substantial progress in each iteration.
The proof makes use of the lemmas developed above.

````{prf:proof}
We run the proof in backtracking mode.
We start from $\bz^{k}$ and go back step by step
through pruning, estimation, support merger, and identification
to connect it with $\bz^{k-1}$. 

1. From {prf:ref}`lem:greedy:cosamp:pruning_bound` we have

    $$
    \| \bx - \bz^k \|_2  = \| \bx - \bb|_K \|_2 \leq 2 \| \bx  - \bb \|_2.
    $$
1. Applying {prf:ref}`lem:greedy:cosamp:estimation_x_omega_c_energy_bound`
   for the least squares estimation step gives us

    $$
    2 \| \bx - \bb \|_2 \leq 2 \cdot (1.112 \| \bx_{T^c}\|_2  + 1.0541 \| \be \|_2)
    = 2.224 \| \bx_{T^c}\|_2  + 2.1082 \| \be \|_2.
    $$
1. {prf:ref}`lem:greedy:cosamp:support_merger_x_omega_c_energy_bound` (Support merger)
   tells us that

    $$
    \| \bx_{T^c} \|_2 \leq \| \bd^{k - 1}_{\Omega^c} \|_2.
    $$
1. This gives us

    $$
    \| \bx - \bz^k \|_2 
    \leq 2.224  \| \bd^{k - 1}_{\Omega^c} \|_2  + 2.1082 \| \be \|_2.
    $$
1. From identification step we have 
   {prf:ref}`lem:greedy:cosamp:identification_proxy_support_energy_bound`

    $$
    \| \bd^{k - 1}_{\Omega^c} \|_2 
    \leq  0.223 \|  \bd^{k - 1}  \|_2  + 2.331 \| \be \|_2.
    $$
1. This gives us

    $$
    \| \bx - \bz^k \|_2  
    &\leq 2.224  \left ( 0.223 \|  \bd^{k - 1}  \|_2  
        + 2.331 \| \be \|_2 \right )   + 2.1082 \| \be \|_2\\
    &\leq 0.5 \|  \bd^{k - 1}  \|_2 + 7.5 \| \be \|_2\\
    &= \frac{1}{2} \|  \bx - \bz^{k - 1}  \|_2 + 7.5 \| \be \|_2.
    $$
    The constants have been simplified to make them look better.
1. For the 2nd result in this theorem, we add up the error at each stage as 

    $$
    (1 + 2^{-1} + 2^{-2} + \dots + 2^{-(k-1)}) 7.5 \| \be \|_2 
    \leq 2 \cdot 7.5 \| \be\|_2 = 15 \| \be \|_2.
    $$
1. At $k=1$ we have $\bz^0 = \bzero$.
1. This gives us the result

    $$
    \| \bx  - \bz^{k} \|_2 \leq 2^{-k} \| \bx \|_2 + 15 \| \be \|_2.
    $$
````

## CoSaMP Analysis General Case

Having completed the analysis for the sparse case
(where the signal $\bx$ is $K$-sparse) it is time
for us to generalize the analysis for the case where
$\bx$ is assumed to be an arbitrary signal in $\CC^N$.
Although it may look hard at first sight but there is a
simple way to transform the problem 
into the problem of CoSaMP for the sparse case.

1. We decompose $\bx$ into its $K$-sparse
   approximation and the approximation error.
1. Further, we absorb the approximation error term
   into the measurement error term.
1. Since sparse case analysis is applicable
   for an arbitrary measurement error,
   this approach gives us an upper bound on the performance
   of CoSaMP over arbitrary signals.

---

````{div}
1. We start with writing

    $$
    \bx = \bx - \bx|_K + \bx|_K
    $$
    where $\bx|_K$ is the best $K$-term approximation of $\bx$
    ({prf:ref}`lem:ssm:best_k_term_approximation`).
1. Thus we have

    $$
    \by =  \Phi \bx + \be  
    = \Phi (\bx - \bx|_K + \bx|_K)  + \be 
    = \Phi \bx|_K + \Phi (\bx - \bx|_K)  + \be.
    $$
1. We define
   
   $$
    \widehat{\be} = \Phi (\bx - \bx|_K)  + \be.
   $$
1. This lets us write
   
   $$
    \by = \Phi \bx|_K  + \widehat{\be}.
   $$
1. In this formulation, the problem is equivalent to recovering
   the $K$-sparse signal $\bx|_K$ from
   the measurement vector $\by$.
1. The results of {ref}`sec:greedy:cosamp:sparse_case_analysis`
   and in particular the iteration invariant 
   {prf:ref}`thm:greedy:cosamp:iteration_invariant_sparse_case`
   apply directly.
1. The remaining problem is to estimate the norm of modified
   error $\widehat{\be}$.
1. We have

    $$
    \| \widehat{\be} \|_2 
    = \| \Phi (\bx - \bx|_K)  + \be \|_2 
    \leq \| \Phi (\bx - \bx|_K) \|_2 + \|\be \|_2.
    $$
1. Another result for RIP on the energy bound of embedding of
   arbitrary signals from {prf:ref}`thm:proj:rip:arbitrary_signal_energy_bound` gives us

    $$
    \|  \Phi (\bx - \bx|_K)\|_2 
    \leq  \sqrt{ 1 + \delta_K} 
    \left [  \| \bx - \bx|_K \|_2 + \frac{1}{\sqrt{K}} 
    \| \bx - \bx|_K \|_1 \right ].
    $$
1. Thus we have an upper bound on $\|\widehat{\be} \|_2$ 
   given by

    $$
    \| \widehat{\be} \|_2 
    \leq \sqrt{ 1 + \delta_K} 
    \left [  \| \bx - \bx|_K \|_2 + \frac{1}{\sqrt{K}} 
    \| \bx - \bx|_K \|_1 \right ] +  \|\be \|_2.
    $$
1. Since we have assumed throughout that $\delta_{4K} \leq 0.1$,
   it gives us

    $$
    \| \widehat{\be} \|_2 
    \leq 1.05 \left [  \| \bx - \bx|_K \|_2 
    + \frac{1}{\sqrt{K}} \| \bx - \bx|_K \|_1 \right ] 
    +  \|\be \|_2.
    $$
1. This inequality is able to combine measurement error
   and approximation error into a single expression.
1. To fix ideas further, we define the notion of
   unrecoverable energy in CoSaMP.
````

````{prf:definition} Unrecoverable energy
:label: def:greedy:cosamp:unrecoverable_energy

The *unrecoverable energy* in CoSaMP algorithm is defined as

$$
\nu =  \left [  \| \bx - \bx|_K \|_2 + 
\frac{1}{\sqrt{K}} \| \bx - \bx|_K \|_1 \right ] +  \|\be \|_2.
$$
This quantity measures the baseline error in the CoSaMP recovery consisting of measurement error and approximation error.
````

````{div}
It is obvious that

$$
\| \widehat{\be} \|_2 \leq 1.05 \nu.
$$
````

We summarize this analysis in following lemma.
````{prf:lemma}
:label: lem:greedy:cosamp:reduction_sparse_case

Let $\bx \in \CC^N$ be an arbitrary signal.
Let $\bx|_K$ be its best $K$-term approximation.
The measurement vector $\by = \Phi \bx + \be$ 
can be expressed as $\by = \Phi \bx|_K + \widehat{\be}$
where

$$
\| \widehat{\be} \|_2 
\leq 1.05 \left [  \| \bx - \bx|_K \|_2 
+ \frac{1}{\sqrt{K}} \| \bx - \bx|_K \|_1 \right ] 
+  \|\be \|_2 \leq 1.05 \nu.
$$
````
We now move ahead with the development of the
iteration invariant for the general case.

````{div}

1. Invoking {prf:ref}`thm:greedy:cosamp:iteration_invariant_sparse_case`
   for the iteration invariant for recovery of a sparse signal gives us
    
    $$
    \| \bx|_K - \bz^{k} \|_2 
    \leq \frac{1}{2} \| \bx|_K - \bz^{k-1} \|_2 
    + 7.5 \|\widehat{\be} \|_2.
    $$
1. What remains is to generalize this inequality for the 
   arbitrary signal $\bx$ itself.
1. We can write

    $$
    \| \bx|_K - \bx + \bx - \bz^{k} \|_2 
    \leq \frac{1}{2} \| \bx|_K  - \bx + \bx - \bz^{k-1} \|_2 
    + 7.5 \|\widehat{\be} \|_2.
    $$
1. We simplify L.H.S. as
    
    $$
    \| \bx|_K - \bx + \bx - \bz^{k} \|_2 
    = \|(\bx - \bz^{k}) - (\bx - \bx|_K)\|_2 
    \geq \| \bx - \bz^{k} \|_2 - \|\bx - \bx|_K \|_2.
    $$
1. On the R.H.S. we expand as

    $$
    \| \bx|_K  - \bx + \bx - \bz^{k-1} \|_2 
    \leq \|  \bx - \bz^{k-1} \|_2 + \|\bx - \bx|_K \|_2.
    $$
1. Combining the two we get

    $$
    \| \bx - \bz^{k} \|_2 
    \leq 0.5  \|  \bx - \bz^{k-1} \|_2 
    + 1.5 \|\bx - \bx|_K \|_2 +  7.5 \|\widehat{\be} \|_2.
    $$
1. Putting the estimate of $\|\widehat{\be}\|_2$ from
   {prf:ref}`lem:greedy:cosamp:reduction_sparse_case`
   we get

    $$
    \| \bx - \bz^{k} \|_2 
    \leq 0.5  \|  \bx - \bz^{k-1} \|_2 
    + 9.375 \|\bx - \bx|_K \|_2 
    +  \frac{7.875}{\sqrt{K}}\| \bx - \bx|_K \|_1 
    +  7.5 \|\be \|_2.
    $$
1. Now

    $$
    & 9.375 \|\bx - \bx|_K \|_2 
    +  \frac{7.875}{\sqrt{K}}\| \bx - \bx|_K \|_1 
    +  7.5 \|\be \|_2 \\
    & \leq
    10 \left (\left [  \| \bx - \bx|_K \|_2 
        + \frac{1}{\sqrt{K}} \| \bx - \bx|_K \|_1 \right ] 
        +  \|\be \|_2 \right ).
    $$
1. Thus we write a simplified expression

    $$
    \| \bx - \bz^{k} \|_2 
    \leq 0.5  \|  \bx - \bz^{k-1} \|_2  + 10 \nu
    $$
    where $\nu$ is the unrecoverable energy ({prf:ref}`def:greedy:cosamp:unrecoverable_energy`).
````

We can summarize the analysis for the general case in the following theorem.

````{prf:theorem} CoSaMP iteration invariant for general signal recovery
:label: thm:greedy:cosamp:iteration_invariant_general_case

Assume that $\Phi$ satisfies RIP of order $4K$
with $\delta_{4K} \leq 0.1$.
For each iteration number $k \geq 1$, the signal estimate
$\bz^k$ is $K$-sparse and satisfies 

$$
\| \bx - \bz^{k} \|_2 
\leq \frac{1}{2} \| \bx - \bz^{k-1} \|_2 + 10 \nu.
$$
In particular

```{math}
:label: eq:greedy:cosamp:iteration_invariant_general_case_invariant

\| \bx  - \bz^{k} \|_2 
\leq 2^{-k} \| \bx \|_2 + 20 \nu.
```
````
````{prf:proof}
1st result was developed in the development before the theorem. 
For the 2nd result in this theorem, we add up the error
at each stage as 

$$
(1 + 2^{-1} + 2^{-2} + \dots + 2^{-(k-1)}) 10 \nu 
\leq 2 \cdot 10 \nu = 20 \nu.
$$
At $k=1$ we have $\bz^0 = \bzero$. This gives us the result.
````


 
### SNR Analysis

````{div}

1. A sensible though unusual definition of *signal-to-noise ratio*
   (as proposed in {cite}`needell2009cosamp`)
   is as follows

    ```{math}
    :label: eq:greedy:cosamp:snr

    \SNR = 10 \log \left ( \frac{\| \bx \|_2 }{ \nu}\right ).
    ```
1. The whole of unrecoverable energy is treated as noise.
1. The signal $\ell_2$ norm rather than its square is
   being treated as the measure of its energy.
   This is the unusual part.
1. Yet the way $\nu$ has been developed,
   this definition is quite sensible.
1. Further we define the *reconstruction SNR* or *recovery SNR*
   as the ratio between signal energy and recovery error energy.

   ```{math}
    :label: eq:greedy:cosamp:r-snr
    \RSNR = 10 \log 
    \left ( \frac{\| \bx \|_2 }{ \| \bx - \bz \|_2 }\right ).
    ```
1. Both $\SNR$ and $\RSNR$ are expressed in dB.
1. Certainly we have
   
   $$
    \RSNR \leq \SNR.
   $$
1. Let us look closely at the iteration invariant 

    $$
    \| \bx  - \bz^{k} \|_2 \leq 2^{-k} \| \bx \|_2 + 20 \nu.
    $$
1. In the initial iterations, 
   $2^{-k} \| \bx \|_2$ term dominates in the R.H.S. 
1. Assuming 

    $$
    2^{-k} \| \bx \|_2 \geq 20 \nu
    $$
    we can write
    
    $$
    \| \bx  - \bz^{k} \|_2 \leq 2 \cdot 2^{-k} \| \bx \|_2.
    $$
1. This gives us

    ```{math}
    & \| \bx  - \bz^{k} \|_2 
    \leq 2^{-k + 1} \| \bx \|_2 \\
    \implies & \frac{\| \bx \|_2 }{ \| \bx - \bz \|_2 } 
    \geq 2^{k-1}\\
    \implies & \RSNR \geq 10 (k-1) \log 2 
    \geq 3 k - 3.
    ```
1. In the later iterations, the $20\nu$ term dominates
   in the R.H.S. 
1. Assuming 
    
    $$
    2^{-k} \| \bx \|_2 \leq 20 \nu
    $$
    we can write
    
    $$
    \| \bx  - \bz^{k} \|_2 \leq 2 \cdot 20 \nu = 40 \nu.
    $$
1. This gives us

    ```{math}
    & \| \bx  - \bz^{k} \|_2 \leq  40 \nu\\
    \implies & \frac{\| \bx \|_2 }{ \| \bx - \bz \|_2 } 
    \geq \frac{1}{40} \frac{\| \bx \|_2 }{ \nu }\\
    \implies & \RSNR \geq \SNR - 10 \log 40 
    \geq \SNR - 16 = \SNR - 13 - 3.
    ```
1. We combine these two results into the following

    ```{math}
    :label: eq:greedy:cosamp:r_snr_lower_bound

    \RSNR \geq \min\{ 3 k, \SNR - 13 \} - 3.
    ```
1. This result tells us that in the
   initial iterations the reconstruction SNR keeps
   improving by $3$dB per iteration till 
   it hits the noise floor given by $\SNR - 16$ dB.
1. Thus roughly the number of iterations required
   for converging to the noise floor is given by

    $$
    k \approx \frac{\SNR - 13}{3}.
    $$
````
