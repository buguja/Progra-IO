__author__ = 'José Pablo'

class SimplexCore:
    def __init__(self, qDescicion, qHolgura):
        self.base = []
        self.descicion = []
        for i in range(0,qDescicion):
            self.descicion.append([])
        self.holgura = []
        for j in range(0,qHolgura):
            self.holgura.append([])
        self.val_sol = []
        self.Solucion = ""
        #Flags
        self.empateFlag = False

    def addRestricion(self,iBase, iDescicion, iHolgura, iSol):
        self.base.append(iBase)
        for i in range(0, len(iDescicion)):
            self.descicion[i].append(iDescicion[i])
        for j in range(0, len(iHolgura)):
            self.holgura[i].append(iHolgura[i])
        self.val_sol.append(iSol)

    def SimplexIterate(self):
        pass


    def SimplexStart(self):
        for var_d in self.descicion:
            if 0==len([z for z in var_d if z>=0]):
                self.Solucion = "No acotada"
                return self
        return self.SimplexIterate()
