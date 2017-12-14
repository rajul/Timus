n = int(input().strip())

counter = {}
max_count = 0
max_num = 0

for i in range(n):
	t = int(input().strip())

	try:
		counter[t] = counter[t] + 1
	except KeyError:
		counter[t] = 1

	if max_count < counter[t]:
		max_count = counter[t]
		max_num = t

print(max_num)