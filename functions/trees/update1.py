from hexlet import fs
import copy


tree = fs.mkdir(
    "/",
    [
        fs.mkfile("oNe"),
        fs.mkfile("Two"),
        fs.mkdir("THREE"),
    ],
)


# Приводим к нижнему регистру имена директорий и файлов внутри конкретной директории
def to_lower(node):
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    if fs.is_directory(node):
        return fs.mkdir(name.lower(), fs.get_children(node), new_meta)
    return fs.mkfile(name.lower(), new_meta)


children = fs.get_children(tree)
new_children = list(map(to_lower, children))
# Обязательно копируем метаданные
new_meta = copy.deepcopy(fs.get_meta(tree))
tree2 = fs.mkdir(fs.get_name(tree), new_children, new_meta)
list(map(fs.get_name, fs.get_children(tree2)))
print(list(map(fs.get_name, fs.get_children(tree2))))