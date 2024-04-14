import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

N = 5
x_values = np.arange(N)
y_values = np.array([700.949074, 715.616206, 726.958614, 730.983909, 730.427020])

coeffs = np.polyfit(x_values, y_values, N - 1)
polynomial = Polynomial(coeffs[::-1])

extrapolated_value = polynomial(N)
print(extrapolated_value)

