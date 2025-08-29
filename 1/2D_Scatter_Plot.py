import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv("cancer.csv")
# x = df['Radius (mean)']
# y = df['Texture (mean)']

x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.title("2D Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
