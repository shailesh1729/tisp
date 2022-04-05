(sec:opt:optimization-intro)=
# Mathematical Optimization

Main references for this section are {cite}`boyd2004convex,bertsekas2003convex`.

This section provides a general overview of optimization problems.
The notion of objective or cost functions and constraint functions
is introduced. Standard form for optimization problems is introduced.
Several examples are discussed for equivalent forms of optimization problems.
The standard form focuses on minimizing the objective function
over a set of equality and inequality constraints. Maximization
problems can also be converted into minimization problems by
changing the sign of the objective function.

We introduce the notion of the domain of an optimization problem,
feasible points or solutions, feasible set of solutions, the optimal
value of the minimization problem, optimal points or solutions,
optimal set etc.. We discuss when the problem may be infeasible
or feasible but unbounded. We discuss situations where the problem
may be feasible and have a global minimum/optimal value and yet
a feasible solution may not exist. 

We then discuss general requirements for the feasibility
of the optimization problem and existence of an optimal 
solution. We introduce the notion of coercive functions
which provide the Weierstrass type result for the existence
of optimal solutions.

## Optimization Problems

Let $\VV$ be a real $n$-dimensional inner product space.

In the most general form, an optimization problem can
be considered as minimizing or maximizing the value
of a real valued function $f : \VV \to \RR$ over
its domain $S = \dom f$.


```{div}
1. We call $f$ as the objective function which is being
   minimized or maximized.
1. The variable $\bx \in \VV$ is called the optimization
   variable.
1. $S = \dom f$ is called the feasible set of solutions
   for the optimization problem.
1. A point $\bx \in S$ is called a feasible point or feasible solution.
1. Our goal is to find an $\bx^* \in S$ which maximizes
   or minimizes the objective function $f$.
```

```{prf:definition} Globally optimal value and points
:label: def-opt-global-optimal-point

Let $f : \VV \to \RR$ be a real valued function with
$S = \dom f$.

1. The maximum value of $f$ is given by
   
   $$
   \sup \{ f(\bx) \ST \bx \in S \}.
   $$
1. The minimum value of $f$ is given by
   
   $$
   \inf \{ f(\bx) \ST \bx \in S \}.
   $$
1. We allow the maximum and minimum values to take $\infty$ and $-\infty$
   values.
1. The function $f$ may or may not attain its maximum / minimum 
   value at some point in its domain $S$.
1. $\bx^* \in S$ is called a *global minimum point* if
   $f(\bx) \geq f(\bx^*)$ for every $\bx \in S$.
1. $\bx^* \in S$ is called a *global maximum point* if
   $f(\bx) \leq f(\bx^*)$ for every $\bx \in S$.
1. $\bx^* \in S$ is called a *strict global minimum point* if
   $f(\bx) > f(\bx^*)$ for every $\bx \in S$ with $\bx \neq \bx^*$.
1. $\bx^* \in S$ is called a *strict global minimum point* if
   $f(\bx) < f(\bx^*)$ for every $\bx \in S$ with $\bx \neq \bx^*$.
1. A point $\bx^* \in S$ is called a *global optimal point* if
   it is either a global maximum or minimum point.
1. The maximum and minimum values of $f$ are always unique
   as opposed to global optimal points which may not be unique.
1. The set of global minimizers is given by

   $$
   \argmin \{ f(\bx) \ST \bx \in S \}.
   $$
1. The set of global maximizers is given by

   $$
   \argmax \{ f(\bx) \ST \bx \in S \}.
   $$
```

In a more restricted setting, an optimization problem can
be considered as minimizing or maximizing the value
of a real valued function $f : \VV \to \RR$ with $S = \dom f$
over a set $A$ such that $A \subseteq S$.

```{div}
1. In this case, the feasible set is restricted to $A$.
1. Minimizers and maximizers are searched within this subset $A$.
1. This problem can be converted into the earlier general form
   by considering the restriction $\tilde{f} : \VV \to \RR$ of
   $f$ such that $A = \dom \tilde{f}$ and

   $$
   \tilde{f}(\bx) = f(\bx) \Forall \bx \in A.
   $$
```

In several problems, it may not be possible to
establish whether a point is globally optimal.
However, it is easier to establish if a point
is optimal in a neighborhood around it. Such
points are called locally optimal points
or extreme values.

```{prf:definition} Local optimal points
:label: def-opt-local-optimal-point

Let $f : \VV \to \RR$ be a real valued function with
$S = \dom f$.
We say that $f(\ba)$ is a *local extreme value*
or *local optimal value*
of $f$ at $\ba \in \dom f$ 
if there exists
$\delta > 0$ such that $f(\bx) - f(\ba)$ doesn't change sign on
$B(\ba, \delta) \cap S$.

More specifically,

1. $f(\ba)$ is a *local maximum value* of $f$ if for some $\delta > 0$:

   $$
   f(\bx) \leq f(\ba) \Forall \bx \in B(\ba, \delta) \cap S.
   $$ 
1. $f(\ba)$ is a *local minimum value* of $f$ if for some $\delta > 0$:

   $$
   f(\bx) \geq f(\ba) \Forall \bx \in B(\ba, \delta) \cap S.
   $$ 

The point $\bx=\ba$ is called a *local extreme point*
or *local optimal point* of $f$ or more 
specifically, a *local maximum* or a *local minimum* point of $f$.


1. $\ba$ is a *strict local maximum point* if for some $\delta > 0$:

   $$
   f(\bx) > f(\ba) \Forall \bx \in B_d(\ba, \delta) \cap S.
   $$ 
1. $\ba$ is a *strict local minimum point* of $f$ if for some $\delta > 0$:

   $$
   f(\bx) > f(\ba) \Forall \bx \in B_d(\ba, \delta) \cap S.
   $$ 

Here $B_d(\ba, \delta)$ denotes the deleted neighborhood
(an open ball of radius $\delta$ excluding $\ba$ itself).
```

```{prf:remark} Local optimal points for open domain
:label: rem-opt-local-optimal-point-open-dom


Let $f : \VV \to \RR$ be a real valued function with
$S = \dom f$.
Assume that $S$ is open.

1. If $\ba \in S$ is a local maximum point, then there exists $r_1 > 0$
   such that

   $$
   f(\bx) \leq f(\ba) \Forall \bx \in B(\ba, r_1) \cap S.
   $$
1. But since $S$ is open, hence $\ba \in \interior S$. Thus,
   there exists an open ball $B(\ba, r_2) \subseteq S$.
1. Let $r = \min(r_1, r_2)$. 
1. Then, $B(\ba, r) \subseteq S$ and $B(\ba, r) \subseteq B(\ba, r_1)$.
1. Thus, $B(\ba, r) \subseteq B(\ba, r_1) \cap S$.
1. Thus, $f(\bx) \leq f(\ba) \Forall \bx \in B(\ba, r) \subseteq S$.
1. Thus, the local optimality condition simplifies to looking for 
   an open ball of radius $r$ totally contained inside the open domain $S$.

Based on this discussion, we can adjust the conditions for local
optimality.

1. $\ba$ is a *local maximum point* of $f$ if for some $r > 0$:

   $$
   f(\bx) \leq f(\ba) \Forall \bx \in B(\ba, r) \subseteq S.
   $$
1. $\ba$ is a *local minimum point* of $f$ if for some $r > 0$:

   $$
   f(\bx) \geq f(\ba) \Forall \bx \in B(\ba, r) \subseteq S.
   $$
1. $\ba$ is a *strict local maximum point* if for some $r > 0$:

   $$
   f(\bx) > f(\ba) \Forall \bx \in B_d(\ba, r) \subseteq S.
   $$ 
1. $\ba$ is a *strict local minimum point* of $f$ if for some $r > 0$:

   $$
   f(\bx) > f(\ba) \Forall \bx \in B_d(\ba, r) \subseteq S.
   $$
```

### Standard Form for Mathematical Optimization Problems

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
   the *feasible set* or the *constraint set*. We shall denote
   the feasible set by $C$.

   $$
   C = \dom f_0 \cap \bigcap_{i=1}^m f_i^{-1}(-\infty, 0] \cap \bigcap_{j=1}^p h_j^{-1}(0).
   $$
   It is the intersection of the domain of $f_0$,
   the 0-sublevel sets of $f_i$ for $i=1,\dots,m$,
   and the $0$-level sets of $h_j$ for $j=1,\dots,p$.
1. Thus, if the problem is infeasible, then $C = \EmptySet$.
1. The *optimum value* $p^* \in \ERL$ of the optimization problem is defined as

   $$
   p^* = \inf \{ f_0(\bx) \ST f_i(\bx) \leq 0, i=1,\dots,m, \;
    h_j(\bx) =  0, j= 1, \dots, p\}.
   $$
   In other words,

   $$
   p^* = \inf \{ f_0(\bx) \ST \bx \in C \}.
   $$
   We allow $p^*$ to take the extended values $\infty$ and $-\infty$.
1. If the problem is infeasible, then $p^* = \infty$
   It is consistent with the convention that the infimum of an empty set is $\infty$.
1. If $p^* = -\infty$, then the problem is called *unbounded below*. In this case,
   there exists a sequence $\{ \bx_k \}$ of $C$ such that $\lim f_0(\bx_k) = -\infty$.
1. We say that $\bx^*$ is an *optimal point* if it solves {eq}`eq-opt-prob-standard-form`.
   In other words, $\bx^* \in C$ and $f(\bx^*) = p^*$.
1. The set of all optimal points is known as the *optimal set* denoted by $X_{\text{opt}}$.

   $$
   X_{\text{opt}} \triangleq \{ \bx \ST f_i(\bx) \leq 0, i=1,\dots,m, \;
      h_j(\bx) = 0, j=1,\dots,p, \; f_0(\bx) = p^* \}.
   $$
   In other words,

   $$
   X_{\text{opt}}  = \{ \bx \in C \ST f_0(\bx) = p^* \}.
   $$
1. If an optimal point exists in $C$, then we say that the optimal value is
   *attained* or *achieved*.
1. If $X_{\text{opt}}$ is empty, then we say that the optimal value is not
   attained or not achieved.
1. In particular, if the problem is unbounded below, then $X_{\text{opt}}$ is
   indeed empty.
1. If the feasible set $C$ is not closed, then it is quite possible that
   The optimum value $p^*$ is finite and yet it is not attained at any
   feasible point. Then, there exists a sequence $\{ \bx_k \}$
   of feasible points such that $\lim f(\bx_k) = p^*$.
   However, there is no $\bx \in C$ such that $f(\bx) = p^*$.
1. A feasible point $\bx \in C$ with $f_0(\bx) \leq p^* + \epsilon$ is called 
   an *$\epsilon$-suboptimal point*.
1. The set of all $\epsilon$-suboptimal points is called the 
   *$\epsilon$-suboptimal set* for the problem {eq}`eq-opt-prob-standard-form`.
1. We say that a feasible point $\bx$ is *locally optimal* if there exists
   $r > 0$ such that 

   $$
   f_0(\bx) = \inf \{f_0(\bz) \ST \bz \in B[\bx, r] \cap C \}.
   $$
   In other words, $\bx$ minimizes $f$ over a local neighborhood 
   of feasible points.
1. If $\bx$ is feasible and $f_i(\bx) = 0$, we say that $i$-th inequality
   constraint is *active* at $\bx$. Otherwise, $f_i(\bx) < 0$  and we say
   that the $i$-th inequality constraint is *inactive*.
1. We say that a constraint is *redundant* if removing it does not change
   the feasible set.
1. If we choose an orthonormal basis $\BBB = \{\be_1, \dots, \be_n \}$ for $\VV$,
   then $\VV$ is
   isomorphic to $\RR^n$ under the bracket operator $[\cdot]_{\BBB}$.
   The optimization variable $\bx$ has a representation
   $(x_1, \dots, x_n)$ in $\RR^n$ given by

   $$
   \bx = \sum_{i=1}^n x_i \be_i.
   $$
1. Thus, determining $\bx$ is same as determining its components 
   $(x_1, \dots, x_n)$.
1. Since there are $n$ scalar components in the representation of $\bx$,
   hence we can say that the optimization problem has $n$ (scalar) variables.
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


```{prf:example} Maximization problem in standard form
:label: ex-opt-maximization-problem-form

Consider the problem 

$$
& \text{maximize }   & & f_0(\bx) \\
& \text{subject to } & & f_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
$$

If we replace $f_0$ by $-f_0$, then maximizing $f_0$
is same as minimizing $-f_0$. Thus, this problem has an equivalent form


$$
& \text{minimize }   & & -f_0(\bx) \\
& \text{subject to } & & f_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
$$
```

````{prf:definition} Feasibility problem
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

## Equivalent Problems

```{prf:definition} Equivalent optimization problems
:label: def-opt-eq-problem
We provide an informal definition of equivalent optimization problems.

Two optimization problems are called *equivalent* if it is possible
to find the solution of one problem from the other problem and 
the vice versa.
````

The primary reason for transforming an optimization problem to an
equivalent one is that it may be easier to solve an equivalent problem.
If we can transform a problem into a form which has a well known
closed form solution or has a well known algorithm to solve the problem,
then we can solve the original problem by first solving the equivalent
problem and then transforming the solution of the equivalent problem
to the solution of the original problem.

1. Transform the problem to an equivalent problem with a known algorithm for solution.
1. Solve the equivalent problem.
1. Transform the solution of the equivalent problem to the solution of the original
   problem.

In this sense, the computational complexity of solving an optimization problem
cannot be greater than the complexity of solving the equivalent problem plus
the complexity of transforming the solution of the equivalent problem to the solution 
of the original problem.

There are several ways to obtain an equivalent optimization problem
from an existing optimization problem. 

### Scaling

```{prf:proposition} Equivalent problems by scaling of objective or constraint functions
:label: res-opt-eq-problem-scaling

Consider the problem given by

$$
& \text{minimize }   & & f'_0(\bx) = \alpha_0 f_0(\bx) \\
& \text{subject to } & & f'_i(\bx) = \alpha_i f_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h'_j(\bx) = \beta_j h_j(\bx) = 0,    & \quad j=1,\dots,p
$$
where $\alpha_i > 0$ for $i=0,\dots,m$ and $\beta_j \neq 0$ for $j=1,\dots,p$.

This problem is obtained from the optimization problem in standard from in
{eq}`eq-opt-prob-standard-form` by *scaling* the objective function and
the inequality constraint functions by positive constants and the
equality constraints by nonzero constants.
```

```{div}
1. $\alpha_0$ cannot be negative otherwise it will convert a minimization
   problem to a maximization problem.
1. $\alpha_0$ cannot be zero as that will convert the optimization problem
   into a feasibility problem.
1. $\alpha_i$ for $i=1,\dots,m$ cannot be negative as it will turn
   the inequality sign from $f_i(\bx) \leq 0$ to $f'(\bx) \geq 0$.
1. $\alpha_i$ for $i=1,\dots,m$ cannot be zero as it will remove the
   corresponding constraint altogether.
1. $\beta_j$ cannot be zero. A zero value will discard the corresponding
   equality constraint. 
1. The feasible sets for both problems are identical.
1. The optimal sets for both problems are identical.
1. The optimal values for both problems are not identical however
   (unless $\alpha_0 = 1$). 
   Since $f'_0$ is a scaled version of $f_0$, hence the
   optimal value is also scaled accordingly.
```

### Change of Variables

````{prf:proposition} Change of variables
:label: res-opt-eq-form-change-variables

Let $\phi : \VV \to \VV$ be an injective function with
$\DDD \subseteq \range \phi$. 

For the problem {eq}`eq-opt-prob-standard-form`, introduce the following functions

$$
\tilde{f}_i(\bz) = f_i(\phi(\bz)), \; i=0,\dots,m
\quad \text{ and } \quad
\tilde{h}_j(\bz) = h_j(\phi(\bz)), \; j=1,\dots,p.
$$

Now, consider the problem

```{math}
:label: eq-opt-prob-var-change
& \text{minimize }   & & \tilde{f}_0(\bz) \\
& \text{subject to } & & \tilde{f}_i(\bz) \leq 0, & \quad i=1,\dots,m\\
&                    & & \tilde{h}_j(\bz) = 0,    & \quad j=1,\dots,p
```
with the variable $\bz \in \VV$.

We say that the two problems are related by the *change of variable*
or *substitution* of the variable $\bx = \phi (\bz)$.
````

```{div}
Suppose $\bz^*$ is the solution to {eq}`eq-opt-prob-var-change`, then
$\bx^* = \phi(\bz^*)$ is a solution to {eq}`eq-opt-prob-standard-form`.


Similarly, if $\bx^*$ is a solution to {eq}`eq-opt-prob-standard-form`,
then $\bz^* = \phi^{-1}(\bx^*)$ is a solution to {eq}`eq-opt-prob-var-change`.
```

### Transformation with Monotone Functions

````{prf:proposition} Transformation of objective and constraint functions
:label: def-opt-eq-form-monotone-transform

For the problem {eq}`eq-opt-prob-standard-form`, we introduce the following:

1. Let $\psi_0: \RR \to \RR$ be a strictly increasing function over $\range f_0$.
1. Let $\psi_i : \RR \to \RR$ for $i=1,\dots,m$ be strictly increasing
   functions  over $\range f_i$ with $\psi_i(u) \leq 0 \iff u \leq 0$.
1. Let $\eta_j : \RR \to \RR$ for $j=1,\dots,p$ be real functions that satisfy 
   $\eta_j(u) = 0 \iff u = 0$.
1. Let $\tilde{f}_i (\bx) = \psi_i (f_i(\bx))$ for $i=0,\dots,m$.
1. Let $\tilde{h}_j (\bx) = \eta_j (h_j(\bx))$ for $j=1,\dots,p$. 

Now, consider the problem

```{math}
:label: eq-opt-prob-monotone-trans
& \text{minimize }   & & \tilde{f}_0(\bx) \\
& \text{subject to } & & \tilde{f}_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & \tilde{h}_j(\bx) = 0,    & \quad j=1,\dots,p
```
with the variable $\bx \in \VV$.

The problem {eq}`eq-opt-prob-monotone-trans` is equivalent to
{eq}`eq-opt-prob-standard-form`.
````


```{prf:example} Least norms and least norms squared
:label: ex-opt-eq-norm-norm-squared 

Consider the unconstrained least norm problem

$$
\text{minimize} \| \bA \bx - \bb \|_2
$$
with $\bx \in \RR^n$, $\bA \in \RR^{m \times n}$ and $\bb \in \RR^m$.
We have $f_0(\bx) = \| \bA \bx - \bb \|_2$. Then, $\range f_0 = \RR_+$.
Consider $\psi_0 : \RR \to \RR$ as

$$
\psi_0 (x) = x^2.
$$
Then, $\psi_0$ is strictly increasing over $\RR_+$. Let 

$$
\tilde{f}_0 (\bx) = \psi_0 (f_0(\bx)) = \| \bA \bx - \bb \|_2^2
= (\bA \bx - \bb)^T (\bA \bx - \bb).
$$

Then, the least norm minimization problem is equivalent to the
problem

$$
\text{minimize} (\bA \bx - \bb)^T (\bA \bx - \bb)
$$
which is the least norm squared problem.

We note that while $\tilde{f}_0$ is differentiable, 
$f_0$ is not. It is a key difference between the
two problems. Solving the least norm squared problem 
can be done using gradient methods since the objective
function is differentiable.
```

### Slack Variables

````{prf:proposition} Slack variables
:label: res-opt-eq-form-slack-variables

For the inequality constraints in the problem {eq}`eq-opt-prob-standard-form`, 
we can introduce the variables $s_i \geq 0$ so that
$f_i(\bx) + s_i = 0$. This way, we can convert an inequality constraint
to an equality constraint and introduce simpler inequality constraints
for the variables $s_i \geq 0$.
The resultant problem:


```{math}
:label: eq-opt-prob-slack-vars
& \text{minimize }   & & f_0(\bx) \\
& \text{subject to } & & s_i\geq 0, & \quad i=1,\dots,m\\
&                    & & f_i(\bx) + s_i =  0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
```
where the optimization variables are $\bx \in \VV$ and $\bs \in \RR^m$
is equivalent to {eq}`eq-opt-prob-standard-form`. 

The variables $s_i$ are known as *slack variables*. 
$\bs = (s_1, \dots, s_m)$ is a vector that collects all the slack variables.
````

```{div}
1. This form has $m$ inequality constraints and $m+p$ equality constraints.
1. It has $n+m$ optimization variables $x_1, \dots, x_n$ and $s_1, \dots, s_m$.
1. If $(\bx, \bs)$ is a feasible point for {eq}`eq-opt-prob-slack-vars`,
   then $\bx$ is a feasible point for {eq}`eq-opt-prob-standard-form`.
1. If $\bx$ is a feasible point for {eq}`eq-opt-prob-standard-form`,
   then we can pick $s_i = -f_i(\bx)$ to form $\bs$ making $(\bx, \bs)$
   a feasible point for {eq}`eq-opt-prob-slack-vars`.
1. $\bx$ is an optimal point for {eq}`eq-opt-prob-standard-form`
   if and only if $(\bx, \bs)$ is an optimal point for
   {eq}`eq-opt-prob-slack-vars` where $s_i = - f_i(\bx)$.
1. The slack variables
   measure how much slack does an inequality constraint function have
   at a feasible point. 
1. If $s_i = 0$ then, $f_i$ is active and it has no slack.
1. If $s_i > 0$, then $f_i$ inactive and it has some slack.
```


### Epigraph Polar Form


````{prf:proposition} Epigraph polar form
:label: res-opt-eq-epigraph-polar-form

The problem {eq}`eq-opt-prob-standard-form` is equivalent to the
optimization problem below:

```{math}
:label: eq-opt-prob-epigraph-polar-form
& \text{minimize }   & & t \\
& \text{subject to } & & f_0(\bx) - t\leq 0, & \\
&                    & & f_i(\bx) \leq 0, & \quad i=1,\dots,m\\
&                    & & h_j(\bx) = 0,    & \quad j=1,\dots,p
```
with the optimization variable $(\bx, t) \in \VV \oplus \RR$.
````


```{div}

1. Note that $t$ appears only in a single inequality in {eq}`eq-opt-prob-epigraph-polar-form`.
1. At the optimal point, $f_0(\bx) = t$ must hold true.
   If $f(\bx) < t$, then we can always choose a lower value of $t$ as the solution.
1. If $\bx$ is an optimal point for {eq}`eq-opt-prob-standard-form`, 
   then $(\bx, f(\bx))$ must be
   an optimal point for {eq}`eq-opt-prob-epigraph-polar-form`.
1. Similarly, if $(\bx, t)$ is an optimal point for {eq}`eq-opt-prob-epigraph-polar-form`,
   then $\bx$ must be an optimal point for {eq}`eq-opt-prob-standard-form`
   and $t=f_0(\bx)$ must hold true.
1. The two problems are indeed equivalent.
1. This problem has $m+1$ inequality constraints and $p$ equality constraints.
1. The objective function for the epigraph form is a linear function of $(\bx, t)$.
```


## First Order Conditions

In this subsection, we focus on objective functions of type
$f : \RR^n \to \RR$ which are differentiable.

````{prf:theorem} First order optimality criterion for local optimal points
:label: res-opt-first-order-optimality-local

Let $f : \RR^n \to \RR$ be a real valued function with $S = \dom f$.
Suppose that $\bx^* \in \interior S$ is a local optimal point.
Assume that all the partial derivatives of $f$ exist at $\bx^*$.  
Then, $\nabla f(\bx^*) = \bzero$.


1. Let $i=1,\dots,n$.
1. Consider the one-dimensional function $g_i : \RR \to \RR$ given by

   $$
   g_i (t) = f(\bx^* + t \be_i)
   $$
   where $\be_i$ is the $i$-th unit vector of $\RR^n$.
1. We note that $g_i$ is differentiable at $t=0$ and

   $$
   g_i'(0) = \frac{\partial f}{\partial x_i} (\bx^*).
   $$
1. Since $\bx^*$ is a local optimal point of $f$, hence
   $t=0$ is a local optimal point of $g_i$.
1. Thus, $g_i'(0) = 0$.
1. Thus, $\frac{\partial f}{\partial x_i} (\bx^*) = 0$.
1. Since, this is true for every $i=1,\dots,n$, hence
   $\nabla f(\bx^*) = \bzero$.
````

We mention that gradient being zero is a necessary condition;
i.e., if a point is an optimal point then the gradient of $f$
at that point must be zero. It is not a sufficient condition.
The gradient may be zero and yet the point may not be an
optimal point.

```{prf:definition} Stationary point
:label: def-opt-stationary-point

Let $f : \RR^n \to \RR$ be a real valued function with $S = \dom f$.
Let $\bx^* \in \interior S$ and assume that $f$ is differentiable
in some neighborhood of $\bx^*$.
Then, $\bx^*$ is called a *stationary point* if
$\nabla f(\bx^*) = \bzero$.
```

Thus, the locally optimal points are necessarily
stationary points.


## Second Order Conditions


```{prf:theorem} Necessary second order optimality conditions
:label: res-opt-2nd-order-optimality-local-nec

Let $f : \RR^n \to \RR$ be a real valued function with $S = \dom f$.
Assume that $S$ is open.
Further, assume that $f$ is twice continuously differentiable over $S$
and that $\ba \in S$ is a stationary point.

Then, the following hold.

1. If $\ba$ is a local minimum point of $f$ over $S$, then
   $\nabla^2 f(\ba) \succeq \ZERO$.
1. If $\ba$ is a local maximum point of $f$ over $S$, then
   $\nabla^2 f(\ba) \preceq \ZERO$.   
```

```{prf:proof}
Assume $\ba$ to be a local minimum point.

1. Then, there exists an open ball $B(\ba, r) \subseteq S$
   such that $f(\bx) \geq f(\ba)$ for all $\bx \in B(\ba, r)$.
1. Let $\bd \in \RR^n$ be a nonzero vector.
1. For $0 < t < \frac{r}{\| \bd \|}$, we define

   $$
   \ba_t = \ba + t \bd.
   $$
   By definition, $\ba_t \in B(\ba, r)$.
1. Hence, for any $t \in (0, \frac{r}{\| \bd \|})$, 
   $f(\ba_t) \geq f(\ba)$.
1. By linear approximation theorem ({prf:ref}`res-mvc-linear-approx-theorem`),
   there exists a vector $\bz_t \in [\ba, \ba_t]$
   such that

   $$
   f(\ba_t) - f(\ba) = \nabla f(\ba)^T (\ba_t - \ba) 
   + \frac{1}{2} (\ba_t - \ba)^T \nabla^2 f(\bz_t) (\ba_t - \ba).
   $$
1. Since $\ba$ is a stationary point, hence $\nabla f(\ba) = \bzero$.
1. Also, by definition of $\ba_t$, $\ba_t - \ba = t \bd$.
1. Thus,

   $$
   f(\ba_t) - f(\ba) = \frac{t^2}{2} \bd^T \nabla^2 f(\bz_t) \bd.
   $$
1. Since $f(\ba)$ is local minimum. Hence, $f(\ba_t) - f(\ba) \geq 0$.
1. Thus, for any $\bd \in \RR^n$ and any $0 < t < \frac{r}{\| \bd \|}$, we have

   $$
   \frac{t^2}{2} \bd^T \nabla^2 f(\bz_t) \bd \geq 0.
   $$
1. By the continuity of the Hessian, and the fact that $\bz_t \to \ba$
   as $t \to 0^+$, we obtain that

   $$
   \frac{t^2}{2} \bd^T \nabla^2 f(\ba) \bd \geq 0 \Forall \bd \in \RR^n.
   $$
1. Thus, $\nabla^2 f(\ba) \succeq \ZERO$.

The argument for second statement is similar. We can apply the
same argument on $-f$ and recognize that if $\ba$ is a local maximum
for $f$ then it is a local minimum for $-f$.
```

```{prf:theorem} Sufficient second order optimality conditions
:label: res-opt-2nd-order-optimality-local-suf

Let $f : \RR^n \to \RR$ be a real valued function with $S = \dom f$.
Assume that $S$ is open.
Further, assume that $f$ is twice continuously differentiable over $S$
and that $\ba \in S$ is a stationary point.

Then, the following hold.

1. If $\nabla^2 f(\ba) \succ \ZERO$,
   then $\ba$ is a strict local minimum point of $f$ over $S$.
1. If $\nabla^2 f(\ba) \prec \ZERO$,
   then $\ba$ is a strict local maximum point of $f$ over $S$.
```


```{prf:proof}
Let $\ba \in S$ is a stationary point satisfying $\nabla^2 f(\ba) \succ \ZERO$.

1. Since the Hessian is continuous ($f$ is twice continuously differentiable),
   hence there exists an open ball $B(\ba, r)$ such that
   $\nabla^2 f(\bx) \succ \ZERO$ for every $\bx \in B(\ba, r)$.
1. By linear approximation theorem ({prf:ref}`res-mvc-linear-approx-theorem`),
   for any $\bx \in B(\ba, r)$, there exists a vector $\bz \in [\ba, \bx]$
   such that

   $$
   f(\bx) - f(\ba) = \frac{1}{2} (\bx - \ba)^T \nabla^2 f(\bz) (\bx - \ba).
   $$
1. We note that $\bz \in B(\ba, r)$. Hence, $\nabla^2 f(\bz) \succ \ZERO$.
1. Thus, $\frac{1}{2} (\bx - \ba)^T \nabla^2 f(\bz) (\bx - \ba) > 0$.
1. Thus, $f(\bx) - f(\ba) > 0$ holds true for every $\bx \in B(\ba, r)$.
1. Thus, $\ba$ is a strict local minimum point for $f$ over $S$.

The proof for the second statement is similar.
```



## Minimization of Proper Functions

```{div}
Let $\VV$ be a real $n$-dimensional normed linear space.
Let $f : \VV \to \RERL$ be a proper function with $S = \dom f$.
We consider the problem of minimizing $f$ over a set $A \subseteq S$.

1. $f$ is the objective function or cost function (being minimized).
1. The set $A$ is the feasible set or constraint set.
1. Any $\bx \in A$ is a feasible solution or feasible point.
1. If there is at least one feasible point (i.e., $A$ is nonempty),
   the problem is feasible.
1. Otherwise, the problem is infeasible.
1. Let $p^* = \inf_{\bx \in A} f(\bx)$ be the optimal value of the minimization problem.
1. We allow $p^*$ to take values over the extended real line $\ERL$.
1. If the minimization problem is infeasible, then $p^* = \infty$.
1. If $p^* = -\infty$, then the problem is unbounded below.
1. If there is some $\bx^* \in A$ such that $f(\bx^*) = p^*$, then
   $\bx^*$ is an optimal solution or optimal point or minimizing point
   or minimizer or global minimum over $A$.
1. Alternatively, $f$ attains a minimum over $A$ at $\bx^*$.
   We write this as 

   $$
   \bx^* \in \underset{\bx \in A}{\argmin} f(\bx).
   $$ 
1. If $\bx^*$ is a unique minimizer of $f$ over $A$, then we abuse the notation and write

   $$
   \bx^* = \underset{\bx \in A}{\argmin} f(\bx).
   $$
1. It is possible that $p^*$ is finite and yet there is no optimal point
   in $A$. 
1. In other words, the set $\underset{\bx \in A}{\argmin} f(\bx)$ may be empty.
```

A basic question of optimization is whether an optimal solution exists.

```{prf:remark} The set of optimal points
:label: res-opt-min-f-optimal-set

The set of optimal points for the problem of minimization of a proper function
$f$ over a feasible set $A$ is given by

$$
\argmin_{\bx \in A} f(\bx) = A \cap f^{-1}(p^*)
$$
where $p^* = \inf_{\bx \in A} f(\bx)$
and $f^{-1}(y)$ denotes the level set of $f$ given by $\{\bx \in S \ST f(\bx) = y \}$.

This comes directly from the fact that

1. $\bx^*$ must be feasible. Hence $\bx^* \in A$.
1. $f$ must attain the optimal value at $\bx^*$. Thus, $p^* = f(\bx^*)$.
   Hence, $\bx^* \in f^{-1}(p^*)$.


In other words, the optimal set is the intersection of the feasible set
$A$ with the level set $f^{-1}(p^*)$.


Thus, for an optimal solution to exist

1. $p^*$ must be finite. 
1. The level set $f^{-1}(p^*)$ must be nonempty.
1. The feasible set $A$ must be nonempty.
1. The intersection of $A$ with $f^{-1}(p^*)$ must be nonempty.
```

### Coercive Functions


```{prf:definition} Coercive function
:label: def-opt-coercive-function

A proper function $f: \VV \to \RERL$ is called *coercive* over
a set $A$ if for every sequence $\{ \bx_n \}$ of $A$ such that
$ \lim_{k \to \infty} \| \bx_k \| = \infty$, we have $\lim_{k \to \infty} f(\bx_k) = \infty$.

If $f$ is coercive over the entire vector space $\VV$, we say that $f$ is *coercive*.
```

One way to think about coercive functions is that they grow rapidly
at the extremes of the domain on which they are defined.


```{prf:remark} Level sets of coercive functions
:label: res-opt-coercive-level-sets

Let $f : \VV \to \RERL$ be a coercive proper function. Let $a \in \RR$.
If the level set $f^{-1}(a)$ is nonempty, then it is bounded. 

In other words, all nonempty level sets of a coercive function are bounded.
```

```{prf:proof}
For contradiction, assume that there exists $a \in \RR$ such that $A = f^{-1}(a)$
is unbounded.

1. Then, there exists a sequence $\{ \bx_k \}$ of $A$ such that
   $ \lim_{k \to \infty} \| \bx_k \| = \infty$.
1. Since $f$ is coercive, hence $\lim_{k \to \infty} f(\bx_k) = \infty$. 
1. But, by definition, $f(\bx_k) = a$. 
1. Hence $\lim_{k \to \infty} f(\bx_k) = a$.
1. We have a contradiction.
1. Hence, $f^{-1}(a)$ must be bounded.
```

```{prf:remark} Sublevel sets of coercive functions
:label: res-opt-coercive-sublevel-sets

Let $f : \VV \to \RERL$ be a coercive proper function with $S = \dom f$.
For every $r \in \RR$, define the sublevel set
$S_r$ as $\{ \bx \in S \ST  f(\bx) \leq r \}$.
If $S_r$ is nonempty, then it is bounded. 

In other words, all nonempty sublevel sets of a coercive function are bounded.
```

```{prf:proof}
For contradiction, assume that there exists $r \in \RR$ such that $S_r$
is unbounded.

1. Then, there exists a sequence $\{ \bx_k \}$ of $S_r$ such that
   $ \lim_{k \to \infty} \| \bx_k \| = \infty$.
1. Since $f$ is coercive, hence $\lim_{k \to \infty} f(\bx_k) = \infty$. 
1. But, by definition, $f(\bx_k) \leq r$. 
1. Hence $\lim_{k \to \infty} f(\bx_k) \leq r$.
1. We have a contradiction.
1. Hence, $S_r$ must be bounded.
```


### Weierstrass' Theorem

In this subsection, we examine the problem of unconstrained
minimization of a proper closed function.
Recall from {prf:ref}`def-ms-closed-function` that a function
is called closed if all its sublevel sets are closed.


```{prf:theorem} Unconstrained minimization of a proper closed function
:label: res-opt-proper-closed-unconstrained-min

Let $\VV$ be a real $n$-dim normed linear space.
Let $f : \VV \to \RERL$ be a proper closed function with $S = \dom f$.

Let $p^* = \inf_{\bx \in \VV} f(\bx)$.
Let $X = f^{-1}(p^*)$ be the set of minimizers of $f$ (over all of $\VV$).
For every $p \in \RR$, let $S_p$ denote the sublevel set $\{ \bx \ST f(\bx) \leq p \}$.
Then,

1. $p^* < \infty$.
1. $X = \bigcap_{p > p^*} S_p$.
1. $X$ is closed.
```

```{prf:proof}

We show that $p^* < \infty$.

1. Since $f$ is proper, hence $S$ is nonempty. 
1. Thus, there exists $\bx \in S$ such that $f(\bx) < \infty$.
1. Hence, $p^* = \inf_{\bx \in \VV} f(\bx) < \infty$.

Let $Y = \bigcap_{p > p^*} S_p$.
We have to show that $X = Y$.

We first show that $X \subseteq Y$.

1. let $\bx \in X$.
1. Then, $f(\bx) = p^*$.
1. Then, $f(\bx) < p$ for every $p > p^*$.
1. Hence, $\bx \in S_p$ for every $p > p^*$.
1. Thus, $\bx \in Y$.
1. Thus, $X \subseteq Y$.

We now show that $Y \subseteq X$.

1. Let $\bx \in Y$.
1. Then, $f(\bx) = p^*$ must hold true.
1. $f(\bx)$ cannot be smaller than $p^*$ since by definition 
   $p^* = \inf f(\bx)$.
1. Thus, $f(\bx) \geq p^*$ must hold true.
1. Now, for contradiction, assume that $f(\bx) > p^*$.
   1. Let $q = f(\bx)$.
   1. Let $p = \frac{p^* + q}{2}$.
   1. Then, $p^* < p < q$.
   1. Hence, $\bx \notin S_p$.
   1. But then, $\bx \notin Y$ since $Y \subseteq S_p$ as $p > p^*$. 
   1. A contradiction.
1. Thus, the only allowed value for $f(\bx)$ is $p^*$.
1. Thus, $\bx \in X$.
1. Thus, $Y \subseteq X$.
1. Thus, 

   $$
   X = f^{-1}(p^*) = Y = \bigcap_{p > p^*} S_p.
   $$

We show that $X$ is closed.

1. If $X$ is empty, then it is closed by definition.
1. Otherwise, $X$ is an intersection of sublevel sets.
1. Since $f$ is closed, its sublevel sets are closed.
1. Hence $S_p$ is closed for every $p$.
1. Thus, $X$ is an intersection of closed sets.
1. Thus, $X$ is closed.
```



```{prf:theorem} Weierstrass' theorem
:label: res-opt-weierstrass-theorem

Let $\VV$ be a real $n$-dim normed linear space.
Let $f : \VV \to \RERL$ be a proper closed function with $S = \dom f$.

Let $p^* = \inf_{\bx \in \VV} f(\bx)$.
Let $X = f^{-1}(p^*)$ be the set of minimizers of $f$ (over all of $\VV$).
For every $p \in \RR$, let $S_p$ denote the sublevel set $\{ \bx \ST f(\bx) \leq p \}$.

Assume that one of the following conditions are true.


1. $S = \dom f$ is closed and bounded.
1. There exists a scalar $r \in \RR$ such that the sublevel set
   $ S_r = \{ \bx \ST f(\bx) \leq r \}$ is nonempty and bounded.
1. $f$ is coercive.

Then, $X$ (the set of minimizers of $f$) is nonempty and compact.
```

```{prf:proof}

If there exists $\bx \in S$ such that $f(\bx) = p^*$,
then $X$ is nonempty.
To show that $X$ is compact, we just need to show
that it is closed and bounded.
By {prf:ref}`res-la-ndim-compact-closed-bounded`,
every closed and bounded subset of $\VV$ which is a real
$n$-dimensional normed linear space is compact.
By {prf:ref}`res-opt-proper-closed-unconstrained-min`, $X$ is also closed.
Thus, we just need to show that $X$ is bounded.


Assume that condition (1) holds.

1. Since $f$ is proper, hence $S$ is nonempty.
1. Consider a sequence $\{ \bx_k \}$ of $S$ such that
   $\lim_{k \to \infty} f(\bx_k) = p^*$.
1. Since $S$ is bounded, hence $\{ \bx_k \}$ has a convergent subsequence
   by Bolzano-Weierstrass theorem
   ({prf:ref}`res-la-bounded-seq-bolzano-weierstrass`).
1. Let $\{ \bx_l \}$ be the convergent subsequence of $\{ \bx_k \}$ with
   $\lim \bx_l = \bx^*$.
1. Since $S$ is closed, hence $\bx^* \in S$.
1. Since $\{ f(\bx_k) \}$ is  convergent and $\{ f(\bx_l) \}$ is
   a subsequence of $\{ f(\bx_k) \}$, hence
   
   $$
   \lim_{l \to \infty} f(\bx_l) = \lim_{k \to \infty} f(\bx_k) = p^*.
   $$
1. Since $f$ is closed, hence it is lower semicontinuous (l.s.c.) at $\bx^* \in S$
   (see {prf:ref}`res-ms-func-lsc-closed-func`).
1. Also, note that since $\{ f(\bx_k) \}$ is convergent, hence
   
   $$
   \liminf_{l \to \infty} f(\bx_l) =  \lim_{l \to \infty} f(\bx_l).
   $$
1. Since $f$ is l.s.c. at $\bx^* \in S$, hence by {prf:ref}`res-ms-semicont-seq-converge`,
   
   $$
   f(\bx^*) \leq \liminf_{l \to \infty} f(\bx_l)
   = \lim_{l \to \infty} f(\bx_l) 
   = \liminf_{k \to \infty} f(\bx_k) = p^*.
   $$
1. Since $p^*$ is the infimum value of $f$, hence $f(\bx^*)$ cannot be smaller than $p^*$.
1. Thus, $f(\bx^*) = p^*$ must be true.
1. Thus, $f(\bx^*) = p^*$ means that $\bx^*$ is an optimal solution for the
   minimization of $f$.
1. Thus, the set $X = f^{-1}(p^*)$ is nonempty.
1. $X$ is bounded since $S$ is bounded by hypothesis.
1. Since $X$ is closed and bounded. Hence, $X$ is compact.

Assume that condition (2) holds.

1. The sublevel set $S_r$ is nonempty and bounded.
1. Since $f$ is closed, hence $S_r$ is also closed.
1. Consider the restriction of $f$ on $S_r$ given by

   $$
   \tilde{f} = \begin{cases} 
   f(\bx), & f(\bx) \leq r \\
   \infty, & \text{ otherwise }.
   \end{cases}
   $$
1. Then, $\dom \tilde{f} = S_r$. Thus, $\dom \tilde{f}$ is nonempty, closed and bounded.
1. Then, $\tilde{f}$ never takes the value $-\infty$ and is not identically $\infty$.
   Hence, $\tilde{f}$ is a proper function.
1. Since $f$ is closed, hence sublevel sets of $\tilde{f}$ are also closed.
   1. For any $p > r$, the sublevel set of $\tilde{f}$ is identical to $S_r$.
   1. For any $p \leq r$, the sublevel set of $\tilde{f}$ is identical to $S_p$,
      the corresponding sublevel set of $f$.
1. Thus, $\tilde{f}$ is closed too.
1. Applying condition (1) on $\tilde{f}$, the set of minimizers of $\tilde{f}$ is
   nonempty and compact.
1. We also note that the minimizers of $f$ are identical to the minimizers of $\tilde{f}$.
1. Thus, the set of minimizers of $f$ is nonempty and closed.

Assume that condition (3) holds.

1. Since $f$ is proper, hence it has some nonempty sublevel sets.
1. Let $r \in \RR$ be one such scalar such that the sublevel set
   $S_r = \{ \bx \in S \ST f(\bx) \leq r \}$ is nonempty.
1. By {prf:ref}`res-opt-coercive-sublevel-sets`, the nonempty sublevel sets
   of $f$ are bounded. Hence, $S_r$ is bounded.
1. Then, by applying condition (2), the set of minimizers of $f$ is
   nonempty and compact.
```


```{prf:corollary} Minimizing a proper closed function over a closed set
:label: res-opt-min-proper-func-closed-set

Let $f : \VV \to \RERL$ be a proper closed function with $S = \dom f$.
Let $A \subseteq S$ be a nonempty closed set. 
Consider the problem of minimizing $f$ over $A$.

Further, assume that one of the following conditions are true.


1. $A$ is bounded.
1. There exists a scalar $r \in \RR$ such that the set
   $\{ \bx \in A \ST f(\bx) \leq r \}$ is nonempty and bounded.
1. $f$ is coercive over $A$.

Then, the set of minimizers of $f$ over $A$ is nonempty and compact.
```

```{prf:proof}
We define a restriction $g : \VV \to \RERL$ of $f$ over the set $A$ as follows

$$
g(\bx) = \begin{cases}
f(\bx), & \bx \in A \\
\infty, & \text{ otherwise }.
\end{cases}
$$

1. $\dom g = A$. Thus, $\dom g$ is closed.
1. Since $f$ never takes the value $-\infty$, hence $g$ also never takes the value $-\infty$.
1. Since $A$ is nonempty, hence there exists $\bx \in \VV$ such that $g(\bx) < \infty$.
1. Hence, $g$ is a proper function.
1. Also, note that the set $\{ \bx \in A \ST f(\bx) \leq r \}$ is
   nothing but the sublevel set of $g$ for the scalar $r$.

   $$
   \{ \bx  \ST g(\bx) \leq r \} = A \cap \{ \bx \ST f(\bx) \leq r \}.
   $$
1. Since $f$ is closed, all its sublevel sets are closed. 
1. $A$ is closed, hence $ A \cap \{ \bx \ST f(\bx) \leq r \}$ is also closed.
1. Hence, all the sublevel sets of $g$ are also closed. Hence, $g$ is also closed.
1. The set of minimizers of $f$ over $A$ is nothing but the set of minimizers
   of $g$.
1. If $f$ is coercive over $A$, then $g$ is coercive (over its entire domain). 

Thus, applying {prf:ref}`res-opt-weierstrass-theorem`,
the set of minimizers of $g$ is nonempty and compact.
So is the set of minimizers of $f$ over $A$.
```

```{prf:corollary} Minimizing a real valued l.s.c. function over a closed set
:label: res-opt-min-rv-func-closed-set

Let $f : \VV \to \RR$ be a real valued function with $\dom f = \VV$.
Let $A \subseteq \VV$ be a nonempty closed set. 
Assume that $f$ is lower semicontinuous over $A$.
Consider the problem of minimizing $f$ over $A$.

Further, assume that one of the following conditions are true.


1. $A$ is bounded.
1. There exists a scalar $r \in \RR$ such that the set
   $\{ \bx \in A \ST f(\bx) \leq r \}$ is nonempty and bounded.
1. $f$ is coercive over $A$.

Then, the set of minimizers of $f$ over $A$ is nonempty and compact.
```

```{prf:proof}
We define a restriction $g : \VV \to \RERL$ of $f$ over the set $A$ as follows

$$
g(\bx) = \begin{cases}
f(\bx), & \bx \in A \\
\infty, & \text{ otherwise }.
\end{cases}
$$

1. $\dom g = A$. Thus, $\dom g$ is closed.
1. Since $f$ is real valued hence $g$ also never takes the value $-\infty$.
1. Since $A$ is nonempty, hence there exists $\bx \in \VV$ such that $g(\bx) < \infty$.
1. Hence, $g$ is a proper function.
1. Since $f$ is l.s.c. on $A$, hence $g$ is closed.
1. Also, note that the set $\{ \bx \in A \ST f(\bx) \leq r \}$ is
   nothing but the sublevel set of $g$ for the scalar $r$.
1. The set of minimizers of $f$ over $A$ is nothing but the set of minimizers
   of $g$.
1. If $f$ is coercive over $A$, then $g$ is coercive (over its entire domain). 

Thus, applying {prf:ref}`res-opt-weierstrass-theorem`,
the set of minimizers of $g$ is nonempty and compact.
So is the set of minimizers of $f$ over $A$.
```

