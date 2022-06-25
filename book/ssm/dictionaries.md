(sec:ssm:dictionaries)=
# Dictionaries

In this section we review various properties associated with a dictionary $\bDDD$ which are
useful in understanding the behavior and capabilities of a dictionary.

```{div}
We recall that a dictionary $\bDDD$ consists of a finite number of unit norm vectors in $\CC^N$ called
atoms  which span the signal space $\CC^N$.
Atoms of the dictionary are indexed by an index set $\Omega$; i.e.,

$$
\bDDD = \{ \bd_{\omega} : \omega \in \Omega \}
$$
with $|\Omega| = D$ and $N \leq D$
with $\| d_{\omega} \|_2 = 1$ for every atom.

The vectors $\bx \in \CC^N$ can be represented by a synthesis matrix consisting of
the atoms of $\bDDD$ by a vector $\ba \in \CC^D$ as

$$
\bx = \bDDD \ba.
$$
Note that we are using the same symbol $\bDDD$ to represent the dictionary
as a set of atoms as well as the corresponding synthesis matrix.
We can write the matrix $\bDDD$ consisting of its columns as

$$
\bDDD = 
\begin{bmatrix}
\bd_1 & \dots & \bd_D
\end{bmatrix}
$$
This shouldn't be causing any confusion.
When we write the subscript as $\bd_{\omega}$
where $\omega \in \Omega$
we are referring to the atoms of the dictionary $\bDDD$
indexed by the set $\Omega$, while
when we write the subscript as $\bd_i$
we are referring to a column of corresponding synthesis matrix.
In this case, $\Omega$ will simply mean
the index set $\{ 1, \dots, D \}$.
Obviously $|\Omega| = D$ holds still. 

Often, we will be working with a subset of atoms in a dictionary.
Usually such a subset
of atoms will be indexed by an index set $\Lambda \subseteq \Omega$. $\Lambda$ will take the form of
$\Lambda \subseteq \{\omega_1, \dots, \omega_D\}$ or
$\Lambda \subseteq \{1, \dots, D\}$ depending upon
whether we are talking about
the subset of atoms in the dictionary
or a subset of columns from the corresponding
synthesis matrix.

Often we will need the notion of a sub-dictionary {cite}`tropp2006just` described below.
```

```{index} Subdictionary
```
````{prf:definition} Subdictionary
:label: def:ssm:subdictionary

A subdictionary is a linearly independent collection of atoms. 
Let $\Lambda \subset \{\omega_1, \dots, \omega_D\}$
be the index set for the
atoms in the subdictionary.
We denote the subdictionary as $\bDDD_{\Lambda}$.
We also use $\bDDD_{\Lambda}$
to denote the corresponding matrix with
$\Lambda \subset \{1, \dots, D\}$.
````

````{prf:remark} Rank of subdictionary
:label: res-ssm-subdictionary-rank

A subdictionary is full rank.
````
This is obvious since it is a collection of linearly independent atoms.

For subdictionaries, often we will say
$K = | \Lambda |$ and 
$\bG = \bDDD_{\Lambda}^H \bDDD_{\Lambda}$ as its
Gram matrix.
Sometimes, we will also be considering $\bG^{-1}$.
$\bG^{-1}$ has a useful interpretation
in terms of the *dual vectors* for the atoms in
$\bDDD_{\Lambda}$ {cite}`tropp2004just`.

```{div}
Let $\{ \bd_{\lambda} \}_{\lambda \in \Lambda}$
denote the atoms in $\bDDD_{\Lambda}$. 
Let $\{ \bc_{\lambda} \}_{\lambda \in \Lambda}$
be chosen such that

$$
\langle \bd_{\lambda} , \bc_{\lambda} \rangle = 1
$$
and

$$
\langle \bd_{\lambda} , \bc_{\omega} \rangle = 0
\text { for } \lambda, \omega \in \Lambda, \lambda \neq \omega.
$$
Each dual vector $\bc_{\lambda}$ is orthogonal to atoms in the subdictionary at different indices
and is long enough so that
its inner product with $\bd_{\lambda}$ is one.
The dual system somehow
inverts the sub-dictionary.
In fact the dual vectors are nothing but the columns of the 
matrix $\bB = (\bDDD_{\Lambda}^{\dag})^H$.
Now, a simple calculation shows that:

$$
\bB^H \bB 
= (\bDDD_{\Lambda}^{\dag}) (\bDDD_{\Lambda}^{\dag})^H 
= (\bDDD_{\Lambda}^H \bDDD_{\Lambda})^{-1} \bDDD_{\Lambda}^H \bDDD_{\Lambda} (\bDDD_{\Lambda}^H \bDDD_{\Lambda})^{-1} 
= (\bDDD_{\Lambda}^H \bDDD_{\Lambda})^{-1} = \bG^{-1}.
$$
Therefore, the inverse Gram matrix lists the inner products
between the dual vectors. 

Sometimes we will be discussing tools
which apply for general matrices. We will use
the symbol $\Phi$ for representing general matrices.
Whenever the dictionary is 
an orthonormal basis, we will use the symbol $\Psi$.
