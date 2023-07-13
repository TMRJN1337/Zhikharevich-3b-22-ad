import sqlite3

# Создаем базу данных
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Создаем таблицу фильмов
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
                  (title TEXT, genre TEXT, rating REAL)''')

# Добавляем фильмы в таблицу
movies = [('The Shawshank Redemption', 'Drama', 9.3),
          ('The Godfather', 'Crime', 9.2),
          ('The Dark Knight', 'Action', 9.0),
          ('12 Angry Men', 'Drama', 8.9),
          ('Schindler\'s List', 'Biography', 8.9),
          ('The Lord of the Rings: The Return of the King', 'Adventure', 8.9),
          ('Pulp Fiction', 'Crime', 8.9),
          ('The Good, the Bad and the Ugly', 'Western', 8.8),
          ('Fight Club', 'Drama', 8.8),
          ('Forrest Gump', 'Drama', 8.8)]
cursor.executemany("INSERT INTO movies VALUES (?, ?, ?)", movies)

# Выводим все фильмы выбранного жанра
genre = 'Drama'
cursor.execute("SELECT * FROM movies WHERE genre=?", (genre,))
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()