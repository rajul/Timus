n = int(raw_input())

teams = {}

for i in range(n):
	line = raw_input().strip().split()

	name1 = line[0]
	name2 = line[1]
	name3 = line[2]

	try:
		teams[name1].add(name2)
		teams[name1].add(name3)
	except KeyError:
		teams[name1] = set()
		teams[name1].add(name2)
		teams[name1].add(name3)


	try:
		teams[name2].add(name1)
		teams[name2].add(name3)
	except KeyError:
		teams[name2] = set()
		teams[name2].add(name1)
		teams[name2].add(name3)


	try:
		teams[name3].add(name1)
		teams[name3].add(name2)
	except KeyError:
		teams[name3] = set()
		teams[name3].add(name1)
		teams[name3].add(name2)


# print teams

player_levels = {}

for i in teams.keys():
	player_levels[i] = None

if "Isenbaev" in teams:
	player_levels["Isenbaev"] = 0

	q = ["Isenbaev"]
	level = 0

	while len(q) != 0:
		t = q.pop(0)
		level = player_levels[t] + 1

		for i in teams[t]:
			if player_levels[i] == None or player_levels[i] > level:
				player_levels[i] = level
				q.append(i)

# print player_levels

for k, v in sorted(player_levels.items()):
	if v == None:
		print k, "undefined"
	else:
		print k, v
