line = raw_input().strip().split()

n = int(line[0])
m = int(line[1])

for i in range(1, n+1):
	print i,

print

for i in range(1, m+1):
	print i*n + 1,

print