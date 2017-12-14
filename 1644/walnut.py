n = int(raw_input())

hungry = 2
satisfied = 10

inconsistent_flag = False

for i in range(n):
	line = raw_input().strip().split()

	x = int(line[0])
	y = line[1]

	if y == "hungry":
		if x >= satisfied:
			inconsistent_flag = True
			break

		if x > hungry:
			hungry = x
	elif y == "satisfied":
		if x <= hungry:
			inconsistent_flag = True
			break
		
		if x < satisfied:
			satisfied = x

if inconsistent_flag == True:
	print "Inconsistent"
else:
	print satisfied
