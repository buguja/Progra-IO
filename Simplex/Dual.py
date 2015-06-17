__author__ = 'José Pablo'

from Simplex.Core import SimplexCore
from Simplex.Simplex import Simplex
from Simplex.DosFases import DosFases

class Dual:
    def __init__(self,qDescicion, qHolgura, qArtificial, qSuperhabit, qDir):
        self.Base = Simplex(qDescicion,qHolgura,qDir) if qArtificial<1 else DosFases(qDescicion, qHolgura, qArtificial, qSuperhabit, qDir)

    def Start(self):
        return self.Base.Start()


