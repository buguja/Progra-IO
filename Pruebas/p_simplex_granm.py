__author__ = 'José Pablo'

from Simplex.GranM import GranM
from Enums import mtype

test = GranM(2,2,1,1,mtype.Max)
test.addRestricion("h0",[2,0],[1,0],[0],[0],8)
test.addRestricion("h1",[0,4],[0,1],[0],[0],24)
test.addRestricion("h2",[6,10],[0,0],[-1],[1],60)
test.addFunObj([-6,-10])

print(test)
print()
print()

test.Start()
