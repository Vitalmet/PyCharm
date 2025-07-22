# Эта программа просит пользователя ввести сумму
# бюджета выделенного на 1 месяц, при помощи цикла
# просит ввести суммы отдельных статей расхода и
# считает перерасход или экоомию бюджета.

monthly_budget = float(input("Введите сумму, выделенную на месяц: "))
total_expenses = 0.0
stop_cycle = 'д'

while stop_cycle.lower() == 'д':
    expense = float(input("Введите сумму расхода: "))
    total_expenses += expense  # Суммируем расходы
    stop_cycle = input("Добавить ещё расход? (д/н): ")

balance = monthly_budget - total_expenses

if balance > 0:
    print(f"Экономия: {balance:.2f} руб.")
elif balance < 0:
    print(f"Перерасход: {abs(balance):.2f} руб.")
else:
    print("Бюджет сведён ровно!")
