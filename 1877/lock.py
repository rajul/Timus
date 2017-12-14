def is_odd(n):
	return (n % 2) != 0

def is_even(n):
	return (n % 2) == 0
	

code1 = int(raw_input())
code2 = int(raw_input())

if is_even(code1) or is_odd(code2):
	print "yes"
else:
	print "no"