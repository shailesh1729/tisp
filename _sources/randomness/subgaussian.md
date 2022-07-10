(sec:randomness:subgaussian)=
# Subgaussian Distributions

In this section we review subgaussian distributions and
matrices drawn from subgaussian distributions.

Examples of subgaussian distributions include


*  Gaussian distribution
*  Rademacher distribution taking values $\pm \frac{1}{\sqrt{M}}$
*  Any zero mean distribution with a bounded support



````{prf:definition}
:label: def-random-subgaussian

A random variable $X$ is called *subgaussian* if there exists a constant $c > 0$ such that

```{math}
:label: eq:sub_gaussian_definition

M_X(t)  = \EE [\exp(X t) ] \leq \exp \left (\frac{c^2 t^2}{2} \right )
```
holds for all $t \in \RR$.
We use the notation  $X \sim \Sub (c^2)$ to denote that $X$ satisfies the 
constraint {eq}`eq:sub_gaussian_definition`.
We also say that $X$ is $c$-subgaussian.
````

$\EE [\exp(X t) ]$ is moment generating function of $X$.

$\exp \left (\frac{c^2 t^2}{2} \right )$ is moment generating function
of a Gaussian random variable with variance $c^2$.

The definition means that for a subgaussian variable $X$,
its M.G.F. is bounded by the M.G.F. of a Gaussian random variable
$\sim \NNN(0, c^2)$.

````{prf:example} Gaussian r.v. as subgaussian r.v.
:label: ex-random-subgaussian-1

Consider zero-mean Gaussian random variable $X \sim \NNN(0, \sigma^2)$
with variance $\sigma^2$.
Then 

$$
\EE [\exp(X t) ] = \exp\left ( \frac{\sigma^2 t^2}{2} \right ).
$$
Putting $c = \sigma$
we see that {eq}`eq:sub_gaussian_definition` is satisfied.
Hence $X\sim \Sub(\sigma^2)$ is a subgaussian r.v.
or $X$ is $\sigma$-subgaussian.
````

````{prf:example} Rademacher distribution
:label: ex-random-subgaussian-2

Consider $X$ with 

$$
\PP_X(x) = \frac{1}{2}\delta(x-1) + \frac{1}{2}\delta(x + 1) 
$$
i.e. $X$ takes a value $1$ with probability $0.5$ and value $-1$ with probability $0.5$.

Then 

$$
\EE [\exp(X t) ] = \frac{1}{2} \exp(-t) + \frac{1}{2} \exp(t)
= \cosh t \leq \exp \left ( \frac{t^2}{2} \right).
$$

Thus $X \sim \Sub(1)$ or $X$ is 1-subgaussian.
````

````{prf:example} Uniform distribution
:label: ex-random-subgaussian-3

Consider $X$ as uniformly distributed over the interval $[-a, a]$
for some $a > 0$. i.e.

$$
f_X(x) = \begin{cases}
\frac{1}{2 a} & -a \leq x \leq a\\
0 & \text{otherwise}
\end{cases}
$$
Then

$$
\EE [\exp(X t) ]
= \frac{1}{2 a}  \int_{-a}^{a} \exp(x t)d x 
=  \frac{1}{2 a t}  [e^{at} - e^{-at}]
= \sum_{n = 0}^{\infty}\frac{(at)^{2 n}}{(2 n + 1)!}
$$
But $(2n+1)! \geq n! 2^n$.
Hence we have

$$
\sum_{n = 0}^{\infty}\frac{(at)^{2 n}}{(2 n + 1)!} 
\leq \sum_{n = 0}^{\infty}\frac{(at)^{2 n}}{( n! 2^n)} 
= \sum_{n = 0}^{\infty}\frac{(a^2 t^2 / 2)^{n}}{( n!)} 
= \exp \left (\frac{a^2 t^2}{2} \right ).
$$
Thus

$$
\EE [\exp(X t ]  \leq \exp \left ( \frac{a^2 t^2}{2} \right ).
$$

Hence $X \sim \Sub(a^2)$ or $X$ is $a$-subgaussian.
````

````{prf:example} Random variable with bounded support
:label: ex-random-subgaussian-4

Consider $X$ as a zero mean, bounded random variable i.e.

$$
\PP(|X| \leq B) = 1 
$$
for some $B \in \RR^+$
and

$$
\EE(X) = 0.
$$
Then, the following upper bound holds:

$$
\EE [ \exp(X t) ] 
=  \int_{-B}^{B} \exp(x t) f_X(x) d x 
\leq \exp\left (\frac{B^2 t^2}{2} \right ).
$$

This result can be proven with some advanced calculus. 
$X \sim \Sub(B^2)$ or $X$ is $B$-subgaussian.
````

There are some useful properties of subgaussian random variables.

````{prf:lemma} Mean and variance of subgaussian random variables
:label: res-prob-subgaussian-mean-var

If $X \sim \Sub(c^2)$ then

$$
\EE (X) = 0
$$
and

$$
\EE(X^2) \leq c^2.
$$
````
Thus subgaussian random variables are always zero-mean.
Their variance is always bounded by the variance of the bounding Gaussian distribution.

````{prf:proof}
We proceed as follows:

1. Note that

    $$
      \sum_{n = 0}^{\infty} \frac{t^n}{n!} \EE (X^n)
      = \EE \left( \sum_{n = 0}^{\infty} \frac{(X t)^n}{n!} \right ) 
      = \EE \left ( \exp(X t) \right ).
    $$
1. But since $X \sim \Sub(c^2)$ hence
    
    $$
      \sum_{n = 0}^{\infty} \frac{t^n}{n!} \EE (X^n) 
      \leq \exp \left ( \frac{c^2 t^2}{2} \right) = 
      \sum_{n = 0}^{\infty} \frac{c^{2 n} t^{2 n}}{2^n n!}.
    $$
1. Restating
    
    $$
      \EE (X) t + \EE (X^2) \frac{t^2}{2!} 
      \leq \frac{c^2 t^2}{2} + \smallO (t^2) \text{ as } t \to 0.
    $$
1. Dividing throughout by $t > 0$ and letting $t \to 0$ we get $\EE (X) \leq 0$.
1. Dividing throughout by $t < 0$ and letting $t \to 0$ we get $\EE (X) \geq 0$. 
1. Thus $\EE (X) = 0$. So $\Var(X) = \EE (X^2)$.
1. Now we are left with
    
    $$
     \EE (X^2) \frac{t^2}{2!} 
     \leq \frac{c^2 t^2}{2} + \smallO (t^2) \text{ as } t \to 0.
    $$
1. Dividing throughout by $t^2$ and letting $t \to 0$ we get  $\Var(X) \leq c^2$.
````
Subgaussian variables have a linear structure.


````{prf:theorem} Linearity of subgaussian variables
:label: res-prob-subgaussian-linear

If $X \sim \Sub(c^2)$ i.e. $X$ is $c$-subgaussian, 
then for any $\alpha \in \RR$, the
r.v. $\alpha X$ is $|\alpha| c$-subgaussian.

If $X_1, X_2$ are r.v. such that $X_i$ is
$c_i$-subgaussian, then 
$X_1 + X_2$ is $c_1 + c_2$-subgaussian.
````

````{prf:proof}
Scalar multiplication:

1. Let $X$ be $c$-subgaussian.
1. Then
    
    $$
      \EE [\exp(X t) ] \leq \exp \left (\frac{c^2 t^2}{2} \right ).
    $$
1. Now for $\alpha \neq 0$, we have
    
    $$
    \EE [\exp(\alpha X t) ] \leq \exp \left (\frac{\alpha^2 c^2 t^2}{2} \right )
    \leq \exp \left (\frac{(|\alpha | c)^2 t^2}{2} \right ).
    $$
1. Hence $\alpha X$ is $|\alpha| c$-subgaussian.

Addition:

1. Consider $X_1$ as $c_1$-subgaussian and $X_2$ as $c_2$-subgaussian.
1. Thus
    
    $$
      \EE (\exp(X_i t) ) \leq \exp \left (\frac{c_i^2 t^2}{2} \right ).
    $$
1. Let $p, q >1 $ be two numbers s.t. $\frac{1}{p} + \frac{1}{q} = 1$.
1. Using  H\"older's inequality, we have
    
    $$
    \EE (\exp((X_1  + X_2)t) ) 
    &\leq 
    \left [ \EE (\exp(X_1 t) )^p\right ]^{\frac{1}{p}}
    \left [ \EE (\exp(X_2 t) )^q\right ]^{\frac{1}{q}}\\
    &= 
    \left [ \EE (\exp( p X_1 t) )\right ]^{\frac{1}{p}}
    \left [ \EE (\exp(q X_2 t) )\right ]^{\frac{1}{q}}\\
    &\leq
    \left [ \exp \left (\frac{(p c_1)^2 t^2}{2} \right ) \right ]^{\frac{1}{p}}
    \left [ \exp \left (\frac{(q c_2)^2 t^2}{2} \right ) \right ]^{\frac{1}{q}}\\
    &= \exp \left ( \frac{t^2}{2} ( p c_1^2 + q c_2^2) \right ) \\
    &= \exp \left ( \frac{t^2}{2} ( p c_1^2 + \frac{p}{p - 1} c_2^2) \right ).
    $$
1. Since this is valid for any $p > 1$, we can minimize the r.h.s. 
   over $p > 1$.
1. If suffices to minimize the term

   $$
    r = p c_1^2 + \frac{p}{p - 1} c_2^2.
    $$
1. We have 
    
    $$
    \frac{\partial r}{\partial p} = c_1^2 - \frac{1}{(p-1)^2}c_2^2.
    $$
1. Equating it to 0 gives us
    
    $$
    p - 1 = \frac{c_2}{c_1}
    \implies p = \frac{c_1 + c_2}{c_1}
    \implies \frac{p}{p -1} = \frac{c_1 + c_2}{c_2}.
    $$
1. Taking second derivative, we can verify that this is indeed a minimum value.
1. Thus
    
    $$
    r_{\min} = (c_1 + c_2)^2.
    $$
1. Hence we have the result

    $$
    \EE (\exp((X_1  + X_2)t) ) 
    \leq
    \exp \left (\frac{(c_1+ c_2)^2 t^2}{2} \right ).
    $$
1. Thus $X_1 + X_2$ is $(c_1 + c_2)$-subgaussian.
````

If $X_1$ and $X_2$ are independent, then 
$X_1 + X_2$ is $\sqrt{c_1^2 + c_2^2}$-subgaussian.


If $X$ is $c$-subgaussian then naturally, $X$ is $d$-subgaussian
for any $d \geq c$.
A question arises as to what is the minimum
value of $c$ such that $X$ is $c$-subgaussian. 

````{prf:definition} Subgaussian moment
:label: def-prob-subgaussian-moment

For a centered random variable $X$, the *subgaussian moment*
of $X$, denoted by $\sigma(X)$, is defined as

$$
\sigma(X) = \inf \left \{ c \geq 0 \; |  \;
\EE (\exp(X t) ) \leq \exp \left (\frac{c^2 t^2}{2} \right ), \Forall t \in \RR.
 \right \}
$$
$X$ is subgaussian if and only if $\sigma(X)$ is finite.
````

We can also show that $\sigma(\cdot)$ is a norm on the
space of subgaussian random variables.
And this normed space is complete.

For centered Gaussian r.v. $X \sim \NNN(0, \sigma^2)$, 
the subgaussian moment coincides with the standard deviation.
$\sigma(X) = \sigma$.

Sometimes it is useful to consider more restrictive class of subgaussian random variables.

````{prf:definition} Strictly subgaussian distribution
:label: def-prob-strict-subgaussian

A random variable $X$ is called *strictly subgaussian*
if $X \sim \Sub(\sigma^2)$ where
$\sigma^2 =  \EE(X^2)$, i.e. the inequality

$$
\EE (\exp(X t) ) \leq \exp \left (\frac{\sigma^2 t^2}{2} \right ) 
$$
holds true for all $t \in \RR$. 

We will denote strictly subgaussian variables by $X \sim \SSub (\sigma^2)$.
````

````{prf:example} Gaussian distribution
:label: ex-prob-strict-subgaussian-1

If $X \sim \NNN (0, \sigma^2)$ then $X \sim \SSub(\sigma^2)$.
````


## Characterization

We quickly review Markov's inequality which will help us establish
the results in this subsection.

````{div}
Let $X$ be a non-negative random variable. And let $t > 0$. Then

$$
\PP (X \geq t ) \leq \frac{\EE (X)}{t}.
$$
````

````{prf:theorem}
:label: res-prob-subgaussian-charac

For a centered random variable $X$, the following statements are 
equivalent:

1. moment generating function condition:

   $$
    \EE [\exp(X t) ] 
    \leq \exp \left (\frac{c^2 t^2}{2} \right ) \Forall t \in \RR.
   $$
1. Subgaussian tail estimate: There exists $a > 0$ such that 
   
   $$
    \PP(|X| \geq \lambda) 
    \leq 2 \exp (- a \lambda^2) \Forall \lambda > 0.
   $$
1. $\psi_2$-condition: There exists some $b > 0$ such that
   
   $$
    \EE [\exp (b X^2) ] \leq 2.
   $$
````

````{prf:proof}
$(1) \implies (2)$

1. Using Markov's inequality, for any $t > 0$ we have
   
   $$
    \PP(X \geq \lambda) 
    &= \PP (t X \geq t \lambda) 
    = \PP \left(e^{t X} \geq e^{t \lambda} \right )\\
    &\leq \frac{\EE \left ( e^{t X} \right ) }{e^{t \lambda}} 
    \leq \exp \left ( - t \lambda + \frac{c^2 t^2}{2}\right ) \Forall t \in \RR. 
   $$
1. Since this is valid for all $t \in \RR$, hence it should be valid for
   the minimum value of r.h.s.
1. The minimum value is obtained for $t = \frac{\lambda}{c^2}$.
1. Thus we get
   
   $$
    \PP(X \geq \lambda) \leq \exp \left ( - \frac{\lambda^2}{2 c^2}\right ). 
   $$
1. Since $X$ is $c$-subgaussian, hence $-X$ is also $c$-subgaussian.
1. Hence
   
   $$
    \PP (X \leq - \lambda) = \PP (-X \geq \lambda)
    \leq \exp \left ( - \frac{\lambda^2}{2 c^2}\right ).
   $$
1. Thus
   
   $$
    \PP(|X| \geq \lambda) = \PP (X \leq - \lambda) + \PP(X \geq \lambda)
    \leq 2 \exp \left ( - \frac{\lambda^2}{2 c^2}\right ).
   $$
1. Thus we can choose $a = \frac{1}{2 c^2}$ to complete the proof.

$(2)\implies (3)$

TODO PROVE THIS

$$
    \EE (\exp (b X^2)) \leq 1 + \int_0^{\infty} 2 b t \exp (b t^2) \PP (|X| > t)d t
$$

$(3)\implies (1)$

TODO PROVE THIS
````

## More Properties
We also have the following result on the exponential moment
of a subgaussian random variable.

````{prf:lemma}
:label: lem:subgaussian_exp_square_moment

Suppose $X \sim \Sub(c^2)$. Then 

$$
\EE \left [\exp \left ( \frac{\lambda X^2}{2 c^2} \right ) \right ]
\leq \frac{1}{\sqrt{1 - \lambda}} 
$$
for any $\lambda \in [0,1)$.
````

````{prf:proof}
We are given that 

$$
&\EE (\exp(X t) ) \leq \exp \left (\frac{c^2 t^2}{2} \right )\\
&\implies \int_{-\infty}^{\infty} \exp(t x) f_X(x) d x 
\leq \exp \left (\frac{c^2 t^2}{2} \right ) \Forall t \in \RR\\
$$
Multiplying on both sides with $\exp \left ( -\frac{c^2 t^2}{2 \lambda} \right )$:

$$
\int_{-\infty}^{\infty} \exp \left (t x - \frac{c^2 t^2}{2 \lambda}\right ) f_X(x) d x 
\leq \exp \left (\frac{c^2 t^2}{2}\frac{\lambda-1}{\lambda} \right )
= \exp \left (-\frac{t^2}{2}\frac{c^2 (1 - \lambda)}{\lambda} \right )
$$
Integrating on both sides w.r.t. $t$ we get:

$$
\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} 
\exp \left (t x - \frac{c^2 t^2}{2 \lambda}\right ) f_X(x) d x  d t 
\leq \int_{-\infty}^{\infty} \exp \left (-\frac{t^2}{2}\frac{c^2 (1 - \lambda)}{\lambda} \right ) d t
$$
which reduces to:

$$
&\frac{1}{c} \sqrt{2 \pi \lambda} \int_{-\infty}^{\infty} 
\exp \left ( \frac{\lambda x^2}{2 c^2} \right ) f_X(x) d x
\leq \frac{1}{c} \sqrt {\frac{2 \pi \lambda}{1 - \lambda}}\\
\implies
&  \EE \left (\exp \left ( \frac{\lambda X^2}{2 c^2} \right ) \right ) \leq \frac{1}{\sqrt{1 - \lambda}}  
$$
which completes the proof.
````
## Subgaussian Random Vectors

The linearity property of subgaussian r.v.s can be extended
to random vectors also.
This is stated more formally in following result.

````{prf:theorem}
:label: res-prob-subgaussian-vec-linear

Suppose that $X = [X_1, X_2,\dots, X_N]$, where each $X_i$ is i.i.d. with
$X_i \sim \Sub(c^2)$.
Then for any $\alpha \in \RR^N$,
$ \langle X, \alpha \rangle \sim \Sub(c^2 \| \alpha \|^2_2)$.
Similarly if each  $X_i \sim \SSub(\sigma^2)$, then
for any $\alpha \in \RR^N$,
$\langle X, \alpha \rangle \sim \SSub(\sigma^2 \| \alpha \|^2_2)$.
````

````{div}
Norm of a subgaussian random vector

1. Let $X$ be a random vector where each $X_i$ is i.i.d. with $X_i \sim \Sub (c^2)$.
1. Consider the $l_2$ norm $\| X \|_2$. It is a random variable in its own right.
1. It would be useful to understand the average behavior of the norm.
1. Suppose $N=1$.  Then $\| X \|_2 = |X_1|$.
1. Also $\| X \|^2_2 = X_1^2$. Thus $\EE (\| X \|^2_2) = \sigma^2$.
1. It looks like $\EE (\| X \|^2_2)$ should be connected with $\sigma^2$.
1. Norm can increase or decrease compared to the average value.
1. A ratio based measure between actual value and average value would be useful.
1. What is the probability that the norm increases beyond a given factor?
1. What is the probability that the norm reduces beyond a given factor?

These bounds are stated formally in the following theorem.
````

````{prf:theorem}

Suppose that $X = [X_1, X_2,\dots, X_N]$,
where each $X_i$ is i.i.d. with $X_i \sim \Sub(c^2)$.
Then

```{math}
:label: eq:subgaussian_vector_norm_expectation

\EE (\| X \|_2^2 ) = N \sigma^2.
```
Moreover, for any $\alpha \in (0,1)$
and for any $\beta \in [\frac{c^2}{\sigma^2}, \beta_{\max}]$,
there exists a constant $\kappa^* \geq 4$ depending only on 
$\beta_{\max}$ and the ratio $\frac{\sigma^2}{c^2}$ such that

```{math}
:label: eq:subgaussian_vector_norm_reduction_probability
\PP (\| X \|_2^2 \leq \alpha N \sigma^2) 
\leq \exp \left ( - \frac{ N (1 - \alpha)^2}{\kappa^*} \right ) 
```
and
```{math}
:label: eq:subgaussian_vector_norm_expansion_probability

\PP (\| X \|_2^2 \geq \beta N \sigma^2) 
\leq \exp \left ( - \frac{ N (\beta - 1)^2}{\kappa^*} \right ) 
```
````

*  First equation gives the average value of the square of the norm.
*  Second inequality states the upper bound on the probability that norm 
could reduce beyond a factor given by $\alpha < 1$.
*  Third inequality states the upper bound on the probability that norm
could increase beyond a factor given by $\beta > 1$.
*  Note that if $X_i$ are strictly subgaussian, then $c=\sigma$. Hence
$\beta \in (1, \beta_{\max})$.


````{prf:proof}
Since $X_i$ are independent hence

$$
    \EE \left [ \| X \|_2^2 \right ]  = \EE \left [ \sum_{i=1}^N X_i^2 \right ] 
    = \sum_{i=1}^N \EE \left [ X_i^2 \right ] = N \sigma^2.
$$
This proves the first part.

Now let us look at {eq}`eq:subgaussian_vector_norm_expansion_probability`.

By applying Markov's inequality for any $\lambda > 0$ we have:

$$
\PP (\| X \|_2^2 \geq \beta N \sigma^2)  
&= \PP \left ( \exp (\lambda \| X \|_2^2 ) \geq \exp (\lambda \beta N \sigma^2) \right) \\
& \leq \frac{\EE (\exp (\lambda \| X \|_2^2 )) }{\exp (\lambda \beta N \sigma^2)}
= \frac{\prod_{i=1}^{N}\EE (\exp ( \lambda X_i^2 )) }{\exp (\lambda \beta N \sigma^2)}
$$

Since $X_i$ is $c$-subgaussian, hence from \cref {lem:subgaussian_exp_square_moment}
we have 

$$
\EE (\exp ( \lambda X_i^2 )) = \EE \left (\exp \left ( \frac{2 c^2\lambda X_i^2}{2 c^2} \right ) \right)
\leq \frac{1}{\sqrt{1 - 2 c^2 \lambda}}.
$$

Thus:

$$
\prod_{i=1}^{N}\EE (\exp ( \lambda X_i^2 )) 
\leq  \left ( \frac{1}{\sqrt{1 - 2 c^2 \lambda}} \right )^{\frac{N}{2}}.
$$
Putting it back we get:

$$
\PP (\| X \|_2^2 \geq \beta N \sigma^2)  
\leq \left (\frac{\exp (- 2\lambda \beta \sigma^2)}{\sqrt{1 - 2 c^2 \lambda}}\right )^{\frac{N}{2}}.
$$
Since above is valid for all $\lambda > 0$,
we can minimize the R.H.S. over $\lambda$ by setting the
derivative w.r.t. $\lambda$ to $0$.

Thus we get optimum $\lambda$ as:

$$
\lambda = \frac{\beta \sigma^2  - c^2 }{2 c^2 \sigma^2 (1 + \beta)}.
$$

Plugging this back we get:

$$
\PP (\| X \|_2^2 \geq \beta N \sigma^2)  \leq
\left ( \beta \frac{\sigma^2}{c^2}  
    \exp \left ( 1  - \beta \frac{\sigma^2}{c^2} \right ) \right ) ^{\frac{N}{2}}.
$$
Similarly proceeding for {eq}`eq:subgaussian_vector_norm_reduction_probability` we get

$$
\PP (\| X \|_2^2 \leq \alpha N \sigma^2)  \leq
\left ( \alpha \frac{\sigma^2}{c^2}  
    \exp \left ( 1  - \alpha \frac{\sigma^2}{c^2} \right ) \right ) ^{\frac{N}{2}}.
$$
We need to simplify these equations. We will do some jugglery now.
Consider the function

$$
f(\gamma) = \frac{2 (\gamma - 1)^2}{(\gamma-1) - \ln \gamma}  \Forall \gamma > 0.
$$

By differentiating twice, we can show that this is a strictly increasing function.
Let us have $\gamma \in (0, \gamma_{\max}]$. 
Define

$$
\kappa^* = \max \left ( 4, \frac{2 (\gamma_{\max} - 1)^2}{(\gamma_{\max}-1) - \ln \gamma_{\max}} \right )
$$
Clearly

$$
\kappa^* \geq  \frac{2 (\gamma - 1)^2}{(\gamma-1) - \ln \gamma} 
\Forall \gamma \in (0, \gamma_{\max}].
$$
Which gives us:

$$
\ln (\gamma) \leq (\gamma - 1) - \frac{2 (\gamma - 1)^2}{\kappa^*}.
$$

Hence by exponentiating on both sides we get:

$$
\gamma \leq \exp \left [ (\gamma - 1) - \frac{2 (\gamma - 1)^2}{\kappa^*} \right ].
$$

By slight manipulation we get:

$$
\gamma  \exp ( 1 - \gamma) \leq \exp \left [ \frac{2 (1 - \gamma )^2}{\kappa^*} \right ].
$$
We now choose 

$$
\gamma = \alpha \frac{\sigma^2}{c^2}
$$
Substituting we get:

$$
\PP (\| X \|_2^2 \leq \alpha N \sigma^2)  \leq
\left ( \gamma \exp \left ( 1  - \gamma \right ) \right ) ^{\frac{N}{2}}
\leq \exp \left [ \frac{N (1 - \gamma )^2}{\kappa^*} \right ] .
$$
Finally

$$
c \geq \sigma \implies \frac{\sigma^2}{c^2}\leq 1 \implies \gamma \leq \alpha 
\implies 1 - \gamma \geq 1 - \alpha
$$
Thus we get

$$
\PP (\| X \|_2^2 \leq \alpha N \sigma^2) 
\leq \exp \left [ \frac{N (1 - \alpha )^2}{\kappa^*} \right ] .
$$
Similarly by choosing $\gamma = \beta \frac{\sigma^2}{c^2}$ proves the other bound.

We can now map $\gamma_{\max}$ to some $\beta_{\max}$ by:

$$
\gamma_{\max} = \frac {\beta_{\max} \sigma^2 }{c^2}.
$$
````
This result tells us that given a vector with entries drawn from a subgaussian
distribution, we can expect the norm of the vector to concentrate around its 
expected value $N\sigma^2$. 

