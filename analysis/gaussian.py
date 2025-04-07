from math import *

f = lambda x: exp(-(x*x)/2)
# f = lambda x: abs(sin(2*pi*x)/(6*x))
# f0 = pi/3

roots = [0.9061798459, 0.5384693101, 0, -0.5384693101, -0.9061798459]
weights = [0.2369268850, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268850]

total = 0
for i in range(len(roots)):
    total += (weights[i] *  f(roots[i]))

print(f'Estimate = {total:.10f}')
