import math
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt

n = 10
h = 2*math.pi/n

# Võrk
x = np.linspace(0, 2*math.pi, n+1)

# Kvadratuurvalemi kaalud
w = np.ones(n+1) * h
w[0] = h/2.0
w[n] = h/2.0

# B maatriks
B = np.zeros((n+1, n+1))
for i in range(n+1):
    for j in range(n+1):
        B[i, j] = w[j] * math.sin(x[i] + 2*x[j])

# b vektor
b = x.copy()

# A maatriks ehk A = (I - B)
A = np.eye(n+1) - B

### 1. Pöördmaatriksi leidmine
start=timer()
A_inverse = np.linalg.inv(A)

u_1 = np.dot(A_inverse, b)
end=timer()
print(u_1)
print(f"Aega kulus {end - start} sekundit\n")

### 2. Gaussi elimineerimismeetod

start=timer()
u_2 = np.linalg.solve(A, b)
end=timer()

print(u_2)
print(f"Aega kulus {end - start} sekundit\n")

### 3. Harilik iteratsioonimeetod

u_i = np.zeros(n+1)
max_iter = 1000

start=timer()
for i in range(max_iter):
    u_next = np.dot(B, u_i) + b

    if np.linalg.norm(u_next - u_i) < 1e-7:
        break

    u_i = u_next

u_3 = u_i
end=timer()
print(u_3)
print(f"Aega kulus {end - start} sekundit\n")

# Täpsed lahendid
u_4 = x - np.pi * np.cos(x)

plt.figure()
plt.plot(x, u_4, 'k-', label='Täpne lahend')
plt.plot(x, u_1, 'ro--', label='Pöördmaatriksi leidmine')
plt.plot(x, u_2, 'bs--', label='Gaussi elimineerimismeetod')
plt.plot(x, u_3, 'gx--', label='Harilik iteratsioonimeetod')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.legend()
plt.title("N={}".format(n))
plt.show()