import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative

def f(x):
    # return 1.5*x*x+2
    return 150*np.sin(x) + 1.5*x*x+2
x = [i for i in np.arange(-20,20,0.1)]
y = [f(xn) for xn in x]

xn = 0
yn = f(xn)
dx = 0.01

for i in range(5):
    xn = xn - dx*derivative(f, xn)
    yn = f(xn)
print('y_min =',yn)
print('x_min =',xn)

# Построение графиков
plt.plot(x, y, "b", xn, yn, 'go')
plt.show()