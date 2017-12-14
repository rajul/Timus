n = int(raw_input())

houses = ["Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"]
students = {
	"Slytherin": [],
	"Hufflepuff": [],
	"Gryffindor": [],
	"Ravenclaw": []
}

for i in range(n):
	name = raw_input().strip()
	house = raw_input().strip()

	students[house].append(name)

for house in houses:
	print house + ":"
	for student in students[house]:
		print student

	if house != "Ravenclaw":
		print
