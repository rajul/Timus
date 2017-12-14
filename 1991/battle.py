line = raw_input().strip().split()

n = int(line[0])
k = int(line[1])

line = raw_input().strip().split()

b = [int(x) for x in line]


boom = 0
droid = 0

for i in b:
	if i < k:
		droid = droid + (k - i)
	else:
		boom = boom + (i - k)

print boom, droid

