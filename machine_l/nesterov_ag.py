import numpy as np

class NesterovAG:
    def __init__(self, *, alpha: float = 0.9, eta: float = 0.1):
        self.alpha = alpha
        self.eta = eta

    def optimize(self, oracle: 'Oracle', x0: np.ndarray, *, max_iter: int = 100, eps: float = 1e-5) -> np.ndarray:
        x = x0.copy()
        v = np.zeros_like(x0)
        for _ in range(max_iter):
            predicted_x = x - self.alpha * v
            grad = oracle.gradient(predicted_x)
            if np.linalg.norm(grad) < eps:
                break
            v = self.alpha * v + self.eta * grad
            x -= v
        return x


class Oracle:
    def value(self, x: np.ndarray) -> float:
        return np.sum((x - 3) ** 2)

    def gradient(self, x: np.ndarray) -> np.ndarray:
        return 2 * (x - 3)
