from sqlite3 import *
from  db_class import *
from db import create_connection

connection = create_connection("test_database")

students = Student_Table(connection)
students.insert_student(5, "fghjkl", 31, 2.0, 7 )

students.get_all_students()

