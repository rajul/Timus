line1 = raw_input().strip().split()
line2 = raw_input().strip().split()

team1 = int(line1[0])
team2 = int(line1[1])

penalty = sum([int(x) for x in line2]) * 20

if (team2 - penalty) < team1:
	print "Dirty debug :("
else:
	print "No chance."