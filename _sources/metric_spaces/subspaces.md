(sec:ms:subspaces)=
# Subspace Topology

Let $(X, d)$ be a metric space. Let $Y \subseteq X$. 
Recall that $(Y, d)$ is a metric subspace with the
distance function $d$ restricted to $Y \times Y$.

```{prf:remark}
Let $Y$ be a metric subspace of $X$ and $S \subseteq Y$.
The interior, closure and boundary of $S$ w.r.t. $X$ 
and w.r.t. $Y$ may be different.

If a subspace hasn't been specified, by default, we shall
assume that we are computing the interior, closure and 
boundary w.r.t. the metric space $X$.
```

## Open Sets

```{prf:theorem} Open sets in subspace topology
:label: res-ms-subspace-open 

Let $Y$ be a metric subspace of $X$. Let $S \subseteq Y$.

$S$ is open in $Y$ if and only if $S = O \cap Y$ where $O$ 
is an open subset of $X$.
```

```{prf:proof}
abc
```

```{prf:example}
:label: ex-ms-semiclosed-set-as-open-in-subspace

* $[0, 1)$ is open in the metric space $\RR_+$.
```



## Closed Sets

```{prf:theorem} Closed sets in subspace topology
:label: res-ms-subspace-closed 

Let $Y$ be a metric subspace of $X$. Let $S \subseteq Y$.

$S$ is closed in $Y$ if and only if
$S = C \cap Y$ where
$C$ is a closed subset of $X$.
```

```{prf:proof} 

Let $S$ be closed in $Y$.

1. Then, $Y \setminus S$ is open in $Y$.
1. By definition of subspace topology,
   
   $$
   Y \setminus S = Y \cap O
   $$
   where $O$ is some open subset of $X$.
1. Then,

   $$
   S &= Y \setminus (Y \setminus S) \\
   &= Y \setminus (Y \cap O) \\
   &= Y \setminus O \\
   &= Y \cap (X \setminus O).
   $$
1. But $C = X \setminus O$ is closed in $X$.
```
