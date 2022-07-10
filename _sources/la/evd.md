(sec:la:evd)=
# Eigen Values

In this subsection, we discuss the eigenvalues and eigenvectors of square matrices.
Much of the discussion in this section will be equally applicable to real
as well as complex square matrices. We will use the complex notation mostly and
make specific remarks for real matrices wherever needed.
Of specific interest is the eigenvalue decomposition of real symmetric matrices.

## Eigen Values

````{prf:definition} Eigen value
:label: def:mat:eigen_value

A scalar $\lambda$ is an *eigen value* of an $n \times n$ matrix $\bA = [ a_{i j} ]$
if there exists a nonzero vector $\bx$ such that

```{math}
:label: eq:mat:eigen_value
\bA \bx = \lambda \bx.
```

A nonzero vector $\bx$ which satisfies this equation is called an *eigen vector*
of $\bA$ for the eigen value $\lambda$.

An eigen value is also known as a *characteristic value*, *proper value*
or a *latent value*.
````

We note that {eq}`eq:mat:eigen_value` can be written as

$$
\bA \bx  = \lambda \bI_n \bx \iff  (\bA - \lambda \bI_n) \bx  = \bzero.
$$
Thus $\lambda$ is an eigen value of $\bA$ if and only if the matrix $\bA - \lambda \bI$
is singular.

````{prf:definition} Spectrum of eigen values
:label: def:mat:spectrum

The set comprising of eigen values of a matrix $\bA$ is known as its *spectrum*.
````

````{prf:remark} Uniqueness of eigen value for an eigen vector
:label: res-mat-unique-ev-ev

For each eigen vector $\bx$ for a matrix $\bA$, the corresponding eigen value $\lambda$ is
unique.
````
````{prf:proof}
We show this by contradiction.

1. Assume that for $\bx$ there are two eigen values $\lambda_1$ and $\lambda_2$.
1. Then
   
   $$
   \bA \bx = \lambda_1 \bx = \lambda_2 \bx 
   \implies (\lambda_1 - \lambda_2 ) \bx = \bzero.
   $$
1. This can happen only when either $\bx = \bzero$ or $\lambda_1 = \lambda_2$.
1. Since $\bx$ is an eigen vector, it cannot be $\bzero$.
1. Thus $\lambda_1 = \lambda_2$.
````

````{prf:remark}
:label: res-mat-eval-from-evec

If $\bx$ is an eigen vector for $\bA$, then the corresponding eigen value is given by

$$
\lambda = \frac{\bx^H \bA \bx }{\bx^H \bx}.
$$
````
````{prf:proof}
We proceed as follows:

$$
\bA \bx = \lambda \bx 
\implies \bx^H \bA \bx = \lambda \bx^H \bx 
\implies \lambda = \frac{\bx^H \bA \bx }{\bx^H \bx}.
$$
since $\bx$ is nonzero.
````

````{prf:remark}
:label: res-mat-evec-nullspace

An eigen vector $\bx$ of $\bA$ for eigen value $\lambda$
belongs to the nullspace of $\bA - \lambda \bI$;
i.e.,

$$
\bx \in \NullSpace(\bA - \lambda \bI).
$$
In other words $\bx$ is a nontrivial solution
to the homogeneous system of linear equations given by

$$
(\bA - \lambda \bI) \bz = \bzero.
$$
````

We can put together eigen vectors of a matrix into another matrix by itself. This
can be very useful tool. We start with a simple idea.

````{prf:lemma} Matrix of eigen vectors
:label: res-mat-evec-mat

Let $\bA$ be an $n \times n$ matrix.
Let $\bu_1, \bu_2, \dots, \bu_r$ be $r$ nonzero vectors from $\FF^n$.
Let us construct an $n \times r$ matrix

$$
\bU = \begin{bmatrix} \bu_1 & \bu_2 & \dots & \bu_r \end{bmatrix}.
$$
Then all the $r$ vectors are eigen vectors of $\bA$ if and only if
there exists a diagonal matrix $\bD = \Diag(d_1, \dots, d_r)$ such that

$$
\bA \bU  = \bU \bD.
$$
````
````{prf:proof}
Expanding the equation, we can write

$$
\begin{bmatrix} \bA \bu_1 & \bA \bu_2 & \dots & \bA \bu_r \end{bmatrix}
=
\begin{bmatrix} d_1 \bu_1 & d_2 \bu_2 & \dots & d_r \bu_r \end{bmatrix}.
$$
Clearly we want

$$
\bA \bu_i = d_i \bu_i
$$
where $\bu_i$ are nonzero.
This is possible only when $d_i$ is an eigen value of $\bA$ and $\bu_i$ is
an eigen vector for $d_i$.

Converse: Assume that $\bu_i$ are eigen vectors. Choose $d_i$ to be
corresponding eigen values. Then the equation holds. 
````
This idea will be extended further in building the eigen value
decomposition of matrices.

````{prf:observation}
:label: rem-mat-eval-ax-x-angle

Let $\bA \in \RR^{n \times n}$.
Let $\lambda$ be a nonzero real eigen value of $\bA$
and $\bx \in \RR^n$ be an eigenvector of $\bA$ for $\lambda$.
Then $\bA \bx$ and $\bx$ are collinear.

In other words the angle between $\bA \bx$ and $\bx$ is either $0^{\circ}$ 
when $\lambda$ is positive and is $180^{\circ}$ when $\lambda$ is
negative. Let us look at the inner product:

$$
\langle \bA \bx, \bx \rangle = \bx^T \bA \bx = \bx^H \lambda \bx = \lambda \| \bx\|_2^2.
$$
Meanwhile

$$
\| \bA \bx \|_2 = \| \lambda \bx \|_2 = |\lambda| \| \bx \|_2. 
$$
Thus

$$
|\langle \bA \bx, \bx \rangle |  = \| \bA \bx \|_2 \| \bx \|_2.
$$
The angle $\theta$ between $\bA \bx$ and $\bx$ is given by

$$
\cos \theta = \frac{\langle \bA \bx, \bx \rangle}{\| \bA \bx \|_2 \| \bx \|_2} 
= \frac{\lambda \| \bx \|_2^2}{|\lambda| \| \bx \|_2^2} = \pm 1.
$$
````

## Eigen Space

````{prf:definition} Eigen space
:label: def:mat:eigen_space

Let $\lambda$ be an eigen value for a square matrix $\bA$.
Then its *eigen space* is the nullspace of $\bA - \lambda \bI$
i.e. $\NullSpace(\bA - \lambda \bI)$. 
````

````{prf:remark} Eigen vectors for an eigen value
:label: res-mat-evecs-for-eval

The set comprising all the eigen vectors of $\bA$ for an
eigen value $\lambda$ is given by

$$
\NullSpace(\bA - \lambda \bI) \setminus \{ \bzero \}
$$
since $\bzero$ cannot be an eigen vector.
````

````{prf:definition} Geometric multiplicity
:label: def:mat:eigen:geometric_multiplicity

Let $\lambda$ be an eigen value for a square matrix $\bA$. 
The dimension of its eigen space $\NullSpace(\bA - \lambda \bI)$
is known as the *geometric multiplicity* of the eigen value $\lambda$.
````

We can see that

```{math}
:label: eq-mat-rank-nullity-eigenspace
\dim (\NullSpace(\bA - \lambda \bI)) = n - \Rank(\bA - \lambda \bI).
```

## Characteristic Polynomial

````{prf:remark} Singularity of $\bA - \lambda \bI$
:label: res-mat-singular-a-min-ev-i

A scalar $\lambda$ can be an eigen value of a square matrix $\bA$
if and only if

$$
\det (\bA - \lambda \bI) = 0.
$$
````
$\det (\bA - \lambda \bI)$ is a polynomial in $\lambda$ of degree $n$.

````{prf:observation} Eigenvalues as zeros of a polynomial
:label: res-mat-evals-zeros-polynomial

We can write the determinant as a polynomial:

$$
\det (\bA - \lambda \bI) 
= p(\lambda) = \alpha^n \lambda^n + \alpha^{n-1} \lambda^{n-1} + \dots 
+ \alpha^1 \lambda + \alpha_0
$$
where $\alpha_i$ depend on entries in $\bA$.
In this sense, an eigenvalue of $\bA$ is a root of the equation

$$
p(\lambda) = 0.
$$
It is easy to show that $\alpha^n = (-1)^n$.
````

````{prf:definition} Characteristic polynomial
:label: def:mat:characteristic_polynomial

For any square matrix $\bA$, the polynomial given by

$$
p(\lambda) = \det(\bA - \lambda \bI)
$$
is known as its *characteristic polynomial*.
The equation give by

$$
p(\lambda) = 0
$$
is known as its *characteristic equation*.
The eigen values of $\bA$ are the roots of its characteristic polynomial or
solutions of its characteristic equation.
````

````{prf:observation} Factors of characteristic polynomial
:label: res-mat-factors-charac-poly

For real square matrices, if we restrict eigen values to real values, then 
the characteristic polynomial can be factored as

```{math}
:label: eq-mat-eig-charac-poly-real-factors
p(\lambda) = (-1)^n (\lambda - \lambda_1)^{r_1} \dots (\lambda - \lambda_k)^{r_k} q(\lambda).
```
The polynomial has $k$ distinct real roots.
For each root $\lambda_i$, $r_i$ is a positive
integer indicating how many times the root appears.
$q(\lambda)$ is a polynomial that has no real roots.
The following is true

$$
r_1 + \dots + r_k + \mathrm{deg}(q(\lambda)) = n.
$$
Clearly $k \leq n$.

For complex square matrices where eigen values can be complex (including real square matrices),
the characteristic polynomial can be factored as

```{math}
:label: eq-mat-eig-charac-poly-complex-factors
p(\lambda) = (-1)^n (\lambda - \lambda_1)^{r_1} \dots (\lambda - \lambda_k)^{r_k}.
```
The polynomial can be completely factorized into first degree polynomials.
There are $k$ distinct roots or eigen values. The following is true

$$
r_1 + \dots + r_k = n.
$$
Thus, including the duplicates there are exactly $n$ eigen values for a complex square matrix.
````
It is quite possible that a real square matrix doesn't have any real eigen values.

````{prf:definition} Algebraic multiplicity
:label: def:mat:eigen:algebraic_multiplicity

The number of times an eigen value appears in the factorization of the characteristic polynomial
of a square matrix $\bA$ is known as its *algebraic multiplicity*.
In other words,
$r_i$ is the algebraic multiplicity for $\lambda_i$ in the factorization
{eq}`eq-mat-eig-charac-poly-real-factors`
and {eq}`eq-mat-eig-charac-poly-complex-factors`.
````

````{prf:theorem} Geometric and algebraic multiplicities
:label: thm:mat:eig_geometric_algebraic_multiplicity

Let $\lambda$ be an eigen value of a square matrix $\bA$.
Then the geometric multiplicity 
of $\lambda$ is less than or equal to its algebraic multiplicity.
````

````{prf:corollary} Distinct eigen values and multiplicity
:label: res-mat-eig-distinct-multiplicity

If an $n \times n$ matrix $\bA$ has $n$ distinct eigen values,
then each of them has a geometric (and algebraic) multiplicity of $1$. 
````
````{prf:proof}
The algebraic multiplicity of an eigen value is greater than or equal to 1.
But the sum cannot exceed $n$.
Since there are $n$ distinct eigen values,
thus each of them has algebraic multiplicity of $1$.
Further, geometric multiplicity of an eigen value is greater than equal to 1
and less than equal to its algebraic multiplicity. 
````

````{prf:corollary}
:label: res-mat-eig-alg-geom-mult-2

Let an $n \times n$ matrix $\bA$ has $k$ distinct eigen values
$\lambda_1, \lambda_2, \dots, \lambda_k$ 
with algebraic multiplicities 
$r_1, r_2, \dots, r_k$
and geometric multiplicities $g_1, g_2, \dots g_k$ 
respectively.
Then

$$
\sum_{i=1}^k g_k \leq \sum_{i=1}^k r_k \leq n. 
$$
Moreover if

$$
\sum_{i=1}^k g_i = \sum_{i=1}^k r_i
$$
then

$$
g_i = r_i \Forall i=1,\dots,k.
$$
````

````{prf:remark} Spectrum from roots of characteristic polynomial
:label: res-mat-charac-roots-spectrum

In the factorization {eq}`eq-mat-eig-charac-poly-complex-factors`
of the characteristic polynomial $p(\lambda)$,
the set $\{\lambda_1, \dots, \lambda_k\}$ forms the spectrum of $\bA$.
````

Let us consider the sum of $r_i$ which gives the count of total number of roots
of $p(\lambda)$.

$$
m = \sum_{i=1}^k r_i.
$$
With this there are $m$ not-necessarily distinct roots of $p(\lambda)$. 
Let us write $p(\lambda)$ from {eq}`eq-mat-eig-charac-poly-real-factors` as

$$
p(\lambda) = (-1)^n (\lambda - c_1) (\lambda - c_2)\dots (\lambda - c_m)q(\lambda).
$$
where $c_1, c_2, \dots, c_m$ are $m$ scalars (not necessarily distinct) of which
$r_1$ scalars are $\lambda_1$, $r_2$ are $\lambda_2$ and so on.
For the complex case, we have $q(\lambda)=1$.

We will refer to the set (allowing repetitions) 
$\{c_1, c_2, \dots, c_m \}$ as the eigen values of the
matrix $\bA$ where $c_i$ are not necessarily distinct.
In contrast the spectrum of $\bA$ refers to the set of distinct eigen values of $\bA$.
The symbol $c$ has been chosen based on the other name for eigen values
(the characteristic values).


## The Zero Eigen Value

````{prf:lemma} $0$ as an eigen value
:label: res-mat-0-ev

$0$ is an eigen value of a square matrix $\bA$ if and only if $\bA$ is singular.
````
````{prf:proof}
Let $0$ be an eigen value of $\bA$.
1. Then there exists $\bu \neq \bzero$ such that
   
   $$
   \bA \bu = 0 \bu = \bzero.
   $$
1. Thus $\bu$ is a non-trivial solution of the homogeneous linear system $\bA \bx = \bzero$.
1. Thus $\bA$ is singular.

Converse:
1. Assume that $\bA$ is singular.
1. Then there exists $\bu \neq \bzero$ s.t.
   
   $$
   \bA \bu = \bzero = 0 \bu.
   $$
1. Thus $0$ is an eigen value of $\bA$.
````

````{prf:lemma} Eigenspace of the zero eigen value
:label: res-mat-0-eval-eigenspace

If a square matrix $\bA$ is singular,
then $\NullSpace(\bA)$ is the eigen space for the eigen value $\lambda = 0$.
````
````{prf:proof}
This is straight forward from the definition of eigen space (see {prf:ref}`def:mat:eigen_space`).
````

````{prf:remark}
:label: res-mat-0-eval-geometric-multiplicity

Clearly the geometric multiplicity of $\lambda=0$ equals $\Nullity(\bA) = n  - \Rank(\bA)$.
````

## Transpose

````{prf:lemma} Eigen values of the transpose
:label: res-mat-eval-transpose

Let $\bA$ be a square matrix. Then $\bA$ and $\bA^T$ have same eigen values.
````
````{prf:proof}
The eigen values of $\bA^T$ are given by 

$$
\det (\bA^T - \lambda \bI) = 0.
$$
But

$$
\bA^T - \lambda \bI = \bA^T - (\lambda \bI )^T = (\bA - \lambda \bI)^T.
$$
Hence (using {prf:ref}`lem:mat:determinant_transpose_rule`)

$$
\det (\bA^T - \lambda \bI)
= \det \left (  (\bA - \lambda \bI)^T \right )
= \det (\bA - \lambda \bI).
$$
Thus the characteristic polynomials of $\bA$ and $\bA^T$ are same.
Hence the eigen values are same.
In other words the spectrum of $\bA$ and $\bA^T$ are same.
````


## Powers and Inverses

````{prf:lemma} Power rule
:label: lem:mat:eigen:power_rule

Let $\bA$ be a square matrix and $\lambda$ be an eigen value of $\bA$.
Let $p \in \Nat$. Then $\lambda^p$ is an eigen value of $\bA^{p}$.
````
````{prf:proof}
We prove this by mathematical induction.

1. For $p=1$ the statement holds trivially since $\lambda^1$ is an eigen value of $\bA^1$.
1. Assume that the statement holds for some value of $p$.
1. Thus let $\lambda^p$ be an eigen
   value of $\bA^{p}$ and let $\bu$ be corresponding eigen vector.
1. Now
   
   $$
   \bA^{p + 1} \bu 
   = \bA^p ( \bA \bu) = \bA^{p} \lambda \bu  = \lambda \bA^{p} \bu 
   = \lambda \lambda^p \bu 
   = \lambda^{p + 1} \bu.
   $$
1. Thus $\lambda^{p + 1}$ is an eigen value for $\bA^{p + 1}$
   with the same eigen vector $\bu$.
1. With the principle of mathematical induction, the proof is complete.
````

````{prf:lemma} Eigenvalue of the inverse
:label: res-mat-inverse-eval

Let a square matrix $\bA$ be non singular and
let $\lambda \neq 0$ be some eigen value of $\bA$.
Then $\lambda^{-1}$ is an eigen value of $\bA^{-1}$.
Moreover, all eigen values of $\bA^{-1}$ are obtained
by taking inverses of eigen values of $\bA$;
i.e., if $\mu \neq 0$ is an eigen value of $\bA^{-1}$
then $\frac{1}{\mu}$ is an eigen value of $\bA$ also.
Also, $\bA$ and $\bA^{-1}$ share the same set of eigen vectors.
````
````{prf:proof}
Since $\bA$ is invertible, hence all its eigenvalues are nonzero.

1. Let $\bu \neq \bzero$ be an eigen vector of $\bA$ for the eigen value $\lambda$.
1. Then
   
   $$
   \bA \bu = \lambda \bu 
   \implies \bu = \bA^{-1} \lambda \bu 
   \implies \frac{1}{\lambda} \bu = \bA^{-1} \bu.
   $$
1. Thus $\bu$ is also an eigen vector of $\bA^{-1}$
   for the eigen value $\frac{1}{\lambda}$.
1. Now let $\bB = \bA^{-1}$.
1. Then $\bB^{-1} = \bA$.
1. Thus if $\mu$ is an eigen value of $\bB$
   then $\frac{1}{\mu}$ is an eigen value of $\bB^{-1} = \bA$. 
1. Thus if $\bA$ is invertible then eigen values of
   $\bA$ and $\bA^{-1}$ have one to one correspondence (being reciprocal).
````

## Invariant Subspaces
````{prf:definition} Invariant subspace
:label: def:mat:invariant_subspace

Let $\bA$ be a square $n\times n$ matrix and let $\WW$ be a linear subspace
of $\FF^n$.
Then $\WW$ is *invariant* relative
to $\bA$ if 

$$
\bA \bw \in \WW \Forall \bw \in \WW.
$$
In other words, $\bA (\WW) \subseteq \WW$
or for every vector $\bw \in \WW$ its mapping
$\bA \bw$ is also in $\WW$.
Thus action of $\bA$ on $\WW$ doesn't take us outside of $\WW$.

We also say that $\WW$ is $\bA$-*invariant*.
````
Eigen vectors are generators of invariant subspaces. 

````{prf:lemma} Spans of eigenvectors are invariant
:label: lem:mat:span_of_eigenvectors_invariant

Let $\bA$ be an $n \times n$ matrix.
Let $\bx_1, \bx_2, \dots, \bx_r$ be $r$ eigen vectors of $\bA$. 
Let us construct an $n \times r$ matrix

$$
\bX = \begin{bmatrix} \bx_1 & \bx_2 & \dots & \bx_r \end{bmatrix}.
$$
Then the column space of $\bX$;
i.e., $\ColSpace(\bX)$ is invariant relative to $\bA$.
````
````{prf:proof}
Let us assume that $c_1, c_2, \dots, c_r$ are the eigen values
corresponding to $\bx_1, \bx_2, \dots, \bx_r$ (not necessarily distinct).

Let any vector $\bx \in \ColSpace(\bX)$ be given by

$$
\bx = \sum_{i=1}^r \alpha_i \bx_i.
$$
Then 

$$
\bA \bx =  \bA \sum_{i=1}^r \alpha_i \bx_i 
= \sum_{i=1}^r \alpha_i \bA \bx_i 
= \sum_{i=1}^r \alpha_i c_i \bx_i.
$$
Clearly $\bA \bx$ is also a linear combination of $\bx_i$.
Hence it belongs to $\ColSpace(\bX)$.
Thus $\ColSpace(\bX)$ is invariant relative to $\bA$
or $\ColSpace(\bX)$ is $\bA$-invariant.
````

## Triangular Matrices
````{prf:lemma} Eigenvalues of triangular matrices
:label: lem:mat:eig:triangular_matrix_diagonal

Let $\bA$ be an $n\times n$ upper or lower triangular matrix.
Then its eigen values are the entries on its main diagonal.
````
````{prf:proof}
We are given that $\bA$ is triangular.
1. Then $\bA - \lambda \bI$ is also triangular
   with its diagonal entries being $(a_{i i} - \lambda)$.
1. Using  {prf:ref}`lem:determinant_triangular_matrix_rule`,
   we have
   
   $$
   p(\lambda) = \det (\bA - \lambda \bI) 
   = \prod_{i=1}^n (a_{i i} - \lambda).
   $$
1. Clearly the roots of characteristic polynomial are $a_{i i}$.
````
Several small results follow from this lemma.

````{prf:corollary} Eigenvalues of triangular matrices
:label: lem:mat:eig:triangular_matrix_diagonal-2

Let $\bA = [a_{i j}]$ be an $n \times n$ triangular matrix.

*  The characteristic polynomial of $\bA$ is 
   
   $$
   p(\lambda) = (-1)^n (\lambda - a_{i i}).
   $$
*  A scalar $\lambda$ is an eigen value of $\bA$
   iff it is one of the diagonal entries of $\bA$.
*  The algebraic multiplicity of an eigen value $\lambda$
   is equal to the number of times
   it appears on the main diagonal of $\bA$.
*  The spectrum of $\bA$ is given by the distinct entries
   on the main diagonal of $\bA$. 
````

A diagonal matrix is naturally both an upper triangular matrix
as well as a lower triangular matrix.
Similar results hold for the eigen values of a diagonal matrix also.

````{prf:lemma} Eigenvalues of diagonal matrices
:label: lem:mat:eig:diagonal_matrix_diagonal

Let $\bA = [a_{i j}]$ be an $n \times n$ diagonal matrix.

*  Its eigen values are the entries on its main diagonal.
*  The characteristic polynomial of $\bA$ is 
   
   $$
   p(\lambda) = (-1)^n (\lambda - a_{i i}).
   $$
*  A scalar $\lambda$ is an eigen value of $\bA$
   iff it is one of the diagonal entries of $A$.
*  The algebraic multiplicity of an eigen value $\lambda$
   is equal to the number of times
   it appears on the main diagonal of $\bA$.
*  The spectrum of $\bA$ is given by the distinct entries
   on the main diagonal of $\bA$. 
````

There is also a result for the geometric multiplicity of eigen values
for a diagonal matrix.

````{prf:lemma} Geometric multiplicity of eigenvalues for diagonal matrices
:label: res-mat-diagonal-mat-eval-geom-mult

Let $\bA = [a_{i j}]$ be an $n \times n$ diagonal matrix.
The geometric multiplicity of an eigen value $\lambda$
is equal to the number of times
it appears on the main diagonal of $\bA$.
````
````{prf:proof}
The unit vectors $\be_i$ are eigen vectors for $\bA$ since

$$
\bA \be_i = a_{i i } \be_i.
$$
1. They are linearly independent.
1. Thus if a particular eigen value appears $r$ number of times, then
   there are $r$ linearly independent eigen vectors for the eigen value.
1. Thus its geometric multiplicity is equal to the algebraic multiplicity.
````

## Similar Matrices
Some very useful results are available for similar matrices.

````{prf:lemma} Characteristic polynomial of similar matrices
:label: lem:mat:eig:simlar_matrix_spectrum

The characteristic polynomial and spectrum of similar matrices is same.
````
````{prf:proof}
Let $\bB$ be similar to $\bA$.

1. Then there exists an invertible matrix $\bC$ such that

   $$
   \bB   = \bC^{-1} \bA \bC.
   $$
1. Now
   
   $$
   \bB - \lambda \bI 
   &= \bC^{-1} \bA \bC - \lambda \bI \\
   &= \bC^{-1} \bA \bC - \lambda \bC^{-1} \bC \\
   &=  \bC^{-1}  ( \bA \bC - \lambda \bC) \\
   &=  \bC^{-1} (\bA - \lambda \bI) \bC.
   $$
1. Thus $\bB - \lambda \bI$ is similar to $\bA - \lambda \bI$.
1. Hence due to 
   {prf:ref}`lem:determinant_simlar_matrix_rule`,
   their determinant is equal. 
1. In other words,

   $$
   \det(\bB - \lambda \bI ) = \det (\bA - \lambda \bI).
   $$
1. This means that the characteristic polynomials of $\bA$ and $\bB$ are same.
1. Since eigen values are nothing but
   roots of the characteristic polynomial,
   hence they are same too.
1. This means that the spectrum (the set of
   distinct eigen values) is same.
````
This result is very useful. Since if it can be shown that a matrix $\bA$
is similar to a diagonal or a triangular matrix whose eigen values are easy
to obtain then determination of the eigen values of $\bA$ becomes straight forward.

````{prf:corollary} Eigenvalues of similar matrices
:label: lem:mat:eig:evals-similar-mat

If $\bA$ and $\bB$ are similar to each other then

*  An eigen value has same algebraic and geometric multiplicity
   for both $\bA$ and $\bB$.
*  The (not necessarily distinct) eigen values of $\bA$ and $\bB$ are same.
````
Although the eigen values are same, but the eigen vectors are different.

````{prf:lemma} Eigenvectors of similar matrices
:label: lem:mat:eig:similar_matrix_eigen_value

Let $\bA$ and $\bB$ be similar with 

$$
\bB   = \bC^{-1} \bA \bC
$$
for some invertible matrix $\bC$.
If $\bu$ is an eigenvector of $\bA$
for an eigenvalue $\lambda$,
then $C^{-1} \bu$ 
is an eigen vector of $\bB$ for the same eigen value.
````
````{prf:proof}
We are given that $\bu$ is an eigen vector of $\bA$
for an eigen value $\lambda$.

1. Thus we have
   
   $$
    \bA \bu  = \lambda \bu.
   $$
1. Thus
   
   $$
   \bB \bC^{-1} \bu  
   = \bC^{-1} \bA \bC  \bC^{-1} \bu 
   = \bC^{-1} \bA \bu 
   = \bC^{-1} \lambda \bu = \lambda \bC^{-1} \bu.
   $$
1. Now $\bu \neq \bzero$ and $\bC^{-1}$ is non singular.
1. Thus $\bC^{-1} \bu \neq \bzero$.
1. Thus $\bC^{-1} \bu$ is an eigen vector of $\bB$.
````


## Linear Independence of Eigenvectors

````{prf:theorem} Linear independence of eigenvectors with distinct eigenvalues
:label: thm:mat:eig:independence_distinc_eigen_values

Let $\bA$ be an $n\times n$ square matrix.
Let $\bx_1, \bx_2, \dots , \bx_k$ be any $k$ eigen vectors
of $A$ for distinct eigen values 
$\lambda_1, \lambda_2, \dots, \lambda_k$ respectively.
Then $\bx_1, \bx_2, \dots , \bx_k$  are linearly independent.
````
````{prf:proof}
We first prove the simpler case with 2 eigen vectors
$\bx_1$ and $\bx_2$ and corresponding eigen values
$\lambda_1$ and $\lambda_2$ respectively.

1. Let there be a linear relationship between $\bx_1$ and $\bx_2$ given by

   $$
   \alpha_1 \bx_1 + \alpha_2 \bx_2 = \bzero.
   $$
1. Multiplying both sides with $(\bA - \lambda_1 \bI)$ we get
   
   $$
   & \alpha_1 (\bA - \lambda_1 \bI) \bx_1 
   + \alpha_2(\bA - \lambda_1 \bI) \bx_2  = \bzero\\
   \implies & \alpha_1 (\lambda_1 - \lambda_1) \bx_1 
   + \alpha_2(\lambda_2  - \lambda_1) \bx_2 = \bzero \\
   \implies & \alpha_2(\lambda_2 - \lambda_1) \bx_2 = \bzero.
   $$
1. Since $\lambda_1 \neq \lambda_2$ and $\bx_2 \neq \bzero$,
   hence $\alpha_2 = 0$.
1. Similarly by multiplying with $(\bA - \lambda_2 \bI)$
   on both sides, we can show that $\alpha_1 = 0$.
1. Thus $\bx_1$ and $\bx_2$ are linearly independent. 
1. Now for the general case, consider a linear relationship
   between $\bx_1, \bx_2, \dots , \bx_k$  given by
   
   $$
   \alpha_1 \bx_1 + \alpha_2 \bx_2 + \dots \alpha_k \bx_k = \bzero.
   $$
1. Multiplying by
   $\prod_{i \neq j, i=1}^k (\bA - \lambda_i \bI)$
   and using the fact that $\lambda_i \neq \lambda_j$ if $i \neq j$, 
   we get $\alpha_j = 0$.
1. Thus the only linear relationship is the trivial relationship.
1. This completes the proof.
````

For eigen values with geometric multiplicity greater than $1$
there are multiple eigenvectors corresponding
to the eigen value which are linearly independent.
In this context, above theorem can be generalized further.

````{prf:theorem} Linear independence of eigenvectors from different eigen spaces
:label: thm:mat:eig:independence_distinc_eigen_values_general

Let $\lambda_1, \lambda_2, \dots, \lambda_k$ be $k$ distinct eigen values of $\bA$. 
Let $\{\bx_1^j, \bx_2^j, \dots \bx_{g_j}^j\}$
be any $\bg_j$ linearly independent eigen vectors from 
the eigen space of $\lambda_j$
where $g_j$ is the geometric multiplicity of $\lambda_j$. 
Then the combined set of eigen vectors given by

$$
\{\bx_1^1, \dots, \bx_{g_1}^1, 
\dots, \bx_1^k, \dots, \bx_{g_k}^k\}
$$
consisting of $\sum_{j=1}^k g_j$ 
eigen vectors is linearly independent.
````
This result puts an upper limit on the number of
linearly independent eigen vectors of a square matrix.

````{prf:lemma} Maximum number of linearly independent eigenvectors
:label: res-mat-eig-upper-limit-lin-ind-evecs

Let $\{ \lambda_1, \dots, \lambda_k \}$ represents the spectrum of an
$n \times n$ matrix $\bA$. 
Let $g_1, \dots, g_k$ be the geometric multiplicities of
$\lambda_1, \dots \lambda_k$ respectively.
Then the number of linearly independent eigen vectors for $\bA$ is 

$$
\sum_{i=1}^k g_i.
$$

Moreover if 

$$
\sum_{i=1}^k g_i = n
$$
then a set of $n$ linearly independent eigen vectors of $\bA$
can be found which forms a basis for $\FF^n$.
````
## Diagonalization


Diagonalization is one of the fundamental operations in linear algebra.
This section discusses diagonalization of square matrices in depth.

````{prf:definition} diagonalizable matrix
:label: def:mat:diagonalizable

An $n \times n$ matrix $\bA$ is said to be *diagonalizable*
if it is *similar* to a diagonal matrix.
In other words there exists an
$n\times n$ non-singular matrix $\bP$
such that $\bD = \bP^{-1} \bA \bP$ is a diagonal matrix. 
If this happens then we say that $\bP$ *diagonalizes* $\bA$
or $\bA$ is diagonalized by $\bP$. 
````
````{prf:remark}
:label: rem-mat-diagonalizable-1

$$
\bD =  \bP^{-1} \bA \bP \iff \bP \bD = \bA \bP 
\iff \bP \bD \bP^{-1} = \bA.
$$
````
We note that if we restrict to real matrices, then $\bU$ and $\bD$ should also be real.
If $\bA \in \CC^{n \times n}$ (it may still be real)
then $\bP$ and $\bD$ can be complex.

In other words, if $\bA \in \RR^{n \times n}$ is diagonalizable
then both $\bP$ and $\bD$ must be real.


The next theorem is the culmination of a variety of results studied so far.
````{prf:theorem} Properties of diagonalizable matrices
:label: thm:mat:diagonalizable_matrix_properties

Let $\bA$ be a diagonalizable matrix with $\bD = \bP^{-1} \bA \bP$
being its diagonalization.
Let $\bD =  \Diag(d_1, d_2, \dots, d_n)$.
Then the following hold

*  $\Rank(\bA) = \Rank(\bD)$ which equals the number of nonzero entries
   on the main diagonal of $\bD$.
*  $\det(\bA) = d_1 d_2 \dots d_n$.
*  $\Trace(\bA) = d_1 + d_2 + \dots d_n$.
*  The characteristic polynomial of $\bA$ is
   
   $$
   p(\lambda) = (-1)^n (\lambda - d_1) (\lambda -d_2) \dots (\lambda - d_n).
   $$
*  The spectrum of $\bA$ comprises the distinct scalars
   on the diagonal entries in $\bD$.
*  The (not necessarily distinct) eigenvalues of $\bA$
   are the diagonal elements of $\bD$.
*  The columns of $\bP$ are (linearly independent) eigenvectors of $\bA$. 
*  The algebraic and geometric multiplicities of an eigenvalue $\lambda$ of $\bA$
   equal the number of diagonal elements of $\bD$ that equal $\lambda$.
````

````{prf:proof}
From {prf:ref}`def:mat:diagonalizable` we note that $\bD$ and $\bA$ are similar.

1. Due to {prf:ref}`lem:determinant_simlar_matrix_rule`
   
   $$
    \det(\bA) = \det(\bD).
   $$
1. Due to {prf:ref}`lem:determinant_diagonal_matrix_rule`
   
   $$
    \det(\bD) = \prod_{i=1}^n d_i.
   $$
1. Now due to {prf:ref}`lem:mat:trace_similar_matrices`
   
   $$
    \Trace(\bA) = \Trace(\bD) = \sum_{i=1}^n d_i.
   $$
1. Further due to {prf:ref}`lem:mat:eig:simlar_matrix_spectrum`
   the characteristic polynomial and spectrum of $\bA$ and $\bD$ are same.
1. Due to {prf:ref}`lem:mat:eig:diagonal_matrix_diagonal` the eigen values of $\bD$
   are nothing but its diagonal entries.
1. Hence they are also the eigen values of $\bA$.
1. We recall that

   $$
   \bD = \bP^{-1} \bA \bP \implies \bA \bP = \bP \bD.
   $$
1. Now writing
   
   $$
   \bP  = \begin{bmatrix}
    \bp_1 & \bp_2 & \dots & \bp_n
    \end{bmatrix}
   $$
   we have
   
   $$
   \bA \bP  = \begin{bmatrix}
    \bA \bp_1 & \bA \bp_2 & \dots & \bA \bp_n
    \end{bmatrix}
   =  \bP \bD =
    \begin{bmatrix}
    d_1 \bp_1 & d_2 \bp_2 & \dots & d_n \bp_n
    \end{bmatrix}.
   $$
1. Matching columns, we see that
 
   $$
   \bA \bp_i = d_i \bp_i \Forall i=1,\dots,n.
   $$
1. Thus $\bp_i$ are eigen vectors of $\bA$.
1. Since $\bP$ is invertible, hence its columns are linearly independent.
1. Hence all the eigenvectors of $\bA$ are linearly independent.
1. Since the characteristic polynomials of $\bA$ and $\bD$ are same,
   hence the algebraic multiplicities of eigen values are same. 
1. From {prf:ref}`lem:mat:eig:similar_matrix_eigen_value`
   we get that there is a one to one correspondence between
   the eigen vectors of $\bA$ and $\bD$ through
   the change of basis given by $\bP$.
1. Thus the linear independence relationships
   between the eigen vectors remain the same.
1. Hence the geometric multiplicities
   of individual eigenvalues are also the same.
1. This completes the proof.
````

So far we have verified various results which are available if 
a matrix $\bA$ is diagonalizable. We haven't yet identified the
conditions under which $\bA$ is diagonalizable. We note that
not every matrix is diagonalizable. The following theorem
gives necessary and sufficient conditions under which 
a matrix is diagonalizable. 

````{prf:theorem} Diagonalizability: necessary and sufficient conditions
:label: thm:mat:eig:necessary_condition_diagonalizability

An $n \times n$ matrix $\bA$ is diagonalizable by an $n \times n$
nonsingular matrix
$\bP$ if and only if the columns of $\bP$ are (linearly independent)
eigenvectors of $\bA$.
````
````{prf:proof}
We note that since $\bP$ is nonsingular
hence columns of $\bP$ have to be linearly independent.

The necessary condition part was proven in {prf:ref}`thm:mat:diagonalizable_matrix_properties`.
We now show that if $\bP$ consists of
$n$ linearly independent eigen vectors of $\bA$
then $\bA$ is diagonalizable.

1. Let the columns of $\bP$ be 
   $\bp_1, \bp_2, \dots, \bp_n$
   and corresponding (not necessarily distinct) eigen values
   be $d_1, d_2, \dots , d_n$.
1. Then
   
   $$
   \bA \bp_i = d_i \bp_i.
   $$
1. Thus by letting $\bD = \Diag (d_1, d_2, \dots, d_n)$, we have
   
   $$
   \bA \bP = \bP \bD.
   $$
1. Since columns of $\bP$ are linearly independent,
   hence $\bP$ is invertible.
1. This gives us
   
   $$
   \bD = \bP^{-1} \bA \bP. 
   $$
1. Thus $\bA$ is similar to a diagonal matrix $\bD$.
1. Hence $\bA$ is diagonalizable.
1. This validates the sufficient condition.
````
A corollary follows.

````{prf:corollary} Diagonalizability and linear independence of eigen vectors
:label: res-mat-eig-diagonalizable-lin-ind-evec

An $n \times n$ matrix is diagonalizable if and only if there exists a linearly
independent set of $n$ eigenvectors of $\bA$.
````
Now we know that geometric multiplicities of eigen values of $\bA$
provide us information about the number of
linearly independent eigenvectors of $\bA$. 

````{prf:corollary} Diagonalizability and geometric multiplicities
:label: res-mat-eig-diagonalizable-geom-mult

Let $\bA$ be an $n \times n$ matrix.
Let $\lambda_1, \lambda_2, \dots, \lambda_k$ be
its $k$ distinct eigen values (comprising its spectrum).
Let $g_j$ be the geometric multiplicity of $\lambda_j$.
Then $\bA$ is diagonalizable if and only if

$$
\sum_{i=1}^n g_i = n.
$$
````

## Real Symmetric Matrices
This subsection is focused on real symmetric matrices.

Following is a fundamental property of real symmetric matrices.

````{prf:theorem} Existence of eigenvalues
:label: thm:mat:eig_real_symmetric_eigenvalue_guarantee

Every real symmetric matrix has an eigen value.
````
The proof of this result is beyond the scope of this book.

````{prf:lemma} Orthogonality of eigenvectors for distinct eigenvalues
:label: thm:mat:eig:symmetric_orthogonal

Let $\bA$ be an $n \times n$ real symmetric matrix.
Let $\lambda_1$ and $\lambda_2$ be any two distinct
eigen values of $\bA$ and
let $\bx_1$ and $\bx_2$ be any two corresponding eigen vectors.
Then $\bx_1$ and $\bx_2$ are orthogonal.
````
````{prf:proof}
By definition we have 
$\bA \bx_1 = \lambda_1 \bx_1$ and $\bA \bx_2 = \lambda_2 \bx_2$.
Thus

$$
& \bx_2^T \bA \bx_1 = \lambda_1 \bx_2^T \bx_1\\
\implies & \bx_1^T \bA^T \bx_2 = \lambda_1 \bx_1^T \bx_2 \\
\implies & \bx_1^T \bA \bx_2 = \lambda_1 \bx_1^T \bx_2\\
\implies & \bx_1^T \lambda_2 \bx_2 = \lambda_1 \bx_1^T \bx_2\\
\implies & (\lambda_1 - \lambda_2) \bx_1^T \bx_2 = 0 \\
\implies & \bx_1^T \bx_2 = 0.
$$
Thus $\bx_1$ and $\bx_2$ are orthogonal.
In between we took transpose on both sides,
used the fact that $\bA= \bA^T$ 
and $\lambda_1 - \lambda_2 \neq 0$.
````
````{prf:definition} Orthogonally diagonalizable matrix
:label: def:mat:orthogonally_diagonalizable_matrix

A real $n \times n$ matrix $A$ is said to be *orthogonally diagonalizable* if
there exists an orthogonal matrix $\bU$ which can diagonalize $\bA$; i.e.,

$$
\bD = \bU^T \bA \bU 
$$
is a real diagonal matrix.
````

````{prf:lemma}
:label: res-mat-orth-diag-symmetric

Every orthogonally diagonalizable matrix $\bA$ is symmetric.
````
````{prf:proof}
We have a diagonal matrix $\bD$ such that

$$
\bA = \bU \bD \bU^T. 
$$
Taking transpose on both sides we get

$$
\bA^T = \bU \bD^T \bU^T = \bU \bD \bU^T = \bA.
$$
Thus $\bA$ is symmetric.
````

````{prf:theorem}
:label: thm:mat:eig:symmetric_orthogonal_sufficient_condition

Every symmetric matrix $\bA$ is orthogonally diagonalizable. 
````
We skip the proof of this theorem.
## Hermitian Matrices
Following is a fundamental property of Hermitian matrices.

````{prf:theorem} Existence of eigen values for Hermitian matrices
:label: thm:mat:eig_hermitian_eigenvalue_guarantee

Every Hermitian matrix has an eigen value.
````
The proof of this result is beyond the scope of this book.


````{prf:lemma} Real eigen values for Hermitian matrices
:label: lem:mat:eig:hermitian_eigenvalues_real

The eigenvalues of a Hermitian matrix are real.
````
````{prf:proof}
Let $\bA$ be a Hermitian matrix and
let $\lambda$ be an eigen value of $\bA$.
Let $\bu$ be a corresponding eigen vector.
Then

$$
& \bA \bu = \lambda \bu\\
\implies & \bu^H \bA^H = \bu^H \overline{\lambda} \\
\implies & \bu^H \bA^H \bu = \bu^H \overline{\lambda} \bu\\
\implies & \bu^H \bA \bu = \overline{\lambda} \bu^H \bu \\
\implies & \bu^H \lambda \bu = \overline{\lambda} \bu^H \bu \\
\implies &\|u\|_2^2 (\lambda - \overline{\lambda}) = 0\\
\implies & \lambda = \overline{\lambda}.
$$
Thus $\lambda$ is real.
We used the facts that $\bA = \bA^H$ and $\bu \neq \bzero \implies \|\bu\|_2 \neq 0$.
````


````{prf:lemma} Orthogonality of eigenvectors for distinct eigenvalues
:label: thm:mat:eig:hermitiaan_orthogonal

Let $\bA$ be an $n \times n$ complex Hermitian matrix.
Let $\lambda_1$ and $\lambda_2$ be any two distinct
eigen values of $\bA$ and let
$\bx_1$ and $\bx_2$ be any two corresponding eigen vectors.
Then $\bx_1$ and $\bx_2$ are orthogonal.
````
````{prf:proof}
By definition we have
$\bA \bx_1 = \lambda_1 \bx_1$ and $\bA \bx_2 = \lambda_2 \bx_2$.
Thus

$$
& \bx_2^H \bA \bx_1 = \lambda_1 \bx_2^H \bx_1\\
\implies & \bx_1^H \bA^H \bx_2 = \lambda_1 \bx_1^H \bx_2 \\
\implies & \bx_1^H \bA \bx_2 = \lambda_1 \bx_1^H \bx_2\\
\implies & \bx_1^H \lambda_2 \bx_2 = \lambda_1 \bx_1^H \bx_2\\
\implies & (\lambda_1 - \lambda_2) \bx_1^H \bx_2 = 0 \\
\implies & \bx_1^H \bx_2 = 0.
$$
Thus $\bx_1$ and $\bx_2$ are orthogonal.
In between we took conjugate transpose on both sides,
used the fact that $\bA= \bA^H$ 
and $\lambda_1 - \lambda_2 \neq 0$.
````


````{prf:definition} Unitary diagonalizable matrix
:label: def:mat:unitary_diagonalizable_matrix

A complex $n \times n$ matrix $\bA$ is said to be *unitary diagonalizable* if
there exists a unitary matrix $\bU$ which can diagonalize $\bA$; i.e.,

$$
\bD = \bU^H \bA \bU 
$$
is a complex diagonal matrix.
````
````{prf:lemma}
:label: res-mat-eig-complex-a-unit-diag-real-hermitian

Let $\bA$ be a unitary diagonalizable matrix
whose diagonalization $\bD$ is real. Then $\bA$
is Hermitian.
````
````{prf:proof}
We have a real diagonal matrix $\bD$ such that

$$
\bA = \bU \bD \bU^H. 
$$
Taking conjugate transpose on both sides we get

$$
\bA^H = \bU \bD^H \bU^H = \bU \bD \bU^H = \bA.
$$
Thus $\bA$ is Hermitian.
We used the fact that $\bD^H = \bD$ since $\bD$ is real.
````

````{prf:theorem}
:label: thm:mat:eig:hermitian_unitary_sufficient_condition

Every Hermitian matrix $\bA$ is unitary diagonalizable. 
````
We skip the proof of this theorem.
The theorem means that if $\bA$ is Hermitian
then $\bA = \bU \Lambda \bU^H$ where $\Lambda$ is a real diagonal matrix. 

````{prf:definition} Eigen value decomposition of a Hermitian matrix
:label: def:mat:eig:evd_hermitian_matrix

Let $\bA$ be an $n \times n$ Hermitian matrix.
Let $\lambda_1, \dots \lambda_n$ be its eigen values
such that $|\lambda_1| \geq |\lambda_2| \geq \dots \geq |\lambda_n |$.
Let

$$
\Lambda = \Diag(\lambda_1, \dots, \lambda_n).
$$
Let $\bU$ be a unit matrix consisting of orthonormal
eigen vectors corresponding to 
$\lambda_1, \dots, \lambda_n$.
Then the *eigen value decomposition* of $\bA$ is defined as

$$
\bA = \bU \Lambda \bU^H.
$$
If $\lambda_i$ are distinct, then the decomposition is unique.
````

````{prf:remark}
:label: res-mat-evd-norm-bounds-eigen-nng

Let $\Lambda$ be a diagonal matrix as in
{prf:ref}`def:mat:eig:evd_hermitian_matrix`.
Consider some vector $\bx \in \CC^n$.

$$
\bx^H \Lambda \bx = \sum_{i=1}^n \lambda_i | x_i |^2.
$$
Now if $\lambda_i \geq 0$ then 

$$
\bx^H \Lambda \bx  
\leq \lambda_1 \sum_{i=1}^n  | x_i |^2 = \lambda_1 \| \bx \|_2^2.
$$
Also

$$
\bx^H \Lambda \bx
\geq \lambda_n \sum_{i=1}^n | x_i |^2 = \lambda_n \| \bx \|_2^2.
$$
````

````{prf:lemma}
:label: lem:mat:eig:hermitian_psd_x_h_a_x_range

Let $\bA$ be a Hermitian matrix with non-negative eigen values.
Let $\lambda_1$ be its largest
and $\lambda_n$ be its smallest eigen values. 

$$
\lambda_n  \|\bx\|_2^2 \leq \bx^H \bA \bx 
\leq  \lambda_1  \|\bx \|_2^2 \Forall  \bx \in \CC^n.
$$
````
````{prf:proof}
$\bA$ has an eigen value decomposition given by

$$
\bA = \bU \Lambda \bU^H.
$$
1. Let $\bx \in \CC^n$ and let $\bv = U^H \bx$.
1. Clearly $\| \bx \|_2 = \| \bv \|_2$.
1. Then 
   
   $$
   \bx^H \bA \bx = \bx^H \bU \Lambda \bU^H \bx = \bv^H \Lambda \bv.
   $$
1. From previous remark we have
   
   $$
    \lambda_n \| \bv \|_2^2 \leq \bv^H \Lambda \bv 
    \leq \lambda_1 \| \bv \|_2^2.
   $$
1. Thus we get
   
   $$
    \lambda_n \| \bx \|_2^2 \leq \bx^H \bA \bx 
    \leq \lambda_1 \| \bx \|_2^2.
   $$
````
## Miscellaneous Properties
This subsection lists some miscellaneous properties of eigen values of a square matrix.

````{prf:lemma}
:label: lem:mat:eig:lambda_k_sum

$\lambda$ is an eigen value of $\bA$
if and only if $\lambda + k$ is an eigen value
of $\bA + k \bI$.
Moreover $\bA$ and $\bA + k \bI$ share the same eigen vectors.
````
````{prf:proof}
We can see that

$$
& \bA \bx = \lambda \bx \\
\iff & \bA \bx  + \bk \bx = \lambda \bx + k \bx \\
\iff & (\bA + k \bI ) \bx = (\lambda + k) \bx.
$$
Thus $\lambda$ is an eigen value of $\bA$ with an eigen vector $\bx$
if and only if
$\lambda + k$ is an eigen vector of $\bA + k\bI$ with an eigen vector $\bx$.
````



## Semidefinite, Definite and Indefinite Matrices

### Positive Semidefinite Matrices

````{prf:definition} Positive semidefinite matrix
:label: def-la-psd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *positive semi-definite* if
$\bv^T \bX \bv \geq 0$ for all $\bv \in \RR^n$.

The notation $\bX \succeq \ZERO$ means $\bv^T \bX \bv \geq 0 \Forall \bv \in \RR^n$
or the matrix $\bX$ is positive semi-definite.

We define the *set of symmetric positive semidefinite matrices* as

$$
\SS_+^n = \{\bX \in \SS^n \ST \bX \succeq \ZERO \}.
$$

"positive semidefinite" is often abbreviated as "p.s.d.".
````


```{prf:theorem} 
:label: res-la-ata-as-psd-matrix

Let $\bA \in \RR^{m \times n}$ be an arbitrary matrix. 
Then, $\bA^T \bA$ is a p.s.d. matrix in $\SS^n$ and
$\bA \bA^T$ is a p.s.d. matrix in $\SS^m$.
```

```{prf:proof}

We shall just prove this for $\bA^T \bA$.

1. We note that

   $$
   (\bA^T \bA)^T = \bA^T \bA.
   $$
   Thus,  $\bA^T \bA$ is symmetric.
1. $\bA^T \bA \in \RR^{n \times n}$. Since it is symmetric, hence $\bA^T \bA \in \SS^n$.
1. Let $\bv \in \RR^n$.
1. Then,

   $$
   \bv^T \bA^T \bA \bv  = (\bA \bv)^T (\bA \bv) 
   = \| \bA \bv \|^2 \geq 0
   $$
   where $\| \cdot \|$ is the norm induced by the dot product on
   $\RR^n$.
1. Thus, $\bA^T \bA$ is p.s.d..
```

```{prf:theorem} Non-negativity of the diagonal elements of p.s.d. matrices
:label: res-la-psd-diag-nng

Let $\bA \in \RR^{n \times n}$ be positive semidefinite.
Then, its diagonal elements are non-negative.
```

```{prf:proof}

Let $\bA \in \SS_+^n$.

1. Then, for every nonzero $\bv \in \RR^n$, $\bv^T \bA \bv \geq 0$.
1. In particular, this is true for standard unit vectors.
1. But $\be_i^T \bA \be_i = A_{i,i}$.
1. Hence, $A_{i,i} \geq 0$ must be true.
```



```{prf:definition} Square root of a positive semidefinite matrix
:label: def-la-psd-square-root

Let $\bA \in \SS^n$ be a positive semidefinite matrix. The
*square root* of $\bA$, denoted by $\bA^{\frac{1}{2}}$ is defined
as follows. 

Let $\bA = \bU \bD \bU^T$ be the eigenvalue decomposition of $\bA$.
Let $d_1,\dots,d_n$ be the diagonal elements of $\bD$.
Let $\bE = \Diag(\sqrt{d_1}, \dots, \sqrt{d_n})$. Then, 

$$
\bA^{\frac{1}{2}} \triangleq \bU \bE \bU^T.
$$
The matrix $\bU \bE \bU^T$ is known as the *positive semidefinite square root*.
```
The definition of $\bE$ is justified since $d_i \geq 0$ for a p.s.d. matrix.

We can see that

$$
ç \bA^{\frac{1}{2}} = 
\bU \bE \bU^T \bU \bE \bU^T
= \bU \bE \bE \bU^T = \bU \bD \bU^T = \bA.
$$


### Positive Definite Matrices

````{prf:definition} Positive definite matrix
:label: def-la-pd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *positive definite* if
$\bv^T \bX \bv > 0$ for all nonzero $\bv \in \RR^n$.

The notation $\bX \succ \ZERO$ means $\bv^T \bX \bv  > 0 \Forall \bv \in \RR^n, \bv \neq 0$
or the matrix $\bX$ is positive definite.

We define the *set of symmetric positive definite matrices* as

$$
\SS_{++}^n = \{\bX \in \SS^n \ST \bX \succ 0 \}.
$$

"positive definite" is often abbreviated as "p.d.".
````


```{prf:theorem} Positivity of the diagonal elements of p.d. matrices
:label: res-la-pd-diag-positive

Let $\bA \in \RR^{n \times n}$ be positive definite.
Then, its diagonal elements are positive.
```

```{prf:proof}

Let $\bA \in \SS_{++}^n$.

1. Then, for every nonzero $\bv \in \RR^n$, $\bv^T \bA \bv > 0$.
1. In particular, this is true for standard unit vectors.
1. But $\be_i^T \bA \be_i = A_{i,i}$.
1. Hence, $A_{i,i} > 0$ must be true.
```


```{prf:theorem} Principal minors criterion
:label: res-la-pd-principal-minors-criterion

A matrix $\bA \in \SS^n$ is positive definite if and only if
the determinants of all the principal minors are positive.

In other words, $D_1(\bA) > 0, D_2(\bA) > 0, \dots, D_n(\bA) > 0$
where $D_i(\bA)$ denotes the determinant of the upper left $i \times i$
submatrix (the $i$-th principal minor). 
```

### Negative Semidefinite Matrices

````{prf:definition} Negative semidefinite matrix
:label: def-la-nsd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *negative semi-definite* if
$\bv^T \bX \bv \leq 0$ for all $\bv \in \RR^n$.

The notation $\bX \preceq \ZERO$ means $\bv^T \bX \bv \leq 0 \Forall \bv \in \RR^n$
or the matrix $\bX$ is negative semi-definite.

We define the *set of symmetric negative semidefinite matrices* as

$$
    \SS_-^n = \{\bX \in \SS^n \ST \bX \preceq \ZERO \}.
$$

"negative semidefinite" is sometimes abbreviated as "n.s.d.".
````


### Negative Definite Matrices

````{prf:definition} Negative definite matrix
:label: def-la-nd-matrix

A symmetric matrix $\bX \in \SS^n$ is called *negative definite* if
$\bv^T \bX \bv < 0$ for all nonzero $\bv \in \RR^n$.

The notation $\bX \prec \ZERO$ means $\bv^T \bX \bv  < 0 \Forall \bv \in \RR^n, \bv \neq 0$
or the matrix $\bX$ is negative definite.

We define the *set of symmetric negative definite matrices* as

$$
\SS_{--}^n = \{\bX \in \SS^n \ST \bX \prec 0 \}.
$$

"negative definite" is sometimes abbreviated as "n.d.".
````


### Indefinite Matrices

````{prf:definition} Indefinite matrix
:label: def-la-indefinite-matrix

A symmetric matrix $\bA \in \SS^n$ is called *indefinite* if
there exist $\bx, \by \in \RR^n$ such that
$\bx^T \bA \bx < 0$ and $\by^T \bA \by > 0$.
````

Indefinite matrices are neither positive semidefinite nor negative semidefinite.

```{prf:theorem} Diagonal elements and indefiniteness
:label: res-la-diag-indefinite

Let $\bA \in \SS^n$. If the diagonal elements of $\bA$ are both
positive and negative, then $\bA$ is indefinite.
```

```{prf:proof}
Each diagonal element corresponds to $\be_i^T \bA \be_i$ for a
unit vector $\be_i$.
If the diagonal elements are both positive and negative, then
there exist unit vectors $\be_i$ and $\be_j$ such that
$\be_i^T \bA \be_i < 0$ and $\be_j^T \bA \be_j > 0$. 
Thus, $\bA$ is indefinite.
```

### Eigenvalue Decomposition

```{prf:theorem} Eigenvalue characterization theorem
:label: res-la-evd-definiteness-charac

Let $\bA \in \SS^n$ be an $n\times n$ symmetric matrix.

1. $\bA$ is positive definite if and only if all its eigenvalues are positive.
1. $\bA$ is positive semidefinite if and only if all its eigenvalues are nonnegative.
1. $\bA$ is negative definite if and only if all its eigenvalues are negative.
1. $\bA$ is negative semidefinite if and only if all its eigenvalues are nonpositive.
1. $\bA$ is indefinite if and only if at least one eigenvalue is positive and
   at least one eigenvalue is negative.
```

```{prf:proof}
Let the eigenvalue decomposition of $\bA$ be given by
$\bA = \bU \bD \bU^T$.

We prove (1).

1. Let $\bv \in \RR^n$.
1. Then

   $$
   \bv^T \bA \bv = \bv^T \bU \bD \bU^T \bv
   = \bw^T \bD \bw = \sum_{i=1}^n d_i w_i^2.
   $$
   where $\bw = \bU^T \bv$.
1. Since $\bU$ is nonsingular, hence $\bv^T \bA \bv > 0$ for every $\bv \neq \bzero$
   if and only if $\sum_{i=1}^n d_i w_i^2 > 0$ for every $\bw \neq \bzero$.
1. Plugging $\be_i$ for $\bw$, we see that $d_i > 0$ is a necessary condition.
1. Also, if $d_i > 0$ for every $i$, then, the sum is positive for every nonzero $\bw$
   since at least one $w_i \neq 0$.
   Hence, it is a sufficient condition. 

Similar arguments apply for other statements.
```

### Trace and Determinant

```{prf:corollary} Trace and determinant of positive definite matrices
:label: res-la-pd-trace-det

Let $\bA$ be a symmetric positive definite matrix. Then, $\Trace (\bA)$ and $\det (\bA)$
are positive.
```

```{prf:proof}
Trace is the sum of eigenvalues. Determinant is the product of eigenvalues.
If $\bA$ is symmetric positive definite, then its eigenvalues are positive.
Hence, trace and determinant are positive.
```

```{prf:corollary} Trace and determinant of positive semidefinite matrices
:label: res-la-psd-trace-det

Let $\bA$ be a symmetric positive definite matrix. Then, $\Trace (\bA)$ and $\det (\bA)$
are nonnegative.
```

(sec:mat:diagonally_dominant_matrix)=
## Diagonally Dominant Matrices

```{prf:definition} Diagonally dominant matrix
:label: def-la-sym-diagonally-dominant-matrix

Let $\bA \in \FF^{n \times n}$ with $\bA = [a_{i j}]$. 

1. $\bA$ is called *diagonally dominant* if

   $$
   | a_{i i} | \geq \sum_{j, j \neq i} | a_{i j} | 
   $$
   for every $i=1,\dots,n$.
   In other words, the absolute value of the diagonal entry in a row
   is greater than or equal to the sum of absolute values of non diagonal entries in the row.
1. $\bA$ is called *strictly diagonally dominant* if

   $$
   | a_{i i} | > \sum_{j, j \neq i} | a_{i j} | 
   $$
   for every $i=1,\dots,n$.
   In other words, the absolute value
   of the diagonal element is bigger than the sum of absolute values
   of all the off diagonal elements on that row.
```

````{prf:example} Strictly diagonally dominant matrix
:label: ex-mat-diag-dominate-1

Let us consider

$$
\bA = \begin{bmatrix}
-4 & -2 & -1 & 0\\
-4 & 7 & 2 & 0\\
3 & -4 & 9 & 1\\
2 & -1 & -3 & 15
\end{bmatrix}.
$$

We can see that the strict diagonal dominance condition is satisfied for each row as follows:

$$
& \text{ row 1}: \quad & |-4| > |-2| + |-1| + |0| = 3 \\
& \text{ row 2}: \quad & |7| > |-4| + |2| + |0| = 6 \\
& \text{ row 3}: \quad & |9| > |3| + |-4| + |1| = 8 \\
& \text{ row 4}: \quad & |15| > |2| + |-1| + |-3| = 6.
$$
````

```{prf:theorem} Positive semidefiniteness of diagonally dominant matrices
:label: res-la-sym-ddm-psd

Let $\bA \in \SS^n$ be a real symmetric matrix. 

1. If $\bA$ is diagonally dominant whose diagonal entries are nonnegative then
   $\bA$ is positive semidefinite.
1. If $\bA$ is strictly diagonally dominant whose diagonal entries are positive
   then $\bA$ is positive definite.
```

```{prf:proof}

Assume that $\bA$ is diagonally dominant with nonnegative diagonal entries.

1. For contradiction, assume that $\bA$ is not positive semidefinite.
1. Then, there is an eigen value $\lambda < 0$ and corresponding eigenvector $\bu$.
1. Consider the absolute values of entries of $\bu$ given by $(|u_1|, \dots, |u_n|)$.
1. Let $i \in 1,\dots,n$ denote the index of the largest absolute value entry of $\bu$.
1. We also have $\bA \bu = \lambda \bu$.
1. For the $i$-th row, we get the equality

   $$
   & \sum_{j = 1}^n A_{i j} u_j = \lambda u_i \\
   & \iff \sum_{j \neq i} A_{i j} u_j = \lambda u_i - A_{i i} u_i \\
   & \implies \left | \sum_{j \neq i} A_{i j} u_j \right | 
   = | \lambda - A_{i i} | |u_i | \\
   & \implies  | \lambda - A_{i i} | |u_i | 
   \leq \left ( \sum_{j \neq i} | A_{i j} | \right ) | u_i |
   \leq |A_{ i i} | |u_i |.
   $$
1. Thus,  $| \lambda - A_{i i} |  = |A_{ i i} - \lambda | \leq |A_{ i i} |$.
1. But $A_{i i}$ is nonnegative and $\lambda$ is negative, hence this reduces to
   $A_{ i i} - \lambda \leq A_{i i}$ or $\lambda \geq 0$.
1. We have arrived at a contradiction.
1. Thus, $\bA$ must be positive semidefinite.


Now, assume that $\bA$ is strictly diagonally dominant with positive diagonal entries.

1. By first part, it is clear that $\bA$ is p.s.d..
1. We just need to show that all eigenvalues are positive. There are no zero eigenvalues.
1. For contradiction, assume that $0$ is indeed an eigenvalue of $\bA$.
1. Let $\bu \neq \bzero$ be corresponding eigenvector satisfying
   $\bA \bu = \bzero$.
1. Let $i \in 1,\dots,n$ denote the index of the largest absolute value entry of $\bu$.
1. Following the earlier argument

   $$
   | A_{i i}| |u_i | &= \left | \sum_{j \neq i} A_{i j} u_j  \right | \\
   &\leq \left ( \sum_{j \neq i} | A_{i j} | \right ) |u_i| \\
   &< | A_{i i} | |u_i|.
   $$
1. This is impossible. Hence, $\bA$ must be positive definite.
```

Strictly diagonally dominant matrices have a very special property. They are
always non-singular. The following result is valid for both real
and complex strictly diagonally dominant matrices.

````{prf:theorem}
:label: thm:mat:strictly_diagonally_dominant_matrix_nonsingularity

Strictly diagonally dominant matrices are non-singular.
````
````{prf:proof}
For contradiction, suppose that $\bA$ is strictly diagonally dominant and singular.

1. Then there exists a vector
   $u \in \CC^n$ with $\bu \neq \bzero$ such that 
   
   $$
   \bA \bu = \bzero.
   $$
1. Let

   $$
   \bu = \begin{pmatrix} u_1 & u_2 & \dots & u_n \end{pmatrix}.
   $$
1. We first show that every entry in $\bu$ cannot be equal in magnitude.
1. For contradiction, let us assume that there exists $c > 0$ such that
   
   $$
   c = | u_1 | = | u_2 | = \dots = | u_n|.
   $$
1. Since $\bu \neq \bzero$ hence $c \neq 0$.
1. We can write $u_j = c \exp(i \theta_j)$ for every $j=1,\dots,n$.
1. Now for any row $i$ in $\bA \bu = \bzero$, we have

   $$
   & \sum_{j=1}^n a_{ij} u_j = 0\\
   \implies &  \sum_{j=1}^n a_{ij} c \exp(i \theta_j) = 0\\
   \implies & \sum_{j=1}^n  a_{ij} \exp(i \theta_j) = 0\\
   \implies & - a_{ii} \exp(i \theta_j) = \sum_{j \neq i} a_{ij} \exp(i \theta_j)\\
   \implies &  |a_{ii}| = \left| \sum_{j \neq i} a_{ij} \exp(i \theta_j) \right |\\
   \implies &  |a_{ii}| \leq \sum_{j \neq i} |a_{ij}|
   $$
   by triangle inequality.
1. But this contradicts our assumption that $\bA$ is strictly diagonally dominant.
1. Thus all entries in $\bu$ are not equal in magnitude. 
1. Let us now assume that
   the largest entry in $\bu$ lies at index $i$ with $|u_i| = c$. 
1. Without loss of generality we can scale down $\bu$ by $c$ to get
   another vector in which all entries are less than or equal to 1 in magnitude
   while $i$-th entry has a magnitude of $1$.
1. In other words, $|u_i| = 1$
   and $|u_j| \leq 1$ for all other entries.
1. From $\bA \bu = \bzero$ we get for the $i$-th row

   $$
   & \sum_{j=1}^n a_{ij} u_j = 0\\\
   \implies & - a_{ii} u_i = \sum_{j \neq i} u_j a_{ij}\\
   \implies & | a_{ii} u_i | = \left | \sum_{j \neq i} u_j a_{ij} \right |\\
   \implies & |a_{ii}| \leq \sum_{j \neq i} |u_j a_{ij}| 
   \leq \sum_{j \neq i} |a_{ij}|
   $$
   which again contradicts our assumption that $\bA$ is strictly diagonally dominant.
1. Hence strictly diagonally dominant matrices are non-singular.
````

## Gershgorin's Theorem
We are now ready to examine Gershgorin' theorem
which provides very useful bounds on the
spectrum of a square matrix.

````{prf:theorem} Gershgorin's circle theorem
:label: thm:mat:gershgorin_circle_theorem:a

Every eigen value $\lambda$ of a square matrix $\bA \in \CC^{n\times n}$ satisfies 

```{math}
:label: eq:mat:gershgorin_circle_theorem:a

| \lambda - a_{ii}| 
\leq \sum_{j, j\neq i} |a_{ij}|
\text{ for some } i \in \{1,2, \dots, n \}.
```
````
````{prf:proof}
The proof is a straight forward application of non-singularity of 
diagonally dominant matrices.

1. We know that for an eigen value $\lambda$,
   $\det(\lambda \bI  - \bA) = 0$
1. In other words, the matrix $(\lambda \bI  - \bA)$ is singular.
1. Hence it cannot be strictly diagonally dominant
   due to {prf:ref}`thm:mat:strictly_diagonally_dominant_matrix_nonsingularity`.
1. Thus looking at each row $i$ of $(\lambda \bI  - \bA)$ we can say that
   
   $$
    | \lambda - a_{ii}| > \sum_{j, j\neq i} |a_{i j}|
   $$
   cannot be true for all rows simultaneously.
1. In other words, this condition must fail at least for one row.
1. This means that there exists at least one row $i$ for which
   
   $$
   | \lambda - a_{ii}| \leq \sum_{j, j\neq i} |a_{i j}|
   $$
   holds true.
````

What this theorem means is pretty simple.
1. Consider a disc in the complex plane
   for the $i$-th row of $\bA$ whose center is given by $a_{ii}$ and whose 
   radius is given by $r = \sum_{j\neq i} |a_{i j}|$ i.e. the sum of
   magnitudes of all non-diagonal entries in $i$-th row.
1. There are $n$ such discs corresponding to $n$ rows in $\bA$. 
1. {eq}`eq:mat:gershgorin_circle_theorem:a` means that every eigen value
   must lie within the union of these discs. It cannot lie outside.

This idea is crystallized in following definition.

````{prf:definition} Gershgorin's disc
:label: def:mat:gershgorin_disk

For $i$-th row of the square matrix $\bA$
we define the radius $r_i = \sum_{j, j\neq i} |a_{i j}|$
and the center $c_i = a_{ii}$.
Then the set given by

$$
D_i = \{z \in \CC \ST  |z - a_{ii}| \leq r_i \}
$$
is called the $i$-th *Gershgorin's disc* of $\bA$.
````
We note that the definition is equally valid for real as well as complex matrices.
For real matrices, the centers of disks lie on the real line.
For complex matrices, the centers may lie anywhere in the complex plane.

Clearly there is nothing extraordinary about the rows of $\bA$.
We can as well consider the columns of $\bA$.

````{prf:theorem} Gershgorin's circle theorem for columns
:label: thm:mat:gershgorin_circle_theorem:b

Every eigen value of a matrix $\bA$ must lie in a
Gershgorin disc corresponding to the
columns of $\bA$ where the  Gershgorin disc for $j$-th column is given by

$$
D_j = \{z \in \CC \ST  | z - a_{j j} | \leq r_j \}
$$
with 

$$
r_j =  \sum_{i, i \neq j} |a_{i j}|
$$
````
````{prf:proof}
We know that eigen values of $\bA$ are same as eigen values of $\bA^T$ and
columns of $\bA$ are nothing but rows of $\bA^T$. Hence eigen values of $\bA$
must satisfy conditions in {prf:ref}`thm:mat:gershgorin_circle_theorem:a`
w.r.t. the matrix $\bA^T$. This completes the proof.
````

