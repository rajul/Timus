def main():
	n = int(raw_input())

	team_wise_problem_solved = []

	for i in range(n):
		temp = raw_input()
		temp = temp.strip().split()

		team_wise_problem_solved.append((int(temp[0]), int(temp[1])))

	team_standings = sorted(team_wise_problem_solved, key = lambda x: x[1], reverse=True)

	for i in team_standings:
		print i[0], i[1]


if __name__ == '__main__':
	main()