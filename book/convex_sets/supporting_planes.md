# Supporting and Separating Hyperplanes


## Separating Hyperplane Theorem


```{prf:theorem} Separating hyperplane theorem
:label: res-cvx-separating-hyperplane

Let $C$ and $D$ be two convex sets in a real vector space $\VV$ that do not intersect;
i.e., $C \cap D = \EmptySet$. 
Then, there exists $\ba \in \VV^*$, $\ba \neq \bzero$ and $b \in \RR$ such that 

$$
\langle \bx, \ba \rangle \leq b \Forall \bx \in C
$$ 
and

$$
\langle \bx, \ba \rangle \geq b \Forall \bx \in D.
$$

The hyperplane given by $\{ \bx \ST \langle \bx, \ba \rangle = b \}$ is called
a *separating hyperplane* between $C$ and $D$.
```
Note that the theorem implies the existence of a separating hyperplane. It doesn't preclude
existence of a multitude of such separating hyperplanes.


```{prf:proof}

Consider the distance between $C$ and $D$ given by:

$$
\dist (C, D) = \inf \{ \| \bu - \bv \| \ST \bu \in C, \bv \in D \}.
$$


Assume that $\dist (C, D) > 0$ and there exist $\bc \in C$ and $\bd \in D$ such that
$\dist (C, D) = \| \bc - \bd \|$.

1. Define $\ba = \bd - \bc$.
1. Define $b = \frac{1}{2}(\| \bd \|^2 - \| \bc \|^2)$.
1. Consider the affine function $f(\bx) = \langle \bx, \ba \rangle - b$.
1. Note that 

   $$
   f(\bx) = \langle \bx, \bd - \bc \rangle - \frac{1}{2}\langle \bd + \bc, \bd - \bc \rangle
   = \left \langle \bx - \frac{1}{2}(\bd + \bc), \bd - \bc \right \rangle.
   $$
```
