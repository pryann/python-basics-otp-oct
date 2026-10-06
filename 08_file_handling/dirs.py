from os import mkdir, rename, chdir, rmdir, listdir, getcwd, path
from shutil import move, copy, rmtree

# create a new folder in project root
# mkdir("new_dir")

# rename("new_dir", "renamed_dir")

# print(getcwd())
# chdir("renamed_dir")
# print(getcwd())

#  delete EMPTY folder
# rmdir("renamed_dir")

# delete folders and subfolders
# rmtree("renamed_dir")

src = path.join(getcwd(), "renamed_dir")
dest = path.join(getcwd(), "08_file_handling", "renamed_dir")
move(src, dest)
# copy()
