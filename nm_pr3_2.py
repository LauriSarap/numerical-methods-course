
def f(x) -> float:
    return (4*x - 7) / (x - 2)

def df(x) -> float:
    return -1 / (x - 2)**2

def newton(x0, f: callable, df: callable, eps: float, maxit: int) -> tuple[float, int]:
    x = x0
    delta = 1
    for i in range(maxit):
        x_new = x - f(x)/df(x)
        delta = abs(x_new - x)
        x = x_new
        print(f"Iteration {i + 1}: x = {x}, delta = {delta}")
        if delta < eps:
            return x, i + 1

    return x, i + 1

x, i = newton(0.5, f, df, 1e-5, 20)
print(f"x* = {x}, iterations = {i}")
