from math import log, ceil

line = input().strip().split()

n = int(line[0])
k = int(line[1])

active_comp = 1
hrs = 0

while active_comp < k and active_comp < n:
	active_comp = active_comp * 2
	hrs = hrs + 1

if active_comp < n:
	hrs = hrs + ceil((n - active_comp) / float(k))

print(hrs)
