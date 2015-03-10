__author__ = 'curso'
import re

textoTxt="1" \
         "2*x+3*y <= 1500" \
         "2*x+y <= 1000" \
         "x >= 0" \
         "y >= 0"
profilesList = re.split(r'\n{2,}', textoTxt)
