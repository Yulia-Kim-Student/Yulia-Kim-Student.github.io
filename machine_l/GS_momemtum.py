import numpy as np


class Oracle:
    '''Provides an interface for evaluating the Rosenbrock function and its derivative'''

    def __init__(self, a=1, b=100):
        self.a = a
        self.b = b

    def value(self, xy: np.ndarray) -> float:
        '''Evaluates the Rosenbrock function at point `xy`'''
        x, y = xy
        return (self.a - x) ** 2 + self.b * (y - x ** 2) ** 2

    def gradient(self, xy: np.ndarray) -> np.ndarray:
        '''Evaluates the Rosenbrock function derivative at point `xy`'''
        x, y = xy
        dfdx = -2 * (self.a - x) - 4 * self.b * x * (y - x ** 2)
        dfdy = 2 * self.b * (y - x ** 2)
        return np.array([dfdx, dfdy])


class GDM:
    '''Represents a Gradient Descent with Momentum optimizer'''

    def __init__(self, *, alpha: float = 0.9, eta: float = 0.1):
        '''Initializes `eta` (learning rate) and `alpha` (exponential decay factor) fields'''
        self.eta = eta
        self.alpha = alpha

    def optimize(self, oracle: Oracle, x0: np.ndarray, *,
                 max_iter: int = 100, eps: float = 1e-5) -> np.ndarray:
        v = np.zeros_like(x0)
        for i in range(max_iter):
            grad = oracle.gradient(x0)
            if np.linalg.norm(grad) < eps:
                break

            v = self.alpha * v - self.eta * grad
            x0 += v

        return x0


oracle = Oracle()
optimizer = GDM(alpha=0.9, eta=0.001)
x0 = np.array([-2.0, 2.0])
xy_min = optimizer.optimize(oracle, x0)

print(f"Точка минимума: {xy_min}")
