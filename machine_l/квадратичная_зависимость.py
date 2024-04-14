import numpy as np

with open('input.txt', 'r') as file_op:
    N = int(file_op.readline().strip())
    data = np.array([list(map(float, line.split())) for line in file_op.readlines()])

X = data[:, 0]
Y = data[:, 1]

A = np.vstack([X**2, X, np.ones(N)]).T
beta = np.linalg.lstsq(A, Y, rcond=None)[0]
beta = [np.round(i, decimals=3) for i in beta]

print(*beta, file=open('output.txt', 'w'))


