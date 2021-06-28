class Students:

    def __init__(self, surname, name, gpa, age): #конструктор
        self.surname = surname #инициализация
        self.name = name #student1 == self
        self.gpa = gpa
        self.age = age

    def say_hello(self):
        return "Hello, ", self.name
    def next_year(self):
        return "In a year you'll be", self.age + 1
    def check(self):
        # self.name = name
        if self.surname == " ":
            print(self.name)


student1 = Students(" ", "Ziya", 3.6, 18)
student2 = Students("Syzdykov", "Murat", 2.9, 22)
#print(student1.name, student2.age)

student1.name = "Derbes" #изменения
student1.age = 25

student1.check()
print(student1.age)

# del student1.name # удаление
# print(student1.name)

# print(student1.say_hello())
# print(student1.gpa)
# print(student2.next_year())

# def max(a, b):
#     if a > b:
#         return student1.name
#     return student2.name
#
# print(max(student1.age, student2.age))