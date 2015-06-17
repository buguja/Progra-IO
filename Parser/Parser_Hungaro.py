__author__ = 'luisdiegopizarro'
class ParserHungaro:
     def __init__(self,text):
        self.tipo = 0
        self.costos = []
        self.atiende = [1,1,1]
        self.parse(text)

     def parse(self,text):
         lineas=text.split("\n")
         self.tipo=int(lineas[0])
         if(lineas[1]!=''):
             self.atiende=[int(i) for i in lineas[1].split(" ")]
         print(lineas)
         lineas=lineas[2:]
         for val in lineas:
             self.costos.append(([int(i) for i in val.split(" ")]))

         print(self.costos)