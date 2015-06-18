__author__ = 'luisdiegopizarro'
import sys

strRespuesta=''
todasMatrices=[]

def RespuestaFinal(Matriz):
    global strRespuesta
    s = [[str(e) for e in row] for row in Matriz]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    strRespuesta+= '\n'.join(table)
    strRespuesta+="\n\n"

def getColumn(index,matrix):
    column=[]
    for i,val in enumerate(matrix):
        column.append(val[index])
    return column

def tablas(etapas,pesos):
    global todasMatrices
    acumulado=[0]*len(etapas[len(etapas)-2])
    for i in range(len(etapas)-1,0,-1):#recorre las etapas
        fila=[]
        matriz=[]
        for j in range(0,len(etapas[i-1])):#recorre la etapa anterior
            #matriz=[['x',etapas[i][j],'f(x)','X']]
            fila.append(str(etapas[i-1][j]))
            for z in range(0,len(etapas[i])):#nodos destino
                element=pesos[etapas[i-1][j]][etapas[i][z]]
                if(element==0):
                    fila.append('-')
                else:
                    fila.append(element+acumulado[z])
            minElemnt=min(fila,key=lambda x: sys.maxsize if(type(x)==str) else x)
            fila.append(minElemnt)
            fila.append(etapas[i][fila.index(minElemnt)-1])
            matriz.append(fila[:])
            fila.clear()
        acumulado=getColumn(len(matriz[0])-2,matriz)
        RespuestaFinal(matriz)
        todasMatrices.append(matriz[:])
        matriz.clear()

def calcularEtapas(pesos):
    etapas=[[1]]
    for i in range(1,len(pesos)):
        singleEtapa=[]
        for j in range(1,len(pesos[0])):
            if(pesos[i][j]!=0):
                if(not j in etapas[len(etapas)-1]):
                     singleEtapa.append(j)
        if(singleEtapa!=[]):
            etapas.append(singleEtapa)
    return etapas


def calcularRespuesta():
    global strRespuesta,todasMatrices
    nodo=todasMatrices[-1][0][-1]
    strRespuesta+="1->"
    strRespuesta+=str(nodo)+"->"
    for i in reversed(todasMatrices[:-1]):
        nodo=i[1][-1]
        strRespuesta+=str(nodo)+"->"
    strRespuesta=strRespuesta[:-2]
    strRespuesta+="\nEl Costo es: "+str(todasMatrices[-1][0][-2])






def rutacorta(pesos):
    global strRespuesta,todasMatrices
    todasMatrices=[]
    strRespuesta=''
    etapas=calcularEtapas(pesos)
    tablas(etapas,pesos)
    calcularRespuesta()
    print(strRespuesta)
    return strRespuesta

'''
rutacorta([
[0,1,2,3,4,5,6,7,8,9,10],
[1,0,2,4,3,0,0,0,0,0,0],
[2,0,0,0,0,7,4,6,0,0,0],
[3,0,0,0,0,3,2,4,0,0,0],
[4,0,0,0,0,4,1,5,0,0,0],
[5,0,0,0,0,0,0,0,1,4,0],
[6,0,0,0,0,0,0,0,6,3,0],
[7,0,0,0,0,0,0,0,3,3,0],
[8,0,0,0,0,0,0,0,0,0,3],
[9,0,0,0,0,0,0,0,0,0,4],
[10,0,0,0,0,0,0,0,0,0,0]])
'''

rutacorta([
[0,1,2,3,4,5,6,7],
[1,0,5,9,8,0,0,0],
[2,0,0,0,0,10,17,0],
[3,0,0,0,0,4,10,0],
[4,0,0,0,0,9,0,0],
[5,0,0,0,0,0,0,8],
[6,0,0,0,0,0,0,9],
[7,0,0,0,0,0,0,0]])
