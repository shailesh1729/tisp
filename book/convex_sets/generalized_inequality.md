# Generalized Inequalities

A {prf:ref}`proper cone <def-proper-cone>` $K$ can be used to define 
a *generalized inequality*, which is a partial ordering on $\RR^n$.

````{prf:definition}
:label: def-generalized-inequality

Let $K \subseteq \RR^n$ be a proper cone. A *partial ordering* on
$\RR^n$ associated with the proper cone $K$ is defined as

$$
    x \preceq_{K} y \iff y - x \in K.
$$

We also write $x \succeq_K y$ if $y \preceq_K x$. This is also known
as a *generalized inequality*.

A *strict partial ordering* on $\RR^n$ associated with the proper cone $K$
is defined as

$$
    x \prec_{K} y \iff y - x \in \Interior{K}.
$$

where $\Interior{K}$ is the interior of $K$.
We also write $x \succ_K y$ if $y \prec_K x$.
This is also known as a *strict generalized inequality*.

````

When $K = \RR_+$, then $\preceq_K$ is same as usual $\leq$
and $\prec_K$ is same as usual $<$ operators on $\RR_+$.

````{prf:example} Nonnegative orthant and component-wise inequality
:label: ex-cvx-nng-orth-component-wise-inequality

The nonnegative orthant $K=\RR_+^n$ is a proper cone. Then the
associated generalized inequality $\preceq_{K}$ means that

$$
    x \preceq_K y \implies (y-x) \in \RR_+^n
    \implies x_i \leq y_i \Forall i= 1,\dots,n.
$$

This is usually known as *component-wise inequality* and
usually denoted as $x \preceq y$.

````

````{prf:example} Positive semidefinite cone and matrix inequality
:label: ex-cvx-psd-cone-matrix-inequality

The positive semidefinite cone $S_+^n \subseteq S^n$ is a proper
cone in the vector space $S^n$.

The associated generalized inequality means

$$
    X \preceq_{S_+^n} Y \implies Y - X \in S_+^n
$$

i.e. $Y - X$ is positive semidefinite.
This is also usually denoted as $X \preceq Y$.
````






## Minima and maxima



The generalized inequalities ($\preceq_K, \prec_K$) w.r.t. the proper cone
$K \subset \RR^n$ 
define
a partial ordering over any arbitrary set $S \subseteq \RR^n$.

But since they may not enforce a total ordering on $S$,  not every
pair of elements $x, y\in S$ may be related by $\preceq_K$ or $\prec_K$.

````{prf:example} Partial ordering with nonnegative orthant cone
:label: ex-cvx-nng-orthant-partial-ordering

Let $K = \RR^2_+ \subset \RR^2$.
Let $x_1 = (2,3), x_2 = (4, 5), x_3=(-3, 5)$. Then we have

*  $x_1 \prec x_2$, $x_2 \succ x_1$ and $x_3 \preceq x_2$.
*  But neither $x_1 \preceq x_3$ nor $x_1 \succeq x_3$ holds.
*  In general For any $x , y \in \RR^2$, $x \preceq y$ if and only if
$y$ is to the right and above of $x$ in the $\RR^2$ plane.
*  If $y$ is to the right but below or $y$ is above but to the left of $x$, then
no ordering holds.

````

````{prf:definition}
:label: def-cvx-generalized-inequality-minimum-element

We say that $x \in S \subseteq \RR^n$ is *the minimum element* of $S$
w.r.t. the generalized inequality $\preceq_K$ if for every $ y \in S$ we have
$x \preceq y$.

````


*  $x$ must belong to $S$.
*  It is highly possible that there is no minimum element in $S$.
*  If a set $S$ has a minimum element, then by definition it is unique (Prove it!).


````{prf:definition}
:label: def-cvx-generalized-inequality-maximum-element

We say that $x \in S \subseteq \RR^n$ is *the maximum element* of $S$
w.r.t. the generalized inequality $\preceq_K$ if for every $ y \in S$ we have
$y \preceq x$.

````


*  $x$ must belong to $S$.
*  It is highly possible that there is no maximum element in $S$.
*  If a set $S$ has a maximum element, then by definition it is unique.


````{prf:example} Minimum element
:label: ex-cvx-gen-inequality-minimum-element

Consider $K = \RR^n_+$ and $S = \RR^n_+$. Then $0 \in S$ is the minimum element
since $0 \preceq x \Forall x \in \RR^n_+$.
````


````{prf:example} Maximum element
:label: ex-cvx-gen-inequality-maximum-element

Consider $K = \RR^n_+$ and $S = \{x | x_i \leq 0 \Forall i=1,\dots,n\}$.
Then $0 \in S$ is the maximum element
since $x \preceq 0 \Forall x \in S$.
````




There are many sets for which no minimum element exists. In this context
we can define a slightly weaker concept known as minimal element.

````{prf:definition}
:label: def-cvx-gen-inequality-minimal-element

An element $x\in S$ is called a *minimal element* of $S$
w.r.t. the generalized inequality $\preceq_K$ if there is no
element $y \in S$ distinct from $x$ such that $y \preceq_K x$.
In other words $y \preceq_K x \implies y = x$.

````

````{prf:definition}
:label: def-cvx-gen-inequality-maximal-element

An element $x\in S$ is called a *maximal element* of $S$
w.r.t. the generalized inequality $\preceq_K$ if there is no
element $y \in S$ distinct from $x$ such that $x \preceq_K y$.
In other words $x \preceq_K y \implies y = x$.

````


*  The minimal or maximal element $x$ must belong to $S$.
*  It is highly possible that there is no minimal or maximal element in $S$.
*  Minimal or maximal element need not be unique. A set may have many minimal or maximal elements.


````{prf:lemma}
:label: res-cvx-gen-inequality-minimum-element-charac

A point $x \in S$ is the minimum element of $S$ if and only if

$$
S \subseteq x + K
$$

````

````{prf:proof}
Let $x \in S$ be the minimum element.
Then by definition $x \preceq_K y \Forall y \in S$.  Thus

$$
    & y - x \in K \Forall y \in S \\
    \implies & \text{ there exists some } k \in K  \Forall y \in S \text{ such that } y = x + k\\
    \implies & y \in x + K \Forall y \in S\\
    \implies & S \subseteq x + K.
$$

Note that $k \in K$ would be distinct for each $ y \in S$.

Now let us prove the converse.

Let $S \subseteq x + K$ where $x \in S$. Thus

$$
    & \exists k \in K \text{ such that } y = x + k \Forall y \in S\\
    \implies & y - x = k \in K  \Forall y \in S\\
    \implies & x \preceq_K y \Forall y \in S.
$$

Thus $x$ is the minimum element of $S$ since there can be only one minimum element
of S.

````

$x + K $ denotes all the points that are comparable to $x$ and greater than
or equal to $x$ according to $\preceq_K$.

````{prf:lemma}
:label: res-cvx-gen-inequality-minimal-point-charac

A point $x \in S$ is a minimal point if and only if

$$
    \{ x - K \} \cap S = \{ x \}.
$$

````

````{prf:proof}
Let $x \in S$ be a minimal element of $S$. Thus there is no
element $y \in S$ distinct from $x$ such that $y \preceq_K x$.

Consider the set $R = x - K = \{x - k | k \in K \}$.

$$
    r \in R \iff r = x - k \text { for some } k \in K
    \iff x - r \in K \iff  r \preceq_K x.
$$

Thus $x - K$ consists of all points $r \in \RR^n$ which satisfy
$ r \preceq_K x$. But there is only one such point in $S$ namely $x$
which satisfies this. Hence

$$
    \{ x - K \} \cap S = \{ x \}.
$$

Now let us assume that $\{ x - K \} \cap S = \{ x \}$.  Thus the only
point $y \in S$ which satisfies $y \preceq_K x$ is $x$ itself.
Hence $x$ is a minimal element of $S$.
````

$x - K$ represents the set of points that are comparable to $x$ and are 
less than or equal to $x$ according to $\preceq_K$.
