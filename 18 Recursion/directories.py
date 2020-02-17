# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html


import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    return sorted(os.listdir(path))


def print_files(path, prefix = ''):
    """ Print recursive listing of contents of path """
    if prefix == '':
        print(f'Folder listing for {path}')
        prefix += '| '

    dirlist = get_dirlist(path)
    for filename in dirlist:
        print(prefix + filename)
        dir_full_name = f'{path}\\{filename}'
        if os.path.isdir(dir_full_name):
            print_files(dir_full_name, prefix + '| ')


def main():
    print_files('d:\Projects\_testdir')


if __name__ == '__main__':
    main()