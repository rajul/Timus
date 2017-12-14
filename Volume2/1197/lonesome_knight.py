class Square:
	def __init__(self, square_index):
		if len(square_index) > 2:
			raise ValueException()

		self.row = ord(square_index[0]) - 97;
		self.col = int(square_index[1]) - 1;

	def get_number_knight_moves(self):
		count = 0
		moves = []

		moves.append((self.row + 2, self.col + 1))
		moves.append((self.row + 2, self.col - 1))
		moves.append((self.row - 2, self.col + 1))
		moves.append((self.row - 2, self.col - 1))
		moves.append((self.row + 1, self.col + 2))
		moves.append((self.row + 1, self.col - 2))
		moves.append((self.row - 1, self.col + 2))
		moves.append((self.row - 1, self.col - 2))

		for i in moves:
			if i[0] >= 0 and i[0] < 8 and i[1] >=0 and i[1] < 8:
				count = count + 1

		return count


def main():
	n = int(raw_input())

	for i in range(n):
		temp = raw_input()
		square = Square(temp)
		print square.get_number_knight_moves()

if __name__ == '__main__':
	main()