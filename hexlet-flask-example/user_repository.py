import json
import sys
import uuid


class UserRepository():
    def __init__(self):
        self._load_users()

    def _load_users(self):
        """Загружает пользователей из файла"""
        try:
            with open("./users.json", 'r') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = []

    def _save_users(self):
        """Сохраняет пользователей в файл"""
        with open("./users.json", "w") as f:
            json.dump(self.users, f, indent=2)  # Добавил indent для читаемости

    def get_content(self):
        """Возвращает всех пользователей"""
        self._load_users()  # Всегда свежие данные
        return self.users

    def find(self, id):
        self._load_users()  # Всегда загружаем свежие данные
        for user in self.users:
            if str(id) == str(user.get('id', '')):
                return user
        return None

    def save(self, new_user):
        self._load_users()  # Загружаем свежие данные

        # Обновляем существующего пользователя
        if new_user.get('id'):
            for i, current in enumerate(self.users):
                if str(new_user['id']) == str(current.get('id', '')):
                    self.users[i] = new_user
                    self._save_users()
                    return new_user['id']

        # Добавляем нового пользователя
        new_user['id'] = str(uuid.uuid4())
        self.users.append(new_user)
        self._save_users()
        return new_user['id']