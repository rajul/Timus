line = raw_input().strip().split()

a = int(line[0])
b = int(line[1])

res = max(2 * b + 40, 2 * a + 39)

print res