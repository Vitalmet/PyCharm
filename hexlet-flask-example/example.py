from flask import Flask, render_template, request

# Это callable WSGI-приложение
app = Flask(__name__)

users = [
    {'id': 1, 'name': 'mike'},
    {'id': 2, 'name': 'mishel'},
    {'id': 3, 'name': 'adel'},
    {'id': 4, 'name': 'keks'},
    {'id': 5, 'name': 'kamila'}
]

@app.route("/")
def hello_world():
    return "Welcome to Flask!"

@app.get("/users/")
def get_users():
    term = request.args.get('term', '')
    print(users)
    filtered_users = [user for user in users if term in user['name']]
    return render_template(
        'users/index.html',
        users=filtered_users,
        search=term,
    )

@app.post('/users')
def for_users():
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