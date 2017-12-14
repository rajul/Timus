import sys

def is_sentence_end(ch):
	return (ch == '.' or ch == '!' or ch == '?')

def process_message(message, flag):
	new_message = []

	for ch in message:
		if flag == True:
			if ch.isalpha():
				new_message.append(ch.upper())
				flag = False
			else:
				new_message.append(ch.lower())
		else:
			new_message.append(ch.lower())

		if is_sentence_end(ch):
			flag = True

	return ''.join(new_message), flag

if __name__ == '__main__':
	flag = True

	while True:
		message = sys.stdin.readline().strip()
		if message == '':
			break

		processed_message, flag = process_message(message, flag)
		print(processed_message)
