import sys
__author__ = 'luisdiegopizarro'

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

#
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



#marcarLineas([[0,6,1,0],[5,0,0,7],[5,0,0,7],[0,1,5,5]])

#resta todas las filas su menor elemento respectivamente
def menorFila(matriz):
    largo=len(matriz)
    for f in range(0,largo):
        menor=matriz[f][0]
        for c in range(0,largo):
            if(matriz[f][c]<menor):menor=matriz[f][c]
        for r in range(0,largo):matriz[f][r]=matriz[f][r]-menor

    return matriz
#resta a todas las columnas su menor elemento respectivamente
def menorColumna(matriz):
    largo=len(matriz)
    for c in range(0,largo):
        menor=matriz[0][c]

        for f in range(0,largo):
            if(matriz[f][c]<menor):menor=matriz[f][c]
        for r in range(0,largo):matriz[r][c]=matriz[r][c]-menor
    return matriz

#resta el menor valor no marcado, a todos los valores NO marcados
#se lo suma a los valores que esten en las intersecciones
def operaMenor(matriz,celdasMarcadas):
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





a=menorColumna(menorFila([[10,9,5],[9,8,3],[6,4,7]]))
b=marcarLineas(a)
print(operaMenor(a,b))
















