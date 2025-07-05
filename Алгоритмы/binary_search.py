def binary_search(arr, item):
    low = 0              # в переменных low и high хранятся границы той части
    high = len(arr) - 1  # списка, в котророй выполняется поиск

    while low <= high:          # Пока эта часть не сократится до одного элемента
        mid = (low + high) // 2 # проверяем соседний элемент
        guess = arr[mid]
        if guess == item:       # Значение найдено
            return mid
        elif guess > item:      # много
            high = mid - 1
        else:                   # мало
            low = mid + 1
    return None                 # Значения не существует

my_list = list(range(1, 200, 1))      # Тестируем функцию

print(binary_search(my_list, 128))

