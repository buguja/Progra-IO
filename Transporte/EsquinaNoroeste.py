__author__ = 'luisdiegopizarro'
import numpy as np
from copy import deepcopy
def marcarFila(table,fila,cantColumnas):
    table[fila]=["-"]*(cantColumnas+1)

def marcarColumna(table,columna,cantFilas):
    for i in range(0,cantFilas+1):
            table[i][columna]="-"

#para hacer pruebas
def printTable(table):
    for i,val in enumerate(table):
        fila=''
        for j,val2 in enumerate(val):
           fila+=str(val2)+' '
        print(fila)
    print(' ')

def iteraciones(table,tablaFinal):
    contador=5
    fila=0
    columna=0
    cantFilas=len(table)-1
    cantColumnas=len(table[0])-1

    while(columna<cantColumnas and fila<cantFilas):
        oferta=table[fila][cantColumnas]
        demanda=table[cantFilas][columna]
        if(oferta<demanda):
            tablaFinal[fila][columna]=oferta
            marcarFila(table,fila,cantColumnas)
            table[cantFilas][columna]=demanda-oferta
            fila+=1
        elif(oferta>demanda):
            tablaFinal[fila][columna]=demanda
            marcarColumna(table,columna,cantFilas)
            table[fila][cantColumnas]=oferta-demanda
            columna+=1
        else:
            tablaFinal[fila][columna]=oferta
            marcarFila(table,fila,cantColumnas)
            marcarColumna(table,columna,cantFilas)

            fila+=1
            columna+=1
        contador-=1
        printTable(table)
    printTable(tablaFinal)

def limpiarTablaFinal(tablaFinal):
    filas=len(tablaFinal)
    columnas=len(tablaFinal[0])
    for i in range(0,filas-1):
        for j in range(columnas-1):
            tablaFinal[i][j]=0
    return tablaFinal

def getCostoTotal(costos,tablaFinal):
    largo=len(costos)
    costos=costos[:largo-1]
    tablaFinal=tablaFinal[:largo-1]
    for i,val in enumerate(costos):
        costos[i].pop(largo-1)
        tablaFinal[i].pop(largo-1)
    costos=np.array(costos)
    tablaFinal=np.array(tablaFinal)
    return sum(sum(costos*tablaFinal))

def esquinaNoroestre(costos):
    table=deepcopy(costos)
    tablaFinal=limpiarTablaFinal(deepcopy(costos))
    iteraciones(table,tablaFinal)
    return getCostoTotal(costos,tablaFinal)


#print(esquinaNoroestre([[5,2,7,3,80],[3,6,6,1,30],[6,1,2,4,60],[4,3,6,6,45],[70,40,70,35,0]]))
#print(esquinaNoroestre([[2,3,4,6,100],[1,5,8,3,120],[8,5,1,4,80],[4,5,6,3,95],[125,50,130,90,0]]))