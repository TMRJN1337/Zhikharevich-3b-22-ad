import sqlite3

# Создаем базу данных
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Создаем таблицу студентов
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (name TEXT, age INTEGER, average_score REAL)''')

# Добавляем данные о студентах в таблицу
students = [('Иванов Иван', 20, 4.5),
            ('Петрова Анна', 19, 4.2),
            ('Сидоров Павел', 21, 4.8),
            ('Козлова Екатерина', 20, 4.6),
            ('Смирнов Дмитрий', 19, 4.3)]
cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", students)

# Выводим все данные о студентах
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
