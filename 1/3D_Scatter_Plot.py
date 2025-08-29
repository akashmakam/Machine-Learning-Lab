import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv("cancer.csv")
# x = df['Radius (mean)']
# y = df['Texture (mean)']
# z = df['Perimeter (mean)']

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x, y, z)
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()
