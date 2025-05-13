import math

x = 1.5
k = 8
delta = 0.5 * 10**(-k)

def f(x, k=k):
    return round(math.exp(2*x), k)

def dfdx(x):
    return 2*math.exp(2*x)

def valem_1(x, h):
    return (f(x+h)-f(x)) / h

def valem_2(x, h):
    return (f(x+h)-f(x-h)) / (2*h)

def valem_3(x, h):
    return (f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)) / (12*h)

def h_optimaalne_valem_1(x):
    return math.sqrt(2 * delta / abs(4 * math.exp(2*x)))

def h_optimaalne_valem_2(x):
    return (3 * delta / abs(8 * math.exp(2*x))) ** (1/3)

def h_optimaalne_valem_3(x):
    return (15 * delta / (2 * abs(32 * math.exp(2*x)))) ** (1/5)

valemid = [valem_1, valem_2, valem_3]
h_opt_valemid = [h_optimaalne_valem_1, h_optimaalne_valem_2, h_optimaalne_valem_3]
oige = dfdx(x)

for j in range(0, 3):

    parim_i = None
    parim_h = None
    parim_vaartus = None
    parim_viga = float('inf')

    for i in range(1, 10):
        h = 10**(-i)
        vaartus = valemid[j](x, h)
        viga = abs(vaartus - oige)
        #print(h, vaartus, viga)
        if viga < parim_viga:
            parim_viga = viga
            parim_i = i
            parim_h = h
            parim_vaartus = vaartus
    
    h_optimaalne = h_opt_valemid[j](x)

    print(parim_i, parim_h, parim_vaartus, parim_viga, h_optimaalne)