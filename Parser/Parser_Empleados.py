__author__ = 'José Pablo'

from Dinamica.Empleados import ContratacionEmpleados

def ParserEMP(strlist):
    fun1 = strlist[0]
    fun2 = strlist[1]
    semanas = strlist[2:]
    return ContratacionEmpleados(list(map(int,semanas)),fun1,fun2)