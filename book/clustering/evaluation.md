# Evaluation

There are two possible approaches for
evaluation of a clustering algorithm.

1. Full reference
1. No reference

In full reference evaluation, a ground truth
about an ideal clustering of the data is given.
E.g., suppose our goal is to cluster a set of
facial images of different persons. The ground
truth in this case is the name/id of each person
associated with each image.

## Full Reference Evaluation

Let $\bY$ be a given set of data points.
Assume that the ideal/reference clustering of $\bY$
is given beforehand.

1. Assume that the dataset $\bY$ can be divided into $K$ clusters.
1. Let these clusters be named $\bY_1, \dots, \bY_K$.
1. Assume that it is known which point belongs to which
   cluster.

In general a *clustering* $\CCC$ of a set $\bY$ constructed
by a clustering algorithm is a set
$\{\CCC_1, \dots, \CCC_C\}$ of non-empty disjoint subsets
of $\bY$ such that their union equals $\bY$.
Clearly: $|\CCC_c| > 0$.


The clustering process may make a number of mistakes.

1. It may identify incorrect number of clusters
   and $C$ may not be equal to $K$.
1. More-over even if $K = C$, 
   the data points may be placed in wrong clusters.

Ideally, we want $K = C$ and $\CCC_c = Y_k$
with a bijective mapping between
$1 \leq c \leq C$ and $1 \leq k \leq K$.
In practice, a clustering algorithm estimates the number of
clusters $C$ and
assigns a label $l_s$, $1 \leq s \leq S$ to each vector
$y_s$ where $1\leq l_s \leq C$.  
All the labels can be put in a label vector $L$
where $L \in \{1, \dots, C\}^S$.
The permutation matrix $\Gamma$ can be easily 
obtained from $L$.
 


Following {cite}`wagner2007comparing`,
we will quickly establish the commonly used measures for 
clustering performance. 
1. We have a reference clustering of
   vectors in $\bY$ given by
   $\BBB = \{\bY_1, \dots, \bY_K\}$ which is known
   to us in advance
   (either by construction in synthetic experiments
   or as ground truth with real life data-sets). 
1. The clustering obtained
   by the algorithm is given by
   $\CCC= \{\CCC_1, \dots, \CCC_C\}$.

````{div}
For two arbitrary points $\by_i, \by_j \in \bY$, there are four possibilities:

1. they belong to same cluster in both $\BBB$ and $\CCC$ (true positive),
1. they are in same cluster in $\BBB$ but different cluster in $\CCC$
   (false negative)
1. they are in different clusters in $\BBB$ but in same cluster in $\CCC$
1. they are in different clusters in both $\BBB$ and $\CCC$ (true negative).

Consider some cluster $\bY_i \in \BBB$ and $\CCC_j \in \CC$. 
1. The elements common to $\bY_i$ and $\CCC_j$ are given by $\bY_i \cap \CCC_j$.
1. We define

    $$
    \text{precision}_{i j} \triangleq \frac{|\bY_i \cap \CCC_j|}{|\CCC_j|}.
    $$
1. We define the overall precision for $\CCC_j$ as

    $$
    \text{precision}(\CCC_j) \triangleq  \underset{i}{\max}(\text{precision}_{i j}).
    $$
1. We define $\text{recall}_{i j} \triangleq \frac{|\bY_i \cap \CCC_j|}{|\bY_i|}$.
1. We define the overall recall for $\bY_i$ as
   
   $$
   \text{recall}(\bY_i) \triangleq  \underset{j}{\max}(\text{recall}_{i j}).
   $$
1. We define the $F$ score as
   
   $$
   F_{i j} \triangleq 
   \frac{2 \text{precision}_{i j} \text{recall}_{i j} }
   {\text{precision}_{i j} + \text{recall}_{i j}}.
   $$
1. We define the overall $F$-score for $\bY_i$ as 
   
   $$
   F(\bY_i) \triangleq  \underset{j}{\max}(F_{i j}).
   $$
1. We note that cluster $\CCC_j$ for which the maximum is achieved
   is best matching cluster for $\bY_i$.
1. Finally, we define the overall $F$-score for the clustering 
   
   $$
   F(\BBB, \CCC) \triangleq  \frac{1}{S}\sum_{i=1}^p |\bY_i | F(\bY_i)
   $$
  where $S$ is the total number of vectors in $\bY$.
1. We also define a clustering ratio given by the factor 
   
   $$
   \eta \triangleq \frac{C}{K}.
   $$

There are different ways to define *clustering error*.
For the special case where the number of clusters is known in advance,
and we ensure that the data-set is divided into exactly those many
clusters, it is possible to define subspace clustering error as
follows:

$$
\text{clustering error}
= \frac{\text{# of misclassified points}}
{\text{total # of points}}.
$$
The definition is adopted from {cite}`elhamifar2013sparse` for comparing
the results in this paper with their results. This definition can be
used after a proper one-one mapping between original labels
and cluster labels assigned by the clustering algorithms has been 
identified. We can compute this mapping by comparing $F$-scores.







