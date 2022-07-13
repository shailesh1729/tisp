(ch:subspace:clustering)=
# Subspace Clustering

High dimensional data-sets are now pervasive in various signal 
processing applications. 
For example, high resolution surveillance cameras are now commonplace
generating millions of images continually. 
A major factor in the success of current generation signal processing
algorithms is the fact that, even though these data-sets are high
dimensional, their intrinsic dimension is often much smaller than
the dimension of the ambient space. 

```{image} images/union_of_subspaces.png
```


````{div}
One resorts to inferring (or learning) a quantitative model 
$\MM$ of a given set of data points 
$\bY = \{ \by_1, \dots, \by_S\} \subset \RR^M$.
Such a model enables us to obtain a low dimensional representation 
of a high dimensional data set. 
The low dimensional representations
enable efficient implementation of acquisition, compression, 
storage, and various statistical inferencing tasks without losing
significant precision. There is no such thing as a perfect model.
Rather, we seek a model $\MM^*$ that is best among a 
restricted class of
models $\MMM = \{ \MM \}$ which is rich enough to 
describe the data set to a desired accuracy yet restricted
enough so that selecting the best model is tractable.

In absence of training data, the problem of modeling falls
into the category of *unsupervised learning*. There
are two common viewpoints of data modeling. A *statistical*
viewpoint assumes that data points are random samples from
a probabilistic distribution. *Statistical models* try
to learn the distribution from the dataset. In contrast,
a *geometrical* viewpoint assumes that data points 
belong to a geometrical object (a smooth manifold or a topological
space). A *geometrical model* attempts to learn the shape of
the object to which the data points belong. Examples of 
statistical modeling include maximum likelihood, 
maximum a posteriori estimates, Bayesian models etc. 
An example of geometrical models is 
Principal Component Analysis (PCA) 
which assumes that data
is drawn from a low dimensional subspace of the high dimensional
ambient space. PCA is simple to implement and has found 
tremendous success in different fields e.g., pattern recognition,
data compression, image processing, computer vision, etc.
[^pca].

The assumption that all the data points in a data set could be
drawn from a single model however happens
to be a stretched one. In practice, it often occurs that
if we *group* or *segment* the data set $\bY$ into
multiple disjoint subsets: 
$\bY = \bY_1 \cup \dots \cup \bY_K$,
then each subset can be modeled sufficiently well by a model
$\MM_k^*$ ($1 \leq k \leq K$) chosen from a simple model class.
Each model $\MM_k^*$ is called a *primitive* or *component*
model. In this sense, the data set $\bY$ is called a *mixed*
dataset and the collection of primitive models is called a
*hybrid* model for the dataset. Let us look at some examples
of mixed data sets.

Consider the problem of *vanishing point detection* in computer
vision. Under perspective projection, a group of parallel lines 
pass through a common point in the image plane which is known as
the vanishing point for the group. For a typical scene consisting
of multiple sets of parallel lines, the problem of detecting
all vanishing points in the image plane 
from the set of edge segments (identified in the image) can be 
transformed into clustering points (in edge segments) into
multiple 2D subspaces in $\RR^3$ (world coordinates of the scene).

In the *Motion segmentation* problem, an image
sequence consisting of multiple moving objects is
segmented so that each segment consists of motion 
from only one object. This is a fundamental problem
in applications such as motion capture, vision based navigation,
target tracking and surveillance. We first track the
trajectories of feature points (from all objects) over the image
sequence. It has been shown (see {ref}`sec:motion_segmentation`)
that trajectories of feature points for rigid motion
for a single object form a low dimensional subspace.
Thus motion segmentation problem can be solved by
segmenting the feature point trajectories  
for different objects separately and estimating
the motion of each object from corresponding trajectories.

In a *face clustering* problem, we have 
a collection of unlabeled images of different faces taken
under varying illumination conditions. Our goal is to
cluster, images of the same face in one group each.
For a Lambertian object, it has been shown
that the set of images taken under different lighting 
conditions forms a cone in the image space. This cone
can be well approximated by a low-dimensional subspace
{cite}`basri2003lambertian, ho2003clustering`.  The images of the face
of each person form one low dimensional subspace and the face clustering
problem reduces to clustering the collection of images to 
multiple subspaces. 

As the examples above suggest, a typical hybrid model 
for a mixed data set consists of multiple primitive models
where each primitive is a (low dimensional) subspace. 
The data set is modeled as being sampled from a collection
or arrangement $\UUU$ of linear (or affine) subspaces
$\UUU_k \subset \RR^M$ : 
$\UUU = \{ \UUU_1  , \dots , \UUU_K \}$. 
The union of the subspaces[^union] 
is denoted as
$Z_{\UUU} = \UUU_1 \cup \dots \cup \UUU_K$.
This is indeed a geometric
model.
In such modeling problems, 
individual subspaces (dimension and orientation of each subspace and total number of subspaces) and 
the membership of a data point (a single image
in the face clustering problem) to a particular subspace is 
unknown beforehand. This entails the need for algorithms
which can simultaneously identify the subspaces
involved and cluster/segment 
the data points from individual subspaces
into separate groups. 
This problem is known as *subspace clustering* which is the
focus of this paper. 
An earlier detailed introduction to subspace clustering can be found in 
{cite}`vidal2010tutorial`.

An example of a statistical hybrid model is a Gaussian Mixture
Model (GMM) where one assumes that the sample points are drawn
independently from a mixture of Gaussian distributions. 
A way of estimating such a mixture model is the 
expectation maximization (EM) method.

The fundamental difficulty in the estimation of hybrid models
is the "chicken-and-egg" relationship between data segmentation
and model estimation. If the data segmentation was known,
one could easily fit a primitive model to each subset. 
Alternatively, if the constituent primitive models were known,
one could easily segment the data by choosing the best model
for each data point. An iterative approach starts with 
an initial (hopefully good) guess of primitive models 
or data segments. It then alternates between estimating
the models for each segment and segmenting the data based
on current primitive models till the solution converges.
On the contrary, a global algorithm can perform the segmentation
and primitive modeling simultaneously. In the sequel, we will
look at a variety of algorithms for solving the subspace
clustering problem.
````



 
## Notation

````{div}
First some general notation for vectors and matrices.
1. For a vector $\bv \in \RR^n$, its support
   is denoted by $\supp(\bv)$ and is defined as
   $\supp(\bv) \triangleq \{i : v_i \neq 0, 1 \leq i \leq n \}$.
1. $|\bv|$ denotes a vector obtained by taking the absolute
   values of entries in $\bv$.  
1. $\bone_n \in \RR^n$ denotes a vector whose every entry is $1$.
1. $\| \bv \|_p$ denotes
   the $\ell_p$ norm of $v$.
1. $\| \bv \|_0$ denotes 
   the $\ell_0$-"norm" of $\bv$.
1. Let $\bA$ be any $m \times n$ real matrix 
   ($\bA \in \RR^{m \times n}$). 
1. $a_{i, j}$ is the element at the $i$-th row
   and $j$-th column of $\bA$.
1. $\ba_j$ with
   $1 \leq j \leq n$ denotes the $j$-th column
   vector of $\bA$.
1. $\underline{a}_i$ with
   $1 \leq i \leq m$ denotes the $i$-th row vector of
   $\bA$.
1. $a_{j,k}$ is the $k$-th entry in $\ba_j$. 
1. $\underline{a}_{i,k}$ is the $k$-th entry in
   $\underline{a}_i$. 
1. $\bA_{\Lambda}$ denotes a submatrix of $\bA$
   consisting of columns indexed by 
   $\Lambda \subset \{1, \dots, n \}$.
1. $\underline{\bA}_{\Lambda}$  denotes a 
   submatrix of $\bA$ consisting of rows indexed 
   by $\Lambda \subset \{1, \dots, m \}$.
1. $|\bA|$ denotes the matrix consisting of
   absolute values of entries in $\bA$.
1. $\supp(\bA)$ denotes the index set of non-zero rows of $\bA$.
1. Clearly, $\supp(\bA) \subseteq \{1, \dots, m\}$.
1. $\| \bA \|_{0}$ denotes the number of non-zero rows of $\bA$.
1. Clearly, $\| \bA \|_{0} = |\supp(\bA)|$.
1. We note that while $\| \bA \|_{0}$ is not a norm,
   its behavior is similar to the $\ell_0$-"norm"
   for vectors $\bv \in \RR^n$ defined
   as $\| \bv \|_0 \triangleq | \supp(\bv) |$.
1. We use $f(x)$ and $F(x)$ to denote the
   PDF and CDF of a continuous random variable.
1. We use $p(x)$ to denote the PMF of a 
   discrete random variable.
1. We use $\PP(E)$ to denote the probability of an event.
````

### Problem Formulation

````{div}
The data set can be modeled as a set of data points
lying in a union of low dimensional linear or
affine subspaces in a Euclidean space $\RR^M$ 
where $M$ denotes the dimension of ambient space. 

1. Let the data set be $\{ \by_j  \in \RR^M \}_{j=1}^S$
   drawn from the union of subspaces under consideration.
1. $S$ is the total number of data points being analyzed
   simultaneously.
1. We put the data points together in a *data matrix* as
   
   $$
    \bY  \triangleq \begin{bmatrix}
    \by_1 & \dots & \by_S
    \end{bmatrix}.
   $$
1. The data matrix $Y$ is known to us.
1. Note that in statistic books, data samples are
   placed in each row of the data matrix.
   We are putting data samples in each column
   of the data matrix.
1. We will slightly abuse the notation
   and let $\bY$ denote the *set* of data points
   $\{ \by_j  \in \RR^M \}_{j=1}^S$ also.
1. We will use the terms data points and vectors interchangeably. 
1. Let the vectors be drawn from a set of $K$ (linear or affine) subspaces. 
1. The number of subspaces may not be known in advance. 
1. The subspaces are indexed by a variable $k$ with $1 \leq k \leq K$.
1. The $k$-th subspace is denoted by $\UUU_k$.
1. Let the (linear or affine) dimension of $k$-th subspace be
   $\dim(\UUU_k) = D_k$ with $D_k \leq D$.
1. Here $D$ is an upper bound on the dimension of individual subspaces. 
1. We may or may not know $D$.
1. We assume that none of the subspaces is contained in another.
1. A pair of subspaces may not intersect (e.g. parallel lines or planes),
   may have a trivial intersection (lines passing through origin),
   or a non-trivial intersection (two planes intersecting at a line).
1. The collection of subspaces may also be independent or disjoint
   (see {ref}`sec:sscl:linear:algebra`). 
1. The vectors in $\bY$ can be grouped (or segmented or clustered) 
   as submatrices $\bY_1, \bY_2, \dots, \bY_K$ such 
   that all vectors in $\bY_k$ lie in subspace $\UUU_k$. 
1. Thus, we can write
   
   $$
    \bY^* = \bY \Gamma 
    = \begin{bmatrix} \by_1 & \dots & \by_S \end{bmatrix} 
    \Gamma
    = \begin{bmatrix} \bY_1 & \dots & \bY_K \end{bmatrix} 
   $$
   where $\Gamma$ is an $S \times S$ unknown permutation
   matrix placing each vector to the right subspace. 
1. This segmentation is straight-forward if the (affine)
   subspaces do not intersect or the subspaces intersect
   trivially at one point (e.g. any pair of linear
   subspaces passes through origin). 
1. Let there be $S_k$ vectors in $\bY_k$ with
   $S = S_1 + \dots + S_K$.
1. We may not have any prior information about the 
   number of points in individual subspaces.
1. We do typically require that there are enough vectors 
   drawn from each subspace so that they can span the corresponding subspace.
1. This requirement may vary for individual subspace clustering algorithms.
1. For example, for linear subspaces, 
   sparse representation based algorithms require that whenever
   a vector is removed from $\bY_k$, the remaining set of vectors spans
   $\UUU_k$.
1. This guarantees that every vector in $\bY_k$ can be represented
   in terms of other vectors in $\bY_k$.
1. The minimum required $S_k$ for which this is possible is $S_k = D_k + 1$
   when the data points from each subspace are in general position
   (i.e. $\spark(\bY_k) = D_k + 1$).
1. Let $\bQ_k$ be an orthonormal basis for subspace $\UUU_k$.
1. Then, the subspaces can be described as 
   
   $$
    \UUU_k = \{ \by \in \RR^M \ST \by = \mu_k + \bQ_k \ba \}, \quad 1 \leq k \leq K 
   $$
1. For linear subspaces, $\mu_k = \bzero$.
1. We will abuse $\bY_k$ to also denote the set of vectors from the
   $k$-th subspace.
1. The basic objective of *subspace clustering* algorithms 
   is to obtain a clustering or segmentation of vectors in $\bY$
   into $\bY_1, \dots, \bY_K$.
1. This involves finding out the number of subspaces/clusters $K$,
   and placing each vector $\by_s$ in its cluster correctly.
1. Alternatively, if we can identify $\Gamma$ and the numbers
   $S_1, \dots, S_K$ correctly, we have solved the clustering problem.
1. Since the clusters fall into different subspaces, 
   as part of subspace clustering, we may also identify
   the dimensions $\{D_k\}_{k=1}^K$ of individual subspaces, the
   bases $\{ \bQ_k \}_{k=1}^K$ and the offset vectors $\{ \mu_k \}_{k=1}^K$
   in case of affine subspaces.
1. These quantities emerge due to modeling the clustering problem
   as a subspace clustering problem. 
1. However, they are not essential outputs of the subspace clustering algorithms.
1. Some subspace clustering algorithms may not calculate them, 
   yet they are useful in the analysis of the algorithm. 
1. See {ref}`ch:ml:clustering` for a quick review of
   data clustering terminology.
````

### Noisy Case

```{div}

1. We also consider clustering of data points which are contaminated
   with noise.
1. The data points do not perfectly lie in a
   subspace but can be approximated as a sum of a component which
   lies perfectly in a subspace and a noise component. 
1. Let

    $$
    \by_s = \bar{\by}_s + \be_s , \Forall 1 \leq s \leq S
    $$
    be the $s$-th vector that is obtained by corrupting
    an error free vector $\bar{\by}_s$ (which perfectly lies in
    a low dimensional subspace) with a noise vector $\be_s \in \RR^M$.
1. The clustering problem remains the same. Our goal would
   be to characterize the behavior of the clustering algorithm
   in the presence of noise at different levels.
```


(sec:sscl:linear:algebra)=
## Linear Algebra

This section reviews some useful concepts from linear algebra
relevant for the chapter.

A collection of linear subspaces $\{ \UUU^i\}_{i=1}^n$ is called *independent*
if $\dim(\oplus_{i=1}^n \UUU^i)$ equals $\sum_{i=1}^n \dim (\UUU^i)$.

A collection of linear subspaces is called *disjoint*
if they are pairwise independent
{cite}`elhamifar2010clustering`.
In other words, every pair of subspaces intersect only at the origin.

(sec:sscl:affine:subspace)=
### Affine Subspaces

For a detailed introduction to affine concepts,
see {cite}`kelly1979geometry`.

````{div}
1. For a vector $\bv \in \RR^n$, the function $f$ defined
   by $f (\bx) = \bx + \bv, \bx \in \RR^n$ is a *translation*
   of $\RR^n$ by $\bv$.
1. The image of any set $\SSS$ 
   under $f$ is the *$\bv$-translate* of $\SSS$.
1. A translation of space is a one to one isometry of
   $\RR^n$ onto $\RR^n$.
1. A translate of a $d$-dimensional linear subspace
   of $\RR^n$ is a $d$-*dimensional flat* or simply
   $d$-*flat* in $\RR^n$.
1. Flats of dimension 1, 2, and $n-1$ are also called
   lines, planes, and hyperplanes, respectively.
1. Flats are also known as *affine subspaces*.  
1. Every $d$-flat in $\RR^n$ is congruent to the Euclidean space $\RR^d$.
1. Flats are closed sets.

Affine combinations

1. An *affine combination* of the vectors $\bv_1, \dots, \bv_m$
   is a linear combination in which the sum of coefficients is 1.
1. Thus, $\bb$ is an affine combination of $\bv_1, \dots, \bv_m$ 
   if $\bb = k_1 \bv_1 + \dots k_m \bv_m$ and 
   $k_1 + \dots + k_m = 1$.
1. The set of affine combinations of a set of vectors
   $\{ \bv_1, \dots, \bv_m \}$ is their
   *affine span*.
1. A finite set of vectors $\{\bv_1, \dots, \bv_m\}$ is called 
   *affine independent* if the only
   *zero-sum linear combination*
   representing the null vector is the null combination.
   i.e. $k_1 \bv_1 + \dots + k_m \bv_m = \bzero$ and
   $k_1 + \dots + k_m = 0$ implies
   $k_1 = \dots = k_m = 0$.
1. Otherwise, the set is *affinely dependent*.
1. A finite set of two or more vectors is affine independent
   if and only if none of them is an affine combination
   of the others.

Vectors vs. Points
1. We often use capital letters to denote points
   and bold small letters to denote vectors.
1. The origin is referred to by the letter $O$.
1. An n-tuple $(x_1, \dots, x_n)$ is used to refer to a
   point $X$ in $\RR^n$ as well as to a vector
   from origin $O$ to $X$ in $\RR^n$. 
1. In basic linear algebra, the terms vector and point
   are used interchangeably.
1. While discussing geometrical concepts (affine or convex sets etc.),
   it is useful to distinguish between vectors and points.
1. When the terms "dependent" and "independent"
   are used without qualification to points, they
   refer to affine dependence/independence.
1. When used for vectors, they mean linear dependence/independence.

$k$-flats

1. The span of $k+1$ independent points is a $k$-flat
   and is the unique $k$-flat that contains all $k+1$
   points.
1. Every $k$-flat contains $k+1$ (affine) independent points.
1. Each set of $k+1$ independent points in the $k$-flat forms an
   *affine basis* for the flat.
1. Each point of a $k$-flat is represented by one and only one
   affine combination of a given affine basis for the
   flat.
1. The coefficients of the affine combination of a point are the *affine coordinates*
   of the point in the given affine basis of the $k$-flat.
1. A $d$-flat is contained in a linear subspace of dimension $d+1$.
1. This can be easily obtained by choosing an affine basis for the flat and
   constructing its linear span. 

Affine functions

1. A function $f$ defined on a vector space $\VV$ 
   is an *affine function* or *affine transformation* or *affine mapping*
   if it maps every affine combination of vectors $\bu, \bv$ in
   $\VV$ onto the same affine combination of their images.
1. If $f$ is real valued, then $f$ is an  *affine functional*.
1. A property which is invariant under an affine mapping is called
   *affine invariant*.
1. The image of a flat under an affine function is a flat. 
1. Every affine function differs from a linear function
   by a translation.

Affine functionals

1. A functional is an affine functional if and only if there exists a unique
   vector $\ba \in \RR^n$ and a unique real number 
   $k$ such that  $f(\bx) = \langle \ba, \bx \rangle + k$.
1. Affine functionals are continuous.
1. If $\ba \neq \bzero$, then the linear functional
   $f(\bx) = \langle \ba, \bx \rangle$ and the affine 
   functional $g(\bx) = \langle \ba, \bx \rangle + k$ map
   bounded sets onto bounded sets, neighborhoods
   onto neighborhoods, balls onto balls and open sets
   onto open sets.
````

### Hyperplanes and Halfspaces


````{div}

1. Corresponding to a hyperplane $\HHH$ in $\RR^n$
   (an $n-1$-flat), there exists a non-null vector
   $\ba$ and a real number $k$ such that $\HHH$
   is the graph of $\langle \ba , \bx \rangle = k$.
1. The vector $\ba$ is orthogonal to $PQ$ for all 
   $P, Q \in \HHH$.
1. All non-null vectors $\ba$ to 
   have this property are *normal* to the
   hyperplane.
1. The directions of $\ba$ and $-\ba$ are called
   opposite normal directions of $\HHH$. 
1. Conversely, the graph of $\langle \ba , \bx \rangle = k$,
   $\ba \neq \bzero$, is a hyperplane for which $\ba$
   is a normal vector. If $\langle a, x \rangle = k$ and 
   $\langle \bb, \bx \rangle = h$,
   $\ba \neq \bzero$, $\bb \neq \bzero$
   are both representations of a hyperplane 
   $\HHH$, then there exists a real non-zero
   number $\lambda$ such that $\bb = \lambda \ba$ and
   $h = \lambda k$.
1. We can find a unit norm normal vector for $\HHH$.
1. Each point $P$ in space has a unique foot 
   (nearest point) $P_0$ in a Hyperplane $\HHH$.
1. Distance of the point $P$ with vector $\bp$ from
   a hyperplane $\HHH : \langle \ba , \bx \rangle = k$
   is given by 

    $$
    d(P, \HHH) = \frac{|\langle \ba, \bp \rangle - k|}{\| \ba \|_2}.
    $$
1. The coordinate $\bp_0$ of the foot $P_0$ is given by
    
    $$
    \bp_0 = \bp  - \frac{\langle \ba, \bp \rangle - k}{\| \ba \|_2^2} \ba.
    $$
1. Hyperplanes $\HHH$ and $\mathcal{K}$ are parallel if they don't intersect.
1. This occurs if and only if they have a common normal direction.
1. They are different constant sets of the same linear functional.
1. If  $\HHH_1 : \langle \ba , \bx \rangle = k_1$
   and $\HHH_2 : \langle \ba, \bx \rangle  = k_2$ 
   are parallel hyperplanes, then the distance between 
   the two hyperplanes is given by

    $$
    d(\HHH_1 , \HHH_2) = 
    \frac{| k_1  - k_2|}{\| \ba \|_2}.
    $$

Half-spaces

1. If $\langle \ba, \bx \rangle = k$, $\ba \neq \bzero$, is
   a hyperplane $\HHH$, then the graphs of 
   $\langle \ba , \bx \rangle > k$ and 
   $\langle \ba , \bx \rangle < k$ are the 
   *opposite sides* or 
   *opposite open half spaces* of $\HHH$.
1. The graphs of $\langle \ba , \bx \rangle \geq k$ and
   $\langle \ba , \bx \rangle \leq k$ are the 
   *opposite closed half spaces* of $\HHH$.
1. $\HHH$ is the *face* of the 
   four half-spaces.
1. Corresponding to a hyperplane $\HHH$, there exists
   a unique pair of sets $\SSS_1$ 
   and $\SSS_2$ that are the opposite sides
   of $\HHH$.
1. Open half spaces are open sets
   and closed half spaces are closed sets.
1. If $A$ and $B$ belong to the opposite sides of a 
   hyperplane $\HHH$, then there exists
   a unique point of $\HHH$ that is between
   $A$ and $B$.
````

### General Position


````{div}

1. A *general position* for a set of points or other
   geometric objects is a notion of genericity.
1. It means the general case situation as opposed to more special
   and coincidental cases.
1. For example, generically, two lines in a plane intersect in a single point.
1. The special cases are when the two lines are either parallel
   or coincident.
1. Three points in a plane in general are not collinear.
1. If they are, then it is a degenerate case.
1. A set of $n+1$ or more points in $\RR^n$ is in said to be
   in general position if every subset of $n$ points is linearly
   independent.
1. In general, a set of $k+1$ or more points in a $k$-flat is said to be
   in *general linear position* if no hyperplane contains
   more than $k$ points.
````

## Matrix Factorizations

### Singular Value Decomposition

````{div}
1. A non-negative real value $\sigma$ is a singular value
   for a matrix $\bA \in \RR^{m \times n}$ if and only if
   there exist unit length vectors $\bu \in \RR^m$ and $\bv \in \RR^n$
   such that $\bA \bv = \sigma \bu$ and $\bA^T \bu = \sigma \bv$.
1. The vectors $\bu$ and $\bv$ are called left singular
   and right singular vectors for $\sigma$ respectively.
1. For every $\bA \in \RR^{m \times n}$ 
   with $k = \min(m, n)$, there exist two orthogonal matrices 
   $\bU \in \RR^{m \times m}$ and $\bV \in \RR^{n \times n}$ and
   a sequence of real numbers $\sigma_1 \geq \dots \geq \sigma_k \geq 0$
   such that $\bU^T \bA \bV = \Sigma$
   where $\Sigma = \text{diag}(\sigma_1, \dots, \sigma_k, 0, \dots, 0) \in \RR^{m \times n}$
   (Extra columns or rows are filled with zeros).
1. The decomposition of $\bA$ given by
   $\bA = \bU \Sigma \bV^T$ is called the singular value decomposition of $\bA$.
1. The first $k$ columns of $\bU$ and $\bV$ are the left and right
   singular vectors of $\bA$ corresponding to the singular values
   $\sigma_1, \dots, \sigma_k$.
1. The rank of $\bA$ is equal to the
   number of non-zero singular values
   which equals the rank of $\Sigma$.
1. The eigen values of positive semi-definite matrices $\bA^T \bA$ 
   and $\bA \bA^T$ are given by $\sigma_1^2, \dots, \sigma_k^2$
   (remaining eigen values being $0$).
1. Specifically, $\bA^T \bA = \bV \Sigma^T \Sigma \bV^T$ and
   $\bA \bA^T = \bU \Sigma \Sigma^T \bU^T$. 
1. We can rewrite $\bA = \sum_{i=1}^k \sigma_i \bu_i \bv_i^T$.
1. $\sigma_1 \bu_1 \bv_1^T$ is rank-1 approximation of $\bA$
   in Frobenius norm sense.
1. The spectral radius and $2$-norm of $\bA$ is given by
   its largest singular value $\sigma_1$. 
1. The Moore-Penrose pseudo-inverse of $\Sigma$
   is easily obtained by taking the transpose of $\Sigma$ and inverting
   the non-zero singular values.
1. Further, $\bA^{\dag} = \bV \Sigma^{\dag} \bU^T$.
1. The non-zero singular values of $\bA^{\dag}$ are just reciprocals of 
   the non-zero singular values of $\bA$.
1. Geometrically, singular values of $\bA$ are the
   precisely the lengths of the semi-axes of the 
   hyper-ellipsoid $E$ defined by 
   
    $$
    E = \{ \bA \bx \ST \| \bx \|_2  = 1 \}
    $$
    (i.e. image of the unit sphere under $\bA$).
1. Thus, if $\bA$ is a data matrix, then the SVD of $\bA$
   is strongly connected with the principal component
   analysis of $\bA$.
````


## Principal Angles

````{div}
1. If $\UUU$ and $\VVV$ are two linear subspaces of $\RR^M$, then
   the *smallest principal angle* between them
   denoted by $\theta$ is defined as {cite}`bjorck1973numerical`

    $$
    \cos \theta = \underset{\bu \in \UUU, \bv \in \VVV}{\max}
    \frac{\bu^T \bv}{\| \bu \|_2 \| \bv \|_2}.
    $$
1. In other words, we try to find unit norm vectors in the two
   spaces which are maximally aligned with each other.
1. The angle between them is the smallest principal angle.
1. Note that  $\theta \in [0, \pi /2 ]$
  ($\cos \theta$ as defined above is always positive).
1. If we have $\bU$ and $\bV$ as matrices whose column spans are 
   the subspaces $\UUU$ and $\VVV$
   respectively, then in order to find the principal angles, we construct
   orthogonal bases $\bQ_U$ and $\bQ_V$.
1. We then compute the inner product matrix $\bG = \bQ_U^T \bQ_V$.
1. The SVD of $\bG$ gives the principal angles. 
1. In particular, the smallest principal angle is given by
   $\cos \theta = \sigma_1$, the largest singular value.
````

[^pca]: PCA can also be viewed as a statistical model. 
When the data points are independent samples drawn from 
a Gaussian distribution, the geometric formulation of PCA
coincides with its statistical formulation.

[^union]: We would use the
terms arrangement and union interchangeably. 
For more discussion see {ref}`sec:algebraic_geometry`.

