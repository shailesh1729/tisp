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

```{math}
:label: eq:ripbound
(1 - \delta_K) \| \bx \|_2^2 
\leq \| \Phi \bx \|_2^2 
\leq (1 + \delta_K) \| \bx \|_2^2 
\Forall \bx : \| x \|_0 \leq K.
```
We will study more about this property known as restricted isometry property (RIP) 
in {ref}`sec:ssm:rip`.
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



 
## Recovery in Presence of Measurement Noise

````{div}
Measurement vector in the presence of noise is given by

$$
\by =\Phi \bx + \be
$$
where $\be$ is the measurement noise or error.
$\| \be \|_2$ is the $\ell_2$ size of measurement error.

Recovery error as usual is given by

$$
\| \Delta (\by) - \bx \|_2 = \| \Delta (\Phi \bx + \be) - \bx \|_2. 
$$

*Stability* of a recovery algorithm is characterized by comparing
variation of recovery error w.r.t. measurement error.

NSP is both necessary and sufficient for establishing guarantees of the form:

$$
\| \Delta (\Phi \bx) - \bx \|_2 \leq C \frac{\sigma_K (\bx)_1}{\sqrt{K}}.
$$
These guarantees do not account for presence of noise during measurement.

We need stronger conditions for handling noise.
The restricted isometry property for sensing matrices comes to our rescue.
````

### Restricted Isometry Property

````{div}
We recall that a matrix $\Phi$ satisfies the *restricted isometry property* (RIP)
of order $K$  if there exists $\delta_K \in (0,1)$ such that

$$
(1- \delta_K) \| \bx \|^2_2 
\leq \| \Phi \bx \|^2_2 
\leq (1 + \delta_K) \| \bx \|^2_2  
$$
holds for every $\bx \in \Sigma_K = \{ \bx \ST \| \bx\|_0 \leq K \}$. 

* If a matrix satisfies RIP of order $K$, then we can see that it *approximately* preserves 
  the size of a $K$-sparse vector.
* If a matrix satisfies RIP of order $2K$, then we can see that it  *approximately* preserves the 
  distance between any two $K$-sparse vectors since difference vectors would be $2K$ sparse
  (see {prf:ref}`lem:proj:rip_distance_preservation`) . 
* We say that the matrix is *nearly orthonormal* for sparse vectors.
* If a matrix satisfies RIP of order $K$ with a constant $\delta_K$,
  it automatically satisfies
  RIP of any order $K' < K$ with a constant $\delta_{K'} \leq \delta_{K}$.
````

### Stability

Informally a recovery algorithm is stable if recovery error is small
in the presence of small measurement noise.

Is RIP necessary and sufficient for sparse signal recovery from noisy measurements? 
Let us look at the necessary part. 

We will define a notion of stability of the recovery algorithm.

````{prf:definition} $C$ stable encoder-decoder pair
:label: def:recovery_algorithm_stability

Let $\Phi : \RR^N \to \RR^M$ be a sensing matrix 
and $\Delta : \RR^M \to \RR^N$ be a recovery algorithm.
We say that the pair $(\Phi, \Delta)$ is *$C$-stable* if for any $\bx \in \Sigma_K$
and any $\be \in \RR^M$ we have that

$$
\| \Delta(\Phi \bx + \be) - \bx\|_2  \leq C \| \be\|_2. 
$$
````

*  Error is added to the measurements.
*  LHS is $\ell_2$ norm of recovery error.
*  RHS consists of scaling of the $\ell_2$ norm of measurement error.
*  The definition says that recovery error is bounded by a
   multiple of the measurement error.
*  Thus adding a small amount of measurement noise
   shouldn't be causing arbitrarily large recovery error.

It turns out that $C$-stability requires $\Phi$ to satisfy RIP.

````{prf:theorem} Necessity of RIP for $C$-stability
:label: thm:stability_requires_rip

If a pair $(\Phi, \Delta)$ is $C$-stable then

$$
\frac{1}{C} \| \bx\|_2 \leq \| \Phi \bx  \|_2  
$$
for all $\bx \in \Sigma_{2K}$.
````
````{prf:proof}
Remember that any $\bx \in \Sigma_{2K}$ can be written in the form of
$\bx  = \by - \bz$ where
$\by, \bz \in \Sigma_K$.

1. Let $\bx \in \Sigma_{2K}$.
1. Split it in the form of $\bx = \by -\bz$ with $\by, \bz \in \Sigma_{K}$.

1. Define
   
   $$
   \be_y = \frac{\Phi (\bz - \by)}{2} \quad \text{and} \quad \be_z = \frac{\Phi (\by - \bz)}{2}.
   $$

1. Thus
   
   $$
   \be_y - \be_z = \Phi (\bz - \by) \implies \Phi \by + \be_y = \Phi \bz + \be_z.
   $$
1. We have
   
   $$
   \Phi \by + \be_y = \Phi \bz + \be_z = \frac{\Phi (\by + \bz)}{2}.
   $$

1. Also we have
   
   $$
   \| \be_y \|_2 = \| \be_z \|_2 = \frac{\| \Phi (\by - \bz) \|_2}{2} = \frac{\| \Phi \bx \|_2}{2}.
   $$
1. Let 
   
   $$
   \by' = \Delta (\Phi \by + \be_y) = \Delta (\Phi \bz + \be_z).
   $$
1. Since $(\Phi, \Delta)$ is $C$-stable, hence we have
   
   $$
   \| \by'- \by\|_2  \leq C \| \be_y\|_2. 
   $$

1. Also
   
   $$
   \| \by'- \bz\|_2  \leq C \| \be_z\|_2. 
   $$
1. Using the triangle inequality

   $$
   \| \bx \|_2 
   &= \| \by - \bz\|_2  = \| \by - \by' + \by' - \bz \|_2\\ 
   &\leq \| \by - \by' \|_2 + \| \by' - \bz\|_2\\
   &\leq  C \| \be_y \|_2 + C \| \be_z \|_2 
   = C (\| \be_y \|_2 + \| \be_z \|_2)
   = C \| \Phi \bx \|_2.
   $$
1. Thus we have for every $\bx \in \Sigma_{2K}$ 
   
   $$
   \frac{1}{C}\| \bx \|_2 \leq \| \Phi \bx \|_2. 
   $$
````

This theorem gives us the lower bound for RIP property of
order $2K$ in {eq}`eq:ripbound` with 
$\delta_{2K} = 1 - \frac{1}{C^2}$
as a necessary condition for $C$-stable recovery algorithms.

Note that smaller the constant $C$, lower is the bound on recovery error
(w.r.t. measurement error).
But as $C \to 1$, $ \delta_{2K} \to 0$,
thus reducing the impact of measurement noise requires
sensing matrix $\Phi$ to be designed with tighter RIP constraints.

This result doesn't require an upper bound on the RIP property in {eq}`eq:ripbound`.

It turns out that If $\Phi$ satisfies RIP, 
then this is also sufficient for a variety of algorithms to be able to successfully recover
a sparse signal from noisy measurements. We will discuss this later.

### Measurement Bounds

As stated in previous section, for a $(\Phi, \Delta)$ pair to be $C$-stable
we require that
$\Phi$ satisfies RIP of order $2K$ with a constant $\delta_{2K}$. 
Let us ignore $\delta_{2K}$ for the time being and look at relationship between $M$, $N$ and $K$.
We have a sensing matrix $\Phi$ of size $M\times N$ and expect it to provide RIP of order $2K$. 
How many measurements $M$ are necessary? 
We will assume that $K < N / 2$. This assumption is valid for approximately sparse signals.

````{div}
Before we start figuring out the bounds, let us develop a special subset of $\Sigma_K$ sets.
Consider the set 

$$
U = \{ \bx \in \{0, +1, -1\}^N \ST \| \bx\|_0 = K  \}.
$$
When we say $ \| \bx\|_0 = K$,
we mean that exactly $K$ terms in each member of $U$ can be non-zero (i.e. $-1$ or $+1$).

Hence $U$ is a set of signal vectors $\bx$ of length $N$
where each sample takes values from $\{0, +1, -1\}$ and
number of allowed non-zero samples is fixed at $K$.
An example below explains it further. 
````

````{prf:example} $U$ for $N=6$ and $K=2$
:label: ex-ssm-cs-u-set-6-2

Each vector in $U$ will have 6 elements out of which $2$ can be non zero.
There are $\binom{6}{2}$ ways of choosing the non-zero elements.
Some of those sets are listed below as examples:

$$
&(+1,+1,0,0,0,0)\\
&(+1,-1,0,0,0,0)\\
&(0,-1,0,+1,0,0)\\
&(0,-1,0,+1,0,0)\\
&(0,0,0,0,-1,+1)\\
&(0,0,-1,-1,0,0).
$$
````
````{div}
Revisiting

$$
U = \{ \bx \in \{0, +1, -1\}^N \ST \| \bx \|_0 = K \}   
$$
It is now obvious that

$$
\| \bx \|_2^2 = K \Forall \bx \in U.
$$
Since there are $\binom{N}{K}$ ways of choosing $K$ non-zero elements
and each non zero element can take 
either of the two values $+1$ or $-1$, hence the cardinality of
set $U$ is given by:

$$
|U| = \binom{N}{K} 2^K.
$$
By definition 

$$
U \subset \Sigma_K.
$$
Further Let $\bx, \by \in U$.  
Then $\bx - \by$ will have a maximum of $2K$ non-zero elements.
The non-zero elements would have values in $\{-2,-1,1,2\}$.
Thus $ \|\bx - \by \|_0 = R \leq 2K$.
Further $\| \bx - \by \|_2^2 \geq R$.
Hence

$$
\| \bx - \by \|_0 \leq \| \bx - \by \|_2^2 \Forall \bx, \by \in U.
$$
We now state a result which will help us in getting to the bounds.
````
````{prf:lemma}
:label: lem:rip_bound_X_lemma

Let $K$ and $N$ satisfying $K < \frac{N}{2}$ be given.
There exists a set $X \subset \Sigma_K$ such that 
for any $\bx \in X$ we have $\|\bx \|_2 \leq \sqrt{K}$
and for any $\bx, \by \in X$ with $\bx \neq \by$,

$$
\| \bx - \by \|_2 \geq \sqrt{\frac{K}{2}}
$$
and

$$
\ln | X | \geq \frac{K}{2} \ln \left( \frac{N}{K} \right).
$$
````

````{prf:proof}
We just need to find one set $X$ which satisfies the requirements of this lemma.
We have to construct a set $X$ such that


1. $\| \bx \|_2 \leq \sqrt{K}  \Forall \bx \in X$.
1. $\| \bx - \by \|_2 \geq \sqrt{\frac{K}{2}}$ for every $bx, \by \in X$.
1. $\ln | X | \geq \frac{K}{2} \ln \left( \frac{N}{K} \right)$
   or equivalently $|X| \geq \left( \frac{N}{K} \right)^{\frac{K}{2}}$.

First condition states that the set $X$ lies in the intersection of
$\Sigma_K$ and the closed ball $B[\bzero, \sqrt{K}]$.
Second condition states that the points in $X$ are sufficiently
distant from each other.
Third condition states that there are at least a certain number of points
in $X$.

We will construct $X$ by picking vectors from $U$. Thus $X \subset U$.

1. Since $\bx \in X \subset U$ hence
   $\| \bx \|_2 = \sqrt{K} \leq \sqrt{K} \Forall \bx \in X$.
1. Consider any fixed $\bx \in U$.
1. How many elements $\by$ are there in $U$ such that $\|\bx - \by\|_2^2 < \frac{K}{2}$?
1. Define
   
   $$
   U_x^2 = \left \{\by \in U \ST \|\bx - \by\|_2^2  < \frac{K}{2} \right \}.
   $$
1. Clearly by requirements in the lemma,
   if $\bx \in X$ then $U_x^2 \cap X = \EmptySet$;
   i.e., no vector in $U_x^2$ belongs to $X$.
1. How many elements are there in  $U_x^2$? Let us find an upper bound.
1. $\Forall \bx, \by \in U$ we have $\|\bx - \by\|_0  \leq \|\bx - \by\|_2^2$.
1. If $\bx$ and $\by$ differ in $\frac{K}{2}$ or more places, then naturally 
   $\|\bx - \by\|_2^2 \geq \frac{K}{2}$.
1. Hence if $\|\bx - \by\|_2^2 < \frac{K}{2}$ then 
   $\|\bx - \by\|_0 < \frac{K}{2}$
   hence $\|\bx - \by\|_0 \leq \frac{K}{2}$ for any $\bx, \by \in U_x^2$.
1. So define
   
   $$
   U_x^0 = \left \{\by \in U \ST \|\bx - \by\|_0 \leq \frac{K}{2} \right \}.  
   $$
1. We have 
   
   $$
    U_x^2 \subseteq U_x^0.
   $$

1. Thus we have an upper bound given by
   
   $$
    | U_x^2 | \leq | U_x^0 |.
   $$
1. Let us look at $U_x^0$ carefully. 
1. We can choose $\frac{K}{2}$ indices where $\bx$ and $\by$ *may* differ
   in $\binom{N}{\frac{K}{2}}$ ways.
1. At each of these $\frac{K}{2}$ indices, $y_i$ can take value as one of $(0, +1, -1)$.
1. Thus we have an upper bound
   
   $$
    | U_x^2 | \leq | U_x^0 | \leq \binom {N}{\frac{K}{2}} 3^{\frac{K}{2}}.
   $$
1. We now describe an iterative process for building $X$ from vectors in $U$.
1. Say we have added $j$ vectors to $X$ namely $x_1, x_2,\dots, x_j$. 
1. Then
   
   $$
   (U^2_{x_1} \cup U^2_{x_2} \cup \dots  \cup U^2_{x_j}) \cap X = \EmptySet.
   $$
1. Number of vectors in $U^2_{x_1} \cup U^2_{x_2} \cup \dots  \cup U^2_{x_j}$
   is bounded by $j \binom {N}{ \frac{K}{2}} 3^{\frac{K}{2}}$.
1. Thus we have at least 
   
   $$
    \binom{N}{K} 2^K - j \binom {N}{ \frac{K}{2}} 3^{\frac{K}{2}}  
   $$
   vectors left in $U$ to choose from for adding in $X$.
1. We can keep adding vectors to $X$ till there are no more suitable vectors left.
1. We can construct a set of size $|X|$ provided
   
   ```{math}
   :label: eq:measure_bound_x_size
    |X| \binom {N}{ \frac{K}{2}} 3^{\frac{K}{2}} \leq \binom{N}{K} 2^K
   ```
1. Now
   
   $$
      \frac{\binom{N}{K}}{\binom{N}{\frac{K}{2}}} 
      = \frac
        {\left ( \frac{K}{2} \right ) !  \left (N  - \frac{K}{2} \right ) ! }
        {K! (N-K)!}
      = \prod_{i=1}^{\frac{K}{2}}  \frac{N - K + i}{ K/ 2 + i}.
   $$
1. Note that $\frac{N - K + i}{ K/ 2 + i}$ is a decreasing function of $i$.
1. Its minimum value is achieved for $i=\frac{K}{2}$ as $(\frac{N}{K} - \frac{1}{2})$.
1. So we have
   
   $$
      &\frac{N - K + i}{ K/ 2 + i} \geq \frac{N}{K} - \frac{1}{2}\\
      &\implies \prod_{i=1}^{\frac{K}{2}}  \frac{N - K + i}{ K/ 2 + i}  \geq  \left ( \frac{N}{K} - \frac{1}{2} \right )^{\frac{K}{2}}\\
      &\implies \frac{\binom{N}{K}}{\binom{N}{\frac{K}{2}}} \geq \left ( \frac{N}{K} - \frac{1}{2} \right )^{\frac{K}{2}}
   $$
1. Rephrasing the bound on $|X$ in {eq}`eq:measure_bound_x_size` we have
   
   $$
    |X| \left( \frac{3}{4} \right )^{\frac{K}{2}} \leq   \frac{\binom{N}{K}}{\binom{N}{\frac{K}{2}}}
   $$
1. Hence we can definitely construct a set $X$ with the cardinality satisfying
   
   $$
      |X| \left( \frac{3}{4} \right ) ^{\frac{K}{2}}  \leq \left ( \frac{N}{K} - \frac{1}{2} \right )^{\frac{K}{2}}.
   $$
1. Now it is given that $ K < \frac{N}{2}$. So we have:

   $$
    & K < \frac{N}{2}\\
    &\implies \frac{N}{K} > 2\\
    &\implies \frac{N}{4K} > \frac{1}{2}\\
    &\implies \frac{N}{K} - \frac{N}{4K} < \frac{N}{K} - \frac{1}{2}\\
    &\implies \frac{3N}{4K} < \frac{N}{K} - \frac{1}{2}\\
    &\implies \left( \frac{3N}{4K} \right) ^ {\frac{K}{2}}< \left ( \frac{N}{K} - \frac{1}{2} \right )^{\frac{K}{2}}\\
   $$
1. Thus we have
   
   $$
    \left( \frac{N}{K} \right) ^ {\frac{K}{2}}   \left( \frac{3}{4} \right) ^ {\frac{K}{2}}  < \frac{\binom{N}{K}}{\binom{N}{\frac{K}{2}}}
   $$
1. Choose
   
   $$
      |X| = \left( \frac{N}{K} \right) ^ {\frac{K}{2}} 
   $$
1. Clearly this value of $|X|$ satisfies {eq}`eq:measure_bound_x_size`.
1. Hence $X$ can have at least these many elements.
1. Thus
   
   $$
      &|X| \geq \left( \frac{N}{K} \right) ^ {\frac{K}{2}}\\
      &\implies \ln |X| \geq \frac{K}{2} \ln \left( \frac{N}{K} \right) 
   $$
   which completes the proof.
````


We can now establish following bound on the required number of measurements to satisfy RIP.

At this moment, we won't worry about exact value of $\delta_{2K}$. We will just assume that
$\delta_{2K}$ is small in range $(0, \frac{1}{2}]$.

````{prf:theorem} Minimum number of required measurements for RIP of order $2K$
:label: thm:rip_measurement_bound

Let $\Phi$ be an $M \times N$ matrix that satisfies RIP of order $2K$
with constant $\delta_{2K} \in (0, \frac{1}{2}]$.
Then

$$
M \geq C K \ln \left ( \frac{N}{K} \right ) 
$$
where

$$
C = \frac{1}{2 \ln (\sqrt{24} + 1)} \approx 0.28173.
$$
````

````{prf:proof}
Since $\Phi$ satisfies RIP of order $2K$ we have

$$
& (1  - \delta_{2K}) \| \bx \|^2_2 
   \leq \| \Phi \bx \|^2_2 
   \leq (1 + \delta_{2K}) \| \bx\|^2_2  \Forall \bx \in \Sigma_{2K}\\
& \implies (1  - \delta_{2K}) \| \bx - \by \|^2_2 
\leq \| \Phi \bx -  \Phi \by\|^2_2 
\leq (1 + \delta_{2K}) \| \bx - \by\|^2_2  \Forall \bx, \by \in \Sigma_K.
$$
Also

$$
\delta_{2K} \leq \frac{1}{2}
\implies 1 - \delta_{2K} \geq 
\frac{1}{2} \text{ and }  1 + \delta_{2K} \leq \frac{3}{2}.
$$
Consider the set $X \subset U \subset \Sigma_K$ developed in {prf:ref}`lem:rip_bound_X_lemma`.
We have

$$
&\| \bx - \by\|^2_2 \geq  \frac{K}{2} \Forall \bx, \by \in X\\
&\implies (1  - \delta_{2K}) \| \bx - \by \|^2_2 \geq  \frac{K}{4}\\
&\implies \| \Phi \bx -  \Phi \by\|^2_2 \geq  \frac{K}{4}\\
&\implies \| \Phi \bx -  \Phi \by\|_2 \geq  \sqrt{\frac{K}{4}} \Forall \bx, \by \in X.
$$
Also

$$
&\| \Phi \bx \|^2_2 
\leq (1 + \delta_{2K}) \| \bx\|^2_2 
\leq  \frac{3}{2}  \| \bx\|^2_2 
\Forall \bx \in X \subset \Sigma_K \subset \Sigma_{2K}\\
&\implies \| \Phi \bx \|_2 
\leq \sqrt {\frac{3}{2}}  \| \bx\|_2  \leq \sqrt {\frac{3K}{2}} \Forall \bx \in X
$$
since $\|\bx\|_2 \leq \sqrt{K} \Forall \bx \in X$.
So we have a lower bound:

```{math}
:label: eq:rip_lower_bound_x
\| \Phi \bx -  \Phi \by\|_2 \geq  \sqrt{\frac{K}{4}} \Forall \bx, \by \in X.
```
and an upper bound:

```{math}
:label: eq:rip_upper_bound_x
\| \Phi \bx \|_2 \leq \sqrt {\frac{3K}{2}} \Forall \bx \in X.
```
What do these bounds mean? Let us start with the lower bound.

$\Phi \bx$ and $\Phi \by$ are projections of $\bx$ and $\by$ in $\RR^M$ (measurement space).

Construct $\ell_2$ balls of radius
$\sqrt{\frac{K}{4}} / 2= \sqrt{\frac{K}{16}}$ in $\RR^M$ around $\Phi \bx$ and $\Phi \by$.

Lower bound says that these balls are disjoint.
Since $\bx, \by$ are arbitrary, this applies to every $\bx \in X$.

Upper bound tells us that all vectors $\Phi \bx$ lie in a ball of radius
$\sqrt {\frac{3K}{2}}$ around origin in $\RR^M$.

Thus the set of all balls lies within a larger ball of radius  $\sqrt {\frac{3K}{2}} + \sqrt{\frac{K}{16}}$  around origin in $\RR^M$.

So we require that the volume of the larger ball MUST be greater than the sum of volumes of $|X|$ individual balls. 

Since volume of an $\ell_2$ ball of radius $r$ is proportional to $r^M$, we have: 

$$
&\left ( \sqrt {\frac{3K}{2}} + \sqrt{\frac{K}{16}}    \right )^M \geq |X| \left ( \sqrt{\frac{K}{16}} \right )^M\\. 
& \implies (\sqrt {24} + 1)^M \geq  |X| \\
& \implies  M \geq \frac{\ln |X| }{\ln (\sqrt {24} + 1) }
$$
Again from {prf:ref}`lem:rip_bound_X_lemma` we have

$$
\ln |X| \geq \frac{K}{2} \ln \left ( \frac{N}{K} \right ).
$$
Putting back we get

$$
M \geq \frac{\frac{K}{2} \ln \left ( \frac{N}{K} \right ) }{\ln (\sqrt {24} + 1) }
$$
which establishes a lower bound on the number of measurements $M$.
````

````{prf:example} Lower bounds on $M$ for RIP of order $2K$
:label: ex-ssm-cs-lb-m-rip-2k-1000

*  $N=1000, K=100 \implies M \geq 65$.
*  $N=1000, K=200 \implies M \geq 91$.
*  $N=1000, K=400 \implies M \geq 104$.
````

Some remarks are in order:

*  The theorem only establishes a necessary lower bound on $M$. It doesn't mean that if we choose an $M$ larger
  than the lower bound then $\Phi$ will have RIP of order $2K$ with any constant $\delta_{2K} \in (0, \frac{1}{2}]$.
*  The restriction $\delta_{2K} \leq \frac{1}{2}$ is arbitrary and is made for convenience. In general, we can work with
  $0 < \delta_{2K} \leq \delta_{\text{max}} < 1$ and develop the bounds accordingly.
*  This result fails to capture dependence of $M$ on the RIP constant $\delta_{2K}$ directly. 
  *Johnson-Lindenstrauss lemma* helps us resolve this which concerns embeddings of finite sets of points in
  low-dimensional spaces.
*  We haven't made significant efforts to optimize the constants. Still they are quite reasonable.

## RIP and NSP



RIP and NSP are connected.
If a matrix $\Phi$ satisfies RIP then it also satisfies NSP
(under certain conditions). 

Thus RIP is strictly stronger than NSP (under certain conditions).

We will need following lemma which applies to any arbitrary $\bh \in \RR^N$.
The lemma will be proved later.

````{prf:lemma}
:label: lem:rip_arbitrary_h

Suppose that $\Phi$ satisfies RIP of order $2K$.
Let $\bh \in \RR^N, \bh \neq \bzero$ be arbitrary.
Let  $\Lambda_0$ be any subset of $\{1,2,\dots, N\}$
such that $|\Lambda_0| \leq K$.

Define $\Lambda_1$ as the index set corresponding to the
$K$ entries of $h_{\Lambda_0^c}$ with largest magnitude,
and set $\Lambda = \Lambda_0 \cup \Lambda_1$.
Then

$$
\| \bh_{\Lambda} \|_2 \leq 
\alpha \frac{\| \bh_{\Lambda_0^c} \|_1 }{ \sqrt{K}} 
+ \beta \frac{| \langle \Phi \bh_{\Lambda}, \Phi \bh \rangle | }{\| \bh_{\Lambda} \|_2},
$$
where

$$
\alpha = \frac{\sqrt{2} \delta_{2K}}{ 1 - \delta_{2K}} , 
\beta = \frac{1}{ 1 - \delta_{2K}}.
$$
````

```{div}
Let us understand this lemma a bit.
If $\bh \in \NullSpace (\Phi)$,
then the lemma simplifies to

$$
\| \bh_{\Lambda} \|_2 \leq \alpha \frac{\| \bh_{\Lambda_0^c} \|_1 }{ \sqrt{K}}
$$


*  $\Lambda_0$ maps to the initial few ($K$ or less) elements we chose.
*  $\Lambda_0^c$ maps to all other elements.
*  $\Lambda_1$ maps to largest (in magnitude) $K$ elements of $\Lambda_0^c$.
*  $h_{\Lambda}$ contains a maximum of $2K$ non-zero elements.
*  $\Phi$ satisfies RIP of order $2K$.
*  Thus 

   $$
   (1 - \delta_{2K}) \| \bh_{\Lambda} \|_2 
   \leq \| \Phi \bh_{\Lambda} \|_2 
   \leq (1 + \delta_{2K}) \| \bh_{\Lambda} \|_2.
   $$
```
We now state the connection between RIP and NSP.

````{prf:theorem}
Suppose that $\Phi$ satisfies RIP of order $2K$ with $\delta_{2K} < \sqrt{2} - 1$.
Then $\Phi$ satisfies the NSP of order $2K$ with constant 

$$
C= \frac
{\sqrt{2} \delta_{2K}}
{1 - (1 + \sqrt{2})\delta_{2K}}
$$
````

````{prf:proof}
We are given that

$$
(1- \delta_{2K}) \| \bx \|^2_2 \leq \| \Phi \bx \|^2_2 \leq (1 + \delta_{2K}) \| \bx \|^2_2  
$$
holds for all $\bx \in \Sigma_{2K}$ where $\delta_{2K}  < \sqrt{2} - 1$.
We have to show that:

$$
\| \bh_{\Lambda}\|_2 \leq C \frac{\| \bh_{{\Lambda}^c}\|_1 }{\sqrt{K}}
$$
holds $\Forall \bh \in \NullSpace (\Phi)$
and $\Forall \Lambda$ such that $|\Lambda| \leq 2K$.

1. Let $\bh \in \NullSpace(\Phi)$.
1. Then $ \Phi \bh = \bzero$. 
1. Let $\Lambda_m$ denote the $2K$ largest entries of $\bh$.
1. Then
   
   $$
    \| \bh_{\Lambda}\|_2  
    \leq \| \bh_{\Lambda_m}\|_2 \Forall \Lambda \ST |\Lambda| \leq 2K. 
   $$
1. Similarly
   
   $$
    \| \bh_{\Lambda^c}\|_1  
    \geq \| \bh_{\Lambda_m^c}\|_1 \Forall \Lambda \ST |\Lambda| \leq 2K. 
   $$
1. Thus if we show that $\Phi$ satisfies NSP of order $2K$ for $\Lambda_m$; i.e.,
   
   $$
    \| \bh_{\Lambda_m}\|_2 \leq C 
    \frac{\| \bh_{{\Lambda_m}^c}\|_1 }{\sqrt{K}}
   $$
   then we would have shown
   it for all $\Lambda$ such that $|\Lambda| \leq 2K$.
1. Hence let $\Lambda = \Lambda_m$.
1. We can divide $\Lambda$ into two components $\Lambda_0$ and $\Lambda_1$ of size $K$ each.
1. Since $\Lambda$ maps to the largest $2K$ entries in $\bh$,
   hence whatever entries we choose in
   $\Lambda_0$, the largest $K$ entries in $\Lambda_0^c$ will be $\Lambda_1$.
1. Hence as per {prf:ref}`lem:rip_arbitrary_h`
   above, we have
   
   $$
    \| \bh_{\Lambda} \|_2 \leq \alpha \frac{\| \bh_{\Lambda_0^c}\|_1}{\sqrt{K}}.
   $$

1. Also 
   
   $$
    \Lambda = \Lambda_0 \cup \Lambda_1 
    \implies \Lambda_0 = \Lambda \setminus \Lambda_1 = \Lambda \cap \Lambda_1^c
    \implies \Lambda_0^c = \Lambda_1 \cup \Lambda^c.
   $$
1. Thus we have
   
   $$
    \| \bh_{\Lambda_0^c} \|_1 = \| \bh_{\Lambda_1} \|_1 + \| \bh_{\Lambda^c} \|_1. 
   $$
1. We have to get rid of $\Lambda_1$.
1. Since $\bh_{\Lambda_1} \in \Sigma_K$, 
   by applying {prf:ref}`lem:u_sigma_k_norms` we get
   
   $$
   \| \bh_{\Lambda_1} \|_1 \leq  \sqrt{K} \| \bh_{\Lambda_1} \|_2
   $$
1. Hence
   
   $$
    \| \bh_{\Lambda} \|_2 \leq 
    \alpha \left ( 
      \| \bh_{\Lambda_1} \|_2 + 
      \frac{\| \bh_{\Lambda^c} \|_1}{\sqrt{K}} 
      \right)
   $$
1. But since $\Lambda_1 \subset \Lambda$,
   hence $ \| \bh_{\Lambda_1} \|_2 \leq  \| \bh_{\Lambda} \|_2$.
1. Hence
   
   $$
    &\| \bh_{\Lambda} \|_2 \leq 
    \alpha \left ( 
      \| \bh_{\Lambda} \|_2 + 
      \frac{\| \bh_{\Lambda^c} \|_1}{\sqrt{K}} 
      \right)\\
    \implies &(1 - \alpha) \| \bh_{\Lambda} \|_2 
    \leq  \alpha \frac{\| \bh_{\Lambda^c} \|_1}{\sqrt{K}}\\
    \implies &\| \bh_{\Lambda} \|_2 
    \leq \frac{\alpha}{1 - \alpha} \frac{\| \bh_{\Lambda^c} \|_1}{\sqrt{K}} 
    \quad \text{ if } \alpha \leq 1.
   $$
1. Note that the inequality is also satisfied for $\alpha = 1$ in which case,
   we don't need to bring $1-\alpha$ to denominator.
1. Now
   
   $$
    &\alpha \leq 1\\
    \implies &\frac{\sqrt{2} \delta_{2K}}{ 1 - \delta_{2K}} \leq 1 \\
    \implies &\sqrt{2} \delta_{2K} \leq 1 - \delta_{2K}\\
    \implies &(\sqrt{2} + 1) \delta_{2K} \leq 1\\
    \implies &\delta_{2K} \leq \sqrt{2} - 1. 
   $$
1. Putting 
   
   $$
      C = \frac{\alpha}{1 - \alpha}  = \frac
      {\sqrt{2} \delta_{2K}}
      {1 - (1 + \sqrt{2})\delta_{2K}}
   $$
   we see that $\Phi$ satisfies NSP of order $2K$
   whenever $\Phi$ satisfies RIP of order $2K$
   with $\delta_{2K} \leq \sqrt{2} -1$.
````
Note that for $\delta_{2K} = \sqrt{2} - 1$, $C=\infty$.


