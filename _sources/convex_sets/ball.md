# Euclidean Balls and Ellipsoids

(def:euclidean_closed_ball)=
````{prf:definition}
A **Euclidean closed ball** (or just ball) in $\RR^N$ has the form

$$
    B = \{ x | \|  x - x_c\|_2 \leq r \} = \{x | (x - x_c)^T (x  - x_c) \leq r^2 \},
$$

where $r > 0$ and $ \| \cdot \|_2$ denotes the Euclidean norm.

$x_c$ is the **center** of the ball.

$r$ is the **radius** of the ball.
````

An equivalent definition is given by

$$
    B = \{x_c +  r u \, | \, \| u \|_2 \leq 1  \}.
$$


````{prf:remark}
A Euclidean ball is a convex set.
````

````{prf:proof}
Let $x_1, x_2$ be any two points in $B$. We have

$$
    \| x_1 - x_c\|_2 \leq r
$$

and

$$
    \| x_2 - x_c\|_2 \leq r
$$

Let $\theta \in [0,1]$ and consider the point $x  = \theta x_1 + (1 - \theta) x_2$.
Then

$$
    \| x - x_c \|_2 &= \| \theta x_1 + (1 - \theta) x_2 - x_c\|_2\\
    &=  \| \theta (x_1 - x_c) + (1 - \theta) (x_2 - x_c) \|_2\\
    &\leq \theta \| (x_1 - x_c)\|_2  + (1 - \theta)\| (x_2 - x_c)\|_2\\
    &\leq \theta r + (1 - \theta) r\\
    &= r
$$

Thus $x \in B$, hence $B$ is a convex set.
````

(def:ellipsoid)=
````{prf:definition}
An **ellipsoid** is a set of the form

$$
    \xi = \{x | (x - x_c)^T P^{-1} (x - x_c) \leq 1\}
$$

where $P = P^T \succ 0$ i.e. $P$ is symmetric and positive definite.

The vector $x_c \in \RR^N$ is the **centroid** of the ellipse.

Eigen values of the matrix $P$ (which are all positive) determine
how far the ellipsoid extends in every direction from $x_c$.

The lengths of semi-axes of $\xi$ are given by $\sqrt{\lambda_i}$
where $\lambda_i$ are the eigen values of $P$.
````

 ````{prf:remark}
 A ball is an ellipsoid with $P = r^2 I$.
````


An alternative representation of an ellipsoid is given by

$$
    \xi = \{x_c + A u | \| u\|_2 \leq 1 \}
$$

where $A$ is a square and nonsingular matrix.

To show the equivalence of the two definitions, we proceed as follows.

Let $P = A A^T$. Let $x$ be any arbitrary element in $\xi$.

Then $x - x_c = A u$ for some $u$ such that $\| u \|_2 \leq 1$.

Thus

$$
    &(x - x_c)^T P^{-1} (x - x_c) =  (A u)^T (A A^T)^{-1} (A u)\\ 
    &= u^T A^T (A^T)^{-1} A^{-1} A u = u^T u  \\
    &= \| u \|_2^2 \leq 1
$$


The two representations of an ellipsoid are therefore equivalent.

````{prf:remark}
An ellipsoid is a convex set.
````
