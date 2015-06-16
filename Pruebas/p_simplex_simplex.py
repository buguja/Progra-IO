__author__ = 'José Pablo'

from Enums import mtype
from Simplex.Simplex import Simplex


test = Simplex(2,3,mtype.Max)
test.addRestricion("d",[4,3],[1,0,0],12)
test.addRestricion("f",[4,1],[0,1,0],8)
test.addRestricion("g",[4,-1],[0,0,1],8)
test.addRestricion("x",[-2,-1],[0,0,0],0)

print(test);

test.Start();