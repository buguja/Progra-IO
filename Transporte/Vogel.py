__author__ = 'luisdiegopizarro'
from copy import deepcopy

def redefineTable(table,tablaFinal):
    posiciones=findMaxPenali(table)
    len_filas=len(table)
    len_columnas=len(table[0])
    fila=posiciones[0]
    columna=posiciones[1]
    oferta=table[fila][len_columnas-2]
    demanda=table[len_filas-2][columna]


    if(demanda>oferta):
        table.pop(fila)
        table[len_filas-3][columna]=demanda-oferta
        tablaFinal[fila][columna]=oferta
    else:
        for i in range(0,len(table)):
            table[i].pop(columna)
            table[fila][len_columnas-3]=oferta-demanda
        tablaFinal[fila][columna]=demanda


#retorna la fila y columna del max Penali y el min en dicha fila o columna
#return [fila,columna]
def findMaxPenali(table):
    len_filas=len(table)
    len_columnas=len(table[0])
    penali_Fila=table[len_filas-1]
    penali_Columna=getColumn(len_columnas-1,table)
    max_Penali_Fila=max(penali_Fila)
    max_Penali_Columna=max(penali_Columna)

    #el valor maximo esta en la fila
    if(max_Penali_Fila>max_Penali_Columna):
        pos1=penali_Fila.index(max_Penali_Fila)#agarra el # de columna de la fila de penalizacion
        column=getColumn(pos1,table)
        column=column[:len(column)-2]
        minValue=min(column)
        pos2=column.index(minValue)

        return[pos2,pos1]
    #cualquier otro caso
    else:
        pos1=penali_Columna.index(max_Penali_Columna)
        fila=table[pos1]

        pos2=table[pos1].index(min(fila[0:len_columnas-2]))
        return [pos1,pos2]

#calcula y asigna la fila y columa de penalizacion en la table
def calculatePenali(table):
    len_filas=len(table)
    len_columnas=len(table[0])

    #calcula la penalizacion de las filas
    for i in range(0,len_filas-2):
        fila=table[i]
        table[i][len_columnas-1]=penaliCelda(fila[0:len_columnas-2])

    #calcula la penalizacion de las columnas
    for x in range(0,len_columnas-2):
        columna=getColumn(x,table)
        table[len_filas-1][x]=penaliCelda(columna[0:len_filas-2])
    return table

#llena la tabla con 0's en las penalizaciones para luego poder trabajar cayendole encima a los valores
def fillTable(table):
   for i,val in enumerate(table):
       val.append(0)
   table.append([0]*len(table[0]))
   return table


#encuentra los menores valores lo resta en valor absoluto
def penaliCelda(celda):
    menor1=min(celda)
    celda.remove(menor1)
    menor2=min(celda)
    return abs(menor1-menor2)

#para hacer pruebas
def printTable(table):
    for i,val in enumerate(table):
        fila=''
        for j,val2 in enumerate(val):
           fila+=str(val2)+' '
        print(fila)
    print(' ')

#retorna la columna que queremos de una tabla
def getColumn(index,table):
    return [row[index] for row in table]

def limpiarTablaFinal(tablaFinal):
    filas=len(tablaFinal)
    columnas=len(tablaFinal[0])
    for i in range(0,filas-1):
        for j in range(columnas-1):
            tablaFinal[i][j]=0
    return tablaFinal

def vogel(costos):
    table=deepcopy(costos)
    tablaFinal=limpiarTablaFinal(deepcopy(costos))
    fillTable(table)
    while(len(table)!=3 and len(table[0])!=3):
        calculatePenali(table)
        printTable(table)
        redefineTable(table,tablaFinal)
    print(table)
    printTable(table)
    printTable(tablaFinal)




vogel([[5,2,7,3,80],[3,6,6,1,30],[6,1,2,4,60],[4,3,6,6,45],[70,40,70,35,0]])
#vogel([[2,3,4,6,100],[1,5,8,3,120],[8,5,1,4,80],[4,5,6,3,95],[125,50,130,90,0]])
#vogel([[5,1,8,12],[2,4,0,14],[3,6,7,4],[9,10,11,0]])
