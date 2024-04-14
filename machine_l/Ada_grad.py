import numpy as np

class Oracle:

    def value(self, x: np.ndarray) -> float:
        return np.sum(x**2)

    def gradient(self, x: np.ndarray) -> np.ndarray:
        return 2 * x


class AdaGrad:
    def __init__(self, *, eta: float = 0.1, epsilon: float = 1e-8):
        self.eta = eta
        self.epsilon = epsilon
        self.grad_sqrt = None

    def optimize(self, oracle: Oracle, x0: np.ndarray, *,
                 max_iter: int = 100, eps: float = 1e-5) -> np.ndarray:
        x = x0.copy()
        if self.grad_sqrt is None:
            self.grad_sqrt = np.zeros_like(x0)

        for i in range(max_iter):
            grad = oracle.gradient(x)
            if np.linalg.norm(grad) < eps:
                break
            self.grad_sqrt += grad ** 2
            x -= self.eta * grad / (np.sqrt(self.grad_sqrt) + self.epsilon)
        return x

oracle = Oracle()
x0 = np.array([4.0, 10.0])
optimizer = AdaGrad()
x_min = optimizer.optimize(oracle, x0)

print(x_min)
print(oracle.value(x_min))



