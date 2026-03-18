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

# Урок 7

def save_lesson(conn, lesson):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        if lesson.id is None:
            cur.execute(
                "INSERT INTO lessons (name, text, course_id) VALUES (%s, %s, %s) RETURNING id",
                (lesson.name, lesson.text, lesson.course_id)
            )
            lesson.id = cur.fetchone().id
        else:
            cur.execute(
                "UPDATE lessons SET name = %s, text = %s, course_id = %s WHERE id = %s",
                (lesson.name, lesson.text, lesson.course_id, lesson.id)
            )
    return lesson.id

def find_lesson(conn, lesson_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT id, name, text, course_id FROM lessons WHERE id = %s", (lesson_id,))
        result = cur.fetchone()
        if result:
            return Lesson(
                id=result.id,
                name=result.name,
                text=result.text,
                course_id=result.course_id
                )
    return None

def get_course_lessons(conn, course_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT id, name, text, course_id FROM lessons WHERE course_id = %s", (course_id,))
        return [
            Lesson(id=row.id, name=row.name, text=row.text, course_id=row.course_id)
            for row in cur.fetchall()
        ]