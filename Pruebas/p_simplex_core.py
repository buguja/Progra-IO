__author__ = 'José Pablo'

from Enums import mtype
from  Simplex.Core import SimplexCore
from decimal import *
"""
test = SimplexCore(2,3,mtype.Max)
test.addRestricion("h",[Decimal( 2), Decimal(1)],[Decimal(1),Decimal(0),Decimal(0)],Decimal(18))
test.addRestricion("s",[Decimal( 3), Decimal(2)],[Decimal(0),Decimal(1),Decimal(0)],Decimal(42))
test.addRestricion("d",[Decimal( 3), Decimal(1)],[Decimal(0),Decimal(0),Decimal(1)],Decimal(24))
test.addRestricion("z",[Decimal(-3), Decimal(-2)],[Decimal(0),Decimal(0),Decimal(0)],Decimal(0))
"""
test = SimplexCore(2,3,mtype.Max)
test.addRestricion("h",[ 2,1],[1,0,0],18)
test.addRestricion("s",[ 2,3],[0,1,0],42)
test.addRestricion("d",[ 3,1],[0,0,1],24)
test.addRestricion("z",[-3,-2],[0,0,0],0)

print(test);

test.SimplexStart();

print(test);