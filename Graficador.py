__author__ = 'luisdiegopizarro/José Pablo'
import matplotlib.pyplot as plt
import numpy as np
from sympy import solve

from Tools import findInt, findXY, setdiff


def despejar(f, var):
    a = solve(f, var)
    #print(str(a[0]))
    return str(a[0])


def dibujar(puntos, ptosOptimos, valorOptimo, equations, originals, lenght_x, lenght_y):
    # lenght_x=20
    # lenght_y=20
    if(puntos!=[]):
        area = plt.Polygon(puntos, closed=True, alpha=0.5)
    ax = plt.gca()
    ax.cla()

    ax.set_xlim((0, lenght_x ))
    ax.set_ylim((0, lenght_y ))
    ax.set_aspect('equal')
    if(puntos!=[]):
         fig = plt.gcf()
         fig.gca().add_artist(area)

    x = np.linspace(0, lenght_x)
    for eq in equations:
        xy = findXY(eq)
        if xy == 0:

            ax.plot(x, eval(despejar(eq, "y")), lw=2.0)
        else:
            entero = findInt(eq)

            if xy == 1:  #inecuacion sin y
                y = (0, 100000000000)
                x1 = (entero, entero)
                ax.plot(x1, y, lw=2.0)

            elif xy == 2:  #inecuacion sin x
                x1 = (0, 100000000000)
                y = (entero, entero)
                ax.plot(x1, y, lw=2.0)
    optimos = []
    if(ptosOptimos!=[]):
        for opdot in ptosOptimos:
            opdot_x = opdot[0]
            opdot_y = opdot[1]
            optimos.append("{} = {}".format(opdot, valorOptimo))
            ax.plot(opdot_x, opdot_y, "p", markersize=12, lw=2.0)
        others = setdiff(puntos, ptosOptimos)
        for dot in others:
            ax.plot(dot[0], dot[1], "o", lw=2.0)

    ax.grid('on')

    plt.legend(originals + optimos, bbox_to_anchor=(0.75, 1), loc=2, borderaxespad=0.)

    plt.show()

def grafico(lenght_x, lenght_y,remplazoI,remplazoF,anos):
    ax = plt.gca()
    ax.set_xlim((1, lenght_x ))
    ax.set_ylim((0, lenght_y ))

    for i,val in enumerate(anos):
        for j,val2 in enumerate(val):
            if(val2<remplazoI):
                ax.plot((i+1,i+2),(val2,val2+1),color="red")
            if(remplazoI<=val2<=remplazoF):
                ax.plot((i+1,i+2),(val2,val2+1),color="red")
                ax.plot((i+1,i+2),(val2,1),color="blue")
            if(val2>remplazoF):
                ax.plot((i+1,i+2),(val2,1),color="blue")
    #ax.plot((1,2),(3,1))


    ax.grid('on')
    plt.show()






