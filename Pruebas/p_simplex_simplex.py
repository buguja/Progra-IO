__author__ = 'José Pablo'

from Enums import Mtype
from Simplex.Simplex import Simplex


"""
test = Simplex(2,3,mtype.Max)
test.addRestricion("d",[4,3],[1,0,0],12)
test.addRestricion("f",[4,1],[0,1,0],8)
test.addRestricion("g",[4,-1],[0,0,1],8)
test.addFunObj("x",[-2,-1])
"""
test = Simplex(2,2,Mtype.Min)
test.addRestricion("g",[4,1],[1,0],13)
test.addRestricion("h",[2,3],[0,1], 6)
test.addFunObj([3,-8])


#print(test);

test.Start();
print(test.result())