# Box-Plot
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = np.random.randn(100)
sns.boxplot(x)
plt.title("Box Plot")
plt.show()


# Alpha-Beta Pruning Algorithm
import math

def alphabeta(depth, index, is_max, scores, max_depth, alpha, beta):
    if depth == max_depth:
        return scores[index]
    for i in range(2):
        val = alphabeta(depth + 1, index * 2 + i, not is_max, scores, max_depth, alpha, beta)
        if is_max:
            alpha = max(alpha, val)
        else:
            beta = min(beta, val)
        if beta <= alpha:
            break
    return alpha if is_max else beta

scores = [3,4,2,1,7,8,9,10,2,11,1,12,14,9,13,16]
depth = math.log2(len(scores))

result = alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf'))
print("Alpha-Beta Optimal Value:", result)
