# Basic Subgradient Method

The theory of subgradients for convex functions
is discussed in {ref}`sec:cvxf:subgradients`.
This section discusses basic subgradient method
for optimization.
Primary references for this section are
{cite}`boyd2008subgradient`.


Recall that a vector $\bg$ is a subgradient of $f$ at a point $\bx$ if

$$
f(\by) \geq f(\bx) + \langle \by - \bx, \bg \rangle \Forall \by \in \RR^n.
$$

## Unconstrained Minimization

````{div}
We start with a simple case of minimizing a convex function $f: \RR^n \to \RR$.
1. The optimal value shall be denoted by $f^*$. 
1. We shall assume that the optimal value is finite (i.e., $f^* > -\infty$).
1. The set of optimal minimizers shall be denoted by $X^*$.
1. Since $f$ attains its optimal value, hence $X^*$ is nonempty.
1. A global minimizer will be denoted by $\bx^*$.


The basic subgradient method uses the following iteration.
```{math}
:label: eq-sgm-basic-iteration

\bx^{k+1} = \bx^k - t_k \bg^k.
```

In this iteration

1. $\bx^k$ is the current ($k$-th) iterate.
1. $\bg^k$ is any subgradient of $f$ at $\bx^k$. We have $\bg^k \in \partial f(\bx^k)$.
1. $t_k > 0$ is the step size for the $k$-th iteration
   in the negative subgradient direction $- \bg^k$.
1. $\bx^{k+1}$ is the new ($k+1$-th) iterate.
1. $\| t_k \bg^k \|_2$ denotes the step-length.

Thus, in each iteration of the subgradient method, we take a step in the
direction of a negative subgradient.
````

### Descent Directions

```{prf:observation} Negative subgradient need not be a descent direction
:label: res-sgm-neg-subgradient-descent

1. Recall from {prf:ref}`def-opt-descent-direction` that
    a descent direction of $f$ at $\bx$ is a direction
    along which the directional derivative is negative; i.e.,
    $f'(\bx; \bd) < 0$.

1. If $\bd$ is a descent direction at $\bx$, then there exists
    a step size $t > 0$ such that

    $$
    f(\bx + t \bd) < f(\bx).
    $$
1. If $f$ is a differentiable function and $\bd = - \nabla f(\bx)$,
   then

   $$
   f'(\bx; - \nabla f(\bx)) = - \| \nabla f(\bx) \|^2 \leq 0.
   $$
1. Hence, the negative gradient is always a descent direction
   if the gradient is nonzero.
1. However, for a nondifferentiable function $f$, a
   negative subgradient may not be a descent direction.

1. Recall from max formula ({prf:ref}`res-cvxf-subg-dir-der-max-formula`)
    that

    $$
    f'(\bx;\bd) = \sup \{ \langle \bd, \bg \rangle \ST \bg \in \partial f(\bx) \}.
    $$
1. Let $\tilde{\bg}$ be the chosen subgradient at an iteration
   of the subgradient method.
1. Then 

    $$
    f'(\bx; -\tilde{\bg}) 
    = \sup_{\bg \in \partial f(\bx)} \{ \langle - \tilde{\bg}, \bg \rangle\}
    = - \inf_{\bg \in \partial f(\bx)} \{ \langle \tilde{\bg}, \bg \rangle\}.
    $$
1. It is possible that the quantity $\langle \tilde{\bg}, \bg \rangle$
   is negative for some other subgradient $\bg$ at $\bx$.
1. Hence the directional derivative along $-\tilde{\bg}$ may be positive.
1. This argument shows that a negative subgradient is not necessarily a
   descent direction.
```


### Tracking of the Best Estimate

1. Since the negative subgradient $-\bg^k$ may not be a descent
   direction, hence it is quite likely that $f(\bx^{k+1}) > f(\bx^k)$.
1. Even if the selected $-\bg^k$ is a descent direction at $\bx^k$,
   it is possible that the step size can be such that
   $f(\bx^{k+1}) > f(\bx^k)$.
1. This happens since typically there is no local line search
   method invoked to select an appropriate step size in a
   subgradient method.
1. Since the negative subgradient itself may not be a descent direction, 
   hence running a local line search will be futile.
1. The alternative is to track the best estimate of the optimal value
   so far using the following rule

   $$
   f_{\best}^k = \min \{f_{\best}^{k-1}, f(\bx^k) \}.
   $$
1. If the best estimate has decreased, we also update the
   estimate of the local minimizer as $\bx_{\best}$ to $\bx^{k+1}$.
1. It is easy to see that

   $$
   f_{\best}^k = \min \{f(\bx^1), \dots, f(\bx^k) \}.
   $$
1. We can see that the sequence $\{ f_{\best}^k \}$ is a nonincreasing
   sequence.
1. Hence it has a limit.
1. The success of the subgradient method depends on whether the
   limit equals the optimal value.

### Step Size Selection

```{div}
In a gradient descent method, one typically uses a line search
method to select the step size. Hence, it depends on current iterate
and the function values in its neighborhood.

In a subgradient method, the step size selection is different.
Typically, the step sizes (or step lengths) are determined beforehand
and they don't depend on the data computed during the execution
of the algorithm.
Following are some of the common methods for step size selection.

1. *Constant step size*. $t_k = t$ for some positive constant $t > 0$
   which is independent of $k$.
1. *Constant step length*. 

   $$
   t_k = \frac{c}{\| \bg^k \|_2}
   $$
   where $c > 0$ is a predefined step length.
   Note that with this choice of step size, we have:

   $$
   \| \bx^{k + 1} - \bx^k \|_2 = \| t_k \bg^k \|_2 = c.
   $$
1. *Square summable but not summable*. We choose step sizes
   that satisfy the following constraints:

   $$
   t_k > 0 \Forall k, \quad
   \sum_{k=1}^{\infty} t_k^2 < \infty,
   \sum_{k=1}^{\infty} t_k = \infty.
   $$
   As an example, fix some $a > 0$ and $b \geq 0$ and let

   $$
   t_k = \frac{a}{b + k}.
   $$
1. *Nonsummable diminishing*. We choose step sizes
    that satisfy the following constraints:

    $$
    t_k > 0 \Forall k, \quad
    \lim_{k \to \infty} t_k = 0, \quad
    \sum_{k=1}^{\infty} t_k = \infty.
    $$
    As and example, fix some $a > 0$ and let

    $$
    t_k = \frac{a}{\sqrt{k}}.
    $$
1. *Nonsummable diminishing step lengths*: We choose
    step sizes as $t_k = \frac{c_k}{\| \bg^k \|_2}$
    where

    $$
    c_k > 0, \quad
    \lim_{k \to \infty} c_k = 0,\quad
    \sum_{k=1}^{\infty} c_k = \infty.
    $$
```
### The Subgradient Method

We now present the overall template for the subgradient method.

```{prf:algorithm} The subgradient method
:label: alg-sgm-subgradient-method

Inputs

1. $f$ : function to be minimized
1. $\bx^1$: initial guess for the minimizer
1. $t_1$: initial step size

Outputs

1. $f_{\best}^1$: Best estimate of minimum value of $f$
1. $\bx_{\best}^1$ the best estimate of the minimizer

Initialization

1. $f_{\best} = f(\bx^1)$.
1. $\bx_{\best} = \bx^1$.

General iteration: for $k=1,2,\dots$, execute the following steps

1. Select a subgradient $\bg^k$ from $\partial f(\bx^k)$.
1. Select a step size: $t_k$.
1. Update minimizer estimate: $\bx^{k+1} = \bx^k - t_k \bg^k$.
1. $k = k + 1$.
1. Compute $f(\bx^k)$.
1. if $f_{\best}^{k-1} > f(\bx^k)$:
   1. Update best estimate of optimal value: $f_{\best}^k = f(\bx^k)$.
   1. Update best estimate of minimizer: $\bx_{\best}^k = \bx^k$.
1. Otherwise, retain current values
   1. $f_{\best}^k = f_{\best}^{k-1}$.
   1. $\bx_{\best}^k = \bx_{\best}^{k-1}$.
1. If stopping criterion is met, then STOP.
```

For a concrete implementation, we shall need the following:

1. A way to compute $f(\bx)$ at every $\bx$.
1. A way to pick a subgradient $\bg \in \partial f(\bx)$
   at every $\bx$. 
1. A step size selection strategy.
1. A stopping criterion.

Note that there is no need to specify the complete
subdifferential at every $\bx$.
The stopping criterion will be developed in the
following as part of the convergence analysis of
the algorithm.


## Convergence Analysis

```{div}
Our goal is to show that $f_{\best}^k \downarrow f^*$.
We shall make the following assumptions in the analysis.

1. $f$ is a real valued convex function.
1. The optimal value $f^*$ is finite and the minimizer $\bx^*$ exists.
1. The norm of the subgradients is bounded. i.e., there exists $G > 0$
   such that

   $$
   \| \bg \|_2 \leq G \Forall \bg \in \partial f(\bx) \Forall \bx.
   $$
   Recall from {prf:ref}`res-cvxf-subdiff-bounded-lipschitz-continuous`
   that if a convex function is Lipschitz continuous, then its
   subgradients are bounded.
1. A number $R$ that satisfies 

   $$
   R \geq \| \bx^* - \bx^1 \|_2
   $$
   for some $\bx^* \in X^*$
   is known beforehand.
   $R$ can be interpreted as an upper bound on the distance
   of the initial point to the set of optimal minimizers.

   $$
   R \geq \text{dist}(\bx^1, X^*).
   $$
```


````{prf:theorem} Upper bound on the estimation error
:label: res-sgm-error-upper-bound

Let $\| \bx^1 - \bx^* \|_2 \leq R$.

After $k$ iterations of the subgradient method, we have
```{math}
:label: eq-sgm-error-ub-k-g
f_{\best}^k - f^* \leq 
\frac{R^2 + \sum_{i=1}^k t_i^2 \| \bg_i \|_2^2 }{2 \sum_{i=1}^k t_i }.
```

If the subgradients of $f$ are bounded by $\| \bg \| \leq G$
for all $\bg \in \partial f(\bx)$ for every $\bx$, then this
simplifies to:

```{math}
:label: eq-sgm-error-ub-k
f_{\best}^k - f^* \leq \frac{R^2 + G^2 \sum_{i=1}^k t_i^2}{2 \sum_{i=1}^k t_i }.
```
````

```{prf:proof}
Let $\bx^*$ be a minimizer of $f$.
From the subgradient inequality, we have

$$
f^* = f(\bx^*) \geq f(\bx^k) + \langle \bx^* - \bx^k, \bg^k \rangle. 
$$
Hence

$$
\langle \bx^* - \bx^k, \bg^k \rangle \leq f^* - f(\bx^k).
$$

We first develop an upper bound on the distance between
the $k+1$-th iterate and a minimizer.

$$
\| \bx^{k+1} - \bx^* \|_2^2
& = \| \bx^k - t_k \bg^k - \bx^* \|_2^2 \\
& = \| (\bx^k - \bx^*) - t_k \bg^k \|_2^2 \\
& = \| \bx^k - \bx^* \|_2^2 - 2 t_k \langle \bx^k - \bx^*, \bg^k \rangle
+ t_k^2 \| \bg^k \|_2^2 \\
& \leq \| \bx^k - \bx^* \|_2^2 - 2 t_k (f(\bx^k) - f^*)
+ t_k^2 \| \bg^k \|_2^2.
$$

Applying this inequality recursively, we get

$$
\| \bx^{k+1} - \bx^* \|_2^2
\leq \| \bx^1 - \bx^* \|_2^2 - 2 \sum_{i=1}^k t_i (f(\bx^i) - f^*)
+ \sum_{i=1}^k t_i^2 \| \bg^i \|_2^2.
$$

Using the fact that $\| \bx^{k+1} - \bx^* \|_2^2 \geq 0$
and $\| \bx^1 - \bx^* \|_2 \leq R$, we have

$$
2 \sum_{i=1}^k t_i (f(\bx^i) - f^*) \leq R^2 + \sum_{i=1}^k t_i^2 \| \bg^i \|_2^2.
$$

On the L.H.S., we can see that

$$
\sum_{i=1}^k t_i (f(\bx^i) - f^*)
\geq \left ( \sum_{i=1}^k t_i \right ) \min_{i=1,\dots,k} (f(\bx^i) - f^*)
= \left ( \sum_{i=1}^k t_i \right ) (f_{\best}^k - f^* ).
$$

Combining this with the previous inequality, we get

$$
2 \left ( \sum_{i=1}^k t_i \right ) (f_{\best}^k - f^* )
\leq  R^2 + \sum_{i=1}^k t_i^2 \| \bg^i \|_2^2.
$$
This can be rewritten as

$$
f_{\best}^k - f^* \leq 
\frac{R^2 + \sum_{i=1}^k t_i^2 \| \bg_i \|_2^2 }{2 \sum_{i=1}^k t_i }
$$
as desired.

Applying the upper bound on the subgradient $\| \bg \|_2 \leq G$,
we have

$$
f_{\best}^k - f^* \leq \frac{R^2 +  G^2 \sum_{i=1}^k t_i^2}{2\sum_{i=1}^k t_i }
$$
as desired.
```

Based on this result, we can provide upper bounds on the
estimation error for different step size selection strategies.

### Constant Step Size

```{prf:corollary} Convergence of subgradient method with constant step size
:label: res-sgm-error-ub-constant-step-size

If $t_k = t$ for all $k$, then we have

$$
f_{\best}^k - f^* \leq \frac{R^2 + G^2 t^2 k}{2 t k }.
$$

The subgradient method converges to within $G^2 t / 2$ of the
optimal value $f^*$. In other words,

$$
\lim_{k \to \infty} f_{\best}^k - f^* \leq \frac{G^2 t}{2}.
$$
Also, $f_{\best}^k - f^* \leq G^2 t$ within at most
$R^2 / (G^2 t^2)$ steps.
```

```{prf:proof}
By putting $t_k = t$ in {eq}`eq-sgm-error-ub-k`, we obtain
the desired upper bound. Taking the limit $k \to \infty$,
we see that

$$
\lim_{k \to \infty} (f_{\best}^k - f^*) \leq \frac{G^2 t}{2}.
$$

Now, 

$$
& \frac{R^2 + G^2 t^2 k}{2 t k } \leq G^2 t \\
\iff & R^2 + G^2 t^2 k \leq 2  G^2 t^2 k \\
\iff & R^2 \leq G^2 t^2 k \\
\iff & k \geq \frac{R^2}{G^2 t^2}.
$$

Since $f_{\best}^k$ is a nonincreasing sequence, hence
for all $k \geq R^2 / (G^2 t^2)$, we must have

$$
f_{\best}^k - f^* \leq G^2 t.
$$
```


### Constant Step Length

```{prf:corollary} Convergence of subgradient method with constant step length
:label: res-sgm-error-ub-constant-step-length

Let $c$ be the constant step length for the subgradient method.
Let $t_k = \frac{c}{\| \bg^k \|_2}$ for every $k$.
Then we have

$$
f_{\best}^k - f^* \leq \frac{R^2 + c^2 k}{2 c k / G }.
$$

The subgradient method converges to within $G c / 2$ of the
optimal value $f^*$. In other words,

$$
\lim_{k \to \infty} f_{\best}^k - f^* \leq \frac{G c}{2}.
$$
```
```{prf:proof}
By putting $t_i = \frac{c}{\| \bg^i \|_2}$ in
{eq}`eq-sgm-error-ub-k-g`, we see that

$$
f_{\best}^k - f^* \leq 
\frac{R^2 + \sum_{i=1}^k c^2 }{2 \sum_{i=1}^k t_i }.
$$
Also, note that

$$
& t_i = \frac{c}{\| \bg^i \|_2}\\
\implies & t_i \geq \frac{c}{ G} \\
\implies & \sum_{i=1}^k t_i \geq \frac{c k}{G} \\
\implies & \frac{1}{\sum_{i=1}^k t_i} \leq \frac{1}{c k / G}.
$$
Putting this back, we have

$$
f_{\best}^k - f^* \leq 
\frac{R^2 + c^2 k }{2 c k / G }.
$$
Taking the limit $k \to \infty$, we see that

$$
\lim_{k \to \infty} (f_{\best}^k - f^*) \leq \frac{G c}{2}.
$$
```

### Square Summable Step Sizes

```{prf:corollary} Convergence of subgradient method with square summable step sizes
:label: res-sgm-error-ub-sq-sum-step-sizes

Let the step sizes satisfy the rule

$$
t_k > 0 \Forall k, \quad
\sum_{k=1}^{\infty} t_k^2 < \infty,
\sum_{k=1}^{\infty} t_k = \infty.
$$
Further, let $T = \sum_{k=1}^{\infty} t_k^2$.

Then we have

$$
f_{\best}^k - f^* \leq \frac{R^2 + G^2 T}{2 \sum_{i=1}^k t_k}.
$$

The subgradient method converges to $f^*$.
```

```{prf:proof}
By putting the step size constraints into
{eq}`eq-sgm-error-ub-k`, we obtain

$$
f_{\best}^k - f^* \leq \frac{R^2 + G^2 T}{2 \sum_{i=1}^k t_i }.
$$

Taking the limit $k \to \infty$, the denominator grows to $\infty$
while the numerator converges to $R^2 + G^2 T$.
Hence

$$
\lim_{k \to \infty} f_{\best}^k - f^*  = 0.
$$
```

### Diminishing Step Sizes

```{prf:corollary} Convergence of subgradient method with diminishing step sizes
:label: res-sgm-error-ub-diminishing-step-sizes

Let the step sizes satisfy the rule

$$
t_k > 0 \Forall k, \quad
\lim_{k \to \infty} t_k = 0, \quad
\sum_{k=1}^{\infty} t_k = \infty.
$$
Then the subgradient method converges to $f^*$.
```

```{prf:proof}
We shall show that the R.H.S. of {eq}`eq-sgm-error-ub-k`
converges to 0 as $k \to \infty$.

1. Let $\epsilon > 0$.
1. There exists integer $n_1$ such that
   $t_i \leq \epsilon / G^2$ for all $i > n_1$
   since $t_k \to 0$.
1. There also exists an integer $n_2$ such that
   
   $$
   \sum_{i=1}^{n_2} t_i \geq \frac{1}{\epsilon}
   \left ( R^2 + G^2 \sum_{i=1}^{n_1} t_i^2 \right)
   $$
   since $t_i$ is nonsummable.
1. Let $n = \max\{n_1, n_2 \}$.
1. Then, for every $k > n$, we have

   $$
   \frac{R^2 + G^2 \sum_{i=1}^k t_i^2}{2 \sum_{i=1}^k t_i}
   = \frac{R^2 + G^2 \sum_{i=1}^{n_1} t_i^2}{2 \sum_{i=1}^k t_i}
   + \frac{G^2 \sum_{i=n_1 + 1}^k t_i^2}{2 \sum_{i=1}^{n_1} t_i + 2 \sum_{i=n_1 + 1}^k t_i}.
   $$
1. We can see that

   $$
   \sum_{i=1}^k t_i \geq \sum_{i=1}^{n_2} t_i
   \geq \frac{1}{\epsilon}
   \left ( R^2 + G^2 \sum_{i=1}^{n_1} t_i^2 \right).
   $$
1. Hence

   $$
   \frac{R^2 + G^2 \sum_{i=1}^{n_1} t_i^2}{2 \sum_{i=1}^k t_i} \leq
   \frac{\epsilon}{2}.
   $$
1. For every $i > n_1$, we have $t_i < \epsilon / G^2$.
1. Hence

   $$
   G^2 \sum_{i=n_1 + 1}^k t_i^2
   \leq \epsilon \sum_{i=n_1 + 1}^k t_i.
   $$
1. We can now see that 

   $$
   & \frac{G^2 \sum_{i=n_1 + 1}^k t_i^2}{2 \sum_{i=1}^{n_1} t_i + 2 \sum_{i=n_1 + 1}^k t_i}\\
   & < \frac{G^2 \sum_{i=n_1 + 1}^k t_i^2}{2 \sum_{i=n_1 + 1}^k t_i}\\
   & \leq \frac{\epsilon \sum_{i=n_1 + 1}^k t_i}{2 \sum_{i=n_1 + 1}^k t_i}\\
   &= \frac{\epsilon}{2}.
   $$
1. Combining, we have

   $$
   \frac{R^2 + G^2 \sum_{i=1}^k t_i^2}{2 \sum_{i=1}^k t_i}
   < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
   $$
   for every $k > n$.
1. Thus, for every $\epsilon > 0$, there exists $n$ such that
   for all $k > n$, we have

   $$
   \frac{R^2 + G^2 \sum_{i=1}^k t_i^2}{2 \sum_{i=1}^k t_i} < \epsilon.
   $$

1. Hence 

   $$
   \lim_{k \to \infty}\frac{R^2 + G^2 \sum_{i=1}^k t_i^2}{2 \sum_{i=1}^k t_i} = 0.
   $$
1. Hence the subgradient method converges.
```

### Diminishing Step Lengths

```{prf:corollary} Convergence of subgradient method with diminishing step lengths
:label: res-sgm-error-ub-diminishing-step-length

Let the step sizes $t_k = \frac{c_k}{\| \bg^k \|_2}$
be chosen such that

$$
c_k > 0, \quad
\lim_{k \to \infty} c_k = 0,\quad
\sum_{k=1}^{\infty} c_k = \infty
$$
where $c_k$ is the step length for the $k$-th iteration.

Then the subgradient method converges to $f^*$.
```

```{prf:proof}

From {eq}`eq-sgm-error-ub-k-g` we have

$$
f_{\best}^k - f^* \leq 
\frac{R^2 + \sum_{i=1}^k t_i^2 \| \bg_i \|_2^2 }{2 \sum_{i=1}^k t_i }
= \frac{R^2 + \sum_{i=1}^k c_i^2}{2 \sum_{i=1}^k t_i}.
$$

1. We have

   $$
   \sum_{i=1}^k t_i = \sum_{i=1}^k \frac{c_i}{\| \bg^i \|_2}
   \geq \sum_{i=1}^k \frac{c_i}{G}.
   $$
1. Hence we have

   $$
   f_{\best}^k - f^* \leq \frac{R^2 + \sum_{i=1}^k c_i^2}{(2/G) \sum_{i=1}^k c_i}.
   $$
1. Following an argument similar to the proof of {prf:ref}`res-sgm-error-ub-diminishing-step-sizes`,
   the R.H.S. converges to 0 as $k \to \infty$.
1. Hence

   $$
   \lim_{k \to \infty} f_{\best}^k - f^* = 0.
   $$
```