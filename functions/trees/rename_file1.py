from hexlet import fs
import copy

# Создаёт файл 'one' с метаданными
file = fs.mkfile("one", {"size": 35})

# Копирует метаданные файла
new_meta = copy.deepcopy(fs.get_meta(file))

# Создаёт новый файл с новым именем и старыми метаданными
new_file = fs.mkfile("new name", new_meta)

# Проверка работы кода
print(fs.get_name(file))  # Ожидается 'one'
print(fs.get_meta(file))  # Ожидается {'size': 35}
print(fs.get_name(new_file))  # Ожидается 'new name'
print(fs.get_meta(new_file))  # Ожидается {'size': 35}