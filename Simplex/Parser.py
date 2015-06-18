__author__ = 'José Pablo'


from Simplex.Simplex import Simplex
from Simplex.GranM import GranM
from Simplex.DosFases import DosFases
from Simplex.Dual import Dual

from Enums import SimplexFamily, Mtype
from Simplex.Identity import bloqid

def SimplexParser(strlist,metodo):
    temp = [inequa.split(" ") for inequa in strlist]
    restric = temp[:-1]
    fo=temp[-1]

    # para generar los bloques
    col_h = 0
    col_s = 0
    col_a = 0

    list_h = []
    list_s = []
    list_a = []

    varD = []
    valSol = []


    # inicia para darle vuelta al dual
    if metodo == SimplexFamily.Dual:
        len_d = len(restric[0])
        tmp_mx = [[] for _ in fo[1:]]
        tm_va = []
        minmax = fo[0].upper()
        if (minmax == "MAX"):
            tm_va.append("Min")
        elif (minmax == "MIN"):
            tm_va.append("Max")
        else:
            raise Exception("No Max o min en FO, llego {}".format(fo[0]))
        for row in restric:
            symbol = row[-2]
            if symbol == "<=" or symbol == "<":
                continue
            elif symbol == "=":
                row[-2] = "<="
            else:
                stop = len(row)
                for i in range(0, stop):
                    if i==stop:
                        row[i] = "<="
                    else:
                        row[i]*=-1

        for j,row in enumerate(restric):
            for i,elem in enumerate(row):
                if (i==len_d-1):
                    tm_va.append(elem)
                elif (i == len_d-2):
                    continue
                else:
                    tmp_mx[i].append(elem)
        for row in tmp_mx:
            row.append(">=")
        for ix,row in enumerate(tmp_mx):
            row.append(fo[ix+1])


        fo = tm_va
        restric = tmp_mx

    #finaliza la vuelta del dual
    for i,line in enumerate(restric):
        varD.append(list(map(int,line[0:-2])))
        valSol.append(int(line[-1]))
        symbol = line[-2]
        if symbol == "<=" or symbol == "<":
            list_h.append((i,col_h))
            col_h+=1
        elif symbol == ">=" or symbol == ">":
            list_s.append((i,col_s))
            col_s+=1
            list_a.append((i,col_a))
            col_a+=1
        elif symbol == "=":
            list_a.append((i,col_a))
            col_a+=1
        else:
            raise Exception("Formato incorrecto en la linea {}, llego un {}".format(i,symbol))

    altura = len(valSol)
    len_d = len(varD[0])
    bloque_h = bloqid(col_h,altura,list_h)
    bloque_s = bloqid(col_s,altura,list_s,-1)
    bloque_a = bloqid(col_a,altura,list_a)

    minmax = fo[0].upper()
    qdir = None
    if (minmax == "MAX"):
        qdir = Mtype.Max
    elif (minmax == "MIN"):
        qdir = Mtype.Min
    else:
        raise Exception("No Max o min en FO, llego {}".format(fo[0]))
    valFo = list(map((lambda x: x*-1), map(int,fo[1:])))

    base = None
    if metodo == SimplexFamily.Simplex:
        base = Simplex(len_d,col_h,qdir)
    elif metodo == SimplexFamily.GranM:
        base = GranM(len_d,col_h,col_a,col_s,qdir)
    elif metodo == SimplexFamily.DosFases:
        base = DosFases(len_d,col_h,col_a,col_s,qdir)
    elif metodo == SimplexFamily.Dual:
        base = Dual(len_d,col_h,col_a,col_s,qdir)
    else:
        raise Exception("Método Desconocido")

    if metodo ==SimplexFamily.Simplex:
        for i in range(0,altura):
            base.addRestricion("i{}".format(i),varD[i],bloque_h[i],valSol[i])
        base.addFunObj(valFo)
    elif metodo ==SimplexFamily.Dual:
        if col_a <1:
            for i in range(0,altura):
                base.Base.addRestricion("i{}".format(i),varD[i],bloque_h[i],valSol[i])
            base.Base.addFunObj(valFo)
        else:
            for i in range(0,altura):
                base.Base.addRestricion("i{}".format(i),varD[i],bloque_h[i],bloque_s[i],bloque_a[i],valSol[i])
            base.Base.addFunObj(valFo)
    else:
        for i in range(0,altura):
            base.addRestricion("i{}".format(i),varD[i],bloque_h[i],bloque_s[i],bloque_a[i],valSol[i])
        base.addFunObj(valFo)

    return (base,base.Start())





