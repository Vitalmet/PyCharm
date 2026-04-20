import psycopg2
from psycopg2.extras import RealDictCursor
import os


class UserRepository():
    def __init__(self, db_url=None):
        if db_url is None:
            self.db_url = os.getenv('DATABASE_URL')
        else:
            self.db_url = db_url

        if not self.db_url:
            raise Exception("DATABASE_URL не настроена! Проверьте .env файл")

    def _get_connection(self):
        """Создаёт соединение с БД"""
        return psycopg2.connect(self.db_url)

    def get_content(self):
        """Возвращает всех пользователей"""
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT id, name, email FROM users ORDER BY id")
                return cur.fetchall()

    def find(self, id):
        """Находит пользователя по id"""
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT id, name, email FROM users WHERE id = %s", (id,))
                return cur.fetchone()

    def save(self, user_data):
        """Сохраняет пользователя"""
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                if user_data.get('id'):
                    # Обновление
                    cur.execute(
                        "UPDATE users SET name = %s, email = %s WHERE id = %s",
                        (user_data['name'], user_data['email'], user_data['id'])
                    )
                else:
                    # Создание нового
                    cur.execute(
                        "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
                        (user_data['name'], user_data['email'])
                    )
                    user_data['id'] = cur.fetchone()[0]
                conn.commit()
                return user_data['id']

    def destroy(self, id):
        """Удаляет пользователя"""
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id = %s", (id,))
                conn.commit()
                return cur.rowcount > 0