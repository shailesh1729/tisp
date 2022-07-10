(ch:sparse:signal:models)=
# Sparse Signal Models

```{image} images/concepts.png
:alt: concepts
```

(sec:ssm:outline)=
## Outline

In this chapter we develop initial concepts of sparse signal models.


We begin our study with a review of solutions of under-determined systems.
We build a case for solutions which promote sparsity. 

We show that although the real life signals may not be sparse yet they
are compressible and can be approximated with sparse signals.

We then review orthonormal bases and explain the inadequacy of those bases
in exploiting the sparsity in many signals of interest. We develop an
example of Dirac Fourier basis as a two ortho basis and demonstrate how
it can better exploit signal sparsity compared to Dirac basis and Fourier
basis individually.

We follow this with a general discussion of redundant signal dictionaries. 
We show how they can be used to create sparse and redundant signal representations.

We study various properties of signal dictionaries which are useful in
characterizing the capabilities of a signal dictionary in exploiting signal sparsity.

In this chapter, our signals of interest will typically lie in
the finite $N$-dimensional real or complex vector space $\RR^N$ or $\CC^N$.
Sometimes we will restrict our attention to the $N$ dimensional Euclidean space to simplify discussion.

We will be concerned with different representations of our signals of interest in
$\CC^D$ where $D \geq N$. This aspect will become clearer as we go along in this chapter.


 
## Sparsity
We quickly define the notion of sparsity in a signal.

```{div}
We recall the definition
of $l_0$-"norm" (don't forget the quotes) of $\bx \in \CC^N$ given by

$$
\| \bx \|_0 = \card(\supp(\bx))
$$
where $\supp(x) = \{ i : x_i \neq 0\}$ denotes the support of $\bx$
and $\card$ denotes the cardinality of a set.
Informally we say that a signal $\bx \in \CC^N$ is *sparse*
if $\| \bx \|_0  \ll N$.

More generally if 

$$
\bx = \bDDD \alpha
$$
where $\bDDD \in \CC^{N \times D}$ with
$D > N$ is some signal dictionary (to be formally defined later), then $\bx$ is 
sparse in dictionary $\bDDD$ if $ \| \alpha \|_0 \ll D$. 

Sometimes we simply say that $\bx$ is $K$-sparse if $\| \bx \|_0 \leq K$ where
$K < N$. We do not specifically require that $K \ll N$.

An even more general definition of sparsity is the degrees of freedom a signal
may have.

```{prf:example} Degrees of freedom on the surface of a sphere
:label: ex-ssm-dof-surface-sphere

1. Consider all points on the surface of a unit sphere in $\RR^N$.
1. For every point $\bx$ belonging to the surface, we have $\|\bx \|_2 = 1$.
1. Thus if we choose the values of $N-1$ components of $\bx$ 
   then the value of the remaining component is automatically fixed.
1. Thus the number of degrees of freedom $\bx$ has on the surface of 
   the unit sphere in $\RR^N$ is $N-1$.
1. Such a surface represents a manifold in the ambient Euclidean space. 
1. Of special  interest are low dimensional manifolds 
   where the number of degrees of freedom $K \ll N$.
```


