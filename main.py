import  sqlite3
import os
from inspect import CORO_RUNNING


def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor


def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students
    (
        id    INTEGER PRIMARY KEY,
        name  VARCHAR NOT NULL,
        age   INTEGER,
        email VARCHAR UNIQUE,
        city  VARCHAR
    )
    ''')

    cursor.execute('''
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER
        )
        ''')


def insert_sample_data(cursor):
    students = [
        (1,'Alice Johnson',20,'alice@gmail.com','New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'adavid@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle'),
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)",students )


    courses = [
        (1,'Python Programming','Dr. Anderson',3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2),

    ]
    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)",courses )
    print("Sampel data inserted successfully!")


def basic_sql_operations(cursor):
    #1-)SELECT ALL
    print("----------SELECT ALL--------")
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #2-)SELECT COLUMNS
    print("----------SELECT COLUMNS--------")
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    for row in records:
        print(row)

    #3-)WHERE CLAUSE
    print("----------WHERE AGE = 20--------")
    cursor.execute("SELECT * FROM Students WHERE age = 20")
    records = cursor.fetchall()
    for row in records:
        print(row)


    # 4-)WHERE WİTH STRİNG
    print("----------WHERE city = NEW YORK--------")
    cursor.execute("SELECT * FROM Students WHERE city = 'New York'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 5-)ORDER BY
    print("----------ORDER BY AGE--------")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 6-)LIMIT
    print("----------ORDER BY AGE--------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall()
    for row in records:
        print(row)


def sql_update_delete_insert_operations(conn,cursor):
    #1-)INSERT
    cursor.execute("INSERT INTO Students VALUES (6,'Frank Miller',23,'frank@gmail.com','Miami')")
    conn.commit()

    #2-)UPDATE
    cursor.execute("UPDATE Students SET age=24 WHERE id = 2")
    conn.commit()

    # 3-)DELETE
    cursor.execute("DELETE FROM Students WHERE id = 2")
    conn.commit()



def aggregate_functions(cursor):
    #1-)COUNT
    print("----------COUNT--------")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result = cursor.fetchall()
    print(result[0][0])

    # 2-)AVERAGE
    print("----------AVERAGE--------")
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchall()
    print(result[0][0])

    # 3-)MAX-MİN
    print("----------MAX-MİN--------")
    cursor.execute("SELECT MAX(age),MIN(age) FROM Students")
    result = cursor.fetchall()
    print(result)





def main():
    conn,cursor=create_database()

    try:

       create_tables(cursor)
       insert_sample_data(cursor)
       basic_sql_operations(cursor)
       sql_update_delete_insert_operations(conn,cursor)
       aggregate_functions(cursor)
       conn.commit()
       print("Database and tables created succesfully!")

    except sqlite3.Error as e:
        print(e)

    finally:
        if conn:
            conn.close()



if __name__ == "__main__":
    main()