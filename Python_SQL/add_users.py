import psycopg2
from psycopg2.extras import execute_batch, execute_values

# Подключаемся к базе
conn = psycopg2.connect(
    dbname="hexlet_db",
    user="vital",
    password="Kurt1994!",
    host="localhost"
)

# Создаем курсор
curs = conn.cursor()

# Вариант с execute_batch
users = (
    ("Bob", "232435"),
    ("Alice", "0987"),
    ("John", "234646757"),
)
execute_batch(curs, "INSERT INTO courses (username, phone) VALUES (%s, %s)", users)

# Сохраняем изменения
conn.commit()

# Проверяем, что добавилось
curs.execute("SELECT * FROM courses;")
for row in curs.fetchall():
    print(row)

# Закрываем соединение
curs.close()
conn.close()