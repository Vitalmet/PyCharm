import psycopg2


# Подключаемся к базе
conn = psycopg2.connect(
    dbname="hexlet_db",
    user="vital",
    password="Kurt1994!",
    host="localhost"
)

sql = "INSERT INTO courses (username, phone) VALUES ('Ыспанец-Гриша', '457458');"

curs = conn.cursor()
curs.execute(sql)

# Никакие изменения не сохраняются, пока не вызван commit().


raise Exception("Ошибка во время транзакции")
conn.commit()
conn.close()
