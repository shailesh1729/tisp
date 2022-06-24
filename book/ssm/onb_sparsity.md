(sec:ssm:sparsity:onb)= 
# Sparsity in Orthonormal Bases

We start this section with a quick review of orthonormal bases and 
orthogonal transforms for finite dimensional 
signals $\bx \in \CC^N$. We look at several examples of sparse signals
in different orthonormal bases. We then demonstrate that
while an orthonormal bases is a complete representation of all signals 
$\bx \in \CC^N$ yet, it is not a good tool for exploiting the sparsity 
in $\bx$ adequately. 

We present an uncertainty principle which explains why a pair of
orthonormal bases (like Dirac and Fourier basis) cannot have sparse
representation of the same signal simultaneously. 

We then demonstrate that a combination of two orthonormal bases can be
quite useful  in creating a redundant yet sparse representation of 
a larger class of signals which could not be sparsely represented
in either of the two bases individually.

This motivates us to discuss more general over-complete signal dictionaries in 
the next section.

 
## Orthonormal Bases and Orthogonal Transforms

In signal processing, we often convert a finite length time domain signal into a different domain 
using finite length transforms. Some of the most common transforms are
*discrete Fourier transform*,
the *discrete cosine transform*, and the *Haar transform*. 
They all belong to the class of transforms called orthogonal transforms.

````{div}
Orthogonal transforms are characterized by a pair of equations

```{math}
:label: eq:ssm:onb:synthesis
\bx  = \Psi \ba
```
and

```{math}
:label: eq:ssm:onb:analysis
\ba  = \Psi^H \bx
```
where $\Psi$ is an *orthonormal basis* for the complex vector space $\CC^N$.
In particular, the columns of $\Psi$ are unit norm, and orthogonal to each other.
Thus if we write

$$
\Psi = \begin{bmatrix} \psi_1 & \psi_2 & \dots & \psi_N \end{bmatrix}
$$
then

$$
\langle \psi_i, \psi_j  \rangle  = \delta(i-j).
$$
In other words: 

$$
    \Psi^{-1} = \Psi^H.
$$

Eq. {eq}`eq:ssm:onb:synthesis` is known as
the synthesis equation ($\bx$ is synthesized by columns of $\Psi$). 
Eq. {eq}`eq:ssm:onb:analysis` is  known as
the analysis equation as we compute the coefficients in $\ba$ by taking
the inner product of $\bx$ with columns of $\Psi$. 

$\Psi$ is known as synthesis operator while $\Psi^H$ is known as analysis operator.
Orthogonal transforms preserve the norm of the signal:

$$
\| \bx \|_2^2 = \| \ba \|_2^2.
$$

This result is commonly known as *Parseval's identity* in signal processing community.

More generally, orthogonal transforms preserve inner products:

$$
\langle \bx, \by \rangle =\langle \Psi \bx, \Psi \by \rangle  \Forall \bx, \by \in \CC^N.
$$
````

````{prf:example} Dirac basis and sparse signals
:label: ex-ssm-dirac-basis-sparsity

The simplest orthogonal transform is the identity basis or the standard ordered
basis for $\CC^N$.

$$
\Psi = \bI_N.
$$
We have

$$
\Psi^{-1} = \Psi^H = \bI_N^H = \bI_N. 
$$

In this basis

$$
\bx  = \bI_N \ba = \ba.
$$
We will drop $N$ from suffix for convenience and refer to the matrix as $\bI$ only.

This basis is also known as *Dirac basis*. The name *Dirac* comes from the
Dirac delta functions used in signal analysis in continuous time domain.

The basis consists of finite length impulses denoted by $\be_i$ where

$$
& \be_1  = (1,0,\dots, 0),\\
& \be_2  = (0,1,\dots, 0),\\
&\vdots\\
& \be_N  = (0,0,\dots, 1)
$$

If a signal $\bx$ consists of a linear combination of few $K \ll N$ impulses, then it is
a sparse signal in this basis. For example the signal

$$
\bx = (3, 4 , 0, 0, -2, 0, 0, \dots, 0 , 0, 0)
$$
is $3$-sparse in Dirac basis since

$$
\bx = 3 \be_1 + 4 \be_2  - 2 \be_5
$$
can be expressed as a linear combination of just 3 impulses.

In contrast if we consider a complex sinusoid in $\CC^N$, there is no way we can 
find a sparse representation for it in the Dirac basis.
````


 
## Fourier Basis and Sparse Signals

````{div}
The most popular finite length orthogonal transform is DFT (Discrete Fourier Transform).

We define the $N$-th root of unity as

$$
\omega = \exp\left(\frac{i 2 \pi }{N} \right).
$$

Clearly

$$
\omega^N  = \exp (i 2 \pi) = 1.
$$

We define the synthesis matrix of DFT as 

$$
\Psi = \bF_N 
= \frac{1}{\sqrt{N}} 
\begin{bmatrix} \omega^{kn} \end{bmatrix} \Forall 0 \leq k \leq N-1, 0 \leq n \leq N-1
$$
where 

$$
\omega^{kn}  = \exp\left(\frac{i 2 \pi  kn }{N}\right).
$$
$k$ iterates over rows of $\bF_N$ while $n$ iterates over columns of $\bF_N$.

The definition is symmetric. Hence

$$
\bF_N = \bF_N^T.
$$
Note that we have multiplied with
$\frac{1}{\sqrt{N}}$ to make sure that columns of $\bF_N$ are unit norm.

The columns of $\bF_N$ form the *Fourier basis* for signals in $\CC^N$.
````

````{prf:example} Fourier basis for $N=2$
:label: ex-ssm-fourier-basis-2

2nd root of unity is given by

$$
\omega = \exp(i \pi) = -1.
$$
Hence

$$
\bF_2 = 
\frac{1}{\sqrt{2}}
\begin{bmatrix}
\omega^0 & \omega^0\\
\omega^0 & \omega^1\\
\end{bmatrix}
=
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1\\
1 & -1\\
\end{bmatrix}
$$

In this case

$$
\bF_2^H = \bF_2.
$$
````

````{prf:example} Fourier basis for $N=3$
:label: ex-ssm-fourier-basis-3

3rd root of unity is given by

$$
\omega = \exp\left(\frac{i 2\pi}{3}\right) = -0.5 + 0.866 i.
$$
Hence

$$
\bF_3 = 
\frac{1}{\sqrt{3}}
\begin{bmatrix}
\omega^0 & \omega^0 & \omega^0\\
\omega^0 & \omega^1 & \omega^2\\
\omega^0 & \omega^2 & \omega^4
\end{bmatrix}
=
\frac{1}{\sqrt{3}}
\begin{bmatrix}
1 & 1 & 1\\
1 & -0.5  + 0.866 i & -0.5  - 0.866 i\\
1 & -0.5 - 0.866 i & -0.5 + 0.866 i
\end{bmatrix}
$$
In this case

$$
\bF_3^H = 
\frac{1}{\sqrt{3}}
\begin{bmatrix}
1 & 1 & 1\\
1 & -0.5  - 0.866 i & -0.5  + 0.866 i\\
1 & -0.5 + 0.866 i & -0.5 - 0.866 i
\end{bmatrix}
$$
````

````{prf:example} Fourier basis for $N=4$
:label: ex-ssm-fourier-basis-4

4th root of unity is given by

$$
\omega = \exp\left(\frac{i 2\pi}{4}\right) =  i.
$$
Hence

$$
\bF_4 = 
\frac{1}{2}
\begin{bmatrix}
\omega^0 & \omega^0 & \omega^0 & \omega^0\\
\omega^0 & \omega^1 & \omega^2 & \omega^3\\
\omega^0 & \omega^2 & \omega^4 & \omega^6\\
\omega^0 & \omega^3 & \omega^6 & \omega^9
\end{bmatrix}
=
\frac{1}{2}
\begin{bmatrix}
\omega^0 & \omega^0 & \omega^0 & \omega^0\\
\omega^0 & \omega^1 & \omega^2 & \omega^3\\
\omega^0 & \omega^2 & 1 & \omega^2\\
\omega^0 & \omega^3 & \omega^2 & \omega^1
\end{bmatrix}
=
\frac{1}{2}
\begin{bmatrix}
1 & 1 & 1 & 1\\
1 & i & -1 & -i \\
1 & -1 & 1 & -1\\
1 & -i & -1 & i
\end{bmatrix}
$$
In this case

$$
\bF_4^H = 
\frac{1}{2}
\begin{bmatrix}
1 & 1 & 1 & 1\\
1 & -i & -1 & i \\
1 & -1 & 1 & -1\\
1 & i & -1 & -i
\end{bmatrix}
$$
````

We drop the suffix $N$ wherever convenient and simply refer to the synthesis matrix as $\bF$.

If a signal $\bx$ is a linear combination of only a few ($K \ll N$) complex sinusoids,
then $\bx$ has a sparse representation in the DFT basis $\bF$.

````{prf:example} Sparse signals in $\bF$
:label: ex-ssm-fourier-basis-sparse-signals

Consider the following signal

$$
\bx  = \begin{pmatrix}
 -0.5 &  0.5 - i & 1.5  & 0.5 + i
\end{pmatrix}
$$

Its representation in $\bF_4$ is given by

$$
\ba = \bF_4^H \bx = \begin{pmatrix}1 & -2 & 0 & 0\end{pmatrix}.
$$

Clearly the signal is $2$-sparse in $\bF_4$.

Now consider a signal $\be_2$ which is sparse in the Dirac basis

$$
\be_2 = \begin{pmatrix}
 0 & 1 & 0 & 0
\end{pmatrix}.
$$

Its representation in $\bF_4$ is 

$$
\ba = \bF_4^H \be_2 =  \begin{pmatrix}
 0.5 & 0.5 i & -0.5 & 0.5 i
\end{pmatrix}.
$$
Thus we see that while $\be_2$ is sparse in $\bI_4$, it is 
not at all sparse in $\bF_4$.
````

## An Uncertainty Principle

```{div}
As we noted, Dirac basis can give sparse representations for impulses but
not for complex sinusoids. Vice versa Fourier basis can give sparse
representations for complex sinusoids but not impulses. 

Can we claim that a signal cannot be simultaneously represented 
both in time (Dirac basis) and in frequency domain (Fourier basis)?

More generally, let $\Psi$ and $\Chi$ be any two arbitrary orthonormal bases for $\CC^N$. 
For some $\bx \in \CC^N$, let  

$$
\bx = \Psi \ba = \Chi \bb
$$
where $\ba$ and $\bb$ are representations of $\bx$ in $\Psi$ and $\Chi$ respectively. 
Can we claim something for the relationship between sparsity levels $\| \ba \|_0$ and $\| \bb \|_0$? 

The answer turns out to be yes, but it depends on how much the two bases are similar or close to each other.
The results in this section were originally developed in {cite}`elad2002generalized`.
```

```{index} Mutual coherence, Proximity
```
````{prf:definition} Proximity/Mutual coherence
:label: def-ssm-mutual-coherence-two-ortho-bases

The *proximity* between two orthonormal bases $\Psi$ and $\Chi$ where

$$
\Psi = \begin{bmatrix}
\psi_1 & \dots & \psi_N
\end{bmatrix}
$$
and 

$$
\Chi = \begin{bmatrix}
\chi_1 & \dots & \chi_N
\end{bmatrix}
$$

is defined as the maximum absolute value of inner products between the columns of these two bases:

$$
\mu (\Psi, \Chi) = \underset{1 \leq i, j \leq N}{\max} | \langle \psi_i, \chi_j \rangle |.
$$
This is also known as *mutual coherence* of the two orthonormal bases.
````

If the two bases are identical, then clearly $\mu = 1$. If any vector in $\Psi$ is very close
to some vector in $\Chi$ then we will have a very high value of $\mu$ (close to 1). 

If the vectors in $\Psi$ and $\Chi$ are highly dissimilar, then we will have very low
value of $\mu$ close to 0.

````{prf:example} Proximity or mutual coherence of Dirac and Fourier bases
:label: ex-ssm-proximity-dirac-fourier-bases

Consider the mutual coherence between Dirac and Fourier bases. 

For some small values of $N$ (the dimension of ambient space $\CC^N$) the values are tabulated in
below.

| N | $\mu$ |
| --- | --- |
| 2 | 0.7071| 
| 4 | 0.5000| 
| 6 | 0.4082 | 
| 8 | 0.3536| 

For larger values of $N$ we can see the variation of $\mu$ in the plot below.
```{figure} images/coherence_dirac_fourier_bases.png
---
name: fig:ssm:coherence:dirac:fourier:bases
---
Mutual coherence for Dirac and Fourier bases 
```
````
We present some results related to mutual coherence of two orthonormal bases.

````{prf:theorem} Product of orthonormal bases
:label: res-ssm-product-two-ortho-bases

The product of two orthonormal bases $\Psi$ and $\Chi$ for $\CC^N$ given by
$\Psi^H \Chi$ forms an orthonormal basis by itself.
````

````{prf:proof}
Consider the matrix $\Psi^H \Chi$ 

$$
\Psi^H \Chi = 
\begin{bmatrix}
\psi_1^H \\ \dots \\ \psi_N^H
\end{bmatrix} 
\begin{bmatrix}
\chi_1 &  \dots &  \chi_N
\end{bmatrix}
= 
\begin{bmatrix}
\psi_1^H \chi_1 & \psi_1^H \chi_2 & \dots & \psi_1^H \chi_N\\
\psi_2^H \chi_1 & \psi_2^H \chi_2 & \dots & \psi_2^H \chi_N\\
\vdots & \vdots & \ddots & \vdots \\ 
\psi_N^H \chi_1 & \psi_N^H \chi_2 & \dots & \psi_N^H \chi_N
\end{bmatrix}
$$
Any column of the product matrix is

$$
\begin{bmatrix}
\psi_1^H \chi_i \\ 
\psi_2^H \chi_i \\ 
\vdots & \vdots \\
\psi_N^H \chi_i 
\end{bmatrix}
= \Psi^H \chi_i
$$

But then $\Psi$ preserves norms, hence

$$
\| \Psi^H \chi_i \|_2 = \| \chi_i \|_2  = 1. 
$$

Thus each column of the product $\Psi^H \Chi$ is itself a unit norm vector.

Consider the inner product of two columns of $\Psi^H \Chi$

$$
\langle \Psi^H \chi_i, \Psi^H \chi_j \rangle = \chi_j^H \Psi \Psi^H \chi_i = \chi_j^H \chi_i = \delta(i - j).
$$
Thus, the columns of $\Psi^H \Chi$ are orthogonal to each other.

Hence $\Psi^H \Chi$ forms an orthonormal basis.
````

````{prf:remark} The group of orthonormal bases
:label: rem-ssm-onb-group

A more general result would be to show that the set of orthonormal bases forms a group
under the matrix multiplication operation.
The identity element is the Dirac basis. The inverse of an orthonormal basis is
also an orthonormal basis. The product of two orthonormal bases is also an orthonormal basis.
The matrix multiplication satisfies associative law.
````

````{prf:theorem} Mutual coherence bounds
:label: res-ssm-2-onb-coherence-bounds

Mutual coherence of two orthonormal bases $\Psi$ and $\Chi$ for the complex
vector space $\CC^N$ is bounded by

```{math}
:label: eq:ssm:bound_two_ortho_basis_mutual_coherence
\frac{1}{\sqrt{N}} \leq \mu(\Psi, \Chi) \leq 1.
```
````

````{prf:proof}
Since columns of both $\Psi$ and $\Chi$ are unit norm,
hence $|\langle \psi_i, \chi_j \rangle |$ 
cannot be greater than 1.

Now if $\Psi = \Chi$ then we have $\mu(\Psi, \Chi) = 1$. This proves the upper bound.

Now consider the matrix $\Psi^H \Chi$ which forms an orthonormal basis by itself. 
Consider any column of this matrix

$$
\begin{bmatrix}
\psi_1^H \chi_i \\ 
\psi_2^H \chi_i \\ 
\vdots & \vdots \\
\psi_N^H \chi_i 
\end{bmatrix}
= \Psi^H \chi_i
$$

Since the column is unit norm, hence some of squares of the absolute values of entries of the column is 1.
Thus the absolute value of each of the entries cannot be simultaneously less than $\frac{1}{\sqrt{N}}$.

Hence there exists an entry (in each column) such that

$$
|\psi_j^H \chi_i | \geq  \frac{1}{\sqrt{N}}.
$$
Hence we get the lower bound on mutual coherence of $\Psi$ and $\Chi$ given by

$$
\mu (\Psi, \Chi) \geq \frac{1}{\sqrt{N}}.
$$
````

````{prf:theorem} Mutual coherence of Dirac and Fourier bases
:label: res-ssm-coherence-dirac-fourier

Mutual coherence of Dirac and Fourier bases is $\frac{1}{\sqrt{N}}$.

$$
\mu(\bI_N, \bF_N) = \frac{1}{\sqrt{N}}.
$$
````

````{prf:proof}
{prf:ref}`res-ssm-2-onb-coherence-bounds` shows that

$$
\mu(\bI_N, \bF_N) \geq \frac{1}{\sqrt{N}}.
$$
We just need to show that its in fact an equality.

Consider $i$-th column of $\bI$ as $\be_i$. 

Consider $j$-th column of $\bF$:

$$
\bf_j = 
\frac{1}{\sqrt{N}}
\begin{bmatrix}
\omega^{0} \\ 
\omega^{j}  \\
\omega^{2 j} \\
\vdots \\
\omega^{(N-1)j}
\end{bmatrix}
$$
where $\omega$ is the $N$-th root of unity.
Then 

$$
\langle \be_i,  \bf_j \rangle = \frac{1}{\sqrt{N}} \omega^{-(i-1)j}
\implies |\langle e_i,  f_j \rangle| = \frac{1}{\sqrt{N}}.
$$
This doesn't depend on the choice of $i$-th column of $\bI_N$ and $j$-th column of 
$\bF_N$.
Hence

$$
\mu(\bI_N, \bF_N) = \frac{1}{\sqrt{N}}.
$$
````

With basic properties of mutual coherence in place, we are now ready to state
an uncertainty principle on the sparsity levels of representations of same signal
$x$ in two different orthonormal bases:

````{prf:theorem} Uncertainty principle
:label: res-ssm-uncertainty-principle-2-onb-mu

For any arbitrary pair of orthonormal bases $\Psi$, $\Chi$ with mutual coherence
$\mu(\Psi, \Chi)$, and for any arbitrary non-zero vector $\bx \in \CC^N$ with representations
$\ba$ and $\bb$ respectively, the following inequality holds true:

```{math}
:label: eq-ssm-l0-uncertainty-mu-2-onb
\| \ba \|_0 + \| \bb \|_0 \geq \frac{2}{\mu(\Psi, \Chi)}.
```

Moreover for unit-length $\bx$ we have:

```{math}
:label: eq:ssm:l1_uncertainty_principle_coherence_two_ortho_basis
\| \ba \|_1 + \| \bb \|_1 \geq \frac{2}{\sqrt{\mu(\Psi, \Chi)}}.
```
````

````{prf:proof}
Dividing $\bx$ by $\| \bx \|_2$ doesn't change $\ell_0$ "norm" of $\ba$ and $\bb$. i.e.,

$$
\left \| \frac{\ba}{\| \bx \|_2} \right \|_0 = \| \ba \|_0. 
$$

Hence without loss of
generality, we will assume that $\| \bx \|_2 = 1$.

We are given that $\bx^H \bx = 1$, $\bx = \Psi \ba$ and $\bx = \Chi \bb$. 
Since $\Psi$ and $\Chi$ are orthonormal bases hence $\| \ba \|_2 = \| \bb \|_2 = 1$ also.

We can write

$$
1 &= \bx^H \bx\\
&= (\Psi \ba)^H (\Chi \bb) = \ba ^H \Psi^H \Chi \bb\\
&= \sum_{i=1}^N \sum_{j=1}^N \overline{a_i} b_j \psi_i^H \chi_j\\
&= \left | \sum_{i=1}^N \sum_{j=1}^N \overline{a_i} b_j \psi_i^H \chi_j \right |\\
&\leq \sum_{i=1}^N \sum_{j=1}^N |a_i | |b_j | |\psi_i^H \chi_j |\\
&\leq \mu(\Psi, \Chi)\sum_{i=1}^N \sum_{j=1}^N | a_i | |b_j | \\
&= \mu(\Psi, \Chi) \| \ba \|_1 \| \bb \|_1
$$

where we note that

$$
\| \ba \|_1 \| \bb \|_1 = \left (\sum_{i=1}^N |a_i | \right) \left (\sum_{j=1}^N |b_j | \right)
= \sum_{i=1}^N \sum_{j=1}^N | a_i | |b_j |
$$
and

$$
\mu(\Psi, \Chi)  \geq |\psi_i^H \chi_j |.
$$
Hence we get the inequality

$$
\mu(\Psi, \Chi) \| \ba \|_1 \| \bb \|_1 \geq 1
$$
Using the inequality between algebraic mean and geometric mean 

$$
\sqrt{ab} \leq \frac{a + b}{2} \Forall a, b \geq 0
$$
we get

$$
\| \ba \|_1 + \| \bb \|_1 \geq 2 \sqrt{\| \ba \|_1 \| \bb \|_1} \geq \frac{2}{\sqrt{\mu(\Psi, \Chi)}}.
$$
This is an uncertainty principle for the $\ell_1$ norms of the two representations. 
We still have to get the uncertainty principle for $\ell_0$ case.
Let

$$
\| \ba \|_0  = A 
\text{ and }
\| \bb \|_0 = B
$$
Consider the sets

$$
X_A = \{ \by \ST \by = \Psi \bu  \text{ and }  \| \bu \|_0 = A, \|\bu\|_2 = 1\}
$$
and

$$
X_B = \{ \by : \by = \Chi \bv  \text{ and }  \| \bv \|_0 = B, \|\bv\|_2 = 1\}.
$$
Clearly 

$$
\bx \in X_A \cap X_B.
$$
The representations $\bu$ for vectors $\by$ in $X_A$ have exactly $A$ non-zero entries and 
are all unit norm representations. 
Which of them would have the longest $\ell_1$ norm $\| \bu \|_1$?

This can be written as an optimization problem of the form 

```{math}
:label: eq-ssm-uncertainty-opt-prob-a-psi
\underset{\by \in X_A}{\text{maximize}} 
\| \bu \|_1 \text{ where } \bu = \Psi^H \by.
```

Let the optimal solution for this problem be $\bv_a$
with corresponding representation $\ba^* = \Psi^H \bv_a$. Clearly

$$
\| \ba^* \|_1 \geq \| \ba \|_1.
$$
Similarly from the set $X_B$ let us find the vector $\bv_b$ with maximum
$\ell_1$ norm representation in $\Chi$

```{math}
:label: eq-ssm-uncertainty-opt-prob-a-chi

\underset{\by \in X_B}{\text{maximize}} 
\| \bv \|_1 \text{ where } \bv = \Chi^H \by.
```
Let the optimal solution for this problem be $\bv_b$
with corresponding representation $\bb^* = \Chi^H \bv_b$.
Clearly

$$
\| \bb^* \|_1 \geq \| \bb \|_1.
$$

Returning back to the inequality

$$
\| \ba \|_1 \| \bb \|_1 \geq \frac{1}{\mu(\Psi, \Chi)}
$$
we can write

$$
\| \ba^* \|_1 \| \bb^* \|_1 \geq \frac{1}{\mu(\Psi, \Chi)}.
$$
An equivalent formulation of the optimization problem
{eq}`eq-ssm-uncertainty-opt-prob-a-psi`is

```{math}
:label: eq-ssm-uncertainty-opt-prob-b-psi
& \underset{a}{\text{maximize}} 
& &  \| \ba \|_1 \\
& \text{subject to }
& &  \| \ba \|_2^2 = \ba^H \ba = 1\\
& \text{and }
& & \|\ba \|_0 = A.
```
This formulation doesn't require any specific mention of the basis $\Psi$.
Let the optimal value for this problem be given by

$$
\| \ba^* \|_1 = g(A) = g(\| \ba \|_0)
$$
Here we consider the optimization problem to be parameterized by the $\ell_0$-"norm" of $\ba$;
i.e., 
$\| \ba \|_0 = A$ and we write the optimal value as a function $g$ of the parameter $A$.

Then by symmetry, optimal value for the problem {eq}`eq-ssm-uncertainty-opt-prob-a-chi` is

$$
\| \bb^* \|_1 = g(B) = g(\| \bb \|_0)
$$
Thus we can write

```{math}
:label: eq-ssm-intermediate-bound-l0-norm-products
g(\| \ba \|_0) g(\| \bb \|_0) \geq  \frac{1}{\mu(\Psi, \Chi)}.
```
This is our intended result since we have been able to write the inequality as 
a function of $\ell_0$ "norm"s of the representations $\ba$ and $\bb$.

In order to complete the result, we need to find the solution of the
optimization problem {eq}`eq-ssm-uncertainty-opt-prob-b-psi` given 
by the function $g$.

Without loss of generality, let us assume that the $A$ non-zero entries
in the optimization variable $\ba$ appear in its first $A$ entries and rest are zero. 
This is fine since changing the 
order of entries in $\ba$ doesn't affect any of the norms of concern $\| \ba \|_0$, $\| \ba \|_1$
and $\| \ba \|_2$.

Let us further assume that all non-zero entries of $\ba$ are strictly positive real numbers.
This assumption is valid since only absolute values are used in this problem. Specifically
for any $\ba$ with non-zero complex entries $(a_1, a_2, \dots, a_A, 0, \dots, 0)$ there
exists $\ba'$ with positive entries $(|a_1|, |a_2|, \dots, |a_A|, 0, \dots, 0)$ such that
$\|\ba\|_0 = \|\ba'\|_0$, $\|\ba\|_1 = \|\ba'\|_1$ and $\|\ba\|_2 = \|\ba'\|_2$,
hence solving the optimization
problem for complex $\ba$ is same as solving the optimization problem for 
$\ba$ with strictly positive first $A$ entries.

Using Lagrange multipliers, the $\ell_0$ constraint vanishes (since the assumptions
mentioned above allow us to focus on only the first $A$ coordinates of $\ba$), and
we obtain

$$
\LLL(\ba) = \sum_{i=1}^{A} a_i + \lambda \left(1 - \sum_{i=1}^A a_i^2\right).
$$
Differentiating w.r.t. $a_i$ and equating to 0 we get

$$
1 - 2 \lambda a_i = 0 \implies a_i = \frac{1}{2\lambda}.
$$
The $\ell_2$ constraint requires 

$$
\sum_{i=1}^A a_i^2 = A \frac{1}{4 \lambda^2} = 1 \implies \lambda = \frac{\sqrt{A}}{2 }
$$
Thus 

$$
a_i = \frac{1}{\sqrt{A}}
$$
and 

$$
\| \ba \|_1 = \sum_{i=1}^A |a_i| = \sqrt{A}.
$$
Thus the optimal value of the optimization problem {eq}`eq-ssm-uncertainty-opt-prob-b-psi` is

$$
g(A) = \sqrt{A} = \sqrt{\|\ba \|_0}.
$$
Similarly

$$
g(B) = \sqrt{B} = \sqrt{\|\bb \|_0}.
$$
Putting back in {eq}`eq-ssm-intermediate-bound-l0-norm-products` we get

$$
\sqrt{\| \ba \|_0 \| \bb \|_0} \geq  \frac{1}{\mu(\Psi, \Chi)}.
$$
Applying the algebraic mean-geometric mean inequality we get the desired result

$$
\| \ba \|_0 + \| \bb \|_0 \geq \frac{2}{\mu(\Psi, \Chi)}.
$$
````

This  theorem suggests that if two orthonormal bases have low mutual coherence then

*  the two representations for $\bx$ cannot be jointly $l_1$-short and
*  the two representations for $\bx$ cannot be jointly sparse.

```{admonition} Challenge
Can we show that the above result is sharp? i.e. For a pair of orthonormal bases
$\Psi$ and $\Chi$, it is always possible to find a non-zero vector $\bx$ with corresponding
representations $\bx = \Psi \ba$ and $\bx = \Chi \bb$ which satisfies the lower bound

$$
\| \ba \|_0 + \| \bb \|_0 = \frac{2}{\mu(\Psi, \Chi)}?
$$
```

````{prf:example} Sparse representations with Dirac and Fourier bases
:label: ex-ssm-dirac-fourier-sparse-rep-2

We showed in {prf:ref}`res-ssm-coherence-dirac-fourier`
that 

$$
\mu(\bI, \bF) = \frac{1}{\sqrt{N}}.
$$
Let $\bx \in \CC^N$. Let its representation in $\bF$ be given by

$$
\bx = \bF \ba.
$$

Applying {prf:ref}`res-ssm-uncertainty-principle-2-onb-mu` we have

$$
\| \bx \|_0 + \| \ba \|_0 \geq \frac{2}{\mu(\Psi, \Chi)} = 2 \sqrt{N}.
$$

This tells us that a signal cannot have fewer than $2 \sqrt{N}$ non-zeros in 
time and frequency domain together.
````
 
## Linear Combinations of Impulses and Sinusoids

What happens if a signal $\bx$ is a linear combination of few complex sinusoids 
and few impulses?

The set of sinusoids and impulses involved in the construction of $\bx$ actually
specifies the degrees of freedom of $\bx$. This is the indicator of inherent
sparsity of $\bx$ provided this set of component signals of $\bx$ is known 
a priori.

In absence of prior knowledge of component signals of $\bx$, we attempt to
look for a sparse representation of $\bx$ in one of the well understood
orthonormal bases. Here we are specifically looking at the two bases
Dirac and Fourier.

While the Dirac basis can provide sparse representation for impulses,
sinusoids have dense representation in Dirac basis. Vice versa, 
in Fourier basis, complex sinusoids have sparse representation, yet
impulses have dense representations. Thus neither of the two bases
is capable of providing a sparse representation for a combination
of impulses and sinusoids.

The natural question arises if there is a way to come up with a sparse
representation for such signals by combining the Dirac and Fourier basis? 


(sec:ssm:dirac:fourier:basis)=
## Dirac Fourier Basis

Now we develop a representation of signals $\bx \in \CC^N$ 
in terms of a combination of Dirac basis $\bI$ and Fourier 
basis $\bF$.

We define a new synthesis matrix

```{math}
:label: eq-ssm-dirac-fourier-synthesis-matrix
\bH = \begin{bmatrix}
\bI & \bF
\end{bmatrix}
\in \CC^{N \times 2 N}.
```
We can write $\bI$ as

$$
\bI = \begin{bmatrix}
\be_1 &\dots & \be_N
\end{bmatrix}
$$
and $\bF$ as

$$
\bF = \begin{bmatrix}
\bf_1 &\dots & \bf_N
\end{bmatrix}.
$$
This enables us to write $\bH$ as

$$
\bH = \begin{bmatrix}
\be_1 &\dots & \be_N & \bf_1 &\dots & \bf_N
\end{bmatrix}.
$$
We will look for a representation of $\bx$
using the synthesis matrix $\bH$ as

$$
\bx  = \bH \ba
$$
where $\ba \in \CC^{2N}$.

Since this representation is under-determined and $\ColSpace (\bH ) = \CC^N$ hence
there are always infinitely many possible representations of $\bx$ in $\bH$.

We would prefer to choose the sparsest representation which can be stated as an
optimization problem

```{math}
:label: eq-ssm-df-sparse-rep-prob
& \underset{\ba}{\text{minimize}} 
& &  \| \ba \|_0 \\
& \text{subject to }
& &  \bx = \bH \ba.
```

````{prf:example} Sparse representation using Dirac Fourier Basis
:label: ex-ssm-sparse-rep-with-df-basis

Let $N=4$.
Then the Dirac Fourier basis is

$$
\bH = 
\begin{bmatrix}
1 & 0 & 0 & 0 & .5 & .5 & .5 & .5\\
0 & 1 & 0 & 0 & .5 & .5 i & -.5 & -.5 i \\
0 & 0 & 1 & 0 & .5 & -.5 & .5 & -.5\\
0 & 0 & 0 & 1 & .5 & -.5 i & -.5 & .5 i
\end{bmatrix}
$$
Let 

$$
\bx = 3 \be_1  - 2 \bf_2 = 
\begin{pmatrix}
2  & -i & 1 & i
\end{pmatrix}.
$$
A sparse representation of $\bx$ in $\bH$ is

$$
\ba = \begin{pmatrix}
3 & 0 & 0 & 0 & 0 & -2 & 0 & 0
\end{pmatrix}.
$$
This representation is $2$-sparse.

Thus we see that Dirac Fourier basis is able to provide a sparser representation 
of a linear combination of impulses and sinusoids compared to individual 
orthonormal bases (the Dirac basis and the Fourier basis).
````

This gives us motivation to consider such combination of bases which help us
provide a sparse representation to a larger class of signals. This is the
objective of the next section.

In due course we will revisit the Dirac Fourier basis further in several examples.

 
## Two-Ortho Basis
Before we leave this section, let us define general two-ortho bases.

```{index} Two ortho basis
```
````{prf:definition} Two ortho basis
:label: def-ssm-two-ortho-basis

Let $\Psi$ and $\Chi$ be any two $\CC^{N \times N}$ matrices 
whose columns vectors form orthonormal bases 
for the complex vector space $\CC^N$ individually.

We define 

```{math}
:label: eq-ssm-two-ortho-synthesis-matrix

\Eta = \begin{bmatrix}
\Psi & \Chi
\end{bmatrix}
\in \CC^{N \times 2 N}.
```
The columns of $\Eta$ form a *two-ortho basis* for $\CC^N$.
````
Clearly columns of $\Eta$ span $\CC^N$. 

```{prf:remark} Coherence of a two ortho basis
The *coherence* of a two ortho basis is defined as

$$
\mu (\Eta )  = \mu( \Psi, \Chi).
$$
It is the magnitude of the largest inner product between
columns of $\Eta$.
```
We present a very interesting result about the null space of $\Eta$.

````{prf:theorem} Denseness of vectors in null space of two ortho bases
:label: res-ssm-2onb-nullspace-vec-sparsity

For a two ortho basis $\Eta = \begin{bmatrix}\Psi & \Chi \end{bmatrix}$ with low coherence, 
the non-zero vectors in the null space of $\Eta$ are not sparse.

Concretely

$$
\| \bv \|_0 \geq \frac{2}{\mu(\Eta)} \Forall \bv \in \NullSpace(\Eta).
$$
````

````{prf:proof}
Let $\bv \in \NullSpace(\Eta)$ be some non-zero vector.

Now let $\bv_{\psi}$ and $\bv_{\chi}$ be first N and last N entries of $\bv$. 
Then

$$
\begin{bmatrix}
\Psi & \Chi
\end{bmatrix}
\begin{bmatrix}
\bv_{\psi}\\
\bv_{\chi}
\end{bmatrix}
= \bzero
\implies 
\Psi \bv_{\psi} = - \Chi \bv_{\chi} = \by \neq \bzero.
$$

If $\by$ were $\bzero$,
then both $\bv_{\psi}$ and $\bv_{\chi}$ would have to be $\bzero$ which is not
the case since by assumption $\bv \neq \bzero$.

We note that $\bv_{\psi}$ and $-\bv_{\chi}$ are representations of same vector $\by$ in two different
orthonormal bases $\Psi$ and $\Chi$ respectively, and $\| -\bv_{\chi}\|_0 = \| \bv_{\chi} \|_0$.

Applying {prf:ref}`res-ssm-uncertainty-principle-2-onb-mu` we have

$$
\| \bv \|_0 = \| \bv_{\psi} \|_0 + \| \bv_{\chi} \|_0 \geq \frac{2}{\mu(\Eta)}.
$$
We also note that since the orthonormal bases preserve norm, hence

$$
\| \by \|_2 = \| \bv_{\psi} \|_2 =  \| \bv_{\chi} \|_2.
$$
This shows us that the energy of a null space vector is evenly distributed in the two 
components corresponding to each orthonormal basis.
````

```{admonition} Challenge
For a two-ortho basis $\Eta = \begin{bmatrix}\Psi & \Chi \end{bmatrix}$
is it possible to find a null space vector $\bv$ satisfying the lower bound

$$
\| \bv \|_0 = \frac{2}{\mu(\Eta)}?
$$
```
Let $\bx \in \CC^N$ be any arbitrary signal.
Then its representation in $\Eta$ is given by

$$
\bx = \Eta \ba.
$$
Obviously for every $\bz \in \NullSpace(\Eta)$,
the vector $\ba + \bz$ is also a representation of $\bx$.

What we are particularly interested in are sparse representations of $\bx$. A key
concern for us is to ensure that a sparse representation of $\bx$ in $\Eta$ is unique. 
Under what conditions such is possible? 

Formally, let $\ba$ and $\bb$ be two different representations of $\bx$ in 
$\Eta$. Can we say that if $\ba$ is sparse then $\bb$ won't be sparse? 

This is established in the next uncertainty principle.

````{prf:theorem} Uncertainty principle for representations in two ortho basis
:label: res-ssm-uncertainty-principle-distinct-reps-2onb

Let $\bx \in \CC^N$ be any signal and let $\Eta$ be a two ortho basis defined in 
{eq}`eq-ssm-two-ortho-synthesis-matrix`.
Let $\ba$ and $\bb$ be two distinct representations of
$\bx$ in $\Eta$ i.e.

$$
\bx = \Eta \ba  = \Eta \bb.
$$
Then the following holds

$$
\| \ba \|_0 + \| \bb \|_0 \geq \frac{2}{\mu(\Eta)}.
$$
This is an uncertainty principle for the sparsity of distinct representations in two ortho basis. 
````

````{prf:proof}
Let

$$
\be = \ba - \bb
$$
be the difference vector of representations of $\bx$.
Clearly

$$
\Eta \be  = \Eta \ba - \Eta \bb = \bx - \bx = \bzero.
$$

Thus $\be \in \NullSpace(\Eta)$.
Applying {prf:ref}`res-ssm-2onb-nullspace-vec-sparsity`, we get

$$
\| \be \|_0 \geq \frac{2}{\mu(\Eta)}.
$$

But since $\be = \ba - \bb$ hence we have

$$
\| \ba  \|_0 + \| \bb \|_0 \geq \| \be \|_0 \geq \frac{2}{\mu(\Eta)}.
$$
````

```{admonition} Challenge
For a two-ortho basis $\Eta = \begin{bmatrix}\Psi & \Chi \end{bmatrix}$
is it possible to find a vector $\bx$ with two alternative
representations $\ba$ and $\bb$ satisfying the lower bound

$$
\| \ba \|_0 + \| \bb \|_0 = \frac{2}{\mu(\Eta)} ?
$$
```
This theorem suggests as that if $\mu(\Eta)$ is small (i.e. the coherence
between the two orthonormal bases is small) then two representations of $\bx$ 
cannot be simultaneously sparse. 

Rather if a representation is sufficiently sparse, then all other representations
of $\bx$ are guaranteed to be non-sparse providing the uniqueness of sparse representation.

This is stated formally in the following *uniqueness* theorem.

````{prf:theorem} Uniqueness of sparse representation in two ortho basis
:label: res-ssm-sparse-unique-2onb

If a representation of $\bx$ in the two ortho basis
$\Eta = \begin{bmatrix}\Psi & \Chi \end{bmatrix}$ 
has fewer than $\frac{1}{\mu(\Eta)}$ non-zero entries,
then it is necessarily the sparsest one possible, and any other representation must be denser.
````
````{prf:proof}
Let $\ba$ be a candidate representation with

$$
\| \ba \|_0 < \frac{1}{\mu(\Eta)}.
$$
Let $\bb$ be any other candidate representation.
By applying {prf:ref}`res-ssm-uncertainty-principle-distinct-reps-2onb`
we have 

$$
\| \ba  \|_0 + \| \bb \|_0  \geq \frac{2}{\mu(\Eta)}.
$$
This gives us

$$
\| \bb \|_0 \geq \frac{2}{\mu(\Eta)} - \| \ba  \|_0 
\implies \| \bb \|_0  > \frac{1}{\mu(\Eta)}.
$$
Thus we find that

$$
\| \bb \|_0 > \| \ba  \|_0
$$
which is true for every representation $\bb$ of $\bx$ in $\Eta$ other than 
$\ba$.

Hence $\ba$ is the sparsest possible representation of $\bx$ in $\Eta$.
````

We note here that any arbitrary choice of two bases may not be helpful
in coming up with a two ortho basis which can provide us sparse
representations for our signals of interest. In next few sections, we will
explore this issue further in the more general context of signal dictionaries.

```{admonition} Challenge
Clearly, are signals for which a sufficiently sparse (and unique) representation
doesn't exist in a given two-ortho basis. What kind of relationships may exist
between different (insufficiently) sparse representations of such signals?
```