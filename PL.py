from Tools import findXY, findInt

__author__ = 'luisdiegopizarro'
from sympy.solvers import solve
from sympy import Symbol
import math


def getDatosPL(originals,restricciones,FO):

    todospuntos=calcularPuntosEjes(restricciones)
    rectas=todospuntos[0]#tiene los puntos para saber las rectas y luego calcular intersecciones
    puntosArea=todospuntos[1]#guarda los puntos de dichas rectas



    puntosArea=(calcularPuntosInterseccion(rectas,puntosArea))#se le agregar los puntos de intersecciones de rectas
    puntosSol=puntosSolucion(puntosArea,originals)
    print(puntosSol)

    Limites=getMaxXY(puntosArea)
    max_x=Limites[0]
    max_y=Limites[1]

    puntosSol=sortPointsPolygon(puntosSol)
    return [puntosSol,max_x,max_y]

class Ecuacion():
    def __init__(self):
        self.pto1=[]
        self.pto2=[]

    def setPoints(self,ecua):
        y = Symbol('y')
        x=0
        self.pto1=(x,solve(ecua(x,y), y)[0])

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
        entero=1
        if xy==0:
            form1.setPoints(lambda x,y:eval(i))
            puntos.append(form1.pto1)
            puntos.append(form1.pto2)
        else:
            entero=findInt(i)
            if xy==1:#inecuacion sin y
                form1.pto1=(entero,0)
                form1.pto2=(entero,1)
                puntos.append(form1.pto1)

            if xy==2:#inecucion sin x
                form1.pto1=(0,entero)
                form1.pto2=(1,entero)
                puntos.append(form1.pto1)

        if entero!=0:#esta condicion es para no volver a meter los ejes x>=0 y>=0
            rectas.append(form1)

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

def sortPointsPolygon(pp):
    cent=(sum([p[0] for p in pp])/len(pp),sum([p[1] for p in pp])/len(pp))
    pp.sort(key=lambda p: math.atan2(p[1]-cent[1],p[0]-cent[0]))
    return pp

def getMaxXY(puntos):#retorna losvalores maximos para poder dibujar bien cada eje
    max_x=0
    max_y=0
    for i in puntos:
        x=i[0]
        y=i[1]
        if(x>max_x):
            max_x=x
        if(y>max_y):
            max_y=y
    return [max_x,max_y]

def getPtosOptimos(puntos,FO,determin):#determin 1 Max 0 para Min

    ptosOptimos=[]
    x=puntos[0][0]
    y=puntos[0][1]
    ptoOp=eval(FO)
    ptosOptimos.append((x,y))#se agrega el primer punto para tener un margen de comparacion
    if determin==1:
        fun=lambda x:x>=ptoOp
    elif determin==0:
        fun=lambda x:x<=ptoOp

    puntos=puntos[1:]
    for i in puntos:
        x=i[0]
        y=i[1]
        ptoEval=eval(FO)

        if fun(ptoEval):
            if ptoEval==ptoOp:#si se encuentra un optimo con el mismo valor
                ptosOptimos.append((x,y))
            else:
                ptosOptimos=[(x,y)]
            ptoOp=ptoEval

    return (ptosOptimos,ptoOp)

