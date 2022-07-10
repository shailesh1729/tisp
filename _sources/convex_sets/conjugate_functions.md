(sec:conjugate-functions)=
# Conjugate Functions

```{div}

Throughout this section, we assume that $\VV, \WW$ are 
real vector spaces. Wherever necessary, 
they are equipped with a
{prf:ref}`norm <def-la-norm>` $\| \cdot \|$
or an {prf:ref}`real inner product <def-la-real-inner-product>`
$\langle \cdot, \cdot \rangle$. 
They are also equipped with a metric $d(\bx, \by) = \| \bx - \by \|$
as needed.
$\VV^*$ denotes the dual vector space (to $\VV$).
```

## Definition and Properties

```{index} Conjugate function
```
```{prf:definition} Conjugate function
:label: def-cvxf-conjugate-function

Let $f : \VV \to \ERL$ be an extended real valued function. 
Its *conjugate function* $f^*: \VV^* \to \ERL$ is given by

$$
f^*(\by) = \underset{\bx \in \VV}{\sup} \{ \langle \bx, \by \rangle - f(\bx)\}
\Forall \by \in \VV^*.
$$ 
```

Note that the conjugate function is a mapping from the *dual* vector space
to extended real line.

Recall from {prf:ref}`def-cvxf-support-function` that
the support function of a set $C$ is given by

$$
\sigma_C (\bx) =  \sup_{\bz \in C} \langle \bz, \bx \rangle.
$$


### Indicator Functions

```{prf:theorem} Conjugate of an indicator function
:label: res-cvxf-conjugate-indicator-func

Let $C \subseteq \VV$ be a nonempty set. 
Let $I_C : \VV \to \RERL$ be the indicator function for the set $C$.
Then,

$$
I_C^*(\by) = \sigma_C (\by) = \underset{\bx \in C}{\sup} \langle \bx, \by \rangle. 
$$

In other words, the conjugate of the indicator function of a set
is the support function of the same set.
```

```{prf:proof}

Let $\by \in \VV*$ be arbitrary.

1. At any $\bx \in C$, we have
   
   $$
   \langle \bx, \by \rangle - I_C(\bx) = \langle \bx, \by \rangle. 
   $$
1. At any $\bx \notin C$, we have

   $$
   \langle \bx, \by \rangle - I_C(\bx) = -\infty. 
   $$
1. Since $C$ is nonempty, hence

   $$
   \underset{\bx \in \VV}{\sup} \{ \langle \bx, \by \rangle - f(\bx)\}
   = \underset{\bx \in C}{\sup} \langle \bx, \by \rangle.
   $$
   The result follows.
```

### Fenchel's Inequality

```{prf:theorem} Fenchel's inequality
:label: res-cvxf-conjugate-fenchel

Let $f: \VV \to \RERL$ be a proper function
and let $f^*$ be its conjugate function.
Then, for any $\bx \in \VV$ and $\by \in \VV^*$:

$$
f(\bx) + f^*(\by) \geq \langle \bx, \by \rangle.
$$
```
```{prf:proof}
We proceed as follows.

1. By definition

   $$
   f^*(\by) = \underset{\bx \in \VV}{\sup} 
   \{ \langle \bx, \by \rangle - f(\bx)\}.
   $$
1. Thus, for any $\bx \in \VV$ and any $\by \in \VV^*$,

   $$
   f^*(\by) \geq \langle \bx, \by \rangle - f(\bx).
   $$
1. Since $f$ is proper, hence $f(\bx) > -\infty$ for ever $\bx$.
1. Since $f$ is proper, hence there exists $\ba \in \VV$
   such that $f(\ba) < \infty$.
1. Then,
    
   $$
   f^*(\by) \geq \langle \ba, \by \rangle - f(\ba). 
   $$
1. The R.H.S. is a finite quantity.
1. Thus, $f^*(\by) > -\infty$ for every $\by$.
1. If either $f(\bx)$ or $f^*(\by)$ are $\infty$,
   then the Fenchel inequality is valid trivially.
1. When, both of them are finite, then the
   inequality $f^*(\by) \geq \langle \bx, \by \rangle - f(\bx)$
   simplifies to

   $$
   f(\bx) + f^*(\by) \geq \langle \bx, \by \rangle .
   $$
```

### Convexity and Closedness

```{prf:theorem} Convexity and closedness
:label: res-cvxf-conjugate-convex-closed

Let $f : \VV \to \RERL$ be an extended real valued function. 
Then, the conjugate function $f^*$ is closed and convex.    
```

```{prf:proof}
We note that for a fixed $\bx$, the function

$$
g_x(\by) =  \langle \bx, \by \rangle - f(\bx)
$$
is an affine function. 

1. Due to {prf:ref}`res-la-affine-finite-closed-func`,
   affine functions are closed.
1. Due to {prf:ref}`res-cvxf-affine-functional-convex`,
   affine functions are convex.
1. Thus, $g_x$ is indeed convex and closed for every $\bx$.
1. Thus, $f$ is a pointwise supremum of convex and closed functions.
1. By {prf:ref}`res-ms-ptws-sup-closed-functions-closed`, $f$ is closed.
1. By {prf:ref}`res-cvx-ptws-supremum`, $f$ is convex.
1. Thus, $f$ is closed and convex.
```

The beauty of this result is the fact that
The conjugate function is always closed and
convex even if the original function is not
convex or not closed.


### Properness

```{prf:theorem} Properness of conjugates of proper convex functions
:label: res-cvxf-proper-func-conjugate-proper

Let $f : \VV \to \RERL$ be a proper convex function.
Then, its conjugate $f^*$ is proper. 
```

```{prf:proof}
We are given that $f$ is a proper convex function.
We shall first show that $f*$ never attains $-\infty$.
We shall then show that $f^*$ is not $\infty$ everywhere. 

1. Since $f$ is proper, there exists $\ba \in \VV$ 
   such that $f(\ba) < \infty$.
1. By definition, for any $\by \in \VV^*$

   $$
   f^*(\by) \geq \langle \ba, \by \rangle - f(\ba).
   $$
1. The R.H.S. in this inequality is finite for every $\by \in \VV^*$.
1. Thus, $f^*(\by) > -\infty$ for every $\by$.
1. We also need to show that there exists $\by \in \VV^*$
   such that $f^*(\by) < \infty$.
1. Since $f$ is a proper convex function,
   hence by {prf:ref}`res-cvxf-subdiff-exist-relint`,
   there exists $\bx \in \dom f$ at which
   the subdifferential $\partial f(\bx)$ is nonempty.
1. Consider any $\by \in \partial f(\bx)$.
1. By subgradient inequality {eq}`eq-cvxf-subgradient-inequality`,

   $$
   f(\bz) \geq f(\bx) + \langle \bz - \bx, \by \rangle
   $$
   for every $\bz \in \VV$.
1. Thus,

   $$
   \langle \bz, \by \rangle - f(\bz)
   \leq \langle \bx, \by \rangle - f(\bx)
   \Forall \bz \in \VV.
   $$
1. The quantity $\langle \bx, \by \rangle - f(\bx)$ 
   on the R.H.S. is finite and fixed.
1. Taking supremum on the L.H.S., we obtain

   $$
   f^*(\by) = \sup_{\bz \in \VV} (\langle \bz, \by \rangle - f(\bz))
   \leq \langle \bx, \by \rangle - f(\bx).
   $$
1. Thus, $f^*(\by) < \infty$.
1. Thus, $f^*$ is a proper function.
```


## Biconjugate

```{div}
The conjugate of the conjugate is called the *biconjugate*. 
We recall that when $\VV$ is finite dimensional,
then the dual of the dual $\VV^**$
is isomorphic to $\VV$.
```

```{index} Biconjugate
```
```{prf:definition} Biconjugate
:label: def-cvxf-biconjugate-func

Let $f : \VV \to \ERL$ be an extended real valued function. 
Its *biconjugate function* $f^{**}: \VV \to \ERL$ is given by

$$
f^{**} (\bx) = \underset{\by \in \VV^*}{\sup} 
\{ \langle \bx, \by \rangle - f^*(\by)  \}, \quad \bx \in \VV.
$$
```

###  As Underestimators

```{prf:theorem} Biconjugate is an underestimator
:label: res-cvxf-biconjugate-underestimator

The biconjugate is an underestimator of the original function.

$$
f(\bx) \geq f^{**} (\bx) \Forall \bx \in \VV. 
$$
```

```{prf:proof}
We proceed as follows.

1. From the definition of the conjugate

   $$
   f^*(\by) \geq \langle \bx, \by \rangle - f(\bx)
   $$
   holds true for any $\bx \in \VV$ and $\by \in \VV^*$.
1. Rewriting, we get

   $$
   f(\bx) \geq \langle \bx, \by \rangle - f^*(\by).
   $$
1. Taking supremum over $\by \in \VV^*$ on the R.H.S.,

   $$
   f(\bx) \geq \sup_{\by \in \VV^*}
   (\langle \bx, \by \rangle - f^*(\by))
   = f^{**}(\bx).
   $$
```
Thus, the biconjugate of $f$ is always a lower bound for $f$.
Naturally, one is interested in conditions under which
biconjugate of $f$ equals $f$.

### Proper Closed and Convex Functions

```{prf:theorem} Biconjugate for proper closed and convex functions
:label: res-cvxf-biconjugate-proper-closed-convex

Let $f : \VV \to \RERL$ be a proper, closed and convex function. 
Then,

$$
f(\bx) = f^{**} (\bx) \Forall x \in \VV. 
$$

In other words, $f^{**} = f$. Or the biconjugate
of a proper closed and convex function is the function
itself.
```

```{prf:proof}
In {prf:ref}`res-cvxf-biconjugate-underestimator`,
we have already shown that $f^{**} \preceq f$.
We shall now show that $f \preceq f^{**}$ also
holds true when $f$ is proper, closed and convex. 


1. For contradiction, assume that there exists
   $\bx \in \VV$ such that
   $f^{**}(\bx) < f(\bx)$.
1. Thus, $(\bx, f^{**}(\bx)) \notin \epi f$.
1. Recall the definition of inner product for the
   direct sum space $\VV \oplus \RR$ from
   {prf:ref}`def-cvx-real-vector-space-r-prod`
   given by

   $$
   \langle (\bx, s), (\by, t) \rangle
   \triangleq \langle \bx, \by \rangle + st.
   $$
1. Since $f$ is proper, hence $\epi f$ is nonempty.
1. Since $f$ is closed, hence $\epi f$ is closed.
1. Since $f$ is convex, hence $\epi f$ is convex.
1. Thus, $\epi f$ is nonempty, closed and convex.
1. By strict separation theorem
   ({prf:ref}`res-cvxf-cl-convex-set-strict-separation`),
   the set $\epi f$ and the point $(\bx, f^{**}(\bx))$
   can be strictly separated.
1. There exists a point $(\ba, b)$ with $\ba \in \VV^*$, $b \in \RR$
   and a scalar $\alpha \in \RR$ such that

   $$
   \langle \bx, \ba \rangle + f^{**}(\bx) b > \alpha
   \text{ and }
   \langle \bz, \ba \rangle + s b \leq \alpha
   \Forall (\bz, s) \in \epi f. 
   $$
1. It is then easy to identify constants $c_1, c_2 \in \RR$
   such that

   $$
   \langle \bz, \ba \rangle + s b \leq c_1
   < c_2 \leq  \langle \bx, \ba \rangle + f^{**}(\bx) b
   \Forall (\bz, s) \in \epi f. 
   $$
   Pick $c_1 = \alpha$ and $c_2 = \langle \bx, \ba \rangle + f^{**}(\bx) b$
   for example. 
1. By simple arithmetic, we can conclude that

   $$
   \langle \bz - \bx, \ba \rangle + (s - f^{**}(\bx)) b
   \leq c_1 - c_2 \triangleq c < 0
   \Forall (\bz, s) \in \epi f. 
   $$
1. The scalar $b$ must be nonpositive.
   If for contradiction, $b > 0$, then fixing a $\bz$
   and increasing $s$ sufficiently, the inequality can be violated.
1. We now consider different cases for $b \leq 0$.
1. Consider the case where $b < 0$.
   1. Dividing the inequality by $-b$ and letting $\by = \frac{\ba}{-b}$,
      we obtain

      $$
      \langle \bz - \bx, \by \rangle - s + f^{**}(\bx) \leq \frac{c}{-b} < 0
      \Forall (\bz, s) \in \epi f.
      $$
   1. In particular, for $s = f(\bz)$, we have

      $$
      \langle \bz, \by \rangle - \langle \bx, \by \rangle 
      - f(\bz) + f^{**}(\bx) \leq \frac{c}{-b} < 0
      \Forall \bz \in \VV.
      $$
      This is valid for $\bz \notin \dom f$ also as in that case
      $s = f(\bz) = \infty$.
   1. Taking the supremum over $\bz$ on the L.H.S., we obtain

      $$
      f^*(\by) - \langle \bx, \by \rangle + f^{**}(\bx) 
      \leq \frac{c}{-b} < 0.
      $$
   1. This implies $f^*(\by) + f^{**}(\bx) < \langle \bx, \by \rangle$.
   1. This contradicts the Fenchel inequality.
   1. Thus, $b < 0$ is not possible.
1. Now consider the case where $b=0$.
   1. Since $f^*$ is proper, hence $\dom f^* \neq \EmptySet$.
   1. Take any $\widehat{\by} \in \dom f^*$.
   1. Pick some $\epsilon > 0$.
   1. Let $\widehat{\ba} = \ba + \epsilon \widehat{\by}$.
   1. Let $\widehat{b} = - \epsilon$.
   1. Then, for any $\bz \in \dom f$ with $s=f(\bz)$,

      $$
      \langle \bz - \bx, \widehat{\ba} \rangle + (f(\bz) - f^{**}(\bx)) \widehat{b}
      &= \langle \bz - \bx, \ba \rangle 
         + \langle \bz - \bx, \epsilon \widehat{\by} \rangle 
         - \epsilon (f(\bz) - f^{**}(\bx)) \\
      &= \langle \bz - \bx, \ba \rangle
         + \epsilon [\langle \bz - \bx, \widehat{\by} \rangle -f(\bz) + f^{**}(\bx)] \\
      &\leq c + \epsilon[\langle \bz, \widehat{\by} \rangle  - f(\bz) + f^{**}(\bx) - \langle \bx, \widehat{\by} \rangle]\\
      &\leq c + \epsilon [f^*(\widehat{\by}) + f^{**}(\bx) - \langle \bx, \widehat{\by} \rangle].
      $$
   1. Let $\widehat{c} = c + \epsilon [f^*(\widehat{\by}) + f^{**}(\bx) - \langle \bx, \widehat{\by} \rangle]$.
   1. Since $c < 0$, we can pick $\epsilon > 0$ small enough such that $\widehat{c} < 0$.
   1. Then, we have the inequality

      $$
      \langle \bz - \bx, \widehat{\ba} \rangle + (f(\bz) - f^{**}(\bx)) \widehat{b} \leq \widehat{c} < 0.
      $$
   1. We now have a situation similar to the case of $b < 0$. Here we have $\widehat{b} < 0$.
   1. Dividing both sides by $-\widehat{b}$ and letting $\tilde{\by} = \frac{\widehat{\ba}}{-\widehat{b}}$,
      we obtain

      $$
      \langle \bz, \tilde{\by} \rangle - f(\bz) 
      - \langle \bx, \tilde{\by} \rangle + f^{**}(\bx) 
      \leq - \frac{\widehat{c}}{\widehat{b}} < 0
      \Forall \bz \in \VV.
      $$
   1. Taking the supremum over $\bz$ on the L.H.S., we get

      $$
      f^*(\tilde{\by}) + f^{**}(\bx) < \langle \bx, \tilde{\by} \rangle.
      $$
   1. This again is a contradiction of Fenchel inequality.
1. Thus, $f^{**}(\bx) \geq f(\bx)$ must be true for every $\bx \in \dom f$.
```

### Indicator and Support Functions

```{prf:example} Indicator and support functions
:label: ex-cvxf-biconjucate-indicator-support

Let $C$ be a nonempty set.

1. By {prf:ref}`res-cvxf-conjugate-indicator-func`,

   $$
   I^*_C = \sigma_C.
   $$
1. The set $\closure \ConvexHull C$ is nonempty, closed and convex. 
1. We note that since $\closure \convex C$ is a nonempty, closed and convex set,
   hence $I_{\closure \convex C}$ is a closed and convex function.
1. By {prf:ref}`res-cvxf-conjugate-indicator-func`, we have

   $$
   I^*_{\closure \convex C} = \sigma_{\closure \convex C}
   $$
1. Then, by {prf:ref}`res-cvxf-biconjugate-proper-closed-convex`,

   $$
   \sigma^*_{\closure \convex C}
   = (I^*_{\closure \convex C})^*
   = I^{**}_{\closure \convex C}
   = I_{\closure \convex C}.
   $$
1. By {prf:ref}`res-cvxf-supp-closure-hull`,
  
   $$
   \sigma_C = \sigma_{\closure C}
   \text{ and }
   \sigma_C = \sigma_{\convex C}.
   $$
1. Combining
   
   $$
   \sigma_C = \sigma_{\closure \convex C}.
   $$
1. Thus, we have
   
   $$
   \sigma^*_C = \sigma^*_{\closure \convex C}
   = I_{\closure \convex C}.
   $$
1. If $C$ is nonempty, closed and convex, then
   
   $$
   \closure \convex C = C.
   $$
1. In this case,

   $$
   \sigma^*_C =  I_C.
   $$

Summary:

For a nonempty, closed and convex set $C \subseteq \VV$, 

$$
\sigma^*_C = I_C.
$$

For an arbitrary nonempty set $C \subseteq \VV$, 

$$
\sigma^*_C = I_{\closure \ConvexHull C}.
$$
```

### Max Function

```{prf:example} Conjugate for max function
:label: ex-cvxf-conjugate-max-function

Let $f : \RR^n \to \RR$ be given by

$$
f(\bx) \triangleq \max \{x_1, x_2, \dots, x_n \}.
$$

We can rewrite it as

$$
f(\bx) = \underset{\by \in \Delta_n}{\sup} \langle \by, \bx \rangle
= \sigma_{\Delta_n} (x)
$$
where $\Delta_n$ is the unit simplex in $\RR^n$.
1. Recall from {prf:ref}`def-convex-unit-simplex` that
   
   $$
    \Delta_n \triangleq \{\bx \in \RR^n 
        \ST \langle \bx, \bone \rangle = 1, \bx \succeq \bzero \}.
   $$
1. In other words, for every $\by \in \Delta_n$,
   $y_i \geq 0$ and $\sum y_i = 1$.
1. $\langle \by, \bx \rangle = \sum_{i=1}^n y_i x_i$.
1. For $\by \in \Delta_n$, this represents the weighted average
   of the components of $\bx$.
1. The supremum value of the weighted average occurs when 
   $y_i$ corresponding to the largest component of $\bx$ is 1
   and all remaining $y_j$ are 0.
1. This provides the justification of the formula above.

We recall that $\Delta_n$ is a nonempty, closed and convex set.
Then, following {prf:ref}`ex-cvxf-biconjucate-indicator-support`,
the conjugate of max function $f$ is 

$$
f^* = \delta_{\Delta_n}.
$$
```

## Conjugate Calculus


### Separable functions

```{prf:theorem} Conjugate for separable functions
:label: res-cvxf-conjugate-separable

Let $g: \VV_1 \oplus \VV_2 \oplus \dots \oplus \VV_p \to \RERL$ be given by 

$$
g(\bx_1, \bx_2, \dots, \bx_p) = \sum_{i=1}^p f_i (\bx_i)
$$
where $f_i : \VV_i \to \RERL$ are proper functions.
Then: 

$$
g^*(\by_1, \by_2, \dots, \by_p) = 
\sum_{i=1}^p f_i^*(\by_i) \Forall \by_i \in \VV_i^*, 1 \leq i \leq p.
$$
```

```{prf:proof}
Let $\by = (\by_1, \dots, \by_p) \in \VV^*_1 \oplus \dots \oplus \VV^*_p$.

Then,

$$
g^*(\by)
&= g^*(\by_1, \dots, \by_p) \\
&= \sup_{\bx_1, \dots, \bx_p} \{ 
    \langle (\bx_1, \dots, \bx_p), (\by_1, \dots, \by_p) \rangle
    - g(\bx_1, \dots, \bx_p)\} \\
&= \sup_{\bx_1, \dots, \bx_p} \left \{
    \sum_{i=1}^p \langle \bx_i, \by_i \rangle
    - \sum_{i=1}^p f_i(\bx_i) \right \} \\
&= \sum_{i=1}^p \sup_{\bx_i} \{ \langle \bx_i, \by_i \rangle - f_i(\bx_i) \} \\
&= \sum_{i=1}^p f^*_i(\bx_i).
$$
```

### Affine Transformations

```{prf:theorem} Invertible affine transformation
:label: res-cvxf-conjugate-affine-trans-inv

Let $f : \VV \to \RERL$ be an extended real valued function.
Let $\bAAA : \WW \to \VV$ be an invertible linear transformation.
Let $\ba \in \WW$, $\bb \in \WW^*$ and $c \in \RR$. 
Consider the function $g: \WW \to  \RERL$ given by:

$$
g(\bx) \triangleq f\left (\bAAA (\bx - \ba) \right ) + \langle \bx, \bb \rangle + c
\Forall \bx \in \WW.
$$

Then the convex conjugate of $g$ is given by:

$$
g^*(\by) = f^*\left ((\bAAA^T)^{-1} (\by - \bb) \right ) 
+ \langle \by, \ba \rangle 
- \langle \bb, \ba \rangle - c
\Forall \by \in \WW^*.
$$
```

```{prf:proof}
We introduce a variable $\bz = \bAAA (\bx - \ba)$.
1. We can see that $\bz  = \bAAA \bx - \bAAA \ba$.
1. Thus, $\bx \mapsto \bz$ is an affine transformation.
1. Since $\bAAA$ is invertible, hence this affine transformation is also invertible.
1. Also, by invertibility of $\bAAA$, $\bx = \bAAA^{-1}(\bz) + \ba$.

Now, for any $\by \in \WW^*$, 

$$
g^*(\by) &= \sup_{\bx \in \WW} \{ \langle \bx, \by \rangle - g(\bx) \} \\
&=  \sup_{\bx } \{ \langle \bx, \by \rangle - 
f\left (\bAAA (\bx - \ba) \right ) - \langle \bx, \bb \rangle - c \} \\
&=  \sup_{\bz} \{ \langle \bAAA^{-1}(\bz) + \ba, \by \rangle - 
f (\bz) - \langle \bAAA^{-1}(\bz) + \ba, \bb \rangle - c \} \\
&=  \sup_{\bz} \{ \langle \bAAA^{-1}(\bz), \by - \bb \rangle - 
f (\bz) + \langle \ba, \by \rangle - \langle \ba, \bb \rangle - c \} \\
&=  \sup_{\bz} \{ \langle \bz, (\bAAA^{-1})^T(\by - \bb) \rangle - 
f (\bz) + \langle \ba, \by \rangle - \langle \ba, \bb \rangle - c \} \\
&= f^* \left ( (\bAAA^{-1})^T(\by - \bb) \right )
+ \langle \ba, \by \rangle - \langle \ba, \bb \rangle - c\\
&= f^* \left ( (\bAAA^T)^{-1}(\by - \bb) \right )
+ \langle \by, \ba \rangle - \langle \bb, \ba \rangle - c\\
$$

In this derivation, we have used following facts

1. $(\bAAA^T)^{-1} = (\bAAA^{-1})^T$.
1. $\langle \bx, \by \rangle = \langle \by, \bx \rangle$.
1. $\langle \bA (\bx), \by \rangle = \langle \bx, \bA^T (\by) \rangle$.
```


### Scaling

```{prf:theorem} Scaling
:label: res-cvxf-conjugate-scaling

Let $f : \VV \to \RERL$ be an extended real valued function.
Let $\alpha > 0$.

1. The conjugate of the function $g(\bx) = \alpha f(\bx)$ is given by:

   $$
   g^*(\by) = \alpha f^*\left (\frac{\by}{\alpha} \right ) \Forall \by \in \VV^*.
   $$
1. The conjugate of the function $h(\bx) = \alpha f(\frac{\bx}{\alpha})$ is given by:

   $$
   h^*(\by) = \alpha f^*(\by) \Forall \by \in \VV^*.
   $$ 
```

```{prf:proof}
(1) For any $\by \in \VV^*$

$$
g^*(\by) &= \sup_{\bx \in \VV} \{ \langle \bx, \by \rangle - g(\bx) \} \\
&= \sup_{\bx} \{ \langle \bx, \by \rangle - \alpha f(\bx) \} \\
&= \alpha \sup_{\bx} \{ \langle \bx, \frac{\by}{\alpha} \rangle - \alpha f(\bx) \} \\
&= \alpha f^*\left ( \frac{\by}{\alpha} \right ).
$$

(2) Similarly, for any $\by \in \VV^*$

$$
h^*(\by) &= \sup_{\bx \in \VV} \{ \langle \bx, \by \rangle - h(\bx) \} & \\
&= \sup_{\bx \in \VV} \{ \langle \bx, \by \rangle - \alpha f(\frac{\bx}{\alpha}) \} & s\\
&= \alpha \sup_{\bx \in \VV} 
\left \{ \left \langle \frac{\bx}{\alpha}, \by \right \rangle 
- f\left (\frac{\bx}{\alpha} \right ) \right \} & \\
&= \alpha \sup_{\bz \in \VV} \{ \langle \bz, \by \rangle - f(\bz) \} 
    & \bz \triangleq \frac{\bx}{\alpha} \\
&= \alpha f^*(\by).
$$
```

## Subgradients



```{prf:theorem} Conjugate subgradient theorem
:label: res-cvxf-conjugate-subgradient

Let $f : \VV \to \RERL$ be proper and convex. 
The following statements are equivalent for any $\bx \in \VV$
and $\by \in \VV^*$:

1. $\langle \by, \bx \rangle = f(\bx) + f^*(\by)$.
2. $\by \in \partial f(\bx)$.

If $f$ is closed, then 1 and 2 are equivalent to:

3.. $\bx \in \partial f^*(\by)$.
```

```{prf:proof}
$\by \in \partial f(\bx)$ is true if and only if

$$
f(\bz) \geq f(\bx) + \langle \bz - \bx , \by \rangle 
\Forall \bz \in \VV.
$$
This is equivalent to

$$
\langle \bx , \by \rangle  - f(\bx) \geq 
\langle \bz , \by \rangle  - f(\bz)
\Forall \bz \in \VV.
$$
Taking this supremum over $\bz$ on the R.H.S.,
we see that this is equivalent to

$$
\langle \bx , \by \rangle  - f(\bx) \geq f^*(\by).
$$
By Fenchel's inequality {prf:ref}`res-cvxf-conjugate-fenchel`,

$$
f(\bx) + f^*(\by) \geq \langle \bx, \by \rangle.
$$

Thus, the previous inequality must be an equality, giving us

$$
f(\bx) + f^*(\by) = \langle \bx, \by \rangle.
$$

This establishes the equivalence between (1) and (2).

We now assume that $f$ is closed. 
Thus $f$ is proper, closed and convex.
Due to {prf:ref}`res-cvxf-biconjugate-proper-closed-convex`

$$
f^{**} = f.
$$

Then (1) is equivalent to 

$$
g^*(\bx) + g(\by) = \langle \bx, \by \rangle.
$$
where $g = f^*$.

Then applying the equivalence between (1)
and (2) for the function $g$, we see that

$$
\bx \in \partial g(\by) = \partial f^*(\by).
$$
```


```{prf:corollary} Conjugate subgradient theorem - second formulation
:label: res-cvxf-conjugate-subgradient-2

Let $f : \VV \to \RERL$ be a proper, closed and convex function. 
Then for any $\bx \in \VV$ and $\by \in \VV^*$:

$$
\partial f(\bx) = \argmax_{\bu \in \VV^*} 
\{ \langle \bx, \bu \rangle - f^*(\bu) \}
$$

and 

$$
\partial f^*(\by) = \argmax_{\bv \in \VV} 
\{ \langle \bv, \by \rangle - f(\bv) \}.
$$
```

```{prf:proof}

We proceed as follows.

1. Let $\by \in \dom \partial f^*$ and $\bx \in \partial f^*(\by)$.
1. Then by {prf:ref}`res-cvxf-conjugate-subgradient`,
   it is equivalent to
   
   $$
   f^*(\by) = \langle \bx, \by \rangle - f(\bx).
   $$
1. By definition of the conjugate function

   $$
   f^*(\by) = \sup_{\bv \in \VV} \{ \langle \bv, \by \rangle  - f(\bv) \}.
   $$
1. since the supremum is attained at $\bx$, hence this is equivalent to

   $$
   \bx \in \argmax_{\bv \in \VV} \{ \langle \bv, \by \rangle  - f(\bv) \}.
   $$
1. Hence

   $$
   \partial f^*(\by) = \argmax_{\bv \in \VV} \{ \langle \bv, \by \rangle  - f(\bv) \}.
   $$
1. Similarly, let $\bx \in \partial f$ and $\by \in \partial f(\bx)$.
1. Following similar argument, this is equivalent to

   $$
   \by \in \argmax_{\bu \in \VV^*} \{ \langle \bx, \bu \rangle  - f^*(\bu) \}.
   $$
1. Hence

   $$
   \partial f(\bx) = \argmax_{\bu \in \VV^*} \{ \langle \bx, \bu \rangle  - f^*(\bu) \}.
   $$
```

### Lipschitz Continuity

Recall that {prf:ref}`res-cvxf-subdiff-bounded-lipschitz-continuous`
shows the equivalence between the boundedness of the subgradients
of a function $f$ over a set $X$ and the Lipschitz continuity
of $f$ over $X$.
A similar result is available in terms of the boundedness
of the domain of the conjugate.

```{prf:theorem} Lipschitz continuity and boundedness of the domain of the conjugate
:label: res-cvxf-lipschitz-cont-bounded-conjugate

Let $f: \VV \to \RR$ be convex. Then the following statements are equivalent
for a constant $L > 0$.

1. $| f(\bx) - f(\by) | \leq L \| \bx - \by \|$ for any $\bx, \by \in \VV$.
1. $ \| \bg \|_* \leq L$ for any $\bg \in \partial f(\bx)$ where $\bx \in \VV$.
1. $\dom f^* \subseteq B_{\| \cdot \|_*} [\bzero, L]$.
```

```{prf:proof}
The equivalence between (1) and (2) follows from
{prf:ref}`res-cvxf-subdiff-bounded-lipschitz-continuous`.

We first show that (3) $\implies$ (2)

1. Assume that (3) holds true.
1. By conjugate subgradient theorem ({prf:ref}`res-cvxf-conjugate-subgradient-2`),
   for any $\bx \in \VV$,

   $$
   \partial f(\bx) = \argmax_{\by \in \VV^*} 
   \{ \langle \bx, \by \rangle - f^*(\by) \}.
   $$
1. The maximum on the R.H.S. can be attained only at points where $f^*(\by) < \infty$.
1. Thus if $\by \in \partial f(\bx)$ then $f^*(\by) < \infty$ must hold true.
1. Thus $\partial f(\bx) \subseteq \dom f^*$ for every $\bx \in \VV$.
1. By hypothesis (3) $\partial f(\bx) \subseteq B_{\| \cdot \|_*} [\bzero, L]$
   for every $\bx \in \VV$.
1. Hence $\bg \in B_{\| \cdot \|_*} [\bzero, L]$ for every $\bg \in \partial f(\bx)$
   for every $\bx \in \VV$.
1. Hence $\| \bg \|_* \leq L$ for every $\bg \in \partial f(\bx)$
   for every $\bx \in \VV$..

In the reverse direction, we will show that (1) $\implies$ (3)

1. Towards this, we shall show that if (1) is true then
   for any $\bz \in \VV^*$, 
   if $\| \bz \|_* > L$ then $\bz \notin \dom f^*$.
1. By hypothesis (1), for every $\bx \in \VV$,

   $$
   f(\bx) - f(\bzero) \leq |f(\bx) - f(\bzero) | \leq L \| \bx \|.
   $$
1. Rearranging

   $$
   -f(\bx) \geq - f(\bzero) - L \| \bx \|
   $$
   holds true for every $\bx \in \VV$.
1. Then for any $\by \in \VV^*$

   $$
   f^*(\by) &= \sup_{\bx \in \VV} \{\langle \bx, \by \rangle - f(\bx) \} \\
   &\geq \sup_{\bx \in \VV} \{\langle \bx, \by \rangle - f(\bzero) - L \| \bx \| \}.
   $$
1. Pick any $\bz \in \VV^*$ satisfying $\| \bz \|_* > L$.
1. Pick a vector $\bu \in \VV$ such that $\| \bu \| = 1$ and 
   $\langle \bu, \bz \rangle = \| \bz \|_*$. 
   Such a vector exists by definition of dual norm.
1. Consider the ray $C = \{ t \bu \ST t \geq 0 \} \subseteq \VV$.
1. Continuing with the inequality for $f^*$ for $\by = \bz$ 

   $$
   f^*(\bz) &\geq \sup_{\bx \in \VV} \{\langle \bx, \bz \rangle - f(\bzero) - L \| \bx \| \}\\
   &\geq \sup_{\bx \in C} \{\langle \bx, \bz \rangle - f(\bzero) - L \| \bx \| \}\\
   &= \sup_{t \geq 0} \{\langle t \bu, \bz \rangle - f(\bzero) - L t \| \bu \| \}\\
   &= \sup_{t \geq 0} \{t \| \bz \|_* - f(\bzero) - L t \}\\
   &= \sup_{t \geq 0} \{t (\| \bz \|_* - L)  - f(\bzero) \}\\
   &= \infty
   $$
   since $\| \bz \|_* > L$.
1. Hence $\bz \notin \dom f^*$.
1. Hence for any $\by \in \dom f^*$ we have $\| \by \|_* \leq L$.
1. Hence $\dom f^* \subseteq B_{\| \cdot \|_*} [\bzero, L]$ as desired.
```





## 1-dim Functions


```{prf:theorem} Exponent
:label: res-cvxf-conjugate-exponent

Let $f : \RR \to \RR$, be given by $f(x) = e^x$.
Then, the conjugate is given by:

$$
f^*(y) = \begin{cases}
y \ln y - y, & y \geq 0, \\
\infty, & \text{ otherwise }.
\end{cases}
$$

```


```{prf:proof}
To see this, we proceed as follows:

$$
f^*(y) &= \sup_{x \in \RR} \{ x y - f(x) \} \\
&= \sup_{x \in \RR} \{ x y - e^x \}.
$$

1. If $y < 0$, then the supremum value is $\infty$
   as $x \to -\infty$.
1. If $y = 0$, then the supremum value is $0$ 
   as $x \to -\infty$.
1. If $y > 0$, then the unique maximizer is obtained
   by differentiating $x y - e^x$ w.r.t. $x$
   giving us $y = e^{\tilde{x}}$ or $\tilde{x} = \ln y$.
1. Then, the supremum value for $y > 0$ is $y \ln y - y$.
1. Under the convention that $y \ln y = 0$ when $y = 0$,
   we see that $y \ln y - y = 0$ for $y = 0$.
1. Thus, $f^*(y) = y \ln y - y$ for $y \geq 0$.
1. $f^*(y) = \infty$ otherwise. 
```

```{prf:theorem} Negative log
:label: res-cvxf-conjugate-negative-log

Let $f : \RR \to (-\infty,\infty]$ be given by: 

$$
f(x) = \begin{cases}
- \ln (x) & x > 0 \\
\infty &  x \leq 0
\end{cases}.
$$

Then, the conjugate is:

$$
f^*(y) = \begin{cases}
-1 - \ln (-y) & y < 0 \\
\infty & y \geq 0
\end{cases}.
$$
```


```{prf:proof}
To show this, we proceed as follows:

$$
f^*(y) &= \sup_{x > 0} \{ xy - f(x) \} \\
&= \sup_{x > 0} \{ xy + \ln (x) \}. 
$$

1. If $y \geq 0$, then the supremum value is $\infty$.
1. If $y < 0$, then we can differentiate the expression
   $xy + \ln (x)$ and set it to 0 to obtain the optimal solution.

   $$
   \frac{d}{d x} (x y + \ln(x)) = y + \frac{1}{x}.
   $$
1. Setting it to zero, we get $\tilde{x} = - \frac{1}{y}$.
1. The supremum value is thus $-1 - \ln(-y)$.
```

```{prf:theorem} Hinge loss
:label: res-cvxf-conjugate-hinge-loss

Let $f : \RR \to \RR$ be given by:

$$
f(x) = \max \{1 - x, 0 \}
$$

Then, the conjugate is:

$$
f^*(y) = y + I_{[-1,0]} (y) \Forall y \in \RR
$$
where $I$ is the indicator function.
```


```{prf:proof}
To see this, note that

$$
f^*(y) &= \sup_{x} \{ xy - f(x) \} \\
&= \sup_{x} [ xy - \max \{1 - x, 0 \} ] \\
&= \sup_{x} [ \min \{xy - (1-x), xy \} ] \\
&= \sup_{x} [ \min \{(1+y)x - 1, yx \} ].
$$

1. The terms $(1+y)x - 1$ and $yx$ are affine in $x$
   representing straight lines.
1. The two lines intersect at 

   $$
   & (1+y)x - 1 = y x \\
   & \implies x - 1 = 0 \\
   & \implies x = 1.
   $$
1. For $x < 1$,  $(1+y)x - 1 < y x$.
1. For $x > 1$, $(1+y)x - 1 > y x$.
1. Thus, the function $ \min \{(1+y)x - 1, y x \}$ is a piece-wise linear function
   of $x$.

   $$
   \min \{(1+y)x - 1, y x \} = \begin{cases}
   (1+y)x - 1, & x < 1 \\
   y x, & x \geq 1.
   \end{cases}
   $$
1. The first piece is a line $(1+y)x - 1$ with slope $1+y$ over $x \in (-\infty, 1]$.
1. The second piece is a line $y x$ with slope $y$ over $x \in [1, \infty)$.
1. A finite supremum of this piecewise linear function exists if
   the slope of the left piece is nonnegative and the slope
   of the right piece is nonpositive. 
1. In other words, $1 + y \geq 0$  and $y \leq 0$. 
1. Thus, a finite supremum exists only for $y \in [-1, 0]$.
1. The supremum value for this range of $y$ values is attained at $x=1$
   (where the two pieces intersect) and the supremum value equals $y$. 
1. For all $y \notin [-1, 0]$ the supremum is infinite.
1. Thus, $\dom f^* = [-1,0]$ and $f^*(y) = y \Forall y \in \dom f^*$.
1. $f^*(y) = \infty \Forall y \notin [-1,0]$.
1. This is succinctly represented in the expression for $f^*$ with the
   help of an indicator function above.
```


```{prf:theorem} p-th power of absolute value for $p > 1$.
:label: res-cvxf-conjugate-abs-pth-power

Let for some $p > 1$, the function $f : \RR \to \RR$ be given by:

$$
f(x) = \frac{1}{p} | x |^p
$$

Then, its conjugate is:

$$
f^*(y) = \frac{1}{q} | y |^q \quad \Forall y \in \RR
$$

where $q > 1$ is the conjugate exponent satisfying: 

$$
\frac{1}{p} + \frac{1}{q} = 1.
$$
```


```{prf:proof}
To see this, we proceed as follows:

1. The conjugate is given by

   $$
   f^*(y) = \sup_{x} \{ x y - f (x) \}
   = \sup_x \{x y -  \frac{1}{p} | x |^p \}.
   $$
1. The concave function $xy - \frac{1}{p} | x |^p$ is differentiable.

   $$
   \frac{d}{d x} (xy - \frac{1}{p} | x |^p) = y - \sgn (x) | x |^{p - 1}.
   $$
1. Setting the derivative to $0$, the points at which the derivative
   vanishes are given by

   $$
   y - \sgn (\tilde{x}) | \tilde{x} |^{p - 1} = 0.
   $$
1. We can rewrite this as 

   $$
   y = \sgn(y) | y | = \sgn (\tilde{x}) | \tilde{x} |^{p - 1}.
   $$
1. Therefore, $\sgn (y) = \sgn (\tilde{x})$ and
   $| \tilde{x} |^{p - 1} = | y|$.
1. Thus, 

   $$
   \tilde{x} = \sgn (\tilde{x}) |\tilde{x} | = \sgn (y)| y|^{\frac{1}{p - 1}}.
   $$
1. Accordingly, the supremum value at $\tilde{x}$ is

   $$
   f^*(y) &= \tilde{x} y - \frac{1}{p} | \tilde{x} |^p \\
   &= |y|^{1 + \frac{1}{p - 1}} - \frac{1}{p}| y|^{\frac{p}{p - 1}} \\
   &= |y|^{\frac{p}{p - 1}} - \frac{1}{p}| y|^{\frac{p}{p - 1}} \\
   &= \left (1 - \frac{1}{p} \right ) | y|^{\frac{p}{p - 1}} \\
   &= \frac{1}{q} | y|^q
   $$
   where $q = \frac{p}{p -1}$ is the conjugate exponent of $p$.
```


```{prf:theorem} p-th power of absolute value for $0 < p < 1$
:label: res-cvxf-conjugate-abs-pth-power-lt-1

Let for some $0 < p < 1$, $f : \RR \to \RR$ be given by:

$$
f(x) = \begin{cases}
- \frac{1}{p} x^p &  x \geq 0 \\
\infty & x < 0
\end{cases}.
$$

Then, its conjugate is:

$$
f^*(y) = \begin{cases}
- \frac{(-y)^q}{q}  &  y < 0 \\
\infty & \text{ otherwise }
\end{cases}
$$

where $q < 0$ is a negative number satisfying: 

$$
\frac{1}{p} + \frac{1}{q} = 1.
$$
```


```{prf:proof}
To see this, we proceed as follows:

1. The conjugate is given by

   $$
   f^*(y) = \sup_{x} \{ x y - f (x) \}
   = \sup_{x \geq 0} \{x y +  \frac{1}{p} x^p \}.
   $$
1. Define $ g : \RR \to \RR$ with $\dom g = \RR_+$

   $$
   g(x) \triangleq x y +  \frac{1}{p} x ^p.
   $$
1. When $y \geq 0$,  then $g(x) \to \infty$ as $x \to \infty$.
1. When $y < 0$, then $g'(x) = 0$ at $x = \tilde{x} = (-y)^{\frac{1}{p -1}}$.
1. We note that $g$ is a concave function for $y < 0$.
1. Thus, $g$ achieves its supremum at $\tilde{x}$.
1. The supremum value is given by

   $$
   f^*(y) &= g(\tilde{x}) \\
   &= \tilde{x} y +  \frac{1}{p} \tilde{x}^p \\
   &= (-y)^{\frac{1}{p -1}} y + \frac{1}{p} (-y)^{\frac{p}{p -1}} \\
   &= - (-y)^{\frac{p}{p -1}} + \frac{1}{p} (-y)^{\frac{p}{p -1}} \\
   &= - \left (1 - \frac{1}{p} \right ) (-y)^{\frac{p}{p -1}} \\
   &= - \frac{1}{q} (-y)^{q}
   $$
   where $q = \frac{p}{p -1}$.
1. The domain of $f^*$ is $y < 0$.
```

## n-dim functions

### Quadratics


```{prf:theorem} Strictly convex quadratic
:label: res-cvxf-conjugate-strictly-convex-quadratic

Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) \triangleq \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c 
$$

where $A \in \SS^n_{++}$, $\bb \in \RR^n$ and $c \in \RR$. 

Then, the conjugate is:

$$
f^*(\by) = \frac{1}{2}(\by - \bb)^T \bA^{-1}(\by -\bb) - c.
$$
```


```{prf:proof}
We proceed as follows. For any $\by \in \RR^n$,

$$
f^*(\by) &= \sup_{\bx} \{ \langle \bx, \by \rangle - f(\bx) \} \\
&= \sup_{\bx} \{ \by^T \bx - \frac{1}{2} \bx^T \bA \bx - \bb^T \bx - c \} \\
&= \sup_{\bx} \{ - \frac{1}{2} \bx^T \bA \bx - (\bb - \by)^T \bx - c \}.
$$
1. The supremum of the quadratic above is achieved at $\bx = \bA^{-1}(\by - \bb)$.
1. The supremum value is $\frac{1}{2}(\by - \bb)^T \bA^{-1}(\by -\bb) - c$.
```


```{prf:theorem} Convex quadratic
:label: res-cvxf-conjugate-convex-quadratic

Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) \triangleq \frac{1}{2} \bx^T \bA \bx + \bb^T \bx + c 
$$

where $A \in \SS^n_{+}$, $\bb \in \RR^n$ and $c \in \RR$. 

Then, the conjugate is:

$$
f^*(\by) = \begin{cases}
\frac{1}{2}(\by - \bb)^T \bA^{\dag}(\by -\bb) - c & \by \in \bb + \range \bA,\\
\infty & \text{ otherwise }.
\end{cases}
$$
```

```{prf:proof}
In this case, $\bA$ is not positive definite but only semidefinite.

For any $\by \in \RR^n$,

$$
f^*(\by) &= \sup_{\bx} \{ \langle \bx, \by \rangle - f(\bx) \} \\
&= \sup_{\bx} \{ \by^T \bx - \frac{1}{2} \bx^T \bA \bx - \bb^T \bx - c \} \\
&= \sup_{\bx} \{ - \frac{1}{2} \bx^T \bA \bx + (\by - \bb)^T \bx - c \}.
$$

1. Define $g : \RR^n \to \RR$ as

   $$
   g(\bx) = - \frac{1}{2} \bx^T \bA \bx + (\by - \bb)^T \bx - c.
   $$
1. Then,

   $$
   f^*(\by) = \sup_{\bx} g(\bx).
   $$
1. The gradient of $g$ is given by $\nabla g(\bx) = - \bA \bx + (\by - \bb)$.
1. The maximizers of $g$ are at points where the gradient vanishes, given by
   $\bA \bx = \by - \bb$.
1. This system has a solution if and only if $\by \in \range \bA + \bb$.
1. If $\by \in \range \bA + \bb$, we can choose one of the solutions
   to the zero gradient equation above. 
1. One possible solution is given by the Moore-Penrose pseudo inverse of $\bA$,
   namely $\tilde{\bx} = \bA^{\dag} (\by - \bb)$.
1. For this solution,
 
   $$
   f^*(\by) &= - \frac{1}{2} \tilde{\bx}^T \bA \tilde{\bx} + (\by - \bb)^T \tilde{\bx} - c \\
   &= - \frac{1}{2} (\by - \bb)^T \bA^{\dag} \bA \bA^{\dag} (\by - \bb) + (\by - \bb)^T \bA^{\dag} (\by - \bb) - c\\
   &=  \frac{1}{2} (\by - \bb)^T \bA^{\dag} (\by - \bb) - c.
   $$
   We used the fact that $(\bA^{\dag})^T = \bA^{\dag}$ since $\bA$ is symmetric.
   Also, $\bA^{\dag} \bA \bA^{\dag} = \bA^{\dag}$.
1. We now consider the case where $\by \notin \range \bA + \bb$.
1. This is same as $\by - \bb \notin \range \bA$.
1. Recall that $\range \bA = (\nullspace \bA)^{\perp}$.
1. Thus, $\by - \bb \notin (\nullspace \bA)^{\perp}$.
1. Thus, there exists a vector $\bv \in \nullspace \bA$ such that
   $(\by - \bb)^T \bv > 0$.
1. Now, for any $t \in \RR$, 

   $$
   g(t \bv) &= - \frac{1}{2} \bx^T \bA \bx + (\by - \bb)^T \bx - c \\
   &= - \frac{t^2}{2} \bv^T \bA \bv + t (\by - \bb)^T \bv - c \\
   &= t (\by - \bb)^T \bv - c
   $$
   since $\bA \bv = \bzero$.
1. Since $(\by - \bb)^T \bv > 0$, hence $g(t \bv) \to \infty$ as $t \to \infty$.
1. Thus,  $f^*(\by) = \sup_{\bx} g(\bx) = \infty$ if $\by \notin \range \bA + \bb$.
1. Thus, $\dom f^* = \range \bA + \bb$.
```

### Entropy

```{prf:theorem} Negative entropy
:label: res-cvxf-conjugate-negative-entropy

Let $f : \RR^n \to \RERL$ be given by:

$$
f(\bx) \triangleq \begin{cases}
\sum_{i=1}^n x_i \ln (x_i) & \bx \succeq \bzero,\\
\infty & \text{ otherwise }.
\end{cases}
$$

Then, the conjugate is:

$$
f^*(\by) = \sum_{i=1}^n e^{y_i - 1}.
$$
```
```{prf:proof}
We note that the function $f(\bx)$ is separable over
the components of $\bx$. Thus, it is enough to
compute the conjugate of the scalar function
$g : \RR \to \RR$ defined as

$$
g(t) = \begin{cases} 
t \ln t & \Forall t \geq 0, \\
\infty & \text{ otherwise }.
\end{cases}
$$
We can then apply {prf:ref}`res-cvxf-conjugate-separable`
to compute the conjugate of $f$.

Now,

$$
g^*(s) &= \sup_{t} \{ st - g(t) \} \\
&= \sup_{t \geq 0} \{ st - t \ln t \}.
$$

It is easy to see that the supremum of the expression
$st - t \ln t$ is achieved at $t = e^{s - 1}$.
Thus,

$$
g^*(s) = s e^{s - 1} - (s - 1) e^{s - 1} = e^{s - 1}.
$$

Finally,

$$
f(\bx) = \sum_{i=1}^n g(x_i).
$$
Thus, due to {prf:ref}`res-cvxf-conjugate-separable`,

$$
f^*(\by) = \sum_{i=1}^n g^* (y_i) = \sum_{i=1}^n e^{y_i - 1}.
$$
```


```{prf:theorem} Negative sum of logs
:label: res-cvx-conjugate-neg-sum-logs

Let $f : \RR^n \to \RERL$ be given by:

$$
f(\bx) \triangleq \begin{cases}
- \sum_{i=1}^n \ln (x_i) & \bx \succ \bzero,\\
\infty & \text{ otherwise }.
\end{cases}
$$

Then, the conjugate is:

$$
f^*(\by) =  \begin{cases}
- n - \sum_{i=1}^n \ln(-y_i) & \by \prec \bzero, \\
\infty & \text{ otherwise}.
\end{cases}
$$
```

```{prf:proof}
$f$ is separable. Define $g : \RR \to \RR$ as

$$
g(t) = \begin{cases}
- \ln t & t > 0, \\
\infty & t \leq 0.
\end{cases}
$$

Then,

$$
f(\bx)  = \sum_{i=1}^n g(x_i).
$$

By {prf:ref}`res-cvxf-conjugate-negative-log`,

$$
g^*(y) = \begin{cases}
-1 - \ln (-y) & y < 0 \\
\infty & y \geq 0
\end{cases}.
$$

Due to {prf:ref}`res-cvxf-conjugate-separable`,

$$
f^*(\by) = \sum_{i=1}^n g^*(y_i).
$$

For $\by \prec \bzero$

$$
f^*(\by) = \sum_{i=1}^n  (- 1 - \ln (-y_i))
= -n - \sum_{i=1}^n \ln (-y_i).
$$

For $\by \succeq \bzero$, one of the $g^*(y_i) = \infty$. Hence, $f^*(\by) = \infty$.
```

```{prf:theorem} Negative entropy over unit simplex
:label: res-cvxf-conjugate-neg-entropy-unit-simplex

Let $f : \RR^n \to \RERL$ be given by:

$$
f(\bx) \triangleq \begin{cases}
\sum_{i=1}^n x_i \ln x_i & \bx \in \Delta_n\\
\infty & \text{ otherwise }
\end{cases}.
$$


The conjugate is:

$$
f^*(\by) =  \ln \left ( \sum_{j=1}^n e^{y_j}
    \right )
$$
```
Recall from {prf:ref}`def-convex-unit-simplex` that a
unit simplex in $\RR^n$ is the set of
nonnegative vectors with elements
summing up to $1$. 

$$
\Delta_n = \{\bx \in \RR^n 
    \ST \langle \bx, \bone \rangle = 1, \bx \succeq \bzero \}.
$$


```{prf:proof}

For any $\by \in \RR^n$, 

$$
f^*(\by) &= \sup_{\bx}  \{ \langle \bx, \by \rangle - f(\bx)\}\\
&= \sup_{\bx} \left \{ \sum_{i=1}^n y_i x_i - \sum_{i=1}^n x_i \ln x_i \ST
\sum_{i=1}^n x_i = 1, x_1, \dots, x_n \geq 0 \right \}.
$$

This maximization problem is equivalent to the
minimization problem discussed later in
{prf:ref}`ex-opt-unit-simplex-1`.
The optimal solution is given by

$$
x_i^* = \frac{e^{y_i}}{\sum_{j=1}^n e^{y_j}} \Forall i = 1,\dots,n.
$$
Accordingly, the optimal (supremum) value
(following {prf:ref}`ex-opt-unit-simplex-1`) is

$$
f^*(\by) = \ln \left ( \sum_{i=1}^n e^{y_i} \right ).
$$
In other words, the conjugate of the negative entropy
function is the log-sum-exp function.
```



```{prf:theorem} Log sum exp
:label: res-cvxf-conjugate-log-sum-exp

Let $f : \RR^n \to \RR$ be given by:

$$
f(\bx) \triangleq \ln \left ( \sum_{j=1}^n e^{x_j}
    \right ).
$$

The conjugate is:

$$
f^*(\by) =  \begin{cases}
\sum_{i=1}^n y_i \ln y_i & \by \in \Delta_n\\
\infty & \text{ otherwise }
\end{cases}.
$$
```

```{prf:proof}
Following {prf:ref}`res-cvxf-conjugate-neg-entropy-unit-simplex`,
$f = g^*$ where $g$ is the negative entropy over the
unit simplex function.
Since $g$ is proper, closed and convex, hence
due to {prf:ref}`res-cvxf-biconjugate-proper-closed-convex`,

$$
f^* = g^{**} = g.
$$
```


Log-sum-exp and negative entropy over simplex and conjugate
of each other.


### Norms


```{prf:theorem} Norm
:label: res-cvxf-conjugate-norm

Let $f : \VV \to \RR$ be given by

$$
f(\bx) = \| \bx \|
$$

Then, the conjugate $f^* : \VV^* \to \RERL$ for any $\by \in \VV^*$
is given by:

$$
f^*(\by) = I_{B_{\| \cdot \|_*}[\bzero, 1]}
= \begin{cases}
0 & \| \by \|_* \leq 1 \\
\infty & \text{ otherwise }.
\end{cases}
$$

In other words, it is the indicator function for the unit ball
w.r.t. the dual norm $\| \cdot \|_*$.
```

```{prf:proof}
We proceed as follows.

1. By {prf:ref}`res-cvxf-support-unit-ball`, the support
   function for a closed unit ball of a norm is its dual
   norm.
1. Thus,

   $$
   \sigma_{B_{\| \cdot \|_*}[\bzero, 1]} = \| \cdot \| = f.
   $$
   Here, we have used the fact that the dual norm of the dual norm
   is the norm itself.
1. By {prf:ref}`ex-cvxf-biconjucate-indicator-support`,
   for a nonempty, closed and convex set $C \subseteq \VV$, 

   $$
   \sigma^*_C = I_C.
   $$
1. The set $B_{\| \cdot \|_*}[\bzero, 1]$ is nonempty,
   closed and convex.
1. Hence,
 
   $$
   f^* = \sigma^*_{B_{\| \cdot \|_*}[\bzero, 1]}
   = I_{B_{\| \cdot \|_*}[\bzero, 1]}.
   $$
```

```{prf:theorem} Squared norm
:label: res-cvxf-conjugate-squared-norm

Let $f : \VV \to \RR$ be given by

$$
f(\bx) = \frac{1}{2}\| \bx \|^2
$$

Then, the conjugate $f^* : \VV^* \to \RERL$ for any $\by \in \VV^*$
is given by:

$$
f^*(\by) = \frac{1}{2} \| \by \|_*^2.
$$
```

```{prf:proof}
We proceed as follows

1. By definition of the conjugate

   $$
   f^*(\by) =  \sup_{\bx \in \VV}\left \{ 
      \langle \bx, \by \rangle - \frac{1}{2}\| \bx \|^2 \right \}.
   $$
1. Consider the set $S_t = \{ \bx \in \RR \ST \| \bx \|  = t \}$.
1. Then, we can write $\VV = \bigcup_{t \geq 0} S_t$.
1. Define 
  
  $$
  g_t(\by) = \sup_{\bx \in S_t}\left \{ 
   \langle \bx, \by \rangle - \frac{1}{2}\| \bx \|^2 \right \}
  = \sup_{\bx \ST \| \bx \|  = t} \left \{ 
   \langle \bx, \by \rangle - \frac{1}{2}t^2 \right \}.
  $$

1. Then it is easy to see that

   $$
   f^*(\by) = \sup_{t \geq 0}g_t(\by).
   $$
1. In other words, we transform the maximization (for conjugate)
   into a double maximization as

   $$
   f^*(\by) = \sup_{t \geq 0} \sup_{\bx \ST \| \bx \| = t}
   \left \{ \langle \bx, \by \rangle - \frac{1}{2}t^2 \right \}.
   $$
1.  Now

    $$
    g_t(\by) &= \sup_{\bx \ST \| \bx \|  = t}
    \left \{ \langle \bx, \by \rangle - \frac{1}{2}t^2 \right \}\\
    &= \sup_{\bx \ST \| \bx \|  = t}
    \{ \langle \bx, \by \rangle \} - \frac{1}{2}t^2 \\
    &= t \| \by \|_* - \frac{1}{2}t^2.
    $$
1. Hence

   $$
   f^*(\by) = \sup_{t \geq 0}g_t(\by)
   = \sup_{t \geq 0} \left ( t \| \by \|_* - \frac{1}{2}t^2 \right ).
   $$
1. Differentiating $g_t(\by)$ w.r.t. $t$ and setting it to zero,
   we obtain

   $$
   \| \by \|_* - t^* = 0
   $$
1. Evaluating $g_t(\by)$ at $t^* = \| \by \|_*$, we get

   $$
   f^*(\by) = \| \by \|_*^2 -  \frac{1}{2} \| \by \|_*^2 
   = \frac{1}{2} \| \by \|_*^2.
   $$
```



```{prf:theorem} Ball-pen
:label: res-cvxf-conjugate-ball-pen

Let $f : \VV \to \RERL$ be given by

$$
f(\bx) \triangleq \begin{cases}
- \sqrt{1 - \| x \|^2} & \| x \| \leq 1\\
\infty & \text{ otherwise }.
\end{cases}
$$

Then, the conjugate $f^* : \VV^* \to \RERL$ for any $\by \in \VV^*$
is given by:

$$
f^*(\by) = \sqrt{\| y \|_*^2 + 1}.
$$

Generalizing further, let $f_{\alpha}$ for some $\alpha > 0$ be defined as

$$
f_{\alpha}(\bx) \triangleq \begin{cases}
- \sqrt{\alpha^2 - \| x \|^2} & \| x \| \leq \alpha\\
\infty & \text{ otherwise }.
\end{cases}
$$

The conjugate is given by:

$$
f_{\alpha}^*(\by) = \alpha \sqrt{\| y \|_*^2 + 1}.
$$
```

```{prf:proof}
We shall use the double maximization approach here.


$$
f^*(\by) &= \sup \left \{
   \langle \bx, \by \rangle + \sqrt{1 - \| x \|^2} \ST \| \bx \| \leq 1 
   \right \} \\
&= \sup_{t \in [0,1]} \sup_{\bx \ST \| \bx \| = t}
\left \{ \langle \bx, \by \rangle + \sqrt{1 - t^2} \right \} \\
&= \sup_{t \in [0,1]} \left \{ 
   t \| \by \|_* + \sqrt{1 - t^2}
   \right \}.
$$

Introduce

$$
g(t) = t \| \by \|_* + \sqrt{1 - t^2}.
$$

Differentiating w.r.t. $t$ and setting the derivative to 0, we get

$$
& \| \by \|_* - \frac{ t }{\sqrt{1-t^2}} = 0 \\
\implies & \| \by \|_* = \frac{ t }{\sqrt{1-t^2}} \\
\implies & \| \by \|_*^2 = \frac{ t^2 }{1-t^2} \\
\implies & 1 + \| \by \|_*^2 = \frac{1 }{1-t^2} \\
\implies & \frac{1}{1 + \| \by \|_*^2} = 1-t^2 \\
\implies & 1 - \frac{1}{1 + \| \by \|_*^2} = t^2 \\
\implies & \frac{\| \by \|_*^2}{1 + \| \by \|_*^2} = t^2 \\
\implies & t^* = \frac{\| \by \|_*}{\sqrt{1 + \| \by \|_*^2}}.
$$
Since $t \in [0,1]$ hence only the positive square root is considered.
It is easy to see that $t^* \in [0,1]$.

Putting back the value of $t^*$ into $f^*(\by)$,

$$
f^*(\by) &=
 \frac{\| \by \|_*^2}{\sqrt{1 + \| \by \|_*^2}}
   + \sqrt{1 - \frac{\| \by \|_*^2}{1 + \| \by \|_*^2}} \\
&=  \frac{\| \by \|_*^2}{\sqrt{1 + \| \by \|_*^2}} + 
\frac{1}{\sqrt{1 + \| \by \|_*^2}} \\
&= \frac{1 + \| \by \|_*^2}{\sqrt{1 + \| \by \|_*^2}} \\
&= \sqrt{1 + \| \by \|_*^2}.
$$

Next, we note that

$$
f_{\alpha} (\bx) = \alpha f\left ( \frac{\bx}{\alpha} \right ).
$$

Applying {prf:ref}`res-cvxf-conjugate-scaling`,

$$
f^*_{\alpha} (\bx) = \alpha f^*(\by) = \alpha \sqrt{1 + \| \by \|_*^2}.
$$
```



```{prf:theorem} $\sqrt{t^2 + \| \cdot \|^2}$
:label: res-cvxf-conjugate-ball-pen-ext

Let $g_t : \VV \to \RR$  for some $\alpha > 0$ be given by:

$$
g_t (\bx) = \sqrt{t^2 + \| x \|^2}.
$$

Then the conjugate is given by:

$$
g_{t}^*(\by) = \begin{cases}
-t \sqrt{1 - \| y \|_*^2} & \| y \|_* \leq 1\\
\infty & \text{ otherwise }
\end{cases}.
$$
```

```{prf:proof}
We proceed as follows.

1. Define $g(\bx) = \sqrt{1 + \|\bx \|^2}$.
1. We can see that $g_t(\bx) = t g \left ( \frac{\bx}{t} \right)$.
1. By {prf:ref}`res-cvxf-conjugate-ball-pen`,
   $g = f^*$ where $f$ is the ball-pen function given by

   $$
   f(\by) = \begin{cases}
   - \sqrt{1 - \| \by \|_*^2} & \| \by \|_* \leq 1\\
   \infty & \text{ otherwise }.
   \end{cases}
   $$
1. We note that $f$ is proper, closed and convex function.
1. By {prf:ref}`res-cvxf-biconjugate-proper-closed-convex`

   $$
   g^* = f^{**} = f.
   $$
1. Thus,

   $$
   g^* (\by) = \begin{cases}
   - \sqrt{1 - \| \by \|_*^2} & \| \by \|_* \leq 1\\
   \infty & \text{ otherwise }.
   \end{cases}
   $$
1. Applying {prf:ref}`res-cvxf-conjugate-scaling`,

   $$
   g_t^*(\by) = t g^*(\by) = \begin{cases}
   - t \sqrt{1 - \| \by \|_*^2} & \| \by \|_* \leq 1\\
   \infty & \text{ otherwise }.
   \end{cases}
   $$
```


