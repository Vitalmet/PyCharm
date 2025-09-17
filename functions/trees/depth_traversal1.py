from hexlet import fs


tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkfile('bashrc'),
        fs.mkfile('consul.cfg'),
    ]),
    fs.mkfile('hexletrc'),
    fs.mkdir('bin', [
        fs.mkfile('ls'),
        fs.mkfile('cat'),
    ]),
])


def dfs(node):
    # Распечатываем имя узла
    print(fs.get_name(node))
    # Если это файл, то возвращаем управление
    if fs.is_file(node):
        return

    # Получаем потомков
    children = fs.get_children(node)

    # Применяем функцию dfs ко всем элементам-потомкам
    # Множество рекурсивных вызовов в рамках одного вызова функции
    # называется древовидной рекурсией
    list(map(dfs, children))

print(dfs(tree))
