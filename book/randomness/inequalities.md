# Basic Inequalities

Probability theory is full of inequalities.
Many results are derived from
the application of these inequalities.
This section collects some basic inequalities.

A good reference is [Wikipedia list of inequalities](http://en.wikipedia.org/wiki/List_of_inequalities). 
In particular see the 
[section on probability inequalities](http://en.wikipedia.org/wiki/List_of_inequalities#Probability_theory_and_statistics).

In this section we will cover the basic inequalities.


## Markov's inequality


````{prf:theorem}
:label: res:prob:markov_inequality

Let $X$ be a non-negative random variable and $a > 0$. Then

$$
\PP (X \geq a) \leq \frac{\EE (X)}{a}.
$$
````


## Chebyshev's inequality


````{prf:theorem}
:label: res:prob:chebyshev_inequality

Let $X$ be a random variable with finite mean $\mu$ and finite non-zero variance $\sigma^2$.
Then for any real number $k > 0$, the following holds

$$
\PP (| X - \mu | \geq k \sigma) \leq \frac{1}{k^2}.
$$
````
````{prf:proof}
TBD.
````
Choosing $k = \sqrt{2}$, we see that at least half of the values lie in the interval 
$(\mu - \sqrt{2} \sigma, \mu + \sqrt{2} \sigma)$.


## Boole's inequality


This is also known as union bound.

## Fano's inequality

## Cramér–Rao inequality

## Hoeffding's inequality


This inequality provides an upper bound on the probability that the sum of random variables
deviates from its expected value.

We start with a version of the inequality for i.i.d Bernoulli random variables.

````{prf:theorem}
:label: res:prob:hoeffding_inequality_bernoulli

Let $X_1, \dots, X_n$ be  i.i.d. Bernoulli random variables with probability of success as $p$. 
$\EE \left [\sum_i X_i \right] = p n $. The probability of the sum deviating from the mean  
by $\epsilon n$ for some $\epsilon > 0$
is bounded by

$$
\PP \left (\sum_i X_i \leq (p - \epsilon) n \right ) \leq \exp ( -2 \epsilon^2 n) 
$$
and

$$
\PP \left (\sum_i X_i \geq (p + \epsilon) n \right ) \leq \exp ( -2 \epsilon^2 n).
$$
The two inequalities can be summarized as

$$
\PP \left [ (p - \epsilon) n 
\leq \sum_i X_i 
\leq (p + \epsilon) n \right ] \geq 1 - 2\exp ( -2 \epsilon^2 n). 
$$
````
The inequality states that the number of successes that we see is concentrated around its mean
with exponentially small tail.

We now state the inequality for the general case for any (almost surely) bounded random variable.

````{prf:theorem}
:label: res:prob:hoeffding_inequality

Let $X_1, \dots, X_n$ be independent r.v.s. Assume that $X_i$ are almost surely bounded; i.e.: 

$$
\PP \left ( X_i \in [ a_i, b_i] \right ) = 1, \quad 1 \leq i \leq n. 
$$
Define the empirical mean of the variables as

$$
\overline{X}  \triangleq \frac{1}{n} \left ( X_1  + \dots + X_n \right).
$$
Then the probability that $\overline{X}$ deviates from its mean $\EE(\overline{X})$ 
by an amount $t > 0$
is bounded
by following inequalities:

$$
\PP \left ( \overline{X} -  \EE(\overline{X}) \geq t \right ) \leq 
\exp \left ( - \frac{2 n^2 t^2}{\sum_{i = 1}^n (b_i - a_i)^2} \right)
$$
and

$$
\PP \left ( \overline{X} -  \EE(\overline{X}) \leq -t \right ) \leq 
\exp \left ( - \frac{2 n^2 t^2}{\sum_{i = 1}^n (b_i - a_i)^2} \right).
$$
Together, we have

$$
\PP \left ( \left | \overline{X} -  \EE(\overline{X}) \right | \geq t \right ) \leq 
2\exp \left ( - \frac{2 n^2 t^2}{\sum_{i = 1}^n (b_i - a_i)^2} \right).
$$
````
Note that we don't require $X_i$ to be identically distributed in this formulation. 
For the special case when $X_i$ are i.i.d. uniform r.v.s over $[0, 1]$, then
$\EE(\overline{X}) = \EE(X_i) = \frac{1}{2}$ and

$$
\PP \left ( \left | \overline{X} -  \frac{1}{2}\right | \geq t \right ) \leq 
2\exp \left ( - 2 n t^2 \right).
$$
Clearly, $\overline{X}$ starts concentrating around its mean as $n$ increases and
the tail falls exponentially.

The proof of this result depends on what is known as *Hoeffding's Lemma*.

````{prf:lemma}
:label: res:prob:hoeffding_lemma

Let $X$ be a zero mean r.v.  with $\PP (X \in [a, b]) = 1$. Then

$$
\EE \left [ \exp (t X) \right] \leq \exp \left ( \frac{1}{8} t^2 (b - a)^2 \right ).
$$
````

## Jensen's inequality
Jensen's inequality relates the value of a convex function of an integral to the
integral of the convex function.  In the context of probability theory, the inequality
take the following form.

````{prf:theorem}
:label: res:prob:jensen_inequality

Let $f : \RR \to \RR$ be a convex function. Then

$$
f \left ( \EE [X] \right ) \leq \EE \left [ f  ( X ) \right  ].
$$
````
The equality holds if and only if either $X$ is a constant r.v. or $f$ is linear.

## Bernstein inequalities




## Chernoff's inequality


This is also known as Chernoff bound.


## Fréchet inequalities


