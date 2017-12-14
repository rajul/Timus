line = raw_input().strip().split()

m = int(line[0])
n = int(line[1])

if ((m*n) %2) == 0:
	print "[:=[first]"
else:
	print "[second]=:]"