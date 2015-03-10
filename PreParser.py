__author__ = "José Pablo Parajeles"
import Tools

class Preparser:
    MIN = 0
    MAX = 1



    def __init__(self, p_s_func_obj="", p_l_s_restricciones=[], p_c_tipo=MAX):
        self._inequations = []
        self.funcion_objetivo = p_s_func_obj
        self._restricciones = p_l_s_restricciones[:]
        self.tipo = p_c_tipo
        self.Reformat()

    def Reformat(self):
        restric = []
        defaults = []
        for op in self.restricciones:
            current = []
            origin = []
            last = ""
            replace = False
            for actual in op:
                if(Tools.IsComparator(actual)):
                    if(not replace):
                        replace = True
                        current.append("-(")
                    origin.append(actual)
                    continue
                elif( not Tools.IsDigit(actual) and not Tools.IsOperator(actual) and Tools.IsDigit(last) ):
                    current.append("*")
                last = actual
                origin.append(actual)
                current.append(actual)
            if replace:
                current.append(")")
            restric.append("".join(current))
            defaults.append("".join(origin))
        self._restricciones = restric
        self._inequations = defaults

        def GetRestrictions():
            return self._restricciones[:]

