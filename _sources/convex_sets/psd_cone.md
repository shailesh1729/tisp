# Positive Semidefinite Cone

(def:symmetric_matrices)=
````{prf:definition}
We define the **set of symmetric $N\times N$ matrices** as

$$
    S^N = \{X \in \RR^{N \times N} | X = X^T\}.
$$

````

````{prf:lemma}
$S^N$ is a vector space with dimension $\frac{N(N+1)}{2}$.
````

(def:positive_semidefinite_matrices)=
````{prf:definition}
We define the **set of symmetric positive semidefinite matrices** as

$$
    S_+^N = \{X \in S^N | X \succeq 0 \}.
$$

The notation $X \succeq 0$ means $v^T X v \geq 0 \Forall v \in \RR^N$.

````

(def:positive_definite_matrices)=
````{prf:definition}
We define the **set of symmetric positive definite matrices** as

$$
    S_{++}^N = \{X \in S^N | X \succ 0 \}.
$$

The notation $X \succ 0$ means $v^T X v  > 0 \Forall v \in \RR^N$.

````

````{prf:lemma}
The set $S_+^N$ is a convex cone.
````

````{prf:proof}
Let $A, B \in S_+^N$ and $\theta_1, \theta_2 \geq 0$. We have to show that
$\theta_1 A + \theta_2 B \in S_+^N$.

$$
    A \in S_+^N \implies v^T A v \geq 0 \Forall v \in \RR^N.
$$

$$
    B \in S_+^N \implies v^T B v \geq 0 \Forall v \in \RR^N.
$$

Now

$$
    v^T (\theta_1 A + \theta_2 B) v = \theta_1 v^T A v + \theta_2 v^T B v \geq 0 \Forall v \in \RR^N.
$$

Hence $\theta_1 A + \theta_2 B \in S_+^N$.

````
