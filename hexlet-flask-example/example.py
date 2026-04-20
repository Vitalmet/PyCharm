import os
import psycopg2
import logging
from dotenv import load_dotenv
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

load_dotenv()

# Получаем URL базы данных (для Render)
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

logging.basicConfig(
    level=logging.ERROR,  # Изменено с DEBUG на ERROR
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Это callable WSGI-приложение
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'my-secret-key')

# Глобальный репозиторий с подключением к БД
repo = UserRepository(DATABASE_URL)

@app.route("/")
def hello_world():
    return "Welcome to Flask!"


@app.route("/users/")
def get_users():
    users = repo.get_content()
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


    # Создаем нового пользователя
    new_user = {
        'name': user_data['name'].strip(),
        'email': user_data['email'].strip(),
    }

    try:
        user_id = repo.save(new_user)
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


@app.route("/users/<id>/delete", methods=['POST'])
def users_delete(id):
    user = repo.find(id)
    if not user:
        flash('Пользователь не найден', 'error')
        return redirect(url_for('get_users'), code=302)

    repo.destroy(id)
    flash('Пользователь удален', 'success')
    return redirect(url_for('get_users'), code=302)


@app.route('/users/<id>')
def show_user(id):
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


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # ← порт для Render
    logger.info(f"Запуск приложения на порту {port}")
    try:
        app.run(host='0.0.0.0', port=port)  # ← host='0.0.0.0' для Render
    except Exception as e:
        logger.critical(f"Критическая ошибка при запуске приложения: {e}")