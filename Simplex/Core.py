from Simplex.printing import list_str_w, matrix_str_w, head_m

__author__ = 'José Pablo'
from Enums import mtype


class SimplexCore:
    def __init__(self, qDescicion, qHolgura,qDir=mtype.Min):
        self.base = []
        self.decision = []
        for i in range(0,qDescicion):
            self.decision.append([])
        self.holgura = []
        for j in range(0,qHolgura):
            self.holgura.append([])
        self.val_sol = []
        self.Solucion = ""
        #Funcion
        self.find = max if qDir==mtype.Max else min

        #Flags
        self.empateFlag = False
        self.empateList = []


    def addRestricion(self,iBase, iDescicion, iHolgura, iSol):
        self.base.append(iBase)
        for i in range(0, len(iDescicion)):
            self.decision[i].append(iDescicion[i])
        for j in range(0, len(iHolgura)):
            self.holgura[i].append(iHolgura[i])
        self.val_sol.append(iSol)


    def getIndex(self):
        # encuentra el valor de el min/max entre descion y holgura
        value = self.find(self.decision[-1]+self.holgura[-1])
        # retorna el index
        return (self.decision[-1]+self.holgura[-1]).index(value)

    def getOut(self,index_pivote_c):
        # altura de la matrix
        len_decsn = len(self.decision)
        # Usar (Descicion o Holgura)
        submatrix = self.decision if index_pivote_c< len_decsn else self.holgura
        index_pivote_c_1 = index_pivote_c if index_pivote_c < len_decsn else index_pivote_c-len_decsn
        # Obtener la columna
        pivote_c = [submatrix[i][index_pivote_c_1] for i in range(0,len_decsn)]
        # si no hay empate en el paso pasado
        if not self.empateFlag:
            # dividir ValSol / columna pivote
            list_div = [self.val_sol[i]/pivote_c[i] for i in range(0,len(self.base))]
            # obtener el minimo
            minimum = min(list_div)
            # dejar el indece del min en empateList
            self.empateList = [o for o,val in enumerate(list_div) if val==minimum ]
        # set Flag de empate si hay mas de 1 elemento en la lista
        self.empateFlag = True if len(self.empateList) >1 else False
        # retornar el 1ro de la lista, indices de fila
        return self.empateList.pop(0)

    def UpdatePivote(self, index_x, index_y):
        pass


    def SimplexIterate(self):
        var_in = self.getIndex() # simplex[][i]
        var_out = self.getOut(var_in) # simples[i][]



    def SimplexStart(self):
        for var_d in self.decision:
            if 0==len([z for z in var_d if z>=0]):
                self.Solucion = "No acotada"
                return self
        return self.SimplexIterate()

    def __str__(self):
        # Warning! Heavy use of lists comprehension ahead. Proceed with extreme care
        width = max([list_str_w(self.base),matrix_str_w(self.decision),matrix_str_w(self.holgura),list_str_w(self.val_sol),len("Val Sol")])
        len_d = len(self.decision[0])
        leng_h = len(self.holgura[0])
        heads = ["x{}".format(d) for d in range(0, len_d)] + ["h{}".format(d) for d in range(0, len_d)] + ["Val Sol"]
        quantity = 1 + 1 + len_d + leng_h
        head = head_m(quantity).format("Base",*heads,width=width)
        matrix = [head_m(quantity).format([[self.base[ii]]+[d_ij for d_ij in self.decision[ii]]+[d_jj for d_jj in self.holgura[ii]]+[self.val_sol[ii]] for ii in len(self.base)],width=width)]
        return "\n".join(head+matrix)
