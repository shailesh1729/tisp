# Dictionaries II

This section continues the development of
dictionaries for sparse and redundant representations.

(sec:dic:dirac_dct_dictionary)=
## Dirac-DCT dictionary

````{prf:definition}
:label: def:dic:dirac_dct_dictionary

The Dirac-DCT dictionary is a two-ortho dictionary consisting of 
the union of the Dirac and the DCT bases.
````
This dictionary is suitable for real signals since both
Dirac and DCT are totally real bases $\in \RR^{N \times N}$. 

The dictionary is obtained by combining the $N \times N$ identity matrix
(Dirac basis)
with the $N \times N$ DCT matrix for signals in $\RR^N$.

Let $\Psi_{\text{DCT}, N}$ denote the DCT matrix for $\RR^N$.
Let $\bI_N$ denote the identity matrix for $\RR^N$. 
Then

$$
\bDDD_{\text{DCT}} = \begin{bmatrix}
\bI_N & \Psi_{\text{DCT}, N}
\end{bmatrix}.
$$
Let

$$
\Psi_{\text{DCT}, N} = \begin{bmatrix}
\psi_1 & \psi_2 & \dots & \psi_N
\end{bmatrix}
$$
The $k$-th column of $\Psi_{\text{DCT}, N}$ is given by

```{math}
:label: eq:dict:dct_matrix_kth_column

\psi_k(n) = \sqrt{\frac{2}{N}} \Omega_k \cos \left (\frac{\pi}{2 N} (2 n - 1) (k - 1) \right ), n = 1, \dots, N,
```
with $\Omega_k = \frac{1}{\sqrt{2}}$ for $k=1$
and $\Omega_k = 1$ for $2 \leq k \leq N$. 

Note that for $k=1$, the entries become

$$
\sqrt{\frac{2}{N}} \frac{1}{\sqrt{2}} \cos 0 = \sqrt{\frac{1}{N}}.
$$
Thus, the $\ell_2$ norm of $\psi_1$ is 1.
We can similarly verify the $\ell_2$ norm of other columns also.
They are all one.

````{prf:theorem}
:label: res:dic:dirac_dct_dictionary_coherence

The Dirac-DCT dictionary has coherence $\sqrt{\frac{2}{N}}$.
````
````{prf:proof}
The coherence of a two ortho basis where one basis is Dirac basis is given by the
magnitude of the largest entry in the other basis.

1. For $\Psi_{\text{DCT}, N}$, the largest value is obtained when $\Omega_k = 1$
    and the $\cos$ term evaluates to 1. 
1. Clearly, 
   
   $$
    \mu (\bDDD_{\text{DCT}}) = \sqrt{\frac{2}{N}}.
   $$
````


````{prf:theorem}
:label: res:dic:dirac_dct_dictionary_babel

The $p$-Babel function for Dirac-DCT dictionary is given by

$$
\mu_p(k) = k^{\frac{1}{p}} \mu \Forall 1\leq k \leq N.
$$
In particular, the standard Babel function
is given by

$$
\mu_1(k) = k\mu
$$
````
````{prf:proof}
TODO prove it.
````


