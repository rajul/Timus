n = int(input().strip())

line = input().strip().split()

a = [int(x) for x in line]

total = sum(a) + max(a)

print(total)