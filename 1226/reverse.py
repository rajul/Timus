import sys

def process_line(line):
	temp = ''
	for i in line:
		if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
			temp = i + temp
		else:
			if temp != '':
				print(temp, end='')
				temp = ''

			print(i, end='')

if __name__ == '__main__':
	while True:
		line = sys.stdin.read()

		if line == '':
			break

		x = process_line(line)
