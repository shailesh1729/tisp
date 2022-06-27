# Matrices III

## Orthogonal Matrices
````{prf:definition}
:label: def:mat:orthogonal_matrix

A real square matrix $\bU$ is called *orthogonal*
if the columns of $\bU$ form an orthonormal set.
In other words, let

$$
\bU = \begin{bmatrix}
\bu_1 & \bu_2 & \dots & \bu_n
\end{bmatrix}
$$
with $\bu_i \in \RR^n$. Then we have

$$
\bu_i \cdot \bu_j = \delta_{i , j}.
$$ 
````

````{prf:lemma}
:label: lem:mat:orthogonal_transpose_inverse

An orthogonal matrix $\bU$ is invertible with $\bU^T = \bU^{-1}$.
````
````{prf:proof}
Let

$$
\bU = \begin{bmatrix}
\bu_1 & \bu_2 & \dots & \bu_n
\end{bmatrix}
$$
be orthogonal with 

$$
\bU^T = \begin{bmatrix}
\bu_1^T \\ \bu_2^T \\ \vdots \\ \bu_n^T
\end{bmatrix}.
$$
Then

$$
\bU^T \bU = \begin{bmatrix}
\bu_1^T \\ \bu_2^T \\ \vdots \\ \bu_n^T
\end{bmatrix}
\begin{bmatrix}
\bu_1 & \bu_2 & \dots & \bu_n
\end{bmatrix} 
= \begin{bmatrix} \bu_i \cdot \bu_j \end{bmatrix} = \bI. 
$$
Since columns of $\bU$ are linearly independent and span $\RR^n$, hence $\bU$ is invertible.
Thus

$$
\bU^T = \bU^{-1}.
$$
````
````{prf:lemma} Determinant of an orthogonal matrix
:label: lem:determinant_orthogonal_matrix

Determinant of an orthogonal matrix is $\pm 1$. 
````
````{prf:proof}
Let $\bU$ be an orthogonal matrix. Then

$$
\det (\bU^T \bU) = \det (\bI) \implies \left ( \det (\bU) \right )^2  = 1.
$$
Thus we have

$$
\det(\bU) = \pm 1.
$$
````
## Unitary Matrices
````{prf:definition} Unitary matrix
:label: def:mat:unitary_matrix

A complex square matrix $\bU$ is called *unitary*
if the columns of $\bU$ form an orthonormal set.
In other words, let

$$
\bU = \begin{bmatrix}
\bu_1 & \bu_2 & \dots & \bu_n
\end{bmatrix}
$$
with $u_i \in \CC^n$. Then we have

$$
\bu_i \cdot \bu_j = \langle \bu_i , \bu_j \rangle = \bu_j^H \bu_i = \delta_{i , j}.
$$ 
````

````{prf:lemma}
:label: lem:mat:unitary_conjugate_transpose_inverse

A unitary matrix $\bU$ is invertible with $\bU^H = \bU^{-1}$.
````
````{prf:proof}
Let

$$
\bU = \begin{bmatrix}
\bu_1 & \bu_2 & \dots & \bu_n
\end{bmatrix}
$$
be unitary with 

$$
\bU^H = \begin{bmatrix}
\bu_1^H \\ \bu_2^H \\ \vdots \\ \bu_n^H
\end{bmatrix}.
$$
Then

$$
\bU^H \bU = \begin{bmatrix}
\bu_1^H \\ \bu_2^H \\ \vdots \\ \bu_n^H
\end{bmatrix}
\begin{bmatrix}
\bu_1 & \bu_2 & \dots & \bu_n
\end{bmatrix} 
= \begin{bmatrix} \bu_i^H \bu_j \end{bmatrix} = \bI. 
$$
Since columns of $\bU$ are linearly independent and span $\CC^n$,
hence $\bU$ is invertible.
Thus

$$
\bU^H = \bU^{-1}.
$$
````

````{prf:lemma} Determinant of unitary matrices
:label: lem:determinant_unitary_matrix

The magnitude of determinant of a unitary matrix is $1$. 
````
````{prf:proof}
Let $\bU$ be a unitary matrix. Then

$$
\det (\bU^H \bU) = \det (\bI) 
\implies \det(\bU^H) \det(\bU)  = 1 
\implies \overline{\det(\bU)}{\det(\bU)} = 1.
$$
Thus we have

$$
 |\det(\bU) |^2 = 1 \implies  |\det(\bU) |  = 1.
$$
````



## F Unitary Matrices

We provide a common definition for unitary matrices over any field $\FF$.
This definition applies to both real and complex matrices.

````{prf:definition}
:label: def:mat:f_unitary_matrix

A square matrix $\bU \in \FF^{n \times n}$ is called *$\FF$ unitary*
if the columns of $\bU$ form an orthonormal set.
In other words, let

$$
\bU = \begin{bmatrix}
\bu_1 & \bu_2 & \dots & \bu_n
\end{bmatrix}
$$

with $\bu_i \in \FF^n$. Then we have

$$
\langle \bu_i , \bu_j \rangle = \bu_j^H \bu_i = \delta_{i , j}.
$$ 
````
We note that a suitable definition of inner product transports the definition appropriately
into orthogonal matrices over $\RR$ and unitary matrices over $\CC$.

When we are talking about $\FF$ unitary matrices, then we will use the symbol $\bU^H$ to mean
its inverse. In the complex case, it will map to its conjugate transpose, while in real case
it will map to simple transpose. 

This definition helps us simplify some of the discussions in the sequel (like singular value
decomposition).

Following results apply equally to orthogonal matrices for real case and unitary matrices
for complex case.

````{prf:lemma} Norm preservation
:label: lem:mat:unitary_norm_preservation

$\FF$-unitary matrices preserve norm. i.e.

$$
\| \bU \bx \|_2 = \| \bx \|_2.
$$
````

````{prf:proof}
We have

$$
\| \bU \bx \|_2^2 = (\bU \bx)^H (\bU \bx)  = \bx^H \bU^H \bU \bx 
= \bx^H \bI \bx = \| \bx \|_2^2.
$$
````


````{prf:remark}
:label: res-mat-orthogonal-norm-preservation

For the real case we have

$$
\| \bU \bx \|_2^2 = (\bU \bx)^T (\bU \bx)  
= \bx^T \bU^T \bU \bx = \bx^T \bI \bx = \| \bx\|_2^2.
$$
````

````{prf:lemma} Preservation of inner products
:label: lem:mat:unitary_inner_product_preservation

$\FF$-unitary matrices preserve inner product. i.e.

$$
\langle \bU \bx, \bU \by \rangle = \langle \bx, \by \rangle.
$$
````

````{prf:proof}
We have

$$
\langle \bU \bx, \bU \by \rangle = (\bU \by)^H \bU \bx 
= \by^H \bU^H \bU \bx = \by^H \bx.
$$
````

````{prf:remark}
:label: lem:mat:orthogonal_inner_product_preservation

For the real case we have

$$
\langle \bU \bx, \bU \by \rangle = (\bU \by)^T \bU \bx = \by^T \bU^T \bU \bx = \by^T \bx.
$$
````
