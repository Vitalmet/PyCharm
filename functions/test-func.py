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
"""
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + " " + self.surname

    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(" ")

    @full_name.deleter
    def full_name(self):
        print("Удаляем имя и фамилию.")
        self.name = None
        self.surname = None

tom = Person("Tom", "Smith")
del tom.full_name
print(tom.surname)
"""
"""# ООП очень важный пример!
class Address:
    def __init__(self, street, house, zipcode):
        self.street = street
        self.house = house
        self.zipcode = zipcode

    def __str__(self):
        return f"{self.street}, {self.house}, {self.zipcode}"


class User:
    def __init__(self, address):
        self.street = address["street"]
        self.house = address["house"]
        self.zipcode = address["zipcode"]

    def get_address(self):
        # Поскольку у нас объект-значение,
        # мы можем создавать его столько раз, сколько нам нужно,
        # но при необходимости этот процесс можно оптимизировать
        return Address(self.street, self.house, self.zipcode)


address = {"street": "Красноярская", "house": 17, "zipcode": 565800}
user = User(address)
print(user.get_address())"""

import re
c = re.compile("(?=.*[A-Z])(?=.*\\d+)(?=.*[&*$?=!@#+])(?=.*[a-z]).{8,}")
res = c.match("Padsd45&,l")
if res:
    print(res.group())
