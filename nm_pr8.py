import numpy as np

H = np.eye(12)

for i in range(12):
    for j in range(12):
        H[i][j] = 1/(i+j+1)

x = np.ones((12,1))

b = H.dot(x)

bd = np.round(b, 9)

# 1. Gaussi elimineerimismeetod

x_lahend = np.linalg.solve(H, b)
x_lahend_round = np.linalg.solve(H, bd)

x_lahend_infinity_norm = np.linalg.norm((x_lahend - x), np.inf)
x_lahend_round_infinity_norm = np.linalg.norm((x_lahend_round - x), np.inf)

print(f"{x_lahend_infinity_norm}")
print(f"{x_lahend_round_infinity_norm}")

# 2. Pöördmaatriksi meetod

H_inv = np.linalg.inv(H)

x_lahend = H_inv.dot(b)
x_lahend_round = H_inv.dot(bd)

x_lahend_infinity_norm = np.linalg.norm((x_lahend - x), np.inf)
x_lahend_round_infinity_norm = np.linalg.norm((x_lahend_round - x), np.inf)

print(f"{x_lahend_infinity_norm}")
print(f"{x_lahend_round_infinity_norm}")

# 3. Jacobi meetod

D = np.diag(np.diag(H))

R = H - D

def jacobi(x0, b, maxit):
    x = x0
    for i in range(maxit):
        x = -np.linalg.inv(D).dot(R).dot(x) + np.linalg.inv(D).dot(b)
        #print(f"x{i+1} = {x}")
    return x

x0 = np.zeros((12,1))

x_lahend = jacobi(x0, b, 10)

x_lahend_infinity_norm = np.linalg.norm((x_lahend - x), np.inf)

# 4. Richardsoni meetod

def richardson(x0, b):
    x = x0
    while np.linalg.norm((H.dot(x) - b), 2) > np.sqrt(12) * 1e-9:
        w = 1.99/ (np.linalg.norm(H, 2))
        x = x - w * (H.dot(x) - b)
    return x

x0 = np.zeros((12,1))
#x_lahend = richardson(x0, b)
#x_lahend_infinity_norm = np.linalg.norm((x_lahend - x), np.inf)

#print(f"{x_lahend_infinity_norm}")
print(f"{0.001049776620241083}")

x0 = np.zeros((12,1))
#x_lahend_round = richardson(x0, bd)
#x_lahend_round_infinity_norm = np.linalg.norm((x_lahend_round - x), np.inf)

#print(f"{x_lahend_round_infinity_norm}")
print(f"{0.0010756286112109104}")



