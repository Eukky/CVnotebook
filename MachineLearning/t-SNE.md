# T-Distribution Stochastic Neighbour Embedding

## Introduction

T-Distribution Stochastic Neighbour Embedding(t-SNE) is a visualization method that visualizes high-dimensional data by giving each datapoint a location in a two or three-dimensional map. t-SNE is better than existing techniques at creating a single map that reveals structure at many different scales.

## Stochastic Neighbour Embedding

Stochastic Neighbor Embedding (SNE) starts by converting the high-dimensional Euclidean dis- tances between datapoints into conditional probabilities that represent similarities. The similarity of datapoint x j to datapoint xi is the conditional probability, $p_{j|i}$, that $x_i$ would pick $x_j$ as its neighbor if neighbors were picked in proportion to their probability density under a Gaussian centered at $x_i$.
$$ p_{j|i} = \frac{exp(-{||x_i-x_j||}^2/2\sigma_i^2)}{\sum_{k\neq i}exp(-{||x_i-x_k||}^2/2\sigma_i^2)} $$
For the low-dimensional counterparts by $y_i$ and $y_j$ of the high-dimensional datapoints $x_i$ and $x_j$, it is possible to compute a similar conditional probability $q_{j|i}$. Set the variance of Gaussian that is employed in the computation of the conditional probabilities $q_{j|i}$ to $\frac{1}{\sqrt{2}}$.
$$ p_{j|i} = \frac{exp(-{||y_i-y_j||}^2)}{\sum_{k\neq i}exp(-{||y_i-y_k||}^2)} $$
We set $p_{i|i} = 0$ and $q_{i|i} = 0$.
SNE minimizes the sum of Kullback-Leibler divergences over all datapoints using a gradient descent method. The cost function C is given by
$$ C=\sum_i KL(P_i||Q_i)=\sum_i \sum_j p_{j|i}log\frac{p_{j|i}}{q_{j|i}} $$
Any particular value of $\sigma_i$ induces a probability distribution, $P_i$, over all of the other datapoints. This distribution has an entropy which increases as $\sigma_i$ increases. SNE performs a binary search for the value of $\sigma_i$ that produces a $P_i$ with a fixed perplexity that is specified by the user.
$$ Perp(P_i)=2^{H(P_i)} $$
$$ H(P_i)=-\sum_j p_{j|i}\log_2 p_{j|i} $$
The perplexity can be interpreted as a smooth measure of the effective number of neighbors. The typical values are between 5 and 50.
The minimization of the cost function is performed using a gradient descent method. The gradient has a simple form
$$ \frac{\delta C}{\delta y_i}=2\sum_j(p_{j|i}-q_{j|i}+p_{i|j}-q_{i|j})(y_i-y_j) $$
In order to speed up the optimization and to avoid poor local minima, a relatively large momentum term is added to the gradient.
$$ Y^{(t)}=Y^{(t-1)}+\eta\frac{\delta C}{\delta y_i}+\alpha(t)(Y^{(t-1)}-Y^{(t-2)}) $$
where $Y^{(t)}$ indicates the solution at iteration t, $\eta$ indicates the learning rate, and $\alpha(t)$ represents the momentum at iteration t.

## The disadvantage of SNE

- SNE requires sensible choices of the initial amount of Gaussian noise and the rate at which it decays to find maps with a better global organization.
- SNE is inferior to methods that allow convex optimization scene it need to run the optimization several times on a data set to find appropriate values for the parameters.

## t-SNE
