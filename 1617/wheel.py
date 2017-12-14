n = int(input().strip())

wheels = {}

for i in range(n):
	t = int(input().strip())

	try:
		wheels[t] = wheels[t] + 1
	except KeyError:
		wheels[t] = 1

total = 0

for k, v in wheels.items():
	total = total + (v // 4)

print(total)