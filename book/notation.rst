Notation
=================

This section summarizes major notation used in the book.


Numbers
------------

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - Notation 
      - Meaning
      - Reference
    * - :math:`\Nat`
      - The set of natural numbers
      -
    * - :math:`\ZZ`
      - The set of integers
      -
    * - :math:`\QQ`
      - The set of rational numbers
      -
    * - :math:`\RR`
      - The set of real numbers
      - :prf:ref:`def-real-numbers`
    * - :math:`\ERL`
      - The extended real line :math:`[-\infty, \infty]`
      - :prf:ref:`def-bra-extended-real-line`
    * - :math:`\CC`
      - The set of complex numbers
      -
    * - :math:`\Re(x)`
      - The real part of a complex number
      -
    * - :math:`\Im(x)`
      - The imaginary part of a complex number
      -


Sets and Functions
---------------------

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - Notation 
      - Meaning
      - Reference
    * - :math:`\dom f`
      - Domain of a function :math:`f` 
      - :prf:ref:`def-st-function-domain`
    * - :math:`\range f`
      - Range of a function :math:`f`
      - :prf:ref:`def-st-function-range`
    * - :math:`\epi f`
      - Epigraph of a function :math:`f`
      - 
    * - :math:`\supp f`
      - Support of a function :math:`f`
      - 
    * - :math:`g \circ f`
      - Composition of functions :math:`g` and :math:`f` with 
        :math:`(g \circ f)(x) = g(f(x))`
      - :prf:ref:`def-st-function-composition`



Linear Algebra
-------------------

.. list-table:: 
    :widths: 20 80
    :header-rows: 1

    * - Notation 
      - Meaning
    * - :math:`\VV`
      - A vector space (usually finite dimensional)
    * - :math:`\EE`
      - A normed vector space (usually finite dimensional and Euclidean)
    * - :math:`\RR^n`
      - :math:`n` dimensional Euclidean real vector space
    * - :math:`\RR^{m \times n}`
      - The space of :math:`m \times n` real matrices
    * - :math:`\SS^{n}`
      - The space of :math:`n \times n` symmetric real matrices
    * - :math:`\NullSpace(A)`
      - Null space of a matrix :math:`A`
    * - :math:`\ColSpace(A)`
      - Column space of a matrix :math:`A`
    * - :math:`\RowSpace(A)`
      - Row space of a matrix :math:`A`
    * - :math:`\Range(A)`
      - Range of a set of vectors :math:`A`
    * - :math:`\Nullity(A)`
      - Nullity of a an operator :math:`A`
    * - :math:`\Trace(A)`
      - Trace of a matrix :math:`A`
    * - :math:`\Diag(A)`
      - Diagonal of a matrix :math:`A`
    * - :math:`\supp(v)`
      - Support of a vector :math:`v` (non-zero indices)
    * - :math:`\bzero`
      - The all zeros vector
    * - :math:`\bone`
      - The all ones vector


Topology / Metric Spaces
----------------------------

.. list-table:: 
    :widths: 20 80
    :header-rows: 1

    * - Notation 
      - Meaning
    * - :math:`\interior A`
      - The interior of a set :math:`A`
    * - :math:`\closure A`
      - The closure of a set :math:`A`
    * - :math:`\boundary A`
      - The boundary of a set :math:`A`
    * - :math:`\diam A`
      - The diam of a set :math:`A`
    * - :math:`\relint A`
      - The relative interior of a set :math:`A`


Calculus
----------------------------

.. list-table:: 
    :widths: 20 60 20
    :header-rows: 1

    * - Notation 
      - Meaning
      - Reference
    * - :math:`\lim_{x \to a} f(x)`
      - Limit of :math:`f` as :math:`x` approaches :math:`a`
      - :prf:ref:`def-bra-real-function-limit`
    * - :math:`x \to a^-`
      - :math:`x` approaches :math:`a` from the left
      - :prf:ref:`def-bra-rf-one-sided-limit`
    * - :math:`x \to a^+`
      - :math:`x` approaches :math:`a` from the right
      - :prf:ref:`def-bra-rf-one-sided-limit`
    * - :math:`f(a^-)`
      - Left hand limit of :math:`f` at :math:`x=a`
      - :prf:ref:`def-bra-rf-one-sided-limit`
    * - :math:`f(a^+)`
      - Right hand limit of :math:`f` at :math:`x=a`
      - :prf:ref:`def-bra-rf-one-sided-limit`
    * - :math:`f'`
      - First derivative of :math:`f`
      - :prf:ref:`def-bra-rf-differentiable-function`
    * - :math:`f^{(1)}`
      - 1st derivative of :math:`f`
      - :prf:ref:`def-bra-rf-nth-derivative`
    * - :math:`f^{(n)}`
      - n-th derivative of :math:`f`
      - :prf:ref:`def-bra-rf-nth-derivative`
    * - :math:`f^{(0)}`
      - 0-th derivative of :math:`f` (:math:`f^{(0)}=f`)
      - :prf:ref:`def-bra-rf-nth-derivative`
    * - :math:`f'_-(a)`
      - Left hand derivative of :math:`f` at :math:`x=a`
      - :prf:ref:`def-bra-df-one-sided-derivative`
    * - :math:`f'_+(a)`
      - Right hand derivative of :math:`f` at :math:`x=a`
      - :prf:ref:`def-bra-df-one-sided-derivative`
    * - :math:`\nabla f`
      - Gradient of :math:`f`
      -

Convex Analysis
-------------------------


.. list-table:: 
    :widths: 20 80
    :header-rows: 1

    * - Notation 
      - Meaning
    * - :math:`\prox_f`
      - The proximal operator for a function :math:`f` 
