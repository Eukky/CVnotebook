# Principal Components Analysis

## Introduction

Principal components analysis is a technique for analyzing and simplifying data sets. Principal components analysis is always used to reduce the dimensionality of a data set.

## Computation Method

The goal is to transform a given data set **X** of dimension $n$ to an alternative data set **Y** of smaller dimension $k$.

1. Calculate the deviations from the mean.
   $$ x_i=x_i-\frac{1}{m}\sum_{j=1}^{m}{x_j} $$

2. Find the covariance matrix.
   $$ C=\frac{1}{m}XX^T $$

3. Find the eigenvectors and eigenvalues of the covariance matrix.

4. Rearrange the eigenvectors and eigenvalues from top to bottom according to the corresponding feature value, and the first k rows are formed into a matrix P.

5. $Y=PX$ is the matrix that with a smaller dimension $k$.

## Advantage

- It is only affected by variance, and will not be affected by factors other than data.

- Orthogonality between each principal component. There is no effect between raw data components.

- The calculation method is simple. The main operation is eigenvalue decomposition and it is easy to implement.

## Disadvantage

- Non-principal components with small variances may also contain important information about sample differences, as dimensionality reduction may have an impact on subsequent data processing.

- The meaning of each feature dimension of the principal component is not exact.