__author__ = 'José Pablo'
from Parser import Parser_PL

txt = "1\n3u+2w\n   6x + d <=3\nvaa\n3x+3<=3\n3u+3x=0\na==2\nu+u<u+u=3\nxx+3=0 "

a = Parser_PL.ParserPLG()
print(a.Mm)
print(a.fo)
print(a.eq)
a.init(txt)
print(a.Mm)
print(a.fo)
print(a.eq)
print(a.errorequa)