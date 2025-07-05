"""
Эта прогамма просит пользователя ввести количкство секунд
и преобразует их количество в минуты, часы и дни.
"""
# в минуте 60 секунд
# в часе 3600 секунд
# в дне 86400 секунд

seconds = int(input('Введите количество секунд: '))

minutes = seconds // 60
remaining_seconds = seconds % 60

if seconds <= 60 or seconds < 3600:
    print(f'Время составляет: {minutes} мин. {remaining_seconds} сек.')

elif seconds == 3600 or seconds < 86400:

    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds_final = remaining_seconds % 60

    print(f'Время составляет: {hours} час. {minutes} мин. {seconds_final} сек.')

elif seconds >= 86400:

    days = seconds // 86400
    remaining_after_days = seconds % 86400

    hours = remaining_after_days // 3600
    remaining_after_hours = remaining_after_days % 3600

    minutes = remaining_after_hours // 60
    seconds_final = remaining_after_hours % 60

    print(f'Время составляет: {days} дн. {hours} час. {minutes} мин. {seconds_final} сек.')
