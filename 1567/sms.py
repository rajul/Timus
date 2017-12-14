def  get_key_press(c):
	if c == '.' or c == ' ':
		return 1
	if c == ',':
		return 2
	if c == '!':
		return 3

	return (ord(c) - 97) % 3 + 1

if __name__ == '__main__':
	line = raw_input().strip()

	t = 0
	for i in line:
		t = t + get_key_press(i)

	print t