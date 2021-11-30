# Convexity Preserving Operations

In the following, we will discuss several operations which
transform a convex set into another convex set, and thus
preserve convexity.

Understanding these operations is useful for determining
the convexity of a wide variety of sets.

Usually, it is easier to prove that a set is convex by showing
that it is obtained by a convexity preserving operation from
a convex set compared to directly verifying the convexity property
i.e. 

$$
    \theta x_1 + (1 - \theta) x_2 \in C \Forall x_1, x_2 \in C, \theta \in [0,1]
$$
.



## Intersection



````{prf:lemma}
If $S_1$ and $S_2$ are convex sets then $S_1 \cap S_2$ is convex.
````

````{prf:proof}
Let $x_1, x_2 \in S_1 \cap S_2$. We have to show that

$$
    \theta x_1 + (1 - \theta) x_2 \in S_1 \cap S_2, \Forall \theta \in [0,1].
$$

Since $S_1$ is convex and $x_1, x_2 \in S_1$, hence

$$
    \theta x_1 + (1 - \theta) x_2 \in S_1, \Forall \theta \in [0,1].
$$

Similarly

$$
    \theta x_1 + (1 - \theta) x_2 \in S_2, \Forall \theta \in [0,1].
$$

Thus

$$
    \theta x_1 + (1 - \theta) x_2 \in S_1 \cap S_2, \Forall \theta \in [0,1].
$$

which completes the proof.
````

We can generalize it further.

````{prf:lemma}
Let $\{ A_i\}_{i \in I}$ be a family of sets such that $A_i$ is convex
for all $i \in I$.  Then $\cap_{i \in I} A_i$ is convex.
````

````{prf:proof}
Let $x_1, x_2$ be any two arbitrary elements in $\cap_{i \in I} A_i$.

$$
    &x_1, x_2 \in \cap_{i \in I} A_i\\
    \implies & x_1, x_2 \in A_i \Forall i \in I\\
    \implies &\theta x_1 + (1 - \theta) x_2 \in A_i \Forall \theta \in [0,1] \Forall i \in I
    \text{ since $A_i$ is convex }\\
    \implies &\theta x_1 + (1 - \theta) x_2 \in \cap_{i \in I} A_i
$$

Hence $\cap_{i \in I} A_i$ is convex.
````




## Affine functions



(def:affine_function)=
````{prf:definition}
A function $f : \RR^N \to \RR^M$ is affine if it is a sum of a linear
function and a constant, i.e.

$$
    f = A x + b
$$

where $A \in \RR^{M \times N}$ and $b \in \RR^M$.

````

````{prf:lemma}
Let $S \subseteq \RR^N$ be convex and $f : \RR^N \to \RR^M$ be an
affine function. Then the image of $S$ under $f$ given by

$$
    f(S) = \{ f(x) | x \in S\}
$$

is a convex set.
````

It applies in the reverse direction also.
````{prf:lemma}
Let $f : \RR^K \to \RR^N $ be affine and $S \subseteq \RR^N$ be convex.
Then the inverse image of $S$ under $f$ given by

$$
    f^{-1}(S) = \{ x \in \RR^K | f(x) \in S\}
$$

is convex.
````

````{prf:example} Affine functions preserving convexity

Let $S \in \RR^N$ be convex.

*   For some $\alpha \in \RR$ ,
$\alpha S$  given by

$$
    \alpha S = \{\alpha x | x \in S\}
$$

is convex. This is the **scaling** operation.
*  For some $a \in \RR^N$, $ S + a$ given by

$$
    S + a = \{x + a | x \in S\}
$$

is convex. This is the **translation** operation.
*  Let $N = M + K$ where $M, N \in \Nat$. Then, let
$\RR^N = \RR^M \times \RR^K$.
A vector $x \in S$ can be written as $x = (x_1, x_2)$
where $x_1 \in \RR^M$ and $x_2 \in \RR^K$.
Then

$$
    T = \{ x_1 \in \RR^M | (x_1, x_2) \in S \text{ for some } x_2 \in \RR^K\}
$$

is convex. This is the **projection** operation.

````

(def:sum_of_two_sets)=
````{prf:definition}
Let $S_1$ and $S_2$ be two arbitrary subsets of $\RR^N$. Then their **sum**
is defined as

$$
    S_1 + S_2  = \{ x + y | x \in S_1 , y \in S_2\}.
$$

````

````{prf:lemma}
Let $S_1$ and $S_2$ be two convex subsets of $\RR^N$. Then
$S_1 + S_2$ is convex.
````
