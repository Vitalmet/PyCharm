
color_for_mix = str(input('Введите цвет для смешивания: ')) # цвет для смешивания
color_for_mix1 = str(input('Введите цвет для смешивания: ')) # цвет для смешивания

color_for_mix = color_for_mix.lower() # чтобы не было зависимости от регистра
color_for_mix1 = color_for_mix1.lower() # чтобы не было зависимости от регистра

if color_for_mix == 'красный' and color_for_mix1 == 'синий':
    print ('Фиолетовый')

elif color_for_mix == 'красный' and color_for_mix1 == 'желтый':
    print('Оранжевый')

elif color_for_mix == 'синий' and color_for_mix1 == 'желтый':
    print('Зеленый')

else:
    print('Олшибка, смешиваем только основные цвета, потомучто их нельзя получить путем смешивания.')

