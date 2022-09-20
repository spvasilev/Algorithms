import matplotlib.pyplot as plt
import numpy as np

def f(x):
    # return 1.5*x*x+2
    return 150*np.sin(x) + 1.5*x*x+2
x = [i for i in np.arange(-20,20,0.1)]
y = [f(xn) for xn in x]

# Произвольное первое состояние
s0 = -20
e1 = 0
tmax = 10000
tmin = 1
ds = 0.5
alpha = 1
ti = tmax
# Desirable values
s_des = 0
e_des = 0
# print(f(16)-f(18))

while (ti > tmin) & (s0 < 20):
    s1 = s0
    s0 = s0 + ds
    de = f(s0) - f(s1)
    # print('Разность', de)
    if ((f(s0) - f(s1)) <= 0) & (e_des > f(s0)):
        s_des = s0
        e_des = f(s_des)
        ti = ti - alpha
        # print('s0',s0,'Значения', s_des, e_des)
    else:
        p = np.exp(-de/ti)
        if (p > 0.5) & (e_des > f(s0)):
            s_des = s0
            e_des = f(s_des)
            # print(s_des, e_des)

print('x_min =', s_des)
print('y_min =', e_des)
plt.plot(x, y, 'b', s_des, e_des, 'go')
plt.show()



