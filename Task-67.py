import sqlite3

# Создаем базу данных
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Создаем таблицу книг
cursor.execute('''CREATE TABLE IF NOT EXISTS books
                  (title TEXT, author TEXT, year INTEGER)''')

# Добавляем книги в таблицу
books = [('Метро 2033', 'Дмитрий Глуховский', 2005),
         ('Три товарища', 'Эрих Мария Ремарк', 1936),
         ('12 стульев', 'Илья Ильф и Евгений Петров', 1928),
         ('Мастер и Маргарита', 'Михаил Булгаков', 1967),
         ('А зори здесь тихие...', 'Борис Васильев', 1969),
         ('Алхимик', 'Пауло Коэльо', 1988),
         ('Остров Сахалин', 'Антон Чехов', 1893),
         ('Война и мир', 'Лев Толстой', 1869),
         ('Преступление и наказание', 'Федор Достоевский', 1866),
         ('Отцы и дети', 'Иван Тургенев', 1862)]
cursor.executemany("INSERT INTO books VALUES (?, ?, ?)", books)

# Выводим все книги, выпущенные после 2000 года
cursor.execute("SELECT * FROM books WHERE year > 2000")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закрываем соединение с базой данных
conn.close()
