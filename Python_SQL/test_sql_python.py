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

# или можно решить так при помощи контекстнного менеджера

import psycopg2

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN
def get_all_cars(conn):
    with conn.cursor() as c:
        sql = "SELECT * FROM cars ORDER BY brand ASC;"
        c.execute(sql)
        result = c.fetchall()
    return result
# END

# урок 4
'''name = "John"
age = 19

with conn.cursor() as curs:
    # для позиционных аргументов всегда передается последовательность, даже если параметр один
    # здесь передается кортеж (name,)
    curs.execute("SELECT id, name FROM users WHERE name=%s;", (name,))
    curs.fetchall()

with conn.cursor() as curs:
    # также можно использовать именованные аргументы
    curs.execute(
        "INSERT INTO users (name, age) VALUES (%(name)s, %(age)s);",
        {"age": age, "name": name},
    )
    conn.commit()

conn.close()

Ускорение запросов

from psycopg2.extras import execute_batch, execute_values

users = (
    ("Bob", "bob@mail.com"),
    ("Alice", "alice@mail.com"),
    ("John", "john@mail.com"),
)
execute_batch(curs, "INSERT INTO users (name, email) VALUES (%s, %s)", users)

# в случае execute_values запрос будет выглядеть так
users = [
    ("Bob", "bob@mail.com"),
    ("Alice", "alice@mail.com"),
    ("John", "john@mail.com"),
]
execute_values(curs, "INSERT INTO users (name, email) VALUES %s", users)

Возврат идентификатора

user = User()
# Сохраняем пользователя в базу данных
# После этого становится доступен id
id = user.get_id()
# Его можно использовать для формирования ссылок или вставки связанных записей

# RETURNING возвращает указанное поле
 with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
            (user.name, user.email)
        )
        user.id = cur.fetchone()[0]
conn.close()'''

import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def batch_insert(conn, products):
    with conn.cursor() as curs:
        # Преобразуем словари в кортежи
        products_data = [(p['name'], p['price'], p['quantity']) for p in products]
        execute_values(curs, "INSERT INTO products (name, price, quantity) VALUES %s", products_data)
    conn.commit()


def get_all_products(conn):
    with conn.cursor() as curs:
        curs.execute("SELECT * FROM products ORDER BY price DESC;")
        return curs.fetchall()
# END

import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN
def batch_insert(conn, products):
    with conn.cursor() as cur:
        values = [(p['name'], p['price'], p['quantity']) for p in products]

        insert_query = "INSERT INTO products (name, price, quantity) VALUES %s"

        execute_values(cur, insert_query, values)
    conn.commit()


def get_all_products(conn):
    with conn.cursor() as cur:
        sql = "SELECT * FROM products ORDER BY price DESC;"
        cur.execute(sql)
        result = cur.fetchall()
    conn.commit()
    return result
# END

# урок 5

import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def get_order_sum(conn, month):
    cursor = conn.cursor()

    # Запрос с JOIN, фильтрацией по месяцу и группировкой
    cursor.execute("""
        SELECT 
            c.customer_name,
            SUM(o.total_amount) as total
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        WHERE EXTRACT(MONTH FROM o.order_date) = %s
        GROUP BY c.customer_id, c.customer_name
        ORDER BY c.customer_name
    """, (month,))

    # Формируем строку результата
    result_lines = []
    for row in cursor:
        result_lines.append(f"Покупатель {row[0]} совершил покупок на сумму {row[1]}")

    cursor.close()

    # Объединяем строки с переносом
    return "\n".join(result_lines)
# END
