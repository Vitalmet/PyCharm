"""
Эта программа просит ввести пользователя год и затем показывает
количество дней в феврале этого года.
"""

# Определить делится ли год на 100, если делится то этот год высокосный
# только тогда, когда делится ещё и на 400
# Eсли год не делится на 100, то он высокосный только тогда,
# когда делится на 4.

year = int(input('Введите год: '))

if year % 100 == 0 and year % 400 == 0 and year % 100 != 0 and year % 4 == 0:
    print(f'В {year} году 29 дней')
else:
    print(f'В {year} году 28 дней')