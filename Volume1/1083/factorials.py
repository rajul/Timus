a = raw_input()
a = a.strip().split()

n = int(a[0])
k = len(a[1])

if n % k == 0:
	l = k
else:
	l = n % k

t = n
f = 1

while t >= l:
	f = f * t
	t = t - k

print f
