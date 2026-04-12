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
from user_repository import UserRepository

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
    repo = UserRepository()
    users = repo.get_content()  # Добавьте этот метод в UserRepository

    messages = get_flashed_messages(with_categories=True)
    term = request.args.get('term', '')
    filtered_users = [user for user in users if term.lower() in user['name'].lower()]
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
        ), 422

    repo = UserRepository()

    # Создаем нового пользователя
    new_user = {
        'name': user_data['name'].strip(),
        'email': user_data['email'].strip(),
    }

    try:
        user_id = repo.save(new_user)  # Repository сам сгенерирует id
        flash('Пользователь успешно добавлен', 'success')
    except Exception as e:
        logger.error(f"Ошибка при сохранении: {e}")
        flash('Ошибка при сохранении пользователя', 'error')
        return render_template('users/new.html', user=user_data, errors=errors), 500

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


@app.route("/users/<id>/edit")
def users_edit(id):
    repo = UserRepository()
    user = repo.find(id)

    if not user:
        flash('Пользователь не найден', 'error')
        return redirect(url_for('get_users'))

    errors = {}
    return render_template(
        'users/edit.html',
        user=user,
        errors=errors,
    )


@app.route("/users/<id>/patch", methods=['POST'])
def users_patch(id):
    repo = UserRepository()
    user = repo.find(id)

    if not user:
        flash('Пользователь не найден', 'error')
        return redirect(url_for('get_users'), code=302)

    data = request.form.to_dict()
    errors = validate(data)

    if errors:
        return render_template(
            'users/edit.html',
            user=user,
            errors=errors,
        ), 422

    # Обновляем данные пользователя
    user['name'] = data['name'].strip()
    user['email'] = data['email'].strip()

    try:
        repo.save(user)
        flash('Пользователь успешно обновлен', 'success')
    except Exception as e:
        logger.error(f"Ошибка при обновлении: {e}")
        flash('Ошибка при обновлении пользователя', 'error')
        return render_template('users/edit.html', user=user, errors=errors), 500

    return redirect(url_for('get_users'), code=302)


@app.route('/users/<id>')
def show_user(id):
    repo = UserRepository()
    user = repo.find(id)

    if not user:
        flash('Пользователь не найден', 'error')
        return redirect(url_for('get_users'))

    return render_template('users/show.html', user=user)

def validate(user):
    errors = {}
    if not user.get('name', '').strip():
        errors['name'] = "Имя не может быть пустым"
    if not user.get('email', '').strip():
        errors['email'] = "Email не может быть пустым"
    elif '@' not in user['email']:
        errors['email'] = "Введите корректный email (должен содержать @)"
    return errors


@app.route("/courses/<int:id>")
def courses_show(id):
    course = {
        "id": id,
        "name": f"Курс #{id}",
        "description": "Описание курса появится позже",
        "duration": "Не указана"
    }
    return render_template('courses/show.html', course=course)


@app.route("/courses")
def courses_list():
    empty_courses = []
    return render_template('courses/index.html', courses=empty_courses)


if __name__ == "__main__":
    logger.info("Запуск приложения")
    try:
        app.run(debug=True)
    except Exception as e:
        logger.critical(f"Критическая ошибка при запуске приложения: {e}")