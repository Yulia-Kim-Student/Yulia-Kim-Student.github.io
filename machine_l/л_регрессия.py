import numpy as np

def linear_func(theta, x):
    return np.dot(theta, x)
def linear_func_all(theta, X):
    return np.dot(X, theta)
def mean_squared_error(theta, X, y):
    predictions = linear_func_all(theta, X)
    return np.mean((predictions - y) ** 2)
def grad_mean_squared_error(theta, X, y):
    predictions = linear_func_all(theta, X)
    return 2 / X.shape[0] * np.dot(X.T, (predictions - y))

X = np.array([[1,2],[3,4],[4,5]])

theta = np.array([5, 6])

y = np.array([1, 2, 1])

print(linear_func_all(theta, X))

print(mean_squared_error(theta, X, y))

print(grad_mean_squared_error(theta, X, y))
