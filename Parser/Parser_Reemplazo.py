__author__ = 'luisdiegopizarro'
class ParserReemplazo:
   def __init__(self,text):
        self.anoInicial=0
        self.periodo=0
        self.remplazoI=0
        self.remplazoF=0
        self.costoMaquina=0
        self.costos = []
        self.parse(text)

   def parse(self,text):
         lineas=text.split("\n")
         self.anoInicial=int(lineas[0])
         self.periodo=int(lineas[1])
         self.remplazoI=int(lineas[2])
         self.remplazoF=int(lineas[3])
         self.costoMaquina=int(lineas[4])
         lineas=lineas[5:]
         for val in lineas:
             self.costos.append([int(i) for i in val.split(" ")])





