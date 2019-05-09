# Covariance Matrix

## Introduction

Covariance matrix is a matrix whose element in the i, j position is the covariance between the i-th and j-th elements of a random vector. A random vector is a random variable with multiple dimensions.

## Definition

$$ \mathbf{X}=
\left[
 \begin{matrix}
   X_1 \\
   X_2 \\
   . \\
   . \\
   . \\
   X_n
  \end{matrix}
\right]
$$

$\mu_i$ is the expected value of $X_i$, $\mu_i=E(X_i)$. The element of covariance in i, j position is the covariance:

$$ \Sigma_{ij}=cov(X_i, X_j)=E[(X_i-\mu_i)(X_j-\mu_j)] $$

The covariance matrix is:

$$\Sigma=E[(\mathbf{X}-E[\mathbf{X}])(\mathbf{X}-E[\mathbf{X}])^T]\\=
\left[
 \begin{matrix}
   E[(X_1-\mu_1)(X_1-\mu_1)] & E[(X_1-\mu_1)(X_2-\mu_2)] & ... & E[(X_1-\mu_1)(X_n-\mu_n)]\\
   E[(X_2-\mu_2)(X_1-\mu_1)] & E[(X_2-\mu_2)(X_2-\mu_2)] & ... & E[(X_2-\mu_2)(X_n-\mu_n)]\\
   . & . & . & .\\
   . & . & . & .\\
   . & . & . & .\\
   E[(X_n-\mu_n)(X_1-\mu_1)] & E[(X_n-\mu_n)(X_n-\mu_n)] & ... & E[(X_n-\mu_n)(X_n-\mu_n)]
  \end{matrix}
\right]
$$