# Matrix Norms

This section reviews various matrix norms on the vector space of
complex matrices over the field of complex numbers $(\CC^{m \times n}, \CC)$.

We know $(\CC^{m \times n}, \CC)$ is a finite dimensional vector space with
dimension $m n$. We will usually refer to it as $\CC^{m \times n}$.

Matrix norms will follow the usual definition of norms for a vector space.

````{prf:definition} Matrix norm
:label: def:mat:matrix_norm

A function $\| \cdot \| : \CC^{m \times n} \to \RR$ is called a *matrix norm* on
$\CC^{m \times n}$ if for all $\bA, \bB \in \CC^{m \times n}$ and all $\alpha \in \CC$
it satisfies the following

* [Positivity] 

   $$
    \| \bA \| \geq 0 
   $$
   with $\| \bA \| = 0 \iff \bA  = \ZERO$.  
*  [Homogeneity]

    $$
        \| \alpha \bA \| = | \alpha | \| \bA \|.
    $$
*  [Triangle inequality]

    $$
        \| \bA + \bB \| \leq \| \bA \| + \| \bB \|.
    $$
````

We recall some of the standard results on finite dimensional normed vector spaces.

All matrix norms are equivalent. Let $\| \cdot \|$ and $\| \cdot \|'$
be two different matrix norms on  $\CC^{m \times n}$. Then 
there exist two constants $a$ and $b$ such that the following holds

$$
a \| \bA \| \leq \| \bA \|' \leq b \|A \|  \Forall \bA \in \CC^{m \times n}.
$$
A matrix norm is a continuous function $\| \cdot \| : \CC^{m \times n} \to \RR$.

## Norms like $\ell_p$ on Complex Vector Space
Following norms are quite like $\ell_p$ norms on
finite dimensional complex vector space $\CC^n$. 
They are developed
by the fact that the matrix vector space $\CC^{m\times n}$
has one to one correspondence with the complex vector space $\CC^{m n}$.

````{prf:definition} Sum norm
:label: def:mat:sum_norm

Let $\bA \in \CC^{m\times n}$ and $\bA  = [a_{i j}]$.

Matrix *sum norm* is defined as

$$
\| \bA \|_S  = \sum_{i=1}^{m} \sum_{j=1}^n | a_{i j} |
$$
````


````{prf:definition} Frobenius norm
:label: def:mat:frobenius_norm

Let $\bA \in \CC^{m\times n}$ and $\bA  = [a_{i j}]$.

Matrix *Frobenius norm* is defined as

$$
\| \bA \|_F  = \left ( \sum_{i=1}^{m} \sum_{j=1}^n | a_{i j} |^2 \right )^{\frac{1}{2}}.
$$
````

````{prf:definition} Max norm
:label: def:mat:max_norm

Let $\bA \in \CC^{m\times n}$ and $\bA  = [a_{i j}]$.

Matrix *Max norm* is defined as

$$
\| \bA \|_M  = \underset{\substack{
1 \leq i \leq m \\ 1 \leq j \leq n}}{\max} | a_{i j} |.
$$
````
## Properties of Frobenius Norm
We now prove some elementary properties of Frobenius norm.

````{prf:lemma}
:label: lem:mat:frobenius_norm_hermitian_transpose

The Frobenius norm of a matrix is equal to the Frobenius norm of its Hermitian transpose.

$$
\| \bA^H \|_F = \| \bA \|_F.
$$
````

````{prf:proof}
This is valid since the norm involves only the absolute values of entries
in the matrix.

1. Let 

    $$
        \bA = [a_{i j}].
    $$
1. Then

    $$
        \bA^H = [\overline{a_{j i}}]
    $$
1. Then

    $$
        \| \bA^H \|_F^2 
        = \left ( \sum_{j=1}^n \sum_{i=1}^{m} | \overline{a_{i j}} |^2 \right )
        = \left ( \sum_{i=1}^{m} \\ \sum_{j=1}^n | a_{i j} |^2 \right )
        = \| \bA \|_F^2.
    $$
1. Now

   $$
    \| \bA^H \|_F^2 = \| \bA \|_F^2 \implies \| \bA^H \|_F = \| \bA \|_F.
   $$
````

````{prf:lemma} Expansion in squared norms of columns
:label: lem:mat:frob_norm_column_vectors

Let $\bA \in \CC^{m \times n}$ be written as a row of column vectors

$$
\bA = \begin{bmatrix}
\ba_1 & \dots & \ba_n
\end{bmatrix}.
$$
Then

$$
\| \bA \|_F^2 = \sum_{j=1}^{n} \| \ba_j \|_2^2.
$$
````

````{prf:proof}
We note that 

$$
    \| \ba_j \|_2^2 = \sum_{i=1}^m \| a_{i j} \|_2^2.
$$
Now

$$
\| \bA \|_F^2 = \left ( \sum_{i=1}^{m} \sum_{j=1}^n | a_{i j} |^2 \right )
= \left ( \sum_{j=1}^n \left ( \sum_{i=1}^{m}  | a_{i j} |^2  \right ) \right )
= \left (\sum_{j=1}^n  \| \ba_j \|_2^2 \right).
$$
````

We thus showed that that the square of the Frobenius norm of a matrix
is nothing but the sum of squares of $\ell_2$ norms of its columns.

````{prf:lemma}
:label: lem:mat:frob_norm_row_vectors

Let $\bA \in \CC^{m \times n}$ be written as a column of row vectors

$$
\bA = \begin{bmatrix}
\underline{\ba}^1 \\
\vdots \\
\underline{\ba}^m
\end{bmatrix}.
$$
Then

$$
\| \bA \|_F^2 = \sum_{i=1}^{m} \| \underline{\ba}^i \|_2^2.
$$
````

````{prf:proof}
We note that 

$$
\| \underline{\ba}^i \|_2^2 = \sum_{j=1}^n \| a_{i j} \|_2^2.
$$
Now

$$
\| \bA \|_F^2 = \left ( \sum_{i=1}^{m} \sum_{j=1}^n | a_{i j} |^2 \right )
= \sum_{i=1}^{m} \| \underline{\ba}^i \|_2^2.
$$
````

We now consider how the Frobenius norm is affected with the action of unitary matrices.

1. Let $\bA$ be any arbitrary matrix in $\CC^{m \times n}$.
1. Let $\bU$ be some unitary matrices in $\CC^{m \times m}$. 
1. Let $\bV$ be some unitary matrices in $\CC^{n \times n}$.

We present our first result that multiplication with unitary matrices
doesn't change Frobenius norm of a matrix.

````{prf:theorem}
:label: thm:mat:frobenius_norm_unitary_matrix_invariant

The Frobenius norm of a matrix is invariant to
pre or post multiplication by a unitary matrix. i.e.

$$
\| \bU \bA \|_F = \| \bA \|_F
$$
and

$$
\| \bA \bV \|_F = \| \bA \|_F.
$$
````

````{prf:proof}
We can write $\bA$ as

$$
\bA = \begin{bmatrix}
\ba_1 & \dots & \ba_n
\end{bmatrix}.
$$
So 

$$
\bU \bA = \begin{bmatrix}
\bU \ba_1 & \dots & \bU \ba_n
\end{bmatrix}.
$$
Then applying {prf:ref}`lem:mat:frob_norm_column_vectors` clearly

$$
\| \bU \bA \|_F^2 =  \sum_{j=1}^{n} \|\bU \ba_j \|_2^2.
$$

But we know that unitary matrices are norm preserving. Hence

$$
\|\bU \ba_j \|_2^2 = \| \ba_j \|_2^2.
$$
Thus

$$
\| \bU \bA \|_F^2 = \sum_{j=1}^{n} \|\ba_j \|_2^2 = \| \bA \|_F^2
$$
which implies

$$
\| \bU \bA \|_F = \| \bA \|_F.
$$

Similarly writing $\bA$ as

$$
\bA = \begin{bmatrix}
\br_1 \\
\vdots \\
\br_m
\end{bmatrix}.
$$
we have

$$
\bA \bV = \begin{bmatrix}
\br_1  \bV\\
\vdots \\
\br_m \bV
\end{bmatrix}.
$$

Then applying {prf:ref}`lem:mat:frob_norm_row_vectors` clearly

$$
\| \bA \bV \|_F^2 = \sum_{i=1}^{m} \| \br_i \bV \|_2^2.
$$
But we know that unitary matrices are norm preserving. Hence

$$
\|\br_i \bV \|_2^2 = \|\br_i \|_2^2.
$$
Thus

$$
\| \bA \bV \|_F^2 = \sum_{i=1}^{m} \| \br_i \|_2^2 =  \| \bA \|_F^2
$$
which implies

$$
\| \bA \bV \|_F = \| \bA \|_F.
$$

An alternative approach for the 2nd part of the proof using the first part is just one line

$$
\| \bA \bV \|_F 
= \| (\bA \bV)^H \|_F = \| \bV^H \bA^H \|_F = \| \bA^H \|_F = \| \bA \|_F.
$$
In above we use {prf:ref}`lem:mat:frobenius_norm_hermitian_transpose` 
and the fact that $\bV$ is a unitary matrix implies that $\bV^H$ is also a unitary matrix.
We have already shown that pre multiplication by a unitary matrix preserves Frobenius norm.
````

````{prf:theorem} Consistency of Frobenius norm
:label: thm:mat:frobenius_norm_consistency

Let $\bA \in \CC^{m \times n}$ and $\bB \in \CC^{n \times p}$ be two matrices.
Then the Frobenius norm of their product is less than
or equal to the product of Frobenius norms
of the matrices themselves. i.e.

$$
\| \bA \bB \|_F \leq \| \bA \|_F \| \bB \|_F.
$$
````

````{prf:proof}
We can write $\bA$ as

$$
\bA = \begin{bmatrix}
\ba_1^T \\
\vdots \\
\ba_m^T
\end{bmatrix}
$$
where $\ba_i$ are $m$ column vectors corresponding to rows of $\bA$.
Similarly we can write  $\bB$ as

$$
\bB = \begin{bmatrix}
\bb_1 &
\dots &
\bb_p
\end{bmatrix}
$$
where $\bb_i$ are column vectors corresponding to columns of $\bB$.

Then

$$
\bA \bB = 
\begin{bmatrix}
\ba_1^T \\
\vdots \\
\ba_m^T
\end{bmatrix}
\begin{bmatrix}
\bb_1 &
\dots &
\bb_p
\end{bmatrix}
=  \begin{bmatrix}
\ba_1^T \bb_1 & \dots & \ba_1^T \bb_p\\
\vdots  & \ddots & \vdots \\
\ba_m^T \bb_1 & \dots & \ba_m^T \bb_p
\end{bmatrix}
= \begin{bmatrix}
\ba_i^T \bb_j
\end{bmatrix}
.
$$
Now looking carefully

$$
\ba_i^T \bb_j = \langle \ba_i, \overline{\bb_j} \rangle.
$$
Applying the Cauchy-Schwartz inequality we have

$$
| \langle \ba_i, \overline{\bb_j} \rangle |^2 
\leq \| \ba_i \|_2^2 \| \overline{\bb_j} \|_2^2 
 =  \| \ba_i \|_2^2 \| \bb_j \|_2^2. 
$$
Now

$$
\| \bA \bB \|_F^2 
&= \sum_{i=1}^{m} \sum_{j=1}^{p} | \ba_i^T \bb_j |^2\\
&\leq \sum_{i=1}^{m} \sum_{j=1}^{p} \| \ba_i \|_2^2 \| \bb_j \|_2^2\\
&= \left ( \sum_{i=1}^{m} \| \ba_i \|_2^2 \right ) \left ( \sum_{j=1}^{p}  \| \bb_j \|_2^2\right )\\
&= \| \bA \|_F^2  \| \bB \|_F^2 
$$
which implies

$$
\| \bA \bB \|_F \leq \| \bA \|_F \| \bB \|_F
$$
by taking square roots on both sides.
````

````{prf:corollary}
:label: cor:mat:frobenius_norm_subordinate_euclidean_norm

Let $\bA \in \CC^{m \times n}$ and let $\bx \in \CC^n$. Then

$$
\| \bA \bx \|_2 \leq \| \bA \|_F \| \bx \|_2.
$$
````

````{prf:proof}
We note that Frobenius norm for a column matrix is same as 
$\ell_2$ norm for corresponding column vector. i.e.

$$
\| \bx \|_F = \| \bx \|_2 \Forall \bx \in \CC^n.
$$

Now applying  {prf:ref}`thm:mat:frobenius_norm_consistency` we have

$$
\| \bA \bx \|_2 
= \| \bA \bx \|_F \leq \| \bA \|_F \| \bx \|_F 
=  \| \bA \|_F \| \bx \|_2 \Forall \bx \in \CC^n.
$$
````

It turns out that Frobenius norm is intimately related to the
singular value decomposition 
of a matrix.

````{prf:lemma} Frobenius norm and singular values
:label: res:mat:frobenius_norm_sum_of_singular_values

Let $\bA \in \CC^{m \times n}$. Let the singular value decomposition of $\bA$
be given by

$$
\bA = \bU \Sigma \bV^H.
$$
Let the singular values of $\bA$ be $\sigma_1, \dots, \sigma_k$
where $k = \min(m, n)$.
Then 

$$
\| \bA \|_F = \sqrt {\sum_{i=1}^k \sigma_i^2}.
$$
````
````{prf:proof}
This comes from the invariance of Frobenius norm with unitary
transformations.

$$
\bA = \bU \Sigma \bV^H \implies \|A \|_F = \| \bU \Sigma \bV^H \|_F.
$$
But

$$
 \| \bU \Sigma \bV^H \|_F = \| \Sigma \bV^H \|_F = \| \Sigma \|_F
$$
since $\bU$ and $\bV$ are unitary matrices (see {prf:ref}`thm:mat:frobenius_norm_unitary_matrix_invariant`
). 
Now the only nonzero terms in $\Sigma$ are the singular values.  Hence

$$
\| \bA \|_F = \| \Sigma \|_F = \sqrt {\sum_{i=1}^k \sigma_i^2}.
$$
````

## Consistency of a Matrix Norm

````{prf:definition} Consistent matrix norm
:label: def:mat:consistent_matrix_norm

A matrix norm $\| \cdot \|$ is called *consistent* on $\CC^{n \times n}$ if

```{math}
:label: eq:consistent_matrix_norm_equation

\| \bA \bB \| \leq \| \bA \| \| \bB \| 
```
holds true for all $\bA, \bB \in \CC^{n \times n}$.
A matrix norm $\| \cdot \|$ is called  *consistent* if it is defined on $\CC^{m \times n}$ 
for all $m, n \in \Nat$ and
{eq}`eq:consistent_matrix_norm_equation` holds for all matrices
$\bA, \bB$ for which the product $\bA \bB$ is defined. 

A consistent matrix norm is also known as a *sub-multiplicative norm*.
````

With this definition and results in {prf:ref}`thm:mat:frobenius_norm_consistency` we can
see that Frobenius norm is consistent.

## Subordinate Matrix Norm

A matrix operates on vectors from one space to generate vectors in another space.
It is interesting to explore the connection between the norm of a matrix
and norms of vectors in the domain and co-domain of a matrix.

````{prf:definition}
:label: def:mat:subordinate_matrix_norm

Let $m, n \in \Nat$ be given. Let $\| \cdot \|_{\alpha}$  be some norm on $\CC^m$ and
$\| \cdot \|_{\beta}$  be some norm on $\CC^n$.
Let $\| \cdot \|$ be some norm on
matrices in $\CC^{m \times n}$.
We say that $\| \cdot \|$ is *subordinate*
to the vector norms $\| \cdot \|_{\alpha}$ and $\| \cdot \|_{\beta}$ if 

$$
\| \bA \bx \|_{\alpha} \leq \| \bA \| \| \bx \|_{\beta}
$$
for all $\bA \in \CC^{m \times n}$ and for all $\bx \in \CC^n$.
In other words the length of the vector doesn't increase by the operation of $\bA$
beyond a factor given by the norm of the matrix itself.

If $\| \cdot \|_{\alpha}$ and $\| \cdot \|_{\beta}$ are same then we say that
$\| \cdot \|$ is *subordinate* to the vector norm $\| \cdot \|_{\alpha}$.
````

We have shown earlier in {prf:ref}`cor:mat:frobenius_norm_subordinate_euclidean_norm` 
that Frobenius norm is subordinate to Euclidean norm.

## Operator Norm

We now consider the maximum factor by which a matrix $\bA$ can increase the
length of a vector.

````{prf:definition} Operator norm
:label: def:mat:operator_norm

Let $m, n \in \Nat$ be given.
Let $\| \cdot \|_{\alpha}$  be some norm on $\CC^n$ and
$\| \cdot \|_{\beta}$  be some norm on $\CC^m$.
For $\bA \in \CC^{m \times n}$ we define 

$$
\| \bA \| \triangleq \| \bA \|_{\alpha \to \beta} 
\triangleq \underset{\bx \neq 0}{\max }
\frac{\| \bA \bx \|_{\beta}}{\| \bx \|_{\alpha}}.
$$

The term $\frac{\| \bA \bx \|_{\beta}}{\| \bx \|_{\alpha}}$
represents the factor with which the length of $\bx$ increased by
operation of $\bA$.
We simply pick up the maximum value of such scaling factors over all nonzero $\bx$.

The norm as defined above is known as $(\alpha \to \beta)$ *operator norm*,
the $(\alpha \to \beta)$-norm,
or simply the $\alpha$-norm if $\alpha = \beta$.
````

````{div}
We need to verify that this definition satisfies all properties of a norm.

Nonnegativity

1. Clearly if $\bA = \ZERO$ then $\bA \bx = \bzero$ always, hence $\| \bA \| = 0$.
1. Conversely, if $\| \bA \| = 0$ then $\| \bA \bx \|_{\beta} = 0 \Forall \bx \in \CC^n$.
1. Hence $\bA \bx = \bzero$ for every $\bx \in \CC^n$.
1. In particular this is true for the unit vectors $\be_i \in \CC^n$.
1. The $i$-th column of $\bA$ is given by
   $\bA \be_i$ which is $\bzero$.
1. Thus each column in $\bA$ is $\bzero$.
1. Hence $\bA = \ZERO$. 

Homogeneity

1. Consider $c \in \CC$. 
1. Then

    $$
    \| c \bA \| = \underset{\bx \neq 0}{\max } \frac{\| c \bA \bx \|_{\beta}}{\| \bx \|_{\alpha}} 
    = | c | \underset{\bx \neq 0}{\max } \frac{\| \bA \bx \|_{\beta}}{\| \bx \|_{\alpha}} 
    = | c | \| \bA \|.
    $$

We now present some useful observations on operator norm before we can prove triangle
inequality for operator norm.

1. For any $\bx \in \Kernel(\bA)$,
   $\bA \bx = \bzero$ hence we only need to consider vectors which don't belong
   to the kernel of $\bA$.
1. Thus we can write

   $$
    \| \bA \|_{\alpha \to \beta} 
    = \underset{\bx \notin \Kernel(\bA)} {\max } 
    \frac{\| \bA \bx \|_{\beta}}{\| \bx \|_{\alpha}}.
   $$
1. We also note that 
   
   $$
    \frac{\| \bA c \bx \|_{\beta}}{\| c \bx \|_{\alpha}} 
    = \frac{| c | \| \bA \bx \|_{\beta}}{ | c | \| \bx \|_{\alpha}}
    = \frac{\| \bA \bx \|_{\beta}}{\| \bx \|_{\alpha}}  
    \Forall c \neq 0,  \bx \neq \bzero.
   $$
1. Thus, it is sufficient to find the maximum on unit norm vectors:
   
   $$
    \| \bA \|_{\alpha \to \beta} 
    = \underset{\| \bx \|_{\alpha} = 1} {\max } \| \bA \bx \|_{\beta}.
   $$
1. Note that since $\|\bx \|_{\alpha} = 1$ hence the term in denominator goes away.
````

````{prf:lemma} Operator norm is subordinate
:label: lem:mat:operator_norm_subordinate

The $(\alpha \to \beta)$-operator norm is subordinate to vector norms $\| \cdot \|_{\alpha}$
and $\| \cdot \|_{\beta}$. i.e.

$$
\| \bA \bx \|_{\beta} \leq \| \bA \|_{\alpha \to \beta } \| \bx \|_{\alpha}. 
$$
````
````{prf:proof}
For $\bx = \bzero$ the inequality is trivially satisfied.
For $\bx \neq \bzero$, by definition, we have

$$
\| \bA \|_{\alpha \to \beta } \geq 
\frac{\| \bA \bx \|_{\beta}}{\| \bx \|_{\alpha}} 
\implies \| \bA \|_{\alpha \to \beta } \| \bx \|_{\alpha} 
\geq \| \bA \bx \|_{\beta}.
$$
````

````{prf:theorem} Existence of the maximizer for operator norm
:label: res-mat-operator-norm-maximizer-exist

There exists a vector $\bx^* \in \CC^{n}$
with unit norm ($\| \bx^* \|_{\alpha} = 1$) such that

$$
\| \bA \|_{\alpha \to \beta} = \| \bA \bx^* \|_{\beta}.
$$
````

````{prf:proof}

Recall that

$$
\| \bA \|_{\alpha \to \beta} 
= \underset{\| \bx \|_{\alpha} = 1} {\max } \| \bA \bx \|_{\beta}.
$$

1. The norm function $\| \cdot \|_{\beta}$ is continuous on $\CC^m$.
1. The mapping $\bx \mapsto \bA \bx$ is continuous.
1. Hence the function $\bx \mapsto \| \bA \bx \|_{\beta}$ is continuous.
1. The set $\{ \bx \in \CC^n \ST \| \bx \|_{\alpha} = 1\}$ is compact.
1. Hence, the function attains a supremum value over this set.
````
We are now ready to prove triangle inequality for operator norm.


````{prf:lemma} Triangle inequality for operator norm
:label: lem:mat:operator_norm_triangular_inequality

Operator norm as defined in {prf:ref}`def:mat:operator_norm` satisfies triangle inequality.
````

````{prf:proof}
Let $\bA$ and $\bB$ be some matrices in $\CC^{m \times n}$.

1. Consider the operator norm of matrix $\bA + \bB$.
1. From previous remarks, there exists some vector
   $\bx^* \in \CC^n$ with $\| \bx^* \|_{\alpha} = 1$ such that
   
   $$
    \| \bA + \bB \| = \| (\bA + \bB) \bx^* \|_{\beta}.
   $$
1. Now 
   
   $$
    \| (\bA + \bB) \bx^* \|_{\beta}
    = \| \bA \bx^* + \bB \bx^* \|_{\beta} 
    \leq \| \bA \bx^*\|_{\beta} + \| \bB \bx^*\|_{\beta}. 
   $$
1. From subordinate property of operator norm, we have
   
   $$
    \| \bA \bx^*\|_{\beta}  \leq \| \bA \| \|\bx^*\|_{\alpha} = \| \bA \|
   $$
   and
   
   $$
    \| \bB \bx^*\|_{\beta}  \leq \| \bB \| \|\bx^*\|_{\alpha} = \|B \|
   $$
   since $\| \bx^* \|_{\alpha} = 1$.
1. Hence we have
   
   $$
    \| \bA + \bB \| \leq \| \bA \| + \| \bB \|.
   $$
````
It turns out that operator norm is also consistent under certain conditions. 

````{prf:lemma} Consistency of operator norm
:label: lem:mat:p_matrix_norms_are_consistent

Let $\| \cdot \|_{\alpha}$ be defined over all $m \in \Nat$.
Let $\| \cdot \|_{\beta} = \| \cdot \|_{\alpha}$. 
Then the operator norm

$$
\| \bA \|_{\alpha} 
= \underset{\bx \neq \bzero}{\max } \frac{\| \bA \bx \|_{\alpha}}{\| \bx \|_{\alpha}}
$$
is consistent.
````

````{prf:proof}
We need to show that

$$
\| \bA \bB \|_{\alpha} \leq \| \bA \|_{\alpha} \| \bB \|_{\alpha}.
$$

1. Now
   
   $$
    \| \bA \bB \|_{\alpha} 
    = \underset{\bx \neq \bzero}{\max } \frac{\| \bA \bB \bx \|_{\alpha}}{\| \bx \|_{\alpha}}.
   $$
1. We note that if $\bB \bx = \bzero$, then $\bA \bB \bx = \bzero$.
1. Hence we can rewrite as
   
   $$
    \| \bA \bB \|_{\alpha} 
    = \underset{\bB \bx \neq \bzero}{\max } 
    \frac{\| \bA \bB \bx \|_{\alpha}}{\| \bx \|_{\alpha}}.
   $$
1. Now if $\bB \bx \neq \bzero$ then $ \| \bB \bx \|_{\alpha} \neq 0$.
1. Hence
   
   $$
    \frac{\| \bA \bB \bx \|_{\alpha}}{\| \bx \|_{\alpha}} 
    = \frac{\| \bA \bB \bx \|_{\alpha}}{\|\bB \bx \|_{\alpha}} 
    \frac{\| \bB \bx \|_{\alpha}}{\| \bx \|_{\alpha}}
   $$
   and
   
   $$
     \underset{\bB \bx \neq \bzero}{\max }
     \frac{\| \bA \bB \bx \|_{\alpha}}{\| \bx \|_{\alpha}} \leq 
     \underset{\bB \bx \neq \bzero}{\max } 
     \frac{\| \bA \bB \bx \|_{\alpha}}{\|\bB \bx \|_{\alpha}} 
     \underset{\bB \bx \neq \bzero}{\max } 
     \frac{\| \bB \bx \|_{\alpha}}{\| \bx \|_{\alpha}}.
   $$
1. Clearly
   
   $$
    \| \bB \|_{\alpha} 
    = \underset{\bB \bx \neq \bzero}{\max } 
    \frac{\| \bB \bx \|_{\alpha}}{\| \bx \|_{\alpha}}.
   $$
1. Furthermore 
   
   $$
     \underset{\bB \bx \neq \bzero}{\max }
     \frac{\| \bA \bB \bx \|_{\alpha}}{\|\bB \bx \|_{\alpha}} 
     \leq
      \underset{\by \neq \bzero}{\max }
      \frac{\| \bA \by \|_{\alpha}}{\| \by \|_{\alpha}} 
      = \|\bA \|_{\alpha}.
   $$
1. Thus we have 
   
   $$
    \| \bA \bB \|_{\alpha} \leq \| \bA \|_{\alpha} \| \bB \|_{\alpha}.
   $$
````

(sec:mat:p_norm)=
## $p$-norm for Matrices

````{div}
We recall the definition of $\ell_p$ norms for vectors $\bx \in \CC^n$

$$
\| \bx \|_p = \begin{cases}
\left ( \sum_{i=1}^{n} | \bx |_i^p  \right ) ^ {\frac{1}{p}} &  p \in [1, \infty)\\
\underset{1 \leq i \leq n}{\max} |x_i| &  p = \infty
\end{cases}.
$$

The operator norms $\| \cdot \|_p$ defined from $\ell_p$ vector norms
are of specific interest.

````{prf:definition} Matrix $p$-norm
:label: def:mat:p_matrix_norm

The $p$-norm for a matrix $\bA \in \CC^{m \times n}$ is defined as

$$
\| \bA \|_p \triangleq \underset{\bx \neq \bzero}{\max }
\frac{\| \bA \bx \|_p}{\| \bx \|_p} 
= \underset{\| \bx \|_p = 1}{\max } \| \bA \bx \|_p
$$
where $\| \bx \|_p$ is the standard $\ell_p$ norm for vectors in $\CC^m$ and $\CC^n$.
````
As per {prf:ref}`lem:mat:p_matrix_norms_are_consistent` $p$-norms
for matrices are consistent norms.
They are also sub-ordinate to $\ell_p$ vector norms.

Special cases are considered for $p=1,2$  and $\infty$.

````{prf:theorem} Max column sum, max row sum, spectral norms
:label: thm:mat:closed_form_p_norms

Let $\bA \in \CC^{m \times n}$.

For $p=1$ we have

$$
\| \bA \|_1 = \underset{1\leq j \leq n}{\max} \sum_{i=1}^m | a_{i j}|.
$$
This is also known as *max column sum norm*.

For $p=\infty$ we have

$$
\| \bA \|_{\infty} = \underset{1\leq i \leq m}{\max} \sum_{j=1}^n | a_{i j}|.
$$
This is also known as *max row sum norm*.

Finally for $p=2$ we have

$$
\| \bA \|_2 = \sigma_1
$$
where $\sigma_1$ is the largest singular value of $\bA$.
This is also known as *spectral norm*.
````

````{prf:proof}
Max column sum norm:

1. Let

    $$
    \bA = \begin{bmatrix}
    \ba^1 & \dots, & \ba^n
    \end{bmatrix}.
    $$
1. Then

    $$
    \begin{aligned}
    \| \bA \bx \|_1 
    &= \left \| \sum_{j=1}^n x_j \ba^j \right \|_1 \\
    &\leq \sum_{j=1}^n \left \|  x_j \ba^j \right \|_1 \\
    &= \sum_{j=1}^n |x_j|  \left \| \ba^j \right \|_1 \\
    &\leq \underset{1 \leq j \leq n}{\max}\| \ba^j \|_1 \sum_{j=1}^n |x_j| \\
    &= \underset{1 \leq j \leq n}{\max}\| \ba^j \|_1 \| \bx \|_1.
    \end{aligned}
    $$
1. Thus,

    $$
    \| \bA \|_1 = \underset{\bx \neq \bzero}{\max } \frac{\| \bA \bx \|_1}{\| \bx \|_1}
    \leq \underset{1 \leq j \leq n}{\max}\| \ba^j \|_1
    $$
    which the maximum column sum.
1. We need to show that this upper bound is indeed an equality.
1. Indeed for any $\bx=\be_j$ where $\be_j$ is a unit vector
   with $1$ in $j$-th entry and 0 elsewhere, 

    $$
    \| \bA \be_j \|_1 = \| \ba^j \|_1.
    $$
1. Thus

    $$
    \| \bA \|_1 \geq \| \ba^j \|_1 \quad \Forall 1 \leq j \leq n.
    $$ 
1. Combining the two, we see that

    $$
    \| \bA \|_1 = \underset{1 \leq j \leq n}{\max}\| \ba^j \|_1.
    $$

Max row sum norm:

1. For $p=\infty$, we proceed as follows.

    $$
    \begin{aligned}
    \| \bA \bx \|_{\infty} &= \underset{1 \leq i \leq m}{\max}
    \left | \sum_{j=1}^n a_{i j } x_j \right | \\
    & \leq  \underset{1 \leq i \leq m}{\max}
    \sum_{j=1}^n | a_{i j } | | x_j |\\
    & \leq \underset{1 \leq j \leq n}{\max} | x_j | 
    \underset{1 \leq i \leq m}{\max} \sum_{j=1}^n | a_{i j } |\\
    &= \| \bx \|_{\infty} 
    \underset{1 \leq i \leq m}{\max}\| \underline{\ba}^i \|_1
    \end{aligned}
    $$
    where $\underline{\ba}^i$ are the rows of $\bA$.
1. This shows that

    $$
    \| \bA \bx \|_{\infty} \leq \underset{1 \leq i \leq m}{\max}\| \underline{\ba}^i \|_1.
    $$
1. We need to show that this is indeed an equality.
1. Fix an $i = k$ and choose $\bx$ such that

    $$
    x_j = \sgn (a_{k j}).
    $$
1. Clearly $\| \bx \|_{\infty} = 1$.
1. Then

    $$
    \begin{aligned}
    \| \bA \bx \|_{\infty} &= \underset{1 \leq i \leq m}{\max}
    \left | \sum_{j=1}^n a_{i j } x_j \right | \\
    &\geq \left | \sum_{j=1}^n a_{k j } x_j \right | \\
    &= \left |  \sum_{j=1}^n | a_{k j } |   \right | \\
    &= \sum_{j=1}^n | a_{k j } |\\
    &= \| \underline{\ba}^k \|_1.
    \end{aligned}
    $$
1. Thus, 

    $$
    \| \bA \|_{\infty} \geq \underset{1 \leq i \leq m}{\max}\| \underline{\ba}^i \|_1.
    $$
1. Combining the two inequalities we get:

    $$
    \| \bA \|_{\infty} = \underset{1 \leq i \leq m}{\max}\| \underline{\ba}^i \|_1.
    $$

Spectral norm:

1. Remaining case is for $p=2$.
1. For any vector $\bx$ with $\| \bx \|_2 = 1$,

    $$
    \| \bA \bx \|_2  = \| \bU \Sigma \bV^H \bx \|_2 
    = \| \bU (\Sigma \bV^H \bx )\|_2  = \| \Sigma \bV^H \bx \|_2
    $$
    since $\ell_2$ norm is invariant to unitary transformations.
1. Let $\bv = \bV^H \bx$.
1. Then $\|\bv\|_2 = \| \bV^H \bx \|_2 = \| \bx \|_2 = 1$.
1. Let $k = \min(m, n)$.
1. Now

    $$
    \| \bA \bx \|_2 &= \| \Sigma \bv \|_2\\ 
    &= \left ( \sum_{j=1}^k | \sigma_j v_j |^2 \right )^{\frac{1}{2}}\\
    &\leq  \sigma_1 \left ( \sum_{j=1}^k | v_j |^2 \right )^{\frac{1}{2}}\\
    &= \sigma_1 \| \bv \|_2 = \sigma_1.
    $$
1. This shows that 

    $$
    \| \bA \|_2 \leq \sigma_1.
    $$
1. Now consider some vector $\bx$ such that $\bv = (1, 0, \dots, 0)$.
1. Then

    $$
    \| \bA \bx \|_2 = \| \Sigma \bv \|_2 = \sigma_1.
    $$
1. Thus

    $$
    \| \bA \|_2 \geq \sigma_1.
    $$
1. Combining the two, we get that $\| \bA \|_2 = \sigma_1$.
````

(sec:mat:2_norm_matrix)=
## The $2$-norm

````{prf:theorem}
:label: thm:mat:2_norm_square_matrices

Let $\bA \in \CC^{n \times n}$ have singular values
$\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_n$. 
Let the eigen values for $\bA$ be
$\lambda_1, \lambda_2, \dots, \lambda_n$
with $|\lambda_1| \geq |\lambda_2| \geq \dots \geq |\lambda_n|$.
Then the following hold

$$
\| \bA \|_2 = \sigma_1 
$$
and if $\bA$ is nonsingular, then

$$
\| \bA^{-1} \|_2 = \frac{1}{\sigma_n}. 
$$

If $\bA$ is symmetric and positive definite, then

$$
\| \bA \|_2 = \lambda_1 
$$
and if $\bA$ is nonsingular, then

$$
\| \bA^{-1} \|_2 = \frac{1}{\lambda_n}.
$$
If $\bA$ is normal then

$$
\| \bA \|_2 = |\lambda_1|
$$
and if $\bA$ is nonsingular, then

$$
\| \bA^{-1} \|_2 = \frac{1}{|\lambda_n|}.
$$
````

## Unitary Invariant Norms

````{prf:definition} Unitary invariant norm
:label: def:mat:unitary_invariant_matrix_norms

A matrix norm $\| \cdot \|$ on $\CC^{m \times n}$ is called *unitary invariant* if
$\| \bU \bA \bV \| = \| \bA \|$ for any $\bA \in \CC^{m \times n}$
and any unitary matrices
$\bU \in \CC^{m \times m}$ and $\bV \in \CC^{n \times n}$.
````

We have already seen in {prf:ref}`thm:mat:frobenius_norm_unitary_matrix_invariant`
that Frobenius norm is unitary invariant. 

It turns out that spectral norm is also unitary invariant. 

## More Properties of Operator Norms

````{div}
In this section we will focus on operator norms connecting 
normed linear spaces $(\CC^n, \| \cdot \|_{p})$ and
$(\CC^m, \| \cdot \|_{q})$.
Typical values of $p, q$ would be in $\{1, 2, \infty\}$.

We recall that

$$
\| \bA \|_{p \to q } 
= \underset{\bx \neq \bzero}{\max} \frac{\| \bA \bx \|_q}{\| \bx \|_p}
= \underset{ \| \bx \|_p = 1}{\max} \| \bA \bx \|_q 
= \underset{\| \bx \|_p \leq 1}{\max} \| \bA \bx \|_q.
$$

The table below {cite}`tropp2004just` shows how to compute
different $(p, q)$ norms.
Some can be computed easily while others are NP-hard to compute.
````

````{list-table} Typical $(p \to q)$ norms
:header-rows: 1
:name: tbl:mat:calculation_p_q_operator_norms
* - $p$
  - $q$
  - $\| \bA \|_{p \to q}$
  - Calculation
* - 1 
  - 1 
  - $\| \bA \|_{1 }$ 
  - Maximum $l_1$ norm of a column 
* - 1 
  - 2 
  - $\| \bA \|_{1  \to 2}$ 
  - Maximum $l_2$ norm of a column
* - 1 
  - $\infty$ 
  - $\| \bA \|_{1  \to \infty}$ 
  - Maximum absolute entry of a matrix
* - 2 
  - 1 
  - $\| \bA \|_{2 \to 1}$ 
  - NP hard
* - 2 
  - 2 
  - $\| \bA \|_{2}$ 
  - Maximum singular value
* - 2 
  - $\infty$ 
  - $\| \bA \|_{2  \to \infty}$ 
  - Maximum $l_2$ norm of a row
* - $\infty$ 
  - 1 
  - $\| \bA \|_{\infty  \to 1}$ 
  - NP hard
* - $\infty$ 
  - 2 
  - $\| \bA \|_{\infty  \to 2}$ 
  - NP hard
* - $\infty$ 
  - $\infty$ 
  - $\| \bA \|_{\infty}$
  - Maximum $l_1$-norm of a row 
````

The topological dual of the finite dimensional normed linear space
$(\CC^n, \| \cdot \|_{p})$ 
is the normed linear space $(\CC^n, \| \cdot \|_{p'})$
where 

$$
\frac{1}{p} + \frac{1}{p'} = 1.
$$
* $\ell_2$-norm is dual of $l_2$-norm. It is a self dual. 
* $\ell_1$ norm and $\ell_{\infty}$-norm are dual of each other.

```{div}
When a matrix $\bA$ maps from the space $(\CC^n, \| \cdot \|_{p})$ to
the space $(\CC^m, \| \cdot \|_{q})$, we can view its
conjugate transpose $\bA^H$
as a mapping from the space $(\CC^m, \| \cdot \|_{q'})$
to $(\CC^n, \| \cdot \|_{p'})$.
```
````{prf:theorem} Operator norm and conjugate transpose
:label: res:mat:operator_norm_conjugate_transpose

Operator norm of a matrix always equals the operator norm of its conjugate transpose.
In other words

$$
\| \bA \|_{p \to q} = \| \bA^H \|_{q' \to p'}
$$
where

$$
\frac{1}{p} + \frac{1}{p'} = 1, \frac{1}{q} + \frac{1}{q'} = 1.
$$
````
````{div}
Specific applications of this result are:

$$
\| \bA \|_2 = \| \bA^H \|_2.
$$
This is obvious since the maximum singular value of a matrix and its conjugate 
transpose are same.

$$
\| \bA \|_1 = \| \bA^H \|_{\infty}, \quad \| \bA \|_{\infty} = \| \bA^H \|_1.
$$

This is also obvious since max column sum of $\bA$ is same as
the max row sum norm of $\bA^H$ and vice versa.

$$
\| \bA \|_{1 \to \infty} = \| \bA^H \|_{1 \to \infty}.
$$

$$
\| \bA \|_{1 \to 2} = \| \bA^H \|_{2 \to \infty}.
$$

$$
\| \bA \|_{\infty \to 2} = \| \bA^H \|_{2 \to 1}.
$$
````

We now need to show the result for the general case (arbitrary $1 \leq p, q \leq \infty$).
````{prf:proof}
TODO
````
````{prf:theorem} $1 \to p$ norm
:label: res:mat:1_to_p_operator_norm

$$
\| \bA \|_{1 \to p} = \underset{1 \leq j \leq n}{\max}\| \ba^j \|_p.
$$
where

$$
\bA = \begin{bmatrix}
\ba^1 & \dots, & \ba^n
\end{bmatrix}.
$$
````
````{prf:proof}
Expanding:

$$
\| \bA \bx \|_p 
&= \left \| \sum_{j=1}^n x_j \ba^j \right \|_p \\
&\leq \sum_{j=1}^n \left \|  x_j \ba^j \right \|_p \\
&= \sum_{j=1}^n |x_j|  \left \|   \ba^j \right \|_p \\
&\leq \underset{1 \leq j \leq n}{\max}\| \ba^j \|_p \sum_{j=1}^n |x_j| \\
&= \underset{1 \leq j \leq n}{\max}\| \ba^j \|_p \| \bx \|_1.
$$
Thus,

$$
\| \bA \|_{1 \to p} = \underset{\bx \neq \bzero}{\max } 
\frac{\| \bA \bx \|_p}{\| \bx \|_1}
\leq \underset{1 \leq j \leq n}{\max}\| \ba^j \|_p.
$$
We need to show that this upper bound is indeed an equality.

Indeed for any $\bx=\be_j$ where $\be_j$ is a unit vector
with $1$ in $j$-th entry and 0 elsewhere, 

$$
\| \bA \be_j \|_p = \| \ba^j \|_p.
$$
Thus

$$
\| \bA \|_{1 \to p} \geq \| \ba^j \|_p \quad \Forall 1 \leq j \leq n.
$$ 
Combining the two, we see that

$$
\| \bA \|_{1 \to p} = \underset{1 \leq j \leq n}{\max}\| \ba^j \|_p.
$$
````

````{prf:theorem} $p \to \infty$ norm
:label: res:mat:p_to_infty_operator_norm

$$
\| \bA \|_{p \to \infty} = \underset{1 \leq i \leq m}{\max}\| \underline{\ba}^i \|_q
$$
where

$$
\frac{1}{p} + \frac{1}{q} = 1.
$$
````
````{prf:proof}
Using {prf:ref}`res:mat:operator_norm_conjugate_transpose`, we get 

$$
\| \bA \|_{p \to \infty} = \| \bA^H \|_{1 \to q}.
$$
Using {prf:ref}`res:mat:1_to_p_operator_norm`, we get

$$
\| \bA^H \|_{1 \to q} = \underset{1 \leq i \leq m}{\max}\| \underline{\ba}^i \|_q.
$$
This completes the proof.
````


````{prf:theorem} Consistency of $p \to q$ norms
:label: res:mat:p_q_norm_consistency

For two matrices $\bA$ and $\bB$ with $p,q,s \geq 1$, we have

$$
\| \bA \bB \|_{p \to q} \leq 
 \| \bB \|_{p \to s} \| \bA \|_{s \to q}.
$$
````
````{prf:proof}
We start with

$$
\| \bA \bB \|_{p \to q}  = 
\underset{\| \bx \|_p = 1}{\max} \| \bA ( \bB \bx) \|_q.
$$

From {prf:ref}`lem:mat:operator_norm_subordinate`, we obtain

$$
\| \bA ( \bB \bx) \|_q \leq 
\| \bA \|_{s \to q} \| ( \bB \bx) \|_s.
$$ 
Thus,

$$
\| \bA \bB \|_{p \to q}  \leq  \| \bA \|_{s \to q}
\underset{\| \bx \|_p = 1}{\max} \| ( \bB \bx) \|_s
= \| \bA \|_{s \to q} \| \bB \|_{p \to s}.
$$
````

````{prf:theorem} Consistency of $p \to \infty$ norms
:label: res:mat:p_infty_norm_consistency

For two matrices $\bA$ and $\bB$ and $p \geq 1$, we have

$$
\| \bA \bB \|_{p \to \infty} \leq 
\| \bA \|_{\infty} \| \bB \|_{p \to \infty}.
$$
````
````{prf:proof}
We start with

$$
\| \bA \bB \|_{p \to \infty}  = 
\underset{\| \bx \|_p = 1}{\max} \| \bA ( \bB \bx) \|_{\infty}.
$$
From {prf:ref}`lem:mat:operator_norm_subordinate`, we obtain

$$
\| \bA ( \bB \bx) \|_{\infty} \leq 
\| \bA \|_{\infty \to \infty} \| ( \bB \bx) \|_{\infty}.
$$ 
Thus,

$$
\| \bA \bB \|_{p \to \infty}  \leq  \| \bA \|_{\infty \to \infty}
\underset{\| \bx \|_p = 1}{\max} \| ( \bB \bx) \|_{\infty}
= \| \bA \|_{\infty} \| \bB \|_{p \to \infty}.
$$
````

````{prf:theorem} Dominance of $p$-norm on $p \to \infty$ norm
:label: res:mat:dominance_p_infty_p_norm

$$
\| \bA \|_{p \to \infty} \leq \| \bA \|_{p}.
$$
In particular

$$
\| \bA \|_{1 \to \infty} \leq  \| \bA \|_{1}.
$$
Also:

$$
\| \bA \|_{2 \to \infty} \leq  \| \bA \|_{2}.
$$
````
````{prf:proof}
Choosing $q = \infty$ and $s = p$ and
applying {prf:ref}`res:mat:p_q_norm_consistency`

$$
\| \bI \bA \|_{p \to \infty} \leq 
 \| \bA \|_{p \to p} \| \bI \|_{p \to \infty}.
$$

But $\| \bI \|_{p \to \infty}$ is the maximum $\ell_p$
norm of any row of $\bI$ which is $1$.
Thus

$$
\| \bA \|_{p \to \infty} \leq  \| \bA \|_{p \to p}.
$$
````
````{div}
Consider the expression

$$
\underset{ \substack{\bz \in \ColSpace(\bA^H) \\ \bz \neq \bzero}}{\min} 
\frac{\| \bA \bz \|_{q}}{\| \bz \|_p}. 
$$

The constraint $\bz \in  \ColSpace(\bA^H), \bz \neq \bzero$ 
means there exists some vector $\bu \notin \Kernel(\bA^H)$ such that 
$\bz = \bA^H \bu$.

This expression measures the factor by which the non-singular part of $\bA$
can change the length of a vector.
````

````{prf:theorem}
:label: res:mat:bound_range_A_H_p_q_norm_pseudoinverse

The following bound holds for every matrix $\bA$:

$$
\underset{\substack{\bz \in \ColSpace(\bA^H)\\ \bz \neq \bzero}}{\min}
\frac{\| \bA \bz \|_{q}}{\| \bz \|_p}
\geq \| \bA^{\dag}\|_{q \to p}^{-1}.
$$
If $\bA$ is surjective (onto), then the equality holds. 
When $\bA$ is bijective (one-one onto, square, invertible),
then the result implies

$$
\underset{\substack{\bz \in \ColSpace(\bA^H) \\ \bz \neq \bzero}}{\min} 
\frac{\| \bA \bz \|_{q}}{\| \bz \|_p}
= \| \bA^{-1}\|_{q \to p}^{-1}.
$$
````
````{prf:proof}
The spaces $\ColSpace(\bA^H)$ and $\ColSpace(\bA)$
have same dimensions given by $\Rank(\bA)$.

1. We recall that $\bA^{\dag} \bA$ is a projector onto the column space of $\bA^H$. 
   
   $$
    \bw = \bA \bz \iff \bz = \bA^{\dag} \bw 
    = \bA^{\dag} \bA \bz \Forall \bz \in \ColSpace (\bA^H).
   $$
1. As a result we can write
   
   $$
   \frac{\| \bz \|_p}{ \| \bA \bz \|_q} =  \frac{\| \bA^{\dag} \bw \|_p}{ \| \bw \|_q} 
   $$
   whenever $\bz \in \ColSpace(\bA^H)$ and $\bz \neq \bzero$.
1. Now
   
   $$
     \left [ 
     \underset{\substack{\bz \in \ColSpace(\bA^H)\\ \bz \neq \bzero}}{\min} 
     \frac{\| \bA \bz \|_q}{\| \bz \|_p}\right ]^{-1}
    = \underset{\substack{\bz \in \ColSpace(\bA^H)\\ \bz \neq \bzero}}{\max} 
    \frac{\| \bz \|_p}{ \| \bA \bz \|_q}
    = \underset{\substack{\bw \in \ColSpace(\bA) \\ \bw \neq \bzero}}{\max} 
    \frac{\| \bA^{\dag} \bw \|_p}{ \| \bw \|_q} 
    \leq \underset{\bw \neq \bzero}{\max} \frac{\| \bA^{\dag} \bw \|_p}{ \| \bw \|_q}.
   $$
1. When $\bA$ is surjective, then $\ColSpace(\bA) = \CC^m$.
1. Hence
   
   $$
    \underset{\substack{\bw \in \ColSpace(\bA)\\ \bw \neq \bzero}}{\max} 
    \frac{\| \bA^{\dag} \bw \|_p}{ \| \bw \|_q} 
    = \underset{\bw \neq \bzero}{\max} \frac{\| \bA^{\dag} \bw \|_p}{ \| \bw \|_q}.
   $$
1. Thus, the inequality changes into equality.
1. Finally
   
   $$
    \underset{\bw \neq \bzero}{\max} 
    \frac{\| \bA^{\dag} \bw \|_p}{ \| \bw \|_q} = \| \bA^{\dag} \|_{q \to p}
   $$
   which completes the proof.
````

## Row Column Norms

A common way of measuring the norm of a matrix is to compute the
$\ell_p$ norm for each row and then compute the $\ell_q$ norm
of the resultant column vector. Such norms are known as
row column norms. 
1. If $p=q=2$, then the resultant norm is same as the Frobenius norm.
1. If $p=q=1$, then the resultant norm is same as the sum norm.
1. If $p=q=\infty$, then the resultant norm is same as the max norm.

Thus, one can think of the row column norms as a generalization of
these norms.

````{prf:definition} Row-column norms
:label: def:mat:row_column_norm

Let $\bA$ be an $m\times n$ matrix with rows $\underline{\ba}^i$ as

$$
\bA = \begin{bmatrix}
\underline{\ba}^1\\
\vdots \\
\underline{\ba}^m
\end{bmatrix}
$$
Then we define

$$
\| \bA \|_{p, \infty} 
\triangleq \underset{1 \leq i \leq m}{\max} \| \underline{\ba}^i \|_p
= \underset{1 \leq i \leq m}{\max} 
\left ( \sum_{j=1}^n |\underline{a}^i_j |^p \right )^{\frac{1}{p}}
$$
where $1 \leq p < \infty$.
In other words, we take $\ell_p$-norms of all row vectors and then find the maximum.

We define 

$$
\| \bA \|_{\infty, \infty} = \underset{i, j}{\max} |a_{i j}|. 
$$
This is equivalent to taking $\ell_{\infty}$ norm on each row and then taking
the maximum of all the norms.

For $1 \leq p , q < \infty$, we define the norm

$$
\| \bA \|_{p, q} 
\triangleq \left [ \sum_{i=1}^m 
\left ( \| \underline{\ba}^i \|_p \right )^q \right ]^{\frac{1}{q}}.
$$
In other words, we compute $\ell_p$-norm of all the row vectors to form another vector
and then take $\ell_q$-norm of that vector.
````

```{div}
Note that the norm $\| \bA \|_{p, \infty}$ 
is different from the operator norm $\| \bA \|_{p \to \infty}$.
Similarly $\| \bA \|_{p, q}$ is different from $\| \bA \|_{p \to q}$.
````

````{prf:theorem}
:label: res:row_col_norm_p_infty_norm

$$
\| \bA \|_{p, \infty}  = \| \bA \|_{q \to \infty}
$$
where 

$$
\frac{1}{p} + \frac{1}{q} = 1.
$$
````
````{prf:proof}
From {prf:ref}`res:mat:p_to_infty_operator_norm` we get

$$
\| \bA \|_{q \to \infty} = \underset{1 \leq i \leq m}{\max}\| \underline{\ba}^i \|_p.
$$
This is exactly the definition of $\| \bA \|_{p, \infty}$.
````


````{prf:theorem}
:label: res:row_col_norm_1_p_norm

$$
\| \bA \|_{1 \to p} = \| \bA^H \|_{p, \infty}. 
$$
````
````{prf:proof}
We note that:

$$
\| \bA \|_{1 \to p} = \| \bA^H \|_{q \to \infty}.
$$
From {prf:ref}`res:row_col_norm_p_infty_norm`

$$
\| \bA^H \|_{q \to \infty} = \| \bA^H \|_{p, \infty}.
$$
````

````{prf:theorem}
:label: res:mat:consistency_p_infty_row_col_norm

For any two matrices $\bA, \bB$, we have

$$
\frac{\| \bA \bB \|_{p, \infty}}{\| \bB \|_{p, \infty}} 
\leq \| \bA \|_{\infty \to \infty}.
$$
````
````{prf:proof}
Let $q$ be such that $\frac{1}{p} + \frac{1}{q} = 1$.

1. From {prf:ref}`res:mat:p_infty_norm_consistency`, we have

    $$
        \| \bA \bB \|_{q \to \infty} \leq 
        \| \bA \|_{\infty \to \infty} \| \bB \|_{q \to \infty}.
    $$
1. From {prf:ref}`res:row_col_norm_p_infty_norm`

    $$
    \| \bA \bB \|_{q \to \infty} = \| \bA \bB\|_{p, \infty}
    $$
    and 

    $$
    \| \bB \|_{q \to \infty} = \| \bB \|_{p, \infty}.
    $$
1. Thus

    $$
    \| \bA \bB\|_{p, \infty} \leq \| \bA \|_{\infty \to \infty} \| \bB \|_{p, \infty}.
    $$
````


````{prf:theorem} Relations between $(p,q)$ and $(p \to q)$ norms
:label: res:mat:p_q_p_to_q_relations

Relations between $(p, q)$ norms and $(p \to q)$ norms

$$
\| \bA \|_{1, \infty}  = \| \bA \|_{\infty \to \infty}.
$$

$$
\| \bA \|_{2, \infty}  = \| \bA \|_{2 \to \infty}.
$$

$$
\| \bA \|_{\infty, \infty}  = \| \bA \|_{1 \to \infty}.
$$

$$
\| \bA \|_{1 \to 1} = \| \bA^H \|_{1, \infty}.
$$

$$
\| \bA \|_{1 \to 2} = \| \bA^H \|_{2, \infty}
$$
````
````{prf:proof}
The first three are straight forward applications of
{prf:ref}`res:row_col_norm_p_infty_norm`.
The next two are applications of {prf:ref}`res:row_col_norm_1_p_norm`.
See also {numref}`tbl:mat:calculation_p_q_operator_norms`.
````

## Block Diagonally Dominant Matrices and Generalized Gershgorin Circle Theorem


In {cite}`feingold1962block` the idea of diagonally dominant matrices
(see {ref}`sec:mat:diagonally_dominant_matrix`)
has been generalized to block matrices using matrix norms.
We consider the specific case with spectral norm. 

````{prf:definition} Block diagonally dominant matrix
:label: def:mat:block_diagonally_dominant_matrix

Let $\bA$ be a square matrix in $\CC^{n \times n}$ which is partitioned in following manner

$$
\bA = \begin{bmatrix}
\bA_{11} & \bA_{12} & \dots & \bA_{1 k}\\
\bA_{21} & \bA_{22} & \dots & \bA_{2 k}\\
\vdots & \vdots & \ddots & \vdots\\
\bA_{k 1} & \bA_{k 2} & \dots & \bA_{k k}\\
\end{bmatrix}
$$
where each of the submatrices $\bA_{i j}$
is a square matrix of size $m \times m$.
Thus $n = k m $.

$\bA$ is called *block diagonally dominant* if 

$$
\| \bA_{ii}\|_2 \geq \sum_{j, j \neq i } \|\bA_{i j} \|_2. 
$$
holds true for all $1 \leq i \leq k$.

If the inequality satisfies strictly for all $i$, then $\bA$ is called
*block strictly diagonally dominant matrix*.
````

````{prf:theorem} Nonsingularity of block strictly diagonally dominant matrices
:label: thm:mat:block_diagonally_dominant_matrix_nonsingular

If the partitioned matrix $\bA$ of {prf:ref}`def:mat:block_diagonally_dominant_matrix` is
block strictly diagonally dominant matrix, then it is nonsingular. 
````
For proof see {cite}`feingold1962block`.

This leads to the generalized Gershgorin disc theorem.

````{prf:theorem} Generalized Gershgorin disc theorem
:label: thm:block_gershgorin_disc_theorem

Let $\bA$ be a square matrix in $\CC^{n \times n}$
which is partitioned in following manner

$$
\bA = \begin{bmatrix}
\bA_{11} & \bA_{12} & \dots & \bA_{1 k}\\
\bA_{21} & \bA_{22} & \dots & \bA_{2 k}\\
\vdots & \vdots & \ddots & \vdots\\
\bA_{k 1} & \bA_{k 2} & \dots & \bA_{k k}\\
\end{bmatrix}
$$
where each of the submatrices $\bA_{i j}$
is a square matrix of size $m \times m$.

Then each eigenvalue $\lambda$ of $\bA$ satisfies 

$$
\| \lambda \bI  - \bA_{ii}\|_2 
\leq \sum_{j, j\neq i} \|\bA_{ij} \|_2 \text{ for some } i \in \{1,2, \dots, k\}.
$$
````
For proof see {cite}`feingold1962block`.


Since the $2$-norm of a positive semidefinite matrix
is nothing but its largest eigen value, the theorem
directly leads to the following result.

````{prf:corollary} $2$ norm of a Hermitian positive semidefinite matrix
:label: col:block_gershgorin_disc_theorem_psd_matrix

Let $\bA$ be a Hermitian positive semidefinite matrix. 
Let $\bA$ be partitioned as in {prf:ref}`thm:block_gershgorin_disc_theorem`. 
Then its $2$-norm  $\| \bA \|_2$ satisfies

$$
\left | \| \bA \|_2  - \| \bA_{ii}\|_2 \right | 
\leq \sum_{j, j\neq i} \|\bA_{i j} \|_2 \text{ for some } i \in \{1,2, \dots, k \}.
$$
````

