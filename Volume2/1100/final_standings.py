# Time limit exceeded by about 50 ms
# need to figure out why

def merge(left_half, right_half):
	merged_list = []
	
	len_left = len(left_half)
	len_right = len(right_half)

	i = 0
	j = 0

	while i < len_left and j < len_right:
		if left_half[i][1] >= right_half[j][1]:
			merged_list.append(left_half[i])
			i = i + 1
		else:
			merged_list.append(right_half[j])
			j = j + 1

	if i < len_left:
		merged_list.extend(left_half[i:])
	elif j < len_right:
		merged_list.extend(right_half[j:])

	return merged_list


def merge_sort_by_problem_solved(team_wise_problem_solved):
	l = len(team_wise_problem_solved)

	if l <= 1:
		return team_wise_problem_solved

	left_half = merge_sort_by_problem_solved(team_wise_problem_solved[:l/2])
	right_half = merge_sort_by_problem_solved(team_wise_problem_solved[l/2:])

	return merge(left_half, right_half)

def main():
	n = int(raw_input())

	team_wise_problem_solved = []

	for i in range(n):
		temp = raw_input()
		temp = temp.strip().split()

		team_wise_problem_solved.append((int(temp[0]), int(temp[1])))

	team_standings = merge_sort_by_problem_solved(team_wise_problem_solved)

	for i in team_standings:
		print i[0], i[1]


if __name__ == '__main__':
	main()