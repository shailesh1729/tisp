(sec:algebraic_geometry)=
# Algebraic Geometry

This section covers essential notions and facts from algebraic geometry
needed for these notes.
For a systematic introduction to the subject, see
{cite}`hartshorne1977algebraic,harris2013algebraic, griffiths2014principles`.
Algebraic geometry is the study of geometries that come from algebra.
The geometrical objects being studied are
the solution sets of systems of multivariate polynomial equations. 
A data set being studied can be thought of as a collection of
sample points from a geometrical object (e.g. a union of subspaces).
The objective is to infer the said
geometrical object from the given data set and decompose
the object into simpler objects which help in better
understanding of the data set.

(sec:polynomial_rings)=
## Polynomial Rings

````{div}
1. Let $\FF^m$ be $m$-dimensional vector space where $\FF$ 
  is either $\RR$ or $\CC$ (a field of characteristic 0). 
1. For $\bx = [x_1, \dots, x_m]^T \in \FF^m$,
   let $\FF[\bx] = [x_1, \dots, x_m]$
   be the set of all polynomials of $m$ variables $x_1, \dots,x_m$.
1. $\FF[\bx]$ is a commutative ring {cite}`artin2017algebra`. 
1. A monomial is a product of variables.
   Its degree is the number of variables in the product. 
1. A monomial of degree $n$ is of the form 
   $x^n = x_1^{n_1}\dots x_m^{n_m}$ with $0 \leq n_j \leq n$
   and $n_1 + \dots + n_m = n$.
1. There are a total of
   $A_n(m) = \binom{m + n -1}{n} = \binom{m + n -1}{m - 1}$
   different degree-$n$ monomials.
1. We now construct an embedding of vectors in $\FF^m$
   to $\FF^{A_n(m)}$.
1. The Veronese map of degree $n$, denoted as
   $v_n : \FF^m \to \FF^{A_n(m)}$, is defined as

    $$
    v_n : [x_1, \dots, x_m]^T \to [\dots, x^n, \dots]^T
    $$
    where $x^n$ are degree-n monomials chosen in
    the degree lexicographic order.
1. For example, the Veronese map of degree 2 from
   $\RR^3$ to $\RR^6$ is defined as 

    $$
    v_2(\bx) 
    = v_2([x_1, x_2, x_3]^T) 
    = [x_1^2, x_1x_2, x_1x_3,x_2^2, x_2x_3, x_3^2 ]^T.
    $$
1. A *term* is a scalar multiplying a monomial.
1. A polynomial $p(\bx)$ is said to be *homogeneous*
   if all its terms have the same degree.
1. Homogeneous polynomials are also known as *forms*.
1. A *linear form* is a homogeneous polynomial of degree 1. 
1. A *quadratic form* is a homogeneous polynomial of degree 2.
1. A degree-n form $p(\bx)$ can be written as 
    
    $$
    p(\bx) = c_n^T v_n(\bx) 
    = \sum c_{n_1, \dots, n_m}x_1^{n_1}\dots x_m^{n_m},
    $$
    where $c_{n_1, \dots, n_m} \in \FF$
    are the coefficients associated 
    with the monomials $x_1^{n_1}\dots x_m^{n_m}$. 
1. A *projective space* corresponding to a vector space $\VV$
   is the set of lines passing through its origin
   (the one dimensional subspaces).
1. Each such line can be represented by any non-zero point on the line.
1. For a degree-n form $p(\bx)$ and a scalar $b \in \FF$,
   we have:

    $$
    p(b x_1, \dots, b x_m ) = b^n p (x_1, \dots, x_m).
    $$
1. Therefore, if $p(\bx) = 0$, then
   $p(\alpha \bx) = 0 \Forall \alpha \in \FF$
   and the zero-set of $p(\bx)$ includes the one dimensional subspace 
   containing $\bx$
   (the line passing through $\bx$ and $0$).
1. Our interest is in the zero sets of homogeneous polynomials.
1. Thus, it is useful to view $\FF^n$ as a projective space.
1. For a form $p(\bx)$, $p(\bzero)$ is always 0.
1. If $p(\ba) = 0$ for some $\ba \neq \bzero$,
   then $p(\bx) = 0 \Forall \bx = b \ba, b \in \FF$.
1. The ring $\FF[\bx]$ can be viewed as a
   *graded ring* {cite}`lang2002algebra` and decomposed as

    ```{math}
    :label: eq:graded_ring

    \FF[\bx] 
    = \bigoplus_{i=0}^{\infty} \FF_0 
    \oplus \FF_1 \oplus \dots \FF_p \oplus \dots,
    ```
    where $\FF_i$ consists of all homogeneous polynomials of degree $i$.
1. $\FF_0 = \FF$ is the set of scalars (polynomials of degree 0).
1. $\FF_1$ is the set of all 1-forms:
    
    $$
    \FF_1 = \{b_1 x_1 + \dots + b_m x_m \ST [b_1, \dots b_m]^T \in \FF^m \}.
    $$
1. Note that the polynomial $0 = \bzero^T \bx$ is included in every $\FF_i$. 
1. This enables us to treat $\FF_i$ as a vector space of $i$-forms.
1. $\FF_1$ can also be viewed as the dual-space of linear functionals
   for the vector space $\FF^m$.
1. We will also need following sets later:

    $$
    &\FF_{\leq p} 
    = \bigoplus_{i=0}^p \FF_i 
    = \FF_0 \oplus \dots \oplus \FF_p.\\
    &\FF_{\geq p} 
    = \bigoplus_{i=p}^{\infty}\FF_i 
    = \FF_p \oplus \FF_{p+1}\oplus \dots.
    $$
1. An *ideal* in the ring $\FF[\bx]$ is an additive subgroup
   $I$ such that if $p(\bx) \in I$ and $q(\bx) \in \FF[\bx]$,
   then $p(\bx) q(\bx) \in I$.
1. $\FF[\bx]$ is a trivial ideal. 
1. $I$ is called a proper ideal if $I \neq \FF[\bx]$.
1. A proper ideal $I$ is called *maximal* if no other proper ideal
   of $\FF[\bx]$ contains $I$.
1. An ideal $I$ is called a *subideal* of an ideal $J$ if $I \subset J$.
1. If $I$ and $J$ are two ideals in $\FF[\bx]$,
   then $I \cap J$ is also an ideal.
1. An ideal $I$ is said to be *generated* by a subset $\GGG \subset I$, 
   if every  $p(\bx) \in I$ can be written as 
   
   $$
    p(\bx) 
    = \sum_{i=1}^k q_i(\bx) g_i (\bx), q_i(\bx) \in \FF[\bx],\, 
    g_i(\bx) \in \GGG.
   $$
1. It is denoted by $(\GGG)$.
1. If $\GGG$ is finite, $(\GGG = \{ g_1, \dots, g_k\})$,
   then the generated ideal is also denoted by $(g_1, \dots, g_k)$.
1. An ideal generated by a single element $p(\bx)$ is called a 
   *principal ideal* denoted by $(p(\bx))$.
    
    $$
    (p(\bx)) = \{f(\bx) p(\bx) \Forall f(\bx) \in \FF[\bx] \}.
    $$
1. Given two ideals $I$ and $J$, the ideal that is generated
   by product of elements in $I$ and $J$:
   $\{ f(\bx)g(\bx) : f(\bx) \in I, g(\bx) \in J \}$
   is called the *product ideal* $IJ$. 
1. A prime ideal is similar to prime numbers in the
   ring of integers.
1. A proper ideal $I$ is called *prime* if $p(\bx) q(\bx) \in I$
   implies that $p(\bx) \in I$ or $q(\bx) \in I$.
1. A polynomial $p(\bx)$ is said to be *prime* or *irreducible*
   if it generates a prime ideal.
1. A *homogeneous ideal* of $\FF[\bx]$ is an ideal 
   generated by homogeneous polynomials. 
````

(sec:algebraic_sets)=
## Algebraic Sets

````{div}
1. Given a set of homogeneous polynomials $J \subset \FF[\bx]$,
   a corresponding *projective algebraic set* 
   $Z(J) \subset \FF^m$ is defined as 

    $$
    Z(J) = \{y \in \FF^m | p(y) = 0, \Forall p(\bx) \in J \}.
    $$
1. In other words, $Z(J)$ is the zero set of polynomials
   in $J$ (intersection of zero sets of each polynomial in $J$).
1. Let $I$ and $K$ be sets of homogeneous polynomials and 
   $X = Z(I)$ and $Y = Z(K)$ such that $Y \subset X$.
1. Then $Y$ is called an *algebraic subset* of $X$.
1. A nonempty algebraic set is called *irreducible*
   if it is not the union of two nonempty smaller algebraic
   sets.
1. An *irreducible algebraic set* is also known as *algebraic variety*.
1. Any subspace of $\FF^m$ is an *algebraic variety*.
1. Given any subset $X \in \FF^m$, we define the 
   *vanishing ideal* of $X$ as the set of
   all polynomials that vanish on $X$.
    
    $$
    I(X) = \{ f(\bx) \in \FF[\bx] | f(y) = 0, \Forall y \in X \}.
    $$
1. It is easy to see that if $f(\bx) \in I(X)$,
   then $f(\bx) g(\bx) \in I(X)$ for all 
   $g(\bx) \in \FF[\bx]$.
1. Thus, $I(X)$ is indeed an ideal.
````
---

````{div}
1. Let $J \subset \FF[\bx]$ be a set of homogeneous polynomials. 
1. $Z(J)$ is the zero set of $J$ (an algebraic set). 
1. $I(Z(J))$ is the vanishing ideal of the zero set of $J$. 
1. It can be shown that $I(Z(J))$ is an ideal that contains $J$.
1. Similarly, let $X \subset \FF^m$ be an arbitrary set of vectors
   in $\FF^m$.
1. $I(X)$ is the vanishing ideal of $X$ and $Z(I(X))$ is the zero set
   of the vanishing ideal of $X$.
1. Then, $Z(I(X))$ is an algebraic set that contains $X$. 
````
---

It turns out that irreducible algebraic sets and 
prime ideals are connected. In fact, If $X$ is an algebraic
set and $I(X)$ is the vanishing ideal of $X$, then $X$
is irreducible if and only if $I(X)$ is a prime ideal.

The natural progression is to look for a one-to-one 
correspondence between ideals and algebraic sets.
The concept of a radical ideal is useful in this context.

````{div}
1. Given a (homogeneous) ideal $I$ of $\FF[\bx]$,
   the  *(homogeneous) radical ideal * of $I$ is defined to be

    $$
    \text{rad}(I) 
    = \{ f(\bx) \in \FF[\bx] \ST 
        f(\bx)^p \in I \,\text{for some } p \in \Nat\}.
    $$
1. $\text{rad}(I)$ is an ideal in itself and 
   $I \subset \text{rad}(I)$.
1. $\text{rad}(I)$ is a fixed-point in the sense that 
   $\text{rad}(\text{rad}(I)) = \text{rad}(I)$.
1. Also, if $I$ is homogeneous,
   then so is $\text{rad}(I)$.
1  A theorem by Hilbert suggests the following:
   If $\FF$ is an algebraically closed field (e.g. $\FF = \CC$)
   and $I \subset \FF[\bx]$ is an (homogeneous) ideal, then

    $$
    I(Z(I)) = \text{rad}(I).
    $$
1. Thus, the mappings $I \to Z(I)$ and $X \to I(X)$
   induce a one-to-one correspondence between the collection of
   (projective) algebraic sets of $\FF^m$ and 
   (homogeneous) radical ideals of $\FF[\bx]$.
1. This result is known as *Nullstellensatz*.
````

(sec:algebraic_sampling_theory)=
## Algebraic Sampling Theory

We will now explore the problem of identifying
a (projective) algebraic set $Z \in \FF^m$ from a
finite number of sample points in $Z$. 

````{div}
1. In general, the algebraic set $Z$ may not be irreducible
   and the ideal $I(Z)$ may not be prime.
1. Let  $\{z_1, \dots, z_S\} \subset Z$ be the finite
   (but  sufficiently large) set of sample points from $Z$
   for the following discussion. 
1. For an arbitrary point $z \in Z$, we abuse $z$ to 
   mean the corresponding projective point (i.e. the
   line passing between 0 and $z$). 
1. Let $\mathfrak{m} = I(z)$ be the vanishing ideal of (the line) $z$.
1. Then, $\mathfrak{m}$ is a *submaximal* ideal
  (i.e. it cannot be a subideal of any other homogeneous ideal
  of $\FF[\bx]$). Let 
1. $\mathfrak{m}_i$ be the vanishing ideal of $z_i$. Then the vanishing
   ideal for the set of points is 

    $$
    \mathfrak{a}_S = \mathfrak{m}_1 \cap \dots \cap \mathfrak{m}_S.
    $$
1. This is a radical ideal and is in general much larger than
   $I(Z)$.
1. In order to ensure that we can infer $I(Z)$
   correctly from the set of samples $\{ z_i \}$,
   we need some additional constraints.
1. We require that $I(Z)$ is generated by a set of (homogeneous)
   polynomials whose degrees are bound by a relatively small $n$.
    
    $$
    I(Z) = (f_1, \dots, f_s) \text{ s.t. }\, \deg(f_j) \leq n.
    $$
1. Then, the zero set of $I$ is given by
    
    $$
    Z(I) = \{ z  \in \FF^m | f_i(z) = 0, i = 1, 2, \dots, s\}.
    $$
1. In general, $I(Z)$ is always a proper subideal of $I_S$
    regardless of how large $S$ is.
1. We introduce an algebraic sampling theorem which
   comes to our rescue.
1. It suggests that if $I(Z)$ is generated by polynomials
   in $\FF_{\leq n}$, then there is a finite sequence of
   points $Z_S = \{z_1, \dots, z_S \}$ such that the subspace 
   $I(Z_S) \cap \FF_{\leq n}$ generates $I(Z)$.
1. While the theorem doesn't suggest a bound on $S$,
   it turns out that with probability one,
   the vanishing ideal of an algebraic set can be correctly
   determined from a randomly chosen sequence of samples.
1. This theorem is analogous to the classical Nyquist-Shannon
   sampling theorem.
````
So far we have looked at modeling a data set as an algebraic
set and obtaining its vanishing ideal.
The next step is to extract the internal geometric
or algebraic structure of the algebraic set.
The idea is to find simpler (possibly irreducible)
algebraic sets which can be composed to form the given algebraic
set. For example, if an algebraic set is a union of subspaces,
then we would like to find out the component subspaces. In other
words, given an algebraic set $X$ or its vanishing ideal $I(X)$,
the objective is to decompose it into a union of subsets each of
which cannot be decomposed further. 

````{div}
1. An algebraic set can have only finitely many irreducible components.
1. In other words, there exists a finite $n$ such that
    
    $$
    X = X_1 \cup \dots \cup X_n,
    $$
    where $X_i$ are irreducible algebraic varieties.
1. The vanishing ideal $I(X_i)$ must be a prime ideal
   that is minimal over the radical
   ideal $I(X)$ (i.e. there is no prime subideal of $I(X_i)$)
   that includes $I(X)$.
1. The ideal $I(X)$ is given by
    
    $$
    I(X) = I(X_1) \cap \dots \cap I(X_n).
    $$
1. This is known as the *minimal primary decomposition*
   of the radical ideal $I(X)$.
1. Given a (projective) algebraic set $X$ and its vanishing ideal $I(Z)$,
   we can grade the ideal by degree as:

    $$
    I(Z) = I_0(Z) \oplus I_1(Z) \oplus \dots. 
    $$
1. The *Hilbert function* of $Z$ is defined to be 

    ```{math}
    :label: eq:hilbert_function
    h_I(i) \triangleq \text{dim} (I_i(Z)).
    ```
1. $h_I(i)$ denotes the number of linearly independent polynomials of
   degree $i$ that vanish on $Z$.
1. *Hilbert series* of an ideal $I$ is defined as the power series:

    $$
    \HHH(I, t)\triangleq \sum_{i=0}^{\infty} h_I(i) t^i.
    $$
````


## Subspace Arrangements

We are interested in special class of algebraic sets known as
*subspace arrangements* in $\RR^M$.

````{div}
1. A subspace arrangement is a finite collection of linear or
   affine subspaces in $\RR^M$
   $\UUU = \{ \UUU_1, \dots, \UUU_K \}$.
1. The set $Z_{\UUU} = \UUU_1 \cup \dots \cup \UUU_K$
   is the *union of subspaces*.
1. It is an algebraic set. 
1. We will explore the algebraic properties of 
   $Z_{\UUU}$ in the following. 
1. We say a subspace arrangement is
   *central* if every subspace passes through origin.
1. In the sequel, we will focus on central subspace arrangements only.
1. A $D$-dimensional subspace $\VV$ can be defined by $D' = M - D$
   linearly independent linear forms $\{b_1, b_2, \dots, b_{D'} \}$:

    $$
    \VV = \{\bx \in \RR^M | b_i(\bx) = 0,  1 \leq i \leq D' \}.
    $$
1. Let $\VV^*$ denote the vector space of all linear forms
   that vanish on $\VV$.
1. Then $\dim(\VV^*) = D' = M - D$. 
1. $\VV$ is the zero set of $\VV^*$ (i.e. $\VV = Z(\VV^*))$.
1. The vanishing ideal of $\VV$ is

    $$
    I(\VV) = \{ p(\bx) \in \RR[\bx] : p(\bx) = 0, \Forall \bx \in \VV \}.
    $$
1. $I(\VV)$ is an ideal generated by linear forms in $\VV^*$.
1. It contains polynomials of all degrees that vanish on $\VV$.
1. Every polynomial $p(\bx) \in I(\VV)$ can be written as

    $$
    p(\bx) = h_1 b_1 + \dots  + h_{D'} b_{D'}
    $$
    where $h_i \in \RR[\bx]$.
1. $I(\VV)$ is a prime ideal. 
1. The vanishing ideal of the subspace 
   arrangement $Z_{\UUU} = \UUU_1 \cup \dots \cup \UUU_K$ is

    $$
    I(Z_{\UUU}) = I(\UUU_1) \cap \dots \cap I(\UUU_K).
    $$
1. The ideal can be graded by degree of the polynomial as:

    ```{math}
    :label: eq:graded_ring_subspace_arrangement
    I(Z_{\UUU}) = I_m(Z_{\UUU}) \oplus I_{m+1}(Z_{\UUU}) \oplus \dots.
    ```
1. Each $I_i(Z_{\UUU})$ is a vector space that contains forms of
   degree $i$ in $I(Z_{\UUU})$ and $m\geq 1$
   is the least degree of the polynomials in $I(Z_{\UUU})$.
1. The sequence of dimensions of $I_i(Z_{\UUU})$ is the Hilbert function
   $h_I(i)$ of $Z_{\UUU}$.
1. Based on a result on the regularity of subspace arrangements 
   {cite}`derksen2007hilbert`, the subspace arrangement $Z_{\UUU}$
   is uniquely determined as the zero set of all polynomials
   of degree up to $K$ in its vanishing ideal. i.e. 

    $$
    Z_{\UUU} = Z (I_0 \oplus I_1 \oplus \dots \oplus I_K).
    $$
1. Thus, we don't really need to determine polynomials of higher degree.
1. We need to characterize $I(Z_{\UUU})$ further. 
1. Recall that $\UUU_k$ is a (linear) subspace 
    and $\UUU_k^*$ is the vector space of linear forms
    which vanish on $\UUU_k$.
1. We can construct a *product of linear forms* by choosing
   one linear form from each $\UUU_k^*$.
1. Let $J(Z_{\UUU})$ be the ideal generated by the products
   of linear forms 

    $$
    \{ b_1 \cdot b_2 \cdot \dots \cdot b_K 
        \ST \quad b_k \in \UUU_k^* \Forall 1 \leq k \leq K \}
    $$
1. Equivalently, we can say that :

    $$
    J(Z_{\UUU}) \triangleq I(\UUU_1) I(\UUU_2)  \dots I(\UUU_K) 
    $$ 
    is the product ideal of the vanishing ideals of each of the subspaces.
1. Evidently, $J(Z_{\UUU})$ is a subideal in $I(Z_{\UUU})$.
1. In fact, the two ideals share the same zero set:

    $$
    Z_{\UUU} = Z(J(Z_{\UUU})) = Z(I(Z_{\UUU})).
    $$
1. Now, $I(Z_{\UUU})$ is the largest ideal which vanishes on
   $Z_{\UUU}$. 
1. In fact,  $I(Z_{\UUU})$ is the *radical ideal* of $J(Z_{\UUU})$. 
1. Now, just like we graded $I(Z_{\UUU})$, we can also grade
   $J(Z_{\UUU})$ as:

    $$
    J(Z_{\UUU}) = J_K(Z_{\UUU}) \oplus J_{K+1}(Z_{\UUU}) \oplus \dots.
    $$
1. Note that, the lowest degree of polynomials is always $K$ which is
   the number of subspaces in $\UUU$.
1. Hilbert function of $J$ is
   denoted as $h_J(i) = \text{dim} (J_i(Z_{\UUU}))$.
1. It turns out that Hilbert functions of the vanishing ideal $I$
   and the product ideal $J$ have interesting and useful relationships.
````

(sec:subspace_embedding)=
## Subspace Embeddings

````{div}
1. Let $Z_{\UUU'} = \UUU'_1 \cup \dots \cup \UUU'_{K'}$
   be another (central) subspace arrangement such that 
   $Z_{\UUU} \subseteq Z_{\UUU'}$.
1. Then it is necessary that for each $\UUU_k$,
   there exists $\UUU'_{k'}$ such that
   $\UUU_k \subseteq \UUU_{k'}$.
1. We call $(Z_{\UUU} \subseteq Z_{\UUU'})$,
   a *subspace embedding*. 
1. If $Z_{\UUU'}$ happens to be
   hyperplane arrangement, we call the embedding as a 
   *hyperplane embedding*.
1. Let us consider how to create a hyperplane embedding
   for a given subspace arrangement.
1. In general, the zero set of each homogeneous component
   of $I(Z_{\UUU})$ (i.e. $I_i(Z_{\UUU})$),
   need not be a subspace embedding of $Z_{\UUU}$.
1. In fact, it may not even be a subspace arrangement.
1. However, the derivatives of the polynomials in $I(Z_{\UUU})$
   come to our rescue. 
1. We denote the derivative of $p(\bx)$ w.r.t. $\bx \in \RR^M$ 
   by $ D p(\bx)$. 
1. Consider a polynomial $p(\bx) \in I(Z_{\UUU})$.
1. Pick a point $x_k$ from each subspace $\UUU_k$ ($x_k \in \UUU_k$).
1. Compute the derivative of $p(\bx)$ and evaluate it at $x_k$
   as $D p(x_k)$. 
1. Now, construct the hyperplane $H_k = \{ \bx : D p(x_k)^T \bx = 0 \}$.
1. Recall that the derivative of a smooth function $f(\bx)$
   is orthogonal to (the tangent space of) 
   its level set $f(\bx) = c$.
1. Thus, $H_k$ contains $\UUU_k$.
1. It turns out that if the $K$ points
   $\{ x_1, \dots, x_K \}$ (from each subspace) 
   are in general position, then the union of hyperplanes
   $\cup_{k=1}^K H_k$ is a hyperplane embedding of the subspace
   arrangement $Z(\UUU)$.
1. For each polynomial in $I(Z(\UUU))$, we can construct
   a hyperplane embedding of the subspace arrangement $Z(\UUU)$.
1. The intersection of hyperplane embeddings constructed from 
   a collection of polynomials in $I(Z(\UUU))$
   is a subspace embedding of $Z(\UUU)$.
1. When this collection of polynomials contains all the generators of
   $I(Z(\UUU))$, the subspace embedding becomes tight.
1. In fact, the resulting subspace arrangement coincides
   with the original one.
1. An ideal is said to be *pl-generated* if it is generated
   by *products of linear forms*.
1. The $J(Z_{\UUU})$ defined above is a *pl-generated* ideal.
1. If the ideal of a subspace arrangement $J(Z_{\UUU})$ is pl-generated,
   then the zero-set of every generator gives
   a hyperplane embedding  of $J(Z_{\UUU})$. 
1. If $J(Z_{\UUU})$ is a hyperplane arrangement, then 
   $I(J(Z_{\UUU}))$ is always pl-generated as it is
   generated by a single polynomial of the form 
   $p(\bx) = (b_1^T \bx) \dots (b_K^T \bx)$ where
   $b_k \in \RR^M$ are the normal vectors to the
   $K$ hyperplanes in the arrangement.
1. In fact, it is also a principal ideal.
1. The vanishing ideal of a single subspace
   is always pl-generated.
1. The vanishing ideal of an arrangement of two subspaces
   is also pl-generated but this is not true in general.
1. But something can be said if the $K$ subspaces in the
   arrangement are in general position.
````

## Hilbert Functions of Subspace Arrangements



If a subspace arrangement $\UUU$ is in general position,
then the values of the Hilbert function $h_I(i)$ of
its vanishing ideal $I(Z_{\UUU})$ depend solely on 
the dimensions of the subspaces $D_1, \dots, D_K$ and they
are invariant under a continuous change of the position of the
subspaces. When identifying a subspace arrangement from
a set of samples, the first level parameters to be identified
are number of subspaces and the dimensions of each subspace.
