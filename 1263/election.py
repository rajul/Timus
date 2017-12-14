line = raw_input().strip().split()

n = int(line[0])
m = int(line[1])

votes = {}

for i in range(1, n+1):
	votes[i] = 0

for i in range(m):
	x = int(raw_input())
	votes[x] = votes[x] + 1

for i in range(1, n+1):
	perc = (votes[i] * 100.0) / m

	print "%.2f%%"%(perc)
