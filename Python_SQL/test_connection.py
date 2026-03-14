import psycopg2

try:
    # Подключаемся к базе
    conn = psycopg2.connect(
        dbname="hexlet_db",
        user="vital",
        password="Kurt1994!",
        host="localhost",
        port="5432"
    )
    print("✅ Подключение к базе данных успешно!")

    # Создаем курсор и выполняем простой запрос
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"📊 Версия PostgreSQL: {version[0]}")

    # Закрываем соединение
    cursor.close()
    conn.close()
    print("🔌 Соединение закрыто")

except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
    print("\n🔍 Детали ошибки помогут найти причину")