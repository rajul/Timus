m = raw_input().strip()

stack = []

for i in m:
	if len(stack) == 0 or stack[-1] != i:
		stack.append(i)
	else:
		stack.pop(-1)

print ''.join(stack)