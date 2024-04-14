import numpy as np

class Oracle:
    def get_func(self, x):
        return x ** 2

    def get_grad(self, x):
        return 2 * x

class GradientOptimizer:
    def __init__(self, oracle, x0):
        self.oracle = oracle
        self.x0 = x0

    def optimize(self, iterations, eps, alpha):
        x = self.x0
        for i in range(iterations):
            grad = self.oracle.get_grad(x)
            if np.linalg.norm(grad) < eps:
                break
            x = x - alpha * grad
        return x

oracle = Oracle()
optimizer = GradientOptimizer(oracle, x0=np.array([10.0]))

optimized_x = optimizer.optimize(100, 0.01, 0.1)
print(optimized_x)
