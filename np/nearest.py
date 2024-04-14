import numpy as np
# def nearest(points: np.ndarray, a: np.ndarray) -> np.ndarray:
#     distances = [sum((i-a)**2)**0.5 for i in points]
#     min_index = distances.index(min(distances))
#     return points[min_index]
def nearest(points: np.ndarray, a: np.ndarray) -> np.ndarray:
    distances = np.sum((points - a) ** 2, axis=1)
    min_index = np.argmin(distances)
    return points[min_index]
print(*nearest(np.array(b), np.array([1, 1])))
