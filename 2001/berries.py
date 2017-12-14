line1 = raw_input()
line2 = raw_input()
line3 = raw_input()

line1_parts = line1.split()
line2_parts = line2.split()
line3_parts = line3.split()

a1 = int(line1_parts[0])
b1 = int(line1_parts[1])

a2 = int(line2_parts[0])
b2 = int(line2_parts[1])

a3 = int(line3_parts[0])
b4 = int(line3_parts[1])

print (a1 - a3), (b1 - b2)