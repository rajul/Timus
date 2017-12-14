# def check_named_schol(marks):
# 	flag = True

# 	for i in marks:
# 		if i < 5:
# 			flag = False
# 			break

# 	return flag

# def check_high_schol(marks):
# 	avg = (1.0 * sum(marks)) / len(marks)

# 	return avg >= 4.5

def check_no_schol(marks):
	flag = False

	for i in marks:
		if i == 3:
			flag = True
			break

	return flag

n = int(raw_input())

exams = []

for i in range(n):
	exams.append(int(raw_input().strip()))

total = sum(exams)

avg = (1.0 * total) / n

# if check_named_schol(exams):
# 	print "Named"
# elif check_high_schol(exams):
# 	print "High"
# elif check_no_schol(exams):
# 	print "None"
# else:
# 	print "Common"

if check_no_schol(exams):
	print "None"
elif avg == 5.0:
	print "Named"
elif avg >= 4.5:
	print "High"
else:
	print "Common"