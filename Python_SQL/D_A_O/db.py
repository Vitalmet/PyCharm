# db.py
import psycopg2
from psycopg2.extras import DictCursor


def get_connection():
    return psycopg2.connect(
        dbname="hexlet_db",
        user="vital",
        password="Kurt1994!",
        host="localhost",
        cursor_factory=DictCursor,
    )


def commit(conn):
    conn.commit()


def save_user(conn, user):
    with conn.cursor() as cur:
        if user.id is None:
            cur.execute(
                "INSERT INTO courses (username, phone) VALUES (%s, %s) RETURNING id;",
                (user.username, user.phone),
            )
            user.id = cur.fetchone()["id"]
        else:
            cur.execute(
                "UPDATE courses SET username = %s, phone = %s WHERE id = %s;",
                (user.username, user.phone, user.id),
            )
    return user


def find_user(conn, user_id):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM courses WHERE id = %s;", (user_id,))
        result = cur.fetchone()
        if result:
            return User(**result)
    return None

def delete_user(conn, user_id):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM courses WHERE id = %s;", (user_id,))
        # Возвращаем количество удаленных строк (1 если пользователь был, 0 если нет)
        return cur.rowcount > 0