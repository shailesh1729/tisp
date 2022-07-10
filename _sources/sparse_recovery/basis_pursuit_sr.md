# Basis Pursuit


## Introduction

We recall following sparse recovery problems in compressive sensing.
For simplicity, 
we assume the sparsifying dictionary to be the Dirac basis
(i.e. $\bDDD = \bI$ and $N  = D$).
Further, we assume signal $\bx$ to be $K$-sparse in $\CC^N$.
With the sensing matrix $\Phi$ and the measurement vector $\by$,
the CS sparse recovery problem in the
absence of measurement noise (i.e. $\by = \Phi \bx$) is stated as:

````{math}
:label: eq:bp:cs_noiseless_recovery

\widehat{\bx} = \text{arg } \underset{\bx \in \CC^N}{\min} 
\| \bx \|_0 \text{ subject to } \by = \Phi \bx.
````
In the presence of measurement noise (i.e. $\by = \Phi \bx + \be$),
the recovery problem takes the form of

````{math}
:label: eq:bp:cs_sparse_recovery_sparsity_bound

\widehat{\bx} 
= \text{arg } \underset{\bx \in \CC^N}{\min} 
\| \by - \Phi \bx \|_2\text{ subject to }  \| \bx \|_0 \leq K.
````
when a bound on sparsity is provided, or alternatively:

````{math}
:label: eq:bp:cs_sparse_recovery_error_bound

\widehat{\bx} = \text{arg } \underset{\bx \in \CC^N}{\min} 
\| \bx \|_0 \text{ subject to }  \| \by - \Phi \bx \|_2 \leq \epsilon.
````
when a bound on the measurement noise is provided.
