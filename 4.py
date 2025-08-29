# Heat map
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = np.random.rand(10, 10)
sns.heatmap(data, cmap='viridis')
plt.title("Heat Map")
plt.show()


# Mini-max algorithm
import math

def mini_max(depth, index, is_max, scores, maxdepth):
  if depth == maxdepth:
    return scores[index]
  left = mini_max(depth + 1, index * 2, not is_max, scores, maxdepth)
  right = mini_max(depth + 1, index * 2 + 1, not is_max, scores, maxdepth)
  return max(left, right) if is_max else min(left, right)

scores = [3, 5, 6, 9, 1, 2, 0, -1]
depth = math.log2(len(scores))

print(f"Optimal Minimax Score: {mini_max(0, 0, True, scores, depth)}")
