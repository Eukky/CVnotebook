# Asymptotic Notations

## Big Theta Notation

- ### Notation
$$ f(n) = \Theta(g(n)) $$

- ### Definition
$$ \exists k_1>0, \exists k_2>0, \exists n_0, \forall n>n_0, k_1 \cdot g(n) \leq f(n) \leq k_2 \cdot g(n) $$

## Big O Notation

- ### Notation
$$ f(n) = O(g(n)) $$

- ### Definition
$$ \exists k>0, \exists n_0, \forall n>n_0, f(n) \leq k \cdot g(n) $$

## Big Omega Notation

- ### Notation
$$ f(n) = \Omega(g(n)) $$

- ### Definition
$$ \exists k>0, \exists n_0, \forall n>n_0, f(n) \geq k \cdot g(n) $$

## Small O Notation

- ### Notation
$$ f(n) = o (g(n)) $$

- ### Definition
$$ \exists k>0, \exists n_0, \forall n>n_0, f(n) < k \cdot g(n) $$

## Small Omega Notation

- ### Notation
$$ f(n) = \omega(g(n)) $$

- ### Definition
$$ \exists k>0, \exists n_0, \forall n>n_0, f(n) > k \cdot g(n) $$