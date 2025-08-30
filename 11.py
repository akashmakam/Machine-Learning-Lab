# Single Layer Perceptron Algorithm
import numpy as np

def perceptron(X, y):
    w = np.zeros(X.shape[1])
    lr = 0.1
    b = 0
    for i in range(10):
        for xi, target in zip(X, y):
            pred = np.dot(w, xi) + b
            update = lr * (target - (pred > 0))
            w += update * xi
            b += update
    return w, b

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y_and = np.array([0,0,0,1])
w, b = perceptron(X, y_and)
print("AND:", [(int(np.dot(x, w) + b > 0)) for x in X])

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y_or = np.array([0,1,1,1])
w, b = perceptron(X, y_or)
print("OR:", [(int(np.dot(x, w) + b > 0)) for x in X])
