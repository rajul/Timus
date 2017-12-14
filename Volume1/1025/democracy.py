n = int(raw_input())

k = raw_input()
k = k.split()
k = [int(i) for i in k]

k = sorted(k)

t = k[:(n/2 + 1)]

x = 0

for i in t:
	x = x + (i/2) + 1

print x