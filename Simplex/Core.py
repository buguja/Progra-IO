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
