import sqlite3

def create_employees_table():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
                        name TEXT, 
                        title TEXT, 
                        salary REAL
                    )""")
    conn.commit()
    conn.close()

def insert_employees_data():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    employees = [('Arkadiy', 'manager', 35000), 
                 ('George', 'director', 60000), 
                 ('Pavel', 'cleaning', 10000), 
                 ('Michael', 'manager', 30000)]
    cursor.executemany("INSERT INTO employees VALUES(?, ?, ?);", employees)
    conn.commit()
    conn.close()

def select_managers():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE title='manager';")
    all_employees = cursor.fetchall()
    for employee in all_employees:
        print(f'Имя: {employee[0]}, Должность: {employee[1]}, Зарплата: {employee[2]}')
    conn.close()

create_employees_table()
insert_employees_data()
select_managers()
