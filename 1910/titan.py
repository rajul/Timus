n = int(raw_input())

line = raw_input()
parts = line.strip().split()

fields = [int(x) for x in parts]

max_field = -1
max_index = 0

for i in range(1, n - 1):
	t = fields[i-1] + fields[i] + fields[i+1]
	if t > max_field:
		max_field = t
		max_index = (i + 1)

print max_field, max_index

