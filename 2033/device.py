device_map = {}

for i in range(6):
	friend_name = raw_input()
	device_name = raw_input().strip()
	device_price = int(raw_input().strip())

	if device_name in device_map:
		device_map[device_name][0] = device_map[device_name][0] + 1
		device_map[device_name][1].append(device_price)
		if device_price < device_map[device_name][2]:
			device_map[device_name][2] = device_price
	else:
		device_map[device_name] = []
		device_map[device_name].append(1)
		device_map[device_name].append([device_price])
		device_map[device_name].append(device_price)

t = sorted(device_map.items(), key = lambda x: (x[1][0], -x[1][2]))

print t[-1][0]