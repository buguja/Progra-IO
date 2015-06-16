__author__ = 'José Pablo'

from Tools import fill_w
from Enums import mtype
from  Simplex.Core import SimplexCore

class DualCore1(SimplexCore):
    def __init__(self,qDescicion, qHolgura, qArtificial, qSuperhabit):
        super(qDescicion, qHolgura, qArtificial, qSuperhabit, mtype.Max)
        self.stop = lambda x: x == 1
        self.Zcuantity = 2

    def getSubZ(self,submatrix):
        return [col[-2] for col in submatrix]

    def stopf(self):
        last_row = self.getSubZ(self.artificial)
        return len([elem for elem in last_row if self.stop(elem)]) < len(last_row)

    # always must be [-1]
    def addZ(self,iDecision):
        self.addRestricion("z",iDecision,fill_w(self.holgura), fill_w(self.superhabit),fill_w(self.artificial))

    #always must be [-2]
    def addZPrima(self):
        self.addRestricion("z'",fill_w(self.decision),fill_w(self.holgura), fill_w(self.superhabit),fill_w(self.artificial,1))

    def Prepare_sub(self,sub):
        leng = len(self.base)
        for col in sub:
            acc = 0
            for i in range(0,leng-2):
                acc+=col[i]
            col[-2] -=acc

    def Prepare(self):
        self.Prepare_sub(self.decision)
        self.Prepare_sub(self.holgura)
        self.Prepare_sub(self.superhabit)
        self.Prepare_sub(self.artificial)



    def Start(self):
        if not self.CheckAcotada():
            return self
        self.Prepare()
        self.SimplexIterate()


class DualCore2(SimplexCore):
    def __init__(self,qDescicion, qHolgura, qSuperhabit, qDir):
        super(qDescicion, qHolgura, 0, qSuperhabit, qDir)
    def addRestricion(self, iBase, iDescicion, iHolgura,iSuperhabit, iSol):
        super().addRestricion(iBase,iDescicion,iHolgura,iSuperhabit,[],iSol)

class Dual():
    def __init__(self,qDescicion, qHolgura, qArtificial, qSuperhabit,qDir):
        self.fase1 = DualCore1(qDescicion, qHolgura, qArtificial, qSuperhabit)
        self.fase2 = DualCore2(qDescicion, qHolgura, qSuperhabit,qDir)

    def addRestrictuion(self, iBase, iDescicion, iHolgura,iSuperhabit, iArtificial, iSol):
        self.fase1.addRestricion(iBase, iDescicion, iHolgura,iSuperhabit, iArtificial, iSol)

    def addFunObj(self,iDecision):
        self.fase1.addZPrima()
        self.fase1.addZ(iDecision)

    def sbrow(self,sub,i):
        return [col[i] for col in sub]

    def Start(self):
        self.fase1.Start()
        for i, elem in enumerate(self.fase1.base):
            self.fase2.addRestricion(elem,self.sbrow(self.fase1.decision,i), self.sbrow(self.fase1.holgura,i),self.sbrow(self.fase1.superhabit,i) ,self.fase1.val_sol[i])
        self.fase2.Start()
