day = int(input('Введите число: '))

if day < 1 or day > 7:
    print('Такой день недели существует только в другой галактике.')
else:
    if day == 1:
        print('Понедельник')
    if day == 2:
        print('Вторник')
    if day == 3:
        print('Среда')
    if day == 4:
        print('Четверг')
    if day == 5:
        print('Пятница')
    if day == 6:
        print('Суббота')
    if day == 7:
        print('Воскресенье')
