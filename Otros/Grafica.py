'''
from __future__ import division

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

L1 = line([0,1], [2,3])
L2 = line([2,3], [0,4])

print(L1)
R = intersection(L1, L2)
if R:
    print ("Intersection detected:", R)
else:
    print ("No single intersection point detected")


'''
from cvxopt.modeling import variable, op
import matplotlib.pyplot as plt
import numpy as np

x = variable()
y = variable()
c1 = (2 * x + 3 * y <= 1500)
c2 = (2 * x + y <= 1000)
c3 = (x >= 0)
c4 = (y >= 0)
lp1 = op(-50 * x - 40 * y, [c1, c2, c3, c4])
lp1.solve()

print('\nEstado: {}'.format(lp1.status))
print('Valor óptimo: {}'.format(-round(lp1.objective.value()[0])))
print('Valor óptimo: {}'.format(-round(lp1.objective.value()[0])))
print('Óptimo x: {}'.format(round(x.value[0])))
print('hola')
print('Óptimo x: {}'.format(round(x.value[0])))
print('Óptimo y: {}'.format(round(y.value[0])))

p1, p2, p3, p4 = [(0, 0), (0, 500), (375, 250), (500, 0)]
pol = plt.Polygon([p1, p2, p3, p4], closed=True, alpha=0.5)
ax = plt.gca()
ax.cla()

# especifica los limites del grafico
ax.set_xlim((-100, 300))
ax.set_ylim((-100, 300))
ax.set_aspect('equal')
fig = plt.gcf()
fig.gca().add_artist(pol)
t = np.linspace(0, 1000, 100)
#x = np.linspace(0, 1000, 100)

#dibuja las lineas
ax.plot(t, (1500 - 2 * t) / 3., color='red', lw=2.0)
ax.plot(t, 1000 - 2 * t, lw=2.0)
ax.plot(t, eval("3*t"), lw=2.0)
ax.plot(500, 500, "o", lw=2.0)
ax.plot(500, 600, "o", lw=2.0)

#muestra el punto solucion
ax.plot(round(x.value[0]), round(y.value[0]), 'ko', lw=2.0)

#titulo
ax.set_title('Problema Grandes Almacenes')

#Legenda
plt.legend([r'2x+3y=1500', r'$2x+y=1000$', r'$P=(375,\; 250)\; f(P)=28750$'])
ax.grid('on')
plt.show()
