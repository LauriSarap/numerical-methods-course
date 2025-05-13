import math
alpha=24
eps = 1e-8
maxit = 20

def g_small(x):
    return (1+0.001*alpha)**x / (10+alpha)

def g_small_derivative(x):
    return ((math.log(1+0.001*alpha))/(10+alpha)) * (1+0.001*alpha)**x

def g_large(x):
    return (math.log((10+alpha)*x))/(math.log(1+0.001*alpha))

def iter(x0: float, g: callable, eps: float, maxit: int) -> float:

    x = x0

    if g == g_small:
        q_complex_inverse = ((1 - g_small_derivative(1)) / g_small_derivative(1))
        epsilon = eps * q_complex_inverse
    else:
        epsilon = eps

    print("Starting with x0 =", x)
    for i in range(maxit):
        x1 = g(x)
        print(f"x{i+1} = {x1}")
        if abs(x1 - x) <= epsilon:
            return x1
        x = x1
    return x1

smaller_solution = iter(0.5, g_small, eps, maxit)
greater_solution = iter(1, g_large, eps, maxit)

print(alpha,smaller_solution, greater_solution)