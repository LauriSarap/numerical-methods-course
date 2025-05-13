from numpy import linalg
import numpy as np

maxit = 50
epsilon = 1e-5

def F(x):
    f1 = 3*x[0] - x[1]**2 - x[2] - 2
    f2 = x[0]**2 + 10*x[1] - x[2] - 11
    f3 = x[1]**2 + 7*x[2] - 7
    return [f1, f2, f3]

def dF(x):
    f11 = 3
    f12 = -2*x[1]
    f13 = -1
    f21 = 2*x[0]
    f22 = 10
    f23 = -1
    f31 = 0
    f32 = 2*x[1]
    f33 = 7
    return [[f11,f12,f13],
            [f21,f22,f23],
            [f31,f32,f33]]

def newton(x0: list[float], F: callable, dF: callable, eps: float, maxit: int):
    x = np.array(x0, dtype=float)
    for i in range(maxit):
        jacobian = linalg.inv(dF(x))
        x_new = x - np.dot(jacobian, F(x)).flatten()
        print(f"x{i+1} = {x_new}")

        norm = linalg.norm(abs(x_new - x), ord=1)
        print(f"norm = {norm}")
        
        if norm < eps:
            return ([x_new[0], x_new[1], x_new[2]], i + 1)
        x = x_new
    return ([x_new[0], x_new[1], x_new[2]], i + 1)

def modnewton(x0: list[float], F: callable, dF: callable, eps: float, maxit: int):
    x = np.array(x0, dtype=float)
    jacobian_inv = linalg.inv(dF(x))
    
    for i in range(maxit):
        z = np.dot(jacobian_inv, F(x)).flatten()
        x_new = x - z
        print(f"x{i+1} = {x_new}")

        norm = linalg.norm(x_new - x, ord=1)
        print(f"norm = {norm}")
        
        if norm < eps:
            return ([x_new[0], x_new[1], x_new[2]], i + 1)
        x = x_new
    
    return ([x_new[0], x_new[1], x_new[2]], i + 1)

x0 = np.array([1.0, 1.0, 1.0])

print("\nNewtoni meetod:")
print(f"x = {newton(x0, F, dF, epsilon, maxit)}")

print("\nModifitseeritud Newtoni meetod:")
print(f"x = {modnewton(x0, F, dF, epsilon, maxit)}")
        
        