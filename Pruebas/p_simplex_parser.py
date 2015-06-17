__author__ = 'José Pablo'
from Enums import SimplexFamily
from Simplex.Parser import SimplexParser
"""
strl = [
    "2 1 < 18",
    "2 3 < 42",
    "3 1 < 24",
    "Max 3 2"
]
SimplexParser(strl,SimplexFamily.Simplex)
"""
"""
strl = [
    "2 0 < 8",
    "0 4 < 24",
    "6 10 > 60",
    "Max 6 10"
]
a = SimplexParser(strl,SimplexFamily.GranM)
"""
"""
strl = [
    "6 12 0 > 40",
    "4 2 4 = 30",
    "min 12 8 8"
]
SimplexParser(strl,SimplexFamily.DosFases)
"""
#"""
strl = [
    "1 0 < 8",
    "0 1 < 12",
    "6 4 < 36",
    "2 8 < 20",
    "Max 6 10"
]
SimplexParser(strl,SimplexFamily.Dual)