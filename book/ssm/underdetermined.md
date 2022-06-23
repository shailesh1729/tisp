(sec:ssm:underdetermined)= 
# Underdetermined Linear Systems
The discussion in this section is primarily based on 
chapter 1 of {cite}`elad2010sparse`.

1. Consider a matrix $\Phi \in \CC^{M \times N}$ with $M < N$. 
1. Define an under-determined system of linear equations:

   $$
   \Phi \bx = \by
   $$
   where $\by \in \CC^M$ is known and $\bx \in \CC^N$ is unknown. 

1. This system has $N$ unknowns and $M$ linear equations. 
1. There are more unknowns than equations.
1. Let the columns of $\Phi$ be given by $\phi_1, \phi_2, \dots, \phi_N$.
1. Column space of $\Phi$ (vector space spanned by all columns of $\Phi$)
   is denoted by $\ColSpace(\Phi)$; i.e.,

    $$
    \ColSpace(\Phi) = \sum_{i=1}^{N} c_i \phi_i, \quad c_i \in \CC.
    $$
1. We know that $\ColSpace(\Phi) \subset \CC^M$. 
1. Clearly $\Phi \bx \in \ColSpace(\Phi)$ for every $\bx \in \CC^N$.
1. Thus if $\by \notin \ColSpace(\Phi)$ then we have no solution.
1. But, if $\by \in \ColSpace(\Phi)$ then we have infinite number of solutions.
1. Let $\NullSpace(\Phi)$ represent the null space of $\Phi$ given by 

    $$
    \NullSpace(\Phi) = \{ \bx \in \CC^N : \Phi \bx = \bzero \}.
    $$
1. Let $\widehat{\bx}$ be a solution of $\by = \Phi \bx$. 
1. Let $\bz \in \NullSpace(\Phi)$.
1. Then 

    $$
    \Phi (\widehat{\bx} + \bz) = \Phi \widehat{\bx} + \Phi \bz = \by + \bzero  = \by.
    $$
1. Hence $\widehat{\bx} + \bz$ is also a solution of of the system $\Phi \bx = \by$.
1. Thus the set $\widehat{x} + \NullSpace(\Phi)$
   forms the complete set of infinite solutions to the
   problem $\by = \Phi \bx$ where

    $$
    \widehat{\bx} + \NullSpace(\Phi) = \{\widehat{\bx} + \bz \ST \bz \in \NullSpace(\Phi)\}.
    $$

`````{prf:example} An under-determined system
:label: ex-ssm-underdetermined-system-1

As a running example in this section,
we will consider a simple under-determined system
in $\RR^2$. 

The system is specified by

$$
\Phi  = 
\begin{bmatrix}
3 & 4
\end{bmatrix}
$$
and

$$
\bx = \begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
$$
with

$$
\Phi \bx = y = 12.
$$
where $\bx$ is unknown and $y$ is known.
Alternatively 

$$
\begin{bmatrix}
3 & 4
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
= 12
$$
or more simply

$$
3 x_1 + 4 x_2 = 12.
$$
The solution space of this system is a line in $\RR^2$.

````{figure} images/underdetermined_system.png
---
name: fig:ssm:ex:underdetermined:system
---
An underdetermined system
````

Specification of the under-determined system as above,
doesn't give us any reason to pick one
particular point on the line as the preferred solution.

Two specific solutions are of interest

1. $(x_1, x_2) = (4,0)$ lies on the $x_1$ axis.
1. $(x_1, x_2) = (0,3)$ lies on the $x_2$ axis.

In both of these solutions, one component is 0,
thus leading these solutions to be sparse.

It is easy to visualize sparsity in this simplified 2-dimensional setup
but situation becomes
more difficult when we are looking at high dimensional signal spaces. 
We need well defined criteria to promote sparse solutions.
`````


 
## Regularization

Are all these solutions equivalent or can we say  that one solution
is better than the other in some sense? 
In order to suggest that some solution is better than other solutions,
we need to define a criteria for comparing two solutions.

In optimization theory, this idea is known as *regularization*. 

We define a cost function $J(x) : \CC^N \to \RR$ which defines the *desirability*
of a given solution $x$ out
of infinitely possible solutions.
The higher the cost, lower is the desirability of the solution.

Thus the goal of the optimization problem is to find a desired $\bx$
with minimum possible cost.

We can write this optimization problem as

```{math}
:label: eq:ssm:cost:function:minimization:problem
& \underset{\bx}{\text{minimize}} 
& &  J(\bx) \\
& \text{subject to }
& &  \by = \Phi \bx.
```
If $J(\bx)$ is convex, then its possible to find a global minimum cost solution
over the solution set.

If $J(\bx)$ is not convex, then it may not be possible to find a
global minimum, we may have to settle with a local minimum. 

A variety of such cost function based criteria can be considered. 

 
## $\ell_2$ Regularization

One of the most common criteria is to choose a solution with the smallest $\ell_2$ norm.

`````{div}
The problem can then be reformulated as an optimization problem 

````{math}
:label: eq:ssm:l2:norm:minimization:problem
& \underset{\bx}{\text{minimize}} 
& &  \| \bx \|_2 \\
& \text{subject to }
& &  \by = \Phi \bx.
````
We can see that minimizing $\| \bx \|_2$ is same as minimizing its square 
$\| \bx \|_2^2 = \bx^H \bx$; i.e., both functions have exactly the
same minimizer under the given constraints.

Hence an equivalent formulation is 

````{math}
& \underset{\bx}{\text{minimize}} 
& &  \bx^H \bx \\
& \text{subject to }
& &  \by = \Phi \bx.
````
`````

````{prf:example} Minimum $\ell_2$ norm solution for an under-determined system
:label: ex-ssm-underdetermined-system-l2-min

We continue with our running example.

We can write $\bx_2$ as

$$
\bx_2 = 3 - \frac{3}{4} \bx_1.
$$
With this definition the squared $\ell_2$ norm of $x$ becomes

$$
\| \bx \|_2^2 = x_1^2 + x_2^2
&=  x_1^2 + \left ( 
3 - \frac{3}{4} x_1 \right )^2\\
& = \frac{25}{16} x_1^2 - \frac{9}{2} x_1 + 9.
$$

Minimizing  $\| \bx \|_2^2$ over all $\bx$ is same as minimizing over all $x_1$.

Since $\| \bx \|_2^2$ is a quadratic function of $x_1$,
we can simply differentiate
it and equate to 0 giving us

$$
\frac{25}{8} x_1 -  \frac{9}{2} = 0  \implies x_1  = \frac{36}{25} = 1.44.
$$
This gives us

$$
x_2 = \frac{48}{25} = 1.92.
$$

Thus the optimal $\ell_2$ norm solution is obtained at $(x_1, x_2) = (1.44, 1.92)$.

We note that the minimum $\ell_2$ norm at this solution is

$$
\| \bx \|_2 = \frac{12}{5} = 2.4.
$$

It is instructive to note that the $\ell_2$ norm cost function prefers
a non-sparse solution to the optimization problem.

We can view this solution graphically by drawing $\ell_2$ norm balls of different radii. 
The ball which just touches the solution space line (i.e. the line is tangent to the ball)
gives us the optimal solution. 

```{figure} images/underdetermined_system_l2_balls.png
---
name: fig:ssm:ex:underdetermined:system:min:l2:norm
---
Minimum $\ell_2$ norm solution for the under-determined system $3 x_1  + 4 x_2 = 12$}
```

All other norm balls either don't touch the solution line at all, or they cross it at
exactly two points.
````

````{prf:remark} Least squares via Lagrangian multipliers
:label: res-ssm-underdetermined-l2-min-lm

A formal solution to $\ell_2$ norm minimization problem can be easily obtained using
Lagrange multipliers.

We define the Lagrangian

$$
\LLL(x) = \|\bx\|_2^2 + \lambda^H (\Phi \bx  - \by)
$$
with $\lambda \in \CC^M$ being the Lagrange multipliers for the (equality) constraint set.

Differentiating $\LLL(\bx)$ w.r.t. $\bx$ we get

$$
\frac{\partial \LLL(\bx)} {\partial \bx} = 2 \bx + \Phi^H \lambda.
$$

By equating the derivative to $\bzero$ we obtain the optimal value of $\bx$ as

$$
\bx^* = - \frac{1}{2} \Phi^H \lambda.
$$

Plugging this solution back into the constraint $\Phi \bx = \by$ gives us

$$
\Phi \bx^* = - \frac{1}{2} (\Phi \Phi^H) \lambda
= \by
\implies \lambda = -2(\Phi \Phi^H)^{-1} \by.
$$

In above we are implicitly assuming that $\Phi$ is a full rank matrix.
Hence $\Phi \Phi^H$ is invertible and positive definite.

Putting $\lambda$ back in the expression for $\bx^*$ we obtain
the well known closed form least squares solution using pseudo-inverse solution

$$
\bx^* = \Phi^H (\Phi \Phi^H)^{-1} \by = \Phi^{\dag} \by.
$$

We would like to mention that there are several iterative approaches to solve the
$\ell_2$ norm minimization
problem (like gradient descent and conjugate descent).  For large systems, they are more effective
than computing the pseudo-inverse. 

The beauty of $\ell_2$ norm minimization lies in its simplicity and availability of closed form
analytical solutions. This has led to its prevalence in various fields of science and engineering.
But $\ell_2$ norm is by no means the only suitable cost function. Rather the simplicity of $\ell_2$ norm
often drives engineers away from trying other possible cost functions. In the following, we will
look at various other possible cost functions.
````
 
### Convexity

```{div}
Convex optimization problems have a unique feature that it is possible to
find the global optimal solution if such a solution exists. 

The solution space  $ \Omega = \{\bx : \Phi \bx = \by\}$ is convex.
Thus the feasible set of solutions for the optimization problem
{eq}`eq:ssm:cost:function:minimization:problem`
is also convex. 
All it remains is to make sure that we choose a cost function
$J(x)$ which happens to be convex. 
This will ensure that a global minimum can be found through
convex optimization techniques.
Moreover, if $J(x)$ is strictly convex, then it is guaranteed
that the global minimum solution is *unique*. 
Thus even though, we may not have
a nice looking closed form expression for the solution of
a strictly convex cost function minimization problem,
the guarantee of the existence and uniqueness of solution
as well as well developed algorithms
for solving the problem make it very appealing to choose cost functions which are convex.

We recall that all $\ell_p$ norms with $p \geq 1$ are convex functions.
In particular $\ell_{\infty}$ and $\ell_1$ norms are very interesting and popular where

$$
\| x \|_{\infty} = \max\{ |x_i| \ST i=1,\dots,N \}
$$
and

$$
 \| \bx \|_1 = \sum_{i=1}^{N} |x_i|.
$$

In the following section we will attempt to find a unique solution to our 
optimization problem {eq}`eq:ssm:cost:function:minimization:problem` using $\ell_1$ norm.
```
 
## $\ell_1$ Regularization

`````{div}
In this subsection we will restrict our attention to the
Euclidean space case where $\bx \in \RR^N$,
$\Phi \in \RR^{M \times N}$ and $\by \in \RR^M$.

We choose our cost function $J(\bx) = \| \bx \|_1$.
The cost minimization problem can be reformulated as

````{math}
:label: eq:ssm:l1:norm:min:underdetermined
& \underset{\bx}{\text{minimize}} 
& &  \| \bx \|_1 \\
& \text{subject to }
& &  \Phi \bx = \by.
````
`````

````{prf:example} Minimum $\ell_1$ norm solution for an under-determined system
:label: ex-ssm-underdetermined-system-l1-min

We continue with our running example.
we can view this solution graphically by drawing $\ell_1$ norm balls of different radii. 
The ball which just touches the solution space line
gives us the optimal solution. 

```{figure} images/underdetermined_system_l1_balls.png
---
name: fig:ssm:ex:underdetermined:system:min:l1:norm
---
Minimum $\ell_1$ norm solution for the under-determined system $3 x_1  + 4 x_2 = 12$
```
As we can see from the figure the minimum $\ell_1$ norm solution is given by $(x_1,x_2)  = (0,3)$.

It is interesting to note that $\ell_1$ norm solution promotes sparser solutions while
$\ell_2$ norm solution promotes solutions in which signal energy is distributed among
all of its components.
````

```{div}
It is time to have a closer look at our cost function $J(x) = \| \bx \|_1$.
This function is convex yet not strictly convex.
``` 

````{prf:example} $\| x\|_1$ is not strictly convex
:label: ex-ssm-l1-norm-not-strict-convex

Consider again $\bx \in \RR^2$. For $\bx \in \RR_+^2$ (the first quadrant), 

$$
\| \bx \|_1 = x_1 + x_2.
$$

Hence for any $c_1, c_2 \geq 0$ and $\bx, \by \in \RR_+^2$:

$$
\|(c_1 \bx + c_2 \by)\|_1 =  (c_1 \bx + c_2 \by)_1 + (c_1 \bx + c_2 \by)_2 = c_1 \| \bx\|_1 + c_2 \| \by \|_1.
$$
Thus, $\ell_1$-norm is not strictly convex.
Consequently, a unique solution may not exist for $\ell_1$ norm minimization problem.

As an example consider the under-determined system

$$
3 x_1 + 3 x_2 = 12.
$$

1. We can easily visualize that the solution line will pass through points $(0,4)$ and
   $(4,0)$.
1. Moreover, it will be clearly parallel with $\ell_1$-norm ball of radius $4$ in
   the first quadrant.
1. This gives us infinitely possible solutions to the minimization problem
   {eq}`eq:ssm:l1:norm:min:underdetermined`.

We can still observe that 

*  these solutions are gathered in a small line segment that
   is bounded (a bounded convex set) and
*  There exist two solutions $(4,0)$ and $(0,4)$ among these solutions which have
   only 1 non-zero component.
````

For the $\ell_1$ norm minimization problem since $J(\bx)$ is not strictly convex,
hence a unique solution may not be guaranteed. In specific cases, there may be
infinitely many solutions. Yet what we can claim is

*  these solutions are gathered in a set that is bounded and convex, and
*  among these solutions, there exists at least one solution with at most
   $M$ non-zeros (as the number of constraints in $\Phi \bx = \by$).


````{prf:theorem} Existence of a sparse solution for $\ell_1$ minimization
:label: res-ssm-l1-norm-min-sparse-solution-guarantee

Let $S$ denote the solution set of
$\ell_1$ norm minimization problem {eq}`eq:ssm:l1:norm:min:underdetermined`.
$S$ contains at least one solution $\widehat{x}$ with $\| \widehat{x} \|_0 = M$.
````

````{prf:proof}
We have the following facts

*  $S$ is  convex and bounded.
*  $\Phi \bx^* = \by \, \Forall \bx^* \in S$.
*  Since $\Phi \in \RR^{M \times N}$ is full rank and $M < N$, hence $\rank \Phi = M$.

We proceed as follows.

1. Let $\bx^* \in S$ be an optimal solution with $\| \bx^* \|_0 = L > M$.
1. Consider the $L$ columns of $\Phi$ which correspond to $\supp(\bx^*)$. 
1. Since $L > M$ and $\rank \Phi = M$ hence these columns linearly dependent.
1. Thus there exists a nonzero vector $\bh \in \RR^N$ with $\supp(\bh) \subseteq \supp(\bx^*)$
   such that 
   
   $$
   \Phi \bh = \bzero.
   $$
1. Note that since we are only considering those columns of $\Phi$ which correspond to
   $\supp(\bx)$, hence we require $h_i = 0$ whenever $\bx^*_i = 0$.
1. Consider a new vector 
   
   $$
   \bx = \bx^* + \epsilon \bh
   $$
   where $\epsilon$ is small enough such that every element in $\bx$ has the same sign as $\bx^*$.
   As long as

   $$
   |\epsilon| \leq \underset{i \in \supp(\bh)}{\min} \frac{|\bx^*_i|}{|h_i|} = \epsilon_0
   $$
   such an $\bx$ can be constructed.
1. Note that $x_i = 0$ whenever $x^*_i = 0$.
1. Clearly

   $$
   \Phi \bx = \Phi (\bx^* + \epsilon \bh) = \by + \epsilon \bzero = \by.
   $$
1. Thus $\bx$ is a feasible solution to the problem {eq}`eq:ssm:l1:norm:min:underdetermined`
   though it need not be an optimal solution.
1. But since $\bx^*$ is optimal hence, we must assume that $\ell_1$ norm of $\bx$ is
   greater than or equal to the $\ell_1$ norm of $\bx^*$

   $$
   \| \bx \|_1 = \|\bx^* + \epsilon \bh \|_1  \geq \| \bx^* \|_1 \Forall |\epsilon| \leq \epsilon_0.
   $$
1. Now look at $\|\bx \|_1$ as a function of $\epsilon$ in the region $|\epsilon| \leq \epsilon_0$.
1. In this region, $\ell_1$ function is continuous and differentiable (w.r.t. $\epsilon$) since
   all vectors $\bx^* + \epsilon \bh$ have the same sign pattern. 
1. If we define $\by^* = | \bx^* |$ (the vector of absolute values), then

   $$
   \| \bx^* \|_1 = \| \by^* \|_1 = \sum_{i=1}^N y^*_i.
   $$
1. Since the sign patterns don't change, hence

   $$
   |x_i| = |x^*_i   + \epsilon h_i | = y^*_i + \epsilon h_i \sgn(x^*_i).
   $$
1. Thus


   $$
   \|\bx \|_1 &= \sum_{i=1}^N |x_i| \\
   &= \sum_{i=1}^N \left (y^*_i + \epsilon h_i \sgn(x^*_i) \right) \\
   &= \| \bx^* \|_1 + \epsilon \sum_{i=1}^N h_i \sgn(x^*_i)\\
   &= \| \bx^* \|_1 + \epsilon \bh^T \sgn(\bx^*).
   $$
1. The quantity $\bh^T \sgn(\bx^*)$ is a constant.
1. The inequality $\|\bx \|_1 \geq \| \bx^* \|_1$ 
   applies to both positive and negative values of $\epsilon$ in the region
   $|\epsilon | \leq \epsilon_0$.
1. This is possible only when inequality is in fact an equality. 
1. This implies that the addition / subtraction of $\epsilon \bh$ under these conditions
   does not change the $\ell_1$ length of the solution.
1. Thus, $\bx \in S$ is also an optimal solution.
1. This can happen only if
   
   $$
   \bh^T \sgn(\bx^*) = 0.
   $$
1. We now wish to tune $\epsilon$ such that one entry in $x^*$ gets zeroed while keeping
   the solutions $\ell_1$ length.
1. We choose $i$ corresponding to $\epsilon_0$ (defined above) and pick

   $$
   \epsilon = \frac{-x^*_i}{h_i}.
   $$
1. Clearly for the corresponding

   $$
   \bx  = \bx^* + \epsilon \bh
   $$
   the $i$-th entry is zeroed while others keep their sign and the $\ell_1$ norm is also preserved.
1. Thus, we have got a new optimal solution with $L-1$ non-zeros at the most.
1. It is possible that more than 1 entries get zeroed during this operation.
1. We can repeat this procedure till we are left with $M$ non-zero elements. 
1. Beyond this we may not proceed since $\rank \Phi = M$.
   Hence we cannot say that corresponding columns of $\Phi$ are linearly dependent.
````

We thus note that $\ell_1$ norm has a tendency to prefer sparse solutions. This is a
well known and fundamental property of linear programming.

 
## $\ell_1$ Norm Minimization as a Linear Programming Problem


We now show that {eq}`eq:ssm:l1:norm:min:underdetermined` in $\RR^N$ 
is in fact a linear programming problem.

Recalling the problem:

````{math}
& \underset{x \in \RR^N}{\text{minimize}} 
& &  \| x \|_1 \\
& \text{subject to }
& &  y = \Phi x.
````

Let us write $\bx$ as $\bu  - \bv$  where $\bu, \bv \in \RR^N$ are both non-negative vectors such that
$\bu$ takes all positive entries in $\bx$ while $\bv$ takes all the negative entries in $\bx$.

````{prf:example} $\bx = \bu - \bv$
:label: ex-ssm-split-vec-pos-neg-entries
Let 

$$
\bx = (-1, 0 , 0 , 2, 0 , 0, 0, 4, 0, 0, -3, 0 , 0 , 0 , 0, 2 , 10).
$$

Then

$$
\bu = (0, 0 , 0 , 2, 0 , 0, 0, 4, 0, 0, 0, 0 , 0 , 0 , 0, 2 , 10).
$$
And

$$
\bv = (1, 0 , 0 , 0, 0 , 0, 0, 0, 0, 0, 3, 0 , 0 , 0 , 0, 0 , 0).
$$

Clearly $\bx  = \bu - \bv$.
````

```{div}
We note here that by definition

$$
\supp(\bu) \cap \supp(\bv) = \EmptySet
$$
i.e., support of $\bu$ and $\bv$ are disjoint.

We now construct a vector

$$
\bz = \begin{bmatrix}
\bu \\ \bv
\end{bmatrix} \in \RR^{2N}.
$$

We can now verify that

$$
\| \bx \|_1 = \|\bu\|_1 + \| \bv \|_1 = \bone^T \bz.
$$
Also 

$$
\Phi \bx = \Phi (\bu - \bv) 
= \Phi \bu - \Phi \bv = 
\begin{bmatrix}
\Phi & -\Phi
\end{bmatrix}
\begin{bmatrix}
\bu \\ \bv
\end{bmatrix}
= \begin{bmatrix}
\Phi & -\Phi
\end{bmatrix} \bz 
$$ 
where  $\bz \succeq \bzero$.
```

Hence the optimization problem {eq}`eq:ssm:l1:norm:min:underdetermined` can be recast as
````{math}
:label: eq:ssm:l1:norm:min:underdetermined:as:lp
& \underset{\bz \in \RR^{2N}}{\text{minimize}} 
& &  \bone^T \bz \\
& \text{subject to }
& &  \begin{bmatrix} \Phi & -\Phi \end{bmatrix} \bz = \by\\
& \text{and }
& & \bz \succeq \bzero.
````
This optimization problem has the classic Linear Programming structure since the
objective function is affine as well as constraints are affine.

`````{prf:remark} Justification for the equivalence of the linear program
:label: res-ssm-l1-min-lin-prog-just

Let $\bz^* =\begin{bmatrix} \bu^* \\ \bv^* \end{bmatrix}$ be an optimal solution
of the linear program {eq}`eq:ssm:l1:norm:min:underdetermined:as:lp`.  

In order to show that the two optimization problems are equivalent, we need
to verify that our assumption about the decomposition of $\bx$ into positive entries in $\bu$ 
and negative entries in $\bv$ is indeed satisfied by the optimal solution $\bu^*$ and $\bv^*$.
i.e., the support of $\bu^*$ and $\bv^*$ do not overlap.

1. Since $\bz \succeq \bzero$,
   hence $\langle \bu^* , \bv^* \rangle  \geq \bzero$.
1. If support of $\bu^*$ and $\bv^*$  don't overlap,
   then we  have $\langle \bu^* , \bv^* \rangle = \bzero$.
1. And if they overlap then $\langle \bu^* , \bv^* \rangle > 0$.
1. Now for the sake of contradiction, let us assume that support of
   $\bu^*$ and $\bv^*$ do overlap for the optimal solution $\bz^*$.
1. Let $k$ be one of the indices at which both $u_k \neq 0$ and $v_k \neq 0$.
1. Since $\bz \succeq \bzero$, hence $u_k > 0$ and $v_k > 0$.
1. Without loss of generality let us assume that $u_k > v_k > 0$.
1. In the equality constraint

   $$
   \begin{bmatrix} \Phi & -\Phi \end{bmatrix} \begin{bmatrix} \bu \\ \bv \end{bmatrix} = \by
   $$
   both of these coefficients multiply the same column of $\Phi$
   with opposite signs giving us a term

   $$
    \phi_k (u_k - v_k). 
   $$
1. Now if we replace the two entries in $\bz^*$ by

   $$
    u_k'  = u_k - v_k
   $$
   and

   $$
    v_k' = 0
   $$
   to obtain an new vector $\bz'$, 
   we see that there is no impact in the equality constraint since

   $$
    \begin{bmatrix} \Phi & -\Phi \end{bmatrix} \bz' = \by.
   $$

1. Also the nonnegativity constraint

   $$
    \bz \succeq \bzero
   $$
   is satisfied for $\bz'$.
1. This means that $\bz'$ is a feasible solution.
1. On the other hand the objective function $\bone^T \bz$ value reduces by
   $2 v_k$ for $\bz'$. 
1. This contradicts our assumption that $\bz^*$ is the optimal solution.
1. Hence for the optimal solution of {eq}`eq:ssm:l1:norm:min:underdetermined:as:lp`
   we must have

   $$
    \supp(\bu^*) \cap \supp(\bv^*) = \EmptySet.
   $$
1. Thus 

   $$
    \bx^* = \bu^* - \bv^*
   $$
   is indeed the desired solution for the optimization problem
   {eq}`eq:ssm:l1:norm:min:underdetermined`.
`````


