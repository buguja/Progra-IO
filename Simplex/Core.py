from Tools import special_div

__author__ = 'José Pablo'
from Enums import mtype
from Simplex.printing import list_str_w, matrix_str_w, head_m

class SimplexCore:
    def __init__(self, qDescicion, qHolgura, qDir=mtype.Min):
        self.base = []
        self.decision = []
        for i in range(0, qDescicion):
            self.decision.append([])
        self.holgura = []
        for j in range(0, qHolgura):
            self.holgura.append([])
        self.val_sol = []
        self.Solucion = ""
        # Funcion
        self.find = min if qDir == mtype.Max else max
        self.stop = lambda x: x < 0 if qDir == mtype.Max else lambda x: x > 0

        self.heigth = 0
        # Flags
        self.empateFlag = False
        self.empateList = []
        self.inlist = []
        self.multipleFlag = []

    def addRestricion(self, iBase, iDescicion, iHolgura, iSol):
        self.base.append(iBase)
        for i in range(0, len(iDescicion)):
            self.decision[i].append(iDescicion[i])
        for j in range(0, len(iHolgura)):
            self.holgura[j].append(iHolgura[j])
        self.val_sol.append(iSol)
        self.heigth += 1

    def getIn(self):
        # encuentra el valor de el min/max entre descion y holgura
        last_row = [col[-1] for col in self.decision] + [col[-1] for col in self.holgura]
        value = self.find(last_row)
        # retorna el index
        return last_row.index(value)


    def getOut(self, index_pivote_c):
        # Usar (Descicion o Holgura)
        submatrix = self.local_sub(index_pivote_c)
        index_pivote_c_1 = self.local_index(index_pivote_c)
        # Obtener la columna
        pivote_c = submatrix[index_pivote_c_1]
        # si no hay empate en el paso pasado
        if not self.empateFlag:
            # dividir ValSol / columna pivote
            list_div = [special_div(self.val_sol[i] , pivote_c[i]) for i in range(0, len(self.base))]
            # obtener el minimo
            minimum = min([positive for positive in list_div if positive > 0])
            # dejar el indece del min en empateList
            self.empateList = [o for o, val in enumerate(list_div) if val == minimum]
        # set Flag de empate si hay mas de 1 elemento en la lista
        self.empateFlag = True if len(self.empateList) > 1 else False
        # retornar el 1ro de la lista, indices de fila
        return self.empateList.pop(0)

    def local_index(self, index_pivote_c):
        leng = len(self.decision)
        return index_pivote_c if index_pivote_c < leng else index_pivote_c - leng

    def local_sub(self, index_pivote_c):
        return self.decision if index_pivote_c < len(self.decision) else self.holgura

    def map_pivote(self, matrix, pivote, index):
        # para cada elemento de la lista dividalo entre el pivote
        for col in matrix:
            col[index] /= pivote

    def update_pivote(self, index_x, index_y):
        # Usar (Descicion o Holgura)
        submatrix = self.local_sub(index_y)
        index_y_local = self.local_index(index_y)
        # obtener pivote operacional
        pivote = submatrix[index_y_local][index_x]
        # actualizar la base
        self.base[index_x] = "{}{}".format("x" if index_y == index_y_local else "h", index_y_local)
        # actualizar la submatriz de desicion
        self.map_pivote(self.decision, pivote,index_x)
        # actualizar la submatriz de holgura
        self.map_pivote(self.holgura, pivote,index_x)
        # actualizar el val solucion
        self.val_sol[index_x] /= pivote

    def map_otras(self, matrix, altura, fpivote, pivoteCol):
        for index,col in enumerate(matrix):
            col[altura] = col[altura]- (pivoteCol * fpivote[index])

    def update_resto(self, index_x, index_y):
        # fila pivote
        pivote_d = [col[index_x] for col in self.decision]
        pivote_h = [col[index_x] for col in self.holgura]
        pivote_vs = self.val_sol[index_x]
        # Usar (Descicion o Holgura)
        submatrix = self.local_sub(index_y)
        index_y_local = self.local_index(index_y)
        for fila in range(0, self.heigth):
            #No actualizar la pivote
            if(fila == index_x):
                continue
            # valor de la columna pivote en la fila actual
            pivore_columna = submatrix[index_y_local][fila]
            # actualizar resto de la filas
            # decision
            self.map_otras(self.decision,fila, pivote_d, pivore_columna)
            # holgura
            self.map_otras(self.holgura, fila, pivote_h, pivore_columna)
            # val sol
            self.val_sol[fila] = self.val_sol[fila] - (pivote_vs * pivore_columna)

    def chechSol(self):
        # Hay 0 (+|-) segun el metodo
        if (len([elem for elem in (self.decision[-1] + self.holgura[-1]) if self.stop(elem)]) > 0):
            # Hay almenos 1, iterar una vez más
            return False
        # Revisar por el degenerado
        diff = list(set(range(0, len([zero for zero in self.decision if zero == 0]))) - set(self.inlist))
        # Hay 0 de diff
        if (len(diff) > 0):
            # Caso degenerado
            self.multipleFlag = diff
            return False
        # end
        return True

    def SimplexIterate(self):
        # simplex c f
        # simplex[][i]
        var_in = self.getIn() if len(self.multipleFlag) == 0 else self.multipleFlag.pop(0)
        # Ya se uso
        self.inlist.append(var_in)
        # simples[i][]
        var_out = self.getOut(var_in)
        # pivote
        self.update_pivote(var_out,var_in)
        # resto
        self.update_resto(var_out, var_in)
        print(self)
        print()
        return self if self.chechSol() else self.SimplexIterate()

    def SimplexStart(self):
        for var_d in self.decision:
            if 0 == len([z for z in var_d if z >= 0]):
                self.Solucion = "No acotada"
                return self
        return self.SimplexIterate()

    def __str__(self):
        # Warning! Heavy use of lists comprehension ahead. Proceed with extreme care
        width = max(
            [list_str_w(self.base), matrix_str_w(self.decision), matrix_str_w(self.holgura), list_str_w(self.val_sol),
             len("Val Sol")])
        len_d = len(self.decision)
        len_h = len(self.holgura)
        heads = ["x{}".format(d) for d in range(0, len_d)] + ["h{}".format(d) for d in range(0, len_h)] + ["Val Sol"]
        quantity = 1 + 1 + len_d + len_h
        head = head_m(quantity).format("Base", *heads, width=width)
        # matrix = [head_m(quantity).format([[self.base[ii]]
        #                                   + [d_ij[ii] for d_ij in self.decision]
        #                                  + [d_jj[ii] for d_jj in self.holgura]
        #                                   + [self.val_sol[ii]] for ii in range(0,self.heigth-1)], width=width)]
        matrix = [head_m(quantity).format(str(self.base[ii]),
                                          *([str(d_ij[ii]) for d_ij in self.decision]
                                           + [str(d_jj[ii]) for d_jj in self.holgura]
                                           + [str(self.val_sol[ii])]),width=width) for ii in range(0,self.heigth)]
        matrix.insert(0,head)
        return "\n".join(matrix)
