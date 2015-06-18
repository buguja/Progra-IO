__author__ = 'José Pablo'


class ContratacionEmpleados:
    def __init__(self, ibi, str_C1, str_C2):
        self.bi = ibi
        self.C1 = lambda x: eval(str_C1)
        self.C2 = lambda x: eval("0 if x<=0 else " + str_C2)
        self.qetapa = len(ibi)
        self.etapa = self.qetapa
        self.matrix_etapa = [[] for _ in ibi]
        self.sols = []
        self.currntSol = 0

    def get_bi(self, i):
        return 0 if i == 0 else self.bi[i - 1]

    def get_xi(self, i):
        if i == self.qetapa:
            return [self.get_bi(i)]
        else:
            return [elem[0] for elem in self.matrix_etapa[i][1:]]

    def get_xn(self, init, finit, maximo):
        mayor = self.get_bi(init)
        menor = self.get_bi(finit)
        if mayor >= menor:
            return list(range(menor, max(mayor, maximo) + 1))
        else:
            return list(range(menor, max(menor, maximo) + 1))

    def get_acumulado(self, etapa, xin):
        if etapa == self.qetapa:
            return 0
        head = [row[0] for row in self.matrix_etapa[etapa][1:]]
        return self.matrix_etapa[etapa][head.index(xin) + 1][-2]

    def Iterate(self):
        last_xn = 0
        for etapa in range(self.qetapa, 0, -1):
            x_n = self.get_xn(etapa, etapa - 1, last_xn) if etapa != 1 else [0]
            x_i = self.get_xi(etapa)
            last_xn = max(x_n)

            bi = self.get_bi(etapa)

            current_matrix = self.matrix_etapa[etapa - 1]
            current_matrix.append([])
            current_row = current_matrix[0]
            current_row.append("xn")
            current_row += x_i[:]
            current_row.append("f{}(x{})".format(etapa, etapa - 1))
            current_row.append("x{}*".format(etapa))

            for i, row in enumerate(x_n):
                current_matrix.append([])
                current_row = current_matrix[i + 1]
                current_row.append(x_n[i])
                temp = []
                for col in x_i:
                    accumulado = self.get_acumulado(etapa, col)
                    temp.append(self.C1(col - bi) + self.C2(col - row) + accumulado)
                current_row += temp[:]
                minimum = min(temp[:])
                current_row.append(minimum)
                current_row.append([x_i[o] for o, val in enumerate(temp) if val == minimum])
                # end fila
                # end etapa

    def getNext(self, etapa, val):
        head = [row[0] for row in self.matrix_etapa[etapa-1][1:]]
        return self.matrix_etapa[etapa-1][head.index(val) + 1][-1]

    def CheckSol(self):
        self.sols.append([])
        lastL = self.matrix_etapa[0][1][-1]
        for i, subsol in enumerate(lastL):
            if (i == 0):
                self.sols[0].append(subsol)
                self.AuxCheckSol(2, subsol, 0)
            else:
                self.currntSol += 1
                self.sols.append(self.sols[0])
                self.AuxCheckSol(2, subsol, self.currntSol)

    def AuxCheckSol(self, etapa, last, solnum):
        if etapa>self.qetapa:
            return
        lastL = self.getNext(etapa, last)
        for i, subsol in enumerate(lastL):
            if (i == 0):
                self.sols[solnum].append(subsol)
                self.AuxCheckSol(etapa + 1, subsol, solnum)
            else:
                self.currntSol += 1
                self.sols.append(self.sols.append(self.sols[solnum]))
                self.AuxCheckSol(etapa + 1, subsol, self.currntSol)

    def PrintB(self):
        strbf = "{0}{1}\t{0}{1}".format("{",":^{width}}")
        for sol in self.sols:
            leng = max(max(map((lambda x:len(str(x))),sol)),10)
            print(strbf.format("Semana #", "Contratar",width=leng))
            for i,sol in enumerate(sol):
                print(strbf.format(i,sol,width=leng))


    def Start(self):
        self.Iterate()
        self.CheckSol()
