(sec:ml:cluster:k-means)=
# K-Means Clustering

An initial version of the k-means algorithm was originally
developed by Lloyd in 1957 but was published for the
first time in 1982 {cite}`lloyd1982least`.

Given a set of $n$ data points in $\RR^m$, the objective
is to select $k$ centroids so as to minimize the
sum of squared distances between each point and
its closest centroid. In general the problem is
NP-hard but a local search method to this problem
as described in {prf:ref}`alg:ml:cluster:k_means`
is generally quite successful in finding reasonable
solutions.

See {cite}`macqueen1967some, duda2012pattern, hartigan1975clustering`
for a detailed treatment of the algorithm.

## Basic Algorithm

K-means clustering algorithm is a hard clustering algorithm
as it assigns each data point to exactly one cluster.

````{prf:algorithm} Basic k-means clustering algorithm
:label: alg:ml:cluster:k_means

1. Select $k$ points as initial centroids.
1. Repeat
   1. Segmentation: Form $k$ clusters by assigning all points to the
      nearest centroid.
   2. Estimation: Recompute the centroid for each cluster.
5. Until the segmentation has stopped improving.
````


1. The input to an algorithm is an unlabeled dataset
   
   $$
   \bX = \{ \bx_1, \bx_2, \dots, \bx_n \}
   $$
   where each data point belongs to the ambient feature
   space $\RR^m$.
1. Our goal is to partition the dataset into $k$ different clusters.
1. The clustering is denoted by

   $$
   \CCC = \{C_1, \dots, C_k \}
   $$
   where $C_j$ is the list of indices of data points
   belonging to the $j$-th cluster.
1. The clustering can be conveniently represented in the form
   of a label array $L$ consisting of $n$ entries
   each of which can take a value from $\{ 1, \dots, k \}$.
1. In other words, if $L[i] = j$, then the data point
   $\bx_i$ belongs to the $j$-th cluster ($i \in C_j$).
1. Each cluster $C_j$ is represented by a centroid (or a mean vector) $\mu_j$.
1. The algorithm consists of two major steps: 

   1. Segmentation
   1. Estimation
1. The goal of segmentation step is to partition the data points
   into clusters according to the nearest cluster centroids.
1. The goal of estimation step is to compute the new centroid
   for each cluster based on the current clustering.

   $$
   \mu_j = \frac{1}{n} \sum_{i \in C_j} \bx_i.
   $$
1. We start with an initial set of centroids for each cluster.
1. One way to pick the initial centroids is to pick $k$ points
   randomly from the dataset.
1. In each iteration, we segment the data points into individual clusters
   by assigning a data point to the cluster corresponding to
   the nearest centroid.
1. Then, we estimate the new centroid for each cluster.
1. We return a labels array $L$ which maps each point to
   corresponding cluster.


We note that the basic structure of the k-means is not
really an algorithm. It is more like a template of the
algorithm. For a concrete implementation of the
k-means algorithm, there are many aspects that
need to be carefully selected.

- Initialization of the centroids
- Number of clusters
- Choice of the distance metric
- Criterion for evaluation of the quality of the clustering
- Stopping criterion

### Example

````{prf:example} A k-means example
:label: ex-ml-cl-kmeans-1

We show a simple simulation of k-means algorithm.

- The data consists of randomly generated points
  organized in 4 clusters.
- The algorithm is seeded with random points at
  the beginning.
- After each iteration, the centroids are moved
  to a new location based on the current members
  of the cluster.
- The animation below shows how the centroids
  are moving and cluster memberships are changing.

```{figure} images/kmeans/kmeans.gif
This animation shows how the centroids move from one iteration to the
next. The centroids have been initialized randomly in the first iteration.
```

The figure below shows the clusters and centroids of all the
six iterations in a grid. You can open this figure in
a different tab to see its enlarged version.

```{figure} images/kmeans/grid.png
```

We have 4 centroids randomly initialized
at iteration 1. Let us call them as

- A near $(-5, -8)$  (centroid of yellow cluster)
- B near $(1.5, -1)$ (centroid of blue cluster)
- C near $(6, 2.5)$ (centroid of the green cluster)
- D near $(8.5, 6)$ (centroid of the purple cluster)

Look at centroid A over time

- It starts from the location $(-5, -8)$.
- More than half of the points from the eventual blue
  cluster are still belonging to the yellow cluster
  in the first iteration.
- As the centroid starts moving towards its eventual
  location near $(-9, -8.5)$, extra points from 
  the yellow cluster are dropped.

Next look at the journey of centroid B.

- In the beginning it contains about 70% points
  of the cluster around origin and only about 20%
  points of the cluster around $(1.5, -7.5)$.
- But it is enough to start pulling the centroid
  downward.
- As the centroid C starts moving left & down, 
  the points around origin start becoming green.
- Since centroid A is also moving left, the points
  around $(1.5, -7.5)$ start turning blue.

Centroid D doesn't really move much.
- Initially it is in competition with centroid C
  for some of its points around its boundary.
- However as C starts moving to its final destination,
  all the points around D turn purple.
- Since not many points had to change cluster membership
  here, hence their centroid location didn't shift much
  over these iterations.


We also note that after iteration 5, there is no further
change in cluster memberships. Hence the centroids stop
moving.
````

### Stopping Criterion

As we noticed that in the previous example that
centroids converge fast during the initial iterations
and then they start moving very slowly. Once the
segmentation stops changing, then the centroids
will also stop moving. When the cluster boundaries
are not clear, it is often good enough to stop
the algorithm when relatively very few points
are changing clusters.


### Evaluation

````{div}
A simple measure for the evaluation of the k-means algorithm
is the within-cluster-scatter given by

$$
S = \sum_{j=1}^k \sum_{i \in C_j} (\bx_i - \mu_j)^T (\bx_i - \mu_j) 
= \sum_{j=1}^k \sum_{i \in C_j} \| \bx_i - \mu_j \|_2^2.
$$
````
As can be seen from the formula, this is essentially the
sum of squared errors w.r.t. the corresponding cluster centroids.

### Convergence

It can be shown that the scatter is monotonically decreasing over the
k-means iterations.

1. One can easily see that there are only at most $k^n$ possible
   clusterings.
1. Each partition has a different value of scatter.
1. Since the scatter is monotonically decreasing, hence no configuration
   is repeated twice.
1. Since the number of possible clusterings is finite, hence the
   algorithm must terminate eventually.



### Number of Clusters

The algorithm requires that the user provide the desired
number of clusters $k$ as an input to the algorithm.
It doesn't discover the the number of clusters automatically.
We can also see that one straight-forward way to decrease
the within cluster scatter is to increase the number of
clusters.
In fact, when $k=n$, then the optimal within cluster scanner
will be $0$.
However, a lower scatter may provide a clustering which will
not be very useful. 

This begs the question how do we select the number of clusters?
Here are a few choices:

- Run the algorithm on the data with different values of $k$
  and then choose a clustering by inspecting the results.
- Use another clustering method like EM.
- Use some domain specific prior knowledge to decide the
  number of clusters.

### Initialization

There are a few options for selection
of initial centroids:

1. Randomly chosen data points from the data set.
1. Random points in the feature space $\RR^m$.
1. Create a random partition of $\bX$ into $k$ clusters and take
   the centroid of each partition.
1. Identify regions of space which are dense
   (in terms of number of data points per unit volume)
   and then select points from those regions as centroids.
1. Uniformly spaced points in the feature space.

Later, we will discuss a specific algorithm called
k-means++ which carefully selects the initial centroids.

k-means algorithm doesn't provide a globally optimal clustering
for a given number of clusters. It does converge to a locally
optimal solution based on the initial selection of the centroids.

One way to address this is to run the k-means algorithm multiple
times with different initializations. At the end, we
select the clustering with the smallest scatter.


## Scale and Correlation

One way to address the issue of scale variation in features
and correlation among features is using the Mahalanobis distance
for distance calculations. To do this, in the estimation step
we shall calculate the covariance matrix for each cluster
separately.


````{prf:algorithm} k-means clustering with Mahalanobis distance
:label: alg-ml-cl-k-means-mahalanobis

Inputs:

* The data set $\bX = \{ \bx_s\}_{s=1}^n \subset \RR^m$
* Number of clusters : $k$

Outputs:
* Clusters: $\{\bX_j^{(i)} \}_{j=1}^k$
* Cluster labels array: $L[1:n]$


Initialization:

1. $i \leftarrow 0$. # Iteration counter
1. For each cluster $j \in \{1, \dots, k\}$:
   1. Initialize $\mu_j^{(0)}$ and  $\Sigma_j^{(0)}$ suitably.
   1. Set $\bX_j^{(0)}$ to empty set.

Algorithm:


1. If the segmentation has stopped changing: break.
1. Segmentation: for each data point $\bx_s \in \bX$:
   1. Find the nearest centroid via Mahalanobis distance.

       $$
       L(s) \leftarrow
            l \leftarrow \underset{j=1,\dots, k}{\text{arg min}} 
                \| \bx_s - \mu_j^{(i)} \|^2_{\Sigma_j^{(i)}}.
       $$
       Use the centroid number as the label for the point.
   1. Assign $\bx_s$ to the cluster $\bX_l^{(i+1)}$.
1. Estimation: for each cluster $j \in \{1, \dots, k\}$:
   1. Compute new mean/centroid for the cluster: 
   
      $$
      \mu_j^{(i+1)} \leftarrow \text{mean}(\bX_j^{(i+1)}).
      $$
   1. Compute the covariance matrix for the cluster:

      $$
      \Sigma_j^{(i+1)} \leftarrow \text{cov}(\bX_j^{(i+1)}).
      $$
1. $i \leftarrow i+1$. # Increase iteration counter
1. Go to step 1.
````

A *within-cluster-scatter* can be defined as

$$
w(L) = \frac{1}{n} \sum_{j=1}^k \sum_{L(s) = j} \| y_s - \mu_j \|^2_{\Sigma_j}.
$$
This represents the average (squared) distance of each point
to the respective cluster mean. The $k$-means algorithm reduces
the scatter in each iteration. it is guaranteed to converge to
a local minimum.

