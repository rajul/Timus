def get_chars(word):
	chars = [x for x in word]
	return chars


def convert_chars_to_nums(chars):
	return [(ord(char) - ord('a')) for char in chars]

def decouple_last_op(chars):
	nums = [chars[0],]

	multiplier = 0
	for i in range(1, len(chars)):
		if chars[i] < chars[i - 1]:
			multiplier = multiplier + 1
		
		nums.append(multiplier * 26 + chars[i])

	return nums

def decouple_other_op(nums):
	x = nums[0] - 5

	if x < 0:
		x = x + 26
	
	t = [x,]

	for i in range(1, len(nums)):
		t.append(nums[i] - nums[i - 1])

	return t

def final_message_convert(nums):
	return ''.join([chr(x + ord('a')) for x in nums])

if __name__ == '__main__':
	word = input().strip()

	chars = get_chars(word)
	char_nums = convert_chars_to_nums(chars)

	# print(char_nums)

	decouple1 = decouple_last_op(char_nums)
	# print(decouple1)

	decouple2 = decouple_other_op(decouple1)
	# print(decouple2)

	message = final_message_convert(decouple2)

	print(message)


