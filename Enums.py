__author__ = 'José Pablo'

from enum import Enum


class Mtype(Enum):
    Min = 1
    Max = 2


class SimplexFamily(Enum):
    Simplex = 1
    GranM = 2
    DosFases = 3
    Dual = 4