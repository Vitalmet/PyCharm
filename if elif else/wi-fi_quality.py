"""
Эта программа проводит пользователя по шагам исправления
плогоо Wi-Fi соединения.
"""

print('Перезагрузите компьютер и попробуйте подключиться.')

answer = str(input('Вы исправили проблему? '))

if answer.lower() == 'нет':
    print('Перезагрузите маршрутизатор и попробуйте подключиться.')
if answer.lower() == 'да':
    exit()
else:
    if answer.lower() != 'нет' and answer.lower() != 'да':
        print('Ошибка ввода, для корректной работы нужен ответ да или нет')

answer = str(input('Вы исправили проблему? '))

if answer.lower() == 'нет':
    print('Убедитесь что кабели между маршрутизатором и модемом подсоеденены.')
if answer.lower() == 'да':
    exit()
else:
    if answer.lower() != 'нет' and answer.lower() != 'да':
        print('Ошибка ввода, для корректной работы нужен ответ да или нет')

answer = str(input('Вы исправили проблему? '))

if answer.lower() == 'нет':
    print('Переместите марщрутизатор на новое место.')
if answer.lower() == 'да':
   exit()
else:
    if answer.lower() != 'нет' and answer.lower() != 'да':
        print('Ошибка ввода, для корректной работы нужен ответ да или нет')

answer = str(input('Вы исправили проблему? '))

if answer.lower() == 'нет':
    print('Возьмите новый марщрутизатор.')
if answer.lower() == 'да':
    exit()
else:
    if answer.lower() != 'нет' and answer.lower() != 'да':
        print('Ошибка ввода, для корректной работы нужен ответ да или нет')

