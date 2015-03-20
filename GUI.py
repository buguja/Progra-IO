import Graficador
import PL
from Parser.Parser_PL import ParserPLG
from Parser.PosParser import Posparser
from Parser.PreParser import Preparser

__author__ = 'José Pablo Parajeles'

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showwarning, showerror
import Tools


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
        self.Loader.grid(row=0, column=0, columnspan=4)
        # file name
        self.FileName = tk.Label(self)
        self.FileName["text"] = "Archivo"
        self.FileName.grid(row=1, column=0)
        # file name placeholder
        self.FileNameName = tk.Label(self, text="file")
        self.FileNameName.grid(row=1, column=1, columnspan=3)
        # text
        self.TextF = tk.Text(self, height=30, width=50)
        self.TextF.grid(column=0, row=2, rowspan=5, columnspan=4)
        # Metodo Grafico
        self.Metodo_Grafico = tk.Button(self, text="Método Grafico", command=self._metodo_grafico)
        self.Metodo_Grafico.grid(column=5, row=2)
        # Transporte
        self.Transporte = tk.Button(self, text="Transporte", command=self._transporte)
        self.Transporte.grid(column=5, row=3)
        # Simplex
        self.Transporte = tk.Button(self, text="Simplex", command=self._simplex)
        self.Transporte.grid(column=5, row=4)

    def load(self):
        self.file = askopenfilename()
        pre = Preparser(self.file)
        self.FileNameName["text"]=self.file
        if(not pre.pl()):
            showerror(self, "Error al abrir el archivo")
        if len(pre.errors)>0:
            msj_1 = "\n".join(pre.errors)
            showwarning(self, "Error en las siguientes restricciones:\n {}".format(msj_1))
        self.TextF.insert("1.0", pre.text)

    def _metodo_grafico(self):
        text_f_get = self.TextF.get("1.0", "end-1c")
        if text_f_get[-1]=="\n":
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
        max_x = int(DataGraficar[1] * 1.10)
        max_y = int(DataGraficar[2] * 1.10)

        po = PL.getPtosOptimos(puntos, objetivo, 1);

        Graficador.dibujar(puntos, po[0], po[1], restric, origin, max_x, max_y)


    def _transporte(self):
        pass

    def _simplex(self):
        pass


root = tk.Tk()
app = Application(master=root)

app.mainloop()