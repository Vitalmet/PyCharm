"""# Эта программа имеет две функции
# Сначала определяем главную функцию

def main():
    print('У меня для вас известие.')
    message()
    print('До свидания!')

# Затем мы определяем функцию message.

def message():
    print('Я - Артур,')
    print('король британцев.')

# Вызвать главную функцию
main()
"""

"""def get_count(sentence):
    count = 0
    for char in sentence:
        if char.lower() == 'aeiou':
            count += 1
    return count

get_count('aeiou')
"""
"""                                                    
# Сортировка по выбору
line = [int(elem) for elem in input().split(" ")]

for j in range(len(line)):
    for i in range(j, len(line)):
        if line[i] < line[j]:
            t = line[j]
            line[j] = line[i]
            line[i] = t
print(line)
"""

"""line = input()
lst = [int(elem) for elem in line.split()]
N = lst[0]
M = lst[1]

arr = []
for i in range(N):
    line = input()
    lst = [int(elem) for elem in line.split()]
    arr.append(lst)

print(arr)
"""
"""def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

answer = factorial(int(input()))
print(answer)
"""

"""def flatten(nested_list):
    flat_list = []

    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list

nested = [1, [2, [3, 4], 5], [6, 7], [1, 2, 3, 4, [5], [], 10 ]]
print(flatten(nested))
"""

"""def factorial(n): #рекурсивный процесс
    if n == 1:
        return 1
    else:
        return n * factorial(n)

result = factorial(12)
print(result)
"""

"""def factorial(n): #итеативный процесс
    if n == 0:
        return 1


    def inner(counter, acc):
        if counter == 1:
            return acc
        return inner(counter - 1, acc * counter)

    return inner(n, 1)
result = factorial(25)
print(result)
"""
"""
items = [2, [3, [4, [5, [6]]], [7]]]

def check(num):
    if num % 2 == 0 and num > 4:
        return num
    return 1

def aggregate(items):
    if isinstance(items, int):
        return check(items)
    result = list(map(aggregate, items))
    return sum(result)

print(aggregate(items))
"""

from hexlet import fs

tree = fs.mkdir(
    "/",
    [
        fs.mkdir(
            "etc",
            [
                fs.mkdir("apache"),
                fs.mkdir(
                    "nginx",
                    [
                        fs.mkfile("nginx.conf"),
                    ],
                ),
                fs.mkdir(
                    "consul",
                    [
                        fs.mkfile("config.json"),
                        fs.mkdir("data"),
                    ],
                ),
            ],
        ),
        fs.mkdir("logs"),
        fs.mkfile("hosts"),
    ],
)


def find_empty_dirs(tree):
    name = fs.get_name(tree)
    # Получаем потомков узла (директории)
    children = fs.get_children(tree)
    # Если потомков нет, то возвращаем директорию
    if len(children) == 0:
        return name
    # Фильтруем файлы, они нас не интересуют
    dir_names = filter(fs.is_directory, children)
    # Ищем пустые директории внутри текущей
    empty_dir_names = list(map(find_empty_dirs, dir_names))
    # Далее flatten делает список плоским
    return fs.flatten(empty_dir_names)


print(find_empty_dirs(tree))