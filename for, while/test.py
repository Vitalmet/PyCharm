''' product = 0  # Инициализация переменной

while product < 100:
    number = int(input("Введите число: "))
    product = number * 10
    print(f"Результат: {product}")

print("Цикл завершён (product >= 100)") '''

'''name = "д"

while name == "д" or name == "Д":
    num_1 = int(input("Введите число: "))
    num_2 = int(input("Введите ещё число: "))
    sum = num_1 + num_2
    print(f"Сумма вводимых чисел равна: {sum}")

    name = input("Ещё будете вводить число? " +
                    "(Введите д, если да): ")
print("Программа завершена.")'''


'''for x in range(0, 1001, 10):
    print (x)'''

'''total = 0  # Инициализируем переменную для нарастающего итога

for i in range(1, 11):  # Цикл на 10 итераций
    number = float(input(f"Введите число {i}: "))  # Запрос числа с номером попытки
    total += number  # Добавляем введенное число к итогу
    print(f"Текущий итог: {total}")  # Выводим промежуточный результат

print("\nФинальный нарастающий итог:", total)  # Выводим окончательный результат'''

"""
total = 0.0  # Инициализируем переменную для суммы

for n in range(1, 31):  # n от 1 до 30
    denominator = 31 - n  # Знаменатель (30, 29, 28,...1)
    term = n / denominator  # Вычисляем текущий член ряда
    total += term  # Добавляем к сумме

    # Для наглядности выводим каждый шаг (можно убрать)
    print(f"{n}/{denominator} = {term:.4f}")

print(f"\nСумма ряда: {total:.6f}") """

"""rows = 10
cols = 15
for r in range(rows):
    for c in range(cols):
        print("#", end="")
    print()"""

"""number = int(input("Введите положительное число: "))
while number <= 0:
    print("ERROR: число не может быть отрицательным или равно 0")
    number = int(input("Введите положительное число: "))
else:
    print("OK")"""

'''number = int(input("Введите число от 1 до 100: "))
while number <= 0 or number > 100:
    print("ERROR: число не входит в заданный диапазон")
    number = int(input("Введите число от 1 до 100: "))
    print("OK")'''

""""# Пройденное растояние
# Эта программа просит пользователя ввести скорость ТС
# и затем считает расстояние пройденное за определенное время время.

vehicle_speed = int(input("Какая скорость транспортного средства в км/ч? "))
time = int(input("Сколько часов оно двигалось? "))

# Печатаем заголовки таблицы.
print()
print("Час\tПройденное расстояние")
print("-----------------------------")

# выводим формулу расстояние = скорость * время

for d in range(1, time + 1):
    distance  = vehicle_speed * d
    print(f'{d}\t{distance:.2f}')
"""

"""def greatest_common_divisor(num1, num2):
    while num2 != 0:
        remainder = num1 % num2  # Сохраняем остаток
        num1 = num2              # Обновляем num1
        num2 = remainder         # Обновляем num2
    return num1
"""

"""def func(a, b, *args, f="bar", k=42, **kwargs):
    # параметр 'a' содержит первый аргумент
    print(f"a -> {a}")
    # параметр 'b' содержит второй аргумент
    print(f"b -> {b}")
    # args содержит все остальные позиционные аргументы
    print(f"args -> {args}")
    # f содержит именованный аргумент и равен bar по умолчанию
    print(f"f -> {f}")
    # k содержит именованный аргумент и равен 42 по умолчанию
    print(f"k -> {k}")
    # kwargs содержит все остальные именованные аргументы
    print(f"kwargs -> {kwargs}")


func(1, 2, 3, 4, 5, f="hello", k=24, l=[1, 2], ll={"key": "value"})
"""

"""# толщина осадков

year = int(input("Введите кол-во лет за которое нужно посчитать толщину осадков: "))

for t in range(1, year + 1):
    total = 0
    for m in range(1, 13):
        precipitation = int(input(f"Введите кол-во осадков в мм за {m}-й месяц {t}-го года: "))
        total += precipitation
        print("------------------------------")

    print(f"Сумма осадков за {t}-й год: {total} мм")"""

""""# вывести таблицу температур между Цельсия и Фаренгейт
for x in range(5):
    c = float(input("Введите температуру по Цельсия: "))
    f = (9 / 5) * c + 32
    print()
    print("--------------------------\t-------------------------------")
    print(f"Температура по Цельсия:{c}\tТемпература по Фаренгейту:{f}")"""

"""daily_salary = 0.1  # Зарплата за 1 день (в рублях)
days_worked = int(input("Введите количество отработанных дней: "))
total_salary = days_worked * daily_salary

print("\n----------------\t------------------")
print(f"ЗП в рублях за весь период составляет: {total_salary:.2f}")"""

