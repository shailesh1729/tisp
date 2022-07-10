# Sequences

```{index} Sequence
```
````{prf:definition} Sequence
:label: def-st-sequence

Let $A$ be a set.
Any function $x : \Nat \to A$, where $\Nat = \{1,2,3,\dots\}$ is the set of natural numbers,
is called a *sequence* of $A$.

We say that $x(n)$ denoted by $x_n$ is the $n^{\text{th}}$ *term in the sequence*.
We denote the sequence by $ \{ x_n \}$.

We also write the sequence as:

$$
\{ x_1, x_2, \dots, \}.
$$

We can assign a symbol to a sequence as:

$$
X \triangleq \{ x_1, x_2, \dots, \}.
$$
````


Note that sequence may have repeated elements and the 
order of elements in a sequence is important.
Tuples (like $(a,b,c,d)$) are also ordered but they are finite length.
Sequences are ordered and of infinite 
(but countable) length.

```{prf:remark}
We shall abuse the notation and use $X$ to denote
both the sequence $\{x_n \}$ and the set of 
elements in the sequence. Thus, $X$ as a set
is a subset of $A$. By $x \in X$, we shall 
mean that there exists a $k \in \Nat$ such that
$x$ is the k-th element of the sequence $X = \{ x_n \}$.
```

```{index} Sequence; eventual satisfaction
```
````{prf:definition} Eventually
:label: def-st-sequence-eventual-satisfaction

We say that a sequence $\{ x_n \}$ of a set $A$ satisfies a property $(P)$
*eventually* if there exists some natural number $n_0$ such that $x_n$ satisfies
the property $(P)$ for all $n > n_0$.
````

```{prf:example}
:label: ex-st-seq-property-eventually-1

Consider the sequence $\{ x_n = \frac{1000}{n} \}$.
For all $n > 1000$, it satisfies the property that
$x_n < 1$.
```

```{index} Subsequence
```
````{prf:definition} Subsequence
:label: def-st-sub-sequence

A *subsequence* of a sequence $\{ x_n \}$ is a sequence
$\{ y_n \}$ for which there exists a strictly increasing sequence
$\{ k_n \}$ of natural numbers (i.e. $1 \leq k_1 < k_2  < k_3 < \ldots)$
such that $y_n = x_{k_n}$ holds for each $n$.
````

