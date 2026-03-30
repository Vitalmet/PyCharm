from flask import render_template, Flask

# Это callable WSGI-приложение
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Welcome to Flask!"

@app.get("/users")
def users_get():
    return "GET /users"


@app.post('/users')
def users():
    return 'Users', 302

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

@app.route('/users/<id>')
def show_user(id):
    user = {
        "id": id,
        "name": f"user-{id}"
    }
    return render_template(
        'users/show.html',
        user=user,
    )


if __name__ == "__main__":
    app.run(debug=True)