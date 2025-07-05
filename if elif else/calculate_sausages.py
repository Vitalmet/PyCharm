

SAUSAGES = 10
BUNS = 8
peoples = int(input('Введите количество участников пикника: '))
hotdogs = int(input('Введите количество хот-догов для каждого участника: '))

number_hotdogs = peoples*hotdogs
print('Общее количество хот-догов:',number_hotdogs)

if number_hotdogs%10==0 and number_hotdogs%8==0:
    bag_sausages = number_hotdogs // SAUSAGES
    bag_buns = number_hotdogs // BUNS
    print('Количество упаковок с сосисками:', bag_sausages)
    print('Количество упаковок с булками:', bag_buns)

    remaining_sausages = bag_sausages*SAUSAGES-number_hotdogs
    remaining_buns = bag_buns*BUNS - number_hotdogs

    print('Оставшиеся сосиски', remaining_sausages)
    print('Оставшиеся булочки', remaining_buns)
elif number_hotdogs%10==0:
    bag_sausages = number_hotdogs // SAUSAGES
    bag_buns = number_hotdogs // BUNS+1
    print('Количество упаковок с сосисками:', bag_sausages)
    print('Количество упаковок с булками:', bag_buns)

    remaining_sausages = bag_sausages * SAUSAGES - number_hotdogs
    remaining_buns = bag_buns * BUNS - number_hotdogs

    print('Оставшиеся сосиски', remaining_sausages)
    print('Оставшиеся булочки', remaining_buns)
else:
    bag_sausages = number_hotdogs//SAUSAGES+1
    bag_buns = number_hotdogs//BUNS+1
    print('Количество упаковок с сосисками:',bag_sausages)
    print('Количество упаковок с булками:',bag_buns)

    remaining_sausages = bag_sausages*10-number_hotdogs
    remaining_buns = bag_buns*8-number_hotdogs

    print('Оставшиеся сосиски',remaining_sausages)
    print('Оставшиеся булочки',remaining_buns)