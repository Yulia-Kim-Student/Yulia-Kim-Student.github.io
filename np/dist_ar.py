import numpy as np


def calculate(start_points: np.ndarray, end_points: np.ndarray, point: np.ndarray) -> np.ndarray:
    '''Возвращает одномерный np.ndarray, содержащий расстояния до линий

    Args:
        start_points: двумерный np.ndarray, содержащий координаты первых точек линий
        end_points: двумерный np.ndarray, содержащий координаты вторых точек линий
        p: двумерный np.ndarray, содержайщий координаты точки point.

        start_points.shape == end_points.shape

    Returns:
        одномерный np.ndarray, содержащий расстояния от точки point до линий
    '''
    x0, y0 = point[0]
    x1, y1 = start_points[:, 0], start_points[:, 1]
    x2, y2 = end_points[:, 0], end_points[:, 1]
    numerator = np.abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominator = np.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    distances = np.round(numerator / denominator, 4)
    return distances
print(*calculate(
        np.array([[1, 2.5], [3.5, 3], [3.5, 4]]),
        np.array([[3, 2.5], [3.5, 0.5], [2.5, 5]]),
        np.array([[2.5, 4]])))