(sec:ssm:compressive:sensing)= 
# Compressive Sensing

In this section we formally define the problem of compressive sensing. 

*Compressive sensing* refers to the idea that for sparse or compressible signals,
a small number of nonadaptive measurements carry sufficient information
to approximate the signal well.
In the literature it is also known as
*compressed sensing* and *compressive sampling*.
Different authors seem to prefer different names.

```{div}
In this section we will represent a signal dictionary
as well as its synthesis matrix as $\bDDD$. 
We recall the definition of sparse signals from {prf:ref}`def-ssm-d-k-sparse-signal`.

A signal $\bx \in \CC^N$ is $K$-sparse in $\bDDD$
if there exists a representation $\ba$ for $\bx$ which
has at most $K$ non-zero entries; i.e.,

$$
\bx = \bDDD \ba
$$
and 

$$
\| \ba \|_0 \leq K.
$$

The dictionary could be standard basis, Fourier basis, wavelet basis,
a wavelet packet dictionary,
a multi-ONB or even a randomly generated dictionary. 

Real life signals are not sparse, yet they are compressible in the sense that
entries in the signal decay rapidly when sorted by magnitude.
As a result compressible signals are well
approximated by sparse signals.
Note that we are talking about the sparsity or compressibility
of the signal in a suitable dictionary.
Thus we mean that the signal $\bx$ has a representation
$\ba$ in $\bDDD$ in which the coefficients decay rapidly when sorted by magnitude. 
```

## Definition

```{image} images/srr_cs.png
```

```{index} Compressive sensing, Compressed sensing, Compressive sampling
```
```{index} Signal space, Measurement space
```
````{prf:definition} Compressive sensing
:label: def:ssm:compressed_sensing

In compressive sensing, a *measurement* is a linear functional applied to a signal

$$
y = \langle \bx, \bf \rangle.
$$
The compressive sensor makes multiple such linear measurements.
This can best be represented by the action of a *sensing matrix* $\Phi$
on the signal $\bx$ given by 

$$
\by = \Phi \bx
$$
where $\Phi \in \CC^{M \times N}$ represents $M$ different measurements
made on the signal $\bx$
by the sensing process.
Each row of $\Phi$ represents one linear measurement.

The vector $\by \in \CC^M$ is known as *measurement vector*.

$\CC^N$ forms the *signal space* while $\CC^M$ forms the *measurement space*.
We also note that above can be written as

$$
\by  = \Phi \bx = \Phi \bDDD \ba = (\Phi \bDDD) \ba.
$$
It is assumed that the signal $\bx$ is $K$-sparse or $K$-compressible in
$\bDDD$ and $K \ll N$.

The objective is to recover $\bx$ from $\by$ given that $\Phi$ and $\bDDD$ are known.

We do this by first recovering the sparse representation $\ba$ from $\by$
and then computing $\bx = \bDDD \ba$.

If $M \geq N$ then the problem is a straight forward least squares problem.
So we don't consider it here.

The more interesting case is when $K < M \ll N$;
i.e., the number of measurements is much less
than the dimension of the ambient signal space
while more than the sparsity level of signal namely $K$.

We note that given $\ba$ is found, finding $\bx$ is straightforward.  
We therefore can remove the dictionary from our consideration and look at
the simplified problem given as: 

Recover $\bx$ from $\by$ with

$$
\by = \Phi \bx
$$
where $\bx \in \CC^N$ itself is assumed to be $K$-sparse or $K$-compressible 
and $\Phi \in \CC^{M \times N}$ is the sensing matrix.
````

(sec:ssm:sensing_matrix)=
## The Sensing Matrix

````{div}
There are two ways to look at the sensing matrix.
First view is in terms of its columns

```{math}
:label: eq:ssm:sensing_matrix_column_view

\Phi = \begin{bmatrix}
\phi_1 & \phi_2 & \dots & \phi_N
\end{bmatrix}
```
where $\phi_i \in \CC^M$ are the columns of sensing matrix. 
In this view we see that

$$
\by = \sum_{i=1}^{N} x_i \phi_i;
$$
i.e., $\by$ belongs to the column span of $\Phi$ and one representation of
$\by$ in $\Phi$ is given by $x$.

This view looks very similar to a dictionary and its atoms but there is a difference.
In a dictionary, we require each atom to be unit norm.
We don't require columns of the sensing matrix $\Phi$ to be unit norm.

The second view of sensing matrix $\Phi$ is in terms of its columns. We write

```{math}
:label: eq:ssm:sensing_matrix_row_view

\Phi = \begin{bmatrix}
\bf_1^H \\
\bf_2^H \\
\vdots \\
\bf_M^H
\end{bmatrix}
```
where $\bf_i \in \CC^N$ are conjugate transposes of rows of $\Phi$.
This view gives us following expression:

```{math}
:label: eq-ssm-cs-row-linear-measurements

\begin{bmatrix}
y_1\\
y_2 \\
\vdots\\
y_M
\end{bmatrix}
= \begin{bmatrix}
\bf_1^H \\
\bf_2^H \\
\vdots \\
\bf_M^H
\end{bmatrix}
\bx
= \begin{bmatrix}
\bf_1^H \bx\\
\bf_2^H \bx\\
\vdots \\
\bf_M^H \bx
\end{bmatrix}
= \begin{bmatrix}
\langle \bx , \bf_1 \rangle \\
\langle \bx , \bf_2 \rangle \\
\vdots \\
\langle \bx , \bf_M \rangle \\
\end{bmatrix}
```

In this view $y_i$ is a measurement given by the inner product of
$\bx$ with $\bf_i$ 
$( \langle \bx , \bf_i \rangle = \bf_i^H \bx)$. 

We will call $\bf_i$ as a *sensing vector*.
There are $M$ such sensing vectors in $\CC^N$
comprising $\Phi$ corresponding to $M$ measurements in the measurement space $\CC^M$.
````

## Number of Measurements


A fundamental question of compressive sensing framework is:
*How many measurements are  necessary to acquire $K$-sparse signals*?
By necessary we mean that $\by$ carries
enough information about $\bx$ such that $\bx$ can be recovered from $\by$. 

Clearly if $M < K$ then recovery is not possible. 

We further note that the sensing matrix $\Phi$ should not map two different $K$-sparse
signals to the same measurement vector.
Thus we will need $M \geq 2K$ and each
collection of $2K$ columns in $\Phi$ must be non-singular. 

If the $K$-column  sub matrices of $\Phi$ are badly conditioned, then it is possible that
some sparse signals get mapped to very similar measurement vectors.
Then it is numerically unstable
to recover the signal. 
Moreover, if noise is present, stability further degrades. 

````{div}
In {cite}`candes2006near` Cand\`es and Tao  showed that the geometry of sparse
signals should be preserved under the action of a sensing matrix. In particular
the distance between two sparse signals shouldn't change by much during sensing.

They quantified this idea in the form of a *restricted isometric constant* of a matrix
$\Phi$ as the smallest number $\delta_K$ for which the following holds

$$
(1 - \delta_K) \| \bx \|_2^2 
\leq \| \Phi \bx \|_2^2 
\leq (1 + \delta_K) \| \bx \|_2^2 
\Forall \bx : \| x \|_0 \leq K.
$$
We will study more about this property known as restricted isometry property (RIP) 
in {prf:ref}`sec:proj:restricted_isometry_property`.
Here we just sketch the implications of RIP for compressive sensing.

When $\delta_K < 1$ then the inequalities imply that
every collection of $K$ columns from $\Phi$ is
non-singular.
Since we need every collection of $2K$ columns to be non-singular,
we actually need $\delta_{2K} < 1$ which is the minimum requirement
for recovery of $K$ sparse signals. 

Further if $\delta_{2K} \ll 1$ then we note that sensing operator
very nearly maintains the $\ell_2$ distance between any two $K$ sparse signals.
As a consequence, it is possible to invert the sensing process stably.

It is now known that many randomly generated matrices have excellent RIP behavior.
One can show  that if $\delta_{2K} \leq 0.1$, then with 

$$
M = \bigO{K \ln ^{\ba} N}
$$
measurements, one can recover $\bx$ with high probability. 

Some of the typical random matrices which have suitable RIP properties are

*  Gaussian sensing matrices
*  Partial Fourier matrices
*  Rademacher sensing matrices
````

(sec:ssm:sparse:recovery)=
## Signal Recovery

The second fundamental problem in compressive sensing is:
*Given the compressive measurements $\by$ how do we recover the signal $\bx$*?
This problem is known as SPARSE-RECOVERY problem.

````{div}
A simple formulation of the problem as: 
minimize $\| \bx \|_0$ subject to $\by = \Phi \bx$ is hopeless
since it entails a combinatorial explosion of search space.  

Over the years, people have developed
a number of algorithms to tackle the sparse recovery problem.

The algorithms can be broadly classified into following categories

* [Greedy pursuits] These algorithms attempt to build the approximation of
  the signal iteratively by making locally optimal choices at each step.
  Examples of such algorithms include OMP (orthogonal matching pursuit),
  stage-wise OMP, regularized OMP, CoSaMP (compressive sampling pursuit)
  and IHT (iterative hard thresholding). 
* [Convex relaxation] These techniques relax the $\ell_0$ "norm" minimization problem
  into a suitable  problem which is a convex optimization problem.
  This relaxation is valid for a large class of signals of interest.
  Once the problem has been formulated as a convex optimization problem,
  a number of solutions are available, e.g. 
  interior point methods, projected gradient methods and iterative thresholding.  
*  [Combinatorial algorithms] These methods are based on research in group testing
   and are specifically suited for situations where highly structured measurements
   of the signal are taken.
   This class includes algorithms like Fourier sampling, chaining pursuit, and HHS pursuit.

A major emphasis of the following chapters will be the study
of these sparse recovery algorithms.

In the following we present examples of real life problems
which can be modeled as compressive sensing problems.
````

## Error Correction in Linear Codes

The classical error correction problem was discussed in one of the 
seminal founding papers on compressive sensing {cite}`candes2005decoding`.

````{prf:example} Error correction in linear codes as a compressive sensing problem
:label: ex-ssm-cs-error-correction-linear-codes

Let $\bf \in \RR^N$ be a "plaintext" message being sent over a communication channel.

In order to make the message robust against errors in communication channel, we encode 
the error with an error correcting code.

We consider $\bA \in \RR^{D \times N}$ with $D > N$ as a *linear code*.
$\bA$ is essentially a collection of code words given by

$$
\bA = \begin{bmatrix}
\ba_1 & \ba_2 & \dots & \ba_N 
\end{bmatrix}
$$
where $\ba_i \in \RR^D$ are the code words.

We construct the "ciphertext"  

$$
\bx = \bA \bf
$$
where $\bx \in \RR^D$ is sent over the communication channel.
Clearly $\bx$ is a redundant representation of $\bf$
which is expected to be robust against  small errors during transmission.

$\bA$ is assumed to be full column rank.
Thus $\bA^T \bA$ is invertible and we can easily see that

$$
\bf = \bA^{\dag} \bx 
$$
where

$$
\bA^{\dag} = (\bA^T \bA)^{-1}\bA^T
$$
is the left pseudo inverse of $\bA$.

The communication channel is going to add some error.
What we actually receive is

$$
\by = \bx + \be = \bA \bf + \be
$$
where $\be \in \RR^D$ is the error being introduced by the channel.

The least squares solution by minimizing the error $\ell_2$ norm is given by 

$$
\bf' = \bA^{\dag} \by = \bA^{\dag} (\bA \bf + \be) = \bf + \bA^{\dag} \be.
$$

Since $\bA^{\dag} \be$ is usually non-zero
(we cannot assume that $\bA^{\dag}$ will annihilate $\be$),
hence $\bf'$ is not an exact replica of $\bf$. 

What is needed is an exact reconstruction of $\bf$.
To achieve this,  a common assumption in literature is that 
error vector $\be$ is in fact sparse. i.e. 

$$
\| \be \|_0 \leq K \ll D.
$$

To reconstruct $\bf$ it is sufficient to reconstruct $\be$
since once $\be$ is known we can get

$$
\bx  = \by - \be
$$
and from there $\bf$ can be faithfully reconstructed.

The question is: for a given sparsity level $K$ for the error vector $\be$
can one reconstruct
$\be$ via practical algorithms? 
By practical we mean algorithms which are of polynomial
time w.r.t. the length of "ciphertext" ($D$).

The approach in {cite}`candes2005decoding` is as follows. 
We construct a matrix $\bF \in \RR^{M \times D}$ which can annihilate $\bA$; 
i.e.,

$$
\bF \bA  = \ZERO.
$$
We then apply $\bF$ to $\by$ giving us

$$
\tilde{\by} = \bF (\bA \bf + \be) = \bF\be.
$$

Therefore the decoding problem is reduced to that of reconstructing
a sparse vector $\be \in \RR^D$
from the measurements $\bF \be \in \RR^M$ where we would like to have $M \ll D$. 

With this the problem of finding $\be$ can be cast
as problem of finding a sparse solution
for the under-determined system given by

```{math}
:label: eq:ssm:error_correction_k_sparse_error
& \underset{\be \in \Sigma_K}{\text{minimize}} 
& &  \| \be \|_0 \\
& \text{subject to }
& &  \tilde{\by} = \bF \be.
```

This now becomes the compressive sensing problem. The natural questions are

*  How many measurements $M$ are necessary (in $\bF$) to be able to recover $\be$ exactly? 
*  How should $\bF$ be constructed?
*  How do we recover $\be$ from $\tilde{\by}$?

These problems are addressed in following chapters as we discuss
sensing matrices and signal recovery algorithms.
````
