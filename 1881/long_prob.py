line = raw_input().strip().split()

h = int(line[0])
w = int(line[1])
n = int(line[2])

n_pages = 1
n_line = 1
n_words = -1

for i in range(n):
	x = raw_input().strip()

	t = n_words + 1 + len(x)

	if t > w:
		n_line = n_line + 1
		n_words = len(x)
	else:
		n_words = t

	if n_line > h:
		n_pages = n_pages + 1
		n_line = 1

print n_pages
