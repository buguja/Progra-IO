__author__ = 'José Pablo'
from Enums import mtype
from  Simplex.Core import SimplexCore

class DualCore1(SimplexCore):
    def __init__(self,qDescicion, qHolgura, qArtificial, qSuperhabit):
        super(qDescicion, qHolgura, qArtificial, qSuperhabit, mtype.Max)

    #def


class DualCore2(SimplexCore):
    def __init__(self,qDescicion, qHolgura, qArtificial, qSuperhabit, qDir):
        super(qDescicion, qHolgura, qArtificial, qSuperhabit, qDir)