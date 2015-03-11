__author__ = 'luisdiegopizarro'
from sympy.solvers import solve
from sympy import Symbol
import re
import PreParser


def getPtosArea(restricciones,ecuaciones):

    todospuntos=calcularPuntosEjes(ecuaciones)
    rectas=todospuntos[0]#tiene los puntos para saber las rectas y luego calcular intersecciones
    puntosArea=todospuntos[1]#guarda los puntos de dichas rectas

    puntosArea=(calcularPuntosInterseccion(rectas,puntosArea))#se le agregar los puntos de intersecciones de rectas
    puntosSol=puntosSolucion(puntosArea,restricciones)
    print(puntosSol)

class Ecuacion():
    def __init__(self):
        self.pto1=[]
        self.pto2=[]

    def setPoints(self,ecua):
        y = Symbol('y')
        x=0
        self.pto1=(x,  (ecua(x,y), y)[0])

        x = Symbol('x')
        y=0
        self.pto2=(solve(ecua(x,y), x)[0],y)

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return (x,y)
    else:
        return False

#verifica si en un string hay x o y
def findXY(ecua):
    if ecua.find('y')==-1:
        return 1
    elif ecua.find('x')==-1:
        return 2
    else:
        return 0

#retorna el numero de una ecuacion x>=2 return 2
def findInt(ecua):
    return int(re.findall(r'\d+', ecua)[0])

#eilima los repetidos de una arreglo
def eliminaRepetidos(lista):
    lista_nueva=[lista[0]]
    for i in lista:
      repetido=1
      for y  in lista_nueva:
          if i==y:
              repetido=0
              break
      if repetido:
          lista_nueva.append(i)
    return lista_nueva


def calcularPuntosEjes(ecuaciones):
    rectas=[]
    puntos=[]
    for i in ecuaciones:
        form1=Ecuacion()
        xy=findXY(i)
        if xy==0:
            form1.setPoints(lambda x,y:eval(i))
        else:
            entero=findInt(i)
            if xy==1:#inecuacion sin y
                form1.pto1=(entero,0)
                form1.pto2=(entero,1)

            if xy==2:#inecucion sin x
                form1.pto1=(0,entero)
                form1.pto2=(1,entero)

        rectas.append(form1)
        puntos.append(form1.pto1)
        puntos.append(form1.pto2)
    return [rectas,puntos]


def calcularPuntosInterseccion(rectas,puntos):
    for x in range(0,len(rectas)):
        for y in range(x, len(rectas)):
            L1 = line(rectas[x].pto1,rectas[x].pto2)
            L2 = line(rectas[y].pto1, rectas[y].pto2)
            R = intersection(L1, L2)
            if R:
                puntos.append(R)
    puntos.append((0,0))
    return puntos



def puntosSolucion(puntos,restricciones):
    puntosSol=[]
    for p in puntos:
        x=p[0]
        y=p[1]
        contador=0#cuenta cuantas restricciones cumple
        for ec in restricciones:
            if eval(ec):
                contador+=1
            else:
                break
        if contador==len(restricciones):
            puntosSol.append(p)

    puntosSol=eliminaRepetidos(puntosSol)
    return puntosSol

b = [
    "6x+4y<=24",
    "x+2y<=6",
    "-x+y<=1",
    "y<=2",
    "x>=0"
]


a = PreParser.Preparser(p_l_s_restricciones=b)


getPtosArea(a.get_originals(),a.get_restrictions())





