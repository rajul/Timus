import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distance(self, other):
		d_x = self.x - other.x
		d_y = self.y - other.y

		return math.sqrt(d_x**2 + d_y**2)

	def __repr__(self):
		return '(' + str(self.x) + ', ' + str(self.y) + ')'

def circumference(r):
	return 2 * math.pi * r



if __name__ == '__main__':
	line = raw_input().strip().split()

	n = int(line[0])
	r = float(line[1])

	c = circumference(r)

	points = []
	for i in range(n):
		t = raw_input().strip().split()
		points.append(Point(float(t[0]), float(t[1])))

	# print points

	d = 0
	for i in range(n):
		a = points[i]

		if (i+1) < n:
			b = points[i+1]
		else:
			b = points[0]

		d = d + a.distance(b)

	# print d

	print '%.2f'%(d + c)