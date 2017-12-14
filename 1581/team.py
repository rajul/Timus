n = int(raw_input())

line = raw_input().strip().split()

nums = [int(x) for x in line]

count = 0
for i in range(n - 1):
	if nums[i] == nums[i + 1]:
		count = count + 1
	else:
		count = count + 1
		print count, nums[i],
		count = 0

count = count + 1
print count, nums[-1]
