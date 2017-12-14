def get_seat_type(seat_number):
	row_number = int(seat_number[:-1])
	seat_char = seat_number[-1]

	if row_number >=1 and row_number <=2:
		if seat_char == 'B' or seat_char == 'C':
			return "aisle"
		else:
			return "window"
	elif row_number >=3 and row_number <= 20:
		if seat_char == 'B' or seat_char == 'C':
			return "aisle"
		elif seat_char == 'D' or seat_char == 'E':
			return "aisle"
		else:
			return "window"
	else:
		if seat_char == 'C' or seat_char == 'D':
			return "aisle"
		elif seat_char == 'G' or seat_char == 'H':
			return "aisle"
		elif seat_char == 'A' or seat_char == 'K':
			return "window"
		else:
			return "neither"

if __name__ == '__main__':
	seat = raw_input().strip()

	print get_seat_type(seat)