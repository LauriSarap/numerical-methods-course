import numpy as np

def f(x):
    return -2*x*np.exp(-x) + np.exp(-2*x) + x**2

def df(x):
    return 2*x*np.exp(-x) - 2*np.exp(-x) - 2*np.exp(-2*x) + 2*x

def newton(x0, f: callable, df: callable, eps: float, maxit: int) -> tuple[float, int]:
    x = x0
    x_array = [x0]
    delta = 1
    for i in range(maxit):
        x_new = x - 2 * f(x)/df(x)
        delta = abs(x_new - x)
        x = x_new
        x_array.append(x)
        print(f"Iteration {i + 1}: x = {x}, delta = {delta}")
        if delta < eps:
            return x, i + 1, x_array

    return x, i + 1, x_array

x, i, x_array = newton(0, f, df, 1e-5, 20)
print(f"x* = {x}, iterations = {i}")

def kordsus(x_array: list[float]) -> float:
    n = len(x_array) - 1
    numerator = x_array[n] - x_array[n - 1]
    denominator = x_array[n - 1] - x_array[n - 2]
    return numerator / denominator

print(kordsus(x_array))
