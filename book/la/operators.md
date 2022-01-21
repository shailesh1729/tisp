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

```{prf:definition} Affine operator
:label: def-la-affine-operator

Let $\XX$ and $\YY$ be vector spaces. 
An operator $T : \XX \to \YY$ (on some field $\FF$) is called *affine* if
for every $\bx,\by \in \XX$ and for every $\lambda \in \FF$

$$
T (\lambda \bx + (1 - \lambda) \by) = \lambda T(\bx) + (1 - \lambda) T(\by).
$$
```


```{prf:remark}
$T$ is affine if and only if the mapping $\bx \mapsto T(\bx) - T(\bzero)$
is linear.
```

