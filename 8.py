import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("IRIS.csv")
X = df.iloc[:, :-1].values

kmeans = KMeans(n_clusters=3, random_state=0)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

print("K-means Labels:", labels.tolist())
print("\nK-means Centroids:\n", pd.DataFrame(centroids, columns=df.columns[:-1]))

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], s=60, c='red', marker='X', label='Centroids')
plt.title("K-Means Clustering")
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.legend()
plt.grid(True)
plt.show()
