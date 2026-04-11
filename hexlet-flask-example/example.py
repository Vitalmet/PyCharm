import json
import uuid
import logging
from urllib import request

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
    get_flashed_messages,
    flash
)

# Минимальное логирование - только ошибки
logging.basicConfig(
    level=logging.ERROR,  # Изменено с DEBUG на ERROR
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Это callable WSGI-приложение
app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/")
def hello_world():
    return "Welcome to Flask!"

@app.route("/users/")
def get_users():
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError as e:
        logger.error(f"Файл users.json не найден при чтении: {e}")
        users = []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга users.json при чтении: {e}")
        users = []

    messages = get_flashed_messages(with_categories=True)
    term = request.args.get('term', '')
    filtered_users = [user for user in users if term in user['name']]
    return render_template(
        'users/index.html',
        users=filtered_users,
        search=term,
        messages=messages,
    )


@app.post('/users')
def users_post():
    user_data = request.form.to_dict()
    errors = validate(user_data)

    if errors:
        return render_template(
            'users/new.html',
            user=user_data,
            errors=errors,
        )

    # ✅ Читаем актуальные данные ИЗ ФАЙЛА прямо сейчас
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []  # Если файла нет, начинаем с пустого списка

    id = str(uuid.uuid4())
    user = {
        'id': id,
        'name': user_data['name'],
        'email': user_data['email'],
    }

    users.append(user)  # ✅ Добавляем в свежепрочитанный список

    try:
        with open('users.json', 'w') as f:
            json.dump(users, f)
        flash('Пользователь успешно добавлен', 'success')
    except Exception as e:
        logger.error(f"Ошибка при сохранении: {e}")
        flash('Ошибка при сохранении пользователя', 'error')
        return render_template('users/new.html', user=user_data, errors=errors)

    return redirect(url_for('get_users'), code=302)

@app.route("/users/new")
def users_new():
    user = {'name': '', 'email': ''}
    errors = {}
    return render_template(
        'users/new.html',
        user=user,
        errors=errors,
    )

@app.route('/users/<id>')
def show_user(id):
    try:
        with open('./users.json', 'r') as f:
            users = json.load(f)
        user = next(user for user in users if id == str(user['id']))
        return render_template(
            'users/show.html',
            user=user,
        )
    except FileNotFoundError as e:
        logger.error(f"Файл users.json не найден: {e}")
        return "Пользователь не найден", 404
    except StopIteration:
        return "Пользователь не найден", 404
    except Exception as e:
        logger.error(f"Ошибка при поиске пользователя id={id}: {e}")
        return "Ошибка сервера", 500

@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'

def validate(user):
    errors = {}
    if not user['name']:
        errors['name'] = "Can't be blank"
    if not user['email']:
        errors['email'] = "Can't be blank"
    return errors

@app.route("/courses/<int:id>")
def courses_show(id):
    # Создаем объект курса
    course = {
        "id": id,
        "name": f"Курс #{id}",
        "description": "Описание курса появится позже",
        "duration": "Не указана"
    }
    return render_template('courses/show.html', course=course)

@app.route("/courses")
def courses_list():
    # Можно передать пустой список или сгенерировать данные на лету
    empty_courses = []
    return render_template('courses/index.html', courses=empty_courses)

if __name__ == "__main__":
    logger.info("Запуск приложения")
    try:
        app.run(debug=True)
    except Exception as e:
        logger.critical(f"Критическая ошибка при запуске приложения: {e}")