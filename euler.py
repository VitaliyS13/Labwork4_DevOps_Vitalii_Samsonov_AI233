import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, h, a, b):
    n = int((b - a) / h) + 1
    x_values = np.linspace(a, b, n)
    y_values = np.zeros(n)
    y_values[0] = y0
    for i in range(1, n):
        y_values[i] = y_values[i-1] + h * f(x_values[i-1], y_values[i-1])
    return x_values, y_values

def f(x, y):
    return x + np.sin(y / 3)

if __name__ == "__main__":

    x0, y0, a, b, h = 1.6, 4.6, 1.6, 2.6, 0.1
    x_vals, y_vals = euler_method(f, x0, y0, h, a, b)

    print("Лабораторна робота № 4 виконав студент групи АІ233 Самсонов Віталій")

    for x, y in zip(x_vals, y_vals):
        print(f"x = {x:.4f}, y = {y:.4f}")

    plt.plot(x_vals, y_vals, label="Метод Ейлера")
    plt.title("Задача Коші методом Ейлера")
    plt.legend()
    plt.savefig("result.png")
