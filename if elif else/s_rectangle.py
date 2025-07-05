length_first_rectangle = int(input('Введите длинну первого прямоугольника: ')) # длина первого прямоугольника
width_first_rectangle = int(input('Введите ширину первого прямоугольника: ')) # ширина первого прямоугольника

length_second_rectangle = int(input('Введите длинну второго прямоугольника: ')) # длина второго прямоугольника
width_second_rectangle = int(input('Введите ширину второго прямоугольника: ')) # ширина второго прямоугольника

s_first_rectangle = length_first_rectangle * width_first_rectangle
s_second_rectangle = length_second_rectangle * width_second_rectangle

if s_first_rectangle > s_second_rectangle:
    print('Площадь первого прямоугольника больше площади второго прямоуголника')
if s_second_rectangle > s_first_rectangle:
    print('Площадь второго прямоугольника больше площади первого прямоуголника')
else:
    print('Площади равны')
