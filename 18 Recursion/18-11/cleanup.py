# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 11
# ============
# Write a program named litter.py that creates an empty file named trash.txt in
# each subdirectory of a directory tree given the root of the tree as an argument
# (or the current directory as a default). Now write a program named cleanup.py
# that removes all these files.

import os, sys


def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    return sorted(os.listdir(path))


def remove_files(path=None, filename='trash.txt'):
    """ Removes file named trash.txt in each subdirectory of
    a directory tree given the root of the tree as an argument (or the current
    directory as a default)
    """
    if not path:
        path = os.getcwd()

    dirlist = get_dirlist(path)
    full_filename = os.path.join(path, filename)
    os.remove(full_filename)
    print('{} deleted'.format(full_filename))

    for f in dirlist:
        full_name = os.path.join(path, f)
        if os.path.isdir(full_name):
            remove_files(full_name, filename)


def main():
##    if len(sys.argv) > 2:
##        print('Usage: python litter.py [directory]')
##        exit(1)
##
##    if len(sys.argv) == 1:
##        dirname = None
##    else:
##        dirname = sys.argv[1]
##        if not os.path.exists(dirname):
##            print(f"Directory {dirname} doesn't exist")
##            exit(2)

##    remove_files()
    remove_files('d:\Projects\_testdir')


if __name__ == '__main__':
    main()
