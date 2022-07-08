(sec:sa:omp)=
# Orthogonal Matching Pursuit

*Orthogonal Matching Pursuit* is a greedy algorithm for
computing sparse approximations of a signal in a suitable
dictionary.
The goal of this algorithm is to select a small number of
atoms from the dictionary which can provide a representation
for the signal with low error.
The algorithm is iterative in structure.
In each step we greedily select one new atom from the
dictionary which can maximally reduce the representation error.
Once we have enough atoms selected such that the representation
error is below an acceptable bound, we stop.
The algorithm is presented in {prf:ref}`alg-sa-omp`.


````{prf:algorithm} Orthogonal matching pursuit for sparse approximation
:label: alg-sa-omp

Inputs:
* Signal dictionary $\bDDD \in \CC^{N \times D}$ with $\spark(\bDDD) > 2K \ll D$
* Threshold $\epsilon_0$
* Signal $\bx \in \CC^N$

Outputs:
* $K$-sparse approximate representation $\ba \in \Sigma_{K} \subseteq \CC^D$
  satisfying $\|\bx - \bDDD \ba\|_2 \leq \epsilon_0$
* $S$ support for sparse solution identified by the algorithm


Initialization:
1. $k \leftarrow 0$ # Iteration counter
1. $\ba^0 \leftarrow \bzero$ # Solution vector $\ba \in \CC^D$
1. $\br^0 \leftarrow \bx - \bDDD \ba^0 = \bx$ # Residual $\br \in \CC^N$
1. $S^0 \leftarrow \EmptySet$ # Solution support $S = \supp(\ba)$

Algorithm:

1. If $\| \br^k \|_2 \leq \epsilon_0$ break.
1. $k \leftarrow k + 1$ # Next iteration
1. $\bz \leftarrow \bDDD^H \br^{k - 1}$ # Sweep 
1. Update support
   1. Find $j_0$ that maximizes $|z_j| \Forall j \notin S^{k-1}$ 
   1. $S^{k} \leftarrow S^{k - 1} \cup \{ j_0\}$ 
1. Update provisional solution 
  
   $$
   \ba^k \leftarrow \underset{\ba}{\text{minimize}}\, \| \bDDD \ba - \bx \|^2_2
   \quad \text{ subject to }\quad \supp(\ba) = S^{k}.
   $$
1. $\br^k \leftarrow \bx - \bDDD \ba^k = \bx - \bDDD_{S^k} \ba^k_{S^k}$ # Update residual
1. Go to step 1.
````


## The Algorithm

````{div}
*  We start with the initial estimate of solution $\ba=\bzero$. 
*  We also maintain the support of $\ba$; i.e., the set of indices for which $\ba$ is non-zero.
*  We start with an empty support.
*  In each ($k$-th) iteration we attempt to reduce the difference between the actual signal $\bx$ 
   and the approximate signal based on current solution $\ba^{k-1}$
   given by $\br^{k-1} = \bx - \bDDD \ba^{k-1}$.
*  We do this by choosing a new index in $\ba$ given by $j_0$ for the column $\bd_{j_0}$
   which most closely matches our current residual.
*  We include this to our support for $\ba$ and estimate new solution vector $\ba^k$.
*  We then compute the new residual $\br^k$.
*  We stop when the residual magnitude is below a threshold $\epsilon_0$ defined by us.


Each iteration of algorithm consists of following stages:

1. [Sweep] We try to find the best matching atom from the dictionary with the current residual.
   1. The best matching atom is selected using the least square error principle.
   1. For each column $\bd_j$ in our dictionary,
      we measure the projection of residual from previous iteration $\br^{k-1}$
      on the column
   1. We compute the magnitude of error between the projection and residual.
   1. The square of minimum error for $\bd_j$ is given by:
      
      $$
      \epsilon^2(j) = \| \br^{k-1}\|_2^2 - |\bd_j^H \br^{k-1}|^2.
      $$
   1. We can also note that minimizing over $\epsilon(j)$ is equivalent to 
      maximizing over the inner product of $\bd_j$ with $\br^{k-1}$.
1. [Update support] Ignoring the columns which have already been included in the support,
   we pick up the column which most closely resembles the residual of previous stage;
   i.e., the magnitude of error is minimum.
   We include the index of this column $j_0$ in the support set $S^{k}$.
1. [Update provisional solution]
   1. In this step we find the solution of minimizing $\| \bDDD \ba - \bx \|^2$
      over the support $S^k$ as our next candidate solution vector.
   1. By keeping $a_i = 0$ for $i \notin S^k$ we are leaving out corresponding
      columns $\bd_i$ from our calculations.
   1. Thus we pickup up only the columns specified by $S^k$ from $\bDDD$.
   1. Let us call this subdictionary as $\bDDD_{S^k}$.
   1. The size of this subdictionary is $N \times | S^k | = N \times k$. 
   1. Let us call corresponding sub vector as $\ba_{S^k}$.
      > Suppose $D=4$, then
      > $\bDDD = \begin{bmatrix} \bd_1 & \bd_2 & \bd_3 & \bd_4 \end{bmatrix}$.
      > Let $S^k = \{1, 4\}$.
      > Then $\bDDD_{S^k} = \begin{bmatrix} \bd_1 & \bd_4 \end{bmatrix}$
      > and $\ba_{S^k} = (a_1, a_4)$.
   1. Our minimization problem then reduces to minimizing $\|\bDDD_{S^k} \ba_{S^k} - \bx \|_2$.
   1. We use standard least squares estimate for getting the coefficients
      for $\ba_{S^k}$ over these indices.
   1. We put back $\ba_{S^k}$ to obtain our new solution estimate $\ba^k$.
      > In the running example after obtaining the values $a_1$ and $a_4$,
      > we will have $\ba^k = (a_1, 0 , 0, a_4)$.
   1. The solution to this minimization problem is given by
      
      $$
      \bDDD_{S^k}^H ( \bDDD_{S^k}\ba_{S^k} - \bx ) = \bzero 
      \implies \ba_{S^k} = ( \bDDD_{S^k}^H \bDDD_{S^k} )^{-1} \bDDD_{S^k}^H \bx.
      $$

   1. Interestingly we note that $\br^k = \bx - \bDDD \ba^k = \bx - \bDDD_{S^k} \ba_{S^k}$, thus
      
      $$
      \bDDD_{S^k}^H \br^k = \bzero
      $$
      which means that columns in $\bDDD_{S^k}$ which are part of support $S^k$
      are necessarily orthogonal to the residual $\br^k$.
   1. This implies that these columns will not be considered in the coming iterations
      for extending the support.
   1. This orthogonality is the reason behind the name of the algorithm as OMP.
1. [Update residual] We finally update the residual vector to $\br^k$
   based on new solution vector estimate.
````

````{prf:example} $(\bDDD, K)$-EXACT-SPARSE reconstruction with OMP

Let us consider a dictionary of size $10 \times 20$. 
Thus $N=10$ and $D=20$. In order to fit into the display, we will
present the matrix in two 10 column parts.

```{math}
\bDDD_a = \frac{1}{\sqrt{10}}
\begin{bmatrix}
-1 & -1 & -1 & 1 & -1 & -1 & 1 & 1 & -1 & 1\\
1 & 1 & 1 & 1 & 1 & -1 & -1 & 1 & -1 & -1\\
-1 & -1 & -1 & -1 & -1 & 1 & 1 & 1 & 1 & 1\\
1 & -1 & -1 & 1 & 1 & 1 & -1 & 1 & 1 & 1\\
1 & 1 & 1 & -1 & -1 & 1 & -1 & -1 & 1 & 1\\
1 & -1 & 1 & -1 & -1 & -1 & 1 & -1 & 1 & -1\\
-1 & -1 & 1 & 1 & -1 & -1 & -1 & -1 & 1 & -1\\
1 & -1 & 1 & 1 & -1 & 1 & -1 & -1 & -1 & 1\\
-1 & 1 & -1 & 1 & 1 & -1 & -1 & -1 & 1 & 1\\
1 & 1 & 1 & 1 & -1 & 1 & -1 & 1 & -1 & 1
\end{bmatrix}\\
\bDDD_b = \frac{1}{\sqrt{10}}
\begin{bmatrix}
1 & -1 & -1 & -1 & 1 & 1 & 1 & -1 & -1 & -1\\
1 & 1 & 1 & -1 & -1 & -1 & -1 & -1 & -1 & 1\\
-1 & 1 & 1 & 1 & 1 & 1 & -1 & -1 & -1 & -1\\
1 & -1 & 1 & -1 & 1 & 1 & 1 & -1 & -1 & -1\\
1 & -1 & -1 & 1 & 1 & 1 & -1 & 1 & 1 & -1\\
-1 & 1 & 1 & 1 & -1 & 1 & -1 & 1 & -1 & 1\\
-1 & 1 & 1 & -1 & 1 & -1 & -1 & -1 & 1 & 1\\
1 & -1 & -1 & 1 & 1 & -1 & -1 & 1 & -1 & 1\\
1 & 1 & 1 & 1 & -1 & -1 & 1 & 1 & 1 & -1\\
-1 & -1 & 1 & 1 & -1 & 1 & 1 & -1 & -1 & 1
\end{bmatrix}
```

with $\bDDD = \begin{bmatrix}\bDDD_a & \bDDD_b \end{bmatrix}$.

1. You may verify that each column is unit norm. 
1. It is known that $\Rank(\bDDD) = 10$ and $\spark(\bDDD)= 6$.
1. Thus if a signal $\bx$ has a $2$ sparse representation in $\bDDD$
   then the representation is necessarily unique.
1. We now consider a signal $\bx$ given by

    ```{math}
    \bx = \begin{pmatrix}
    4.74342 & -4.74342 & 1.58114 & -4.74342 & -1.58114 \\
    1.58114 & -4.74342 & -1.58114 & -4.74342 & -4.74342
    \end{pmatrix}.
    ```
    For saving space, we have written it as an $n$-tuple over two rows. 
    You should treat it as a column vector of size $10 \times 1$.
1. It is known that the vector has a two sparse representation in $\bDDD$.
1. Let us go through the steps of OMP and see how it works.
1. In step 0, $\br^0= \bx$, $\ba^0 = \bzero$, and $S^0  = \EmptySet$. 
1. We now compute absolute value of inner product of $\br^0$ with each of the columns.
   They are given by

    $$
    \begin{pmatrix}
    4 & 4 & 4 & 7 & 3 & 1 & 11 & 1 & 2 & 1 \\ 
    2 & 1 & 7 & 0 & 2 & 4 & 0 & 2 & 1 & 3
    \end{pmatrix}.
    $$
1. We quickly note that the maximum occurs at index 7 with value 11.
1. We modify our support to $S^1 = \{ 7 \}$.
1. We now solve the least squares problem 
   
   $$
    \text{minimize} \left \| \bx - [\bd_7] a_7 \right \|_2^2.
   $$
1. The solution gives us $a_7 = 11.00$.
1. Thus we get

    $$
    \ba^1 = \begin{pmatrix}
    0 & 0 & 0 & 0 & 0 & 0 & 11 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0
    \end{pmatrix}.
    $$
    Again note that to save space we have presented $\ba$ over two rows.
    You should consider it as a $20 \times 1$ column vector.
1. This leaves us the residual as
    
    $$
    \br^1 = \bx - \bDDD \ba^1 = 
    \begin{pmatrix}
    1.26491 & -1.26491 & -1.89737 & -1.26491 & 1.89737 \\
    -1.89737 & -1.26491 & 1.89737 & -1.26491 & -1.26491
    \end{pmatrix}.
    $$
1. We can cross check that the residual is indeed orthogonal to the columns already selected,
   for
    
    $$
    \langle \br^1 , \bd_7 \rangle  = 0.
    $$
1. Next we compute inner product of $\br^1$ with all the columns in $\bDDD$
   and take absolute values.
1. They are given by
    
    $$
    \begin{pmatrix}
    0.4 & 0.4 & 0.4 & 0.4 & 0.8 & 1.2 & 0 & 1.2 & 2 & 1.2 \\
    2.4 & 3.2 & 4.8 & 0 & 2 & 0.4 & 0 & 2 & 1.2 & 0.8
    \end{pmatrix}
    $$
1. We quickly note that the maximum occurs at index 13 with value $4.8$.
1. We modify our support to $S^1 = \{ 7, 13 \}$.
1. We now solve the least squares problem
    
    $$
    \text{minimize} 
    \left \| \bx - \begin{bmatrix} \bd_7 & \bd_{13} \end{bmatrix}  
    \begin{bmatrix}  a_7  \\ a_{13} \end{bmatrix}  \right \|_2^2.
    $$
1. This gives us $a_7 = 10$ and $a_{13} = -5$.
1. Thus we get

    $$
    \ba^2 = \begin{pmatrix}
    0 & 0 & 0 & 0 & 0 & 0 & 10 & 0 & 0 & 0 \\
    0 & 0 & -5 & 0 & 0 & 0 & 0 & 0 & 0 & 0
    \end{pmatrix}
    $$
1. Finally the residual we get at step 2 is
    
    $$
    \br^2 = \bx - \bDDD \ba^2 = 
    10^{-14} \begin{pmatrix}
    0 & 0 & -0.111022 & 0 & 0.111022 \\
    -0.111022 & 0 & 0.111022 & 0 & 0
    \end{pmatrix}
    $$
1. The magnitude of residual is very small.
1. We conclude that our OMP algorithm has converged and we have been able
   to recover the exact 2 sparse representation of $\bx$ in $\bDDD$.
````

## Exact Recovery Conditions

````{div}
In this subsection, following {cite}`tropp2004greed`, we will closely look at some conditions
under which OMP is guaranteed to recover the solution for $(\mathcal{D}, K)$-EXACT-SPARSE
{prf:ref}`problem <def-ssm-d-k-exact-sparse-problem>`.

1. It is given that $\bx = \bDDD \ba$ where $\ba$ contains at most $K$ non-zero entries. 
1. Both the support and entries of $\ba$ are known
   and can be used to verify the correctness of OMP.
   Note that $\ba$ itself won't be given to OMP.
1. Let $\Lambda_{\opt} = \supp(\ba)$; i.e., the set of indices at which
   optimal representation $\ba$ has non-zero entries.
1. Then we can write
    
    $$
    \bx  = \sum_{i \in \Lambda} a_i \bd_i.
    $$
1. From the dictionary $\bDDD$ we can extract a $N \times K$ matrix $\bDDD_{\opt}$
   whose columns are indexed by $\Lambda_{\opt}$. 
   
   $$
    \bDDD_{\opt} \triangleq \begin{bmatrix} \bd_{\lambda_1} & \dots & \bd_{\lambda_K} \end{bmatrix} 
   $$
   where $\lambda_i \in \Lambda_{\opt}$.
1. Thus we can also write
   
   $$
    \bx  = \bDDD_{\opt}  \ba_{\opt}
    $$
    where $\ba_{\opt} \in \CC^K$ is a vector of $K$ complex entries.
1. The columns of optimum $\bDDD_{\opt}$ are linearly independent.
   Hence $\bDDD_{\opt}$ has full column rank.
1. We define another matrix $\bHHH_{\opt}$ whose columns are the remaining $D - K$ columns of $\bDDD$.
1. Thus $\bHHH_{\opt}$ consists of atoms or columns which do not participate
   in the optimum representation of $\bx$.
1. OMP starts with an empty support.
1. At every step, it picks up one column from $\bDDD$ and adds to the
   support of approximation.
1. If we can ensure that it never selects any column from $\bHHH_{\opt}$
   we will be guaranteed that correct $K$ sparse representation is recovered.
1. We will use mathematical induction and assume that OMP has succeeded in its first $k$ steps
   and has chosen $k$ columns from $\bDDD_{\opt}$ so far.
1. At this point it is left with the residual $\br^k$. 
1. In $(k+1)$-th iteration, we compute inner product of $\br^k$ with all columns in $\bDDD$
   and choose the column which has highest inner product. 
1. We note that the maximum value of inner product of $\br^k$ with any of the columns in
   $\bHHH_{\opt}$ is given by

   $$
    \| \bHHH_{\opt}^H \br^k \|_{\infty}.
   $$
1. Correspondingly, the maximum value of inner product of $\br^k$ with any of the columns in $\bDDD_{\opt}$
   is given by
   
   $$
    \| \bDDD_{\opt}^H \br^k \|_{\infty}.
   $$
1. since we have shown that $\br^k$ is orthogonal to the columns already chosen,
  hence they will not contribute to this term.
1. In order to make sure that none of the columns in $\bHHH_{\opt}$ is selected,
   we need
   
   $$
    \| \bHHH_{\opt}^H \br^k \|_{\infty} < \| \bDDD_{\opt}^H \br^k \|_{\infty}.
   $$
````

````{prf:definition} Greedy selection ratio
:label: def:greedy:omp:greedy_selection_ratio

We define a ratio

```{math}
:label: eq:greedy:omp:greedy_selection_ratio

\rho(\br^k) \triangleq 
\frac{\| \bHHH_{\opt}^H \br^k \|_{\infty}}
{\| \bDDD_{\opt}^H \br^k \|_{\infty}}.
```
This ratio is known as *greedy selection ratio*.
````


1. We can see that as long as $\rho(\br^k) < 1$,
   OMP will make a right decision at $(k+1)$-th stage.
1. If $\rho(\br^k) = 1$ then
   there is no guarantee that OMP will make the right decision.
1. We will assume pessimistically that OMP makes wrong decision in such situations.

We note that this definition of $\rho(\br^k)$ looks very similar to matrix $p$-norms defined
in  {prf:ref}`def:mat:p_matrix_norm`.
It is suggested to review the properties of $p$-norms for matrices at this point.

We now present a condition which guarantees that $\rho(\br^k) < 1$ is always satisfied.

````{prf:theorem} A sufficient condition for exact recovery using OMP
:label: thm:greedy:omp_exact_recovery_sufficient_condition

A sufficient condition for Orthogonal Matching Pursuit
to resolve $\bx$ completely in $K$ steps is that

```{math}
:label: eq:greedy:omp_exact_recovery_sufficient_condition

\underset{\bh}{\max} \| \bDDD_{\opt}^{\dag} \bh \|_1 < 1,
```
where $\bh$ ranges over columns in $\bHHH_{\opt}$.

Moreover, Orthogonal Matching Pursuit is a correct algorithm for
the $(\mathcal{D}, K)$-EXACT-SPARSE problem
whenever the condition holds for every superposition of $K$ atoms from $\bDDD$.
````

````{prf:proof}
.

1. In  {eq}`eq:greedy:omp_exact_recovery_sufficient_condition`,
   $\bDDD_{\opt}^{\dag}$ is the pseudo-inverse of $\bDDD_{\opt}$.
   
   $$
    \bDDD_{\opt}^{\dag} = (\bDDD_{\opt}^H \bDDD_{\opt})^{-1} \bDDD_{\opt}^H.
   $$
1. What we need to show is if {eq}`eq:greedy:omp_exact_recovery_sufficient_condition`
   holds true then $\rho(\br^k)$ will always be less than 1.
1. We note that the projection operator for the column span of $\bDDD_{\opt}$ is given by 
   
   $$
    \bDDD_{\opt} (\bDDD_{\opt}^H \bDDD_{\opt})^{-1} \bDDD_{\opt}^H
    = (\bDDD_{\opt}^{\dag})^H \bDDD_{\opt}^H.
   $$
1. We also note that by assumption since $\bx \in \ColSpace(\bDDD_{\opt})$ and
   the approximation at the $k$-th step, $\bx^k = \bDDD \ba^k  \in \ColSpace(\bDDD_{\opt})$.
1. Hence $\br^k = \bx - \bx^k$ also belongs to $\ColSpace(\bDDD_{\opt})$.
1. Thus
   
   $$
   \br^k = (\bDDD_{\opt}^{\dag})^H \bDDD_{\opt}^H \br^k
   $$
   i.e. applying the projection operator for $\bDDD_{\opt}$ on $\br^k$ doesn't change it.
1. Using this we can rewrite $\rho(\br^k)$ as
   
   $$
    \rho(\br^k) 
    = \frac{\| \bHHH_{\opt}^H \br^k \|_{\infty}}{\| \bDDD_{\opt}^H \br^k \|_{\infty}}
    = \frac{\| \bHHH_{\opt}^H (\bDDD_{\opt}^{\dag})^H \bDDD_{\opt}^H \br^k \|_{\infty}}
    {\| \bDDD_{\opt}^H \br^k \|_{\infty}}.
   $$
1. We see the term $\bDDD_{\opt}^H \br^k$ appearing both in numerator and denominator.
1. Now consider the matrix $\bHHH_{\opt}^H (\bDDD_{\opt}^{\dag})^H$
   and recall the definition of matrix $\infty$-norm from {prf:ref}`def:mat:p_matrix_norm`
   
   $$
    \| \bA\|_{\infty}
    = \underset{\bx \neq 0}{\max } \frac{\| \bA \bx \|_{\infty}}{\| \bx \|_{\infty}} 
    \geq  \frac{\| \bA \bx \|_{\infty}}{\| \bx \|_{\infty}} \Forall \bx \neq \bzero.
   $$
1. Thus
   
   $$
    \| \bHHH_{\opt}^H (\bDDD_{\opt}^{\dag})^H \|_{\infty} \geq \frac{\| \bHHH_{\opt}^H (\bDDD_{\opt}^{\dag})^H \bDDD_{\opt}^H \br^k \|_{\infty}}
    {\| \bDDD_{\opt}^H \br^k \|_{\infty}}
   $$
   which gives us
   
   $$
    \rho(\br^k)  \leq \| \bHHH_{\opt}^H (\bDDD_{\opt}^{\dag})^H \|_{\infty} 
    = \| \left ( \bDDD_{\opt}^{\dag} \bHHH_{\opt} \right )^H \|_{\infty}.
   $$
1. We recall that $\| \bA\|_{\infty}$ is max row sum norm while
   $\| \bA\|_1$ is max column sum norm.
1. Hence
   
   $$
    \| \bA\|_{\infty} = \| \bA^T \|_1= \| \bA^H \|_1
   $$
   which means
   
   $$
    \| \left ( \bDDD_{\opt}^{\dag} \bHHH_{\opt} \right )^H \|_{\infty} 
    = \| \bDDD_{\opt}^{\dag} \bHHH_{\opt} \|_1.
   $$
1. Thus we have:
   
   $$
    \rho(\br^k) \leq \| \bDDD_{\opt}^{\dag} \bHHH_{\opt} \|_1.
   $$
1. Now the columns of $\bDDD_{\opt}^{\dag} \bHHH_{\opt}$  are nothing but
   $\bDDD_{\opt}^{\dag} \bh$ where $\bh$ ranges over columns of $\bHHH_{\opt}$.
1. Thus in terms of max column sum norm
   
   $$
    \rho(\br^k) \leq \underset{\bh}{\max} \| \bDDD_{\opt}^{\dag} \bh \|_1.
   $$
1. Thus assuming that OMP has made $k$ correct decision and $\br^k$ 
   lies in $\ColSpace( \bDDD_{\opt})$, $\rho(\br^k) < 1$ whenever

   $$
    \underset{\bh}{\max} \| \bDDD_{\opt}^{\dag} \bh \|_1 < 1.
   $$
1. The initial residual $\br^0 = \bx$ which always lies in column space of $\bDDD_{\opt}$.
1. By above logic, OMP will always select an optimal column in each step.
1. Since the residual is always orthogonal to the columns already selected,
   hence it will never select the same column twice.
1. Thus in $K$ steps it will retrieve all $K$ atoms which comprise $\bx$. 
````


## Babel Function Estimates

````{div}
There is a small problem with {prf:ref}`thm:greedy:omp_exact_recovery_sufficient_condition`.
Since we don't know the support of $\ba$ a-priori hence its not possible to verify that 

$$
 \underset{\bh}{\max} \| \bDDD_{\opt}^{\dag} \bh \|_1 < 1
$$
holds.
Verifying this for all $K$ column sub-matrices is computationally prohibitive. 

It turns out that Babel function (recall {prf:ref}`def:babel_function`)
can be used to relax the sufficient condition in a manner so that it becomes
computationally tractable.
We show how Babel function guarantees that exact recovery condition for OMP holds.
````

````{prf:theorem} Babel function based guarantee for exact recovery using OMP
:label: thm:greedy:omp_exact_recovery_babel_function

Suppose that $\mu_1$ is the Babel function for a dictionary $\bDDD$.
The exact recovery condition holds whenever

```{math}
:label: eq:greedy:omp_exact_recovery_babel_function

\mu_1 (K - 1) + \mu_1(K) < 1.
```
Thus, Orthogonal Matching Pursuit is a correct algorithm for
the $(\mathcal{D}, K)$-EXACT-SPARSE problem
whenever {eq}`eq:greedy:omp_exact_recovery_babel_function` holds. 

In other words, for sufficiently small $K$ for which
{eq}`eq:greedy:omp_exact_recovery_babel_function` holds,
OMP will recover any arbitrary superposition of $K$ atoms from $\bDDD$.
````

````{prf:proof}
.

1. We can write
   
   $$
     \underset{\bh}{\max} \| \bDDD_{\opt}^{\dag} \bh \|_1 
     =  \underset{\bh}{\max} \| (\bDDD_{\opt}^H \bDDD_{\opt})^{-1} \bDDD_{\opt}^H \bh \|_1 
   $$
1. We recall from {prf:ref}`lem:mat:operator_norm_subordinate`
   that operator-norm is subordinate; i.e.,
   
   $$
    \| \bA \bx \|_1 \leq \| \bA \|_1 \| \bx \|_1.
   $$
1. Thus with $\bA = (\bDDD_{\opt}^H \bDDD_{\opt})^{-1}$ we have
   
   $$
    \| (\bDDD_{\opt}^H \bDDD_{\opt})^{-1} \bDDD_{\opt}^H \bh \|_1
    \leq  \| (\bDDD_{\opt}^H \bDDD_{\opt})^{-1} \|_1 \| \bDDD_{\opt}^H \bh \|_1.
   $$
1. With this we have
   
   $$
     \underset{\bh}{\max} \| \bDDD_{\opt}^{\dag} \bh \|_1  \leq 
     \| (\bDDD_{\opt}^H \bDDD_{\opt})^{-1} \|_1 \underset{\bh}{\max} \| \bDDD_{\opt}^H \bh \|_1.
   $$
1. Now let us look at $\| \bDDD_{\opt}^H \bh \|_1$ closely.
1. There are $K$ columns in  $ \bDDD_{\opt}$.
1. For each column we compute its inner product with $\bh$
   and then absolute sum of the inner product. 
1. Also recall the definition of Babel function:
   
   $$
    \mu_1(K) = \underset{|\Lambda| = K}{\max} \; \underset {\bh}{\max} 
    \sum_{\Lambda} | \langle \bh, \bd_{\lambda} \rangle |.
   $$
1. Clearly 
   
   $$
    \underset{\bh}{\max} \| \bDDD_{\opt}^H \bh \|_1 
    = \underset{\bh}{\max}  \sum_{\Lambda_{\opt}} | \langle \bh, \bd_{\lambda_i} \rangle | 
    \leq \mu_1(K). 
    $$
1. We also need to provide a bound on
   $ \| (\bDDD_{\opt}^H \bDDD_{\opt})^{-1} \|_1$ which
   requires more work.
1. First note that since all columns in $\bDDD$ are unit norm,
   hence the diagonal of $\bDDD_{\opt}^H \bDDD_{\opt}$ contains unit entries.
1. Thus we can write
   
   $$
    \bDDD_{\opt}^H \bDDD_{\opt} = \bI_K + \bA
   $$
   where $\bA$ contains the off diagonal terms in $\bDDD_{\opt}^H \bDDD_{\opt}$.
1. Looking carefully , each column of $\bA$ lists the inner products between
   one atom of $\bDDD_{\opt}$ and the remaining $K-1$ atoms.
1. By definition of Babel function
   
   $$
    \|\bA \|_1 
    = \max_{k=1}^K \sum_{j, j \neq k} | \langle \bd_{\lambda_k} \bd_{\lambda_j} \rangle | 
    \leq \mu_1(K -1).
   $$
1. Whenever $\| \bA \|_1 < 1$ then the Von Neumann series
   $\sum(-\bA)^k$ converges to the inverse
   $(\bI_K + \bA)^{-1}$.
1. Thus we have
   
   $$
    \| (\bDDD_{\opt}^H \bDDD_{\opt})^{-1} \|_1 &= \| ( \bI_K + \bA )^{-1} \|_1 \\
    &= \| \sum_{ k = 0}^{\infty} (-\bA)^k \|_1\\
    & \leq \sum_{ k = 0}^{\infty}  \| \bA\|^k_1 \\
    &= \frac{1}{1 - \| \bA \|_1}\\
    & \leq \frac{1}{1 - \mu_1(K-1)}.
   $$
1. Putting things together we get
   
   $$
     \underset{\bh}{\max} \| \bDDD_{\opt}^{\dag} \bh \|_1  
     \leq \frac{\mu_1(K)}{1  - \mu_1(K-1)}.
   $$
1. Thus whenever $\mu_1 (K - 1) + \mu_1(K) < 1$ holds,   
   we have
   
   $$
   \underset{\bh}{\max} \| \bDDD_{\opt}^{\dag} \bh \|_1   < 1.
   $$
````
## Sparse Approximation Conditions

We now remove the assumption that $\bx$ is $K$-sparse in $\bDDD$.
This is indeed true for all real life signals as they are not truly sparse.

In this subsection we will look at conditions under which
OMP can successfully solve the $(\mathcal{D}, K)$-SPARSE approximation
problem as described in {prf:ref}`def-ssm-d-k-sparse-approx-prob`. 

1. Let $\bx$ be an arbitrary signal.
1. Suppose that $\ba_{\opt}$ is
   an optimal $K$-term approximation representation of $\bx$; i.e.,
   $\ba_{\opt}$  is a solution to {eq}`eq-ssm-d-k-sparse-approx-problem`
   and the optimal $K$-term approximation of $\bx$ is given by
   
   $$
    \bx_{\opt} = \bDDD \ba_{\opt}.
   $$
   We note that $\ba_{\opt}$  may not be unique. 
1. Let $\Lambda_{\opt}$ be the support of $\ba_{\opt}$ which
   identifies the atoms in $\bDDD$ that participate
   in the $K$-term approximation of $\bx$.
1. Let $\bDDD_{\opt}$ be the subdictionary consisting of columns
   of $\bDDD$ indexed by  $\Lambda_{\opt}$.
1. We assume that columns in $\bDDD_{\opt}$ are linearly independent.
   This is easily established since if any atom in this set were
   linearly dependent on other atoms, we could always find a sparser
   solution which would contradict the fact that $\ba_{\opt}$ is optimal.
1. Again let $\bHHH_{\opt}$ be the matrix of $(D - K)$ columns which
   are not indexed by $\Lambda_{\opt}$.
1. We note that if $\Lambda_{\opt}$ is identified then finding
   $\ba_{\opt}$ is a straightforward least squares problem.

We now present a condition under which Orthogonal Matching Pursuit is able
to recover the optimal atoms.

````{prf:theorem}
:label: thm:greedy:omp:general_recovery

Assume that $\mu_1(K) < \frac{1}{2}$, and suppose that at $k$-th
iteration, the support $S^k$ for $\ba^k$ consists only of atoms from
an optimal $k$-term approximation of the signal $\bx$.
At step $(k+1)$, Orthogonal Matching Pursuit will recover another atom
indexed by $\Lambda_{\opt}$ whenever

```{math}
:label: eq:greedy:omp:general_recovery

\| \bx - \bDDD \ba^k \|_2 > \sqrt{1 + \frac{K ( 1 - \mu_1(K))}{(1 - 2 \mu_1(K))^2} } \;
\| \bx - \bDDD \ba_{\opt}\|_2.
```
````
A few remarks are in order.

1. $\| \bx - \bDDD \ba^k \|_2$ is the approximation error norm at 
   $k$-th iteration.
1. $\| \bx - \bDDD \ba_{\opt}\|_2$ is the optimum approximation
   error after $K$ iterations.
1. The theorem says that OMP makes absolute progress whenever the current
   approximation error is larger than the optimum error by a factor.
1. As a result of this theorem, we note that every optimal $K$-term
   approximation of $\bx$ contains the same kernel of atoms.
1. The optimum error is always independent of choice of atoms in
   $K$ term approximation (since it is optimum).
1. Initial error is also independent of choice of atoms (since initial support is empty).
1. OMP always selects the same set of atoms by design.

````{prf:proof}
.

1. Let us assume that after $k$ steps, OMP has recovered an approximation $\bx^k$
   given by
   
   $$
    \bx^k = \bDDD_{S^k} \ba^k
   $$
   where $S^k = \supp(\ba^k)$ chooses $k$ columns from $\bDDD$
   all of which belong to $\bDDD_{\opt}$.
1. Let the residual at $k$-th stage be
   
   $$
    \br^k = \bx - \bx^k =  \bx - \bDDD_{S^k} \ba^k.
   $$
1. Recalling from previous section, a sufficient condition for 
   recovering another optimal atom is
   
   $$
    \rho(\br^k) 
    = \frac{\| \bHHH_{\opt}^H \br^k \|_{\infty}}{\| \bDDD_{\opt}^H \br^k \|_{\infty}} < 1.
   $$
1. One difference from previous section is that $\br^k \notin \ColSpace(\bDDD_{\opt})$.
1. We can write
   
   $$
    \br^k = \bx - \bx^k = (\bx  - \bx_{\opt}) + (\bx_{\opt} - \bx^k).
   $$
1. Note that $(\bx  - \bx_{\opt})$ is nothing but the residual left after
   $K$ iterations. 
1. We also note that since residual in OMP is always orthogonal to already selected
   columns, hence
   
   $$
    \bDDD_{\opt}^H (\bx  - \bx_{\opt}) = \bzero.
   $$
1. We will now use these expressions to simplify $\rho(\br^k)$.

   $$
    \rho(\br^k) 
    &= \frac{\| \bHHH_{\opt}^H \br^k \|_{\infty}}
    {\| \bDDD_{\opt}^H \br^k \|_{\infty}}\\
    &=  \frac{\| \bHHH_{\opt}^H (\bx - \bx_{\opt}) + \bHHH_{\opt}^H (\bx_{\opt} - \bx^k)\|_{\infty}}
    {\| \bDDD_{\opt}^H (\bx - \bx_{\opt})  + \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_{\infty}}\\
    & = \frac{\| \bHHH_{\opt}^H (\bx - \bx_{\opt}) + \bHHH_{\opt}^H (\bx_{\opt} - \bx^k)\|_{\infty}}
    {\| \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_{\infty}}\\
    &\leq \frac{\| \bHHH_{\opt}^H (\bx - \bx_{\opt})\|_{\infty}}
    {\| \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_{\infty}}
    + \frac{\| \bHHH_{\opt}^H (\bx_{\opt} - \bx^k)\|_{\infty}}
    {\| \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_{\infty}}
   $$
1. We now define two new terms

   $$
    \rho_{\text{err}}(\br^k) \triangleq \frac{\| \bHHH_{\opt}^H (\bx - \bx_{\opt})\|_{\infty}}
    {\| \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_{\infty}}
   $$
   and
   
   $$
    \rho_{\opt}(\br^k) \triangleq  \frac{\| \bHHH_{\opt}^H (\bx_{\opt} - \bx^k)\|_{\infty}}
    {\| \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_{\infty}}.
   $$
1. With these we have
   
   ```{math}
    :label: eq:greedy:omp_rho_r_k_sparse_opt_err_breakup

    \rho(\br^k) \leq \rho_{\opt}(\br^k) + \rho_{\text{err}}(\br^k)
    ```
1. Now $\bx_{\opt}$ has an exact $K$-term representation in $\bDDD$ given by
   $\ba_{\opt}$.
1. Hence $\rho_{\opt}(\br^k)$ is nothing
   but $\rho(\br^k)$ for corresponding EXACT-SPARSE problem.
1. From the proof of {prf:ref}`thm:greedy:omp_exact_recovery_babel_function` we recall

   $$
    \rho_{\opt}(\br^k) \leq \frac{\mu_1(K)}{1 - \mu_1(K-1)} 
    \leq \frac{\mu_1(K)}{1 - \mu_1(K)}
   $$
   since
   
   $$
    \mu_1(K-1) \leq \mu_1(K) \implies 1 - \mu_1(K-1) \geq 1 - \mu_1(K).
   $$
1. The remaining problem is $\rho_{\text{err}}(\br^k)$.
1. Let us look at its numerator and denominator one by one.
1. $\| \bHHH_{\opt}^H (\bx - \bx_{\opt})\|_{\infty}$ 
   is the maximum (absolute) inner product between
   any column in $\bHHH_{\opt}$ with $\bx - \bx_{\opt}$.
1. We can write
   
   $$
    \| \bHHH_{\opt}^H (\bx - \bx_{\opt})\|_{\infty} 
    \leq \underset{\bh}{\max} | \bh^H (\bx - \bx_{\opt}) |
    \leq \underset{\bh}{\max} \|\bh \|_2 \| \bx - \bx_{\opt}\|_2
    = \| \bx - \bx_{\opt}\|_2
   $$
   since all columns in $\bDDD$ are unit norm.
   In between we used Cauchy-Schwartz inequality.
1. Now look at denominator $\| \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_{\infty}$
   where $(\bx_{\opt} - \bx^k) \in \CC^N$
   and  $\bDDD_{\opt} \in \CC^{N \times K}$.
1. Thus
   
   $$
    \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \in \CC^{K}.
   $$
1. Now for every $\bv \in \CC^K$ we have
   
   $$
    \| \bv \|_2 \leq \sqrt{K} \| \bv\|_{\infty}.
   $$
1. Hence
   
   $$
    \| \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_{\infty}
    \geq K^{-1/2} \| \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_2.
   $$
1. Since $\bDDD_{\opt}$ has full column rank, hence its singular values 
   are non-zero.
1. Thus
   
   $$
    \| \bDDD_{\opt}^H  (\bx_{\opt} - \bx^k) \|_2 
    \geq \sigma_{\text{min}}(\bDDD_{\opt}) \| \bx_{\opt} - \bx^k \|_2.
   $$
1. From  {prf:ref}`lem:ssm:babel_singular_value_condition` we have
   
   $$
    \sigma_{\text{min}}(\bDDD_{\opt}) \geq \sqrt{1 - \mu_1(K-1)} \geq \sqrt{1 - \mu_1(K)}.
   $$
1. Combining these observations we get
   
   $$
    \rho_{\text{err}}(\br^k) \leq 
    \frac{\sqrt{K} \| \bx - \bx_{\opt}\|_2}
    {\sqrt{1 - \mu_1(K)} \| \bx_{\opt} - \bx^k \|_2}.
   $$
1. Now from {eq}`eq:greedy:omp_rho_r_k_sparse_opt_err_breakup`
   $\rho(\br^k) <1$ whenever $\rho_{\opt}(\br^k) + \rho_{\text{err}}(\br^k) < 1$.
1. Thus a sufficient condition for $\rho(\br^k) <1$ can be written as
   
   $$
    \frac{\mu_1(K)}{1 - \mu_1(K)} + 
    \frac{\sqrt{K} \| \bx - \bx_{\opt}\|_2}
    {\sqrt{1 - \mu_1(K)} \| \bx_{\opt} - \bx^k \|_2} < 1.
   $$
1. We need to simplify this expression a bit.
   Multiplying by $(1 - \mu_1(K))$ on both sides we get
   
   $$
    &\mu_1(K) + \frac{\sqrt{K} \sqrt{1 - \mu_1(K)} \| \bx - \bx_{\opt}\|_2}
    { \| \bx_{\opt} - \bx^k \|_2} < 1 - \mu_1(K)\\
    \implies & \frac{\sqrt{K(1 - \mu_1(K)}) \| \bx - \bx_{\opt}\|_2}
    { \| \bx_{\opt} - \bx^k \|_2} < 1  - 2 \mu_1(K)\\
    \implies & \| \bx_{\opt} - \bx^k \|_2 > \frac{\sqrt{K(1 - \mu_1(K)})} {1  - 2 \mu_1(K)}\| \bx - \bx_{\opt}\|_2.
   $$
   We assumed $\mu_1(K) < \frac{1}{2}$ thus $1 - 2 \mu_1(K) > 0$ which validates the
   steps above.

1. We recall that $(\bx  - \bx_{\opt}) \perp \ColSpace(\bDDD_{\opt})$ and
   $(\bx_{\opt} - \bx^k) \in \ColSpace(\bDDD_{\opt})$ thus $(\bx  - \bx_{\opt})$ 
   and $(\bx_{\opt} - \bx^k)$ are orthogonal to each other.
1. Thus by applying Pythagorean theorem we have
   
   $$
    \| \bx - \bx^k\|_2^2 
    = \| \bx  - \bx_{\opt} \|_2^2 + \| \bx_{\opt} - \bx^k \|_2^2.
   $$
1. Thus we have
   
   $$
    \| \bx - \bx^k\|_2^2 
    > \frac{K(1 - \mu_1(K))} {(1  - 2 \mu_1(K))^2}
    \| \bx - \bx_{\opt}\|_2^2 + \| \bx - \bx_{\opt}\|_2^2.
   $$
1. This gives us a sufficient condition
   
   ```{math}
    :label: eq:greedy:9c009833-7f6d-4609-9543-6110fdcc8461
    \| \bx - \bx^k\|_2 
    > \sqrt{1 + \frac{K(1 - \mu_1(K))} {(1  - 2 \mu_1(K))^2}}
    \| \bx - \bx_{\opt}\|_2.
    ```
1. In other words, whenever {eq}`eq:greedy:9c009833-7f6d-4609-9543-6110fdcc8461` holds true,
   we have $\rho(\br^k) < 1$ which leads to OMP making a correct choice
   and choosing an atom from the optimal set.
1. Putting $\bx^k = \bDDD \ba^k$ and $\bx_{\opt} = \bDDD \ba_{\opt}$ we get back
   {eq}`eq:greedy:omp:general_recovery` which is the desired result.
````

 {prf:ref}`thm:greedy:omp:general_recovery` establishes that
as long as {eq}`eq:greedy:omp:general_recovery` holds for each of the
steps from 1 to $K$, OMP will recover a $K$ term optimum approximation $\bx_{\opt}$.
If $\bx \in \CC^N$ is completely arbitrary, then it may not be possible that 
{eq}`eq:greedy:omp:general_recovery` holds for all the $K$ iterations. In this
situation, a question arises as to what is the worst $K$-term approximation error that
OMP will incur if {eq}`eq:greedy:omp:general_recovery` doesn't hold true all the way.

This is answered in following corollary of {prf:ref}`thm:greedy:omp:general_recovery`.

````{prf:corollary} An estimate for the worst case $K$-term approximation error by OMP
:label: res-omp-sa-worst-k-term-approx-error

Assume that $\mu_1(K)  < \frac{1}{2}$ and let $\bx \in \CC^N$ be a completely arbitrary
signal.
Orthogonal Matching Pursuit produces a $K$-term approximation $\bx^K$ which 
satisfies

```{math}
:label: eq:greedy:omp:worst_k_term_approximation_error

\| \bx  - \bx^K \|_2 \leq \sqrt{1 + C(\bDDD, K)} \| \bx - \bx_{\opt} \|_2
```
where $\bx_{\opt}$ is the optimum $K$-term approximation of $\bx$ in dictionary $\bDDD$
(i.e. $\bx_{\opt} = \bDDD \ba_{\opt}$ where $\ba_{\opt}$
is an optimal solution of {eq}`eq-ssm-d-k-sparse-approx-problem`). 
$C(\bDDD, K)$ is a constant depending upon the dictionary $\bDDD$ and
the desired sparsity level $K$. An estimate of $C(\bDDD, K)$ is given by

$$
C(\bDDD, K) \leq \frac{K ( 1 - \mu_1(K))}{(1 - 2 \mu_1(K))^2}.
$$
````

````{prf:proof}
.

1. Suppose that OMP runs fine for first $p$ steps where $p < K$.
1. Thus {eq}`eq:greedy:omp:general_recovery`  keeps holding for first $p$ steps.
1. We now assume that {eq}`eq:greedy:omp:general_recovery`  breaks
   at step $p+1$ and OMP is no longer guaranteed to make an
   optimal choice of column from $\bDDD_{\opt}$.
1. Thus at step $p+1$ we have
   
   $$
    \| \bx - \bx^p \|_2  
    \leq \sqrt{1 + \frac{K(1 - \mu_1(K))} {(1  - 2 \mu_1(K))^2}} 
    \| \bx - \bx_{\opt} \|_2.
   $$
1. Any further iterations of OMP will only reduce the error further
   (although not in an optimal way). 
1. This gives us
   
   $$
    \| \bx  - \bx^K \|_2 
    \leq \| \bx - \bx^p \|_2  \leq \sqrt{1 + \frac{K(1 - \mu_1(K))} {(1  - 2 \mu_1(K))^2}} \| \bx - \bx_{\opt} \|_2.
   $$
1. Choosing
   
   $$
    C(\bDDD, K) = \frac{K ( 1 - \mu_1(K))}{(1 - 2 \mu_1(K))^2}
   $$
   we can rewrite this as
   
   $$
    \| \bx  - \bx^K \|_2 \leq \sqrt{1 + C(\bDDD, K)} \| \bx - \bx_{\opt} \|_2.
   $$
````

````{div}
This is a very useful result.
It establishes that even if OMP is not able to recover the optimum $K$-term
representation of $\bx$, it always constructs an approximation whose error lies
within a constant factor of optimum approximation error
where the constant factor is given by $\sqrt{1 + C(\bDDD, K)}$.

1. If the optimum approximation error $\| \bx - \bx_{\opt} \|_2$ is small then 
   $\| \bx  - \bx^K \|_2$ will also be not too large.
1. If $\| \bx - \bx_{\opt} \|_2$ is moderate, then the OMP may inflate the
   approximation error to a higher value.
   But in this case, probably sparse approximation is not the right tool for signal
   representation over the dictionary.
````
