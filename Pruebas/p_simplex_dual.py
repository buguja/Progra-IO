__author__ = 'José Pablo'

from Simplex.Simplex import Simplex
from Simplex.Dual import Dual
from Enums import mtype

#"""
test = Dual(4,0,2,2,mtype.Min)
test.Base.addRestricion("s0",[1,0,6,2],[],[-1,0],[1,0],6)
test.Base.addRestricion("s1",[0,1,4,8],[],[0,-1],[0,1],10)
test.Base.addFunObj([-8,-12,-36,-20])

tx = Simplex(2,4,mtype.Max)
tx.addRestricion("h0",[1,0],[1,0,0,0],8)
tx.addRestricion("h1",[0,1],[0,1,0,0],12)
tx.addRestricion("h2",[6,4],[0,0,1,0],36)
tx.addRestricion("h3",[2,8],[0,0,0,1],20)
tx.addFunObj([-6,-10])
"""
test = Dual(3,0,2,2,mtype.Min)
test.Base.addRestricion("s0",[1,0,1],[],[-1,0],[1,0],15)
test.Base.addRestricion("s1",[0,1,1],[],[0,-1],[0,1],10)
test.Base.addFunObj([-2,-3,-4])

tx = Simplex(2,3,mtype.Max)
tx.addRestricion("h0",[1,0],[1,0,0],2)
tx.addRestricion("h1",[0,1],[0,1,0],3)
tx.addRestricion("h2",[1,1],[0,0,1],4)
tx.addFunObj([-15,-10])
#"""
test.Base.Start()
tx.Start()

