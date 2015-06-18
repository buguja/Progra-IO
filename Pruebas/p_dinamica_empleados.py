__author__ = 'José Pablo'
from Dinamica.Empleados import ContratacionEmpleados

test = ContratacionEmpleados([5,7,8,4,6],"300*x","400+200*x")
#test = ContratacionEmpleados([6,5,3,6,8],"600*x","700+300*x")
test.Start()
test.PrintB()