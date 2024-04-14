import numpy as np


def fit_linear_regression(X, y):
    theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)  # theta = (X^T * X)^-1 * X^T * y
    return theta


X = np.array([
    [1200, 3],
    [1500, 4],
    [1700, 3],
    [2000, 5],
    [2300, 4],
    [2500, 5]])
y = np.array([300000, 350000, 360000, 400000, 420000, 450000])
coefs = fit_linear_regression(X, y)
print(np.round(coefs))
