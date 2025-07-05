month = int(input('Введите месяц рождениия (1-12): '))
day = int(input('Введите день рождениия (1-31): '))
year = int(input('Введите двузначный год рождения (00-99): '))

magic = day * month

if magic == year:
    print(f'{day}.0{month}.{year}: {magic} = {year} Дата рождения магическая')
else:
    print(f'{day}.0{month}.{year}: {magic} != {year} Дата рождения не является магической')