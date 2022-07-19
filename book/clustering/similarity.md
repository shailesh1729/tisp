# Similarity Measures

This section provides a review of popular similarity
and dissimilarity measures in literature.

## Introduction

### Similarity Function

The following is an informal definition of a similarity function.

```{index} Similarity function
```
```{prf:definition} Similarity function
:label: def-ml-cl-similarity-function

Let $\bX$ be a dataset of $n$ data points sampled from
the Euclidean space $\RR^m$. Then a *similarity function*
is some function $s : \RR^m \times \RR^m \to \RR$ for
any pair of data points $\bx, \by \in \RR^m$
with a structure

$$
s(\bx, \by) = s(x_1, \dots, x_d, y_1, \dots, y_d)
$$
which grows as the data points look similar to each other
and satisfies the following properties

1. $0 \leq s(\bx, \by) \leq 1$.
1. $s (\bx, \bx) = 1$ for every $\bx \in \RR^m$.
1. $s(\bx, \by) = s(\by, \bx)$.
```

Normally, we require that the similarity function is symmetric; i.e.,

```{math}
s(\bx, \by) = s(\by, \bx).
```
There are rare cases where asymmetric similarity functions have
been used.


```{prf:example} Similarity from metrics
:label: ex-ml-cl-similarity-distance-1

Let $d$ be a metric (distance function) defined on $\RR^n$.
Then we have for any $\bx, \by, \bz \in \RR^m$,

1. $d (\bx, \bx)  = 0$.
1. $d (\bx, \by) \geq 0$.
1. $d (\bx, \by) = d(\by, \bx)$.
1. $d (\bx, \by) \leq d(\bx, \bz) + d(\bz, \by)$.

One way to induce a similarity function is:

$$
s(\bx, \by) = \exp (- d(\bx, \by)).
$$

We can see that

1. Since $\exp(t) \geq 0$ for every $t \in \RR$, hence $s(\bx, \by) \geq 0$.
1. Since $d(\bx, \by) \geq 0$, hence $s(\bx, \by) \leq 1$.
1. Since $d$ is symmetric, hence $s$ is symmetric.
1. Since $d(\bx, \bx) = 0$, hence $s (\bx, \bx) = 1$.

Thus, $s$ is indeed a similarity function.

Note that a metric satisfies the triangle inequality. However,
this property was not required for the similarity function
induced from the metric.
Thus, a metric imposes an additional structure which is more
stringent than the needs for a similarity measure.

For example, the squared distance function $d^2$
satisfies the identity of indiscernibles,
is nonnegative and symmetric. It doesn't satisfy
triangle inequality. However, we can construct
a similarity function

$$
s'(\bx, \by) = \exp (- d^2(\bx, \by)).
$$
``` 

### Proximity Matrices

```{index} Distance matrix
```
```{prf:definition} Distance matrix
:label: def-ml-cl-distance-matrix

Let $d$ be a metric on the space $\RR^m$.
Let $\bX$ be a dataset of $n$ points
$\{ \bx_1, \dots, \bx_n \}$. Then the
*distance matrix* for $\bX$ is defined as

$$
\bM_{\dist}(\bX) = \begin{bmatrix}
0 & d_{1 2} & \dots & d_{1 n}\\
d_{2 1} & 0 & \dots & d_{2 n} \\
\vdots & \vdots & \ddots & \vdots \\
d_{n 1} & d_{n 2} & \dots & 0
\end{bmatrix}
$$
where $d_{i j} = d(\bx_i, \bx_j)$.
```

```{index} Similarity matrix
```
```{prf:definition} Similarity matrix
:label: def-ml-cl-similarity-matrix

Let $s$ be a similarity function on the space $\RR^m$.
Let $\bX$ be a dataset of $n$ points
$\{ \bx_1, \dots, \bx_n \}$. Then the
*similarity matrix* for $\bX$ is defined as

$$
\bM_{\sim}(\bX) = \begin{bmatrix}
1 & s_{1 2} & \dots & s_{1 n}\\
s_{2 1} & 1 & \dots & s_{2 n} \\
\vdots & \vdots & \ddots & \vdots \\
s_{n 1} & s_{n 2} & \dots & 1
\end{bmatrix}
$$
where $s_{i j} = s(\bx_i, \bx_j)$.
```

```{index} Proximity matrix
```
```{prf:definition} Proximity matrix
:label: def-ml-cl-proximity-matrix

Let $\bX$ be a dataset of $n$ points
$\{ \bx_1, \dots, \bx_n \}$. Then an $n \times n$
square matrix $\bM$ where every
$(i,j)$-th element is some measure of similarity
or distance between $\bx_i$ and $\bx_j$
is known as a *proximity matrix*.

In other words, a proximity matrix is
either a distance matrix or a similarity matrix.

Each entry in a proximity matrix is called
a *proximity index*.
```


```{prf:remark} Asymmetry in proximity
:label: rem-ml-cl-asymmetric-proximity

There are several problems where a proximity metric
may not be symmetric. For example, when the objects
in the dataset are locations in a hilly area and
the measure of the distance is the time taken
in going from point A to point B, the time taken
may be quite different when going uphill or downhill.
Such problems do give rise to asymmetrical proximity
matrices. However, we will normally be concerned
with symmetric cases.
```

```{index} Proximity graph
```
```{prf:definition} Proximity graph
:label: def-ml-cl-proximity-graph

Let $\bX$ be a dataset of $n$ points
$\{ \bx_1, \dots, \bx_n \}$.
Let $\bM$ be a proximity matrix associated
with the dataset $\bX$.
Then the corresponding *proximity graph*
$\GGG$ is a weighted graph whose
nodes/vertices are the data points $\bx_i$
and the edges have weights equal to the
proximity indices.

A symmetric proximity matrix leads to
an undirected graph while an asymmetric
proximity matrix leads to a directed graph.
```


### Scatter and Covariance

```{index} Scatter matrix
```
```{prf:definition} Scatter matrix
:label: def-ml-cl-scatter-matrix

Let $\bX$ be a dataset of $n$ points
$\{ \bx_1, \dots, \bx_n \}$
sampled from the Euclidean space $\RR^n$.
Let $\bar{\bx}$ be the arithmetic mean
of the data points.

$$
\bar{\bx} = \frac{1}{n}\sum_{i=1}^n \bx_i.
$$
Then the scatter matrix for $\bX$ is defined
as 

$$
\bM_t(\bX) = \sum_{i=1}^n (\bx_i - \bar{\bx}) (\bx_i - \bar{\bx})^T.
$$
```


```{index} Statistical scatter
```
```{prf:definition} Statistical scatter
:label: def-ml-cl-scatter

The trace of the scatter matrix is known as the
*statistical scatter* of the data set.
It is given by

$$
\Trace(\bM_t(\bX)) = \sum_{i=1}^n (\bx_i - \bar{\bx})^T (\bx_i - \bar{\bx}).
$$
```

Recall that $\Trace(\bA \bB) = \Trace (\bB \bA)$.

Hence

$$
\Trace(\bM_t(\bX)) 
= \Trace\left ( \sum_{i=1}^n (\bx_i - \bar{\bx}) (\bx_i - \bar{\bx})^T \right )
= \Trace \left ( \sum_{i=1}^n (\bx_i - \bar{\bx})^T (\bx_i - \bar{\bx}) \right )
= \sum_{i=1}^n (\bx_i - \bar{\bx})^T (\bx_i - \bar{\bx})
$$
since this quantity is a scalar.


Let $\CCC = \{C_1, \dots, C_k \}$ be a (hard) clustering (partition) of $\bX$
into $k$ clusters.
Then for a given cluster $C_j$, the *within-scatter-matrix* is
given by

$$
\bM_t(C_j) = \sum_{i \in C_j} (\bx_i - \bz_j) (\bx_i - \bz_j)^T
$$
where $\bz_j$ is the mean of the cluster $C_i$

$$
\bz_j = \frac{1}{|C_j|} \sum_{i \in C_j} \bx_i.
$$
The *within-cluster* scatter matrix of the partition
is given by

```{math}
:label: eq-ml-cl-within-cluster-scatter-matrix

\bM_w(\CCC) = \sum_{j=1}^k \bM_t(C_j)
= \sum_{j=1}^k \sum_{i \in C_j} (\bx_i - \bz_j) (\bx_i - \bz_j)^T.
```

The *between-cluster* scatter matrix for the partition $\CCC$ is
given by

$$
\bM_b(\CCC) = \bM_t(\bX) - \bM_w(\CCC).
$$
We shall denote the dataset after mean removal as

$$
\widetilde{\bX} = \bX - \bar{\bx}
$$
where the matrix vector subtraction is done according to the
standard broadcasting rules.


The covariance matrix of the dataset is given by

```{math}
:label: eq-ml-cl-covariance-matrix

\Sigma = \frac{1}{n} \widetilde{\bX} \widetilde{\bX}^T.
```

Sample covariance matrix is often used in statistics which is given by

```{math}
:label: eq-ml-cl-sample-covariance-matrix
\bS =  \frac{1}{n - 1} \widetilde{\bX} \widetilde{\bX}^T
= \frac{n}{n - 1} \Sigma.
```

## Common Proximity Measures

We look at some of the common proximity measures for
numerical data.

### Euclidean Distance

```{math}
:label: eq-ml-cl-euclidean-distance

d_2(\bx, \by) = \sqrt{\sum_{i=1}^m (x_i - y_i)^2}
= \sqrt{ (\bx - \by)^T (\bx - \by)}. 
```

### Squared Euclidean Distance

```{math}
:label: eq-ml-cl-sqr-euclidean-distance

d_2^2(\bx, \by) = \sum_{i=1}^m (x_i - y_i)^2
= (\bx - \by)^T (\bx - \by). 
```

### Manhattan Distance

This is also known as city-block distance

```{math}
:label: eq-ml-cl-manhattan-distance

d_1(\bx, \by) = \sum_{i=1}^m |x_i - y_i|.
```


Manhattan segmental distance is a variant in which
only some of the dimensions selected by a subset $P \subseteq \{ 1,\dots, m\}$
are used.

```{math}
:label: eq-ml-cl-manhattan-segment-distance

d_P(\bx, \by) = \frac{1}{|P|} \sum_{i \in P} |x_i - y_i|.
```

### Maximum Distance

This is also known as the *Chebyshev distance*.

```{math}
:label: eq-ml-cl-chebyshev-distance

d_{\max}(\bx, \by) = \max_{i=1}^m |x_i - y_i|.
```


### Minkowski Distance

This is the generalization of Euclidean, Manhattan and Chebyshev distances
for some $p \geq 1$.

```{math}
:label: eq-ml-cl-minkowski-distance

d_p(\bx, \by) = \left ( \sum_{i=1}^m |x_i - y_i|^p \right )^{\frac{1}{p}}.
```

### Mahalanobis Distance 

As discussed in {prf:ref}`ex-ml-cl-l2-dist-susceptible-1`,
Mahalanobis distance can address the issues related
to the scale differences between different features
and the correlation among features. This is
given by

```{math}
:label: eq-ml-cl-mahalanobis-distance

d_{\mah}(\bx, \by) 
= \sqrt{ (\bx - \by)^T \Sigma^{-1} (\bx - \by)}.
```

Mahalanobis distance is invariant to nonsingular transformations.
Let $\bC$ be any $m \times m$ non-singular matrix.

Let $\bY = \{ \by_1, \dots, \by_n \}$ be a new dataset
constructed by transforming the dataset $\bX$ as

$$
\by_i  = \bC \by_i.
$$

Then

$$
d_{\mah}(\bx_i, \bx_j) = d_{\mah}(\by_i, \by_j).
$$


### Chord Distance

We normalize the data points to project them
to the unit sphere in $\RR^m$. Then we measure
the length of the chord between the two points
on the sphere. It is given by


```{math}
:label: eq-ml-cl-chord-distance

d_{\chord}(\bx, \by) 
= \sqrt{ 2 - 2 \frac{\langle \bx, \by \rangle}{\| \bx \|_2 \| \by\|_2}}.
```

````{div}
It is easy to see how this formula is arrived at.
Assume $\bx, \by$ lie on the unit sphere. Then

$$
\langle \bx - \by, \bx - \by \rangle
= \| \bx \|_2^2 + \| \by \|_2^2 - 2 \langle \bx, \by \rangle
= 2 - 2 \langle \bx, \by \rangle.
$$
When they are not normalized, we normalize them

$$
2 - 2 \frac{\langle \bx, \by \rangle}{\| \bx \|_2 \| \by\|_2}.
$$
Finally, for computing the length of the chord, we need
to take the square root.
````


### Geodesic Distance

Once the data points have been normalized to the
unit sphere, one can calculate the shortest path (arc)
between any two data points along the surface
of the unit sphere. This is known as the
*geodesic distance*. It is given by

```{math}
:label: eq-ml-cl-geo-distance

d_{\geo}(\bx, \by) 
= \arccos \left ( 1 -  \frac{d_{\chord}(\bx, \by) }{2} \right).
```

### Cosine Similarity

The cosine similarity between two points is given by

```{math}
:label: eq-ml-cl-cosine-similarity

s_{\cos}(\bx, \by) = 
\frac{|\langle \bx, \by \rangle | }{\| \bx \|_2 \| \by\|_2}.
```

It is easy to see that cosine similarity is bound between
$0$ and $1$, is symmetric and $s_{\cos}(\bx, \bx) = 1$. 


## Proximity Between Clusters

Many clustering algorithms are hierarchical. In the
context of agglomerative hierarchical clustering,
one needs to merge clusters which are similar to
each other in each iteration.
Thus, it is imperative to have some measures of
similarity or dissimilarity between clusters.

In this subsection, we shall consider two
arbitrary clusters of the dataset $\bX$
denoted by $C_1$ and $C_2$ where

$$
C_1 = \{ \by_1, \dots, \by_r \}
\text{ and }
C_2 = \{ \bz_1, \dots, \bz_s \}.
$$
Let the mean of $C_1$ be given by

$$
\bar{\by} = \frac{1}{r} \sum_{i=1}^r \by_i.
$$
Let the mean of $C_2$ be given by

$$
\bar{\bz} = \frac{1}{s} \sum_{i=1}^s \bz_i.
$$

### Mean Based Distance

The mean based distance between two clusters is
defined as

```{math}
:label: eq-ml-cl-cluster-mean-distance

d_{\mean}(C_1, C_2) = d(\bar{\by}, \bar{\bz}).
```

### Nearest Neighbor Distance

```{math}
:label: eq-ml-cl-cluster-nn-distance

d_{\nn}(C_1, C_2) = \min_{1 \leq i \leq r, 1 \leq j \leq s} d(\by_i, \bz_j).
```


### Farthest Neighbor Distance

```{math}
:label: eq-ml-cl-cluster-fn-distance

d_{\fn}(C_1, C_2) = \max_{1 \leq i \leq r, 1 \leq j \leq s} d(\by_i, \bz_j).
```


### Average Neighbor Distance

```{math}
:label: eq-ml-cl-cluster-ave-distance

d_{\ave}(C_1, C_2) = \frac{1}{r s} \sum_{i=1}^r \sum_{j=1}^s d(\by_i, \bz_j).
```


### Statistical Distance

```{math}
:label: eq-ml-cl-cluster-stat-distance

d_{\stat}(C_1, C_2) = \frac{r s}{r + s} 
(\bar{\by} - \bar{\bz})^T (\bar{\by} - \bar{\bz}).
```


### Lance-Williams Formula

Consider a step in an agglomerative hierarchical algorithm
where clusters $C_i$ and $C_j$ are being merged into a new
cluster $C$ and we wish to consider the distance between
another cluster $C_k$ and the new cluster $C$.

The following formula provides a recursive definition
such that we can compute the distance $d(C_k, C)$
using existing distance information.

```{math}
:label: eq-ml-cl-cluster-lw-distance

d(C_k, C_i \cup C_j)
= \alpha_i d( C_k, C_i)
+ \alpha_j d(C_k, C_j)
+ \beta d( C_i, C_j)
+ \gamma | d(C_k, C_i) - d(C_k, C_j) |
```
where $d$ is some distance function between
two clusters.

Some common choices of the parameters
$\alpha_i, \alpha_j, \beta, \gamma$ are
given in the following table.

```{list-table}

* - Algorithm
  - $\alpha_i$
  - $\alpha_j$
  - $\beta$
  - $\gamma$
* - Single-link
  - $\frac{1}{2}$
  - $\frac{1}{2}$
  - $0$
  - $-\frac{1}{2}$
* - Complete-link
  - $\frac{1}{2}$
  - $\frac{1}{2}$
  - $0$
  - $\frac{1}{2}$
* - Group-average
  - $\frac{n_i}{n_i + n_j}$
  - $\frac{n_j}{n_i + n_j}$
  - $0$
  - $0$
* - Weighted group average
  - $\frac{1}{2}$
  - $\frac{1}{2}$
  - $0$
  - $0$
* - Centroid
  - $\frac{n_i}{n_i + n_j}$
  - $\frac{n_j}{n_i + n_j}$
  - $\frac{-n_i n_j}{(n_i + n_j)^2}$
  - $0$
* - Median
  - $\frac{1}{2}$
  - $\frac{1}{2}$
  - $-\frac{1}{4}$
  - $0$
```
