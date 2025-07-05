age = float(input('Введите возраст: '))

if age <= 1:
    print('baby')
if age > 1 and age <= 13:
    print('child')
if age >= 13 and age <= 20:
    print('teenager')
if age > 20:
    print('adult')