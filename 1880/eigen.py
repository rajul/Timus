def intersection(a, b):
	i = 0 
	j = 0

	res = []

	while i < len(a) and j < len(b):
		if a[i] == b[j]:
			res.append(a[i])
			i = i + 1
			j = j + 1
		elif a[i] < b[j]:
			i = i + 1
		else:
			j = j + 1

	return res

if __name__ == '__main__':
	n1 = int(raw_input())
	line = raw_input().strip().split()

	x1 = [int(x) for x in line]

	n2 = int(raw_input())
	line = raw_input().strip().split()

	x2 = [int(x) for x in line]

	n3 = int(raw_input())
	line = raw_input().strip().split()

	x3 = [int(x) for x in line]

	print len(intersection(intersection(x1, x2), x3))