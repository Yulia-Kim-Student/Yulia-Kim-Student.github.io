import numpy as np
N, T = map(int, input().split())
probability = np.array([list(map(float, input().split())) for i in range(N)])
quantity = np.array([list(map(float, input().split())) for i in range(N)])
population = np.array(list(map(float, input().split())))

for i in range(T):
    population = np.sum(probability * quantity * population.reshape(-1, 1), axis=0)
print(*population)

