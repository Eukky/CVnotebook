# T-Distribution Stochastic Neighbour Embedding

## Introduction

T-Distribution Stochastic Neighbour Embedding(t-SNE) is a visualization method that visualizes high-dimensional data by giving each datapoint a location in a two or three-dimensional map. t-SNE is better than existing techniques at creating a single map that reveals structure at many different scales.

## Stochastic Neighbour Embedding

Stochastic Neighbor Embedding (SNE) starts by converting the high-dimensional Euclidean dis- tances between datapoints into conditional probabilities that represent similarities. The similarity of datapoint x j to datapoint xi is the conditional probability, $p_{j|i}$, that $x_i$ would pick $x_j$ as its neighbor if neighbors were picked in proportion to their probability density under a Gaussian centered at $x_i$.
$$ p_{j|i} = \frac{exp(-{||x_i-x_j||}^2/2\sigma_i^2)}{\sum_{k\neq i}exp(-{||x_i-x_k||}^2/2\sigma_i^2)} $$
For the low-dimensional counterparts by $y_i$ and $y_j$ of the high-dimensional datapoints $x_i$ and $x_j$, it is possible to compute a similar conditional probability $q_{j|i}$. Set the variance of Gaussian that is employed in the computation of the conditional probabilities $q_{j|i}$ to $\frac{1}{\sqrt{2}}$.
$$ q_{j|i} = \frac{exp(-{||y_i-y_j||}^2)}{\sum_{k\neq i}exp(-{||y_i-y_k||}^2)} $$
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

## Symmetric SNE

Set $p_{i|j}=p_{j|i}$ and $q_{i|j}=q_{j|i}$, it is possible to minimize a single KL divergence between P and Q.
$$ C=KL(P||Q)=\sum_i \sum_j p_{ij}log\frac{p_{ij}}{q_{ij}} $$
$$ q_{j|i} = \frac{exp(-{||y_i-y_j||}^2)}{\sum_{k\neq i}exp(-{||y_k-y_l||}^2)} $$
$$ p_{j|i} = \frac{exp(-{||x_i-x_j||}^2/2\sigma_i^2)}{\sum_{k\neq i}exp(-{||x_k-x_l||}^2/2\sigma_i^2)} $$
To make each datapoint $x_i$ makes a significant contribution to the cost function, set $p_{ij}=\frac{p_{j|i}+p_{i|j}}{2n}$. It ensures that $\sum_jp_{ij}>\frac{1}{2n}$ for all datappoints $x_i$. The gradient of symmetric SNE is given by
$$ \frac{\delta C}{\delta y_i}=4\sum_j(p_{ij}-q_{ij})(y_i-y_j) $$

## t-SNE

Using a Gaussian distribution in the high-gimensional space and using a probability distribution that has much heavier tails than a Gaussian distribution allows a moderate distance in the high dimensional space to be faithfully modeled by a much larger distance in the map. It also eliminates the unwanted attractive forces between map points that represent moderately dissimilar datapoints.  
The t-SNE use a Student t-distribution with one degerr of freedom as the heavy-tailed distribution in the low-dimensional map.
$$ q_{ij}=\frac{(1+||y_i-y_j||^2)^{-1}}{\sum_{k\neq l}{(1+||y_k-y_l||^2)^{-1}}} $$
The gradient of the KL divergence between P and Student-t based joint probability distribution Q is given by
$$ \frac{\delta C}{\delta y_i}=4\sum_j(p_{ij}-q_{ij})(y_i-y_j)(1+||y_i-y_j||^2)^{-1} $$

## The advantage of t-SNE

- The t-SNE gradient strongly repels dissimilar datapoints that are modeled by a small pair- wise distance in the low-dimensional representation.
- Although t-SNE introduces strong repulsions between dissimilar datapoints that are modeled by small pairwise distances, these repulsions do not go to infinity.

## ALgorighm

>**Data**: data set $X=\{x_1,x_2,...x_n\}$,  
cost function parameters: perplexity $Perp$,  
optimization parameters: number of iterations $T$, learning rate $\eta$, momentum $\alpha(t)$.  
**Result**: low-dimensional data representation $Y^{(T)}=\{y_1,y_2,...y_n\}$.  
**begin**  
&emsp;&emsp;compute pairwise affinities $p_{j|i}$ with perplexity $Perp$  
&emsp;&emsp;set $p_ij=\frac{p_{j|i}+p_{i|j}}{2n}$  
&emsp;&emsp;sample initial solution $Y^{(0)}=\{y_1,y_2,...y_n\}$ from $N(0,10^{-4}I)$  
&emsp;&emsp;**for** $t=1$ **to** $T$ **do**  
&emsp;&emsp;&emsp;&emsp;compute low-dimensional affinities $q_{ij}$  
&emsp;&emsp;&emsp;&emsp;compute gradient $\frac{\delta C}{\delta y_i}$  
&emsp;&emsp;&emsp;&emsp;set $Y^{(t)}=Y^{(t-1)}+\eta\frac{\delta C}{\delta y_i}+\alpha(t)(Y^{(t-1)}-Y^{(t-2)})$  
&emsp;&emsp;**end**  
**end**

## Optimization Methods for t-SNE

- Early compression  
  To force the map points to stay close together at the start of the optimization.
- Early exaggeration  
  To multiply all of the $p_{ij}$ 4(for example) times in the initial stages of the optimization.  

## Example

[t-sne(python)](./SourceCode/t-sne.py)
