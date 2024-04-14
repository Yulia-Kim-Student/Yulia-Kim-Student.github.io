import numpy as np


def k_point_crossover(a: np.ndarray, b: np.ndarray, points: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    cr_a = a.copy()
    cr_b = b.copy()

    for i in range(0, len(points), 2):
        start = points[i]
        if i + 1 < len(points):
            end = points[i + 1]
        else:
            end = len(a)
        cr_a[start + 1:end] = b[start + 1:end]
        cr_b[start + 1:end] = a[start + 1:end]

    return cr_a, cr_b


a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
prep = lambda x: ' '.join(map(str, x))
# print(*map(prep, single_point_crossover(a, b, 4)), '', sep='\n')
# print(*map(prep, two_point_crossover(a, b, 2, 7)), '', sep='\n')
print(*map(prep, k_point_crossover(a, b, np.array([1, 5, 8]))), '', sep='\n')
# k_point_crossover(a, b, np.array([0, 1, 5, 8]))
