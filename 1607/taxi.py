line = raw_input().strip().split()

a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

offer_diff = c - a

if offer_diff < 0:
	print a
else:	
	rate = b + d

	t = offer_diff / rate

	pass_last = a + (t + 1) * b
	taxi_last = c - t * d

	print min(pass_last, taxi_last)
