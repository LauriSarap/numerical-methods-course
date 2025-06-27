import typing
import math


def f(x: float) -> float:
    return x*math.exp(x)

def area(a: float, b: float) -> float:
    def integral(x):
        return math.exp(x) * (x-1)
    
    return integral(b) - integral(a)

def ristkylik(a: float, b: float, f: typing.Callable,  n: int) -> float :
    h = (b-a)/n
    S = 0.0

    for i in range(n):
        fi = f(a + (i+0.5)*h)
        S += fi
    
    return S*h

def trapets(a: float, b: float, f: typing.Callable, n: int) -> float:
    h = (b-a)/n
    Sum = 0.0
    for i in range(n+1):
        xi = a + h*i
        if i == 0 or i == n:
            Sum += f(xi)
        else:
            Sum += 2*f(xi)
    
    return h/2 * Sum

def simpson(a: float, b: float, f: typing.Callable, n: int) -> float:
    h = (b-a)/n
    Sum = 0.0
    for i in range(n+1):
        xi = a + h*i
        if i == 0 or i == n:
            Sum += f(xi)
        elif i % 2 == 0:
            Sum += 2*f(xi)
        else:
            Sum += 4*f(xi)    
    
    return h / 3 * Sum

def runge(a: float, b: float, f: typing.Callable, valem: str, eps: float):

    error = math.inf
    n = 2
    while True:
        if valem == "ristkylik":
            approx_2h = ristkylik(a,b,f,n)
            n = n * 2
            approx_h = ristkylik(a,b,f,n)
            error = abs(approx_h - approx_2h) / (2**2 - 1)
        elif valem == "trapets":
            approx_2h = trapets(a,b,f,n)
            n = n * 2
            approx_h = trapets(a,b,f,n)
            error = abs(approx_h - approx_2h) / (2**2 - 1)
        elif valem == "simpson":
            approx_2h = simpson(a,b,f,n)
            n = n * 2
            approx_h = simpson(a,b,f,n)
            error = abs(approx_h - approx_2h) / (2**4 - 1)
        
        print(f"n: {n}, error: {error}")

        if error <= eps:
            return [approx_h, n]

s_approx_1 = ristkylik(1,2,f,8)
s_approx_2 = trapets(1,2,f,8)
s_approx_3 = simpson(1,2,f,8)
s = area(1,2)

print(s_approx_1)
print(s_approx_2)
print(s_approx_3)
print(s)


tulem = runge(1,2,f,"ristkylik",1e-5)
print(tulem)
tulem = runge(1,2,f,"trapets",1e-5)
print(tulem)
tulem = runge(1,2,f,"simpson",1e-5)
print(tulem)

