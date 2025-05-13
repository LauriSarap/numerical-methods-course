#!/usr/bin/python
import os
from numpy import *

#Siin algab teie programmikood, kus defineerite vajalikud funktsioonid

def f(x):
    return abs(x)

def P(m, n, x):
    
    xi = array([-1 + 2*i/m for i in range(m+1)])
    fi = f(xi)

    # Normaalvõrrandite süsteem
    A = zeros((n+1, n+1))
    b = zeros(n+1)
    
    for j in range(n+1):
        for k in range(n+1):
            A[j,k] = sum(xi**(j+k))
    
    for j in range(n+1):
        b[j] = sum(fi*xi**j)

    c = linalg.solve(A, b)

    # Lõplik lähend
    result = 0.0
    for k in range(n+1):
        result += c[k] * (x**k)
    return result

def viga(m, n):
    xx = linspace(-1, 1, 10*m+1)
    err = max(abs(P(m, n, xx) - abs(xx)))
    return err

m = 10
x=linspace(-1,1,m+1)

pn_values = []
v_values = []
for n in [2, 5, 8]:
    pn = P(m, n, x)
    pn_values.append(pn)
    v = viga(m, n)
    print(f"Viga n={n}: {v}")
    v_values.append(v)

y=f(x)

#Siin lõppevad kõik arvutused/definitsioonid ja algab graafikute joonestamine

if not(os.environ.get('DISPLAY','') == ''):
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import tkinter as tk
    root= tk.Tk() 
    figure1 = plt.Figure(figsize=(6,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    
    #Graafikute joonestamise käsud andke siin
    ax1.plot(x,y)
    for i, n in enumerate([2, 5, 8]):
        pn = pn_values[i]
        ax1.plot(x, pn, label=f'$P_{{{n}}}(x)$')

    ax1.legend()
    ax1.set_title('Vähimruutude mõttes lähendid')
    root.mainloop()