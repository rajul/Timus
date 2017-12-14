n = int(raw_input())

stores = []

for i in range(n):
	line = raw_input().strip()
	stores.append(line)

store_set = set(stores)

print (n - len(store_set))