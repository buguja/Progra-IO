__author__ = 'luisdiegopizarro'
class ParserVogel:
     def __init__(self,text):
        self.costos = []
        self.parse(text)

     def parse(self,text):
         lineas=text.split("\n")
         for val in lineas:
             self.costos.append([int(i) for i in val.split(" ")])
