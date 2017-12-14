n = int(input().strip())

a = [int(i) for i in input().strip().split()]

total_litres = sum(a)

litre_per_person = total_litres / (n + 1)

difference = [(x - litre_per_person) for x in a]

difference_normal = []

for x in difference:
	if x > 0:
		difference_normal.append(x * 1000)
	else:
		difference_normal.append(0)

total_difference = sum(difference_normal)

if total_difference == 0:
	for i in range(n):
		difference_normal[i] = 1

compensation = []

for i in difference_normal:
	compensation.append((i / total_difference) * 100.0)

print(' '.join([str(int(x)) for x in compensation]))

