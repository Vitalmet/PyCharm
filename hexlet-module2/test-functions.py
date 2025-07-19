"""a = 42

def find():
    def inner_find():
        print(a)

    inner_find()

find()"""
from sys import prefix

"""def outer():
    x = 42
    def inner():
        x = 12
        print("Local x =", x)
    # вызываем ф-ию
    # ведь окружения создаются лишь в момент вызова, а не определения ф-ии.
    inner()
    print("New x = ", x)

outer()
# Local x = 12
# New = 42"""

"""def outer():
    x = 42

    def inner():
        # обращаемся к внещней х и переопределяем ее
        nonlocal x # ключевое слово
        print("Nonlocal x = ", x)
        x = 12

    inner()
    print("New x = ", x)

outer()
# Nonlocal x = 42
# New = 12"""

"""x = 42

def change():
    # переопределяем существующую глобальгую переменную
    global x
    x = 12

change()
print(x)"""

"""def a():
    # создаем новую глобальную переменную
    global y
    y = 2
    print(y)

def b():
    # т.к у глобальная, то доступна даже внутри другой ф-ии
    print(y + 10)

a()
b()"""

"""# ЗАМЫКАНИЕ
def create_print():
    name = "King"

    def print_name():
        print(name)

    return print_name

my_print = create_print()
my_print()"""

n = 0
double_null = '00'

def id_generator(prefix):
    global n
    n += 1
    res = prefix + '-' + double_null + str(n)
    return res
