from flask import Flask, redirect

# Это callable WSGI-приложение
app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Welcome to Flask!'

@app.get("/users")
def users_get():
    return "GET /users"

@app.post("/users")
def users():
    return redirect("/")

@app.route("/courses/<id>")
def courses_show(id):
    return f"Course id: {id}"

