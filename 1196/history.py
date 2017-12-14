def binary_search(A, n, k):
	l = 0
	h = n - 1

	while l <= h:
		mid = (l + h) / 2

		if k == A[mid]:
			return mid
		elif k < A[mid]:
			h = mid - 1
		else:
			l = mid + 1

	return -1


n = int(raw_input())

x = []

for i in range(n):
	t = int(raw_input())	
	x.append(t)

# prof_nums = set(x)

m = int(raw_input())
count = 0

for i in range(m):
	t = int(raw_input())

	# if t in prof_nums:
	y = binary_search(x, n, t)
	# print t, y
	if  y != -1:
		count = count + 1

print count

