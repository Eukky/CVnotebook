import numpy as np
from categorical_scatter import categorical_scatter_2d
from load_data import load_mnist

def neg_squared_euc_dist(X):
    """
    Compute matrix containing negative squared euclidean
    distance for all pairs of points in input matrix X

    Arguments:
        X: matrix of size NxD
        X为NxD的输入矩阵
    Returns:
        NxN matrix D, with entry D_ij = negative squared
        euclidean distance between rows X_i and X_j
        该函数返回一个N阶方阵，第i行第j列个元素为输入点x_i与x_j之间的负欧几里得距离平方
    计算矩阵中Xi行与Xj行之间的距离
    -||x_i - x_j||^2 = -(x_i^2 - 2 * x_i * x_j + x_j^2)
    """

    sum_X = np.sum(np.square(X), 1)
    D = np.add(np.add(-2 * np.dot(X, X.T), sum_X).T, sum_X)
    return -D

def softmax(X, diag_zero=True):
    """
    Take softmax of each row of matrix X.
    计算矩阵X的softmax函数
    """

    #不知道为什么要减去最大值，论文中的公式只是直接计算了距离
    e_x = np.exp(X - np.max(X, axis=1).reshape([-1, 1]))

    #将对角元素设置为0，是考虑了p_i|j=0的情况
    if diag_zero:
        np.fill_diagonal(e_x, 0.)
    
    e_x = e_x + 1e-8

    return e_x / e_x.sum(axis=1).reshape([-1, 1])

def calc_prob_matrix(distances, sigmas=None):
    """
    Convert a distances matrix to a matrix of probabilities.
    计算条件概率P矩阵

    distances: 计算出来的负欧几里得距离平方
    sigmas: 长度为N的向量，其中包含了每一个sigma_i的值
    """

    if sigmas is not None:
        two_sig_sq = 2. * np.square(sigmas.reshape((-1, 1)))
        return softmax(distances / two_sig_sq)
    else:
        return softmax(distances)

def binary_search(eval_fn, target, tol=1e-10, max_iter=10000, lower=1e-20, upper=1000.):
    """
    Perform a binary search over input values to eval_fn.
    为了寻找困惑度的二分搜索
    
    Arguments
        eval_fn: Function that we are optimising over.
        target: Target value we want the function to output.
        tol: Float, once our guess is this close to target, stop.
        max_iter: Integer, maximum num. iterations to search for.
        lower: Float, lower bound of search range.
        upper: Float, upper bound of search range.
    Returns:
        Float, best input value to function found during search.
    """
    for i in range(max_iter):
        guess = (lower + upper) / 2.
        val = eval_fn(guess)
        if val > target:
            upper = guess
        else:
            lower = guess
        if np.abs(val - target) <= tol:
            break
    return guess

def calc_perplexity(prob_matrix):
    """
    Calculate the perplexity of each row 
    of a matrix of probabilities.
    从概率矩阵计算困惑度
    """

    entropy = -np.sum(prob_matrix * np.log2(prob_matrix), 1)
    perplexity = 2 ** entropy
    return perplexity

def perplexity(distances, sigmas):
    """
    Wrapper function for quick calculation of 
    perplexity over a distance matrix.
    从距离矩阵直接计算困惑度
    """
    
    return calc_perplexity(calc_prob_matrix(distances, sigmas))

def find_optimal_sigmas(distances, target_perplexity):
    """
    For each row of distances matrix, find sigma that results
    in target perplexity for that role.
    """

    sigmas = []
    #遍历距离矩阵中的每一行(代表每个数据点)
    for i in range(distances.shape[0]):
        eval_fn = lambda sigma: perplexity(distances[i, :], np.array(sigma))
        correct_sigma = binary_search(eval_fn, target_perplexity)
        sigmas.append(correct_sigma)
    return np.array(sigmas)

def q_joint(Y):
    """
    Given low-dimensional representations Y, compute
    matrix of joint probabilities with entries q_ij.
    该函数用于计算对称SNE重的q概率矩阵
    """

    #计算距离
    distances = neg_squared_euc_dist(Y)
    
    #同样是使用softmax函数计算出q_ij，与之前的softmax不同的是这次分母计算的是整个矩阵的和而不是每一行的和
    exp_distances = np.exp(distances)
    np.fill_diagonal(exp_distances, 0.)
    return exp_distances / np.sum(exp_distances, None)

def p_conditional_to_joint(P):
    """
    Given conditional probabilities matrix P, return
    approximation of joint distribution probabilities.
    定义p_ij = (p_j|i + p_i|j)/2n
    """

    return (P + P.T) / (2. * P.shape[0])

def p_joint(X, target_perplexity):
    """
    Given a data matrix X, gives joint probabilities matrix.
    计算出对称SNE的概率矩阵

    Arguments
        X: Input data matrix.
    Returns:
        P: Matrix with entries p_ij = joint probabilities.
    """

    distances = neg_squared_euc_dist(X)
    sigmas = find_optimal_sigmas(distances, target_perplexity)
    p_conditional = calc_prob_matrix(distances, sigmas)
    P = p_conditional_to_joint(p_conditional)
    return P 

def symmetric_sne_grad(P, Q, Y):
    """
    Estimate the gradient of the cost with respect to Y
    梯度计算
    最后返回的grad为Nx2矩阵，第i行表示dC/dy_i
    """

    #矩阵形状为NxN
    pq_diff = P - Q
    #将矩阵形状变为NxNx1
    pq_expanded = np.expand_dims(pq_diff, 2)
    #矩阵形状为NxNx2
    y_diff = np.expand_dims(Y, 1) - np.expand_dims(Y, 0)
    #矩阵形状为Nx2
    grad = 4. * (pq_expanded * y_diff).sum(1)
    return grad

def q_tsne(Y):
    """
    t-SNE: Given low-dimensional representations Y, compute
    matrix of joint probabilities with entries q_ij.
    """

    distances = neg_squared_euc_dist(Y)
    inv_distances = np.power(1. - distances, -1)
    np.fill_diagonal(inv_distances, 0.)
    return inv_distances / np.sum(inv_distances), inv_distances

def tsne_grad(P, Q, Y, inv_distances):
    """
    Estimate the gradient of t-SNE cost with respect to Y.
    """
    pq_diff = P - Q
    pq_expanded = np.expand_dims(pq_diff, 2)
    y_diffs = np.expand_dims(Y, 1) - np.expand_dims(Y, 0)

    # Expand our inv_distances matrix so can multiply by y_diffs
    distances_expanded = np.expand_dims(inv_distances, 2)

    # Multiply this by inverse distances matrix
    y_diffs_wt = y_diffs * distances_expanded

    # Multiply then sum over j's
    grad = 4. * (pq_expanded * y_diffs_wt).sum(1)
    return grad 

def estimate_sne(X, y, P, rng, num_iters, q_fn, grad_fn, learning_rate, momentum, plot):
    """
    Estimates a SNE model.

    Arguments
        X: Input data matrix.
        y: Class labels for that matrix.
        P: Matrix of joint probabilities.
        rng: np.random.RandomState().
        num_iters: Iterations to train for.
        q_fn: Function that takes Y and gives Q prob matrix.
        plot: How many times to plot during training.
    Returns:
        Y: Matrix, low-dimensional representation of X.
    """

    #初始化Y矩阵
    Y = rng.normal(0., 0.0001, [X.shape[0], 2])

    #初始化过去值，用于生成动量
    if momentum:
        Y_m2 = Y.copy()
        Y_m1 = Y.copy()

    #梯度下降循环
    for i in range(num_iters):

        #t-sne
        Q, distances = q_fn(Y)
        grads = grad_fn(P, Q, Y, distances)

        #symmetric sne
        # Q = q_fn(Y)
        # grads = grad_fn(P, Q, Y)

        #更新Y
        Y = Y - learning_rate * grads
        if momentum:
            Y += momentum * (Y_m1 - Y_m2)
            Y_m2 = Y_m1.copy()
            Y_m1 = Y.copy()

        #绘图
        if plot and i % (num_iters / plot) == 0:
            categorical_scatter_2d(Y, y, alpha=1.0, ms=6, show=True, figsize=(9, 6))

    return Y


# Set global parameters
NUM_POINTS = 200            # Number of samples from MNIST
CLASSES_TO_USE = [0, 1, 8]  # MNIST classes to use
PERPLEXITY = 20
SEED = 1                    # Random seed
MOMENTUM = 0.9
LEARNING_RATE = 10.
NUM_ITERS = 500             # Num iterations to train for
TSNE = True               # If False, Symmetric SNE
NUM_PLOTS = 5               # Num. times to plot in training

def main():
    # numpy RandomState for reproducibility
    rng = np.random.RandomState(SEED)

    # Load the first NUM_POINTS 0's, 1's and 8's from MNIST
    X, y = load_mnist('datasets/',
                      digits_to_keep=CLASSES_TO_USE,
                      N=NUM_POINTS)

    # Obtain matrix of joint probabilities p_ij
    P = p_joint(X, PERPLEXITY)

    # Fit SNE or t-SNE
    Y = estimate_sne(X, y, P, rng,
             num_iters=NUM_ITERS,
             q_fn=q_tsne if TSNE else q_joint,
             grad_fn=tsne_grad if TSNE else symmetric_sne_grad,
             learning_rate=LEARNING_RATE,
             momentum=MOMENTUM,
             plot=NUM_PLOTS)

if __name__ == '__main__':
    main()