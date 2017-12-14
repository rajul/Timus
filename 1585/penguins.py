n = int(raw_input())

emp_count = 0
lit_count = 0
mac_count = 0

for i in range(n):
	line = raw_input().strip()

	if line[0] == 'E':
		emp_count = emp_count + 1
	elif line[0] == 'L':
		lit_count = lit_count + 1
	elif line[0] == 'M':
		mac_count = mac_count + 1

if emp_count > lit_count and emp_count > mac_count:
	print "Emperor Penguin"
elif lit_count > mac_count:
	print "Little Penguin"
else:
	print "Macaroni Penguin"