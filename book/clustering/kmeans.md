(sec:ml:cluster:k-means)=
# K-Means Clustering

## Introduction

K-means clustering algorithm
{cite}`macqueen1967some, duda2012pattern, hartigan1975clustering`
[see {prf:ref}`alg:ml:cluster:k_means`] is a hard clustering algorithm.

1. The input to an algorithm is an unlabeled dataset
   
   $$
   \bX = \{ \bx_1, \bx_2, \dots, \bx_n \}.
   $$
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
1. Each cluster $C_j$ is represented by a centroid (or a mean vector) $\mu_j$
   and its covariance matrix $\Sigma_j$.
1. The algorithm consists of two major steps: 

   1. Segmentation
   1. Estimation
1. The goal of segmentation step is to partition the data points
   into their nearest cluster centroids.
1. The goal of estimation step is to compute the new mean and
   covariance matrix based on the current clustering.
1. We start with an initial set of means and covariance matrices for each cluster.
1. In each iteration, we segment the data points into individual clusters
   by choosing the nearest centroid.
1. Then, we estimate the new mean and covariance matrices.
1. We return a label vector $L[1:k]$ which maps each point to
   corresponding cluster. 


## Example

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

A *within-cluster-scatter* can be defined as

$$
w(L) = \frac{1}{n} \sum_{j=1}^k \sum_{L(s) = j} \| y_s - \mu_j \|^2_{\Sigma_j}.
$$
This represents the average (squared) distance of each point
to the respective cluster mean. The $k$-means algorithm reduces
the scatter in each iteration. it is guaranteed to converge to
a local minimum.

A simpler version of this algorithm is based on Euclidean distance
and doesn't compute or updates the covariance matrices for each cluster.

## Algorithm

````{prf:algorithm} k-means clustering
:label: alg:ml:cluster:k_means

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
   1. Find the nearest centroid via Mahanalobis distance.

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


