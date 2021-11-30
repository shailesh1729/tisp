# Hyperplanes and Half spaces

(def:hyperplane)=
````{prf:definition}
A **hyperplane**  is a set of the form

$$
       H =  \{ x : a^T x = b \}
$$

where $a \in \RR^N, a \neq 0$ and $b \in \RR$.

The vector $a$ is called the **normal vector** to the hyperplane.
````


*  Analytically, it is a solution set of a 
   nontrivial linear equation. 
   Thus, it is an affine set.
*  Geometrically, it is a set of points with a 
   constant inner product to a given vector $a$.

Let $x_0$ be an arbitrary element in $H$. Then

$$
             &a^T x_0 = b\\
    \implies &a^T x = a^T x_0 \Forall x \in H\\
    \implies &a^T (x - x_0) = 0 \Forall x \in H\\
    \implies &H = \{ x | a^T(x-x_0) = 0\}
$$


Consider the *orthogonal complement* of $a$ defined as

$$
    a^{\bot} = \{ v | a^T v  = 0\}
$$


i.e. the set of all vectors that are orthogonal to $a$.

Now, consider the set

$$
    S = x_0 + a^{\bot} 
$$


Clearly, for every $x \in S$, $a^T x = a^T x_0 = b$.

Thus, we can say that

$$
    H = \{ x | a^T(x-x_0) = 0\} = x_0 + a^{\bot}
$$


Thus, the hyperplane consists of an offset $x_0$ plus 
all vectors orthogonal to the (normal) vector $a$.

(def:halfspace)=
````{prf:definition}
A hyperplane divides $\RR^N$ into two **halfspaces**.
The two (closed) halfspaces are given by

$$
    H_+ = \{ x : a^T x \geq b \}
$$

and

$$
    H_- = \{ x : a^T x \leq b \}
$$

The halfspace $H_+$ extends in the direction of $a$ while
$H_-$ extends in the direction of $-a$.
````


*  A halfspace is the solution set of one (nontrivial) linear inequality.
*  A halfspace  is convex but not affine.
*  The halfspace can be written alternatively as 

$$
    H_+  = \{ x | a^T (x - x_0) \geq 0\}\\
    H_-  = \{ x | a^T (x - x_0) \leq 0\}
$$


where $x_0$ is any point in the associated hyperplane $H$.
*  Geometrically, points in $H_+$ make an acute angle with $a$ while
points in $H_-$ make an obtuse angle with $a$.


(def:open_halfspace)=
````{prf:definition}
The sets given by

$$
    \Interior{H_+} = \{ x | a^T x > b\}\\
    \Interior{H_-} = \{ x | a^T x < b\}
$$

are called **open halfspaces**. They are the interior
of corresponding closed halfspaces.
````
