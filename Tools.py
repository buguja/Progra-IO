import re

__author__ = 'José Pablo'
_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","."]
_operators = ["+", "-", "*", "^", "/"]
_comparators = ["<", ">", "="]
_OpenB = "("
_CloseB =")"

def IsDigit(x):
    return _digits.count(x) == 1


def IsOperator(x):
    return _operators.count(x) == 1


def IsComparator(x):
    return _comparators.count(x) == 1


# verifica si en un string hay x o y
def findXY(ecua):
    if ecua.find('y') == -1:
        return 1
    elif ecua.find('x') == -1:
        return 2
    else:
        return 0


# retorna el numero de una ecuacion x>=2 return 2
def findInt(ecua):
    return int(re.findall(r'\d+', ecua)[0])


def setdiff(a, b):
    return [aa for aa in a if aa not in b]


def read(filenane):
    with open(filenane, encoding='utf-8') as file:
        data = file.read()
    return data

def special_div(dividendo,divisor):
    return -1 if divisor == 0 else dividendo/divisor

def fill_w(sub, w=0):
    return [w for _ in sub]

def BStack(charz,count):
    if charz == _OpenB:
        count+=1
    elif charz == _CloseB:
        count-=1
    return count

def isB(charz):
    return charz == _OpenB or charz == _CloseB

def isBClose(charz):
    return charz == _CloseB