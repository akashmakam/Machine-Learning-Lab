# 2D Scatter Plot
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


# 3D Scatter Plot
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


# Hill Climbing Algorithm
import math
import numpy as np
import matplotlib.pyplot as plt

def objective_function(x):
    return math.sin(x) + math.sin(0.1*x**2)

def hill_climbing(start_x, step_size, max_iterations):
    history_x = []
    history_y = []

    current_x = start_x
    current_score = objective_function(current_x)
    history_x.append(current_x)
    history_y.append(current_score)

    for i in range(max_iterations):
        left = current_x - step_size
        right = current_x + step_size

        left_score = objective_function(left)
        right_score = objective_function(right)

        next_x, next_score = current_x, current_score
        if left_score > next_score:
            next_x, next_score = left, left_score
        if right_score > next_score:
            next_x, next_score = right, right_score

        if next_score > current_score:
            current_x, current_score = next_x, next_score
            history_x.append(current_x)
            history_y.append(current_score)
        else:
            break

    return history_x, history_y

hx, hy = hill_climbing(start_x=0, step_size=0.2, max_iterations=100)

xs = np.linspace(-5, 5, 1000)
ys = [objective_function(x) for x in xs]

plt.plot(xs, ys, label="f(x)")
plt.scatter(hx, hy, color="red", label="Hill Climbing Path")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Hill Climbing Algorithm")
plt.legend()
plt.show()
