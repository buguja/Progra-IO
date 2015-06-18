import sys
import numpy as np
from copy import deepcopy
__author__ = 'luisdiegopizarro'

strRespuesta=''
todaMatrices=[]
#se va considerar una celda como todo un conjunto de celas llamese una fila o una columna
class Celdas:
    def __init__(self,pcantidadCeros,pPosicion,pOrientacion,pPosicionCeros):
        self.cantidadCeros=pcantidadCeros
        self.posicion=pPosicion #esto es el numero de fila o columna
        self.orientacion=pOrientacion #0 si es fila 1 es si columna
        self.posicionCeros=pPosicionCeros #arreglo que dice en q posicion se encuentran los 0's
    def printCeldas(self):
        print(str(self.cantidadCeros)+" "+str(self.posicion)+" "+self.orientacion+" "+str(self.posicionCeros))

#entrada:matriz que se necesitan contar los 0's
#salida:arreglo de celdas ordenado por mayor cantidad de 0's
def contarCeros(matriz):
    largo=len(matriz)
    celdas=[]
    #cuenta los 0's en las filas
    for f in range(0,largo):
        cantcerosfila=0
        cantceroscolumn=0
        posicionCerosFilas=[]
        posicionCerosColumnas=[]
        for c in range(0,largo):
            if(matriz[f][c]==0):#encontro un 0 en fila
                cantcerosfila+=1
                posicionCerosFilas.append(c)
            if(matriz[c][f]==0):#encontro un 0 en columna
                cantceroscolumn+=1
                posicionCerosColumnas.append(c)
        celdas.append(Celdas(cantcerosfila,f,'fila',posicionCerosFilas))
        celdas.append(Celdas(cantceroscolumn,f,'columna',posicionCerosColumnas))

    quick_sort(celdas)

    return celdas

#entrada:matriz
#salida:arreglo [[filas marcadas][columnas marcadas]]
#ojo esta a veces si marca toda la matriz, pero creo q solo lo hace cuando ya funca
def marcarLineas(matriz):
    arregloCerosContados=contarCeros(matriz)
    filasMarcadas=[]
    columnasMarcadas=[]

    while(arregloCerosContados[0].cantidadCeros!=0):
        celdaMarcada=arregloCerosContados[0]
        if(celdaMarcada.orientacion=='fila'):
            filasMarcadas.append(celdaMarcada.posicion)
        else:
            columnasMarcadas.append(celdaMarcada.posicion)
        eliminarCeros(arregloCerosContados[1:],arregloCerosContados[0])
        arregloCerosContados=arregloCerosContados[1:]
        quick_sort(arregloCerosContados)
    return [filasMarcadas,columnasMarcadas]


#entra el arreglo de celdas y la celda que se esta marcando
#salida: el arreglo celdas sin la celda marcada y con las otras celdas modificadas
def eliminarCeros(arregloCeldas,celdaMarcada):
    orientacionBorrar=celdaMarcada.orientacion
    posicionBorrar=celdaMarcada.posicion
    for i,posicion in enumerate(celdaMarcada.posicionCeros):
        for j,celda in enumerate(arregloCeldas):
            if(celda.orientacion!=orientacionBorrar and celda.posicion==posicion):
                celda.cantidadCeros-=1
                celda.posicionCeros.remove(posicionBorrar)

#quicksort descendiente especial para la clase Celda
def quick_sort(items):

    if len(items) > 1:
        pivote = len(items) // 2
        itemsMenores = []
        itemsMayores = []

        for i, val in enumerate(items):
            if i != pivote:
                if val.cantidadCeros > items[pivote].cantidadCeros:
                    itemsMayores.append(val)
                else:
                    itemsMenores.append(val)
        quick_sort(itemsMayores)
        quick_sort(itemsMenores)

        items[:] = itemsMayores + [items[pivote]] + itemsMenores



def printCeldas(items):
    for i,val in enumerate(items):
        val.printCeldas()


#resta todas las filas su menor elemento respectivamente
def menorFila(matrizOriginal):
    matriz=deepcopy(matrizOriginal)
    largo=len(matriz)
    global strRespuesta
    for f in range(0,largo):
        menor=matriz[f][0]
        for c in range(0,largo):
            if(matriz[f][c]<menor):menor=matriz[f][c]
        for r in range(0,largo):matriz[f][r]=matriz[f][r]-menor
    strRespuesta+=("\n".join(["\t".join(map(str, r)) for r in matriz]))
    strRespuesta+="\n\n"
    return matriz
#resta a todas las columnas su menor elemento respectivamente
def menorColumna(matrizOriginal):
    matriz=deepcopy(matrizOriginal)
    largo=len(matriz)
    global strRespuesta
    for c in range(0,largo):
        menor=matriz[0][c]

        for f in range(0,largo):
            if(matriz[f][c]<menor):menor=matriz[f][c]
        for r in range(0,largo):matriz[r][c]=matriz[r][c]-menor
    strRespuesta+=("\n".join(["\t".join(map(str, r)) for r in matriz]))
    strRespuesta+="\n\n"
    return matriz

#resta el menor valor no marcado, a todos los valores NO marcados
#se lo suma a los valores que esten en las intersecciones
def operaMenor(matrizOriginal,celdasMarcadas):
    matriz=deepcopy(matrizOriginal)
    filas=celdasMarcadas[0]
    columnas=celdasMarcadas[1]
    menor=findMenor(matriz,celdasMarcadas)
    for i,fila in enumerate(matriz):
            for j,val in enumerate(fila):
                if((not i in filas)and (not j in columnas)):
                    matriz[i][j]=val-menor
                if(i in filas and j in columnas):
                    matriz[i][j]=val+menor
    return matriz

#encuentra el menor valor de las filas y columnas que no estan marcadas
def findMenor(matriz,celdasMarcadas):
    filas=celdasMarcadas[0]
    columnas=celdasMarcadas[1]
    menor=sys.maxsize
    for i,fila in enumerate(matriz):
        if(not i in filas):
            for j,val in enumerate(fila):
                if(not j in columnas):
                    if(val<menor):menor=val
    return menor

#entrada:celdas con los 0's contados
#salida:
def getFilas(celdas):
    arregloFilas=[]
    for i,val in enumerate(celdas):
        if(val.orientacion=='fila'):
            arregloFilas.append([val.posicion,val.posicionCeros])
    arregloFilas.sort()
    arregloFilasFinal=[]
    for j,val2 in enumerate(arregloFilas):#les quita la posicion de para solo retornas las filas
        arregloFilasFinal.append(val2[1])
    return arregloFilasFinal

#entrada:filas con las posicion de sus 0's
#salida:arreglo con las posiciones de los 0's que si son solucion
def getSoluciones(filas):
    return getSolucionesAux(filas,[],[])
def getSolucionesAux(items,solucionTotal,solucionParcial):
    if (items==[]):
        return [solucionParcial]
    for i,posiciones in enumerate(items[0]):
            if posiciones in solucionParcial:
                continue
            else:
                solucionTotal.extend(getSolucionesAux(items[1:],[],solucionParcial+[posiciones]))
    return solucionTotal

class Solucion:
    def __init__(self,valor,elementos):
        self.valor=valor
        self.elementos=elementos

def evaluar(matrizCostos,soluciones,tipo):
    respuesta=[]
    if(tipo):
        f=lambda x,y:x>y
        totalSolucion=0
    else:
        f=lambda x,y:x<y
        totalSolucion=sys.maxsize

    for i,sol in enumerate(soluciones):
        totalParcial=0
        for j,val in enumerate(sol):
            totalParcial+=matrizCostos[j][val]
        if(totalParcial==totalSolucion):
            respuesta.append(Solucion(totalSolucion,sol))

        elif(f(totalParcial,totalSolucion)):
            totalSolucion=totalParcial
            respuesta=[]
            respuesta.append(Solucion(totalSolucion,sol))
    return respuesta

def printSolucion(respuestas,pAtiende):
    for j,solucion in enumerate(respuestas):
        global strRespuesta
        contador=1
        atiende=deepcopy(pAtiende)
        for i in range(0,len(solucion.elementos)):
                strRespuesta+="El proveedor "+str(contador)+" atiende a "+str(solucion.elementos[i]+1)+"\n"
                atiende[0]-=1
                if(atiende[0]==0):
                    contador+=1
                    atiende=atiende[1:]

        strRespuesta+="Tiene un costo total de "+str(solucion.valor)+"\n\n"

#entrada:matriz original, solo se corre cuando el proceso es de maximizar
#salida:matriz con la fomra Mayor-entradas
def setMatrizMax(matrizOriginal):
    matriz=deepcopy(matrizOriginal)
    mayor=0
    global strRespuesta
    for i,f in enumerate(matriz):
        for j,c in enumerate(f):
            if(c>mayor):mayor=c
    for x,f1 in enumerate(matriz):
        for y,c1 in enumerate(f):
            matriz[x][y]=mayor-matriz[x][y]
    strRespuesta+=("\n".join(["\t".join(map(str, r)) for r in matriz]))
    strRespuesta+="\n\n"
    return matriz

#en caso de que un proveedor pueda atender varias, se va a expandir la matriz de costos para que quede de nxn
def expandirCostos(matriz,atiende):
    nueva=[]
    global strRespuesta
    for i,val in enumerate(atiende):
        for j in range(0,val):
            nueva.append(deepcopy(matriz[i]))
    strRespuesta+=("\n".join(["\t".join(map(str, r)) for r in nueva]))
    strRespuesta+="\n\n"
    return nueva

def eliminaRepetidos(soluciones,atiende):#en caso de que hayan que atienden varios, se eliminan las opciones repetidas
    if(atiende==[1]*len(atiende)):#si solo atiende 1 cada proovedor no pasa nada
        return soluciones
    op=[]
    largo=len(atiende)

    for i,val1 in enumerate(soluciones):
        d=True
        for j,val2 in enumerate(soluciones[1:]):
            conta=0
            igual=0
            for z,cant in enumerate(atiende):
                if(set(val1[conta:conta+cant])==set(val2[conta:conta+cant])):
                    igual+=1
                    conta+=cant
            if(igual==largo):
                d=False
                break
        soluciones=soluciones[1:]
        if(d):
            op.append(val1)
    return op

#tipo 0 minimizar 1 maximizar
#atiende: arreglo con la cantidad que atiende cada proveedor
def hungaro(matrizCostos,tipo,atiende):
    global strRespuesta,todaMatrices
    strRespuesta=''
    todaMatrices=[]

    matrizCostos=expandirCostos(matrizCostos,atiende)
    costos=matrizCostos

    if(tipo):
        matrizCostos=setMatrizMax(matrizCostos)
    p1=menorColumna(menorFila(matrizCostos))#resta el menor de cada fila y el de cada columna
    p2=marcarLineas(p1)#marca la lineas
    p3=p1
    while(len(p2[0])+len(p2[1])<len(matrizCostos)):#mientas no se hayan hecho suficientes marcas
        p3=operaMenor(p1,p2)#resta a todos los no marcados el menor, y a la interseccion se lo suma
        p2=marcarLineas(p3)#vuelve a marcar lineas
        strRespuesta+=("\n".join(["\t".join(map(str, r)) for r in p3]))
        strRespuesta+="\n\n"
    filasCeros=getFilas(contarCeros(p3))#arreglo con las posiciones donde estan los 0's en cada fila
    soluciones=eliminaRepetidos(getSoluciones(filasCeros),atiende)
    printSolucion(evaluar(costos,soluciones,tipo),atiende)
    return strRespuesta


hungaro([[10,9,5],[9,8,3],[6,4,7]],0,[1,1,1])
#hungaro([[13,7,12,12],[10,13,15,7],[13,10,8,7]],1,[1,2,1])
#hungaro([[10,8,2],[3,9,3],[4,10,5]],0,[1,1,1])#tiene 3 soluciones
#hungaro([[15,10,9],[9,15,10],[10,12,8]],0,[1,1,1])












