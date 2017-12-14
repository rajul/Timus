n = int(raw_input())

spam = {}

for i in range(n):
	x = raw_input().strip()
	try:
		spam[x] = spam[x] + 1
	except KeyError:
		spam[x] = 1

for k, v in spam.items():
	if v > 1:
		print k

