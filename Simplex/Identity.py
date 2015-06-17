__author__ = 'José Pablo'

def identiy_generator(l):
    return [[0 if row != col else 1 for row in range(0,l) ] for col in range(0,l)]

def bloqid(b,h,list,yes=1, no=0):
    return [[yes if (col,row) in list else no for row in range(0,b) ] for col in range(0,h)]