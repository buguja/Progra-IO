NEWLINE = "\n"
IGUAL = "="
MENOR = ">"
MAYOR = "<"
Y = "y"
X_ = "x+"
__author__ = 'José Pablo'

class Preparser:
    def __init__(self, filename):
        self.text=""
        self.name = filename
        self.errors = []

    def adderror(self,msj):
        self.errors.append(msj)

    def addformatoerror(self, index):
        self.adderror("Mal formato en linea {}".format(index + 1))

    def pl(self):
        try:
            with open(self.name, encoding='utf-8') as file:
                data = file.readlines()
                file.close()
        except IOError:
            return False
        ret = [data[0], data[1].replace(NEWLINE,"") + X_ + data[2].replace(NEWLINE,"") + Y+ NEWLINE]
        index = 3
        while index<len(data):
            mayormenor = data[index + 2].replace(NEWLINE,"")
            igual = data[index+3].replace(NEWLINE,"")
            if(mayormenor != MAYOR and mayormenor != MENOR):
                self.addformatoerror(index)
            elif(igual!= IGUAL):
                self.addformatoerror(index)
            else:
                subx = data[index].replace(NEWLINE,"")
                suby = data[index + 1].replace(NEWLINE,"")
                subret = data[index + 4].replace(NEWLINE,"")
                ret.append(subx + X_ + suby +Y+mayormenor+igual+ subret+ NEWLINE)
            index+=5
        self.text=("".join(ret))[:-1]
        return True


