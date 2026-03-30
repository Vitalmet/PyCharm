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
    curs.execute("SELECT id, name FROM courses WHERE name=%s;", (name,))
    curs.fetchall()

with conn.cursor() as curs:
    # также можно использовать именованные аргументы
    curs.execute(
        "INSERT INTO courses (name, age) VALUES (%(name)s, %(age)s);",
        {"age": age, "name": name},
    )
    conn.commit()

conn.close()

Ускорение запросов

from psycopg2.extras import execute_batch, execute_values

courses = (
    ("Bob", "bob@mail.com"),
    ("Alice", "alice@mail.com"),
    ("John", "john@mail.com"),
)
execute_batch(curs, "INSERT INTO courses (name, email) VALUES (%s, %s)", courses)

# в случае execute_values запрос будет выглядеть так
courses = [
    ("Bob", "bob@mail.com"),
    ("Alice", "alice@mail.com"),
    ("John", "john@mail.com"),
]
execute_values(curs, "INSERT INTO courses (name, email) VALUES %s", courses)

Возврат идентификатора

user = User()
# Сохраняем пользователя в базу данных
# После этого становится доступен id
id = user.get_id()
# Его можно использовать для формирования ссылок или вставки связанных записей

# RETURNING возвращает указанное поле
 with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO courses (name, email) VALUES (%s, %s) RETURNING id;",
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

# урок 6
import psycopg2
from psycopg2.extras import DictCursor

conn = psycopg2.connect('postgresql://tirion:secret@localhost:5432/tirion')


# BEGIN (write your solution here)
def create_post(conn, post_data):
    with conn.cursor(cursor_factory=RealDictCursor) as curs:
        # Вставляем данные из словаря
        curs.execute("""
            INSERT INTO posts (title, content, author_id)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (post_data['title'], post_data['content'], post_data['author_id']))

        # Получаем результат с id
        result = curs.fetchone()

        # Возвращаем id созданного поста
        return result['id']


def add_comment(conn, dict_comm_data):
    with conn.cursor(cursor_factory=RealDictCursor) as curs:
        curs.execute("""
        INSERT INTO comments (post_id, author_id, content)
        VALUES (%s, %s, %s)
        RETURNING id
        """, (dict_comm_data['post_id'], dict_comm_data['author_id'], dict_comm_data['content']))

        result = curs.fetchone()

        return result['id']


from psycopg2.extras import RealDictCursor

def get_latest_posts(conn, n):
    with conn.cursor(cursor_factory=RealDictCursor) as curs:
        # Сначала получаем n последних постов
        curs.execute("""
            SELECT id, title, content, author_id, created_at
            FROM posts
            ORDER BY created_at DESC
            LIMIT %s
        """, (n,))

        posts = curs.fetchall()

        # Для каждого поста получаем комментарии
        for post in posts:
            curs.execute("""
                SELECT id, author_id, content, created_at
                FROM comments
                WHERE post_id = %s
                ORDER BY created_at
            """, (post['id'],))

            post['comments'] = curs.fetchall()

        return posts
# END