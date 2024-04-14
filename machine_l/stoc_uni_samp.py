import numpy as np

def sus(fitness: np.ndarray, n: int, start: float) -> list:

    sum_fitness = np.sum(fitness)
    indiv_dist = sum_fitness / n
    start_points = [start + i * indiv_dist for i in range(n)]
    print(start_points)
    start_points = [point % sum_fitness for point in start_points]
    print(start_points)
    selected = []
    for point in start_points:
        cumulate = 0
        print('cumulate', cumulate)
        for i, fit in enumerate(fitness):
            cumulate += fit
            print('lev2cum', cumulate)
            if cumulate >= point:
                selected.append(i)
                break

    return selected


fitness = np.array([10, 4, 3, 2, 1])
selected_indices = sus(fitness, 3, 6)
print(f"Selected indices: {selected_indices}")
for index in selected_indices:
    print(fitness[index], end=' ')