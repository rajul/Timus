# Run with Python 3

x = input().strip()

count = []

l = len(x)

max_pos = 0
max_seen = 0

for i in range(l):
	count.append(0)


for i in range(l):
	for j in range(l):
		if x[i] == x[j]:
			count[i] = count[i] + 1
			
			if count[i] > max_seen:
				max_pos = i
				max_seen = count[i]


print(x[max_pos])
