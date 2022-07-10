(sec:ssm:rip)= 
# Restricted Isometry Property
This section dwells deep into the implications of restricted isometry property.

````{prf:definition} Restricted isometry property
:label: def:proj:restricted_isometry_property

A matrix $\Phi \in \CC^{M\times N}$ is said to satisfy the
*RIP (restricted isometry property)*
of order $K$ with a constant $\delta \in (0, 1)$
if  the following holds:

```{math}
:label: eq:proj:restricted_isometry_property_bound

(1 - \delta) \|\bx\|^2_2 \leq \| \Phi \bx \|^2_2 \leq (1 + \delta) \|\bx\|^2_2
```
for every $\bx \in \Sigma_K$ where 

$$
\Sigma_K = \{\bx \in \CC^N : \|\bx\|_0 \leq K \}
$$
is the set of all $K$-sparse vectors in $\CC^N$.
````


````{prf:definition} Restricted isometry constant
:label: def:proj:rip:restricted_isometry_constant

If a matrix $\Phi \in \CC^{M\times N}$ satisfies RIP of order $K$
then the smallest value of $\delta$ (denoted as $\delta_K$)
for which the following holds

```{math}
:label: eq:proj:restricted_isometry_constant_bound_def
(1 - \delta) \|\bx\|^2_2 
\leq \| \Phi \bx \|^2_2 
\leq (1 + \delta) \|\bx\|^2_2 \; \Forall \bx \in \Sigma_K
```
is known as the $K$-th *restricted isometry constant* for $\Phi$. 
It is also written in short as $K$-th *RIP constant*.
We write the bounds as in terms of $\delta_K$ as

```{math}
:label: eq:proj:restricted_isometry_constant_bound

(1 - \delta_K) \|\bx\|^2_2 
\leq \| \Phi \bx \|^2_2 
\leq (1 + \delta_K) \|\bx\|^2_2 \; \Forall \bx \in \Sigma_K.
```
````
Some remarks are in order.

* $\Phi$ maps a vector $\bx \in \Sigma_K \subseteq \CC^N$
  into $\CC^M$ as a vector $\Phi \bx$ (usually $M < N$). 
* We will call $\Phi \bx \in \CC^M$ as an *embedding* of $\bx \in \CC^N$ into $\CC^M$.
* RIP quantifies the idea as to how much the squared length of a 
  sparse signal changes during this embedding process.
* We can compare matrices satisfying RIP with orthonormal bases.
* An orthonormal basis or the corresponding unitary matrix
  preserves the length of a vector exactly. 
* A matrix $\Phi$ satisfying RIP of order $K$
  is able to preserve the length of $K$ sparse signals approximately 
  (the approximation range given by $\delta_K$). 
* In this sense we can say that
  $\Phi$ implements a *restricted almost orthonormal system* {cite}`candes2005decoding`. 
* By restricted we mean
  that orthonormality is limited to $K$-sparse signals. 
* By almost we mean that
  the squared length is not preserved exactly. 
  Rather it is preserved approximately.
* An arbitrary matrix $\Phi$ need not satisfy RIP of any order at all.
* If $\Phi$ satisfies RIP of order $K$ then it is easy to see that
  $\Phi$ satisfies RIP of any order $L < K$
  (since $\Sigma_L \subset \Sigma_K$ whenever $L < K$).
* If $\Phi$ satisfies RIP of order $K$,
  then it may or many not satisfy RIP of order $L > K$.
* Restricted isometry constant is a function of sparsity level $K$
  of the signal $\bx \in \CC^N$.

````{prf:example} Restricted isometry constant
:label: ex-ssm-rip-ex-1

As a running example in this section
we will use following matrix


$$
\Phi = \frac{1}{2}
\begin{bmatrix}
 1  &  -1 &  1 & 1 &  1 & -1 &  1 &  1\\
-1  &  -1 &  1 & 1 & -1 &  1 &  1 & -1\\
-1  &  -1 & -1 & 1 & -1 & -1 & -1 &  1\\
-1  &   1 &  1 & 1 &  1 & -1 & -1 & -1
\end{bmatrix}
\in \RR^{4 \times 8}.
$$
Consider 

$$
\bx = 
\begin{pmatrix}
-2 & 0 & 0 & 0 & 0 & -3 & -1 & 0
\end{pmatrix}
$$
which is a $3$-sparse vector in $\RR^8$.
We have

$$
\by = \Phi \bx =
\begin{pmatrix}
0 & -1 & 3 & 3
\end{pmatrix}
$$
Now

$$
\|\bx \|_2^2 = 14, \quad \|\bx \|_2 = 3.7417
$$
and

$$
\|\by \|_2^2 = 19, \quad \| \by \|_2 = 4.3589.
$$
We note that 

$$
\frac{\| \by \|^2_2}{\|\bx \|^2_2} = 1.3571.
$$
With this much information, all we can say that
$\delta_3 \geq .3571$ for this matrix $\Phi$
if $\Phi$ satisfies RIP of order $3$
since we haven't examined all possible $3$-sparse
vectors.

Still what is comforting to note is 
that for this particular example,
the distance hasn't increased by a large factor.
````

For a given $K$-sparse vector $\bx$,
let $J$ denote the support of $\bx$; i.e.,

$$
J  = \{ 1 \leq i \leq N \ST x_i \neq 0 \}.
$$
In the running example

$$
J = \{ 1, 6, 7 \}.
$$
We define $\bx_J \in \CC^K$ to be the vector
formed by keeping the elements in $\bx$ indexed
by $J$ and dropping of other elements
(the zero elements).
Note that the order of elements is preserved.
In the running example,

$$
\bx_J = \begin{pmatrix}
-2 & -3 & -1
\end{pmatrix}.
$$
Let $\Phi_J$ be the corresponding sub-matrix
by choosing columns from $\Phi$ indexed by
the set $J$.
Note that the order of columns is preserved.
In the running example

$$
\Phi_J = \frac{1}{2}
\begin{bmatrix}
 1 & -1 &  1\\
-1 &  1 &  1\\
-1 & -1 & -1\\
-1 & -1 & -1
\end{bmatrix}
\in \RR^{4 \times 3}.
$$
It is easy to see that

$$
\by = \Phi \bx = \Phi_J \bx_J.
$$
There are $\binom{N}{K}$ ways of choosing
a $K$-sparse support for $\bx$.
Thus we have to consider $\binom{N}{K}$
corresponding submatrices  $\Phi_J$.

For each such submatrix $\Phi_J$, the RIP bounds can be rewritten as

```{math}
:label: eq:proj:rip:K_sub_matrix_rip_bound
(1 - \delta_K) \|\bx\|^2_2 \leq \| \Phi_J \bx \|^2_2 \leq (1 + \delta_K) \|\bx\|^2_2
```
for every $\bx \in \CC^K$.
Note that

$$
 \| \Phi_J \bx \|^2_2 = 
 (\Phi_J \bx)^H (\Phi_J \bx)
 = \bx^H \Phi_J^H \Phi_J \bx.
$$

````{prf:theorem}
:label: lem:proj:rip:max_rip_order

An $M \times N$ matrix $\Phi$ cannot satisfy RIP of order $K > M$. 
````
````{prf:proof}
This comes from the fact that for a wide matrix $\rank \Phi \leq M$.
1. Since every $\phi_j \in \CC^M$ hence any set of $M+1$ columns in $\Phi$ 
   is linearly dependent.
1. Thus there exists a nonzero $M+1$ sparse signal $\bx \in \CC^N$ 
   such that $\Phi \bx = \bzero$ (it belongs to the null space of the chosen $M+1$ columns).
1. RIP {eq}`eq:proj:restricted_isometry_property_bound`
   requires that a nonzero vector be embedded as a nonzero vector.
1. Thus $\Phi$  cannot satisfy RIP of order $M+1$.
1. The argument can be easily extended for any $K > M$.
````

````{prf:theorem}
:label: lem:proj:rip:lower_order_rip_satisfaction

If $\Phi$ satisfies RIP of order $l$ then it satisfies RIP of order $k$ where $k < l$. 
````
````{prf:proof}
Every $k$ sparse signal is also $l$ sparse signal.
Thus if $\Phi$ satisfies RIP of
order $l$ then it automatically satisfies RIP of order $k < l$.
````

````{prf:theorem}
:label: lem:proj:rip:non_decreasing_constants

Let $\Phi$ satisfy RIP of order $k$ and $l$ where $k < l$.
Then $\delta_k \leq \delta_l$.
In other words, restricted isometry constants are non-decreasing.
````
````{prf:proof}
Since every $k$ sparse signal is also $l$ sparse signal,
hence for every $\bx \in \Sigma_k$ following must be satisfied

$$
(1 - \delta_k) \|\bx\|^2_2 
\leq \| \Phi \bx \|^2_2 
\leq (1 + \delta_k) \|\bx\|^2_2
$$
and

$$
(1 - \delta_l) \|\bx\|^2_2 \leq \| \Phi \bx \|^2_2 \leq (1 + \delta_l) \|\bx\|^2_2.
$$
Since $\delta_k$ is smallest such value for which these inequalities are satisfied
hence $\delta_l$ cannot be smaller than $\delta_k$.
````
## The First Restricted Isometry Constant

````{div}
We consider the simplest case where $K=1$.
We can write $\Phi$ in terms of its column vectors

$$
\Phi = \begin{bmatrix}
\phi_1 & \dots & \phi_N
\end{bmatrix}.
$$

1. Now a $1$-sparse vector $\bx$ consists of only one nonzero entry.
1. Say that $\bx$ is nonzero at index $j$. 
1. Then $\Phi \bx$ is nothing but $x_j \phi_j$.
1. With this the restricted isometry inequality can be written as
   
   $$
   (1 - \delta_1) |x_j|^2 \leq \| x_j \phi_j \|_2^2 \leq (1 + \delta_1) |x_j|^2.
   $$
1. Dividing by $|x_j|^2$ we get
   
   $$
   (1 - \delta_1) \leq \| \phi_j \|_2^2 \leq (1 + \delta_1).
   $$
````

Let us formalize this in the following theorem.

````{prf:theorem} Restricted isometry constants of order 1
:label: lem:proj:rip:phi_columns_length_bound

If a matrix $\Phi$ satisfies RIP of order $K \geq 1$ then the 
squared lengths of columns of $\Phi$  satisfy the following bounds

```{math}
:label: eq:proj:rip:phi_columns_length_bound

1 - \delta_1 \leq \| \phi_j \|_2^2 \leq 1 + \delta_1  \; \Forall 1 \leq j \leq N.
```
````
When $\delta_1 = 0$ then all columns of $\Phi$ are unit norm.
Now if columns of $\Phi$ span $\CC^M$ then
$\Phi$ can also be considered as a dictionary for $\CC^M$ 
(see {prf:ref}`def-ssm-dictionary`).

````{prf:remark}
:label: res-ssm-dictionary-rip-1

A dictionary ({prf:ref}`def-ssm-dictionary`) satisfies RIP  of order 1 with
$\delta_1 = 0$.
````
## Sums and Differences of Sparse Vectors

````{prf:theorem}
:label: lem:proj:rip_sum_difference

Let $\bx , \by \in \CC^N$ with $\bx \in  \Sigma_k$ and $\by \in \Sigma_l$;
i.e., $ \| \bx \|_0 \leq k$ and $\| \by \|_0 \leq l$.
Then 

$$
(1 - \delta_{k + l}) \| \bx  \pm \by \|_2^2 
\leq \| \Phi \bx  \pm  \Phi \by \|_2^2 
\leq (1 + \delta_{k + l}) \| \bx  \pm \by \|_2^2
$$
as long as $\Phi$ satisfies RIP of order $k + l$.
````
````{prf:proof}
We know that

$$
\| \bx \pm \by \|_0 \leq \| \bx \|_0 + \| \by \|_0 \leq k + l.
$$
Thus $\bx \pm \by \in \Sigma_{k + l}$. The result follows.
````


## Distance Between Sparse Vectors
````{div}
Let $\bx, \by \in \Sigma_K$. Then clearly $\bx - \by \in \Sigma_{2K}$.

The $\ell_2$ distance between vectors is given by

$$
d(\bx, \by) = \| \bx - \by \|_2 = \sqrt{(\bx  - \by)^H (\bx - \by)}.
$$
Now if $\Phi$ satisfies RIP of order $2K$
then we can see that it approximately preserves $\ell_2$ distances
between $K$-sparse vectors.
````

````{prf:theorem} Approximation preservation of distances
:label: lem:proj:rip_distance_preservation

Let $\bx, \by \in \Sigma_K \subset \CC^N$.
Let $\Phi \bx , \Phi \by \in \CC^M$ be corresponding embeddings. 
If $\Phi$ satisfies RIP of order $2K$, then

$$
(1  - \delta_{2K}) d^2(\bx, \by) 
\leq d^2 (\Phi \bx, \Phi \by) 
\leq (1  + \delta_{2K}) d^2(\bx, \by).
$$
````
````{prf:proof}
Since $\Phi$ satisfies RIP of order $2K$
hence for every vector $\bv \in \Sigma_{2K}$ we have

$$
(1 - \delta_{2K}) \|\bv\|^2_2
\leq \| \Phi \bv \|^2_2 
\leq (1 + \delta_{2K}) \|\bv\|^2_2.
$$
But then $\bx - \by \in \Sigma_{2K}$ for every $\bx, \by \in \Sigma_K$ and

$$
d^2 (\bx, \by) = \| \bx - \by \|_2^2
$$ 
and

$$
d^2 (\Phi \bx, \Phi \by) = \| \Phi \bx - \Phi \by \|_2^2 = \| \Phi (\bx - \by) \|_2^2.
$$
Thus we have the result.
````

## RIP with Unit Length Sparse Vectors
Sometimes it is convenient to state RIP in terms of unit length sparse vectors.

````{prf:theorem} RIP for unit length sparse vectors
:label: lem:proj:rip_unit_length_sparse_vectors

Let $\bx$ be some arbitrary unit length
(i.e., $\| \bx \|_2 = 1$) vector belonging to $\Sigma_K$.
A matrix $\Phi$ is said to satisfy RIP of order $K$
if and only if the following holds

```{math}
:label: eq:proj:rip_bound_unit_length
(1 - \delta_K) \leq \| \Phi \bx \|^2_2 \leq (1 + \delta_K)
```
for every $\bx \in \Sigma_K$ with $\| \bx \|_2 = 1$.
````

````{prf:proof}
If $\Phi$ satisfies RIP of order $K$ then by putting $\|\bx \|_2 =1$ in 
{eq}`eq:proj:restricted_isometry_property_bound` we get
{eq}`eq:proj:rip_bound_unit_length`.

Now the converse.
1. We assume {eq}`eq:proj:rip_bound_unit_length` holds for all
   unit norm vectors $\bx \in \Sigma_K$.
1. We need to show that {eq}`eq:proj:restricted_isometry_property_bound`
   holds for all $\bx \in \Sigma_K$. 
1. For $\bx = \bzero$ the bounds in
   {eq}`eq:proj:restricted_isometry_property_bound` are trivially satisfied. 
1. Let $\bx \in \Sigma_K$ be some nonzero vector.
1. Let $\widehat{\bx} = \frac{\bx} {\| \bx \|_2}$. 
1. Clearly $\widehat{\bx}$ is unit length. Hence

   $$
    & (1 - \delta_K) 
    \leq \| \Phi \widehat{\bx} \|^2_2 
    \leq (1 + \delta_K)\\
    \implies
    & (1 - \delta_K) \leq 
    \left \| \Phi \frac{\bx} {\| \bx \|_2} \right \|^2_2 
    \leq (1 + \delta_K)\\
    \implies &
    (1 - \delta_K) \| \bx \|_2^2 
    \leq \| \Phi \bx\|^2_2 
    \leq (1 + \delta_K) \| \bx \|_2^2. 
    $$
1. Thus $\Phi$ satisfies RIP of order $K$.
````


## Singular and Eigen Values of $K$-Submatrices

Consider any index set $J \subset \{ 1, \dots, N\}$ with $|J|=K$.
Let $\Phi_J$ be a sub matrix of $\Phi$ consisting of columns
indexed by $J$. Assume $K \leq M$.
We define

$$
\bG \triangleq \Phi_J^H \Phi_J \in \CC^{K \times K}
$$ 
as the Gram matrix for columns of $\Phi_J$ (see {ref}`sec:mat:gram_matrix`).

We consider the eigen values of $\bG$ given by

$$
\bG \bx = \lambda \bx 
$$
for some $\bx \in \CC^K$ and $\bx \neq \bzero$.
We will show that eigen values of $\bG$ are bounded by RIP constant.

In the running example

$$
\bG = \begin{bmatrix}
1 & 0 & 0.5\\
0 & 1 & 0.5\\
0.5 & 0.5 & 1
\end{bmatrix}.
$$

Eigen values of G are $(0.2929,1, 1.7071)$.

````{prf:theorem}
:label: lem:proj:rip:k_gram_eigen_value_range

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any sub matrix of $\Phi$ with $K$ columns.
Then the eigen values of $\bG = \Phi_J^H \Phi_J$
lie in the range $[1-\delta_K, 1 + \delta_K]$.
````
````{prf:proof}
We note that $\bG \in \CC^{K \times K}$.

1. Let $\lambda$ be some eigen value of $\bG$.
1. Let $\bx \in \CC^K$ be a corresponding (nonzero) eigenvector.
1. Then
   
   $$
    &\bG \bx = \lambda \bx \\
    \implies & \bx^H \bG \bx = \bx^H \lambda \bx\\
    \implies & \bx^H  \Phi_J^H \Phi_J \bx =  \lambda \| \bx \|_2^2\\
    \implies &\| \Phi_J \bx \|^2_2 = \lambda \| \bx \|_2^2.
   $$
1. From {eq}`eq:proj:rip:K_sub_matrix_rip_bound`
   we recall that $\delta_K$ RIP bounds apply
   for each vector in $\bx \in \CC^K$ for a $K$-column submatrix $\Phi_J$
   given by
   
   $$
    (1 - \delta_K) \| \bx\|^2_2 
    \leq \| \Phi_J \bx \|^2_2 
    \leq (1 + \delta_K) \| \bx\|^2_2.
   $$
1. Thus
   
   $$
    & (1 - \delta_K) \| \bx\|^2_2 
    \leq \lambda \| \bx \|_2^2 
    \leq (1 + \delta_K) \| \bx\|^2_2\\
    \implies &(1 - \delta_K)  
    \leq \lambda \leq (1 + \delta_K)
   $$
   since $\bx \neq \bzero$.
````


````{prf:corollary}
:label: lem:proj:rip:k_gram_invertible

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any submatrix of
$\Phi$ with $K$ columns.
Then the Gram matrix $\bG = \Phi_J^H \Phi_J$ is full rank and invertible.
Moreover $\bG$ is positive definite.
````
````{prf:proof}
From {prf:ref}`lem:proj:rip:k_gram_eigen_value_range`,
the eigen values are in range $[1-\delta_K, 1 + \delta_K]$.

1. Since $\Phi$ satisfies RIP of order $K$, hence $\delta_K < 1$.
1. Hence all eigenvalues of $\bG$ are positive.
1. Hence $\bG$ is positive definite.
1. Hence their product is positive.
1. Thus $\det(\bG)$ is nonzero. 
1. Hence $\bG$ is invertible.
````


````{prf:theorem}
:label: lem:proj:rip:k_submatrix_singular_value_range

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any submatrix of $\Phi$ with $K$ columns.
Then all singular values of $\Phi_J$ are nonzero and they are
in the range given by

$$
\sqrt{1-\delta_K} \leq \sigma \leq \sqrt{1 + \delta_K}
$$
where $\sigma$ is a singular value of $\Phi_J$. 
````
````{prf:proof}
This is straight forward application of 
{prf:ref}`lem:mat:singular:aH_a_eigen_values` and  {prf:ref}`lem:proj:rip:k_gram_eigen_value_range`.
Eigen values of $\Phi_J^H \Phi_J$ are nothing but
squares of the singular values of $\Phi_J$.
````

````{prf:corollary}
:label: cor:proj:rip:k_submatrix_singular_value_range

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any submatrix of
$\Phi$ with $k$ columns where $k \leq K$. 
Then the singular values of $\Phi_J$ are nonzero and they are
in the range given by

$$
\sqrt{1-\delta_K} \leq \sigma \leq \sqrt{1 + \delta_K}
$$
where $\sigma$ is a singular value of $\Phi_J$. 
````
````{prf:proof}
Let $\sigma$ be a  singular value of $\Phi_J$.
1. Since $\Phi$ satisfies RIP of order $K$, it also satisfies RIP of order $k \leq K$. 
1. From {prf:ref}`lem:proj:rip:k_submatrix_singular_value_range` we have

    $$
    \sqrt{1-\delta_k} \leq \sigma \leq \sqrt{1 + \delta_k}.
    $$
1. From {prf:ref}`lem:proj:rip:non_decreasing_constants`
   we have $\delta_k \leq \delta_K$.
1. Thus 

    $$
    1 - \delta_K \leq 1 - \delta_k , \quad 1 + \delta_k \leq 1 + \delta_K.
    $$
1. Thus
    
    $$
    \sqrt{1-\delta_K} \leq \sigma \leq \sqrt{1 + \delta_K}.
    $$
````

````{prf:theorem}
:label: lem:proj:rip:submatrix_eigenvalue_sum_k

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any submatrix of $\Phi$ with $k$ columns where $k \leq K$.
Then the eigen values of $\Phi_J^H \Phi_J + r \bI$ lie in the range

$$
[1-\delta_K + r, 1 + \delta_K + r].
$$
Moreover consider $\Delta = \Phi_J^H \Phi_J - \bI$.
Then 

$$
\| \Delta \|_2 \leq \delta_K.
$$
````
````{prf:proof}
.

1. From {prf:ref}`lem:proj:rip:k_gram_eigen_value_range`
   eigen values of $\Phi_J^H \Phi_J$ lie in the range
   $[1-\delta_K, 1 + \delta_K]$.
1. From {prf:ref}`lem:mat:eig:lambda_k_sum` $\lambda$ is an eigen value of
   $\Phi_J^H \Phi_J$ if and only if 
   $\lambda + r$ is an eigen value of  $\Phi_J^H \Phi_J + r \bI$.
1. Hence the result.

Now for $\Delta = \Phi_J^H \Phi_J - \bI$
1. The eigen values lie in the range $[-\delta_K, \delta_K]$.
1. Thus for every eigen value of $\Delta$ we have 
   $|\lambda| \leq \delta_K$.
1. Since $\Delta$ is Hermitian,
   its spectral norm is nothing but its largest eigen value.
1. Hence 
   
   $$
    \| \Delta \|_2 \leq \delta_K.
   $$
````


From previous few results we see that bound over eigen values of $\Phi_J^H \Phi_J$ given by
$(1 - \delta_K) \leq \lambda \leq (1 + \delta_K)$ is a necessary condition
for $\Phi$ to satisfy RIP of order $K$.
We now show that this is also a sufficient condition.

````{prf:theorem}
:label: lem:proj:rip_gram_matrix_eigen_value_sufficient_condition

Let $\Phi$ be an $M \times N$ matrix with $M \leq N$.
Let $J \subset \{ 1, \dots, N \}$ be any index set 
with $|J| = K \leq M$.
Let $\Phi_J$ be the $K$-column sub-matrix of $\Phi$ indexed by $J$.
Let $\bG = \Phi_J^H \Phi_J$ be the Gram matrix of columns of $\Phi_J$.
Let the eigen values of $\bG$ be $\lambda$.
If there exists a number $\delta \in (0,1)$ such that 

$$
1  - \delta \leq \lambda \leq 1 + \delta
$$
for every eigen value of $\bG$ for every $K$ column submatrix of $\Phi$, then 
$\Phi$ satisfies RIP of order $K$.

Alternatively, let $\Delta = \bG - \bI$.
If 

$$
\| \Delta \|_2 \leq \delta < 1
$$
for every $K$ column submatrix of $\Phi$
then $\Phi$ satisfies RIP of order $K$.

Alternatively, if singular values of $\Phi_J$ satisfy 

$$
\sqrt{1  - \delta} \leq \sigma \leq \sqrt{1 + \delta}
$$
for every $\Phi_J$ then $\Phi$ satisfies RIP of order $K$.
````
````{prf:proof}
Equivalence of sufficient conditions

1. We note that eigen values of $\bG$ are related to eigen values of
   $\Delta$ by the relation (see {prf:ref}`lem:mat:eig:lambda_k_sum`)

    $$
    \lambda_G  - 1 = \lambda_{\Delta} \iff \Lambda_G = 1 + \lambda_{\Delta}.
    $$
1. Hence

    $$
    \| \Delta \|_2 \leq \delta 
    \iff  - \delta \leq  \lambda_{\Delta} \leq \delta 
    \iff 1 - \delta \leq \lambda_G \leq 1 + \delta. 
    $$
1. Thus the first two sufficient conditions are equivalent. 
1. Lastly the eigen values of $\bG$ are squares of singular values of $\Phi_J$.
1. Thus all sufficient conditions are equivalent.

Proof of sufficient condition

1. Now let $\bx \in \Sigma_K$ be an arbitrary vector.
1. Let $J = \supp(\bx)$.
1. Clearly $|J| \leq K$. If $|J| < K$ then augment $J$ 
   by adding some indices arbitrarily till we get $|J| = K$.
1. Clearly $\bx_J$ is an arbitrary vector in $\CC^K$ and
   $\Phi \bx = \Phi_J \bx_J$.
1. Now let $\lambda_1$ be the largest and $\lambda_k$ be
   the smallest eigen value of $\bG = \Phi_J^H \Phi_J$.
1. $\bG$ is Hermitian and all its eigen values are positive,
   hence it is positive definite.  
1. From {prf:ref}`lem:mat:eig:hermitian_psd_x_h_a_x_range` we get
   
   $$
    \lambda_k  \| \bx\|_2^2 \leq \bx^H \bG \bx 
    \leq  \lambda_1  \| \bx \|_2^2 \Forall  \bx \in \CC^K.
   $$
1. Applying the limits on the eigen values and using 
   $\bx^H \bG \bx = \|\Phi_J \bx\|_2^2$, we get
   
   $$
   (1  - \delta)  \| \bx\|_2^2 
   \leq \|\Phi_J \bx\|_2^2 
   \leq (1  + \delta)  \|\bx\|_2^2 
   \Forall  \bx \in \CC^K.
   $$
1. Since this holds for every index set $J$
   with $|J|=K$ hence an equivalent statement is
   
   $$
   (1  - \delta)  \| \bx\|_2^2 
   \leq \|\Phi \bx\|_2^2 
   \leq (1  + \delta)  \| \bx\|_2^2 \Forall \bx \in \Sigma_K \subset \CC^N.
   $$
1. Thus $\Phi$ indeed satisfies RIP of order $K$
   with some $\delta_K$ not larger than $\delta$.
````

````{prf:theorem}
:label: lem:proj:rip:k_submatrix_pseudo_inverse_singular_value_range

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any submatrix of
$\Phi$ with $k$ columns where $k \leq K$. 
Let $\Phi_J^{\dag}$ be its Moore-Penrose pseudo-inverse. 
Then the singular values of $\Phi_J^{\dag}$ are nonzero and they are
in the range given by

$$
\frac{1}{\sqrt{1+\delta_K}} \leq \sigma \leq \frac{1}{\sqrt{1 - \delta_K}}
$$
where $\sigma$ is a singular value of $\Phi_J^{\dag}$.
````
````{prf:proof}
Construction of pseudoinverse of a matrix through
its singular value decomposition is
discussed in {prf:ref}`lem:mat:singular:matrix_pseudo_inverse`.

1. {prf:ref}`lem:mat:singular_pseudo_inverse_singular_values`
   shows that if $\sigma$ is a
   nonzero singular value of $\Phi_J^{\dag}$
   then $\frac{1}{\sigma}$ is a nonzero singular value of $\Phi_J$.
1. From {prf:ref}`cor:proj:rip:k_submatrix_singular_value_range`
   we have that if $\frac{1}{\sigma}$ is a singular value of $\Phi_J$ then,
   
   $$
    \sqrt{1-\delta_K} \leq \frac{1}{\sigma} \leq \sqrt{1 + \delta_K}
   $$
1. Inverting the terms in the inequalities we get our result.
````

````{prf:theorem}
:label: res-rip-gram-eval-lb

Eigen values of $\bG = \Phi_J^H \Phi_J$ 
provide a lower bound on $\delta_K$ given by

$$
\delta_K \geq \max (1 - \lambda_{\min},
\lambda_{\max} - 1)
$$
where $J$ is some index set choosing $K$ columns of $\Phi$ and 
$\delta_K$ is the $K$-th restricted isometry constant for $\Phi$.

In other words, singular values of $\Phi_J$ 
provide a lower bound on $\delta_K$ given by

$$
\delta_K \geq \max (1 - \sigma_{\min}^2,
\sigma_{\max}^2 - 1)
$$
````

````{prf:proof}
Obvious.
````

In the running example, the bounds tell
us that

$$
\delta_3 \geq 0.7071.
$$

Certainly we have to consider
all possible $\binom{N}{K}$ sub-matrices
$\Phi_J$ to come up with an overall lower
bound on $\delta_K$.

This result doesn't provide us any upper
bound on $\delta_K$.

````{prf:theorem}
:label: lem:proj:rip:phi_phi_H_embedding_l2_norm_upper_bound

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any submatrix of
$\Phi$ with $k$ columns where $k \leq K$.
Then 

$$
\| \Phi_J \bx \|_2 
\leq  \sqrt{1 + \delta_K} \| \bx \|_2  \Forall \bx \in \CC^k.
$$
Moreover

$$
\| \Phi_J^H \by \|_2 
\leq  \sqrt{1 + \delta_K} \| \by \|_2 
\Forall \by \in \CC^M.
$$
````

````{prf:proof}
We note that $\Phi_J$ is an $M \times k$ matrix.

1. Let $\sigma_1$ be the largest singular value of $\Phi_J$.
1. Then by
   {prf:ref}`lem:mat:singular:largest_singular_value_l2_norm_bound_A_A^H`
   we have

   $$
    \| \Phi_J \bx \|_2 \leq \sigma_1 \| \bx \|_2 \Forall \bx \in \CC^k.
   $$
   and
   
   $$
    \| \Phi_J^H \by \|_2 \leq \sigma_1 \| \by \|_2 \Forall \by \in \CC^M.
   $$
1. From {prf:ref}`lem:proj:rip:k_submatrix_singular_value_range` and
   {prf:ref}`cor:proj:rip:k_submatrix_singular_value_range`
   we get
   
   $$
    \sigma_1  \leq \sqrt{1 + \delta_K}.
   $$
1. This completes the proof.
````
First inequality is a restatement of restricted isometry property
in {eq}`eq:proj:rip:K_sub_matrix_rip_bound`.
Second inequality is interesting.
In compressive sensing terms, $\by$ is a measurement vector
and we are using $\Phi_J^H$ to project $\by$ back into $\CC^N$
over a $k$ sparse support identified by $J$.
The inequality provides an upper bound on how much
the length can increase during this operation.

````{prf:theorem}
:label: lem:proj:rip:phi_pseudo_inverse_embedding_l2_norm_upper_bound

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any submatrix of
$\Phi$ with $k$ columns where $k \leq K$. 
Let $\Phi_J^{\dag}$ be its Moore-Penrose pseudo-inverse. 
Then 

$$
\| \Phi_J^{\dag} \by \|_2 
\leq  \frac{1}{\sqrt{1 - \delta_K}} \| \by \|_2  \Forall \by \in \CC^M.
$$
````
````{prf:proof}
We note that $\Phi_J^{\dag}$ is an $k \times M$ matrix.

1. Let $\sigma_1$ be the largest singular value of $\Phi_J^{\dag}$.
1. Then by
   {prf:ref}`lem:mat:singular:largest_singular_value_l2_norm_bound_A_A^H`
   we have
   
   $$
    \| \Phi_J^{\dag} \by \|_2 
    \leq \sigma_1 \| \by \|_2 \Forall y \in \CC^M.
   $$
1. From {prf:ref}`lem:proj:rip:k_submatrix_pseudo_inverse_singular_value_range`
   we see that singular values
   of $\Phi_J^{\dag}$ satisfy the inequalities  
   
   $$
   \frac{1}{\sqrt{1+\delta_K}} \leq \sigma \leq \frac{1}{\sqrt{1 - \delta_K}}.
   $$
1. Thus

   $$
    \sigma_1 \leq \frac{1}{\sqrt{1 - \delta_K}}.
   $$
1. Plugging it in we get
   
   $$
   \| \Phi_J^{\dag} \by \|_2 
   \leq \frac{1}{\sqrt{1 - \delta_K}} \| \by \|_2 
   \Forall \by \in \CC^M.
   $$
````
In the previous theorem we saw that back-projection using $\Phi_J^H$
had an upper bound on how 
much the length of measurement vector could increase.
In this theorem we see another upper bound
on how much the length of measurement vector can
increase when back projected using the pseudo inverse
of $\Phi_J$.

````{prf:theorem}
:label: lem:proj:rip:phi_J_gram_embedding_l2_norm_bounds_range

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any submatrix of
$\Phi$ with $k$ columns where $k \leq K$.
Then

$$
(1 - \delta_K) \| \bx \|_2 
\leq \| \Phi_J^H \Phi_J \bx \|_2  
\leq (1 + \delta_K) \| \bx \|_2  \Forall \bx \in \CC^k.
$$
Moreover

$$
\frac{1}{1 + \delta_K} \| \bx \|_2 
\leq \| \left (\Phi_J^H \Phi_J \right)^{-1} \bx \|_2  
\leq \frac{1}{1 - \delta_K} \| \bx \|_2  \Forall \bx \in \CC^k.
$$
````
````{prf:proof}
We note that $\Phi_J$ is a full column rank tall matrix. 
1. We recall that all singular values of $\Phi_J$ are positive
   and are bounded by ({prf:ref}`cor:proj:rip:k_submatrix_singular_value_range`):
   
   $$
   \sqrt{1-\delta_K} \leq \sigma_k \leq \dots \leq \sigma_1 \leq \sqrt{1 + \delta_K}
   $$
   where $\sigma_1, \dots, \sigma_k$
   are the singular values of $\Phi_J$ (in descending order).
1. We note that $\Phi_J^H \Phi_J$ is an $k \times k$ matrix
   which is invertible ({prf:ref}`lem:proj:rip:k_gram_invertible`). 
1. From 
   {prf:ref}`lem:mat:singular:full_column_rank_gram_embedding_l2_norm_bound`
   we get

   $$
    \sigma_k^2 \| \bx \|_2 
    \leq \| \Phi_J^H \Phi_J \bx \|_2 
    \leq \sigma_1^2 \| \bx \|_2  
    \Forall \bx \in \CC^k.
   $$
1. Applying the bounds on $\sigma_i$ we get the result
   
   $$
    (1 - \delta_K) \| \bx \|_2 
    \leq \| \Phi_J^H \Phi_J \bx \|_2  
    \leq (1 + \delta_K) \| \bx \|_2  \Forall \bx \in \CC^k.
   $$
1. From
   {prf:ref}`lem:mat:singular:full_column_rank_inverse_gram_embedding_l2_norm_bound` 
   we have the bounds for
   $\left ( \Phi_J^H \Phi_J \right) ^{-1}$ given by
   
   $$
    \frac{1}{\sigma_1^2} \| \bx \|_2 
    \leq \| \left(\Phi_J^H \Phi_J \right)^{-1} \bx \|_2 
    \leq \frac{1}{\sigma_k^2} \| \bx \|_2  \Forall \bx \in \CC^k.
   $$
1. Applying the bounds on $\sigma_i$ we get the result
   
   $$
    \frac{1}{1 + \delta_K} \| \bx \|_2 
    \leq \| \left (\Phi_J^H \Phi_J \right)^{-1} \bx \|_2
    \leq \frac{1}{1 - \delta_K} \| \bx \|_2  
    \Forall \bx \in \CC^k.
   $$
````
In the sequel we will discuss that $\Phi^H \Phi \bx$ 
can work as a very good proxy for the signal $\bx$. The
results in this theorem are very comforting in this regard.

````{prf:theorem}
:label: lem:proj:rip:phi_J_gram_minus_I_embedding_l2_norm_upper_bound

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $\Phi_J$ be any sub matrix of
$\Phi$ with $k$ columns where $k \leq K$.
Then

$$
\| (\Phi_J^H \Phi_J - \bI ) \bx \|_2 
\leq \delta_K \| \bx \|_2  
\Forall \bx \in \CC^k.
$$
````
````{prf:proof}
.

1. From {prf:ref}`lem:proj:rip:submatrix_eigenvalue_sum_k` we get
   
   $$
    \| \Phi_J^H \Phi_J - \bI \|_2 \leq \delta_k \leq \delta_K.
   $$
1. Thus since spectral norm is subordinate 
   
   $$
    \| (\Phi_J^H \Phi_J - \bI ) \bx \|_2  
    \leq \|\Phi_J^H \Phi_J - \bI \|_2 \| \bx \|_2
    \leq \delta_K \| \bx \|_2  \Forall \bx \in \CC^k.
   $$
````

## Approximate Orthogonality

We are going to show that disjoint sets of columns from 
$\Phi$ span nearly orthogonal 
subspaces.
This property is proved in {cite}`needell2009cosamp`.

````{prf:theorem}
:label: lem:proj:rip:approximate_orthogonality 

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$.
Let $S$ and $T$ denote index sets over the
columns of $\Phi$ with $|S| + |T| \leq K$
and $S \cap T = \EmptySet$.
In other words, $S$ and $T$ are disjoint index sets.
Let $\Phi_S$ and $\Phi_T$ denote corresponding sub-matrices 
consisting of columns indexed by $S$ and $T$ respectively.
Then

$$
\| \Phi_S^H \Phi_T \|_2  \leq \delta_K
$$
where $\| \cdot \|_2$ denotes the $2$-norm or spectral norm of a matrix.
````
````{prf:proof}
Define $R = S \cup T$.
1. Consider the sub-matrix $\Phi_R$.
1. Construct another matrix
   $\Psi  = \Phi_R^H \Phi_R - \bI$.
1. The off-diagonal entries of $\Psi$ are nothing
   but inner products of columns of $\Phi_R$. 
1. We note that every entry in the matrix $\Phi_S^H \Phi_T$ 
   is an entry in $\Psi$.
1. Moreover, $\Phi_S^H \Phi_T$ is a submatrix of $\Psi$.
1. The spectral norm of a sub-matrix is never greater than 
   the spectral norm of the matrix containing it.
1. Thus
   
   $$
    \| \Phi_S^H \Phi_T \|_2 \leq \| \Phi_R^H \Phi_R - \bI \|_2.
   $$
1. From {prf:ref}`lem:proj:rip:submatrix_eigenvalue_sum_k`
   the eigen values of $\Phi_R^H \Phi_R - \bI$ satisfy
   
   $$
    1-\delta_K - 1 \leq \lambda \leq  1 + \delta_K -1.
   $$
1. Thus the spectral norm of $\Phi_R^H \Phi_R - \bI$
   which is its largest eigen value
   (see {prf:ref}`thm:mat:2_norm_square_matrices`)
   satisfies
   
   $$
    \| \Phi_R^H \Phi_R - \bI \|_2 \leq \delta_K.
   $$
1. Plugging back we get
   
   $$
    \| \Phi_S^H \Phi_T \|_2  \leq \delta_K.
   $$
````


This result has a useful corollary. It establishes the approximate
orthogonality between a set of columns in $\Phi$ and portion of a
sparse vector not covered by those columns.

````{prf:corollary}
:label: cor:approximate_orthogonality_submatrix_vector

Let $\Phi$ satisfy the RIP of order $K$ where $K \leq M$. 
Let $T \subset \{1, \dots, N \}$ be an index set and 
let $\bx \in \CC^N$ be some vector.
Let $S = \supp(\bx)$.
Further let us assume that $K \geq | T \cup S |$.
Define $R = S \setminus T$.

Then the following holds

$$
\| \Phi_T^H \Phi \bx_R \|_2 \leq \delta_K \| \bx_R \|_2
$$
where $\bx_R$ is obtained by keeping entries in $\bx$
indexed by $R$ while setting others to 0
(see {prf:ref}`def:ssm:signal_restriction`).
````

````{prf:proof}
The set $R$ denotes the indices at which $\bx$
is nonzero but not yet covered in $T$. In a typical
sparse recovery algorithm, one has discovered
a candidate support $T$ which may not include
all of $S$.

1. Since 
   
   $$
    \Phi \bx = \sum_{i=1}^N \phi_i x_i
   $$
   and $\bx_R$ is zero on entries not indexed by $R$, hence

   $$
    \Phi \bx_R = \Phi_R \bx_R
   $$
   where on the R.H.S. $\bx_R \in \CC^{|R|}$
   by dropping the 0 entries from it not indexed by $R$
   (see  {prf:ref}`def:ssm:signal_restriction`).
1. Thus we have
   
   $$
    \| \Phi_T^H \Phi \bx_R \|_2 = \| \Phi_T^H \Phi_R \bx_R \|_2.
   $$
1. From {prf:ref}`lem:mat:operator_norm_subordinate`
   we know that any operator norm is subordinate.
1. Thus
   
   $$
    \| \Phi_T^H \Phi_R \bx_R \|_2 
    \leq \| \Phi_T^H \Phi_R \|_2 \| \bx_R \|_2.
   $$
1. Since $K \geq | T \cup S |$ hence we have
   
   $$
    | R | = | S \setminus T | \leq K.
   $$ 
1. Further $T$ and $R$ are disjoint and $| T \cup R | \leq K$.
1. Applying {prf:ref}`lem:proj:rip:approximate_orthogonality`
   we get
   
   $$
    \| \Phi_T^H \Phi_R \|_2 \leq \delta_K.
   $$
1. Putting back, we get our desired result
   
   $$
    \| \Phi_T^H \Phi \bx_R \|_2 \leq \delta_K \| \bx_R \|_2.
   $$
````

## Signal Proxy


We can use the results so far to formalize 
the idea of signal proxy.

````{prf:theorem}
:label: lem:proj:rip:signal_proxy_bounds

Let $\bx$ be a $k$-sparse signal 
Let $\Phi$ satisfy the RIP of order $k + l$ or higher.
Let $\bp$ be defined as

$$
\bp = (\Phi^H \Phi \bx)|_l
$$
i.e. $\bp$ is obtained by keeping the $l$ 
largest entries in $\bb = \Phi^H \Phi \bx$.
Then the following holds

$$
\| \bp \|_2 \leq (1 + \delta_l + \delta_{k + l})
\| \bx \|_2.
$$
````
````{prf:proof}
Let $A = \supp(\bx)$ and $B = \supp(\bp)$.

1. Then $|A| \leq k$ and $|B| \leq l$.
1. Clearly

   $$
   \bp = (\Phi^H \Phi \bx)|_l = (\Phi^H \Phi \bx)_B.
   $$
1. From {prf:ref}`lem:ssm:restriction_on_matrix_vector_product`
   we get
   
   $$
   \bp = \Phi_B^H \Phi \bx.
   $$
1. Let $C  = A \setminus B$.
1. Since $\bx$ is
   supported on  $A$ only, hence we can write
   
   $$
    \bx = \bx_B + \bx_C.
   $$
1. Thus from {prf:ref}`cor:ssm:matrix_vector_product_disjoint_set_seperation`
   we get ($B$ and $C$ are disjoint)
   
   $$
    \Phi \bx = \Phi_B \bx_B + \Phi_C \bx_C.
   $$
1. Thus we have
   
   $$
    \bp = \Phi_B^H \Phi_B \bx_B + \Phi_B^H \Phi_C \bx_C.
   $$
1. Using triangle inequality we can write
   
   $$
    \| \bp \|_2 
    \leq \|\Phi_B^H \Phi_B \bx_B \|_2 
    + \| \Phi_B^H \Phi_C \bx_C\|_2.
   $$
1. {prf:ref}`lem:proj:rip:phi_J_gram_embedding_l2_norm_bounds_range` gives us
   
   $$
    \|\Phi_B^H \Phi_B \bx_B \|_2 \leq (1 + \delta_l) \|\bx_B \|_2.
   $$
1. Since $B$ and $C$ are disjoint, hence 
   {prf:ref}`lem:proj:rip:approximate_orthogonality` gives us
   
   $$
    \| \Phi_B^H \Phi_C \bx_C\|_2 \leq \delta_{k +l} \| \bx_C \|_2.
   $$
1. Since $B$ and $C$ are disjoint, hence
   
   $$
   \| \bx_B \|_2 \leq \| \bx \|_2
   \text{ and }
   \| \bx_C \|_2 \leq \| \bx \|_2.
   $$
1. Finally 
   
   $$
    \| \bp \|_2
    \leq (1 + \delta_l) \|\bx_B \|_2 +  \delta_{k +l} \| \bx_C \|_2
    \leq (1 + \delta_l + \delta_{k +l}) \| \bx \|_2.
   $$
````

## RIP and Inner Product

Let $\bx$ and $\bx'$ be two different vectors in $\CC^N$
such that their support is disjoint.
i.e. if 

$$
T = \supp(\bx) \subseteq \{ 1 , \dots, N \}
$$
and

$$
T' = \supp(\bx') \subseteq \{ 1, \dots, N \}
$$
then $T \cap T' = \EmptySet$.

```{div}
Clearly

$$
\| \bx \|_0 = |T |
$$
and

$$
\| \bx' \|_0 = | T' |.
$$

Since the support of $\bx$ and $\bx'$ are disjoint
hence it is straightforward that

$$
\langle \bx, \bx' \rangle = 0.
$$

What can we say about the inner product of
their corresponding embedded vectors $\Phi \bx $ and $\Phi \bx'$? 
```

Following theorem provides an upper bound on the magnitude
of the inner product when the signal vectors
$\bx , \bx'$ belong to the Euclidean space $\RR^N$.
This result is adapted from {cite}`candes2008restricted`.

````{prf:theorem}
:label: lem:rip:inner_product_upper_bound

Assume that the sensing matrix $\Phi \in \RR^{M \times N}$.
For all $\bx, \bx' \in \RR^N$
supported on disjoint subsets $T, T' \subseteq \{1,\dots, N \}$
with $ |T| < k$ and 
$|T| < k'$, we have 

$$
| \langle \Phi \bx, \Phi \bx' \rangle | 
\leq \delta_{k + k'} \| \bx \|_2 \| \bx' \|_2
$$
where $\delta_{k + k'}$ is the restricted isometry constant
for the sparsity level $k + k'$.
````

````{prf:proof}

Let $\widehat{\bx} = \frac{ \bx}{\| \bx \|_2}$
and $\widehat{\bx'} = \frac{\bx'}{\| \bx' \|_2}$
be the corresponding unit norm vectors. 

1. Then
   
   $$
    \langle  \Phi \bx, \Phi \bx' \rangle 
    = \langle  \Phi \widehat{x}, \Phi \widehat{x'} \rangle
     \| \bx \|_2 \| \bx' \|_2.
   $$
1. Hence if we prove the bound for unit norm vectors,
   then it will be straightforward to prove the bound for
   arbitrary vectors.
1. Let us assume without loss of generality that 
   $\bx, \bx'$ are unit norm.
1. We need to show that
   
   $$
    | \langle \Phi \bx, \Phi \bx' \rangle | 
    \leq \delta_{k + k'}.
   $$
1. With the help of parallelogram identity
   ({prf:ref}`res-la-parallelogram-identity-2`), we have
   
   $$
    \langle \Phi \bx, \Phi \bx' \rangle  = \frac{1}{4} 
    \left ( 
    \|\Phi \bx + \Phi \bx' \|_2^2 - \| \Phi \bx - \Phi \bx' \|_2^2
    \right ).
   $$
1. Thus
   
   $$
    |\langle \Phi \bx, \Phi \bx' \rangle |  = \frac{1}{4} 
    \left |
    \|\Phi \bx + \Phi \bx' \|_2^2 - \| \Phi \bx - \Phi \bx' \|_2^2
    \right |.
   $$
1. Now 
   
   $$
    \| \bx \pm \bx' \|_2^2 
    = \| \bx\|_2^2 + \| \bx' \|_2^2 
    \pm 2 \langle \bx, \bx' \rangle 
    =  \| \bx\|_2^2 + \| \bx' \|_2^2 = 2
   $$
   since $\bx , \bx'$ are orthogonal and unit norm.
1. Using {prf:ref}`lem:proj:rip_sum_difference` we have
   
   $$
    &(1 - \delta_{k + k'}) \| \bx  \pm \bx' \|_2^2 
    \leq \| \Phi \bx  \pm  \Phi \bx' \|_2^2 
    \leq (1 + \delta_{k + k'}) \| \bx  \pm  \bx' \|_2^2\\
    \implies &  2 (1 - \delta_{k + k'}) 
    \leq \| \Phi \bx  \pm  \Phi \bx' \|_2^2 
    \leq 2 (1 + \delta_{k + k'}).
   $$
1. Hence the maximum value of
   $\| \Phi \bx  \pm  \Phi \bx' \|_2^2$ can be $2 (1 + \delta_{k + k'})$
   while the minimum value of
   $\| \Phi \bx  \pm \Phi \bx' \|_2^2$ can be $2 (1 - \delta_{k + k'})$. 
1. This gives us the upper bound
   
   $$
    |\langle \Phi \bx, \Phi \bx' \rangle | 
    \leq \frac{1}{4} \left ( 2 (1 + \delta_{k + k'}) - 2 (1 - \delta_{k + k'})\right )
    =  \delta_{k + k'}.
   $$
1. Finally when $\bx, \bx'$ are not unit norm, 
   the bound generalizes to
   
   $$
    |\langle \Phi \bx, \Phi \bx' \rangle | 
    \leq  \delta_{k + k'} \| \bx \|_2 \| \bx' \|_2.
   $$
````

A variation of this result is presented below:

````{prf:theorem}
:label: lem:rip:inner_product_upper_bound_2

Assume that the sensing matrix $\Phi \in \RR^{M \times N}$.
Let $\bu, \bv \in \RR^N$ be given and let 

$$
K = \max( \| \bu + \bv \|_0 , \| \bu - \bv \|_0). 
$$
Let $\Phi$ satisfy RIP of order $K$ with the constant $\delta_K$.
Then

$$
| \langle \Phi \bu, \Phi \bv \rangle - \langle \bu, \bv \rangle | 
\leq \delta_{K} \| \bu \|_2 \| \bv \|_2.
$$
````
This result is more general as it doesn't require $\bu, \bv$ to be
supported on disjoint index sets. All it requires is them 
to be sufficiently sparse.

````{prf:proof}
As, in the previous result, it is sufficient to prove it 
for the case where $\| \bu \|_2 = \| \bv \|_2 = 1$.
The simplified inequality becomes

$$
| \langle \Phi \bu, \Phi \bv \rangle - \langle \bu, \bv \rangle | 
\leq \delta_{K}.
$$
1. Clearly
   
   $$
    \| \bu \pm \bv \|_2^2 = \| \bu \|_2^2 + \| \bv \|_2^2 \pm 2 
    \langle \bu , \bv \rangle
    = 2 \pm 2 \langle \bu , \bv \rangle. 
   $$
1. Due to RIP, we have
   
   $$
    (1 - \delta_K) (2 \pm 2 \langle \bu , \bv \rangle) 
    \leq \| \Phi (\bu \pm \bv ) \|_2^2
    \leq (1 + \delta_K)(2 \pm 2 \langle \bu , \bv \rangle).
   $$
1. From the parallelogram identity, we have
   
   ```{math}
    :label: eq:proj:33e1bfe4-c5be-47f6-b84e-0d26788ea290

    \langle \Phi \bu , \Phi \bv \rangle 
    = \frac{1}{4} \left ( 
    \| \Phi ( \bu + \bv) \|_2^2 - \| \Phi ( \bu - \bv) \|_2^2
    \right ).
   ```
1. Taking the upper bound on $\| \Phi ( \bu + \bv) \|_2^2$ 
   and the lower bound on $\| \Phi ( \bu - \bv) \|_2^2$ in 
   {eq}`eq:proj:33e1bfe4-c5be-47f6-b84e-0d26788ea290`, we obtain
   
   $$
    \langle \Phi \bu , \Phi \bv \rangle \leq \frac{1}{2}
    \left ((1 + \delta_K)(1 +  \langle \bu , \bv \rangle)  
    - (1 - \delta_K)(1  -  \langle \bu , \bv \rangle) 
    \right ).
   $$
1. Simplifying, we get
   
   $$
    \langle \Phi \bu , \Phi \bv \rangle 
    \leq \langle \bu , \bv \rangle + \delta_K.
   $$
1. At the same time, taking the lower bound on $\| \Phi ( \bu + \bv) \|_2^2$ 
   and the upper bound on $\| \Phi ( \bu - \bv) \|_2^2$ in 
   {eq}`eq:proj:33e1bfe4-c5be-47f6-b84e-0d26788ea290`, we obtain
   
   $$
    \langle \Phi \bu , \Phi \bv \rangle \geq \frac{1}{2}
    \left ((1 - \delta_K)(1 +  \langle \bu , \bv \rangle)  
    - (1 + \delta_K)(1  -  \langle \bu , \bv \rangle) 
    \right ).
   $$
1. Simplifying, we get
   
   $$
    \langle \Phi \bu , \Phi \bv \rangle \geq \langle \bu , \bv \rangle - \delta_K.
   $$
1. Combining the two results, we obtain
   
   $$
    | \langle \Phi \bu , \Phi \bv \rangle - \langle \bu , \bv \rangle | 
    \leq \delta_K.
   $$
````


For the complex case, the result can be generalized if we 
choose a bilinear inner product rather than the usual
sesquilinear  inner product.

````{prf:theorem}
:label: lem:rip:inner_product_upper_bound_2_complex

Let $\bu, \bv \in \CC^N$ be given and let 

$$
K = \max( \| \bu + \bv \|_0 , \| \bu - \bv \|_0). 
$$
Let the complex space $\CC^N$ be equipped with the
bilinear inner product

$$
\langle \bu, \bv \rangle_B \triangleq \Re (\langle \bu, \bv \rangle)
$$
i.e. the real part of the standard inner product.

Let $\Phi$ satisfy RIP of order $K$ with the constant $\delta_K$.
Then

$$
| \langle \Phi \bu, \Phi \bv \rangle_B - \langle \bu, \bv \rangle_B | 
\leq \delta_{K} \| \bu \|_2 \| \bv \|_2.
$$
````

````{prf:proof}
Recall that the norm induced by the bilinear inner product 
$\langle \bu, \bv \rangle_B$ is the usual $\ell_2$ norm since

$$
\langle \bu, \bu \rangle_B  = \Re (\langle \bu, \bu \rangle) 
= \Re (\| \bu \|_2^2) =\| \bu \|_2^2.  
$$

1. Let us just work out the parallelogram identity for the complex case
   
   $$
    \| \bx \pm \by \|_2^2 
    &= \langle \bx \pm \by , \bx \pm \by \rangle_B\\
    &= \langle \bx, \bx \rangle_B 
    + \langle \by, \by \rangle_B 
    \pm \langle \bx, \by \rangle_B 
    \pm \langle \by, \bx \rangle_B\\
    &= \langle \bx, \bx \rangle_B 
    + \langle \by, \by \rangle_B \pm 2 \langle \bx, \by \rangle_B
   $$
   due to the bilinearity of the real inner product.
1. We can see that the rest of the proof is identical to the proof of
   {prf:ref}`lem:rip:inner_product_upper_bound_2`.
````



## RIP and Orthogonal Projection

The first result in this section is presented for real matrices. 
The generalization for complex matrices will be done later.

1. Let $\Lambda \subset \{1, \dots, N \}$
   be an index set.
1. Let $\Phi \in \RR^{M \times N}$ satisfy RIP of order $K$
   with the restricted isometry constant $\delta_K$.
1. Assume that the columns of $\Phi_{\Lambda}$
   are linearly independent. 
1. We can define the pseudo inverse as

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
   $\ColSpace(\Phi_{\Lambda})$
   (column space of $\Phi_{\Lambda}$) is given by

    $$
    \bP_{\Lambda}^{\perp} = \bI - \bP_{\Lambda}.
    $$
1. Both $\bP_{\Lambda}$ and $\bP_{\Lambda}^{\perp}$
   satisfy the usual properties like $\bP = \bP^H$ and $\bP^2 = \bP$.

We further define

$$
\Psi_{\Lambda} = \bP_{\Lambda}^{\perp} \Phi.
$$
1. We are orthogonalizing the columns in $\Phi$
   against $\ColSpace(\Phi_{\Lambda})$.
1. In other words, keeping the component of the column
   which is orthogonal to the column space 
   of $\Phi_{\Lambda}$.
1. Obviously the columns in $\Psi_{\Lambda}$ corresponding
   to the index set $\Lambda$ would be $\bzero$.

We now present a result which shows that
the matrix $\Psi_{\Lambda}$
satisfies a modified version of RIP {cite}`davenport2010analysis`.

````{prf:theorem}
:label: res:proj:rip_orthogonal_projection

If $\Phi$ satisfies the RIP of order $K$
with isometry constant $\delta_K$, and
$\Lambda \subset \{1, \dots, N\}$
with $|\Lambda | < K$, 
then the matrix
$\Psi_{\Lambda}$ satisfies the modified 
version of RIP  as

```{math}
:label: eq:proj:rip_orthogonal_projection

\left ( 1 - \frac{\delta_K}{1 - \delta_K} \right )
\| \bx \|_2^2 
\leq \| \Psi_{\Lambda} \bx \|_2^2
\leq (1 + \delta_K) \| \bx \|_2^2
```
for all $\bx \in \RR^N$ such that
$\|\bx \|_0 \leq K - | \Lambda|$
and $\supp(\bx) \cap \Lambda = \EmptySet$.
````

In words, if $\Phi$ satisfies
RIP of order $K$, then $\Psi_{\Lambda}$
acts as an approximate isometry on every 
$(K - |\Lambda|)$-sparse vector supported
on $\Lambda^c$. 
````{prf:proof}
From the definition of $\Psi_{\Lambda}$, we have

$$
\Psi_{\Lambda} \bx = (\bI - \bP_{\Lambda})\Phi \bx
= \Phi \bx - \bP_{\Lambda} \Phi \bx.
$$
1. Alternatively
   
   $$
     \Phi \bx = \Psi_{\Lambda} \bx + \bP_{\Lambda} \Phi \bx.
   $$
1. Since $\bP_{\Lambda}$ is an orthogonal
   projection, hence the vectors
   $\bP_{\Lambda} \Phi \bx$ and
   $\Psi_{\Lambda} \bx = \bP_{\Lambda}^{\perp} \Phi \bx$
   are orthogonal.
1. Thus, we can write
   
   ```{math}
    :label: eq:proj:43731f7a-f6ad-4e22-a3ac-0b6f9b1edaf4

    \| \Phi \bx \|_2^2 
    = \| \bP_{\Lambda} \Phi \bx \|_2^2 
    + \|\Psi_{\Lambda} \bx \|_2^2.
   ```
1. We need to show that 
   $\| \Phi \bx \|_2 \approx \|\Psi_{\Lambda} \bx \|_2$
   or alternatively that $\| \bP_{\Lambda} \Phi \bx \|_2$
   is small under the conditions of the theorem.
1. Since $ P_{\Lambda} \Phi \bx $ is
   orthogonal to $\Psi_{\Lambda} \bx$,
   hence
   
   ```{math}
    :label: eq:proj:67c2f988-5a17-4f3c-a60f-521d6a7e34c9
    \langle \bP_{\Lambda} \Phi \bx, \Phi \bx \rangle
    &= \langle \bP_{\Lambda} \Phi \bx, \Psi_{\Lambda} \bx + \bP_{\Lambda} \Phi \bx \rangle \\
    &=  \langle \bP_{\Lambda} \Phi \bx, \bP_{\Lambda} \Phi \bx \rangle + 
    \langle \bP_{\Lambda} \Phi \bx, \Psi_{\Lambda} \bx \rangle\\
    &= \langle \bP_{\Lambda} \Phi \bx, \bP_{\Lambda} \Phi \bx \rangle\\
    &= \| \bP_{\Lambda} \Phi \bx \|_2^2.
    ```
1. Since $\bP_{\Lambda}$ is a projection onto the 
   $\ColSpace(\Phi_{\Lambda})$
   (column space of $\Phi_{\Lambda}$),
   there exists a vector $\bz \in \CC^N$, such that
   $P_{\Lambda} \Phi \bx =  \Phi \bz$ and $\supp(\bz) \subseteq \Lambda$.
1. Since $\supp(\bx) \cap \Lambda = \EmptySet$, hence 
   $\langle \bx, \bz \rangle = 0$.
1. We also note that $\| \bx + \bz \|_0 = \| \bx - \bz \|_0 \leq K$. 
1. Invoking {prf:ref}`lem:rip:inner_product_upper_bound_2`, we have
   
   $$
    | \langle \Phi \bz, \Phi \bx \rangle | 
    \leq \delta_{K} \| \bz \|_2 \| \bx \|_2.
   $$
1. Alternatively
   
   $$
    | \langle \bP_{\Lambda} \Phi \bx, \Phi \bx \rangle | 
    \leq \delta_{K} \| \bz \|_2 \| \bx \|_2.
   $$
1. From RIP, we have
   
   $$
    \sqrt{1 - \delta_K} \| \bz \|_2 \leq \| \Phi \bz \|_2
   $$
   and
   
   $$
    \sqrt{1 - \delta_K} \| \bx \|_2 \leq \| \Phi \bx \|_2.
   $$
1. Thus
   
   $$
    (1 - \delta_K)\| \bz \|_2 \| \bx \|_2 
    \leq \| \Phi \bz \|_2 \| \Phi \bx \|_2.
   $$
1. This gives us
   
   $$
    | \langle \bP_{\Lambda} \Phi \bx, \Phi \bx \rangle | 
    \leq \frac{\delta_K}{1 - \delta_K} \|  P_{\Lambda} \Phi \bx \|_2 \| \Phi \bx \|_2.
   $$
1. Applying {eq}`eq:proj:67c2f988-5a17-4f3c-a60f-521d6a7e34c9`, we get
   
   $$
    \|  \bP_{\Lambda} \Phi \bx \|_2^2
    \leq \frac{\delta_K}{1 - \delta_K} \|  \bP_{\Lambda} \Phi \bx \|_2 \| \Phi \bx \|_2.
   $$
1. Canceling the common term, we get
   
   $$
    \|  \bP_{\Lambda} \Phi \bx \|_2 \leq \frac{\delta_K}{1 - \delta_K} \| \Phi \bx \|_2.
   $$
1. Trivially, we have $\|  \bP_{\Lambda} \Phi \bx \|_2 \geq 0$.
1. Applying these bounds on {eq}`eq:proj:43731f7a-f6ad-4e22-a3ac-0b6f9b1edaf4`,
   we obtain
   
   $$
    \left ( 1 -  \left ( \frac{\delta_K}{1 - \delta_K}\right )^2 \right )
    \| \Phi \bx \|_2^2
    \leq  
    \|\Psi_{\Lambda} \bx \|_2^2
    \leq \| \Phi \bx \|_2^2.
   $$
1. Finally, using the RIP again with
   
   $$
    (1 - \delta_K) \| \bx \|_2^2 
    \leq \|\Phi \bx \|_2^2 
    \leq (1 + \delta_K) \| \bx \|_2^2
   $$
   we obtain
   
   $$
    \left ( 1 -  \left ( \frac{\delta_K}{1 - \delta_K}\right )^2 \right )
    (1 - \delta_K) \| \bx \|_2^2 
    \leq  
    \|\Psi_{\Lambda} \bx \|_2^2
    \leq (1 + \delta_K) \| \bx \|_2^2 .
   $$
1. Simplifying
   
   $$
    \left ( 1 -  \left ( \frac{\delta_K}{1 - \delta_K}\right )^2 \right )
    (1 - \delta_K)
    &= \frac{1 + \delta_K^2 - 2 \delta_K - \delta_K^2}{1 - \delta_K}\\
    &= \frac{1 - 2 \delta_K }{1 - \delta_K} \\
    &= 1  - \frac{\delta_K}{1 - \delta_K}.
   $$
1. Thus, we get the intended result in 
   {eq}`eq:proj:rip_orthogonal_projection`.
````

## RIP for Higher Orders

If $\Phi$ satisfies RIP of order $K$, does it satisfy RIP of some other order $K' > K$? 
There are some results available to answer this question.

````{prf:theorem}
:label: lem:rip:higher_order_rip_constant_bound

Let $c$ and $k$ be integers and let $\Phi$ satisfy RIP of order $2 k$.
$\Phi$ satisfies RIP of order $c k$ with a restricted isometry constant 

$$
\delta_{ck} \leq c \delta_{2 k}
$$
if $c \delta_{2 k} < 1$. 
````
Note that this is only a sufficient condition.
Thus if $c \delta_{2 k} \geq 1$ we are not claiming
whether $\Phi$ satisfies RIP of order $ck$ or not.

````{prf:proof}
For $c=1$, $\delta_k \leq  \delta_{2 k}$.
For $c=2$, $\delta_{2 k} \leq 2 \delta_{2 k}$.
These two cases are trivial.
We now consider the case for $c \geq 3$.

1. Let $S$ be an arbitrary index set of size $c k$. Let
   
   $$
    \Delta = \Phi_S^H \Phi_S - \bI.
   $$
1. From {prf:ref}`lem:proj:rip_gram_matrix_eigen_value_sufficient_condition`,
   a sufficient condition for $\Phi$ to satisfy RIP of order $c k$ is that 

    $$
        \| \Delta \|_2 < 1
    $$
    for all index sets $S$ with $|S|= c k$.
1. Thus if we can show that

    $$
        \| \Delta \|_2 \leq c \delta_{2 k} 
    $$
    we would have shown that $\Phi$ satisfies RIP of order $c k$.
1. We note that $\Phi_S$ is of size $M \times c k$.
1. Thus $\Delta$ is of size $c k \times c k$.
1. We partition $\Delta$ into a block matrix of size $c \times c$ 

    $$
        \Delta = \begin{bmatrix}
        \Delta_{11} & \Delta_{12} & \dots & \Delta_{1 c}\\
        \Delta_{21} & \Delta_{22} & \dots & \Delta_{2 c}\\
        \vdots & \vdots & \ddots & \vdots\\
        \Delta_{c 1} & \Delta_{c 2} & \dots & \Delta_{c c}\\
        \end{bmatrix}
    $$
   where each entry $\Delta_{i j}$ is a square matrix of size $k \times k$.
1. Each diagonal matrix $\Delta_{i i}$ corresponds to some
   $\Phi_T^H \Phi_T - \bI$ where $|T| = k$. 
1. Thus we have (see {prf:ref}`lem:proj:rip:submatrix_eigenvalue_sum_k`)
    
    $$
        \| \Delta_{i i} \|_2 \leq \delta_k.
    $$
1. The off-diagonal matrices $\Delta_{i j}$ are

    $$
        \Delta_{i j} = \Phi_P^H \Phi_Q
    $$
   where $P$ and $Q$ are disjoint index sets with $|P| = |Q| = k$
   with $ | P \cup Q | = 2 k$.
1. Thus  from the approximate orthogonality condition
   ({prf:ref}`lem:proj:rip:approximate_orthogonality` )
   we have

    $$
        \| \Delta_{i j} \|_2 \leq \delta_{2 k}.
    $$
1. Finally we apply Gershgorin circle theorem for block matrices
   ({prf:ref}`col:block_gershgorin_disc_theorem_psd_matrix`).
1. This gives us

    $$
     | \| \Delta \|_2  - \|\Delta_{ii}\|_2| 
     \leq \sum_{j, j\neq i} \|\Delta_{i j} \| \text{ for some } i \in \{1,2, \dots, c \}.
    $$
1. Thus we have

    $$
    &  | \| \Delta \|_2  - \delta_k | 
    \leq \sum_{j, j\neq i} \delta_{2 k} \\
     \implies & | \| \Delta \|_2  - \delta_k | \leq  (c - 1) \delta_{2 k} \\
     \implies &  \| \Delta \|_2 \leq \delta_k +  (c - 1) \delta_{2 k} \\
     \implies &  \| \Delta \|_2 \leq \delta_{2 k} +  (c - 1) \delta_{2 k} \\
     \implies &  \| \Delta \|_2 \leq  c \delta_{2 k}.
    $$
1. We have shown that $\| \Delta \|_2 \leq  c \delta_{2 k} < 1$.
1. Thus $\delta_{c k} \leq \| \Delta \|_2$.
1. Hence $\Phi$ indeed satisfies RIP of order $c k$.
````
This theorem helps us extend RIP from an order $K$ to higher orders.
If $\delta_{2 k}$ isn't sufficiently small, the bound isn't useful.

## Embeddings of Arbitrary Signals

So far we have considered only sparse signals while analyzing the embedding 
properties of a RIP satisfying matrix $\Phi$. In this subsection
we wish to explore bounds on the $\ell_2$ norm of an arbitrary signal when
embedded by $\Phi$.
This result is adapted from {cite}`needell2009cosamp`.


````{prf:theorem}
:label: thm:proj:rip:arbitrary_signal_energy_bound

Let $\Phi$ be an an $M \times N$ matrix satisfying 

```{math}
:label: eq:rip:arbitrary_signal_energy_bound_rip_upper_bound_condition

\| \Phi \bx \|_2 \leq \sqrt{1 + \delta_K} \| \bx \|_2 \Forall \bx \in \Sigma_K.
```
Then for every signal $\bx \in \CC^N$, the following holds:

$$
\| \Phi \bx \|_2 
\leq \sqrt{ 1 + \delta_K} \left [  \| \bx \|_2 + \frac{1}{\sqrt{K}} \| \bx \|_1 \right ].
$$
````
We note that the theorem requires $\Phi$ to satisfy only the upper bound of RIP
property {eq}`eq:proj:restricted_isometry_property_bound`.
The proof is slightly involved.

````{prf:proof}
We note that the bound is trivially true for $\bx = \bzero$.
Hence in the following we will consider only for $\bx \neq \bzero$.

1. Consider an arbitrary index set 
   $\Lambda \subset \{ 1, 2, \dots, N \}$ such that $| \Lambda | \leq K$.
1. Consider the unit ball in the Banach space $\ell_2(\Lambda)$ given by

    ```{math}
    :label: eq:rip:arbitrary_signal_energy_bound_l_2_K_banach_space_unit_ball
    B_2^{\Lambda} = \{ \bx \in \CC^N \ST \supp(\bx) = \Lambda \text{ and } \| \bx \|_2 \leq 1 \}
    ```
    i.e. the set of all signals whose support is $\Lambda$ and
    whose $\ell_2$ norm is less than or equal to 1.
1. Now define a convex body 

    ```{math}
    :label: eq:rip:arbitrary_signal_energy_bound_k_sparse_unit_ball_convex_hull
    S = \ConvexHull \left \{ \bigcup_{| \Lambda | \leq K}  
    B_2^{\Lambda} \right \} \subset \CC^N.
    ```
1. We recall from {prf:ref}`def-convex-hull` that if
   $\bx$ and $\by$ belong to $S$ then their
   convex combination $\theta \bx + (1 - \theta) \by$
   with $\theta \in [0,1]$ must lie in $S$.
1. Further it can be verified that $S$ is a compact 
   convex set with non-empty interior.
1. Hence it is a convex body.
1. Consider any $\bx \in B_2^{\Lambda_1}$ and $\by \in B_2^{\Lambda_2}$. 
1. From {eq}`eq:rip:arbitrary_signal_energy_bound_rip_upper_bound_condition`
   and 
   {eq}`eq:rip:arbitrary_signal_energy_bound_l_2_K_banach_space_unit_ball`
   we have

    $$
    \| \Phi \bx \|_2 \leq  \sqrt{1 + \delta_K} \| \bx \|_2 \leq \sqrt{1 + \delta_K}
    $$
    and

    $$
    \| \Phi \by \|_2 \leq  \sqrt{1 + \delta_K} \| \by \|_2 \leq \sqrt{1 + \delta_K}.
    $$
1. Now let 

    $$
        \bz  = \theta \bx + (1 - \theta ) \by \text{ where } \theta \in [0, 1].
    $$
1. Then 

    $$
        \| \bz \|_2 = \| \theta \bx + (1 - \theta ) \by \|_2 
        \leq \theta \| \bx \|_2 + (1 - \theta ) \| \by \|_2
        \leq \theta + (1 - \theta) = 1.
    $$
1. Further

    $$
    \| \Phi \bz  \|_2 &= \| \Phi ( \theta \bx + (1 - \theta ) \by) \|_2 \\
    &\leq \| \Phi \theta \bx\|_2  + \| \Phi(1 - \theta ) \by \|_2\\
    &= \theta \| \Phi \bx \|_2 + (1 - \theta) \| \Phi \by \|_2 \\
    &\leq \theta \sqrt{1 + \delta_K} + (1  - \theta) \sqrt{1 + \delta_K}\\
    &\leq  \sqrt{1 + \delta_K}.
    $$
1. Similarly, it can be shown that for every vector $\bx \in S$ we have
   $\| \bx\|_2 \leq 1$ and $\| \Phi \bx \|_2 \leq \sqrt{1 + \delta_K}$.
   1. Let $\bx \in S$.
   1. Then $\bx = \sum_{i=1}^r t_i \bx_i$ such that
      $\bx_i \in  B_2^{\Lambda_i}$ where $|\Lambda_i| \leq K$,
      $t_i \geq 0$ and $\sum t_i = 1$.
   1. Hence $ \| \bx_i \|_2 \leq 1$ for every $i$.
   1. Hence 

      $$
      \| \bx \|_2 \leq \sum_{i=1}^r t_i \| \bx_i \|_2 \leq \sum_{i=1}^r t_i = 1.
      $$
   1. Similarly $\| \Phi \bx_i \|_2 \leq \sqrt{1 + \delta_K}$.
   1. Hence 

      $$
      \| \Phi \bx \|_2 
      \leq  \sum_{i=1}^r t_i \| \Phi \bx_i \|_2
      \leq \sqrt{1 + \delta_K}.
      $$
1. We now define another convex body 

    ```{math}
    :label: eq:rip:arbitrary_signal_energy_bound_convex_body_2
    \Gamma = \left \{ \bx \ST \| \bx \|_2 + \frac{1}{\sqrt{K}} \| \bx \|_1 
    \leq 1 \right \} \subset \CC^N.
    ```
1. We quickly verify the convexity property.
   1. Let $\bx, \by \in \Gamma$.
   1. Let 
      
      $$
      \bz = \theta \bx + (1  - \theta) \by \quad \text{ where }  \theta \in [0,1].
      $$
    1. Then 

        $$
        & \| \bz \| + \frac{1}{\sqrt{K}} \| \bz \|_1 \\
        & = \| \theta \bx + (1  - \theta) \by \|_2 
        + \frac{1}{\sqrt{K}} \| \theta \bx + (1  - \theta) \by \|_1\\
        & \leq \theta \| \bx \|_2  + (1 - \theta) \| \by \|_2 
        + \frac{\theta}{\sqrt{K}} \| \bx \|_1 
        + \frac{(1  - \theta)}{\sqrt{K}} \| \by \|_1 \\
        & = \theta \left [ \| \bx \|_2 + \frac{1}{\sqrt{K}} \| \bx \|_1  \right ] + 
        (1 - \theta) \left [\| \by \|_2 + \frac{1}{\sqrt{K}} \| \by \|_1  \right ] \\
        & \leq \theta + (1 - \theta) = 1.
        $$

    1. Thus $\bz \in \Gamma$.
    1. This analysis shows that all convex combinations
       of elements in $\Gamma$ belong to $\Gamma$.
    1. Thus $\Gamma$ is convex.
    1. Further it can be verified that $\Gamma$ is a compact 
       convex set with non-empty interior. 
    1. Hence it is a convex body. 
1. For any $\bx \in \CC^N$
   one can find a $\by \in \Gamma$
   by simply applying an appropriate nonzero scale $\by = c \bx$
   where the scale factor $c$ depends on $\bx$.
1. For a moment suppose that $\Gamma \subset S$.
1. Then if $\by \in \Gamma$ the following are true:

   $$
    \| \by \|_2 + \frac{1}{\sqrt{K}} \| \by \|_1 \leq 1
   $$
   and

   $$
    \| \Phi \by \|_2 \leq \sqrt{1 + \delta_K}.
   $$
1. Now consider an arbitrary nonzero $\bx \in \CC^N$.
1. Let

    $$
    \alpha  = \| \bx \|_2 + \frac{1}{\sqrt{K}} \| \bx \|_1.
    $$
1. Define 
    
    $$
    \by = \frac{1}{\alpha} \bx.
    $$
1. Then 
   
   $$
    \|\by \|_2  + \frac{1}{\sqrt{K}} \| \by \|_1 = 
    \frac{1}{\alpha} \left ( \| \bx \|_2  + \frac{1}{\sqrt{K}} \| \bx \|_1\right ) = 1. 
   $$
1. Thus $\by \in \Gamma$ and 

    $$
    & \| \Phi \by \|_2 \leq \sqrt{1 + \delta_K}\\
    \implies & \left \| \Phi \frac{1}{\alpha} \bx \right \|_2  \leq \sqrt{1 + \delta_K}\\
    \implies & \| \Phi \bx \|_2 \leq  \sqrt{1 + \delta_K} \alpha \\
    \implies & \| \Phi \bx \|_2 \leq  \sqrt{1 + \delta_K} 
    \left ( \| \bx \|_2 + \frac{1}{\sqrt{K}} \| \bx \|_1 \right )
    \Forall \bx \in \CC^N
    $$
    which is our intended result.
1. Hence if we show that $\Gamma \subset S$ holds, 
   we would have proven our theorem.

We will achieve this by showing that every vector $\bx \in \Gamma$ can be
shown to be a convex combination of vectors in $S$.
1. We start with an arbitrary $\bx \in \Gamma$.
1. Let $I = \supp(\bx)$.
1. We partition $I$ into disjoint sets of size $K$.
1. Let there be $J+1$ such sets given by

    $$
    I = \bigcup_{j = 0}^J I_j.
    $$
1. Let $I_0$ index the $K$ largest entries in $\bx$ (magnitude wise).
1. Let $I_1$ be next $K$ largest entries and so on. 
1. Since $|I|$ may not be a multiple of $K$, hence 
   the last index set $I_J$ may not have
   $K$ indices.
1. We define 
   
   $$
    \bx_{I_j}(i) = \left\{
            \begin{array}{ll}
                x(i) & \mbox{if $i \in I_j$};\\
                0 & \mbox{otherwise}.
            \end{array}
          \right.
   $$
1. Thus we can write

    $$
    \bx = \sum_{j = 0}^J \bx_{I_j}.
    $$
1. Now let 

    $$
    \theta_j = \| \bx_{I_j} \|_2 \; \text{ and } \; 
    \by_j = \frac{1}{\theta_j} \bx_{I_j}.
    $$
1. We can write

    $$
    \bx = \sum_{j = 0}^J \theta_j \by_j.
    $$
1. In this construction of $\bx$ we can see that
   $1 \geq \theta_0 \geq \theta_1 \geq \dots \geq \theta_J \geq 0$.
1. Also $\by_j \in S$ since $\by_j$ is a unit norm $K$ sparse vector 
  {eq}`eq:rip:arbitrary_signal_energy_bound_k_sparse_unit_ball_convex_hull`.
1. We will show that $\sum_j \theta_j \leq 1$ in a short while.
1. This will imply that $\bx$ is a convex combination of vectors from $S$.
1. But since $S$ is convex hence $\bx \in S$.
1. This will imply that $\Gamma \subset S$. 
1. The proof will be complete.

We now show that $\sum_j \theta_j \leq 1$.

1. Pick any $j \in \{1, \dots, J \}$.
1. Since $\bx_{I_j}$ is $K$-sparse hence due to 
   {prf:ref}`lem:u_sigma_k_norms` we have

    $$
    \theta_j = \| \bx_{I_j} \|_2 \leq \sqrt{K} \| \bx_{I_j} \|_{\infty}.
    $$
1. It is easy to see that $I_{j-1}$ identifies exactly $K$ nonzero entries in $\bx$
   and each of nonzero entries in $\bx_{I_{j -1}}$ is larger than the largest entry 
   in $\bx_{I_j}$ (magnitude wise).
1. Thus we have

    $$
     \| \bx_{I_{j-1}} \|_1 = \sum_{ i \in I_{j-1}} | x_i |
     \geq \sum_{ i \in I_{j-1}} \| \bx_{I_j} \|_{\infty}
      = K \| \bx_{I_j} \|_{\infty}.
    $$
1. Thus

    $$
    \| \bx_{I_j} \|_{\infty} \leq \frac{1}{K} \| \bx_{I_{j-1}} \|_1.
    $$
1. Combining the two inequalities we get

    $$
    \theta_j \leq \frac{1}{\sqrt{K}} \| \bx_{I_{j -1}} \|_1.
    $$
1. This lets us write

    $$
    \sum_{j=1}^{J}\theta_j \leq \sum_{j=1}^{J}\frac{1}{\sqrt{K}} \| \bx_{I_{j -1}} \|_1 
    \leq  \frac{1}{\sqrt{K}} \| \bx \|_1
    $$
    since 

    $$
    \| \bx \|_1 = \sum_{j = 0}^J \| \bx_{I_j} \|_1 
    \geq \sum_{j = 1}^J \| \bx_{I_{j-1}} \|_1.
    $$
1. Finally 

    $$
    \theta_0 = \| \bx_{I_0} \|_2 \leq \| \bx \|_2.
    $$
1. This gives us the inequality 

    $$
    \sum_{j = 0}^J  \theta_j \leq \| \bx \|_2 
    + \frac{1}{\sqrt{K}} \| \bx \|_1 \leq 1 
    $$
    since  $\bx \in \Gamma$.
1. Recalling our steps we can express $\bx$  as

    $$
    \bx  = \theta_j \by_j 
    $$
    where $\by_j \in S$ and 
    $\sum \theta_j \leq 1$ implies that $\bx \in S$ since $S$
    is convex.
1. Thus $\Gamma \subset S$.
1. This completes the proof.
````

## A General Form of RIP



A more general restricted isometry bound can be for an arbitrary matrix 
$\Phi$ can be as follows

$$
\alpha \| \bx \|^2_2 \leq \| \Phi \bx \|^2_2 \leq \beta \| \bx \|^2_2  
$$
where $0 < \alpha \leq \beta < \infty$.

It is straightforward to scale $\Phi$ to match the bounds in
{eq}`eq:proj:restricted_isometry_property_bound`. 

Let $\delta_K = \frac{\beta - \alpha}{\alpha + \beta}$. 
Then $1 - \delta_K = \frac{2\alpha}{\alpha + \beta}$
and $1 + \delta_K = \frac{2\beta}{\alpha + \beta}$.

Putting in  {eq}`eq:proj:restricted_isometry_property_bound` we get

$$
& \frac{2\alpha}{\alpha + \beta} \| \bx \|^2_2 
\leq \| \Phi \bx \|^2_2 
\leq \frac{2\beta}{\alpha + \beta} \| \bx \|^2_2  \\
\implies & \alpha \| \bx \|^2_2 
\leq \| \sqrt{\frac{\alpha + \beta}{2}} \Phi \bx \|^2_2 
\leq \beta \| \bx \|^2_2.
$$
Thus by multiplying $\Phi$ with $\sqrt{2/(\alpha + \beta)}$
we can transform the more general bound 
to the form of {eq}`eq:proj:restricted_isometry_property_bound`.

## Finding out RIP Constants

The optimal value of RIP constant of $K$-th order $\delta_K$
can be obtained by solving the following optimization problem.

````{prf:algorithm}
:label: def:proj:optimal_rip_constant

$$
& \underset{0 < \delta < 1}{\text{minimize}} 
& & \delta\\
& \text{subject to }
& &  (1 - \delta) \|\bx\|^2_2 
\leq \| \Phi \bx \|^2_2 
\leq (1 + \delta) \| \bx\|^2_2 
\Forall \bx \in \Sigma_K.
$$
````
This problem isn't easy to solve.
In fact it has been shown in {cite}`bandeira2013certifying`
that this problem is NP-hard.

## RIP and Coherence

Here we establish a relationship between the RIP constants
and coherence of a dictionary.

Rather than a general matrix $\Phi$, we restrict our attention to a 
dictionary $\bDDD \in \CC^{N \times D}$
We assume that the dictionary
is overcomplete $(D > N)$ and full rank $\Rank(\bDDD) = N$.
Dictionary is assumed to satisfy RIP of some order.

````{prf:theorem} Coherence upper bound for RIP constant
:label: res:proj:rip_coherence_bound

Let $\bDDD$ satisfy RIP of order $K$. Then

$$
\delta_K \leq (K - 1) \mu (\bDDD).
$$
````
````{prf:proof}
We recall that $\delta_K$ is the smallest constant $\delta$ satisfying

$$
(1 - \delta) \| \bx\|^2_2 
\leq \| \bDDD \bx \|^2_2 
\leq (1 + \delta) \| \bx\|^2_2 \; 
\Forall \bx \in \Sigma_K.
$$

1. Let $\Lambda$ be any index set with $| \Lambda | = K$. 
1. Then

    $$
     \| \bDDD \bx \|^2_2 
     =  \| \bDDD_{\Lambda} \bx_{\Lambda} \|^2_2 
     \Forall \bx \in \CC^{\Lambda}.
    $$
1. Since $\bDDD$ satisfies RIP of order $K$, 
   hence $\bDDD_{\Lambda}$ is a subdictionary
   (its columns are linearly independent).
1. Recall from {prf:ref}`res:ssm:subdict_norm_bound_coherence` that

    $$
    (1 - (K - 1)   \mu) \| \bv \|_2^2 
    \leq \| \bDDD_{\Lambda} \bv \|_2^2 
    \leq (1 + (K - 1)   \mu)\| \bv \|_2^2 
    $$
    holds true for every $\bv \in \CC^K$.
1. Since $\delta_K$ is smallest possible constant, hence

    $$
    1 + \delta_K \leq 1 + (K - 1)   \mu 
    \implies \delta_K \leq (K - 1) \mu (\bDDD).
    $$
````

