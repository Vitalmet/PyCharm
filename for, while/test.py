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