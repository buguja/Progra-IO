__author__ = 'luisdiegopizarro'
from copy import deepcopy
'''
matriz=[['x','y','500-x-y'],['200-x','300-y','-100+x+y']]
x=0
y=100
'''

matrizEquations=[]
equations=''
costos=[]
strRespuesta=''

def RespuestaFinal(Matriz):
    global strRespuesta
    s = [[str(e) for e in row] for row in Matriz]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    strRespuesta+= '\n'.join(table)
    strRespuesta+="\n\n"

def setTabla(solucion):
    global matrizEquations,strRespuesta

    x=solucion[0]
    y=solucion[1]
    nuevaMatriz=deepcopy(matrizEquations)
    for i,val in enumerate(matrizEquations):
        fila=[]
        for j,val2 in enumerate(val):
            nuevaMatriz[i][j]=eval(val2)
            fila.append(eval(val2))
        nuevaMatriz.append(fila)
    print(nuevaMatriz)

#setTabla(matriz,[x,y])
def setEquations(matriz):
    global equations
    for i,val in enumerate(matriz):
        for j,val2 in enumerate(val):
            equations+=val2+">=0\n"
    return equations[:-1]

def setFO():
    global matrizEquations,costos,equations
    equations='0\n'
    for i in range(0,len(matrizEquations)):
        for j in range(0,len(matrizEquations[0])):
            equations+=str(costos[i][j])+"*("+str(matrizEquations[i][j])+")+"
    equations=equations[:-1]+"\n"

def transporte(pcostos):
    global matrizEquations,costos,strRespuesta
    matriz=[]
    strRespuesta=''
    costos=pcostos
    fila1=['x','y',str(costos[0][3])+'-x'+'-y']
    fila2=[str(costos[2][0])+'-x',str(costos[2][1])+'-y',str(int(costos[2][2])-int(costos[0][3]))+'+x+y']
    matriz.append(fila1)
    matriz.append(fila2)
    matrizEquations=matriz
    setFO()
    return setEquations(matriz)


#print(transporte([[3,7,1,800],[2,2,6,1500],[1000,700,600,0]]))

'''
transporte([[50,60,10,500],
             [25,40,20,400],
            [200,300,400,0]])
        '''

