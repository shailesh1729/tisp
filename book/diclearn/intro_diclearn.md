# Introduction

When designing a dictionary for a particular application, we have several  options {cite}`rubinstein2010dictionaries`. 
On the one hand we can go through the long list of analytically constructed or tunable dictionaries and
select one of them as suitable for the application in concern. 
On the other hand, we can take up a number of real example signals
from our application 
and try to construct a dictionary which is optimized for these. 

*Dictionary learning* (DL) 
{cite}`tosic2011dictionary, elad2010sparse`
is a process which attempts to solve the problem of constructing a dictionary  directly from the set of example signals.
The atoms of a learnt dictionary come from the underlying
empirical data of training set of example signals
for the specific application. 
While analytically constructed dictionaries are typically
meant for only specific applications,
the learning method allows one to construct dictionaries 
for any family of signals which are amenable to
the sparse and redundant representations model. 
This certainly comes at a cost.
Learnt dictionaries have to be held completely in memory 
explicitly as they happen to be lack any structure. 
Thus they don't provide an efficient implementation of analysis 
($\bDDD^H \bx$) and synthesis ($\bDDD \ba$) operators. 
Thus using them in applications leads to more computational costs. 

---

We start by formalizing the notation for Dictionary Learning (DL).

````{div}
1. We consider a set of $S$ example signals put together in
   a signal matrix $\bX \in \CC^{N \times S}$. 
1. Consider a dictionary $\bDDD \in \CC^{N \times D}$. 
1. Let $\ba^i \in \CC^{D}$ be the sparsest possible representation
   of $\bx^i$ in $\bDDD$ 
   with 

   $$
   \bx^i = \bDDD \ba^i + \be^i.
   $$
1. We put all $\ba^i$ together in a matrix
   $\bA \in \CC^{D \times S}$.
1. Then we have

   $$
   \bX = \bDDD \bA + \bE
   $$
   where $\bE \in \CC^{N \times S}$ represents approximation error. 
1. We are looking for best dictionary from the set of
   possible dictionaries such that we are able
   to get sparse representations of $\bx^i$
   with low approximation error. 
1. We can quantify the  notion of good approximation by
   putting an upper bound on the norm of approximation error as
   $\| \be^i \|_2 \leq \epsilon$.
1. Combining these ideas, we introduce the notion of a 
   *sparse signal model* denoted 
   as $\MMM_{\bDDD, K, \epsilon}$ which consists of a 
   dictionary $\bDDD$ providing $K$-sparse representations 
   for a class of signals
   (from which the example signals are drawn)
   with an upper bound on approximation
   error given by $\epsilon$.
1. The DL problem tries to learn best model $\MMM$ based on
   the example signals $\bX$.

---

```{div}
1. We can formulate the DL problem as an
   optimization problem as follows:

    ```{math}
    :label: eq-dl-opt-problem-1

    & \underset{\bDDD, \{\ba^i \}_{i=1}^{S} }{\text{minimize }}
    & & \sum_{i=1}^S \| \ba^i \|_0 \\
    & \text{subject to }
    & & \| \bx^i - \bDDD \ba^i \|_2  \leq \epsilon, \; i = 1, \ldots, S.
    ```
1. In this version, we are trying to minimize total sparsity of
   $\ba^i$ while using the upper bound on approximation error as optimization constraint.
1. We are not enforcing sparsity constraint that
   $\| \ba^i \|_0  \leq K \Forall 1 \leq i \leq S$.
1. Alternatively we can also write:
    ```{math}
    :label: eq-dl-opt-problem-2
        & \underset{\bDDD, \{\ba^i \}_{i=1}^{S} }{\text{minimize }}
        & & \sum_{i=1}^S \| \bx^i - \bDDD \ba^i \|_2^2 \\
        & \text{subject to }
        & &  \| \ba^i \|_0 \leq K, \; i = 1, \ldots, S.
    ```
1. In this version we are trying to minimize approximation error
   while keeping $K$-sparsity as optimization constraint.
1. We are not enforcing the constraint that
   $\| \be^i \|_2 \leq \epsilon$.
1. Unfortunately, there doesn't exist any computationally
   tractable algorithm to solve these optimization problems.
1. An alternative is to consider a heuristic iterative approach
   presented in {prf:ref}`alg:dl:iterative_approach`.
````

````{prf:algorithm} Dictionary learning: iterative approach
:label: alg:dl:iterative_approach

Initialization:

1. Choose an initial dictionary  $\bDDD^0$.
1. $k \leftarrow 0$ # iteration counter.
\Repeat{halting criteria is true}{

Algorithm:

1. If halting criteria is met: break. 
1. $k \leftarrow k + 1$.
1. Obtain representations $\ba^i$ for $\bx^i$
   with the given $\bDDD^{k-1}$ and sparsity level $K$
   using some sparse approximation algorithm.
1. Obtain new dictionary $\bDDD^k$ from the signals
   $\bx^i$ and their representations $\ba^i$.
````

````{div}
Some possible halting criteria are: 

*  Stop after a fixed number of iterations.
*  Stop when $\| \be^i \|_2 \leq \epsilon$ for every example.
*  Stop when approximation errors stop improving.

For initialization of the algorithm, we have few options. 

*  We can start with a randomly generated dictionary.
*  We can select $D$ examples from $\bX$ and
   put them together as our starting dictionary.
*  We can start with some analytical dictionary
   suitable for the application domain. 
````

## Dictionary Learning Methods

Two popular algorithms implementing this approach are
MOD (Method of Optimal Directions) and K-SVD.


### Method Of Optimal Directions

````{div}
In *MOD* {cite}`engan1999method`, dictionary update is formulated as

$$
\bDDD^k = \text{arg} \underset{\bDDD}{\min} \| \bX - \bDDD \bA^k \|_{F}^2
$$
A straight forward least squares solution is obtained as

$$
\bDDD^k = \bX (\bA^k)^{\dag}.
$$
````

### K-SVD

````{div}

K-SVD {cite}`aharon2005k` is slightly different.
Rather than recomputing whole dictionary
at once by solving the LS problem, it updates atoms of $\bDDD$ one by one.

1. Let $j$ be the index of atom $\bd_j$ being updated.
1. Consider the error 

    $$
    \bE_j = \bX - \sum_{k, k\neq j} \bd_k \bb_k^T
    $$
1. $\bb_k$ refers to the $k$-th row of $\bA$;
   i.e. entries for atom $\bd_k$ in every example.
1. $\bE_j$ means the approximation error when the atom $\bd_j$
   (and corresponding entries in $\bA$)
   has been dropped from consideration.
1. We can see that
    
    $$
    \bX - \bDDD \bA = \bX - \sum_{k=1}^D \bd_k \bb_k^T
    = \bX - \sum_{k, k\neq j} \bd_k \bb_k^T - \bd_j \bb_j^T
    = \bE_j - \bd_j \bb_j^T.
    $$
1. Hence

    $$
    \| \bX - \bDDD \bA \|_F^2 = \| \bE_j - \bd_j \bb_j^T \|_F^2.
    $$
1. On the L.H.S. we have total approximation error.
1. On the R.H.S. we have the same expressed in terms of $\bE_j$
   and $\bd_j$ where $\bE_j$ doesn't depend on $\bd_j$.
1. An optimal $\bd_j$ is one which can minimize R.H.S.
1. This can easily be obtained by rank-1 approximation of $\bE_j$.
1. The rank-1 approximation gives us both $\bd_j$ as well as the entries in
   the $j$-th row of $\bA$ given by $\bb_j$.
   There is a small catch though.
1. In general the rank-1 approximation
   can lead to a dense $\bb_j$ meaning the atom $\bd_j$
   gets used in many signal representations.
   We wish to avoid that.
   We don't want $\bd_j$ to appear in many signal representations.
1. For this, we identify representations $\ba^i$ in which atom $\bd_j$ appears,
   and let them be indexed by $\Gamma$.
1. We then restrict $\bE_j$ to signals indexed by $\Gamma$
   to avoid a dense  $\bb_j$.
1. Rank-1 approximation can be easily obtained using singular value decomposition. 
1. We perform  SVD of $\bE_{j,\Gamma} = \bU \Sigma \bV^H$. 
1. We then pick $\bu_1, \sigma_1, \bv_1$.
1. $\bu_1$ is the new update for $\bd_j$. 
1. Further $\sigma_1 \bv_1$ is the update for $\bb_{j, \Gamma}$.
1. Rest of $\bb_j$ is left with zero entries.
1. We repeat the process for each of the atoms in $\bDDD$
   to obtain next update of $\bDDD$.
````
