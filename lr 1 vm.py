#метод градиентного
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определение функции f(x)
def f(x1, x2):
    return x1**4 + x2**2 + x2**2 + x1*x2 + x2*x2

# Градиент функции f(x)
def gradient_f(x1, x2):
    df_x1 = x1**4 + x2**2 + x2**2 + x1*x2 + x2*x2
    df_x2 = x1**4 + x2**2 + x2**2 + x1*x2 + x2*x2
    return df_x1, df_x2

# Начальная точка x(0)
x1_0, x2_0 = 0, 0
step_size = 0.1

# Шаг градиентного спуска
grad_x1, grad_x2 = gradient_f(x1_0, x2_0)
x1_1 = x1_0 - step_size * grad_x1
x2_1 = x2_0 - step_size * grad_x2

# Значения функции в точках x(0) и x(1)
f_x0 = f(x1_0, x2_0)
f_x1 = f(x1_1, x2_1)

# Вывод значений функции в точках x(0) и x(1)
print(f"f(x_0): {f_x0}")
print(f"f(x_1): {f_x1}")

# Построение 3D-графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = np.linspace(-2, 2, 100)
x2 = np.linspace(-2, 2, 100)
x1, x2 = np.meshgrid(x1, x2)
z = f(x1, x2)
print(z)

ax.plot_surface(x1, x2, z, cmap='viridis')

ax.scatter(x1_0, x2_0, f_x0, color='red', label='x(0)')
ax.scatter(x1_1, x2_1, f_x1, color='blue', label='x(1)')
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('f(x)')
ax.legend()

# Добавление метки к точкам x(0) и x(1)
ax.text(x1_0, x2_0, f_x0, "x(0)", color='black')
ax.text(x1_1, x2_1, f_x1, "x(1)", color='black')

plt.show()

#метод наискорейшего спуска
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определение функции f(x)
def f(x):
    x1, x2 = x
    return 7*x1**2 + 2*x1*x2 + 5*x2**2 + x1 - 10*x2

# Градиент функции f(x)
def gradient_f(x):
    x1, x2 = x
    df_x1 = 14*x1 + 2*x2 + 1
    df_x2 = 2*x1 + 10*x2 - 10
    return np.array([df_x1, df_x2])

# Начальная точка x(0)
x1_0, x2_0 = 0, 0
step_size = 0.1
epsilon = 0.01 # Условие остановки

# Метод наискорейшего спуска
while True:
    grad = gradient_f([x1_0, x2_0])
    if np.all(np.abs(grad) <= epsilon):
        break

x1_0 = x1_0 - step_size * grad[0]
x2_0 = x2_0 - step_size * grad[1]

# Значение функции в конечной точке
f_x_final = f([x1_0, x2_0])

# Вывод значения функции в конечной точке
print(f"f(x_final): {f_x_final}")
print(f"Final point x: ({x1_0}, {x2_0})")

# Построение 3D-графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = np.linspace(-2, 2, 100)
x2 = np.linspace(-2, 2, 100)
x1, x2 = np.meshgrid(x1, x2)
z = f([x1, x2])

ax.plot_surface(x1, x2, z, cmap='viridis')

ax.scatter(x1_0, x2_0, f_x_final, color='red', label='x_final')
ax.text(x1_0, x2_0, f_x_final, f'({x1_0:.2f}, {x2_0:.2f}, {f_x_final:.2f})', color='black')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('f(x)')
ax.legend()

plt.show()
