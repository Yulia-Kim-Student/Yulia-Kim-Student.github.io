import numpy as np
file = open('../np/input.txt')
n, m = map(int, file.readline().split())
scale = [float(i) for i in file.readline().split()]
time_series = [float(i) for i in file.readline().split()]
window = np.array(scale)/np.sum(scale)
smoothed_series = np.convolve(time_series, window, mode='valid')
smoothed_series = np.round(smoothed_series, decimals=4)
print(*smoothed_series, file=open('output.txt', 'w'))
