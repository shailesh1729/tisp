# Sequences

````{prf:definition} Sequence
:label: def-st-sequence

Any function $x : \Nat \to X$, where $\Nat = \{1,2,3,\dots\}$ is the set of natural numbers,
is called a *sequence* of $X$.

We say that $x(n)$ denoted by $x_n$ is the $n^{\text{th}}$ *term in the sequence*.
We denote the sequence by $ \{ x_n \}$.

````

Note that sequence may have repeated elements and the 
order of elements in a sequence is important.
Tuples (like $(a,b,c,d)$) are also ordered but they are finite length.
Sequences are ordered and of infinite length.

````{prf:definition} Subsequence
:label: def-st-sub-sequence

A *subsequence* of a sequence $\{ x_n \}$ is a sequence
$\{ y_n \}$ for which there exists a strictly increasing sequence
$\{ k_n \}$ of natural numbers (i.e. $1 \leq k_1 < k_2  < k_3 < \ldots)$
such that $y_n = x_{k_n}$ holds for each $n$.
````

