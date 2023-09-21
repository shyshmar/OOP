class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

point = [Point(i, i) for i in range(1, 2000, 2)]
point[1].color = 'yellow'

thispoint = point[1]
print(thispoint.color)