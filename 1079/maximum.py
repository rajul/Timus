terms = []

terms.append(0)
terms.append(1)

for i in range(2, 100001):
	if i % 2 == 0:
		terms.append(terms[i / 2])
	else:
		terms.append(terms[i / 2] + terms[(i/2) + 1])

while True:
	n = int(raw_input())

	if n == 0:
		break

	print max(terms[:n+1])

