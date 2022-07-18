# Similarity Measures

This section provides a review of popular similarity
and dissimilarity measures in literature.

The following is an informal definition of similarity coefficients.

```{prf:definition} Similarity coefficient
:label: ml-cl-similarity-coefficient

Let $\bX$ be a dataset of $n$ data points sampled from
the Euclidean space $\RR^d$. Then the *similarity coefficient*
is some function $s : \RR^d \times \RR^d \to \RR$ for
any pair of data points $\bx, \by \in \RR^d$
with a structure

$$
s(\bx, \by) = s(x_1, \dots, x_d, y_1, \dots, y_d)
$$
which grows as the data points look similar to each other
and satisfies the following properties

1. $0 \leq s(\bx, \by) \leq 1$.
1. $s (\bx, \bx) = 1$ for every $\bx \in \RR^d$.
1. $s(\bx, \by) = s(\by, \bx)$.
```

Normally, we require that the similarity coefficient is symmetric; i.e.,

```{math}
s(\bx, \by) = s(\by, \bx).
```
There are rare cases where asymmetric similarity coefficients have
been used.


```{prf:example} Similarity from metrics
:label: ex-ml-cl-similarity-distance-1

Let $d$ be a metric (distance function) defined on $\RR^n$.
Then we have for any $\bx, \by, \bz \in \RR^d$,

1. $d (\bx, \bx)  = 0$.
1. $d (\bx, \by) \geq 0$.
1. $d (\bx, \by) = d(\by, \bx)$.
1. $d (\bx, \by) \leq d(\bx, \bz) + d(\bz, \by)$.

One way to induce a similarity coefficient is:

$$
s(\bx, \by) = \exp (- d(\bx, \by)).
$$

We can see that

1. Since $\exp(t) \geq 0$ for every $t \in \RR$, hence $s(\bx, \by) \geq 0$.
1. Since $d(\bx, \by) \geq 0$, hence $s(\bx, \by) \leq 1$.
1. Since $d$ is symmetric, hence $s$ is symmetric.
1. Since $d(\bx, \bx) = 0$, hence $s (\bx, \bx) = 1$.

Thus, $s$ is indeed a similarity coefficient.

Note that a metric satisfies the triangle inequality. However,
this property was not required for the similarity coefficient
induced from the metric.
Thus, a metric imposes an additional structure which is more
stringent than the needs for a similarity measure.
``` 

