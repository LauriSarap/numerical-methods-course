#!/usr/bin/python
import os
from numpy import *

#Siin algab teie programmikood, kus defineerite vajalikd 
#suurused ja prindite vajalikud arvud ekraanile.
#Olemasolev tekst vajab muutmist

alpha = 24
epsilon = 1e-8
maxit = 100

def f(x):
    return x * cos(x/(x-alpha))

def z(x):
    return x * 0

def loikajate_meetod(x_current: float, x_previous: float, f: callable):
    return x_current - (x_current - x_previous) / (f(x_current) - f(x_previous)) * f(x_current)

def secant(x0: float, x1: float, f: callable, epsilon: float, maxit: int):
    x_current = x1
    x_previous = x0

    print(f"x0 = {x0}, x1 = {x1}")
    
    for i in range(maxit):
        x_next = loikajate_meetod(x_current, x_previous, f)
        print(f"x{i+1} = {x_next}")

        if abs(f(x_next)) < epsilon:
            return [x_next, i+1]
        
        x_previous = x_current
        x_current = x_next

    return [x_current, maxit]

first_root, iterations_list_first_root = secant(10, 13.0, f, epsilon, maxit)
second_root, iterations_list_second_root = secant(18.0, 21.0, f, epsilon, maxit)
print(alpha, first_root, second_root)

#Siin lõppevad kõik arvutused ja algab graafikute joonestamine

x = linspace(0, 22.3, 100)
y = [f(x_i) for x_i in x]
y2 = z(x)

if not(os.environ.get('DISPLAY','') == ''):
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import tkinter as tk
    root= tk.Tk() 
    figure1 = plt.Figure(figsize=(8,8), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    
    #Graafikute joonestamise käsud andke siin
    ax1.plot(x,y, label='f(x)')
    ax1.plot(x,y2, 'k--', label='0')

    ax1.plot(first_root, 0, 'bo', markersize=8)
    ax1.plot(second_root, 0, 'bo', markersize=8)


    # Esimese nullkoha 1. lõikaja
    x0 = 10.0
    x1 = 13.0
    f_x0 = f(x0)
    f_x1 = f(x1)

    m = (f_x1 - f_x0) / (x1 - x0)
    x2 = loikajate_meetod(x1, x0, f)

    x_minimum_for_line = min([x0, x1, x2])
    x_maximum_for_line = max([x0, x1, x2])

    x_line = linspace(x_minimum_for_line, x_maximum_for_line, 100)
    y_line = [m * (x_i - x0) + f_x0 for x_i in x_line]

    ax1.plot(x_line, y_line, 'r--', label='Esimene lõikaja')

    ax1.plot(x0, f_x0, 'ro', markersize=6)
    ax1.plot(x1, f_x1, 'ro', markersize=6)
    ax1.plot(x2, 0, 'ro', markersize=6)

    # Teise nullkoha 1. lõikaja
    x0 = 18.0
    x1 = 21.0
    f_x0 = f(x0)
    f_x1 = f(x1)

    m = (f_x1 - f_x0) / (x1 - x0)
    x2 = loikajate_meetod(x1, x0, f)

    x_minimum_for_line = min([x0, x1, x2])
    x_maximum_for_line = max([x0, x1, x2])

    x_line = linspace(x_minimum_for_line, x_maximum_for_line, 100)
    y_line = [m * (x_i - x0) + f_x0 for x_i in x_line]

    ax1.plot(x_line, y_line, 'g--', label='Teine lõikaja')

    ax1.plot(x0, f_x0, 'go', markersize=6)
    ax1.plot(x1, f_x1, 'go', markersize=6)
    ax1.plot(x2, 0, 'go', markersize=6)

    ax1.grid(True)
    ax1.set_title('Lõikajate meetod')
    root.mainloop()