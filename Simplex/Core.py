__author__ = 'José Pablo'

class SimplexCore:
    rMAX=True
    rMIN=False
    def __init__(self, qDescicion, qHolgura,qDir=rMIN):
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
        self.find = max if qDir else min

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

    def getOut(self):
        index_pivote_c = self.getIndex()
        len_decsn = len(self.decision)
        pivote_c = self.decision[index_pivote_c] if index_pivote_c< len_decsn else self.holgura[index_pivote_c- len_decsn]
        if  self.empateFlag:
            pass
        else:
            for divi in []: #> add lista de divisiones ##> check for 0=> inf
                pass #find el menor ##> check for equals => flag


    def SimplexIterate(self):
        pass


    def SimplexStart(self):
        for var_d in self.decision:
            if 0==len([z for z in var_d if z>=0]):
                self.Solucion = "No acotada"
                return self
        return self.SimplexIterate()
