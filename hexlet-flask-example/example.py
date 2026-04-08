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



#настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Это callable WSGI-приложение
app = Flask(__name__)
app.secret_key = "secret_key"

try:
    users = json.load(open('users.json'))
    logger.debug(f"Загружено {len(users)} пользователей из users.json")
except FileNotFoundError as e:
    logger.error(f"Файл users.json не найден: {e}")
    users = []
except json.JSONDecodeError as e:
    logger.error(f"Ошибка парсинга users.json: {e}")
    users = []

@app.route("/")
def hello_world():
    logger.debug("Запрос главной странцы")
    return "Welcome to Flask!"

@app.route("/users/")
def get_users():
    logger.debug("Запрос списка ползователей")
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
        logger.debug(f"Загружено {len(users)} пользователей из файла")
    except FileNotFoundError as e:
        logger.error(f"Файл users.json не найден при чтении: {e}")
        users = []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга users.json при чтении: {e}")
        users = []

    messages = get_flashed_messages(with_categories=True)
    term = request.args.get('term', '')
    filtered_users = [user for user in users if term in user['name']]
    logger.debug(f"Поиск по запросу '{term}': найдено {len(filtered_users)} пользователей")
    return render_template(
        'users/index.html',
        users=filtered_users,
        search=term,
        messages=messages,
    )

@app.post('/users')
def users_post():
    logger.debug(f"Получены данные формы: {request.form.to_dict()}")
    user_data = request.form.to_dict()
    errors = validate(user_data)
    if errors:
        logger.warning(f"Ошибки валидации при создании пользователя: {errors}")
        return render_template(
            'users/new.html',
            user=user_data,
            errors=errors,
        )
    id = str(uuid.uuid4())
    user = {
        'id': id,
        'name': user_data['name'],
        'email': user_data['email'],
    }
    users.append(user)
    try:
        with open('./users.json', 'w') as f:
            json.dump(users, f)
        logger.info(f"Создан новый пользователь: id={id}, name={user['name']}, email={user['email']}")
    except Exception as e:
        logger.error(f"Ошибка при сохранении пользователя в файл: {e}")
        flash('Пользователь успешно добавлен', 'success')
    return redirect(url_for('get_users'), code=302)

@app.route("/users/new")
def users_new():
    logger.debug("Отображение формы создания пользователя")
    user = {'name': '', 'email': ''}
    errors = {}
    return render_template(
        'users/new.html',
        user=user,
        errors=errors,
    )


@app.route('/users/<id>')
def show_user(id):
    logger.debug(f"Запрос просмотра пользователя с id={id}")
    try:
        with open('./users.json', 'r') as f:
            users = json.load(f)
        user = next(user for user in users if id == str(user['id']))
        logger.debug(f"Найден пользователь: {user['name']}")
        return render_template(
            'users/show.html',
            user=user,
        )
    except FileNotFoundError as e:
        logger.error(f"Файл users.json не найден: {e}")
        return "Пользователь не найден", 404
    except StopIteration:
        logger.warning(f"Пользователь с id={id} не найден")
        return "Пользователь не найден", 404
    except Exception as e:
        logger.error(f"Ошибка при поиске пользователя id={id}: {e}")
        return "Ошибка сервера", 500


@app.route('/courses/<id>')
def courses(id):
    logger.debug(f"Запрос курса с id={id}")
    return f'Course id: {id}'

def validate(user):
    errors = {}
    if not user['name']:
        errors['name'] = "Can't be blank"
        logger.debug("Валидация: отсутствует имя пользователя")
    if not user['email']:
        errors['email'] = "Can't be blank"
        logger.debug("Валидация: отсутствует email пользователя")
    return errors


@app.route("/courses/<int:id>")
def courses_show(id):
    logger.debug(f"Запрос просмотра курса с id={id}")
    # Создаем объект курса
    course = {
        "id": id,
        "name": f"Курс #{id}",
        "description": "Описание курса появится позже",
        "duration": "Не указана"
    }
    logger.debug(f"Отображение курса: {course['name']}")
    return render_template('courses/show.html', course=course)


@app.route("/courses")
def courses_list():
    logger.debug("Запрос списка курсов")
    # Можно передать пустой список или сгенерировать данные на лету
    empty_courses = []
    logger.debug(f"Найдено {len(empty_courses)} курсов")
    return render_template('courses/index.html', courses=empty_courses)


if __name__ == "__main__":
    logger.info("Запуск приложения")
    try:
        app.run(debug=True)
    except Exception as e:
        logger.critical(f"Критическая ошибка при запуске приложения: {e}")