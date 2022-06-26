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

```{index} Compressive sensing; embedding
```
````{prf:definition} Embedding of a signal
:label: def:ssm:cs:embedding

Given a signal $\bx \in \RR^N$,
a vector $\by = \Phi \bx \in \RR^M$
is called an *embedding* of $\bx$ in the measurement space $\RR^M$. 
````

```{index} Compressive sensing; explanation
```
````{prf:definition} Explanation of a measurement
:label: def:explanation_signal

A signal $\bx \in \RR^N$ is called an *explanation* of a measurement
$\by \in \RR^M$ w.r.t. sensing matrix $\Phi$ if $\by = \Phi \bx$. 
````
In the following we present examples of real life problems
which can be modeled as compressive sensing problems.

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

## Piecewise Cubic Polynomial Signal

````{prf:example} Piecewise cubic polynomial signal
:label: ex-ssm-cs-piecewise-cubic-polynomial-signal

This example was discussed in {cite}`candRomb2004practical`.
Our signal of interest is a piecewise cubic polynomial signal
as shown below.
```{figure} images/piecewise_polynomial/signal.png
---
name: fig:ssm:piecewise_polynomial:signal
---
A piecewise cubic polynomials signal
```

It has a compressible representation in a wavelet basis.

```{figure} images/piecewise_polynomial/representation.png
---
name: fig:ssm:piecewise_polynomial:representation
---
Compressible representation of signal in wavelet basis
```

The representation is described by the equation.

$$
\bx = \Psi \alpha
$$
The chosen basis is a Daubechies wavelet basis $\Psi$.
```{figure} images/piecewise_polynomial/dictionary.png
---
name: fig:ssm:piecewise_polynomial:dictionary
---
Daubechies-8 wavelet basis
```
In this example $N = 2048$. We have $\bx \in \RR^N$.
$\Psi$ is a complete dictionary of size $N \times N$.
Thus we have $D = N$ and $\alpha \in \RR^N$.

We can sort the wavelet coefficients by magnitude and plot
them in descending order to visualize how sparse the 
representation is.
```{figure} images/piecewise_polynomial/representation_sorted.png
---
name: fig:ssm:piecewise_polynomial:representation_sorted
---
Wavelet coefficients sorted by magnitude
```

Before making compressive measurements, we need to decide
how many compressive measurements will be sufficient?

Closely examining the coefficients in $\alpha$ we can note that
$\max(\alpha_i) = 78.0546$.
Further if we put different thresholds
over magnitudes of entries in $\alpha$ we can find the number
of coefficients higher than different thresholds as listed below.

```{div}
Entries in wavelet representation of piecewise cubic polynomial
signal higher than a threshold

| Threshold | Entries higher than threshold|
| --- | --- |
| 1 | 129|
| 1E-1 | 173|
| 1E-2 | 186|
| 1E-4 | 197|
| 1E-8 | 199|
| 1E-12 | 200|
```
A choice of $M = 600$ looks quite reasonable given the decay
of entries in $\alpha$. Later we shall provide theoretical
bounds for choice of $M$.

A Gaussian random sensing matrix $\Phi$
is used to generate the compressed measurements.
```{figure} images/piecewise_polynomial/sensing_matrix.png
---
name: fig:ssm:piecewise_polynomial:sensing_matrix
---
Gaussian sensing matrix $\Phi$
```
The measurement process is described by the equation

$$
\by = \Phi \bx + \be = \Phi \Psi \alpha + \be
$$
with $\bx \in \RR^N$, $\Phi \in \RR^{M \times N}$,
and measurement vector $\by \in \RR^M$.
For this example we chose the measurement noise to be $\be = \bzero$. 

The compressed measurements are shown below.
```{figure} images/piecewise_polynomial/measurements.png
---
name: fig:ssm:piecewise_polynomial:measurements
---
Measurement vector $\by = \Phi \bx + \be$
```


Finally the product of $\Phi$ and $\Psi$ given by $\Phi \Psi$ 
will be used for actual recovery of sparse representation
$\alpha$ from the measurements $\by$.
```{figure} images/piecewise_polynomial/recovery_matrix.png
---
name: fig:ssm:piecewise_polynomial:recovery_matrix
---
Recovery matrix $\Phi \Psi$
```

The sparse signal recovery problem is denoted as

$$
\widehat{\alpha} = \text{recovery}(\Phi \Psi, \by, K).
$$
where $\widehat{\alpha}$ is a $K$-sparse approximation of $\alpha$.
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

A major emphasis of these notes will be the study
of these sparse recovery algorithms. We shall provide
some basic results in this section.
We shall work under the following framework
in the remainder of this section.

1. Let $\bx \in \RR^N$ be our signal of interest where $N$ is the number 
   of signal components or *dimension* of the signal space $\RR^N$.
1. Let us make $M$ linear measurements of the signal.
1. The measurements are given by

   $$
   \by = \Phi \bx.
   $$
1. $\by \in \RR^M$ is our measurement vector in the measurement space $\RR^M$
   and $M$ is the dimension of our measurement space.
1. $\Phi$ is an $M\times N$ matrix known as the *sensing matrix*.
1. $M \ll N$, hence $\Phi$ achieves a *dimensionality reduction* over $\bx$.
1. We assume that measurements are *non-adaptive*; i.e.,
   the matrix $\Phi$ is predefined and doesn't depend on $\bx$.
1. The recovery process is denoted by 

   $$
   \bx' = \Delta \by = \Delta (\Phi \bx) 
   $$
   where $\Delta : \RR^M \to \RR^N$ is a (usually nonlinear) recovery algorithm. 

We will look at three kinds of situations:

*  Signals are truly sparse. A signal has up to $K  (K \ll N)$ non-zero values
   only where $K$ is known in advance.
   Measurement process is ideal and no noise is introduced during measurement.
   We will look for guarantees which can ensure exact recovery of signal from
   $M (K < M \ll N)$ linear measurements.
*  Signals are not truly sparse but they have few $K (K \ll N)$ values
   which dominate the signal.
   Thus if we approximate the signal by these $K$ values,
   then approximation error is not noticeable.
   We again assume that there is no measurement noise being introduced.
   When we recover the signal, it will in general not be exact recovery.
   We expect the recovery error to be bounded (by approximation error). 
   Also in special cases where the signal turns out
   to be $K$-sparse, we expect the recovery algorithm to recover the signal exactly.
   Such an algorithm with bounded recovery error will be called *robust*.
*  Signals are not sparse. Also there is measurement noise being introduced.
   We expect recovery algorithm to minimize error and thus perform *stable* recovery
   in the presence of measurement noise.
````

## Exact Recovery of Sparse Signals

````{div}
The null space of a matrix $\Phi$ is denoted as 

$$
\NullSpace(\Phi) = \{ \bv \in \RR^N :\Phi \bv = \bzero\}.
$$
The set of $K$-sparse signals is defined as 

$$
\Sigma_K = \{ \bx \in \RR^N :  \|\bx\|_0 \leq K\}.
$$

````{prf:example} K sparse signals
:label: ex-ssm-k-sparse-signal-2

Let $N=10$. 
*  $\bx=(1,2, 1, -1, 2 , -3, 4, -2, 2, -2) \in \RR^{10}$ is not a sparse signal.
*  $\bx=(0,0,0,0,1,0,0,-1,0,0)\in \RR^{10}$ is a 2-sparse signal. Its also a 4 sparse signal.
````


````{prf:lemma}
:label: lem:difference_k_sparse_signals

If $\ba$ and $\bb$ are two $K$ sparse signals then $\ba - \bb$ is a $2K$ sparse signal.
````

````{prf:proof}
$(a - b)_i$ is non zero only if at least one of $a_i$ and $b_i$ is non-zero.
Hence number of non-zero components of $\ba - \bb$ cannot exceed $2K$.
Hence $\ba - \bb$ is a $2K$-sparse signal.
````

````{prf:example} Difference of K sparse signals
Let N = 5. 

*  Let $\ba = (0,1,-1,0, 0)$ and $\bb = (0,2,0,-1, 0)$.
   Then $\ba - \bb = (0,-1,-1,1, 0) $ is a 3 sparse as well as 4 sparse signal.
*  Let $\ba = (0,1,-1,0, 0)$ and $\bb = (0,2,-1,0, 0)$. 
   Then $\ba - \bb = (0,-1,-2,0, 0) $ is a 2 sparse as well as 4 sparse signal.
*  Let $\ba = (0,1,-1,0, 0)$ and $\bb = (0,0,0,1, -1)$.
   Then $\ba - \bb = (0,1,-1,-1, 1) $ is a 4 sparse signal.
````

```{prf:definition} Unique embedding of a set
:label: def-ssm-cs-unique-embeddings

We say that a sensing matrix $\Phi$ uniquely embeds
a set $C \subseteq \RR^N$ if for any $\ba, \bb \in C$, we have

$$
\Phi \bb \neq \Phi \bb.
$$
```


````{prf:theorem} Unique embeddings of $K$ sparse vectors
:label: lem:k_sparse_unique_representation_requirement

A sensing matrix $\Phi$ uniquely embeds every
$\bx \in \Sigma_K$ if and only if $\NullSpace(\Phi) \cap \Sigma_{2K} = \EmptySet$;
i.e., $\NullSpace(\Phi)$ contains no vectors in $\Sigma_{2K}$.
````  

````{prf:proof}
We first show that the difference of sparse signals is not in the nullspace.
1. Let $\ba$ and $\bb$ be two $K$ sparse signals.
1. Then $\Phi \ba$ and $\Phi \bb$ are corresponding measurements.
1. Now if $\Phi$ provides unique embedding of all $K$ sparse signals,
   then $\Phi \ba \neq \Phi \bb$.
1. Thus  $\Phi (\ba - \bb) \neq \bzero$.
1. Thus $\ba - \bb \notin \NullSpace(\Phi)$. 

We show the converse by contradiction.

1. Let $\bx \in \NullSpace(\Phi) \cap \Sigma_{2K}$.
1. Thus $\Phi \bx = \bzero$ and $\|\bx\|_0 \leq 2K$.
1. Then we can find $\by, \bz \in \Sigma_K$
   such that $\bx = \bz - \by$.
1. Thus there exists $\bm \in \RR^M$ such that $\bm = \Phi \bz = \Phi \by$.
1. But then, $\Phi$ doesn't uniquely embed $\by, \bz \in \Sigma_K$. 
````
There are equivalent ways of characterizing this condition.
In the following, we present a condition based on spark.

### Spark
We recall from {prf:ref}`def:spark`, that spark of a matrix $\Phi$ is defined as the
minimum number of columns which are linearly dependent.


````{prf:theorem} Unique explanations and spark
:label: thm:k_sparse_explanation_spark_requirement

For any measurement $\by \in \RR^M$, there exists at most one signal
$\bx  \in \Sigma_K$ such that
$\by = \Phi \bx$ if and only if $\spark(\Phi) > 2K$.
````

````{prf:proof}
We need to show

*  If for every measurement, there is only one $K$-sparse explanation, then $\spark(\Phi) > 2K$.
*  If $\spark(\Phi) > 2K$ then for every measurement, there is only one $K$-sparse explanation.

Assume that for every $\by \in \RR^M$
there exists at most one signal $\bx \in \Sigma_K$ such that $\by = \Phi \bx$.

1. Now assume that $\spark(\Phi) \leq 2K$.
1. Thus there exists a set of at most $2K$ columns which are linearly dependent. 
1. Thus there exists $\bv \in \Sigma_{2K}$ such that $ \Phi \bv = \bzero$.
1. Thus $\bv \in \NullSpace (\Phi)$.  
1. Thus $\Sigma_{2K} \cap \NullSpace (\Phi) \neq \EmptySet$. 
1. Hence $\Phi$ doesn't uniquely embed each signal $\bx \in \Sigma_K$.
   A contradiction.
1. Hence $\spark(\Phi) > 2K$.

Now suppose that $\spark(\Phi) > 2K$. 
1. Assume that for some $y$ there exist two different $K$-sparse explanations
   $\bx, \bx'$ such that $\by = \Phi \bx =\Phi \bx'$.  
1. Then $\Phi (\bx  - \bx') = \bzero$.
1. Thus $\bx - \bx' \in \NullSpace (\Phi)$ and $\bx - \bx' \in  \Sigma_{2K}$. 
1. Hence, there exists a set of at most $2K$ columns in $\Phi$ which is
   linearly dependent.
1. Thus $\spark(\Phi) \leq 2K$. A contradiction. 
1. Hence, for every $\by \in \RR^M$, there exists at most one $\bx \in \Sigma_K$.
````

Since $\spark(\Phi) \in [2, M+1]$ and we require that
$\spark(\Phi) > 2K$ hence we require that $M \geq 2K$.
 
## Recovery of Approximately Sparse Signals

Spark is a useful criteria for characterization of sensing matrices for truly sparse signals.
But this doesn't work well for *approximately* sparse signals.
We need to have more restrictive criteria on $\Phi$
for ensuring  recovery of approximately sparse signals from compressed measurements.

In this context we will deal with two types of errors: 


Approximation error
* Let us approximate a signal $\bx$ using only $K$ coefficients. 
* Let us call the approximation as $\widehat{\bx}$.
* Thus $\be_a = (\bx - \widehat{\bx})$ is approximation error.

Recovery error
* Let $\Phi$ be a sensing matrix. 
* Let $\Delta$ be a recovery algorithm. 
* Then $\bx'= \Delta(\Phi \bx)$ is the recovered signal vector.
* The error $\be_r = (\bx - \bx')$ is recovery error.

Ideally, the recovery error should not be too large compared to the
approximation error.

In this following we will

*  Formalize the notion of null space property (NSP) of a matrix $\Phi$.
*  Describe a measure for performance of an arbitrary recovery algorithm $\Delta$.
*  Establish the connection between NSP and performance guarantee for recovery algorithms.

````{div}
Suppose we approximate $\bx$ by a $K$-sparse signal
$\widehat{\bx} \in \Sigma_K$, then the minimum error under $\ell_p$ norm is given by

$$
\sigma_K(\bx)_p = \min_{\widehat{\bx} \in \Sigma_K} \| \bx - \widehat{\bx}\|_p. 
$$

One specific $\widehat{\bx} \in \Sigma_K$ for which this minimum is achieved
is the best $K$-term approximation
({prf:ref}`lem:ssm:best_k_term_approximation`).

In the following, we will need some additional notation.
1. Let $ I = \{1,2,\dots, N\}$ be the set of indices for signal $\bx \in \RR^N$.
1. Let $\Lambda \subset I$  be a subset of indices.
1. Let $\Lambda^c = I \setminus \Lambda$.
1. $\bx_{\Lambda}$ will denote a signal vector obtained by setting the entries of 
   $\bx$ indexed by $\Lambda^c$ to zero.
````

````{prf:example}
:label: ex-ssm-cs-signal-restriction-1

1. Let N = 4.
1. Then $I = \{1,2,3,4\}$.
1. Let $\Lambda = \{1,3\}$. 
1. Then $\Lambda^c = \{2, 4\}$. 
1. Now let $\bx = (-1,1,2,-4)$.
1. Then $\bx_{\Lambda} = (-1, 0, 2, 0)$.
````

$\Phi_{\Lambda}$ will denote a $M\times N$ matrix obtained by setting the columns of $\Phi$
indexed by $\Lambda^c$ to zero.

````{prf:example}
:label: ex-ssm-cs-matrix-restriction-1

1. Let N = 4.
1. Then $I = \{1,2,3,4\}$.
1. Let $\Lambda = \{1,3\}$. 
1. Then $\Lambda^c = \{2, 4\}$. 
1. Now let $\bx = (-1,1,2,-4)$. 
1. Then $\bx_{\Lambda} = (-1, 0, 2, -4)$.

1. Now let 
   
   $$
   \Phi = \begin{pmatrix}
        1 & 0 & -1 & 1\\
        -1 & -2 & 2 & 3
      \end{pmatrix}.
   $$

1. Then 
    
    $$
    \Phi_{\Lambda} = \begin{pmatrix}
        1 & 0 & -1 & 0\\
        -1 & 0 & 2 & 0
      \end{pmatrix}.
    $$
````

### Null Space Property

```{index} Null space property
```
````{prf:definition} Null space property
:label: def:null_space_property

A matrix $\Phi$ satisfies the *null space property (NSP)* of order $K$
if there exists a constant $C > 0$ such that,


$$
\| \bh_{\Lambda}\|_2 \leq C \frac{\| \bh_{{\Lambda}^c}\|_1 }{\sqrt{K}}
$$
holds for every $\bh \in \NullSpace (\Phi)$ and for every
$\Lambda$ such that $|\Lambda| \leq K$.
````


*  Let $\bh$ be $K$ sparse. Thus choosing the indices on which $\bh$ is non-zero, I can
   construct a $\Lambda$ such that $|\Lambda| \leq K$ and $\bh_{{\Lambda}^c} = 0$. 
   Thus $\| \bh_{{\Lambda}^c}\|_1$ = 0. Hence above condition is not satisfied. Thus
   such a vector $\bh$ should not belong to $\NullSpace(\Phi)$ if $\Phi$ satisfies NSP.
*  Essentially vectors in $\NullSpace (\Phi)$ shouldn't be concentrated in a small subset of indices.
*  If $\Phi$ satisfies NSP then the only $K$-sparse vector in $\NullSpace(\Phi)$ is $\bh = \bzero$.


### Measuring the Performance of a Recovery Algorithm

Let $\Delta : \RR^M \to \RR^N$ represent a recovery method to
recover approximately sparse $\bx$ from $\by$.

````{div}
$\ell_2$ recovery error is given by 

$$
\| \Delta (\Phi \bx) - \bx \|_2.
$$

The $\ell_1$ error for $K$-term approximation is given by $\sigma_K(\bx)_1$.

We will be interested in guarantees of the form

```{math}
:label: eq:nspguarantee

\| \Delta (\Phi \bx) - \bx \|_2 \leq C \frac{\sigma_K (\bx)_1}{\sqrt{K}}.
```
Why, this recovery guarantee formulation?

*  Exact recovery of K-sparse signals. $\sigma_K (\bx)_1 = 0$ if $\bx \in \Sigma_K$.
*  Robust recovery of non-sparse signals
*  Recovery dependent on how well the signals are approximated by $K$-sparse vectors.
*  Such guarantees are known as *instance optimal* guarantees.
*  Also known as *uniform* guarantees.


Why the specific choice of norms? 

*  Different choices of $\ell_p$ norms lead to different guarantees.
*  $\ell_2$ norm on the LHS is a typical least squares error.
*  $\ell_2$ norm on the RHS will require prohibitively large number of measurements.
*  $\ell_1$ norm on the RHS helps us keep the number of measurements less.

If an algorithm $\Delta$ provides instance optimal guarantees as defined above, what
kind of requirements does it place on the sensing matrix $\Phi$?

We show that NSP of order $2K$ is a necessary condition for providing uniform guarantees.
````

### NSP and Instance Optimal Guarantees

````{prf:theorem} NSP and instance optimal guarantees
:label: thm:nsp_guarantee_requirement

Let $\Phi : \RR^N \to \RR^M$ denote a sensing matrix 
and $\Delta : \RR^M \to \RR^N$ denote an arbitrary recovery algorithm.
If the pair $(\Phi, \Delta)$ satisfies instance optimal guarantee
{eq}`eq:nspguarantee`,
then  $\Phi$ satisfies NSP of the order $2K$.
````

````{prf:proof}
We are given that

*  $(\Phi, \Delta)$ form an encoder-decoder pair.
*  Together, they satisfy instance optimal guarantee {eq}`eq:nspguarantee`.
*  Thus they are able to recover all sparse signals exactly.
*  For non-sparse signals, they are able to recover their $K$-sparse approximation with bounded recovery error.


We need to show that if $\bh \in \NullSpace(\Phi)$, then $\bh$ satisfies

$$
\| \bh_{\Lambda}\|_2 \leq C \frac{\| \bh_{{\Lambda}^c}\|_1 }{\sqrt{2K}}
$$
where $\Lambda$ corresponds to $2K$ largest magnitude entries in $\bh$.
Note that we have used $2K$ in this expression, since we need to show that 
$\Phi$ satisfies NSP of order $2K$.

1. Let $\bh \in \NullSpace(\Phi)$.
1. Let $\Lambda$ be the indices corresponding to the $2K$ largest entries of $\bh$.
1. Then 
   
   $$
    \bh = \bh_{\Lambda}  + \bh_{\Lambda^c}.
   $$
1. Split $\Lambda$ into $\Lambda_0$ and $\Lambda_1$
   such that $|\Lambda_0| = |\Lambda_1| = K$.
1. We have

   $$
   \bh_{\Lambda} = \bh_{\Lambda_0} + \bh_{\Lambda_1}.
   $$
1. Let
   
   $$
   \bx = \bh_{\Lambda_0} + \bh_{\Lambda^c}.
   $$

1. Let 
   
   $$
   \bx' = - \bh_{\Lambda_1}.
   $$

1. Then 
   
   $$
   \bh =  \bx - \bx'.
   $$
1. By assumption $\bh \in \NullSpace(\Phi)$.
1. Thus

   $$
   \Phi \bh = \Phi(\bx - \bx') = \bzero \implies \Phi \bx = \Phi \bx'.
   $$
1. But since $\bx' \in \Sigma_K$ (recall that $\Lambda_1$ indexes only $K$ entries) 
   and  $\Delta$ is able to recover all $K$-sparse signals exactly, hence
   
   $$
   \bx' = \Delta (\Phi \bx').
   $$
1. Thus 
   
   $$
   \Delta (\Phi \bx) = \Delta (\Phi  \bx') = \bx';
   $$
   i.e., the recovery algorithm $\Delta$ recovers $\bx'$ for
   the signal $\bx$.
1. Certainly $\bx$ is not $K$-sparse since $\Delta$ recovers every
   $K$-sparse signal uniquely.
1. Hence $\Lambda^c$ must be nonempty.
1. Finally we also have
   
   $$
   \| \bh_{\Lambda} \|_2 \leq \| \bh \|_2  = \| \bx  - \bx'\|_2 
   = \| \bx - \Delta (\Phi \bx)\| _2
   $$
   since $\bh$ contains some additional non-zero entries.
1. But as per instance optimal recovery guarantee {eq}`eq:nspguarantee`
   for $(\Phi, \Delta)$ pair,  we have
   
   $$
    \| \Delta (\Phi \bx) - \bx \|_2 \leq C \frac{\sigma_K (\bx)_1}{\sqrt{K}}.
   $$
1. Thus
   
   $$
    \| \bh_{\Lambda} \|_2 \leq C \frac{\sigma_K (\bx)_1}{\sqrt{K}}.
   $$
1. But 
   
   $$
   \sigma_K (\bx)_1 = \min_{\widehat{x} \in \Sigma_K} \|\bx - \widehat{\bx}\|_1. 
   $$
1. Recall that $\bx =\bh_{\Lambda_0} + \bh_{\Lambda^c}$
   where $\Lambda_0$ indexes $K$ entries of $\bh$
   which are (magnitude wise) larger than all entries indexed by $\Lambda^c$.
1. Hence the best $\ell_1$-norm $K$ term
   approximation of $\bx$ is given by  $\bh_{\Lambda_0}$. 
1. Hence

   $$
   \sigma_K (\bx)_1  = \|  \bh_{\Lambda^c} \|_1. 
   $$
1. Thus we finally have
   
   $$
   \| \bh_{\Lambda} \|_2 \leq C \frac{\|  \bh_{\Lambda^c} \|_1}{\sqrt{K}} 
   = \sqrt{2}C \frac{\|  \bh_{\Lambda^c} \|_1}{\sqrt{2K}}  
   \quad \Forall \bh \in \NullSpace(\Phi).
   $$
1. Thus $\Phi$ satisfies the NSP of order $2K$.
````
It turns out that NSP of order $2K$ is also sufficient to establish a guarantee of the form
above for a practical recovery algorithm.