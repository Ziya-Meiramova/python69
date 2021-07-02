# class Animals:
#     def __init__(self, weight, length, age):
#         self.weight = weight
#         self.length = length
#         self.age = age
#     def hear(self):
#         return "I hear"
#     def eat(self):
#         return "I'm eating"
#     def see(self):
#         return "I see"
#
# class Fish(Animals):
#     def __init__(self, weight, length, age, scale):
#         super().__init__(weight, length, age)
#         self.scale = scale
#     def swim(self):
#         return "I am swimming"
# class Earth(Animals):
#     def __init__(self, weight, length, age, color):
#         super().__init__(weight, length, age)
#         self.color = color
#     def walk(self):
#         return "I am walking"
# a = Animals(340, 200, 20)
# b = Fish(3, 1, 4, "dark")
# c = Earth(44, 2, 3, "brown")
# print(b.swim(), b.scale)
# print(c.walk(), c.color)
# print(a.eat(), a.see(), a.hear())

