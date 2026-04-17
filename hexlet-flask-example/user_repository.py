import psycopg2
from psycopg2.extras import RealDictCursor
import os
import uuid


class UserRepository():
    def __init__(self, db_url=None):
        if db_url is None:
            self.db_url = os.getenv('DATABASE_URL')

        # Всегда используем БД, если есть URL
        self._use_session = self.db_url is None

        if self._use_session:
            # Для совместимости - НО НЕ ИСПОЛЬЗУЕМ session здесь!
            # Вместо этого используем просто список
            self._users = []
            self._next_id = 1

    def _get_connection(self):
        """Создаёт соединение с БД"""
        if not self.db_url:
            raise Exception("DATABASE_URL not configured")
        return psycopg2.connect(self.db_url)

    def get_content(self):
        """Возвращает всех пользователей"""
        if self._use_session:
            # Возвращаем копию списка
            return [user.copy() for user in self._users]

        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT id, name, email FROM users ORDER BY id")
                return cur.fetchall()

    def find(self, id):
        """Находит пользователя по id"""
        if self._use_session:
            for user in self._users:
                if str(id) == str(user.get('id', '')):
                    return user.copy()
            return None

        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT id, name, email FROM users WHERE id = %s", (id,))
                return cur.fetchone()

    def save(self, user_data):
        """Сохраняет пользователя"""
        if self._use_session:
            # Ищем существующего пользователя
            if user_data.get('id'):
                for i, current in enumerate(self._users):
                    if str(user_data['id']) == str(current.get('id', '')):
                        self._users[i] = user_data.copy()
                        return user_data['id']

            # Создаем нового
            new_id = str(uuid.uuid4())
            user_data['id'] = new_id
            self._users.append(user_data.copy())
            return new_id

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
        if self._use_session:
            original_count = len(self._users)
            self._users = [user for user in self._users if str(user.get('id', '')) != str(id)]
            return len(self._users) < original_count

        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE id = %s", (id,))
                conn.commit()
                return cur.rowcount > 0