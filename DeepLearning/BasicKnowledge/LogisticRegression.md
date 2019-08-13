# Logistic Regression

## Introduction

Logistic regression is a statistical model that in its basic form uses a logistic function to model a binary dependent variable. Logistic regression model can also seem as simple neural network. It is a learning algorithm that we use when the output labels Y in a supervised learning problem are all either zero or one, so for binary classification problems.

## Algorithm

1. Define a sigmoid function

   $$ \sigma(z)=\frac{1}{1+e^{-z}} $$

2. Calculate the the predict value $\hat{y}$

   $$ \hat{y}^i=\sigma(w^Tx^i+b) $$
   We need a train set $m$ to train the model so that it can find the suitable parameter $w$ and $b$ to predict $\hat{y}$.

3. Calculate the loss function $L(\hat{y},y)$

   $$ L(\hat{y},y)=-ylog\hat{y}-(1-y)log(1-\hat{y}) $$

4. Calculate the cost function

   $$ J(w,b)=\frac{1}{m}\sum^{m}_{i=1}L(\hat{y}^{i},y^{i})=\frac{1}{m}\sum^{m}_{i=1}(-y^ilog\hat{y}^i-(1-y^i)log(1-\hat{y}^i)) $$

5. Use the gradient optimization to update the $dw$ and $db$.

   $$ dw := dw - a\frac{\partial J(w,b)}{\partial w} $$
   $$ db := db - a\frac{\partial J(w,b)}{\partial b} $$

## Example

[Logistic Regression(python)](./SourceCode/LogisticRegression.py)
