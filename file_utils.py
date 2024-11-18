from os.path import splitext, exists, join
from shutil import move


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        name = make_unique(dest, name)
    move(entry, f"{dest}/{name}")
