def knapsack(a, target):
	if len(a) == 0:
		return 0
	if len(a) == 1:
		if a[0] <= target:
			return a[0]
		else:
			return 0

	if a[0] <= target:
		return max(a[0] + knapsack(a[1:], target - a[0]), knapsack(a[1:], target))
	else:
		return knapsack(a[1:], target)

if __name__ == '__main__':
	n = int(input().strip())
	line = input().strip().split()
	x = [int(i) for i in line]

	total = sum(x)
	target = total // 2

	t = knapsack(x, target)
	u = total - t

	print(abs(t - u))