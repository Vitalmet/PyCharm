import turtle

# Задаём координаты прямоугольника
x_min, y_min = 100, 100  # Левый верхний угол (ось Y идёт вниз)
x_max, y_max = 200, 200  # Правый нижний угол

# Перемещаем черепаху в какую-то точку (например, (150, 150))
turtle.penup()
turtle.goto(150, 150)

# Получаем текущие координаты черепахи
current_x = turtle.xcor()
current_y = turtle.ycor()

# Проверяем, находится ли черепаха внутри прямоугольника
if (x_min <= current_x <= x_max) and (y_min <= current_y <= y_max):
    turtle.hideturtle()  # Если да — прячем черепаху
    print("Черепаха внутри прямоугольника и скрыта!")
else:
    print("Черепаха вне прямоугольника.")

turtle.done()  # Оставляем окно открытым