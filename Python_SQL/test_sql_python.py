# Урок 2
def add_movies(conn):
    # Исправлено: второй фильм - The Green Mile
    ins_movi = "INSERT INTO movies (title, duration, release_year) VALUES ('Godfather', 175, 1972)"
    ins_movi2 = "INSERT INTO movies (title, duration, release_year) VALUES ('The Green Mile', 189, 1999)"

    cursor = conn.cursor()
    cursor.execute(ins_movi)
    cursor.execute(ins_movi2)
    conn.commit()
    cursor.close()


def get_all_movies(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, release_year, duration FROM movies ORDER BY id;")
    movies = cursor.fetchall()
    cursor.close()
    return movies

# урок 3

import psycopg2

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def get_all_cars(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars ORDER BY brand;")
    all_cars = cursor.fetchall()
    cursor.close()
    return all_cars
# END
