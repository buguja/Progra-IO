__author__ = 'José Pablo'

def list_str_w(list):
    return max(map((lambda x:len(str(x))),list))
def matrix_str_w(matrix):
    return max(list(map((lambda x:len(str(x))),[element for file in matrix for element in file ])))
def head_m(q):
    return " | ".join(["{}{}{}".format("{",str(i),":^{width}}") for i in range(0,q)])