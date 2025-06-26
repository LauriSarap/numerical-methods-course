import math

def f(x):
    return 1 / (1 + x**2)

def newton_cortes(n: int, a: float, b: float) -> float:
    if n == 3:
        coefficients = [1/8, 3/8, 3/8, 1/8]
    elif n == 4:
        coefficients = [7/90, 32/90, 12/90, 32/90, 7/90]
    elif n == 5:
        coefficients = [19/288, 75/288, 50/288, 50/288, 75/288, 19/288]
    elif n == 6:
        coefficients = [41/840, 216/840, 27/840, 272/840, 27/840, 216/840, 41/840]
    
    h = (b - a) / n
    sum = 0.0
    for i in range(n + 1):
        xi = a + i*h
        sum += coefficients[i] * f(xi)
        #print(f"i: {i}, x: {xi:.6f}, coefficient: {coefficients[i]:.6f}, f(xi): {f(xi):.6f}, partial sum: {sum:.6f}")
    
    integral = (b - a) * sum
    return integral

def trapets_valem(n: int, a: float, b: float) -> float:
    h = (b - a) / n
    sum = 0.0
    for i in range(n + 1):
        xi = a + i*h
        if i == 0 or i == n:
            sum += f(xi)
        else:
            sum += 2*f(xi)
    integral = h/2 * sum
    return integral

actual_value = 2 * math.atan(4)

for i in range(3,7):
    newton_cortes_value = newton_cortes(i, -4, 4)
    trapets_value = trapets_valem(i, -4, 4)
    diff_with_cortes= actual_value - newton_cortes_value
    diff_with_trapets = actual_value - trapets_value

    print(i, newton_cortes_value, diff_with_cortes, diff_with_trapets)