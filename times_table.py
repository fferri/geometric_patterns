import sys
from math import *
n = int(sys.argv[1])
t = int(sys.argv[2])
r = 1000
P = [(r*(1+cos(a)), r*(1+sin(a))) for a in [i*pi*2/n for i in range(n)]]
L = set()
for i in range(n):
    M = set()
    while True:
        j = i * t % n
        if (i, j) in M: break
        M.add((i, j))
        i = j
    for m in M: L.add(m)
print('<svg height="{}" width="{}">'.format(2*r,2*r))
for (i, j) in L: print('<line x1="{}" y1="{}" x2="{}" y2="{}" style="stroke:rgb(55,55,200);stroke-width:1;stroke-opacity:0.3;" />'.format(*P[i]+P[j]))
print('</svg>')
