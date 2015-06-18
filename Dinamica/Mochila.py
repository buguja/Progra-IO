__author__ = 'luisdiegopizarro'
from copy import deepcopy

strRespuesta=''
todaMatrices=[]


def getColumn(index,matrix):
    column=[]
    for i,val in enumerate(matrix):
        column.append(val[index])
    return column

def matrizToString():
    global strRespuesta
    for i,val in enumerate(todaMatrices):
        strRespuesta+=("\n".join(["\t".join(map(str, r)) for r in val]))
        strRespuesta+="\n\n"


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
        fila.clear()
    todaMatrices.append(deepcopy(matriz))
    fx.clear()
    fx.extend(getColumn(division+1,matriz))

def calculateProducts(Contenedor,pesos):
    global strRespuesta
    pesoLibre=Contenedor
    i=0
    for val in reversed(todaMatrices):
        largo=len(val[0])
        cant=max(getColumn(largo-1,val),key=lambda x: 0 if(x*pesos[i]>pesoLibre) else x)
        pesoLibre-=cant*pesos[i]
        i+=1
        strRespuesta+="Articulo "+str(i)+" Cantidad "+str(cant)+"\n"
    ultimaMatriz=todaMatrices[len(todaMatrices)-1]
    cantColumnas=len(ultimaMatriz[0])
    strRespuesta+="Ingreso Total "+str(max(getColumn(cantColumnas-2,ultimaMatriz)))

def mochila(matrizArticulos,Contenedor):
    global strRespuesta,todaMatrices
    strRespuesta=''
    todaMatrices=[]

    fx=[0]*(Contenedor+1)
    pesos=getColumn(0,matrizArticulos)
    for val in reversed(matrizArticulos):
        peso=val[0]
        ingreso=val[1]
        llenaMatriz(Contenedor//peso,ingreso,peso,fx,Contenedor)
    matrizToString()
    calculateProducts(Contenedor,pesos)
    return strRespuesta



#mochila([[2,5],[3,6],[4,12],[1,2]],11)
#mochila([[2,5],[3,6],[4,12],[1,2]],11)
#mochila([[2,31],[3,47],[1,14]],4)
