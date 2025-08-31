# Naive Bayes Classifier Algorithm
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

df = pd.read_csv("Titanic.csv")
df = df[["Survived", "Pclass", "Sex", "Age", "Fare"]].dropna()
df["Sex"] = LabelEncoder().fit_transform(df["Sex"])

X = df.drop(columns="Survived")
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

nb = GaussianNB()
nb.fit(X_train, y_train)
pred = nb.predict(X_test)
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))
print("\nAccuracy Score:", accuracy_score(y_test, pred))
