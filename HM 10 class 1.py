import math
class regtangle:
    def __init__(self, sideA, sideB, color):
        self.sideA = sideA
        self.sideB = sideB
        self.color = color
    def area(self):
        return self.sideA * self.sideB
    def perimetr(self):
        return (self.sideA + self.sideB) * 2
a1 = int(input())
a = regtangle(a1, 4, "red")
b = regtangle(5, 8, "green")
print(a.area(), a.perimetr(), a.color)
print(b.area(), b.perimetr(), b.color)

class circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def area_circle(self):
        return self.radius**2 * math.pi
    def length(self):
        return 2 * math.pi * self.radius
c = circle(5, "yellow")
print(c.length(), c.area_circle())

class square:
    def __init__(self, side, color):
        self.side = side
        self.color = color
    def area_square(self):
        return self.side**2
    def perimetr_square(self):
        return 4 * self.side
d = square(3, "blue")
print(d.area_square(), d.perimetr_square(), d.color)