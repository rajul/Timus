# def find_summands(x, y, c):
# 	flag = True
# 	if x < y:
# 		lower = x
# 		higher = y
# 	else:
# 		lower = y
# 		higher = x
# 		flag = False

# 	for i in range(lower + 1):
# 		if (c - i) <= higher:
# 			if flag == True:
# 				a = i
# 				b = c - i
# 				break 
# 			else:
# 				a = c - i
# 				b = i
# 				break

# 	return a, b

if __name__ == '__main__':
	line = input().strip().split()

	x = int(line[0])
	y = int(line[1])
	c = int(line[2])


	if (x + y) < c:
		print("Impossible")
	elif (x < c):
		# a, b = find_summands(x, y, c)
		print(x, c - x)
	elif (y < c):
		# a, b = find_summands(x, y, c)
		print(c- y, y)
	else:
		print(0, c)

