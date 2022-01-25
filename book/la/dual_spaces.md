(sec:la:dual_spaces)=
# Dual Spaces


Recall from {prf:ref}`def-la-lt-vector-space`
that $\LinTSpace(\VV, \WW)$ denotes the
vector space of linear transformations 
from $\VV$ to $\WW$ where both
$\VV$ and $\WW$ are vector spaces.
In {prf:ref}`ex-field-is-vector-space`, we showed
that $\FF$ is a vector space in its own right.

In this section, we explore the vector space
of linear maps(transformations, functions, operators)
from a vector space $\VV$ to its field of scalars $\FF$;
i.e., $\WW = \FF$.


## Linear Functionals

```{prf:definition} Linear functional
:label: def-la-linear-functional

A *linear functional* on $\VV$ is a linear map 
$\bf : \VV \to \FF$ from a vector space $\VV$ to
its field of scalars $\FF$.
A linear functional is a member of the 
vector space $\LinTSpace(\VV, \FF)$. 
```
A linear functional is both *homogeneous* and *additive*.
If $\bf$ is a linear functional, then

$$
\bf(t \bx + \by)  = t \bf(\bx) + \bf(\by)
$$
holds true for all $\bx, \by \in \VV$.


Recall that two functions are considered equal
if they have identical domain and they produce
same output for every value in the domain.

```{prf:definition} Equality of linear functionals
:label: def-la-linear-functional-equality

Two linear functionals $\bf$ and $\bg$ in $\VV^*$ 
are considered equal if

$$
\bf(\bv) = \bg(\bv) \Forall \bv \in \VV
$$
```

```{prf:lemma} Equality of linear functionals on a basis
:label: res-la-linear-functional-equality-basis

Let $\VV$ be a finite dimensional vector space and
$\BBB = \{ \bv_1, \dots, \bv_n \}$ be a basis of $\VV$.

If two linear functionals agree on the basis vectors,
then they are equal.
```

```{prf:proof}
Let $\bf, \bg \in \VV^*$.
Any $\bv \in \VV$ can be written as:

$$
\bv = \sum_{i=1}^n c_i \bv_i.
$$
Due to linearity, 

$$
\bf (\bv) = \sum_{i=1}^n c_i \bf (\bv_i)
\text{ and }
\bg (\bv) = \sum_{i=1}^n c_i \bg (\bv_i).
$$

Thus, if $\bf (\bv_i) = \bg (\bv_i)$ for $i=1, \dots, n$, then
$\bf$ and $\bg$ equal on every $\bv \in \VV$.
```


## Dual Spaces

```{prf:definition} Dual space
:label: def-la-dual-space

The *dual space* of a vector space $\VV$,
denoted by $\VV^*$,
is the set of all of the linear functionals
on $\VV$. 

In other words: $\VV^* = \LinTSpace(\VV, \FF)$.
```

```{prf:observation}
:label: res-la-dual-space-is-vector-space

Since the space of linear transformations from $\VV$
to $\FF$ (as a vector space) is a vector space, hence
$\VV^*$ is a vector space.
The elements of the dual space are the linear functionals.
```

Every vector space has a zero vector. The
dual space must have one too.

```{prf:definition} Zero functional
:label: def-la-zero-functional

A zero functional $\bzero : \VV \to \FF$ is a 
linear functional which maps every vector $\bv \in \VV$
to $0 \in \FF$.

$$
\bzero (\bv ) = 0 \Forall \bv \in \VV.
$$
```

```{div}
It is easy to see that the zero functional is linear
and indeed a member of $\LinTSpace(\VV, \FF)$.

We will be using the same symbol $\bzero$ to denote both the
zero functional in $\VV^*$ and the zero vector in $\VV$. 
It should be clear from the context which one is being referred to.

If $\bf \neq \bzero$, then there exists at least one $\bx \in \VV$
such that $\bf (\bx) \neq 0$. 
```


When we have a vector space, it is natural to ask for
its dimension and provide a way to build a basis for 
the space.

## Basis for Dual Space

```{prf:theorem} Basis for dual space
:label: res-la-finite-dual-space-basis

Let $\VV$ be a finite dimensional vector space.
Let $\BBB = \{\bv_1, \dots, \bv_n\}$ be a basis
of $\VV$. 

For each $i=1,\dots,n$, define a linear functional
$\bf_i : \VV \to \FF$ by setting:

$$
\bf_i(\bv_j) = \begin{cases}
1 && \text{ if } && i = j\\
0 && \text{ if } && i \neq j
\end{cases}
$$
and then extending $\bf_i$ linearly to all of $\VV$,
meaning, for any $\bv = \sum_{j=1}^n \alpha_j \bv_j$,

$$
\bf_i (\bv) = \bf_i (\sum_{j=1}^n \alpha_j \bv_j) 
= \sum_{j=1}^n \alpha_j \bf_i(\bv_j) = \alpha_i.
$$

Then, $\FFF = \{ \bf_1, \dots, \bf_n \}$ form a basis for $\VV^*$.
The basis $\FFF$ is called the *dual basis* of $\BBB$.
```


```{prf:proof}
We first show that $\bf_1, \dots, \bf_n$ are 
linearly independent.

Let $c_1, \dots, c_n \in \FF$ such that:

$$
c_1 \bf_1 + \dots + c_n \bf_n  = \bzero.
$$
Note that the $\bzero$ in the R.H.S. denotes the zero functional.
This means that $c_1 \bf_1 + \dots + c_n \bf_n$ maps every 
vector to 0; i.e.,

$$
(c_1 \bf_1 + \dots + c_n \bf_n) (\bv) = 0 \Forall \bv \in \VV.
$$
This is valid in particular for the basis vectors in $\BBB$.
Thus, 

$$
(c_1 \bf_1 + \dots + c_n \bf_n) (\bv_j) = 0 \Forall 1 \leq j \leq n.
$$

But,

$$
(c_1 \bf_1 + \dots + c_n \bf_n) (\bv_j) = \sum_{i=1}^n c_i \bf_i (\bv_j) = c_j
$$
from the definition of $\bf_i$. Thus, $c_j = 0$ for $j=1,\dots, n$. 
Hence, there is only a trivial linear combination of $\bf_i$ which equals the
zero functional. Thus, $\FFF$ is a set of linearly independent vectors.

Next, we show that $\FFF$ spans $\VV^*$. Let $\bf \in \VV^*$. 
Let 

$$
b_i = \bf (\bv_i) \Forall i=1,\dots, n
$$
be the value of the linear functional $\bf$ on the basis vectors in $\BBB$.
We claim that:

$$
\bf = b_1 \bf_1 + \dots + b_n \bf_n = \sum_{i=1}^n b_i \bf_i.
$$
As shown in {prf:ref}`res-la-linear-functional-equality-basis`,
if both functionals agree on the basis vectors in $\BBB$, then
they are equal.
Now,

$$
(b_1 \bf_1 + \dots + b_n \bf_n) (\bv_i) = \sum_{j=1}^n b_j \bf_j (\bv_i) = b_i = \bf(\bv_i)
$$
from the definitions of $\bf_i$ and $b_i$.
Thus, the functionals $\bf$ and $b_1 \bf_1 + \dots + b_n \bf_n$ agree on the basis. 
Thus, they are equal as elements of $\VV^*$.
Since $\bf \in \VV^*$ was arbitrary, hence, $\FFF$ spans $\VV^*$.

Since functionals in $\FFF$ are linearly independent and they span $\VV^*$,
they form a basis of $\VV^*$. 
```

```{prf:corollary} Dimension of the dual space
:label: res-la-finite-dual-space-dimension

If $\VV$ is finite dimensional,
then its dual space $\VV^*$ is also finite dimensional and

$$
\dim \VV = \dim \VV^*.
$$
```


```{prf:theorem}
Let $\VV$ be finite dimensional.
Let $\bv \in \VV$ such that $\bf(\bv) = 0$ for every $\bf \in \VV^*$. 
Then $\bv = \bzero$.
```

```{prf:proof}
Let $\BBB  = \{ \bv_1, \dots, \bv_n\}$ be a basis of $\VV$.
Let $\FFF = \{ \bf_1, \dots, \bf_n\}$ be the dual basis of $\VV^*$
with $\bf_i(\bv_j) = \delta(i, j)$.

$\bv$ can be written as as the linear combination of the basis vectors: 

$$
\bv = a_1 \bv_1 + \dots + a_n \bv_n.
$$
By hypothesis $\bf_i(\bv) = 0$.
Thus,

$$
\bf_i(\bv) = \sum_{j=1}^n a_i \bf_i (\bv_j) = a_i = 0.
$$

Thus, $a_i = 0$ for all $i=1,\dots, n$. Thus, 

$$
\bv = \sum_{i=1}^n a_i \bv_i = \bzero.
$$
```

## Null Space of Linear Functionals

We shall describe the null space of a linear functional
and show that for finite dimensional vector spaces,
its codimension is 1.

```{prf:theorem} Null space/kernel of a linear functional
:label: res-la-linear-functional-kernel

If $\bf$ is a linear functional on $\VV$, then

$$
\bf^{-1}(0) = \{ \bx \in \VV \ST \bf (\bv) = 0 \}
$$
is a linear subspace of $\VV$.
```
```{prf:proof}
We know that $0$ is the zero vector of the vector space $\FF$.
Thus, $\bf^{-1}(0)$ is nothing but the null space of $\bf$
and hence it is a linear subspace of $\VV$.

Another proof from first principles:

1. Let $\bu, \bv \in \bf^{-1}(0)$. 
1. Then, $\bf (\alpha \bu + \bv) = \alpha \bf (\bu) + \bf (\bv) = 0$.
1. Thus, $\alpha \bu + \bv \in \bf^{-1}(0)$.
1. Hence, $\bf^{-1}(0)$ is a subspace.
```

```{prf:theorem} 
:label: res-la-linear-functional-kernel-rep

Let $\bf$ be a nonzero linear functional on $\VV$. 
Let $\ba \in \VV$ be such that $\bf(\ba)\neq 0$. 
Then, any point $\bp \in \VV$ can be written 
uniquely as:

$$
\bp = \lambda \ba + \bx
$$
where $\lambda \in \FF$ and $\bx \in \bf^{-1}(0)$.
```
In this representation, $\bf$ and $\ba$ are fixed
while $\lambda$ and $\bx$ are allowed to vary.

```{prf:proof}
Let $\bp \in \VV$ be arbitrary. We wish to
construct a representation:

$$
\bp = \lambda \ba + \bx
$$
such that $\bx \in \bf^{-1}(0)$ and $\lambda \in \FF$.

Applying $\bf$ on both sides, we get:

$$
\bf(\bp) = \lambda \bf(\ba) + \bf(\bx) = \lambda \bf(\ba) 
$$
since $\bx \in \bf^{-1}(0)$.

This gives us:

$$
\lambda = \frac{\bf(\bp)}{\bf(\ba)}
$$
since we know that $\bf(\ba)\neq 0$.

Putting this particular value of $\lambda$, we get:

$$
\bx = \bp  - \frac{\bf(\bp)}{\bf(\ba)} \ba.
$$
Thus, for every $\bp \in \VV$, we can find
$\lambda = \frac{\bf(\bp)}{\bf(\ba)}$ and
$\bx =  \bp  - \frac{\bf(\bp)}{\bf(\ba)} \ba$ 
such that $\bf(\bx) = 0$  and:

$$
\bp = \lambda \ba + \bx.
$$

We have established existence of this representation.
Next, we establish that this representation is unique.

Suppose their was another representation:

$$
\bp = \mu \ba + \by
$$
with $\bf(\by) = 0$ and $\mu \in \FF$.

Then, we would have:

$$
\bf(\mu \ba + \by) = \mu \bf(\ba) = \bf (\lambda \ba + \bx) = \lambda \bf (\ba).
$$

Since $\bf (\ba) \neq 0$, hence $\lambda = \mu$ must hold.
Therefore, $\bx = \by$ must hold true too.
Hence, the representation is unique.
```

```{prf:theorem} Dimension of the kernel of a linear functional
:label: res-la-linear-functional-kernel-dim

Let $\VV$ be a finite dimensional vector space
of dimension $n$. Then, the dimension of
the null space of any nonzero linear functional on $\VV$ is $n-1$.
In other words, the codimension of the kernel of a nonzero
linear functional is 1.
````
```{prf:proof}
Let $\BBB = \{\bv_1, \dots, \bv_k \}$ the any basis
for the space $\bf^{-1}(0)$. 

Choose any $\ba \in \VV$ such that $\bf(\ba) \neq 0$.

Then, the set:

$$
\CCC = \{\ba, \bv_1, \dots, \bv_k \}
$$
is linearly independent since $\ba \notin \bf^{-1}(0)$.

At the same time, since any vector $\bx \in \VV$ can be
represented using $\ba$ and the null space spanned
by $\BBB$, hence $\CCC$ spans $\VV$ 
(while $\BBB$ doesn't).
Thus,

$$
n = k + 1.
$$

Alternatively:

$$
\dim \bf^{-1}(0) = k = n - 1
$$

or 

$$
\codim \bf^{-1}(0) = n - \dim \bf^{-1}(0) = 1.
$$
```

## Hyper Planes

We present a general definition of hyperplanes in this
section. For a definition specific to real vector spaces,
see {prf:ref}`def-hyperplane`.

```{prf:definition} Hyperplane
:label: def-la-hyperplane-functional

Let $\bf$ be a nonzero linear functional on $\VV$. Let $a \in \FF$.
A set of the form:

$$
H_{\bf, a} \triangleq \{ \bx \in \VV \ST \bf(\bx) = a \}
$$
is called a hyperplane. In other words,

$$
H_{\bf, a} = \bf^{-1}(a).
$$
```

```{prf:theorem} A span as a hyperplane
:label: res-la-lf-hyperplane-span

Let $\VV$ be a finite dimensional space with $\dim \VV = n$.
Let $S = \{\bv_1, \dots, \bv_{n-1} \}$ be any set of
$n-1$ linearly independent vectors of $\VV$. Then,
$\span S$ is a hyperplane.
```

```{prf:proof}
Since $\dim \VV = n$, it is possible to select
a vector $\bv_n$ such that $\BBB = S \cup \{ \bv_n \}$
is linearly independent and forms a basis for $\VV$.

Following {prf:ref}`res-la-finite-dual-space-basis`,
it is possible to construct a linear functional $\bf$
such that:

$$
\bf(\bv_i) = \begin{cases}
1 && \text{ if } && i = n\\
0 && \text{ if } && 1 \leq i < n
\end{cases} . 
$$

Now, consider the null space of $\bf$
given by  $\bf^{-1}(0)$. It is clear by definition
that $\bv_i \in \bf^{-1}(0)$ for $i=1,\dots, n-1$.

From {prf:ref}`res-la-linear-functional-kernel-dim`,
$\dim \bf^{-1}(0) = n -1$. Thus, $S$ forms a basis
for $\bf^{-1}(0)$ and:

$$
\span S = \bf^{-1}(0).
$$

Thus, $\span S$ is a hyperplane.
```
## Dual Space of Dual Space

```{div}
Since $\VV^*$ (the dual of $\VV$) is a vector space, we can
think of the dual space of $\VV^*$ too.
The dual of the dual is denoted by $\VV^{**}$.
Consider the case where $\VV$ is finite dimensional.

1. $\VV$ and $\VV^*$ have the same dimension. 
1. Thus, \VV$ and $\VV^*$ are isomorphic.
1. Since $\VV^*$ is finite dimensional, hence $\VV^{**}$ is finite dimensional too.
1. In fact, $\dim \VV^* = \dim \VV^{**}$.
1. Thus, $\VV^*$ and $\VV^{**}$ are isomorphic.
1. Hence, $\VV$ and $\VV^{**}$ are isomorphic too.

It is possible to write an isomorphism between $\VV$ and $\VV^{**}$
without the choice of a basis. Such an isomorphism is said to be *natural*.
```

## Normed Vector Spaces

If $\VV$ is equipped with a norm $\| \cdot \|$, it makes sense
to come up with the notion of a norm on the dual space too.
The *dual norm* is a measure of size of the linear functional.
By size of a functional, we mean how big is the number $|f(\bx)|$
with respect to the size of $\bx$ given by $\| \bx \|$. 

```{prf:definition} Dual norm
:label: def-la-dual-norm

Let $\VV$ be a normed vector space and $\VV^*$ be its dual space
of linear functionals. 
The *dual norm* of a linear functional $\bf$ belonging to $\VV^*$
is defined as:

$$
\| \bf \|_* \triangleq \sup \{ |\bf(\bx)| \ST \| \bx \| \leq 1 \}.
$$
```

## Inner Product Spaces
The {prf:ref}`inner product <def-la-inner-product>`
is a binary operator from $\VV \times \VV$ to $\FF$.
If the second argument is fixed, then it becomes a linear functional.

```{prf:theorem} Inner product as linear functional
:label: res-la-inner-product-linear-functional

Let $\VV$ be an inner product space. 
For any $\bv \in \VV$, the
mapping $T_{\bv} : \VV \to \FF$ defined by:

$$
T_{\bv} (\bx) \triangleq \langle \bx , \bv \rangle  \Forall \bx \in \VV
$$
is a linear functional. Consequently, $T_{\bv} \in \VV^*$.
```

```{prf:proof}
Since an inner product is linear in the first argument, hence:

$$
T_{\bv} (\alpha \bx + \by) = \langle \alpha \bx + \by , \bv \rangle
= \alpha \langle \bx , \bv \rangle + \langle \by , \bv \rangle
=  \alpha T_{\bv} (\bx) + T_{\bv} (\by).
$$
Thus, the functional $T_{\bv}$ is linear.
```

```{prf:theorem} Arithmetic on linear functionals
:label: res-la-ip-linear-functional-arithmetic

Addition of inner product based linear functionals:

$$
T_{\bx} + T_{\by} = T_{\bx + \by}.
$$
Scalar multiplication on inner product based linear functions:

$$
\alpha T_{\bx} = T_{ \overline{\alpha} \bx}.
$$
```

```{prf:proof}
Recall that sum of functions is defined as:

$$
(T_{\bx} + T_{\by}) (\bv) = T_{\bx}(\bv) + T_{\by}(\bv).
$$
Now,

$$
T_{\bx + \by}(\bv) = \langle \bv, \bx + \by \rangle 
= \langle \bv, \bx \rangle + \langle \bv, \by \rangle
=  T_{\bx}(\bv) + T_{\by}(\bv)
= (T_{\bx} + T_{\by}) (\bv)
$$

Thus, $T_{\bx + \by} = T_{\bx + \by}$.

Recall that scaling of a function is defined as:

$$
(\alpha T_{\bx}) (\bv) = \alpha (T_{\bx}(\bv)).
$$

Now,

$$
\alpha (T_{\bx}(\bv))
= \alpha \langle \bv, \bx \rangle
= \langle \bv, \overline{\alpha} \bx \rangle
= T_{ \overline{\alpha} \bx} (\bv).
$$

Thus, $\alpha T_{\bx} = T_{ \overline{\alpha} \bx}$.
```



```{prf:theorem} Linear functional as inner product
:label: res-la-linear-functional-inner-product

Let $\VV$ be a finite dimensional inner product space and let
$\bf$ be a linear functional in $\VV^*$. 
Then, there exists a vector $\bv \in \VV$ 
such that $\bf = T_{\bv}$. 

In other words, every linear functional is an inner product.
```

```{prf:proof}
Recall from {prf:ref}`res-la-ip-finite-onb-existence`
that every finite dimensional inner product space
has an orthonormal basis.

Let $\BBB = \{\be_1, \dots, \be_n \}$
be an orthonormal basis of $\VV$.

Now, consider the corresponding linear functionals $T_{\be_j}$
for $j = 1, \dots, n$.

Note that:

$$
T_{\be_j} (\be_i) = \langle \be_i , \be_j \rangle = \delta(i, j)
$$
since $\BBB$ is an orthonormal basis.

Then, following {prf:ref}`res-la-finite-dual-space-basis`,
the set $\FFF = \{T_{\be_1}, \dots, T_{\be_n} \}$
forms a basis $\VV^*$.

Thus, any $\bf \in \VV^*$ can be written as:

$$
\bf = \sum_{j=1}^n c_j T_{\be_j} 
= \sum_{j=1}^n  T_{\overline{c_j}\be_j} 
= T_{\sum_{j=1}^n \overline{c_j}\be_j}
$$
using {prf:ref}`res-la-ip-linear-functional-arithmetic` above.

Thus, $\bf$ is equal to an inner product by the vector
$\sum_{j=1}^n \overline{c_j}\be_j$.
```

```{prf:theorem} Zero functional in inner product space
:label: res-la-ip-zero-functional

Let $\VV$ be an inner product space. Then,
$\bzero \in \VV^*$ is same as $T_{\bzero} = \langle \cdot, \bzero \rangle$.

In other words,

$$
T_{\bzero} = \bzero \in \VV^*
$$
and there is no other $\bv \in V$ such that $T_{\bv} = \bzero$.
```

```{prf:proof}
For $\bzero \in \VV$, it is straight-forward to see that

$$
T_{\bzero}(\bv) = \langle \bv, \bzero \rangle = 0.
$$

Thus, $T_{\bzero}$ is the zero functional. 
To show that there is no other $\bv \in \VV$ such that
$T_{\bv}$ is a zero functional, we note that,

$$
\bv \neq 0 \implies \langle \bv, \bv \rangle > 0.
$$

Thus, $T_{\bv} (\bv) > 0$ if $\bv \neq \bzero$.
```


```{prf:theorem} Isomorphism between $\VV$ and $\VV^*$
:label: res-la-ip-dual-space-isomorphism

Let $\VV$ be an inner product space. Define a map $T : \VV \to \VV^*$ by

$$
T (\bv) \triangleq \langle \cdot, \bv \rangle = T_{\bv};
$$
i.e., $T_{\bv}$ is a linear functional on $\VV$ whose value
on $\bx \in \VV$ is $\langle \bx, \bw \rangle$.

Then, $T$ is an isomorphism.
```

```{prf:proof}
To show that $T$ is an isomorphism, we need to show that:

* $T$ is injective.
* $T$ is surjective.
* $T$ preserves the vector space algebraic structure.
```
