import psycopg2

try:
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(
        dbname="hexlet_db",
        user="vital",
        password="Kurt1994!",
        host="localhost",
        port="5432"
    )
except:
    # в случае сбоя подключения будет выведено сообщение  в STDOUT
    print("Can`t establish connection to database")