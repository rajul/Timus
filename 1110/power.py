def power_mod(x, n, m):
	power = 1
	for i in range(n):
		power = power * x
		power = power % m

	return power


line = raw_input().strip().split()

n = int(line[0])
m = int(line[1])
y = int(line[2])

flag = False

for j in range(m):
	t = power_mod(j, n, m)
	if t == y:
		flag = True
		print j,

if flag == False:
	print -1,
	
print
