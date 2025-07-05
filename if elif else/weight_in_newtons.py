body_weight = float(input('Введите массу тела (в кг): '))
weight = body_weight * 9.8

if weight > 500:
    print(f"Вес тела: {weight:.2f} Н - тело слишком тяжелое")
elif weight < 100:
    print(f"Вес тела: {weight:.2f} Н - тело слишком легкое")
else:
    print(f"Вес тела: {weight:.2f} Н - тело в нормальном диапазоне")