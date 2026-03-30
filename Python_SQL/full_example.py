import psycopg2

try:
    # Подключаемся
    conn = psycopg2.connect(
        dbname="hexlet_db",
        user="vital",
        password="Kurt1994!",
        host="localhost",
        port="5432"
    )
    print("✅ Подключились к БД")

    cursor = conn.cursor()

    # Создаем таблицу (IF NOT EXISTS - чтобы не было ошибки, если таблица уже есть)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255),
            phone VARCHAR(255)
        );
    """)
    conn.commit()
    print("✅ Таблица courses создана")

    # Очищаем таблицу от предыдущих записей (чтобы не было дубликатов)
    cursor.execute("DELETE FROM courses;")

    # Вставляем несколько записей
    users_data = [
        ('tommy', '123456789'),
        ('ann', '987654321'),
        ('john', '555555555')
    ]

    for username, phone in users_data:
        cursor.execute(
            "INSERT INTO courses (username, phone) VALUES (%s, %s);",
            (username, phone)
        )

    conn.commit()
    print(f"✅ Добавлено {len(users_data)} пользователей")

    # Читаем все данные
    cursor.execute("SELECT * FROM courses;")
    print("\n📊 Содержимое таблицы courses:")
    for row in cursor.fetchall():
        print(f"  ID: {row[0]}, Username: {row[1]}, Phone: {row[2]}")

    cursor.close()
    conn.close()
    print("🔌 Соединение закрыто")

except Exception as e:
    print(f"❌ Ошибка: {e}")