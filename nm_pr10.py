#!/usr/bin/python
import os
from numpy import *
import math
#Siin algab teie programmikood, kus defineerite vajalikud funktsioonid

def f(x):
    return abs(x)

def knotseq(n):
    return linspace(-1, 1, n+1)

def knotsch(n):
    x = []
    for i in range(n+1):
        x.append(math.cos(math.pi*(2*i+1)/(2*(n+1))))
    return x

def l(solmed, n, i, x):
    l = 1
    for j in range(n+1):
        if i != j:
            l *= (x-solmed[j])/(solmed[i]-solmed[j])
    return l

def lagr(solmed, n, x):
    P = 0
    for i in range(n+1):
        P += f(solmed[i]) * l(solmed, n, i, x)
    return P

def difsuhe(solmed):
    x = solmed
    y = [f(xi) for xi in solmed]
    
    n = len(solmed)
    if n == 1:
        return f(solmed[0])
    
    # Maatriks
    diff_suhted = [[0 for i in range(n)] for i in range(n)]

    # Esimeses reas 0 astme differentsuhted ehk funktsioon ise
    for i in range(n):
        diff_suhted[i][0] = y[i]
    
    # Järgnevad astmed tulenevad kolmnurksest maatriks-tabelist
    # Iga differentsuhe tabelis kohal [i][j] kasutab
    # väärtusi tablelist [i+1][j-1] ja [i][j-1]
    for j in range(1, n):
        for i in range(n - j):
            lugeja = diff_suhted[i+1][j-1] - diff_suhted[i][j-1]
            nimetaja = x[i+j] - x[i]
            diff_suhted[i][j] = lugeja / nimetaja

    # Tagastame n-1 järku differentssuhte
    return float(diff_suhted[0][n-1])

def newton(solmed, n, x):
    coefs = []
    for i in range(n+1):
        coefs.append(difsuhe(solmed[:i+1]))
    
    P = coefs[0]
    korrutis = 1

    for i in range(1, n+1):
        korrutis *= (x - solmed[i-1])
        P += coefs[i] * korrutis
    
    return P

def viga(solmed, n):
    x_tihedam = linspace(-1, 1, 10*n + 1)
    max_viga = 0
    for xi in x_tihedam:
        lagrange = lagr(solmed, n, xi)
        error = abs(f(xi) - lagrange)
        if error > max_viga:
            max_viga = error
    
    return float(max_viga)

erinevad_solmed = [4, 8, 12]

for s_a in erinevad_solmed:
    print(f"\n Sõlmede arv: {s_a}")

    # Võrdsed vahed
    solmed = knotseq(s_a)
    error = viga(solmed, s_a)
    print(f"Võrdsete vahedega sõlmede viga: {error}")

    # Tšebõšovi vahed
    solmed = knotsch(s_a)
    error = viga(solmed, s_a)
    print(f"Tšebõšovi sõlmede viga: {error}")

# Joonistamine
x_plot = linspace(-1, 1, 200)
y_orig = f(x_plot)

polynoomid = []
for s_a in erinevad_solmed:
    solmed_tsebs = knotsch(s_a)
    y_lagr = array([lagr(solmed_tsebs, s_a, xi) for xi in x_plot])
    polynoomid.append((s_a, y_lagr, solmed_tsebs))


#Siin lõppevad kõik arvutused/definitsioonid ja algab graafikute joonestamine
if not(os.environ.get('DISPLAY','') == ''):
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import tkinter as tk
    root= tk.Tk() 
    figure1 = plt.Figure(figsize=(10,7), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    
    #Graafikute joonestamise käsud andke siin
    ax1.plot(x_plot, y_orig, 'k-', linewidth=2, label='$f(x) = |x|$')

    varvid = ['b-', 'r-', 'g-']
    for i, (aste, y_poly, solmed) in enumerate(polynoomid):
        ax1.plot(x_plot, y_poly, varvid[i], linewidth=1.5, label=f'$P_{{{aste}}}(x)$ Lagrange')
        
        # Sõlmed
        ax1.plot(solmed, f(solmed), 'o', markersize=4, color=varvid[i][0])

    ax1.legend()
    ax1.grid(True)
    ax1.set_title('Interpolatsioonipolünoomid Tšebõšovi sõlmedega')
    root.mainloop()