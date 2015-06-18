__author__ = 'luisdiegopizarro'
class ParserTransporte:
     def __init__(self,text):
        self.PL = []
        self.parse(text)

     def parse(self,text):
         lineas=text.split("\n")
         for val in lineas:
             self.PL.append([int(i) for i in val.split(" ")])
