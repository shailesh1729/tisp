(sec:ml:cluster:k-means)=
# K-Means Clustering

K-means clustering algorithm
{cite}`macqueen1967some, duda2012pattern, hartigan1975clustering`
[see {prf:ref}`alg:ml:cluster:k_means`] is an 
iterative clustering method.
We start with an initial set of means 
and covariance matrices for each cluster.
In each iteration, we segment the data points into individual clusters
by choosing the nearest mean.
Then, we estimate the new mean and covariance matrices.
We return a label vector $L[1:K]$ which maps each point to
corresponding cluster. A *within-cluster-scatter* can be defined as

$$
w(L) = \frac{1}{S} \sum_{k=1}^K \sum_{L(s) = k} \| y_s - \mu_k \|^2_{\Sigma_k}.
$$
This represents the average (squared) distance of each point
to the respective cluster mean. The $K$-means algorithm reduces
the scatter in each iteration. it is guaranteed to converge to
a local minimum.

A simpler version of this algorithm is based on Euclidean distance
and doesn't compute or updates the covariance matrices for each cluster.



````{prf:algorithm} K-means clustering
:label: alg:ml:cluster:k_means

Inputs:

* The data set $\bY = \{ \by_s\}_{s=1}^S \subset \RR^n$
* Number of clusters : $K$

Outputs:
* Clusters: $\{\bY_k^{(i)} \}_{k=1}^K$
* Cluster labels array: $L[1:S]$


Initialization:

1. $i \leftarrow 0$. # Iteration counter
1. For each cluster $k \in \{1, \dots, K\}$:
   1. Initialize $\mu_k^{(0)}$ and  $\Sigma_k^{(0)}$ suitably.
   1. Set $\bY_k^{(0)}$ to empty set.

Algorithm:


1. If the segmentation has stopped changing: break.
1. Segmentation: for each data point $\by_s \in \bY$:
   1. Find the nearest centroid via Mahanalobis distance.

       $$
       L(s) \leftarrow
            l \leftarrow \underset{k=1,\dots, K}{\text{arg min}} 
                \| \by_s - \mu_k^{(i)} \|^2_{\Sigma_k^{(i)}}.
       $$
       Use the centroid number as the label for the point.
   1. Assign $\by_s$ to the cluster $\bY_l^{(i+1)}$.
1. Estimation: for each cluster $k \in \{1, \dots, K\}$:
   1. Compute new mean/centroid for the cluster: 
   
      $$
      \mu_k^{(i+1)} \leftarrow \text{mean}(\bY_k^{(i+1)}).
      $$
   1. Compute the covariance matrix for the cluster:

      $$
      \Sigma_k^{(i+1)} \leftarrow \text{cov}(\bY_k^{(i+1)}).
      $$
1. $i \leftarrow i+1$. # Increase iteration counter
1. Go to step 1.
````


