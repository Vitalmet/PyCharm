from hexlet import fs

tree = fs.mkdir("/", [fs.mkfile("hexlet.log")], {"hidden": True})
fs.get_name(tree)
# '/'
fs.get_meta(tree).get("hidden")
# True
[file] = fs.get_children(tree)
fs.get_name(file)
# 'hexlet.log'
fs.get_meta(file).get("unknown")
print(fs.get_name(tree))
print(fs.get_meta(tree).get("hidden"))
print([file])
print(fs.get_meta(file).get("unknown"))
