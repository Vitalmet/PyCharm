# Эта программа показывает сколько каллорий можно
# сжечь, при беге определенное время от 10 до 30 минут.

calories_per_minute = 4.2

print("Минуты\tКалории")
print("----------------")

for minutes in range(10, 31, 5):  # от 10 до 30 с шагом 5
    calories_burned = minutes * calories_per_minute
    print(f"{minutes}\t{calories_burned:.1f}")