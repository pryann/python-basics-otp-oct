# use path module to join path parts!!!
from os import getcwd, path

file_path = path.join(getcwd(), "08_file_handling", "text.txt")

with open(file_path, "r") as f:
    print(f.read())
    f.seek(0)
    print(f.readline())
    f.seek(0)
    print(f.readlines())
    f.seek(0)
    for line in f:
        print(line, end="")

file_path = path.join(getcwd(), "08_file_handling", "newfile.txt")
text = "lorem ipsum"
lines = ["new\n", "line"]

with open(file_path, "w", encoding="UTF-8") as f:
    # f.write(text)
    f.writelines(lines)

with open(file_path, "a+", encoding="UTF-8") as f:
    f.write("\nappend content")
