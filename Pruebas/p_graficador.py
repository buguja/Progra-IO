import Graficador
import PL
import PosParser

__author__ = 'José Pablo'
def Grafica(restricciones,FO):
    parseado = PosParser.Posparser(p_l_s_restricciones=restricciones)

    origin=parseado.get_originals()
    restric=parseado.get_restrictions()


    DataGraficar=PL.getDatosPL(origin,restric,FO)
    puntos=DataGraficar[0]
    max_x=int(DataGraficar[1]*1.10)
    max_y=int(DataGraficar[2]*1.10)

    po=PL.getPtosOptimos(puntos,FO,1);

    Graficador.dibujar(puntos,po[0],po[1],restric,origin,max_x,max_y)

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


d=[
    "x+y-200>=0",
    "x>=0",
    "1000-x>=0",
    "y>=0",
    "700-y>=0",
    "800-x-y>=0"

]

Grafica(c,"6*x+10*y+3000")
"""
e=[
    "x<=2000",
    "y<=2000",
    "x+y<=3000"
]

Grafica(e,"1000*x+1500*y")

f=[
    "x+3y<=15",
    "5x+y<=20",
    "3x+4y<=24"
]
Grafica(f,"0.75*x+y")

g=[
    "x+y>=6",
    "x+y<=2",
    "x>=0",
    "y>=0"
]
Grafica(g,"3*x+8*y")


h=[
    "y<=2x",
    "y>=x/2"
]
Grafica(h,"x+y")




#restricciones
#['6*x+4*y-(24)', 'x+2*y-(6)', '-x+y-(1)', 'x*y*x*1+2*x-(3*x)', '3*a-(2)']
#originals
#['6*x+4*y<=24', 'x+2*y<=6', '-x+y<=1', 'x*y*x*1+2*x>=3*x', '3*a<=2']
"""
