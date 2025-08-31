# PCA
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("abalone.csv")
X = df.drop(columns="Type")
y = df['Type']

X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

colors = {'M': 'red', 'F': 'blue', 'I': 'green'}

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y.map(colors))
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("PCA Projection of Abalone Data")
plt.show()


# LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("abalone.csv")
X = df.drop(columns="Type")
y = df['Type']

X_scaled = StandardScaler().fit_transform(X)

lda = LDA(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

colors = {'M': 'red', 'F': 'blue', 'I': 'green'}

plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y.map(colors))
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.title("LDA Projection of Abalone Data")
plt.show()
