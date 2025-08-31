# KNN Classifier Algorithm
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("glass.csv")
X = df.drop(columns=["Type"])
y = df["Type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Euclidean Distance
knn = KNeighborsClassifier(n_neighbors=3, metric="euclidean")
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print("Confusion matrix:\n", confusion_matrix(y_test, pred))
print("\nAccuracy score: ", accuracy_score(y_test, pred))

# Manhattan Distance
knn = KNeighborsClassifier(n_neighbors=3, metric="manhattan")
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print("Confusion matrix:\n", confusion_matrix(y_test, pred))
print("\nAccuracy score: ", accuracy_score(y_test, pred))
