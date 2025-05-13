import math

epsilon = 1e-8
maxit = 50

def f(x):
    return x**4 - x - 2

def df(x):
    return 4*x**3 - 1

def ddf(x):
    return 12*x**2

def iter(x0: float, f: callable, df: callable, ddf: callable, eps: float, maxit: int) -> tuple[float, int]:
    x = x0
    iter = 0

    for i in range(maxit):
        iter += 1
        numerator_1 = -df(x) - math.sqrt(df(x)**2 - 2*ddf(x)*f(x))
        numerator_2 = -df(x) + math.sqrt(df(x)**2 - 2*ddf(x)*f(x))
        denominator = ddf(x)
        x_new_1 = numerator_1 / denominator
        x_new_2 = numerator_2 / denominator

        if abs(x_new_1) < abs(x_new_2):
            x_new = x_new_1
        else:
            x_new = x_new_2
        
        x = x + x_new

        print(f"x_{i+1} = {x}")
        if abs(f(x)) < eps:
            return x, iter

    return x, iter

def euler(x0: float, f: callable, df: callable, ddf: callable, eps: float, maxit: int) -> tuple[float, int]:
    x = x0
    iter = 0

    for i in range(maxit):
        iter += 1

        x_new = x - f(x) / df(x) - ddf(x) / (2*df(x)) * (f(x) / df(x))**2
        x = x_new

        print(f"x_{i+1} = {x}")
        if abs(f(x)) < eps:
            return x, iter

    return x, iter

def halley(x0: float, f: callable, df: callable, ddf: callable, eps: float, maxit: int) -> tuple[float, int]:
    x = x0
    iter = 0

    for i in range(maxit):
        iter += 1

        x_new = x - f(x) * df(x) / (df(x)**2 - 0.5 * ddf(x) * f(x))
        x = x_new

        print(f"x_{i+1} = {x}")
        if abs(f(x)) < eps:
            return x, iter

    return x, iter


print(f"iter: {iter(0.3, f, df, ddf, epsilon, maxit)}")
print(f"euler: {euler(0.3, f, df, ddf, epsilon, maxit)}")
print(f"halley: {halley(0.3, f, df, ddf, epsilon, maxit)}")
