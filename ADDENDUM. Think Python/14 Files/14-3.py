'''
Exercise 14.3. In a large collection of MP3 files, there may be more than one
copy of the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.
1. Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a given
suffix (like .mp3). Hint: os.path provides several useful functions for
manipulating file and path names.
2. To recognize duplicates, you can use md5sum to compute a “checksum” for each
files. If two files have the same checksum, they probably have the same contents.
3. To double-check, you can use the Unix command diff.
Solution: http://thinkpython2.com/code/find_duplicates.py
'''
import os


def find_duplicates(path, filter_func=lambda name: True):
    import os

    #import collections
    # duplicates = collections.defaultdict(lambda :[])
    duplicates = dict()

    def helper(path):
        files_list = os.listdir(path)
        for file in files_list:
            fullname = os.path.join(path, file)
            if os.path.isdir(fullname):
                helper(fullname)
            else:
                if not filter_func(fullname):
                    continue
                cmd_md5sum = f'md5sum {fullname}'
                with os.popen(cmd_md5sum) as fp:
                    md5_hash = fp.read().split()[0]

                if md5_hash in duplicates:
                    cmd_diff = f'diff {fullname} {duplicates[md5_hash][0]}'
                    with os.popen(cmd_diff) as fp:
                        files_difference = fp.read()
                    if files_difference:
                        print('CAUTION! md5 sums of the files {} and {} match ')
                        print('but the files are different') \
                            .format(fullname, duplicates[md5_hash][0])
                    else:
                        duplicates[md5_hash].append(fullname)
                else:
                    duplicates[md5_hash] = [fullname]

    helper(path)
    return dict(duplicates)


def is_textfile(filename):
    return filename.endswith('.txt')


def main():
    path = 'test_dir'
    duplicates = find_duplicates(path, is_textfile)
    print('Groups of matching files:')
    print('--------------------------\n')
    for _, fileslist in duplicates.items():
        print('\n'.join((map(lambda f: os.path.relpath(f, path), fileslist))))
        print()


if __name__ == '__main__':
    main()
