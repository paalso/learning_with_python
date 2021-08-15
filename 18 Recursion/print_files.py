import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    return sorted(map(str, os.listdir(path)))


def print_files(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if not prefix:
        print("Folder listing for {}".format(path))
        prefix = "| "
    for f in get_dirlist(path):
        fullname = os.path.join(path, f)
        print("{}{}".format(prefix, f))
        if os.path.isdir(fullname):
            print_files(fullname, "{} | ".format(prefix))


print_files(os.getcwd())
