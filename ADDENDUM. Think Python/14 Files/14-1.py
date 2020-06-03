'''
Exercise 14.1. Write a function called sed that takes as arguments a pattern
string, a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files, your
program should catch the exception, print an error message, and exit.
Solution: http://thinkpython2.com/code/sed
py .
'''

def sed(pattern_str, replacement_str, source_file, output_file):
    try:
        fin = open(source_file, 'r')
    except:
        print(f'File {source_file} open error')
        return 1

    try:
        fout = open(output_file, 'w')
    except:
        print(f'File {output_file} open error')
        return 2

    try:
        for line in fin:
            try:
                fout.write(line.replace(pattern_str, replacement_str))
            except:
                print(f'File {output_file} writing error')
                return 3
    except:
        print(f'File {input_file} reading error')
        return 4

    try:
        fin.close()
    except:
        print(f'File {input_file} closing error')
        return 5

    try:
        fout.close()
    except:
        print(f'File {output_file} open error')
        return 6


def main():
    infile = 'input.txt'
    outfile = 'output.txt'
    errnum = sed('mama', 'bambino', infile, outfile)
    if errnum:
        print('Error # {}'.format(errnum))
    else:
        print('No errors')

if __name__ == '__main__':
    main()
