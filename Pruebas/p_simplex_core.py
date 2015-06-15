__author__ = 'José Pablo'

from Enums import mtype
from  Simplex.Core import SimplexCore
from decimal import *
"""
test = SimplexCore(2,3,mtype.Max)
test.addRestricion("h",[ 2,1],[1,0,0],18)
test.addRestricion("s",[ 2,3],[0,1,0],42)
test.addRestricion("d",[ 3,1],[0,0,1],24)
test.addRestricion("z",[-3,-2],[0,0,0],0)
"""
"""
test = SimplexCore(2,3,mtype.Max)
test.addRestricion("d",[4,3],[1,0,0],12)
test.addRestricion("f",[4,1],[0,1,0],8)
test.addRestricion("g",[4,-1],[0,0,1],8)
test.addRestricion("x",[-2,-1],[0,0,0],0)
"""
"""
test = SimplexCore(2,2,0,0,mtype.Max)
test.addRestricion("f",[2,7],[1,0],[],[],21)
test.addRestricion("g",[7,2],[0,1],[],[],21)
test.addRestricion("z",[-4,-14],[0,0],[],[],0)
"""
"""
test = SimplexCore()
"""
print(test);

test.SimplexStart();

print(test);
print(test.Solucion)