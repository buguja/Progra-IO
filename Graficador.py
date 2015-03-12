__author__ = 'luisdiegopizarro/José Pablo'
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import solve



import PL
import PreParser


def despejar(f,var):
    a = solve(f,var)
    print(str(a[0]))
    return str(a[0])

def Grafica(puntos, equations,originals, lenght_x=10, lenght_y=10):
    area = plt.Polygon(puntos, closed=True, alpha=0.5)
    ax = plt.gca()
    ax.cla()

    ax.set_xlim((0,lenght_x ))
    ax.set_ylim((0,lenght_y ))
    ax.set_aspect('equal')
    fig = plt.gcf()
    fig.gca().add_artist(area)

    x = np.linspace(0, 10)
    for eq in equations:
        xy=PL.findXY(eq)
        if xy==0:
            ax.plot(x, eval(despejar(eq,"y")), lw=2.0)
        else:
            entero=PL.findInt(eq)

            if xy==1:#inecuacion sin y
                y=[0,100000000000]
                x=[entero,entero]
                ax.plot(x,y,lw=2.0)

            elif xy==2:#inecuacion sin x
                x=[0,100000000000]
                y=[entero,entero]
                ax.plot(x,y,lw=2.0)

    for dot in puntos:
        ax.plot(dot[0],dot[1], "o",lw=2.0)

    ax.grid('on')
    plt.legend(originals+puntos)

    plt.show()


b = [
    "6x+4y<=24",
    "x+2y<=6",
    "-x+y<=1",
    "y<=2",
    "x>=0"
]

a = PreParser.Preparser(p_l_s_restricciones=b)
puntos=PL.getPtosArea(a.get_originals(),a.get_restrictions())



Grafica(puntos,a.get_restrictions(),a.get_originals())

#restricciones
#['6*x+4*y-(24)', 'x+2*y-(6)', '-x+y-(1)', 'x*y*x*1+2*x-(3*x)', '3*a-(2)']
#originals
#['6*x+4*y<=24', 'x+2*y<=6', '-x+y<=1', 'x*y*x*1+2*x>=3*x', '3*a<=2']


