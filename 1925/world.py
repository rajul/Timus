line = raw_input().strip().split()

n = int(line[0])
k = int(line[1])

b = []
g = []

for i in range(n):
	line = raw_input().strip().split()

	x = int(line[0])
	y = int(line[1])

	b.append(x)
	g.append(y)

expected_sum = sum(b) + k - 2 * (n + 1)
real_sum = sum(g)

num = expected_sum - real_sum

if num < 0:
	print "Big Bang!"
else:
	print num
