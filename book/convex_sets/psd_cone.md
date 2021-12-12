# Positive Semidefinite Cone

````{prf:definition} Symmetric matrix
:label: def-symmetric-matrix

We define the *set of symmetric $n\times n$ matrices* as

$$
    \SS^n = \{X \in \RR^{n \times n} | X = X^T\}.
$$

````

````{prf:lemma}
$\SS^n$ is a vector space with dimension $\frac{n(n+1)}{2}$.
````

````{prf:definition} Positive semidefinite matrix
:label: def-positive-semidefinite-symmetric-matrix

We define the *set of symmetric positive semidefinite matrices* as

$$
    \SS_+^n = \{X \in \SS^n | X \succeq 0 \}.
$$

The notation $X \succeq 0$ means $v^T X v \geq 0 \Forall v \in \RR^n$.

````

````{prf:definition} Positive definite matrix
:label: def-positive-definite-symmetric-matrix

We define the *set of symmetric positive definite matrices* as

$$
    \SS_{++}^n = \{X \in \SS^n | X \succ 0 \}.
$$

The notation $X \succ 0$ means $v^T X v  > 0 \Forall v \in \RR^n$.

````

````{prf:lemma}
The set $\SS_+^n$ is a convex cone.
````

````{prf:proof}
Let $A, B \in \SS_+^n$ and $\theta_1, \theta_2 \geq 0$. We have to show that
$\theta_1 A + \theta_2 B \in \SS_+^n$.

$$
    A \in \SS_+^n \implies v^T A v \geq 0 \Forall v \in \RR^n.
$$

$$
    B \in \SS_+^n \implies v^T B v \geq 0 \Forall v \in \RR^n.
$$

Now

$$
    v^T (\theta_1 A + \theta_2 B) v = \theta_1 v^T A v + \theta_2 v^T B v \geq 0 \Forall v \in \RR^n.
$$

Hence $\theta_1 A + \theta_2 B \in \SS_+^n$.
````
