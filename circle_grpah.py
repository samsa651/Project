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

for i in range(2600,5000):
    for j in range(2600,5000):
        R = i/100
        a = R
        b=j/100
        if R**2-(x-R)**2>=0:
            h = b-math.sqrt(R**2-(x-R)**2)
            if R**2 - x**2 + 2*a*x - a**2 > 0:
                dev = (x-a)/(math.sqrt(R**2 - x**2 + 2*a*x - a**2))
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
                            if b-a > 0:
                                if dist > maxi:
                                    maxi = dist
                                    maxa = a
                                    maxb = b
                                    maxtf = tf
                                    maxh = h
                                    maxang = ang

print(maxi,maxa,maxb,maxtf, maxh , maxang )