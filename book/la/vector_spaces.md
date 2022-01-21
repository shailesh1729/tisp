(sec:la:vector-spaces)=
# Vector Spaces

(sec:la:algebraic_structure)=
## Algebraic Structures

In mathematics, the term *algebraic structure* refers to an arbitrary set 
with one or more operations defined on it.

* Simpler algebraic structures include groups, rings, and fields. 
* More complex algebraic structures like vector spaces are built 
  on top of the simpler structures.

We will develop the notion of vector spaces as a progression 
of these algebraic structures.

### Groups

A group is a set with a single binary operation. It is one of the simplest
algebraic structures.

````{prf:definition} Group
:label: def-la-group

Let $G$ be a set. 
Let $* : G \times G \to G$ be a binary operation 
defined on $G$ mapping $(g_1, g_2) \to * (g_1, g_2)$ and denoted as

$$
* (g_1, g_2)\triangleq g_1 * g_2.
$$
If the binary operation $*$ satisfies the following properties:

1. [Closure] The set $G$ is closed under the binary operation $*$. i.e.

   $$
   \forall g_1, g_2 \in G, g_1 * g_2 \in G.
   $$
1. [Associativity] For every $g_1, g_2, g_3 \in G$

   $$
   g_1 * (g_2 * g_3) = (g_1 * g_2) * g_3
   $$
1. [Identity element] There exists an element $e \in G$ such that

   $$
   g * e = e * g = g \quad \forall g \in G
   $$
1. [Inverse element] For every $g \in G$ there exists an 
   element $g^{-1} \in G$ such that

   $$
   g * g^{-1} = g^{-1} * g = e
   $$

then the set $G$ together with the operator $*$ denoted 
as $(G, *)$ is known as a *group*.
````

Above properties are known as *group axioms*.
Note that commutativity is not a requirement of a group.

```{prf:remark}
Frequently, the group operation is the regular mathematical
addition. In those cases, we write $g_1 * g_2$ as $g_1 + g_2$. 
Otherwise, we will write $g_1 * g_2$ as $g_1 g_2$. 

Often, we may simply write a group $(G, *)$ as $G$ 
when the underlying operation $*$ is
clear from the context.
```

### Commutative groups

A commutative group is a richer structure than a group. Its
elements also satisfy the commutativity property.

````{prf:definition} Commutative group
:label: def-la-commutative-group

Let $(G, *)$ be a group such that its binary operation $*$ 
satisfies an additional property:

1. [Commutativity] For every $g_1, g_2 \in G$

   $$
   g_1 g_2 = g_2 g_1 
   $$

Then $(G,*)$ is known as a *commutative group* 
or an *Abelian group*.
````

### Rings

A ring is a set with two binary operations defined over it 
with some properties as described below. 

(def:alg:associative_ring)=
````{prf:definition} Associative ring
:label: def-la-associative-ring

Let $R$ be a set with two binary operations 
$+ : R \times R \to R$ (addition) mapping $(r_1, r_2) \mapsto  r_1 + r_2$
and 
$\cdot : R \times R \to R$ (multiplication) mapping $(r_1, r_2) \mapsto  r_1 \cdot r_2$
such that $(R, +, \cdot)$ satisfies following properties:

1. $(R, +)$ is a commutative group.
1. $R$ is closed under multiplication.

   $$
   r_1 \cdot r_2 \in R \quad \forall r_1, r_2 \in R
   $$
1. Multiplication is associative.

   $$
   r_1 \cdot (r_2 \cdot r_3) = (r_1 \cdot r_2) \cdot r_3 \quad \forall r_1, r_2, r_3 \in R
   $$
1. Multiplication distributes over addition.

   $$
    \begin{aligned}
        &r_1 \cdot (r_2 + r_3) = (r_1 \cdot r_2) + (r_1 \cdot r_3) \quad \forall r_1, r_2, r_3 \in R\\
        &(r_1 + r_2) \cdot r_3 = (r_1 \cdot r_3) + (r_2 \cdot r_3) \quad \forall r_1, r_2, r_3 \in R
    \end{aligned}
   $$

Then, $(R, +, \cdot)$ is known as an *associative ring*.
We denote the identity element for $+$ as $0$ and call it additive identity.
````

```{prf:remark}
In the sequel we will write $r_1 \cdot r_2$ as $r_1 r_2$. 
We may simply write a ring $(R, +, \cdot)$ as $R$ when 
the underlying operations $+,\cdot$ are
clear from the context.
```

There is a hierarchy of ring like structures. In particular we mention:


1. Associative ring with identity
1. Field



````{prf:definition} Associative ring with identity
:label: def-la-associative-ring-identity

Let $(R, +, \cdot)$ be an associate ring with the property that
there exists an element $1 \in R$ (known as multiplicative identity) such that

$$
1 \cdot r = r \cdot 1 = r \quad \forall r \in R.
$$

Then $(R, +, \cdot)$ is known as an *associative ring with identity*.
````


### Fields

 Field is the richest algebraic structure on one set with two operations.

````{prf:definition} Field
:label: def-la-field

Let $F$ be a set with two binary operations 
$+: F \times F \to F$ (addition) mapping $(x_1, x_2) \mapsto  x_1 + x_2$
and $\cdot: F \times F \to F$ (multiplication) mapping $(x_1, x_2) \mapsto  x_1 \cdot x_2$
such that $(F, +, \cdot)$ satisfies following properties:

1. $(F, +)$ is a commutative group (with additive identity as $0 \in F$).
1. $(F \setminus \{0\}, \cdot)$ is a commutative group (with multiplicative identity as $1 \in F$).
1. Multiplication distributes over addition:

   $$
    \alpha \cdot (\beta + \gamma) = (\alpha \cdot \beta) + (\alpha \cdot \gamma) \quad \forall \alpha, \beta, \gamma \in F
   $$

Then $(F, +, \cdot)$ is known as a *field*.
````

The definition above implies a number of properties. For any $a,b,c \in F$, we have:

* Closure: $a + b \in F$, $a b \in F$.
* Associativity of addition and multiplication: $a + (b + c) = (a + b) + c$ and $a (b c) = (a b) c$.
* Commutativity of addition and multiplication: $a + b = b + a$ and $a b = b a $.
* Additive identity: $0 + a = a + 0 = a$.
* Multiplicative identity: $1 a = a 1 = a$.
* Additive inverses: $a + (-a) = (-a) + a = 0$.
* Multiplicative inverses for every $a \neq 0$: $ a a^{-1} = a^{-1} a  = 1$.
* Distributivity: $a ( b + c) = (a b) + (a c)$.


````{prf:example} Examples of fields
*  The set of real numbers $\RR$ is a field.
*  The set of complex numbers $\CC$ is a field.
*  The Galois field GF-2 is the the set $\{ 0, 1 \}$ with modulo-2 additions and multiplications.
````

## Vector Spaces

We are now ready to define a vector space. 
A vector space involves two sets. 
One set $\VV$ contains the vectors. 
The other set $\FF$ (a field) contains scalars 
which are used to scale the vectors.


````{prf:definition} Vector space
:label: def-la-vector-space

A set $\VV$ is called a *vector space* over the field $\FF$ 
(or a $\FF$-vector space) if there exist two mappings:

* Vector addition: $+ : \VV \times \VV \to \VV$ mapping $(\bv_1, \bv_2) \to  \bv_1 + \bv_2$ 
  for any $\bv_1, \bv_2 \in \VV$ to another vector in $\VV$ denoted by $\bv_1 + \bv_2$
* Scalar multiplication: $\cdot : \FF \times \VV \to \VV$ mapping 
  $(\alpha, \bv) \to  \alpha \cdot \bv$ with $\alpha \in \FF$ and $\bv \in \VV$
  to another vector in $\VV$ denoted by $\alpha \cdot \bv$ or just $\alpha \bv$

which satisfy following requirements:

1. $(\VV, +)$ is a commutative group.
1. Scalar multiplication $\cdot$ distributes over vector addition $+$:

   $$
    \alpha (\bv_1 + \bv_2) = \alpha \bv_1 + \alpha \bv_2 \quad \forall \alpha \in \FF; \forall \bv_1, \bv_2 \in \VV.
   $$
1. Addition in $\FF$ distributes over scalar multiplication $\cdot$:

   $$
   ( \alpha + \beta) \bv = (\alpha \bv) + (\beta \bv) \quad \forall \alpha, \beta \in \FF; \forall \bv \in \VV.
   $$
1. Multiplication in $\FF$ commutes over scalar multiplication:

   $$
    (\alpha \beta)  \cdot \bv = \alpha \cdot (\beta \cdot \bv) = \beta  \cdot (\alpha \cdot \bv) = (\beta \alpha) \cdot \bv
        \quad \forall \alpha, \beta \in \FF; \forall \bv \in \VV.
   $$
1. Scalar multiplication from multiplicative identity $1 \in \FF$ satisfies the following:

   $$
    1 \bv = \bv \quad \forall \bv \in \VV.
   $$
````

Some remarks are in order:


*  $\VV$ as defined above is also known as a $\FF$ vector space.
*  Elements of $\VV$ are known as vectors.
*  Elements of $\FF$ are known as scalars.
*  There are two $0$s involved: $0 \in \FF$ and $\bzero \in \VV$. 
   It should be clear from context which $0$ is being referred to.
*  $\bzero \in \VV$ is known as the zero vector.
*  All vectors in $\VV \setminus \{\bzero\}$ are non-zero vectors.
*  We will typically denote elements of $\FF$ by $\alpha, \beta, \dots$.
*  We will typically denote elements of $\VV$ by $\bv_1, \bv_2, \dots$.


We quickly look at some vector spaces which will appear again and again in our discussions.

### N-Tuples

````{prf:example} $N$-tuples as a vector space
:label: def-la-n-tuple-vector-space

Let $\FF$ be some field.

The set of all $N$-tuples $(a_1, a_2, \dots, a_N)$ with $a_1, a_2, \dots, a_N \in \FF$
is denoted as $\FF^N$. 
This is a vector space with the operations of coordinate-wise
addition and scalar multiplication.

Let $\bu, \bv \in \FF^N$ with

$$
    \bu = (u_1, \dots, u_N)
$$

and

$$
    \bv = (v_1, \dots, v_N).
$$

Addition is defined as

$$
    \bu + \bv \triangleq (u_1 + v_1,  \dots, u_N + v_N).
$$

Let $c \in \FF$. Scalar multiplication is defined as

$$
    c \bu \triangleq (c u_1, \dots, c u_N).
$$

$\bu, \bv$ are called equal if $u_1 = v_1, \dots, u_N = v_N$.

In matrix notation, vectors in $\FF^N$ are also written as row vectors

$$
    \bu = \begin{bmatrix} u_1 & \dots & u_N \end{bmatrix}
$$

or column vectors

$$
    \bu = \begin{bmatrix} u_1 \\ \vdots \\ u_N \end{bmatrix}
$$

````

### Matrices

````{prf:example} Matrices
:label: def-la-matrix-vector-space

Let $\FF$ be some field. A matrix is an array of the form

$$
    \begin{bmatrix}
    a_{11} & a_{12} & \dots & a_{1N} \\
    a_{21} & a_{22} & \dots & a_{2N} \\
    \vdots & \vdots & \ddots &  \vdots \\
    a_{M 1} & a_{M 2} & \dots & a_{MN} \\
    \end{bmatrix}
$$

with $M$ rows and $N$ columns where $a_{ij} \in \FF$.

The set of these matrices is denoted as $\FF^{M \times N}$ which is a vector space with
operations of matrix addition and scalar multiplication.

Let $A, B \in \FF^{M \times N}$. Matrix addition is defined by

$$
    (A + B)_{ij} \triangleq A_{ij} + B_{ij}.
$$

Let $c \in \FF$. Scalar multiplication is defined by

$$
    (cA)_{ij} \triangleq c A_{ij}.
$$
````

### Polynomials

````{prf:example} Polynomials
:label: def-la-polynomial-vector-space

Let $\FF[x]$ denote the set of all polynomials with coefficients drawn from
field $\FF$. i.e. if $f(x) \in \FF[x]$, then it can be written as

$$
    f(x) = a_n x^n + a_{n-1}x^{n -1} + \dots + a_1 x + a_0
$$

where $a_i \in \FF$.

The set $\FF[x]$ is a vector space with usual operations of addition and scalar multiplication

$$
    f(x) + g(x) = (a_n + b_n)x^n + \dots + (a_1 + b_1 ) x + (a_0 + b_0).
$$

$$
    c f(x) = c a_n x^n + \dots + c a_1 x + c a_0.
$$

````

### Vector Space Identities 

Some useful identities are presented here.
````{prf:theorem} Uniqueness of additive identity
The $\bzero$ vector in a vector space $\VV$ is unique.
````
```{prf:proof}
Assume that there is another vector $\bo$ satisfying

$$
\bv + \bo = \bo + \bv = \bv \Forall \bv \in \VV.
$$

Then, in particular, it satisfies: $\bzero + \bo = \bzero$.
At the same time, we have $\bo = \bo + \bzero$.
Thus,

$$
\bzero = \bzero + \bo = \bo + \bzero = \bo.
$$
Thus, $\bzero$ is unique.
```

````{prf:theorem} Cancellation law
:label: res-la-vs-cancellation-law

Let $\VV$ be an $\FF$ vector space. 
Let $\bx, \by, \bz$ be some vectors in $\VV$ such that
$\bx + \bz = \by + \bz$. 
Then $\bx = \by$.
````
```{prf:proof}
Since $\bz \in \VV$, there exists an additive inverse $\bv \in \VV$ such that
$\bz + \bv = \bzero$.

Now

$$
\bx = \bx + \bzero = \bx + (\bz + \bv) = (\bx + \bz) + \bv = (\by + \bz) + \bv 
= \by + (\bz + \bv)  = \by + \bzero = \by.
$$
```

````{prf:corollary} Uniqueness of additive inverse
The additive inverse of a vector $\bx$ in $\VV$ is unique.
````
```{prf:proof}
Let $\by$ and $\bz$ be additive inverses of $\bx$. Then,
we have:

$$
\bx + \by = \bzero = \bx + \bz.
$$
By cancellation law, $\by = \bz$.

Thus, the additive inverse of a vector is unique.
```

````{prf:theorem}
In a vector space $\VV$ the following statements are true

1. $0 \bx = \bzero \Forall \bx \in \VV$.
1. $a \bzero = \bzero \Forall a \in \FF$.
1. $(-a)\bx = - (a \bx) = a(- \bx) \Forall a \in \FF \text{ and } \bx \in \VV$.
````

```{prf:proof}
(1) $0 \bx = \bzero \Forall \bx \in \VV$.

By distributive law:

$$
0 \bx =  (0 + 0) \bx = 0 \bx + 0 \bx.
$$

By existence of zero vector:

$$
0 \bx = \bzero + 0 \bx.
$$

Thus,

$$
0 \bx = 0 \bx + 0 \bx = \bzero + 0 \bx.
$$

Now, by cancellation law:

$$
0 \bx = \bzero.
$$


(2) $a \bzero = \bzero \Forall a \in \FF$.

Due to additive identity and distribution law:

$$
a \bzero = a (\bzero + \bzero) = a \bzero + a \bzero.
$$

Due to additive identity:

$$
a \bzero = \bzero + a \bzero.
$$

Combining

$$
a \bzero + a \bzero = \bzero + a \bzero. 
$$

Now applying the cancellation law, we get:

$$
a \bzero = \bzero. 
$$

(3) $(-a)\bx = - (a \bx) = a(- \bx) \Forall a \in \FF \text{ and } \bx \in \VV$.

We start with

$$
\bzero = 0 \bx = (a + (-a)) \bx = a \bx + (-a)\bx.
$$
Thus, $(-a)\bx$ is the additive inverse of $a \bx$. Thus, $ (-a)\bx =  -(a\bx)$.


Similarly,

$$
\bzero = a \bzero = a (\bx + (-\bx)) = a \bx + a (-\bx).
$$
Thus, $a (-\bx)$ is also additive inverse of $a \bx$. Thus, $a (-\bx) = - (a \bx)$.
```

## Linear Independence

````{prf:definition} Linear combination
:label: def-la-linear-combination

A *linear combination* of two vectors $\bv_1, \bv_2 \in \VV$ is defined as

$$
      \alpha \bv_1 + \beta \bv_2
$$

where $\alpha, \beta \in \FF$.

A *linear combination* of $p$ vectors $\bv_1,\dots, \bv_p \in \VV$ is defined as

$$
      \sum_{i=1}^{p} \alpha_i \bv_i
$$
where $\alpha_i \in \FF$.
````
Note that a linear combination *always* consists of a *finite* number of vectors.


````{prf:definition} Linear combination vector
:label: def-la-linear-combination-2

Let $\VV$ be a vector space and let $S$ be a nonempty subset of $\VV$. 
A vector $\bv \in \VV$ is called
a *linear combination* of vectors of $S$ 
if there exist a finite number of vectors
$\bs_1, \bs_2, \dots, \bs_n \in S$ and scalars 
$a_1, \dots, a_N$ in $\FF$ such that

$$
    \bv = a_1 \bs_1 + a_2 \bs_2 + \dots a_n \bs_n.
$$
We also say that $v$ is a linear combination of 
$\bs_1, \bs_2, \dots, \bs_n$ and $a_1, a_2, \dots, a_n$
are the coefficients of linear combination.
````

```{prf:definition} Trivial linear combination
A linear combination $a_1 \bs_1 + a_2 \bs_2 + \dots a_n \bs_n$
is called *trivial* if $a_1 = a_2 = \dots = a_n = 0$.

$\bzero$ is a trivial linear combination of any subset of $\VV$ as:

$$
    \bzero = 0 \bs_1 + 0 \bs_2 + \dots 0 \bs_n.
$$
```

A linear combination may refer to the expression itself or its value. 
e.g. two different linear combinations may have same value.

````{prf:definition} Linear dependence
:label: def-la-linearly-dependent

A finite set of non-zero vectors 
$\{\bv_1, \cdots, \bv_p\} \subset \VV$ is called *linearly dependent* if
there exist $\alpha_1,\dots,\alpha_p \in \FF$ not all $0$ such that

$$
\sum_{i=1}^{p} \alpha_i \bv_i = \bzero.
$$
````
Since $\alpha_i$ are not all zero, hence, it is a non-trivial combination.

````{prf:definition} Linearly dependent set
:label: def-la-linearly-dependent-set

A set $S \subseteq \VV$ is called *linearly dependent* if 
there exist a finite number of distinct
vectors $\bu_1, \bu_2, \dots, \bu_n \in S$
and scalars $a_1, a_2, \dots, a_n \in \FF$ not all zero,
such that

$$
    a_1 \bu_1 + a_2 \bu_2 + \dots + a_n \bu_n = \bzero.
$$
````
In other words, there exists a non-trivial linear 
combination which equals $\bzero$.

````{prf:definition} Linearly independent set
:label: def-la-linearly-independent-set

A set $S \subseteq \VV$ is called 
*linearly independent* if it is not linearly dependent.
````

````{prf:definition} Linearly independent vectors
:label: def-la-linearly-independent-vectors

More specifically a finite set of non-zero vectors
$\{\bv_1, \dots, \bv_n\} \subset \VV$ is called 
*linearly independent* if

$$
\sum_{i=1}^{n} \alpha_i \bv_i = 0 \implies \alpha_i  = \bzero \Forall 1 \leq i \leq n.
$$
````
In other words, the only linear combination giving us $\bzero$ vector
is the trivial linear combination.

````{prf:example} Examples of linearly dependent and independent sets

* The empty set is linearly independent.
* A set of a single non-zero vector $\{\bv\}$ is always linearly independent. Prove!
* If two vectors are linearly dependent, we say that they are *collinear*.
* Alternatively if two vectors are linearly independent, we say that they are not *collinear*.
* If a set $\{\bv_1, \dots, \bv_p\}$ is linearly independent, 
  then any subset of it will be linearly independent. Prove!
* Adding another vector $\bv$ to the set may make it linearly dependent. When?
* It is possible to have an infinite set to be linearly independent.
  Consider the set of polynomials $\{1, x, x^2, x^3, \dots\}$.
  This set is infinite, yet linearly independent.
````

````{prf:theorem}
Let $\VV$ be a vector space. Let $S_1 \subseteq S_2 \subseteq \VV$. 
If $S_1$ is linearly dependent,
then $S_2$ is linearly dependent.
````

````{prf:corollary}
Let $\VV$ be a vector space. 
Let $S_1 \subseteq S_2 \subseteq \VV$. 
If $S_2$ is linearly independent,
then $S_1$ is linearly independent.
````


## Span 
Vectors can be combined to form other vectors. 
It makes sense to consider the set of all vectors which
can be created by combining a given set of vectors.

````{prf:definition} Span
:label: def-la-span

Let $S \subset \VV$ be a subset of vectors. 
The *span* of $S$ denoted as $\langle S \rangle$ or $\span S$
is the
set of all possible linear combinations of vectors belonging to $S$.

$$
\span S = \langle S \rangle \triangleq
\{ \bv \in \VV \ST \bv = \sum_{i=1}^{p} \alpha_i \bv_i
\quad \text{for some} \quad \bv_i \in S;\; \alpha_i \in \FF; \; p \in \mathbb{N}\}
$$

For convenience we define $\span \EmptySet = \{ \bzero\}$.
````

Span of a finite set of vectors 
$\{\bv_1, \cdots, \bv_p\}$ is denoted by 
$\langle \bv_1, \cdots, \bv_p \rangle$.

$$
\langle \bv_1, \cdots, \bv_p \rangle = \left \{\sum_{i=1}^{p} \alpha_i \bv_i \ST \alpha_i \in \FF \right \}.
$$  
We say that a set of vectors $S \subseteq \VV$
spans $\VV$ if $\langle S \rangle = \VV$.

````{prf:proposition}
Let $S \subseteq \VV$, then $\Span (S) \subseteq \VV$.
````

````{prf:definition} Spanning a vector space
Let $S \subset \VV$. We say that $S$ *spans (or generates)* $\VV$ if

$$
\langle S \rangle = \VV.
$$

In this case we also say that vectors of $S$ span (or generate) $\VV$.
````

````{prf:theorem}
Let $S$ be a linearly independent subset of a vector space $\VV$ 
and let $\bv \in \VV \setminus S$.
Then $S \cup \{ v \}$ is linearly dependent 
if and only if $ v \in \Span(S)$.
````

## Basis
````{prf:definition}
:label: def-la-basis

A set of linearly independent vectors $\BBB$ is called a
*basis* of $\VV$ if $\langle \BBB \rangle = \VV$;
i.e., $\BBB$ spans $\VV$.
````

````{prf:example} Basis examples
:label: def-la-standard-basis

* Since $\Span(\EmptySet) = \{ \bzero \}$ 
  and $\EmptySet$ is linearly independent,
  $\EmptySet$ is a basis for the zero vector space $\{ 0 \}$.
* The basis $\{ \be_1, \dots, \be_N\}$ with $\be_1 = (1, 0, \dots, 0)$,
  $\be_2 = (0, 1, \dots, 0)$, $\dots$, $\be_N = (0, 0, \dots, 1)$,
  is called the *standard basis* for $\FF^N$.
* The set $\{1, x, x^2, x^3, \dots\}$ is the 
  *standard basis* for $\FF[x]$. 
  Indeed, an infinite basis. 
  Note that though the basis itself is infinite, 
  yet every polynomial $p \in \FF[x]$
  is a linear combination of finite number of elements from the basis.
````

We review some properties of bases.

````{prf:theorem} Unique representation
:label: res-la-basis-characterization-unique-rep

Let $\VV$ be a vector space and 
$\BBB = \{ \bv_1, \bv_2, \dots, \bv_n\}$ be a subset of $\VV$.
Then $\BBB$ is a basis for $\VV$ if and only if
each $v \in \VV$ can be uniquely
expressed as a linear combination of vectors of $\BBB$.
In other words:

$$
\bv = a_1 \bv_1 + a_2 \bv_2  + \dots + a_n \bv_n
$$
for unique scalars $a_1, \dots, a_n$.
````
This theorem states that a basis $\BBB$ provides a unique representation
to each vector $v \in \VV$ where the representation is defined as the $n$-tuple
$(a_1, a_2, \dots, a_n)$.


If the basis is infinite, then the above theorem needs to be modified as follows:
````{prf:theorem} Unique representation for infinite basis
:label: res-la-infinite-basis-characterization-unique-rep

Let $\VV$ be a vector space and $\BBB$ be a subset of $\VV$.
Then $\BBB$ is a basis for $\VV$
if and only if each $\bv \in \VV$ can be uniquely
expressed as a linear combination of vectors of $\BBB$:

$$
    \bv = a_1 \bv_1 + a_2 \bv_2  + \dots + a_n \bv_n
$$
for unique scalars $a_1, \dots, a_n$
and unique vectors $\bv_1, \bv_2, \dots \bv_n \in \BBB$.
````

````{prf:theorem}
:label: res-la-finite-basis

If a vector space $\VV$ is spanned by a finite set $S$, 
then some subset of $S$ is a basis
for $\VV$. Hence $\VV$ has a finite basis.
````

````{prf:theorem} Replacement theorem
:label: res-la-replacement-theorem
Let $\VV$ be a vector space that is spanned by a set $G$
containing exactly $n$ vectors.
Let $L$ be a linearly independent subset of $\VV$ 
containing exactly $m$ vectors.

Then $m \leq n$ and there exists a subset $H$ of $G$
containing exactly $n-m$ vectors
such that $L \cup H$ spans $\VV$.
````

````{prf:corollary}
Let $\VV$ be a vector space having a finite basis. 
Then, every basis for $\VV$ contains
the same number of vectors.
````

````{prf:definition} Dimension of vector space
:label: def-la-dimension

A vector space $\VV$ is called *finite-dimensional*
if it has a basis
consisting of a finite number of vectors.
This unique number of vectors in any basis
$\BBB$ of the vector space $\VV$
is called the *dimension* or *dimensionality* of the vector space.
It is denoted as $\dim \VV$. We say:

$$
\dim \VV \triangleq |\BBB|
$$

If $\VV$ is not finite-dimensional,
then we say that $\VV$ is *infinite-dimensional*.
````

````{prf:example} Vector space dimensions

*  Dimension of $\FF^N$ is $N$.
*  Dimension of $\FF^{M \times N}$ is $MN$.
*  The vector space of polynomials $\FF[x]$ is infinite dimensional.
````

````{prf:proposition}
Let $\VV$ be a vector space with dimension $n$.

1. Any finite spanning set for $\VV$ contains at least $n$ vectors, 
   and a spanning set that contains exactly $n$ vectors is a basis for $\VV$.
1. Any linearly independent subset of $\VV$ that contains exactly $n$ vectors 
   is a basis for $\VV$.
1. Every linearly independent subset of $\VV$ can be extended to a basis for $\VV$.
````


````{prf:definition} Ordered basis
:label: def-la-ordered-basis

For a finite dimensional vector space $\VV$, an *ordered basis*
is a basis for $\VV$ with a specific order. In other words,
it is a finite *sequence* (or tuple) of linearly independent vectors in
$\VV$ that spans $\VV$.
````

Typically, we will write an ordered basis as 
$\BBB  = \{ \bv_1, \bv_2, \dots, \bv_n\}$
and assume that the basis vectors are ordered 
in the order they appear.

With the help of an ordered basis, 
we can define a coordinate vector.

````{prf:definition} Coordinate vector
:label: def-la-coordinate-vector

Let $\BBB  = \{ \bv_1, \dots, \bv_n\}$ be an ordered basis for $\VV$.
For any $\bx \in \VV$,
let $\alpha_1, \dots, \alpha_n$ be unique scalars such that

$$
    x = \sum_{i=1}^n \alpha_i \bv_i.
$$
The *coordinate vector* of $\bx$ relative to $\BBB$ is defined as

$$
    [\bx]_{\BBB} = \begin{bmatrix}
    \alpha_1\\
    \vdots\\
    \alpha_n
    \end{bmatrix}.
$$
````

## Subspaces

````{prf:definition} Subspace
:label: def-la-subspace

Let $\WW$ be a subset of $\VV$. 
Then $\WW$ is called a *subspace* if $\WW$ is a vector space 
in its own right under the same vector addition $+$ 
and scalar multiplication $\cdot$ operations. i.e.

$$
\begin{aligned}
  + : &\WW \times \WW \to \WW\\
      &(\bw_1, \bw_2) \to  \bw_1 + \bw_2 \quad \bw_1, \bw_2 \in \WW
\end{aligned}
$$

$$
\begin{aligned}
  \cdot : &\FF \times \WW \to \WW\\
      &(\alpha, \bw) \to  \alpha \cdot \bw  \triangleq \alpha \bw \quad \alpha \in \FF; \bw \in \WW
\end{aligned}
$$
are defined by restricting $+ : \VV \times \VV \to \VV$ 
and $\cdot : \VV \times \VV \to \VV$ to $\WW$ and
$\WW$ is closed under these operations.
````

````{prf:example} Trivial subspaces

*  $\VV$ is a subspace of $\VV$.
*  $\{\bzero\}$ is a subspace of any $\VV$.
````

````{prf:theorem} Subspace characterization
:label: res-subspace-verification-condition

A subset $\WW \subseteq \VV$ is a subspace of $\VV$ if and only if

*  $\bzero \in\WW $.
*  $\bx + \by \in\WW $ whenever $\bx, \by \in\WW$.
*  $\alpha \bx \in\WW $ whenever $\alpha \in \FF$ and $\bx \in\WW $.
````

````{prf:example} Symmetric matrices
:label: ex-la-symmetric-matrix-subspace

A matrix $M \in \FF^{M \times N}$ is *symmetric* if

$$
    M^T = M.
$$
The set of symmetric matrices forms a subspace of set of all $M\times N$ matrices.
````

````{prf:example} Diagonal matrices
:label: ex-la-diagonal-matrix-subspace

A matrix $M$ is called a *diagonal* if $M_{ij} = 0$ whenever $i \neq j$.

The set of diagonal matrices is a subspace of $\FF^{M \times N}$.
````

````{prf:theorem} Intersection of subspaces
:label: res-la-subspace-intersection

Any intersection of subspaces of a vector space $\VV$ is a subspace of $\VV$.
````

We note that a union of subspaces is not necessarily a subspace, since its
not closed under addition. 

````{prf:theorem} Span is a subspace
The span of a set $S \subset \VV$ given by $\langle S \rangle$ is a subspace of $\VV$.
Moreover any subspace of $\VV$ that contains $S$ must also contain the span of $S$.
````

This theorem is quite useful. It allows us to construct subspaces from a given basis.

Let $\BBB$ be a basis of an $n$ dimensional space $\VV$.
There are $n$ vectors in $\BBB$.
We can create $2^n$ distinct subsets of $\BBB$.
Thus we can easily construct $2^n$ distinct subspaces of $\VV$.

Choosing some other basis lets us construct another set of subspaces. 

An $n$-dimensional vector space has infinite number of bases. 
Correspondingly, there are infinite possible subspaces. 

If $\WW_1$ and $\WW_2$ are two subspaces of $\VV$ 
then we say that $\WW_1$ is smaller than $\WW_2$ 
if $\WW_1 \subset \WW_2$.

````{prf:theorem}
Let $W$ be the smallest subspace containing vectors 
$\{ \bv_1, \dots, \bv_p \}$.
Then

$$
\WW = \langle \bv_1, \dots, \bv_p \rangle.
$$

i.e. $\WW$ is same as the span of $\{ \bv_1, \dots, \bv_p \}$.
````

````{prf:theorem} Subspace dimension
:label: res-la-subspace-dimension

Let $\WW$ be a subspace of a finite-dimensional vector space $\VV$. 
Then $\WW$ is finite dimensional and

$$
\dim \WW \leq \dim \VV.
$$

Moreover, if

$$
\dim \WW  = \dim \VV,
$$
then $\WW = \VV$.
````

````{prf:corollary}
If $\WW$ is a subspace for a finite-dimensional vector space $\VV$ 
then any basis for $\WW$ can be extended to a basis for $\VV$.
````



````{prf:definition} Subspace codimension
:label: def-subspace-codimension 

Let $\VV$ be a finite dimensional vector space and
$\WW$ be a subspace of $\VV$. The *codimension*
of $\WW$ is defined as

$$
\text{codim} \WW = \dim \VV - \dim \WW.
$$
````



## Sets in Vector Spaces

```{prf:definition} Arithmetic on sets
:label: def-vs-set-arithmetic

Let $C$, $D$ be subsets of an $\FF$ vector space
$\VV$. Let $\bz \in \VV$. 
Let $\lambda \in \FF$.
Let $\Lambda \subseteq \FF$.

The addition of sets is defined as:

$$
C + D \triangleq \{ \bx + \by \ST \bx \in C, \by \in D \}.
$$

The subtraction of sets is defined as:

$$
C - D \triangleq \{ \bx - \by \ST \bx \in C, \by \in D \}.
$$

Addition of a set with a vector is defined as:

$$
\bz + C \triangleq \{ \bz + \bx \ST \bx \in C\} = \{ \bz \} + C.
$$

Subtraction of set with a vector is defined as:

$$
C - \bz \triangleq \{ \bx - \bz \ST \bx \in C\} = C - \{ \bz \}.
$$

Scalar multiplication of a set with a scalar is defined as:

$$
\lambda C \triangleq \{ \lambda \bx \ST \bx \in C \}.
$$

Multiplication of a set of scalars with a set of vectors is defined as:

$$
\Lambda C \triangleq \bigcup_{\lambda \in \Lambda} \lambda C.
$$

Multiplication of a set of scalars with a vector is defined as:

$$
\Lambda \bz \triangleq \Lambda \{ \bz \} = \{ \lambda \bz \ST \lambda \in \Lambda\}.
$$
```

## Real Vector Spaces

```{prf:definition} Real vector space
:label: def-la-real-vector-space

A *real vector space* $\VV$ is a vector space
defined over the real field $\RR$.

In other words, the scalars come from the field of
real numbers.
```

There are several features associated with the real field.

* $\RR$ is {prf:ref}`totally ordered <def-st-totally-ordered-set>`.
* $\RR$ is {prf:ref}`complete <def-ms-complete-metric-space>`.