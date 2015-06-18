from Enums import Mtype

__author__ = 'José Pablo'

from Tools import fill_w
from fractions import Fraction
from Simplex.TypeM import M
from Simplex.Core import SimplexCore
class GranM(SimplexCore):


    def __init__(self, qDescicion, qHolgura, qArtificial, qSuperhabit, qDir):
        super().__init__(qDescicion, qHolgura, qArtificial, qSuperhabit, qDir)
        self.prepF = 1 if qDir==Mtype.Min else -1


    def addFunObj(self,iDescicion):
        super().addRestricion("z",list(map(M,map(Fraction.from_float,iDescicion))),
                              fill_w(self.holgura,M(0)),
                              fill_w(self.superhabit, M(0)),
                              fill_w(self.artificial, M(Fraction(0,1),Fraction(self.prepF*-1,1))),
                              M(0))
    def addRestricion(self, iBase, iDescicion, iHolgura,iSuperhabit, iArtificial, iSol):
        super().addRestricion(iBase,list(map(M,map(Fraction.from_float,iDescicion))),
                                 list(map(M,map(Fraction.from_float,iHolgura))),
                                 list(map(M,map(Fraction.from_float,iSuperhabit))),
                                 list(map(M,map(Fraction.from_float,iArtificial))), M(Fraction.from_float(iSol)))

    def getRowsM(self):
        return [i for col in self.artificial for i,elem in enumerate(col) if elem == 1]

    def Prep_sub(self,sub, cols):
        for col in sub:
            col[-1] += sum(map((lambda x: col[x]),cols))*M(0,self.prepF)
    def Prep(self):
        cols = self.getRowsM()
        self.Prep_sub(self.decision,cols)
        self.Prep_sub(self.holgura,cols)
        self.Prep_sub(self.superhabit,cols)
        self.Prep_sub(self.artificial,cols)
        self.val_sol[-1] += sum(map((lambda x: self.val_sol[x]),cols))*M(0,self.prepF)


    def Start(self):
        if not self.CheckAcotada():
            return self
        else:
            self.Prep()
            self.Output.append(str(self))
            self.SimplexIterate()