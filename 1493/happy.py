def check_lucky(n):
	break_point = 3
	if len(n) <= 3:
		return False
	elif len(n) == 4:
		break_point = 1
	elif len(n) == 5:
		break_point = 2

	part_1 = n[:break_point]
	part_2 = n[break_point:]

	sum1 = sum([int(x) for x in part_1])
	sum2 = sum([int(x) for x in part_2])

	if sum1 == sum2:
		return True
	else:
		return False

n = int(raw_input().strip())

succ = str(n + 1)
pred = str(n - 1)

if check_lucky(succ) or check_lucky(pred):
	print "Yes"
else:
	print "No"
