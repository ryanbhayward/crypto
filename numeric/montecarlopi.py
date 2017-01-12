from random import random
from math import pow, sqrt
darts=1000000
hits = 0
throws = 0
for _ in range (darts):
	throws += 1
	x = random()
	y = random()
	if sqrt(pow(x, 2) + pow(y, 2)) <= 1.0:
		hits = hits + 1.0
print "pi = %s" %(4*(hits/throws))
