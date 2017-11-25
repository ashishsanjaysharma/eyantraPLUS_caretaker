import numpy
import math
from math import pi
from trianglesolver import solve

def distance(x1,y1,x2,y2):
    dist = math.hypot(x2-x1, y2-y1)
    return dist

def angle(a,b,c):
    degree = pi/180
    a,b,c,A,B,C = solve(a, b, c)
    Angle_A=A/degree
    y=int(math.floor(Angle_A))
    return y
    
x=distance(2,3,4,6)
z=angle(1,2,2)
print x,z
