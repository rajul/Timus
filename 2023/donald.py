def get_number_of_steps(cases, n):
	steps = 0

	for i in range(n):
		steps = steps + abs(cases[i] - cases[i+1])

	return steps


locations = {
	'Alice': 0,
	'Phil': 0,
	'Phoebus': 0,
	'Ariel': 0,
	'Peter': 0,
	'Ralph': 0,
	'Aurora': 0,
	'Olaf': 0,
	'Robin': 0,
	'Bambi': 1,
	'Mulan': 1,
	'Silver': 1,
	'Belle': 1,
	'Mowgli': 1,
	'Simba': 1,
	'Bolt': 1,
	'Mickey': 1,
	'Stitch': 1,
	'Dumbo': 2,
	'Kuzko': 2,
	'Tarzan': 2,
	'Genie': 2,
	'Kida': 2,
	'Tiana': 2,
	'Jiminy': 2,
	'Kenai': 2,
	'Winnie': 2
}

n = int(raw_input())

cases = [0,]

for i in range(n):
	name = raw_input()
	loc = locations[name]

	cases.append(loc)

steps = get_number_of_steps(cases, n)

print steps