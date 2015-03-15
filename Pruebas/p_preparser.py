__author__ = 'José Pablo'
"""
import matplotlib.pyplot as plt
import numpy as np
from cvxopt.modeling import variable, op

x = variable()
y = variable()
c1 = (2*x+3*y <= 1500)
#c2 = (2*x+y <= 1000)
c2 = eval("(2*x+y <= 1000)")
c3 = (x >= 0)
c4 = (y >= 0)
lp1 = op(-50*x-40*y, [c1, c2, c3, c4])
lp1.solve()
print('\nEstado: {}'.format(lp1.status))
print('Valor óptimo: {}'.format(-round(lp1.objective.value()[0])))
print('Óptimo x: {}'.format(round(x.value[0])))
print('Óptimo y: {}'.format(round(y.value[0])))
print('Mult óptimo primera restricción: {}'.format(c1.multiplier.value[0]))
print('Mult óptimo segunda restricción: {}'.format(c2.multiplier.value[0]))
print('Mult óptimo tercera restricción: {}'.format(c3.multiplier.value[0]))
print('Mult óptimo cuarta restricción: {}\n'.format(c4.multiplier.value[0]))

p1, p2, p3, p4 = [(0, 0), (0, 500), (375, 250), (500, 0)]
pol = plt.Polygon([p1, p2, p3, p4], closed=True, alpha=0.5)
ax = plt.gca()
ax.cla()
ax.set_xlim((0, 1000))
ax.set_ylim((0, 1000))
ax.set_aspect('equal')
fig = plt.gcf()
fig.gca().add_artist(pol)
t = np.linspace(0, 1000, 100)
ax.plot(t, (1500-2*t) / 3., color='red', lw=2.0)
ax.plot(t, 1000-2*t, color='green', lw=2.0)
ax.plot(round(x.value[0]), round(y.value[0]), 'ko', lw=2.0)
ax.set_title('Problema Grandes Almacenes')
plt.legend([r'$2x+3y=1500$', r'$2x+y=1000$', r'$P=(375,\; 250)\; f(P)=28750$'])
ax.grid('on')
plt.show()
"""

import PreParser


b = [
    "6x+4y<=24",
    "x+2y<=6",
    "-x+y<=1",
    "x*y*x*1+2x>=3x",
    "3a<=2"
]


a = PreParser.Preparser(p_l_s_restricciones=b)
print(a.get_restrictions())
print(a.get_originals())

