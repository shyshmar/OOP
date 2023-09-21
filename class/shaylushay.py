import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

    def setcoords(self, sp, ep):
        self.sp = sp
        self.ep = ep

    def null(self):
        self.sp = (0, 0)
        self.ep = (0, 0)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


f = lambda: random.randint(0, 10)
fig = [Line, Rect, Ellipse]

elements = [random.choice(fig)(f(), f(), f(), f()) for i in range(217)]

print(elements)