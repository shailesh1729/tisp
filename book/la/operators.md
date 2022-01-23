(sec:la:operators)=
# Operators

Operators are mappings from one vector space to another space.
Normally, they are {prf:ref}`total functions <def-st-total-function>`.

In this section, we introduce different types of operators
between vector spaces. Some operators are relevant 
only for {prf:ref}`real vector spaces <def-la-real-vector-space>`.

```{prf:definition} Homogeneous operator
:label: def-la-homogeneous-operator

Let $\XX$ and $\YY$ be vector spaces (over some field $\FF$). 
An operator $T : \XX \to \YY$ is called *homogeneous* if
for every $\bx \in \XX$ and for every $\lambda \in \FF$

$$
T(\lambda \bx) = \lambda T (\bx).
$$
```

```{prf:definition} Positively homogeneous operator
:label: def-la-positive-homogeneous-operator

Let $\XX$ and $\YY$ be *real* vector spaces (on field $\RR$). 
An operator $T : \XX \to \YY$ is called *positively homogeneous* if
for every $\bx \in \XX$ and for every $\lambda \in \RR_{++}$

$$
T(\lambda \bx) = \lambda T (\bx).
$$
```

```{prf:definition} Additive operator
:label: def-la-additive-operator

Let $\XX$ and $\YY$ be vector spaces. 
An operator $T : \XX \to \YY$ is called *additive* if
for every $\bx,\by \in \XX$

$$
T (\bx + \by) = T(\bx) + T(\by).
$$
```

```{prf:definition} Linear operator
:label: def-la-linear-operator

Let $\XX$ and $\YY$ be vector spaces. 
An operator $T : \XX \to \YY$ is called *linear* if
for every $\bx,\by \in \XX$ and for every $\lambda \in \RR$

$$
T (\lambda \bx + \by) = \lambda T(\bx) + T(\by).
$$
```
A linear operator is additive and homogeneous.
Linear operators are also known as linear transformations.
They are extensively developed in {ref}`sec:la:linear-transformations`.


## Affine Operators

```{prf:definition} Affine operator
:label: def-la-affine-operator

Let $\XX$ and $\YY$ be vector spaces. 
An operator $T : \XX \to \YY$ (on some field $\FF$) is called *affine* if
for every $\bx,\by \in \XX$ and for every $t \in \FF$

$$
T (t \bx + (1 - t) \by) = t T(\bx) + (1 - t) T(\by).
$$

An affine operator is also known as an *affine function*
or an *affine transformation*.
```


```{prf:theorem}
:label: res-la-op-affine-linear-p-offset

$T$ is affine if and only if the mapping $\bx \mapsto T(\bx) - T(\bzero)$
is linear.

In other words, an affine operator can be written as a linear
operator plus an offset.
```

```{prf:proof}
Let $T : \XX \to \YY$ be some mapping. Define:

$$
L (\bx) = T (\bx)  - T(\bzero).
$$

Assume $T$ to be affine. We shall show that $L$ is linear.

Let $\bx, \by \in \XX$ and $t \in \FF$. Then

$$
L(t\bx) &= T (t\bx) - T(\bzero)\\
&= T(t\bx + (1-t) \bzero) - T(\bzero)\\
&= t T(\bx) + (1-t)T(\bzero) - T(\bzero)\\
&= t (T(\bx) - T(\bzero)) = t L(\bx).
$$

$$
L (\bx + \by) &= T (\bx + \by)  - T(\bzero)\\
&= T(\frac{1}{2} 2 \bx + \frac{1}{2} 2 \by) - T(\bzero)\\
&= \frac{1}{2} T (2 \bx) + \frac{1}{2} T(2 \by) - T(\bzero)\\
&= \frac{1}{2} (T (2\bx) - T(\bzero)) + \frac{1}{2}( T(2\by) - T(\bzero))\\
&= \frac{1}{2} (L (2\bx)  + L (2\by))\\
&= \frac{1}{2} (2 L (\bx)  + 2 L (\by))\\
&= L(\bx) + L (\by).
$$
Thus, $L$ is linear.
Here, we used the fact that $L(2\bx) = T(2\bx) - T(\bzero)$
and $L$ was already shown to be homogeneous above giving 
$L(2\bx) = 2 L(\bx)$.


Now, assume $L$ to be linear. We shall show that $T$ is affine.


Let $\bx, \by \in \XX$ and $t \in \FF$. Then

$$
T (t \bx + (1 - t) \by) 
&= L (t \bx + (1 - t) \by) + T(\bzero)  \\
&= t L(\bx) + (1 -t) L (\by) + T(\bzero) \\
&= t L(\bx) + t T(\bzero) + (1 -t) L (\by) + (1-t)T(\bzero) \\
&= t (L (\bx) + T(\bzero)) + (1 -t) (L (\by) + T(\bzero))\\
&= tT (\bx) + (1- t) T(\by).
$$
Thus, $T$ is affine.
```

We show that affine functions distribute over
arbitrary affine combinations.

```{prf:theorem} Affine functions on affine combinations
:label: res-la-aff-func-aff-comb

Let $\XX$ and $\YY$ be vector spaces on a field $\FF$.
Let $T : \XX \to \YY$ be affine. 

Let $\bx_0, \bx_1, \dots, \bx_k \in \XX$ and 
$t_0, t_1, \dots, t_k \in \FF$ such that
$\sum_{i=0}^k t_i = 1$ where $1 \in \FF$.
Then,

$$
T \left ( \sum_{i=0}^k t_i \bx_i \right ) = \sum_{i=0}^k t_i T(\bx_i).
$$
```

```{prf:proof}

Define:

$$
L(\bx) = T(\bx)  - T(\bzero).
$$

We know that $L$ is linear. We have $T(\bx) = L(\bx) + T(\bzero)$.

Now,

$$
T \left ( \sum_{i=0}^k t_i \bx_i \right ) 
&= L \left ( \sum_{i=0}^k t_i \bx_i \right )  + T(\bzero)\\
&= \sum_{i=0}^k t_i L( \bx_i)  + T(\bzero)\\
&= \sum_{i=0}^k t_i L( \bx_i)  + (sum_{i=0}^k t_i) T(\bzero)\\
&= \sum_{i=0}^k t_i \left (L( \bx_i)  + T(\bzero) \right )\\
&= \sum_{i=0}^k t_i T( \bx_i).
$$
```
