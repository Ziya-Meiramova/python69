class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    def walk(self):
        return "I'm walking"
    def eat(self):
        return "I'am eating"
    def think(self):
        return "I think"

class Teacher(Person):
    def __init__(self, name, age, weight, height, exp):
        super().__init__(name, age, weight, height)
        self.exp = exp
    def teach(self):
        return "I'm teaching"
person1 = Person("Olga", 35, 56, 170)
teacher1 = Teacher("Igor", 45, 70, 160, 20)
print(person1.think(), person1.name, person1.eat())
print(teacher1.teach(), teacher1.name, teacher1.exp)