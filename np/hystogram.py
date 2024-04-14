import numpy as np

file = open('input.txt')
n = int(file.readline())
selection = sorted([int(i) for i in file.readline().split()])
file.close()
k = int(1 + np.floor(np.log2(n)))
b_array = np.linspace(selection[0], selection[-1], k+1)
b_array[-1] += 1
intervals = np.digitize(selection, b_array, right=False)
print(*[list(intervals).count(i) for i in range(1, k+1)], file=open('output.txt', 'w'))

