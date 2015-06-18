__author__ = 'José Pablo'

from fractions import Fraction
from Tools import fill_w
from Enums import Mtype
from  Simplex.Core import SimplexCore

class DosFasesCore1(SimplexCore):
    def __init__(self,qDescicion, qHolgura, qArtificial, qSuperhabit):
        super().__init__(qDescicion, qHolgura, qArtificial, qSuperhabit, Mtype.Max)
        self.stop = lambda x: x == 1
        self.Zcuantity = 2

    def getSubZ(self,submatrix):
        return [col[-2] for col in submatrix]

    def stopf(self):
        last_row = self.getSubZ(self.artificial)
        return len([elem for elem in last_row if self.stop(elem)]) < len(last_row)

    def chechSol(self):
        # Hay 0 (+|-) segun el metodo
        if self.stopf():
            # Hay almenos 1, iterar una vez más
            return False
        return True

    # always must be [-1]
    def addZ(self,iDecision):
        self.addRestricion("z",iDecision,fill_w(self.holgura), fill_w(self.superhabit),fill_w(self.artificial),0)

    #always must be [-2]
    def addZPrima(self):
        self.addRestricion("z'",fill_w(self.decision),fill_w(self.holgura), fill_w(self.superhabit),fill_w(self.artificial,1),0)

    def Prepare_sub(self,sub):
        for col in sub:
            acc = 0
            for i in range(0,self.heigth-2):
                acc+=col[i]
            col[-2] -=acc

    def Prepare_valSol(self):
        acc = 0
        for i in range(0,self.heigth-2):
            acc+=self.val_sol[i]
        self.val_sol[-2] -=acc

    def Prepare(self):
        self.Prepare_sub(self.decision)
        self.Prepare_sub(self.holgura)
        self.Prepare_sub(self.superhabit)
        self.Prepare_sub(self.artificial)
        self.Prepare_valSol()



    def Start(self):
        if not self.CheckAcotada():
            return self
        self.Prepare()
        print(self)
        return self.SimplexIterate()


class DosFasesCore2(SimplexCore):
    def __init__(self,qDescicion, qHolgura, qSuperhabit, qDir):
        super().__init__(qDescicion, qHolgura, 0, qSuperhabit, qDir)

    def addRestricion(self, iBase, iDescicion, iHolgura,iSuperhabit, iSol):
        super().addRestricion(iBase,iDescicion,iHolgura,iSuperhabit,[],iSol)




class DosFases():

    def __init__(self,qDescicion, qHolgura, qArtificial, qSuperhabit,qDir):
        self.fase1 = DosFasesCore1(qDescicion, qHolgura, qArtificial, qSuperhabit)
        self.fase2 = DosFasesCore2(qDescicion, qHolgura, qSuperhabit,qDir)
        self.Result="";
        self.Output = []

    def addRestricion(self, iBase, iDescicion, iHolgura,iSuperhabit, iArtificial, iSol):
        self.fase1.addRestricion(iBase, list(map(Fraction.from_float,iDescicion)),
                                 list(map(Fraction.from_float,iHolgura)),
                                 list(map(Fraction.from_float,iSuperhabit)),
                                 list(map(Fraction.from_float,iArtificial)), iSol)

    def addFunObj(self,iDecision):
        self.fase1.addZPrima()
        self.fase1.addZ(iDecision)

    def sbrow(self,sub,i):
        return [col[i] for col in sub]

    def Start(self):
        self.Output.append(str(self.fase1))
        ret = self.fase1.Start()
        self.Output+=ret.Output
        self.Output.append(" ")
        if(ret.val_sol[-2]!=0):
            result = "Sin Solución"
            return self.fase1
        for i, elem in enumerate(self.fase1.base):
            if i == self.fase1.heigth-2:
                continue
            self.fase2.addRestricion(elem,self.sbrow(ret.decision,i), self.sbrow(ret.holgura,i),self.sbrow(ret.superhabit,i) ,ret.val_sol[i])
        ret2 = self.fase2.Start() if not self.fase2.chechSol() else self.fase2
        self.Output+= ret2.Output
        return ret2
