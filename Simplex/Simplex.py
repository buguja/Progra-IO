__author__ = 'José Pablo'

from Tools import fill_w
from Enums import mtype
from  Simplex.Core import SimplexCore

class Simplex (SimplexCore):
    def __init__(self, qDescicion, qHolgura, qDir=mtype.Max):
        super(qDescicion, qHolgura,0,0,0,qDir)

    def addRestricion(self, iBase, iDescicion, iHolgura, iSol):
        super().addRestricion(iBase, iDescicion, iHolgura, [], [], iSol)

    def addFunObj(self,iDescicion):
        self.addRestricion("z",iDescicion,fill_w(self.holgura))

