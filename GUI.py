__author__ = 'José Pablo Parajeles && Luis Diego Pizarro'

import math
import Graficador
import PL
from Enums import SimplexFamily
from Dinamica.Mochila import mochila
from Dinamica.Reemplazo import reemplazo
from Transporte.Hungaro import hungaro
from Transporte.Vogel import vogel
from Dinamica.Reemplazo import graficar
from Transp import  transporte,setTabla
from Transporte.EsquinaNoroeste import esquinaNoroestre
from Parser.Parser_Reemplazo import ParserReemplazo
from Parser.Parser_Transporte import ParserTransporte
from Parser.Parser_Vogel import ParserVogel
from Parser.Parser_Hungaro import ParserHungaro
from Parser.Parser_Mochila import ParserMochila
from Parser.Parser_PL import ParserPLG
from Parser.PosParser import Posparser
from Parser.PreParser import Preparser
from Simplex.Parser import SimplexParser
from Parser.Parser_Empleados import ContratacionEmpleados, ParserEMP



import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showwarning, showerror


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.file = ""

    # noinspection PyAttributeOutsideInit
    def create_widgets(self):

        # file loader
        self.Loader = tk.Button(self)
        self.Loader["text"] = "Abrir"
        self.Loader["command"] = self.load
        self.Loader["width"] = 50
        self.Loader.grid(row=0, column=0, columnspan=3)
        # file name
        self.FileName = tk.Label(self)
        self.FileName["text"] = "Archivo"
        self.FileName.grid(row=1, column=0)
        # file name placeholder
        self.FileNameName = tk.Label(self, text="file")
        self.FileNameName.grid(row=1, column=1, columnspan=3)
        # text
        self.TextF = tk.Text(self, height=30, width=130)
        self.TextF.grid(column=0, row=2, rowspan=10, columnspan=10)
        # Metodo Grafico
        self.Metodo_Grafico = tk.Button(self, text="Método Grafico", command=self._metodo_grafico)
        self.Metodo_Grafico.grid(column=12, row=2)
        # Transporte
        self.Transporte = tk.Button(self, text="Transporte", command=self._transporte)
        self.Transporte.grid(column=12, row=3)
        # Simplex
        self.Simplex = tk.Button(self, text="Simplex", command=self._simplex)
        self.Simplex.grid(column=12, row=4)
        # GranM
        self.GranM = tk.Button(self, text="GranM", command=self._GranM)
        self.GranM.grid(column=12, row=5)
        # DosFases
        self.DosFases = tk.Button(self, text="DosFases", command=self._DosFases)
        self.DosFases.grid(column=12, row=6)
        # Dual
        self.Dual = tk.Button(self, text="Dual", command=self._Dual)
        self.Dual.grid(column=12, row=7)

        # Hungaro
        self.Hungaro = tk.Button(self, text="Hungaro", command=self._hungaro)
        self.Hungaro.grid(column=13, row=2)
        # Vogel
        self.Vogel = tk.Button(self, text="Vogel", command=self._vogel)
        self.Vogel.grid(column=13, row=3)
        # EsquinaNoroeste
        self.Esquina = tk.Button(self, text="EsquinaNoroeste", command=self._esquina)
        self.Esquina.grid(column=13, row=4)

        # Mochila
        self.Mochila = tk.Button(self, text="Mochila", command=self._mochila)
        self.Mochila.grid(column=13, row=5)
        # Reemplazo
        self.Reemplazo = tk.Button(self, text="Reemplazo", command=self._reemplazo)
        self.Reemplazo.grid(column=13, row=6)
        #empleados
        self.Empleados = tk.Button(self, text="Empleados", command=self._empleados)
        self.Empleados.grid(column=13, row=6)


    def load(self):
        self.file = askopenfilename()
        pre = Preparser(self.file)
        self.FileNameName["text"] = self.file
        if (not pre.pl()):
            showerror(self, "Error al abrir el archivo")
        if len(pre.errors) > 0:
            msj_1 = "\n".join(pre.errors)
            showwarning(self, "Error en las siguientes restricciones:\n {}".format(msj_1))
        self.TextF.insert("1.0", pre.text)

    def _metodo_grafico(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        parser = ParserPLG()
        try:
            parser.init(text_f_get)
        except IndexError:
            showerror("Error", "No hay suficientes equaciones validas")
            return
        if (parser.val != 2):
            showerror("Error", "No tiene 2 variables, tiene: {}".format(parser.val))
            return
        if len(parser.errorequa) > 0:
            msj_1 = "\n".join(parser.errorequa)
            showwarning(self, "Error en las siguientes restricciones:\n {}".format(msj_1))
        if len(parser.eq) < 1:
            showerror(self, "No hay suficientes restricciones validas")
            return
        pos = Posparser(parser.fo, parser.eq, parser.Mm)
        origin = pos.get_originals()
        restric = pos.get_restrictions()

        objetivo = pos.funcion_objetivo
        DataGraficar = PL.getDatosPL(origin, restric, objetivo)
        puntos = DataGraficar[0]


        max_x = int(math.ceil(DataGraficar[1] * 1.10))
        max_y = int(math.ceil(DataGraficar[2] * 1.10))

        if(puntos!=[]):
            po = PL.getPtosOptimos(puntos, objetivo, pos.tipo)
            Graficador.dibujar(puntos, po[0], po[1], restric, origin, max_x, max_y)
        else:
            showerror("Error", "No Solucion")
            Graficador.dibujar(puntos,[],[], restric, origin, max_x, max_y)
    def _transporte(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        parserTran=ParserTransporte(text_f_get)
        parser = ParserPLG()

        parser.init(transporte(parserTran.PL))

        pos = Posparser(parser.fo, parser.eq, parser.Mm)
        origin = pos.get_originals()
        restric = pos.get_restrictions()

        objetivo = pos.funcion_objetivo
        DataGraficar = PL.getDatosPL(origin, restric, objetivo)
        puntos = DataGraficar[0]


        max_x = int(math.ceil(DataGraficar[1] * 1.10))
        max_y = int(math.ceil(DataGraficar[2] * 1.10))

        if(puntos!=[]):
            po = PL.getPtosOptimos(puntos, objetivo, pos.tipo)
            top = tk.Toplevel()
            string=setTabla(po[0][0])
            msg = tk.Text(top,height=40, width=130)
            msg.insert("1.0",string)
            msg.pack()
            Graficador.dibujar(puntos, po[0], po[1], restric, origin, max_x, max_y)



        else:
            showerror("Error", "No Solucion")
            Graficador.dibujar(puntos,[],[], restric, origin, max_x, max_y)
        pass
    def _hungaro(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        parser=ParserHungaro(text_f_get)
        top = tk.Toplevel()
        string=hungaro(parser.costos,parser.tipo,parser.atiende)
        msg = tk.Text(top,height=40, width=130)
        msg.insert("1.0",string)
        msg.pack()
        pass

    def _vogel(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        parser=ParserVogel(text_f_get)
        top = tk.Toplevel()
        string=vogel(parser.costos)
        msg = tk.Text(top,height=40, width=130)
        msg.insert("1.0",string)
        msg.pack()
        pass

    def _esquina(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        parser=ParserVogel(text_f_get)#si usa el mismo parser que el vogel
        top = tk.Toplevel()
        string=esquinaNoroestre(parser.costos)
        msg = tk.Text(top,height=40, width=130)
        msg.insert("1.0",string)
        msg.pack()
        pass


    def _mochila(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        parser=ParserMochila(text_f_get)
        top = tk.Toplevel()
        string=mochila(parser.articulos,parser.contenedor)
        msg = tk.Text(top,height=40, width=130)
        msg.insert("1.0",string)
        msg.pack()
        pass

    def _reemplazo(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        parser=ParserReemplazo(text_f_get)
        top = tk.Toplevel()
        string=reemplazo(parser.anoInicial,parser.periodo,parser.remplazoI,parser.remplazoF,parser.costoMaquina,parser.costos)
        msg = tk.Text(top,height=40, width=130)
        msg.insert("1.0",string)
        msg.pack()
        graficar()
        pass
    def _simplex(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        strl = text_f_get.split("\n")
        ret = SimplexParser(strl,SimplexFamily.Simplex)
        self.TextF.insert("end","\n\n-:--:--:--:--:--:--:--:--:--:--:--:--:--:-\n\n")
        self.TextF.insert("end","\n".join(ret[1].Output))
    def _GranM(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        strl = text_f_get.split("\n")
        ret = SimplexParser(strl,SimplexFamily.GranM)
        self.TextF.insert("end","\n\n-:--:--:--:--:--:--:--:--:--:--:--:--:--:-\n\n")
        self.TextF.insert("end","\n".join(ret[1].Output))
    def _DosFases(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        strl = text_f_get.split("\n")
        ret = SimplexParser(strl,SimplexFamily.DosFases)
        self.TextF.insert("end","\n\n-:--:--:--:--:--:--:--:--:--:--:--:--:--:-\n\n")
        self.TextF.insert("end","\n".join(ret[1].Output))
    def _Dual(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        strl = text_f_get.split("\n")
        ret = SimplexParser(strl,SimplexFamily.Dual)
        self.TextF.insert("end","\n\n-:--:--:--:--:--:--:--:--:--:--:--:--:--:-\n\n")
        self.TextF.insert("end","\n".join(ret[1].Output))

    def _empleados(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1] == "\n":
            showerror("Error", "Retire todos los saltos de linea al final inecesarios")
            return
        strl = text_f_get.split("\n")
        empleados = ParserEMP(strl)
        empleados.Start()
        self.TextF.insert("end","\n\n-:--:--:--:--:--:--:--:--:--:--:--:--:--:-\n\n")
        self.TextF.insert("end","\n".join(empleados.OutPut))

root = tk.Tk()
app = Application(master=root)
app.mainloop()