import pathlib


# описываем предикат
def is_py_file(path):
    return pathlib.Path(path).is_file() and pathlib.Path(path).suffix.lower() == ".py"


def get_py_file_names(paths):
    # используем генераторное выражение, чтобы не создавать промежуточные списки
    py_files = (path for path in paths if is_py_file(path))

    return [pathlib.Path(path).stem.lower() for path in py_files]


names = get_py_file_names(["solution.py", "solution_test.py", "README.md", ".venv"])
print(names)

names = get_py_file_names(["solution.py", "solution_test.py", "README.md", ".venv"])
print(names)