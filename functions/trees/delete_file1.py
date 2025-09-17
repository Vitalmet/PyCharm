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
new_children = list(filter(fs.is_directory, children))
new_meta = copy.deepcopy(fs.get_meta(tree))
fs.mkdir(fs.get_name(tree), new_children, new_meta)
print(fs.mkdir(fs.get_name(tree), new_children, new_meta))