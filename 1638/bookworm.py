line = raw_input().strip().split()

t = int(line[0])
c = int(line[1])
s = int(line[2])
e = int(line[3])

if s < e:
	res = (e - s) * c * 2 + (e - s - 1) * t
else:
	res = (s - e) * c * 2 + (s - e + 1) * t

print res