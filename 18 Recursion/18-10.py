# Chapter 18. Recursion
# http://openbookproject.net/thinkcs/python/english3e/recursion.html

# Exercise 10
# ============
# Write a program that walks a directory structure (as in the last section
# of this chapter), but instead of printing filenames, it returns a list of all
# the full paths of files in the directory or the subdirectories. (Don’t include
# directories in this list — just files.) For example, the output list might
# have elements like this:

import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    return sorted(os.listdir(path))


def get_files_list(path):
    """ Returns a list of all the full paths of files in the directory or
    the subdirectories, excluding directories
    """
    fileslist = []
    dirlist = get_dirlist(path)
    for f in dirlist:
        full_name = os.path.join(path, f)
        if os.path.isdir(full_name):
            fileslist.extend(get_files_list(full_name))
        else:
            fileslist.append(full_name)
    return fileslist


def main():
##    print(get_files_list('d:\Projects\_testdir'))
    for f in get_files_list('d:\Projects\_testdir'):
        print(f)


if __name__ == '__main__':
    main()
