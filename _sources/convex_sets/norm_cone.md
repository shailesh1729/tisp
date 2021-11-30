# Norm Cones

(def:norm_cone)=
````{prf:definition}
Let $\|  \cdot \| : \RR^N \to R$ be any norm on $\RR$.
The **norm cone** associated with the norm $\| \cdot \|$ is given by the set

$$
    C = \{ (x,t) \;|\; \| x \| \leq t \} \subseteq \RR^{N+1}
$$

````

 ````{prf:remark}
 A norm cone is convex. Moreover it is a convex cone.
````


(ex:second_order_cone)=
````{prf:example} Second order cone
The second order cone is the norm cone for the Euclidean norm, i.e.

$$
    C  = \{(x,t) \;|\; \| x \|_2 \leq t \} \subseteq \RR^{N+1}
$$

This can be rewritten as

$$
    C = \left \{
    \begin{bmatrix}
    x \\ t
    \end{bmatrix}
    \middle |
    \begin{bmatrix}
    x \\ t
    \end{bmatrix}^T
    \begin{bmatrix}
    I & 0 \\
    0 & -1
    \end{bmatrix}
    \begin{bmatrix}
    x \\ t
    \end{bmatrix}
    \leq 0 , t \geq 0
    \right \}
$$
````
