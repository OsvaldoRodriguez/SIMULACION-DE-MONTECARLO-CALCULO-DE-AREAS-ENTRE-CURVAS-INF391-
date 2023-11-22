import matplotlib.pyplot as plt
import numpy as np

def generar_puntos_aleatorios(n):
    x = np.random.rand(n)
    y = np.random.rand(n)
    return x, y

def f(x):
    return 3 * (x - 1/2)**2 + 1/5

def g(x):
    return -3 * (x - 1/2)**2 + 1/2

def h(x):
    return (9/10) * x

def cumple_restriccion(x, y):
    y_f = f(x)
    y_g = g(x)
    y_h = h(x)
    if y >= y_f and y <= y_g and y <= y_h:
        return True
    else:
        return False

def dibujar_cuadrado_y_puntos(x, y):
    fig, ax = plt.subplots()

    cuadrado = plt.Rectangle((0, 0), 1, 1, fill=None, edgecolor='b')
    ax.add_patch(cuadrado)

    colores = ['r' if cumple_restriccion(xi, yi) else 'gray' for xi, yi in zip(x, y)]
    ax.scatter(x, y, color=colores, marker='o', s = 5)

    sum = 0
    for i in colores:
      if i == 'r':
        sum += 1

    print("\nSi {} es el area de la curva aproximada es {:.10f}".format(n, sum / n))

    x_funcion = np.linspace(0, 1, 100)
    ax.plot(x_funcion, f(x_funcion), label=r'$f(x)=3\left(x-\frac{1}{2}\right)^2+\frac{1}{5}$')
    ax.plot(x_funcion, g(x_funcion), label=r'$g(x)=-3\left(x-\frac{1}{2}\right)^2+\frac{1}{2}$')
    ax.plot(x_funcion, h(x_funcion), label=r'$h(x)=\frac{9x}{10}$')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend()
    plt.show()

# Número de puntos aleatorios
# n = int(input())
N = 100000

i = 10
while i <= N:
  n = i
  puntos_x, puntos_y = generar_puntos_aleatorios(n)
  dibujar_cuadrado_y_puntos(puntos_x, puntos_y)
  i *= 10
