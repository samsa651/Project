from sympy import *
import numpy as np
import math

td = 0
maxi = 0
maxa = 0
maxb = 0
maxtf = 0
maxh = 0
maxang = 0
H = 50
x = 50
c = 50
g=9.81

for i in range(0,1000):
    for j in range(-5000,0):
        a = i/1000
        b=j/1000
        h = a*(x**2)+b*x+c
        dev = 2*a*x + b
        ang = np.arctan(dev)
        ang_gr = ang * 180 / math.pi
        if h > 0 and ang > 0:
            if 2*g*(H-h) >= 0:
                V = math.sqrt(2*g*(H-h))
                tu = (V*np.sin(ang)/g)
                hu=V*np.sin(ang)*tu-(g*(tu**2)/2)
                if 2*(hu+h)/g >= 0:
                    td = math.sqrt(2*(hu+h)/g)
                    tf=tu+td
                    dist = tf * V*np.cos(ang)
                    if -((b**2 - 4*a*c)/4*a) > 0:
                        if dist > maxi:
                            maxi = dist
                            maxa = a
                            maxb = b
                            maxtf = tf
                            maxh = h
                            maxang = ang

print(maxi,maxa,maxb,maxtf, maxh , maxang , -((b**2 - 4*a*c)/4*a))