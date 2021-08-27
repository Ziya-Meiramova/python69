from sqlite3 import *

class Student_Table:
    def __init__(self, connection):
        self.connection = connection

    def get_all_students(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from students")
        data = cursor.fetchall()
        print(data)
    def insert_student(self, ID, name, age, gpa, year_of_study):
        cursor = self.connection.cursor()
        cursor.execute(f" INSERT INTO students VALUES({ID}, '{name}', {age}, {gpa}, {year_of_study} ) ")
        self.connection.commit()
        print("values inserted")

    # delete  with ID

    
