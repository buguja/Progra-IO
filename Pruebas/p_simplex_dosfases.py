__author__ = 'José Pablo'

from Simplex.DosFases import DosFases
from Enums import mtype


test = DosFases(3,0,2,1,mtype.Min)
test.addRestricion("a1",[6,12,0],[],[-1],[1,0],40)
test.addRestricion("a2",[4, 2,4],[],[ 0],[0,1],30)
test.addFunObj([-12,-8,-8])
"""
test = DosFases(2,3,0,0,mtype.Max)
test.addRestricion("d",[4,3],[1,0,0],[],[],12)
test.addRestricion("f",[4,1],[0,1,0],[],[],8)
test.addRestricion("g",[4,-1],[0,0,1],[],[],8)
#test.addRestrictuion("x",[-2,-1],[0,0,0],[],[],0)
test.addFunObj([-2,-1])
"""
print(test.fase1)


test.Start()
