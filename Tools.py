__author__ = 'José Pablo'
_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
_operators = ["+","-","*","^","(",")","/"]
_comparators = ["<",">","="]
def IsDigit(x):
    return _digits.count(x)==1

def IsOperator(x):
    return _operators.count(x) == 1

def IsComparator(x):
    return _comparators.count(x) == 1