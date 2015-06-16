__author__ = 'José Pablo'

from Simplex.Dual import Dual
from Enums import mtype

test = Dual(3,0,2,1,mtype.Min)
test.addRestrictuion("a1",[6,12,0],[],[-1],[1,0],40)
test.addRestrictuion("a2",[4, 2,4],[],[ 0],[0,1],30)
test.addFunObj([-12,-8,-8])

print(test.fase1)


print(test.fase2.stop(-2))
print(test.fase2.find(-2,5))

test.Start()
