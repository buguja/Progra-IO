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
    filas=[]
    columnas=[]
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
    printCeldas(arregloCerosContados)
    celdasMarcadas=[]

    while(arregloCerosContados[0].cantidadCeros!=0):
        celdaMarcada=arregloCerosContados[0]
        celdasMarcadas.append([celdaMarcada.orientacion,celdaMarcada.posicion])
        eliminarCeros(arregloCerosContados[1:],arregloCerosContados[0])
        arregloCerosContados=arregloCerosContados[1:]
        quick_sort(arregloCerosContados)

    print(celdasMarcadas)

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



marcarLineas([[0,6,1,0],[5,0,0,7],[5,0,0,7],[0,1,5,5]])
















