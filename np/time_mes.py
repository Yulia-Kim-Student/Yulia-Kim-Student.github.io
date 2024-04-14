import time
import numpy as np

start_time = time.time()

import numpy as np
file = open('input.txt')
n, m = map(int, file.readline().split())
scale = [float(i) for i in file.readline().split()][::-1]
time_series = [float(i) for i in file.readline().split()]
window = np.sum(scale)
smoothed_series = np.convolve(time_series, scale, mode='valid')/window
smoothed_series = np.round(smoothed_series, decimals=4)
print(*smoothed_series, file=open('output.txt', 'w'))

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time} секунд")