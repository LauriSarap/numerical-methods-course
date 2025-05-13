epsilon = 1e-5
maxit=50

def g1(x1, x2, x3):
    return (13 - x2**2 + 4*x3)/15

def g2(x1, x2, x3):
    return (11 + x3 - x1**2) / 10

def g3(x1, x2, x3):
    return (22 + x2**3) / 25

def G(x1: float, x2: float, x3: float, is_seidel: bool = False) -> list[float]:
    if not is_seidel:
        x1_new = g1(x1, x2, x3)
        x2_new = g2(x1, x2, x3)
        x3_new = g3(x1, x2, x3)
        return [x1_new, x2_new, x3_new]
    else:
        x1_new = g1(x1, x2, x3)
        x2_new = g2(x1_new, x2, x3)
        x3_new = g3(x1_new, x2_new, x3)
        return [x1_new, x2_new, x3_new]

def iter(x0: list[float], G: callable, q: float, eps: float, maxit: int) -> tuple[list[float], int]:
    x = x0
    for i in range(maxit):
        x1 = G(x[0], x[1], x[2])
        print(x1)

        max_row = max(abs(x1[0] - x[0]), abs(x1[1] - x[1]), abs(x1[2] - x[2]))
        if q / (1 - q) * max_row <= eps:
            return x1, i + 1
        x = x1
    
    return x, i + 1

x, iter_count = iter(x0=[0.0001, 0.0001, 0.0001], G=G, q=7/15, eps=epsilon, maxit=50)
print(f"Hariliku iteratsiooni meetodi lõpplahend: {x}, iteratsioone: {iter_count}")

def seidel(x0: list[float], G: callable, q: float, eps: float, maxit: int) -> tuple[list[float], int]:
    x = x0
    for i in range(maxit):
        x1 = G(x[0], x[1], x[2], True)
        print(x1)

        max_row = max(abs(x1[0] - x[0]), abs(x1[1] - x[1]), abs(x1[2] - x[2]))
        if q / (1 - q) * max_row <= eps:
            return x1, i + 1
        x = x1
    
    return x, i + 1

x, iter_count = seidel(x0=[0.0001, 0.0001, 0.0001], G=G, q=7/15, eps=epsilon, maxit=50)
print(f"Seideli meetodi lõpplahend: {x}, iteratsioone: {iter_count}")