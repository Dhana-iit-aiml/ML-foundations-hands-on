# -*- coding: utf-8 -*-
"""Intro to Scikit-learn.ipynb"""

from sklearn.datasets import load_iris
iris = load_iris()

import pandas as pd
X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.head()
y = pd.Series(iris.target)

df = X.copy()
df['target'] = y
df.head()

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x=df['target'])

plt.title("Class Distribution")
plt.xlabel("Target Class")
plt.ylabel("Count")

sns.pairplot(df, hue='target')
plt.suptitle("Pairplot of Iris Features", y=1.02)
plt.show()

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].hist(X.iloc[:, 1], bins=20, color="skyblue")
ax[0].set_title("Before Scaling: Sepal Width")

ax[1].hist(X_train[:, 1], bins=20, color="orange")
ax[1].set_title("After Scaling: Sepal Width")
plt.show()

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=1, random_state=42)
tree.fit(X_train, y_train)
y_pred_tree = tree.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report

def plot_confusion(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(title)
    plt.show()

plot_confusion(y_test, y_pred_knn, "KNN Confusion Matrix")
plot_confusion(y_test, y_pred_tree, "Decision Tree Confusion Matrix")

print("KNN Report:\n", classification_report(y_test, y_pred_knn))
print("Tree Report:\n", classification_report(y_test, y_pred_tree))