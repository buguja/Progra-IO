__author__ = 'luisdiegopizarro'
class ParserMochila:
     def __init__(self,text):
        self.contenedor = 0
        self.articulos = []
        self.parse(text)

     def parse(self,text):
         lineas=text.split("\n")
         self.contenedor=int(lineas[0])
         lineas=lineas[1:]
         for val in lineas:
             self.articulos.append(([int(i) for i in val.split(" ")]))


