n = int(raw_input())

ref = {}

for i in range(n):
	word = raw_input().strip()

	try:
		ref[word[0]].append(word)
	except KeyError:
		ref[word[0]] = [word,]

k = raw_input().strip()

try:
	for i in ref[k]:
		print i
except KeyError:
	pass