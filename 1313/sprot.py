n = int(raw_input())

a = []

for i in range(n):
	line = raw_input().strip().split()
	a.append([int(x) for x in line])

for i in range(n*2 - 1):
	for p in range(i+1):
		q = i - p

		if p < n and q < n:
			print a[q][p],

print