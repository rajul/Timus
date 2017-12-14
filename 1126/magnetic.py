
def get_max_and_max_pos(A, start):
	init_max = max(ns[start:start + m])
	init_max_pos = start

	for i in range(start, start + m):
		if ns[i] == init_max:
			init_max_pos = i
			break

	print("test", init_max, init_max_pos)

	return (init_max, init_max_pos)


m = int(input())

ns = []
count = 0

while True:
	t = int(input())

	if t == -1:
		break

	ns.append(t)
	count = count + 1

print(m)
print(ns)

(init_max, init_max_pos) = get_max_and_max_pos(ns, 0)
print(init_max)

max_seen = init_max
max_seen_pos = init_max_pos

for i in range(m, count):
	if max_seen_pos < (i - m + 1):
		(max_seen, max_seen_pos) = get_max_and_max_pos(ns, i)

	print("abc:", max_seen, max_seen_pos)

	if ns[i] > max_seen:
		max_seen = ns[i]
		max_seen_pos = i

	print(max_seen)

