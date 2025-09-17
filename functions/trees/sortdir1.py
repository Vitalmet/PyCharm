from hexlet import fs
import copy


tree = fs.mkdir(
    "/",
    [
        fs.mkfile("one"),
        fs.mkfile("two"),
        fs.mkdir("three"),
    ],
)

children = fs.get_children(tree)
new_meta = copy.deepcopy(fs.get_meta(tree))
# Reverse изменяет массив, поэтому клонируем
new_children = children[:]
# Делаем сортировку в обратном порядке, то есть разворачиваем список
new_children.reverse()
tree2 = fs.mkdir(fs.get_name(tree), new_children, new_meta)
list(map(fs.get_name, fs.get_children(tree2)))
print(list(map(fs.get_name, fs.get_children(tree2))))