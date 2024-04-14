import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


# X, y = make_blobs(n_samples=100, centers=2)
X, y = make_classification(n_classes=2, class_sep=2, n_features=2, n_redundant=0)
print(np.shape(X),X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=10)


def knn_custom(X_train, y_train, X_test, k=3):
    y_pred = []
    for test_point in X_test:
        distances = np.linalg.norm(X_train - test_point, axis=1)
        k_indices = np.argsort(distances)[:k]
        k_nearest_labels = y_train[k_indices]
        most_common = np.bincount(k_nearest_labels).argmax()
        y_pred.append(most_common)
    return np.array(y_pred)


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_sklearn = knn.predict(X_test)
print(y_sklearn)

y_non_sklearn = knn_custom(X_train, y_train, X_test, k=5)
print(y_non_sklearn)
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='Set1', marker='o')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_sklearn, cmap='Set1', marker='s', edgecolor='k')
plt.title("sklearn")

plt.subplot(1, 2, 2)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='Set1', marker='o')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_non_sklearn, cmap='Set1', marker='s', edgecolor='k')
plt.title("numpy")

plt.show()

