# Introduction


## Optimization Problems

````{prf:definition} Optimization problem standard form
:label: def-opt-problem-standard-form

Let $\VV$ be an $n$-dimensional real vector space.
A mathematical optimization problem of the form

```{math}
:label: eq-opt-prob-standard-form
& \text{minimize }   & & f_0(\bx) \\
& \text{subject to } & & f_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
```
is known as an *optimization problem* in its *standard form*.

1. $\bx \in \VV$ is called the *optimization variable*.
1. $f_0 : \VV \to \RR$ is called the *objective function* or 
   *cost function*.
1. The functions $f_i : \VV \to \RR$ are called the 
   *inequality constraint functions*.
1. The corresponding inequalities $f_i(\bx) \leq 0$ are called
   the *inequality constraints*.
1. The functions $h_j : \VV \to \RR$ are called the
   *equality constraint functions*.
1. The corresponding equations $h_j(\bx) = 0$ are called the
   *equality constraints*.
1. If there are no constraints ($m=0, p=0$), the problem is
   called *unconstrained*.
1. The set 
   
   $$
   \DDD \triangleq \dom f_0 \cap \bigcap_{i=1}^m \dom f_i \cap \bigcap_{j=1}^p \dom h_j
   $$
   is called the *domain* of the optimization problem.
1. A point $\bx \in \DDD$ is called *feasible* if it satisfies
   all the inequality constraints $f_i(\bx) \leq 0$ and
   all the equality constraints $h_i(\bx) = 0$. 
1. The optimization problem is called *feasible* if there exists
   at least one feasible point.
1. If there are no feasible points in the domain $\DDD$, then
   the optimization problem is called *infeasible*.
   Naturally, if $\DDD = \EmptySet$, then the problem is infeasible.
1. The set of feasible points for an optimization problem is called
   the *feasible set* or the *constraint set*.
1. The *optimum value* $p^* \in \ERL$ of the optimization problem is defined as

   $$
   p^* = \inf \{ f_0(\bx) \ST f_i(\bx) \leq 0, i=1,\dots,m, \;
    h_j(\bx) =  0, j= 1, \dots, p\}.
   $$
   We allow $p^*$ to take the extended values $\infty$ and $-\infty$.
1. If the problem is infeasible, then $p^* = \infty$.
1. If $p^* = -\infty$, then the problem is called *unbounded below*. In this case,
   there exists a sequence $\{ \bx_k \}$ of $\DDD$ such that $\lim f_0(\bx_k) = -\infty$.
1. We say that $\bx^*$ is an *optimal point* if it solves {eq}`eq-opt-prob-standard-form`.
   In other words, $\bx^* \in \DDD$ and $f(\bx^*) = p^*$.
1. The set of all optimal points is known as the *optimal set* denoted by $X_{\text{opt}}$.

   $$
   X_{\text{opt}} \triangleq \{ \bx \ST f_i(\bx) \leq 0, i=1,\dots,m, \;
      h_j(\bx) = 0, j=1,\dots,p, \; f_0(\bx) = p^* \}.
   $$
1. If an optimal point exists in $\DDD$, then we say that the optimal value is
   *attained* or *achieved*.
1. If $X_{\text{opt}}$ is empty, then we say that the optimal value is not
   attained or not achieved.
1. In particular, if the problem is unbounded below, then $X_{\text{opt}}$ is
   indeed empty.
1. A feasible point $\bx$ with $f_0(\bx) \leq p^* + \epsilon$ is called 
   an *$\epsilon-suboptimal point*.
1. The set of all $\epsilon$-suboptimal points is called the 
   *$\epsilon$-suboptimal set* for the problem {eq}`eq-opt-prob-standard-form`.
1. We say that a feasible point $\bx$ is *locally optimal* if there exists
   $r > 0$ such that 

   $$
   f_0(\bx) = \inf \{f_0(\bz) \ST \bz \in B[\bx, r] \cap \DDD \}.
   $$
1. If $\bx$ is feasible and $f_i(\bx) = 0$, we say that $i$-th inequality
   constraint is *active* at $\bx$. Otherwise, $f_i(\bx) < 0$  and we say
   that the $i$-th inequality constraint is *inactive*.
1. We say that a constraint is *redundant* if removing it does not change
   the feasible set.
````

In the sequel, we will be presenting a variety of optimization problems. 
We shall show how those problems can be converted to the standard form
described above.

```{prf:example} Box constraints standard form
:label: ex-opt-box-constraints-standard-form

Let $f_0 : \RR^n \to \RR$ be a real valued function.
Consider the optimization problem

$$
& \text{minimize }   & & f_0(\bx)\\
& \text{subject to } & & l_i \leq x_i \leq u_i, & \quad i=1,\dots,n
$$
where $\bx \in \RR^n$ is the optimization variable.
There are $n$ constraints, one on each component of $\bx$.
Each constraint gives a lower and upper bound on one component.
Such constraints are known as *variable bounds* or *box constraints*.

This problem can be transformed into an equivalent problem:

$$
& \text{minimize }   & & f_0(\bx)\\
& \text{subject to } & & l_i - x_i \leq 0, & \quad i=1,\dots,n\\
& \text{subject to } & & x_i - u_i \leq 0, & \quad i=1,\dots,n.
$$
This form has $2n$ inequality constraints. We introduce the
functions

$$
& f_i(\bx) = l_i - x_i, \quad i=1,\dots,n \\
& \text{ and } \\
& f_i(\bx) = x_{i-n} - u_{i-n}, \quad i=n+1,\dots,2 n.
$$

Then, the problem becomes


$$
& \text{minimize }   & & f_0(\bx)\\
& \text{subject to } & & f_i(\bx) \leq 0, & \quad i=1,\dots,2 n.
$$
This is the optimization problem in standard form with $2 n$ 
inequality constraints and 0 equality constraints.
```


## Feasibility Problems

````{prf:definition} Optimization problem standard form
:label: def-opt-feasibility-problem

Let $\VV$ be an $n$-dimensional real vector space.
A mathematical optimization problem of the form

```{math}
:label: eq-opt-prob-feasibility
& \text{find }   & & \bx \in \VV \\
& \text{subject to } & & f_i(\bx) \leq 0, & i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & j=1,\dots,p
```
is called a feasibility problem. 
````

We can convert this problem into the standard problem 
by introducing a cost function which is identically 0:

$$
f_0(\bx) = 0 \Forall \bx \in \VV.
$$ 

```{div}
1. The domain reduces to

   $$
   \DDD = \bigcap_{i=1}^m \dom f_i \cap \bigcap_{j=1}^p \dom h_j.
   $$
1. The optimal value $p^*=\infty$ if the problem is not feasible.
1. Otherwise, the optimal value is $p^* = 0$.
1. Every feasible point is also an optimal point.
1. Every optimization problem in standard form can be converted
   into a feasibility problem by replacing the objective function
   with the function which is identically 0 everywhere.
1. In that case, the problem reduces to checking whether the
   inequality and equality constraints are consistent or not.
   In other words, whether there are some points which satisfy
   all the inequality and equality constraints.
```
