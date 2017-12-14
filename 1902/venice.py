line = raw_input().strip().split()

n = int(line[0])
t = int(line[1])
s = int(line[2])

line = raw_input().strip().split()

xs = [int(i) for i in line]

for x in xs:
	if x < s:
		y = s + ((x + t) - s) / 2.0
	else:
		y = (s + t) - ((s + t) - x) / 2.0

	print '%.6f'%(y)