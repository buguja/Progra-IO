__author__ = 'luisdiegopizarro'



import matplotlib.pyplot as plt
import numpy as np
from sympy import solve


def despejar(f,var):
    a = solve(f,var)
    print(str(a[0]))
    return str(a[0])




def Grafica(puntos, equations, lenght_x=10, lenght_y=10):
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
        ax.plot(x, eval(despejar(eq,"y")), lw=2.0)

    for dot in puntos:
        ax.plot(dot[0],dot[1], "o",lw=2.0)

    ax.grid('on')
    plt.legend(equations+puntos)

    plt.show()



Grafica([(1,1),(1,2),(2,2),(2,1)],["x-y","2*x-y"])







