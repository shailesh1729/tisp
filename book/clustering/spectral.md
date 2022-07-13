(sec:ml:cluster:spectral)=
# Spectral Clustering

Spectral clustering is a graph based clustering algorithm
{cite}`von2007tutorial`.

````{div}
We build a graph $\GGG = \{T, W\}$ to obtain the
clustering $\CCC$ of $X$.
1. Each vertex in the graph represents a data point.
1. Each edge in the graph represents the similarity
   between two data points.
1. $T$ denotes the list of vertices.
1. $W$ denotes the adjacency matrix built from the similarities.

Once the graph has been built, the following steps are performed.

1. The degree of a vertex $t_s \in T$
    is defined as $d_s = \sum_{j = 1}^S w_{s j}$.
1. The *degree matrix* $D$ is defined as the diagonal matrix
   with the degrees $\{ d_s \}_{s =1 }^S$.
1. The unnormalized graph Laplacian is defined
   as $\LLL = D - W$.
1. The normalized graph Laplacian is defined as [^laplacian]

    $$
    \LLL_{\text{rw}} \triangleq D^{-1} \LLL = I - D^{-1} W
    $$
    The subscript $\text{rw}$ stands for random walk.
1. We compute $\LLL_{\text{rw}}$ and examine its eigen-structure
   to estimate the number of clusters $C$ and the label vector $L$.
1. If $C$ is known in advance, usually the first $C$ eigen vectors of
   $\LLL_{\text{rw}}$ corresponding to the smallest eigen-values
   are taken and their row vectors are clustered using K-means algorithm
   {cite}`shi2000normalized`.
1. Since, we don't make any assumption on the number of clusters, we need
   to estimate it. 
1. A simple way is to track the eigen-gap statistic. 
1. After arranging the eigen values in increasing order,
   we can choose the number $C$ such that the
   eigen values $\lambda_1, \dots, \lambda_C$
   are very small and $\lambda_{C + 1}$ is large.
1. This is guided by the theoretical results that if a Graph has
   $C$ connected components then exactly $C$ eigen values of
   $\LLL_{\text{rw}}$ are 0. 
1. However, when the data points are not clearly separated,
   and noise is introduced, this approach
   becomes tricky.
1. We can go for a more robust approach by 
   analyzing the eigen vectors as described in {cite}`zelnik2004self`.
1. The approach of {cite}`zelnik2004self`, with a
   slightly different definition of
   the graph Laplacian $(D^{-1/2} W D^{-1/2})$ {cite}`ng2002spectral`,
   has been adapted for working with the Laplacian 
   $\LLL_{\text{rw}}$ as defined above.
1. We estimate the number of clusters from the Graph Laplacian.
1. It can be easily shown that $0$ is an eigen value of $\LLL_{\text{rw}}$
   with an eigen vector $\OneVec_S$ {cite}`von2007tutorial`.
1. Further, the multiplicity of eigen value $0$ equals the number of connected
   components in $\GGG$.
1. In fact the adjacency matrix can be factored as

    $$
    W = \begin{bmatrix}
    W_1 & \dots  & 0\\
    \vdots & \ddots & \vdots \\
    0 & \dots & W_P
    \end{bmatrix} \Gamma
    $$
    where $W_p \in \RR^{S_p \times S_p}$ is the adjacency matrix for the 
    $p$-th connected component of $\GGG$ corresponding to the $p$-th cluster
    and $\Gamma$ is the unknown permutation matrix. 
1. The graph Laplacian for each $W_p$ has an eigen
   value $0$ and the eigen-vector $\OneVec_{S_p}$.
1. Thus, if we look at the $P$-dimensional eigen-space of $\LLL_{\text{rw}}$
   corresponding to eigen value $0$,
   then there exists a basis $\widehat{V} \in \RR^{S \times P}$
   such that each row of $\widehat{V}$ is a 
   unit vector in $\RR^P$
   and the columns contain $S_1, \dots, S_P$ ones. 
1. Actual eigen vectors obtained through any numerical method will be
   a rotated version of $\widehat{V}$ 
   given by $V = \widehat{V} R$.
1. {cite}`zelnik2004self` suggests a cost function over
   the entries in $V$ such that the cost is minimized
   when the rows of $V$ are close to coordinate vectors.
1. It then estimates a rotation matrix as a product of Givens rotations
   which can rotate $V$ to minimize the cost.
1. The parameters of the rotation matrix are the angles of Givens rotations
   which are estimated through a Gradient descent process.
1. Since $P$ is unknown, the algorithm is run over multiple values of $C$
   and we choose the value which gives minimum cost. 
1. Note that, we reuse the rotated version of $V$ obtained
   for a particular value of $C$ when we go for examining $C+1$ eigen-vectors.
1. This may appear to be ad-hoc, but is seen to help in faster convergence
   of the gradient descent algorithm for next iteration.
1. When $S$ is small, we can do a complete SVD of $\LLL_{\text{rw}}$
   to get the eigen vectors.
1. However, this is time consuming when $S$ is large (say 1000+).
1. An important question is how many eigen vectors we really need to examine!
1. As $C$ increases, the number of Givens rotation parameters increase as $C(C-1)/2$. 
1. Thus, if we examine too many eigen-vectors, we will lose out unnecessarily on speed.
1. We can actually use the eigen-gap  statistic described above to decide
   how many eigen vectors we should examine. 
1. Finally, we assign labels to each data point to identify the cluster they belong to.
1. As described above, we maintain the rotated version of $V$ during the estimation
   of rotation matrix.
1. Once, we have zeroed in on the right value of $C$, then
   assigning labels to $x^s$ is straight-forward.
1. We simply perform *non-maximum suppression*
   on the rows of V, i.e. we keep the largest (magnitude) entry
   in each row of $V$
   and assign zero to the rest.
1. The column number of the largest entry in the $s$-th row of $V$ 
   is the label $l_s$ for $x^s$.
1. This completes the clustering process.

While eigen gap statistic based estimation of number of clusters is quick,
it requires running an additional $K$-means algorithm step on the first $C$
eigen vectors to assign the labels. In contrast, eigen vector based estimation
of number of clusters is involved and slow but it allows us to pick the
labels very quickly.
````

````{div}

[^laplacian]: We specifically use the random walk version of normalized
Graph Laplacian as defined in {cite}`von2007tutorial`.
There are other ways to define normalized graph Laplacian.

````
