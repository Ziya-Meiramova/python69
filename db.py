from sqlite3 import *
def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Success")
    except Error as e:
        print(e)
    return connection

# connection = create_connection("test_database")

CREATE_TABLE = """
    CREATE TABLE students(
        ID INT Primary Key,
        name VARCHAR(40),
        age INT,
        gpa INT,
        year_of_study INT
    )
"""
INSERT_VALUES = """
    INSERT INTO students VALUES(3, "Anel", 23, 2.0, 1);
"""

SELECT_ALL = "SELECT * from students"
# cursor = connection.cursor()
# cursor.execute(SELECT_ALL)
# connection.commit() #with insert

# print(cursor.fetchall())


