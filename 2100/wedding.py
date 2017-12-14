n = int(raw_input())

t = n + 2

for i in range(n):
	x = raw_input().strip()

	if x.endswith('+one'):
		t = t + 1

if t == 13:
	t = t + 1

print t * 100
