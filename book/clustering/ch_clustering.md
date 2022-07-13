(ch:ml:clustering)=
# Clustering

In this chapter, we review some of the traditional 
and general purpose data clustering algorithms. 
The objective of data clustering
is to group the data points into clusters such that
points within each cluster are more related to each other 
than points across different cluster. The relationship
can be measured in various ways: distance between points,
similarity of points, etc.
In distance based clustering, we group the points
into $K$ clusters such that the distance among points in the
same group is significantly smaller than those between clusters.
In similarity based clustering, 
the points within the same cluster are more similar
to each other than points from different cluster. 
A graph based clustering will treat each point as a node
on a graph [with appropriate edges] and split the graph
into connected components.

````{div}
Simplest distance measure is the standard Euclidean distance measure.
But it is susceptible to the choice of basis.
This can be improved by adopting a statistical model for data in each cluster.
We assume that the data in $k$-th cluster is sampled
from a probability distribution with mean $\mu_k$ and covariance
$\Sigma_k$. An appropriate distance measure from the mean of a 
distribution which is invariant of the
choice of basis is the *Mahanalobis distance*:

$$
d^2 (\bx_s, \mu_k) 
= \| \bx_s - \mu_k\|_{\Sigma_k}^2 
= (\bx_s - \mu_k)^T \Sigma_k^{-1}(\bx_s - \mu_k).
$$
For Gaussian distributions, this is proportional to the negative
of the log-likelihood of a sample point. 
A simple way to measure similarity between two points is the
absolute value of the inner product. Alternatively, one can
look at the angle between two points or inner product of the normalized
points. Another way to measure similarity is to consider the
inverse of an appropriate distance measure.
````

