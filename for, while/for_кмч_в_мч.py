# Эта программа преобразует скорости от 60
# до 130 км/ч (с приращиванием в 10 км) в mph.

START_SPEED = 60  # Начальная скорость
END_SPEED = 131   # Конечная скорость
INCREMENT = 10    # Приращение скорости
CONVERSION_FACTOR = 0.6214 # Коэффициент перерасчета

# Напечатать заголовки таблицы
print('KPH\tMPH')
print('---------------')

# Напечатать скорости.
for speed in range(START_SPEED, END_SPEED, INCREMENT):
    mph = speed * CONVERSION_FACTOR
    print(f'{speed}\t{mph:.1f}')

