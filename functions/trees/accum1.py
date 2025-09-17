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