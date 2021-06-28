class Employee:
    cnt = 0
    def __init__(self, surname, name, salary, age):
        self.surname = surname
        self.name = name
        self.salary = salary
        self.age = age
        Employee.cnt+=1
    def print_empl(self):
        print("Имя : {}. Зарплата : {}. Возраст : {}".format(self.name, self.salary, self.age))
    def count(self):
        print("Всего сотрудников : %d" % Employee.cnt)
a = Employee("Kim", "Nikita", 200000, 25)
b = Employee("Meiramova", "Ziya", 250000, 24)

a.print_empl()
b.print_empl()
a.count()