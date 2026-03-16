from models import User
import db

conn = db.get_connection()


user = User(username="John Doe", phone="1234567890")
user.id  # None

new_user = db.save_user(conn, user)
# делаем коммит после каждого изменения
db.commit(conn)
new_user.id  # тут уже выводится какой-то id

found_user = db.find_user(conn, 42)
db.commit(conn)
found_user  # здесь выводится найденный user

# закрываем соединение
conn.close()