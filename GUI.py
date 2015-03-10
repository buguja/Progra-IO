__author__ = 'José Pablo Parajeles'
import tkinter as tk
from tkinter.filedialog import askopenfilename


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
        self.TextF = tk.Text(self, height=30, width=50).grid(column=0, row=2, rowspan=5, columnspan=4)
        # Metodo Grafico
        self.Metodo_Grafico = tk.Button(self, text="Método Grafico", command=self._metodo_grafico).grid(column=5, row=2)
        # Transporte
        self.Transporte = tk.Button(self, text="Transporte", command=self._transporte).grid(column=5, row=3)
        # Simplex
        self.Transporte = tk.Button(self, text="Simplex", command=self._simplex).grid(column=5, row=4)

    def load(self):
        self.file = askopenfilename()

    def _metodo_grafico(self):
        pass

    def _transporte(self):
        pass

    def _simplex(self):
        pass


root = tk.Tk()
app = Application(master=root)


app.mainloop()