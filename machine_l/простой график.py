import matplotlib.pyplot
import numpy as np

def draw(plt, x):
    x = np.array(x)
    y = x**3 - 2*x**2 + 50*np.sin(5*x) + 3
    plt.plot(x, y, color='green')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel(r'$x^3 - 2x^2 + 50\sin(5x) + 3$')
    plt.savefig('output.png')

plt = matplotlib.pyplot
x = np.linspace(-10, 10, 400)
draw(plt, list(x))
