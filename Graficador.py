__author__ = 'luisdiegopizarro/José Pablo'

import matplotlib.pyplot as plt
import numpy as np
from sympy import solve



import PL
import PreParser


def despejar(f,var):
    a = solve(f,var)
    print(str(a[0]))
    return str(a[0])

def Dibujar(puntos,ptosOptimos,valorOptimo,equations,originals,lenght_x,lenght_y):

    #lenght_x=20
    #lenght_y=20
    area = plt.Polygon(puntos, closed=True, alpha=0.5)
    ax = plt.gca()
    ax.cla()

    ax.set_xlim((0,lenght_x ))
    ax.set_ylim((0,lenght_y ))
    ax.set_aspect('equal')
    fig = plt.gcf()
    fig.gca().add_artist(area)

    x = np.linspace(0, lenght_x)
    print(lenght_y)

    for eq in equations:
        xy=PL.findXY(eq)
        if xy==0:
            ax.plot(x, eval(despejar(eq,"y")), lw=2.0)
        else:
            entero=PL.findInt(eq)

            if xy==1:#inecuacion sin y
                y=(0,100000000000)
                x1=(entero,entero)
                ax.plot(x1,y,lw=2.0)

            elif xy==2:#inecuacion sin x
                x1=(0,100000000000)
                y=(entero,entero)
                ax.plot(x1,y,lw=2.0)

    for dot in puntos:
        ax.plot(dot[0],dot[1], "o",lw=2.0)

    ax.grid('on')
    plt.legend(originals+ptosOptimos+[valorOptimo])

    plt.show()




def Grafica(restricciones,FO):
    parseado = PreParser.Preparser(p_l_s_restricciones=restricciones)

    origin=parseado.get_originals()
    restric=parseado.get_restrictions()


    DataGraficar=PL.getDatosPL(origin,restric,FO)
    puntos=DataGraficar[0]
    max_x=int(DataGraficar[1]*1.10)
    max_y=int(DataGraficar[2]*1.10)

    po=PL.getPtosOptimos(puntos,FO,1);

    Dibujar(puntos,po[0],po[1],restric,origin,max_x,max_y)

b = [
    "6x+4y<=24",
    "x+2y<=6",
    "-x+y<=1",
    "y<=2",
    "x>=0"
]

c=[
    "4x+5y<=40",
    "2x+5y<=30",
    "x>=0",
    "y>=0"
]

'''
d=[
    "x+y-200>=0",
    "x>=0",
    "1000-x>=0",
    "y>=0",
    "700-y>=0",
    "800-x-y>=0"

]

Grafica(d,"6*x+10*y+3000")
'''

'''
e=[
    "x<=2000",
    "y<=2000",
    "x+y<=3000"
]

Grafica(e,"1000*x+1500*y")
'''

f=[
    "x+3y<=15",
    "5x+y<=20",
    "3x+4y<=24"
]
Grafica(f,"0.75*x+y")






#restricciones
#['6*x+4*y-(24)', 'x+2*y-(6)', '-x+y-(1)', 'x*y*x*1+2*x-(3*x)', '3*a-(2)']
#originals
#['6*x+4*y<=24', 'x+2*y<=6', '-x+y<=1', 'x*y*x*1+2*x>=3*x', '3*a<=2']


