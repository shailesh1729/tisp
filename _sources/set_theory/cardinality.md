# Cardinality

In this section, we deal with questions concerning the *size* of a set.
When do we say that two sets have same number of elements?

If we can find a one-to-one correspondence between two sets $A$ and $B$ then
we can say that the two sets $A$ and $B$ have same number of elements.

In other words, if there exists a {prf:ref}`bijective <def-st-bijective-function>` 
function $f : A \to B$, we say that $A$ and $B$ have same number of
elements.

````{prf:definition} Equivalent sets
:label: def-st-equivalent-sets

Two sets $A$ and $B$ are said to be *equivalent* (denoted as $A \sim B$)
if there exists a bijective function $f : A \to B$.
When two sets are equivalent, we say that they have *same cardinality*.
````

Note that two sets may be equivalent yet not equal to each other. 

````{prf:example} Equivalent sets

*  The set of natural numbers $\Nat$ is equivalent to the set of integers $\ZZ$.
   Consider the function $f : \Nat \to \ZZ$ given by

   $$
   f (n) =
   \left\{
        \begin{array}{ll}
            (n - 1) / 2 & \mbox{if $n$ is odd};\\
            -n / 2 & \mbox{if $n$ is even}.
        \end{array}
      \right.
   $$
   It is easy to show that this function is bijective.
*  $\Nat$ is equivalent to the set of even natural numbers $E$.
   Consider the function $f  : \Nat \to E$ given by $f(n) = 2n$. 
   This is a bijective mapping.
*  $\Nat$ is equivalent to the set of rational numbers $\QQ$.
*  The sets $\{a, b, c\}$ and $\{1,4, 9\}$ are equivalent but not equal.
````

````{prf:theorem}
:label: res-st-equivalence-is-equivalence-relation

Let $A, B, C$ be sets. Then:

1.  $A \sim A$.
1.  If $A \sim B$, then $B \sim A$.
1.  If $A \sim B$, and $B \sim C$, then $A \sim C$.

Thus it is an equivalence relation.
````

````{prf:proof}
(1). Construct a function $f : A \to A$ given by $f (a) = a \Forall a \in A$. 
This is bijective. Hence $A \sim A$.

(2). It is given that $A \sim B$. Thus, there exists a function 
$f : A \to B$ which is bijective. Thus, there exists an
{prf:ref}`inverse function <def-st-inverse-total-function>` 
$g : B \to A$ which is bijective. Thus, $B \sim A$.

(3). It is given that $A \sim B$ and $B \sim C$. 
Thus, there exist two bijective
functions $f : A \to B$ and $g : B \to C$. 
Define a function $ h : A \to C$ given by
$ h = g \circ f$. Since
{prf:ref}`composition of bijective functions is bijective <res-st-composition-of-bijective-functions>`
, $h$ is bijective. Thus, $A \sim C$.
````

## Cardinality and Natural Numbers

We now look closely at the set of natural numbers $\Nat = \{1,2,3,\dots\}$.

````{prf:definition}
:label: def-st-segment-natural-numbers

Any subset of $\Nat$ of the form $\{1,\dots, n\}$ is called a
*segment* of $\Nat$.
$n$ is called the *number of elements* in the segment or its *cardinality*.
````

```{prf:remark}
Two segments $\{1,\dots,m\}$ and $\{1,\dots,n\}$ are equivalent
only if $m= n$.
```

Thus, a proper subset of a segment cannot be equivalent to the segment.

````{prf:definition}
:label: def-finite-set

A set that is equivalent to a segment is called a *finite set*.

The *cardinality* or number of elements of a set 
which is equivalent to a segment is equal to the 
number of elements in the segment.
````

````{prf:remark}
The empty set $\EmptySet$ is also considered to be finite with zero elements.
````

````{prf:definition}
A set that is not finite is called an *infinite set*.
````

It should be noted that so far we have defined number of elements only
for sets which are equivalent to a segment.
    
````{prf:definition}
:label: def-st-countable-sets

A set $A$ is called *countable* if it is equivalent to $\Nat$,
i.e., if there exists a bijective correspondence of $\Nat$ with the
elements of $A$.
````

````{prf:definition}
:label: def-st-enumeration

A countable set $A$ is usually written as $A = \{a_1, a_2, \dots\}$
which indicates the one-to-one correspondence of $A$ with the set of 
natural numbers $\Nat$.
This notation is also known as the *enumeration* of $A$.
````

````{prf:definition}
:label: def-st-uncountable-set

An infinite set which is not countable is called an *uncountable set*.
````

With the definitions in place, we are now ready to study the connections
between countable, uncountable and finite sets.

## Well Ordering Principle

We recall some properties of natural numbers which will be 
used later.

````{prf:property} Well ordering principle
:label: res-st-well-ordering-principle

Every nonempty subset of $\Nat$ has a least element.
````

Well ordering principle is equivalent to the principle of 
mathematical induction. 

````{prf:theorem} Principle of mathematical induction
:label: res-st-principle-mathematical-induction

If a subset $S$ of $\Nat$ satisfies the following properties:

*  $1 \in S$ and
*  $n \in S \implies n + 1 \in S$,

then $S = \Nat$.
````

The principle of mathematical induction is applied as follows.
We consider a set $S \triangleq \{ n \in \Nat \ST n \text{ satisfies } P \}$ 
where $P$ is some property that the members of this set satisfy. 
We then show that $1$ satisfies the property $P$. Further, we
show that if $n$ satisfies property $P$, then $n + 1$ also 
has to satisfy $P$. 
Then, applying the principle of mathematical
induction, we claim that $S = \Nat$ i.e. every number $n \in \Nat$
satisfies the property $P$.

## Infinite Sets

````{prf:theorem}
Every infinite set contains a countable subset.
````

````{prf:proof}
Let $A$ be an infinite set. 
Clearly, $A \neq \EmptySet$. 
Pick an element $a_1 \in A$.
Consider the set $A_1 \triangleq A \setminus \{a_1 \}$. 
Since $A$ is infinite, hence $A_1$ is nonempty.
Pick an element $a_2 \in A_1$. 
Clearly, $a_2 \neq a_1$.
Consider the set $A_2 \triangleq A \setminus \{a_1, a_2 \}$. 
Again, by the same argument, since
$A$ is infinite, $A_2$ is non-empty. 
We can pick $a_3 \in A_2$. 
Proceeding in the
same way we construct a set 
$B \triangleq \{a_1, a_2, a_3, \dots \}$. 
The set is countable and by construction it is a subset of $A$.
````

````{prf:theorem}
:label: res-st-subset-of-countable-set-is-countable

Every subset of a countable set is either finite or countable. i.e. if $A$ is
countable and $B \subseteq A$, 
then either $B$ is finite or $B \sim A$.
````

````{prf:proof}
Let $A$ be a countable set and $B \subseteq A$. 
If $B$ is finite, then there is nothing to prove. 
So we consider $B$ as infinite and show that it is countable.
Since $A$ is countable, hence $A \sim \Nat$. 
Thus, $B$ is equivalent to a subset of $\Nat$. 
Without loss of generality, let us assume that $B$ is a subset of $\Nat$.
We now construct a mapping $f : \Nat \to B$ as follows. Let $b_1$ be the
least element of $B$ (which exists due to the 
    {prf:ref}`well ordering principle <res-st-well-ordering-principle>`).
We assign $f(1) = b_1$.
Now, let $b_2$ be the least element of $B \setminus \{ b_1\}$. 
We assign $f(2) = b_2$. 
Similarly, assuming that $f(1) = b_1, f(2) = b_2, \dots , f(n) = b_n$ has
been assigned, 
we assign $f(n+1) = $ the least element of $B \setminus \{b_1, \dots, b_n\}$. 
This least element again exists due to the 
{prf:ref}`well ordering principle <res-st-well-ordering-principle>`.
This completes the definition of $f$ using the 
{prf:ref}`principle of mathematical induction <res-st-principle-mathematical-induction>`. 
It is easy to show that the function is bijective.  
This proves that $B \sim \Nat$.
````

We present different characterizations of a countable set.

````{prf:theorem} Characterizations of countable sets
:label: res-countable-set-characterization

Let $A$ be an infinite set. The following are equivalent:

1.  A is countable.
1.  There exists a (partial) function $f: \Nat \to A$ that is onto.
1.  There exists a (total) function $g : A \to \Nat$ that is one-one.
````

````{prf:proof}
(1)$\implies$ (2). Since $A$ is countable, 
there exists a function $f : \Nat \to A$ which
is bijective. Choosing $B = \Nat$, we get the result.

(2)$\implies$ (3).
We are given that there exists a (partial) function $f: \Nat \to A$ that is onto.
For some $a \in A$, consider $f^{-1}(a) = \{ b \in \Nat \ST f(b) = a \}$.
Since $f$ is onto, hence $f^{-1}(a)$ is nonempty. 
Since $f^{-1}(a)$ is a subset of natural numbers, 
it has a least element due to the
{prf:ref}`well ordering principle <res-st-well-ordering-principle>`.
Further, if $a_1, a_2 \in A$ are distinct, then $f^{-1}(a_1)$
and $f^{-1}(a_2)$ are disjoint and the corresponding least elements are distinct.
Assign $g(a) = \text{ least element of } f^{-1}(a) \Forall a \in A$. 
Such a function is well defined by construction. 
Clearly, the function is one-one.

(3)$\implies$ (1).
We are given that there exists a function $g : A \to \Nat$ that is one-one.
Clearly, $A \sim g(A)$ where $g(A) \subseteq \Nat$. Since $A$ is infinite,
hence $g(A)$ is also infinite. Due to 
{prf:ref}`res-st-subset-of-countable-set-is-countable`,
$g(A)$ is countable since it is the subset of a countable set $\Nat$.
Then, $g(A) \sim \Nat$. Thus, $A \sim g(A) \sim \Nat$ and $A$ is countable.
````

````{prf:theorem} Countable union of countable sets
:label: res:st:countable-union-countable-sets

Let $\{A_1, A_2, \dots \}$ be a countable family of sets where each $A_i$ is a countable set. Then

$$
    A = \bigcup_{i=1}^{\infty} A_i
$$

is countable.
````
````{prf:proof}
Let $A_n = \{a_1^n, a_2^n, \dots\} \Forall n \in \Nat$. Further, let
$B = \{2^k 3^n : k, n \in \Nat \}$. Note that every element of $B$ is a natural number,
hence $B \subseteq \Nat$. Since $B$ is infinite, hence by   {ref}`here <res:set:subset_of_countable_set>`
$B$ is countable, i.e. $B \sim \Nat$. 
We note that if $b_1 = 2^{k_1} 3^{n_1}$ and $b_2 = 2^{k_2} 3^{n_2}$,
then $b_1 = b_2$ if and only if $k_1 = k_2$ and $n_1 = n_2$. 
Now define a mapping $f : \Nat \to A$ with $\dom f = B$, given by
$f (2^k 3^n) = a^n_k$ (picking $k$-th element from $n$-th set). 
Clearly, $f$ is well-defined and onto.
Thus, using {prf:ref}`res-countable-set-characterization`, $A$ is countable.
````

(res:set:finite_cartesian_product_of_countable_sets)=
````{prf:theorem}

Let $\{A_1, A_2, \dots, A_n \}$ be a finite collection of sets such that each $A_i$ is countable.
Then their Cartesian product $A = A_1 \times A_2 \times \dots \times A_n$ is countable.
````
````{prf:proof}
Let $A_i = \{a_1^i, a_2^i, \dots\} \Forall 1 \leq i \leq n$. Choose $n$ distinct prime
numbers $p_1, p_2, \dots, p_n$. Consider the set
$B  = \{p_1^{k_1}p_2^{k_2} \dots p_n^{k_n} : k_1, k_2, \dots, k_n \in \Nat \}$.
Clearly, $B \subset \Nat$.
Define a function $f : A \to \Nat $ as

$$
    f (a^1_{k_1}, a^2_{k_2}, \dots, a^n_{k_n}) = p_1^{k_1}p_2^{k_2} \dots p_n^{k_n}.
$$

By fundamental theorem of arithmetic, every natural number has a unique prime factorization. Thus,
$f$ is one-one. Invoking {ref}`here <res:set:countable_set_characterization>`, $A$ is countable.
````

(res:set:rationals_countable)=
````{prf:theorem}

The set of rational numbers $\QQ$ is countable.
````
````{prf:proof}
Let $\frac{p}{q}$ be a positive rational number with $p > 0$ and $q > 0$ having no common factor.
Consider a mapping $f(\frac{p}{q})  = 2^p 3^q$. This is a one-one mapping into natural numbers.
Hence invoking {ref}`here <res:set:countable_set_characterization>`, the set of positive rational
numbers is countable. Similarly, the set of negative rational numbers is countable.
Invoking {ref}`here <res:set:countable_union_countable_sets>`, $\QQ$ is countable.
````

(res:set:finite_subsets_countable)=
````{prf:theorem}
The set of all finite subsets of $\Nat$ is countable.

````
````{prf:proof}
Let $F$ denote the set of finite subsets of $\Nat$. Let $f \in F$. Then
we can write $f = \{n_1, \dots, n_k\}$ where $k$ is the number of elements
in $f$. Consider the sequence of prime numbers $\{p_n\}$ where $p_n$ denotes
$n$-th prime number. Now, define a mapping $g : F \to \Nat$ as

$$
    g (f ) = \prod_{i=1}^k p_{n_i}.
$$

The mapping $g$ is one-one, since the prime decomposition of a natural number
is unique. Hence invoking {ref}`here <res:set:countable_set_characterization>`, $F$ is countable.
````

(res:set:finite_subsets_of_countable_set_is_countable)=
````{prf:corollary}

The set of all finite subsets of a countable set is countable.
````

````{prf:definition}
We say that $A \preceq B$ whenever there exists a one-one function $f : A \to B$.
In other words, $A$ is equivalent to a subset of $B$.
````
In this sense, $B$ has at least as many elements as $A$.
````{prf:theorem}
The relation $\preceq$ satisfies following properties
[label=*\roman*.*]
*  $A \preceq A$ for all sets $A$.
*  If $A \preceq B$ and $b \preceq C$, then $A \preceq C$.
*  If $A \preceq B$ and $B \preceq A$, then $A \sim B$.

````
````{prf:proof}
(i). We can use the identity function $f (a ) = a \Forall a \in A$.

(ii). Straightforward application of the result that
{ref}`composition of injective functions is injective <res:composition_of_one_one_functions>`.

(iii). Straightforward application of
{ref}`Schr{\"o <res:function:schroder_bernstein_theorem>`der-Bernstein theorem}.
````

(res:set:set_power_set_cardinality)=
````{prf:theorem}

If $A$ is a set, then $A \preceq \Power (A)$ and $A \nsim \Power (A)$.
````
````{prf:proof}
If $A = \EmptySet$, then $\Power(A) = \{ \EmptySet\}$ and the result is trivial.
So, lets consider non-empty $A$.
We can choose $f : A \to \Power(A)$ given by $f (x) = \{ x\} \Forall x \in A$. This
is clearly a one-one function leading to $A \preceq \Power (A)$.

Now for the sake of contradiction, lets us assume that $A \sim \Power (A)$. Then,
there exists a bijective function $g : A \to \Power(A)$.
Consider the set $B = \{ a \in A : a \notin g(a) \}$.
Since $B \subseteq A$, and $g$ is bijective, there exists
$a \in A$ such that $g (a) = B$.

Now if $a \in B$ then $a \notin g(a) = B$.
And if $a \notin B$, then $a \in g(a) = B$.
This is impossible, hence $A \nsim \Power(A)$.
````

(def:set:cardinality)=
````{prf:definition}

For every set $A$ a symbol (playing the role of a number) can be assigned that
designates the number of elements in the set. This number is known as *cardinal number*
of the set and is denoted by \Card{A} or $| A |$. It is also known as *cardinality*.
````
Note that the cardinal numbers are different from natural numbers, real numbers etc.
If $A$ is finite, with $A = \{a_1, a_2, \dots, a_n \}$, then $\Card{A} = n$.
We use the symbol $\aleph_0$ to denote the cardinality of $\Nat$. By saying
$A$ has the cardinality of $\aleph_0$, we simply mean that $A \sim \Nat$.

If $a$ and $b$ are two cardinal numbers, then by $a \leq b$, we mean that
there exist two sets $A$ and $B$ such that $\Card{A} = a$, $\Card{B} = b$ and
$A \preceq B$. By $a < b$, we mean that $A \preceq B$ 
and $A \nsim B$. $a \leq b$ and $b \leq a$ guarantees that $a = b$.

It can be shown that $\Power(\Nat) \sim \RR$. The cardinality of $\RR$ is denoted by
$\mathfrak{c}$.

(def:set:infinite_cardinal_number)=
````{prf:definition}

A cardinal number $a$ satisfying $\aleph_0 \leq a$ is known as *infinite cardinal number*.
````

(def:set:cardinality_continuum)=
````{prf:definition}

The cardinality of $\RR$ denoted by $\mathfrak{c}$ is known as the *cardinality of the continuum*.
````

````{prf:theorem}
Let $2 = \{ 0, 1 \}$. Then $2^X \sim \Power (X) $ for every set $X$.
````
````{prf:proof}
$2^X$ is the set of all functions $f : X \to 2$. i.e. a function from $X$ to $\{ 0, 1 \}$ which can
take only one the two values $0$ and $1$.

Define a function $g : \Power (X) \to 2^X$ as follows. Let $y \in \Power(X)$.
Then $g(y)$ is a function $f : X \to \{ 0, 1 \}$ given by

$$
    f(x) =
     \left\{
            \begin{array}{ll}
                1 & \mbox{if $x \in y$};\\
                0 & \mbox{if $x \notin y$}.
            \end{array}
          \right.
$$

The function $g$ is one-one and on-to. Thus $2^X \sim \Power(X)$.
````

We denote the cardinal number of $\Power(X)$ by $2^{\Card{X}}$. Thus, $\mathfrak{c} = 2^{\aleph_0}$.

The following inequalities of cardinal numbers hold:

$$
    0 < 1 < 2 < \dots < n \dots < \aleph_0 < 2^{\aleph_0} = \mathfrak{c} < 2^ \mathfrak{c} < 2^{2^{ \mathfrak{c}}} \dots.
$$


