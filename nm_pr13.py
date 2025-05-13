def ristkylik(a: float, b: float, f: callable, n: int):
    h = (b-a)/n
    S = 0
    for i in range(n):
        fi = f(a + (i+0.5)*h)
        S += fi
    return S*h

def trapets(a: float, b: float, f: callable, n: int):
    h = (b-a)/n
    S = f(a) + f(b)
    for i in range(1, n):
        fi = f(a + i*h)
        S += 2*fi
    return h/2 * S

def simpson(a: float, b: float, f: callable, n: int):
    h = (b-a)/n
    S = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            S += 2*f(a + i*h)
        else:
            S += 4*f(a + i*h)
    return h/3 * S