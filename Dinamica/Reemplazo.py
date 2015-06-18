__author__ = 'luisdiegopizarro'

rt=[]
ct=[]
st=[]
ft=[]
remI=0
I=0
anoMax=0

strRespuesta=''
todaMatrices=[]

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

def ultimaEtapa(posiciones):
    global rt,ct,st,anoMax,matrizEtapa
    matrizEtapa=[['t','K','R','f(t)','D']]
    #matrizEtapa=[]
    for i,val in enumerate(posiciones):
        fila=[]
        t=val
        fila.append(val)
        if(val<anoMax):
            fila.append(rt[t]+st[t+1]-ct[t])
        else:
            fila.append('-')
        fila.append(rt[0]+st[t]+st[1]-ct[0]-I)
        maxVal=max(fila,key=lambda x: 0 if(type(x)==str) else x)
        fila.append(maxVal)
        if(fila.index(maxVal)==2):
                    D='R'
        else:
            D='K'
        fila.append(D)
        matrizEtapa.append(fila)
    todaMatrices.append(matrizEtapa)
    RespuestaFinal(matrizEtapa)
    return matrizEtapa

def etapas(posiciones):
    global rt,ct,st,ft,anoMax,remI,todaMatrices
    matrizEtapa=[['t','K','R','f(t)','D']]
    for i,val in enumerate(posiciones):
        fila=[]
        t=val
        fila.append(val)
        if(val<anoMax):
            fila.append(rt[t]-ct[t]+ft[0][ft[1].index(val+1)])
        else:
            fila.append('-')
        if(val<remI):
            fila.append('-')
        else:
            fila.append(rt[0]+st[t]-ct[0]-I+ft[0][1])
        maxVal=max(fila,key=lambda x: 0 if(type(x)==str) else x)
        fila.append(maxVal)
        if(fila.index(maxVal)==2):
                    D='R'
        else:
            D='K'
        fila.append(D)
        matrizEtapa.append(fila)
    todaMatrices.append(matrizEtapa)
    ft.clear()
    ft.append(getColumn(3,matrizEtapa))
    ft.append(getColumn(0,matrizEtapa))
    RespuestaFinal(matrizEtapa)

def llenarMatriz(inicial,lapso,remplazoI,remplazoF,ano,matriz):#llena el grafico
    matriz[ano].append(inicial)
    if(ano==lapso-1):
        return matriz
    if(inicial>remplazoF):
        return llenarMatriz(1,lapso,remplazoI,remplazoF,ano+1,matriz)
    if(remplazoI<=inicial<=remplazoF):
        llenarMatriz(inicial+1,lapso,remplazoI,remplazoF,ano+1,matriz)
        return llenarMatriz(1,lapso,remplazoI,remplazoF,ano+1,matriz)
    if(inicial<remplazoI):
        return llenarMatriz(inicial+1,lapso,remplazoI,remplazoF,ano+1,matriz)

def respuesta():
    global todaMatrices,strRespuesta
    matrizRespuesta=[[],[],[]]
    fila=todaMatrices[-1]
    A1=fila[1][0]
    costoTotal=fila[1][3]
    i=1
    for val in reversed(todaMatrices):
        matrizRespuesta[0].append("Ano "+str(i))
        columnaAnos=getColumn(0,val)
        indexAno=columnaAnos.index(A1)
        fila=val[indexAno]
        D=fila[4]
        matrizRespuesta[1].append(A1)
        matrizRespuesta[2].append(D)
        if(D=="R"):
            A1=1
        else:
            A1+=1
        i+=1
    RespuestaFinal(matrizRespuesta)
    strRespuesta+="La ganancia tota es de "+str(costoTotal)




def reemplazo(inicial,lapso,remplazoI,remplazoF,Icosto,Mcostos):
    global rt,ct,st,ft,I,anoMax,remI,strRespuesta,todaMatrices
    rt=[]
    ct=[]
    st=[]
    ft=[]
    remI=0
    I=0
    anoMax=0

    strRespuesta=''
    todaMatrices=[]
    rt=getColumn(0,Mcostos)
    ct=getColumn(1,Mcostos)
    st=getColumn(2,Mcostos)
    I=Icosto
    anoMax=len(Mcostos)-1
    remI=remplazoI

    matriz=[]
    for i in range(0,lapso):
        matriz.append([])
    matrizllena=llenarMatriz(inicial,lapso,remplazoI,remplazoF,0,matriz)
    for i in range(0,lapso):#esto llena lo del grafico
        matrizllena[i]=list(set(matrizllena[i]))

    mat=ultimaEtapa(matrizllena[len(matrizllena)-1])
    ft.append(getColumn(3,mat))
    ft.append(getColumn(0,mat))

    matrizllena.pop()
    for val in reversed(matrizllena):
        etapas(val)

    #print(todaMatrices)
    respuesta()
    return strRespuesta
#ano inicial,periodo,lapso del remplazo,lapso remplazo,costo maquina,costos)


'''
reemplazo(2,4,3,5,100000,[[20000,200,0],
                          [19000,600,80000],
                          [18500,1200,60000],
                          [17200,1500,50000],
                          [15500,1700,30000],
                          [14000,1800,10000],
                          [12200,2200,5000]])
'''


'''
reemplazo(3,4,1,5,100000,[[20000,200,0],
                          [19000,600,80000],
                          [18500,1200,60000],
                          [17200,1500,50000],
                          [15500,1700,30000],
                          [14000,1800,10000],
                          [12200,2200,5000]])
                          '''
