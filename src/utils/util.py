import os

file_path = ''


def remove_file(path=''):
    global file_path
    if path:
        file_path = path
    try:
        os.remove(file_path)
    except FileNotFoundError:
        pass
