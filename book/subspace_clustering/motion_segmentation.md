(sec:sscl:motion:segmentation)=
# Motion Segmentation

The theory of structure from motion and motion segmentation
has evolved over a set of papers 
{cite}`tomasi1991detection,tomasi1992shape,boult1991factorization,poelman1997paraperspective,gear1998multibody,costeira1998multibody,kanatani2001motion`. 
In this section, we review the essential ideas
from this series of work.

A typical image sequence 
(from a single camera shot)
may contain multiple objects moving
independently of each other.
In the simplest model, we can assume that images in a sequence
are views of a single moving object observed by a stationary camera or
a stationary object observed by a moving camera.
Only rigid motions are considered.
In either case, the object is moving with respect to the camera.

The *structure from motion* problem
focuses on recovering the (3D) shape and motion information
of the moving object. 
In the general case, there are multiple objects moving
independently.
Thus, we also need to perform a
*motion segmentation* such that motions of 
different objects can be separated and (either
after or simultaneously) shape and motion of each object
can be inferred. 

This problem is typically solved in two stages. In the first
stage, a frame to frame correspondence problem is solved which
identifies 
a set of feature points whose coordinates can be tracked
over the sequence as the point moves from one position to 
other in the sequence.
We obtain a set of
trajectories for these points over the frames in the video.
If there is a single moving object
or the scene is static and the observer is moving then 
all the feature points will belong to the same object.
Otherwise, we need to cluster these feature points to
different objects moving in different directions.
In the second stage, these trajectories are analyzed to group
the feature points into separate objects and recover the shape
and motion for individual objects. In this section we 
assume that the feature trajectories have been obtained
by an appropriate method. Our focus is to 
identify the moving objects and
obtain the
shape and motion information for each object from the
trajectories.

 
## Modeling Structure from Motion for Single Object

````{div}

We start with the simple model of a static camera
and a moving object. All feature point trajectories belong
to the moving object. Our objective is to demonstrate
that the subspace spanned by feature trajectories
of a single moving object is a low dimensional
subspace.

Let the image sequence consist of $F$ frames denoted by
$1 \leq f \leq F$. Let us assume that $S$ 
feature points of the moving object have been tracked
over this image sequence. Let $(u_{f s}, v_{f s})$ be the
image coordinates of the $s$-th point in $f$-th frame.
We form the feature trajectory vector for the $s$-th
point by stacking its coordinates for the $F$ frames
vertically as

$$
\by_s = \begin{bmatrix} 
u_{1 s} & v_{1 s} & u_{2 s} & v_{2 s} & \dots & 
u_{F s} & v_{F s} 
\end{bmatrix}^T. 
$$
Putting together the feature trajectory vectors of $S$
points in a single feature trajectory matrix, we obtain 

$$
\bY = \begin{bmatrix} \by_1 & \by_2 &\dots & \by_S \end{bmatrix}.
$$
This is the data matrix under consideration from which
the shape and motion of the object need to be inferred.

We need two coordinate systems. We use the camera
coordinate system as the world coordinate system
with the $Z$-axis along the optical axis. The coordinates
of different points in the object are changing from
frame to frame in the world coordinate system as the object
is moving. We also establish a coordinate system within
the object with origin at the centroid of the feature points
such that the coordinates of individual points do not
change from frame to frame in the object coordinate system.
The (rigid) motion of the object is then modeled by the
translation (of the centroid) and rotation of its coordinate
system with respect to the world coordinate system. Let
$(a_s, b_s, c_s)$ be the coordinate of the $s$-th point
in the object coordinate system. Then, the matrix

$$
\begin{bmatrix}
a_1 & a_2 & \dots & a_S\\
b_1 & b_2 & \dots & b_S\\
c_1 & c_2 & \dots & c_S\\
\end{bmatrix}
$$
represents the shape of the object (w.r.t. its centroid).

Let us choose an orthonormal basis in the object coordinate
system. Let $\bd_f$ be the position of the centroid and 
$(\bi_f, \bj_f, \bk_f)$ be the (orthonormal) basis vectors of 
the object coordinate system in the $f$-th frame. Then,
the position of the $s$-th point in the world coordinate
system in $f$-th frame is given by

$$
\bh_{f s} = \bd_f + a_s \bi_f + b_s \bj_f + c_s \bk_f.
$$
Assuming orthographic projection and letting
$\bh_{f s} = (u_{f s}, v_{f s}, w_{f s})$, the image 
coordinates are obtained by chopping of the third component
$w_{f s}$.
We define the rotation matrix for $f$-th frame as 

$$
\bR_f \triangleq \begin{bmatrix} 
\bi_f & \bj_f & \bk_f
\end{bmatrix}
= \begin{bmatrix} 
\underline{\bi}_f \\ \underline{\bj}_f 
\\ \underline{\bk}_f 
\end{bmatrix}
$$
where $\underline{\bi}_f$, $\underline{\bj}_f$, $\underline{\bk}_f$
are the row vectors of $\bR_f$.
Let $\bx_s = (a_s, b_s, c_s, 1)$
be the homogeneous coordinates of the $s$-th point in object
coordinate system.
We can write the homogeneous coordinates
in camera coordinate system as 

$$
\begin{bmatrix}
\bh_{f s}\\
1
\end{bmatrix}
=
\begin{bmatrix}
\bR_f & \bd_f \\
\bzero_{1 \times 3} & 1
\end{bmatrix}
\bx_s.
$$
If we write $\bd_f = (d_{f i}, d_{f j}, d_{f k})$, then, the
data matrix $\bY$ can be factorized as

$$
\bY = \begin{bmatrix}
u_{11} & \dots & u_{1S}\\
v_{11} & \dots & v_{1S}\\
\vdots & \dots & \vdots \\
\vdots & \dots & \vdots \\
u_{F1} & \dots & u_{FS}\\
v_{F1} & \dots & v_{FS}
\end{bmatrix}
=
\left[ 
\begin{array}{c|c}
\underline{\bi}_1 & d_{1i}\\
\underline{\bj}_1 & d_{1j}\\
\vdots & \vdots \\ 
\vdots & \vdots \\ 
\underline{\bi}_F & d_{Fi}\\
\underline{\bj}_F & d_{Fj}
\end{array}
\right]
\begin{bmatrix}
\bx_1 & \dots & \bx_S
\end{bmatrix}.
$$
We rewrite this as 

$$
\bY  = \MM \SS
$$
where $\MM$ represents the motion
information of the object and
$\SS$
represents the shape information of the object. 
This factorization is known as
the *Tomasi-Kanade factorization* of shape and motion
information of a moving object.
Note that $\MM \in \RR^{2F \times 4}$ 
and $\SS \in \RR^{4 \times S}$. Thus
the rank of $\bY$ is at most 4. 
Thus the feature trajectories
of the rigid motion of an object span an 
up to 4-dimensional
subspace of the trajectory space $\RR^{2F}$. 
````

## Solving the Structure From Motion Problem

````{div}
We digress a bit to understand how to perform the
factorization of $\bY$ into $\MM$ and $\SS$.
Using SVD, $\bY$ can be decomposed as

$$
\bY = \bU \Sigma \bV^T.
$$
Since $\bY$ is at most rank $4$, we keep only the 
first 4 singular values as 

$$
\Sigma = \text{diag}(\sigma_1, \sigma_2, \sigma_3, \sigma_4).
$$
Matrices $\bU \in \RR^{2F \times 4}$
and $\bV \in \RR^{S \times 4}$
are the left and right singular matrices respectively.

There is no unique factorization of $\bY$ in general. 
One simple factorization can be obtained by defining:

$$
\widehat{\MM} = \bU \Sigma^{\frac{1}{2}},
\quad
\widehat{\SS} = \Sigma^{\frac{1}{2}} \bV^T.
$$
But for any $4 \times 4$ invertible matrix $\bA$, 

$$
\MM = \widehat{\MM} \bA,
\quad
\SS = \bA^{-1}\widehat{\SS}
$$
is also a possible solution since
$\MM \SS = \widehat{\MM} \widehat{\SS} = \bY$. 
Remember that $\MM$ is not an arbitrary matrix
but represents the rigid motion of an object. There is 
considerable structure inside the motion matrix. These
structural constraints can be used to compute an appropriate
$\bA$ and thus obtain $\MM$ from $\widehat{\MM}$.
To proceed further, let us break $\bA$ into two parts

$$
\bA = \left[\begin{array}{c|c} \bA_R & \ba_t \end{array}\right]
$$
where $\bA_R \in \RR^{4 \times 3}$ is the rotational
component and $\ba_t \in \RR^4$ is related to translation. 
We can now write:

$$
\MM = \left [ 
\begin{array}{c|c}
\widehat{\MM} \bA_R & \widehat{\MM} \ba_t 
\end{array}
\right]
$$

**Rotational constraints**

Recall that $\bR_f$ is a rotation matrix hence its rows are 
unit norm and orthogonal to each other.
Thus every row of $\widehat{\MM} \bA_R$
is unit norm and every pair of rows (for
a given frame) is orthogonal. This yields 
following constraints.

$$
& \widehat{\bm}_{2f-1} \bA_R \bA_R^T 
\widehat{\bm}_{2f-1}^T = 1\\
&\widehat{\bm}_{2f} \bA_R \bA_R^T 
\widehat{\bm}_{2f}^T = 1\\
&\widehat{\bm}_{2f-1} \bA_R \bA_R^T 
\widehat{\bm}_{2f}^T = \bzero
$$
where $\widehat{\bm}_k$ are rows of
matrix $\widehat{\MM}$ for
$1 \leq f \leq F$. 
This over-constrained system can be solved for
the entries of $\bA_R$ using least squares techniques.

**Translational constraints**

Recall that the image of a centroid of a set of points
under an isometry (rigid motion) is the centroid 
of the images of the points under the same isometry.
The homogeneous coordinates of the centroid in the
object coordinate system are $(0, 0, 0, 1)$.
The coordinates of the centroid in image are

$$
(\frac{1}{S} \sum_s {u_{f s}}, \frac{1}{S} \sum_s {v_{f s}} ).
$$
Putting back, we obtain

$$
\frac{1}{S}
\begin{bmatrix}
\sum_s {u_{1 s}}\\
\sum_s {v_{1 s}}\\
\vdots\\
\sum_s {u_{F s}}\\
\sum_s {v_{F s}}\\
\end{bmatrix}
= \left [ 
\begin{array}{c|c}
\widehat{\MM} \bA_R & \widehat{\MM} \ba_t 
\end{array}
\right] 
\begin{bmatrix}
0 \\ 0 \\ 0 \\1
\end{bmatrix} = \widehat{\MM} \ba_t .
$$
A least squares solution for $\ba_t$ is straight-forward.
````
 
## Modeling Motion for Multiple Objects

````{div}

The generalization of modeling of motion of one object
to multiple objects is straight-forward. Let there be
$K$ objects in the scene moving independently [^n2]. 
Let $S_1, S_2, \dots, S_K$ feature points be tracked
for objects $1,2, \dots, K$ respectively  for $F$ frames
with
$S = \sum_k S_k$. Let these feature trajectories be
put in a data matrix $\bY \in \RR^{2F \times S}$.
In general, we don't know which feature point belongs
to which object and how many feature points are there
for each object. There is at least one
feature point for each object (otherwise the object
isn't being tracked at all). We could permute the
columns of $\bY$ via an (unknown) permutation $\Gamma$
so that the feature points of each object are placed
contiguously giving us 

$$
\bY^* =  \bY \Gamma = \begin{bmatrix}
\bY_1 & \bY_2 & \dots & \bY_K
\end{bmatrix}.
$$
Clearly, each submatrix $\bY_k$ ($1 \leq k \leq K$) 
which consists of feature trajectories of one object
spans an (up to) 4 dimensional subspace. 
Now, the problem
of *motion segmentation* is essentially separating
$\bY$ into $\bY_k$ which reduces to a standard
subspace clustering problem.

Let us dig a bit deeper to see how the motion shape
factorization identity changes for the multi-object
formulation. Each data submatrix $\bY_k$ can be factorized
as

$$
\bY_k = \bU_k \Sigma_k \bV_k^T = \MM_k  \SS_k
= \widehat{\MM}_k \bA_k \bA_k^{-1} \widehat{\SS}_k.
$$

$\bY^*$ now has the canonical factorization:

$$
\bY^* = 
\begin{bmatrix}
\MM_1 & \dots & \MM_K
\end{bmatrix}
\begin{bmatrix}
\SS_1 & \dots & 0 \\
\vdots & \ddots & \vdots\\
0 & \dots & \SS_K
\end{bmatrix}.
$$
If we further denote :

$$
\MM = \begin{bmatrix}
\MM_1 & \dots & \MM_K
\end{bmatrix}\\
\widehat{\MM} = \begin{bmatrix}
\widehat{\MM}_1 & \dots & \widehat{\MM}_K
\end{bmatrix}\\
\SS = \begin{bmatrix}
\SS_1 & \dots & 0 \\
\vdots & \ddots & \vdots\\
0 & \dots & \SS_K
\end{bmatrix}\\
\widehat{\SS} = \begin{bmatrix}
\widehat{\SS}_1 & \dots & 0 \\
\vdots & \ddots & \vdots\\
0 & \dots & \widehat{\SS}_K
\end{bmatrix}\\
A = \begin{bmatrix}
A_1 & \dots & 0 \\
\vdots & \ddots & \vdots\\
0 & \dots & A_K
\end{bmatrix}\\
U = \begin{bmatrix}
U_1 & \dots & U_K
\end{bmatrix}\\
\Sigma = \begin{bmatrix}
\Sigma_1 & \dots & 0 \\
\vdots & \ddots & \vdots\\
0 & \dots & \Sigma_K
\end{bmatrix}\\
V = \begin{bmatrix}
V_1 & \dots & 0 \\
\vdots & \ddots & \vdots\\
0 & \dots & V_K
\end{bmatrix},
$$
then we obtain a factorization similar to the single
object case given by

$$
Y^* = \MM \SS 
=  \widehat{\MM} A A^{-1}\widehat{\SS}\\
\SS  = A^{-1}\widehat{\SS} 
= A^{-1} \Sigma^{\frac{1}{2}} V^T\\
\MM = \widehat{\MM} A = U \Sigma^{\frac{1}{2}} A.
$$
Thus, when the segmentation of $Y$ in terms of the unknown
permutation $\Gamma$ has been obtained, (sorted) data matrix 
$Y^*$ can be factorized into shape and motion components
as appropriate.
````

## Limitations

Our discussion so far has established that 
feature trajectories for each moving object span a 4-dimensional
space. There are a number of reasons why this is only *approximately*
valid: perspective distortion of camera, tracking errors, and
pixel quantization. Thus, a subspace clustering algorithm
should allow for the presence of noise or corruption of data
in real life applications. 


[^n2]: Our realization of an object is a set of
feature points undergoing same rotation and translation
over a sequence of images. The notion of locality, color, 
connectivity etc. plays no role in this definition.
It is possible that two 
visually distinct objects are undergoing same rotation
and translation within a given image sequence. For the
purposes of inferring an object from its motion, these
two visually distinct object are treated as one.