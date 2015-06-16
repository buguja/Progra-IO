__author__ = 'luisdiegopizarro'
from copy import deepcopy

class FxCant():
    def __init__(self,pFx,pCantArticulos):
        self.fx=pFx
        self.CantArticulos=pCantArticulos

todaMatrices=[]

def getColumn(index,matrix):
    column=[]
    for i,val in enumerate(matrix):
        column.append(val[index])
    return column

def llenaMatriz(division,ingreso,pesoArt,fx,capacidadContenedor):
    matriz=[]
    fila=[]
    fxIndex=[0]*(division+1) #este array va tener las posiciones del fx para irlas sumando en la iteracion
    for j in range(0,capacidadContenedor+1):
        for i in range(0,division+1):
             if(pesoArt*i>j):
                fila.append('-')
             else:
                 fila.append(i*ingreso+fx[fxIndex[i]])
                 fxIndex[i]+=1

        fila.append(max(fila,key=lambda x: 0 if(type(x)==str) else x))
        fila.append(fila.index(max(fila,key=lambda x: 0 if(type(x)==str) else x)))
        matriz.append(deepcopy(fila))
        print(fila)
        fila.clear()
    todaMatrices.append(deepcopy(matriz))
    fx.clear()
    fx.extend(getColumn(division+1,matriz))

def calculateProducts(Contenedor,pesos):
    pesoLibre=Contenedor
    i=0
    for val in reversed(todaMatrices):
        largo=len(val[0])
        cant=max(getColumn(largo-1,val),key=lambda x: 0 if(x*pesos[i]>pesoLibre) else x)
        print (cant)
        pesoLibre-=cant*pesos[i]
        i+=1
    ultimaMatriz=todaMatrices[len(todaMatrices)-1]
    cantColumnas=len(ultimaMatriz[0])
    print(max(getColumn(cantColumnas-2,ultimaMatriz)))

def mochila(matrizArticulos,Contenedor):
    fx=[0]*(Contenedor+1)
    pesos=getColumn(0,matrizArticulos)
    for val in reversed(matrizArticulos):
        peso=val[0]
        ingreso=val[1]
        print (Contenedor//peso)
        llenaMatriz(Contenedor//peso,ingreso,peso,fx,Contenedor)
        print ('')
    calculateProducts(Contenedor,pesos)



mochila([[2,5],[3,6],[4,12],[1,2]],11)
#mochila([[2,31],[3,47],[1,14]],4)
