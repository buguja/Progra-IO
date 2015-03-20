__author__ = 'José Pablo'
from Parser import PreParser

a = PreParser.Preparser(R"C:\Users\José Pablo\Dropbox\IO\Progra\Progra-IO\px2.txt")
a.pl()
print(a.errors)
print(a.text)
print("~~~~~~~~~~")
