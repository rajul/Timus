import sys
import math

x = []

for line in sys.stdin:
	t = line.strip().split()

	x.extend(t)

x.reverse()

for i in x:
	print "%.4f" %(math.sqrt(float(i)))
