from hexlet import fs

tree = fs.mkdir(
    "/",
    [
        fs.mkdir(
            "etc",
            [
                fs.mkfile("bashrc"),
                fs.mkfile("consul.cfg"),
            ],
        ),
        fs.mkfile("hexletrc"),
        fs.mkdir(
            "bin",
            [
                fs.mkfile("ls"),
                fs.mkfile("cat"),
                fs.mkfile("baba"),
            ],
        ),
    ],

)


# В реализации используем рекурсивный процесс,
# чтобы добраться до самого дна дерева
def get_nodes_count(node):
    if fs.is_file(node):
        # Возвращаем 1 для учета текущего файла
        return 1
    # Если узел — директория, получаем его потомков
    children = fs.get_children(node)
    # Самая сложная часть
    # Считаем количество потомков для каждого потомка,
    # вызывая рекурсивно нашу функцию get_nodes_count
    descendant_counts = list(map(get_nodes_count, children))
    # Возвращаем 1 (текущая директория) + общее количество потомков
    return 1 + sum(descendant_counts)

print(get_nodes_count(tree))