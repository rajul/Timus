n = int(raw_input())

labels = []

# Initialize
for i in range(n):
	labels.append([])
	for j in range(n):
		labels[i].append(0)

count = 0
for i in range(n-1, -1, -1):
	for p in range(i, n):
		q = p - i

		if p < n and q < n:
			count = count + 1
			labels[q][p] = count

for i in range(1, n):
	for p in range(i, n):
		q = p - i

		if p < n and q < n:
			count = count + 1
			labels[p][q] = count


for line in labels:
	for label in line:
		print label,
	print