__author__ = 'José Pablo'

from Tools import IsDigit, IsOperator, IsComparator


class ParserPLG:
    def __init__(self):

        self.val = 0
        self.vals = {}
        self.keys = {}
        self.parsedeq = []
        self.__eq = ""
        self.Mm = -1
        self.fo = ""
        self.eq = []
        self.errorequa = []

    def init(self, text=""):
        self.__eq = text.split("\n")[:]
        self.__validate()
        self.Mm = self.__eq[0]
        self.fo = self.__eq[1]
        self.eq = self.__eq[2:]

    def __next_sub(self, var):
        try:
            a = self.vals[var]
        except KeyError:
            a = ["x", "y", "z", "w", "v", "u"][self.val]
            self.val += 1
        return a

    def __validate(self):
        parsedeq = []
        for eaq in self.__eq:
            lastchar = ""
            chars = []
            errorcode = False
            comparador = False
            for c in eaq:
                if c == " ":
                    continue
                elif lastchar == "":
                    if c == "":
                        pass  # Do nothing
                    elif IsDigit(c):
                        chars.append(c)
                    elif IsOperator(c):
                        if c == "+" or c == "-":
                            chars.append(c)
                        else:
                            errorcode = True
                            break
                    elif IsComparator(c):
                        errorcode = True
                        break
                    else:
                        cnext = self.__next_sub(c)
                        self.keys[cnext] = c
                        self.vals[c] = cnext
                        chars.append(cnext)
                elif IsDigit(lastchar):
                    if IsDigit(c) or IsOperator(c):
                        chars.append(c)
                    elif IsComparator(c):
                        if comparador:
                            errorcode = True
                            break
                        else:
                            chars.append(c)
                            comparador = True
                    else:
                        cnext = self.__next_sub(c)
                        self.keys[cnext] = c
                        self.vals[c] = cnext
                        chars.append(cnext)
                elif IsOperator(lastchar):
                    if IsDigit(c):
                        chars.append(c)
                    elif IsOperator(c):
                        if c == "+" or c == "-":
                            chars.append(c)
                        else:
                            errorcode = True
                            break
                    elif IsComparator(c):
                        errorcode = True
                        break
                    else:
                        cnext = self.__next_sub(c)
                        self.keys[cnext] = c
                        self.vals[c] = cnext
                        chars.append(cnext)
                elif IsComparator(lastchar):
                    if IsDigit(c):
                        chars.append(c)
                    elif IsOperator(c):
                        errorcode = True
                        break
                    elif IsComparator(c):
                        if c == "=" and lastchar != "=":
                            chars.append(c)
                        else:
                            errorcode = True
                            break
                    else:
                        cnext = self.__next_sub(c)
                        self.keys[cnext] = c
                        self.vals[c] = cnext
                        chars.append(cnext)
                else:
                    if IsDigit(c):
                        errorcode = True
                        break
                    elif IsOperator(c):
                        chars.append(c)
                    elif IsComparator(c):
                        if comparador:
                            errorcode = True
                            break
                        else:
                            chars.append(c)
                            comparador = True
                    else:
                        errorcode = True
                        break
                lastchar = c
            if errorcode:
                self.errorequa.append(eaq)
                continue
            parsedeq.append("".join(chars))
        self.__eq = parsedeq[:]